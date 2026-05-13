from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path
import hashlib
import re


MODERN_PICK_SECTION = "Editor's Picks"
MODERN_WATCHLIST_SECTION = "Watchlist"
REDISCOVERY_SECTION = "Historical Rediscovery"


@dataclass(frozen=True)
class PaperRecord:
    """A paper-like item parsed from a report markdown file."""

    id: str
    paper_id: str
    title: str
    date: str
    section: str
    authors: str
    summary: str
    keywords: list[str]
    report_id: str
    report_url: str
    html_url: str
    pdf_url: str
    source_file: str
    source_kind: str

    def to_search_item(self):
        """Return a JSON-serializable search-index row."""
        item = asdict(self)
        item["search_text"] = normalize_search_text(
            " ".join(
                [
                    self.paper_id,
                    self.title,
                    self.authors,
                    self.summary,
                    " ".join(self.keywords),
                    self.date,
                    self.section,
                ]
            )
        )
        return item


def report_date_from_filename(filename):
    """Extract a report date from the standard report filename."""
    match = re.match(r"^(\d{4}-\d{2}-\d{2})-RoboPulse(?:\.md)?$", filename)
    return match.group(1) if match else ""


def normalize_paper_id(raw_id):
    """Normalize arXiv IDs across plain IDs, URLs, PDFs, and version suffixes."""
    paper_id = (raw_id or "").strip().strip("`")
    paper_id = paper_id.replace("arXiv:", "")
    paper_id = re.sub(r"^https?://arxiv\.org/(abs|pdf)/", "", paper_id)
    paper_id = re.sub(r"\.pdf$", "", paper_id)
    paper_id = re.sub(r"[?#].*$", "", paper_id)
    paper_id = re.sub(r"v\d+$", "", paper_id)
    return paper_id.strip()


def normalize_whitespace(text):
    """Collapse whitespace for parser output and search text."""
    return re.sub(r"\s+", " ", (text or "")).strip()


def normalize_title_key(title):
    """Build a stable dedupe key for fallback legacy titles."""
    lowered = clean_title(title).lower()
    lowered = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", lowered)
    return normalize_whitespace(lowered)


def normalize_search_text(text):
    """Normalize text used by the browser-side search implementation."""
    return normalize_whitespace(text).lower()


def clean_title(title):
    """Remove RoboPulse resource badge tokens from a paper title."""
    title = re.sub(r"\[\[(?:HTML|PDF|ChatGPT)\]\]\(https?://[^\)]+\)", "", title or "")
    title = re.sub(r"\[\[VIP\]\]", "", title)
    return normalize_whitespace(title)


def extract_resource_links(text):
    """Extract first HTML/PDF badge links from a markdown fragment."""
    html_match = re.search(r"\[\[HTML\]\]\((https?://[^\)]+)\)", text or "")
    pdf_match = re.search(r"\[\[PDF\]\]\((https?://[^\)]+)\)", text or "")
    if not pdf_match:
        pdf_match = re.search(r"https?://arxiv\.org/pdf/[^\s\)]+", text or "")
    return (
        html_match.group(1) if html_match else "",
        pdf_match.group(1) if pdf_match else "",
    )


def get_section(markdown_text, section_title):
    """Return the body of an exact level-2 markdown section."""
    match = re.search(rf"^## {re.escape(section_title)}\s*$", markdown_text, re.MULTILINE)
    if not match:
        return ""
    next_section = re.search(r"^##\s+", markdown_text[match.end() :], re.MULTILINE)
    end = match.end() + next_section.start() if next_section else len(markdown_text)
    return markdown_text[match.end() : end]


def has_modern_sections(markdown_text):
    """Return True when a report uses the modern Picks/Watchlist layout."""
    return bool(get_section(markdown_text, MODERN_PICK_SECTION) and get_section(markdown_text, MODERN_WATCHLIST_SECTION))


def extract_field(block, label):
    """Extract a bold markdown metadata field from a card block."""
    match = re.search(rf"^\s*[*-]\s+\*\*{re.escape(label)}\*\*:\s*(.+)$", block or "", re.MULTILINE)
    return normalize_whitespace(match.group(1)) if match else ""


def extract_keywords(raw_keywords):
    """Parse backtick/comma separated keyword fields."""
    if not raw_keywords:
        return []
    backtick_keywords = re.findall(r"`([^`]+)`", raw_keywords)
    if backtick_keywords:
        return [normalize_whitespace(keyword) for keyword in backtick_keywords if normalize_whitespace(keyword)]
    return [
        normalize_whitespace(keyword)
        for keyword in re.split(r"[,，;；]", raw_keywords)
        if normalize_whitespace(keyword)
    ][:8]


def split_heading_cards(section_text, pattern):
    """Split markdown cards that begin with a level-3 heading."""
    matches = list(re.finditer(pattern, section_text, re.MULTILINE))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section_text)
        yield match, section_text[match.end() : end]


def parse_modern_heading_section(markdown_path, markdown_text, section_title, heading_pattern):
    """Parse modern h3 paper cards from one section."""
    issue_date = report_date_from_filename(markdown_path.name)
    report_id = markdown_path.stem
    section_text = get_section(markdown_text, section_title)
    records = []

    for heading_match, block in split_heading_cards(section_text, heading_pattern):
        raw_title = heading_match.group(1)
        paper_id = normalize_paper_id(extract_field(block, "Paper ID"))
        if not paper_id:
            continue

        heading_html_url, heading_pdf_url = extract_resource_links(raw_title)
        block_html_url, block_pdf_url = extract_resource_links(block)
        authors = extract_field(block, "Authors")
        summary = first_nonempty_field(
            block,
            [
                "一句话结论",
                "问题与切口",
                "为什么还值得留意",
                "当时可能被低估的信号",
                "为什么现在值得再看",
                "摘要介绍",
            ],
        )
        keywords = extract_keywords(extract_field(block, "关键词"))
        records.append(
            PaperRecord(
                id=paper_id,
                paper_id=paper_id,
                title=clean_title(raw_title),
                date=issue_date,
                section=section_title,
                authors=authors,
                summary=summary,
                keywords=keywords,
                report_id=report_id,
                report_url=f"reports/{report_id}/",
                html_url=heading_html_url or block_html_url,
                pdf_url=heading_pdf_url or block_pdf_url,
                source_file=str(markdown_path),
                source_kind="modern",
            )
        )

    return records


def first_nonempty_field(block, labels):
    """Return the first non-empty metadata field for a block."""
    for label in labels:
        value = extract_field(block, label)
        if value:
            return value
    return ""


def parse_rediscovery_section(markdown_path, markdown_text):
    """Parse Historical Rediscovery bullet records."""
    issue_date = report_date_from_filename(markdown_path.name)
    report_id = markdown_path.stem
    section_text = get_section(markdown_text, REDISCOVERY_SECTION)
    if not section_text:
        return []

    records = []
    matches = list(re.finditer(r"^- \*\*Paper\*\*:\s*(.+)$", section_text, re.MULTILINE))
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(section_text)
        block = section_text[match.end() : block_end]
        paper_id = normalize_paper_id(extract_field(block, "Paper ID"))
        if not paper_id:
            continue
        raw_title = match.group(1)
        heading_html_url, heading_pdf_url = extract_resource_links(raw_title)
        block_html_url, block_pdf_url = extract_resource_links(block)
        summary = first_nonempty_field(
            block,
            [
                "为什么现在值得再看",
                "当时可能被低估的信号",
                "建议动作",
            ],
        )
        keywords = extract_keywords(extract_field(block, "关键词"))
        records.append(
            PaperRecord(
                id=paper_id,
                paper_id=paper_id,
                title=clean_title(raw_title),
                date=issue_date,
                section=REDISCOVERY_SECTION,
                authors="",
                summary=summary,
                keywords=keywords,
                report_id=report_id,
                report_url=f"reports/{report_id}/",
                html_url=heading_html_url or block_html_url,
                pdf_url=heading_pdf_url or block_pdf_url,
                source_file=str(markdown_path),
                source_kind="modern",
            )
        )
    return records


def parse_modern_report(markdown_path):
    """Parse all modern paper sections used by search and rediscovery."""
    markdown_text = Path(markdown_path).read_text(encoding="utf-8")
    records = []
    records.extend(
        parse_modern_heading_section(
            Path(markdown_path),
            markdown_text,
            MODERN_PICK_SECTION,
            r"^### \[\d+\]\.\s*(.+)$",
        )
    )
    records.extend(
        parse_modern_heading_section(
            Path(markdown_path),
            markdown_text,
            MODERN_WATCHLIST_SECTION,
            r"^### \[W\d+\]\.\s*(.+)$",
        )
    )
    records.extend(parse_rediscovery_section(Path(markdown_path), markdown_text))
    return records


def parse_legacy_report_for_search(markdown_path):
    """Best-effort legacy parser used only for search-index coverage."""
    markdown_path = Path(markdown_path)
    markdown_text = markdown_path.read_text(encoding="utf-8")
    issue_date = report_date_from_filename(markdown_path.name)
    report_id = markdown_path.stem
    records_by_key = {}

    matches = list(re.finditer(r"^###\s+(?:\[[0-9]+\]\.\s*|[0-9]+\.\s*)?(.+)$", markdown_text, re.MULTILINE))
    for index, match in enumerate(matches):
        raw_title = normalize_whitespace(match.group(1))
        if should_skip_legacy_heading(raw_title):
            continue

        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown_text)
        block = markdown_text[match.end() : block_end]
        explicit_title = extract_field(block, "Title")
        title = clean_title(explicit_title or raw_title)
        title_key = normalize_title_key(title)
        if not title_key:
            continue

        html_url, pdf_url = extract_resource_links(raw_title + "\n" + block)
        summary = first_nonempty_field(block, ["摘要介绍", "一句话总结"])
        keywords = extract_keywords(extract_field(block, "关键词"))
        fallback_id = f"legacy:{issue_date}:{hashlib.sha1(title_key.encode('utf-8')).hexdigest()[:12]}"
        record = PaperRecord(
            id=fallback_id,
            paper_id="",
            title=title,
            date=issue_date,
            section="Legacy Report",
            authors="",
            summary=summary,
            keywords=keywords,
            report_id=report_id,
            report_url=f"reports/{report_id}/",
            html_url=html_url,
            pdf_url=pdf_url,
            source_file=str(markdown_path),
            source_kind="legacy",
        )
        existing = records_by_key.get(title_key)
        if existing is None or legacy_record_score(record) > legacy_record_score(existing):
            records_by_key[title_key] = record

    return list(records_by_key.values())


def should_skip_legacy_heading(title):
    """Filter non-paper or duplicate deep-dive headings in legacy reports."""
    cleaned = normalize_whitespace(title)
    if not cleaned:
        return True
    if cleaned.startswith("💡"):
        return True
    lowered = cleaned.lower()
    if "selected papers deep dive" in lowered:
        return True
    if "chatgpt deep read prompt" in lowered:
        return True
    return False


def legacy_record_score(record):
    """Prefer richer legacy rows when deduping same-date same-title items."""
    score = 0
    if record.summary:
        score += 2
    if record.keywords:
        score += 1
    if record.pdf_url:
        score += 2
    if record.html_url:
        score += 1
    return score


def iter_report_paths(report_dir):
    """Yield markdown report paths sorted by filename."""
    return sorted(Path(report_dir).glob("*.md"))


def parse_report_for_search(markdown_path):
    """Parse one report into search-index records."""
    markdown_path = Path(markdown_path)
    markdown_text = markdown_path.read_text(encoding="utf-8")
    if has_modern_sections(markdown_text):
        return parse_modern_report(markdown_path)
    return parse_legacy_report_for_search(markdown_path)


def build_search_index(report_dir):
    """Build a browser-searchable index from all reports."""
    records = []
    for markdown_path in iter_report_paths(report_dir):
        records.extend(parse_report_for_search(markdown_path))
    records.sort(key=lambda record: (record.date, record.section, record.title), reverse=True)
    return [record.to_search_item() for record in records]


def collect_rediscovery_candidates(report_dir, current_date=None):
    """Return modern Watchlist records not promoted or already rediscovered."""
    current_date = current_date or datetime.now().strftime("%Y-%m-%d")
    historical_records = []
    for markdown_path in iter_report_paths(report_dir):
        issue_date = report_date_from_filename(markdown_path.name)
        if issue_date == current_date:
            continue
        markdown_text = markdown_path.read_text(encoding="utf-8")
        if not has_modern_sections(markdown_text):
            historical_records.extend(parse_rediscovery_section(markdown_path, markdown_text))
            continue
        historical_records.extend(parse_modern_report(markdown_path))

    picks_by_id = {}
    rediscovered_ids = set()
    watchlist = []
    for record in historical_records:
        if record.section == MODERN_PICK_SECTION and record.paper_id:
            picks_by_id.setdefault(record.paper_id, []).append(record.date)
        elif record.section == REDISCOVERY_SECTION and record.paper_id:
            rediscovered_ids.add(record.paper_id)
        elif record.section == MODERN_WATCHLIST_SECTION and record.paper_id:
            watchlist.append(record)

    candidates_by_id = {}
    for record in watchlist:
        if record.paper_id in rediscovered_ids:
            continue
        later_pick_dates = [pick_date for pick_date in picks_by_id.get(record.paper_id, []) if pick_date > record.date]
        if later_pick_dates:
            continue
        existing = candidates_by_id.get(record.paper_id)
        if existing is None or record.date > existing.date:
            candidates_by_id[record.paper_id] = record

    candidates = list(candidates_by_id.values())
    candidates.sort(key=lambda record: (record.date, record.title), reverse=True)
    return candidates
