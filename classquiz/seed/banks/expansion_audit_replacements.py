# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Unique replacement items added after audit deduplication of growth bank."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_RAW: tuple[
    tuple[str, str, str, tuple[str, str, str], str, tuple[str, ...]],
    ...,
] = (
    # CCMA (19)
    # Clinical skills (29)
    # EKG (6)
    # Phlebotomy (13)

















)

FACTS: list[dict] = [
    fact(topic, stem, correct, list(distractors), explanation, list(refs))
    for topic, stem, correct, distractors, explanation, refs in _RAW
]
