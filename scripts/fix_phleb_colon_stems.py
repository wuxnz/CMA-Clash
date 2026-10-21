#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

"""Convert phlebotomy colon-style stems into complete questions ending with ?."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHLEB = ROOT / "classquiz" / "seed" / "banks" / "phleb"

RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^(.+) typically include:$"), r"What \1 are required?"),
    (re.compile(r"^(.+) should be mixed by:$"), r"How should \1 be mixed?"),
    (re.compile(r"^(.+) often require:$"), r"What do \1 often require?"),
    (re.compile(r"^(.+) should follow:$"), r"What should \1 follow?"),
    (re.compile(r"^(.+) should maintain:$"), r"What should \1 maintain?"),
    (re.compile(r"^(.+) may require:$"), r"What may \1 require?"),
    (re.compile(r"^(.+) may falsely elevate:$"), r"Which laboratory values may \1 falsely elevate?"),
    (re.compile(r"^(.+) the usual response is:$"), r"What is the usual response when \1?"),
    (re.compile(r"^(.+) require documentation of:$"), r"What documentation is required for \1?"),
    (re.compile(r"^(.+) must be:$"), r"How must \1 be handled?"),
    (re.compile(r"^(.+) can:$"), r"What can \1 cause?"),
    (re.compile(r"^(.+) need:$"), r"What do \1 need?"),
    (re.compile(r"^(.+) is required for:$"), r"What is required for \1?"),
    (re.compile(r"^(.+) should use:$"), r"What should \1 use?"),
    (re.compile(r"^(.+) should ensure:$"), r"What should \1 ensure?"),
    (re.compile(r"^(.+) should record:$"), r"What should \1 record?"),
    (re.compile(r"^(.+) should:$"), r"What should staff do when \1?"),
    (re.compile(r"^(.+) helps:$"), r"How does \1 help?"),
    (re.compile(r"^(.+) applies:$"), r"When does \1 apply?"),
    (re.compile(r"^(.+) may cause:$"), r"What may \1 cause?"),
    (re.compile(r"^(.+) most threaten:$"), r"What do \1 most threaten?"),
    (re.compile(r"^(.+) helps:$"), r"How does \1 help collection quality?"),
    (re.compile(r"^(.+) matters because:$"), r"Why does \1 matter?"),
    (re.compile(r"^(.+) should:$"), r"What should be done regarding \1?"),
    (re.compile(r"^(.+) requires:$"), r"What does \1 require?"),
    (re.compile(r"^(.+) should be chosen based on:$"), r"How should \1 be chosen?"),
    (re.compile(r"^(.+) before handling filled collection tubes:$"), r"What is required \1 before handling filled collection tubes?"),
    (re.compile(r"^(.+) before CBC analysis:$"), r"What happens when \1 before CBC analysis?"),
    (re.compile(r"^(.+) for courier pickup:$"), r"What is the risk when \1 for courier pickup?"),
    (re.compile(r"^(.+) before leaving the patient helps:$"), r"Why does \1 before leaving the patient help?"),
    (re.compile(r"^(.+) for ammonia-like assays:$"), r"What happens when \1 for ammonia-like assays?"),
    (re.compile(r"^(.+) includes:$"), r"What does \1 include?"),
    (re.compile(r"^(.+) strategy for specimen collectors includes:$"), r"What does \1 include?"),
    (re.compile(r"^(.+) bundle for WHO-aligned blood collection includes:$"), r"What does \1 include?"),
    (re.compile(r"^(.+) for WHO injection safety in phlebotomy includes:$"), r"What does \1 include?"),
]

STEM_LINE = re.compile(r'^(\s+)(["\'])([^"\']*)(["\']),\s*$')


def rewrite(stem: str) -> str | None:
    if not stem.endswith(":"):
        return None
    for pat, repl in RULES:
        m = pat.match(stem)
        if m:
            return pat.sub(repl, stem)
    body = stem[:-1]
    return f"What is the correct practice for {body.lower()}?"


def process_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    count = 0
    out: list[str] = []
    for line in lines:
        m = STEM_LINE.match(line)
        if m:
            indent, q1, inner, q2 = m.groups()
            if inner.endswith(":"):
                new = rewrite(inner)
                if new and new != inner:
                    count += 1
                    line = f"{indent}{q1}{new}{q2},"
        out.append(line)
    if count:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return count


def main() -> None:
    total = 0
    for path in sorted(PHLEB.glob("*.py")):
        if path.name == "__init__.py":
            continue
        n = process_file(path)
        if n:
            print(path.name, n)
            total += n
    print("colon stems fixed:", total)


if __name__ == "__main__":
    main()
