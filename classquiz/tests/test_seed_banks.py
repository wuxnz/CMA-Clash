# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import importlib.util
from collections import Counter
from pathlib import Path


def _load_facts():
    init = Path(__file__).resolve().parents[1] / "seed" / "banks" / "__init__.py"
    spec = importlib.util.spec_from_file_location("cma_seed_banks", init)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load_all_facts()


def test_question_bank_coverage():
    facts = _load_facts()
    assert len(facts) >= 360
    counts = Counter(f["topic"] for f in facts)
    assert len(counts) >= 31
    assert min(counts.values()) >= 12
