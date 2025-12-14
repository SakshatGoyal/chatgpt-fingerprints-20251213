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
from typing import Dict, Any, List

from openai import OpenAI  # Official SDK. See OpenAI docs.  # noqa


FINGERPRINT_INSTRUCTIONS = """\
You are an expert ethnographic indexer + linguist + project research lead.
You will be given ONE chat transcript in markdown.

Task:
Extract a SEMANTIC FINGERPRINT (not a summary) as YAML.

Rules:
- Read the entire chat carefully.
- Use inductive reasoning to infer latent themes, projects, and workstreams; do not rely on superficial keywords.
- Treat this as ethnographic indexing: capture the situation, goals, constraints, and objects of work as they appear in the transcript.
- Prefer concrete, specific phrasing grounded in evidence from the chat (named tools, projects, deliverables, roles, decision points).
- Do NOT summarize the conversation or restate it chronologically.
- Do NOT add advice or solutions.
- Be specific and qualitative (rich phrases, not one-word labels).
- If something is unknown, say "unknown" (do not invent).
- Output MUST be valid YAML (no code fences).

Output YAML keys (keep these exact keys):
chat_file:
  name:
  first_timestamp_utc:         # infer from the first "## You (ISO)" line if present, else unknown
situational_context:
  triggering_situation:
  user_role:
  stakes:
  temporal_orientation:
intent_and_cognition:
  primary_intent:
  secondary_intents:           # YAML list
  cognitive_mode:              # YAML list
  openness_level:
knowledge_domain:
  primary_domain:
  secondary_domains:           # YAML list
  dominant_concepts:           # YAML list
  organizational_context:
artifacts:
  referenced:                  # YAML list
  produced_or_refined:         # YAML list
  artifact_stage:
  downstream_use:
project_continuity:
  project_affiliation:
  project_phase:
  continuity_strength:
  related_chat_likelihood:
values_and_evaluation:
  prioritized_values:          # YAML list
  rejected_patterns:           # YAML list
  implicit_quality_bar:
latent_indexing:
  primary_themes:              # YAML list (2–6 max)
  secondary_themes:            # YAML list (0–8 max)
  candidate_ia_paths:          # YAML list of folder-like paths (1–5), e.g. "PANW/Account Health/Research"
  confidence_notes:            # 2–5 short bullets; what evidence supports the IA paths; note uncertainty
"""

DEFAULT_MODEL = "gpt-4o-mini"


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


def list_md_files(input_dir: Path) -> List[Path]:
    return sorted([p for p in input_dir.glob("*.md") if p.is_file()])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input_dir", default="output", help="Folder with chat .md files")
    ap.add_argument("--limit", type=int, default=0, help="How many chats to process (0 = all chats)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="OpenAI model name")
    ap.add_argument("--out", default="fingerprints_50.md", help="Combined output markdown file")
    ap.add_argument("--cache", default=".fingerprint_cache.json", help="Cache file path")
    ap.add_argument("--sleep", type=float, default=0.3, help="Seconds to sleep between requests")
    ap.add_argument(
        "--test",
        action="store_true",
        help="Local test mode: process first 10 chats (unless --limit is set) and write to fingerprints_test_10.md",
    )
    args = ap.parse_args()

    if args.test:
        if not args.limit or args.limit == 0:
            args.limit = 10
        if args.out == "fingerprints_50.md":
            args.out = "fingerprints_test_10.md"

    input_dir = Path(args.input_dir).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve()
    cache_path = Path(args.cache).expanduser().resolve()

    if not input_dir.exists():
        print(f"ERROR: input_dir not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    client = OpenAI()

    files = list_md_files(input_dir)
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
        f"- Limit: {'all' if not args.limit or args.limit == 0 else args.limit}\n\n"
        f"---\n\n"
    )
    out_path.write_text(header, encoding="utf-8")

    processed = 0
    skipped = 0

    for idx, path in enumerate(target_files, start=1):
        md_text = read_text(path)
        content_hash = sha256_text(md_text)
        cache_key = f"{path.name}:{content_hash}"

        if cache_key in cache:
            skipped += 1
            yaml_out = cache[cache_key]["yaml"]
        else:
            yaml_out = call_openai_extract_yaml(client, args.model, path.name, md_text)
            cache[cache_key] = {
                "file": path.name,
                "hash": content_hash,
                "yaml": yaml_out,
                "model": args.model,
                "created_utc": datetime.now(timezone.utc).isoformat(),
            }
            save_cache(cache_path, cache)
            processed += 1
            time.sleep(args.sleep)

        block = (
            f"## {idx:03d} — {path.name}\n\n"
            f"```yaml\n{yaml_out}\n```\n\n"
            f"---\n\n"
        )
        with open(out_path, "a", encoding="utf-8") as f:
            f.write(block)

        print(
            f"[{idx}/{len(target_files)}] {path.name}  "
            f"(processed_this_run={processed}, skipped_this_run={skipped}, total_cached={len(cache)})"
        )

    print("\nDone.")
    print(f"- Wrote: {out_path}")
    print(f"- Cache: {cache_path}")
    print(f"- New extractions this run: {processed}")
    print(f"- Skipped from cache this run: {skipped}")
    print(f"- Total cached entries: {len(cache)}")


if __name__ == "__main__":
    main()
