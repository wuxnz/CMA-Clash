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
    random.seed(seed)
    banks = bootstrap()
    facts = banks.load_all_facts()
    if cert_filter == "cpr":
        facts = [f for f in facts if f["topic"].startswith("cpr-")]
    for tier in ("beginner", "intermediate", "advanced"):
        pool = [f for f in facts if f.get("difficulty") == tier]
        picks = random.sample(pool, min(2, len(pool)))
        print(f"=== {tier} ===")
        for f in picks:
            print("STEM:", f["stem"])
            print("A)", f["correct"])
            for i, d in enumerate(f["distractors"], 1):
                print(f"{chr(65 + i)})", d)
            print("ANSWER: A")
            print("EXPL:", f["explanation"])
            print()


if __name__ == "__main__":
    main()
