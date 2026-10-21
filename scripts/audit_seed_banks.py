#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

"""Offline audit of seed banks (no FastAPI app import)."""

from __future__ import annotations

import importlib.util
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
    _load("classquiz.seed.fact_finalize", SEED / "fact_finalize.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def main() -> None:
    banks = bootstrap()
    catalog = _load("classquiz.seed.catalog", SEED / "catalog.py")
    facts = banks.load_all_facts()
    growth_path = SEED / "banks" / "expansion_growth.py"
    growth_n = len(re.findall(r'^\s+\("', growth_path.read_text(), re.M))
    topic_to_cert = {
        slug: cert["slug"] for cert in catalog.CERTIFICATIONS for slug, _, _ in cert["topics"]
    }
    by_cert: dict[str, int] = defaultdict(int)
    for f in facts:
        by_cert[topic_to_cert.get(f["topic"], "?")] += 1
    norms = [sys.modules["classquiz.seed.stem_normalize"].normalize_stem(f["stem"]) for f in facts]
    dupes = [s for s, c in Counter(norms).items() if c > 1]

    def sent_count(t: str) -> int:
        return len([p for p in re.split(r"[.!?]+", t) if p.strip()])

    short = [f["stem"][:60] for f in facts if len(f["explanation"]) < 80 or sent_count(f["explanation"]) < 2]
    long_d = sum(1 for f in facts for d in f["distractors"] if len(d) > 58)

    print("total", len(facts))
    print("growth_tuples", growth_n)
    print("duplicates", len(dupes))
    print("short_explanations", len(short))
    print("long_distractors", long_d)
    for c in sorted(by_cert):
        print(f"cert {c} {by_cert[c]}")


if __name__ == "__main__":
    main()
