# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

if [ -n "${MEILI_HOSTPORT:-}" ] && [ -z "${MEILISEARCH_URL:-}" ]; then
	export MEILISEARCH_URL="http://${MEILI_HOSTPORT}"
fi

if [ -n "${REDIS:-}" ] && [ "${REDIS#*decode_responses=}" = "$REDIS" ]; then
	case "$REDIS" in
	*\?) export REDIS="${REDIS}&decode_responses=True" ;;
	*) export REDIS="${REDIS}?decode_responses=True" ;;
	esac
fi

alembic upgrade head

if [ "${AUTO_SEED_CONTENT:-true}" = "true" ]; then
  python -c "import asyncio; from classquiz.seed.runner import run_seed; asyncio.run(run_seed())"
fi
