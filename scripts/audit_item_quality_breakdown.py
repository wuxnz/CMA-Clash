"""Break the item-quality problems down by type and topic."""

from __future__ import annotations

import importlib.util
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_item_quality import GIVEAWAY, KEY_MARGIN, MAX_DISTRACTOR_LEN, bootstrap, item_problems  # noqa: E402


def main() -> None:
    banks = bootstrap()
    facts = banks.load_all_facts()
    by_type = Counter()
    by_cert_type = defaultdict(Counter)
    for fact in facts:
        correct = fact["correct"]
        distractors = list(fact["distractors"])
        for d in distractors:
            if GIVEAWAY.search(d) and not GIVEAWAY.search(correct):
                by_type["giveaway"] += 1
                by_cert_type[fact["topic"].split("-")[0]]["giveaway"] += 1
            if len(d.strip()) > MAX_DISTRACTOR_LEN:
                by_type["long"] += 1
                by_cert_type[fact["topic"].split("-")[0]]["long"] += 1
        lengths = [len(c.strip()) for c in [correct, *distractors]]
        if lengths[0] > max(lengths[1:]) and lengths[0] - min(lengths[1:]) >= KEY_MARGIN:
            by_type["key_margin"] += 1
            by_cert_type[fact["topic"].split("-")[0]]["key_margin"] += 1
        if lengths[0] == max(lengths) and sum(1 for n in lengths if n == max(lengths)) == 1:
            by_type["key_unique_longest"] += 1
            by_cert_type[fact["topic"].split("-")[0]]["key_unique_longest"] += 1
    print("by type:", dict(by_type))
    print()
    for cert in sorted(by_cert_type):
        print(f"  {cert}: {dict(by_cert_type[cert])}")

    # For skill topics the uniquely-longest rule is absolute; elsewhere it is a chunk ratio.
    print()
    print("skill items with a uniquely longest key:")
    for fact in facts:
        if not fact["topic"].startswith("skill-"):
            continue
        lengths = [len(c.strip()) for c in [fact["correct"], *fact["distractors"]]]
        if lengths[0] == max(lengths) and sum(1 for n in lengths if n == max(lengths)) == 1:
            print(f"  {fact['topic']} | {fact['stem'][:60]} | {lengths}")


if __name__ == "__main__":
    main()
