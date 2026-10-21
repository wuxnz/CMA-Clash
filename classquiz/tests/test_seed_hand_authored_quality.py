# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Content-quality guards for hand-authored seed banks (no template artifacts)."""

import re

import pytest

pytestmark = pytest.mark.order("last")

_BANNED_DISTRACTOR_PATTERNS = [
    re.compile(r"\bhiding\s+aed", re.I),
    re.compile(r"\bhide\s+the\s+aed\b", re.I),
    re.compile(r"\bremoving\s+911\b", re.I),
    re.compile(r"\bremove\s+911\b", re.I),
    re.compile(r"\bposted\s+online\b", re.I),
    re.compile(r"\bshoe\s+comfort\b", re.I),
    re.compile(r"\bleave\s+to\s+find\s+food\b", re.I),
    re.compile(r"\bvision\s+acuity\b", re.I),
    re.compile(r"\bdental\s+health\b", re.I),
    re.compile(r"\bdiscourag(e|ing)\s+.*\s*911\b", re.I),
    re.compile(r"^\s*posted\s+online\s*$", re.I),
    re.compile(r"social\s+media\s+posts\s+about\s+health", re.I),
    re.compile(r"\bwaving\s+hello\b", re.I),
    re.compile(r"\bfoot\s+stamping\b", re.I),
]

_PRESENTS_FOR_CARE = re.compile(r"presents\s+for\s+care", re.I)
_FRAGMENT_MUST_BE = re.compile(r"\bmust\s+be\s*\?\s*$", re.I)
_COLON_FRAGMENT_STEM = re.compile(r":\s*\?\s*$")


def _sentence_count(text: str) -> int:
    return len([p for p in re.split(r"[.!?]+", text) if p.strip()])


def test_no_banned_absurd_distractor_patterns():
    from classquiz.seed.banks import load_all_facts

    hits: list[str] = []
    for fact in load_all_facts():
        for choice in fact["distractors"]:
            for pat in _BANNED_DISTRACTOR_PATTERNS:
                if pat.search(choice):
                    hits.append(f"{pat.pattern} in {fact['topic']}: {choice[:70]}")
    assert not hits, f"Banned distractor patterns: {hits[:12]}"


def test_no_generic_presents_for_care_stem_prefix():
    from classquiz.seed.banks import load_all_facts

    bad = [f["stem"] for f in load_all_facts() if _PRESENTS_FOR_CARE.search(f["stem"])]
    assert not bad, f"Generic presents-for-care stems: {bad[:5]}"


def test_cpr_cert_meets_minimum_hand_authored_floor():
    from classquiz.seed.banks import load_all_facts

    cpr = [f for f in load_all_facts() if f["topic"].startswith("cpr-")]
    assert len(cpr) >= 295, f"CPR/BLS cert has {len(cpr)} questions; floor is 295 (+50% vs ~196 baseline)"


def test_cpr_stems_are_complete_questions():
    from classquiz.seed.banks import load_all_facts

    bad: list[str] = []
    for fact in load_all_facts():
        if not fact["topic"].startswith("cpr-"):
            continue
        stem = fact["stem"].strip()
        if _COLON_FRAGMENT_STEM.search(stem) or stem.endswith(":"):
            bad.append(stem[:90])
        if _FRAGMENT_MUST_BE.search(stem):
            bad.append(stem[:90])
        if not stem.endswith("?") and not stem.endswith("."):
            bad.append(stem[:90])
    assert not bad, f"CPR stems not complete questions: {bad[:8]}"


def test_cpr_explanations_are_specific_two_sentence_minimum():
    from classquiz.seed.banks import load_all_facts

    bad: list[str] = []
    for fact in load_all_facts():
        if not fact["topic"].startswith("cpr-"):
            continue
        expl = (fact.get("explanation") or "").strip()
        if len(expl) < 80 or _sentence_count(expl) < 2:
            bad.append(fact["stem"][:70])
    assert not bad, f"CPR explanations too short or generic: {bad[:8]}"
