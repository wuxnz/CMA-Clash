# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import asyncio
import logging
import re
import uuid

from classquiz.cache import clear_cache_for_account
from classquiz.config import meilisearch, settings, storage
from classquiz.db import database
from classquiz.db.cma_models import (
    BattleResult,
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

LOGGER = logging.getLogger(__name__)

DELETE_USER_TIMEOUT_SECONDS = 30
MEILI_DELETE_TIMEOUT_SECONDS = 10

_pic_name_regex = re.compile("^.*/(.{36}--.{36})$")

async def _delete_battle_results_for_user(user: User) -> None:
    """Remove battle rows for this user (winner and participant).

    player_scores keys are display names (see gamification.record_battle_result), not user UUIDs.
    Avoid jsonb_exists in bulk SQL: non-object JSON values can raise and abort the delete transaction.
    """
    user_id = user.id
    username = user.username
    uid_key = str(user_id)
    await BattleResult.objects.filter(winner_user_id=user_id).delete()
    for row in await BattleResult.objects.all():
        scores = row.player_scores
        if not isinstance(scores, dict):
            continue
        if username in scores or uid_key in scores:
            await row.delete()


async def _remove_storage_item_rows(user_id: uuid.UUID) -> list[str]:
    items = await StorageItem.objects.filter(user=user_id).all()
    paths: list[str] = []
    for item in items:
        storage_path = item.storage_path if item.storage_path is not None else item.id.hex
        paths.append(storage_path)
        await item.delete()
    return paths


async def _delete_storage_paths(paths: list[str]) -> None:
    if not paths:
        return
    try:
        await storage.delete(paths)
    except Exception:
        LOGGER.exception("Failed to delete %d storage file(s)", len(paths))


async def _collect_quiz_cleanup(user: User) -> tuple[list[str], list[str]]:
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
    return pics_to_delete, meili_ids


async def _delete_user_quizzes_in_db(user: User) -> int:
    quizzes = await Quiz.objects.filter(user_id=user.id).all()
    for quiz in quizzes:
        await Rating.objects.filter(quiz=quiz.id).delete()
    count = len(quizzes)
    if count:
        await Quiz.objects.filter(user_id=user.id).delete()
    return count


async def _delete_meilisearch_docs(doc_ids: list[str]) -> None:
    if not doc_ids:
        return

    def _delete():
        meilisearch.index(settings.meilisearch_index).delete_documents(doc_ids)

    try:
        await asyncio.wait_for(
            asyncio.to_thread(_delete),
            timeout=MEILI_DELETE_TIMEOUT_SECONDS,
        )
    except Exception:
        LOGGER.exception("Meilisearch delete failed for %d quiz document(s)", len(doc_ids))


async def _delete_user_db_rows(user_id: uuid.UUID, user: User) -> tuple[int, list[str]]:
    await UserGamificationProfile.objects.filter(user_id=user_id).delete()
    await UserTopicStat.objects.filter(user_id=user_id).delete()
    await XpEvent.objects.filter(user_id=user_id).delete()
    await LeaderboardScore.objects.filter(user_id=user_id).delete()
    await _delete_battle_results_for_user(user)
    await Rating.objects.filter(user=user_id).delete()
    await Controller.objects.filter(user=user_id).delete()
    await GameResults.objects.filter(user=user_id).delete()
    await QuizTivityShare.objects.filter(user=user_id).delete()
    await QuizTivity.objects.filter(user=user_id).delete()
    quizzes_deleted = await _delete_user_quizzes_in_db(user)
    storage_paths = await _remove_storage_item_rows(user_id)
    await FidoCredentials.objects.filter(user=user_id).delete()
    await ApiKey.objects.filter(user=user_id).delete()
    await UserSession.objects.filter(user=user_id).delete()
    await User.objects.filter(id=user_id).delete()
    return quizzes_deleted, storage_paths


async def _delete_user_completely_impl(user: User) -> dict:
    """Remove a user and all dependent rows (DB, storage, search index, cache)."""
    user_id = user.id
    pics_to_delete, meili_ids = await _collect_quiz_cleanup(user)

    async with database.transaction():
        quizzes_deleted, storage_paths = await _delete_user_db_rows(user_id, user)

    await _delete_storage_paths(pics_to_delete + storage_paths)
    await _delete_meilisearch_docs(meili_ids)
    await clear_cache_for_account(user)

    return {
        "deleted": 1,
        "quizzes_deleted": quizzes_deleted,
        "storage_items_deleted": len(storage_paths),
    }


async def delete_user_completely(user: User) -> dict:
    return await asyncio.wait_for(_delete_user_completely_impl(user), timeout=DELETE_USER_TIMEOUT_SECONDS)


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
