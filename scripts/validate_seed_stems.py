#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0
"""Validate seed banks for duplicate stems."""

from __future__ import annotations

import sys
from collections import Counter

from classquiz.seed.banks import load_all_facts
from classquiz.seed.stem_normalize import normalize_stem


def main() -> int:
    facts = load_all_facts()
    norms = [normalize_stem(f["stem"]) for f in facts]
    counts = Counter(norms)
    dups = {k: v for k, v in counts.items() if v > 1}
    if dups:
        worst = sorted(dups.items(), key=lambda x: -x[1])[:20]
        print("DUPLICATE STEMS:", len(dups), "groups", file=sys.stderr)
        for stem, n in worst:
            print(f"  [{n}] {stem[:100]}", file=sys.stderr)
        return 1
    print(f"OK: {len(facts)} facts, {len(counts)} unique stems")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
