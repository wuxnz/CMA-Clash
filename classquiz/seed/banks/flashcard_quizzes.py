# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Quiz questions built from the flashcard decks in classquiz/seed/flashcards.

Each flashcard becomes one multiple-choice question: the front is the prompt and the back,
unchanged, is the correct answer. Distractors are backs from the same category that echo
the prompt's words where possible, so the right answer is not the only option that
repeats the question.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import random
import sys
from pathlib import Path

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact
from classquiz.seed.stem_normalize import normalize_stem

_DECK_DIR = Path(__file__).resolve().parent.parent / "flashcards"

# Difficulty follows a fixed 30/40/30 pattern across each deck's cards.
_DIFFICULTY_CYCLE = ("beginner",) * 3 + ("intermediate",) * 4 + ("advanced",) * 3

_DECKS = (
    {
        "file": "phlebotomy.json",
        "topic": "phlebotomy-flashcards-quiz",
        "references": [S.WHO_PHLBOTOMY],
        "stem": lambda card: f"What does '{card['t']}' mean?",
    },
    {
        "file": "diabetes.json",
        "topic": "diabetes-flashcards-quiz",
        "references": [S.CDC_DIABETES],
        "stem": lambda card: card["t"],
    },
)


def _load_deck(file_name: str) -> dict:
    return json.loads((_DECK_DIR / file_name).read_text(encoding="utf-8"))


def _rng(seed_text: str) -> random.Random:
    return random.Random(int(hashlib.sha256(seed_text.encode("utf-8")).hexdigest()[:16], 16))


def _distractors(card: dict, rng: random.Random) -> list[str]:
    """Three of the card's four written wrong answers, chosen with this quiz's seed.

    The right answer should not be the longest option every time, which is a test-taking
    clue. Choices that keep the right answer from being the longest are preferred.
    """
    wrong = list(card["w"])
    if len(wrong) < 3:
        sys.exit(f"card {card['t']!r} needs at least three wrong answers")
    combos = [list(combo) for combo in itertools.combinations(wrong, 3)]
    right_len = len(card["d"])
    balanced = [combo for combo in combos if max(len(text) for text in combo) >= right_len]
    return rng.choice(balanced or combos)


def _unique_prompts(deck_def: dict, cards: list[dict], categories: list[str]) -> list[str]:
    """Question text for each card. Cards that share a term (ACD, CBC, PT and Pt) get a
    different wording so each question is kept by the seed's duplicate check."""
    used: set[str] = set()
    prompts: list[str] = []
    for card in cards:
        candidates = [
            deck_def["stem"](card),
            f"What does the abbreviation '{card['t']}' stand for?",
            f"{deck_def['stem'](card)} ({categories[card['c']]})",
        ]
        for candidate in candidates:
            if normalize_stem(candidate) not in used:
                break
        used.add(normalize_stem(candidate))
        prompts.append(candidate)
    return prompts


def _deck_facts(deck_def: dict) -> list[dict]:
    deck = _load_deck(deck_def["file"])
    cards = deck["cards"]
    prompts = _unique_prompts(deck_def, cards, deck["categories"])
    facts: list[dict] = []
    for i, card in enumerate(cards):
        rng = _rng(f"{deck_def['topic']}:{i}")
        prompt = prompts[i]
        facts.append(
            fact(
                deck_def["topic"],
                prompt,
                card["d"],
                _distractors(card, rng),
                f"{card['t']}: {card['d']}",
                deck_def["references"],
                _DIFFICULTY_CYCLE[i % len(_DIFFICULTY_CYCLE)],
            )
        )
    return facts

FACTS: list[dict] = [fact_ for deck_def in _DECKS for fact_ in _deck_facts(deck_def)]
