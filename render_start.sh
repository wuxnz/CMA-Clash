#!/usr/bin/env sh
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

set -e

export PYTHONPATH=/app
export APP_MODULE=classquiz:app
export WORKER_CLASS=uvicorn.workers.UvicornWorker
export FORWARDED_ALLOW_IPS="${FORWARDED_ALLOW_IPS:-*}"

if [ -f /app/prestart.sh ]; then
	. /app/prestart.sh
fi

PORT="${PORT:-10000}"
exec uvicorn classquiz:app --host 0.0.0.0 --port "$PORT" --proxy-headers --forwarded-allow-ips "$FORWARDED_ALLOW_IPS"
