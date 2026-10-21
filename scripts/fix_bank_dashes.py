#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

"""Replace em/en dashes in seed bank string literals with comma or 'to' phrasing."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [
    ROOT / "classquiz" / "seed" / "banks" / "cpr",
    ROOT / "classquiz" / "seed" / "banks" / "phleb",
]
TARGET_FILES = [
    ROOT / "classquiz" / "seed" / "banks" / "ekg.py",
    ROOT / "classquiz" / "seed" / "banks" / "ccma.py",
    ROOT / "classquiz" / "seed" / "banks" / "clinical_skills.py",
]


def _fix_dashes(text: str) -> str:
    # Numeric ranges: 100–120 -> 100 to 120
    text = re.sub(
        r"(\d)\s*[\u2013\u2014]\s*(\d)",
        r"\1 to \2",
        text,
    )
    text = text.replace("\u2014", ", ")
    text = text.replace("\u2013", ", ")
    text = re.sub(r",\s*,", ", ", text)
    text = re.sub(r"  +", " ", text)
    return text


def main() -> None:
    paths: list[Path] = []
    for d in TARGET_DIRS:
        paths.extend(d.glob("*.py"))
    paths.extend(TARGET_FILES)
    changed = 0
    for path in sorted(set(paths)):
        raw = path.read_text(encoding="utf-8")
        if "\u2014" not in raw and "\u2013" not in raw:
            continue
        new = _fix_dashes(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            changed += 1
            print("fixed", path.relative_to(ROOT))
    print("files changed:", changed)


if __name__ == "__main__":
    main()
