from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
import re

REPORTS_DIR = Path("reports")
STATIC_DIR = Path("static")


@dataclass(frozen=True)
class ReportRecord:
    report_id: str
    filename: str
    title: str
    issue_date: date | None
    modified_at: datetime
    featured_count: int
    watchlist_count: int
    has_vip: bool
    has_html: bool
    has_inline_prompts: bool
    preview: str
    markdown_path: Path


def clean_markdown_preview(md_content, limit=180):
    """Convert report markdown into a short text preview."""
    text = re.sub(r"\[\[[^\]]+\]\]\((https?://[^\)]+)\)", "", md_content)
    text = re.sub(r"\[\[VIP\]\]", "VIP ", text)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"[#>*`_\-\[\]]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def report_title_from_filename(filename):
    """Build a short report label from the markdown filename."""
    return filename.split("-RoboPulse")[0] if "-RoboPulse" in filename else filename


def report_date_from_filename(filename):
    """Extract a YYYY-MM-DD issue date from a report filename when available."""
    match = re.match(r"^(\d{4}-\d{2}-\d{2})-RoboPulse(?:\.md)?$", filename)
    if not match:
        return None
    return datetime.strptime(match.group(1), "%Y-%m-%d").date()


def asset_href(page_depth, rel_path):
    """Return a relative asset path for the current page depth."""
    prefix = "../" * page_depth
    return f"{prefix}{rel_path}"


def report_href(report_id):
    """Return the site-relative href for a report detail page."""
    return f"reports/{report_id}/"


def load_reports(report_dir=REPORTS_DIR):
    """Load report metadata sorted by report issue date, newest first."""
    files = sorted(Path(report_dir).glob("*.md"))
    reports = []

    for path in files:
        content = path.read_text(encoding="utf-8")
        modified_at = datetime.fromtimestamp(path.stat().st_mtime)
        issue_date = report_date_from_filename(path.name)
        featured_count = len(re.findall(r"^###\s+\[(?!W)\d+\]", content, flags=re.MULTILINE))
        watchlist_count = len(re.findall(r"^###\s+\[W\d+\]", content, flags=re.MULTILINE))
        if featured_count == 0 and watchlist_count == 0:
            featured_count = len(re.findall(r"^###\s", content, flags=re.MULTILINE))

        reports.append(
            ReportRecord(
                report_id=path.stem,
                filename=path.name,
                title=report_title_from_filename(path.name),
                issue_date=issue_date,
                modified_at=modified_at,
                featured_count=featured_count,
                watchlist_count=watchlist_count,
                has_vip="[[VIP]]" in content,
                has_html="[[HTML]](" in content,
                has_inline_prompts="ChatGPT Deep Read Prompt" in content,
                preview=clean_markdown_preview(content),
                markdown_path=path,
            )
        )

    reports.sort(
        key=lambda report: (
            report.issue_date or date.min,
            report.modified_at,
            report.filename,
        ),
        reverse=True,
    )
    return reports
