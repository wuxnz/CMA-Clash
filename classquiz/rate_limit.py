# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from fastapi import HTTPException, Request, status

from classquiz.config import redis


async def rate_limit_request(
    request: Request,
    scope: str,
    limit: int,
    window_sec: int,
) -> None:
    host = request.client.host if request.client else "unknown"
    key = f"rl:{scope}:{host}"
    count = await redis.incr(key)
    if count == 1:
        await redis.expire(key, window_sec)
    if count > limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={"code": "rate_limited", "message": "Too many requests. Try again later."},
        )
