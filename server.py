from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import markdown
import os
import glob
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

REPORTS_DIR = "reports"

def get_report_files():
    """Returns a list of markdown files sorted by modification time (newest first)."""
    files = glob.glob(os.path.join(REPORTS_DIR, "*.md"))
    # Sort by modification time, newest first
    files.sort(key=os.path.getmtime, reverse=True)
    return files

@app.get("/", response_class=HTMLResponse)
async def list_reports():
    files = get_report_files()
    
    list_items = ""
    for file_path in files:
        filename = os.path.basename(file_path)
        # Try to parse date from filename or use modification time
        try:
            display_date = filename.split('-RoboPulse')[0]
        except:
            display_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')
            
        list_items += f"""
            <li class="report-item">
                <a href="/report/{filename}" class="report-link">
                    <span class="report-date">{display_date}</span>
                    <span class="report-title">{filename}</span>
                </a>
            </li>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RoboPulse Reports</title>
        <link rel="icon" href="/static/favicon.svg" type="image/svg+xml">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f6f8fa; color: #24292f; }}
            h1 {{ border-bottom: 1px solid #d0d7de; padding-bottom: 10px; margin-bottom: 20px; }}
            ul {{ list-style-type: none; padding: 0; }}
            .report-item {{ background: white; border: 1px solid #d0d7de; border-radius: 6px; margin-bottom: 10px; transition: box-shadow 0.2s; }}
            .report-item:hover {{ box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
            .report-link {{ display: block; padding: 16px; text-decoration: none; color: inherit; display: flex; justify-content: space-between; align-items: center; }}
            .report-date {{ font-weight: 600; color: #0969da; }}
            .report-title {{ color: #57606a; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <h1>📅 RoboPulse Daily Reports</h1>
        <ul>
            {list_items if list_items else "<li>No reports found. Run the generator script first!</li>"}
        </ul>
    </body>
    </html>
    """
    return html_content

@app.get("/report/{filename}", response_class=HTMLResponse)
async def read_report(filename: str):
    file_path = os.path.join(REPORTS_DIR, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Report not found")
    
    with open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_body = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{filename}</title>
        <link rel="icon" href="/static/favicon.svg" type="image/svg+xml">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 40px 20px; background-color: #ffffff; color: #24292f; }}
            a.back-link {{ display: inline-block; margin-bottom: 20px; text-decoration: none; color: #0969da; font-weight: 600; }}
            a.back-link:hover {{ text-decoration: underline; }}
            /* Markdown Styles */
            h1, h2, h3 {{ margin-top: 24px; margin-bottom: 16px; font-weight: 600; line-height: 1.25; }}
            h1 {{ font-size: 2em; padding-bottom: 0.3em; border-bottom: 1px solid #eaecef; }}
            h2 {{ font-size: 1.5em; padding-bottom: 0.3em; border-bottom: 1px solid #eaecef; }}
            h3 {{ font-size: 1.25em; }}
            p {{ margin-top: 0; margin-bottom: 16px; }}
            blockquote {{ margin: 0 0 16px; padding: 0 1em; color: #6a737d; border-left: 0.25em solid #dfe2e5; }}
            code {{ padding: 0.2em 0.4em; margin: 0; font-size: 85%; background-color: #f6f8fa; border-radius: 6px; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace; }}
            pre {{ padding: 16px; overflow: auto; line-height: 1.45; background-color: #f6f8fa; border-radius: 6px; }}
            pre code {{ background-color: transparent; padding: 0; }}
            table {{ border-spacing: 0; border-collapse: collapse; width: 100%; margin-bottom: 16px; }}
            table th, table td {{ padding: 6px 13px; border: 1px solid #dfe2e5; }}
            table th {{ font-weight: 600; background-color: #f6f8fa; }}
            tr:nth-child(2n) {{ background-color: #f8f8f8; }}
            ul, ol {{ padding-left: 2em; margin-bottom: 16px; }}
            img {{ max-width: 100%; box-sizing: content-box; background-color: #fff; }}
            hr {{ height: 0.25em; padding: 0; margin: 24px 0; background-color: #e1e4e8; border: 0; }}
        </style>
    </head>
    <body>
        <a href="/" class="back-link">← Back to List</a>
        {html_body}
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
