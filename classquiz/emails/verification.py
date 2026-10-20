# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import uuid
from datetime import datetime, timedelta, timezone
from enum import Enum

from jose import JWTError, jwt

from classquiz.auth import ALGORITHM
from classquiz.config import settings

settings = settings()
VERIFY_TOKEN_TYPE = "email_verify"
VERIFY_TOKEN_HOURS = 48


class VerifyTokenError(str, Enum):
    INVALID = "invalid_token"
    EXPIRED = "expired_token"
    ALREADY_VERIFIED = "already_verified"


def create_email_verify_token(user_id: uuid.UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(hours=VERIFY_TOKEN_HOURS)
    payload = {
        "typ": VERIFY_TOKEN_TYPE,
        "sub": str(user_id),
        "exp": expire,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def decode_email_verify_token(token: str) -> tuple[uuid.UUID | None, VerifyTokenError | None]:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    except JWTError as err:
        if "expired" in str(err).lower():
            return None, VerifyTokenError.EXPIRED
        return None, VerifyTokenError.INVALID
    if payload.get("typ") != VERIFY_TOKEN_TYPE:
        return None, VerifyTokenError.INVALID
    sub = payload.get("sub")
    try:
        return uuid.UUID(str(sub)), None
    except (ValueError, TypeError):
        return None, VerifyTokenError.INVALID


def verification_link(token: str) -> str:
    base = settings.root_address.rstrip("/")
    return f"{base}/account/verify?token={token}"
