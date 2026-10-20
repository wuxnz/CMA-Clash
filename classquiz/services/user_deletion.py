# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import re
import uuid

from classquiz.cache import clear_cache_for_account
from classquiz.config import meilisearch, settings, storage
from sqlalchemy import text

from classquiz.db import database
from classquiz.db.cma_models import (
    LeaderboardScore,
    UserGamificationProfile,
    UserTopicStat,
    XpEvent,
)
from classquiz.db.models import (
    ApiKey,
    Controller,
    FidoCredentials,
    GameResults,
    Quiz,
    QuizTivity,
    QuizTivityShare,
    Rating,
    StorageItem,
    User,
    UserSession,
)

_pic_name_regex = re.compile("^.*/(.{36}--.{36})$")


async def _delete_user_storage_items(user_id: uuid.UUID) -> int:
    items = await StorageItem.objects.filter(user=user_id).all()
    deleted = 0
    for item in items:
        storage_path = item.storage_path if item.storage_path is not None else item.id.hex
        try:
            await storage.delete(storage_path)
        except Exception:
            pass
        await item.delete()
        deleted += 1
    return deleted


async def _delete_user_quizzes(user: User) -> int:
    quizzes = await Quiz.objects.filter(user_id=user.id).all()
    meili_ids: list[str] = []
    pics_to_delete: list[str] = []
    for quiz in quizzes:
        if quiz.public:
            meili_ids.append(str(quiz.id))
        for question in quiz.questions:
            try:
                image = question.get("image") if isinstance(question, dict) else question["image"]
            except (KeyError, TypeError):
                continue
            if image is not None and not str(image).startswith("https://i.imgur.com/"):
                match = _pic_name_regex.match(str(image))
                if match is not None:
                    pics_to_delete.append(match.group(1))
        await Rating.objects.filter(quiz=quiz.id).delete()
    if pics_to_delete:
        await storage.delete(pics_to_delete)
    if meili_ids:
        meilisearch.index(settings.meilisearch_index).delete_documents(meili_ids)
    count = len(quizzes)
    if count:
        await Quiz.objects.filter(user_id=user.id).delete()
    return count


async def _delete_cma_gamification(user_id: uuid.UUID) -> None:
    await UserGamificationProfile.objects.filter(user_id=user_id).delete()
    await UserTopicStat.objects.filter(user_id=user_id).delete()
    await XpEvent.objects.filter(user_id=user_id).delete()
    await LeaderboardScore.objects.filter(user_id=user_id).delete()
    uid_key = str(user_id)
    await database.execute(
        text(
            "DELETE FROM battle_results WHERE winner_user_id = :user_id "
            "OR player_scores::jsonb ? :uid_key"
        ),
        {"user_id": user_id, "uid_key": uid_key},
    )


async def delete_user_completely(user: User) -> dict:
    """Remove a user and all dependent rows (DB, storage, search index, cache)."""
    user_id = user.id
    await _delete_cma_gamification(user_id)
    await Rating.objects.filter(user=user_id).delete()
    await Controller.objects.filter(user=user_id).delete()
    await GameResults.objects.filter(user=user_id).delete()
    await QuizTivityShare.objects.filter(user=user_id).delete()
    await QuizTivity.objects.filter(user=user_id).delete()
    storage_deleted = await _delete_user_storage_items(user_id)
    quizzes_deleted = await _delete_user_quizzes(user)
    await FidoCredentials.objects.filter(user=user_id).delete()
    await ApiKey.objects.filter(user=user_id).delete()
    await UserSession.objects.filter(user=user_id).delete()
    await clear_cache_for_account(user)
    await User.objects.filter(id=user_id).delete()
    return {
        "deleted": 1,
        "quizzes_deleted": quizzes_deleted,
        "storage_items_deleted": storage_deleted,
    }


async def delete_user_by_id(user_id: uuid.UUID) -> dict | None:
    user = await User.objects.get_or_none(id=user_id)
    if user is None:
        return None
    return await delete_user_completely(user)


async def delete_user_by_username(username: str) -> dict | None:
    user = await User.objects.get_or_none(username=username)
    if user is None:
        return None
    return await delete_user_completely(user)


async def delete_user_by_email(email: str) -> dict | None:
    user = await User.objects.get_or_none(email=email)
    if user is None:
        return None
    return await delete_user_completely(user)
