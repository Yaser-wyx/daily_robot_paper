from robopulse.server import (  # noqa: F401
    app,
    get_report_by_id,
    list_reports,
    list_reports_index,
    read_report,
    redirect_legacy_report_route,
    redirect_report_without_trailing_slash,
    search_index,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
