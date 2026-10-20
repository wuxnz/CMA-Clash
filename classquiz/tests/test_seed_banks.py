# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest
from collections import Counter

pytestmark = pytest.mark.order("last")

from classquiz.seed.banks import load_all_facts


def test_question_bank_coverage():
    facts = load_all_facts()
    assert len(facts) >= 360
    counts = Counter(f["topic"] for f in facts)
    assert len(counts) >= 31
    assert min(counts.values()) >= 12
