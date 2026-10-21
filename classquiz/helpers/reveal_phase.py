# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Reveal phase timing and answer labels for live question_results."""

from __future__ import annotations

import re

from classquiz.db.models import QuizQuestion, QuizQuestionType

REVEAL_HOLD_MIN_SEC = 8.0
REVEAL_HOLD_MAX_SEC = 20.0
REVEAL_WORDS_PER_EXTRA_SEC = 15


def count_words(text: str | None) -> int:
    if not text or not str(text).strip():
        return 0
    return len(re.findall(r"\b\w+\b", str(text)))


def compute_reveal_hold_sec(explanation: str | None) -> float:
    """Hold result + explanation before scoreboard: 8s base + ~1s per 15 words, max 20s."""
    extra = count_words(explanation) // REVEAL_WORDS_PER_EXTRA_SEC
    return min(REVEAL_HOLD_MAX_SEC, REVEAL_HOLD_MIN_SEC + float(extra))


def correct_answer_label(question: QuizQuestion) -> str | None:
    """Human-readable correct answer for reveal (no solution leak during question phase)."""
    q_type = question.type or QuizQuestionType.ABCD
    if q_type == QuizQuestionType.ABCD:
        answers = question.answers
        if not isinstance(answers, list):
            return None
        labels = [a.answer for a in answers if getattr(a, "right", False)]
        return "; ".join(labels) if labels else None
    if q_type == QuizQuestionType.VOTING:
        return None
    if q_type == QuizQuestionType.RANGE:
        if hasattr(question.answers, "min"):
            return f"{question.answers.min} to {question.answers.max}"
        return None
    if q_type in (QuizQuestionType.TEXT, QuizQuestionType.ORDER, QuizQuestionType.CHECK):
        answers = question.answers
        if isinstance(answers, list) and answers:
            first = answers[0]
            if hasattr(first, "answer"):
                return str(first.answer)
        return None
    return None
