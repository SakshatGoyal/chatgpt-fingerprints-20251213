#!/usr/bin/env python3
"""
Split ChatGPT export JSON (large, one-line) into per-conversation Markdown files.

What it produces:
output/
  2023-03-22T13-00-00Z__000001__Branch___Krishna_chant_for_meditation.md

Notes:
- Reads `/Users/sakshatgoyal/Downloads/chatGPT export/conversations.json` by default, so `python split_chatgpt_export.py` just works.
- Uses ijson to stream the top-level list, so it doesn't load the entire 300MB file.
- Reconstructs conversation order using the parent->children chain from the mapping root.
- Outputs only user/assistant messages (skips system/tool by default).
"""

import os
import re
import json
import argparse
from datetime import datetime, timezone

try:
    import ijson  # type: ignore[import-not-found]
except ImportError as e:
    raise SystemExit(
        "Missing dependency: ijson.\n"
        "You installed it into a virtual environment (venv), so VS Code and this script must use that same interpreter.\n\n"
        "Fix:\n"
        "1) cd ~/Desktop/chatgpt_export_tools\n"
        "2) source venv/bin/activate\n"
        "3) pip install ijson\n"
        "4) python split_chatgpt_export.py --in \"/Users/sakshatgoyal/Downloads/chatGPT export/conversations.json\" --out output\n\n"
        "VS Code tip: Cmd+Shift+P → 'Python: Select Interpreter' → choose the one ending in chatgpt_export_tools/venv"
    ) from e


def safe_name(name: str, max_len: int = 120) -> str:
    """Make a filesystem-safe name for a file."""
    if not name:
        name = "Untitled"
    name = name.replace(os.sep, "_")
    name = re.sub(r"[^\w\s\-\.\(\)\[\]]+", "_", name, flags=re.UNICODE)
    name = re.sub(r"\s+", " ", name).strip()
    name = name.replace(" ", "_")
    return name[:max_len]


def ts_to_iso(ts):
    """Convert unix seconds to ISO string, if present."""
    if ts is None:
        return None
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat()
    except Exception:
        return None


def earliest_create_time(records: list):
    """Return the earliest numeric timestamp in the conversation records."""
    earliest = None
    for record in records:
        ts = record.get("create_time")
        if ts is None:
            continue
        try:
            value = float(ts)
        except (TypeError, ValueError):
            continue
        if earliest is None or value < earliest:
            earliest = value
    return earliest


def timestamp_label(ts):
    """Build a filename-safe label for a timestamp."""
    if ts is None:
        return None
    try:
        dt = datetime.fromtimestamp(float(ts), tz=timezone.utc)
    except (TypeError, ValueError, OverflowError):
        return None
    # Use dashes for delimiters to keep the name filesystem-safe.
    return dt.strftime("%Y-%m-%dT%H-%M-%SZ")


def extract_text_parts(message_obj):
    """
    message_obj: the inner "message" dict inside mapping[node]["message"]
    returns a single string for the message content.
    """
    if not message_obj:
        return ""

    content = message_obj.get("content") or {}
    parts = content.get("parts")

    # Typical case: {"content_type":"text","parts":["..."]}
    if isinstance(parts, list):
        # join parts with newlines to preserve paragraph-ish breaks
        return "\n".join(str(p) for p in parts if p is not None).strip()

    # Some messages can be other content types; fall back to JSON string
    try:
        return json.dumps(content, ensure_ascii=False)
    except Exception:
        return ""


def find_root_id(mapping: dict):
    """Find the node with parent == None (root)."""
    for node_id, node in mapping.items():
        if node.get("parent") is None:
            return node_id
    return None


def linearize_from_root(mapping: dict):
    """
    Attempt to reconstruct the primary conversation path:
    root -> its first child -> that child's first child -> ...
    This matches how most exports represent a single linear chat.
    """
    root_id = find_root_id(mapping)
    if not root_id:
        return []

    ordered_ids = []
    current_id = root_id

    # Walk down the first-child chain
    visited = set()
    while True:
        if current_id in visited:
            break
        visited.add(current_id)

        node = mapping.get(current_id) or {}
        children = node.get("children") or []
        if not children:
            break

        # ChatGPT exports typically have one main child path
        current_id = children[0]
        ordered_ids.append(current_id)

    return ordered_ids


def collect_messages(mapping: dict, ordered_ids: list, include_roles=None):
    """
    Build a clean list of message records with role + text + timestamps.
    """
    records = []
    include_roles = include_roles or {"user", "assistant"}

    for node_id in ordered_ids:
        node = mapping.get(node_id) or {}
        msg = node.get("message")
        if not msg:
            continue

        author = (msg.get("author") or {}).get("role")
        if author not in include_roles:
            continue

        text = extract_text_parts(msg)
        if not text:
            continue

        rec = {
            "id": msg.get("id") or node_id,
            "role": author,
            "create_time": msg.get("create_time"),
            "create_time_iso": ts_to_iso(msg.get("create_time")),
            "text": text,
        }
        records.append(rec)

    return records


def write_outputs(out_dir: str, index_num: int, title: str, records: list):
    os.makedirs(out_dir, exist_ok=True)
    title_label = title or "Untitled"
    earliest_ts = earliest_create_time(records)
    ts_label = timestamp_label(earliest_ts) or "no-timestamp"
    file_name = f"{ts_label}__{index_num:06d}__{safe_name(title_label)}.md"
    md_path = os.path.join(out_dir, file_name)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {title_label}\n\n")
        for r in records:
            who = "You" if r["role"] == "user" else "ChatGPT"
            when = r["create_time_iso"] or ""
            if when:
                f.write(f"## {who} ({when})\n\n")
            else:
                f.write(f"## {who}\n\n")
            f.write(r["text"].rstrip() + "\n\n")



def main():
    default_input = "/Users/sakshatgoyal/Downloads/chatGPT export/conversations.json"
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--in",
        dest="infile",
        default=default_input,
        help="Path to conversations.json (default: uses the standard export location)",
    )
    ap.add_argument("--out", dest="outdir", default="output", help="Output folder")
    ap.add_argument(
        "--include-system",
        action="store_true",
        help="Include system messages too (default: only user+assistant)",
    )
    args = ap.parse_args()

    include_roles = {"user", "assistant"}
    if args.include_system:
        include_roles.add("system")

    os.makedirs(args.outdir, exist_ok=True)

    # Stream the top-level JSON array: [ {...}, {...}, ... ]
    with open(args.infile, "rb") as f:
        # Each item is one conversation object
        conv_iter = ijson.items(f, "item")

        count = 0
        for conv in conv_iter:
            count += 1
            title = conv.get("title") or "Untitled"
            mapping = conv.get("mapping") or {}

            # Reconstruct the main message chain
            ordered_ids = linearize_from_root(mapping)

            # If that fails (rare), fall back to sorting by create_time
            if not ordered_ids:
                # collect any node that has a message
                node_ids = list(mapping.keys())
                def node_time(nid):
                    node = mapping.get(nid) or {}
                    msg = node.get("message") or {}
                    return msg.get("create_time") or 0
                ordered_ids = sorted(node_ids, key=node_time)

            records = collect_messages(mapping, ordered_ids, include_roles=include_roles)

            # Write even if empty, but you can skip empties if you want
            write_outputs(args.outdir, count, title, records)

            # Tiny progress ping every 25 conversations
            if count % 25 == 0:
                print(f"Processed {count} conversations...")

    print(f"Done. Wrote conversations to: {os.path.abspath(args.outdir)}")


if __name__ == "__main__":
    main()
