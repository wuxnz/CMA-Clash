# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored phlebotomy question banks by topic (CLSI GP41-aligned)."""

from __future__ import annotations

from .additives import FACTS as ADDITIVES_FACTS
from .complications import FACTS as COMPLICATIONS_FACTS
from .glucose import FACTS as GLUCOSE_FACTS
from .handling import FACTS as HANDLING_FACTS
from .order_draw import FACTS as ORDER_DRAW_FACTS
from .safety import FACTS as SAFETY_FACTS
from .site import FACTS as SITE_FACTS
from .who import FACTS as WHO_FACTS

FACTS: list[dict] = (
    ORDER_DRAW_FACTS
    + ADDITIVES_FACTS
    + SITE_FACTS
    + HANDLING_FACTS
    + COMPLICATIONS_FACTS
    + SAFETY_FACTS
    + WHO_FACTS
    + GLUCOSE_FACTS
)

__all__ = [
    "FACTS",
    "ORDER_DRAW_FACTS",
    "ADDITIVES_FACTS",
    "SITE_FACTS",
    "HANDLING_FACTS",
    "COMPLICATIONS_FACTS",
    "SAFETY_FACTS",
    "WHO_FACTS",
    "GLUCOSE_FACTS",
]
