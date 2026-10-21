# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Question fact banks for CMA Clash seed data."""

from classquiz.seed import sources as S
from classquiz.seed.fact_finalize import enrich_explanation, finalize_fact
from classquiz.seed.fact_choice_hardening import apply_choice_hardening
from classquiz.seed.stem_normalize import normalize_stem

from .ccma import FACTS as CCMA_FACTS
from .clinical_skills import FACTS as CLINICAL_SKILLS_FACTS
from .cpr_bls import FACTS as CPR_BLS_FACTS
from .ekg import FACTS as EKG_FACTS
from .phlebotomy import FACTS as PHLEBOTOMY_FACTS
from .diabetes import FACTS as DIABETES_FACTS
from .phleb_glucose import FACTS as PHLEB_GLUCOSE_FACTS
from .supplement import FACTS as SUPPLEMENT_FACTS
from .expansion_to_28 import FACTS as EXPANSION_TO_28_FACTS
from .expansion_growth import FACTS as EXPANSION_GROWTH_FACTS
from .expansion_audit_replacements import FACTS as EXPANSION_AUDIT_REPLACEMENTS
from .supplement.diabetes_expansion import FACTS as DIABETES_EXPANSION_FACTS

_DIABETES_ALL = DIABETES_FACTS + DIABETES_EXPANSION_FACTS

_ALL_MODULES = (
    CCMA_FACTS,
    CLINICAL_SKILLS_FACTS,
    CPR_BLS_FACTS,
    EKG_FACTS,
    PHLEBOTOMY_FACTS,
    _DIABETES_ALL,
    PHLEB_GLUCOSE_FACTS,
    SUPPLEMENT_FACTS,
    EXPANSION_TO_28_FACTS,
    EXPANSION_GROWTH_FACTS,
    EXPANSION_AUDIT_REPLACEMENTS,
)

_LEGACY_REFERENCE_MAP: dict[str, list[str]] = {
    "CDC": [S.CDC_STANDARD_PRECAUTIONS, S.CDC_HAND_HYGIENE],
    "NHA CCMA": [S.NHA_CCMA],
    "AHA BLS": [S.AHA_WHAT_IS_CPR, S.AHA_ADULT_BLS],
    "AHA": [S.AHA_WHAT_IS_CPR],
    "CLSI": [S.CLSI_GP41],
    "OSHA": [S.OSHA_BBP],
    "HIPAA": [S.HHS_HIPAA_PRIVACY],
}


def _normalize_references(fact: dict) -> dict:
    refs = fact.get("references") or []
    normalized: list[str] = []
    for ref in refs:
        if isinstance(ref, str) and "https://" in ref:
            normalized.append(ref)
        elif isinstance(ref, str) and ref in _LEGACY_REFERENCE_MAP:
            normalized.extend(_LEGACY_REFERENCE_MAP[ref])
        elif isinstance(ref, str):
            normalized.append(ref)
    if normalized:
        fact = {**fact, "references": normalized}
    return fact


def load_all_facts() -> list[dict]:
    """Return all seed question facts from every bank module."""
    merged: list[dict] = []
    seen_stems: set[str] = set()
    for facts in _ALL_MODULES:
        for fact in facts:
            finalized = finalize_fact(_normalize_references(fact))
            key = normalize_stem(finalized["stem"])
            if key in seen_stems:
                continue
            seen_stems.add(key)
            merged.append(finalized)
    merged = apply_choice_hardening(merged)
    for i, fact in enumerate(merged):
        merged[i] = {**fact, "explanation": enrich_explanation(fact)}
    return merged
