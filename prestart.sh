# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

alembic upgrade head

if [ "${AUTO_SEED_CONTENT:-true}" = "true" ]; then
  python -c "import asyncio; from classquiz.seed.runner import run_seed; asyncio.run(run_seed())"
fi
