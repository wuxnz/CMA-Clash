# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import json
import secrets
import uuid
from random import randint

from classquiz.config import redis
from classquiz.db.cma_models import BattleLobbyState
from classquiz.db.models import GameInLobby, PlayGame, Quiz, User

BATTLE_REDIS_PREFIX = "cma_battle"
LOBBY_TTL = 3600


def _lobby_key(code: str) -> str:
    return f"{BATTLE_REDIS_PREFIX}:lobby:{code}"


def _generate_battle_code() -> str:
    return f"{randint(100000, 999999)}"


async def create_battle_lobby(
    host: User,
    quiz_id: uuid.UUID,
    max_players: int = 4,
    certification_slug: str | None = None,
) -> BattleLobbyState:
    code = _generate_battle_code()
    while await redis.get(_lobby_key(code)) is not None:
        code = _generate_battle_code()
    lobby = BattleLobbyState(
        battle_code=code,
        quiz_id=str(quiz_id),
        host_user_id=str(host.id),
        max_players=max(2, min(max_players, 8)),
        player_slots=[
            {
                "user_id": str(host.id),
                "username": host.username,
                "ready": True,
            }
        ],
        certification_slug=certification_slug,
    )
    await redis.set(_lobby_key(code), lobby.model_dump_json(), ex=LOBBY_TTL)
    return lobby


async def create_battle_lobby_guest(
    display_name: str,
    quiz_id: uuid.UUID,
    max_players: int = 4,
    certification_slug: str | None = None,
) -> BattleLobbyState:
    name = display_name.strip()
    if len(name) < 2:
        raise ValueError("invalid_display_name")
    guest_id = str(uuid.uuid4())
    host_secret = secrets.token_urlsafe(24)
    code = _generate_battle_code()
    while await redis.get(_lobby_key(code)) is not None:
        code = _generate_battle_code()
    lobby = BattleLobbyState(
        battle_code=code,
        quiz_id=str(quiz_id),
        host_user_id=guest_id,
        max_players=max(2, min(max_players, 8)),
        player_slots=[
            {
                "user_id": guest_id,
                "username": name,
                "ready": True,
                "guest": True,
            }
        ],
        certification_slug=certification_slug,
        host_secret=host_secret,
        host_is_guest=True,
    )
    await redis.set(_lobby_key(code), lobby.model_dump_json(), ex=LOBBY_TTL)
    return lobby


async def get_battle_lobby(code: str) -> BattleLobbyState | None:
    raw = await redis.get(_lobby_key(code))
    if raw is None:
        return None
    return BattleLobbyState.model_validate_json(raw)


async def join_battle_lobby(code: str, user: User) -> BattleLobbyState:
    lobby = await get_battle_lobby(code)
    if lobby is None:
        raise ValueError("lobby_not_found")
    if lobby.status != "waiting":
        raise ValueError("lobby_started")
    for slot in lobby.player_slots:
        if slot["user_id"] == str(user.id):
            return lobby
    if len(lobby.player_slots) >= lobby.max_players:
        raise ValueError("lobby_full")
    lobby.player_slots.append(
        {"user_id": str(user.id), "username": user.username, "ready": True}
    )
    await redis.set(_lobby_key(code), lobby.model_dump_json(), ex=LOBBY_TTL)
    return lobby


async def join_battle_lobby_guest(
    code: str,
    display_name: str,
    guest_player_id: str | None = None,
) -> tuple[BattleLobbyState, str]:
    name = display_name.strip()
    if len(name) < 2:
        raise ValueError("invalid_display_name")
    lobby = await get_battle_lobby(code)
    if lobby is None:
        raise ValueError("lobby_not_found")
    if lobby.status != "waiting":
        raise ValueError("lobby_started")
    player_id = guest_player_id or str(uuid.uuid4())
    for slot in lobby.player_slots:
        if slot["user_id"] == player_id:
            slot["username"] = name
            await redis.set(_lobby_key(code), lobby.model_dump_json(), ex=LOBBY_TTL)
            return lobby, player_id
    if len(lobby.player_slots) >= lobby.max_players:
        raise ValueError("lobby_full")
    lobby.player_slots.append(
        {"user_id": player_id, "username": name, "ready": True, "guest": True}
    )
    await redis.set(_lobby_key(code), lobby.model_dump_json(), ex=LOBBY_TTL)
    return lobby, player_id


async def start_battle_game(
    code: str,
    requesting_user_id: uuid.UUID | None = None,
    host_secret: str | None = None,
) -> BattleLobbyState:
    lobby = await get_battle_lobby(code)
    if lobby is None:
        raise ValueError("lobby_not_found")
    if lobby.status != "waiting":
        return lobby
    if lobby.host_secret:
        if not host_secret or host_secret != lobby.host_secret:
            raise ValueError("not_host")
    elif requesting_user_id is None or str(requesting_user_id) != lobby.host_user_id:
        raise ValueError("not_host")
    if len(lobby.player_slots) < 2:
        raise ValueError("need_two_players")
    quiz = await Quiz.objects.get_or_none(id=uuid.UUID(lobby.quiz_id))
    if quiz is None:
        raise ValueError("quiz_not_found")
    quiz_owner_id = quiz.user_id.id if hasattr(quiz.user_id, "id") else quiz.user_id
    game_pin = randint(100000, 999999)
    while await redis.get(f"game:{game_pin}") is not None:
        game_pin = randint(100000, 999999)
    game_id = uuid.uuid4()
    game = PlayGame(
        quiz_id=quiz.id,
        game_pin=str(game_pin),
        questions=quiz.questions,
        game_id=game_id,
        title=quiz.title,
        description=quiz.description or "",
        captcha_enabled=False,
        cover_image=quiz.cover_image,
        game_mode="battle",
        user_id=quiz_owner_id,
        background_color=quiz.background_color,
        background_image=quiz.background_image,
    )
    await redis.set(f"game:{game.game_pin}", game.model_dump_json(), ex=18000)
    if not lobby.host_is_guest:
        await redis.set(
            f"game_in_lobby:{uuid.UUID(lobby.host_user_id).hex}",
            GameInLobby(game_id=game.game_id, game_pin=str(game_pin), quiz_title=quiz.title).model_dump_json(),
            ex=900,
        )
    await redis.set(
        f"{BATTLE_REDIS_PREFIX}:meta:{game_pin}",
        json.dumps({"battle_code": code, "player_user_ids": {s["username"]: s["user_id"] for s in lobby.player_slots}}),
        ex=18000,
    )
    lobby.status = "started"
    lobby.game_pin = str(game_pin)
    lobby.game_id = str(game_id)
    await redis.set(_lobby_key(code), lobby.model_dump_json(), ex=LOBBY_TTL)
    return lobby


async def enqueue_matchmaking(user: User, certification_slug: str) -> str | None:
    queue_key = f"{BATTLE_REDIS_PREFIX}:queue:{certification_slug}"
    entry = json.dumps({"user_id": str(user.id), "username": user.username})
    await redis.rpush(queue_key, entry)
    await redis.expire(queue_key, 600)
    return await try_match_players(certification_slug)


async def try_match_players(certification_slug: str) -> str | None:
    queue_key = f"{BATTLE_REDIS_PREFIX}:queue:{certification_slug}"
    length = await redis.llen(queue_key)
    if length < 2:
        return None
    p1 = json.loads(await redis.lpop(queue_key))
    p2 = json.loads(await redis.lpop(queue_key))
    from classquiz.db.cma_models import Certification, Topic

    cert = await Certification.objects.get_or_none(slug=certification_slug)
    if cert is None:
        return None
    topic = await Topic.objects.filter(certification=cert.id).order_by("sort_order").first()
    if topic is None:
        return None
    quiz = (
        await Quiz.objects.filter(topic_id=topic.id, public=True)
        .order_by("-updated_at")
        .first()
    )
    if quiz is None:
        quiz = await Quiz.objects.filter(public=True).order_by("-updated_at").first()
    if quiz is None:
        return None
    host = await User.objects.get_or_none(id=uuid.UUID(p1["user_id"]))
    if host is None:
        return None
    lobby = await create_battle_lobby(host, quiz.id, max_players=2, certification_slug=certification_slug)
    guest = await User.objects.get_or_none(id=uuid.UUID(p2["user_id"]))
    if guest is not None:
        await join_battle_lobby(lobby.battle_code, guest)
    await start_battle_game(lobby.battle_code, host.id)
    refreshed = await get_battle_lobby(lobby.battle_code)
    return refreshed.game_pin if refreshed else None
