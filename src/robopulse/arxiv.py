import re
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from robopulse.config import ARXIV_ABS_URL, ARXIV_HTML_URL, ARXIV_PDF_URL, ARXIV_URL, REQUEST_HEADERS
from robopulse.utils import dedupe_preserve_order, normalize_paper_id, print, truncate_text

class ArxivNotUpdatedError(RuntimeError):
    """Raised when arXiv new submissions have not rolled over to the local day yet."""


def fetch_arxiv_papers():
    """Fetch and parse structured data from arXiv new submissions."""
    print(f"🌐 [Harvester] Fetching from: {ARXIV_URL} ...")

    try:
        response = requests.get(ARXIV_URL, headers=REQUEST_HEADERS, timeout=15)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("❌ [Error] Network request timed out while fetching arXiv.")
        return None
    except requests.exceptions.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "unknown"
        print(f"❌ [Error] arXiv returned HTTP status {status_code}.")
        return None
    except requests.exceptions.ConnectionError as exc:
        error_text = str(exc)
        if "NameResolutionError" in error_text or "Failed to resolve" in error_text:
            print("❌ [Error] DNS resolution failed while connecting to arXiv. Check network or DNS settings.")
        else:
            print(f"❌ [Error] Could not connect to arXiv: {exc}")
        return None
    except requests.exceptions.RequestException as exc:
        print(f"❌ [Error] Network request failed: {exc}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    today = datetime.now()
    expected_date_str = f"{today.day} {today.strftime('%B %Y')}"

    date_header = soup.find("h3", string=re.compile(r"Showing new listings for", re.IGNORECASE))
    if date_header:
        page_date_str = date_header.text.strip()
        if expected_date_str not in page_date_str:
            print("\n⚠️ [Warning] Date mismatch detected between arXiv list and local time.")
            print(f"    > Webpage shows: {page_date_str}")
            print(f"    > Local expects: {expected_date_str}")

            if not sys.stdin.isatty():
                print("⏳ [Harvester] arXiv new submissions are not updated for the local day yet.")
                raise ArxivNotUpdatedError(page_date_str)

            try:
                choice = input("❓ Continue fetching and generating the report? [y/N]: ").strip().lower()
            except EOFError:
                print("⏳ [Harvester] Date mismatch confirmation was unavailable. Treating this as retryable.")
                raise ArxivNotUpdatedError(page_date_str)

            if choice not in ["y", "yes"]:
                print("🛑 [Aborted] Task cancelled by user because arXiv is not updated yet.")
                raise ArxivNotUpdatedError(page_date_str)
            print("▶️ [Continue] Confirmed by user, proceeding...\n")
    else:
        print("⚠️ [Warning] No explicit date identifier found on the page. Proceeding anyway.")

    dt_tags = soup.find_all("dt")
    dd_tags = soup.find_all("dd")

    papers = []
    print(f"📥 [Harvester] Found {len(dt_tags)} papers, starting to parse...")

    for dt, dd in zip(dt_tags, dd_tags):
        id_tag = dt.find("a", title="Abstract")
        if not id_tag:
            continue

        paper_id = normalize_paper_id(id_tag.text.strip())
        url = ARXIV_ABS_URL.format(paper_id=paper_id)

        title_div = dd.find("div", class_="list-title")
        if not title_div:
            print(f"  ⚠️ [Warning] Missing title for ID {paper_id}, skipping.")
            continue
        title = title_div.text.replace("Title:", "").strip()

        authors_div = dd.find("div", class_="list-authors")
        authors = authors_div.text.replace("Authors:", "").strip().replace("\n", " ") if authors_div else "Unknown"

        abstract_p = dd.find("p", class_="mathjax")
        if abstract_p:
            abstract = abstract_p.text.strip().replace("\n", " ")
            print(f"  ✅ [Info] Successfully parsed abstract: {paper_id}")
        else:
            abstract = "Abstract not available."
            print(f"  ⚠️ [Warning] Missing abstract for ID {paper_id}.")

        papers.append(
            {
                "id": paper_id,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "url": url,
                "pdf_url": ARXIV_PDF_URL.format(paper_id=paper_id),
            }
        )

    print(f"✅ [Harvester] Successfully extracted {len(papers)} papers.")
    return papers

def safe_get(url, timeout=15):
    """Fetch a URL and return a response object or None."""
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException:
        return None


def discover_versioned_id(paper_id):
    """Find the latest versioned arXiv ID from the abstract page when needed."""
    if re.search(r"v\d+$", paper_id):
        return paper_id

    response = safe_get(ARXIV_ABS_URL.format(paper_id=paper_id), timeout=10)
    if not response:
        return None

    match = re.search(rf"/abs/({re.escape(paper_id)}v\d+)", response.text)
    if match:
        return match.group(1)

    return None


def looks_like_html_paper(text):
    """Best-effort detection for a rendered paper page instead of an error page."""
    lowered = text.lower()
    if "<html" not in lowered:
        return False
    if "does not have html" in lowered or "not available in html" in lowered:
        return False
    return "ltx_" in lowered or "abstract" in lowered or "section" in lowered


def fetch_arxiv_html(paper):
    """Try several arXiv HTML URLs and return the first viable page."""
    normalized_id = normalize_paper_id(paper["id"])
    candidate_ids = [paper["id"], normalized_id]

    versioned_id = discover_versioned_id(normalized_id)
    if versioned_id:
        candidate_ids.append(versioned_id)

    for candidate_id in dedupe_preserve_order(candidate_ids):
        html_url = ARXIV_HTML_URL.format(paper_id=candidate_id)
        response = safe_get(html_url, timeout=15)
        if response and "text/html" in response.headers.get("content-type", "") and looks_like_html_paper(response.text):
            return html_url, response.text

    return None, None
