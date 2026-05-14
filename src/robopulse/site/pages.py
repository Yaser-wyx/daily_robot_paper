from html import escape
from pathlib import Path
from string import Template

from robopulse.site.markdown import render_markdown_body
from robopulse.site.reports import asset_href, report_href

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"


def render_template(name, context):
    template = Template((TEMPLATE_DIR / name).read_text(encoding="utf-8"))
    return template.safe_substitute(context)


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
            f'''
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
            '''
        )

    latest_cta = f'<a href="{escape(report_href(latest.report_id))}" class="hero-button">Open Latest Report</a>' if latest else ""
    cards_html = ''.join(cards) if cards else '<div class="empty-state">No reports found yet. Run the generator to publish the first issue.</div>'
    return render_template(
        "archive.html",
        {
            "favicon_href": escape(asset_href(page_depth, "static/favicon.svg")),
            "archive_css_href": escape(asset_href(page_depth, "static/css/archive.css")),
            "archive_js_href": escape(asset_href(page_depth, "static/js/archive-search.js")),
            "latest_cta": latest_cta,
            "report_count": str(len(reports)),
            "latest_title": escape(latest.title) if latest else "N/A",
            "search_index_href": escape(asset_href(page_depth, "search-index.json")),
            "cards": cards_html,
        },
    )


def render_detail_page(report, page_depth=2):
    """Render a report detail page."""
    md_content = report.markdown_path.read_text(encoding="utf-8")
    html_body = render_markdown_body(md_content, page_depth=page_depth)
    return render_template(
        "detail.html",
        {
            "filename": escape(report.filename),
            "favicon_href": escape(asset_href(page_depth, "static/favicon.svg")),
            "report_css_href": escape(asset_href(page_depth, "static/css/report.css")),
            "mathjax_config_href": escape(asset_href(page_depth, "static/js/mathjax-config.js")),
            "report_js_href": escape(asset_href(page_depth, "static/js/report-detail.js")),
            "back_href": escape(asset_href(page_depth, "index.html")),
            "report_title": escape(report.title),
            "html_body": html_body,
        },
    )
