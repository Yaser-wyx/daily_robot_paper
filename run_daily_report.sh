#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/daily_run.log"
LOG_DIR="$SCRIPT_DIR/logs"
LOCK_FILE="${TMPDIR:-/tmp}/daily_paper-$(basename "$SCRIPT_DIR").lock"
ARXIV_NOT_UPDATED_EXIT_CODE=75
MAX_LOG_SIZE_BYTES="${MAX_LOG_SIZE_BYTES:-5242880}"
MAX_LOG_ARCHIVES="${MAX_LOG_ARCHIVES:-14}"
AUTO_GIT_PUBLISH="${AUTO_GIT_PUBLISH:-1}"
AUTO_GIT_REMOTE="${AUTO_GIT_REMOTE:-origin}"

cd "$SCRIPT_DIR"

timestamp() {
  date '+%Y-%m-%d %H:%M:%S'
}

log() {
  printf '[%s] %s\n' "$(timestamp)" "$*"
}

acquire_lock() {
  if ! command -v flock >/dev/null 2>&1; then
    log "flock is unavailable. Continuing without a run lock."
    return 0
  fi

  exec 9>"$LOCK_FILE"
  if ! flock -n 9; then
    log "Another report run is already active. Exiting duplicate invocation."
    exit 1
  fi
}

log_exit_status() {
  local exit_code=$?
  if [ "$exit_code" -eq 0 ]; then
    log "Run finished successfully."
  elif [ "$exit_code" -eq "$ARXIV_NOT_UPDATED_EXIT_CODE" ]; then
    log "Run finished with arXiv-not-updated status ($exit_code)."
  else
    log "Run failed with exit code $exit_code."
  fi
}

next_retry_at() {
  date -d '+1 hour' '+%Y-%m-%d %H:%M:%S'
}

github_https_to_ssh() {
  local remote_url="$1"
  if [[ "$remote_url" =~ ^https://github\.com/([^/]+)/([^/]+)\.git$ ]]; then
    printf 'git@github.com:%s/%s.git' "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}"
    return 0
  fi
  return 1
}

push_report_commit() {
  local remote_name="$1"
  local branch_name="$2"
  local remote_url=""
  local ssh_url=""

  if git push "$remote_name" "$branch_name"; then
    log "Auto-pushed report commit to $remote_name/$branch_name."
    return 0
  fi

  remote_url="$(git remote get-url "$remote_name" 2>/dev/null || true)"
  if [ -n "$remote_url" ] && ssh_url="$(github_https_to_ssh "$remote_url")"; then
    log "Primary push via $remote_name failed. Retrying with SSH URL."
    if git push "$ssh_url" "HEAD:$branch_name"; then
      log "Auto-pushed report commit via SSH fallback to $branch_name."
      return 0
    fi
  fi

  log "Auto-push failed for branch $branch_name."
  return 1
}

publish_report_git() {
  local report_rel_path="reports/$RUN_DATE-RoboPulse.md"
  local report_abs_path="$SCRIPT_DIR/$report_rel_path"
  local branch_ref=""
  local branch_name=""
  local tmp_index=""
  local head_tree=""
  local new_tree=""
  local parent_commit=""
  local new_commit=""
  local commit_message="chore(report): publish $RUN_DATE RoboPulse"
  local publish_status=0
  local upstream_ref=""
  local ahead_count=0

  if [ "$AUTO_GIT_PUBLISH" != "1" ]; then
    log "AUTO_GIT_PUBLISH=$AUTO_GIT_PUBLISH. Skipping auto commit/push."
    return 0
  fi

  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    log "Not inside a git worktree. Skipping auto commit/push."
    return 0
  fi

  if [ ! -f "$report_abs_path" ]; then
    log "Expected report file $report_rel_path was not found. Skipping auto commit/push."
    return 1
  fi

  branch_ref="$(git symbolic-ref -q HEAD || true)"
  if [ -z "$branch_ref" ]; then
    log "HEAD is detached. Skipping auto commit/push."
    return 1
  fi
  branch_name="${branch_ref#refs/heads/}"

  upstream_ref="$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null || true)"
  if [ -n "$upstream_ref" ]; then
    ahead_count="$(git rev-list --count "${upstream_ref}..HEAD")"
    if [ "$ahead_count" -gt 0 ]; then
      log "Branch $branch_name is already $ahead_count commit(s) ahead of $upstream_ref. Skipping auto commit/push to avoid publishing unrelated local commits."
      return 1
    fi
  fi

  if ! git config user.name >/dev/null 2>&1 || ! git config user.email >/dev/null 2>&1; then
    log "Git user.name or user.email is not configured. Skipping auto commit/push."
    return 1
  fi

  tmp_index="$(mktemp)"

  if ! GIT_INDEX_FILE="$tmp_index" git read-tree HEAD >/dev/null 2>&1; then
    log "Failed to prepare a temporary git index for report publishing."
    publish_status=1
  elif ! GIT_INDEX_FILE="$tmp_index" git add -- "$report_rel_path" >/dev/null 2>&1; then
    log "Failed to stage $report_rel_path in the temporary git index."
    publish_status=1
  else
    head_tree="$(git rev-parse HEAD^{tree})"
    new_tree="$(GIT_INDEX_FILE="$tmp_index" git write-tree)"
    if [ "$new_tree" = "$head_tree" ]; then
      log "No report diff detected for $report_rel_path. Skipping auto commit/push."
      publish_status=0
    else
      parent_commit="$(git rev-parse HEAD)"
      new_commit="$(
        printf '%s\n' "$commit_message" |
          GIT_INDEX_FILE="$tmp_index" git commit-tree "$new_tree" -p "$parent_commit"
      )"

      if [ -z "$new_commit" ]; then
        log "Failed to create a report commit for $report_rel_path."
        publish_status=1
      elif ! git update-ref "$branch_ref" "$new_commit" "$parent_commit"; then
        log "Failed to move $branch_name to the new report commit."
        publish_status=1
      else
        log "Created report commit $new_commit on $branch_name."
        if ! push_report_commit "$AUTO_GIT_REMOTE" "$branch_name"; then
          log "Report commit exists locally but could not be pushed."
          publish_status=1
        fi
      fi
    fi
  fi

  rm -f "$tmp_index"
  return "$publish_status"
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

trap log_exit_status EXIT
acquire_lock

if [ -t 0 ] || [ -t 1 ]; then
  RUN_CONTEXT="interactive"
else
  RUN_CONTEXT="non-interactive"
fi

log "Run context: $RUN_CONTEXT"
log "Working directory: $SCRIPT_DIR"

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

log "Using python interpreter: $PYTHON_BIN"
log "AUTO_GIT_PUBLISH=$AUTO_GIT_PUBLISH AUTO_GIT_REMOTE=$AUTO_GIT_REMOTE"
log "Starting scheduled report run for $RUN_DATE."

while true; do
  log "Attempt #$ATTEMPT: launching daily.py."

  set +e
  "$PYTHON_BIN" "$SCRIPT_DIR/daily.py"
  EXIT_CODE=$?
  set -e

  if [ "$EXIT_CODE" -eq 0 ]; then
    log "Report generation succeeded."
    if ! publish_report_git; then
      log "Auto commit/push failed after successful report generation."
      exit 1
    fi
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
