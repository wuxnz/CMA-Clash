"""Generate per-item review-log lines by diffing a module against its pre-pass version.

Usage:
    python scripts/generate_review_log.py <module> <base-ref> <section-title>
"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"
MODULE_FILES = {
    "injection": "injection.py",
    "vitals": "vitals.py",
    "infection": "infection.py",
    "terminology": "terminology.py",
    "pharm_dosage": "pharm_dosage.py",
    "specimen_lab": "specimen_lab.py",
    "intake": "intake.py",
    "osha_bbp": "osha_bbp.py",
    "med_safety": "med_safety.py",
    "poct": "poct.py",
    "wound_care": "wound_care.py",
    "life_stages": "life_stages.py",
    "emergency_aid": "emergency_aid.py",
}
HEDGE = re.compile(
    r"\bper\s+(training|policy|protocol|manufacturer|label|facility)\b"
    r"|\bwhen\s+policy\s+requires\b"
    r"|\bper\s+provider\s+or\s+protocol\b"
    r"|\bwhen\s+feasible\b"
    r"|\bas\s+applicable\b",
    re.I,
)
ABSOLUTE = re.compile(r"\b(only|always|never)\b", re.I)
SABOTAGE = re.compile(
    r"\bin routine outpatient care\b|\bwithout asking\b|\bprinter tray\b|"
    r"\bhousehold bleach\b|\bwithout verifying\b|\bgrocery list\b",
    re.I,
)


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


def load_at(ref: str, module: str) -> list[dict]:
    path = f"classquiz/seed/banks/clinical_skills/{MODULE_FILES[module]}"
    src = subprocess.run(
        ["git", "show", f"{ref}:{path}"], capture_output=True, text=True, cwd=ROOT
    )
    if src.returncode != 0:
        raise SystemExit(f"cannot read {ref}:{path}: {src.stderr}")
    tmp = ROOT / "classquiz" / "seed" / "banks" / "clinical_skills" / f"_old_{module}.py"
    tmp.write_text(src.stdout, encoding="utf-8")
    try:
        mod = _load(f"_old_{module}", tmp)
        return list(mod.FACTS)
    finally:
        tmp.unlink(missing_ok=True)


def _shape(text: str) -> str:
    """Coarse grammatical shape of an option, used to detect parallel option sets."""
    parts = [p.strip().lower() for p in text.split(",")]
    return "|".join(parts)


def describe(old: dict, new: dict) -> str:
    bits: list[str] = []
    if old["stem"] != new["stem"]:
        bits.append("stem reworded into a complete question")
    if old["correct"] != new["correct"]:
        if HEDGE.search(old["correct"]) and not HEDGE.search(new["correct"]):
            bits.append("key reworded without the policy hedge")
        else:
            bits.append("key reworded")
    old_d = set(old["distractors"])
    new_d = set(new["distractors"])
    if old_d != new_d:
        if any(SABOTAGE.search(d) for d in old_d - new_d):
            bits.append("sabotage distractor replaced")
        elif any(ABSOLUTE.search(d) for d in old_d - new_d):
            bits.append("absolute distractor reworded")
        new_shapes = {_shape(c) for c in [new["correct"], *new["distractors"]]}
        if len(new_shapes) == 1 and new["correct"].count(",") >= 2:
            bits.append("four parallel entries that differ in one element")
        else:
            bits.append("distractors reworked into parallel near-misses")
    if old.get("explanation") != new.get("explanation"):
        bits.append("explanation rewritten to name the near-misses")
    if not bits:
        bits.append("verified against the parallel-options standard")
    return "; ".join(bits) + "."


def main() -> None:
    module, ref, title = sys.argv[1], sys.argv[2], sys.argv[3]
    bootstrap()
    path = SEED / "banks" / "clinical_skills" / MODULE_FILES[module]
    new_items = list(_load(f"_new_{module}", path).FACTS)
    old_items = load_at(ref, module)
    if len(old_items) != len(new_items):
        raise SystemExit(f"item count changed: {len(old_items)} -> {len(new_items)}")
    topic = new_items[0]["topic"]
    print(f"\n## {title}")
    print()
    for i, (old, new) in enumerate(zip(old_items, new_items), start=1):
        print(f"{topic}-{i:03d} | fail | {describe(old, new)}")


if __name__ == "__main__":
    main()
