#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Per-item report of the choice-quality gates that the repo tests enforce.

Reports, for every seed item:
  * giveaway absolute words in a distractor that the correct answer does not use
  * distractors longer than the plausible-length cap
  * a keyed answer that is the longest option and much longer than the shortest
  * a keyed answer that is the uniquely longest option

Usage:
    python scripts/audit_item_quality.py                 # whole bank
    python scripts/audit_item_quality.py cpr-child       # one topic prefix
    python scripts/audit_item_quality.py --only-failing   # only items with problems
"""

from __future__ import annotations

import importlib.util
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"

GIVEAWAY = re.compile(r"\b(always|never|any|random)\b|(?<![\w-])only(?![\w-])", re.I)
MAX_DISTRACTOR_LEN = 80
KEY_MARGIN = 22


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def bootstrap():
    sys.modules["classquiz"] = types.ModuleType("classquiz")
    pkg = types.ModuleType("classquiz.seed")
    pkg.__path__ = [str(SEED)]
    sys.modules["classquiz.seed"] = pkg
    _load("classquiz.seed.sources", SEED / "sources.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def item_problems(fact: dict) -> list[str]:
    problems: list[str] = []
    correct = fact["correct"]
    distractors = list(fact["distractors"])
    for d in distractors:
        if GIVEAWAY.search(d) and not GIVEAWAY.search(correct):
            problems.append(f"giveaway word in distractor: {d[:60]!r}")
        if len(d.strip()) > MAX_DISTRACTOR_LEN:
            problems.append(f"distractor is {len(d.strip())} chars (max {MAX_DISTRACTOR_LEN}): {d[:60]!r}")
    lengths = [len(c.strip()) for c in [correct, *distractors]]
    if lengths[0] > max(lengths[1:]) and lengths[0] - min(lengths[1:]) >= KEY_MARGIN:
        problems.append(
            f"key is longest by {lengths[0] - min(lengths[1:])} chars over the shortest distractor"
        )
    if lengths[0] == max(lengths) and sum(1 for n in lengths if n == max(lengths)) == 1:
        problems.append("key is the uniquely longest option")
    return problems


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    prefix = args[0] if args else ""
    only_failing = "--only-failing" in sys.argv
    banks = bootstrap()
    facts = banks.load_all_facts()
    total = 0
    items = 0
    for fact in facts:
        if prefix and not fact["topic"].startswith(prefix):
            continue
        problems = item_problems(fact)
        if not problems:
            continue
        items += 1
        total += len(problems)
        if only_failing:
            print(f"{fact['topic']} | {fact['stem'][:70]}")
            for p in problems:
                print(f"    - {p}")
    print(f"\n{items} items with problems, {total} problems")


if __name__ == "__main__":
    main()
