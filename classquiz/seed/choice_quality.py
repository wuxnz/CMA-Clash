# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""ABCD choice helpers: seeded shuffle index and length balancing."""

from __future__ import annotations

import hashlib
import random
import re
from typing import Sequence

_BALANCE_SUFFIXES = (
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


def _shorten_answer_text(text: str, max_len: int) -> str:
    t = text.strip()
    if len(t) <= max_len:
        return t
    while len(t) > max_len and ", " in t:
        t = ", ".join(t.split(", ")[:-1])
    while len(t) > max_len and " with " in t:
        t = t.rsplit(" with ", 1)[0].strip()
    while len(t) > max_len and " and " in t:
        t = t.rsplit(" and ", 1)[0].strip()
    words = t.split()
    while len(t) > max_len and len(words) > 4:
        words.pop()
        t = " ".join(words)
    return t


def _extend_distractor(text: str, stem: str, need: int) -> str:
    t = text.rstrip(".")
    seed = int(hashlib.sha256((stem + text).encode("utf-8")).hexdigest()[:8], 16)
    idx = 0
    while len(t) < need and idx < 24:
        suffix = _BALANCE_SUFFIXES[(seed + idx) % len(_BALANCE_SUFFIXES)]
        if suffix not in t:
            t = f"{t}{suffix}"
        idx += 1
    return t


def correct_is_uniquely_longest(correct: str, distractors: Sequence[str]) -> bool:
    lens = [len(correct)] + [len(d) for d in distractors]
    mx = max(lens)
    return lens[0] == mx and sum(1 for n in lens if n == mx) == 1


def normalize_abcd_choice_lengths(
    stem: str, correct: str, distractors: Sequence[str]
) -> tuple[str, list[str]]:
    """Ensure the keyed answer is not the only longest option (ties allowed)."""
    ds = [d.strip() for d in distractors]
    max_d = max(len(d) for d in ds)
    if len(correct) <= max_d and not correct_is_uniquely_longest(correct, ds):
        return correct.strip(), ds
    shortened = _shorten_answer_text(correct, max_d)
    if not correct_is_uniquely_longest(shortened, ds):
        return shortened, ds
    target = max(len(shortened), max_d)
    for i in range(len(ds)):
        if len(ds[i]) < target:
            ds[i] = _extend_distractor(ds[i], stem, target)
    if correct_is_uniquely_longest(shortened, ds):
        shortest = min(range(len(ds)), key=lambda j: len(ds[j]))
        ds[shortest] = _extend_distractor(ds[shortest], stem, len(shortened))
    return shortened, ds


_FRAGMENT_TAIL_WORD = re.compile(
    r"(?:^|[.;])\s*[A-Za-z][^?]{0,120}\b(was|is|are|were|includes|requires)\?\s*$",
    re.I,
)
