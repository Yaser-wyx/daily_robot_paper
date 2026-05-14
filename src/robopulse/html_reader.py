import re

from bs4 import BeautifulSoup

from robopulse.arxiv import fetch_arxiv_html
from robopulse.config import SECTION_PATTERNS, SHORTLIST_CONTEXT_LIMIT
from robopulse.utils import normalize_whitespace, print, truncate_text

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
