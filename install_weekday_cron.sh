#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
RUNNER="$SCRIPT_DIR/run_daily_report.sh"
CRON_LINE="0 10 * * 1-5 $RUNNER"
TMP_FILE="$(mktemp)"

cleanup() {
  rm -f "$TMP_FILE"
}

trap cleanup EXIT

if crontab -l >"$TMP_FILE" 2>/dev/null; then
  :
else
  : >"$TMP_FILE"
fi

grep -Fv "$RUNNER" "$TMP_FILE" >"${TMP_FILE}.filtered" || true
mv "${TMP_FILE}.filtered" "$TMP_FILE"

printf '%s\n' "$CRON_LINE" >>"$TMP_FILE"
crontab "$TMP_FILE"

echo "Installed weekday cron entry:"
echo "  $CRON_LINE"
