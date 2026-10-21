# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import re

import pytest

pytestmark = pytest.mark.order("last")


def _sentence_count(text: str) -> int:
    return len([p for p in re.split(r"[.!?]+", text) if p.strip()])


def test_explanations_are_two_sentences_and_min_length():
    from classquiz.seed.banks import load_all_facts

    facts = load_all_facts()
    short = []
    for f in facts:
        expl = (f.get("explanation") or "").strip()
        if len(expl) < 80 or _sentence_count(expl) < 2:
            short.append(f["stem"][:70])
    assert not short, f"Short explanations: {short[:8]}"


def test_distractors_are_plausible_length():
    from classquiz.seed.banks import load_all_facts

    for f in load_all_facts():
        for d in f.get("distractors") or []:
            assert len(d) <= 58, f"Long distractor on {f['stem'][:50]}: {d[:40]}..."
