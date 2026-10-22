"""Dump every item that trips the two strict hand-authored seed guards.

Reproduces the checks in ``classquiz/tests/test_seed_hand_authored_quality.py``
without the 12-item truncation the assertions use, so every offender can be
listed with its full option set.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from run_seed_quality_checks import bootstrap  # noqa: E402

bootstrap()

from classquiz.seed.banks import load_all_facts  # noqa: E402
from classquiz.seed.choice_quality import (  # noqa: E402
    correct_is_uniquely_short_by_margin,
)

# Mirrors of the guard module's private patterns.
_INCOMPLETE_STEM_END = re.compile(
    r"\b("
    r"should be|must be|includes|requires|because|should prompt|should include|"
    r"the first priority is|is best prevented by|is called|should usually be held"
    r")\s*\?\s*$",
    re.I,
)
_FRAGMENT_MUST_BE = re.compile(r"\bmust\s+be\s*\?\s*$", re.I)
_COLON_FRAGMENT_STEM = re.compile(r":\s*\?\s*$")
_FRAGMENT_CLAUSE_WAS = re.compile(
    r"(?:^|[.;])\s*[^?]{8,120}\b(was|is|are|were)\?\s*$",
    re.I,
)
_MID_STEM_CAPITAL_ARTICLE = re.compile(r"[a-z] (A|An|The) [A-Z]")
_FRAGMENT_STEM_NO_WH = re.compile(
    r"^(?!.*\b(what|which|why|how|when|where|who|does|do|is|are"
    r"|was|were|can|could|should|would|will|may|might)\b).+\?\s*$",
    re.I,
)
_FRAGMENT_TAIL_QUESTION = re.compile(
    r"(?:"
    r"\bis placed\?|\bshould\?|\bfrom the\?|\bof\?|\bbe\?|\bserves as\?|"
    r"\bare\?|\bshows\?|\bhelp by\?|\brecords\?|\binclude\?|"
    r"\bcontains\?|\bprovides\?|\brequires\?|\bincludes\?|"
    r"\bmeans\?|\bdoes\?|\bperforms\?|\bcarries\?|\bholds\?"
    r")\s*$",
    re.I,
)

_STRICT = ("ekg-", "cpr-", "ccma-", "phleb-")
_STEM_COMPLETE = ("cpr-", "phleb-", "ekg-", "ccma-")


def _matches(prefixes: tuple[str, ...], topic: str) -> bool:
    return topic.startswith(prefixes)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=("short", "stem", "both"), default="both")
    args = ap.parse_args()

    facts = load_all_facts()

    if args.only in ("short", "both"):
        print("=" * 70)
        print("UNIQUE SHORT KEY")
        print("=" * 70)
        for fact in facts:
            if not _matches(_STRICT, fact["topic"]):
                continue
            if correct_is_uniquely_short_by_margin(
                fact["correct"], fact["distractors"]
            ):
                lens = [len(fact["correct"].strip())] + [
                    len(d.strip()) for d in fact["distractors"]
                ]
                print(f"\n{fact['topic']}  lens={lens}")
                print(f"  STEM: {fact['stem']}")
                print(f"  KEY : {fact['correct']}")
                for d in fact["distractors"]:
                    print(f"    D : {d}")
                print(f"  EXPL: {fact['explanation']}")

    if args.only in ("stem", "both"):
        print()
        print("=" * 70)
        print("INCOMPLETE STEM")
        print("=" * 70)
        for fact in facts:
            topic = fact["topic"]
            stem = fact["stem"].strip()
            reasons = []
            if not _matches(_STEM_COMPLETE, topic):
                continue
            if stem.endswith(":"):
                reasons.append("ends with colon")
            if _INCOMPLETE_STEM_END.search(stem):
                reasons.append("incomplete tail")
            if _COLON_FRAGMENT_STEM.search(stem) or _FRAGMENT_MUST_BE.search(stem):
                reasons.append("colon fragment")
            if _matches(_STRICT, topic):
                if _FRAGMENT_TAIL_QUESTION.search(stem):
                    reasons.append("fragment tail question")
                if _FRAGMENT_CLAUSE_WAS.search(stem):
                    reasons.append("fragment clause was")
                if _MID_STEM_CAPITAL_ARTICLE.search(stem):
                    reasons.append("mid stem capital article")
            if _FRAGMENT_STEM_NO_WH.search(stem) and len(stem) < 120:
                reasons.append("no wh-word")
            if reasons:
                print(f"\n{topic}  {reasons}")
                print(f"  STEM: {stem}")
                print(f"  KEY : {fact['correct']}")
                for d in fact["distractors"]:
                    print(f"    D : {d}")
                print(f"  EXPL: {fact['explanation']}")


if __name__ == "__main__":
    main()
