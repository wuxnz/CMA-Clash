# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA certification banks."""

from __future__ import annotations

from .admin import FACTS as ADMIN_FACTS
from .foundational import FACTS as FOUNDATIONAL_FACTS
from .communication import FACTS as COMMUNICATION_FACTS
from .coordination import FACTS as COORDINATION_FACTS
from .anatomy import FACTS as ANATOMY_FACTS
from .clinical_care import FACTS as CLINICAL_CARE_FACTS
from .law_ethics import FACTS as LAW_ETHICS_FACTS
from .hipaa import FACTS as HIPAA_FACTS
from .transmission import FACTS as TRANSMISSION_FACTS
from .vaccines import FACTS as VACCINES_FACTS
from .diabetes import FACTS as DIABETES_FACTS
from .expansion_batch_01 import FACTS as EXPANSION_BATCH_01_FACTS
from .expansion_batch_02 import FACTS as EXPANSION_BATCH_02_FACTS
from .expansion_batch_03 import FACTS as EXPANSION_BATCH_03_FACTS
from .expansion_batch_04 import FACTS as EXPANSION_BATCH_04_FACTS
from .expansion_batch_05 import FACTS as EXPANSION_BATCH_05_FACTS

FACTS: list[dict] = (
    ADMIN_FACTS
    + FOUNDATIONAL_FACTS
    + COMMUNICATION_FACTS
    + COORDINATION_FACTS
    + ANATOMY_FACTS
    + CLINICAL_CARE_FACTS
    + LAW_ETHICS_FACTS
    + HIPAA_FACTS
    + TRANSMISSION_FACTS
    + VACCINES_FACTS
    + DIABETES_FACTS
    + EXPANSION_BATCH_01_FACTS
    + EXPANSION_BATCH_02_FACTS
    + EXPANSION_BATCH_03_FACTS
    + EXPANSION_BATCH_04_FACTS
    + EXPANSION_BATCH_05_FACTS
)

__all__ = [
    "FACTS",
    "ADMIN_FACTS",
    "FOUNDATIONAL_FACTS",
    "COMMUNICATION_FACTS",
    "COORDINATION_FACTS",
    "ANATOMY_FACTS",
    "CLINICAL_CARE_FACTS",
    "LAW_ETHICS_FACTS",
    "HIPAA_FACTS",
    "TRANSMISSION_FACTS",
    "VACCINES_FACTS",
    "DIABETES_FACTS",
    "EXPANSION_BATCH_01_FACTS",
    "EXPANSION_BATCH_02_FACTS",
    "EXPANSION_BATCH_03_FACTS",
    "EXPANSION_BATCH_04_FACTS",
    "EXPANSION_BATCH_05_FACTS",
]

