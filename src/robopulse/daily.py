import sys

from robopulse.arxiv import ArxivNotUpdatedError, fetch_arxiv_papers
from robopulse.codex_client import ensure_runtime_requirements
from robopulse.config import ARXIV_NOT_UPDATED_EXIT_CODE, GENERAL_FAILURE_EXIT_CODE
from robopulse.editor import analyze_shortlist, editor_screening, historical_rediscovery
from robopulse.html_reader import enrich_shortlist_with_html
from robopulse.publisher import publish_report
from robopulse.utils import normalize_paper_id, print

def main():
    """Main application loop."""
    if not ensure_runtime_requirements():
        return GENERAL_FAILURE_EXIT_CODE

    try:
        papers = fetch_arxiv_papers()
    except ArxivNotUpdatedError:
        return ARXIV_NOT_UPDATED_EXIT_CODE

    if papers is None:
        return GENERAL_FAILURE_EXIT_CODE
    if not papers:
        print("⚠️ [Warning] No papers found in the latest arXiv listing.")
        return 0

    screening_result = editor_screening(papers)
    if not screening_result:
        return GENERAL_FAILURE_EXIT_CODE

    paper_map = {normalize_paper_id(paper["id"]): paper for paper in papers}
    shortlisted_papers = [paper_map[paper_id] for paper_id in screening_result["shortlist_ids"] if paper_id in paper_map]
    enriched_papers = enrich_shortlist_with_html(shortlisted_papers)
    analysis_result = analyze_shortlist(screening_result, enriched_papers)
    if not analysis_result:
        return GENERAL_FAILURE_EXIT_CODE

    rediscovery_result = historical_rediscovery()

    publish_report(
        screening_result["title"],
        len(papers),
        screening_result,
        enriched_papers,
        analysis_result,
        rediscovery_result=rediscovery_result,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
