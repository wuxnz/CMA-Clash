# CCMA single-answer audit (2026-10-21e)

Full-bank review for distractors that a CCMA exam key would also mark correct, plus length-balance fixes on flagged tail items.

## Method

1. Automated scan of all **698** `ccma-*` items for:
   - `example of … violation` stems with multiple violation-shaped options
   - `broadly prohibited` / Stark stems where all four options described the same prohibition
   - `what does [principle] mean/require/emphasize` stems with injustice examples or another principle’s definition as distractors
   - `raises concerns about what ethical issue` stems where distractors named valid ethical issues
   - `first action` wound-care item with multiple complete technique chains
2. Manual re-read of the **111** IDs in `docs/ccma-run-rewritten-ids-2026-10-21d.txt`, with code fixes on law/ethics tail, clinical-care-001, communication-034, foundational-001, and diabetes-025.

## Multiple-correct (or equivalent) items found and fixed: **13**

| ID | Issue | Fix |
| --- | --- | --- |
| ccma-clinical-care-001 | Options C/D both described acceptable wound care; D hedged on policy | Key = **hand hygiene first**; distractors are wrong order/sequence only |
| ccma-law-ethics-035 | A–C were all boundary violations | Distractors = appropriate professional conduct; explanation names romance vs professional options |
| ccma-law-ethics-031 | All four options described Stark violations | Stem → scenario; one Stark violation vs lawful referrals/rent/wages |
| ccma-law-ethics-056 | Distractors named other valid ethical issues | Distractors = mislabeled beneficence/nonmaleficence/justice |
| ccma-law-ethics-001 | Beneficence stem with other principles’ duties | Distractors = definitions of nonmaleficence, autonomy, justice |
| ccma-law-ethics-002 | Fidelity stem with breach examples | Distractors = other principle definitions |
| ccma-law-ethics-003 | Nonmaleficence stem with harmful acts | Distractors = other principle definitions |
| ccma-law-ethics-023 | Justice stem; distractor read as equitable allocation | Distractors = other principle definitions |
| ccma-law-ethics-051 | Fidelity definition with breach-style distractors | Distractors = other principle definitions |
| ccma-law-ethics-053 | Justice stem with injustice examples | Distractors = other principle definitions |
| ccma-foundational-001 | Distractors overlapped MA data-gathering; key shortest | Scope overreach distractors; lengthened parallel key |
| ccma-communication-034 | Key shortest plain pair | Parallel-length four options |
| ccma-diabetes-025 | “Mild hunger” failed 1-in-5 escalation peer | Replaced with alert hypoglycemia treated with crackers |

**Additional alignment (not counted as multi-correct):** explanation and length updates on `ccma-law-ethics-047`, `050`, `055`.

## Result

Post-fix automated boundary-violation scan: **one** keyed violation on `ccma-law-ethics-035`. No remaining `broadly prohibited` Stark quadruple-violation pattern.
