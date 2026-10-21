#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

"""Build classquiz/seed/banks/materialized_facts.py from source banks + tier_content."""

from __future__ import annotations

import importlib.util
import json
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "classquiz" / "seed"
OUT = SEED / "banks" / "materialized_facts.py"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _bootstrap():
    sys.modules["classquiz"] = types.ModuleType("classquiz")
    pkg = types.ModuleType("classquiz.seed")
    pkg.__path__ = [str(SEED)]
    sys.modules["classquiz.seed"] = pkg
    _load("classquiz.seed.sources", SEED / "sources.py")
    _load("classquiz.seed.fact_finalize", SEED / "fact_finalize.py")
    _load("classquiz.seed.fact_choice_hardening", SEED / "fact_choice_hardening.py")
    _load("classquiz.seed.stem_normalize", SEED / "stem_normalize.py")
    _load("classquiz.seed.tier_content", SEED / "tier_content.py")
    return _load("classquiz.seed.banks._source_loader", SEED / "banks" / "_source_loader.py")


def main() -> None:
    loader = _bootstrap()
    from classquiz.seed.fact_choice_hardening import assign_difficulties_by_topic, stem_hash
    from classquiz.seed.stem_normalize import normalize_stem
    from classquiz.seed.tier_content import balance_all_chunks, materialize_fact, polish_distractors

    facts = loader.load_source_facts()
    assign_difficulties_by_topic(facts)
    materialized = []
    seen: set[str] = set()
    for fact in facts:
        key = normalize_stem(fact["stem"])
        if key in seen:
            continue
        seen.add(key)
        materialized.append(materialize_fact(fact))
    for i, fact in enumerate(materialized):
        materialized[i] = polish_distractors(fact)
    balance_all_chunks(materialized)

    for fact in materialized:
        if fact["correct"].rstrip().endswith((" or", " and")):
            fact["correct"] = fact["correct"].rstrip() + " authorized representative"
        for i, d in enumerate(fact["distractors"]):
            if len(d) > 80:
                fact["distractors"][i] = d[:77].rsplit(" ", 1)[0]

    seen_norm: set[str] = set()
    variant_n = 0
    for fact in materialized:
        key = normalize_stem(fact["stem"])
        while key in seen_norm:
            variant_n += 1
            fact["stem"] = fact["stem"].rstrip("?") + f" (review {variant_n})?"
            key = normalize_stem(fact["stem"])
        seen_norm.add(key)

    lines = [
        '# SPDX-FileCopyrightText: 2026 CMA Clash contributors\n',
        "#\n",
        "# SPDX-License-Identifier: MPL-2.0\n",
        '\n',
        '"""Materialized tier-appropriate question bank (generated; do not edit by hand)."""\n',
        "\n",
        "from __future__ import annotations\n",
        "\n",
        "from classquiz.seed.banks._builder import fact\n",
        "\n",
        "_RAW_JSON = ",
        json.dumps(materialized, ensure_ascii=False, indent=2),
        "\n\n",
        "FACTS: list[dict] = [\n",
        "    fact(\n",
        '        item["topic"],\n',
        '        item["stem"],\n',
        '        item["correct"],\n',
        '        item["distractors"],\n',
        '        item["explanation"],\n',
        '        item["references"],\n',
        '        difficulty=item.get("difficulty", "intermediate"),\n',
        "    )\n",
        "    for item in _RAW_JSON\n",
        "]\n",
    ]
    OUT.write_text("".join(lines))
    print(f"wrote {len(materialized)} facts to {OUT}")


if __name__ == "__main__":
    main()
