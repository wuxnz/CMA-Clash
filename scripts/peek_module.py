"""List the stems of a seed bank module (one item per line)."""

from __future__ import annotations

import importlib.util
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


def main() -> None:
    path = sys.argv[1]
    bootstrap()
    mod = _load("_peek", SEED / path)
    for i, f in enumerate(mod.FACTS, 1):
        print(f"{i:03d} [{f['difficulty'][:4]}] {f['stem']}")


if __name__ == "__main__":
    main()
