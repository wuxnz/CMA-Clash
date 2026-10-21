#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""List the quiz chunks that carry too many longest-keyed items.

The seeded runner groups items by (topic, difficulty), sorts them by stem, and
slices them into 28-question chunks. The repo test allows at most 30 percent of
a chunk (42 percent for chunks under 20 items) to have a keyed answer that is
longer than every distractor by at least 22 characters.

Usage:
    python scripts/audit_chunk_longest.py            # summary plus the offending items
    python scripts/audit_chunk_longest.py cpr-child  # one topic prefix
"""

from __future__ import annotations

import importlib.util
import math
import sys
import types
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"


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
    _load("classquiz.seed.catalog", SEED / "catalog.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def main() -> None:
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    banks = bootstrap()
    facts = banks.load_all_facts()
    from classquiz.seed.catalog import TOPIC_QUESTIONS_PER_QUIZ
    from classquiz.seed.fact_choice_hardening import is_correct_strictly_longest

    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for f in facts:
        grouped[(f["topic"], f["difficulty"])].append(f)

    total = 0
    for (topic, diff), items in sorted(grouped.items()):
        if prefix and not topic.startswith(prefix):
            continue
        items.sort(key=lambda f: f["stem"])
        chunk_size = TOPIC_QUESTIONS_PER_QUIZ.get(topic, 28)
        for start in range(0, len(items), chunk_size):
            chunk = items[start : start + chunk_size]
            offenders = [f for f in chunk if is_correct_strictly_longest(f)]
            ratio = 0.30 if len(chunk) >= 20 else 0.42
            allowed = max(1, math.ceil(len(chunk) * ratio))
            if len(offenders) > allowed:
                total += len(offenders) - allowed
                print(
                    f"{topic} {diff} chunk {start // chunk_size + 1}: "
                    f"{len(offenders)} over-long keys, allowed {allowed}"
                )
                for f in offenders:
                    lengths = [len(c.strip()) for c in [f["correct"], *f["distractors"]]]
                    print(f"    {f['stem'][:66]}  lengths={lengths}")
    print(f"\n{total} over-long keys must be rebalanced")


if __name__ == "__main__":
    main()
