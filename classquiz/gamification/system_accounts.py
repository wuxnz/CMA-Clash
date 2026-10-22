# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Accounts that must never be ranked on the public leaderboard.

The seed pipeline creates two machine accounts: the content account that owns the
seeded quizzes and the demo account used for walkthroughs. Diagnostic tooling also
registers throwaway accounts under a ``cmaclash-`` prefix with a disposable
mailbox. None of them represent a real player, so they must not appear on a
leaderboard, occupy a rank slot, or push a real player down the board.
"""

from __future__ import annotations

# The seeded content account (owns the seeded quizzes) and the walkthrough demo
# account. Both are created by classquiz.seed.runner.
CONTENT_ACCOUNT_EMAIL = "content@cmaclash.local"
DEMO_ACCOUNT_EMAIL = "demo@cmaclash.local"

SYSTEM_ACCOUNT_EMAILS: frozenset[str] = frozenset({CONTENT_ACCOUNT_EMAIL, DEMO_ACCOUNT_EMAIL})
# Usernames that belong to a machine account even when the email is not listed.
SYSTEM_ACCOUNT_USERNAMES: frozenset[str] = frozenset({"cmaclash_content"})
# Reserved / non-routable email domains used for local accounts.
SYSTEM_ACCOUNT_EMAIL_SUFFIXES: tuple[str, ...] = (".local",)
# Disposable mailbox domains used by the diagnostic, verification, and e2e scripts.
SYSTEM_ACCOUNT_EMAIL_DOMAINS: frozenset[str] = frozenset({"mailinator.com"})
# Username prefixes used by the diagnostic and verification account scripts.
SYSTEM_ACCOUNT_USERNAME_PREFIXES: tuple[str, ...] = ("cmaclash-", "cmaclash_")


def is_system_account(email: str | None, username: str | None = None) -> bool:
    """True when the account is a machine account that must never be ranked."""
    normalized_email = (email or "").strip().lower()
    normalized_username = (username or "").strip().lower()
    if normalized_email in SYSTEM_ACCOUNT_EMAILS:
        return True
    if normalized_username in SYSTEM_ACCOUNT_USERNAMES:
        return True
    if any(normalized_email.endswith(suffix) for suffix in SYSTEM_ACCOUNT_EMAIL_SUFFIXES):
        return True
    domain = normalized_email.rpartition("@")[2]
    if domain in SYSTEM_ACCOUNT_EMAIL_DOMAINS:
        return True
    return any(normalized_username.startswith(prefix) for prefix in SYSTEM_ACCOUNT_USERNAME_PREFIXES)


def system_account_params() -> dict[str, list[str]]:
    """Bind values for :func:`system_account_sql`."""
    return {
        "sys_emails": sorted(SYSTEM_ACCOUNT_EMAILS),
        "sys_usernames": sorted(SYSTEM_ACCOUNT_USERNAMES),
        "sys_email_suffixes": [f"%{suffix}" for suffix in SYSTEM_ACCOUNT_EMAIL_SUFFIXES],
        "sys_email_domains": sorted(SYSTEM_ACCOUNT_EMAIL_DOMAINS),
        "sys_username_prefixes": [f"{prefix}%" for prefix in SYSTEM_ACCOUNT_USERNAME_PREFIXES],
    }


def system_account_sql(alias: str = "u") -> str:
    """SQL predicate that is true for accounts that must not be ranked.

    Bind the result of :func:`system_account_params` alongside it.
    """
    return (
        f"NOT ("
        f"LOWER({alias}.email) = ANY(:sys_emails)"
        f" OR LOWER({alias}.username) = ANY(:sys_usernames)"
        f" OR LOWER({alias}.email) LIKE ANY(:sys_email_suffixes)"
        f" OR SPLIT_PART(LOWER({alias}.email), '@', 2) = ANY(:sys_email_domains)"
        f" OR LOWER({alias}.username) LIKE ANY(:sys_username_prefixes)"
        f")"
    )
