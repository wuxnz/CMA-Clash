"""Check candidate option sets against the two keyed-answer length guards.

The repo guards forbid a keyed answer that is the uniquely longest option and a
keyed answer that is the uniquely shortest option by a wide margin. This tool
runs both checks against candidate option sets so a rewrite can be tuned before
it is applied.

Usage:
    py -3.13 scripts/check_option_balance.py items.json
    py -3.13 scripts/check_option_balance.py '[{"name": "x", "correct": "A", "distractors": ["B", "C", "D"]}]'

The JSON is a list of objects with a "correct" string and a "distractors" list.
An optional "name" is used in the report.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from run_seed_quality_checks import bootstrap  # noqa: E402

bootstrap()

from classquiz.seed.choice_quality import (  # noqa: E402
    correct_is_uniquely_longest,
    correct_is_uniquely_short_by_margin,
)


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    raw = Path(argv[0]).read_text(encoding="utf-8") if Path(argv[0]).exists() else argv[0]
    items = json.loads(raw)

    ok = True
    for item in items:
        correct = item["correct"]
        distractors = list(item["distractors"])
        lens = [len(correct.strip())] + [len(d.strip()) for d in distractors]
        longest = correct_is_uniquely_longest(correct, distractors)
        short = correct_is_uniquely_short_by_margin(correct, distractors)
        mean_d = sum(lens[1:]) / len(lens[1:]) if lens[1:] else 0.0
        status = "OK " if not (longest or short) else "BAD"
        if longest or short:
            ok = False
        print(
            f"{status} {item.get('name', ''):<28} lens={lens} mean_d={mean_d:.1f} "
            f"threshold={0.6 * mean_d:.1f} uniquely_longest={longest} "
            f"uniquely_short={short}"
        )
    print("\nALL OK" if ok else "\nNEEDS WORK")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
