# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from .ccma import FACTS as CCMA_SUPPLEMENT
from .clinical_skills import FACTS as CLINICAL_SUPPLEMENT
from .cpr_bls import FACTS as CPR_SUPPLEMENT
from .ekg import FACTS as EKG_SUPPLEMENT
from .phlebotomy import FACTS as PHLEB_SUPPLEMENT

FACTS: list[dict] = [
    *CCMA_SUPPLEMENT,
    *CLINICAL_SUPPLEMENT,
    *CPR_SUPPLEMENT,
    *EKG_SUPPLEMENT,
    *PHLEB_SUPPLEMENT,
]
