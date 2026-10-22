#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

"""Print random sample questions per difficulty tier (for audit reports)."""

from __future__ import annotations

import importlib.util
import random
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
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 61
    cert_filter = sys.argv[2] if len(sys.argv) > 2 else "cpr"
    mix_certs = cert_filter == "mix"
    random.seed(seed)
    banks = bootstrap()
    facts = banks.load_all_facts()
    if cert_filter == "cpr":
        facts = [f for f in facts if f["topic"].startswith("cpr-")]
    elif cert_filter == "phleb":
        facts = [f for f in facts if f["topic"].startswith("phleb-")]
    elif cert_filter == "ekg":
        facts = [f for f in facts if f["topic"].startswith("ekg-")]
    elif cert_filter == "ccma":
        facts = [f for f in facts if f["topic"].startswith("ccma-")]
    elif cert_filter in ("clinical", "skill"):
        facts = [f for f in facts if f["topic"].startswith("skill-")]
    elif mix_certs:
        pools = {
            "ekg": [f for f in facts if f["topic"].startswith("ekg-")],
            "cpr": [f for f in facts if f["topic"].startswith("cpr-")],
            "phleb": [f for f in facts if f["topic"].startswith("phleb-")],
        }
        picks = []
        for key in ("ekg", "cpr", "phleb"):
            pool = pools[key]
            if pool:
                picks.append(random.choice(pool))
        while len(picks) < 6:
            pool = random.choice(list(pools.values()))
            if pool:
                picks.append(random.choice(pool))
        picks = picks[:6]
        for f in picks:
            _print_fact_with_shuffled_letter(f)
        return

    from classquiz.seed.choice_quality import seeded_correct_index

    for tier in ("beginner", "intermediate", "advanced"):
        pool = [f for f in facts if f.get("difficulty") == tier]
        picks = random.sample(pool, min(2, len(pool)))
        print(f"=== {tier} ===")
        for f in picks:
            _print_fact_with_shuffled_letter(f)


def _print_fact_with_shuffled_letter(f: dict) -> None:
    import hashlib
    import random as py_random

    from classquiz.seed.choice_quality import seeded_correct_index

    pairs: list[tuple[str, bool]] = [(f["correct"], True)] + [(d, False) for d in f["distractors"]]
    rng = py_random.Random(int(hashlib.sha256(f["stem"].encode("utf-8")).hexdigest()[:16], 16))
    rng.shuffle(pairs)
    idx = seeded_correct_index(f["stem"], f["correct"], f["distractors"])
    letter = chr(65 + idx)
    print("TOPIC:", f["topic"])
    print("STEM:", f["stem"])
    for i, (text, _right) in enumerate(pairs):
        print(f"{chr(65 + i)})", text)
    print(f"ANSWER: {letter} (post-seed shuffle index)")
    print("EXPL:", f["explanation"])
    print()


if __name__ == "__main__":
    main()
