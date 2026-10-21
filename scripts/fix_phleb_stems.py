#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

"""Rewrite phlebotomy fragment stems into complete questions (stem lines only)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHLEB = ROOT / "classquiz" / "seed" / "banks" / "phleb"

_INCOMPLETE = re.compile(
    r"\b("
    r"should be|must be|includes\?|requires\?|is best prevented by|is called|"
    r"should usually be held|the first priority is|should prompt|should include|"
    r"can cause|may cause|often need|typically feels|is needed when|"
    r"documentation should include|should follow|should occur|because\?|"
    r"increases risk of|may falsely elevate|should be managed by|"
    r"common cause is|should generally be|reduces risk by|supports safety by|"
    r"primarily improves|must cover|should ensure|stress\?|is used to|"
    r"are used for|you should\?|includes\?|must be\?|should\?$"
    r")\s*\?",
    re.I,
)

_QUESTION_START = re.compile(
    r"^(What|Which|When|Where|Why|How|Who|If|Can|Should|Is|Are|Does|Do|During|After|Before|An|A|The)\b",
    re.I,
)

TRANSFORMS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^(.+) is best prevented by\?$", re.I), r"How is \1 best prevented?"),
    (re.compile(r"^(.+) is called\?$", re.I), r"What is \1 called?"),
    (re.compile(r"^(.+) should usually be held\?$", re.I), r"How long should \1 usually be held?"),
    (re.compile(r"^(.+) the first priority is\?$", re.I), r"When \1 occurs, what is the first priority?"),
    (re.compile(r"^If (.+), you should\?$", re.I), r"If \1, what should you do?"),
    (re.compile(r"^(.+) you should\?$", re.I), r"What should you do when \1?"),
    (re.compile(r"^(.+) should prompt\?$", re.I), r"What action should \1 prompt?"),
    (re.compile(r"^(.+) should include\?$", re.I), r"What should \1 include?"),
    (re.compile(r"^(.+) documentation should include\?$", re.I), r"What should \1 documentation include?"),
    (re.compile(r"^(.+) increases risk of\?$", re.I), r"What does \1 increase the risk of?"),
    (re.compile(r"^(.+) typically feels\?$", re.I), r"How does \1 typically feel on palpation?"),
    (re.compile(r"^(.+) often suggest\?$", re.I), r"What do \1 often suggest?"),
    (re.compile(r"^(.+) may falsely elevate\?$", re.I), r"Which laboratory values may \1 falsely elevate?"),
    (re.compile(r"^(.+) may be falsely lowered if tubes are\?$", re.I), r"When may \1 be falsely lowered because of tube handling?"),
    (re.compile(r"^(.+) can contribute to\?$", re.I), r"What can \1 contribute to?"),
    (re.compile(r"^(.+) can cause\?$", re.I), r"What can \1 cause?"),
    (re.compile(r"^(.+) may cause\?$", re.I), r"What may \1 cause?"),
    (re.compile(r"^(.+) is needed when\?$", re.I), r"When is \1 needed?"),
    (re.compile(r"^(.+) is reduced by\?$", re.I), r"How is \1 reduced?"),
    (re.compile(r"^(.+) include\?$", re.I), r"Which findings are included in \1?"),
    (re.compile(r"^(.+) should be managed by\?$", re.I), r"How should \1 be managed?"),
    (re.compile(r"^(.+) should generally be\?$", re.I), r"When should \1 generally be avoided?"),
    (re.compile(r"^(.+) should follow\?$", re.I), r"What policy should \1 follow?"),
    (re.compile(r"^(.+) requires\?$", re.I), r"What does \1 require?"),
    (re.compile(r"^(.+) must be\?$", re.I), r"How must \1 be handled?"),
    (re.compile(r"^(.+) includes\?$", re.I), r"What does \1 include?"),
    (re.compile(r"^(.+) should be\?$", re.I), r"How should \1 be handled?"),
    (re.compile(r"^(.+) should occur\?$", re.I), r"When should \1 occur?"),
    (re.compile(r"^(.+) are used for\?$", re.I), r"What are \1 used for?"),
    (re.compile(r"^(.+) is required because\?$", re.I), r"Why is \1 required?"),
    (re.compile(r"^(.+) often need\?$", re.I), r"What do \1 often need after venipuncture?"),
    (re.compile(r"^(.+) must cover\?$", re.I), r"What must \1 cover?"),
    (re.compile(r"^(.+) primarily improves\?$", re.I), r"How does \1 primarily improve safety?"),
    (re.compile(r"^(.+) is used to\?$", re.I), r"What is \1 used for?"),
    (re.compile(r"^(.+) stress\?$", re.I), r"What do \1 stress?"),
    (re.compile(r"^(.+) reduces risk by\?$", re.I), r"How does \1 reduce risk?"),
    (re.compile(r"^(.+) should ensure\?$", re.I), r"What should \1 ensure?"),
    (re.compile(r"^(.+) supports safety by\?$", re.I), r"How does \1 support safety?"),
    (re.compile(r"^Most facilities limit the number of venipuncture attempts because\?$", re.I),
     "Why do most facilities limit the number of venipuncture attempts?"),
]

SPECIAL = {
    "Expired glucose test strips should be?": "How should expired glucose test strips be handled?",
    "Incidents such as needlesticks should be reported?": "When should needlestick incidents be reported?",
    "A patient refusal of phlebotomy should be?": "How should a patient refusal of phlebotomy be managed?",
    "After suspected arterial nick at the antecubital fossa, pressure should be?": (
        "How should pressure be applied after a suspected arterial nick at the antecubital fossa?"
    ),
    "Persisting numbness or weakness after venipuncture should be?": (
        "How should persisting numbness or weakness after venipuncture be managed?"
    ),
}


def rewrite_stem(stem: str) -> str | None:
    s = stem.strip()
    if s in SPECIAL:
        return SPECIAL[s]
    if _QUESTION_START.match(s) and not _INCOMPLETE.search(s):
        return None
    if not _INCOMPLETE.search(s) and not s.endswith("because?"):
        return None
    for pat, repl in TRANSFORMS:
        if isinstance(repl, str) and pat.pattern.startswith("^Most"):
            if pat.match(s):
                return repl
            continue
        m = pat.match(s)
        if m:
            return pat.sub(repl, s)
    if _INCOMPLETE.search(s):
        return f"What is the correct practice regarding {s[:-1]}?"
    return None


STEM_LINE = re.compile(r'^(\s+)(["\'])([^"\']*\?)(["\']),\s*$')


def process_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    count = 0
    out: list[str] = []
    for line in lines:
        m = STEM_LINE.match(line)
        if m:
            indent, q1, inner, q2 = m.groups()
            new = rewrite_stem(inner)
            if new and new != inner:
                count += 1
                line = f'{indent}{q1}{new}{q2},'
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
    print("stems rewritten:", total)


if __name__ == "__main__":
    main()
