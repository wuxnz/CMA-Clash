#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Propose and apply the mechanical choice-quality fixes.

Two transformations are applied to distractor text:

1. **Length.** A distractor over 80 characters is truncated at a natural clause
   boundary so the option keeps its clinical point but stops reading as the
   complete answer.
2. **Giveaway words.** ``always``, ``never``, ``any``, ``random`` and ``only``
   in a distractor are replaced or removed, because they tell the student the
   option is wrong.

Run with ``--dry-run`` to review every proposed change before applying.
"""

from __future__ import annotations

import argparse
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"

MAX_LEN = 80
MIN_LEN = 38

# Clause boundaries, most preferred first. Only these are used, and only when the
# result is a complete phrase rather than a dangling fragment.
BREAKS = [
    " without ",
    " so that ",
    " because ",
    " while ",
    " during ",
    " when ",
    " after ",
    " before ",
]

# Words that cannot end a phrase.
DANGLING = {
    "the",
    "a",
    "an",
    "of",
    "in",
    "on",
    "at",
    "to",
    "for",
    "with",
    "and",
    "or",
    "by",
    "from",
    "as",
    "that",
    "than",
    "over",
    "under",
    "into",
    "per",
    "via",
    "its",
    "their",
    "this",
    "these",
    "those",
    "such",
    "any",
    "each",
    "every",
    "both",
    "one",
    "two",
    "three",
}


def _is_clean(candidate: str) -> bool:
    """True when the candidate is a complete phrase with no dangling word."""
    words = candidate.split()
    if not words:
        return False
    last = words[-1].lower().strip(",.;:")
    if last in DANGLING:
        return False
    return True


def _trim_to_clean(text: str) -> str | None:
    """Drop a trailing clause at the best clean boundary that fits the cap."""
    best: str | None = None
    for marker in BREAKS:
        start = 0
        while True:
            idx = text.find(marker, start)
            if idx <= 0:
                break
            candidate = text[:idx].rstrip(" ,;")
            if MIN_LEN <= len(candidate) <= MAX_LEN and _is_clean(candidate):
                if best is None or len(candidate) > len(best):
                    best = candidate
            start = idx + 1
    if best is not None:
        return best
    # Fall back to a comma boundary, then to a clean word-boundary trim.
    for idx in range(len(text) - 1, MIN_LEN - 1, -1):
        if text[idx] == "," and MIN_LEN <= idx <= MAX_LEN and _is_clean(text[:idx]):
            return text[:idx].rstrip()
    trimmed = text[:MAX_LEN]
    cut = trimmed.rfind(" ")
    while cut > MIN_LEN and not _is_clean(trimmed[:cut]):
        cut = trimmed.rfind(" ", 0, cut)
    if cut > MIN_LEN:
        return trimmed[:cut].rstrip(" ,;")
    return None


def _load(name: str, path: Path):
    import importlib.util

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


def shorten(text: str) -> str | None:
    """Truncate a long option at a clause boundary, keeping the clinical claim."""
    text = text.strip()
    if len(text) <= MAX_LEN:
        return None
    return _trim_to_clean(text)


def de_giveaway(text: str) -> str | None:
    """Remove giveaway absolute words from an option.

    Only the unambiguous rewrites are automated. "any", "never" and "only" in a
    meaningful position need a human rewrite, so they are left alone here and
    reported for manual review.
    """
    out = text
    out = re.sub(r"\bwithout any\b", "without", out, flags=re.I)
    out = re.sub(r"\bwithout any other\b", "without further", out, flags=re.I)
    out = re.sub(r"\balways\b", "typically", out, flags=re.I)
    out = re.sub(r"\brandom\b", "arbitrary", out, flags=re.I)
    out = re.sub(r"\s{2,}", " ", out).strip(" ,")
    if out == text:
        return None
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prefix", default="", help="only topics starting with this prefix")
    ap.add_argument("--apply", action="store_true", help="write the changes to disk")
    args = ap.parse_args()

    banks = bootstrap()
    facts = banks.load_all_facts()

    replacements: dict[str, str] = {}
    for fact in facts:
        if args.prefix and not fact["topic"].startswith(args.prefix):
            continue
        correct = fact["correct"]
        give = re.compile(r"\b(always|never|any|random|only)\b", re.I)
        for d in fact["distractors"]:
            new = d
            if len(new.strip()) > MAX_LEN:
                shorter = shorten(new)
                if shorter:
                    new = shorter
            if give.search(new) and not give.search(correct):
                cleaner = de_giveaway(new)
                if cleaner:
                    new = cleaner
            if new != d:
                replacements[d] = new

    print(f"{len(replacements)} proposed changes\n")
    for old, new in replacements.items():
        flag = ""
        if len(new) > MAX_LEN:
            flag = "  [STILL LONG]"
        print(f"- {old}")
        print(f"+ {new}{flag}\n")

    if not args.apply:
        print("dry run; pass --apply to write")
        return

    # Apply to the source files as exact string replacements.
    files = sorted((SEED / "banks").rglob("*.py"))
    changed = 0
    for path in files:
        source = path.read_text(encoding="utf-8")
        original = source
        for old, new in replacements.items():
            needle = f'"{old}"'
            if needle in source:
                source = source.replace(needle, f'"{new}"')
        if source != original:
            path.write_text(source, encoding="utf-8")
            changed += 1
            print(f"updated {path.relative_to(ROOT)}")
    print(f"{changed} files updated")


if __name__ == "__main__":
    main()
