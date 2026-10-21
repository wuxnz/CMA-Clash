"""Locate the specific items that trip each seed quality guard."""

from __future__ import annotations

import importlib.util
import re
import sys
import types
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
    _load("classquiz.seed.fact_finalize", SEED / "fact_finalize.py")
    _load("classquiz.seed.fact_choice_hardening", SEED / "fact_choice_hardening.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def main() -> None:
    only = sys.argv[1] if len(sys.argv) > 1 else ""
    banks = bootstrap()
    facts = banks.load_all_facts()
    guard = _load("_guard", ROOT / "classquiz" / "tests" / "test_seed_hand_authored_quality.py")

    def keep(topic: str) -> bool:
        return topic.startswith(only) if only else True

    print("== em/en dashes ==")
    for f in facts:
        if not keep(f["topic"]):
            continue
        if not guard._topic_matches_prefixes(f["topic"], guard._DASH_CHECK_CERT_PREFIXES):
            continue
        for field in guard._cert_fields(f):
            if guard._DASH_CHARS.search(field):
                print(f"  {f['topic']}: {field[:110]}")
                break

    print("== banned distractor qualifiers ==")
    for f in facts:
        if not keep(f["topic"]):
            continue
        if not guard._topic_matches_prefixes(f["topic"], guard._STRICT_QUALITY_CERT_PREFIXES):
            continue
        for d in f["distractors"]:
            if guard._BANNED_DISTRACTOR_QUALIFIER.search(d):
                print(f"  {f['topic']}: {d[:110]}")
                break

    print("== incomplete stems ==")
    for f in facts:
        if not keep(f["topic"]):
            continue
        if not guard._topic_matches_prefixes(f["topic"], guard._STEM_COMPLETE_CERT_PREFIXES):
            continue
        stem = f["stem"].strip()
        bad = (
            stem.endswith(":")
            or guard._INCOMPLETE_STEM_END.search(stem)
            or guard._COLON_FRAGMENT_STEM.search(stem)
            or guard._FRAGMENT_MUST_BE.search(stem)
            or (
                guard._topic_matches_prefixes(f["topic"], guard._STRICT_QUALITY_CERT_PREFIXES)
                and guard._FRAGMENT_TAIL_QUESTION.search(stem)
            )
            or not (stem.endswith("?") or stem.endswith("."))
        )
        if bad:
            print(f"  {f['topic']}: {stem[:110]}")

    print("== near duplicate stems ==")
    from classquiz.seed.stem_normalize import normalize_stem

    def toks(s):
        return set(re.findall(r"[a-z0-9]+", normalize_stem(s)))

    by_prefix: dict[str, list[dict]] = {}
    for f in facts:
        for p in guard._STRICT_QUALITY_CERT_PREFIXES:
            if f["topic"].startswith(p):
                by_prefix.setdefault(p, []).append(f)
                break
    for prefix, group in by_prefix.items():
        for i, a in enumerate(group):
            ta = toks(a["stem"])
            if not ta:
                continue
            for b in group[i + 1 :]:
                tb = toks(b["stem"])
                if not tb:
                    continue
                ov = len(ta & tb) / len(ta | tb)
                if ov >= 0.82:
                    print(f"  {prefix} {ov:.2f}: {a['topic']} | {b['topic']}")
                    print(f"      A: {a['stem'][:100]}")
                    print(f"      B: {b['stem'][:100]}")

    print("== banned absurd distractors (global) ==")
    for f in facts:
        if not keep(f["topic"]):
            continue
        for d in f["distractors"]:
            for pat in guard._GLOBAL_BANNED_DISTRACTOR_PATTERNS:
                if pat.search(d):
                    print(f"  {f['topic']}: {d[:110]}")
                    break

    print("== cpr short explanations ==")
    for f in facts:
        if not keep(f["topic"]):
            continue
        if not f["topic"].startswith("cpr-"):
            continue
        expl = (f.get("explanation") or "").strip()
        if len(expl) < 80 or guard._sentence_count(expl) < 2:
            print(f"  {f['topic']}: {expl[:140]}")

    print("== skill hedge tells ==")
    for f in facts:
        if not keep(f["topic"]):
            continue
        if not f["topic"].startswith("skill-"):
            continue
        for pat in guard._SKILL_HEDGED_CORRECT_PATTERNS:
            if pat.search(f["correct"]):
                print(f"  {f['topic']}: {f['correct'][:110]}")
                break

    print("== skill self-refuting distractors ==")
    for f in facts:
        if not keep(f["topic"]):
            continue
        if not f["topic"].startswith("skill-"):
            continue
        for d in f["distractors"]:
            for pat in guard._SKILL_SELF_REFUTING_DISTRACTOR_PATTERNS:
                if pat.search(d):
                    print(f"  {f['topic']}: {d[:110]}")
                    break


if __name__ == "__main__":
    main()
