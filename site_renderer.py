from dataclasses import dataclass
from datetime import date, datetime
from html import escape
from pathlib import Path
import re

import markdown
from bs4 import BeautifulSoup

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


def build_badge(label, css_class, href, icon_path):
    """Render a reusable linked badge."""
    return (
        f'<a href="{href}" target="_blank" rel="noopener noreferrer" class="resource-badge {css_class}">'
        '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">'
        f"{icon_path}"
        "</svg>"
        f"{label}</a>"
    )


def build_static_badge(label, css_class, icon_path):
    """Render a non-link badge."""
    return (
        f'<span class="resource-badge {css_class}">'
        '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">'
        f"{icon_path}"
        "</svg>"
        f"{label}</span>"
    )


def decorate_report_structure(soup):
    """Wrap paper sections and add classes for the richer report layout."""
    for h2 in soup.find_all("h2"):
        heading = h2.get_text(" ", strip=True).lower()
        classes = h2.get("class", [])
        classes.append("section-heading")
        if "editor" in heading and "pick" in heading:
            classes.append("picks-heading")
        elif "watchlist" in heading:
            classes.append("watchlist-heading")
        h2["class"] = classes

    for h4 in soup.find_all("h4"):
        heading = h4.get_text(" ", strip=True).lower()
        if "prompt" in heading:
            h4["class"] = h4.get("class", []) + ["prompt-heading"]

    for h3 in list(soup.find_all("h3")):
        heading_text = h3.get_text(" ", strip=True)
        card_class = "paper-card watch-card" if heading_text.startswith("[W") else "paper-card pick-card"
        wrapper = soup.new_tag("section", attrs={"class": card_class})
        h3.insert_before(wrapper)
        wrapper.append(h3.extract())

        sibling = wrapper.next_sibling
        while sibling:
            next_sibling = sibling.next_sibling
            sibling_name = getattr(sibling, "name", None)
            if sibling_name in {"h2", "h3"}:
                break
            if sibling_name is None and not str(sibling).strip():
                sibling.extract()
            else:
                wrapper.append(sibling.extract())
            sibling = next_sibling


def collapse_prompt_blocks(soup):
    """Turn long prompt sections into collapsed details panels."""
    for code_block in list(soup.find_all("div", class_="code-block")):
        heading = code_block.find_previous_sibling("h4")
        if not heading or "prompt-heading" not in heading.get("class", []):
            continue

        nodes_to_move = []
        cursor = heading.next_sibling
        while cursor and cursor != code_block:
            next_cursor = cursor.next_sibling
            nodes_to_move.append(cursor)
            cursor = next_cursor
        nodes_to_move.append(code_block)

        details = soup.new_tag("details", attrs={"class": "prompt-disclosure"})
        summary = soup.new_tag("summary", attrs={"class": "prompt-summary"})
        summary.string = heading.get_text(" ", strip=True)
        body = soup.new_tag("div", attrs={"class": "prompt-body"})

        heading.replace_with(details)
        details.append(summary)
        details.append(body)

        for node in nodes_to_move:
            body.append(node.extract())


def render_markdown_body(md_content, page_depth):
    """Convert markdown into enhanced report HTML."""
    _ = page_depth
    vip_badge_html = build_static_badge(
        "VIP",
        "vip-badge",
        '<path d="m12 2.5 2.95 6.08 6.71.98-4.86 4.76 1.15 6.68L12 17.77 6.05 21l1.15-6.68L2.34 9.56l6.71-.98z"></path>',
    )
    html_badge_html = build_badge(
        "HTML",
        "html-badge",
        r"\1",
        '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18"></path><path d="M12 3a15.3 15.3 0 0 1 0 18"></path><path d="M12 3a15.3 15.3 0 0 0 0 18"></path>',
    )
    pdf_badge_html = build_badge(
        "PDF",
        "pdf-badge",
        r"\1",
        '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>'
        '<polyline points="14 2 14 8 20 8"></polyline>',
    )
    chatgpt_badge_html = build_badge(
        "ChatGPT",
        "chatgpt-badge",
        r"\1",
        '<path d="M12 3.5a3.5 3.5 0 0 1 3.25 2.2A3.5 3.5 0 0 1 18.5 9a3.5 3.5 0 0 1-1 2.45 3.5 3.5 0 0 1-1.1 5.68A3.5 3.5 0 0 1 12 20.5a3.5 3.5 0 0 1-4.4-3.37 3.5 3.5 0 0 1-1.1-5.68A3.5 3.5 0 0 1 5.5 9a3.5 3.5 0 0 1 3.25-3.3A3.5 3.5 0 0 1 12 3.5z"></path>'
        '<path d="M9.2 7.3 12 5.8l2.8 1.5v3.2L12 12l-2.8-1.5z"></path>'
        '<path d="M9.2 16.7 12 18.2l2.8-1.5"></path>',
    )

    md_content = re.sub(r"\[\[VIP\]\]", vip_badge_html, md_content)
    md_content = re.sub(r"\[\[HTML\]\]\((https?://[^\)]+)\)", html_badge_html, md_content)
    md_content = re.sub(r"\[\[PDF\]\]\((https?://[^\)]+)\)", pdf_badge_html, md_content)
    md_content = re.sub(r"\[\[ChatGPT\]\]\((https?://[^\)]+)\)", chatgpt_badge_html, md_content)

    html_body = markdown.markdown(md_content, extensions=["fenced_code", "tables"])
    soup = BeautifulSoup(html_body, "html.parser")

    for pre in soup.find_all("pre"):
        wrapper = soup.new_tag("div", attrs={"class": "code-block"})
        toolbar = soup.new_tag("div", attrs={"class": "code-toolbar"})

        label = soup.new_tag("span", attrs={"class": "code-label"})
        label.string = "Deep Read Prompt"

        button = soup.new_tag("button", attrs={"class": "copy-button", "type": "button"})
        button.string = "Copy Prompt"

        toolbar.append(label)
        toolbar.append(button)
        pre.wrap(wrapper)
        wrapper.insert(0, toolbar)

    decorate_report_structure(soup)
    collapse_prompt_blocks(soup)
    return str(soup)


def render_archive_page(reports, page_depth=0):
    """Render the archive page HTML."""
    latest = reports[0] if reports else None
    cards = []
    for report in reports:
        meta_pills = [f'<span class="meta-pill">{report.featured_count} picks</span>']
        if report.watchlist_count:
            meta_pills.append(f'<span class="meta-pill meta-pill-muted">{report.watchlist_count} watchlist</span>')
        if report.has_vip:
            meta_pills.append('<span class="meta-pill vip-pill">VIP flagged</span>')
        if report.has_html:
            meta_pills.append('<span class="meta-pill meta-pill-muted">HTML enriched</span>')
        if report.has_inline_prompts:
            meta_pills.append('<span class="meta-pill meta-pill-muted">Inline prompts</span>')

        cards.append(
            f"""
            <article class="report-card">
                <a href="{escape(report_href(report.report_id))}" class="report-card-link">
                    <div class="report-card-top">
                        <span class="report-date">{escape(report.title)}</span>
                        <span class="report-updated">Updated {escape(report.modified_at.strftime("%Y-%m-%d %H:%M"))}</span>
                    </div>
                    <h2>{escape(report.filename)}</h2>
                    <p>{escape(report.preview)}</p>
                    <div class="report-meta-row">
                        {''.join(meta_pills)}
                    </div>
                </a>
            </article>
            """
        )

    latest_cta = f'<a href="{escape(report_href(latest.report_id))}" class="hero-button">Open Latest Report</a>' if latest else ""
    favicon_href = asset_href(page_depth, "static/favicon.svg")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RoboPulse Research Briefs</title>
        <link rel="icon" href="{escape(favicon_href)}" type="image/svg+xml">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg: #f4efe6;
                --panel: rgba(255, 252, 246, 0.88);
                --panel-strong: #fffdf8;
                --line: rgba(99, 78, 45, 0.14);
                --ink: #1f2933;
                --muted: #5d6b79;
                --accent: #0b6e69;
                --accent-soft: #dff2ee;
                --warm: #f6d79c;
                --shadow: 0 22px 60px rgba(62, 45, 23, 0.11);
            }}
            * {{ box-sizing: border-box; }}
            body {{
                margin: 0;
                color: var(--ink);
                background:
                    radial-gradient(circle at top left, rgba(246, 215, 156, 0.52), transparent 36%),
                    radial-gradient(circle at 85% 12%, rgba(11, 110, 105, 0.16), transparent 30%),
                    linear-gradient(180deg, #f8f3ea 0%, #f2ede4 100%);
                font-family: "Manrope", sans-serif;
            }}
            a {{ color: inherit; }}
            .shell {{
                max-width: 1180px;
                margin: 0 auto;
                padding: 40px 20px 56px;
            }}
            .hero {{
                padding: 32px;
                border: 1px solid var(--line);
                border-radius: 28px;
                background: var(--panel);
                box-shadow: var(--shadow);
                backdrop-filter: blur(12px);
                margin-bottom: 28px;
            }}
            .hero-kicker {{
                display: inline-flex;
                padding: 8px 14px;
                border-radius: 999px;
                background: var(--accent-soft);
                color: var(--accent);
                font-size: 0.82rem;
                font-weight: 700;
                letter-spacing: 0.04em;
                text-transform: uppercase;
            }}
            .hero-grid {{
                display: grid;
                grid-template-columns: minmax(0, 1.3fr) minmax(280px, 0.7fr);
                gap: 24px;
                align-items: end;
                margin-top: 18px;
            }}
            .hero h1 {{
                margin: 0 0 14px;
                font-family: "Source Serif 4", serif;
                font-size: clamp(2.4rem, 4vw, 4.4rem);
                line-height: 0.95;
                letter-spacing: -0.04em;
            }}
            .hero p {{
                margin: 0;
                max-width: 46rem;
                color: var(--muted);
                font-size: 1rem;
                line-height: 1.8;
            }}
            .hero-stats {{
                display: grid;
                gap: 12px;
            }}
            .stat-card {{
                padding: 18px 20px;
                background: var(--panel-strong);
                border: 1px solid var(--line);
                border-radius: 20px;
            }}
            .stat-label {{
                display: block;
                color: var(--muted);
                font-size: 0.78rem;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                margin-bottom: 8px;
            }}
            .stat-value {{
                font-size: 1.8rem;
                font-weight: 800;
                letter-spacing: -0.04em;
            }}
            .hero-button {{
                display: inline-flex;
                margin-top: 18px;
                align-items: center;
                justify-content: center;
                gap: 10px;
                padding: 14px 18px;
                border-radius: 16px;
                background: var(--accent);
                color: white;
                text-decoration: none;
                font-weight: 700;
                box-shadow: 0 14px 30px rgba(11, 110, 105, 0.22);
            }}
            .section-head {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 16px;
                margin: 0 0 16px;
            }}
            .section-head h2 {{
                margin: 0;
                font-size: 1.2rem;
                letter-spacing: -0.03em;
            }}
            .section-head p {{
                margin: 0;
                color: var(--muted);
                font-size: 0.92rem;
            }}
            .report-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 18px;
            }}
            .report-card {{
                border: 1px solid var(--line);
                border-radius: 24px;
                background: var(--panel);
                box-shadow: var(--shadow);
                transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
            }}
            .report-card:hover {{
                transform: translateY(-4px);
                border-color: rgba(11, 110, 105, 0.28);
                box-shadow: 0 26px 48px rgba(62, 45, 23, 0.14);
            }}
            .report-card-link {{
                display: block;
                padding: 22px;
                text-decoration: none;
            }}
            .report-card-top {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 14px;
                margin-bottom: 14px;
            }}
            .report-date {{
                font-size: 0.95rem;
                font-weight: 800;
                color: var(--accent);
            }}
            .report-updated {{
                color: var(--muted);
                font-size: 0.8rem;
            }}
            .report-card h2 {{
                margin: 0 0 12px;
                font-family: "Source Serif 4", serif;
                font-size: 1.5rem;
                line-height: 1.08;
            }}
            .report-card p {{
                margin: 0 0 16px;
                color: var(--muted);
                line-height: 1.7;
                min-height: 4.8em;
            }}
            .report-meta-row {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }}
            .meta-pill {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 8px 12px;
                border-radius: 999px;
                background: rgba(11, 110, 105, 0.08);
                color: var(--accent);
                font-size: 0.82rem;
                font-weight: 700;
            }}
            .meta-pill-muted {{
                background: rgba(99, 78, 45, 0.08);
                color: var(--muted);
            }}
            .vip-pill {{
                background: rgba(246, 215, 156, 0.42);
                color: #9a5716;
            }}
            .empty-state {{
                padding: 32px;
                border-radius: 24px;
                border: 1px dashed var(--line);
                background: rgba(255, 252, 246, 0.72);
                text-align: center;
                color: var(--muted);
            }}
            @media (max-width: 860px) {{
                .hero-grid {{
                    grid-template-columns: 1fr;
                }}
                .report-card-top {{
                    flex-direction: column;
                    align-items: flex-start;
                }}
            }}
        </style>
    </head>
    <body>
        <main class="shell">
            <section class="hero">
                <span class="hero-kicker">RoboPulse Research Desk</span>
                <div class="hero-grid">
                    <div>
                        <h1>Daily Robotics Briefing, designed for fast paper triage.</h1>
                        <p>
                            Browse each daily report as a research dashboard: richer summaries, sharper filters,
                            and a direct handoff into ChatGPT when a paper is worth a deeper read.
                        </p>
                        {latest_cta}
                    </div>
                    <div class="hero-stats">
                        <div class="stat-card">
                            <span class="stat-label">Reports</span>
                            <span class="stat-value">{len(reports)}</span>
                        </div>
                        <div class="stat-card">
                            <span class="stat-label">Latest Issue</span>
                            <span class="stat-value">{escape(latest.title) if latest else 'N/A'}</span>
                        </div>
                    </div>
                </div>
            </section>

            <section>
                <div class="section-head">
                    <div>
                        <h2>Issue Archive</h2>
                        <p>Open the latest brief or scan older issues by date and preview.</p>
                    </div>
                </div>
                <div class="report-grid">
                    {''.join(cards) if cards else '<div class="empty-state">No reports found yet. Run the generator to publish the first issue.</div>'}
                </div>
            </section>
        </main>
    </body>
    </html>
    """


def render_detail_page(report, page_depth=2):
    """Render a report detail page."""
    md_content = report.markdown_path.read_text(encoding="utf-8")
    html_body = render_markdown_body(md_content, page_depth=page_depth)
    favicon_href = asset_href(page_depth, "static/favicon.svg")
    back_href = asset_href(page_depth, "index.html")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{escape(report.filename)}</title>
        <link rel="icon" href="{escape(favicon_href)}" type="image/svg+xml">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
        <style>
            :root {{
                --page: #f5f0e7;
                --surface: rgba(255, 252, 246, 0.9);
                --surface-strong: #fffdf8;
                --line: rgba(99, 78, 45, 0.14);
                --ink: #1f2933;
                --muted: #5d6b79;
                --accent: #0b6e69;
                --accent-strong: #084e4a;
                --accent-soft: #dff2ee;
                --html: #325cb2;
                --html-soft: #e6eeff;
                --pdf: #b5474f;
                --pdf-soft: #fbe7e9;
                --vip: #9a5716;
                --vip-soft: #fff1d9;
                --shadow: 0 28px 66px rgba(62, 45, 23, 0.12);
            }}
            * {{ box-sizing: border-box; }}
            html {{ scroll-behavior: smooth; }}
            body {{
                margin: 0;
                color: var(--ink);
                background:
                    radial-gradient(circle at 12% 0%, rgba(246, 215, 156, 0.54), transparent 28%),
                    radial-gradient(circle at 100% 18%, rgba(11, 110, 105, 0.14), transparent 24%),
                    linear-gradient(180deg, #faf6ee 0%, #f4efe6 100%);
                font-family: "Manrope", sans-serif;
            }}
            a {{ color: inherit; }}
            .shell {{
                max-width: 1100px;
                margin: 0 auto;
                padding: 32px 20px 64px;
            }}
            .topbar {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 16px;
                margin-bottom: 18px;
            }}
            .back-link {{
                display: inline-flex;
                align-items: center;
                gap: 10px;
                padding: 10px 14px;
                border-radius: 999px;
                border: 1px solid var(--line);
                background: rgba(255, 252, 246, 0.86);
                text-decoration: none;
                color: var(--accent);
                font-weight: 700;
            }}
            .issue-chip {{
                padding: 8px 12px;
                border-radius: 999px;
                background: rgba(11, 110, 105, 0.08);
                color: var(--accent);
                font-size: 0.86rem;
                font-weight: 700;
            }}
            .article-shell {{
                border: 1px solid var(--line);
                border-radius: 30px;
                background: var(--surface);
                box-shadow: var(--shadow);
                overflow: hidden;
            }}
            .article-hero {{
                padding: 32px 32px 22px;
                border-bottom: 1px solid var(--line);
                background:
                    linear-gradient(135deg, rgba(11, 110, 105, 0.08), transparent 55%),
                    linear-gradient(180deg, rgba(246, 215, 156, 0.2), rgba(255, 253, 248, 0.85));
            }}
            .article-hero h1 {{
                margin: 12px 0 10px;
                font-family: "Source Serif 4", serif;
                font-size: clamp(2.4rem, 4vw, 4.4rem);
                line-height: 0.95;
                letter-spacing: -0.04em;
            }}
            .article-hero p {{
                margin: 0;
                max-width: 48rem;
                color: var(--muted);
                line-height: 1.8;
            }}
            .article-body {{
                padding: 28px 32px 36px;
                font-size: 1.02rem;
                line-height: 1.85;
            }}
            .article-body h1,
            .article-body h2,
            .article-body h3 {{
                font-family: "Source Serif 4", serif;
                letter-spacing: -0.02em;
                line-height: 1.05;
            }}
            .article-body h1 {{
                margin: 0 0 20px;
                font-size: 2.5rem;
                padding-bottom: 0.35em;
                border-bottom: 1px solid var(--line);
            }}
            .article-body h2 {{
                margin: 34px 0 16px;
                font-size: 1.7rem;
                padding-bottom: 0.38em;
                border-bottom: 1px solid rgba(99, 78, 45, 0.12);
            }}
            .article-body h3 {{
                display: flex;
                align-items: center;
                flex-wrap: wrap;
                gap: 10px;
                margin: 0 0 12px;
                font-size: 1.3rem;
            }}
            .article-body h4 {{
                margin: 18px 0 10px;
                font-size: 1rem;
                letter-spacing: -0.01em;
            }}
            .article-body p {{
                margin: 0 0 18px;
            }}
            .article-body .section-heading {{
                margin-top: 38px;
            }}
            .paper-card {{
                margin: 0 0 22px;
                padding: 22px 22px 18px;
                border: 1px solid rgba(99, 78, 45, 0.14);
                border-radius: 26px;
                background: rgba(255, 253, 248, 0.9);
                box-shadow: 0 16px 32px rgba(62, 45, 23, 0.08);
            }}
            .pick-card {{
                background:
                    linear-gradient(180deg, rgba(255, 255, 255, 0.9), rgba(255, 251, 244, 0.92)),
                    linear-gradient(135deg, rgba(11, 110, 105, 0.05), transparent 55%);
            }}
            .watch-card {{
                background:
                    linear-gradient(180deg, rgba(255, 252, 246, 0.94), rgba(249, 245, 236, 0.92));
                border-style: dashed;
            }}
            .paper-card > :last-child {{
                margin-bottom: 0;
            }}
            .prompt-heading {{
                display: inline-flex;
                align-items: center;
                padding: 7px 11px;
                border-radius: 999px;
                background: rgba(11, 110, 105, 0.08);
                color: var(--accent);
                font-family: "Manrope", sans-serif;
                font-size: 0.82rem;
                font-weight: 800;
                letter-spacing: 0.04em;
                text-transform: uppercase;
            }}
            .prompt-disclosure {{
                margin: 16px 0 22px;
                border: 1px solid rgba(99, 78, 45, 0.14);
                border-radius: 22px;
                background: rgba(255, 252, 246, 0.82);
                box-shadow: 0 12px 24px rgba(62, 45, 23, 0.06);
                overflow: hidden;
            }}
            .prompt-summary {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 16px;
                padding: 14px 16px;
                cursor: pointer;
                list-style: none;
                color: var(--accent);
                font-family: "Manrope", sans-serif;
                font-size: 0.94rem;
                font-weight: 800;
                letter-spacing: 0.01em;
                background: rgba(11, 110, 105, 0.07);
            }}
            .prompt-summary::-webkit-details-marker {{
                display: none;
            }}
            .prompt-summary::after {{
                content: "Show";
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-width: 64px;
                padding: 6px 10px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.84);
                color: var(--muted);
                font-size: 0.75rem;
                font-weight: 800;
                letter-spacing: 0.06em;
                text-transform: uppercase;
            }}
            .prompt-disclosure[open] .prompt-summary::after {{
                content: "Hide";
            }}
            .prompt-body {{
                padding: 0 14px 14px;
            }}
            .prompt-body blockquote {{
                margin-top: 14px;
                margin-bottom: 14px;
            }}
            .prompt-body .code-block {{
                margin-bottom: 0;
            }}
            .article-body ul,
            .article-body ol {{
                margin: 0 0 20px;
                padding-left: 1.4rem;
            }}
            .article-body li {{
                margin-bottom: 8px;
            }}
            .article-body blockquote {{
                margin: 0 0 22px;
                padding: 16px 18px;
                border-left: 4px solid rgba(11, 110, 105, 0.3);
                border-radius: 0 18px 18px 0;
                background: rgba(11, 110, 105, 0.05);
                color: #36505f;
            }}
            .article-body hr {{
                border: 0;
                height: 1px;
                margin: 28px 0;
                background: linear-gradient(90deg, transparent, rgba(99, 78, 45, 0.22), transparent);
            }}
            .article-body table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 24px;
                overflow: hidden;
                border-radius: 18px;
                border: 1px solid var(--line);
                background: var(--surface-strong);
            }}
            .article-body th,
            .article-body td {{
                padding: 12px 14px;
                border-bottom: 1px solid rgba(99, 78, 45, 0.1);
                text-align: left;
                vertical-align: top;
            }}
            .article-body th {{
                background: rgba(11, 110, 105, 0.06);
                font-weight: 800;
            }}
            .article-body code {{
                font-family: "IBM Plex Mono", monospace;
                font-size: 0.9em;
                padding: 0.15em 0.4em;
                border-radius: 0.5em;
                background: rgba(11, 110, 105, 0.08);
                color: var(--accent-strong);
            }}
            .code-block {{
                margin: 0 0 24px;
                border: 1px solid rgba(99, 78, 45, 0.14);
                border-radius: 22px;
                overflow: hidden;
                background: #fffef9;
                box-shadow: 0 16px 32px rgba(62, 45, 23, 0.08);
            }}
            .code-toolbar {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 12px;
                padding: 12px 14px;
                border-bottom: 1px solid rgba(99, 78, 45, 0.12);
                background: rgba(246, 215, 156, 0.14);
            }}
            .code-label {{
                color: var(--muted);
                font-size: 0.84rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }}
            .copy-button {{
                appearance: none;
                border: 0;
                border-radius: 999px;
                padding: 9px 14px;
                background: var(--accent);
                color: white;
                font-weight: 700;
                cursor: pointer;
                box-shadow: 0 10px 24px rgba(11, 110, 105, 0.18);
            }}
            .copy-button.is-copied {{
                background: #2e8b57;
            }}
            .article-body pre {{
                margin: 0;
                padding: 18px;
                overflow: auto;
                background: transparent;
            }}
            .article-body pre code {{
                display: block;
                padding: 0;
                background: transparent;
                color: #1b2a38;
                line-height: 1.7;
            }}
            .resource-badge {{
                display: inline-flex;
                align-items: center;
                gap: 6px;
                padding: 6px 12px;
                border-radius: 999px;
                text-decoration: none;
                font-family: "Manrope", sans-serif;
                font-size: 0.68em;
                font-weight: 800;
                letter-spacing: 0.04em;
                text-transform: uppercase;
                border: 1px solid transparent;
                transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
            }}
            .resource-badge:hover {{
                transform: translateY(-1px);
            }}
            .resource-badge svg {{
                fill: none;
                stroke: currentColor;
                stroke-width: 1.8;
                stroke-linecap: round;
                stroke-linejoin: round;
            }}
            .vip-badge {{
                color: var(--vip);
                background: var(--vip-soft);
                border-color: rgba(154, 87, 22, 0.18);
            }}
            .vip-badge svg {{
                fill: currentColor;
                stroke: none;
            }}
            .html-badge {{
                color: var(--html);
                background: var(--html-soft);
                border-color: rgba(50, 92, 178, 0.2);
            }}
            .pdf-badge {{
                color: var(--pdf);
                background: var(--pdf-soft);
                border-color: rgba(181, 71, 79, 0.22);
            }}
            .chatgpt-badge {{
                color: var(--accent);
                background: var(--accent-soft);
                border-color: rgba(11, 110, 105, 0.2);
            }}
            @media (max-width: 820px) {{
                .topbar {{
                    flex-direction: column;
                    align-items: flex-start;
                }}
                .article-hero,
                .article-body {{
                    padding-left: 20px;
                    padding-right: 20px;
                }}
                .article-body h1 {{
                    font-size: 2rem;
                }}
            }}
        </style>
        <script>
            MathJax = {{
                tex: {{
                    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
                }},
                svg: {{
                    fontCache: 'global'
                }}
            }};
        </script>
        <script type="text/javascript" id="MathJax-script" async
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        </script>
    </head>
    <body>
        <main class="shell">
            <div class="topbar">
                <a href="{escape(back_href)}" class="back-link">← Back to Archive</a>
                <span class="issue-chip">Issue {escape(report.title)}</span>
            </div>
            <article class="article-shell">
                <header class="article-hero">
                    <span class="issue-chip">RoboPulse Brief</span>
                    <h1>{escape(report.title)}</h1>
                    <p>
                        Start with the editor's picks, skim the watchlist only if needed, then jump into the paper's
                        own HTML, PDF, or customized ChatGPT handoff when a result deserves deeper scrutiny.
                    </p>
                </header>
                <section class="article-body">
                    {html_body}
                </section>
            </article>
        </main>
        <script>
            document.querySelectorAll('.copy-button').forEach((button) => {{
                button.addEventListener('click', async () => {{
                    const code = button.closest('.code-block')?.querySelector('pre code');
                    if (!code) {{
                        return;
                    }}

                    try {{
                        await navigator.clipboard.writeText(code.innerText);
                        const original = button.textContent;
                        button.textContent = 'Copied';
                        button.classList.add('is-copied');
                        window.setTimeout(() => {{
                            button.textContent = original;
                            button.classList.remove('is-copied');
                        }}, 1400);
                    }} catch (error) {{
                        button.textContent = 'Copy failed';
                        window.setTimeout(() => {{
                            button.textContent = 'Copy Prompt';
                        }}, 1400);
                    }}
                }});
            }});
        </script>
    </body>
    </html>
    """
