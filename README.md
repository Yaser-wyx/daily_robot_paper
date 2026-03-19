# RoboPulse

RoboPulse generates a daily robotics paper briefing from arXiv `cs.RO`.

It uses:

- `codex exec` for local screening and summary generation
- ChatGPT Web as the manual deep-reading handoff
- a FastAPI dashboard for browsing daily reports

## Setup

Install dependencies:

```bash
uv sync
```

Or:

```bash
pip install fastapi uvicorn requests beautifulsoup4 markdown
```

Make sure `codex` is installed and logged in:

```bash
codex login
```

Optional environment variables:

```bash
export CODEX_MODEL="gpt-5-codex"
export CHATGPT_WEB_URL="https://chatgpt.com/"
```

## Manual Usage

Generate a report:

```bash
./run_daily_report.sh
```

View the dashboard:

```bash
uv run uvicorn server:app --host 0.0.0.0 --port 8000
```

Then open `http://localhost:8000`.

## Automatic Schedule

Install the weekday cron job:

```bash
./install_weekday_cron.sh
```

Installed schedule:

```cron
0 10 * * 1-5 /mnt/sda/yaser/project/daily_paper/run_daily_report.sh
```

Behavior:

- Runs Monday through Friday at `10:00` local time
- Does not run on Saturday or Sunday
- If arXiv has not updated to the local day yet, retries every hour
- Stops retrying after success or once the local date rolls over
- Only the stale-arXiv case retries automatically; other failures stop immediately

## Logs

Follow the active log:

```bash
tail -f daily_run.log
```

Log rotation behavior:

- `daily_run.log` rotates automatically when it exceeds `5 MB`
- rotated logs are stored in `logs/`
- the newest `14` rotated logs are kept by default
- override with `MAX_LOG_SIZE_BYTES` and `MAX_LOG_ARCHIVES`

## Workflow

1. Read the local daily brief first.
2. Open the `PDF` or `ChatGPT` badge for papers worth deeper attention.
3. Upload the PDF in ChatGPT Web and paste the provided prompt for a full read.

## Project Structure

- `daily.py`: fetches arXiv papers, runs Codex screening, and writes the report
- `run_daily_report.sh`: main runner with retry and log rotation
- `install_weekday_cron.sh`: installs the weekday `10:00` cron job
- `server.py`: FastAPI dashboard for browsing reports
- `reports/`: generated Markdown reports
- `static/`: static assets
