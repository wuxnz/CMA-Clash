# Choice-quality hygiene brief (all seed banks)

This is a mechanical cleanup pass over already-rewritten banks. It does **not**
change what a question asks or what the keyed answer means. It only makes the
keyed answer stop standing out and keeps every option the same size.

## The four gates

The repo enforces these in `classquiz/tests/test_seed_choice_quality.py` and
`classquiz/tests/test_seed_explanation_quality.py`:

1. **No giveaway absolutes in a distractor.**
   `always`, `never`, `any`, `random`, `only` are giveaway words. A distractor
   that uses one of them, when the keyed answer does not, tells the student that
   the option is wrong. Rewrite the distractor as a specific, plausible statement.
   Examples:
   - "Only after ROSC has occurred" -> "After ROSC has been confirmed by EMS"
   - "Never switch to avoid breaking rhythm" -> "Rotate roles on the same fixed cycle"
   - "Any test ordered can be collected capillary" -> "Tests that are validated for capillary collection"
   - "Random fine fibrillatory waves" -> "Fine, disorganized fibrillatory waves"
2. **Distractors stay at or under 80 characters.**
   A long distactor reads as "the complete answer" just as a long key does.
   Shorten it without losing the clinical meaning or the parallel shape.
3. **The keyed answer must not out-length every distractor by 22 or more characters.**
   `is_correct_strictly_longest` in `classquiz/seed/fact_choice_hardening.py`
   is the reference. Shorten the key or extend the shortest distractor. Do not
   change what the key says.
4. **For `skill-` topics the keyed answer must never be the uniquely longest option.**
   This one is absolute, not a per-chunk ratio.

## How to verify

```powershell
python scripts/audit_item_quality.py <topic-prefix> --only-failing
python scripts/audit_chunk_longest.py <topic-prefix>
python scripts/audit_choice_quality.py giveaway
python scripts/audit_choice_quality.py length
python scripts/run_seed_quality_checks.py
```

`audit_item_quality.py` reports per item. `audit_chunk_longest.py` reports the
per-chunk ratio the repo test enforces: the runner groups items by (topic,
difficulty), sorts them by stem, and slices them into 28-question chunks, and at
most 30 percent of a chunk (42 percent for chunks under 20 items) may have an
over-long key.

## Hard rules

- Do not change the item count, the order, the `topic` string, the `difficulty`
  value, or the `references` list.
- Do not change what any keyed answer means. You may reword it to be shorter.
- Do not change the clinical content of a distractor. You may reword it or trim a
  trailing clause.
- Keep all four options in the same grammatical shape. A distractor that is
  visibly different in shape from the key is its own giveaway.
- Keep the stem as it is unless it ends in a fragment, in which case rewrite it
  as a complete question ending in "?" or ".".
- No em dash or en dash anywhere.
- Keep explanations at two or more sentences and 80 characters or more.
- Do not touch any file outside the ones assigned to you.
