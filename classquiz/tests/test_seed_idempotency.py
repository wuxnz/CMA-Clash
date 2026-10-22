# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest

pytestmark = pytest.mark.order("last")


@pytest.mark.asyncio
async def test_run_seed_updates_without_duplicating_quizzes():
    from classquiz.db import database
    from classquiz.db.models import Quiz
    from classquiz.seed.runner import MIXED_DIFFICULTY, SEED_USER_EMAIL, run_seed

    if not database.is_connected:
        await database.connect()
        connected_here = True
    else:
        connected_here = False
    try:
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
            # A merged quiz holds every tier of one topic, so it is only
            # required to hold at least one question.
            assert len(quiz.questions) >= 1
            assert quiz.questions_per_game == 10
    finally:
        # Release the connection so a later module's event loop can use the database.
        if connected_here:
            await database.disconnect()


@pytest.mark.asyncio
async def test_seed_publishes_one_quiz_per_topic():
    from classquiz.db import database
    from classquiz.db.cma_models import Topic
    from classquiz.db.models import Quiz, User
    from classquiz.seed.runner import MIXED_DIFFICULTY, SEED_USER_EMAIL, run_seed

    if not database.is_connected:
        await database.connect()
        connected_here = True
    else:
        connected_here = False
    try:
        await run_seed(force=True)
        seed_user = await User.objects.get_or_none(email=SEED_USER_EMAIL)
        assert seed_user is not None
        public_seed_quizzes = await Quiz.objects.filter(
            user_id=seed_user.id, public=True
        ).exclude(seed_slug=None).all()
        titles = [quiz.title for quiz in public_seed_quizzes]
        assert len(titles) == len(set(titles)), f"Duplicate public quiz titles: {titles}"

        topics = await Topic.objects.all()
        assert len(public_seed_quizzes) == len(topics)
        for quiz in public_seed_quizzes:
            assert quiz.difficulty == MIXED_DIFFICULTY
            assert len(quiz.questions) >= 1
            # A merged quiz must not repeat the same question.
            stems = [q["question"] for q in quiz.questions]
            assert len(stems) == len(set(stems))
    finally:
        if connected_here:
            await database.disconnect()
