# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""End-of-game team rosters: the team_final payload lists every team's members and final total."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest

from classquiz.socket_server import team_live


def _game(team_mode):
    return SimpleNamespace(team_mode=team_mode)


@pytest.mark.asyncio
async def test_team_final_summary_lists_members_and_totals() -> None:
    teams = {"Ada": 0, "Bob": 1, "Cy": 0}
    totals = {"0": "1200", "1": "300"}
    with (
        patch.object(team_live.PlayGame, "get_from_redis", AsyncMock(return_value=_game({"count": 2}))),
        patch.object(team_live, "get_team_map", AsyncMock(return_value=teams)),
        patch.object(team_live, "roster_usernames", AsyncMock(return_value=sorted(teams))),
        patch.object(team_live.redis, "hgetall", AsyncMock(return_value=totals)),
    ):
        summary = await team_live.team_final_summary("PIN1")

    assert summary == {
        "count": 2,
        "teams": [
            {"index": 0, "name": "Team 1", "members": ["Ada", "Cy"], "total": 1200},
            {"index": 1, "name": "Team 2", "members": ["Bob"], "total": 300},
        ],
    }


@pytest.mark.asyncio
async def test_team_final_summary_keeps_empty_team_with_zero_total() -> None:
    with (
        patch.object(team_live.PlayGame, "get_from_redis", AsyncMock(return_value=_game({"count": 2}))),
        patch.object(team_live, "get_team_map", AsyncMock(return_value={"Ada": 0})),
        patch.object(team_live, "roster_usernames", AsyncMock(return_value=["Ada"])),
        patch.object(team_live.redis, "hgetall", AsyncMock(return_value={})),
    ):
        summary = await team_live.team_final_summary("PIN2")

    assert summary["teams"][1] == {"index": 1, "name": "Team 2", "members": [], "total": 0}


@pytest.mark.asyncio
async def test_team_final_summary_is_none_without_teams() -> None:
    with patch.object(team_live.PlayGame, "get_from_redis", AsyncMock(return_value=_game(None))):
        assert await team_live.team_final_summary("PIN3") is None


@pytest.mark.asyncio
async def test_emit_team_final_sends_to_players_and_admin() -> None:
    sio = SimpleNamespace(emit=AsyncMock())
    payload = {"count": 1, "teams": []}
    with patch.object(team_live, "team_final_summary", AsyncMock(return_value=payload)):
        await team_live.emit_team_final(sio, "PIN4")

    sio.emit.assert_any_await("team_final", payload, room="PIN4")
    sio.emit.assert_any_await("team_final", payload, room="admin:PIN4")


@pytest.mark.asyncio
async def test_emit_team_final_is_silent_without_teams() -> None:
    sio = SimpleNamespace(emit=AsyncMock())
    with patch.object(team_live, "team_final_summary", AsyncMock(return_value=None)):
        await team_live.emit_team_final(sio, "PIN5")

    sio.emit.assert_not_awaited()
