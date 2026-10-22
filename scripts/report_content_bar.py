"""Print every flagged item with its full option set so rewrites can be authored."""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"

HEDGED_KEY = re.compile(
    r"\b(per\s+(guidelines?|standards?|policy|policies|protocols?|manufacturer|"
    r"facility|label|textbook|reference)\b"
    r"|as\s+(appropriate|applicable|needed|required|ordered)\b"
    r"|when\s+(appropriate|applicable|needed|feasible|required|indicated)\b"
    r"|if\s+(appropriate|applicable|needed|feasible|required|indicated)\b"
    r"|depending\s+on\s+(the\s+)?(patient|clinical|individual)\b"
    r"|in\s+(some|many|most|certain)\s+(cases|instances|situations)\b"
    r"|may\s+(vary|differ|be)\b"
    r"|typically|generally|usually|\boften\b"
    r"|\b(reasonable|commonly|standard)\s+practice\b"
    r"|at\s+the\s+discretion\b"
    r"|where\s+applicable\b"
    r"|as\s+determined\s+by\b"
    r"|based\s+on\s+(the\s+)?(patient|clinical|individual)\b"
    r")",
    re.I,
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


# A stem that is a truncated question ("Accounts receivable tracks?").
FRAGMENT_STEM = re.compile(
    r"^(?!.*\b(what|which|why|how|when|where|who|does|do|is|are|in|at|on|for|"
    r"the|a|an|under|after|before|during|if|you|your|before|following|given)\b)"
    r"[^?]{6,90}\?$",
    re.I,
)
# The machine template "How should X be assessed on the tracing?".
TRACING_STEM = re.compile(r"\bassessed on the tracing\b", re.I)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", default="")
    args = ap.parse_args()

    banks = bootstrap()
    facts = [f for f in banks.load_all_facts() if f["topic"].startswith(args.prefix)]

    for f in facts:
        key = f["correct"]
        stem = f["stem"]
        issues = []
        if HEDGED_KEY.search(key):
            issues.append("HEDGE")
        if FRAGMENT_STEM.search(stem):
            issues.append("FRAGMENT")
        if TRACING_STEM.search(stem):
            issues.append("TRACING")
        lens = [len(c.strip()) for c in [key, *f["distractors"]]]
        if lens[0] > max(lens[1:]) + 12:
            issues.append("LONGER")
        kt = tokens(key)
        for d in f["distractors"]:
            dt = tokens(d)
            if kt and dt and len(kt & dt) / len(kt | dt) >= 0.8:
                issues.append("DUPP")
        if not issues:
            continue
        print(f"### {f['topic']} [{','.join(issues)}]")
        print(f"STEM: {stem}")
        print(f"KEY: {key}")
        for d in f["distractors"]:
            print(f"  D: {d}")
        print()


if __name__ == "__main__":
    main()
