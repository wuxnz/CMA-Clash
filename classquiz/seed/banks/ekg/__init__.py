# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored EKG certification banks."""

from __future__ import annotations

from .leads import FACTS as LEADS_FACTS
from .rhythm import FACTS as RHYTHM_FACTS
from .intervals import FACTS as INTERVALS_FACTS
from .artifacts import FACTS as ARTIFACTS_FACTS
from .cardiac_ap import FACTS as CARDIAC_AP_FACTS
from .acls_basics import FACTS as ACLS_BASICS_FACTS

FACTS: list[dict] = (LEADS_FACTS + RHYTHM_FACTS + INTERVALS_FACTS + ARTIFACTS_FACTS + CARDIAC_AP_FACTS + ACLS_BASICS_FACTS)

__all__ = ["FACTS", "LEADS_FACTS", "RHYTHM_FACTS", "INTERVALS_FACTS", "ARTIFACTS_FACTS", "CARDIAC_AP_FACTS", "ACLS_BASICS_FACTS"]

