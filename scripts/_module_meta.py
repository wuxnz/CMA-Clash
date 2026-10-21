"""Print item metadata (difficulty + references) for a clinical skills module."""

from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

SEED = Path("classquiz/seed")
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
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")


def main() -> None:
    module = sys.argv[1]
    bootstrap()
    mod = _load("_meta_" + module, SEED / "banks" / "clinical_skills" / MODULE_FILES[module])
    for i, f in enumerate(mod.FACTS, 1):
        short = [r.split(" - ")[0].split(":")[0].strip() for r in f["references"]]
        print(f"{i:03d} | {f['difficulty']:<12} | {','.join(short)}")


if __name__ == "__main__":
    main()
