#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Apply a batch of distractor rewrites to the seed bank source files.

The rewrites live in ``scripts/choice_rewrites.py`` as a dict of
``old option text -> new option text``. Run with ``--apply`` to write them.

    python scripts/apply_choice_rewrites.py            # check the mapping only
    python scripts/apply_choice_rewrites.py --apply    # write to the source files
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"
HERE = Path(__file__).resolve().parent


def load_rewrites() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location("choice_rewrites", HERE / "choice_rewrites.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["choice_rewrites"] = mod
    spec.loader.exec_module(mod)
    return dict(mod.REWRITES)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    rewrites = load_rewrites()
    files = sorted((SEED / "banks").rglob("*.py"))
    applied = 0
    already = 0
    missing: list[str] = []
    for path in files:
        source = path.read_text(encoding="utf-8")
        original = source
        for old, new in rewrites.items():
            for quote in ('"', "'"):
                needle = f"{quote}{old}{quote}"
                if needle in source:
                    source = source.replace(needle, f"{quote}{new}{quote}")
                    applied += 1
                    break
        if source != original:
            if args.apply:
                path.write_text(source, encoding="utf-8")
            print(f"{'updated' if args.apply else 'would update'} {path.relative_to(ROOT)}")

    # A rewrite is satisfied when either the old or the new text is present.
    for old, new in rewrites.items():
        if not any(
            f'"{old}"' in p.read_text(encoding="utf-8")
            or f"'{old}'" in p.read_text(encoding="utf-8")
            or f'"{new}"' in p.read_text(encoding="utf-8")
            or f"'{new}'" in p.read_text(encoding="utf-8")
            for p in files
        ):
            missing.append(old)
    print(f"\n{applied} rewrites applied, {len(rewrites) - len(missing)}/{len(rewrites)} satisfied")
    if missing:
        print(f"{len(missing)} not found:")
        for old in missing[:20]:
            print(f"  {old[:80]}")
    if not args.apply:
        print("dry run; pass --apply to write")


if __name__ == "__main__":
    main()
