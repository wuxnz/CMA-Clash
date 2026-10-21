#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0
"""Sample random questions from rewritten CPR/phleb batches (this run)."""

from __future__ import annotations

import hashlib
import importlib.util
import random
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"


def bootstrap():
    sys.modules["classquiz"] = types.ModuleType("classquiz")
    pkg = types.ModuleType("classquiz.seed")
    pkg.__path__ = [str(SEED)]
    sys.modules["classquiz.seed"] = pkg
    spec = importlib.util.spec_from_file_location("classquiz.seed.banks", SEED / "banks" / "__init__.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["classquiz.seed.banks"] = mod
    spec.loader.exec_module(mod)
    return mod


def seeded_index(stem: str, correct: str, distractors: list[str]) -> int:
    pairs: list[tuple[str, bool]] = [(correct, True)] + [(d, False) for d in distractors]
    rng = random.Random(int(hashlib.sha256(stem.encode("utf-8")).hexdigest()[:16], 16))
    rng.shuffle(pairs)
    return next(i for i, (_t, r) in enumerate(pairs) if r)


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 76
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    random.seed(seed)
    banks = bootstrap()
    facts = banks.load_all_facts()
    # Rewritten this run: cpr-adult 1-50, cpr-child 1-25 (extend as batches land)
    pool = []
    for f in facts:
        t = f["topic"]
        if t == "cpr-adult":
            pool.append(f)
        elif t in ("cpr-child", "cpr-infant", "cpr-aed", "cpr-choking"):
            pool.append(f)
        elif t in (
            "phleb-order-draw",
            "phleb-additives",
            "phleb-site",
            "phleb-handling",
            "phleb-complications",
        ):
            pool.append(f)
        elif t in ("cpr-chain", "cpr-red-cross"):
            pool.append(f)
    picks = random.sample(pool, min(n, len(pool)))
    for f in picks:
        pairs: list[tuple[str, bool]] = [(f["correct"], True)] + [(d, False) for d in f["distractors"]]
        rng = random.Random(int(hashlib.sha256(f["stem"].encode()).hexdigest()[:16], 16))
        rng.shuffle(pairs)
        idx = seeded_index(f["stem"], f["correct"], f["distractors"])
        letter = chr(65 + idx)
        print("TOPIC:", f["topic"])
        print("STEM:", f["stem"])
        for i, (text, _) in enumerate(pairs):
            print(f"{chr(65 + i)})", text)
        print(f"ANSWER: {letter}")
        print("EXPL:", f["explanation"])
        print("---")


if __name__ == "__main__":
    main()
