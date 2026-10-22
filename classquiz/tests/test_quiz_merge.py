# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest

from classquiz.seed.quiz_merge import (
    dedupe_questions,
    difficulty_rank,
    merge_facts_by_topic,
    merge_topic_facts,
    questions_match,
)


def _fact(stem: str, correct: str, difficulty: str = "intermediate", topic: str = "demo") -> dict:
    return {
        "topic": topic,
        "stem": stem,
        "correct": correct,
        "distractors": ["Wrong one", "Wrong two", "Wrong three"],
        "explanation": "Because.",
        "references": [],
        "difficulty": difficulty,
    }


def test_dedupe_keeps_the_harder_question():
    easy = _fact("What is the normal resting pulse rate for an adult?", "60 to 100 bpm", "beginner")
    hard = _fact(
        "What resting pulse rate is considered normal for a healthy adult?",
        "60 to 100 bpm",
        "advanced",
    )
    kept = dedupe_questions([easy, hard])
    assert len(kept) == 1
    assert kept[0]["difficulty"] == "advanced"


def test_questions_that_differ_by_a_scenario_qualifier_are_kept():
    single = _fact(
        "What compression-to-ventilation ratio should a single rescuer use during adult BLS CPR?",
        "30:2",
        "beginner",
    )
    two = _fact(
        "What compression-to-ventilation ratio should two rescuers use during adult BLS CPR?",
        "30:2",
        "advanced",
    )
    assert not questions_match(single, two)
    assert len(dedupe_questions([single, two])) == 2


def test_questions_that_differ_by_a_measurement_are_kept():
    light_blue = _fact(
        "After filling a light blue sodium citrate tube, how many gentle inversions does CLSI typically recommend?",
        "3 to 4 gentle end-over-end inversions",
    )
    lavender = _fact(
        "After filling a lavender EDTA tube for hematology, how many gentle inversions does CLSI typically recommend?",
        "8 to 10 gentle end-over-end inversions",
    )
    assert not questions_match(light_blue, lavender)
    assert len(dedupe_questions([light_blue, lavender])) == 2


def test_reworded_question_with_the_same_answer_is_dropped():
    first = _fact("What does the ST segment represent on the ECG?", "Early ventricular repolarization plateau")
    second = _fact("What does the ST segment represent on an ECG?", "Early ventricular repolarization plateau")
    assert questions_match(first, second)
    assert len(dedupe_questions([first, second])) == 1


def test_merge_groups_by_topic_and_keeps_every_tier():
    facts = [
        _fact("Beginner question about hand hygiene?", "Soap and water", "beginner", topic="a"),
        _fact("Advanced question about hand hygiene?", "Alcohol based rub", "advanced", topic="a"),
        _fact("Another topic question?", "Yes", "intermediate", topic="b"),
    ]
    merged = merge_facts_by_topic(facts)
    assert set(merged) == {"a", "b"}
    assert len(merged["a"]) == 2
    assert len(merged["b"]) == 1


def test_merged_questions_are_ordered_by_tier():
    facts = [
        _fact("Advanced question?", "Yes", "advanced"),
        _fact("Beginner question?", "Yes", "beginner"),
        _fact("Intermediate question?", "Yes", "intermediate"),
    ]
    merged = merge_topic_facts(facts)
    assert [f["difficulty"] for f in merged] == ["beginner", "intermediate", "advanced"]


def test_difficulty_rank_orders_tiers():
    assert difficulty_rank("advanced") > difficulty_rank("intermediate")
    assert difficulty_rank("intermediate") > difficulty_rank("beginner")
    assert difficulty_rank(None) == 0


def test_seed_bank_has_no_duplicate_questions_per_topic():
    from classquiz.seed.banks import load_all_facts

    merged = merge_facts_by_topic(load_all_facts())
    for topic, items in merged.items():
        stems = [fact["stem"] for fact in items]
        assert len(stems) == len(set(stems)), f"duplicate stem in {topic}"


@pytest.mark.parametrize(
    "first,second",
    [
        (
            "Which anatomical landmark is used to place precordial lead V1?",
            "Which anatomical landmark is used to place precordial lead V2?",
        ),
        (
            "What must rescuers do immediately before the AED delivers a shock?",
            "Immediately after the AED delivers a shock, what should rescuers do?",
        ),
        (
            "What does the combining form dermat/o refer to?",
            "What does the combining form gastr/o refer to?",
        ),
    ],
)
def test_distinct_questions_are_not_collapsed(first, second):
    left = _fact(first, "Answer one")
    right = _fact(second, "Answer two")
    assert not questions_match(left, right)
