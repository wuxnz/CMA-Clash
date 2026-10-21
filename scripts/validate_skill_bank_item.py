#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Validate Clinical Skills seed items against the parallel-options quality bar.

Mirrors the guards in ``classquiz/tests/test_seed_hand_authored_quality.py`` so a
single item can be checked while it is being written, without running pytest.

Usage:
    python scripts/validate_skill_bank_item.py --module osha_bbp
    python scripts/validate_skill_bank_item.py --module osha_bbp --item 7
    python scripts/validate_skill_bank_item.py --all
    python scripts/validate_skill_bank_item.py --dump osha_bbp
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

# ---------------------------------------------------------------------------
# Shared patterns (kept in sync with classquiz/tests/test_seed_hand_authored_quality.py)
# ---------------------------------------------------------------------------

GLOBAL_BANNED_DISTRACTOR_PATTERNS = [
    re.compile(r"\bhiding\s+aed", re.I),
    re.compile(r"\bhide\s+the\s+aed\b", re.I),
    re.compile(r"\bremoving\s+911\b", re.I),
    re.compile(r"\bremove\s+911\b", re.I),
    re.compile(r"\bposted\s+online\b", re.I),
    re.compile(r"\bshoe\s+comfort\b", re.I),
    re.compile(r"\bleave\s+to\s+find\s+food\b", re.I),
    re.compile(r"\bvision\s+acuity\b", re.I),
    re.compile(r"\bdental\s+health\b", re.I),
    re.compile(r"^\s*posted\s+online\s*$", re.I),
    re.compile(r"social\s+media\s+posts\s+about\s+health", re.I),
    re.compile(r"\bwaving\s+hello\b", re.I),
    re.compile(r"\bfoot\s+stamping\b", re.I),
]

SKILL_ABSURD_DISTRACTOR_PATTERNS = GLOBAL_BANNED_DISTRACTOR_PATTERNS + [
    re.compile(r"\bsocial\s+media\b", re.I),
    re.compile(r"\bshoe\s+size\b", re.I),
    re.compile(r"\bcosmetic\b", re.I),
    re.compile(r"\birrelevant\b", re.I),
    re.compile(r"\bignore\b", re.I),
    re.compile(r"\bhide\b", re.I),
    re.compile(r"\bjob\s+title\b", re.I),
    re.compile(r"\btutorials\b", re.I),
    re.compile(r"\bpharmacists\b", re.I),
    re.compile(r"\bparking\s+spot\b", re.I),
    re.compile(r"\bplacebo\b", re.I),
    re.compile(r"\bwindowsill\b", re.I),
    re.compile(r"\bfootwear\b", re.I),
    re.compile(r"\bloudspeaker\b", re.I),
]

# Correct answers that hedge with policy/training language telegraph the key.
HEDGED_CORRECT_PATTERNS = [
    re.compile(r"\bper\s+training\b", re.I),
    re.compile(r"\bwhen\s+policy\s+requires\b", re.I),
    re.compile(r"\bin\s+appropriate\s+patients\s+and\s+settings\b", re.I),
    re.compile(r"\bper\s+provider\s+or\s+protocol\b", re.I),
    re.compile(r"\bwhen\s+feasible\b", re.I),
    re.compile(r"\bas\s+applicable\b", re.I),
    re.compile(r"\bwhen\s+technique\s+is\s+correct\b", re.I),
    re.compile(r"\bper\s+(policy|protocol|manufacturer|label|facility)\b", re.I),
    re.compile(r"\bwhen\s+(required|indicated|feasible|appropriate)\s+by\b", re.I),
    re.compile(r"\bas\s+(directed|ordered)\s+by\s+the\s+provider\b", re.I),
    re.compile(r"\bif\s+(available|indicated)\b", re.I),
]

# Distractors padded with obvious technique errors students would not pick.
SELF_REFUTING_DISTRACTOR_PATTERNS = [
    re.compile(r"\bhousehold\s+bleach\b", re.I),
    re.compile(r"\bprinter\s+tray\b", re.I),
    re.compile(r"\bwithout\s+asking\b", re.I),
    re.compile(r"\bfavorite\s+brand\b", re.I),
    re.compile(r"\brelative'?s\s+smoking\b", re.I),
    re.compile(r"\bwithout\s+verifying\b", re.I),
    re.compile(r"\bloosely\s+touching\b", re.I),
    re.compile(r"\bwithout\s+hair\s+pulled\b", re.I),
    re.compile(r"\bear\s+canal\s+wall\b", re.I),
    re.compile(r"\bunfiltered\s+tap\s+water\b", re.I),
    re.compile(r"\bpoured\s+into\b", re.I),
    re.compile(r"\bwaiting\s+area\b.*\bname\s+visible\b", re.I),
    re.compile(r"\bnever\s+(happens|occurs|comes)\b", re.I),
    re.compile(r"\bnobody\s+\w+", re.I),
    re.compile(r"\bskip\s+(the\s+)?(hand\s+hygiene|gloves|safety)", re.I),
    re.compile(r"\bwithout\s+(gloves|eye\s+protection|hand\s+hygiene)", re.I),
    re.compile(r"\bturn\s+(off|off)\s+the\s+alarm\b", re.I),
    re.compile(r"\bignore\s+(the|any)\b", re.I),
]

BANNED_DISTRACTOR_QUALIFIER = re.compile(
    r"\b(only|always|never|skip|unmeasurable)\b|"
    r"\bavoid any\b|"
    r"\bstandard\s*$",
    re.I,
)

DASH_CHARS = re.compile(r"[\u2013\u2014]")
PRESENTS_FOR_CARE = re.compile(r"presents\s+for\s+care", re.I)
COLON_FRAGMENT_STEM = re.compile(r":\s*\?\s*$")
FRAGMENT_MUST_BE = re.compile(r"\bmust\s+be\s*\?\s*$", re.I)
INCOMPLETE_STEM_END = re.compile(
    r"\b("
    r"should be|must be|includes|requires|because|should prompt|should include|"
    r"the first priority is|is best prevented by|is called|should usually be held"
    r")\?\s*$",
    re.I,
)
FRAGMENT_TAIL_QUESTION = re.compile(
    r"(?:"
    r"\bis placed\?|\bshould\?|\bfrom the\?|\bof\?|\bbe\?|\bserves as\?|"
    r"\bare\?|\bshows\?|\bhelp by\?|\brecords\?|\binclude\?|"
    r"\bfunctions mainly as\?|\bis typically\?|\bis commonly placed\?|"
    r"\bis created by viewing from\?|\bis placed at the\?|\bis typically placed\?|"
    r"\bis placed at\?|\bis typically at\?|\bto detect\?|\bto assess\?|"
    r"\bto evaluate\?|\bto improve visualization of\?|"
    r"\badds posterior leads to improve visualization of\?"
    r")\s*$",
    re.I,
)

# Absolute/one-sided wording that makes exactly one option defensible.
ABSOLUTE_OPTION_PATTERNS = [
    re.compile(r"\bnever\b", re.I),
    re.compile(r"\balways\b", re.I),
    re.compile(r"\bevery\s+(patient|time|shift|encounter)\b", re.I),
    re.compile(r"\ball\s+(patients|visits|encounters)\b", re.I),
    re.compile(r"\bany\s+(body\s+fluid|patient|time)\b", re.I),
    re.compile(r"\bcannot\s+ever\b", re.I),
]

NEGATION_WORDS = {
    "not",
    "no",
    "never",
    "without",
    "non",
    "except",
    "omit",
    "omitted",
    "skip",
    "avoid",
    "before",
    "after",
    "during",
    "while",
    "un",
}

STOPWORDS = {
    "a",
    "an",
    "the",
    "of",
    "to",
    "in",
    "on",
    "at",
    "for",
    "and",
    "or",
    "is",
    "are",
    "be",
    "with",
    "by",
    "from",
    "that",
    "this",
    "it",
    "as",
    "should",
    "must",
    "may",
    "can",
    "will",
    "would",
    "when",
    "if",
    "than",
    "then",
    "their",
    "its",
    "his",
    "her",
    "they",
    "them",
    "you",
    "your",
    "not",
    "no",
}


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


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
    _load("classquiz.seed.fact_finalize", SEED / "fact_finalize.py")
    _load("classquiz.seed.fact_choice_hardening", SEED / "fact_choice_hardening.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


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


def load_module_items(module: str) -> list[dict]:
    """Return the raw facts for one clinical skills module, in file order."""
    bootstrap()
    path = SEED / "banks" / "clinical_skills" / MODULE_FILES[module]
    mod = _load(f"_skill_bank_{module}", path)
    return list(mod.FACTS)


def load_all_skill_items() -> list[tuple[str, int, dict]]:
    out: list[tuple[str, int, dict]] = []
    for module in MODULE_FILES:
        for idx, f in enumerate(load_module_items(module), start=1):
            out.append((module, idx, f))
    return out


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOPWORDS}


def _content_tokens(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOPWORDS]


def _sentence_count(text: str) -> int:
    return len([p for p in re.split(r"[.!?]+", text) if p.strip()])


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def check_item(fact: dict, stem: str | None = None) -> tuple[list[str], list[str]]:
    """Return (problems, review_prompts) for one item.

    Problems are hard failures that mirror the pytest guards. Review prompts are
    heuristics that need a human read (for example a distractor that is almost a
    paraphrase of the key, which is expected for a good parallel-options item but
    can also hide a second defensible answer).
    """
    problems: list[str] = []
    reviews: list[str] = []
    stem = stem if stem is not None else fact["stem"]
    correct = fact["correct"]
    distractors = list(fact["distractors"])
    explanation = fact.get("explanation") or ""
    choices = [correct, *distractors]

    # Stem shape
    if PRESENTS_FOR_CARE.search(stem):
        problems.append("stem uses the generic 'presents for care' filler")
    if stem.strip().endswith(":"):
        problems.append("stem ends with a colon fragment")
    if COLON_FRAGMENT_STEM.search(stem) or FRAGMENT_MUST_BE.search(stem):
        problems.append("stem is a colon/must-be fragment")
    if INCOMPLETE_STEM_END.search(stem):
        problems.append("stem ends mid-clause")
    if FRAGMENT_TAIL_QUESTION.search(stem):
        problems.append("stem ends with a fragment tail")
    if not stem.strip().endswith("?") and not stem.strip().endswith("."):
        problems.append("stem is not a complete question")
    if re.search(r"__+|\bTBD\b|\bTODO\b|\[.*?\]", stem):
        problems.append("stem contains a placeholder")

    # Dashes
    for field, label in [(stem, "stem"), (correct, "correct"), (explanation, "explanation")]:
        if DASH_CHARS.search(field):
            problems.append(f"{label} contains an em/en dash")
    for d in distractors:
        if DASH_CHARS.search(d):
            problems.append(f"distractor contains an em/en dash: {d[:40]!r}")

    # Hedged correct answer
    for pat in HEDGED_CORRECT_PATTERNS:
        if pat.search(correct):
            problems.append(f"correct answer hedges ({pat.pattern}): {correct[:60]!r}")
            break

    # Self-refuting / absurd distractors
    for d in distractors:
        for pat in SELF_REFUTING_DISTRACTOR_PATTERNS:
            if pat.search(d):
                problems.append(f"distractor self-refutes ({pat.pattern}): {d[:60]!r}")
                break
        for pat in SKILL_ABSURD_DISTRACTOR_PATTERNS:
            if pat.search(d):
                problems.append(f"distractor uses an absurd pattern ({pat.pattern}): {d[:60]!r}")
                break

    # Banned qualifiers in distractors
    for d in distractors:
        if BANNED_DISTRACTOR_QUALIFIER.search(d):
            problems.append(f"distractor uses a banned qualifier: {d[:60]!r}")

    # Duplicate choices
    norms = [re.sub(r"\s+", " ", c.strip().lower()) for c in choices]
    if len(set(norms)) != len(norms):
        problems.append("duplicate answer options")

    # Length balance
    lengths = [len(c.strip()) for c in choices]
    max_len = max(lengths)
    if lengths[0] == max_len and sum(1 for n in lengths if n == max_len) == 1:
        problems.append(
            "correct answer is uniquely longest "
            f"({lengths[0]} vs {sorted(lengths)})"
        )
    if min(lengths) > 0 and lengths[0] - min(lengths) >= 22:
        problems.append("correct answer is much longer than the shortest option")

    # Explanation
    if len(explanation.strip()) < 80 or _sentence_count(explanation) < 2:
        problems.append("explanation is too short or under two sentences")

    # Second defensible answer heuristics
    correct_tokens = _tokens(correct)
    correct_all = set(_content_tokens(correct))
    for d in distractors:
        sim = _jaccard(correct_tokens, _tokens(d))
        if sim >= 0.7:
            reviews.append(
                f"distractor is near a paraphrase of the key (similarity {sim:.2f}): {d[:60]!r}"
            )
        diff = set(_content_tokens(correct)) ^ set(_content_tokens(d))
        if diff and diff <= NEGATION_WORDS and len(_content_tokens(correct)) >= 2:
            reviews.append(
                f"distractor differs from the key by one negation only ({sorted(diff)}): {d[:60]!r}"
            )
        d_all = set(_content_tokens(d))
        if correct_all and correct_all < d_all:
            reviews.append(
                f"distractor states the key's claim plus extra scope, so it may also be defensible: {d[:60]!r}"
            )
        elif d_all and d_all < correct_all:
            reviews.append(
                f"distractor is a narrower claim than the key, so the stem must exclude it: {d[:60]!r}"
            )
    absolutes = [c for c in choices if any(p.search(c) for p in ABSOLUTE_OPTION_PATTERNS)]
    if len(absolutes) == 1:
        reviews.append(
            f"only one option uses absolute wording, which makes it stand out: {absolutes[0][:60]!r}"
        )

    return problems, reviews


def check_module(module: str) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    items = load_module_items(module)
    problems_by_item: dict[str, list[str]] = {}
    reviews_by_item: dict[str, list[str]] = {}
    for idx, f in enumerate(items, start=1):
        key = f"{module}-{idx:03d}"
        problems, reviews = check_item(f)
        if problems:
            problems_by_item[key] = problems
        if reviews:
            reviews_by_item[key] = reviews
    return problems_by_item, reviews_by_item


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def dump_module(module: str, only: int | None = None) -> None:
    items = load_module_items(module)
    for idx, f in enumerate(items, start=1):
        if only is not None and idx != only:
            continue
        print(f"--- {module}-{idx:03d} ({f.get('difficulty')}) ---")
        print(f"STEM: {f['stem']}")
        print(f"A) {f['correct']}")
        for i, d in enumerate(f["distractors"], start=1):
            print(f"{chr(65 + i)}) {d}")
        print(f"EXPL: {f['explanation']}")
        print()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--module", choices=sorted(MODULE_FILES))
    ap.add_argument("--item", type=int, help="1-based item number within the module")
    ap.add_argument("--all", action="store_true", help="check every clinical skills module")
    ap.add_argument("--dump", help="print full text of a module for review")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on any finding")
    args = ap.parse_args()

    if args.dump:
        dump_module(args.dump, args.item)
        return

    targets = sorted(MODULE_FILES) if args.all else [args.module]
    if not targets or targets == [None]:
        ap.error("provide --module, --all, or --dump")

    total_problems = 0
    total_reviews = 0
    for module in targets:
        problems_by_item, reviews_by_item = check_module(module)
        if args.item is not None:
            suffix = f"-{args.item:03d}"
            problems_by_item = {k: v for k, v in problems_by_item.items() if k.endswith(suffix)}
            reviews_by_item = {k: v for k, v in reviews_by_item.items() if k.endswith(suffix)}
        print(f"== {module}: {len(problems_by_item)} problem item(s), "
              f"{len(reviews_by_item)} review item(s) ==")
        for key, problems in problems_by_item.items():
            print(f"  {key}")
            for p in problems:
                print(f"    - {p}")
        for key, reviews in reviews_by_item.items():
            print(f"  {key} (review)")
            for r in reviews:
                print(f"    ? {r}")
        total_problems += sum(len(v) for v in problems_by_item.values())
        total_reviews += sum(len(v) for v in reviews_by_item.values())
    print(f"\ntotal problems: {total_problems}   total review prompts: {total_reviews}")
    if args.strict and total_problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
