# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import random

from classquiz.helpers.game_questions import (
    DEFAULT_QUESTIONS_PER_GAME,
    MIN_QUESTIONS_PER_GAME,
    resolve_questions_per_game,
    select_questions_for_game,
)


def _make_bank(n: int) -> list[dict]:
    return [{"question": f"Q{i}"} for i in range(n)]


def test_resolve_questions_per_game_caps_at_bank():
    assert resolve_questions_per_game(5, 10) == 5
    assert resolve_questions_per_game(30, 10) == 10


def test_resolve_questions_per_game_minimum_when_bank_allows():
    assert resolve_questions_per_game(30, 6) == MIN_QUESTIONS_PER_GAME
    assert resolve_questions_per_game(30, None) == DEFAULT_QUESTIONS_PER_GAME


def test_select_questions_sample_size_and_no_repeats():
    bank = _make_bank(30)
    rng = random.Random(42)
    picked = select_questions_for_game(bank, 10, rng=rng)
    assert len(picked) == 10
    assert len({q["question"] for q in picked}) == 10


def test_select_questions_order_varies():
    bank = _make_bank(30)
    a = [q["question"] for q in select_questions_for_game(bank, 10, rng=random.Random(1))]
    b = [q["question"] for q in select_questions_for_game(bank, 10, rng=random.Random(2))]
    assert a != b


def test_small_bank_uses_all_questions():
    bank = _make_bank(5)
    picked = select_questions_for_game(bank, 10, rng=random.Random(0))
    assert len(picked) == 5
    assert {q["question"] for q in picked} == {f"Q{i}" for i in range(5)}


def test_host_and_player_share_redis_game_questions():
    """Simulate start_quiz sampling persisted on PlayGame (same list for all clients)."""
    from classquiz.db.models import PlayGame

    bank = _make_bank(28)
    game_questions = select_questions_for_game(bank, 10, rng=random.Random(99))
    game = PlayGame(
        quiz_id="00000000-0000-0000-0000-000000000001",
        game_pin="123456",
        questions=game_questions,
        game_id="00000000-0000-0000-0000-000000000002",
        title="Test",
        description="",
        user_id="00000000-0000-0000-0000-000000000003",
    )
    host_count = len(game.questions)
    player_payload = game.to_player_data()
    assert player_payload["question_count"] == host_count
    assert host_count == 10
