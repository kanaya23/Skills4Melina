#!/usr/bin/env bash
set -euo pipefail

DISPLAY_NUM="${DISPLAY_NUM:-:99}"
SCREEN_SPEC="${SCREEN_SPEC:-1920x1080x24}"
LOG_FILE="${LOG_FILE:-/tmp/xvfb-melina.log}"

if ! command -v Xvfb >/dev/null 2>&1; then
  echo "Xvfb not found in PATH" >&2
  exit 1
fi

if ! pgrep -f "Xvfb ${DISPLAY_NUM}" >/dev/null 2>&1; then
  nohup Xvfb "${DISPLAY_NUM}" -screen 0 "${SCREEN_SPEC}" >"${LOG_FILE}" 2>&1 &
  sleep 2
fi

export DISPLAY="${DISPLAY_NUM}"
echo "DISPLAY=${DISPLAY}"
