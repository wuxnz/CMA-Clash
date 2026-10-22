"""List seed items that fail the choice-quality and explanation-quality gates."""

from __future__ import annotations

import importlib.util
import math
import re
import sys
import types
from collections import Counter, defaultdict
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


def _sentence_count(text: str) -> int:
    return len([p for p in re.split(r"[.!?]+", text) if p.strip()])


def main() -> None:
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    banks = bootstrap()
    facts = banks.load_all_facts()

    if which in ("all", "giveaway"):
        print("== giveaway absolutes in distractors ==")
        give = re.compile(r"\b(always|never|any|random)\b|(?<![\w-])only(?![\w-])", re.I)
        n = 0
        for f in facts:
            for d in f["distractors"]:
                if give.search(d) and not give.search(f["correct"]):
                    print(f"  {f['topic']} | {f['stem'][:55]} | {d[:70]}")
                    n += 1
        print(f"  total {n}")

    if which in ("all", "length"):
        print("== distractors over 80 chars ==")
        n = 0
        for f in facts:
            for d in f["distractors"]:
                if len(d) > 80:
                    print(f"  {f['topic']} | {f['stem'][:55]} | {len(d)} | {d[:90]}")
                    n += 1
        print(f"  total {n}")

    if which in ("all", "explanation"):
        print("== short explanations ==")
        n = 0
        for f in facts:
            expl = (f.get("explanation") or "").strip()
            if len(expl) < 80 or _sentence_count(expl) < 2:
                print(f"  {f['topic']} | {f['stem'][:60]}")
                n += 1
        print(f"  total {n}")

    if which in ("all", "difficulty"):
        print("== difficulty skew ==")
        by_topic: dict[str, Counter[str]] = defaultdict(Counter)
        for f in facts:
            by_topic[f["topic"]][f["difficulty"]] += 1
        for topic, counts in sorted(by_topic.items()):
            n = sum(counts.values())
            if n < 10:
                continue
            for label, target in (("beginner", 0.30), ("intermediate", 0.40), ("advanced", 0.30)):
                share = counts[label] / n
                if abs(share - target) > 0.12:
                    print(
                        f"  {topic} {label} share={share:.3f} target={target} "
                        f"counts={dict(counts)}"
                    )

    if which in ("all", "longest"):
        print("== longest-correct chunks ==")
        from classquiz.seed.catalog import TOPIC_QUESTIONS_PER_QUIZ
        from classquiz.seed.fact_choice_hardening import is_correct_strictly_longest

        grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
        for f in facts:
            grouped[(f["topic"], f["difficulty"])].append(f)
        for (topic, diff), items in sorted(grouped.items()):
            items.sort(key=lambda f: f["stem"])
            chunk_size = TOPIC_QUESTIONS_PER_QUIZ.get(topic, 28)
            for start in range(0, len(items), chunk_size):
                chunk = items[start : start + chunk_size]
                longest = sum(1 for f in chunk if is_correct_strictly_longest(f))
                ratio = 0.30 if len(chunk) >= 20 else 0.42
                allowed = max(1, math.ceil(len(chunk) * ratio))
                if longest > allowed:
                    print(f"  {topic} {diff} chunk {start // chunk_size + 1}: {longest} > {allowed}")


if __name__ == "__main__":
    main()
