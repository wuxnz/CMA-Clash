# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Additional exam-aligned question bank expansion (growth set)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_RAW: tuple[
    tuple[str, str, str, tuple[str, str, str], str, tuple[str, ...]],
    ...,
] = (

)


FACTS: list[dict] = [
    fact(topic, stem, correct, list(distractors), explanation, list(refs))
    for topic, stem, correct, distractors, explanation, refs in _RAW
]
