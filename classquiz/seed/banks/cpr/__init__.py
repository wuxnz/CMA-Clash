# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored CPR/BLS question banks by topic."""

from .adult import FACTS as ADULT_FACTS
from .child import FACTS as CHILD_FACTS
from .infant import FACTS as INFANT_FACTS
from .aed import FACTS as AED_FACTS
from .choking import FACTS as CHOKING_FACTS
from .chain import FACTS as CHAIN_FACTS
from .red_cross import FACTS as RED_CROSS_FACTS

FACTS: list[dict] = (
    ADULT_FACTS
    + CHILD_FACTS
    + INFANT_FACTS
    + AED_FACTS
    + CHOKING_FACTS
    + CHAIN_FACTS
    + RED_CROSS_FACTS
)
