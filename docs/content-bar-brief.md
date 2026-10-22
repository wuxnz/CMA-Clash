# Content-bar cleanup brief (all certification banks)

The Clinical Skills category already went through the full parallel-options rewrite.
The other certifications got a mechanical hygiene pass (giveaway words removed, option
lengths trimmed, keyed answers rebalanced) but still carry machine-generated artifacts.
This pass removes them.

## The five defects

Run `python scripts/report_content_bar.py --prefix <topic-prefix>` to list the items in
your topics that still need work. Each item is printed with every option so you can
rewrite it in place.

### 1. FRAGMENT stems

A stem that is a truncated question, not a question.

```
"Accounts receivable tracks?"                      -> "What does accounts receivable track?"
"Copayment collection at check-in should?"         -> "How should a copayment be collected at check-in?"
"ICD-10-CM codes primarily describe?"             -> "What do ICD-10-CM codes primarily describe?"
"Day sheet reports often summarize?"               -> "What do day sheet reports often summarize?"
```

Rewrite it as a complete question that asks exactly what the old fragment asked.
The stem must end in "?" and must read the way a clinician would ask it.

### 2. TRACING stems

The machine template "How should X be assessed on the tracing?" is meaningless to a
student because there is no tracing involved.

```
"How should A vaccine with cracked glass be assessed on the tracing?"
    -> "What should the medical assistant do with a vaccine that has cracked glass?"
```

### 3. HEDGED keys

A keyed answer that hedges instead of answering. The hedge tells the student that this
option is the cautious one rather than the correct one.

```
"Follow policy and provide a receipt when required"   -> "Collect the copayment and give the patient a receipt"
"Documented and reported per facility policy"         -> "Document the incident and report it"
"Private rooms are unavailable per policy"            -> "The facility has no private room available"
"Is generally acceptable at different sites"          -> "Is acceptable when given at different injection sites"
"Are permitted without patient authorization often"   -> "Are permitted without patient authorization"
"Clipped if needed; shave only if ordered"            -> "Clip the hair, and shave it only if the provider orders it"
```

Remove the hedge and state the answer flatly. Keep the clinical or regulatory meaning.

### 4. Joke distractors

A distractor that no student would choose, which gives the answer away.

```
"Be quietly waived for friends and family of staff"
"Posted on public boards in the clinic waiting room"
"Share the details on public forums"
"Given to the staff as bonuses for the effort"
"Poured straight down the clinic sink drain"
"CC unrelated vendors"
"Replaced by unverified online blogs"
```

Replace each one with a **parallel, plausible near-miss**: the same kind of statement as
the keyed answer, differing in one real clinical, legal, or regulatory detail. A student
should be able to believe it and be wrong.

### 5. Length and shape

* The keyed answer must not be much longer than every distractor (aim for all four
  options within roughly 15 characters of each other).
* A distractor that repeats the keyed answer's content words almost exactly is a second
  defensible answer. Make it differ in one concrete detail instead.

## Hard rules

- Do not change the item count, the order, the `topic` string, the `difficulty` value,
  or the `references` list.
- Do not change what the keyed answer means clinically, legally, or administratively.
  You may reword it to remove a hedge.
- Do not change the clinical content of a distractor. You may replace a joke distractor
  with a real one.
- Keep all four options in the same grammatical shape.
- Keep the stem a complete question ending in "?".
- Keep the explanation at two or more sentences and 80 characters or more. If the
  explanation quotes an option you rewrote, update the quote.
- No em dash or en dash anywhere.
- Keep every clinical, legal, and regulatory fact accurate. Check the reference in
  `classquiz/seed/sources.py` if you need the authority for a statement.
- Do not touch any file outside the ones assigned to you.

## Verification

All four must be clean for your topics before you finish:

```powershell
python scripts/report_content_bar.py --prefix <topic-prefix>   # no items listed
python scripts/audit_item_quality.py --prefix <topic-prefix> --only-failing
python scripts/audit_chunk_longest.py <topic-prefix>
python scripts/run_seed_quality_checks.py                    # 52/52 checks passed
```

`python scripts/run_seed_quality_checks.py` needs no database. It runs the real guard
tests from `classquiz/tests/` against the offline seed banks.

Commit your work when done with a message that starts "fix(seed):".
