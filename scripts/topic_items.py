"""List the items of a topic with their difficulty and a short stem."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_item_quality import bootstrap  # noqa: E402


def main() -> None:
    topic = sys.argv[1]
    want = sys.argv[2] if len(sys.argv) > 2 else ""
    banks = bootstrap()
    rows = [f for f in banks.load_all_facts() if f["topic"] == topic]
    print(f"n = {len(rows)}")
    for i, f in enumerate(rows, 1):
        if want and f["difficulty"] != want:
            continue
        print(f"{i:03d} {f['difficulty'][:4]} {f['stem'][:88]}")


if __name__ == "__main__":
    main()
