# Parallel-options rewrite brief (Clinical Skills banks)

Target style for every `skill-*` item in `classquiz/seed/banks/clinical_skills/*.py`.

The worked reference for this bar is `classquiz/seed/banks/clinical_skills/osha_bbp.py`
(it was rewritten to this standard in pass P05). Read it before you start.

## What "good" looks like

Six audited samples, full text:

**1. Temperature (skill-vitals-035)**
```
STEM: Among common outpatient temperature sites, which measurement site most closely reflects core body temperature?
A) Rectal
B) Oral
C) Tympanic membrane
D) Temporal artery
ANSWER: A
EXPL: Rectal readings track core temperature more closely than skin or tympanic sites when obtained correctly. Oral, tympanic, and temporal readings are useful but can lag or vary with technique and environment.
```

**2. EDTA tube (skill-specimen-lab-033)**
```
STEM: Which tube top color is used for EDTA anticoagulant in hematology collections?
A) Lavender (purple) top
B) Light blue (citrate) top
C) Green (heparin) top
D) Gray (fluoride) top
ANSWER: A
EXPL: Lavender or purple tops contain EDTA for CBC and many whole-blood hematology tests. Light blue is citrate for coagulation, green is heparin for plasma chemistry, and gray is fluoride for glucose preservation.
```

**3. Wound irrigation (skill-wound-care-002)**
```
STEM: Which irrigation solution is most often ordered for a contaminated traumatic wound in clinic?
A) Sterile normal saline
B) Hydrogen peroxide
C) Full-strength povidone-iodine
D) Sterile water
ANSWER: A
EXPL: Saline lavage clears debris with low tissue toxicity. Peroxide and full-strength iodine can irritate tissue, and water alone lacks the tonicity many protocols prefer for wound irrigation.
```

**4. Tobacco documentation (skill-intake-016)**
```
STEM: A patient reports smoking one pack per day until quitting in March 2024. Which tobacco history entry is correct?
A) Former smoker; cigarettes; one pack per day; quit date March 2024
B) Former smoker; cigarettes; one pack per day; quit date not recorded
C) Former smoker; cigarettes; amount not recorded; quit date March 2024
D) Former smoker; cigarettes; one pack per week; quit date March 2024
ANSWER: A
EXPL: Status, product, amount, and quit date should all be captured and match what the patient reports. Omitting the quit date or the amount leaves exposure history unclear, and a different amount misstates it.
```

**5. IV venipuncture (skill-specimen-lab-023)**
```
STEM: A peripheral IV is infusing in the patient's right forearm and venous blood is ordered. What is the best venipuncture plan?
A) Draw from the opposite arm or from a site proximal to the catheter
B) Draw from a vein distal to the IV on the same arm
C) Collect the sample through the IV hub without a separate venipuncture
D) Pause the infusion and use any visible hand vein on the same arm
ANSWER: A
EXPL: Blood drawn distal to a running IV is often diluted by infusate. The opposite extremity or a proximal site may be ordered when a distal stick would falsify results.
```

**6. Waived results (skill-poct-041)**
```
STEM: How should waived test results be relayed to the patient in clinic?
A) Relay results privately after the provider reviews and charts them
B) Relay results privately before the provider reviews and charts the value
C) Post results to the patient portal without any provider sign-off
D) Give the printed result to a family member waiting at the front desk
ANSWER: A
EXPL: A waived result is relayed privately once the provider has reviewed and documented it. Relaying before provider review, posting unreviewed results to the portal, and handing a printed result to someone else each break standard workflow and privacy safeguards.
```

## Rules

1. **Parallel options.** All four options answer the same question in the same grammatical
   shape. Each is a plausible clinical statement. Nothing telegraphs "wrong".
2. **No sabotage distractors.** Do not write options a student would never pick:
   no joke options, no absurd options ("grocery lists", "smiley face stickers",
   "patient portraits", "decorative pens"), no filler tails
   ("in routine outpatient care", "for the flavor of the exercise", "and the room was quiet").
3. **No self-refuting padding.** Distractors must not announce their own wrongness:
   no "household bleach", "printer tray", "without asking", "without verifying",
   "without gloves", "skip hand hygiene", "never happens", "nobody".
4. **No hedge on the correct answer.** The key must not contain policy/training
   hedging such as "per training", "per policy", "per protocol", "per manufacturer",
   "per facility", "per label", "when policy requires", "when feasible", "as applicable",
   "when required by", "as directed by the provider". The key states the answer flatly.
   (Hedging on a *distractor* is also a tell, so avoid it everywhere.)
5. **No banned qualifier words in distractors.** Never use "only", "always", "never",
   "skip", "unmeasurable" in a distractor. ("Standard" as the final word of a
   distractor is also banned.)
6. **Length balance.** The correct answer must not be the uniquely longest option, and
   must not be much longer than the shortest option. Aim for all four options within
   roughly 15 characters of each other. If the key needs to be long, lengthen the
   distractors to match with real content, not filler.
7. **Exactly one defensible answer.** For every item, check each distractor: could a
   knowledgeable student argue it is also correct? If so, rewrite it until only one
   option survives. Watch for distractors that are true statements but do not answer
   the question asked.
8. **Plain question stems.** No "presents for care", no fragment stems, no filler
   scenario tails. The stem is a complete question ending in "?" (or "." for a
   statement that is itself the prompt). Avoid stems that end in a bare fragment such
   as "... requires?", "... records?", "... is?" - the repo guard treats those as
   incomplete stems.
9. **Explanations.** At least 80 characters and at least two sentences. Sentence one
   says why the key is right. Sentence two says why the near-misses are wrong, naming
   them. No em dash or en dash anywhere (use a comma or a hyphen).
10. **Preserve structure.** Keep the same number of items (42), the same order, the same
    `topic` string, and the same `difficulty` for each item. Keep the `references` list
    for each item unless the item's topic changed, in which case swap in a reference
    that actually supports the new content.

## Tooling

From the repo root:

```powershell
python scripts/validate_skill_bank_item.py --module <module>      # per-item problems
python scripts/validate_skill_bank_item.py --dump <module>        # full text for review
python scripts/run_seed_quality_checks.py                         # the real repo guards
```

`validate_skill_bank_item.py` must report **0 problems** for your module before you
finish. Review prompts (marked `?`) are advisory: a high-similarity distractor is
expected and correct when the options are parallel one-detail variants, but read each
one and confirm only one option is defensible.

`run_seed_quality_checks.py` runs the real guard tests from
`classquiz/tests/test_seed_hand_authored_quality.py`. Some guards fail for reasons
outside your module (other banks); you are responsible only for making sure your module
contributes zero failures.
