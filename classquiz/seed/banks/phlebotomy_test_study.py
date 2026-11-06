# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Questions for the "Phlebotomy Test Study Guide" topic.

The cards live in classquiz/seed/flashcards/phlebotomy-test-study.json. The same file drives the
study guide, the battle and match quiz, the flashcards, and the randomized practice test.
"""

from __future__ import annotations

import json
from pathlib import Path

from classquiz.seed.banks._builder import fact

TOPIC = "phlebotomy-test-study"

_DECK_FILE = Path(__file__).resolve().parent.parent / "flashcards" / "phlebotomy-test-study.json"

_DIFFICULTY_CYCLE = ("beginner",) * 3 + ("intermediate",) * 4 + ("advanced",) * 3


def load_deck() -> dict:
    """Return the parsed deck: ``categories`` and ``cards`` in source order."""
    return json.loads(_DECK_FILE.read_text(encoding="utf-8"))


def _facts() -> list[dict]:
    cards = load_deck()["cards"]
    return [
        fact(
            TOPIC,
            card["t"],
            card["d"],
            card["w"],
            card["e"],
            [card["u"]],
            _DIFFICULTY_CYCLE[i % len(_DIFFICULTY_CYCLE)],
        )
        for i, card in enumerate(cards)
    ]


FACTS: list[dict] = _facts()
