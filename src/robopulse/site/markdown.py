import re

import markdown
from bs4 import BeautifulSoup


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
