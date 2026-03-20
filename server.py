from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from site_renderer import REPORTS_DIR, load_reports, render_archive_page, render_detail_page

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


def get_report_by_id(report_id):
    """Look up one report by its stable report_id."""
    for report in load_reports(REPORTS_DIR):
        if report.report_id == report_id:
            return report
    return None


@app.get("/", response_class=HTMLResponse)
async def list_reports():
    reports = load_reports(REPORTS_DIR)
    return render_archive_page(reports, page_depth=0)


@app.get("/index.html", response_class=HTMLResponse)
async def list_reports_index():
    return RedirectResponse(url="/", status_code=308)


@app.get("/reports/{report_id}", response_class=HTMLResponse)
async def redirect_report_without_trailing_slash(report_id: str):
    return RedirectResponse(url=f"/reports/{report_id}/", status_code=308)


@app.get("/reports/{report_id}/", response_class=HTMLResponse)
async def read_report(report_id: str):
    report = get_report_by_id(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return render_detail_page(report, page_depth=2)


@app.get("/report/{filename}", response_class=HTMLResponse)
async def redirect_legacy_report_route(filename: str):
    report_id = Path(filename).stem
    report = get_report_by_id(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return RedirectResponse(url=f"/reports/{report.report_id}/", status_code=308)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
