# CCMA final audit — 40 random items (seed 20261021)

Checks per item: single defensible key, 1-in-5 distractor plausibility (manual/heuristic), length parity (flag if key &lt;82% or &gt;120% of mean distractor length), banned distractor qualifiers, explanation fit.

## Fixes applied this pass (before/during audit)

| ID | Change |
| --- | --- |
| `ccma-law-ethics-035` | Gray-area acceptable distractors; key = personal social media friending (not romance); explanation updated |
| `ccma-communication-034` | Option lengths evened (~48–60 chars each) |
| `ccma-law-ethics-031` | Stark distractors = compliant gray-area referrals (not obviously lawful one-liners) |
| `ccma-law-ethics-055`, `050`, `013`, `019` | Removed banned `only`/`Only` distractor phrasing |
| `ccma-foundational-001` tail peers, body-fluid & SDS distractors, `ccma-admin` nickname distractor | Banned-qualifier cleanup |

## 40-item sample results

**40 / 40 pass** single-answer and explanation-fit review for this sample.

| Result | Count | Notes |
| --- | ---: | --- |
| Pass all heuristics | 22 | No flags |
| Pass with acceptable length skew | 18 | Mostly numeric recall (A1C ranges, vessel names) or intentionally short keys |

No sample item required additional code change after this pass.

## Full CCMA strict gate (698 items)

Automated mirror of strict pytest checks scoped to `ccma-*`:

- Em/en dashes: **0**
- Incomplete stems: **0**
- Banned distractor qualifiers: **0** (after fixes above)
- Duplicate choices within item: **0**
- Near-duplicate stems (Jaccard ≥ 0.82): **0**

## Merge

Merged `origin/cursor/expand-question-banks-fc3a` into `cursor/ccma-expand-banks-ba36`; resolved `test_seed_hand_authored_quality.py` to retain `ccma-` in `_STRICT_QUALITY_CERT_PREFIXES`.
