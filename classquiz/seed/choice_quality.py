# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""ABCD choice helpers: seeded shuffle index and length checks."""

from __future__ import annotations

import hashlib
import random
from typing import Sequence

# Banned: former auto-balance padding (must not appear in authored bank text).
BANNED_BALANCE_SUFFIXES = (
    " on the same tracing",
    " in the same lead group",
    " with similar QRS timing",
    " without matching ST territory",
    " when the patient is still",
    " on repeat acquisition",
)


def seeded_correct_index(stem: str, correct: str, distractors: Sequence[str]) -> int:
    """Index of the correct option after the same shuffle used at seed materialization."""
    pairs: list[tuple[str, bool]] = [(correct, True)] + [(d, False) for d in distractors]
    rng = random.Random(int(hashlib.sha256(stem.encode("utf-8")).hexdigest()[:16], 16))
    rng.shuffle(pairs)
    return next(i for i, (_text, is_right) in enumerate(pairs) if is_right)


def correct_is_uniquely_longest(correct: str, distractors: Sequence[str]) -> bool:
    lens = [len(correct)] + [len(d) for d in distractors]
    mx = max(lens)
    return lens[0] == mx and sum(1 for n in lens if n == mx) == 1


def correct_is_uniquely_short_by_margin(
    correct: str,
    distractors: Sequence[str],
    mean_distractor_ratio: float = 0.60,
) -> bool:
    """True when correct is the only shortest option and under ratio * mean distractor length."""
    if not distractors:
        return False
    c_len = len(correct.strip())
    d_lens = [len(d.strip()) for d in distractors]
    shortest = min([c_len] + d_lens)
    if c_len != shortest:
        return False
    if sum(1 for n in [c_len] + d_lens if n == shortest) > 1:
        return False
    mean_d = sum(d_lens) / len(d_lens)
    if mean_d <= 0:
        return False
    return c_len < mean_distractor_ratio * mean_d
