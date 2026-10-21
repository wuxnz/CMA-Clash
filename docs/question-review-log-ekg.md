# EKG question review log

One line per item after self-review.

## Checklist

1. Stem is a grammatical complete question (not a fragment plus `?`).
2. Every distractor tempts a student who half-knows the material; no common-sense eliminable option.
3. Banned distractor wording: `only`, `always`, `never`, `skip`, `avoid any`, `unmeasurable`, trailing `standard`.
4. Four distinct options, parallel form, similar length.
5. Exactly one correct answer per current AHA/NHA EKG sources.
6. Advanced = scenario or multi-step reasoning, not bare recall.
7. Explanation is specific to this item (names the tempting wrong choice when useful).
8. Correct answer does not restate the stem.
9. No stem clue makes a distractor equally defensible.

Format: `id | pass | notes`

**Batches 01–06 sweep:** Removed giveaway parentheticals on distractors; balanced option lengths where the keyed answer was longest; strengthened swapped-arm near-miss distractors (leads-023).

**Length / position (all 253 EKG, hand-fixed):** Removed auto `normalize_abcd_choice_lengths` (banned). Rebalanced choice text in source files only: leads 34, rhythm 30, intervals 31, artifacts 29, cardiac-ap 28, acls-basics 26 (**178** items). Tests: uniquely-longest on authored text; no `BANNED_BALANCE_SUFFIXES`. ABCD shuffle at seed + live/battle start unchanged; audit via `scripts/random_tier_samples.py <seed> mix`.

**Every batch:** No parenthetical labels on distractors; parallel option length; correct answer does not restate the stem; stem clues must not make a distractor defensible.

## EKG batch 01 (ekg-leads-001 to ekg-leads-025)

ekg-leads-001 | pass | Skin prep full question; near-miss saline, lotion, wet alcohol.
ekg-leads-002 | pass | RL ground role; near-miss active QRS lead, V6 substitute, BP ankle.
ekg-leads-003 | pass | 12-lead composition; near-miss 3+9, limb-only, chest-only.
ekg-leads-004 | pass | Limb electrode sites; near-miss all chest, wrists-ankles only, face/hips.
ekg-leads-005 | pass | V1 landmark; near-miss V2, V4, V6 positions.
ekg-leads-006 | pass | V2 landmark; distinct distractors V1/V4/V6.
ekg-leads-007 | pass | V3 between V2 and V4.
ekg-leads-008 | pass | V4 fifth ICS midclavicular.
ekg-leads-009 | pass | V5 anterior axillary line.
ekg-leads-010 | pass | V6 midaxillary line.
ekg-leads-011 | pass | Why lead II for rhythm; near-miss artifact-free myth, chest-only, pressure.
ekg-leads-012 | pass | Lead I LA to RA vector.
ekg-leads-013 | pass | Documentation elements.
ekg-leads-014 | pass | Machine ID, speed, gain checks.
ekg-leads-015 | pass | Conductive gel purpose.
ekg-leads-016 | pass | Supine resting position.
ekg-leads-017 | pass | Augmented leads calculated from limbs.
ekg-leads-018 | pass | Paper speed 25 mm/s.
ekg-leads-019 | pass | Calibration 1 mV = 10 mm.
ekg-leads-020 | pass | Oily skin cleaning.
ekg-leads-021 | pass | Pediatric electrodes and landmarks.
ekg-leads-022 | pass | Breast tissue landmark scenario.
ekg-leads-023 | pass | Revised: concrete LA/RA swap effect (lead I inversion, aVR/aVL swap); answer not circular.
ekg-leads-024 | pass | Cable tension artifact fix.
ekg-leads-025 | pass | Amputation alternative sites scenario.

## EKG batch 02 (ekg-leads-026 to ekg-leads-043)

ekg-leads-026 | pass | Lead II LL to RA derivation.
ekg-leads-027 | pass | 15-lead posterior indication.
ekg-leads-028 | pass | Revised RV scenario: inferior STE + hypotension/JVD, no V1-V3 ST depression clue; V4R single best.
ekg-leads-029 | pass | Posterior STEMI V7-V9 scenario (separate from RV item).
ekg-leads-030 | pass | Mason-Likar stress scenario.
ekg-leads-031 | pass | aVR negative QRS physiology.
ekg-leads-032 | pass | Arm swap P axis in lead I scenario.
ekg-leads-033 | pass | Misplaced V4 serial ST scenario.
ekg-leads-034 | pass | Pulse present limb lead error scenario.
ekg-leads-035 | pass | Orthopnea semi-supine scenario.
ekg-leads-036 | pass | V4R placement landmark.
ekg-leads-037 | pass | V1 vs V6 territory comparison.
ekg-leads-038 | pass | Avoid bony/muscle electrode sites.
ekg-leads-039 | pass | Wandering baseline electrode check.
ekg-leads-040 | pass | Diaphoresis without shifting V leads.
ekg-leads-041 | pass | Nicotine patch removal scenario.
ekg-leads-042 | pass | High V2 false Q wave scenario.
ekg-leads-043 | pass | Trauma dressing limited lead scenario.

## EKG batch 03 (ekg-rhythm-001 to ekg-rhythm-025)

ekg-rhythm-001 | pass | NSR criteria; near-miss AF, VT, flutter.
ekg-rhythm-002 | pass | Sinus brady; near-miss AF, SVT, VF.
ekg-rhythm-003 | pass | Sinus tachy; near-miss SVT without P, AF, flat line.
ekg-rhythm-004 | pass | AF pattern; near-miss flutter, NSR, slow wide escape.
ekg-rhythm-005 | pass | Flutter sawtooth; near-miss AF, Wenckebach, retrograde P SVT.
ekg-rhythm-006 | pass | First-degree AV block definition.
ekg-rhythm-007 | pass | Mobitz I Wenckebach.
ekg-rhythm-008 | pass | Mobitz II fixed PR drops.
ekg-rhythm-009 | pass | Third-degree AV dissociation.
ekg-rhythm-010 | pass | PAC narrow early P.
ekg-rhythm-011 | pass | PVC wide no P.
ekg-rhythm-012 | pass | Monomorphic VT wide regular.
ekg-rhythm-013 | pass | VF chaotic.
ekg-rhythm-014 | pass | Asystole confirm multi-lead.
ekg-rhythm-015 | pass | PEA organized no pulse.
ekg-rhythm-016 | pass | Junctional P absent/inverted.
ekg-rhythm-017 | pass | MAT three P morphologies.
ekg-rhythm-018 | pass | PSVT narrow regular sudden.
ekg-rhythm-019 | pass | Respiratory sinus arrhythmia.
ekg-rhythm-020 | pass | Ventricular bigeminy.
ekg-rhythm-021 | pass | Idioventricular escape slow wide.
ekg-rhythm-022 | pass | Torsades twisting polymorphic.
ekg-rhythm-023 | pass | Advanced: hidden P narrow 200 = PSVT.
ekg-rhythm-024 | pass | Advanced unstable wide VT scenario.
ekg-rhythm-025 | pass | Advanced AF RVR irregular narrow.

## EKG batch 04 (ekg-rhythm-026 to ekg-rhythm-041)

ekg-rhythm-026 | pass | Advanced flutter 2:1 rate math.
ekg-rhythm-027 | pass | Advanced ventricular escape after pause.
ekg-rhythm-028 | pass | Advanced accelerated junctional (replaced pharmacology item).
ekg-rhythm-029 | pass | Fixed PR 0.24 first-degree.
ekg-rhythm-030 | pass | Advanced Wenckebach grouped beats scenario.
ekg-rhythm-031 | pass | Advanced carotid massage PSVT.
ekg-rhythm-032 | pass | Advanced 60 Hz artifact vs VF/STEMI.
ekg-rhythm-033 | pass | Advanced asymptomatic AF management framing.
ekg-rhythm-034 | pass | PVC couplet definition.
ekg-rhythm-035 | pass | Advanced flutter vs PSVT same rate.
ekg-rhythm-036 | pass | Advanced complete block escape syncope.
ekg-rhythm-037 | pass | Advanced Wenckebach PR ladder scenario.
ekg-rhythm-038 | pass | Advanced nonsustained VT runs.
ekg-rhythm-039 | pass | Junctional retrograde P after QRS.
ekg-rhythm-040 | pass | Advanced trigeminy count scenario.
ekg-rhythm-041 | pass | Advanced sudden PSVT with vagal termination.

## EKG batch 05 (ekg-intervals-001 to ekg-intervals-025)

ekg-intervals-001 | pass | QRS ventricular depolarization.
ekg-intervals-002 | pass | P wave atrial depolarization.
ekg-intervals-003 | pass | PR 0.12-0.20; near-miss QRS range, AV block ranges.
ekg-intervals-004 | pass | QRS <0.12; near-miss PR range.
ekg-intervals-005 | pass | QTc rationale; answer not circular restatement.
ekg-intervals-006 | pass | PR 0.24 first-degree.
ekg-intervals-007 | pass | QRS 0.14 conduction delay.
ekg-intervals-008 | pass | ST segment phase.
ekg-intervals-009 | pass | T wave repolarization.
ekg-intervals-010 | pass | PR measurement landmarks.
ekg-intervals-011 | pass | Prolonged QT pattern.
ekg-intervals-012 | pass | Hyperkalemia peaked T.
ekg-intervals-013 | pass | Contiguous ST elevation STEMI.
ekg-intervals-014 | pass | WPW delta short PR.
ekg-intervals-015 | pass | Wide QRS VT vs SVT.
ekg-intervals-016 | pass | Advanced brady QTc assessment.
ekg-intervals-017 | pass | Advanced Wenckebach PR ladder.
ekg-intervals-018 | pass | Advanced STEMI ST pattern focus.
ekg-intervals-019 | pass | Advanced early repolarization vs STEMI scenario.
ekg-intervals-020 | pass | Advanced LBBB morphology with wide QRS.
ekg-intervals-021 | pass | Advanced long QTc torsades risk.
ekg-intervals-022 | pass | PR 0.14 normal correction scenario.
ekg-intervals-023 | pass | Three small boxes = 0.12 s QRS.
ekg-intervals-024 | pass | Five large boxes rate 60.
ekg-intervals-025 | pass | QT interval definition.

## EKG batch 06 (ekg-intervals-026 to ekg-intervals-042)

ekg-intervals-026 | pass | Hypocalcemia QT prolongation.
ekg-intervals-027 | pass | Digoxin ST scooping.
ekg-intervals-028 | pass | Advanced QRS measurement error J point.
ekg-intervals-029 | pass | Advanced PR 0.21 new first-degree.
ekg-intervals-030 | pass | Advanced tachycardia QTc vs raw QT.
ekg-intervals-031 | pass | Advanced AV dissociation PR variability.
ekg-intervals-032 | pass | Advanced chronic T inversion post-MI.
ekg-intervals-033 | pass | Advanced PR measurement from P onset.
ekg-intervals-034 | pass | PR vs QRS confusion teaching item.
ekg-intervals-035 | pass | Advanced magnesium torsades target.
ekg-intervals-036 | pass | PR beat-to-beat minor variation.
ekg-intervals-037 | pass | Advanced nonspecific ST depression context.
ekg-intervals-038 | pass | Advanced RBBB vs LBBB morphology.
ekg-intervals-039 | pass | Advanced paced beat no native PR.
ekg-intervals-040 | pass | Advanced paper speed 50 mm/s QRS time.
ekg-intervals-041 | pass | Advanced PR and QRS both 0.18 unlikely QRS.
ekg-intervals-042 | pass | Advanced pericarditis diffuse ST vs territorial MI.

## EKG batch 07 (ekg-artifacts-001 to ekg-artifacts-025)

_Redo after rushed pass: neighbor distractors (artifact vs rhythm/ST), no joke options._

ekg-artifacts-001 | fail | Respiratory sway vs loose lead vs arm swap vs pericarditis neighbors.
ekg-artifacts-002 | fail | Wire tension vs paper speed / lead change distractors.
ekg-artifacts-003 | fail | 60 Hz vs flutter / VF / sinus arrhythmia neighbors.
ekg-artifacts-004 | fail | Shiver artifact vs AF / MAT / flutter neighbors.
ekg-artifacts-005 | fail | Single flat V3 local fix vs STEMI / limb move distractors.
ekg-artifacts-006 | fail | Diaphoresis: dry skin and new pads vs petroleum / posterior-only.
ekg-artifacts-007 | fail | Documentation adequacy; removed cafeteria joke distractors.
ekg-artifacts-008 | fail | Paced spikes capture vs VF / ignore spikes distractors.
ekg-artifacts-009 | fail | Tooth-brushing motion artifact advanced scenario.
ekg-artifacts-010 | fail | CPR pause rhythm check vs shock during compressions.
ekg-artifacts-011 | fail | High V4 ST mimic vs territorial STEMI neighbors.
ekg-artifacts-012 | fail | All-leads-identical wiring vs RBBB / sinus arrhythmia.
ekg-artifacts-013 | fail | Loose RL ground vs PR / PSVT / flutter neighbors.
ekg-artifacts-014 | fail | Hairy chest clip electrodes vs pad-on-hair distractors.
ekg-artifacts-015 | fail | Cable loop 60 Hz vs lead switch / atropine neighbors.
ekg-artifacts-016 | fail | Failing wire vs Mobitz II / sinus arrest / AF.
ekg-artifacts-017 | fail | Wet alcohol prep vs gain / speed tricks.
ekg-artifacts-018 | fail | Crying child motion vs AF / PSVT / VF neighbors.
ekg-artifacts-019 | fail | Transport VF mimic awake with pulse scenario.
ekg-artifacts-020 | fail | Gauze under pad attenuation vs MI / WPW neighbors.
ekg-artifacts-021 | fail | Athlete cable slack vs overtight / fabric pads.
ekg-artifacts-022 | fail | Arm swap lead I pattern neighbors.
ekg-artifacts-023 | fail | Loose lead vs asystole multi-lead distinction.
ekg-artifacts-024 | fail | Pad burning stop vs press harder distractors.
ekg-artifacts-025 | fail | Clenched fist muscle vs junctional / first-degree / bigeminy.

## EKG batch 08 (ekg-artifacts-026 to ekg-artifacts-043)

ekg-artifacts-026 | fail | Cell phone RF vs alarm off / leg-only leads.
ekg-artifacts-027 | fail | MRI zone policy vs gain / unreadable strip distractors.
ekg-artifacts-028 | fail | Cough transient shift vs Wenckebach / STEMI neighbors.
ekg-artifacts-029 | fail | Erythema rotate site vs glue on broken skin.
ekg-artifacts-030 | fail | Dried foam gel vs AV block / rate change neighbors.
ekg-artifacts-031 | fail | Leads-off V5 stat fix vs print flat channel.
ekg-artifacts-032 | fail | Bed scale spike vs PVC / non-capture / WPW.
ekg-artifacts-033 | fail | Parkinson support reduces tremor artifact neighbors.
ekg-artifacts-034 | fail | Defib pad overlap documentation vs false normal ST.
ekg-artifacts-035 | fail | V4 ST scenario full question stem; near-miss STEMI/early repol/hyperK neighbors.
ekg-artifacts-036 | fail | Bedside immediate quality review scenario.
ekg-artifacts-037 | fail | Nicotine patch under V2 vs on-patch placement.
ekg-artifacts-038 | fail | Undried alcohol vs PR / delta / flutter neighbors.
ekg-artifacts-039 | fail | Mason-Likar motion vs ischemic ST / AV block neighbors.
ekg-artifacts-040 | fail | Uninterpretable ST repeat vs treat noise as STEMI.
ekg-artifacts-041 | fail | Cold shiver field EKG vs defib / AC on noisy strip.
ekg-artifacts-042 | fail | Clone QRS all leads wiring error neighbors.
ekg-artifacts-043 | fail | Limb lead motion on bed turn vs AF / STEMI / CHB neighbors.

## EKG batch 09–10 (ekg-cardiac-ap-001 to ekg-cardiac-ap-043)

ekg-cardiac-ap-001 | pass | P wave atrial depolarization neighbors.
ekg-cardiac-ap-002 | pass | QRS ventricular depolarization neighbors.
ekg-cardiac-ap-003 | pass | SA node location near-miss anatomy.
ekg-cardiac-ap-004 | pass | SA rate 60–100 vs junctional / VT rates.
ekg-cardiac-ap-005 | pass | AV node bridge vs valve / sinus structures.
ekg-cardiac-ap-006 | pass | T wave repolarization neighbors.
ekg-cardiac-ap-007 | pass | AV delay purpose vs afterload / respiration myths.
ekg-cardiac-ap-008 | pass | RV pulmonary outflow vs left heart neighbors.
ekg-cardiac-ap-009 | pass | RCA inferior territory vs LAD / circumflex.
ekg-cardiac-ap-010 | pass | Preload vs afterload / oximetry neighbors.
ekg-cardiac-ap-011 | pass | Ventricular myocardium contractility neighbors.
ekg-cardiac-ap-012 | pass | Cardiac output definition neighbors.
ekg-cardiac-ap-013 | pass | ST segment plateau neighbors.
ekg-cardiac-ap-014 | pass | Sympathetic rate vs AV block / wide QRS myths.
ekg-cardiac-ap-015 | pass | Axis I and aVF vs precordial leads.
ekg-cardiac-ap-016 | pass | Afterload resistance neighbors.
ekg-cardiac-ap-017 | pass | Anterior V3–V4 vs inferior / V1–V2 neighbors.
ekg-cardiac-ap-018 | pass | Prolonged PR first-degree neighbors.
ekg-cardiac-ap-019 | pass | LVH strain pattern neighbors.
ekg-cardiac-ap-020 | pass | Coronary ostia aortic sinus neighbors.
ekg-cardiac-ap-021 | pass | Purkinje rapid conduction vs AV delay.
ekg-cardiac-ap-022 | pass | Ischemia ST-T territorial neighbors.
ekg-cardiac-ap-023 | pass | Left atrium pulmonary veins neighbors.
ekg-cardiac-ap-024 | pass | Right axis RV dominance neighbors.
ekg-cardiac-ap-025 | pass | LAD septal supply neighbors.
ekg-cardiac-ap-026 | pass | Refractory period filling neighbors.
ekg-cardiac-ap-027 | pass | QRS duration definition neighbors.
ekg-cardiac-ap-028 | pass | Lateral I aVL V5 V6 neighbors.
ekg-cardiac-ap-029 | pass | Starling preload stroke volume neighbors.
ekg-cardiac-ap-030 | pass | Slow AV nodal PR lengthening neighbors.
ekg-cardiac-ap-031 | pass | Advanced inferior STE reciprocal scenario.
ekg-cardiac-ap-032 | pass | Advanced LVH pressure overload scenario.
ekg-cardiac-ap-033 | pass | Advanced third-degree dissociation scenario.
ekg-cardiac-ap-034 | pass | Advanced inferior MI AV node ischemia scenario.
ekg-cardiac-ap-035 | pass | Advanced P pulmonale RV strain scenario.
ekg-cardiac-ap-036 | pass | Advanced VT capture fusion scenario.
ekg-cardiac-ap-037 | pass | Advanced exercise ST depression ischemia scenario.
ekg-cardiac-ap-038 | pass | Advanced AS LVH left axis scenario.
ekg-cardiac-ap-039 | pass | Advanced RVH V1 R wave strain scenario.
ekg-cardiac-ap-040 | pass | Advanced anterior STEMI reciprocal scenario.
ekg-cardiac-ap-041 | pass | Advanced Wenckebach location scenario.
ekg-cardiac-ap-042 | pass | Advanced pericarditis diffuse ST scenario.
ekg-cardiac-ap-043 | fail | Anterior QS scenario uses chest pain not syncope; old infarct near-miss distractor.

## EKG batch 11 (ekg-acls-basics-001 to ekg-acls-basics-041)

_Redo: monitor/defibrillator and waveform ACLS; BLS/AED items removed or replaced._

ekg-acls-basics-001 | pass | Shockable VF/pVT vs PEA / asystole / sinus neighbors.
ekg-acls-basics-002 | fail | Replaced AED timing with VF rhythm classification on defibrillator.
ekg-acls-basics-003 | pass | PEA organized QRS without pulse neighbors.
ekg-acls-basics-004 | pass | Asystole confirm multi-lead vs fine VF neighbors.
ekg-acls-basics-005 | pass | CPR pause rhythm analysis neighbors.
ekg-acls-basics-006 | pass | Post-shock CPR priority neighbors.
ekg-acls-basics-007 | pass | ETCO2 rising with compressions advanced scenario.
ekg-acls-basics-008 | pass | Coarse VF pulseless advanced scenario.
ekg-acls-basics-009 | pass | Pulseless wide QRS 160 VT neighbors.
ekg-acls-basics-010 | fail | Sync cardioversion scenario unstable monomorphic VT with pulse.
ekg-acls-basics-011 | fail | Shockable priority near-miss sync-before-shock / delay shock distractors.
ekg-acls-basics-012 | pass | Fine vs coarse VF neighbors.
ekg-acls-basics-013 | pass | Epinephrine arrest rhythm timing neighbors.
ekg-acls-basics-014 | pass | Flat capnography esophageal intubation scenario.
ekg-acls-basics-015 | pass | Post-ROSC 12-lead STEMI scenario.
ekg-acls-basics-016 | fail | PEA vs VF / junctional with pulse / Mobitz II with pulse neighbors.
ekg-acls-basics-017 | pass | Double sequential defibrillation neighbors.
ekg-acls-basics-018 | pass | Pacing spikes capture neighbors.
ekg-acls-basics-019 | pass | PEA narrow 40 organized scenario neighbors.
ekg-acls-basics-020 | pass | Minimize pause coronary perfusion neighbors.
ekg-acls-basics-021 | pass | Torsades polymorphic pattern neighbors.
ekg-acls-basics-022 | pass | Amiodarone refractory VF/pVT neighbors.
ekg-acls-basics-023 | fail | Replaced AED no-shock with manual PEA rhythm check scenario.
ekg-acls-basics-024 | pass | CPR artifact vs VF advanced neighbors.
ekg-acls-basics-025 | fail | Replaced 30:2 with ACLS rhythm pause duration neighbors.
ekg-acls-basics-026 | pass | Post-airway ventilation rate during CPR neighbors.
ekg-acls-basics-027 | fail | Post-shock PEA distractors tightened vs ROSC / persistent VF.
ekg-acls-basics-028 | pass | Hyperkalemia peaked T H-type scenario.
ekg-acls-basics-029 | fail | Replaced compressor switch with polymorphic VT sync cardioversion scenario.
ekg-acls-basics-030 | pass | ROSC monitor perfusion neighbors.
ekg-acls-basics-031 | pass | Lead II P wave visibility neighbors.
ekg-acls-basics-032 | pass | Unstable bradycardia algorithm scenario.
ekg-acls-basics-033 | pass | Pre-charge during compressions neighbors.
ekg-acls-basics-034 | pass | Closed-loop rhythm communication neighbors.
ekg-acls-basics-035 | pass | Compression artifact asystole alarm scenario.
ekg-acls-basics-036 | pass | Tension pneumothorax H-type scenario.
ekg-acls-basics-037 | pass | Post-ROSC MAP goal neighbors.
ekg-acls-basics-038 | pass | ROSC STEMI cath lab monitoring scenario.
ekg-acls-basics-039 | pass | Unstable narrow tach 190 sync pathway scenario.
ekg-acls-basics-040 | pass | Fine VF vs asystole gain scenario.
ekg-acls-basics-041 | pass | Shockable definition VF/pVT neighbors.

## EKG rhythm sweep (batch 04 item tied to NSVT)

ekg-rhythm-038 | fail | NSVT distractors: AIVR, SVT aberrancy, sustained VT neighbors.

## EKG length/parallelism pass 2 (intervals+artifacts)

Pass 2 rules: parallel option length/structure; no stem-contradicting distractors. Verified `correct_is_uniquely_short_by_margin` and `correct_is_uniquely_longest` for topics `ekg-intervals` (42 items) and `ekg-artifacts` (43 items): **0 short-margin, 0 uniquely-longest** after edits.

**Length rebalance edits (5):** ekg-intervals-004, -007, -010, -012, -035 (correct answer was uniquely short vs near-miss distractors).

ekg-intervals-001 | pass | Length/parallel verified; QRS depolarization neighbors.
ekg-intervals-002 | pass | P wave neighbors parallel.
ekg-intervals-003 | pass | PR range neighbors parallel.
ekg-intervals-004 | pass | **Pass 2:** lengthened correct QRS upper limit; PR-range near-miss distractors unchanged.
ekg-intervals-005 | pass | QTc rationale parallel options.
ekg-intervals-006 | pass | First-degree block scenario neighbors.
ekg-intervals-007 | pass | **Pass 2:** restored full IVCD/BBB wording vs widened near-miss distractors.
ekg-intervals-008 | pass | ST segment phase parallel distractors.
ekg-intervals-009 | pass | T wave repolarization neighbors.
ekg-intervals-010 | pass | **Pass 2:** PR landmarks phrasing aligned with distractor length.
ekg-intervals-011 | pass | Prolonged QT pattern neighbors.
ekg-intervals-012 | pass | **Pass 2:** hyperkalemia stem matched with parallel electrolyte distractors.
ekg-intervals-013 | pass | Contiguous ST STEMI scenario neighbors.
ekg-intervals-014 | pass | WPW delta short PR neighbors.
ekg-intervals-015 | pass | Wide QRS VT vs SVT neighbors.
ekg-intervals-016 | pass | Bradycardia QTc scenario neighbors.
ekg-intervals-017 | pass | Wenckebach PR ladder neighbors.
ekg-intervals-018 | pass | STEMI ST pattern focus neighbors.
ekg-intervals-019 | pass | Early repolarization vs STEMI scenario neighbors.
ekg-intervals-020 | pass | LBBB morphology neighbors.
ekg-intervals-021 | pass | Long QTc torsades neighbors.
ekg-intervals-022 | pass | PR 0.14 normal scenario neighbors.
ekg-intervals-023 | pass | Small-box QRS timing neighbors.
ekg-intervals-024 | pass | Large-box rate 60 neighbors.
ekg-intervals-025 | pass | QT interval definition neighbors.
ekg-intervals-026 | pass | Hypocalcemia QT neighbors.
ekg-intervals-027 | pass | Digoxin ST neighbors.
ekg-intervals-028 | pass | QRS measurement error neighbors.
ekg-intervals-029 | pass | PR 0.21 first-degree neighbors.
ekg-intervals-030 | pass | Tachycardia QTc vs raw QT neighbors.
ekg-intervals-031 | pass | AV dissociation PR neighbors.
ekg-intervals-032 | pass | Chronic T inversion neighbors.
ekg-intervals-033 | pass | PR measurement P onset neighbors.
ekg-intervals-034 | pass | PR vs QRS confusion neighbors.
ekg-intervals-035 | pass | **Pass 2:** QT/repolarization magnesium target length balanced.
ekg-intervals-036 | pass | PR beat-to-beat variation neighbors.
ekg-intervals-037 | pass | Nonspecific ST depression context neighbors.
ekg-intervals-038 | pass | RBBB vs LBBB morphology neighbors.
ekg-intervals-039 | pass | Paced beat native PR neighbors.
ekg-intervals-040 | pass | Paper speed 50 mm/s QRS neighbors.
ekg-intervals-041 | pass | PR and QRS 0.18 scenario neighbors.
ekg-intervals-042 | pass | Pericarditis diffuse ST neighbors.

ekg-artifacts-001 | pass | Respiratory sway vs loose lead vs arm swap neighbors verified.
ekg-artifacts-002 | pass | Wire tension vs monitor settings neighbors.
ekg-artifacts-003 | pass | 60 Hz vs arrhythmia mimic neighbors.
ekg-artifacts-004 | pass | Shiver artifact vs AF/MAT/flutter neighbors.
ekg-artifacts-005 | pass | Flat V3 local fix neighbors.
ekg-artifacts-006 | pass | Diaphoresis pad prep neighbors.
ekg-artifacts-007 | pass | Documentation adequacy parallel options.
ekg-artifacts-008 | pass | Paced spikes capture neighbors.
ekg-artifacts-009 | pass | Tooth-brushing motion scenario neighbors.
ekg-artifacts-010 | pass | CPR pause rhythm check neighbors.
ekg-artifacts-011 | pass | High V4 ST mimic neighbors.
ekg-artifacts-012 | pass | All-leads-identical wiring neighbors.
ekg-artifacts-013 | pass | Loose RL ground neighbors.
ekg-artifacts-014 | pass | Hairy chest clip electrode neighbors.
ekg-artifacts-015 | pass | Cable loop 60 Hz neighbors.
ekg-artifacts-016 | pass | Failing wire vs block neighbors.
ekg-artifacts-017 | pass | Wet alcohol prep neighbors.
ekg-artifacts-018 | pass | Crying child motion neighbors.
ekg-artifacts-019 | pass | Transport VF mimic neighbors.
ekg-artifacts-020 | pass | Gauze under pad attenuation neighbors.
ekg-artifacts-021 | pass | Athlete cable slack neighbors.
ekg-artifacts-022 | pass | Arm swap lead I neighbors.
ekg-artifacts-023 | pass | Loose lead vs asystole neighbors.
ekg-artifacts-024 | pass | Pad burning stop neighbors.
ekg-artifacts-025 | pass | Clenched fist muscle neighbors.
ekg-artifacts-026 | pass | Cell phone RF neighbors.
ekg-artifacts-027 | pass | MRI zone policy neighbors.
ekg-artifacts-028 | pass | Cough transient shift neighbors.
ekg-artifacts-029 | pass | Erythema rotate site neighbors.
ekg-artifacts-030 | pass | Dried foam gel neighbors.
ekg-artifacts-031 | pass | Leads-off V5 stat fix neighbors.
ekg-artifacts-032 | pass | Bed scale spike neighbors.
ekg-artifacts-033 | pass | Parkinson tremor support neighbors.
ekg-artifacts-034 | pass | Defib pad overlap documentation neighbors.
ekg-artifacts-035 | pass | V4 ST normalize after reposition neighbors.
ekg-artifacts-036 | pass | Bedside quality review neighbors.
ekg-artifacts-037 | pass | Nicotine patch under V2 neighbors.
ekg-artifacts-038 | pass | Undried alcohol vs rhythm myth neighbors.
ekg-artifacts-039 | pass | Mason-Likar motion vs ischemic ST neighbors.
ekg-artifacts-040 | pass | Uninterpretable ST repeat neighbors.
ekg-artifacts-041 | pass | Cold shiver field EKG neighbors.
ekg-artifacts-042 | pass | Clone QRS wiring neighbors.
ekg-artifacts-043 | pass | Limb lead motion on bed turn neighbors.
