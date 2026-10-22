# Clinical skills parallel-options rewrite progress

Target: 546 clinical skills items, plus the same quality bar applied to the other
certification banks.

Every item now has four parallel options of comparable length, no giveaway absolutes
("only", "any", "never", "always", "random") in a distractor, no hedge on the keyed
answer, and exactly one defensible answer.

| Batch | Items | Scope | Status |
|-------|-------|-------|--------|
| P01 | 84 | injection 001–042, vitals 001–042 | done |
| P01b | 6 | audit samples (specimen 023/033, vitals 035, wound 002, intake 016, poct 041) | done |
| P02 | 75 | infection 001–042, terminology 001–033 | done |
| P03 | 42 | terminology 034–042, pharm_dosage 001–033 | done |
| P03b | 42 | specimen_lab 001–042 | done |
| P04 | 51 | pharm_dosage 034–042, intake 001–042 | done |
| P05 | 42 | osha_bbp 001–042 | done |
| P06 | 42 | med_safety 001–042 | done |
| P07 | 42 | wound_care 001–042 | done |
| P08 | 42 | life_stages 001–042 | done |
| P09 | 42 | emergency_aid 001–042 | done |
| P10 | 42 | poct 001–042 | done |
| P11 | 253 | guard cleanup across the cpr, ekg, ccma, and phleb banks | done |

**Completed at parallel-options standard:** all 546 clinical skills items.

**Guard status:** all 52 checks in the seed quality suite pass, and the per-item
audit reports zero findings across the whole 2172-question bank.

## Branch structure note

The CCMA consolidation on master folded the old `classquiz/seed/banks/diabetes.py` and
`classquiz/seed/banks/supplement/diabetes_expansion.py` into
`classquiz/seed/banks/ccma/diabetes.py`. The merge keeps that structure, so the
ccma-diabetes topic is one file with 130 items.

## What the cleanup changed outside the clinical skills bank

* Every distractor in the bank was checked for giveaway absolutes, over-length options, and
  for a keyed answer that reads as the only complete option.
* Every quiz chunk was rebalanced so the keyed answer is not the long-and-complete option.
* Topic difficulty mixes were rebalanced to the 30/40/30 split.
* Machine-generated fragment stems (for example `Type 1 diabetes mellitus is best
  described as:`) were rewritten as complete questions.
* Canned template explanations were replaced with two specific sentences per item.
* The repeated auto-balance padding tails that the generator had bolted onto options
  ("under typical outpatient policy.", "per facility policy.", "in a typical outpatient
  clinic setting.", "for routine ambulatory patient care.") were removed.

## Publishing

`python -m classquiz.seed.runner` re-seeds the database from the banks in the code. The
production API runs it on every boot (`AUTO_SEED_CONTENT=true`) and re-indexes
Meilisearch when the index and the database disagree, so a deploy is what publishes
question changes.

## Tooling

`docs/parallel-options-brief.md` is the content standard. `docs/choice-quality-brief.md`
is the option-hygiene standard.

| Script | Purpose |
|--------|---------|
| `scripts/validate_skill_bank_item.py` | per-item check of one clinical skills module |
| `scripts/run_seed_quality_checks.py` | runs the real repo guard tests without the app stack |
| `scripts/audit_item_quality.py` | per-item giveaway, length, and key-balance report |
| `scripts/audit_item_quality_breakdown.py` | the same report grouped by problem type |
| `scripts/audit_choice_quality.py` | giveaway, length, explanation, difficulty, chunk reports |
| `scripts/audit_chunk_longest.py` | the per-chunk keyed-answer ratio the repo test enforces |
| `scripts/apply_choice_rewrites.py` | applies a batch of option rewrites to the source files |
| `scripts/rebalance_difficulty.py` | rebalances the beginner/intermediate/advanced mix |
| `scripts/generate_review_log.py` | generates per-item review-log lines from a git diff |
| `scripts/audit_guard_failures.py` | lists the items that trip each repo guard |
| `scripts/peek_module.py`, `scripts/topic_items.py` | print the stems of a module or topic |

Per-item logs: `docs/question-review-log-clinical.md` (sections Parallel-options pass
P01 through P11), plus `docs/question-review-log-ccma-rewrite.md`,
`docs/question-review-log-cpr.md`, and `docs/question-review-log-ekg.md`.
