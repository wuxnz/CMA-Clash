# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0
import os

from jinja2 import Environment, PackageLoader, select_autoescape

from classquiz.config import settings, redis
from classquiz.db.models import User
from classquiz.emails.transport import send_email
from classquiz.emails.verification import VERIFY_TOKEN_HOURS, create_email_verify_token, verification_link

settings = settings()

jinja = Environment(
    loader=PackageLoader("classquiz.emails", "templates"),
    autoescape=select_autoescape(["html", "xml"]),
    enable_async=True,
)


async def send_register_email(user: User):
    if user is None:
        raise ValueError("User not found")
    token = create_email_verify_token(user.id)
    verify_url = verification_link(token)
    html_template = jinja.get_template("verify_email.jinja2")
    text_template = jinja.get_template("verify_email.txt.jinja2")
    html_body = await html_template.render_async(verify_url=verify_url, expiry_hours=VERIFY_TOKEN_HOURS)
    text_body = await text_template.render_async(verify_url=verify_url, expiry_hours=VERIFY_TOKEN_HOURS)
    send_email(
        to=user.email,
        subject="Verify your CMA Clash email",
        html_body=html_body,
        text_body=text_body,
    )


async def send_forgotten_password_email(email: str):
    user = await User.objects.get_or_none(email=email)
    if user is None:
        raise ValueError("User not found")
    template = jinja.get_template("forgotten_password.jinja2")
    token = os.urandom(32).hex()
    html = await template.render_async(base_url=settings.root_address, token=token)
    await redis.set(f"reset_passwd:{token}", str(user.id), ex=3600)
    send_email(
        to=email,
        subject="Reset your CMA Clash password",
        html_body=html,
        text_body=f"Reset your password: {settings.root_address}/account/password-reset?token={token}",
    )
