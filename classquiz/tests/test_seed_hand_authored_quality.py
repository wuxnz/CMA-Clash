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
_FRAGMENT_CLAUSE_WAS = re.compile(
    r"(?:^|[.;])\s*[^?]{8,120}\b(was|is|are|were)\?\s*$",
    re.I,
)
_FRAGMENT_TAIL_QUESTION = re.compile(
    r"(?:"
    r"\bis placed\?|\bshould\?|\bfrom the\?|\bof\?|\bbe\?|\bserves as\?|"
    r"\bare\?|\bshows\?|\bhelp by\?|\brecords\?|\binclude\?|"
    r"\bfunctions mainly as\?|\bis typically\?|\bis commonly placed\?|"
    r"\bis created by viewing from\?|\bis placed at the\?|\bis typically placed\?|"
    r"\bis placed at\?|\bis typically at\?|\bto detect\?|\bto assess\?|"
    r"\bto evaluate\?|\bto improve visualization of\?|\badds posterior leads to improve visualization of\?"
    r")\s*$",
    re.I,
)
_BANNED_DISTRACTOR_QUALIFIER = re.compile(
    r"\b(only|always|never|skip|unmeasurable)\b|"
    r"\bavoid any\b|"
    r"\bstandard\s*$",
    re.I,
)
_HAND_AUTHORED_BANK_PREFIXES = (
    "cpr-",
    "phleb-",
    "ekg-",
    "ccma-",
    "skill-",
)
# Certs that must pass fragment, duplicate-choice, qualifier, and near-duplicate stem checks.
_STRICT_QUALITY_CERT_PREFIXES = (
    "ekg-",
    # CPR and phleb added incrementally as review batches complete.
)
_AHA_ADULT_CHOKING_FIVE_FIVE = re.compile(
    r"(alternate|alternating)\s+5\s+back|five\s+back\s+blows\s+and\s+five\s+abdominal",
    re.I,
)
_STEM_COMPLETE_CERT_PREFIXES = (
    "cpr-",
    "phleb-",
    "ekg-",
    "ccma-",
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
        if _topic_matches_prefixes(fact["topic"], _STRICT_QUALITY_CERT_PREFIXES):
            if _FRAGMENT_TAIL_QUESTION.search(stem):
                bad.append(stem[:90])
            if _FRAGMENT_CLAUSE_WAS.search(stem):
                bad.append(stem[:90])
        if not stem.endswith("?") and not stem.endswith("."):
            bad.append(stem[:90])
    assert not bad, f"Incomplete stems in hand-authored certs: {bad[:12]}"


def _normalize_choice(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def test_hand_authored_no_duplicate_choices_within_item():
    from classquiz.seed.banks import load_all_facts

    bad: list[str] = []
    for fact in load_all_facts():
        if not _topic_matches_prefixes(fact["topic"], _STRICT_QUALITY_CERT_PREFIXES):
            continue
        choices = [fact["correct"], *fact["distractors"]]
        norms = [_normalize_choice(c) for c in choices]
        if len(set(norms)) != len(norms):
            bad.append(f"{fact['topic']}: {fact['stem'][:70]}")
    assert not bad, f"Duplicate answer options in same item: {bad[:12]}"


def test_hand_authored_distractors_lack_banned_qualifiers():
    from classquiz.seed.banks import load_all_facts

    hits: list[str] = []
    for fact in load_all_facts():
        if not _topic_matches_prefixes(fact["topic"], _STRICT_QUALITY_CERT_PREFIXES):
            continue
        for choice in fact["distractors"]:
            if _BANNED_DISTRACTOR_QUALIFIER.search(choice):
                hits.append(f"{fact['stem'][:50]}: {choice[:60]}")
    assert not hits, f"Banned distractor qualifiers: {hits[:12]}"


def test_hand_authored_no_near_duplicate_stems():
    from classquiz.seed.banks import load_all_facts
    from classquiz.seed.stem_normalize import normalize_stem

    def _tokens(stem: str) -> set[str]:
        return set(re.findall(r"[a-z0-9]+", normalize_stem(stem)))

    by_prefix: dict[str, list[dict]] = {}
    for fact in load_all_facts():
        for prefix in _STRICT_QUALITY_CERT_PREFIXES:
            if fact["topic"].startswith(prefix):
                by_prefix.setdefault(prefix, []).append(fact)
                break

    pairs: list[str] = []
    for prefix, facts in by_prefix.items():
        for i, a in enumerate(facts):
            ta = _tokens(a["stem"])
            if not ta:
                continue
            for b in facts[i + 1 :]:
                tb = _tokens(b["stem"])
                if not tb:
                    continue
                overlap = len(ta & tb) / len(ta | tb)
                if overlap >= 0.82:
                    pairs.append(f"{prefix} {overlap:.2f}: {a['stem'][:45]} | {b['stem'][:45]}")
    assert not pairs, f"Near-duplicate stems (Jaccard>=0.82): {pairs[:10]}"


def test_hand_authored_correct_not_uniquely_longest_option():
    from classquiz.seed.banks import load_all_facts
    from classquiz.seed.choice_quality import correct_is_uniquely_longest

    bad: list[str] = []
    for fact in load_all_facts():
        if not _topic_matches_prefixes(fact["topic"], _STRICT_QUALITY_CERT_PREFIXES):
            continue
        if correct_is_uniquely_longest(fact["correct"], fact["distractors"]):
            bad.append(f"{fact['topic']}: {fact['stem'][:70]}")
    assert not bad, f"Correct answer uniquely longest ({len(bad)} items): {bad[:12]}"


def test_hand_authored_correct_not_uniquely_short_by_wide_margin():
    from classquiz.seed.banks import load_all_facts
    from classquiz.seed.choice_quality import correct_is_uniquely_short_by_margin

    bad: list[str] = []
    for fact in load_all_facts():
        if not _topic_matches_prefixes(fact["topic"], _STRICT_QUALITY_CERT_PREFIXES):
            continue
        if correct_is_uniquely_short_by_margin(fact["correct"], fact["distractors"]):
            bad.append(f"{fact['topic']}: {fact['stem'][:70]}")
    assert not bad, f"Correct answer uniquely short vs distractors ({len(bad)} items): {bad[:12]}"


def test_hand_authored_choices_lack_banned_balance_suffixes():
    from classquiz.seed.banks import load_all_facts
    from classquiz.seed.choice_quality import BANNED_BALANCE_SUFFIXES

    hits: list[str] = []
    for fact in load_all_facts():
        if not _topic_matches_prefixes(
            fact["topic"], ("ekg-", "cpr-", "phleb-")
        ):
            continue
        for choice in (fact["correct"], *fact["distractors"]):
            for suffix in BANNED_BALANCE_SUFFIXES:
                if suffix in choice:
                    hits.append(f"{fact['topic']}: {suffix!r} in {choice[:60]}")
    assert not hits, f"Banned auto-balance suffixes in bank text: {hits[:12]}"


def test_cert_correct_positions_spread_after_seed_shuffle():
    from classquiz.seed.choice_quality import seeded_correct_index

    from classquiz.seed.banks import load_all_facts

    for prefix in _STRICT_QUALITY_CERT_PREFIXES:
        facts = [f for f in load_all_facts() if f["topic"].startswith(prefix)]
        assert facts, f"No facts for {prefix}"
        counts = Counter(seeded_correct_index(f["stem"], f["correct"], f["distractors"]) for f in facts)
        assert len(counts) >= 3, f"{prefix} correct positions use only {counts}"
        dominant = max(counts.values()) / len(facts)
        assert dominant <= 0.45, f"{prefix} position skew {dict(counts)}"


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


def test_ccma_cert_meets_minimum_hand_authored_floor():
    from classquiz.seed.banks import load_all_facts

    ccma = [f for f in load_all_facts() if f["topic"].startswith("ccma-")]
    assert len(ccma) >= 588, f"CCMA cert has {len(ccma)} questions; floor is 588 (+50% vs ~392 baseline)"


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
