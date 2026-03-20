# RoboPulse

RoboPulse generates a daily robotics paper briefing from arXiv `cs.RO`, then publishes it as a browsable research dashboard.

The current workflow is split into two environments:

- Local machine: runs `daily.py`, uses your `codex` login, fetches arXiv, and writes `reports/*.md`
- GitHub: turns committed reports into a static site and deploys it with GitHub Pages

## Pipeline

RoboPulse now works in two editorial stages:

1. `codex exec` screens titles, authors, and abstracts into a shortlist
2. RoboPulse fetches arXiv HTML for the shortlisted papers and upgrades the final brief with richer paper cards

Each report can contain:

- `Editor's Picks`: the main papers worth real attention
- `Watchlist`: shortlist overflow that is still worth a quick skim
- VIP author flags with `Core VIP` and `Extended VIP` priority
- `HTML`, `PDF`, and `ChatGPT` badges on selected papers
- one paper-specific deep-read prompt under each selected paper

## Setup

Install dependencies:

```bash
uv sync
```

Or:

```bash
pip install fastapi uvicorn requests beautifulsoup4 markdown
```

Make sure `codex` is installed and logged in locally:

```bash
codex login
```

Optional environment variables:

```bash
export CODEX_MODEL="gpt-5-codex"
export CHATGPT_WEB_URL="https://chatgpt.com/"
export AUTO_GIT_PUBLISH="1"
export AUTO_GIT_REMOTE="origin"
export MAX_LOG_SIZE_BYTES="5242880"
export MAX_LOG_ARCHIVES="14"
```

## Generate Reports Locally

Run the main entrypoint:

```bash
./run_daily_report.sh
```

This script:

- fetches arXiv `cs.RO`
- screens papers with Codex
- enriches shortlisted papers with arXiv HTML
- writes `reports/YYYY-MM-DD-RoboPulse.md`
- retries hourly if arXiv has not updated yet
- auto-commits and auto-pushes the new report by default after success

Disable auto-publish for one run:

```bash
AUTO_GIT_PUBLISH=0 ./run_daily_report.sh
```

## Preview Locally

### FastAPI Preview

Use the local app when you want dynamic preview routes:

```bash
uv run uvicorn server:app --host 0.0.0.0 --port 8000
```

Then open `http://localhost:8000`.

Routes:

- `/`: archive page
- `/reports/<report_id>/`: report detail page
- `/report/<filename>`: legacy local route that redirects to the new URL

### Static Preview

Build the same static site that GitHub Pages will publish:

```bash
python build_site.py
python -m http.server --directory dist 8000
```

Then open `http://localhost:8000`.

Generated output:

- `dist/index.html`
- `dist/reports/<report_id>/index.html`
- `dist/static/*`
- `dist/.nojekyll`

## GitHub Pages Deployment

The repository now includes `.github/workflows/deploy-pages.yml`.

Deployment behavior:

- triggers on push to `master`
- can also be started manually with `workflow_dispatch`
- installs dependencies with `uv sync --locked`
- builds the static site with `python build_site.py`
- uploads `dist/` and deploys it to GitHub Pages

Important constraints:

- GitHub Actions does not run `daily.py`
- GitHub Actions does not need your `codex` login
- the published site only reflects reports that already exist in Git and have been pushed

If this is the first Pages deployment for the repo, set GitHub Pages to use `GitHub Actions` as the build and deployment source in the repository settings.

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

- runs Monday through Friday at `10:00` local time
- does not run on Saturday or Sunday
- if arXiv has not updated to the local day yet, retries every hour
- stops retrying after success or once the local date rolls over
- only the stale-arXiv case retries automatically; other failures stop immediately

## Logs

Follow the active run log:

```bash
tail -f daily_run.log
```

Log behavior:

- `daily_run.log` is append-only during normal operation
- every line emitted by `daily.py` now includes a timestamp
- the file rotates automatically when it exceeds `5 MB`
- rotated logs are stored in `logs/`
- the newest `14` rotated logs are kept by default

## Project Structure

- `daily.py`: fetches arXiv papers, runs Codex screening, fetches arXiv HTML for shortlisted papers, and writes the report
- `run_daily_report.sh`: main runner with retry logic, log rotation, and optional auto commit/push
- `install_weekday_cron.sh`: installs the weekday `10:00` cron job
- `site_renderer.py`: shared HTML renderer for both FastAPI preview and static site builds
- `server.py`: thin FastAPI preview app that serves the shared renderer
- `build_site.py`: builds the GitHub Pages static output into `dist/`
- `.github/workflows/deploy-pages.yml`: GitHub Pages deployment workflow
- `reports/`: generated Markdown reports
- `static/`: static assets used by the rendered site
