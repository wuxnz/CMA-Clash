# Clinical skills parallel-options rewrite progress

Target: 546 clinical skills items, plus the guard cleanup that the same quality bar
implies for the other certification banks.

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
| P11 | 253 | guard cleanup: cpr, ekg, ccma, phleb banks plus the legacy diabetes bank | done |
| P12 | 251 | content-bar cleanup across all 45 topics | done |
| P13 | 32 | strict-guard fixes: 25 fragment stems, 7 unbalanced option sets | done |

**Completed at parallel-options standard:** all 546 clinical skills items.

**Other banks brought to the same bar:** 1493 items across cpr (313), ekg (253),
ccma (590), and phleb (337).

## P13, the strict-guard fixes

P12 cleared the content bar but left two repo guards failing on the pushed branch:

| Guard | Failure | Items |
|-------|---------|-------|
| `test_hand_authored_stems_are_complete_questions` | stems ending in `include?`, a truncated-question tell | 25 |
| `test_hand_authored_correct_not_uniquely_short_by_wide_margin` | keyed answer far shorter than every distractor | 7 |

The 25 stems were rewritten as complete questions that keep the original question
(`What does active listening include?` becomes `What makes up active listening?`).

The 7 unbalanced items sat in `ccma-anatomy` and `ccma-transmission`. Their keyed
answers were single words (`Liver`, `Ureter`, `Aorta`) sitting beside much longer
distractors, which made the short option the only thin one. Each set was rewritten
so all four options share one length band and the keyed answer is neither the
longest nor the shortest.

## P12, the content-bar cleanup

P11 removed the mechanical tells (giveaway words, over-length options, unbalanced keyed
answers). A content audit then found five residual defect classes that the mechanical
guards did not cover, spread across all 45 topics:

| Defect | Example |
|--------|---------|
| FRAGMENT stem | `Accounts receivable tracks?` |
| TRACING stem | `How should A vaccine with cracked glass be assessed on the tracing?` |
| HEDGE key | `Documented and reported per facility policy` |
| Joke distractor | `Given to the staff as bonuses for the effort` |
| LONGER key | keyed answer 20+ characters longer than every distractor |

`scripts/report_content_bar.py` lists every affected item with all four options, and
`scripts/audit_content_bar.py` reports the counts per topic. The rewrite standard is in
`docs/content-bar-brief.md`.

## What the cleanup changed outside the clinical skills bank

* Every distractor in the whole 2039-item bank was checked for giveaway absolutes and
  for over-length options. 267 giveaway distractors and 155 over-length distractors were
  rewritten.
* Every quiz chunk was rebalanced so the keyed answer is not the long-and-complete
  option. 217 items were rebalanced.
* Topic difficulty mixes were rebalanced to the 30/40/30 split.
* Machine-generated fragment stems (for example `Type 1 diabetes mellitus is best
  described as:`) were rewritten as complete questions.
* Canned template explanations were replaced with two specific sentences per item.

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
| `scripts/report_content_bar.py` | lists the items that still carry a content-bar defect |
| `scripts/audit_content_bar.py` | counts the content-bar defects per topic |
| `scripts/sample_by_cert.py` | prints random items from one certification for review |
| `scripts/report_guard_failures.py` | lists every item that trips the two strict length and stem guards |
| `scripts/check_option_balance.py` | checks candidate option sets against the two length guards |
| `scripts/peek_module.py` | prints the stems of one bank module |
| `scripts/topic_items.py` | prints the stems of one topic with difficulty labels |

Per-item logs: `docs/question-review-log-clinical.md` (sections Parallel-options pass
P01 through P13).
