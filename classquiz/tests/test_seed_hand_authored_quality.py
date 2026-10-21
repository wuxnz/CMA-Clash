# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Content-quality guards for hand-authored seed banks (no template artifacts)."""

import re
from collections import Counter

import pytest

pytestmark = pytest.mark.order("last")

_GLOBAL_BANNED_DISTRACTOR_PATTERNS = [
    re.compile(r"\bhiding\s+aed", re.I),
    re.compile(r"\bhide\s+the\s+aed\b", re.I),
    re.compile(r"\bremoving\s+911\b", re.I),
    re.compile(r"\bremove\s+911\b", re.I),
    re.compile(r"\bposted\s+online\b", re.I),
    re.compile(r"\bshoe\s+comfort\b", re.I),
    re.compile(r"\bleave\s+to\s+find\s+food\b", re.I),
    re.compile(r"\bvision\s+acuity\b", re.I),
    re.compile(r"\bdental\s+health\b", re.I),
    re.compile(r"^\s*posted\s+online\s*$", re.I),
    re.compile(r"social\s+media\s+posts\s+about\s+health", re.I),
    re.compile(r"\bwaving\s+hello\b", re.I),
    re.compile(r"\bfoot\s+stamping\b", re.I),
]

_CPR_BANNED_DISTRACTOR_PATTERNS = _GLOBAL_BANNED_DISTRACTOR_PATTERNS + [
    re.compile(r"\bignore\s+until\s+blue\b", re.I),
    re.compile(r"\bwait\s+for\s+physician\b", re.I),
    re.compile(r"\bstanding\s+immediately\b", re.I),
    re.compile(r"\bunmonitored\s+waiting\s+room\b", re.I),
    re.compile(r"\bleft\s+nipple\s+only\b", re.I),
    re.compile(r"\bhead\s+down\s+only\s+always\b", re.I),
    re.compile(r"\bonly\s+back\s+slaps\s+forever\b", re.I),
    re.compile(r"\bforever\b", re.I),
    re.compile(r"\bonly\s+always\b", re.I),
    re.compile(r"\bdiscourag(e|ing)\s+911\s+calls\b", re.I),
]

_BANNED_EXPLANATION_PHRASES = [
    re.compile(
        r"incorrect here because it would not provide effective BLS care in this scenario",
        re.I,
    ),
]

_PRESENTS_FOR_CARE = re.compile(r"presents\s+for\s+care", re.I)
_FRAGMENT_MUST_BE = re.compile(r"\bmust\s+be\s*\?\s*$", re.I)
_COLON_FRAGMENT_STEM = re.compile(r":\s*\?\s*$")
_DASH_CHARS = re.compile(r"[\u2013\u2014]")
_INCOMPLETE_STEM_END = re.compile(
    r"\b("
    r"should be|must be|includes|requires|because|should prompt|should include|"
    r"the first priority is|is best prevented by|is called|should usually be held"
    r")\?\s*$",
    re.I,
)
_AHA_ADULT_CHOKING_FIVE_FIVE = re.compile(
    r"(alternate|alternating)\s+5\s+back|five\s+back\s+blows\s+and\s+five\s+abdominal",
    re.I,
)
_STEM_COMPLETE_CERT_PREFIXES = (
    "cpr-",
    "phleb-",
    "ekg-",
)
_DASH_CHECK_CERT_PREFIXES = (
    "cpr-",
    "phleb-",
    "ekg",
    "ccma",
    "skill-",
    "clinical-",
)


def _topic_matches_prefixes(topic: str, prefixes: tuple[str, ...]) -> bool:
    return any(
        topic.startswith(p) if p.endswith("-") else topic.startswith(p)
        for p in prefixes
    )


def _cert_fields(fact: dict) -> list[str]:
    return [fact["stem"], fact["correct"], *fact["distractors"], fact.get("explanation") or ""]


def _sentence_count(text: str) -> int:
    return len([p for p in re.split(r"[.!?]+", text) if p.strip()])


def _expl_sentences(text: str) -> list[str]:
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", text.strip()) if p.strip()]
    return parts


def test_no_banned_absurd_distractor_patterns():
    from classquiz.seed.banks import load_all_facts

    hits: list[str] = []
    for fact in load_all_facts():
        for choice in fact["distractors"]:
            for pat in _GLOBAL_BANNED_DISTRACTOR_PATTERNS:
                if pat.search(choice):
                    hits.append(f"{pat.pattern} in {fact['topic']}: {choice[:70]}")
    assert not hits, f"Banned distractor patterns: {hits[:12]}"


def test_cpr_distractors_lack_absurd_patterns():
    from classquiz.seed.banks import load_all_facts

    hits: list[str] = []
    for fact in load_all_facts():
        if not fact["topic"].startswith("cpr-"):
            continue
        for choice in fact["distractors"]:
            for pat in _CPR_BANNED_DISTRACTOR_PATTERNS:
                if pat.search(choice):
                    hits.append(f"{pat.pattern} in {fact['stem'][:50]}: {choice[:70]}")
    assert not hits, f"CPR absurd distractors: {hits[:12]}"


def test_no_generic_presents_for_care_stem_prefix():
    from classquiz.seed.banks import load_all_facts

    bad = [f["stem"] for f in load_all_facts() if _PRESENTS_FOR_CARE.search(f["stem"])]
    assert not bad, f"Generic presents-for-care stems: {bad[:5]}"


def test_cpr_cert_meets_minimum_hand_authored_floor():
    from classquiz.seed.banks import load_all_facts

    cpr = [f for f in load_all_facts() if f["topic"].startswith("cpr-")]
    assert len(cpr) >= 295, f"CPR/BLS cert has {len(cpr)} questions; floor is 295 (+50% vs ~196 baseline)"


def test_hand_authored_certs_have_no_em_or_en_dashes():
    from classquiz.seed.banks import load_all_facts

    hits: list[str] = []
    for fact in load_all_facts():
        if not _topic_matches_prefixes(fact["topic"], _DASH_CHECK_CERT_PREFIXES):
            continue
        for field in _cert_fields(fact):
            if _DASH_CHARS.search(field):
                hits.append(f"{fact['topic']}: {field[:70]}")
    assert not hits, f"Em/en dashes in cert content: {hits[:10]}"


def test_hand_authored_stems_are_complete_questions():
    from classquiz.seed.banks import load_all_facts

    bad: list[str] = []
    for fact in load_all_facts():
        if not _topic_matches_prefixes(fact["topic"], _STEM_COMPLETE_CERT_PREFIXES):
            continue
        stem = fact["stem"].strip()
        if stem.endswith(":"):
            bad.append(stem[:90])
        if _INCOMPLETE_STEM_END.search(stem):
            bad.append(stem[:90])
        if _COLON_FRAGMENT_STEM.search(stem) or _FRAGMENT_MUST_BE.search(stem):
            bad.append(stem[:90])
        if not stem.endswith("?") and not stem.endswith("."):
            bad.append(stem[:90])
    assert not bad, f"Incomplete stems in hand-authored certs: {bad[:12]}"


def test_cpr_aha_choking_does_not_use_red_cross_adult_five_and_five_answer():
    from classquiz.seed.banks import load_all_facts

    bad: list[str] = []
    for fact in load_all_facts():
        if fact["topic"] != "cpr-choking":
            continue
        stem = fact["stem"].lower()
        if "infant" in stem or "child" in stem:
            continue
        if _AHA_ADULT_CHOKING_FIVE_FIVE.search(fact["correct"]):
            bad.append(fact["stem"][:80])
    assert not bad, f"AHA choking items with Red Cross 5+5 answers: {bad[:6]}"


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
        for pat in _BANNED_EXPLANATION_PHRASES:
            if pat.search(expl):
                bad.append(fact["stem"][:70])
    assert not bad, f"CPR explanations too short or templated: {bad[:8]}"


_PHLEB_BANNED_DISTRACTOR_PATTERNS = _GLOBAL_BANNED_DISTRACTOR_PATTERNS + [
    re.compile(r"\bfavorite\s+(color|beverage)\b", re.I),
    re.compile(r"\bshouted\s+in\s+the\s+waiting\s+room\b", re.I),
    re.compile(r"\boverridden\s+by\s+security\b", re.I),
    re.compile(r"\bincompetence\s+without\s+discussion\b", re.I),
]


def test_phleb_distractors_lack_absurd_patterns():
    from classquiz.seed.banks import load_all_facts

    hits: list[str] = []
    for fact in load_all_facts():
        if not fact["topic"].startswith("phleb-"):
            continue
        for choice in fact["distractors"]:
            for pat in _PHLEB_BANNED_DISTRACTOR_PATTERNS:
                if pat.search(choice):
                    hits.append(f"{pat.pattern} in {fact['stem'][:50]}: {choice[:70]}")
    assert not hits, f"Phlebotomy absurd distractors: {hits[:12]}"


def test_ekg_cert_meets_minimum_hand_authored_floor():
    from classquiz.seed.banks import load_all_facts

    ekg = [f for f in load_all_facts() if f["topic"].startswith("ekg-")]
    assert len(ekg) >= 253, f"EKG cert has {len(ekg)} questions; floor is 253"


def test_phleb_cert_meets_minimum_hand_authored_floor():
    from classquiz.seed.banks import load_all_facts

    phleb = [f for f in load_all_facts() if f["topic"].startswith("phleb-")]
    assert len(phleb) >= 337, f"Phlebotomy cert has {len(phleb)} questions; floor is 337 (+50% vs ~224 baseline)"


def test_phleb_explanations_are_specific_two_sentence_minimum():
    from classquiz.seed.banks import load_all_facts

    bad: list[str] = []
    for fact in load_all_facts():
        if not fact["topic"].startswith("phleb-"):
            continue
        expl = (fact.get("explanation") or "").strip()
        if len(expl) < 80 or _sentence_count(expl) < 2:
            bad.append(fact["stem"][:70])
    assert not bad, f"Phlebotomy explanations too short: {bad[:8]}"


def test_phleb_explanation_sentences_not_repeated_across_bank():
    from classquiz.seed.banks import load_all_facts

    phleb = [f for f in load_all_facts() if f["topic"].startswith("phleb-")]
    sentence_counts: Counter[str] = Counter()
    for fact in phleb:
        for sent in _expl_sentences(fact.get("explanation") or ""):
            norm = re.sub(r"\s+", " ", sent.strip().lower())
            if len(norm) < 40:
                continue
            sentence_counts[norm] += 1
    repeats = [(s, n) for s, n in sentence_counts.items() if n > 3]
    assert not repeats, f"Repeated phleb explanation sentences (>3): {repeats[:5]}"


def test_cpr_explanation_sentences_not_repeated_across_bank():
    from classquiz.seed.banks import load_all_facts

    cpr = [f for f in load_all_facts() if f["topic"].startswith("cpr-")]
    sentence_counts: Counter[str] = Counter()
    for fact in cpr:
        for sent in _expl_sentences(fact.get("explanation") or ""):
            norm = re.sub(r"\s+", " ", sent.strip().lower())
            if len(norm) < 40:
                continue
            sentence_counts[norm] += 1
    repeats = [(s, n) for s, n in sentence_counts.items() if n > 3]
    assert not repeats, f"Repeated CPR explanation sentences (>3): {repeats[:5]}"
