#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/daily_run.log"
LOG_DIR="$SCRIPT_DIR/logs"
ARXIV_NOT_UPDATED_EXIT_CODE=75
MAX_LOG_SIZE_BYTES="${MAX_LOG_SIZE_BYTES:-5242880}"
MAX_LOG_ARCHIVES="${MAX_LOG_ARCHIVES:-14}"

cd "$SCRIPT_DIR"

timestamp() {
  date '+%Y-%m-%d %H:%M:%S'
}

log() {
  printf '[%s] %s\n' "$(timestamp)" "$*"
}

next_retry_at() {
  date -d '+1 hour' '+%Y-%m-%d %H:%M:%S'
}

rotate_log_if_needed() {
  local rotated_path=""
  local log_size=0
  local archive_name=""

  mkdir -p "$LOG_DIR"

  if [ -f "$LOG_FILE" ]; then
    log_size=$(wc -c < "$LOG_FILE")
    if [ "$log_size" -ge "$MAX_LOG_SIZE_BYTES" ]; then
      archive_name="$LOG_DIR/daily_run-$(date '+%Y-%m-%d_%H-%M-%S').log"
      mv "$LOG_FILE" "$archive_name"
      rotated_path="$archive_name"
    fi
  fi

  mapfile -t archives < <(find "$LOG_DIR" -maxdepth 1 -type f -name 'daily_run-*.log' | sort)
  if [ "${#archives[@]}" -gt "$MAX_LOG_ARCHIVES" ]; then
    local delete_count=$(( ${#archives[@]} - MAX_LOG_ARCHIVES ))
    for ((i = 0; i < delete_count; i++)); do
      rm -f "${archives[$i]}"
    done
  fi

  printf '%s' "$rotated_path"
}

ROTATED_LOG="$(rotate_log_if_needed)"

# Mirror logs to both terminal and file so manual runs and cron runs are both debuggable.
exec > >(tee -a "$LOG_FILE") 2>&1

# Keep the script portable across machines while still supporting nvm installs.
if ! command -v codex >/dev/null 2>&1; then
  for codex_candidate in "$HOME"/.nvm/versions/node/*/bin/codex; do
    if [ -x "$codex_candidate" ]; then
      export PATH="$(dirname "$codex_candidate"):$PATH"
      break
    fi
  done
fi

if ! command -v codex >/dev/null 2>&1; then
  log "codex CLI not found. Run 'codex login' and ensure it is in PATH."
  exit 1
fi

if [ -x "$SCRIPT_DIR/.venv/bin/python" ]; then
  PYTHON_BIN="$SCRIPT_DIR/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3)"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python)"
else
  log "Python interpreter not found. Create .venv or install python3."
  exit 1
fi

RUN_DATE="$(date '+%Y-%m-%d')"
ATTEMPT=1

if [ -n "$ROTATED_LOG" ]; then
  log "Rotated daily_run.log to $ROTATED_LOG because it exceeded ${MAX_LOG_SIZE_BYTES} bytes."
fi

log "Starting scheduled report run for $RUN_DATE."

while true; do
  log "Attempt #$ATTEMPT: launching daily.py."

  set +e
  "$PYTHON_BIN" "$SCRIPT_DIR/daily.py"
  EXIT_CODE=$?
  set -e

  if [ "$EXIT_CODE" -eq 0 ]; then
    log "Report generation succeeded."
    exit 0
  fi

  if [ "$EXIT_CODE" -ne "$ARXIV_NOT_UPDATED_EXIT_CODE" ]; then
    log "Report generation failed with exit code $EXIT_CODE. Not retrying automatically."
    exit "$EXIT_CODE"
  fi

  CURRENT_DATE="$(date '+%Y-%m-%d')"
  if [ "$CURRENT_DATE" != "$RUN_DATE" ]; then
    log "The local date rolled over to $CURRENT_DATE. Stop retrying the stale arXiv run for $RUN_DATE."
    exit "$ARXIV_NOT_UPDATED_EXIT_CODE"
  fi

  RETRY_TIME="$(next_retry_at)"
  log "arXiv is not updated yet for the local day. Retrying in 1 hour at $RETRY_TIME."
  ATTEMPT=$((ATTEMPT + 1))
  sleep 3600
done
