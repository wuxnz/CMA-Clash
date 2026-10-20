#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0
"""Drop padded or duplicate supplement items."""

from __future__ import annotations

import importlib.util
import json
import re
from collections import Counter
from pathlib import Path

from classquiz.seed.stem_normalize import normalize_stem

ITEMS = Path(__file__).with_name("supplement_items.json")


def _load_base_stems() -> set[str]:
    stems: set[str] = set()
    for path in (
        "classquiz/seed/banks/ccma.py",
        "classquiz/seed/banks/clinical_skills.py",
        "classquiz/seed/banks/cpr_bls.py",
        "classquiz/seed/banks/ekg.py",
        "classquiz/seed/banks/phlebotomy.py",
    ):
        spec = importlib.util.spec_from_file_location("m", Path(__file__).parents[1] / path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for fact in mod.FACTS:
            stems.add(normalize_stem(fact["stem"]))
    return stems


def main() -> None:
    base = _load_base_stems()
    items = json.loads(ITEMS.read_text(encoding="utf-8"))
    kept: list[dict] = []
    seen: set[str] = set(base)
    dropped = 0
    for row in items:
        stem = row["stem"]
        if re.search(r"\((?:scenario|review)\s+\d+\)", stem, re.I):
            dropped += 1
            continue
        norm = normalize_stem(stem)
        if norm in seen:
            dropped += 1
            continue
        kept.append(row)
        seen.add(norm)
    ITEMS.write_text(json.dumps(kept, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"kept {len(kept)}, dropped {dropped}")


if __name__ == "__main__":
    main()
