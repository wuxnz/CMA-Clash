# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import logging
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

import json
import urllib.error
import urllib.request

from classquiz.config import settings

LOGGER = logging.getLogger(__name__)
settings = settings()


def mail_transport_configured() -> bool:
    if settings.resend_api_key:
        return True
    return bool(
        settings.mail_server
        and settings.mail_address
        and settings.mail_username is not None
        and settings.mail_password is not None
        and settings.mail_port
    )


def _from_address() -> str:
    return settings.mail_from or settings.mail_address or "noreply@cmaclash.com"


def send_email(to: str, subject: str, html_body: str, text_body: str) -> None:
    if not mail_transport_configured():
        LOGGER.warning(
            "Email transport not configured; message to %s (%s). Plain-text body logged below.",
            to,
            subject,
        )
        LOGGER.info("--- email fallback ---\n%s\n--- end ---", text_body)
        return

    if settings.resend_api_key:
        _send_resend(to, subject, html_body, text_body)
        return
    _send_smtp(to, subject, html_body, text_body)


def _send_smtp(to: str, subject: str, html_body: str, text_body: str) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = _from_address()
    msg["To"] = to
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    context = ssl.create_default_context()
    with smtplib.SMTP(host=settings.mail_server, port=settings.mail_port, timeout=30) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(settings.mail_username, settings.mail_password)
        server.sendmail(_from_address(), [to], msg.as_string())


def _send_resend(to: str, subject: str, html_body: str, text_body: str) -> None:
    body = json.dumps(
        {
            "from": _from_address(),
            "to": [to],
            "subject": subject,
            "html": html_body,
            "text": text_body,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=body,
        headers={
            "Authorization": f"Bearer {settings.resend_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "cmaclash/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp_body = resp.read().decode("utf-8", errors="replace")
            if resp.status >= 400:
                LOGGER.error("Resend API error %s: %s", resp.status, resp_body)
                raise RuntimeError(f"Resend API error {resp.status}: {resp_body}")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        LOGGER.error("Resend API error %s: %s", e.code, err_body)
        raise RuntimeError(f"Resend API error {e.code}: {err_body}") from e
