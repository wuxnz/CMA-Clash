# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Load raw facts from source bank modules (no materialization)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from classquiz.seed import sources as S
from classquiz.seed.stem_normalize import normalize_stem

_BANKS = Path(__file__).resolve().parent


def _bank_facts(module_name: str) -> list[dict]:
    path = _BANKS / f"{module_name}.py"
    spec = importlib.util.spec_from_file_location(f"_bank_{module_name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.FACTS


from .ccma import FACTS as CCMA_FACTS
CLINICAL_SKILLS_FACTS = _bank_facts("clinical_skills")
CPR_BLS_FACTS = _bank_facts("cpr_bls")
from .ekg import FACTS as EKG_FACTS
PHLEBOTOMY_FACTS = _bank_facts("phlebotomy")
DIABETES_FACTS = _bank_facts("diabetes")
PHLEB_GLUCOSE_FACTS = _bank_facts("phleb_glucose")
SUPPLEMENT_FACTS = []
for _supp_name in ("clinical_skills", "cpr_bls", "phlebotomy"):
    _p = _BANKS / "supplement" / f"{_supp_name}.py"
    _spec = importlib.util.spec_from_file_location(f"_supp_{_supp_name}", _p)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    SUPPLEMENT_FACTS.extend(_mod.FACTS)
EXPANSION_TO_28_FACTS = _bank_facts("expansion_to_28")
EXPANSION_GROWTH_FACTS = _bank_facts("expansion_growth")
EXPANSION_AUDIT_REPLACEMENTS = _bank_facts("expansion_audit_replacements")
_diab_exp_spec = importlib.util.spec_from_file_location(
    "_bank_diabetes_expansion", _BANKS / "supplement" / "diabetes_expansion.py"
)
_diab_exp = importlib.util.module_from_spec(_diab_exp_spec)
_diab_exp_spec.loader.exec_module(_diab_exp)
DIABETES_EXPANSION_FACTS = _diab_exp.FACTS

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


def load_source_facts() -> list[dict]:
    merged: list[dict] = []
    seen: set[str] = set()
    for facts in _ALL_MODULES:
        for fact in facts:
            prepared = _normalize_references(dict(fact))
            key = normalize_stem(prepared["stem"])
            if key in seen:
                continue
            seen.add(key)
            merged.append(prepared)
    return merged
