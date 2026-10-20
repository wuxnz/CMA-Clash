# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0


import uuid

from fastapi import APIRouter, HTTPException
from classquiz.battle.service import create_battle_lobby
from classquiz.db.models import User
from classquiz.config import settings
from classquiz.db.cma_models import XpSource
from classquiz.gamification.service import award_xp

settings = settings()

router = APIRouter()


@router.get("/user/{email}")
async def get_user_by_email(email: str, secret_key: str) -> User:
    if secret_key == settings.secret_key:
        return await User.objects.filter(email=email).get()
    raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/gamification/award-xp")
async def testing_award_xp(email: str, amount: int, secret_key: str):
    if secret_key != settings.secret_key:
        raise HTTPException(status_code=403, detail="Forbidden")
    user = await User.objects.get_or_none(email=email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    profile = await award_xp(user.id, amount, XpSource.QUIZ_PLAY)
    return {"total_xp": profile.total_xp, "level": profile.level}


@router.post("/battle-lobby")
async def testing_create_battle(quiz_id: str, email: str, secret_key: str):
    if secret_key != settings.secret_key:
        raise HTTPException(status_code=403, detail="Forbidden")
    user = await User.objects.get_or_none(email=email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    lobby = await create_battle_lobby(user, uuid.UUID(quiz_id), max_players=2)
    return lobby.model_dump()
