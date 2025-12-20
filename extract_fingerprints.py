#!/usr/bin/env python3
"""\
Extract semantic fingerprints from ChatGPT-exported .md chats.

- Reads markdown files from an input folder (default: ./output)
- Calls OpenAI Responses API to extract a "semantic fingerprint" (YAML)
- Writes ONE combined markdown file (append-only; safe to resume)
- Writes ONE markdown file per batch (synthesis/batch_###.md; append-only; safe to resume)
- Caches results so reruns don't reprocess the same files
- Writes a durable resume pointer committed to the repo (default: synthesis/progress.json)
- (Optional) Commits + pushes checkpoints after each batch and before a soft runtime limit
- (Optional) Self-dispatches a new GitHub Actions run to continue from the checkpoint

Requires:
  pip install openai

Auth:
  export OPENAI_API_KEY="..."
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from openai import OpenAI  # noqa


FINGERPRINT_INSTRUCTIONS = """\
You are an expert ethnographic indexer, information architect, and research librarian for personal knowledge systems.
Your job is to infer the latent structure of ONE ChatGPT transcript and emit a durable SEMANTIC FINGERPRINT for retrieval and IA induction.

You are NOT a summarizer, therapist, coach, or collaborator.
You do not give advice, improvements, or solutions.
You do not mirror tone or style.
You do not invent context that is not evidenced in the transcript.

INPUTS YOU WILL RECEIVE
- chat_file.name (contains timestamp; do NOT infer or output a timestamp)
- one complete chat transcript in markdown

MISSION
Transform the transcript into:
1) a machine-usable semantic fingerprint (YAML, fixed keys)
2) a short end synthesis (a few descriptive sentences) to help a human quickly understand what the chat was, without producing a chronological recap.

HARD RULES
- Read the entire transcript before deciding themes, domains, intents, or project affiliation.
- Prefer latent function over surface keywords (infer what the conversation is DOING).
- Ground claims in evidence from the transcript (tools, artifacts, named entities, deliverables, constraints, explicit decisions).
- If something is unknown or not supported, write "unknown". Do not guess.
- Avoid generic corporate filler (e.g., “critical to organizational performance”) unless the transcript explicitly says so.
- Avoid persona-writing about the user (no invented job titles). Use “unknown” or role as explicitly stated.
- Output MUST be valid YAML only. No code fences. No extra commentary outside the YAML.

CONTROLLED VOCABULARY (use these terms when they fit; otherwise choose precise phrases)
cognitive_mode options (choose 1–4):
- exploratory
- analytical
- evaluative
- synthesis
- planning
- specification
- debugging
- negotiation
- creative_generation
- reflective
- adversarial_testing

project_phase options (choose one):
- ad_hoc
- discovery
- definition
- execution
- iteration
- validation
- handoff
- maintenance
- unknown

PRIMARY PROCEDURE (do this internally; do NOT output these steps)
1) Read the whole transcript end-to-end.
2) Identify the “objects of work” (artifacts, deliverables, decisions, schemas, code, drafts, plans).
3) Infer the user’s primary intent (the job the user hired the model to do).
4) Extract secondary intents only if they are clearly distinct (0–3).
5) Derive latent themes (what keeps recurring or organizing the conversation).
6) Assign domains and concepts (what knowledge areas are operationally used).
7) Determine project affiliation and phase only if evidence supports continuity; else "unknown" or "ad_hoc".
8) Write a short synthesis: 2–5 sentences, descriptive, non-chronological, focused on function + outputs.

OUTPUT FORMAT (YAML ONLY; keys must match exactly)

chat_file:
  name: ""

situational_context:
  triggering_situation: ""          # what caused this chat; concrete phrasing
  temporal_orientation: ""          # e.g., immediate task, retrospective, future-planning, mixed, unknown

intent_and_cognition:
  primary_intent: ""
  secondary_intents: []             # 0–3 items
  cognitive_mode: []                # pick 1–4 from controlled vocabulary
  openness_level: ""                # high/medium/low/unknown; only if evidenced, else unknown

knowledge_domain:
  primary_domain: ""
  secondary_domains: []             # 0–4 items; avoid “NLP/HCI” unless clearly relevant
  dominant_concepts: []             # 5–12 specific concepts, nouns/phrases, not single vague words

artifacts:
  referenced: []                    # concrete items mentioned (docs, tools, files, frameworks, links)
  produced_or_refined: []           # what the chat created/edited/decided
  artifact_stage: ""                # draft/revision/spec/analysis/unknown (choose the best fit)
  downstream_use: ""                # how the artifacts will be used, if stated; else unknown

project_continuity:
  project_affiliation: ""           # project/workstream name if explicit; else unknown/ad_hoc
  project_phase: ""                 # from controlled list or unknown
  continuity_evidence: ""           # 1–2 short phrases citing why you believe it’s part of a project (or unknown)

latent_indexing:
  primary_themes: []                # 2–6 themes; each should be a rich phrase
  secondary_themes: []              # 0–6 themes; optional
  retrieval_tags: []                # 5–15 short tags (lowercase, underscore ok); high-recall indexing

synthesis:
  descriptive_summary: ""           # 2–5 sentences; functional, not chronological; mention outputs & intent

"""

DEFAULT_MODEL = "gpt-4.1"
BATCH_SIZE_DEFAULT = 100
PROGRESS_SCHEMA_VERSION = 1

# Basic secret redaction to avoid pushing secrets into the repo.
# This is conservative on purpose; better to redact than to get blocked by secret-scanning.
_SECRET_PATTERNS: List[Tuple[re.Pattern[str], str]] = [
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "ghp_[REDACTED]"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,}"), "github_pat_[REDACTED]"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "sk-[REDACTED]"),
    (re.compile(r"AIza[0-9A-Za-z\-_]{35}"), "AIza[REDACTED]"),
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def redact_secrets(text: str) -> str:
    for rx, repl in _SECRET_PATTERNS:
        text = rx.sub(repl, text)
    return text


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_first_timestamp_utc(md_text: str) -> str:
    m = re.search(r"^##\s+You\s+\(([^)]+)\)", md_text, flags=re.MULTILINE)
    if not m:
        return "unknown"
    return m.group(1).strip()


def load_cache(cache_path: Path) -> Dict[str, Any]:
    if not cache_path.exists():
        return {}
    try:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_cache(cache_path: Path, cache: Dict[str, Any]) -> None:
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def load_progress(progress_path: Path) -> Dict[str, Any]:
    if not progress_path.exists():
        return {}
    try:
        return json.loads(progress_path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_progress(progress_path: Path, progress: Dict[str, Any]) -> None:
    progress_path.parent.mkdir(parents=True, exist_ok=True)
    progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2), encoding="utf-8")


def call_openai_extract_yaml(client: OpenAI, model: str, chat_filename: str, md_text: str) -> str:
    first_ts = extract_first_timestamp_utc(md_text)

    input_text = (
        f"CHAT FILE NAME: {chat_filename}\n"
        f"CHAT FIRST TIMESTAMP (from transcript if present): {first_ts}\n\n"
        f"CHAT TRANSCRIPT (markdown):\n{md_text}"
    )

    resp = client.responses.create(
        model=model,
        instructions=FINGERPRINT_INSTRUCTIONS,
        input=input_text,
    )

    yaml_out = getattr(resp, "output_text", None) or str(resp)
    return redact_secrets(yaml_out.strip())


def list_md_files(input_dir: Path, *, largest: bool) -> List[Path]:
    files = [p for p in input_dir.glob("*.md") if p.is_file()]
    if largest:
        return sorted(files, key=lambda p: (-p.stat().st_size, p.name))
    return sorted(files, key=lambda p: p.name)


def chunked(seq: List[Path], size: int) -> Iterable[List[Path]]:
    for i in range(0, len(seq), size):
        yield seq[i : i + size]


def batch_md_path(base_dir: Path, batch_index: int) -> Path:
    return base_dir / f"batch_{batch_index:03d}.md"


def _run(cmd: List[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=False, capture_output=True, text=True)


def git_current_branch() -> str:
    r = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return (r.stdout.strip() if r.returncode == 0 else "unknown")


def git_head_sha() -> str:
    r = _run(["git", "rev-parse", "HEAD"])
    return (r.stdout.strip() if r.returncode == 0 else "unknown")


def git_commit_and_push(
    *,
    paths: List[Path],
    message: str,
    remote: str,
    branch: str,
) -> Optional[str]:
    """
    Stages (force-add), commits, and pushes. Returns the pushed commit SHA, or None if nothing changed.
    """
    # Stage files (force so .gitignore cannot defeat durability)
    add_cmd = ["git", "add", "-f"] + [str(p) for p in paths]
    r = _run(add_cmd)
    if r.returncode != 0:
        raise RuntimeError(f"git add failed: {r.stderr.strip() or r.stdout.strip()}")

    # If nothing staged, skip commit/push
    diff = _run(["git", "diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        return None

    c = _run(["git", "commit", "-m", message])
    if c.returncode != 0:
        raise RuntimeError(f"git commit failed: {c.stderr.strip() or c.stdout.strip()}")

    # Push; if rejected, try one rebase then push again.
    p = _run(["git", "push", remote, f"HEAD:{branch}"])
    if p.returncode != 0:
        _run(["git", "fetch", remote, branch])
        rb = _run(["git", "pull", "--rebase", remote, branch])
        if rb.returncode != 0:
            raise RuntimeError(f"git pull --rebase failed: {rb.stderr.strip() or rb.stdout.strip()}")

        p2 = _run(["git", "push", remote, f"HEAD:{branch}"])
        if p2.returncode != 0:
            raise RuntimeError(f"git push failed: {p2.stderr.strip() or p2.stdout.strip()}")

    # Final SHA (important if a rebase occurred)
    return git_head_sha()


def compute_manifest_sha(files: List[Path]) -> str:
    # Include name + size to detect ordering changes for --largest or content churn.
    manifest = "\n".join([f"{p.name}\t{p.stat().st_size}" for p in files])
    return sha256_text(manifest)


def infer_start_index_from_progress(progress: Dict[str, Any], files: List[Path]) -> Tuple[int, str]:
    """
    Returns (start_index, reason).
    """
    total = len(files)
    if not progress:
        return 0, "no_progress_file"

    # Prefer explicit next_file_name if present (robust to minor ordering changes)
    next_name = str(progress.get("next_file_name") or "").strip()
    if next_name:
        for i, p in enumerate(files):
            if p.name == next_name:
                return i, "progress.next_file_name"

    # Fall back to numeric pointer
    try:
        idx = int(progress.get("next_file_index", 0))
    except Exception:
        idx = 0

    if idx < 0:
        idx = 0
    if idx > total:
        idx = total

    return idx, "progress.next_file_index"


def infer_start_index_from_cache(files: List[Path], cache: Dict[str, Any]) -> Tuple[int, str]:
    """
    Heuristic migration path when progress.json doesn't exist yet:
    scan from the beginning until the first file whose (name:hash) is not in cache.
    """
    if not cache:
        return 0, "no_cache"

    for i, p in enumerate(files):
        try:
            md_text = read_text(p)
            cache_key = f"{p.name}:{sha256_text(md_text)}"
        except Exception:
            return 0, "cache_infer_failed_read"
        if cache_key not in cache:
            return i, "cache_prefix_miss"
    return len(files), "cache_all_present"


def dispatch_github_workflow(
    *,
    api_url: str,
    repo: str,
    workflow_file: str,
    ref: str,
    inputs: Dict[str, str],
    token: str,
) -> None:
    """
    Dispatches a workflow via GitHub REST API:
    POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
    workflow_id may be a filename like 'extract_fingerprints.yaml'.
    """
    url = f"{api_url.rstrip('/')}/repos/{repo}/actions/workflows/{workflow_file}/dispatches"
    payload = json.dumps({"ref": ref, "inputs": inputs}).encode("utf-8")
    req = urllib.request.Request(
        url=url,
        data=payload,
        method="POST",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "extract_fingerprints.py",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = getattr(resp, "status", None) or 0
            if status not in (201, 204):
                body = resp.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"workflow dispatch returned HTTP {status}: {body}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else str(e)
        raise RuntimeError(f"workflow dispatch failed: HTTP {e.code}: {body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"workflow dispatch failed: {e}") from e


def ensure_markdown_header(path: Path, header: str) -> None:
    if path.exists() and path.stat().st_size > 0:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input_dir", default="output", help="Folder with chat .md files")
    ap.add_argument("--limit", type=int, default=0, help="How many chats to process (0 = all chats)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="OpenAI model name")
    ap.add_argument("--out", default="fingerprints_50.md", help="Combined output markdown file")
    ap.add_argument("--cache", default=".fingerprint_cache.json", help="Cache file path")
    ap.add_argument("--sleep", type=float, default=0.3, help="Seconds to sleep between requests")
    ap.add_argument("--batch-size", type=int, default=BATCH_SIZE_DEFAULT, help="Chats per batch")
    ap.add_argument("--synthesis-dir", default="synthesis", help="Directory to store per-batch markdown outputs")
    ap.add_argument("--largest", action="store_true", help="Process largest markdown files first")
    ap.add_argument("--commit-each-batch", action="store_true", help="Commit & push outputs after each batch (GitHub Actions)")
    ap.add_argument("--git-remote", default="origin", help="Git remote to push to")
    ap.add_argument("--git-branch", default=os.getenv("GITHUB_REF_NAME", "main"), help="Git branch to push to")

    # Durability / multi-run controls
    ap.add_argument(
        "--progress-file",
        default="",
        help="Resume pointer JSON file (committed). Default: <synthesis-dir>/progress.json",
    )
    ap.add_argument(
        "--max-runtime-minutes",
        type=int,
        default=0,
        help="Soft runtime limit for this run (0 = disabled). When reached, checkpoint + exit.",
    )
    ap.add_argument(
        "--checkpoint-buffer-seconds",
        type=int,
        default=900,
        help="Safety buffer to leave for commit/push/dispatch when using --max-runtime-minutes.",
    )
    ap.add_argument(
        "--max-files-per-run",
        type=int,
        default=0,
        help="Hard cap on files handled per run (0 = disabled). Useful as a deterministic guard.",
    )
    ap.add_argument(
        "--auto-continue",
        action="store_true",
        help="If work remains and running in GitHub Actions, dispatch a fresh run to continue.",
    )
    ap.add_argument(
        "--workflow-file",
        default=os.getenv("GITHUB_WORKFLOW_FILE", "extract_fingerprints.yaml"),
        help="Workflow filename/id used for self-dispatch (GitHub API).",
    )

    args = ap.parse_args()

    if args.batch_size <= 0:
        print("ERROR: --batch-size must be > 0", file=sys.stderr)
        sys.exit(1)

    input_dir = Path(args.input_dir).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve()
    cache_path = Path(args.cache).expanduser().resolve()
    synthesis_dir = Path(args.synthesis_dir).expanduser().resolve()
    progress_path = (
        Path(args.progress_file).expanduser().resolve() if args.progress_file else (synthesis_dir / "progress.json")
    )

    if not input_dir.exists():
        print(f"ERROR: input_dir not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    # Log required diagnostics
    branch = git_current_branch()
    head_sha = git_head_sha()
    print(f"[info] git.branch={branch}")
    print(f"[info] git.head_sha={head_sha}")
    print(f"[info] synthesis.dir={synthesis_dir}")
    print(f"[info] synthesis.dir_abs={str(synthesis_dir)}")
    print(f"[info] progress.file={progress_path}")
    print(f"[info] output.combined={out_path}")
    print(f"[info] cache.file={cache_path}")

    synthesis_dir.mkdir(parents=True, exist_ok=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    client = OpenAI()

    files = list_md_files(input_dir, largest=args.largest)
    if not files:
        print(f"ERROR: no .md files found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    target_files = files[: args.limit] if args.limit and args.limit > 0 else files
    total_files = len(target_files)
    total_batches = (total_files + args.batch_size - 1) // args.batch_size
    manifest_sha = compute_manifest_sha(target_files)

    cache = load_cache(cache_path)

    # Load progress + decide resume point
    progress = load_progress(progress_path)
    resume_index, resume_reason = infer_start_index_from_progress(progress, target_files)

    # If no progress file (or it's empty), try inferring from cache to avoid reprocessing/duplication.
    if not progress:
        resume_index, resume_reason = infer_start_index_from_cache(target_files, cache)

    if resume_index < 0:
        resume_index = 0
    if resume_index > total_files:
        resume_index = total_files

    print(
        f"[info] discovered_files={total_files} batches={total_batches} batch_size={args.batch_size} "
        f"resume_index={resume_index} resume_reason={resume_reason}"
    )

    # Initialize / refresh progress metadata (committed)
    progress.setdefault("schema_version", PROGRESS_SCHEMA_VERSION)
    progress.setdefault("created_utc", utc_now_iso())
    progress["updated_utc"] = utc_now_iso()
    progress["input_dir"] = str(input_dir)
    progress["largest"] = bool(args.largest)
    progress["limit"] = int(args.limit)
    progress["batch_size"] = int(args.batch_size)
    progress["model"] = str(args.model)
    progress["total_files"] = total_files
    progress["total_batches"] = total_batches
    progress["manifest_sha"] = manifest_sha
    progress["git_branch"] = branch
    progress["next_file_index"] = resume_index
    progress["next_file_number"] = resume_index + 1 if resume_index < total_files else total_files + 1
    progress["next_file_name"] = target_files[resume_index].name if resume_index < total_files else ""
    progress["completed"] = bool(resume_index >= total_files)
    # "last_commit_sha" is the last known pushed SHA at the time we wrote this pointer file.
    progress["last_commit_sha"] = head_sha
    progress["github"] = {
        "repository": os.getenv("GITHUB_REPOSITORY", ""),
        "run_id": os.getenv("GITHUB_RUN_ID", ""),
        "run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", ""),
        "workflow": os.getenv("GITHUB_WORKFLOW", ""),
        "actor": os.getenv("GITHUB_ACTOR", ""),
    }
    save_progress(progress_path, progress)

    # Ensure combined header exists (append-only)
    combined_header = (
        "# Semantic Fingerprints\n\n"
        f"- Created (UTC): {utc_now_iso()}\n"
        f"- Input folder: `{input_dir}`\n"
        f"- Model: `{args.model}`\n"
        f"- Limit: {'all' if not args.limit or args.limit == 0 else args.limit}\n"
        f"- Batch size: {args.batch_size}\n"
        f"- Synthesis dir: `{synthesis_dir}`\n\n"
        "---\n\n"
    )
    ensure_markdown_header(out_path, combined_header)

    # Runtime guards
    start_ts = time.time()
    soft_deadline_ts: Optional[float] = None
    if args.max_runtime_minutes and args.max_runtime_minutes > 0:
        soft_deadline_ts = start_ts + (args.max_runtime_minutes * 60) - max(0, args.checkpoint_buffer_seconds)
        print(
            f"[info] soft_deadline_utc={datetime.fromtimestamp(soft_deadline_ts, tz=timezone.utc).isoformat()} "
            f"(max_runtime_minutes={args.max_runtime_minutes}, buffer_seconds={args.checkpoint_buffer_seconds})"
        )

    def should_stop(files_handled_this_run: int) -> Optional[str]:
        if soft_deadline_ts is not None and time.time() > soft_deadline_ts:
            return "time_guard"
        if args.max_files_per_run and args.max_files_per_run > 0 and files_handled_this_run >= args.max_files_per_run:
            return "max_files_per_run"
        return None

    # Track what's been modified since last checkpoint commit
    dirty_paths: List[Path] = []
    dirty_set: set[str] = set()
    updated_batch_files: set[str] = set()

    def mark_dirty(p: Path) -> None:
        sp = str(p)
        if sp not in dirty_set:
            dirty_set.add(sp)
            dirty_paths.append(p)

    def checkpoint(
        reason: str,
        batch_index: Optional[int] = None,
        batch_start_num: Optional[int] = None,
        batch_end_num: Optional[int] = None,
    ) -> Optional[str]:
        """
        Persist a durable checkpoint by committing/pushing the dirty paths.
        Returns pushed SHA if a commit occurred, else None.
        """
        if not args.commit_each_batch:
            return None

        # Update progress checkpoint metadata (and save) before committing.
        progress["updated_utc"] = utc_now_iso()
        progress["last_checkpoint"] = {
            "reason": reason,
            "timestamp_utc": progress["updated_utc"],
            "batch_index": batch_index,
            "batch_range": [batch_start_num, batch_end_num] if batch_start_num and batch_end_num else None,
            "next_file_index": int(progress.get("next_file_index", 0)),
            "next_file_name": str(progress.get("next_file_name", "")),
        }
        progress["last_commit_sha"] = git_head_sha()
        save_progress(progress_path, progress)
        mark_dirty(progress_path)

        if not dirty_paths:
            print(f"[checkpoint:{reason}] nothing to commit (dirty_paths empty)")
            return None

        # Logging required by prompt
        batch_files_sorted = sorted([p for p in updated_batch_files])
        print(f"[checkpoint:{reason}] branch={git_current_branch()}")
        print(f"[checkpoint:{reason}] synthesis_dir_abs={synthesis_dir}")
        print(f"[checkpoint:{reason}] newly_written_batch_files={batch_files_sorted}")

        if reason == "end_of_batch" and batch_index is not None and batch_start_num is not None and batch_end_num is not None:
            msg = f"fingerprints: batch {batch_index:03d} ({batch_start_num}-{batch_end_num} of {total_files})"
        elif reason == "completed":
            msg = f"fingerprints: completed ({total_files} files)"
        else:
            next_n = int(progress.get("next_file_index", 0)) + 1
            msg = f"fingerprints: checkpoint ({reason}) next={next_n}/{total_files}"

        pushed_sha = git_commit_and_push(paths=dirty_paths, message=msg, remote=args.git_remote, branch=args.git_branch)
        if pushed_sha:
            print(f"[checkpoint:{reason}] committed=yes pushed_sha={pushed_sha} remote={args.git_remote} branch={args.git_branch}")
        else:
            print(f"[checkpoint:{reason}] committed=no (no staged changes)")

        # Reset dirty tracking after a successful commit attempt (commit or no-op).
        dirty_paths.clear()
        dirty_set.clear()
        updated_batch_files.clear()

        return pushed_sha

    # Main processing loop (resumable)
    processed_this_run = 0
    skipped_this_run = 0
    errors_this_run = 0
    handled_this_run = 0

    stop_reason: Optional[str] = None

    for i in range(resume_index, total_files):
        stop_reason = should_stop(handled_this_run)
        if stop_reason:
            print(f"[info] stopping_before_file_index={i} reason={stop_reason}")
            break

        path = target_files[i]
        file_num = i + 1  # 1-based across entire corpus
        batch_index = (i // args.batch_size) + 1
        batch_start_num = (batch_index - 1) * args.batch_size + 1
        batch_end_num = min(batch_index * args.batch_size, total_files)

        bpath = batch_md_path(synthesis_dir, batch_index)
        batch_header = (
            f"# Batch {batch_index:03d} Semantic Fingerprints\n\n"
            f"- Created (UTC): {utc_now_iso()}\n"
            f"- Model: `{args.model}`\n"
            f"- Files: {batch_start_num}-{batch_end_num} of {total_files}\n"
            f"- Batch size: {args.batch_size}\n\n"
            "---\n\n"
        )
        ensure_markdown_header(bpath, batch_header)

        yaml_out: Optional[str] = None
        err_msg: Optional[str] = None
        status = "unknown"

        try:
            md_text = read_text(path)
            content_hash = sha256_text(md_text)
            cache_key = f"{path.name}:{content_hash}"

            if cache_key in cache:
                status = "skipped"
                yaml_out = cache[cache_key]["yaml"]
                skipped_this_run += 1
            else:
                status = "processed"
                yaml_out = call_openai_extract_yaml(client, args.model, path.name, md_text)
                cache[cache_key] = {
                    "file": path.name,
                    "hash": content_hash,
                    "yaml": yaml_out,
                    "model": args.model,
                    "created_utc": utc_now_iso(),
                }
                save_cache(cache_path, cache)
                mark_dirty(cache_path)
                processed_this_run += 1
                time.sleep(args.sleep)
        except Exception as exc:
            status = "error"
            err_msg = f"{type(exc).__name__}: {exc}"
            errors_this_run += 1

            # Cache the error so retries don't burn API calls by default.
            try:
                md_text = md_text if "md_text" in locals() else read_text(path)
                content_hash = sha256_text(md_text)
                cache_key = f"{path.name}:{content_hash}"
                cache[cache_key] = {
                    "file": path.name,
                    "hash": content_hash,
                    "yaml": redact_secrets(f"ERROR: {err_msg}"),
                    "model": args.model,
                    "created_utc": utc_now_iso(),
                    "status": "error",
                }
                save_cache(cache_path, cache)
                mark_dirty(cache_path)
            except Exception:
                pass

        block_body = yaml_out if yaml_out else redact_secrets(f"ERROR: {err_msg or 'Unknown error'}")
        block = (
            f"## {file_num:03d} — {path.name}\n\n"
            f"```yaml\n{block_body}\n```\n\n"
            f"---\n\n"
        )

        with open(out_path, "a", encoding="utf-8") as f:
            f.write(block)
        with open(bpath, "a", encoding="utf-8") as f:
            f.write(block)

        mark_dirty(out_path)
        mark_dirty(bpath)
        updated_batch_files.add(str(bpath))

        # Update progress pointer after *successfully writing outputs*
        next_index = i + 1
        progress["updated_utc"] = utc_now_iso()
        progress["next_file_index"] = next_index
        progress["next_file_number"] = next_index + 1 if next_index < total_files else total_files + 1
        progress["next_file_name"] = target_files[next_index].name if next_index < total_files else ""
        progress["completed"] = bool(next_index >= total_files)
        progress["last_commit_sha"] = git_head_sha()
        save_progress(progress_path, progress)
        mark_dirty(progress_path)

        handled_this_run += 1

        print(
            f"[{file_num}/{total_files}] {path.name} "
            f"(status={status}, processed_this_run={processed_this_run}, skipped_this_run={skipped_this_run}, errors_this_run={errors_this_run})"
        )

        # Batch boundary checkpoint (but do NOT stop here; keep running)
        at_batch_end = (file_num % args.batch_size == 0) or (file_num == total_files)
        if args.commit_each_batch and at_batch_end:
            checkpoint("end_of_batch", batch_index=batch_index, batch_start_num=batch_start_num, batch_end_num=batch_end_num)

    # If we exited early due to guard, checkpoint mid-batch and self-dispatch
    if stop_reason and int(progress.get("next_file_index", 0)) < total_files:
        checkpoint(stop_reason)

        if args.auto_continue and os.getenv("GITHUB_ACTIONS", "").lower() == "true":
            token = os.getenv("GITHUB_TOKEN", "")
            repo = os.getenv("GITHUB_REPOSITORY", "")
            api_url = os.getenv("GITHUB_API_URL", "https://api.github.com")

            if not token or not repo:
                print(
                    "[error] auto-continue requested but missing GITHUB_TOKEN or GITHUB_REPOSITORY in env.",
                    file=sys.stderr,
                )
                sys.exit(2)

            print(
                f"[continue] dispatching workflow_file={args.workflow_file} ref={args.git_branch} "
                f"inputs={{model:{args.model}, batch_size:{args.batch_size}, output_branch:{args.git_branch}, "
                f"max_runtime_minutes:{args.max_runtime_minutes}, checkpoint_buffer_seconds:{args.checkpoint_buffer_seconds}, "
                f"max_files_per_run:{args.max_files_per_run}}}"
            )
            dispatch_github_workflow(
                api_url=api_url,
                repo=repo,
                workflow_file=args.workflow_file,
                ref=args.git_branch,
                inputs={
                    "model": str(args.model),
                    "batch_size": str(args.batch_size),
                    "output_branch": str(args.git_branch),
                    "max_runtime_minutes": str(args.max_runtime_minutes),
                    "checkpoint_buffer_seconds": str(args.checkpoint_buffer_seconds),
                    "max_files_per_run": str(args.max_files_per_run),
                },
                token=token,
            )
            print("[continue] dispatched successfully; exiting this run after checkpoint.")
        else:
            print("[continue] auto-continue disabled or not running in GitHub Actions; exiting after checkpoint.")

    # Completion finalization
    if int(progress.get("next_file_index", 0)) >= total_files:
        progress["completed"] = True
        progress["completed_utc"] = utc_now_iso()
        progress["updated_utc"] = utc_now_iso()
        progress["last_commit_sha"] = git_head_sha()
        save_progress(progress_path, progress)
        mark_dirty(progress_path)
        checkpoint("completed")

    print("\nDone.")
    print(f"- Combined markdown: {out_path}")
    print(f"- Progress pointer: {progress_path}")
    print(f"- Cache: {cache_path}")
    print(f"- Batch markdown outputs: {synthesis_dir}")
    print(f"- New extractions this run: {processed_this_run}")
    print(f"- Skipped from cache this run: {skipped_this_run}")
    print(f"- Errors this run: {errors_this_run}")
    print(f"- Total cached entries: {len(cache)}")


if __name__ == "__main__":
    main()
