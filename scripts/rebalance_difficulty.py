#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Rebalance the beginner/intermediate/advanced mix of a seed bank.

The repo requires each topic to sit near a 30/40/30 difficulty split. This tool
picks which items to move by a simple complexity score (option length plus the
number of clinical terms), then rewrites only the difficulty literal of the
selected ``fact(...)`` calls in place.

Usage:
    python scripts/rebalance_difficulty.py --module vitals --dry-run
    python scripts/rebalance_difficulty.py --module vitals
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"

MODULE_FILES = {
    "injection": "injection.py",
    "vitals": "vitals.py",
    "infection": "infection.py",
    "terminology": "terminology.py",
    "pharm_dosage": "pharm_dosage.py",
    "specimen_lab": "specimen_lab.py",
    "intake": "intake.py",
    "osha_bbp": "osha_bbp.py",
    "med_safety": "med_safety.py",
    "poct": "poct.py",
    "wound_care": "wound_care.py",
    "life_stages": "life_stages.py",
    "emergency_aid": "emergency_aid.py",
}

COMPLEX_TERMS = re.compile(
    r"\b(contraindicat\w*|coagulat\w*|intravenou\w*|hypoglyc\w*|hyperglyc\w*|"
    r"anaphyla\w*|sedat\w*|tachycard\w*|arrhythm\w*|renal|hepatic|"
    r"interpret\w*|adjust\w*|complicat\w*|infusion|oxygenation|"
    r"pharmacokinetic\w*|antagonist\w*|metabolis\w*|"
    r"protocol|guideline\w*|contraindicate\w*|reassess\w*|monitor\w*)\b",
    re.I,
)


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
    _load("classquiz.seed.banks._builder", SEED / "banks" / "_builder.py")


def complexity(fact: dict) -> float:
    text = " ".join([fact["stem"], fact["correct"], *fact["distractors"]])
    words = len(text.split())
    terms = len(COMPLEX_TERMS.findall(text))
    return words + terms * 12


def targets(n: int) -> dict[str, int]:
    beginner = int(round(n * 0.30))
    intermediate = int(round(n * 0.40))
    return {
        "beginner": beginner,
        "intermediate": intermediate,
        "advanced": n - beginner - intermediate,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--module", required=True, choices=sorted(MODULE_FILES))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--move",
        action="append",
        default=[],
        metavar="N:label",
        help="explicit move of item N (1-based) to a difficulty label; repeatable",
    )
    args = ap.parse_args()

    bootstrap()
    path = SEED / "banks" / "clinical_skills" / MODULE_FILES[args.module]
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    facts = list(_load("_rb_" + args.module, path).FACTS)
    counts: dict[str, int] = {"beginner": 0, "intermediate": 0, "advanced": 0}
    for f in facts:
        counts[f["difficulty"]] += 1
    want = targets(len(facts))
    print(f"{args.module}: {len(facts)} items, now {counts}, target {want}")

    # Locate each fact() call and its difficulty argument position.
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "fact":
            diff_arg = node.args[6] if len(node.args) > 6 else None
            if diff_arg is None:
                for kw in node.keywords:
                    if kw.arg == "difficulty":
                        diff_arg = kw.value
            if not isinstance(diff_arg, ast.Constant):
                continue
            calls.append((node, diff_arg))
    calls.sort(key=lambda pair: (pair[0].lineno, pair[0].col_offset))
    if len(calls) != len(facts):
        raise SystemExit(f"found {len(calls)} fact calls but {len(facts)} facts")

    new_difficulty = [f["difficulty"] for f in facts]
    if args.move:
        for spec in args.move:
            number, _, label = spec.partition(":")
            index = int(number) - 1
            if not 0 <= index < len(new_difficulty):
                raise SystemExit(f"item {number} is out of range")
            if label not in ("beginner", "intermediate", "advanced"):
                raise SystemExit(f"bad label {label!r}")
            print(f"  manual: item {number} -> {label}")
            new_difficulty[index] = label
    else:
        if counts == want:
            print("already balanced")
            return
        scores = [complexity(f) for f in facts]
        order = sorted(range(len(facts)), key=lambda i: scores[i])
        for _ in range(400):
            counts = {"beginner": 0, "intermediate": 0, "advanced": 0}
            for d in new_difficulty:
                counts[d] += 1
            if counts == want:
                break
            deficits = {k: want[k] - counts[k] for k in want}
            target = max(deficits, key=lambda k: deficits[k])
            if deficits[target] <= 0:
                break
            source_label = max(
                (k for k in want if counts[k] > want[k]),
                key=lambda k: counts[k] - want[k],
            )
            if source_label == target:
                break
            candidates = [i for i in range(len(facts)) if new_difficulty[i] == source_label]
            if target == "beginner":
                pick = min(candidates, key=lambda i: scores[i])
            elif target == "advanced":
                pick = max(candidates, key=lambda i: scores[i])
            else:
                pick = min(candidates, key=lambda i: abs(scores[i] - sum(scores) / len(scores)))
            new_difficulty[pick] = target

    changes = [
        (calls[i][1], new_difficulty[i]) for i in range(len(facts)) if calls[i][1].value != new_difficulty[i]
    ]
    if not changes:
        print("no changes needed")
        return
    print(f"{len(changes)} difficulty labels change")
    for arg, new in changes:
        print(f"  line {arg.lineno}: {arg.value} -> {new}")

    if args.dry_run:
        return

    lines = source.splitlines(keepends=True)
    for arg, new in changes:
        line = lines[arg.lineno - 1]
        # The difficulty literal is the last quoted token on the line for these banks.
        matches = list(re.finditer(r"['\"](beginner|intermediate|advanced)['\"]", line))
        target_match = None
        for m in matches:
            if m.group(0).strip("\"'") == arg.value:
                target_match = m
                break
        if target_match is None:
            raise SystemExit(f"cannot locate difficulty literal on line {arg.lineno}")
        quote = target_match.group(0)[0]
        line = line[: target_match.start()] + f"{quote}{new}{quote}" + line[target_match.end() :]
        lines[arg.lineno - 1] = line
    path.write_text("".join(lines), encoding="utf-8")
    print(f"rewrote {path}")


if __name__ == "__main__":
    main()
