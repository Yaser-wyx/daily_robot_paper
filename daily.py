import sys

from robopulse import codex_client as _codex_client
from robopulse.arxiv import (  # noqa: F401
    ArxivFetchRetryableError,
    ArxivNotUpdatedError,
    discover_versioned_id,
    fetch_arxiv_html,
    fetch_arxiv_papers,
    looks_like_html_paper,
    safe_get,
)
from robopulse.codex_client import (  # noqa: F401
    ensure_runtime_requirements,
    resolve_cli_binary,
    run_codex_structured,
)
from robopulse.config import (  # noqa: F401
    ARXIV_ABS_URL,
    ARXIV_HTML_URL,
    ARXIV_NOT_UPDATED_EXIT_CODE,
    ARXIV_PDF_URL,
    ARXIV_URL,
    CHATGPT_WEB_URL,
    CODEX_MODEL,
    CORE_VIP_AUTHORS,
    EXTENDED_VIP_AUTHORS,
    GENERAL_FAILURE_EXIT_CODE,
    INTERESTS,
    OUTPUT_DIR,
    REQUEST_HEADERS,
    RETRYABLE_GENERATION_EXIT_CODE,
    SECTION_PATTERNS,
    SELECTED_TARGET,
    SHORTLIST_CONTEXT_LIMIT,
    SHORTLIST_TARGET,
    VIP_AUTHORS,
    WATCHLIST_PREFIX,
)
from robopulse.daily import main
from robopulse.editor import (  # noqa: F401
    ANALYSIS_SCHEMA,
    REDISCOVERY_PAPER_SCHEMA,
    REDISCOVERY_SCHEMA,
    SCREENING_SCHEMA,
    SELECTED_PAPER_SCHEMA,
    WATCHLIST_PAPER_SCHEMA,
    analyze_shortlist,
    build_analysis_prompt,
    build_chatgpt_prompt,
    build_rediscovery_prompt,
    build_screening_prompt,
    default_priority_questions,
    default_section_focus,
    default_trend_signals,
    editor_screening,
    extract_context_snippet,
    fallback_deep_section,
    historical_rediscovery,
    sanitize_rediscovery_detail,
    sanitize_selected_detail,
    sanitize_watchlist_detail,
)
from robopulse.html_reader import (  # noqa: F401
    clean_html_soup,
    enrich_shortlist_with_html,
    extract_html_context,
    extract_section_from_heading,
    find_section_text,
)
from robopulse.paper_parser import collect_rediscovery_candidates  # noqa: F401
from robopulse.publisher import (  # noqa: F401
    build_report_markdown,
    content_source_summary,
    publish_report,
    rediscovery_resource_tokens,
    resource_tokens,
)
from robopulse.utils import (  # noqa: F401
    clean_json_string,
    dedupe_preserve_order,
    extract_codex_output_from_jsonl,
    get_author_priority_tier,
    normalize_known_ids,
    normalize_paper_id,
    normalize_whitespace,
    paper_has_vip,
    paper_priority_label,
    paper_vip_tier,
    print,
    timestamp,
    truncate_text,
)


def __getattr__(name):
    if name == "CODEX_BIN":
        return _codex_client.CODEX_BIN
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


if __name__ == "__main__":
    sys.exit(main())
