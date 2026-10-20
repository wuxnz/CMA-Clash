#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0
set -euo pipefail
export PATH="${HOME}/.local/bin:${PATH}"
cd "$(dirname "$0")/.."
source .venv/bin/activate
export PYTHONPATH="${PWD}"
export CMA_CLASH_SKIP_SEED=1

PGPASSWORD=mysecretpassword dropdb -h 127.0.0.1 -U postgres --if-exists classquiz
PGPASSWORD=mysecretpassword createdb -h 127.0.0.1 -U postgres classquiz
alembic upgrade head

for index in classquiz cmaclash; do
  curl -sf -X DELETE "http://127.0.0.1:7700/indexes/${index}" >/dev/null || true
done
for _ in $(seq 1 60); do
  missing=0
  for index in classquiz cmaclash; do
    if curl -sf "http://127.0.0.1:7700/indexes/${index}" >/dev/null 2>&1; then
      missing=1
    fi
  done
  if [ "$missing" -eq 0 ]; then
    break
  fi
  sleep 0.25
done

# Note: `coverage run` breaks TestUsers::test_password_update (passlib/event-loop interaction).
pytest -s -v --asyncio-mode=strict classquiz/tests "$@"
