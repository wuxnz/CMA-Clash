# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest

pytestmark = pytest.mark.order("last")


@pytest.mark.asyncio
async def test_run_seed_updates_without_duplicating_quizzes():
    from classquiz.db import database
    from classquiz.db.models import Quiz
    from classquiz.seed.runner import SEED_USER_EMAIL, run_seed

    if not database.is_connected:
        await database.connect()
    first = await run_seed(force=True)
    count_after_first = await Quiz.objects.exclude(seed_slug=None).count()
    second = await run_seed(force=True)
    count_after_second = await Quiz.objects.exclude(seed_slug=None).count()
    assert count_after_first == count_after_second
    assert second.get("quizzes_created", 0) == 0
    assert second.get("quizzes_updated", 0) >= 1
    from classquiz.db.models import User

    seed_user = await User.objects.get_or_none(email=SEED_USER_EMAIL)
    assert seed_user is not None
    user_quizzes = await Quiz.objects.filter(user_id=seed_user.id).exclude(seed_slug=None).all()
    slugs = [q.seed_slug for q in user_quizzes]
    assert len(slugs) == len(set(slugs))
    for quiz in user_quizzes:
        assert len(quiz.questions) >= 25
        assert quiz.questions_per_game == 10
