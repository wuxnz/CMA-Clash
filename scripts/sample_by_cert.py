"""Sample items across every certification so the current standard can be eyeballed."""

from __future__ import annotations

import argparse
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
    sys.modules["classquiz"].__path__ = [str(ROOT / "classquiz")]
    pkg = types.ModuleType("classquiz.seed")
    pkg.__path__ = [str(SEED)]
    sys.modules["classquiz.seed"] = pkg
    _load("classquiz.seed.sources", SEED / "sources.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    _load("classquiz.seed.catalog", SEED / "catalog.py")
    return _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", default="")
    ap.add_argument("--count", type=int, default=2)
    ap.add_argument("--seed", type=int, default=11)
    args = ap.parse_args()

    banks = bootstrap()
    facts = [f for f in banks.load_all_facts() if f["topic"].startswith(args.prefix)]
    random.seed(args.seed)
    for f in random.sample(facts, min(args.count, len(facts))):
        print(f"=== {f['topic']} ===")
        print("STEM:", f["stem"])
        print("A)", f["correct"])
        for d in f["distractors"]:
            print("  D)", d)
        print("EXPL:", f["explanation"])
        print()


if __name__ == "__main__":
    main()
