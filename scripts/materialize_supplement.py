#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0
"""Materialize supplement/*.py from explicit ITEMS (no templated stems)."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import importlib.util
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

_norm_spec = importlib.util.spec_from_file_location(
    "stem_normalize", ROOT / "classquiz/seed/stem_normalize.py"
)
_norm_mod = importlib.util.module_from_spec(_norm_spec)
_norm_spec.loader.exec_module(_norm_mod)
normalize_stem = _norm_mod.normalize_stem


def fact(
    topic: str,
    stem: str,
    correct: str,
    distractors: list[str],
    explanation: str,
    references: list[str],
    difficulty: str = "intermediate",
) -> dict:
    return {
        "topic": topic,
        "stem": stem,
        "correct": correct,
        "distractors": distractors,
        "explanation": explanation,
        "references": references,
        "difficulty": difficulty,
    }

_spec = importlib.util.spec_from_file_location(
    "cma_sources", ROOT / "classquiz/seed/sources.py"
)
_sources = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sources)
S = _sources
SUPP = ROOT / "classquiz/seed/banks/supplement"
ITEMS_JSON = Path(__file__).with_name("supplement_items.json")

# fmt: off
# Each item: topic, stem, correct, distractors[3], explanation, ref_keys, difficulty
REF = {
    "CDC_HAND": S.CDC_HAND_HYGIENE,
    "CDC_STD": S.CDC_STANDARD_PRECAUTIONS,
    "CDC_ISO": S.CDC_ISOLATION_2007,
    "CDC_INJ": S.CDC_INJECTION_SAFETY,
    "CDC_ONE": S.CDC_ONE_AND_ONLY,
    "CDC_VST": S.CDC_VACCINE_STORAGE,
    "CDC_VAD": S.CDC_VACCINE_ADMIN,
    "OSHA_BBP": S.OSHA_BBP,
    "OSHA_NS": S.OSHA_NEEDLESTICK,
    "AHA_CPR": S.AHA_WHAT_IS_CPR,
    "AHA_BLS": S.AHA_ADULT_BLS,
    "AHA_HQ": S.AHA_HQ_CPR,
    "HHS_PRI": S.HHS_HIPAA_PRIVACY,
    "HHS_SEC": S.HHS_HIPAA_SECURITY,
    "MEDLINE": S.MEDLINEPLUS_HAND_HYGIENE,
    "FDA": S.FDA_MEDICATION_SAFETY,
    "WHO": S.WHO_INJECTION_SAFETY,
    "NHA_CCMA": S.NHA_CCMA,
    "NHA_CET": S.NHA_CET,
    "NHA_CPT": S.NHA_CPT,
    "CLSI": S.CLSI_GP41,
    "RED": S.RED_CROSS_FIRST_AID,
    "CDC_BP": S.CDC_HBP,
}


def _load_items() -> list[dict]:
    raw = json.loads(ITEMS_JSON.read_text(encoding="utf-8"))
    out: list[dict] = []
    for row in raw:
        refs = [REF[k] for k in row["refs"]]
        out.append(
            fact(
                row["topic"],
                row["stem"],
                row["correct"],
                row["distractors"],
                row["explanation"],
                refs,
                row.get("difficulty", "intermediate"),
            )
        )
    return out


def _module_name(topic: str) -> str:
    if topic.startswith("ccma"):
        return "ccma"
    if topic.startswith("skill"):
        return "clinical_skills"
    if topic.startswith("cpr"):
        return "cpr_bls"
    if topic.startswith("ekg"):
        return "ekg"
    if topic.startswith("phleb"):
        return "phlebotomy"
    raise ValueError(topic)


def main() -> None:
    items = _load_items()
    norms = [normalize_stem(i["stem"]) for i in items]
    if len(norms) != len(set(norms)):
        dup = [s for s, c in Counter(norms).items() if c > 1]
        raise SystemExit(f"duplicate stems in ITEMS: {dup[:5]}")

    by_mod: dict[str, list[dict]] = {}
    for item in items:
        by_mod.setdefault(_module_name(item["topic"]), []).append(item)

    for mod, facts in by_mod.items():
        path = SUPP / f"{mod}.py"
        lines = [
            "# SPDX-FileCopyrightText: 2026 CMA Clash contributors",
            "#",
            "# SPDX-License-Identifier: MPL-2.0",
            "",
            "from classquiz.seed.banks._builder import fact",
            "",
            "FACTS: list[dict] = " + repr(facts),
            "",
        ]
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"wrote {path} ({len(facts)} facts)")


if __name__ == "__main__":
    main()
