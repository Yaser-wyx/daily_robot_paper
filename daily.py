import builtins
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# ================= Configuration =================

ARXIV_URL = "https://arxiv.org/list/cs.RO/new"
ARXIV_ABS_URL = "https://arxiv.org/abs/{paper_id}"
ARXIV_HTML_URL = "https://arxiv.org/html/{paper_id}"
ARXIV_PDF_URL = "https://arxiv.org/pdf/{paper_id}"
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}
CODEX_MODEL = os.environ.get("CODEX_MODEL", "").strip()
CHATGPT_WEB_URL = os.environ.get("CHATGPT_WEB_URL", "https://chatgpt.com/").strip()
INTERESTS = (
    "VLA (Vision-Language-Action), Sim2Real, Reinforcement Learning + Vision-Language-Action, "
    "World Model, World Action Model"
)
# Biased toward robot learning / manipulation / VLA / world-model authors who are
# active in embodied AI and likely to appear on cs.RO papers relevant to this brief.
CORE_VIP_AUTHORS = [
    "Sergey Levine",
    "Chelsea Finn",
    "Pieter Abbeel",
    "Dorsa Sadigh",
    "Shuran Song",
    "Yuke Zhu",
    "Jeannette Bohg",
    "Xiaolong Wang",
    "Huazhe Xu",
    "Hao Su",
    "Cewu Lu",
    "Jiangmiao Pang",
    "He Wang",
    "Donglin Wang",
    "Yue Wang",
]
EXTENDED_VIP_AUTHORS = [
    "Fei Xia",
    "Ted Xiao",
    "Karol Hausman",
    "Pierre Sermanet",
    "Dieter Fox",
    "Lerrel Pinto",
    "Pulkit Agrawal",
    "Deepak Pathak",
    "Abhinav Gupta",
    "Danfei Xu",
    "Jiajun Wu",
    "Siddharth Karamcheti",
    "Dhruv Shah",
    "Mohit Shridhar",
    "Daniela Rus",
    "Russ Tedrake",
]
VIP_AUTHORS = list(dict.fromkeys(CORE_VIP_AUTHORS + EXTENDED_VIP_AUTHORS))
OUTPUT_DIR = "./reports"
CODEX_BIN = None
ARXIV_NOT_UPDATED_EXIT_CODE = 75
GENERAL_FAILURE_EXIT_CODE = 1
SHORTLIST_TARGET = 10
SELECTED_TARGET = 6
SHORTLIST_CONTEXT_LIMIT = 4600
WATCHLIST_PREFIX = "W"
SCREENING_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "opening_summary": {"type": "string"},
        "shortlist_ids": {"type": "array", "items": {"type": "string"}},
        "selected_ids": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["title", "opening_summary", "shortlist_ids", "selected_ids"],
    "additionalProperties": False,
}
SELECTED_PAPER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "one_liner": {"type": "string"},
        "what_it_does": {"type": "string"},
        "method_and_evidence": {"type": "string"},
        "body_core_points": {"type": "array", "items": {"type": "string"}},
        "why_it_matters": {"type": "array", "items": {"type": "string"}},
        "risks": {"type": "array", "items": {"type": "string"}},
        "how_to_read": {"type": "string"},
        "keywords": {"type": "array", "items": {"type": "string"}},
        "priority_questions": {"type": "array", "items": {"type": "string"}},
        "section_focus": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "id",
        "one_liner",
        "what_it_does",
        "method_and_evidence",
        "body_core_points",
        "why_it_matters",
        "risks",
        "how_to_read",
        "keywords",
        "priority_questions",
        "section_focus",
    ],
    "additionalProperties": False,
}
WATCHLIST_PAPER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "note": {"type": "string"},
    },
    "required": ["id", "note"],
    "additionalProperties": False,
}
ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "opening_summary": {"type": "string"},
        "trend_signals": {"type": "array", "items": {"type": "string"}},
        "selected_papers": {"type": "array", "items": SELECTED_PAPER_SCHEMA},
        "watchlist_papers": {"type": "array", "items": WATCHLIST_PAPER_SCHEMA},
    },
    "required": ["opening_summary", "trend_signals", "selected_papers", "watchlist_papers"],
    "additionalProperties": False,
}
SECTION_PATTERNS = {
    "Abstract": [r"\babstract\b"],
    "Introduction": [r"\bintroduction\b", r"\boverview\b"],
    "Method": [r"\bmethod\b", r"\bapproach\b", r"\bframework\b", r"\bmodel\b", r"\balgorithm\b"],
    "Experiments": [r"\bexperiments?\b", r"\bevaluation\b", r"\bresults?\b", r"\bbenchmark\b"],
    "Conclusion": [r"\bconclusion\b", r"\bdiscussion\b", r"\blimitation\b", r"\bfinal remarks\b"],
}


class ArxivNotUpdatedError(RuntimeError):
    """Raised when arXiv new submissions have not rolled over to the local day yet."""


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


# ================= Runtime Checks =================

def resolve_cli_binary(binary_name):
    """Find a CLI from PATH or a typical nvm installation."""
    binary_path = shutil.which(binary_name)
    if binary_path:
        return binary_path

    candidates = sorted(
        glob.glob(os.path.expanduser(f"~/.nvm/versions/node/*/bin/{binary_name}")),
        reverse=True,
    )
    for candidate in candidates:
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate

    return None


def ensure_runtime_requirements():
    """Fail fast when local prerequisites are unavailable."""
    global CODEX_BIN
    CODEX_BIN = resolve_cli_binary("codex")
    if not CODEX_BIN:
        print("❌ [Error] Codex CLI not found. Run `codex login` and ensure `codex` is in PATH.")
        return False

    if not CHATGPT_WEB_URL:
        print("❌ [Error] CHATGPT_WEB_URL is empty. Set it or use the default https://chatgpt.com/.")
        return False

    return True


# ================= Phase 1: Harvester =================

def fetch_arxiv_papers():
    """Fetch and parse structured data from arXiv new submissions."""
    print(f"🌐 [Harvester] Fetching from: {ARXIV_URL} ...")

    try:
        response = requests.get(ARXIV_URL, headers=REQUEST_HEADERS, timeout=15)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("❌ [Error] Network request timed out while fetching arXiv.")
        return None
    except requests.exceptions.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "unknown"
        print(f"❌ [Error] arXiv returned HTTP status {status_code}.")
        return None
    except requests.exceptions.ConnectionError as exc:
        error_text = str(exc)
        if "NameResolutionError" in error_text or "Failed to resolve" in error_text:
            print("❌ [Error] DNS resolution failed while connecting to arXiv. Check network or DNS settings.")
        else:
            print(f"❌ [Error] Could not connect to arXiv: {exc}")
        return None
    except requests.exceptions.RequestException as exc:
        print(f"❌ [Error] Network request failed: {exc}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    today = datetime.now()
    expected_date_str = f"{today.day} {today.strftime('%B %Y')}"

    date_header = soup.find("h3", string=re.compile(r"Showing new listings for", re.IGNORECASE))
    if date_header:
        page_date_str = date_header.text.strip()
        if expected_date_str not in page_date_str:
            print("\n⚠️ [Warning] Date mismatch detected between arXiv list and local time.")
            print(f"    > Webpage shows: {page_date_str}")
            print(f"    > Local expects: {expected_date_str}")

            if not sys.stdin.isatty():
                print("⏳ [Harvester] arXiv new submissions are not updated for the local day yet.")
                raise ArxivNotUpdatedError(page_date_str)

            try:
                choice = input("❓ Continue fetching and generating the report? [y/N]: ").strip().lower()
            except EOFError:
                print("⏳ [Harvester] Date mismatch confirmation was unavailable. Treating this as retryable.")
                raise ArxivNotUpdatedError(page_date_str)

            if choice not in ["y", "yes"]:
                print("🛑 [Aborted] Task cancelled by user because arXiv is not updated yet.")
                raise ArxivNotUpdatedError(page_date_str)
            print("▶️ [Continue] Confirmed by user, proceeding...\n")
    else:
        print("⚠️ [Warning] No explicit date identifier found on the page. Proceeding anyway.")

    dt_tags = soup.find_all("dt")
    dd_tags = soup.find_all("dd")

    papers = []
    print(f"📥 [Harvester] Found {len(dt_tags)} papers, starting to parse...")

    for dt, dd in zip(dt_tags, dd_tags):
        id_tag = dt.find("a", title="Abstract")
        if not id_tag:
            continue

        paper_id = normalize_paper_id(id_tag.text.strip())
        url = ARXIV_ABS_URL.format(paper_id=paper_id)

        title_div = dd.find("div", class_="list-title")
        if not title_div:
            print(f"  ⚠️ [Warning] Missing title for ID {paper_id}, skipping.")
            continue
        title = title_div.text.replace("Title:", "").strip()

        authors_div = dd.find("div", class_="list-authors")
        authors = authors_div.text.replace("Authors:", "").strip().replace("\n", " ") if authors_div else "Unknown"

        abstract_p = dd.find("p", class_="mathjax")
        if abstract_p:
            abstract = abstract_p.text.strip().replace("\n", " ")
            print(f"  ✅ [Info] Successfully parsed abstract: {paper_id}")
        else:
            abstract = "Abstract not available."
            print(f"  ⚠️ [Warning] Missing abstract for ID {paper_id}.")

        papers.append(
            {
                "id": paper_id,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "url": url,
                "pdf_url": ARXIV_PDF_URL.format(paper_id=paper_id),
            }
        )

    print(f"✅ [Harvester] Successfully extracted {len(papers)} papers.")
    return papers


# ================= Phase 2: Codex Screening =================

def run_codex_structured(prompt, schema, task_label, max_retries=2, retry_delay=3):
    """Invoke codex exec and force the final message through a JSON schema."""
    codex_bin = CODEX_BIN or resolve_cli_binary("codex")
    if not codex_bin:
        print("❌ [Error] Codex CLI not found. Run `codex login` and ensure `codex` is in PATH.")
        return None

    for attempt in range(max_retries):
        schema_path = None
        output_path = None
        try:
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as schema_file:
                json.dump(schema, schema_file, ensure_ascii=False)
                schema_path = schema_file.name

            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as output_file:
                output_path = output_file.name

            command = [
                codex_bin,
                "exec",
                "--color",
                "never",
                "--json",
                "--ephemeral",
                "--output-schema",
                schema_path,
                "--output-last-message",
                output_path,
                "-",
            ]
            if CODEX_MODEL:
                command[2:2] = ["-m", CODEX_MODEL]

            print(f"  🚀 [Codex] Request submitted. {task_label}...", flush=True)
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
            )

            start_time = time.time()
            stdout = ""
            stderr = ""
            pending_input = prompt
            while True:
                try:
                    stdout, stderr = process.communicate(input=pending_input, timeout=15)
                    break
                except subprocess.TimeoutExpired:
                    pending_input = None
                    elapsed = int(time.time() - start_time)
                    print(f"  ⏳ [Codex] Still working... {elapsed}s elapsed.", flush=True)

            with open(output_path, "r", encoding="utf-8") as output_file:
                structured_output = output_file.read().strip()

            elapsed = int(time.time() - start_time)
            jsonl_output = extract_codex_output_from_jsonl(stdout)
            fallback_output = structured_output or jsonl_output or clean_json_string(stdout)

            if fallback_output:
                if process.returncode != 0:
                    print(
                        f"  ⚠️ [Codex] CLI exited with code {process.returncode}, but a structured response was recovered from stdout.",
                        flush=True,
                    )
                print(f"  ✅ [Codex] Structured response received in {elapsed}s.", flush=True)
                return fallback_output

            if process.returncode != 0:
                error_lines = [line.strip() for line in (stderr or "").splitlines() if line.strip()]
                if not error_lines:
                    error_lines = [line.strip() for line in (stdout or "").splitlines() if line.strip()]
                error_msg = error_lines[-1] if error_lines else "Unknown Codex error"
                print(f"  ⚠️ [Retry {attempt + 1}/{max_retries}] Codex CLI failed: {error_msg}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                return None

            print(
                f"  ⚠️ [Retry {attempt + 1}/{max_retries}] Codex finished after {elapsed}s but returned empty output."
            )
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return None
        except Exception as exc:
            print(f"  ❌ [Retry {attempt + 1}/{max_retries}] Exception calling Codex CLI: {exc}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return None
        finally:
            for temp_path in (schema_path, output_path):
                if temp_path and os.path.exists(temp_path):
                    os.remove(temp_path)

    return None


def build_screening_prompt(papers):
    """Construct the Codex prompt used for shortlist screening."""
    papers_context = []
    for paper in papers:
        vip_tier = paper_vip_tier(paper)
        if vip_tier == "core":
            vip_prefix = "★★ [CORE VIP AUTHOR] "
        elif vip_tier == "extended":
            vip_prefix = "★ [EXTENDED VIP AUTHOR] "
        else:
            vip_prefix = ""
        papers_context.append(
            "\n".join(
                [
                    f"ID: {paper['id']}",
                    f"Title: {vip_prefix}{paper['title']}",
                    f"Authors: {paper['authors']}",
                    f"Abstract: {truncate_text(paper['abstract'], 650)}",
                ]
            )
        )

    today_str = datetime.now().strftime("%Y-%m-%d %A")
    return f"""
你是机器人学方向的资深研究编辑。你只能使用我提供的题目、作者和摘要信息判断，不允许捏造全文实验数字、表格结果或公式细节。

今天是 {today_str}。
我的研究兴趣是：{INTERESTS}。
核心优先作者名单：{", ".join(CORE_VIP_AUTHORS)}。
扩展关注作者名单：{", ".join(EXTENDED_VIP_AUTHORS)}。

目标：先做一个“宁可宽一点也不要漏掉强候选”的 shortlist，再从中挑出最终最值得精读的论文。

筛选规则：
1. `shortlist_ids` 选择 8-10 篇，允许略宽，只要与 VLA、Sim2Real、RL+VLA、World Model、具身智能泛化/评测强相关即可。
2. `selected_ids` 选择 4-6 篇，必须是 `shortlist_ids` 的子集，代表今天真正要精读的 Editor's Picks。
3. 如果两篇论文质量和相关性相近，优先级按 `core VIP > extended VIP > normal`。
4. 如果当天明显没有足够高价值工作，可以少选，甚至 `selected_ids` 为空。
5. 所有 ID 必须来自给定列表，不能捏造。

`opening_summary` 要求：
- 3-5 句中文趋势判断。
- 先写今天这批论文最值得关注的主线，再写本期筛选偏向什么。
- 可以指出 VIP 作者论文是否值得优先跟进。

输出要求：
- 只返回一个合法 JSON 对象，不要使用代码块。
- `title` 用简短日报标题，例如 `RoboPulse | 2026-03-19`。
- `shortlist_ids` 与 `selected_ids` 都只放 arXiv ID 字符串。

论文列表如下：

{os.linesep.join(papers_context)}
"""


def editor_screening(papers):
    """Generate shortlist and selected IDs from titles and abstracts."""
    model_display = CODEX_MODEL if CODEX_MODEL else "codex default model"
    print(f"\n🧐 [Editor] Screening {len(papers)} papers using {model_display}...")
    print(
        f"  🧾 [Editor] Stage 1 sends abstracts only, expands to a shortlist, and locks the final candidates.",
        flush=True,
    )

    response = run_codex_structured(build_screening_prompt(papers), SCREENING_SCHEMA, "Screening abstracts now")
    if not response:
        return None

    paper_map = {normalize_paper_id(paper["id"]): paper for paper in papers}

    try:
        data = json.loads(clean_json_string(response))
    except json.JSONDecodeError as exc:
        print(f"❌ [Error] JSON parsing failed during screening: {exc}")
        return None

    shortlist_ids = normalize_known_ids(data.get("shortlist_ids", []), paper_map)
    selected_ids = normalize_known_ids(data.get("selected_ids", []), paper_map)

    if not shortlist_ids and selected_ids:
        shortlist_ids = selected_ids[:]

    for selected_id in selected_ids:
        if selected_id not in shortlist_ids:
            shortlist_ids.append(selected_id)

    selected_ids = [paper_id for paper_id in selected_ids if paper_id in shortlist_ids]

    if len(shortlist_ids) > SHORTLIST_TARGET:
        pinned = selected_ids[:]
        shortlist_ids = pinned + [paper_id for paper_id in shortlist_ids if paper_id not in pinned]
        shortlist_ids = shortlist_ids[:SHORTLIST_TARGET]
        selected_ids = [paper_id for paper_id in selected_ids if paper_id in shortlist_ids]

    title = normalize_whitespace(data.get("title", "")) or f"RoboPulse | {datetime.now().strftime('%Y-%m-%d')}"
    opening_summary = normalize_whitespace(data.get("opening_summary", ""))

    print(
        f"✅ [Editor] Screening complete. Shortlisted {len(shortlist_ids)} papers, picked {len(selected_ids)} for deep reading."
    )
    return {
        "title": title,
        "opening_summary": opening_summary,
        "shortlist_ids": shortlist_ids,
        "selected_ids": selected_ids,
    }


# ================= Phase 3: HTML Reader =================

def safe_get(url, timeout=15):
    """Fetch a URL and return a response object or None."""
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException:
        return None


def discover_versioned_id(paper_id):
    """Find the latest versioned arXiv ID from the abstract page when needed."""
    if re.search(r"v\d+$", paper_id):
        return paper_id

    response = safe_get(ARXIV_ABS_URL.format(paper_id=paper_id), timeout=10)
    if not response:
        return None

    match = re.search(rf"/abs/({re.escape(paper_id)}v\d+)", response.text)
    if match:
        return match.group(1)

    return None


def looks_like_html_paper(text):
    """Best-effort detection for a rendered paper page instead of an error page."""
    lowered = text.lower()
    if "<html" not in lowered:
        return False
    if "does not have html" in lowered or "not available in html" in lowered:
        return False
    return "ltx_" in lowered or "abstract" in lowered or "section" in lowered


def fetch_arxiv_html(paper):
    """Try several arXiv HTML URLs and return the first viable page."""
    normalized_id = normalize_paper_id(paper["id"])
    candidate_ids = [paper["id"], normalized_id]

    versioned_id = discover_versioned_id(normalized_id)
    if versioned_id:
        candidate_ids.append(versioned_id)

    for candidate_id in dedupe_preserve_order(candidate_ids):
        html_url = ARXIV_HTML_URL.format(paper_id=candidate_id)
        response = safe_get(html_url, timeout=15)
        if response and "text/html" in response.headers.get("content-type", "") and looks_like_html_paper(response.text):
            return html_url, response.text

    return None, None


def clean_html_soup(soup):
    """Remove tags that add noise to downstream summarization."""
    for tag in soup.find_all(
        [
            "script",
            "style",
            "noscript",
            "svg",
            "math",
            "table",
            "figure",
            "figcaption",
            "footer",
            "nav",
            "header",
            "aside",
        ]
    ):
        tag.decompose()

    noise_classes = re.compile(
        r"(ltx_page_navbar|ltx_bibliography|ltx_note|ltx_dates|ltx_acknowledgement|ltx_role_footnote|ltx_tag_figure)"
    )
    for tag in soup.find_all(class_=noise_classes):
        tag.decompose()


def extract_section_from_heading(heading, limit):
    """Capture text from the heading's section or nearest sibling block."""
    parent = heading.parent
    heading_text = normalize_whitespace(heading.get_text(" ", strip=True))

    if getattr(parent, "name", None) in {"section", "div"}:
        parent_text = normalize_whitespace(parent.get_text(" ", strip=True))
        if parent_text and parent_text != heading_text:
            section_text = parent_text.replace(heading_text, "", 1).strip(" :.-")
            if section_text:
                return truncate_text(section_text, limit)

    pieces = []
    for sibling in heading.next_siblings:
        sibling_name = getattr(sibling, "name", None)
        if sibling_name and re.fullmatch(r"h[1-6]", sibling_name):
            break

        text = normalize_whitespace(sibling.get_text(" ", strip=True) if hasattr(sibling, "get_text") else str(sibling))
        if not text:
            continue

        pieces.append(text)
        if len(" ".join(pieces)) >= limit:
            break

    return truncate_text(" ".join(pieces), limit)


def find_section_text(root, regex_patterns, limit):
    """Locate a likely section by heading text."""
    heading_candidates = []
    heading_candidates.extend(root.find_all(re.compile(r"^h[1-6]$")))
    heading_candidates.extend(root.find_all(class_=re.compile(r"ltx_title", re.IGNORECASE)))

    seen = set()
    for heading in heading_candidates:
        if id(heading) in seen:
            continue
        seen.add(id(heading))
        heading_text = normalize_whitespace(heading.get_text(" ", strip=True)).lower()
        if not heading_text:
            continue

        if any(re.search(pattern, heading_text, re.IGNORECASE) for pattern in regex_patterns):
            section_text = extract_section_from_heading(heading, limit)
            if section_text:
                return section_text

    return ""


def extract_html_context(paper, html_text, html_url):
    """Extract concise, high-value text from an arXiv HTML page."""
    soup = BeautifulSoup(html_text, "html.parser")
    clean_html_soup(soup)

    root = soup.find("article") or soup.find("main") or soup.body or soup
    abstract_text = find_section_text(root, SECTION_PATTERNS["Abstract"], 800) or paper["abstract"]
    intro_text = find_section_text(root, SECTION_PATTERNS["Introduction"], 950)
    method_text = find_section_text(root, SECTION_PATTERNS["Method"], 1200)
    experiments_text = find_section_text(root, SECTION_PATTERNS["Experiments"], 1200)
    conclusion_text = find_section_text(root, SECTION_PATTERNS["Conclusion"], 700)
    body_excerpt = truncate_text(root.get_text(" ", strip=True), 2200)

    sections = []
    if intro_text:
        sections.append("Introduction")
    if method_text:
        sections.append("Method")
    if experiments_text:
        sections.append("Experiments")
    if conclusion_text:
        sections.append("Conclusion")

    context_parts = [
        f"Content Source: arXiv HTML",
        f"HTML URL: {html_url}",
        f"Abstract: {truncate_text(abstract_text, 650)}",
    ]
    if intro_text:
        context_parts.append(f"Introduction: {intro_text}")
    if method_text:
        context_parts.append(f"Method: {method_text}")
    if experiments_text:
        context_parts.append(f"Experiments: {experiments_text}")
    if conclusion_text:
        context_parts.append(f"Conclusion: {conclusion_text}")
    if len(context_parts) == 3:
        context_parts.append(f"Body Excerpt: {body_excerpt}")

    return {
        "html_url": html_url,
        "content_source_label": "arXiv HTML",
        "available_sections": sections,
        "html_context": truncate_text("\n\n".join(context_parts), SHORTLIST_CONTEXT_LIMIT),
    }


def enrich_shortlist_with_html(shortlist_papers):
    """Fetch arXiv HTML for shortlisted papers and build compact context snippets."""
    print(f"\n📚 [Reader] Fetching arXiv HTML for {len(shortlist_papers)} shortlisted papers...")
    enriched = []

    for index, paper in enumerate(shortlist_papers, start=1):
        print(f"  🌍 [Reader] [{index}/{len(shortlist_papers)}] {paper['id']} ...", flush=True)
        html_url, html_text = fetch_arxiv_html(paper)
        paper_copy = dict(paper)

        if html_text:
            context = extract_html_context(paper, html_text, html_url)
            paper_copy.update(context)
            sections_label = ", ".join(context["available_sections"]) if context["available_sections"] else "body excerpt"
            print(f"    ✅ [Reader] HTML captured: {sections_label}")
        else:
            paper_copy.update(
                {
                    "html_url": "",
                    "content_source_label": "Abstract fallback",
                    "available_sections": [],
                    "html_context": f"Content Source: Abstract fallback\n\nAbstract: {truncate_text(paper['abstract'], 900)}",
                }
            )
            print("    ⚠️ [Reader] HTML unavailable. Falling back to abstract-only context.")

        enriched.append(paper_copy)

    return enriched


# ================= Phase 4: Deep Analysis =================

def extract_context_snippet(paper, label):
    """Pull one labeled snippet back out of the stored HTML context."""
    pattern = rf"{re.escape(label)}:\s*(.*?)(?:\n\n(?:Abstract|Introduction|Method|Experiments|Conclusion|Body Excerpt):|\Z)"
    match = re.search(pattern, paper.get("html_context", ""), re.DOTALL)
    if not match:
        return ""
    return normalize_whitespace(match.group(1))


def default_trend_signals(summary):
    """Backfill a compact trend section when the model omits it."""
    sentences = [
        normalize_whitespace(chunk)
        for chunk in re.split(r"[。！？!?]+", summary or "")
        if normalize_whitespace(chunk)
    ]
    if len(sentences) >= 3:
        return sentences[:3]

    defaults = list(sentences)
    defaults.extend(
        [
            "优先看进入最终精选的论文之间是否形成一条清晰方法主线，而不是只盯单点结果。",
            "如果 HTML 正文证据不够，就把结论视作趋势判断，回到 PDF 核实实验细节。",
            "VIP 作者论文优先级更高，但是否值得跟进仍以问题强度和证据链完整度为准。",
        ]
    )
    return defaults[:3]


def build_analysis_prompt(screening_result, shortlisted_papers):
    """Construct the second-stage prompt using HTML-enriched shortlist context."""
    selected_ids = screening_result["selected_ids"]
    watchlist_ids = [paper_id for paper_id in screening_result["shortlist_ids"] if paper_id not in selected_ids]

    paper_blocks = []
    for paper in shortlisted_papers:
        is_selected = "yes" if paper["id"] in selected_ids else "no"
        is_watchlist = "yes" if paper["id"] in watchlist_ids else "no"
        vip_tier = paper_vip_tier(paper) or "none"
        html_url = paper["html_url"] or "(unavailable)"

        paper_blocks.append(
            "\n".join(
                [
                    f"ID: {paper['id']}",
                    f"Title: {paper['title']}",
                    f"Authors: {paper['authors']}",
                    f"VIP Author Tier: {vip_tier}",
                    f"Selected for final picks: {is_selected}",
                    f"Assigned to watchlist: {is_watchlist}",
                    f"Abstract URL: {paper['url']}",
                    f"PDF URL: {paper['pdf_url']}",
                    f"HTML URL: {html_url}",
                    paper["html_context"],
                ]
            )
        )

    return f"""
你是机器人学方向的资深研究编辑。现在你拿到了 shortlist 论文的 arXiv HTML 摘录，少数论文可能只有摘要回退信息。

今天的关注方向：{INTERESTS}
核心优先作者名单：{", ".join(CORE_VIP_AUTHORS)}
扩展关注作者名单：{", ".join(EXTENDED_VIP_AUTHORS)}

硬性约束：
1. 必须严格保留这组最终选择，不要改 ID，不要新增或删除：
   - Editor's Picks IDs: {", ".join(selected_ids) if selected_ids else "none"}
   - Watchlist IDs: {", ".join(watchlist_ids) if watchlist_ids else "none"}
2. `selected_papers` 必须与 Editor's Picks IDs 一一对应，顺序一致。
3. `watchlist_papers` 必须与 Watchlist IDs 一一对应，顺序一致。
4. 只能使用我提供的摘要与 HTML 摘录，不允许捏造 PDF 里的具体数字、表格、图号或公式。
5. 如果某条信息在 HTML 摘录中证据不足，请保守表达，明确写成趋势判断或合理推断。

写作目标：
- `opening_summary`：3-5 句中文总结，写清今天主线、为什么这些论文进了最终精选，以及 VIP 作者里哪些值得优先跟踪。
- `trend_signals`：恰好 3 条，每条 1 句，写成“今天最值得记住的研究信号/趋势判断”。
- `selected_papers`：每篇写成接近深度研究简报风格的高质量研究卡片，不要写成提示词模板，也不要只重复摘要。
  - `one_liner`: 一句话判断，直接说值不值得优先看。
  - `what_it_does`: 140-220 字，写这篇在解决什么问题、核心切口是什么、相对已有路线的新意在哪里。
  - `method_and_evidence`: 140-220 字，重点写方法脉络、正文里能读到的关键模块/实验设计/证据边界。
  - `body_core_points`: 恰好 3 条短点，尽量来自 HTML 正文核心内容。优先写贡献点、实验设定、限制条件或作者自己强调的关键观察；不要写空泛套话。
  - `why_it_matters`: 3 条短点，每条独立完整。
  - `risks`: 2 条短点，写边界、实验可信度或复现风险。
  - `how_to_read`: 1-2 句，告诉我作为研究者最值得先看哪条主线。
  - `keywords`: 3-5 个关键词。
  - `priority_questions`: 恰好 3 条，每条都要针对该论文具体方法或主张，不能是泛泛而谈。
  - `section_focus`: 恰好 3 条，写我上传 PDF 后优先核查的章节/实验/图表类型；如果不知道图号，就写章节类型。
- `watchlist_papers`：每篇写 2-4 句，说明为什么进入 shortlist，但为什么没有进入最终精选。

shortlist 论文上下文如下：

{os.linesep.join(paper_blocks)}
"""


def default_priority_questions(paper):
    """Build paper-specific fallback questions when Codex output is incomplete."""
    source = f"{paper['title']} {paper['abstract']}".lower()

    if "world model" in source or "video" in source:
        return [
            "world model 的状态演化或视频 rollout 是如何被约束到可执行机器人动作上的？",
            "作者拿什么证据证明生成轨迹不只是看起来合理，而是真的能提升下游执行？",
            "模型保真度、奖励设计或 rollout 偏差在哪些场景最可能失效？",
        ]
    if "continual" in source or "forget" in source or "replay" in source:
        return [
            "作者如何定义和测量 forgetting、forward transfer 与 recovery？",
            "预训练规模和 replay buffer 大小分别贡献了多少效果？",
            "这个结论是否依赖特定任务分布、评测协议或模型族？",
        ]
    if "retrieval" in source or "benchmark" in source or "evaluation" in source:
        return [
            "检索模块和判别模块分别在泛化分析中承担什么角色？",
            "作者如何证明这个框架真的能区分 interpolation、compositional generalization 和 OOD？",
            "分析结论会不会被数据覆盖度或 embedding 偏置带偏？",
        ]
    if "intent" in source or "trajectory" in source:
        return [
            "意图和执行细节是如何在表示层面被拆开的？",
            "one-shot transfer 真正依赖的是哪个 token、模块或训练约束？",
            "在扰动、任务切换和长时序操作上，作者给了哪些硬证据？",
        ]
    if "vla" in source or "vision-language-action" in source:
        return [
            "这篇工作到底改了 VLA 的哪一层接口或训练链路？",
            "最能证明提升来自新设计而不是数据/模型规模的证据是什么？",
            "方法在跨任务、跨本体或真实机器人落地时最脆弱的环节是什么？",
        ]

    return [
        "这篇论文最核心的技术新意到底落在哪个模块或设计选择上？",
        "作者给出的实验里，哪一部分最能支撑它的主要结论？",
        "如果要复现或迁移到自己的研究里，最大的未知数是什么？",
    ]


def default_section_focus(paper):
    """Build paper-specific fallback reading focus."""
    source = f"{paper['title']} {paper['abstract']}".lower()

    if "world model" in source or "video" in source:
        return ["Method / Framework", "Robot execution experiments", "Ablation on rollout fidelity or reward design"]
    if "continual" in source or "forget" in source:
        return ["Problem setup and metrics", "Main continual learning results", "Replay / pretraining ablations"]
    if "retrieval" in source or "evaluation" in source:
        return ["Pipeline overview", "Controlled evaluation section", "Case studies or qualitative analysis"]
    if "intent" in source or "trajectory" in source:
        return ["Representation or tokenization section", "Transfer / disturbance experiments", "Implementation details for action decoding"]
    if "vla" in source:
        return ["Model architecture", "Main benchmark results", "Generalization or real-robot experiments"]

    return ["Method section", "Main experimental results", "Limitations or appendix details"]


def sanitize_selected_detail(raw_detail, paper):
    """Normalize and backfill a selected paper card."""
    body_core_points = [
        normalize_whitespace(item) for item in raw_detail.get("body_core_points", []) if normalize_whitespace(item)
    ]
    why_it_matters = [normalize_whitespace(item) for item in raw_detail.get("why_it_matters", []) if normalize_whitespace(item)]
    risks = [normalize_whitespace(item) for item in raw_detail.get("risks", []) if normalize_whitespace(item)]
    keywords = [normalize_whitespace(item) for item in raw_detail.get("keywords", []) if normalize_whitespace(item)]
    priority_questions = [
        normalize_whitespace(item) for item in raw_detail.get("priority_questions", []) if normalize_whitespace(item)
    ]
    section_focus = [normalize_whitespace(item) for item in raw_detail.get("section_focus", []) if normalize_whitespace(item)]

    if not why_it_matters:
        why_it_matters = [
            "与当前研究兴趣直接相关。",
            "问题设定具有潜在方法价值。",
            "值得用 PDF 再确认核心证据。",
        ]
    if not risks:
        risks = ["目前证据仍需依赖 PDF 细读确认。", "摘要和 HTML 摘录无法完全替代完整实验表格。"]
    if len(body_core_points) < 3:
        body_core_points = []
        for label in ["Introduction", "Method", "Experiments", "Conclusion", "Abstract"]:
            snippet = extract_context_snippet(paper, label)
            if snippet:
                body_core_points.append(f"{label}: {truncate_text(snippet, 140)}")
            if len(body_core_points) == 3:
                break
    if len(body_core_points) < 3:
        body_core_points.append(f"Abstract: {truncate_text(paper['abstract'], 140)}")
    body_core_points = dedupe_preserve_order(body_core_points)[:3]
    if not keywords:
        keywords = ["robotics", "paper"]
    if len(priority_questions) < 3:
        priority_questions = default_priority_questions(paper)
    else:
        priority_questions = priority_questions[:3]
    if len(section_focus) < 3:
        section_focus = default_section_focus(paper)
    else:
        section_focus = section_focus[:3]

    return {
        "id": paper["id"],
        "one_liner": normalize_whitespace(raw_detail.get("one_liner", "")) or "值得快速精读，但关键证据仍需要看完整 PDF。",
        "what_it_does": normalize_whitespace(raw_detail.get("what_it_does", "")) or truncate_text(paper["abstract"], 220),
        "method_and_evidence": normalize_whitespace(raw_detail.get("method_and_evidence", ""))
        or "目前主要依据 arXiv HTML 摘录与摘要推断方法脉络，具体实验数字仍需回到 PDF 核实。",
        "body_core_points": body_core_points,
        "why_it_matters": why_it_matters[:3],
        "risks": risks[:2],
        "how_to_read": normalize_whitespace(raw_detail.get("how_to_read", ""))
        or "先看方法总览和主实验，再决定是否值得深入复现。",
        "keywords": keywords[:5],
        "priority_questions": priority_questions,
        "section_focus": section_focus,
    }


def sanitize_watchlist_detail(raw_detail, paper):
    """Normalize watchlist note text."""
    note = normalize_whitespace(raw_detail.get("note", ""))
    if not note:
        note = "主题仍有参考价值，但从当前摘要与 HTML 证据看，强度还不足以进入今天的最终精选。"
    return {"id": paper["id"], "note": note}


def analyze_shortlist(screening_result, shortlisted_papers):
    """Generate HTML-enriched cards for selected papers and watchlist notes."""
    if not shortlisted_papers:
        print("⚠️ [Editor] Shortlist is empty. Publishing a summary-only issue.")
        return {
            "opening_summary": screening_result["opening_summary"],
            "trend_signals": default_trend_signals(screening_result["opening_summary"]),
            "selected_papers": [],
            "watchlist_papers": [],
        }

    model_display = CODEX_MODEL if CODEX_MODEL else "codex default model"
    print(f"\n🧠 [Editor] Upgrading the shortlist with HTML reading using {model_display}...")
    print(
        f"  📚 [Editor] Stage 2 sends HTML-enriched context for {len(shortlisted_papers)} shortlisted papers.",
        flush=True,
    )

    response = run_codex_structured(
        build_analysis_prompt(screening_result, shortlisted_papers),
        ANALYSIS_SCHEMA,
        "Reading shortlist HTML and drafting richer paper cards",
    )
    if not response:
        return None

    try:
        data = json.loads(clean_json_string(response))
    except json.JSONDecodeError as exc:
        print(f"❌ [Error] JSON parsing failed during HTML analysis: {exc}")
        return None

    shortlist_map = {paper["id"]: paper for paper in shortlisted_papers}
    selected_ids = screening_result["selected_ids"]
    watchlist_ids = [paper_id for paper_id in screening_result["shortlist_ids"] if paper_id not in selected_ids]

    selected_by_id = {}
    for raw_detail in data.get("selected_papers", []):
        paper = shortlist_map.get(normalize_paper_id(raw_detail.get("id", "")))
        if not paper or paper["id"] not in selected_ids:
            continue
        selected_by_id[paper["id"]] = sanitize_selected_detail(raw_detail, paper)

    watchlist_by_id = {}
    for raw_detail in data.get("watchlist_papers", []):
        paper = shortlist_map.get(normalize_paper_id(raw_detail.get("id", "")))
        if not paper or paper["id"] not in watchlist_ids:
            continue
        watchlist_by_id[paper["id"]] = sanitize_watchlist_detail(raw_detail, paper)

    selected_papers = [
        sanitize_selected_detail(selected_by_id.get(paper_id, {}), shortlist_map[paper_id])
        for paper_id in selected_ids
        if paper_id in shortlist_map
    ]
    watchlist_papers = [
        sanitize_watchlist_detail(watchlist_by_id.get(paper_id, {}), shortlist_map[paper_id])
        for paper_id in watchlist_ids
        if paper_id in shortlist_map
    ]

    print(
        f"✅ [Editor] HTML enrichment complete. Drafted {len(selected_papers)} featured cards and {len(watchlist_papers)} watchlist notes."
    )
    return {
        "opening_summary": normalize_whitespace(data.get("opening_summary", "")) or screening_result["opening_summary"],
        "trend_signals": [
            normalize_whitespace(item) for item in data.get("trend_signals", []) if normalize_whitespace(item)
        ][:3]
        or default_trend_signals(screening_result["opening_summary"]),
        "selected_papers": selected_papers,
        "watchlist_papers": watchlist_papers,
    }


# ================= Phase 5: Prompt Builder =================

def build_chatgpt_prompt(paper, detail):
    """Build a tailored prompt for reading one paper in ChatGPT Web after PDF upload."""
    priority_questions = "\n".join(f"- {question}" for question in detail["priority_questions"])
    section_focus = "\n".join(f"- {section}" for section in detail["section_focus"])

    return f"""你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: {paper['title']}
- Authors: {paper['authors']}
- arXiv Abstract URL: {paper['url']}
- Research Interests: {INTERESTS}
- Quick Judgment: {detail['one_liner']}
- Current Read of the Paper: {detail['what_it_does']}
- Method / Evidence Clues from arXiv HTML: {detail['method_and_evidence']}

这次请优先替我核查下面 3 个问题：
{priority_questions}

上传 PDF 后，请优先查看这些章节、实验或图表类型：
{section_focus}

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？请把关键模块、训练/推理流程串起来。
3. 对上面 3 个核查问题逐一回答。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 不要只重复摘要，要优先验证方法细节、实验可信度和边界条件。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。
"""


# ================= Phase 6: Publisher =================

def resource_tokens(paper, include_chatgpt):
    """Render badge-like markdown tokens for one paper heading."""
    tokens = []
    if paper_has_vip(paper):
        tokens.append("[[VIP]]")
    if paper.get("html_url"):
        tokens.append(f"[[HTML]]({paper['html_url']})")
    tokens.append(f"[[PDF]]({paper['pdf_url']})")
    if include_chatgpt:
        tokens.append(f"[[ChatGPT]]({CHATGPT_WEB_URL})")
    return " ".join(tokens)


def content_source_summary(paper):
    """Describe how much paper body context was available."""
    sections = paper.get("available_sections", [])
    if sections:
        return f"{paper['content_source_label']} ({', '.join(sections)})"
    return paper["content_source_label"]


def build_report_markdown(issue_title, total_papers, screening_result, enriched_papers, analysis_result):
    """Assemble the markdown report body."""
    enriched_map = {paper["id"]: paper for paper in enriched_papers}
    lines = [
        f"# {issue_title}",
        "",
        f"> **Focus**: {INTERESTS}",
        f"> **Pipeline**: {total_papers} papers scanned · {len(screening_result['shortlist_ids'])} shortlisted · {len(screening_result['selected_ids'])} editor's picks",
        "",
        analysis_result["opening_summary"] or screening_result["opening_summary"] or "今天的精选基于摘要初筛和 shortlist HTML 精读生成。",
        "",
        "## 今日信号",
        "",
    ]

    for signal in analysis_result.get("trend_signals", [])[:3]:
        lines.append(f"- {signal}")

    lines.extend(["", "## Editor's Picks", ""])

    if not analysis_result["selected_papers"]:
        lines.append("*(今日没有进入最终精选的论文，但可查看 Watchlist 作为备选。)*")
        lines.append("")

    for index, detail in enumerate(analysis_result["selected_papers"], start=1):
        paper = enriched_map[detail["id"]]
        lines.extend(
            [
                f"### [{index}]. {paper['title']} {resource_tokens(paper, include_chatgpt=True)}".rstrip(),
                f"* **Paper ID**: `{paper['id']}`",
                f"* **Authors**: {paper['authors']}",
                f"* **Author Priority**: {paper_priority_label(paper)}",
                f"* **一句话结论**: {detail['one_liner']}",
                f"* **问题与切口**: {detail['what_it_does']}",
                f"* **核心方法与证据**: {detail['method_and_evidence']}",
                "* **正文要点**:",
            ]
        )
        lines.extend(f"  - {point}" for point in detail["body_core_points"])
        lines.extend(["* **为什么值得跟**:"])
        lines.extend(f"  - {point}" for point in detail["why_it_matters"])
        lines.extend(["* **风险 / 保留意见**:"])
        lines.extend(f"  - {point}" for point in detail["risks"])
        lines.extend(
            [
                f"* **建议先看**: {detail['how_to_read']}",
                "* **关键词**: " + " ".join(f"`{keyword}`" for keyword in detail["keywords"]),
                f"* **证据来源**: {content_source_summary(paper)}",
                "* **读 PDF 先核查**:",
            ]
        )
        lines.extend(f"  - {question}" for question in detail["priority_questions"])
        lines.extend(["* **上传 PDF 后优先看**:"])
        lines.extend(f"  - {section}" for section in detail["section_focus"])
        lines.append("")

    lines.extend(["## Watchlist", ""])
    if not analysis_result["watchlist_papers"]:
        lines.append("*(shortlist 之外没有额外需要保留的备选论文。)*")
        lines.append("")
    else:
        for index, detail in enumerate(analysis_result["watchlist_papers"], start=1):
            paper = enriched_map[detail["id"]]
            lines.extend(
                [
                    f"### [{WATCHLIST_PREFIX}{index}]. {paper['title']} {resource_tokens(paper, include_chatgpt=False)}".rstrip(),
                    f"* **Paper ID**: `{paper['id']}`",
                    f"* **Authors**: {paper['authors']}",
                    f"* **Author Priority**: {paper_priority_label(paper)}",
                    f"* **为什么还值得留意**: {detail['note']}",
                    f"* **证据来源**: {content_source_summary(paper)}",
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def publish_report(issue_title, total_papers, screening_result, enriched_papers, analysis_result):
    """Assemble the markdown report and persist it to disk."""
    print("\n🖨️ [Publisher] Assembling final report...")

    date_str = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    final_content = build_report_markdown(issue_title, total_papers, screening_result, enriched_papers, analysis_result)
    filename = os.path.join(OUTPUT_DIR, f"{date_str}-RoboPulse.md")
    with open(filename, "w", encoding="utf-8") as report_file:
        report_file.write(final_content)

    print(f"🎉 [Done] Report generated successfully: {filename}")
    return filename


# ================= Main Execution =================

def main():
    """Main application loop."""
    if not ensure_runtime_requirements():
        return GENERAL_FAILURE_EXIT_CODE

    try:
        papers = fetch_arxiv_papers()
    except ArxivNotUpdatedError:
        return ARXIV_NOT_UPDATED_EXIT_CODE

    if papers is None:
        return GENERAL_FAILURE_EXIT_CODE
    if not papers:
        print("⚠️ [Warning] No papers found in the latest arXiv listing.")
        return 0

    screening_result = editor_screening(papers)
    if not screening_result:
        return GENERAL_FAILURE_EXIT_CODE

    paper_map = {normalize_paper_id(paper["id"]): paper for paper in papers}
    shortlisted_papers = [paper_map[paper_id] for paper_id in screening_result["shortlist_ids"] if paper_id in paper_map]
    enriched_papers = enrich_shortlist_with_html(shortlisted_papers)
    analysis_result = analyze_shortlist(screening_result, enriched_papers)
    if not analysis_result:
        return GENERAL_FAILURE_EXIT_CODE

    publish_report(
        screening_result["title"],
        len(papers),
        screening_result,
        enriched_papers,
        analysis_result,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
