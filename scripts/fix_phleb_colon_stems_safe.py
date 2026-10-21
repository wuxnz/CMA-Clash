#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

"""Convert colon-ending phleb stems using explicit suffix rules only (no generic fallback)."""

from __future__ import annotations

import re
from pathlib import Path

PHLEB = Path(__file__).resolve().parents[1] / "classquiz" / "seed" / "banks" / "phleb"
STEM_LINE = re.compile(r'^(\s+)(["\'])([^"\']*)(["\']),\s*$')
STARTS = re.compile(r"^(What|Which|When|Where|Why|How|Who|If|Can|Should|Is|Are|Does|Do|During|After|Before|An|A|The)\b", re.I)

SUFFIX_RULES: list[tuple[str, str]] = [
    (" typically include:", " are required?"),
    (" should be mixed by:", " should be mixed?"),
    (" often require:", " often require?"),
    (" should follow:", " should follow?"),
    (" should maintain:", " should maintain?"),
    (" may require:", " may require?"),
    (" may falsely elevate:", " may falsely elevate?"),
    (" the usual response is:", " is the usual response?"),
    (" require documentation of:", " require what documentation?"),
    (" must be:", " must be handled?"),
    (" can:", " can cause what problems?"),
    (" need:", " need what handling?"),
    (" is required for:", " is required for what purpose?"),
    (" should use:", " should use what method?"),
    (" should ensure:", " should ensure what?"),
    (" should record:", " should record what?"),
    (" helps:", " helps how?"),
    (" applies:", " applies when?"),
    (" may cause:", " may cause what?"),
    (" most threaten:", " most threaten what results?"),
    (" matters because:", " matters for what reason?"),
    (" requires:", " requires what?"),
    (" should be chosen based on:", " should be chosen based on what?"),
    (" should generally be limited to:", " should generally be limited to what duration?"),
    (" is usually:", " is usually what?"),
    (" is done by:", " is done how?"),
    (" are especially useful when:", " are especially useful when?"),
    (" should be avoided on an arm that has:", " should be avoided on an arm that has what conditions?"),
    (" should usually be:", " should usually be avoided when?"),
    (" should not be performed through unhealed burns or extensive scar tissue because:", " should not be performed through unhealed burns or extensive scar tissue for what reason?"),
    (" should include:", " should include what steps?"),
    (" should occur:", " should occur when?"),
    (" are appropriate when:", " are appropriate when?"),
    (" is generally:", " is generally handled how?"),
    (" may:", " may help how?"),
    (" should:", " should be done how?"),
    (" is used for:", " is used for what?"),
    (" require that after two unsuccessful venipunctures:", " require what after two unsuccessful venipunctures?"),
    (" balances:", " balances what factors?"),
    (" is to:", " should the collector do first?"),
    (" is:", " is what?"),
    (" contain:", " contain what additive?"),
    (" prevents clotting primarily by:", " prevents clotting primarily by what mechanism?"),
    (" is especially suited to hematology because it:", " is especially suited to hematology for what reason?"),
    (" anticoagulates blood in green-top tubes by:", " anticoagulates blood in green-top tubes by what mechanism?"),
    (" stabilizes glucose mainly by:", " stabilizes glucose mainly by what mechanism?"),
    (" contributes to anticoagulation by:", " contributes to anticoagulation by what mechanism?"),
    (" functions after centrifugation to:", " functions after centrifugation to do what?"),
    (" are pre-coated with:", " are pre-coated with what?"),
    (" may show:", " may show what artifact?"),
    (" can falsely:", " can falsely affect what results?"),
    (" primarily differs in:", " primarily differs in what way?"),
    (" promote:", " promote what process?"),
    (" may use:", " may use what anticoagulant?"),
    (" achieve clotting by:", " achieve clotting by what mechanism?"),
    (" illustrates:", " illustrates what principle?"),
    (" are usually drawn:", " are usually drawn when in the sequence?"),
    (" are typically drawn:", " are typically drawn when in the sequence?"),
    (" mainly apply to:", " mainly apply to what situations?"),
    (" may primarily risk:", " may primarily risk what error?"),
    (" expects:", " expects what technique?"),
    (" is the best immediate action:", " is the best immediate action when unsure?"),
    (" is problematic because it:", " is problematic for what reason?"),
    (" are generally filled:", " should generally be filled when?"),
    (" must be used with:", " must be used with what precautions?"),
    (" should interpret PT/INR from that citrate tube as:", " should interpret PT/INR from that citrate tube as what?"),
    (" should be guided by:", " should be guided by what policy?"),
    (" should include:", " should include what documentation?"),
]


def fix(stem: str) -> str | None:
    if not stem.endswith(":"):
        return None
    if STARTS.match(stem[:-1] + "?"):
        return stem[:-1] + "?"
    for suffix, repl in SUFFIX_RULES:
        if stem.endswith(suffix):
            base = stem[: -len(suffix)]
            qword = "What"
            if suffix in (
                " should be mixed by:",
                " is done by:",
                " should be chosen based on:",
            ):
                qword = "How"
            if suffix in (" matters because:", " should not be performed through unhealed burns or extensive scar tissue because:", " is problematic because it:"):
                qword = "Why"
            if suffix in (" should occur:", " are usually drawn:", " are typically drawn:", " applies:"):
                qword = "When"
            return f"{qword} {base[0].lower()}{base[1:]}{repl}"
    return None


def process(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    n = 0
    out = []
    for line in lines:
        m = STEM_LINE.match(line)
        if m:
            indent, q1, inner, q2 = m.groups()
            new = fix(inner)
            if new and new != inner:
                n += 1
                line = f"{indent}{q1}{new}{q2},"
        out.append(line)
    if n:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return n


def main() -> None:
    total = 0
    for path in sorted(PHLEB.glob("*.py")):
        if path.name == "__init__.py":
            continue
        c = process(path)
        if c:
            print(path.name, c)
            total += c
    print("total", total)


if __name__ == "__main__":
    main()
