#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Strip the repeated auto-balance padding tails from bank options.

Several bank modules were generated with a trailing filler clause bolted onto
every option ("under typical outpatient policy.", "per facility policy.", and so
on). The clause carries no clinical meaning, makes the options read as padding,
and pushes them over the length cap. This removes it from the keyed answer and
from the distractors alike so the option set stays parallel.

Usage:
    python scripts/strip_padding_tails.py --prefix ccma- --dry-run
    python scripts/strip_padding_tails.py --prefix ccma- --apply
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"

TAILS = (
    " under typical outpatient policy.",
    " per facility policy.",
    " in a typical outpatient clinic setting.",
    " for routine ambulatory patient care.",
    " in a typical outpatient clinic.",
    " in routine outpatient care.",
    " in typical outpatient practice.",
    " in the typical outpatient clinic.",
)
TAIL_RE = re.compile(
    r"(?:"
    + "|".join(re.escape(t) for t in sorted(TAILS, key=len, reverse=True))
    + r")\s*$",
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
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def strip(text: str) -> str:
    out = TAIL_RE.sub("", text.strip())
    out = re.sub(r"\s{2,}", " ", out).strip()
    if out and not out.endswith((".", "?", "!")):
        out += "."
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prefix", default="")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    banks = bootstrap()
    facts = banks.load_all_facts()

    replacements: dict[str, str] = {}
    for fact in facts:
        if args.prefix and not fact["topic"].startswith(args.prefix):
            continue
        for choice in [fact["correct"], *fact["distractors"]]:
            new = strip(choice)
            if new != choice:
                replacements[choice] = new

    print(f"{len(replacements)} options would lose a padding tail\n")
    for old, new in list(replacements.items())[:12]:
        print(f"- {old}\n+ {new}\n")

    if not args.apply:
        print("dry run; pass --apply to write")
        return

    changed = 0
    for path in sorted((SEED / "banks").rglob("*.py")):
        source = path.read_text(encoding="utf-8")
        original = source
        for old, new in replacements.items():
            for quote in ('"', "'"):
                needle = f"{quote}{old}{quote}"
                if needle in source:
                    source = source.replace(needle, f"{quote}{new}{quote}")
        if source != original:
            path.write_text(source, encoding="utf-8")
            changed += 1
            print(f"updated {path.relative_to(ROOT)}")
    print(f"{changed} files updated")


if __name__ == "__main__":
    main()
