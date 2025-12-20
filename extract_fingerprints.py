#!/usr/bin/env python3
"""\
Extract semantic fingerprints from ChatGPT-exported .md chats.

- Reads markdown files from an input folder (default: ./output)
- Calls OpenAI Responses API to extract a "semantic fingerprint" (YAML)
- Writes ONE combined markdown file
- Writes ONE markdown file per batch (synthesis/batch_###.md)
- Caches results so reruns don't reprocess the same files
- (Optional) Commits + pushes outputs after each batch (for GitHub Actions durability)

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
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Iterable, List, Optional

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
- Avoid generic corporate filler unless the transcript explicitly says so.
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

OUTPUT FORMAT (YAML ONLY; keys must match exactly)

chat_file:
  name: ""

situational_context:
  triggering_situation: ""
  temporal_orientation: ""

intent_and_cognition:
  primary_intent: ""
  secondary_intents: []
  cognitive_mode: []
  openness_level: ""

knowledge_domain:
  primary_domain: ""
  secondary_domains: []
  dominant_concepts: []

artifacts:
  referenced: []
  produced_or_refined: []
  artifact_stage: ""
  downstream_use: ""

project_continuity:
  project_affiliation: ""
  project_phase: ""
  continuity_evidence: ""

latent_indexing:
  primary_themes: []
  secondary_themes: []
  retrieval_tags: []

synthesis:
  descriptive_summary: ""
"""

DEFAULT_MODEL = "gpt-4.1"
BATCH_SIZE_DEFAULT = 100

# Basic secret redaction to avoid pushing secrets into the repo.
# This is conservative on purpose; better to redact than to get blocked by secret-scanning.
_SECRET_PATTERNS: List[tuple[re.Pattern[str], str]] = [
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "ghp_[REDACTED]"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,}"), "github_pat_[REDACTED]"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "sk-[REDACTED]"),
    (re.compile(r"AIza[0-9A-Za-z\-_]{35}"), "AIza[REDACTED]"),
]


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


def git_commit_and_push(
    *,
    paths: List[Path],
    message: str,
    remote: str,
    branch: str,
) -> None:
    # Stage files
    add_cmd = ["git", "add"] + [str(p) for p in paths]
    r = _run(add_cmd)
    if r.returncode != 0:
        raise RuntimeError(f"git add failed: {r.stderr.strip() or r.stdout.strip()}")

    # If nothing staged, skip commit/push
    diff = _run(["git", "diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        return

    c = _run(["git", "commit", "-m", message])
    if c.returncode != 0:
        raise RuntimeError(f"git commit failed: {c.stderr.strip() or c.stdout.strip()}")

    # Push; if rejected, try one rebase then push again.
    p = _run(["git", "push", remote, f"HEAD:{branch}"])
    if p.returncode == 0:
        return

    # Retry once with rebase
    _run(["git", "fetch", remote, branch])
    rb = _run(["git", "pull", "--rebase", remote, branch])
    if rb.returncode != 0:
        raise RuntimeError(f"git pull --rebase failed: {rb.stderr.strip() or rb.stdout.strip()}")

    p2 = _run(["git", "push", remote, f"HEAD:{branch}"])
    if p2.returncode != 0:
        raise RuntimeError(f"git push failed: {p2.stderr.strip() or p2.stdout.strip()}")


def main():
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

    args = ap.parse_args()

    if args.batch_size <= 0:
        print("ERROR: --batch-size must be > 0", file=sys.stderr)
        sys.exit(1)

    input_dir = Path(args.input_dir).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve()
    cache_path = Path(args.cache).expanduser().resolve()
    synthesis_dir = Path(args.synthesis_dir).expanduser().resolve()

    if not input_dir.exists():
        print(f"ERROR: input_dir not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    client = OpenAI()

    synthesis_dir.mkdir(parents=True, exist_ok=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    files = list_md_files(input_dir, largest=args.largest)
    if not files:
        print(f"ERROR: no .md files found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    target_files = files[: args.limit] if args.limit and args.limit > 0 else files
    total_files = len(target_files)
    total_batches = (total_files + args.batch_size - 1) // args.batch_size

    cache = load_cache(cache_path)

    header = (
        f"# Semantic Fingerprints\n\n"
        f"- Generated: {datetime.now(timezone.utc).isoformat()}\n"
        f"- Input folder: `{input_dir}`\n"
        f"- Model: `{args.model}`\n"
        f"- Limit: {'all' if not args.limit or args.limit == 0 else args.limit}\n"
        f"- Batch size: {args.batch_size}\n"
        f"- Synthesis dir: `{synthesis_dir}`\n\n"
        f"---\n\n"
    )
    out_path.write_text(header, encoding="utf-8")

    print(f"Discovered {total_files} chat files; processing in {total_batches} batch(es) of up to {args.batch_size}.")

    global_processed = 0
    global_skipped = 0
    global_errors = 0
    global_index = 0

    for batch_index, batch_files in enumerate(chunked(target_files, args.batch_size), start=1):
        start_num = global_index + 1
        end_num = global_index + len(batch_files)

        bpath = batch_md_path(synthesis_dir, batch_index)
        batch_header = (
            f"# Batch {batch_index:03d} Semantic Fingerprints\n\n"
            f"- Generated: {datetime.now(timezone.utc).isoformat()}\n"
            f"- Model: `{args.model}`\n"
            f"- Files: {start_num}-{end_num} of {total_files}\n"
            f"- Batch size: {args.batch_size}\n\n"
            f"---\n\n"
        )
        bpath.write_text(batch_header, encoding="utf-8")

        print(f"[batch {batch_index}/{total_batches}] Processing files {start_num}-{end_num} of {total_files}...")

        batch_processed = 0
        batch_skipped = 0
        batch_errors = 0

        for path in batch_files:
            global_index += 1
            yaml_out: Optional[str] = None
            err_msg: Optional[str] = None
            status = "unknown"
            content_hash: Optional[str] = None

            try:
                md_text = read_text(path)
                content_hash = sha256_text(md_text)
                cache_key = f"{path.name}:{content_hash}"

                if cache_key in cache:
                    status = "skipped"
                    yaml_out = cache[cache_key]["yaml"]
                    batch_skipped += 1
                    global_skipped += 1
                else:
                    status = "processed"
                    yaml_out = call_openai_extract_yaml(client, args.model, path.name, md_text)
                    cache[cache_key] = {
                        "file": path.name,
                        "hash": content_hash,
                        "yaml": yaml_out,
                        "model": args.model,
                        "created_utc": datetime.now(timezone.utc).isoformat(),
                    }
                    save_cache(cache_path, cache)
                    batch_processed += 1
                    global_processed += 1
                    time.sleep(args.sleep)
            except Exception as exc:
                status = "error"
                err_msg = f"{type(exc).__name__}: {exc}"
                batch_errors += 1
                global_errors += 1

            block_body = yaml_out if yaml_out else redact_secrets(f"ERROR: {err_msg or 'Unknown error'}")
            block = (
                f"## {global_index:03d} — {path.name}\n\n"
                f"```yaml\n{block_body}\n```\n\n"
                f"---\n\n"
            )

            with open(out_path, "a", encoding="utf-8") as f:
                f.write(block)
            with open(bpath, "a", encoding="utf-8") as f:
                f.write(block)

            print(
                f"[{global_index}/{total_files}] {path.name} "
                f"(status={status}, processed_this_run={global_processed}, skipped_this_run={global_skipped}, errors_this_run={global_errors})"
            )

        print(
            f"[batch {batch_index}/{total_batches}] Wrote batch markdown {bpath} "
            f"(processed={batch_processed}, skipped={batch_skipped}, errors={batch_errors})"
        )

        if args.commit_each_batch:
            try:
                git_commit_and_push(
                    paths=[bpath, out_path, cache_path],
                    message=f"fingerprints: batch {batch_index:03d} ({start_num}-{end_num} of {total_files})",
                    remote=args.git_remote,
                    branch=args.git_branch,
                )
                print(f"[batch {batch_index}/{total_batches}] Committed & pushed to {args.git_remote}/{args.git_branch}")
            except Exception as exc:
                # Fail loudly: you asked for “never again”. If push fails, stop so you know immediately.
                print(f"[batch {batch_index}/{total_batches}] ERROR: failed to commit/push batch outputs: {exc}", file=sys.stderr)
                sys.exit(2)

    print("\nDone.")
    print(f"- Combined markdown: {out_path}")
    print(f"- Cache: {cache_path}")
    print(f"- Batch markdown outputs: {synthesis_dir}")
    print(f"- New extractions this run: {global_processed}")
    print(f"- Skipped from cache this run: {global_skipped}")
    print(f"- Errors this run: {global_errors}")
    print(f"- Total cached entries: {len(cache)}")


if __name__ == "__main__":
    main()
