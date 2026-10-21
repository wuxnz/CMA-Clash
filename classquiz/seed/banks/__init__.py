# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Question fact banks for CMA Clash seed data."""

def load_all_facts() -> list[dict]:
    """Return materialized seed question facts (content is pre-authored in materialized_facts)."""
    from .materialized_facts import FACTS as MATERIALIZED_FACTS

    return [dict(f) for f in MATERIALIZED_FACTS]
