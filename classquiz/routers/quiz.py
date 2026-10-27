# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0


import json
import random
import re
import uuid
from datetime import datetime
from random import randint

import ormar.exceptions

from classquiz.helpers import generate_spreadsheet, handle_import_from_excel
from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile, File
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import ValidationError, BaseModel

from classquiz.auth import get_current_user, get_current_user_optional
from classquiz.rate_limit import rate_limit_request
from classquiz.config import redis, settings, storage, meilisearch
from classquiz.db.models import Quiz, User, PlayGame, GameInLobby, QuizQuestion, QuizQuestionType
from classquiz.helpers.box_controller import generate_code
from classquiz.helpers.game_questions import select_questions_for_game
from classquiz.kahoot_importer.import_quiz import import_quiz
import urllib.parse

settings = settings()

router = APIRouter()


@router.get("/get/{quiz_id}")
async def get_quiz_from_id(quiz_id: str, user: User | None = Depends(get_current_user)):
    try:
        quiz_id = uuid.UUID(quiz_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="badly formed quiz id")
    if user is None:
        quiz = await Quiz.objects.get_or_none(id=quiz_id, public=True)
    else:
        quiz = await Quiz.objects.get_or_none(id=quiz_id, user_id=user.id)
    if quiz is None:
        public_quiz = await Quiz.objects.get_or_none(id=quiz_id, public=True)
        if public_quiz is None:
            return JSONResponse(status_code=404, content={"detail": "quiz not found"})
        else:
            return public_quiz
    else:
        return quiz


class PublicQuizResponseUser(BaseModel):
    username: str
    id: uuid.UUID


class PublicQuizResponse(Quiz.get_pydantic(exclude={"questions"})):
    user_id: PublicQuizResponseUser
    questions: list[QuizQuestion]
    likes: int
    dislikes: int
    views: int
    plays: int


@router.get("/get/public/{quiz_id}")
async def get_public_quiz(quiz_id: uuid.UUID):
    quiz = await Quiz.objects.select_related("user_id").get_or_none(id=quiz_id)
    if quiz is None:
        return JSONResponse(status_code=404, content={"detail": "quiz not found"})
    else:
        quiz.views += 1
        await quiz.update()
        return PublicQuizResponse(**quiz.model_dump())


ANON_QUIZ_START_LIMIT = 12
ANON_QUIZ_START_WINDOW_SEC = 3600


@router.post("/start/{quiz_id}")
async def start_quiz(
    request: Request,
    quiz_id: str,
    game_mode: str,
    captcha_enabled: bool = True,
    custom_field: str | None = None,
    cqcs_enabled: bool = False,
    randomize_answers: bool = False,
    team_count: int = 0,
    team_assign: str = "random",
    user: User | None = Depends(get_current_user_optional),
):
    try:
        quiz_id = uuid.UUID(quiz_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="badly formed quiz id")
    quiz = None
    if user is not None:
        quiz = await Quiz.objects.get_or_none(id=quiz_id, user_id=user.id)
    if quiz is None:
        quiz = await Quiz.objects.get_or_none(id=quiz_id, public=True)
    if quiz is None:
        return JSONResponse(status_code=404, content={"detail": "quiz not found"})
    if user is None:
        await rate_limit_request(
            request,
            "quiz_start_anon",
            limit=ANON_QUIZ_START_LIMIT,
            window_sec=ANON_QUIZ_START_WINDOW_SEC,
        )
    host_user_id = user.id if user is not None else (
        quiz.user_id.id if hasattr(quiz.user_id, "id") else quiz.user_id
    )
    quiz.plays += 1
    await quiz.update()
    game_pin = randint(100000, 999999)
    if custom_field == "":
        custom_field = None
    game = await redis.get(f"game:{game_pin}")
    while game is not None:
        game_pin = randint(100000, 999999)
        game = await redis.get(f"game:{game_pin}")

    game_questions = select_questions_for_game(
        quiz.questions,
        getattr(quiz, "questions_per_game", None),
    )

    from classquiz.helpers.game_questions import shuffle_abcd_answer_positions

    shuffle_abcd_answer_positions(game_questions)

    if randomize_answers:
        for question in game_questions:
            if question["type"] == QuizQuestionType.RANGE:
                continue
            if question["type"] == QuizQuestionType.SLIDE:
                continue
            random.shuffle(question["answers"])

    game = PlayGame(
        quiz_id=quiz_id,
        game_pin=str(game_pin),
        questions=game_questions,
        game_id=uuid.uuid4(),
        title=quiz.title,
        description=quiz.description,
        captcha_enabled=captcha_enabled,
        cover_image=quiz.cover_image,
        game_mode=game_mode,
        user_id=host_user_id,
        background_color=quiz.background_color,
        custom_field=custom_field,
        background_image=quiz.background_image,
    )
    if team_count >= 2 and game_mode != "battle" and team_assign in ("random", "choose"):
        from classquiz.helpers.team_mode import clamp_team_count

        game.team_mode = {"count": clamp_team_count(team_count, 8), "assign": team_assign}
    code = None
    if cqcs_enabled:
        code = generate_code(6)
        await redis.set(f"game:cqc:code:{code}", game_pin, ex=3600)
    await redis.set(f"game:{str(game.game_pin)}", game.model_dump_json(), ex=18000)
    if user is not None:
        await redis.set(f"game_pin:{user.id}:{quiz_id}", game_pin, ex=18000)
        await redis.set(
            f"game_in_lobby:{user.id.hex}",
            GameInLobby(game_id=game.game_id, game_pin=str(game_pin), quiz_title=quiz.title).model_dump_json(),
            ex=900,
        )
    return {**quiz.model_dump(exclude={"id"}), **game.model_dump(exclude={"questions"}), "cqc_code": code}


class CheckIfCaptchaEnabledResponse(BaseModel):
    enabled: bool
    game_mode: str | None = None
    custom_field: str | None = None


@router.get("/play/check_captcha/{game_pin}", response_model=CheckIfCaptchaEnabledResponse)
async def check_if_captcha_enabled(game_pin: str):
    game = await redis.get(f"game:{game_pin}")
    if game is None:
        return JSONResponse(status_code=404, content={"detail": "game not found"})
    game = PlayGame.model_validate_json(game)
    if game.captcha_enabled:
        return CheckIfCaptchaEnabledResponse(enabled=True, game_mode=game.game_mode, custom_field=game.custom_field)
    else:
        return CheckIfCaptchaEnabledResponse(enabled=False, game_mode=game.game_mode, custom_field=game.custom_field)


@router.get("/join/{game_pin}", deprecated=True)
async def get_game_id(game_pin: str):
    redis_res = await redis.get(f"game:{game_pin}")
    if redis_res is None:
        raise HTTPException(status_code=404, detail="game not found")
    else:
        return json.loads(redis_res)["game_id"]


@router.get("/list")
async def get_quiz_list(user: User = Depends(get_current_user), page_size: int | None = 10, page: int | None = 1):
    try:
        return (
            await Quiz.objects.order_by(Quiz.updated_at.desc())
            .filter(user_id=user.id)
            .paginate(page, page_size=page_size)
            .all()
        )
    except ormar.exceptions.QueryDefinitionError:
        raise HTTPException(status_code=400, detail="Invalid page(size). page(size) have to be greater than 0.")


@router.post("/import/{quiz_id}")
async def import_quiz_route(quiz_id: str, user: User = Depends(get_current_user)):
    if user.storage_used > settings.free_storage_limit:
        raise HTTPException(status_code=409, detail="Storage limit reached")
    resp_data = await import_quiz(quiz_id, user)
    try:
        if type(resp_data) is int:
            raise HTTPException(status_code=resp_data, detail="kahoot")
        else:
            return resp_data
    except ValidationError:
        raise HTTPException(400, detail="unsupported")


@router.delete("/delete/{quiz_id}")
async def delete_quiz(quiz_id: str, user: User = Depends(get_current_user)):
    try:
        quiz_id = uuid.UUID(quiz_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="badly formed quiz id")
    quiz = await Quiz.objects.get_or_none(id=quiz_id, user_id=user.id)

    if quiz is None:
        return JSONResponse(status_code=404, content={"detail": "quiz not found"})
    pics_to_delete = []
    pic_name_regex = re.compile("^.*/(.{36}--.{36})$")
    for question in quiz.questions:
        try:
            if question["image"] is not None and not str(question["image"]).startswith("https://i.imgur.com/"):
                old_image_to_delete = pic_name_regex.match(question["image"])
                if old_image_to_delete is not None:
                    pics_to_delete.append(old_image_to_delete.group(1))
        except KeyError:
            pass
    if len(pics_to_delete) != 0:
        await storage.delete(pics_to_delete)
    meilisearch.index(settings.meilisearch_index).delete_document(str(quiz.id))
    return await quiz.delete()


@router.get("/export_data/{export_token}", response_class=StreamingResponse)
async def export_quiz_answers(export_token: str, game_pin: str):
    data = await redis.get(f"export_token:{export_token}")
    if data is None:
        raise HTTPException(status_code=404, detail="export token not found")
    data = json.loads(data)
    data2 = await redis.get(f"game:{game_pin}")
    game_data = PlayGame.model_validate_json(data2)
    quiz = await Quiz.objects.get_or_none(id=game_data.quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="quiz not found")

    player_fields = await redis.hgetall(f"game:{game_pin}:players:custom_fields")
    score_data = await redis.hgetall(f"game_session:{game_pin}:player_scores")
    spreadsheet = await generate_spreadsheet(
        quiz=quiz, quiz_results=data, player_fields=player_fields, player_scores=score_data
    )

    def iter_file():
        yield from spreadsheet

    await redis.delete(f"export_token:{export_token}")
    return StreamingResponse(
        iter_file(),
        media_type="application/vnd.ms-excel",
        headers={
            "Content-Disposition": f"attachment;filename=CMA-Clash-{urllib.parse.quote(quiz.title)}-{datetime.now().strftime('%m-%d-%Y')}.xlsx"  # noqa: E501
        },
    )


@router.post("/excel-import")
async def import_from_excel(file: UploadFile = File(), user: User = Depends(get_current_user)) -> Quiz:
    quiz = await handle_import_from_excel(file.file, user)
    return Quiz.model_validate(quiz.model_dump(exclude={"user_id": ...}))
