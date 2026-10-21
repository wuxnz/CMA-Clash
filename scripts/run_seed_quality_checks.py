#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Run the seed quality guard tests without the full application stack.

``classquiz/tests/conftest.py`` pulls in the FastAPI app (and sentry_sdk), which
is not needed for the content guards. This runner imports the guard module
directly and executes every ``test_*`` function against the offline seed banks.
"""

from __future__ import annotations

import importlib.util
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"
TESTS = ROOT / "classquiz" / "tests"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def bootstrap():
    sys.modules["classquiz"] = type(sys)("classquiz")
    pkg = type(sys)("classquiz.seed")
    pkg.__path__ = [str(SEED)]
    sys.modules["classquiz.seed"] = pkg
    _load("classquiz.seed.sources", SEED / "sources.py")
    _load("classquiz.seed.fact_finalize", SEED / "fact_finalize.py")
    _load("classquiz.seed.fact_choice_hardening", SEED / "fact_choice_hardening.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def main() -> int:
    bootstrap()
    guard = _load("_seed_guard", TESTS / "test_seed_hand_authored_quality.py")
    failures = 0
    ran = 0
    for name in sorted(dir(guard)):
        if not name.startswith("test_"):
            continue
        fn = getattr(guard, name)
        if not callable(fn):
            continue
        ran += 1
        try:
            fn()
            print(f"PASS  {name}")
        except AssertionError as exc:
            failures += 1
            print(f"FAIL  {name}: {exc}")
        except Exception:  # pragma: no cover - unexpected import/runtime errors
            failures += 1
            print(f"ERROR {name}")
            traceback.print_exc()
    print(f"\n{ran - failures}/{ran} guards passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
