#!/usr/bin/env python3
"""
Clean ChatGPT-exported markdown threads IN-PLACE by removing non-conversational metadata
(JSON/dict blobs like user_profile, asset pointers, tool-call junk), while keeping
the actual conversation text.

Defaults:
- Input folder: <script_dir>/output
- Writes changes back to the same files (in-place)
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path


# Speaker headings (used only to remove empty ones)
SPEAKER_HEADING_RE = re.compile(r"^##\s+(You|ChatGPT|System)\b.*$")

# Chat export filenames often start with an ISO-ish timestamp
CHAT_FILENAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T")

# Detect content_type in JSON or python-dict style
CONTENT_TYPE_RE = re.compile(r"""['"]content_type['"]\s*:\s*['"]([^'"]+)['"]""")

# Extract 'text': "..." field from JSON/dict blocks
TEXT_FIELD_RE = re.compile(
    r"""['"]text['"]\s*:\s*(?P<q>["'])(?P<val>(?:\\.|(?!\1).)*)\1""",
    re.S,
)

# Wrappers like <<AudioTranscription: ...>> / <<AudioDisplayed>>
AUDIO_WRAPPER_RE = re.compile(r"<<AudioTranscription:\s*(.*?)>>", re.S)
DISPLAY_WRAPPER_RE = re.compile(r"<<(?:AudioDisplayed|ImageDisplayed|VideoDisplayed)[^>]*>>")

# Tool/citation markers seen in exports (private-use characters + "cite" blocks)
TOOL_MARKER_WITH_PUA_RE = re.compile(r"")
TOOL_MARKER_DEGRADED_RE = re.compile(r"\bcite(?:\s*turn\d+\w+\d+)+\b", re.I)


def strip_private_use_chars(s: str) -> str:
    """
    Remove private-use glyphs and zero-width junk.
    (Keeps normal unicode like emoji; only strips 'Co' category characters.)
    """
    s = s.replace("\ufeff", "").replace("\u200b", "")
    return "".join(ch for ch in s if unicodedata.category(ch) != "Co")


def metadata_block_starts_here(lines: list[str], i: int, in_code_block: bool) -> bool:
    """
    Decide if lines[i] begins a metadata blob (JSON/dict) that should be removed/converted.
    Only runs outside code blocks.
    """
    if in_code_block:
        return False

    first = lines[i].lstrip()
    if not (first.startswith("{") or first.startswith("[")):
        return False

    lookahead = "\n".join(lines[i : min(i + 8, len(lines))])
    keywords = [
        "content_type",
        "asset_pointer",
        "expiry_datetime",
        "user_profile",
        "user_instructions",
        "user_editable_context",
        "real_time_user_audio_video_asset_pointer",
        "audio_asset_pointer",
        "decoding_id",
        "frames_asset_pointers",
        "sediment://",
    ]
    return any(k in lookahead for k in keywords)


def collect_balanced_block(lines: list[str], start: int) -> tuple[str, int]:
    """
    Collect a {...} or [...] block from lines[start], using naive brace/bracket balancing.
    Returns: (block_text, next_index_after_block)
    """
    block: list[str] = []
    brace = 0
    bracket = 0
    i = start
    started = False

    while i < len(lines):
        line = lines[i]
        block.append(line)

        if any(c in line for c in "{}[]"):
            brace += line.count("{") - line.count("}")
            bracket += line.count("[") - line.count("]")
            started = True

        i += 1

        # Stop once we've closed what we opened
        if started and brace <= 0 and bracket <= 0:
            break

    return "\n".join(block), i


def extract_text_from_blob(blob: str) -> str | None:
    """
    From a metadata blob, keep only conversational text when appropriate.

    Keeps:
      - content_type == "audio_transcription"  -> keep blob["text"]
      - content_type == "text"                 -> keep blob["text"] (if present)

    Drops everything else:
      - user_editable_context, code, pointers, etc.
    """
    m_ct = CONTENT_TYPE_RE.search(blob)
    if not m_ct:
        return None

    ct = (m_ct.group(1) or "").strip()

    if ct in {"audio_transcription", "text"}:
        m_text = TEXT_FIELD_RE.search(blob)
        if not m_text:
            return None
        raw = m_text.group("val")
        try:
            decoded = bytes(raw, "utf-8").decode("unicode_escape")
        except Exception:
            decoded = raw
        decoded = strip_private_use_chars(decoded).strip()
        return decoded if decoded else None

    return None


def clean_markdown(raw_text: str, strip_citations: bool = True) -> str:
    lines = raw_text.splitlines()
    out: list[str] = []

    in_code = False
    fence = None  # "```" or "~~~"

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        # --- Preserve real markdown code fences exactly ---
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_code:
                in_code = True
                fence = marker
            else:
                if fence == marker:
                    in_code = False
                    fence = None
            out.append(line.rstrip())
            i += 1
            continue

        # Inside code blocks: do NOT strip anything
        if in_code:
            out.append(line.rstrip())
            i += 1
            continue

        # --- Outside code blocks: clean ---
        line = AUDIO_WRAPPER_RE.sub(lambda m: m.group(1), line)
        line = DISPLAY_WRAPPER_RE.sub("", line)

        if strip_citations:
            line = TOOL_MARKER_WITH_PUA_RE.sub("", line)

        line = strip_private_use_chars(line)

        if strip_citations:
            line = TOOL_MARKER_DEGRADED_RE.sub("", line)

        # Drop obvious pointer lines
        if "sediment://" in line:
            i += 1
            continue

        # Drop/convert metadata blobs (keep only spoken text)
        if metadata_block_starts_here(lines, i, in_code_block=False):
            blob, next_i = collect_balanced_block(lines, i)
            blob = strip_private_use_chars(blob)

            kept = extract_text_from_blob(blob)
            if kept:
                out.append(kept)

            i = next_i
            continue

        out.append(line.rstrip())
        i += 1

    # Collapse huge blank runs (keep max 2 in a row)
    compact: list[str] = []
    blank_run = 0
    for ln in out:
        if ln.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                compact.append("")
        else:
            blank_run = 0
            compact.append(ln)

    # Remove empty speaker blocks like "## You" followed by nothing
    final: list[str] = []
    idx = 0
    while idx < len(compact):
        ln = compact[idx]
        if SPEAKER_HEADING_RE.match(ln.strip()):
            j = idx + 1
            has_content = False
            while j < len(compact) and not SPEAKER_HEADING_RE.match(compact[j].strip()):
                if compact[j].strip():
                    has_content = True
                    break
                j += 1
            if has_content:
                final.append(ln)
            idx += 1
            continue

        final.append(ln)
        idx += 1

    # Trim leading/trailing blanks and ensure newline at EOF
    while final and final[0].strip() == "":
        final.pop(0)
    while final and final[-1].strip() == "":
        final.pop()

    return "\n".join(final) + "\n"


def iter_md_files(input_dir: Path, all_md: bool) -> list[Path]:
    files: list[Path] = []
    for p in input_dir.rglob("*.md"):
        if not p.is_file():
            continue

        parts = set(p.parts)
        if ".git" in parts or "node_modules" in parts:
            continue

        if not all_md and not CHAT_FILENAME_RE.match(p.name):
            continue

        files.append(p)

    files.sort()
    return files


def main(argv: list[str]) -> int:
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description="Clean ChatGPT-exported .md threads in-place (remove non-conversational clutter, keep spoken text)."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=(script_dir / "output"),
        help="Folder containing chat .md files (default: <repo>/output).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Process only the first N files (0 = all).",
    )
    parser.add_argument(
        "--all-md",
        action="store_true",
        help="Process ALL .md files in the input folder (default: only timestamp-named chat files).",
    )
    parser.add_argument(
        "--keep-citations",
        action="store_true",
        help="Keep ChatGPT citation/tool markers (default: remove).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change, but do not write files.",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create a .bak backup next to each file before modifying (default: off).",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print each file as it’s processed.",
    )

    args = parser.parse_args(argv)

    input_dir = args.input.expanduser().resolve()
    if not input_dir.exists() or not input_dir.is_dir():
        print(f"ERROR: Input folder does not exist: {input_dir}", file=sys.stderr)
        return 2

    files = iter_md_files(input_dir, all_md=args.all_md)
    if args.limit and args.limit > 0:
        files = files[: args.limit]

    if not files:
        print("No matching .md files found.")
        print(f"Checked folder: {input_dir}")
        print("Tip: try adding --all-md")
        return 0

    changed = 0
    processed = 0

    for src in files:
        try:
            raw = src.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raw = src.read_text(encoding="utf-8", errors="replace")

        cleaned = clean_markdown(raw, strip_citations=not args.keep_citations)

        processed += 1
        if cleaned != raw:
            changed += 1

            if args.verbose:
                print(f"✎ {src.relative_to(input_dir)}")

            if not args.dry_run:
                if args.backup:
                    bak = src.with_suffix(src.suffix + ".bak")
                    if not bak.exists():
                        bak.write_text(raw, encoding="utf-8")
                src.write_text(cleaned, encoding="utf-8")
        else:
            if args.verbose:
                print(f"✓ {src.relative_to(input_dir)} (no change)")

    print(f"\nDone. Processed {processed} file(s). Changed {changed} file(s).")
    print(f"Folder: {input_dir}")
    if args.dry_run:
        print("Dry run only (no files were modified).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
