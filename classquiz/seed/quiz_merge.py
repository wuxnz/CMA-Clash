# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Merge duplicate quiz sets and drop near-duplicate questions.

The seed banks are authored per difficulty tier, so the same fact can show up
more than once inside a topic (a beginner phrasing of a question that also
exists as an advanced one).  Public quizzes are merged across tiers, so the
bank has to be de-duplicated first: when two questions ask the same thing, the
harder version wins and the easier one is dropped.

Similarity is deliberately conservative.  A pair only counts as the same
question when the keyed answers agree (or overlap closely) and the stems read
alike.  Scenario qualifiers such as "single" versus "two" rescuers, or lead V1
versus V2 placement, change what is being asked, so a pair whose stems differ
by such a qualifier is never collapsed.
"""

from __future__ import annotations

import difflib
import re
from collections import defaultdict
from functools import lru_cache

from classquiz.seed.stem_normalize import normalize_stem

# Higher rank wins when two questions cover the same fact.
DIFFICULTY_RANK: dict[str, int] = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
}

# Words that carry no discriminating meaning for similarity comparisons.
_STOPWORDS = frozenset(
    """
    a an the of in on at to for from with without by as is are was were be been being am
    and or but if then than that this these those there here what which who whom whose
    when where why how does do did done can could may might must shall should will
    would you your yours we our ours they their them he she his her it its
    """.split()
)

# Qualifiers that change the scenario being asked about.  Questions whose stems
# differ by one of these are different questions even when the answers match.
_SCENARIO_QUALIFIERS = frozenset(
    """
    one two three four five six seven eight nine ten single lone solo both dual multiple
    each every adult child infant newborn pediatric neonatal male female pregnant
    nonpregnant left right bilateral unilateral first second third initial repeat
    routine urgent emergent upper lower anterior posterior full partial complete
    minimal moderate severe mild stable unstable acute chronic
    """.split()
)

# Designations and measurements (v1, v4, 500, 30:2) also change the question.
_DESIGNATION_RE = re.compile(r"^[a-z]*\d+$")

# Numbers inside a keyed answer (8 to 10, 30:2) change what the answer is.
_NUMBER_RE = re.compile(r"\d+")

_TOKEN_RE = re.compile(r"[a-z0-9]+")

# Stems must read alike before the answers are even compared.
STEM_TOKEN_SIMILARITY_MIN = 0.45
STEM_CONTAINMENT_MIN = 0.90
STEM_SEQUENCE_MIN = 0.60

# Two questions that expect the same answer are the same question when the
# shorter stem is (almost) covered by the longer one, or when the stems match
# closely on both tokens and characters.
SAME_ANSWER_OVERLAP_MIN = 0.79
SAME_ANSWER_TOKEN_MIN = 0.60

# Two questions with different keyed answers still match when both the stems and
# the answers overlap closely enough to be a rewording of each other.
DIFFERENT_ANSWER_STEM_MIN = 0.55
DIFFERENT_ANSWER_SEQUENCE_MIN = 0.55
ANSWER_TOKEN_SIMILARITY_MIN = 0.35
ANSWER_CONTAINMENT_MIN = 0.60


def difficulty_rank(difficulty: str | None) -> int:
    """Return the numeric rank of a difficulty tier (unknown tiers rank lowest)."""
    return DIFFICULTY_RANK.get((difficulty or "").strip().lower(), 0)


@lru_cache(maxsize=8192)
def content_tokens(text: str) -> frozenset[str]:
    """Reduce free text to the tokens that carry meaning for comparisons."""
    tokens = {tok for tok in _TOKEN_RE.findall((text or "").lower()) if len(tok) > 1}
    return frozenset(tok for tok in tokens if tok not in _STOPWORDS)


def jaccard(left: frozenset[str], right: frozenset[str]) -> float:
    """Return the Jaccard similarity of two token sets."""
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def containment(left: frozenset[str], right: frozenset[str]) -> float:
    """Return how much of the smaller token set is covered by the larger one."""
    if not left or not right:
        return 0.0
    return len(left & right) / min(len(left), len(right))


@lru_cache(maxsize=8192)
def sequence_ratio(left: str, right: str) -> float:
    """Return the character level similarity of two stems."""
    return difflib.SequenceMatcher(None, (left or "").lower(), (right or "").lower()).ratio()


@lru_cache(maxsize=8192)
def _normalized(text: str) -> str:
    """Normalize a stem or answer for comparison (cached, the merge is quadratic)."""
    return normalize_stem(text or "")


def stem_key(fact: dict) -> str:
    """Return the normalized stem used for exact duplicate detection."""
    return _normalized(fact.get("stem", ""))


def answer_key(fact: dict) -> str:
    """Return the normalized keyed answer used for answer equivalence checks."""
    return _normalized(fact.get("correct", ""))


def differing_qualifiers(left: frozenset[str], right: frozenset[str]) -> frozenset[str]:
    """Return the tokens that only one of two stems uses and that change meaning."""
    return frozenset(
        token
        for token in left ^ right
        if token in _SCENARIO_QUALIFIERS or _DESIGNATION_RE.match(token)
    )


@lru_cache(maxsize=8192)
def answer_numbers(text: str) -> frozenset[str]:
    """Return the numbers a keyed answer states (8 to 10, 30:2)."""
    return frozenset(_NUMBER_RE.findall(text or ""))


def questions_match(left: dict, right: dict) -> bool:
    """Return True when two questions ask the same thing the same way.

    The comparison is anchored on the keyed answer: two questions are treated as
    the same question when their stems are close and they expect the same
    answer.  Stems that differ only by a scenario qualifier keep a different
    keyed answer or are excluded by the qualifier guard, so they survive.
    """
    if stem_key(left) == stem_key(right):
        return True

    left_stem = content_tokens(left.get("stem", ""))
    right_stem = content_tokens(right.get("stem", ""))
    if not left_stem or not right_stem:
        return False

    stem_sim = jaccard(left_stem, right_stem)
    stem_overlap = containment(left_stem, right_stem)
    if stem_sim < STEM_TOKEN_SIMILARITY_MIN and stem_overlap < STEM_CONTAINMENT_MIN:
        return False
    if differing_qualifiers(left_stem, right_stem):
        return False

    if answer_key(left) == answer_key(right):
        # Same keyed answer: a reworded stem asks the same question.
        if stem_overlap >= SAME_ANSWER_OVERLAP_MIN:
            return True
        return (
            stem_sim >= SAME_ANSWER_TOKEN_MIN
            and sequence_ratio(left.get("stem", ""), right.get("stem", "")) >= STEM_SEQUENCE_MIN
        )

    left_answer = content_tokens(left.get("correct", ""))
    right_answer = content_tokens(right.get("correct", ""))
    if not left_answer or not right_answer:
        return False
    if stem_sim < DIFFERENT_ANSWER_STEM_MIN:
        return False
    if sequence_ratio(left.get("stem", ""), right.get("stem", "")) < DIFFERENT_ANSWER_SEQUENCE_MIN:
        return False
    left_numbers = answer_numbers(left.get("correct", ""))
    right_numbers = answer_numbers(right.get("correct", ""))
    if (left_numbers or right_numbers) and left_numbers != right_numbers:
        # The answers state different numbers, so they answer different things.
        return False
    return (
        jaccard(left_answer, right_answer) >= ANSWER_TOKEN_SIMILARITY_MIN
        and containment(left_answer, right_answer) >= ANSWER_CONTAINMENT_MIN
    )


def _keep_priority(fact: dict) -> tuple[int, int, str]:
    """Sort key that puts the harder (and more complete) question first."""
    stem = fact.get("stem", "")
    return (-difficulty_rank(fact.get("difficulty")), -len(stem), _normalized(stem))


def dedupe_questions(facts: list[dict], report: list[tuple[dict, dict]] | None = None) -> list[dict]:
    """Drop duplicate or near-duplicate questions, keeping the harder one.

    When ``report`` is given, every (kept, dropped) pair is appended to it.
    """
    kept: list[dict] = []
    kept_by_stem: dict[str, dict] = {}
    for fact in sorted(facts, key=_keep_priority):
        stem = stem_key(fact)
        match = kept_by_stem.get(stem)
        if match is None:
            match = next((other for other in kept if questions_match(fact, other)), None)
        if match is not None:
            if report is not None:
                report.append((match, fact))
            continue
        kept_by_stem[stem] = fact
        kept.append(fact)
    return kept


def merge_topic_facts(facts: list[dict]) -> list[dict]:
    """Return the merged, de-duplicated question list for one topic."""
    deduped = dedupe_questions(facts)
    deduped.sort(key=lambda f: (difficulty_rank(f.get("difficulty")), _normalized(f.get("stem", ""))))
    return deduped


def _facts_by_topic(facts: list[dict]) -> dict[str, list[dict]]:
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for fact in facts:
        by_topic[str(fact["topic"])].append(fact)
    return by_topic


def merge_facts_by_topic(facts: list[dict]) -> dict[str, list[dict]]:
    """Group facts by topic and merge each group into a single question list."""
    return {topic: merge_topic_facts(items) for topic, items in _facts_by_topic(facts).items()}


def duplicate_report(facts: list[dict]) -> list[tuple[dict, dict]]:
    """Return every (kept, dropped) question pair the merge would collapse."""
    report: list[tuple[dict, dict]] = []
    for items in _facts_by_topic(facts).values():
        dedupe_questions(items, report)
    return report
