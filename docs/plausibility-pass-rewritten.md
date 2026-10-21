# Plausibility pass (rewritten banks)

One-in-five student rule: distractors are clinically plausible near-misses (wrong step, timing, or placement), not exaggeration or joke options. Correct keys kept in parallel with distractor length where needed.

## CPR aed

Scope: `classquiz/seed/banks/cpr/aed.py` (50 items, AHA BLS AED/defibrillation). Stems and explanations unchanged unless noted; facts verified against AHA pad placement, shock safety, rhythm criteria, pediatric attenuation, and post-shock CPR flow.

| ID | Result | Notes |
|----|--------|-------|
| cpr-aed-001 | fail | Replaced manual-cover-to-cover delay with warm-chest-before-power-on near-miss. |
| cpr-aed-002 | pass | Anterolateral vs stacked sternum, reversed quadrants, posterior-only near-misses. |
| cpr-aed-003 | fail | Replaced hand-holding reassurance with shoulder-contact stabilization distractor. |
| cpr-aed-004 | pass | Post-shock immediate compressions vs prolonged pulse check, pad removal, vents-only. |
| cpr-aed-005 | pass | Arrest criteria vs awake, sleeping responsive, peripheral-injury with pulse. |
| cpr-aed-006 | fail | Swapped room-disable/battery-drain/joke prompts for partial-clear, tingling myth, arm-contact near-misses. |
| cpr-aed-007 | fail | Replaced silence-cabinet-alarms with scheduled pad swap despite valid expiration near-miss. |
| cpr-aed-008 | pass | Power-on on arrival vs wait for ROSC, EMS death declaration, pre-compression power-on. |
| cpr-aed-009 | pass | Dry bare chest vs shave-first delay, alcohol-only wipe, abdominal pad dodge. |
| cpr-aed-010 | fail | Replaced ten-minute compression hold with breaths-only-until-EMS near-miss. |
| cpr-aed-011 | pass | Expose/dry/diagram vs wet clothing, lotion, jewelry-under-pads. |
| cpr-aed-012 | fail | Replaced CPR-training skip with wait-for-EMS-before-pads near-miss. |
| cpr-aed-013 | fail | Replaced five-minute energy-conservation pause with pulse-check-until-case-open near-miss. |
| cpr-aed-014 | pass | VF/pVT vs shock asystole/PEA, sinus with pulse, bradycardia with pulse parallel set. |
| cpr-aed-015 | pass | Yes/No pulse-check framing; femoral minute and single-shock ROSC near-misses balanced. |
| cpr-aed-016 | fail | Replaced five-minute analysis idle with two-minute analysis pause near-miss. |
| cpr-aed-017 | pass | Shave at sites vs cancel AED, household gel, abdominal bypass. |
| cpr-aed-018 | fail | Replaced cut-through-patch with overlay-patch-then-electrode near-miss. |
| cpr-aed-019 | pass | Pediatric pads/mode vs full adult energy always, arbitrary weight withhold, single sternum pad. |
| cpr-aed-020 | fail | Shallow-water shock and dry-whole-floor delay near-misses; head-towel partial dry retained. |
| cpr-aed-021 | fail | Replaced ten-minute unpack pause with stop-to-read-labels near-miss. |
| cpr-aed-022 | pass | ~2 min CPR before re-analyze vs 1 min, 5 min, five-compression re-analyze. |
| cpr-aed-023 | pass | Agonal gasps treated as abnormal vs effective breathing, recovery position, withhold AED. |
| cpr-aed-024 | pass | Clear during analysis vs compress through, femoral pulse during strip, gel wipe shortcut. |
| cpr-aed-025 | pass | Stop/clear/shock sequence vs compress-through-shock, pad removal, ignore advisory. |
| cpr-aed-026 | pass | Remove nitroglycerin patch vs leave for success, under-pad requirement, pediatric-only removal myth. |
| cpr-aed-027 | pass | Leave pads attached vs inspect-after-each, discard-after-one, power-off-until-EMS. |
| cpr-aed-028 | fail | Replaced speak-full-sentence wait with two-minute breathing observation near-miss. |
| cpr-aed-029 | fail | Replaced open-in-another-room with nurses-station prep until cycle ends near-miss. |
| cpr-aed-030 | pass | Pulseless VT definition vs normal rhythm, awake VT with pulse, sinus tach with pulse. |
| cpr-aed-031 | pass | Attenuator reduces energy vs increase dose, disable shock, CPR replacement myth. |
| cpr-aed-032 | pass | Ventilation during AED pauses vs triple-shock-before-vents, never pause, ignore AED for tube. |
| cpr-aed-033 | pass | Expose chest vs thick coats, thin shirt only, pads under buttoned shirt. |
| cpr-aed-034 | pass | Post-shock CPR then re-analyze vs immediate re-analyze, charge-before-compressions, pulse-first prompt. |
| cpr-aed-035 | fail | Shortened post-shock paper documentation pause to two-minute near-miss; analyze-during-compressions retained. |
| cpr-aed-036 | pass | Pad offset from pacemaker vs center on generator, withhold all AED, leg-only pads. |
| cpr-aed-037 | fail | Replaced order-pads-next-week with wait-for-EMS-pediatric-pads near-miss. |
| cpr-aed-038 | pass | AP/split adult pads vs sternum overlap, withhold under eight, arm-only placement. |
| cpr-aed-039 | pass | Continue CPR on dead AED vs stop resuscitation, building search, wait for battery. |
| cpr-aed-040 | fail | Metal-stretcher myocardium myth and prolonged transfer delay near-misses; refuse-with-insulation kept. |
| cpr-aed-041 | pass | ICD pad avoidance vs center on ICD, avoid all implants, abdomen-only pads. |
| cpr-aed-042 | fail | Replaced cartoon wrong combos with partial dry, wet hair, patch-under-pad, damp-clothing near-misses. |
| cpr-aed-043 | pass | Clear during re-analysis vs two-minute carotid check, pad removal between cycles, oral meds. |
| cpr-aed-044 | pass | Semi-automatic shock button vs battery test myth, no analyze myth, pre-pad button myth. |
| cpr-aed-045 | fail | Attenuator withholds energy (not zero-joule joke) vs awake child, skips skin prep myths. |
| cpr-aed-046 | fail | Movement after shock: ten-minute withhold shortened to two-minute observation near-miss. |
| cpr-aed-047 | pass | CPR for non-shockable vs stop CPR, asystole self-resolves, compressions only for shockable myth. |
| cpr-aed-048 | fail | Replaced tallest-rescuer joke with compressor-must-run-AED near-miss. |
| cpr-aed-049 | fail | Replaced permanently-broken and shock-without-pads with reuse-failure and repeated-button-reset near-misses. |
| cpr-aed-050 | pass | Early defibrillation plus CPR vs AED replaces compressions, hospital-only shock, AED after long compressions only. |

**Batch summary:** 50 items reviewed; 20 items adjusted (40 distractor strings). 30 items passed without edits. No stem or explanation factual changes. Correct-option length: pulse-check item keeps deliberate Yes/No parallel structure; remaining keys already full-sentence and comparable to distractors after edits.

## CPR adult/child/infant

**Facts touched:** 36

- What is the recommended compression depth range for most adults
- An unresponsive adult is on a soft mattress during CPR and comp
- During two-rescuer adult CPR, compressions measure about 1.5 
- Real-time feedback shows an adult victim is receiving compressi
- After return of spontaneous circulation (ROSC) in an adult, what
- When should a lay rescuer stop CPR on an adult who was in card
- After ROSC, an adult breathes normally and moves purposefully,
- During 30:2 adult CPR you give a rescue breath and the chest do
- EMS is still en route but an adult arrest victim starts breath
- Why does AHA stress limiting pauses in chest compressions duri
- For which situation does AHA teach lay rescuers that compressi
- Why does AHA recommend including rescue ventilations during ch
- You confirm scene safety at a playground where a child lies m
- What compression depth target is recommended for most child vi
- Pediatric AED pads or a dose-attenuating system is available 
- When should rescuers use adult compression depth and hand-pla
- Which description best defines who should receive child BLS co
- After return of spontaneous circulation, a breathing child has
- During CPR on a thin 9-year-old, feedback shows compressions 
- Two rescuers have provided high-quality child CPR for nearly t
- During prolonged child CPR on a cool playground, the team has 
- You confirm scene safety and find an infant unresponsive in a
- An unresponsive infant has only weak gasping breaths and no ef
- When should rescuers apply an AED during suspected cardiac ar
- Which description best matches high-quality chest compression
- Why does AHA recommend including rescue ventilations during in
- How should a rescuer deliver each rescue breath during infant 
- When opening the airway for infant CPR and significant trauma
- Which compression technique is preferred when two rescuers pe
- When opening an infant's airway for ventilations during CPR, w
- Why might rescuers cover an infant with a dry blanket during p
- Which action best limits harmful pauses during infant CPR when
- How often should rescuers switch the compressor during two-res
- During CPR on an infant with suspected foreign body obstructio
- During two-rescuer infant CPR, the compressor using two-thumb 
- A premature infant in the home develops unresponsiveness and a

## Phleb site and handling

Scope: `classquiz/seed/banks/phleb/site.py` (43 items, topic phleb-site) and `classquiz/seed/banks/phleb/handling.py` (39 items, topic phleb-handling). Stems, keys, and explanations unchanged unless noted.

| ID | Result | Notes |
|----|--------|-------|
| phleb-site-001 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-002 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-003 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-004 | fail | Replaced neck tourniquet with upper-arm overlap pressure near-miss. |
| phleb-site-005 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-006 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-007 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-008 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-009 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-010 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-011 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-012 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-013 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-014 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-015 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-016 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-017 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-018 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-019 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-020 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-021 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-022 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-023 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-024 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-025 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-026 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-027 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-028 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-029 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-030 | fail | Replaced discharge-without-notify with send-home reschedule without supervisor near-miss. |
| phleb-site-031 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-032 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-033 | fail | Replaced center-of-bruise evacuation with bruise-edge vein-course near-miss. |
| phleb-site-034 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-035 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-036 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-037 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-038 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-039 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-040 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-041 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-042 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-site-043 | pass | Parallel CLSI-aligned near-miss distractors; no edit. |
| phleb-handling-001 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-002 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-003 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-004 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-005 | fail | Replaced sunlight-condensation joke with uncooled trunk transport near-miss. |
| phleb-handling-006 | fail | Replaced deliberate UV with routine fluorescent/no-amber bilirubin near-miss. |
| phleb-handling-007 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-008 | fail | Replaced saline dilution with report-with-note skipping recollect near-miss. |
| phleb-handling-009 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-010 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-011 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-012 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-013 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-014 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-015 | fail | Replaced staff scheduling joke with reference-lab chemistry without custody near-miss. |
| phleb-handling-016 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-017 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-018 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-019 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-020 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-021 | fail | Replaced outdoor temperature with device serial without patient/QC linkage near-miss. |
| phleb-handling-022 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-023 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-024 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-025 | fail | Replaced automatic internal cooling with capped tubes in direct sun stability myth. |
| phleb-handling-026 | fail | Replaced permanent room-temperature freezing with 72-hour gray-tube stability near-miss. |
| phleb-handling-027 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-028 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-029 | fail | Replaced air-bubble cartoon with line-clamp-between-tubes near-miss. |
| phleb-handling-030 | fail | Replaced decorative/shift-bonus jokes with barcode-only, TDM-only, stat-omit near-misses. |
| phleb-handling-031 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-032 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-033 | fail | Replaced formalin storage with indefinite room-temperature hold near-miss. |
| phleb-handling-034 | fail | Replaced patient ice preference with dry-ice-for-all-chemistry near-miss. |
| phleb-handling-035 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-036 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-037 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-038 | pass | Parallel preanalytic near-miss distractors; no edit. |
| phleb-handling-039 | pass | Parallel preanalytic near-miss distractors; no edit. |

**Batch summary:** 82 items reviewed (3 site edits, 11 handling edits). 68 items passed without changes. Distractors use near-miss phlebotomy errors (wrong site, timing, transport, or documentation) rather than joke or self-refuting options.
