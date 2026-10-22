"""Audit every topic for content defects the repo guards do not cover.

Checks, per item:
  * a hedged keyed answer (softeners that dodge the question)
  * a distractor that is a softener/absolute the guard list misses
  * options that are not parallel (the key is much shorter or longer in shape)
  * a distractor that shares almost all of the key's content words, so it may be
    a second defensible answer
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import types
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"

# Softeners that make a keyed answer dodge the question.
HEDGED_KEY = re.compile(
    r"\b(per\s+(guidelines?|standards?|policy|policies|protocols?|manufacturer|"
    r"facility|label|textbook|reference)\b"
    r"|as\s+(appropriate|applicable|needed|required|ordered|per\s+\w+)\b"
    r"|when\s+(appropriate|applicable|needed|feasible|required|indicated)\b"
    r"|if\s+(appropriate|applicable|needed|feasible|required|indicated)\b"
    r"|depending\s+on\s+(the\s+)?(patient|clinical|individual)\b"
    r"|in\s+(some|many|most|certain)\s+(cases|instances|situations)\b"
    r"|may\s+(vary|differ|be)\b"
    r"|typically|generally|usually|often\b"
    r"|\b(reasonable|commonly|standard)\s+practice\b"
    r"|at\s+the\s+discretion\b"
    r"|where\s+applicable\b"
    r"|as\s+determined\s+by\b"
    r"|based\s+on\s+(the\s+)?(patient|clinical|individual)\b"
    r")",
    re.I,
)

SOFTENER = re.compile(
    r"\b(always|never|any|random|only)\b", re.I
)

STOP = {
    "a", "an", "the", "of", "to", "in", "on", "at", "for", "and", "or", "is",
    "are", "be", "with", "by", "from", "as", "that", "this", "it", "should",
    "must", "may", "can", "will", "would", "when", "if", "than", "then", "their",
    "its", "not", "no", "s", "does", "do", "has", "have", "was", "were",
}


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def bootstrap():
    sys.modules["classquiz"] = types.ModuleType("classquiz")
    sys.modules["classquiz"].__path__ = [str(ROOT / "classquiz")]
    pkg = types.ModuleType("classquiz.seed")
    pkg.__path__ = [str(SEED)]
    sys.modules["classquiz.seed"] = pkg
    _load("classquiz.seed.sources", SEED / "sources.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    _load("classquiz.seed.catalog", SEED / "catalog.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOP}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", default="")
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args()

    banks = bootstrap()
    facts = [f for f in banks.load_all_facts() if f["topic"].startswith(args.prefix)]

    by_type: Counter[str] = Counter()
    by_topic: dict[str, Counter[str]] = defaultdict(Counter)
    rows = []
    for f in facts:
        key = f["correct"]
        issues = []
        if HEDGED_KEY.search(key):
            issues.append(f"hedged key: {key[:60]!r}")
        for d in f["distractors"]:
            hit = SOFTENER.search(d)
            if hit:
                issues.append(f"softener {hit.group(1)!r} in distractor: {d[:55]!r}")
        kt = tokens(key)
        for d in f["distractors"]:
            dt = tokens(d)
            if kt and dt:
                overlap = len(kt & dt) / len(kt | dt)
                if overlap >= 0.8:
                    issues.append(f"near-duplicate of key ({overlap:.2f}): {d[:55]!r}")
        lens = [len(c.strip()) for c in [key, *f["distractors"]]]
        if lens[0] > max(lens[1:]) + 12:
            issues.append(f"key much longer than every distractor {lens}")
        if issues:
            by_topic[f["topic"]]["items"] += 1
            for i in issues:
                by_type[i.split(":")[0].split("(")[0].strip()] += 1
                by_topic[f["topic"]][i.split(":")[0].split("(")[0].strip()] += 1
            rows.append((f["topic"], f["stem"], issues))

    print(f"{len(facts)} items checked")
    print("issue totals:", dict(by_type))
    print()
    for topic in sorted(by_topic):
        print(f"  {topic:<28} {dict(by_topic[topic])}")
    if args.show:
        print()
        for topic, stem, issues in rows:
            print(f"{topic} | {stem[:70]}")
            for i in issues:
                print("   -", i)


if __name__ == "__main__":
    main()
