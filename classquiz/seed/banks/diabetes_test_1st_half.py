# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Questions for the "Diabetes Test 1st Half" topic.

The cards live in classquiz/seed/flashcards/diabetes-test-1st-half.json, one card per distinct question
in the order of the handwritten notes (a repeated page or repeated question appears once).
"""

from __future__ import annotations

import json
from pathlib import Path

from classquiz.seed.banks._builder import fact

TOPIC = "diabetes-test-1st-half"

_DECK_FILE = Path(__file__).resolve().parent.parent / "flashcards" / "diabetes-test-1st-half.json"

_DIFFICULTY_CYCLE = ("beginner",) * 3 + ("intermediate",) * 4 + ("advanced",) * 3


def load_deck() -> dict:
    """Return the parsed deck: ``categories`` and ``cards`` in note order."""
    return json.loads(_DECK_FILE.read_text(encoding="utf-8"))


def _facts() -> list[dict]:
    cards = load_deck()["cards"]
    return [
        fact(
            TOPIC,
            card["t"],
            card.get("qd", card["d"]),
            card.get("qw", card["w"]),
            card["e"],
            [card["u"]],
            _DIFFICULTY_CYCLE[i % len(_DIFFICULTY_CYCLE)],
        )
        for i, card in enumerate(cards)
    ]


FACTS: list[dict] = _facts()