import os
import re
import json
import time
import requests
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup

# ================= ⚙️ 配置区域 (Configuration) =================

# 1. 目标 URL (Arxiv New Submissions)
ARXIV_URL = "https://arxiv.org/list/cs.RO/new"

# 2. Gemini 模型名称 (建议使用 Flash 以处理长 Context，或者 Pro)
GEMINI_MODEL = "gemini-3-pro-preview"  # 或 "gemini-1.5-pro"

# 3. 研究兴趣与关键词
INTERESTS = "VLA (Vision-Language-Action), Sim2Real, RL+VLA, World Model"

# 4. 重点关注大佬列表
VIP_AUTHORS = [
    "Sergey Levine", "Chelsea Finn", "Pieter Abbeel", "Dorsa Sadigh",
    "Huazhe Xu", "Cewu Lu", "Xiaolong Wang", "Hao Su",
    "Jiangmiao Pang", "He Wang", "Shuran Song", "Donglin Wang", "Yue Wang"
]

# 5. 输出文件前缀
OUTPUT_DIR = "./reports"


# ================= 🕵️ 阶段一: 采编部 (The Harvester) =================

def fetch_arxiv_papers():
    """抓取网页并解析为结构化数据"""
    print(f"🌐 [Harvester] 正在抓取: {ARXIV_URL} ...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    try:
        response = requests.get(ARXIV_URL, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ 网络请求失败: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Arxiv List 页面结构: <dt>是ID链接, <dd>是内容
    dt_tags = soup.find_all('dt')
    dd_tags = soup.find_all('dd')

    papers = []

    print(f"📥 [Harvester] 发现 {len(dt_tags)} 篇论文，开始解析...")

    for dt, dd in zip(dt_tags, dd_tags):
        # 1. 提取 ID
        id_tag = dt.find('a', title='Abstract')
        if not id_tag: continue
        paper_id = id_tag.text.strip().replace("arXiv:", "")
        url = f"https://arxiv.org/abs/{paper_id}"

        # 2. 提取 Title
        title_div = dd.find('div', class_='list-title')
        if not title_div: continue
        title = title_div.text.replace('Title:', '').strip()

        # 3. 提取 Authors
        authors_div = dd.find('div', class_='list-authors')
        authors = authors_div.text.replace('Authors:', '').strip().replace('\n', ' ') if authors_div else "Unknown"

        # 4. 提取 Abstract (Arxiv list页面通常在 <p class='mathjax'> 中)
        abstract_p = dd.find('p', class_='mathjax')
        abstract = abstract_p.text.strip().replace('\n', ' ') if abstract_p else "Abstract not available in list view."

        papers.append({
            "id": paper_id,
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "url": url
        })

    print(f"✅ [Harvester] 成功整理 {len(papers)} 篇论文数据。")
    return papers


# ================= 🧠 辅助函数: Gemini 调用 =================

def call_gemini(prompt, model=GEMINI_MODEL):
    """调用本地 gemini-cli"""
    try:
        # 使用 subprocess 调用命令行
        result = subprocess.run(
            ['gemini', '-m', model, '-p', prompt],
            capture_output=True,
            text=True,
            encoding='utf-8'  # 防止编码问题
        )
        if result.returncode != 0:
            print(f"⚠️ Gemini CLI Error: {result.stderr}")
            return None
        return result.stdout.strip()
    except Exception as e:
        print(f"❌ 调用 Gemini 失败: {e}")
        return None


def clean_json_string(text):
    """清洗 LLM 返回的 JSON 字符串 (去除 markdown 标记)"""
    # 尝试找到第一个 { 和最后一个 }
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return match.group(0)
    return text


# ================= 👨‍🏫 阶段二: 主编部 (The Editor-in-Chief) =================

def editor_screening(papers):
    """生成简报并筛选需要精读的论文"""
    print("\n🧐 [Editor] 正在阅读论文列表并撰写简报...")

    # 构造上下文数据 (截断摘要以节省 Token)
    papers_context = ""
    for p in papers:
        # 检查是否包含 VIP 作者 (仅用于标记，LLM也会再次检查)
        is_vip = any(vip in p['authors'] for vip in VIP_AUTHORS)
        prefix = "★ [VIP AUTHOR] " if is_vip else ""
        papers_context += f"ID: {p['id']}\nTitle: {prefix}{p['title']}\nAuthors: {p['authors']}\nAbstract: {p['abstract'][:300]}...\n\n"

    today_str = datetime.now().strftime("%Y-%m-%d %A")

    # Prompt 1: 简报生成与筛选
    prompt = f"""
你是一个机器人学领域的顶级学术编辑，正在为专业研究人员撰写一份 Notion 风格的“RoboPulse 机器人学学术脉动”简报。
我的研究兴趣主要集中在: {INTERESTS}。
请注意：今天是 {today_str}。

CONTEXT: System retrieved {len(papers)} papers from arXiv today.

**输入数据**（最新的论文列表）：
{papers_context}

**任务要求：**
1. **筛选与推荐**：请快速阅读上述论文信息，挑选出符合我研究方向（VLA, Sim2Real, RL+VLA, World Model）的论文，以及你认为具备高学术价值的论文。
2. **重点关注作者**：重点关注包含以下作者的论文：
   {", ".join(VIP_AUTHORS)}.
3. **Markdown 内容生成**：请撰写简报内容（Markdown格式），参考结构：
   - 开头问候与整体趋势概述。
   - **重点关注：名校/名家实验室新作**。
   - **具身智能与世界模型高价值论文**。
   - 对于每篇入选论文，请按以下格式输出（不要添加PDF引用）：
     ### [序号]. 论文标题
     * **Title**: 英文原标题
     * **摘要介绍**: 中文介绍，约 100-150 字，直击痛点和贡献。如果是重点关注作者的作品，请在介绍中明确指出。
     * **关键词**: 3-5 个英文关键词。
   - 结尾建议。
4. **输出格式**：仅输出一个合法 JSON 对象，严禁代码块包裹。结构：
{{
  "title": "RoboPulse 简报：VLA 与 World Model 前沿",
  "summary_content": "生成的 Markdown 内容",
  "selected_ids": ["ID1", "ID2", ...]
}}
Ensure the output is valid raw JSON text. Do not wrap it in markdown code blocks.
"""

    response = call_gemini(prompt)
    if not response:
        return None, []

    try:
        cleaned_json = clean_json_string(response)
        data = json.loads(cleaned_json)
        print(f"✅ [Editor] 简报生成完毕，选中了 {len(data.get('selected_ids', []))} 篇论文进行精读。")
        return data.get("summary_content", ""), data.get("selected_ids", [])
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析失败 (LLM 输出格式错误): {e}\nRaw Output: {response[:200]}...")
        # Fallback: 如果解析失败，返回原始文本，且不选精读论文
        return response, []


# ================= 🔬 阶段三: 研究部 (The Researchers) =================

def researcher_deep_dive(paper_info):
    """对单篇论文进行深度拆解"""
    print(f"    🔍 [Researcher] 正在深度解读: {paper_info['title'][:40]}...")

    prompt = f"""
你是一个高级算法科研人员。请对论文《{paper_info['title']}》进行类似 Notion 笔记风格的深度拆解。

摘要内容：{paper_info['abstract']}

**请按照以下 Markdown 格式输出（Heading Level 使用 ### 和 ####，不要使用 # 或 ##）：**

### 💡 {paper_info['title']} (Deep Dive)
> **一句话总结**: 用粗体写一句话，直击痛点和贡献。

#### 📖 背景与动机 (Background & Motivation)
简述该工作解决了什么长期存在的问题？现有方法有什么局限性？（约 50-80 字）

#### ⚙️ 核心方法 (Core Methodology)
详细描述提出的算法或架构。使用了什么关键技术（如 Diffusion Policy, VLM, RL 等）？创新点在哪里？（请分点描述）

#### 📊 实验与结果 (Experiments & Results)
- **实验设置**：在什么环境（Sim/Real）下测试？
- **关键指标**：相比 SOTA 提升了多少？（如成功率、速度等）
- **消融实验**：哪个模块贡献最大？

#### 💭 结论与影响 (Conclusion & Impact)
该工作的核心价值是什么？对未来研究有什么启发？

#### 🏷️ 核心标签
`Methodology Tag` `Application Tag`

---
"""
    return call_gemini(prompt)


# ================= 🖨️ 阶段四: 出版部 (The Publisher) =================

def publish_report(summary, deep_dives):
    """组装并写入文件"""
    print("\n🖨️ [Publisher] 正在组装日报...")

    date_str = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = f"{OUTPUT_DIR}/{date_str}-RoboPulse.md"

    full_content = f"{summary}\n\n"

    if deep_dives:
        full_content += "# 📚 Selected Papers Deep Dive (深度拆解)\n\n"
        full_content += "---\n\n".join(deep_dives)
    else:
        full_content += "\n*(今日无重点论文深度拆解)*"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"🎉 [Done] 日报已生成: {filename}")
    return filename


# ================= 🚀 主程序 (Main) =================

def main():
    # 1. 获取数据
    papers = fetch_arxiv_papers()
    if not papers:
        print("未获取到论文，程序结束。")
        return

    # 2. 筛选与简报
    summary_md, selected_ids = editor_screening(papers)
    if not summary_md:
        print("简报生成失败，程序结束。")
        return

    # 3. 深度解读
    deep_dive_reports = []

    # 创建一个 ID 到 论文信息的映射，方便查找
    paper_map = {p['id']: p for p in papers}

    for pid in selected_ids:
        # 有时 LLM 返回的 ID 可能带有版本号 v1，需要处理
        clean_pid = pid.split('v')[0]

        # 在映射中查找 (尝试精确匹配和模糊匹配)
        target_paper = None
        for k in paper_map:
            if clean_pid in k:
                target_paper = paper_map[k]
                break

        if target_paper:
            report = researcher_deep_dive(target_paper)
            if report:
                deep_dive_reports.append(report)
            # 避免 API 速率限制，稍微 sleep 一下
            time.sleep(2)
        else:
            print(f"⚠️ Warning: 找不到 ID 为 {pid} 的论文信息。")

    # 4. 发布
    publish_report(summary_md, deep_dive_reports)


if __name__ == "__main__":
    main()