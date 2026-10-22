# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills certification banks."""

from __future__ import annotations

from .emergency_aid import FACTS as EMERGENCY_AID_FACTS
from .infection import FACTS as INFECTION_FACTS
from .injection import FACTS as INJECTION_FACTS
from .intake import FACTS as INTAKE_FACTS
from .life_stages import FACTS as LIFE_STAGES_FACTS
from .med_safety import FACTS as MED_SAFETY_FACTS
from .osha_bbp import FACTS as OSHA_BBP_FACTS
from .pharm_dosage import FACTS as PHARM_DOSAGE_FACTS
from .poct import FACTS as POCT_FACTS
from .specimen_lab import FACTS as SPECIMEN_LAB_FACTS
from .terminology import FACTS as TERMINOLOGY_FACTS
from .vitals import FACTS as VITALS_FACTS
from .wound_care import FACTS as WOUND_CARE_FACTS

FACTS: list[dict] = (
    INJECTION_FACTS
    + VITALS_FACTS
    + INFECTION_FACTS
    + TERMINOLOGY_FACTS
    + PHARM_DOSAGE_FACTS
    + SPECIMEN_LAB_FACTS
    + INTAKE_FACTS
    + OSHA_BBP_FACTS
    + MED_SAFETY_FACTS
    + POCT_FACTS
    + WOUND_CARE_FACTS
    + LIFE_STAGES_FACTS
    + EMERGENCY_AID_FACTS
)

__all__ = [
    "FACTS",
    "INJECTION_FACTS",
    "VITALS_FACTS",
    "INFECTION_FACTS",
    "TERMINOLOGY_FACTS",
    "PHARM_DOSAGE_FACTS",
    "SPECIMEN_LAB_FACTS",
    "INTAKE_FACTS",
    "OSHA_BBP_FACTS",
    "MED_SAFETY_FACTS",
    "POCT_FACTS",
    "WOUND_CARE_FACTS",
    "LIFE_STAGES_FACTS",
    "EMERGENCY_AID_FACTS",
]
