# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Question fact banks for CMA Clash seed data."""

from .ccma import FACTS as CCMA_FACTS
from .clinical_skills import FACTS as CLINICAL_SKILLS_FACTS
from .cpr_bls import FACTS as CPR_BLS_FACTS
from .ekg import FACTS as EKG_FACTS
from .phlebotomy import FACTS as PHLEBOTOMY_FACTS

_ALL_MODULES = (
    CCMA_FACTS,
    CLINICAL_SKILLS_FACTS,
    CPR_BLS_FACTS,
    EKG_FACTS,
    PHLEBOTOMY_FACTS,
)


def load_all_facts() -> list[dict]:
    """Return all seed question facts from every bank module."""
    merged: list[dict] = []
    for facts in _ALL_MODULES:
        merged.extend(facts)
    return merged
