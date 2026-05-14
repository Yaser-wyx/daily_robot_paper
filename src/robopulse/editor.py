import json
import os
import re
from datetime import datetime

from robopulse.codex_client import run_codex_structured
from robopulse.config import (
    CHATGPT_WEB_URL,
    CORE_VIP_AUTHORS,
    EXTENDED_VIP_AUTHORS,
    INTERESTS,
    OUTPUT_DIR,
    SHORTLIST_TARGET,
)
from robopulse.paper_parser import collect_rediscovery_candidates
from robopulse.utils import (
    clean_json_string,
    dedupe_preserve_order,
    normalize_known_ids,
    normalize_paper_id,
    normalize_whitespace,
    paper_vip_tier,
    print,
    truncate_text,
)

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
        "background_and_motivation": {"type": "string"},
        "core_methodology": {"type": "string"},
        "experiments_and_results": {"type": "string"},
        "limitations_and_risks": {"type": "array", "items": {"type": "string"}},
        "takeaways": {"type": "string"},
        "keywords": {"type": "array", "items": {"type": "string"}},
        "priority_questions": {"type": "array", "items": {"type": "string"}},
        "section_focus": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "id",
        "one_liner",
        "background_and_motivation",
        "core_methodology",
        "experiments_and_results",
        "limitations_and_risks",
        "takeaways",
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
REDISCOVERY_PAPER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "why_revisit": {"type": "string"},
        "missed_signal": {"type": "string"},
        "current_relevance": {"type": "string"},
        "suggested_action": {"type": "string"},
        "keywords": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["id", "why_revisit", "missed_signal", "current_relevance", "suggested_action", "keywords"],
    "additionalProperties": False,
}
REDISCOVERY_SCHEMA = {
    "type": "object",
    "properties": {
        "rediscovered_papers": {"type": "array", "items": REDISCOVERY_PAPER_SCHEMA},
    },
    "required": ["rediscovered_papers"],
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
- `selected_papers`：每篇写成 3/2-3/10 风格的深度拆解，让读者不打开原文也能理解论文主线、方法、证据与边界；不要写成短卡片，也不要只重复摘要。
  - `one_liner`: 一句话总结，直接说值不值得优先看以及核心原因。
  - `background_and_motivation`: 180-320 字，解释它解决什么问题、为什么这个问题在机器人/VLA/Sim2Real/RL/world model 里重要、现有路线卡在哪里。
  - `core_methodology`: 260-460 字，串起核心模块、训练/推理流程、关键接口和相对已有方法的新意；如果只有摘要或 HTML 证据不足，必须明确写“当前摘录只能确认...”。
  - `experiments_and_results`: 180-340 字，写实验设置、benchmark/任务、对比/消融/真实机器人证据和证据边界；只有 HTML 明确给出的数字才能引用。
  - `limitations_and_risks`: 2-3 条短点，写方法边界、实验可信度、复现风险或部署风险。
  - `takeaways`: 160-280 字，写这篇对我后续选题、复现、系统设计或论文阅读的启发。
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


def fallback_deep_section(paper, section_name, context_labels, caveat, limit):
    """Build a conservative deep-dive fallback from captured HTML snippets."""
    for label in context_labels:
        snippet = extract_context_snippet(paper, label)
        if snippet:
            return f"{caveat} 可用摘录线索（{label}）：{truncate_text(snippet, limit)}"

    abstract = truncate_text(paper.get("abstract", ""), limit)
    if abstract:
        return f"{caveat} 摘要线索：{abstract}"
    return f"{caveat} 当前没有足够文本证据展开“{section_name}”。"


def sanitize_selected_detail(raw_detail, paper):
    """Normalize and backfill a selected paper deep-dive."""
    background = normalize_whitespace(raw_detail.get("background_and_motivation", ""))
    if not background:
        background = normalize_whitespace(raw_detail.get("what_it_does", ""))

    methodology = normalize_whitespace(raw_detail.get("core_methodology", ""))
    if not methodology:
        methodology = normalize_whitespace(raw_detail.get("method_and_evidence", ""))

    experiments = normalize_whitespace(raw_detail.get("experiments_and_results", ""))
    takeaways = normalize_whitespace(raw_detail.get("takeaways", ""))
    limitations = [
        normalize_whitespace(item)
        for item in raw_detail.get("limitations_and_risks", raw_detail.get("risks", []))
        if normalize_whitespace(item)
    ]
    keywords = [normalize_whitespace(item) for item in raw_detail.get("keywords", []) if normalize_whitespace(item)]
    priority_questions = [
        normalize_whitespace(item) for item in raw_detail.get("priority_questions", []) if normalize_whitespace(item)
    ]
    section_focus = [normalize_whitespace(item) for item in raw_detail.get("section_focus", []) if normalize_whitespace(item)]

    if not background:
        background = fallback_deep_section(
            paper,
            "背景与动机",
            ["Introduction", "Abstract"],
            "当前 HTML 摘录没有提供完整背景，只能从摘要保守判断这篇论文的问题设定。",
            360,
        )
    if not methodology:
        methodology = fallback_deep_section(
            paper,
            "核心方法",
            ["Method", "Introduction", "Abstract"],
            "当前 HTML 摘录没有提供足够方法细节，不能替代 PDF 中的模型结构、训练目标或实现说明。",
            460,
        )
    if not experiments:
        experiments = fallback_deep_section(
            paper,
            "实验与结果",
            ["Experiments", "Conclusion", "Abstract"],
            "当前 HTML 摘录没有提供完整实验细节，具体 benchmark、数字结果、消融和失败案例需要回到 PDF 核查。",
            360,
        )
    if not takeaways:
        takeaways = fallback_deep_section(
            paper,
            "结论与启发",
            ["Conclusion", "Abstract"],
            "现阶段只能把这篇论文作为与当前研究兴趣相关的候选方向；是否值得复现取决于 PDF 中的方法细节和实验可信度。",
            320,
        )
    if not limitations:
        limitations = [
            "当前日报只使用 arXiv HTML 与摘要，摘要未覆盖的数字、图表和公式需要回到 PDF 核实。",
            "如果 HTML 摘录缺少实验或消融细节，这里的判断只能作为阅读导引，不能替代完整论文证据。",
        ]
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
        "background_and_motivation": background,
        "core_methodology": methodology,
        "experiments_and_results": experiments,
        "limitations_and_risks": limitations[:3],
        "takeaways": takeaways,
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
- Current Background Read: {detail['background_and_motivation']}
- Method / Evidence Clues from arXiv HTML: {detail['core_methodology']}
- Experiment / Evidence Clues from arXiv HTML: {detail['experiments_and_results']}

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

def build_rediscovery_prompt(candidates, max_candidates=40):
    """Construct the Codex prompt for rediscovering historical Watchlist papers."""
    candidate_blocks = []
    for record in candidates[:max_candidates]:
        candidate_blocks.append(
            "\n".join(
                [
                    f"ID: {record.paper_id}",
                    f"Title: {record.title}",
                    f"Source Date: {record.date}",
                    f"Authors: {record.authors or 'Unknown'}",
                    f"HTML URL: {record.html_url or '(unavailable)'}",
                    f"PDF URL: {record.pdf_url or '(unavailable)'}",
                    f"Historical Watchlist Note: {truncate_text(record.summary, 520) or '(no note captured)'}",
                    f"Historical Keywords: {', '.join(record.keywords) if record.keywords else '(none)'}",
                ]
            )
        )

    today_str = datetime.now().strftime("%Y-%m-%d %A")
    return f"""
你是机器人学方向的资深研究编辑。现在请从历史 Watchlist 中重新发现 3-5 篇可能被低估、但仍值得我今天再看的论文。

今天是 {today_str}。
我的研究兴趣是：{INTERESTS}。

硬性约束：
1. 只能从候选列表中选择论文，`id` 必须严格使用候选列表里的 ID。
2. 不要选择只是泛泛相关的论文；优先选择与 VLA、Sim2Real、RL+VLA、World Model、World Action Model、长时程操作、真实部署评测强相关的论文。
3. 只能基于候选里提供的历史信息判断，不要捏造论文全文细节、实验数字、图表或公式。
4. 如果候选整体质量不够，可以少于 3 篇，但不要超过 5 篇。

输出要求：
- 只返回一个合法 JSON 对象，不要使用代码块。
- `missed_signal` 写当时可能被低估的具体信号。
- `current_relevance` 写为什么现在值得再看，以及它和我的研究兴趣的关系。
- `suggested_action` 只能写一个短动作，例如：`加入精读`、`快速浏览`、`继续跟踪`。

候选论文如下：

{os.linesep.join(candidate_blocks)}
"""


def sanitize_rediscovery_detail(raw_detail, record):
    """Normalize one rediscovered paper record returned by Codex."""
    keywords = [normalize_whitespace(item) for item in raw_detail.get("keywords", []) if normalize_whitespace(item)]
    if not keywords:
        keywords = record.keywords or ["robotics"]
    return {
        "id": record.paper_id,
        "title": record.title,
        "source_date": record.date,
        "html_url": record.html_url,
        "pdf_url": record.pdf_url,
        "why_revisit": normalize_whitespace(raw_detail.get("why_revisit", ""))
        or "这篇历史 Watchlist 论文与当前研究兴趣仍然相关，值得重新快速判断。",
        "missed_signal": normalize_whitespace(raw_detail.get("missed_signal", ""))
        or "当时只进入 Watchlist，可能没有被充分精读。",
        "current_relevance": normalize_whitespace(raw_detail.get("current_relevance", ""))
        or "需要结合当前 VLA、Sim2Real 或 World Model 主线重新评估。",
        "suggested_action": normalize_whitespace(raw_detail.get("suggested_action", "")) or "快速浏览",
        "keywords": keywords[:5],
    }


def historical_rediscovery(current_date=None):
    """Use Codex to pick historical Watchlist papers worth revisiting."""
    current_date = current_date or datetime.now().strftime("%Y-%m-%d")
    candidates = collect_rediscovery_candidates(OUTPUT_DIR, current_date=current_date)
    if not candidates:
        print("ℹ️ [Rediscovery] No historical Watchlist candidates available.")
        return []

    print(f"\n🔁 [Rediscovery] Reviewing {len(candidates)} historical Watchlist candidates...")
    response = run_codex_structured(
        build_rediscovery_prompt(candidates),
        REDISCOVERY_SCHEMA,
        "Rediscovering overlooked historical Watchlist papers",
    )
    if not response:
        print("⚠️ [Rediscovery] Codex rediscovery failed. Continuing without the section.")
        return []

    try:
        data = json.loads(clean_json_string(response))
    except json.JSONDecodeError as exc:
        print(f"⚠️ [Rediscovery] JSON parsing failed: {exc}. Continuing without the section.")
        return []

    candidate_map = {record.paper_id: record for record in candidates}
    rediscovered = []
    for raw_detail in data.get("rediscovered_papers", []):
        paper_id = normalize_paper_id(str(raw_detail.get("id", "")))
        record = candidate_map.get(paper_id)
        if not record:
            continue
        if any(item["id"] == paper_id for item in rediscovered):
            continue
        rediscovered.append(sanitize_rediscovery_detail(raw_detail, record))
        if len(rediscovered) == 5:
            break

    print(f"✅ [Rediscovery] Selected {len(rediscovered)} historical papers for rediscovery.")
    return rediscovered
