# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest
from collections import Counter

pytestmark = pytest.mark.order("last")

from classquiz.seed.banks import load_all_facts
from classquiz.seed.catalog import CERTIFICATIONS
from classquiz.seed.stem_normalize import normalize_stem


def test_question_bank_coverage():
    facts = load_all_facts()
    assert len(facts) >= 2000
    counts = Counter(f["topic"] for f in facts)
    catalog_slugs = {slug for cert in CERTIFICATIONS for slug, _, _ in cert["topics"]}
    assert catalog_slugs.issubset(set(counts.keys()))
    assert len(counts) == 45
    assert min(counts.values()) >= 28
    for fact in facts:
        refs = fact.get("references") or []
        assert refs, f"Missing references on: {fact['stem'][:60]}"
        assert any("https://" in r for r in refs), fact["stem"][:80]


def test_all_facts_have_nonempty_explanation():
    facts = load_all_facts()
    missing = [f["stem"][:80] for f in facts if not (f.get("explanation") or "").strip()]
    assert not missing, f"Missing explanations: {missing[:5]}"


def test_unique_question_stems_globally():
    facts = load_all_facts()
    norms = [normalize_stem(f["stem"]) for f in facts]
    counts = Counter(norms)
    duplicates = [stem for stem, n in counts.items() if n > 1]
    assert not duplicates, f"Duplicate stems: {duplicates[:5]}"


def test_supplement_uses_authoritative_urls():
    facts = load_all_facts()
    domains = (
        "cdc.gov",
        "osha.gov",
        "heart.org",
        "hhs.gov",
        "who.int",
        "nhanow.com",
        "clsi.org",
        "fda.gov",
        "medlineplus.gov",
        "redcross.org",
        "diabetesjournals.org",
        "fda.gov",
    )
    with_url = [f for f in facts if any("https://" in r for r in f.get("references", []))]
    assert len(with_url) == len(facts)
    assert any(any(d in r for r in f.get("references", [])) for f in facts for d in domains)
