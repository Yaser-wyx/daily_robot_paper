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
CODEX_MODEL = os.environ.get("CODEX_MODEL", "").strip()
CHATGPT_WEB_URL = os.environ.get("CHATGPT_WEB_URL", "https://chatgpt.com/").strip()
INTERESTS = "VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model"
VIP_AUTHORS = [
    "Sergey Levine", "Chelsea Finn", "Pieter Abbeel", "Dorsa Sadigh",
    "Huazhe Xu", "Cewu Lu", "Xiaolong Wang", "Hao Su",
    "Jiangmiao Pang", "He Wang", "Shuran Song", "Donglin Wang", "Yue Wang",
]
OUTPUT_DIR = "./reports"
CODEX_BIN = None
ARXIV_NOT_UPDATED_EXIT_CODE = 75
GENERAL_FAILURE_EXIT_CODE = 1
SCREENING_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "summary_content": {"type": "string"},
        "selected_ids": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": ["title", "summary_content", "selected_ids"],
    "additionalProperties": False,
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
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(ARXIV_URL, headers=headers, timeout=15)
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

        paper_id = id_tag.text.strip().replace("arXiv:", "")
        url = f"https://arxiv.org/abs/{paper_id}"

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

        papers.append({
            "id": paper_id,
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "url": url,
        })

    print(f"✅ [Harvester] Successfully extracted {len(papers)} papers.")
    return papers


# ================= Phase 2: Codex Screening =================

def clean_json_string(text):
    """Extract the first JSON object from model output."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text


def run_codex_structured(prompt, schema, max_retries=2, retry_delay=3):
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
                "--ephemeral",
                "--output-schema",
                schema_path,
                "--output-last-message",
                output_path,
                "-",
            ]
            if CODEX_MODEL:
                command[2:2] = ["-m", CODEX_MODEL]

            print("  🚀 [Codex] Request submitted. Screening abstracts now...", flush=True)
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
                    print(f"  ⏳ [Codex] Still screening... {elapsed}s elapsed.", flush=True)

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

            with open(output_path, "r", encoding="utf-8") as output_file:
                structured_output = output_file.read().strip()

            elapsed = int(time.time() - start_time)
            if structured_output:
                print(f"  ✅ [Codex] Structured response received in {elapsed}s.", flush=True)
                return structured_output

            print(f"  ⚠️ [Retry {attempt + 1}/{max_retries}] Codex finished after {elapsed}s but returned empty output.")
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
    """Construct the codex prompt used for daily screening."""
    papers_context = []
    for paper in papers:
        is_vip = any(vip in paper["authors"] for vip in VIP_AUTHORS)
        vip_prefix = "★ [VIP AUTHOR] " if is_vip else ""
        papers_context.append(
            "\n".join(
                [
                    f"ID: {paper['id']}",
                    f"Title: {vip_prefix}{paper['title']}",
                    f"Authors: {paper['authors']}",
                    f"Abstract: {paper['abstract'][:500]}",
                ]
            )
        )

    today_str = datetime.now().strftime("%Y-%m-%d %A")
    return f"""
你是机器人学方向的资深研究编辑。你只能使用我提供的题目、作者和摘要信息判断，不允许捏造全文实验数字、表格结果或公式细节。

今天是 {today_str}。
我的研究兴趣是：{INTERESTS}。
请优先关注作者名单：{", ".join(VIP_AUTHORS)}。

目标：生成一份帮助研究者快速决定“是否值得进一步精读”的中文日报。

筛选规则：
1. 宁缺毋滥，最多选择 6 篇真正相关的论文。
2. 优先选择 VLA、Sim2Real、RL+VLA、World Model，以及相邻的具身智能高价值工作。
3. 如果没有明显符合方向的论文，可以少选甚至不选。
4. `selected_ids` 必须严格对应正文里出现的论文 ID，不能捏造或遗漏。

`summary_content` 里的 Markdown 结构要求：
- 开头给一个中文整体趋势判断，2-4 句。
- 每篇入选论文使用以下结构：
### [序号]. 论文标题
* **Title**: 英文原标题
* **摘要介绍**: 150-220 字中文总结，只基于摘要和标题推断，明确核心问题、方法方向和潜在价值
* **为什么值得看**:
  - 3 条短点，每条 1 句
* **潜在风险/局限**:
  - 2 条短点，每条 1 句
* **关键词**: `kw1` `kw2` `kw3`

输出要求：
- 只返回一个合法 JSON 对象，不要使用代码块。
- `summary_content` 必须是完整 Markdown。
- `selected_ids` 里只放 arXiv ID 字符串。

论文列表如下：

{os.linesep.join(papers_context)}
"""


def editor_screening(papers):
    """Generate a richer daily briefing using Codex."""
    model_display = CODEX_MODEL if CODEX_MODEL else "codex default model"
    print(f"\n🧐 [Editor] Reading paper list and drafting briefing using {model_display}...")
    print(f"  🧾 [Editor] Sending {len(papers)} paper abstracts to Codex. This can take 30-120 seconds.", flush=True)

    response = run_codex_structured(build_screening_prompt(papers), SCREENING_SCHEMA)
    if not response:
        return None, []

    try:
        data = json.loads(clean_json_string(response))
        selected_ids = dedupe_preserve_order(data.get("selected_ids", []))
        print(f"✅ [Editor] Screening complete. Selected {len(selected_ids)} papers.")
        return data.get("summary_content", ""), selected_ids
    except json.JSONDecodeError as exc:
        print(f"❌ [Error] JSON parsing failed: {exc}")
        return response, []


# ================= Phase 3: ChatGPT Follow-up Blocks =================

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


def build_chatgpt_prompt(paper_info):
    """Build the prompt that the user can paste into ChatGPT after uploading the PDF."""
    return f"""你是我的机器人学研究搭档。请先检查我是否已经上传这篇论文的 PDF。

如果我还没有上传 PDF，请先提醒我上传 PDF，再暂停，不要猜测全文细节。

论文基础信息：
- Title: {paper_info['title']}
- Authors: {paper_info['authors']}
- arXiv Abstract URL: {paper_info['url']}
- Research Interests: {INTERESTS}
- Abstract: {paper_info['abstract']}

在我上传 PDF 之后，请严格按下面结构输出中文分析，保留关键英文术语：
1. 这篇论文到底在解决什么问题？
2. 核心方法脉络是什么？
3. 真正的新意有哪些？给 3 条。
4. 实验设置、关键指标和主要结论是什么？
5. 哪些地方最可能是方法边界、实验短板或复现风险？给 3 条。
6. 它与我的研究兴趣有什么关系？
7. 最后给出一个结论：值不值得我进一步精读/复现，为什么？

要求：
- 只有在 PDF 明确给出证据时，才引用数字、表格、公式或模块细节。
- 如果某个信息在 PDF 中不明确，请直接写“不确定”。
- 结尾补一个“下一步阅读建议”，告诉我最该看论文里的哪几个章节、图表或实验。
"""


def build_chatgpt_follow_up(paper_info):
    """Create a manual follow-up block for deeper reading in ChatGPT Web."""
    pdf_url = f"https://arxiv.org/pdf/{paper_info['id']}"
    prompt = build_chatgpt_prompt(paper_info)

    return f"""### 💡 {paper_info['title']} [[PDF]]({pdf_url}) [[ChatGPT]]({CHATGPT_WEB_URL})
> **适合何时点开**: 如果你需要确认方法细节、实验数字、公式推导或复现难度，打开 ChatGPT 后上传 PDF，再粘贴下面的 prompt。

* **Authors**: {paper_info['authors']}
* **Abstract Link**: {paper_info['url']}

```text
{prompt}
```

---
"""


# ================= Phase 4: Publisher =================

def publish_report(summary, follow_ups):
    """Assemble the markdown report and persist it to disk."""
    print("\n🖨️ [Publisher] Assembling final report...")

    date_str = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    final_content = f"{summary}\n\n"
    if follow_ups:
        final_content += "# 🧭 ChatGPT Follow-up Pack\n\n"
        final_content += "\n\n".join(follow_ups)
    else:
        final_content += "*(今日没有需要进一步精读的论文)*\n"

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

    summary_md, selected_ids = editor_screening(papers)
    if not summary_md:
        return GENERAL_FAILURE_EXIT_CODE

    follow_ups = []
    paper_map = {normalize_paper_id(paper["id"]): paper for paper in papers}

    for selected_id in selected_ids:
        target_paper = paper_map.get(normalize_paper_id(selected_id))
        if not target_paper:
            print(f"⚠️ [Warning] Cannot find corresponding paper info for ID: {selected_id}")
            continue
        follow_ups.append(build_chatgpt_follow_up(target_paper))

    publish_report(summary_md, follow_ups)
    return 0


if __name__ == "__main__":
    sys.exit(main())
