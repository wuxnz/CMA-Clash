# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored EKG questions (topic ekg-leads)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ekg-leads-001
    fact(
        "ekg-leads",
        "How should the skin be prepared before attaching resting 12-lead EKG electrodes?",
        "Clean and dry the site; gently remove excess hair or oil when it blocks contact",
        [
            "Soak the skin with saline before every electrode to improve baseline stability",
            "Apply moisturizing lotion under each pad to protect dry skin over the long term",
            "Leave alcohol wet on the skin without drying before electrode pad placement",
        ],
        "Dry, clean skin lowers impedance and baseline wander. Lotion or pooled alcohol increases motion artifact and can mimic ischemic ST changes on the tracing.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-002
    fact(
        "ekg-leads",
        "What is the primary purpose of the right leg (RL) electrode on a standard 12-lead EKG?",
        "To serve as an electrical ground or reference for the recording system",
        [
            "To record ventricular depolarization as the main diagnostic QRS limb lead",
            "To replace precordial lead V6 on the lateral chest wall during acquisition",
            "To measure noninvasive blood pressure through the right ankle electrode",
        ],
        "RL stabilizes the reference point so limb and chest leads share a common ground. It is not an active diagnostic lead like V6 or lead II.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-003
    fact(
        "ekg-leads",
        "How many electrode views make up a standard diagnostic 12-lead EKG?",
        "Six standard limb leads plus six precordial chest leads on the torso",
        [
            "Three limb leads plus nine precordial chest leads on the anterior torso",
            "Six limb leads recorded without any precordial chest electrodes placed",
            "Fifteen precordial chest leads recorded without standard limb electrodes",
        ],
        "The 12-lead study combines bipolar and augmented limb leads with V1 through V6. Confusing limb-only or chest-only setups misses standard axis and territory analysis.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-004
    fact(
        "ekg-leads",
        "Where are the four limb electrodes placed for a standard 12-lead EKG?",
        "Right arm, left arm, right leg, and left leg per standard limb protocol",
        [
            "All four limb electrodes clustered on the anterior chest wall only without limb sites",
            "Both wrists and both ankles with no shared torso reference or ground electrode",
            "Forehead, chin, and both hips substituted for all four standard limb wire positions",
        ],
        "Limb electrodes establish the frontal plane vectors used in leads I, II, III, and the augmented leads. Chest-only placement cannot produce a true 12-lead study.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-005
    fact(
        "ekg-leads",
        "Which anatomical landmark is used to place precordial lead V1?",
        "Fourth intercostal space at the right sternal border",
        [
            "Fourth intercostal space at the left sternal border",
            "Fifth intercostal space at the left midclavicular line",
            "Fifth intercostal space at the left midaxillary line",
        ],
        "V1 sits in the right parasternal position to view septal activity. Left sternal and lateral chest positions describe V2 and V4/V6, not V1.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-006
    fact(
        "ekg-leads",
        "Which anatomical landmark is used to place precordial lead V2?",
        "Fourth intercostal space at the left sternal border",
        [
            "Fourth intercostal space at the right sternal border",
            "Fifth intercostal space at the midclavicular line",
            "Fifth intercostal space at the midaxillary line",
        ],
        "V2 is the left parasternal lead paired with V1 across the septum. Midclavicular and midaxillary placements at the fifth intercostal space describe V4 and V6.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-007
    fact(
        "ekg-leads",
        "Where is precordial lead V3 typically placed?",
        "Between the V2 and V4 positions along the left anterior chest",
        [
            "Fourth intercostal space at the right sternal border (standard V1 position)",
            "Fifth intercostal space at the midaxillary line on the left lateral chest",
            "Second intercostal space at the right sternal angle near the manubrium",
        ],
        "V3 bridges parasternal and anterior leads as transition between V2 and V4. Right parasternal and posterior positions do not match V3 landmarks.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-008
    fact(
        "ekg-leads",
        "Where is precordial lead V4 placed on the chest?",
        "Fifth intercostal space at the left midclavicular line",
        [
            "Fourth intercostal space at the left sternal border",
            "Fifth intercostal space at the left anterior axillary line",
            "Fourth intercostal space at the right sternal border",
        ],
        "V4 captures anterior forces at the midclavicular line. Left sternal fourth intercostal space is V2, and the anterior axillary line at the same level is V5.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-009
    fact(
        "ekg-leads",
        "Where is precordial lead V5 placed on the chest?",
        "Fifth intercostal space at the left anterior axillary line on the chest",
        [
            "Fifth intercostal space at the left midclavicular line on the chest wall",
            "Fifth intercostal space at the left midaxillary line on the lateral chest",
            "Fourth intercostal space at the left sternal border on the anterior chest",
        ],
        "V5 lies lateral to V4 along the anterior axillary line. Midclavicular placement at the same intercostal level is V4, and midaxillary is V6.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-010
    fact(
        "ekg-leads",
        "Where is precordial lead V6 placed on the chest?",
        "Fifth intercostal space at the left midaxillary line",
        [
            "Fifth intercostal space at the left midclavicular line",
            "Fifth intercostal space at the anterior axillary line",
            "Fourth intercostal space at the right sternal border",
        ],
        "V6 is the lateral precordial lead at the midaxillary line. Midclavicular and anterior axillary positions at the fifth intercostal space describe V4 and V5.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-011
    fact(
        "ekg-leads",
        "Why is lead II often selected for single-lead rhythm monitoring?",
        "Lead II often shows clear P waves, helping separate atrial from ventricular rhythms",
        [
            "Lead II eliminates motion artifact by design regardless of skin preparation quality",
            "Lead II is recorded from a single precordial chest electrode like V5 on the lateral wall",
            "Lead II measures left ventricular pressure directly through the limb wire connections",
        ],
        "Lead II aligns the exploring electrode to highlight atrial depolarization. Artifact can still occur, and chest leads record precordial not limb vectors.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-012
    fact(
        "ekg-leads",
        "What electrical vector does limb lead I measure?",
        "Potential difference between the left arm and right arm",
        [
            "Potential difference between the left leg and right leg",
            "Potential difference between chest leads V1 and V6",
            "Potential difference between lead aVR and lead aVL",
        ],
        "Lead I is a bipolar limb lead from RA to LA in the frontal plane. Leg-to-leg vectors relate to other leads, and V1 to V6 are precordial not limb measurements.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-013
    fact(
        "ekg-leads",
        "Which patient and test information should be documented when acquiring a 12-lead EKG?",
        "Patient identifiers, date/time, clinical indication, and lead protocol used",
        [
            "Technician nickname without patient identifiers, medical record number, or ordering provider",
            "Time of day without patient name, date of birth, medical record number, or symptoms",
            "Lead placement diagram only, with no clinical reason or protocol documented for the test",
        ],
        "Complete acquisition data links the tracing to the correct patient and clinical context. Missing identifiers or indication makes later interpretation and legal review unreliable.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-014
    fact(
        "ekg-leads",
        "What should be verified on the EKG machine before starting a resting 12-lead tracing?",
        "Correct patient data entry, paper speed, and gain (calibration) settings",
        [
            "Paper speed set to 50 mm per minute for all adults",
            "Gain left at factory default without checking calibration pulse amplitude",
            "Printer toner level without confirming electrode connections or lead labels",
        ],
        "Standard resting speed is 25 mm/s and gain is typically 10 mm/mV unless protocol differs. Wrong speed or gain distorts interval and voltage measurements.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-015
    fact(
        "ekg-leads",
        "Why are conductive gel or solid gel pads used with EKG electrodes?",
        "They lower skin impedance so the cardiac signal reaches the monitor with less noise",
        [
            "They insulate the skin to block muscle artifact and dampen QRS voltage on the strip",
            "They cool the skin to slow heart rate on the tracing during resting acquisition",
            "They replace the need to check calibration marks before every standard 12-lead study",
        ],
        "Conductive media improve contact between skin and electrode. Insulation or cooling would worsen signal quality and cannot substitute for proper speed and gain settings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-016
    fact(
        "ekg-leads",
        "What patient position is typically used for a resting 12-lead EKG?",
        "Supine with arms relaxed at the sides and legs uncrossed on the bed",
        [
            "Standing with weight shifted to one leg during electrode placement",
            "Prone with both arms pinned overhead as routine for every adult",
            "Seated and leaning forward as the required position for resting studies",
        ],
        "Supine positioning keeps lead placement consistent between studies. Standing or forced prone positions change axis and baseline compared with routine resting acquisition.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-017
    fact(
        "ekg-leads",
        "How are augmented limb leads aVR, aVL, and aVF produced?",
        "They are calculated from combinations of the limb electrode voltages",
        [
            "They are recorded from separate disposable chest sensors on the sternum",
            "They require relocating all limb electrodes onto the abdomen for every resting study",
            "They duplicate precordial leads V1 through V3 on the anterior chest wall",
        ],
        "Augmented leads use Goldberger relationships from RA, LA, and LL signals. They are not independent chest sensors and are not the same as precordial placements.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-018
    fact(
        "ekg-leads",
        "What paper speed is conventionally used for a resting 12-lead EKG?",
        "25 millimeters per second on the recorder (standard resting speed)",
        [
            "50 millimeters per second on the recorder for every resting tracing",
            "25 millimeters per minute labeled on the paper speed control",
            "10 millimeters per second on the recorder without speed labeling",
        ],
        "At 25 mm/s each small box equals 0.04 s. Using minute-based speed or unlabeled slow speeds makes rate and interval calculations wrong.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-019
    fact(
        "ekg-leads",
        "What does the usual calibration mark on an EKG strip indicate?",
        "A 1 mV signal produces a 10 mm (1 cm) deflection at default gain",
        [
            "A 1 mV signal produces a 5 mm deflection at default gain on the printed strip",
            "A 0.5 mV signal produces a 20 mm deflection at default calibration gain",
            "Amplitude is not related to millivolt calibration on modern digital monitors",
        ],
        "Calibration checks that QRS and ST amplitudes are measured against a known voltage scale. Halved or doubled sensitivity misclassifies hypertrophy and ischemic voltage criteria.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-020
    fact(
        "ekg-leads",
        "Which step helps when oily skin or lotion interferes with electrode adhesion?",
        "Gently clean and dry the skin before applying electrodes",
        [
            "Apply petroleum jelly under each electrode pad to seal moisture in",
            "Leave isopropyl alcohol wet under the pad without air drying",
            "Place gauze between skin and electrode pad to absorb surface oil",
        ],
        "Removing surface oils restores conductive contact. Petroleum or wet alcohol increases impedance, and gauze layers block the signal path.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-021
    fact(
        "ekg-leads",
        "What adjustment is appropriate when performing a 12-lead EKG on a small child per protocol?",
        "Use pediatric electrodes and age-appropriate lead placement per protocol",
        [
            "Use full adult precordial electrodes centered on the abdomen for all pediatric ages",
            "Omit skin preparation to shorten setup time when the child is restless or crying",
            "Record a single precordial lead instead of a full diagnostic 12-lead EKG study",
        ],
        "Pediatric anatomy requires smaller sensors and modified landmarks. Abdomen-only or single-lead recordings do not meet a diagnostic pediatric 12-lead protocol.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-leads-022
    fact(
        "ekg-leads",
        "A patient with large breasts needs precordial leads placed for a 12-lead EKG. What is the best approach?",
        "Lift the breast as needed and place electrodes on the chest wall at standard landmarks",
        [
            "Place all precordial electrodes on top of the underwire bra without direct skin contact",
            "Place electrodes on tight clothing over the sternum instead of standard intercostal landmarks",
            "Document the study using limb leads only and omit all precordial chest leads from the tracing",
        ],
        "Electrodes must contact skin at anatomical landmarks regardless of breast tissue. Bra underwire, clothing, or omitted chest leads produce non-diagnostic tracings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-023
    fact(
        "ekg-leads",
        "After a 12-lead EKG is acquired, the tracing shows unexpected axis and morphology. The technician realizes the left and right arm electrodes were swapped. What is the most likely effect?",
        "Inverted P, QRS, and T in lead I with aVR and aVL appearances reversed from expected",
        [
            "Lead II and lead III wires reversed with subtle frontal plane axis shift on every beat",
            "Right and left leg electrodes reversed while lead I remains upright in all beats on the strip",
            "Precordial leads misplaced with normal limb lead morphology throughout the 12-lead study",
        ],
        "With LA and RA reversed, lead I voltage flips so P, QRS, and T deflect opposite to normal. aVR and aVL also trade expected patterns, which can mimic axis shift or ischemia until leads are fixed.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-024
    fact(
        "ekg-leads",
        "During acquisition, pulling on EKG cable wires causes the baseline to wander on the monitor. What is the best immediate action?",
        "Relieve cable tension and secure electrodes without lifting pads from the skin",
        [
            "Increase cable tension to stabilize wires against the torso during quiet breathing",
            "Remove the right-leg ground electrode to reduce noise on the monitor display",
            "Continue tracing without adjusting wires, electrode slack, or patient position",
        ],
        "Motion and tension create somatic artifact that mimics arrhythmia or ischemia. Securing leads addresses the source rather than masking it by removing reference electrodes.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-025
    fact(
        "ekg-leads",
        "A patient has a bilateral below-knee amputation and needs a 12-lead EKG. What should the technician do first?",
        "Follow facility policy for alternative limb electrode placement and document the modification",
        [
            "Refuse to perform any EKG on patients with bilateral or unilateral lower-limb amputations",
            "Place all electrodes randomly on the chest without a written facility protocol or documentation",
            "Proceed with default foot placements on absent limbs without noting the electrode change in the chart",
        ],
        "Documented alternative sites keep tracings interpretable while meeting safety and policy rules. Random placement or unrecorded changes make serial comparison unreliable.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-026
    fact(
        "ekg-leads",
        "From which limb electrodes is standard lead II derived?",
        "Left leg relative to right arm",
        [
            "Left arm relative to right arm",
            "Left leg relative to left arm",
            "Chest lead V5 relative to V1",
        ],
        "Lead II uses the LL to RA vector, which often highlights P waves. Lead I is LA to RA, lead III is LL to LA, and V5 to V1 is not a standard limb lead II.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-027
    fact(
        "ekg-leads",
        "Why might a 15-lead ECG with posterior leads be ordered in addition to the standard 12 leads?",
        "To improve detection of posterior wall ischemia or infarction",
        [
            "To measure hearing thresholds during treadmill stress testing",
            "To replace limb leads when ankles are injured or legs are unavailable",
            "To record dental nerve conduction during routine resting EKG acquisition",
        ],
        "Posterior leads (for example V7 to V9) visualize posterior ST changes that can be subtle on V1 to V6. They do not replace limb leads for frontal plane axis.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-028
    fact(
        "ekg-leads",
        "A patient with acute inferior ST elevation in leads II, III, and aVF has hypotension and jugular venous distension. Which additional precordial lead placement best assesses right ventricular infarction?",
        "Right-sided precordial lead V4R",
        [
            "Posterior lead V9 on the left back",
            "Lead aVR recorded a second time at higher gain",
            "An extra V6 on the left midaxillary line",
        ],
        "Inferior injury plus hypotension and elevated neck veins raise concern for right ventricular involvement. V4R faces the right ventricle; V9 evaluates the posterior left ventricle, and repeating aVR or V6 does not replace V4R.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-029
    fact(
        "ekg-leads",
        "A patient has chest pain and ST depression in V1 to V3 with upright T waves in V1. Which extra leads are most helpful to evaluate posterior infarction?",
        "Posterior leads V7 through V9",
        [
            "Right-sided lead V4R alone",
            "Additional limb lead I on both wrists",
            "Lead aVF recorded a second time",
        ],
        "Posterior STEMI can hide behind anterior ST depression; V7 to V9 face the posterior wall. V4R assesses the right ventricle, not the posterior left ventricle.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-030
    fact(
        "ekg-leads",
        "During an exercise stress test, the team uses a Mason-Likar lead system. Why is this modification made?",
        "Torso limb electrodes reduce motion artifact while the patient walks during stress testing",
        [
            "It removes the need for any skin preparation before exercise or stress-test electrodes",
            "It eliminates the requirement for precordial leads during formal treadmill stress testing",
            "It permanently replaces ICU 12-lead bedside monitoring in critical care units hospital-wide",
        ],
        "Moving limb electrodes to the torso stabilizes wires during exercise. Skin prep and precordial leads are still required, and ICU monitoring still uses standard placements.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-031
    fact(
        "ekg-leads",
        "On a correctly acquired 12-lead EKG, why does lead aVR often show a predominantly negative QRS compared with other limb leads?",
        "It views the heart from the right shoulder toward the left leg, opposite many frontal vectors",
        [
            "The printer was loaded with faded thermal paper during the resting 12-lead acquisition",
            "The patient held a deep breath for the entire resting 12-lead tracing without normal breathing",
            "The monitor automatically inverts every other limb lead on the display without operator input",
        ],
        "aVR orientation explains its typical negative deflection in normal tracings. Paper, respiration, or random inversion settings do not explain consistent aVR morphology.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-032
    fact(
        "ekg-leads",
        "A 12-lead tracing shows negative P waves in lead I and positive P waves in lead aVR, but the patient is in sinus rhythm. What technical error should be suspected first?",
        "Left and right arm electrodes are reversed",
        [
            "Chest leads V1 and V2 are swapped",
            "Paper speed is set to 25 mm/s",
            "The patient is supine with arms at the sides",
        ],
        "Arm electrode reversal flips expected limb lead patterns while rhythm may remain sinus. Swapped V leads affect precordial not global P axis in limb leads I and aVR.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-033
    fact(
        "ekg-leads",
        "A technician compares two resting 12-lead EKGs on the same patient. V4 is one intercostal space higher on the repeat study, and ST segments look different. What is the most likely explanation?",
        "Changed precordial electrode position altered the recorded ST segment",
        [
            "The heart migrated upward between the two resting 12-lead studies",
            "Paper calibration marks changed ventricular rhythm on the printed strip",
            "Lead II was selected instead of lead III on the monitor rhythm display",
        ],
        "ST elevation criteria depend on consistent V4 placement at the fifth intercostal midclavicular line. Higher or lower chest electrodes change amplitude and mimic or mask ischemia.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-034
    fact(
        "ekg-leads",
        "During a code, a monitor shows coarse ventricular activity, but the patient has a pulse. The physician asks whether the limb leads were placed correctly. Which finding best supports swapped arm electrodes?",
        "P wave axis appears inverted in lead I with unexpected limb lead morphology",
        [
            "Identical QRS morphology in both V1 and V6 precordial leads during normal sinus rhythm",
            "Uniform calibration pulse artifact before every QRS complex on the printed strip",
            "Equal R-wave amplitude in V4 and V5 after verified precordial placement at standard landmarks",
        ],
        "Limb lead reversal changes global P and QRS axis in the frontal plane. Identical precordial complexes or calibration artifacts do not explain limb lead axis inversion.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-035
    fact(
        "ekg-leads",
        "A patient cannot lie flat due to orthopnea but urgently needs a 12-lead EKG. What is the best compromise per common practice?",
        "Acquire the study in the most supine position tolerated and document the position used",
        [
            "Delay the EKG until the patient can stand for five minutes without dyspnea or chest pain",
            "Record limb leads in standing position and omit all precordial chest leads from the study",
            "Use a phone camera on the monitor instead of printing a diagnostic 12-lead tracing",
        ],
        "Semi-recumbent acquisition with documentation preserves diagnostic data when full supine is impossible. Standing limb-only recordings omit precordial ischemia assessment.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-036
    fact(
        "ekg-leads",
        "When acquiring a right-sided 12-lead EKG for suspected right ventricular infarction, where is lead V4R placed?",
        "Fifth intercostal space on the right midclavicular line",
        [
            "Fourth intercostal space on the left sternal border (standard V2 position)",
            "Fifth intercostal space on the left midaxillary line (standard V6 position)",
            "Second intercostal space on the right sternal border near the angle of Louis",
        ],
        "V4R mirrors left V4 on the right chest to view the right ventricle. Left sternal V2, left V6, and high right parasternal positions do not substitute for V4R.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-037
    fact(
        "ekg-leads",
        "Which precordial lead pair is most helpful when comparing septal versus lateral ST changes during acute chest pain?",
        "V1 and V6 acquired at the same time in the standard 12-lead set",
        [
            "V1 recorded alone without any other precordial or limb chest leads",
            "V4R and V9 posterior leads without any standard limb electrodes",
            "Lead I and lead II limb tracings without precordial chest electrodes",
        ],
        "V1 reflects septal and right-sided forces while V6 reflects lateral wall activity in the same snapshot. Single-lead or limb-only recordings lose territory comparison.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-038
    fact(
        "ekg-leads",
        "What is the main reason to avoid placing limb electrodes on bony prominences or thick muscle bellies when possible?",
        "Motion and poor contact at those sites increase artifact on the tracing",
        [
            "Bone blocks all electrical activity from reaching the limb electrode pad",
            "Skeletal muscle tissue prevents any cardiac voltage from being detected",
            "Bony prominences automatically double the paper speed on the recorder",
        ],
        "Artifact from movement and unstable contact mimics arrhythmia or ST deviation. Electrical signals still reach electrodes, but noise increases when contact is poor.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-039
    fact(
        "ekg-leads",
        "A resting EKG shows wandering baseline but crisp QRS complexes when the patient lies still. What electrode factor should be rechecked first?",
        "Each pad has intact gel and firm adhesion after proper skin prep",
        [
            "The printer is out of calibration ink on the thermal strip",
            "Lead II was selected on the monitor for single-lead rhythm display",
            "The patient spoke briefly during one respiratory cycle on the tracing",
        ],
        "Loose or dry electrodes cause baseline wander that improves when the patient is motionless. Monitor lead selection or brief speech rarely explains persistent wander across all leads.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-040
    fact(
        "ekg-leads",
        "Why should precordial electrodes not be shifted to the nearest dry skin fold when the standard landmark is moist with diaphoresis?",
        "Misplaced chest leads change ST and R-wave patterns compared with standard positions",
        [
            "Moisture from diaphoresis automatically doubles heart rate on the tracing during acquisition",
            "Diaphoresis prevents any electrical signal from being recorded at the precordial electrode site",
            "Standard precordial landmarks are optional during acute chest pain care when skin is wet",
        ],
        "Ischemia protocols rely on consistent V lead positions. Moving electrodes to skin folds alters voltage and can mimic or hide pathology even when sweat is present.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-leads-041
    fact(
        "ekg-leads",
        "A 12-lead EKG is ordered stat, but the patient is wearing a nicotine patch on the anterior chest. What should the technician do?",
        "Remove the patch if allowed, clean adhesive, and place precordial leads on skin at landmarks",
        [
            "Place precordial electrodes directly on top of the nicotine patch material without removal",
            "Cancel the stat EKG because transdermal patches block all cardiac electrical signals completely",
            "Place all chest leads on the patient's back without documenting the landmark or lead change",
        ],
        "Patches and adhesive interfere with electrode contact and standard landmarks. Documented skin placement preserves interpretability; canceling or undocumented back placement is unsafe.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-042
    fact(
        "ekg-leads",
        "Two serial 12-lead EKGs show new Q waves in V1 to V3, but V2 was placed one rib space too high on the second study. What is the best next step?",
        "Repeat the 12-lead with verified chest landmarks before cath activation from the second tracing alone",
        [
            "Activate the cath lab using only the second tracing without confirming precordial lead placement",
            "Ignore lead position because Q waves on the strip are always true infarction regardless of V lead height",
            "Compare only limb leads from the second study and ignore all precordial leads on both tracings",
        ],
        "High or low V leads distort QRS and ST patterns that mimic infarction. Confirming placement prevents false activation while still treating true ischemia when landmarks are correct.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-leads-043
    fact(
        "ekg-leads",
        "During prehospital acquisition, the monitor offers a reduced lead set because of trauma dressings covering the anterior chest. What is the most appropriate action?",
        "Acquire the best lead set per protocol, document limits, and obtain full 12-lead when dressings allow",
        [
            "Transmit no EKG data to the receiving hospital until every precordial lead is perfect and dry",
            "Label the tracing as normal without noting missing leads, alternative sites, or trauma dressing limits",
            "Place chest electrodes on top of bloody trauma dressings without notifying the clinical team or EMS medical control",
        ],
        "Documented limited acquisitions still guide care while prompting a complete study when safe. Unlabeled incomplete data or electrodes on dressings mislead downstream interpretation.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
