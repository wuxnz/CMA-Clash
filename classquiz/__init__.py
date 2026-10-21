# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

import logging

import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sentry_sdk.integrations.redis import RedisIntegration
from socketio import ASGIApp
from starlette.middleware.sessions import SessionMiddleware

from classquiz.config import settings
from classquiz.db import database

from classquiz.oauth import rememberme_middleware
from classquiz.routers import (
    users,
    quiz,
    utils,
    stats,
    storage,
    search,
    testing_routes,
    editor,
    live,
    eximport,
    login,
    sitemap,
    remote,
    community,
    avatar,
    results,
    admin,
    box_controller,
    quiztivity,
    pixabay,
    moderation,
    clash,
)
from classquiz.socket_server import sio
from classquiz.helpers import meilisearch_init

settings = settings()
if settings.sentry_dsn:
    sentry_sdk.init(dsn=settings.sentry_dsn, integrations=[RedisIntegration()])
app = FastAPI(title="CMA Clash API", redoc_url="", docs_url="/api/docs")
app.state.database = database


class _CORSMiddlewareSkippingSocketIO(CORSMiddleware):
    """CORS for the HTTP API only.

    python-socketio (mounted at "/" below) already validates the Origin and sets
    Access-Control-Allow-* on /socket.io/ itself. Letting this middleware add them
    too produced duplicate Access-Control-Allow-Origin headers, which browsers
    reject, so Engine.IO polling failed from the Vercel frontend.
    """

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and scope.get("path", "").startswith("/socket.io"):
            await self.app(scope, receive, send)
            return
        await super().__call__(scope, receive, send)


_cors_origins = settings.parsed_cors_origins()
if _cors_origins:
    app.add_middleware(
        _CORSMiddlewareSkippingSocketIO,
        allow_origins=_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/api/v1/health")
async def health_check():
    return JSONResponse({"status": "ok"})


@app.middleware("http")
async def sentry_exception(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        with sentry_sdk.push_scope() as scope:
            scope.set_context("request", request)
            sentry_sdk.capture_exception(e)
        raise e


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    try:
        await meilisearch_init()
    except Exception as exc:
        LOGGER = logging.getLogger("uvicorn.error")
        LOGGER.warning("Meilisearch unavailable at startup (%s); search will be degraded until it is reachable.", exc)
    if settings.auto_seed_content:
        from classquiz.seed.runner import run_seed

        await run_seed()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.middleware("http")
async def auth_middleware_wrapper(request: Request, call_next):
    return await rememberme_middleware(request, call_next)


app.include_router(
    moderation.router,
    tags=["moderation"],
    prefix="/api/v1/moderation",
    include_in_schema=True,
)
app.include_router(pixabay.router, tags=["pixabay"], prefix="/api/v1/pixabay", include_in_schema=True)
app.include_router(
    quiztivity.router,
    tags=["quiztivity"],
    prefix="/api/v1/quiztivity",
    include_in_schema=True,
)

app.include_router(
    box_controller.router,
    tags=["boxcontroller"],
    prefix="/api/v1/box-controller",
    include_in_schema=True,
)
app.include_router(results.router, tags=["results"], prefix="/api/v1/results", include_in_schema=True)
app.include_router(remote.router, tags=["remote"], prefix="/api/v1/remote", include_in_schema=True)
app.include_router(login.router, tags=["auth"], prefix="/api/v1/login", include_in_schema=True)

app.add_middleware(SessionMiddleware, secret_key=settings.secret_key)
app.include_router(users.router, tags=["users"], prefix="/api/v1/users", include_in_schema=True)
app.include_router(quiz.router, tags=["quiz"], prefix="/api/v1/quiz", include_in_schema=True)
app.include_router(utils.router, tags=["utils"], prefix="/api/v1/utils", include_in_schema=True)
app.include_router(stats.router, tags=["stats"], prefix="/api/v1/stats", include_in_schema=True)
app.include_router(storage.router, tags=["storage"], prefix="/api/v1/storage", include_in_schema=True)
app.include_router(search.router, tags=["search"], prefix="/api/v1/search", include_in_schema=True)
app.include_router(live.router, tags=["live"], prefix="/api/v1/live", include_in_schema=True)
app.include_router(
    testing_routes.router,
    tags=["internal", "testing"],
    prefix="/api/v1/internal/testing",
    include_in_schema=False,
)
app.include_router(editor.router, tags=["editor"], prefix="/api/v1/editor", include_in_schema=True)
app.include_router(
    eximport.router,
    tags=["export", "import"],
    prefix="/api/v1/eximport",
    include_in_schema=True,
)
app.include_router(sitemap.router, tags=["sitemap"], prefix="/api/v1/sitemap", include_in_schema=True)
app.include_router(
    community.router,
    tags=["community"],
    prefix="/api/v1/community",
    include_in_schema=True,
)
app.include_router(avatar.router, tags=["avatar"], prefix="/api/v1/avatar", include_in_schema=True)
app.include_router(admin.router, tags=["admin"], prefix="/api/v1/admin", include_in_schema=True)
app.include_router(clash.router, tags=["cma-clash"], prefix="/api/v1/clash", include_in_schema=True)
app.mount("/", ASGIApp(sio))
