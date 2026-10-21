# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from classquiz.services.user_deletion import _delete_battle_results_for_user


@pytest.mark.asyncio
async def test_delete_battle_results_removes_participant_by_username():
    user_id = uuid.uuid4()
    user = MagicMock()
    user.id = user_id
    user.username = "Kayvon Martinez"

    row = MagicMock()
    row.winner_user_id = None
    row.player_scores = {"Kayvon Martinez": 10, "Other": 5}
    row.delete = AsyncMock()

    filter_mock = MagicMock()
    filter_mock.delete = AsyncMock()

    with patch("classquiz.services.user_deletion.BattleResult") as battle_model:
        battle_model.objects.filter.return_value = filter_mock
        battle_model.objects.all = AsyncMock(return_value=[row])

        await _delete_battle_results_for_user(user)

        filter_mock.delete.assert_awaited_once()
        row.delete.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_battle_results_skips_non_object_player_scores():
    user_id = uuid.uuid4()
    user = MagicMock()
    user.id = user_id
    user.username = "Aylo"

    bad_row = MagicMock()
    bad_row.winner_user_id = None
    bad_row.player_scores = []
    bad_row.delete = AsyncMock()

    filter_mock = MagicMock()
    filter_mock.delete = AsyncMock()

    with patch("classquiz.services.user_deletion.BattleResult") as battle_model:
        battle_model.objects.filter.return_value = filter_mock
        battle_model.objects.all = AsyncMock(return_value=[bad_row])

        await _delete_battle_results_for_user(user)

        bad_row.delete.assert_not_awaited()
