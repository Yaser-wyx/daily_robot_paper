import os
import re
import json
import time
import requests
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup

# ================= ⚙️ Configuration =================

# 1. Target URL (Arxiv New Submissions)
ARXIV_URL = "https://arxiv.org/list/cs.RO/new"

# 2. Gemini model definitions
# Use gemini-3-pro-preview for global screening, gemini-2.5-pro for individual deep dives.
MODEL_GLOBAL = "gemini-3-pro-preview"
MODEL_LOCAL = "gemini-2.5-pro"

# 3. Research interests and keywords
INTERESTS = "VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model"

# 4. VIP authors list
VIP_AUTHORS = [
    "Sergey Levine", "Chelsea Finn", "Pieter Abbeel", "Dorsa Sadigh",
    "Huazhe Xu", "Cewu Lu", "Xiaolong Wang", "Hao Su",
    "Jiangmiao Pang", "He Wang", "Shuran Song", "Donglin Wang", "Yue Wang"
]

# 5. Output directories
OUTPUT_DIR = "./reports"


# ================= 🕵️ Phase 1: The Harvester =================

def fetch_arxiv_papers():
    """Fetch and parse structured data from arXiv new submissions."""
    print(f"🌐 [Harvester] Fetching from: {ARXIV_URL} ...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(ARXIV_URL, headers=headers, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ [Error] Network request failed: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Verify if the listings are for today to prevent outdated pulls
    today = datetime.now()
    expected_date_str = f"{today.day} {today.strftime('%B %Y')}"

    date_header = soup.find('h3', string=re.compile(r'Showing new listings for', re.IGNORECASE))
    if date_header:
        page_date_str = date_header.text.strip()

        # Block and prompt if dates mismatch (handling arXiv timezone differences)
        if expected_date_str not in page_date_str:
            print(f"\n⚠️ [Warning] Date mismatch detected between arXiv list and local time.")
            print(f"    > Webpage shows: {page_date_str}")
            print(f"    > Local expects: {expected_date_str}")

            choice = input("❓ Continue fetching and generating the report? [y/N]: ").strip().lower()
            if choice not in ['y', 'yes']:
                print("🛑 [Aborted] Task cancelled by user.")
                return []
            print("▶️ [Continue] Confirmed by user, proceeding...\n")
    else:
        print("⚠️ [Warning] No explicit date identifier found on the page. Proceeding anyway.")

    dt_tags = soup.find_all('dt')
    dd_tags = soup.find_all('dd')

    papers = []
    print(f"📥 [Harvester] Found {len(dt_tags)} papers, starting to parse...")

    for dt, dd in zip(dt_tags, dd_tags):
        id_tag = dt.find('a', title='Abstract')
        if not id_tag:
            continue

        paper_id = id_tag.text.strip().replace("arXiv:", "")
        url = f"https://arxiv.org/abs/{paper_id}"

        title_div = dd.find('div', class_='list-title')
        if not title_div:
            print(f"  ⚠️ [Warning] Missing title for ID {paper_id}, skipping.")
            continue
        title = title_div.text.replace('Title:', '').strip()

        authors_div = dd.find('div', class_='list-authors')
        authors = authors_div.text.replace('Authors:', '').strip().replace('\n', ' ') if authors_div else "Unknown"

        abstract_p = dd.find('p', class_='mathjax')
        if abstract_p:
            abstract = abstract_p.text.strip().replace('\n', ' ')
            print(f"  ✅ [Info] Successfully parsed abstract: {paper_id}")
        else:
            abstract = "Abstract not available."
            print(f"  ⚠️ [Warning] Missing abstract for ID {paper_id}.")

        papers.append({
            "id": paper_id,
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "url": url
        })

    print(f"✅ [Harvester] Successfully extracted {len(papers)} papers.")
    return papers


# ================= 🧠 Helper: Gemini Invocation =================

def call_gemini(prompt, model, max_retries=3, retry_delay=5):
    """Invoke local gemini-cli with explicitly specified model and a retry mechanism."""
    for attempt in range(max_retries):
        try:
            result = subprocess.run(
                ['gemini', '-m', model, '-p', prompt],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            if result.returncode != 0:
                # Extract the last substantive line of the error for cleaner logging
                error_msg = result.stderr.strip().split('\n')[-1] if result.stderr else "Unknown error"
                print(f"  ⚠️ [Retry {attempt + 1}/{max_retries}] Gemini CLI failed: {error_msg}")

                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                return None

            return result.stdout.strip()

        except Exception as e:
            print(f"  ❌ [Retry {attempt + 1}/{max_retries}] Exception calling Gemini CLI: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return None

    return None


def clean_json_string(text):
    """Sanitize LLM output to extract raw JSON block, ignoring markdown wrappers."""
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return match.group(0)
    return text


# ================= 👨‍🏫 Phase 2: The Editor-in-Chief =================

def editor_screening(papers):
    """Generate briefing and select papers based on abstracts using the global model."""
    print(f"\n🧐 [Editor] Reading paper list and drafting briefing using {MODEL_GLOBAL}...")

    papers_context = ""
    for p in papers:
        is_vip = any(vip in p['authors'] for vip in VIP_AUTHORS)
        prefix = "★ [VIP AUTHOR] " if is_vip else ""
        papers_context += f"ID: {p['id']}\nTitle: {prefix}{p['title']}\nAuthors: {p['authors']}\nAbstract: {p['abstract'][:300]}...\n\n"

    today_str = datetime.now().strftime("%Y-%m-%d %A")

    prompt = f"""
你是一个机器人学领域的顶级学术编辑，正在为专业研究人员撰写一份学术简报。
我的研究兴趣主要集中在: {INTERESTS}。
请注意：今天是 {today_str}。

CONTEXT: System retrieved {len(papers)} papers from arXiv today.

**任务要求：**
1. **筛选与推荐**：快速阅读上述论文信息，挑选出符合我研究方向的论文。
2. **重点关注作者**：重点关注包含以下作者的论文：
   {", ".join(VIP_AUTHORS)}.
3. **Markdown 内容生成**：请撰写简报内容（Markdown格式），参考结构：
   - 开头问候与整体趋势概述。
   - **重点关注：名校/名家实验室新作**。
   - **具身智能与世界模型高价值论文**。
   - 对于每篇入选论文，按以下格式输出：
     ### [序号]. 论文标题
     * **Title**: 英文原标题
     * **摘要介绍**: 中文介绍，约 100-150 字，直击痛点和贡献。
     * **关键词**: 3-5 个英文关键词。
4. **输出格式**：仅输出一个合法 JSON 对象，严禁代码块包裹。结构：
{{
  "title": "RoboPulse 简报",
  "summary_content": "生成的 Markdown 内容，请确保所有数学符号严格按照 LaTeX 标准（使用 $ 和 $$）包裹。",
  "selected_ids": ["ID1", "ID2"] // ⚠️ 必须严格包含你在 summary_content 中介绍的所有论文的 ID，绝不能遗漏！
}}

{papers_context}
"""

    response = call_gemini(prompt, MODEL_GLOBAL)
    if not response:
        return None, []

    try:
        data = json.loads(clean_json_string(response))
        selected_ids = data.get("selected_ids", [])
        print(f"✅ [Editor] Screening complete. Selected {len(selected_ids)} papers.")
        return data.get("summary_content", ""), selected_ids
    except json.JSONDecodeError as e:
        print(f"❌ [Error] JSON parsing failed: {e}")
        return response, []


# ================= 🔬 Phase 3: The Researchers =================

def extract_text_from_pdf(pdf_path):
    """Fallback method: Extract pure text from an oversized PDF to bypass API limits."""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
        return text
    except ImportError:
        print("      ⚠️ [Error] PyMuPDF (fitz) is not installed. Run `pip install PyMuPDF`.")
        return None
    except Exception as e:
        print(f"      ⚠️ [Error] Failed to extract text from PDF: {e}")
        return None


def researcher_deep_dive(paper_info):
    """Deep dive by downloading the PDF locally. Auto-falls back to pure text if >20MB."""
    print(f"    🔍 [Researcher] Deep diving into {paper_info['title'][:40]}... via {MODEL_LOCAL}")

    pdf_url = f"https://arxiv.org/pdf/{paper_info['id']}"
    clean_id = paper_info['id'].replace('.', '_').replace('/', '_')
    local_pdf_path = f".temp_paper_{clean_id}.pdf"
    local_txt_path = f".temp_paper_{clean_id}.txt"

    # 20MB size limit for Gemini inline file parsing
    MAX_FILE_SIZE_BYTES = 20 * 1024 * 1024

    # 1. Download the PDF locally via Python
    print(f"      ⬇️ Downloading PDF to local storage...")
    try:
        # Use an ArXiv mirror if standard download fails often: e.g., "http://xxx.itp.ac.cn/pdf/{paper_info['id']}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(f"{pdf_url}.pdf", headers=headers, stream=True, timeout=30)
        response.raise_for_status()

        with open(local_pdf_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    except Exception as e:
        print(f"      ❌ Failed to download PDF: {e}")
        return f"### 💡 {paper_info['title']} [[PDF]]({pdf_url})\n> ⚠️ *该论文深度拆解失败，网络连接断开或被 ArXiv 阻断。*\n\n---\n"

    # 2. Check file size and determine the injection strategy
    file_size = os.path.getsize(local_pdf_path)
    injection_file = local_pdf_path

    if file_size > MAX_FILE_SIZE_BYTES:
        print(
            f"      ⚠️ [Fallback] PDF size ({file_size / (1024 * 1024):.1f}MB) exceeds 20MB limit. Extracting pure text...")
        extracted_text = extract_text_from_pdf(local_pdf_path)

        if extracted_text:
            with open(local_txt_path, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            injection_file = local_txt_path
        else:
            # If text extraction also fails, we must skip to prevent API crash
            os.remove(local_pdf_path)
            return f"### 💡 {paper_info['title']} [[PDF]]({pdf_url})\n> ⚠️ *该论文体积超限 ({file_size / (1024 * 1024):.1f}MB) 且纯文本提取失败，已主动跳过。*\n\n---\n"

    # 3. Use gemini-cli's native @file attachment syntax
    prompt = f"""
@./{injection_file}

Based on the attached document above, you are a senior algorithm researcher. Please perform a deep dive analysis of the paper "{paper_info['title']}".

⚠️ 【Anti-Hallucination Guardrail】:
If you cannot read the attached document, or if the content is completely corrupted, DO NOT hallucinate or guess the details! You must ONLY output the exact word: FETCH_FAILED.

如果你成功读取到了全文，请充分利用原文中的描述和数据，严格按以下 Markdown 格式输出拆解报告。
- 所有的数学公式、变量名必须使用标准 LaTeX 格式。行内公式严禁包含两端空格并使用 $ 包裹，独立公式使用 $$ 包裹。绝对不要使用 \\( 或 \\[。

### 💡 {paper_info['title']} [[PDF]]({pdf_url})
> **一句话总结**: 用粗体写一句话，直击痛点和贡献。

#### 📖 背景与动机 (Background & Motivation)
简述该工作解决了什么长期存在的问题？现有方法有什么局限性？

#### ⚙️ 核心方法 (Core Methodology)
详细描述提出的算法或架构。结合论文说明创新点在哪里？（提取底层的架构设计细节，必须参考论文的数学推导）

#### 📊 实验与结果 (Experiments & Results)
- **实验设置**：具体的 Task 和 Benchmark 是什么？
- **关键指标**：相比 SOTA 提升了多少？（请直接从论文的文字或表格描述中提取具体数字）
- **消融实验**：论文中证明了哪个模块对性能贡献最大？

#### 💭 结论与启发 (Conclusion & Takeaways)
该工作的核心价值是什么？对未来的研究有什么启发？

#### 🏷️ 核心标签
`Methodology Tag` `Application Tag`
---
"""

    try:
        report = call_gemini(prompt, MODEL_LOCAL)
    finally:
        # 4. Cleanup all temporary files (both PDF and TXT if it exists)
        if os.path.exists(local_pdf_path):
            os.remove(local_pdf_path)
        if os.path.exists(local_txt_path):
            os.remove(local_txt_path)

    return report


# ================= 🖨️ Phase 4: The Publisher =================

def publish_report(summary, deep_dives):
    """Assemble raw text and write directly to file. Bypassing LLM to prevent data loss."""
    print("\n🖨️ [Publisher] Assembling final report (Bypassing LLM polish to ensure data integrity)...")

    date_str = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Directly concatenate the verified markdown strings
    final_content = f"{summary}\n\n"
    if deep_dives:
        final_content += "# 📚 Selected Papers Deep Dive (深度拆解)\n\n"
        final_content += "\n\n".join(deep_dives)
    else:
        final_content += "\n*(今日无重点论文深度拆解)*"

    filename = os.path.join(OUTPUT_DIR, f"{date_str}-RoboPulse.md")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"🎉 [Done] Report generated successfully: {filename}")
    return filename


# ================= 🚀 Main Execution =================

def main():
    """Main application loop."""
    papers = fetch_arxiv_papers()
    if not papers:
        return

    summary_md, selected_ids = editor_screening(papers)
    if not summary_md:
        return

    deep_dive_reports = []
    paper_map = {p['id']: p for p in papers}

    for pid in selected_ids:
        # Strip versioning tags like 'v1', 'v2' from arXiv IDs
        clean_pid = pid.split('v')[0]
        target_paper = next((paper_map[k] for k in paper_map if clean_pid in k), None)

        if target_paper:
            report = researcher_deep_dive(target_paper)

            # Strict validation to block hallucinations or CLI failures
            if report and "FETCH_FAILED" not in report:
                deep_dive_reports.append(report)
            else:
                # Fallback to prevent silent failure if the PDF parse fails or times out
                pdf_url = f"https://arxiv.org/pdf/{target_paper['id']}"
                deep_dive_reports.append(
                    f"### 💡 {target_paper['title']} [[PDF]]({pdf_url})\n> ⚠️ *该论文深度拆解失败，可能是本地 PDF 挂载失败，已拦截大模型的幻觉输出。*\n\n---\n"
                )

            # Respect API rate limits
            time.sleep(2)
        else:
            print(f"⚠️ [Warning] Cannot find corresponding paper info for ID: {pid}")

    publish_report(summary_md, deep_dive_reports)


if __name__ == "__main__":
    main()