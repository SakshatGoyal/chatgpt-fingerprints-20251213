#!/usr/bin/env python3
"""\
Extract semantic fingerprints from ChatGPT-exported .md chats.

- Reads N markdown files from an input folder (default: ./output)
- Calls OpenAI Responses API to extract a rich "semantic fingerprint"
- Writes ONE combined markdown file (default: ./fingerprints_50.md)
- Caches results so reruns don't reprocess the same files

Requires:
  pip install openai

Auth:
  export OPENAI_API_KEY="..."
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Iterable, List

from openai import OpenAI  # Official SDK. See OpenAI docs.  # noqa


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

    yaml_out = getattr(resp, "output_text", None)
    if not yaml_out:
        yaml_out = str(resp)

    return yaml_out.strip()


def list_md_files(input_dir: Path, *, largest: bool) -> List[Path]:
    files = [p for p in input_dir.glob("*.md") if p.is_file()]
    if largest:
        # sort by size descending then name for deterministic ordering
        return sorted(files, key=lambda p: (-p.stat().st_size, p.name))
    return sorted(files, key=lambda p: p.name)


def chunked(seq: List[Path], size: int) -> Iterable[List[Path]]:
    """Yield fixed-size batches from seq without materializing the whole structure."""
    for i in range(0, len(seq), size):
        yield seq[i : i + size]


def unique_batch_path(base_dir: Path, batch_index: int) -> Path:
    """Return a non-overwriting path for a batch output file."""
    candidate = base_dir / f"batch_{batch_index:03d}.json"
    if not candidate.exists():
        return candidate

    suffix = 1
    while True:
        candidate = base_dir / f"batch_{batch_index:03d}_{suffix}.json"
        if not candidate.exists():
            return candidate
        suffix += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input_dir", default="output", help="Folder with chat .md files")
    ap.add_argument("--limit", type=int, default=0, help="How many chats to process (0 = all chats)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="OpenAI model name")
    ap.add_argument("--out", default="fingerprints_50.md", help="Combined output markdown file")
    ap.add_argument("--cache", default=".fingerprint_cache.json", help="Cache file path")
    ap.add_argument("--sleep", type=float, default=0.3, help="Seconds to sleep between requests")
    ap.add_argument(
        "--batch-size",
        type=int,
        default=BATCH_SIZE_DEFAULT,
        help="Number of chats per batch output (default: 100)",
    )
    ap.add_argument(
        "--synthesis-dir",
        default="synthesis",
        help="Directory to store per-batch outputs (will be created if missing)",
    )
    ap.add_argument(
        "--largest",
        action="store_true",
        help="Process the largest markdown files first before applying --limit",
    )
    ap.add_argument(
        "--test",
        action="store_true",
        help="Local test mode: writes to fingerprints_test_10.md unless overridden",
    )
    args = ap.parse_args()

    if args.batch_size <= 0:
        print("ERROR: --batch-size must be > 0", file=sys.stderr)
        sys.exit(1)

    if args.test:
        if args.out == "fingerprints_50.md":
            args.out = "fingerprints_test_10.md"

    input_dir = Path(args.input_dir).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve()
    cache_path = Path(args.cache).expanduser().resolve()
    synthesis_dir = Path(args.synthesis_dir).expanduser().resolve()

    if not input_dir.exists():
        print(f"ERROR: input_dir not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    client = OpenAI()

    try:
        synthesis_dir.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        print(f"ERROR: unable to create synthesis directory {synthesis_dir}: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        print(f"ERROR: unable to create output directory {out_path.parent}: {exc}", file=sys.stderr)
        sys.exit(1)

    files = list_md_files(input_dir, largest=args.largest)
    if not files:
        print(f"ERROR: no .md files found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    target_files = files[: args.limit] if args.limit and args.limit > 0 else files

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
    try:
        out_path.write_text(header, encoding="utf-8")
    except Exception as exc:
        print(f"ERROR: unable to write to {out_path}: {exc}", file=sys.stderr)
        sys.exit(1)

    total_files = len(target_files)
    total_batches = (total_files + args.batch_size - 1) // args.batch_size
    global_processed = 0
    global_skipped = 0
    global_errors = 0
    global_index = 0

    print(f"Discovered {total_files} chat files; processing in {total_batches} batch(es) of up to {args.batch_size}.")

    # Process in batches so each chunk can be persisted independently (timeout resilience).
    for batch_index, batch_files in enumerate(chunked(target_files, args.batch_size), start=1):
        start_num = global_index + 1
        end_num = global_index + len(batch_files)
        print(f"[batch {batch_index}/{total_batches}] Processing files {start_num}-{end_num} of {total_files}...")

        batch_results: List[Dict[str, Any]] = []
        batch_processed = 0
        batch_skipped = 0
        batch_errors = 0

        for path in batch_files:
            global_index += 1
            yaml_out = None
            err_msg = None
            status = "unknown"
            content_hash = None

            try:
                md_text = read_text(path)
                content_hash = sha256_text(md_text)
                cache_key = f"{path.name}:{content_hash}"

                if cache_key in cache:
                    batch_skipped += 1
                    global_skipped += 1
                    status = "skipped"
                    yaml_out = cache[cache_key]["yaml"]
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
                err_msg = f"{type(exc).__name__}: {exc}"
                batch_errors += 1
                global_errors += 1
                status = "error"

            block_body = yaml_out if yaml_out else f"ERROR: {err_msg or 'Unknown error'}"
            block = (
                f"## {global_index:03d} — {path.name}\n\n"
                f"```yaml\n{block_body}\n```\n\n"
                f"---\n\n"
            )
            with open(out_path, "a", encoding="utf-8") as f:
                f.write(block)

            print(
                f"[{global_index}/{total_files}] {path.name} "
                f"(status={status}, processed_this_run={global_processed}, skipped_this_run={global_skipped}, errors_this_run={global_errors})"
            )

            batch_results.append(
                {
                    "file": path.name,
                    "hash": content_hash,
                    "status": status,
                    "error": err_msg,
                    "yaml": yaml_out,
                }
            )

        batch_output = {
            "meta": {
                "generated_utc": datetime.now(timezone.utc).isoformat(),
                "input_dir": str(input_dir),
                "model": args.model,
                "batch_size": args.batch_size,
                "cache_path": str(cache_path),
            },
            "batch": {
                "index": batch_index,
                "total_batches": total_batches,
                "start_index": start_num,
                "end_index": end_num,
                "item_count": len(batch_files),
                "total_files": total_files,
            },
            "stats": {
                "processed": batch_processed,
                "skipped_from_cache": batch_skipped,
                "errors": batch_errors,
            },
            "items": batch_results,
        }

        try:
            batch_path = unique_batch_path(synthesis_dir, batch_index)
            batch_path.write_text(json.dumps(batch_output, ensure_ascii=False, indent=2), encoding="utf-8")
            try:
                rel_batch = batch_path.relative_to(Path.cwd())
            except ValueError:
                rel_batch = batch_path
            print(
                f"[batch {batch_index}/{total_batches}] Wrote batch file {rel_batch} "
                f"(processed={batch_processed}, skipped={batch_skipped}, errors={batch_errors})"
            )
        except Exception as exc:
            print(f"[batch {batch_index}/{total_batches}] ERROR writing batch output: {exc}", file=sys.stderr)
            sys.exit(1)

    print("\nDone.")
    print(f"- Combined markdown: {out_path}")
    print(f"- Cache: {cache_path}")
    print(f"- Synthesis batch outputs: {synthesis_dir}")
    print(f"- New extractions this run: {global_processed}")
    print(f"- Skipped from cache this run: {global_skipped}")
    print(f"- Errors this run: {global_errors}")
    print(f"- Total cached entries: {len(cache)}")


if __name__ == "__main__":
    main()
