import os
from datetime import datetime

from robopulse.config import CHATGPT_WEB_URL, INTERESTS, OUTPUT_DIR, WATCHLIST_PREFIX
from robopulse.utils import paper_has_vip, paper_priority_label, print

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


def rediscovery_resource_tokens(detail):
    """Render resource badges for a rediscovered historical paper."""
    tokens = []
    if detail.get("html_url"):
        tokens.append(f"[[HTML]]({detail['html_url']})")
    if detail.get("pdf_url"):
        tokens.append(f"[[PDF]]({detail['pdf_url']})")
    return " ".join(tokens)


def content_source_summary(paper):
    """Describe how much paper body context was available."""
    sections = paper.get("available_sections", [])
    if sections:
        return f"{paper['content_source_label']} ({', '.join(sections)})"
    return paper["content_source_label"]


def build_report_markdown(issue_title, total_papers, screening_result, enriched_papers, analysis_result, rediscovery_result=None):
    """Assemble the markdown report body."""
    rediscovery_result = rediscovery_result or []
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

    if rediscovery_result:
        lines.extend(["", "## Historical Rediscovery", ""])
        for detail in rediscovery_result:
            resource_suffix = rediscovery_resource_tokens(detail)
            paper_line = f"- **Paper**: {detail['title']} {resource_suffix}".rstrip()
            lines.extend(
                [
                    paper_line,
                    f"  - **Paper ID**: `{detail['id']}`",
                    f"  - **来源日期**: {detail['source_date']}",
                    f"  - **当时可能被低估的信号**: {detail['missed_signal']}",
                    f"  - **为什么现在值得再看**: {detail['current_relevance']}",
                    f"  - **建议动作**: {detail['suggested_action']}",
                    "  - **关键词**: " + " ".join(f"`{keyword}`" for keyword in detail["keywords"]),
                ]
            )

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
                f"* **关键词**: " + " ".join(f"`{keyword}`" for keyword in detail["keywords"]),
                f"* **证据来源**: {content_source_summary(paper)}",
                "",
                "#### 📖 背景与动机",
                "",
                detail["background_and_motivation"],
                "",
                "#### ⚙️ 核心方法",
                "",
                detail["core_methodology"],
                "",
                "#### 📊 实验与结果",
                "",
                detail["experiments_and_results"],
                "",
                "#### ⚠️ 风险 / 保留意见",
                "",
            ]
        )
        lines.extend(f"- {point}" for point in detail["limitations_and_risks"])
        lines.extend(
            [
                "",
                "#### 💭 结论与启发",
                "",
                detail["takeaways"],
                "",
                "#### 🔎 读 PDF 先核查",
                "",
            ]
        )
        lines.extend(f"- {question}" for question in detail["priority_questions"])
        lines.extend(["", "#### 📌 上传 PDF 后优先看", ""])
        lines.extend(f"- {section}" for section in detail["section_focus"])
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


def publish_report(issue_title, total_papers, screening_result, enriched_papers, analysis_result, rediscovery_result=None):
    """Assemble the markdown report and persist it to disk."""
    print("\n🖨️ [Publisher] Assembling final report...")

    date_str = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    final_content = build_report_markdown(
        issue_title,
        total_papers,
        screening_result,
        enriched_papers,
        analysis_result,
        rediscovery_result=rediscovery_result,
    )
    filename = os.path.join(OUTPUT_DIR, f"{date_str}-RoboPulse.md")
    with open(filename, "w", encoding="utf-8") as report_file:
        report_file.write(final_content)

    print(f"🎉 [Done] Report generated successfully: {filename}")
    return filename
