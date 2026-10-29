# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Quiz questions built from the flashcard decks in classquiz/seed/flashcards.

Each flashcard becomes one multiple-choice question in the forward direction: the
front is the prompt and the back is the correct answer. Distractors are backs from
the same category at a similar length, so the correct answer is not the obvious
pick. The site's practice tests ask the reverse direction, so the quiz and practice
questions never share the same prompt and answer pair.
"""

from __future__ import annotations

import hashlib
import json
import random
import re
from pathlib import Path

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

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


def _words(text: str) -> set[str]:
    return set(re.findall(r"[a-z]{5,}", text.lower()))


def _distractors(cards: list[dict], index: int, prompt: str, rng: random.Random) -> list[str]:
    """Three wrong answers from the same category.

    Wrong answers that repeat the prompt's words come first, so the right answer is
    not the only option that echoes the question. Within that, lengths stay close.
    """
    card = cards[index]
    answer = card["d"]
    prompt_words = _words(prompt)
    same_category = [
        j for j, other in enumerate(cards) if j != index and other["c"] == card["c"] and other["d"] != answer
    ]
    pool = same_category
    if len(pool) < 3:
        pool = [j for j, other in enumerate(cards) if j != index and other["d"] != answer]
    ranked = sorted(
        pool,
        key=lambda j: (
            -len(_words(cards[j]["d"]) & prompt_words),
            abs(len(cards[j]["d"]) - len(answer)),
            j,
        ),
    )
    picked: list[str] = []
    for j in rng.sample(ranked[:6], 3):
        text = cards[j]["d"]
        if text not in picked:
            picked.append(text)
    return picked


_COMMON_WORDS = frozenset(
    """
    about their there these those which where while would could should being through between
    thought cause causes people group groups what does mean have with from this that into other
    after before many much more most some such when your they them will just only also
    """.split()
)


def _key_words(prompt: str) -> set[str]:
    return {w for w in _words(prompt) if w not in _COMMON_WORDS}


def _mask(text: str, key: set[str]) -> str:
    """Blank out the prompt's key words so an option cannot echo the question."""
    for word in sorted(key, key=len, reverse=True):
        text = re.sub(rf"\b{re.escape(word)}\b", "____", text, flags=re.IGNORECASE)
    return text


def _deck_facts(deck_def: dict) -> list[dict]:
    deck = _load_deck(deck_def["file"])
    cards = deck["cards"]
    facts: list[dict] = []
    for i, card in enumerate(cards):
        rng = _rng(f"{deck_def['topic']}:{i}")
        prompt = deck_def["stem"](card)
        key = _key_words(prompt)
        distractors = [_mask(text, key) for text in _distractors(cards, i, prompt, rng)]
        facts.append(
            fact(
                deck_def["topic"],
                prompt,
                _mask(card["d"], key),
                distractors,
                f"{card['t']}: {card['d']}",
                deck_def["references"],
                _DIFFICULTY_CYCLE[i % len(_DIFFICULTY_CYCLE)],
            )
        )
    return facts


FACTS: list[dict] = [fact_ for deck_def in _DECKS for fact_ in _deck_facts(deck_def)]
