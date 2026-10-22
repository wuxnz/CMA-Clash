#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Run the seed quality guard tests without the full application stack.

``classquiz/tests/conftest.py`` pulls in the FastAPI app (and sentry_sdk), which
is not needed for the content guards. This runner stubs the app modules the seed
runner imports, then executes every ``test_*`` function in the seed-focused test
modules against the offline seed banks.

Usage:
    python scripts/run_seed_quality_checks.py [test_module ...]
"""

from __future__ import annotations

import importlib.util
import sys
import traceback
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"
TESTS = ROOT / "classquiz" / "tests"

DEFAULT_MODULES = (
    "test_seed_hand_authored_quality.py",
    "test_seed_banks.py",
    "test_seed_choice_quality.py",
    "test_seed_explanation_quality.py",
    "test_seed_answer_order.py",
    "test_diabetes_content.py",
)


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _stub_app_modules() -> None:
    """Provide the minimum app surface that classquiz.seed.runner imports."""
    if "classquiz.config" in sys.modules:
        return

    class _Answer:
        def __init__(self, right: bool, answer: str):
            self.right = right
            self.answer = answer

    class _Question:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def model_dump(self):
            return dict(self.__dict__)

    class _Type:
        ABCD = "abcd"

    config = types.ModuleType("classquiz.config")
    config.settings = lambda *a, **k: None
    config.meilisearch = types.SimpleNamespace(index=lambda *a, **k: None)
    sys.modules["classquiz.config"] = config

    db = types.ModuleType("classquiz.db")
    db.database = types.SimpleNamespace(get_or_none=lambda *a, **k: None)
    sys.modules["classquiz.db"] = db

    cma_models = types.ModuleType("classquiz.db.cma_models")
    cma_models.Certification = type("Certification", (), {})
    cma_models.Topic = type("Topic", (), {})
    sys.modules["classquiz.db.cma_models"] = cma_models

    models = types.ModuleType("classquiz.db.models")
    models.ABCDQuizAnswer = _Answer
    models.Quiz = type("Quiz", (), {})
    models.QuizQuestion = _Question
    models.QuizQuestionType = _Type
    models.User = type("User", (), {})
    sys.modules["classquiz.db.models"] = models

    auth = types.ModuleType("classquiz.auth")
    auth.get_password_hash = lambda *a, **k: "hash"
    sys.modules["classquiz.auth"] = auth

    helpers = types.ModuleType("classquiz.helpers")
    helpers.get_meili_data = lambda *a, **k: {}
    helpers.meilisearch_init = lambda *a, **k: None
    sys.modules["classquiz.helpers"] = helpers

    avatar = types.ModuleType("classquiz.helpers.avatar")
    avatar.gzipped_user_avatar = lambda *a, **k: b""
    sys.modules["classquiz.helpers.avatar"] = avatar


def bootstrap():
    sys.modules["classquiz"] = types.ModuleType("classquiz")
    pkg = types.ModuleType("classquiz.seed")
    pkg.__path__ = [str(SEED)]
    sys.modules["classquiz.seed"] = pkg
    for name, filename in (
        ("classquiz.seed.sources", "sources.py"),
        ("classquiz.seed.fact_finalize", "fact_finalize.py"),
        ("classquiz.seed.fact_choice_hardening", "fact_choice_hardening.py"),
        ("classquiz.seed.stem_normalize", "stem_normalize.py"),
        ("classquiz.seed.catalog", "catalog.py"),
    ):
        path = SEED / filename
        if path.exists():
            _load(name, path)
    _stub_app_modules()
    _load("classquiz.seed.banks", SEED / "banks" / "__init__.py")


def main() -> int:
    bootstrap()
    modules = sys.argv[1:] or list(DEFAULT_MODULES)
    failures = 0
    ran = 0
    for module_name in modules:
        path = TESTS / module_name
        if not path.exists():
            print(f"SKIP  {module_name} (not found)")
            continue
        guard = _load("_guard_" + module_name.replace(".py", ""), path)
        print(f"--- {module_name} ---")
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
                print(f"FAIL  {name}: {str(exc)[:400]}")
            except Exception:  # pragma: no cover - unexpected import/runtime errors
                failures += 1
                print(f"ERROR {name}")
                traceback.print_exc()
    print(f"\n{ran - failures}/{ran} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
