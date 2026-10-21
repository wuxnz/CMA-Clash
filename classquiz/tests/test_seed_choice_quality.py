# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import math
import re
from collections import Counter, defaultdict

import pytest

from classquiz.seed.catalog import CERTIFICATIONS, TOPIC_QUESTIONS_PER_QUIZ
from classquiz.seed.fact_choice_hardening import VALID_DIFFICULTIES, _is_correct_strictly_longest
from classquiz.seed.runner import QUIZ_BANK_SIZE

pytestmark = pytest.mark.order("last")

_FORBIDDEN = re.compile(r"all of the above|none of the above", re.I)


def test_all_facts_have_valid_difficulty():
    from classquiz.seed.banks import load_all_facts

    for fact in load_all_facts():
        assert fact.get("difficulty") in VALID_DIFFICULTIES


def test_no_forbidden_choice_phrases():
    from classquiz.seed.banks import load_all_facts

    for fact in load_all_facts():
        for choice in [fact["correct"], *fact["distractors"]]:
            assert not _FORBIDDEN.search(choice)


def test_correct_longest_at_most_thirty_percent_per_quiz_chunk():
    from classquiz.seed.banks import load_all_facts

    violations = []
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for fact in load_all_facts():
        grouped[(fact["topic"], fact["difficulty"])].append(fact)
    for (topic, diff), items in grouped.items():
        items.sort(key=lambda f: f["stem"])
        chunk_size = TOPIC_QUESTIONS_PER_QUIZ.get(topic, QUIZ_BANK_SIZE)
        for start in range(0, len(items), chunk_size):
            chunk = items[start : start + chunk_size]
            longest = sum(1 for f in chunk if _is_correct_strictly_longest(f))
            allowed = max(1, int(round(len(chunk) * 0.30)))
            if longest > allowed:
                violations.append((topic, diff, start // chunk_size + 1, longest, allowed))
    assert not violations, f"Too many longest-correct chunks: {violations[:5]}"


def test_difficulty_distribution_near_targets_per_topic():
    from classquiz.seed.banks import load_all_facts

    by_topic: dict[str, Counter[str]] = defaultdict(Counter)
    for fact in load_all_facts():
        by_topic[fact["topic"]][fact["difficulty"]] += 1

    outliers = []
    for topic, counts in by_topic.items():
        n = sum(counts.values())
        if n < 10:
            continue
        for label, target in (("beginner", 0.30), ("intermediate", 0.40), ("advanced", 0.30)):
            share = counts[label] / n
            if abs(share - target) > 0.12:
                outliers.append((topic, label, share, target))
    assert not outliers, f"Difficulty skew: {outliers[:6]}"


def test_difficulty_distribution_per_certification():
    from classquiz.seed.banks import load_all_facts

    topic_to_cert = {
        slug: cert["slug"] for cert in CERTIFICATIONS for slug, _, _ in cert["topics"]
    }
    by_cert: dict[str, Counter[str]] = defaultdict(Counter)
    for fact in load_all_facts():
        by_cert[topic_to_cert[fact["topic"]]][fact["difficulty"]] += 1

    for cert, counts in by_cert.items():
        n = sum(counts.values())
        assert n > 0
        for label in VALID_DIFFICULTIES:
            assert counts[label] > 0, f"{cert} missing {label}"
