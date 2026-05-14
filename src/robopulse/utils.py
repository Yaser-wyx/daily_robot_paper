import builtins
import json
import re
from datetime import datetime

from robopulse.config import CORE_VIP_AUTHORS, EXTENDED_VIP_AUTHORS

def timestamp():
    """Return a local timestamp string for log lines."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print(*args, sep=" ", end="\n", flush=False):
    """Timestamp all stdout lines emitted by this script."""
    message = sep.join(str(arg) for arg in args)
    prefix = f"[{timestamp()}] "

    if end == "":
        builtins.print(f"{prefix}{message}", end="", flush=flush)
        return

    lines = message.splitlines() or [""]
    for index, line in enumerate(lines):
        builtins.print(
            f"{prefix}{line}",
            end="\n",
            flush=flush if index == len(lines) - 1 else False,
        )


def normalize_whitespace(text):
    """Collapse internal whitespace so prompts and markdown stay readable."""
    return re.sub(r"\s+", " ", (text or "")).strip()


def truncate_text(text, limit):
    """Trim long text blocks while preserving sentence flow."""
    compact = normalize_whitespace(text)
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1].rstrip() + "…"


def normalize_paper_id(paper_id):
    """Normalize IDs so selection matching is resilient to version suffixes."""
    normalized = paper_id.strip().replace("arXiv:", "")
    return re.sub(r"v\d+$", "", normalized)


def dedupe_preserve_order(items):
    """Remove duplicate strings while keeping their original order."""
    seen = set()
    ordered = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def get_author_priority_tier(authors_text):
    """Return the highest matched author-priority tier for this author list."""
    authors_lower = authors_text.lower()
    if any(vip.lower() in authors_lower for vip in CORE_VIP_AUTHORS):
        return "core"
    if any(vip.lower() in authors_lower for vip in EXTENDED_VIP_AUTHORS):
        return "extended"
    return None


def paper_has_vip(paper):
    """Return True when a paper belongs to a VIP author list."""
    return get_author_priority_tier(paper.get("authors", "")) is not None


def paper_vip_tier(paper):
    """Return the VIP tier for this paper, if any."""
    return get_author_priority_tier(paper.get("authors", ""))


def paper_priority_label(paper):
    """Return a human-readable label for author priority."""
    tier = paper_vip_tier(paper)
    if tier == "core":
        return "Core VIP"
    if tier == "extended":
        return "Extended VIP"
    return "Standard"


def normalize_known_ids(raw_ids, paper_map):
    """Keep only known arXiv IDs and preserve order."""
    ordered = []
    for raw_id in raw_ids or []:
        normalized = normalize_paper_id(str(raw_id))
        if normalized in paper_map and normalized not in ordered:
            ordered.append(normalized)
    return ordered


def clean_json_string(text):
    """Extract the first JSON object from model output."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text


def extract_codex_output_from_jsonl(stdout_text):
    """Read the final agent message from a Codex `--json` event stream."""
    last_agent_message = ""
    for line in (stdout_text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if event.get("type") != "item.completed":
            continue

        item = event.get("item", {})
        if item.get("type") != "agent_message":
            continue

        text = normalize_whitespace(item.get("text", ""))
        if text:
            last_agent_message = text

    return last_agent_message
