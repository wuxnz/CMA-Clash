# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Normalize question stems for duplicate detection in seed banks."""

from __future__ import annotations

import re

_PAREN_SUFFIX = re.compile(
    r"\s*\((?:scenario|review)\s+\d+\)\s*$",
    re.IGNORECASE,
)


def normalize_stem(stem: str) -> str:
    text = stem.strip().lower()
    text = _PAREN_SUFFIX.sub("", text)
    text = re.sub(r"\s+", " ", text)
    return text
