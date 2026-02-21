# RoboPulse: Daily Arxiv Robotics Report

This project automates the generation of daily reports for new robotics papers from Arxiv (specifically `cs.RO`). It uses Google Gemini to analyze, summarize, and highlight key papers based on your interests.

## Features

- **Automated Fetching**: Retrieves the latest submissions from Arxiv.
- **AI Analysis**: Uses Gemini Pro to screen papers for relevance (VLA, Sim2Real, World Models, etc.) and identify VIP authors.
- **Deep Dives**: Generates detailed "Notion-style" breakdowns for high-value papers.
- **Web Interface**: A simple, clean web interface to browse and read daily reports.

## Setup

1.  **Install Dependencies**:
    This project uses `uv` for package management.
    ```bash
    uv sync
    ```
    Or install manually:
    ```bash
    pip install fastapi uvicorn requests beautifulsoup4 markdown
    ```

2.  **Configuration**:
    - Ensure you have the `gemini` CLI tool installed and configured with your API key.
    - Customize keywords and authors in `daily.py` if needed.

## Usage

### 1. Generate Daily Report

Run the wrapper script:

```bash
./run_daily_report.sh
```

This will:
- Fetch the latest papers.
- Analyze them with Gemini.
- Save a Markdown report in `reports/`.

### 2. View Reports

Start the web server:

```bash
uv run uvicorn server:app --host 0.0.0.0 --port 8000
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Project Structure

- `daily.py`: Main script for fetching and generating reports.
- `server.py`: FastAPI server for viewing reports.
- `reports/`: Directory containing generated Markdown reports.
- `run_daily_report.sh`: Wrapper script for execution.
- `static/`: Static assets (favicon).

