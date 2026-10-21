# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-clinical-care)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-clinical-care-001
    fact(
        'ccma-clinical-care',
        'Before applying a topical antibiotic to an open wound in the clinic, what should the medical assistant do first?',
        'Perform hand hygiene and use clean or aseptic technique per facility policy',
        [
            'Don the same pair of gloves worn during the prior patient encounter',
            'Wipe the wound with a used alcohol pad from the supply cart',
            'Apply ointment without cleansing when the surrounding skin looks dry',
        ],
        'Topical medications can introduce pathogens if hands or supplies are contaminated. Facility policy guides whether clean or sterile technique is required for the specific wound presentation.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-002
    fact(
        'ccma-clinical-care',
        'When performing a capillary blood glucose check at the point of care, which supply practice reduces cross-contamination risk?',
        'Use a new lancet and an in-date test strip for each puncture per policy',
        [
            'Rinse and reuse lancets between patients in the same clinic session',
            'Use test strips past the printed expiration date if the vial is sealed',
            'Puncture the same fingertip site repeatedly without rotating sites',
        ],
        'Single-use lancets and current strips support accurate results and infection control. Reusing sharps or expired reagents is a common source of clinic errors.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-003
    fact(
        'ccma-clinical-care',
        'A patient arrives for a fasting blood draw. Which pre-test instruction aligns with typical laboratory orders?',
        'Take no food or drink except plain water if the order permits water',
        [
            'Drink fruit juice with breakfast before leaving home',
            'Withhold all fluids including water for 24 hours unless instructed otherwise',
            'Take an extra dose of diabetes medication to lower the sample glucose',
        ],
        'Fasting requirements depend on the specific tests ordered; juice and extra medication can invalidate results. Patients should follow the written order and ask the care team when instructions are unclear.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-004
    fact(
        'ccma-clinical-care',
        'Dense hair covers the skin where ECG electrodes will be placed. How should the medical assistant prepare the sites?',
        'Clip the hair close to the skin; shave with a razor only when the provider orders shaving',
        [
            'Shave every electrode site with a razor before each routine tracing',
            'Leave the hair intact and press the electrode directly onto it',
            'Coat the hair with body lotion to improve electrode adhesion',
        ],
        'Good skin contact reduces artifact and improves tracing quality. Routine razor shaving can nick skin and is reserved for orders, whereas clipping is often sufficient.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-005
    fact(
        'ccma-clinical-care',
        'After changing a soiled wound dressing, how should the medical assistant dispose of the contaminated materials?',
        'Place them in the designated biohazard or regulated medical waste container',
        [
            'Discard them in the general office trash receptacle',
            'Send the used dressing home with the patient for later disposal',
            'Set them aside on the counter to reuse during the next dressing change',
        ],
        'Blood-soaked dressings are regulated waste in most outpatient settings. Household trash and patient take-home disposal do not meet occupational safety requirements.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-006
    fact(
        'ccma-clinical-care',
        "An established patient reports new chest pressure while waiting in the exam room. What is the medical assistant's priority action?",
        'Notify the provider immediately and remain with the patient',
        [
            'Complete rooming tasks for other patients before responding',
            'Instruct the patient to walk briskly in the hallway to work through the pain',
            'Plan to document the complaint at the end of the shift',
        ],
        'New chest symptoms may signal acute coronary or other emergent conditions. The assistant stays with the patient while the licensed clinician is alerted without delay.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-007
    fact(
        'ccma-clinical-care',
        'When obtaining an adult body weight for the medical record, which scale setup supports the most reliable measurement?',
        'Use a calibrated scale placed on a firm, level surface',
        [
            'Use a bathroom scale set on thick carpet for patient comfort',
            'Tilt the scale slightly so fluids drain away from the feet',
            'Rely on the same scale reading without periodic calibration checks',
        ],
        'Uneven or soft flooring and uncorrected drift produce false trends in weight-based dosing and monitoring. Calibration logs are part of routine equipment maintenance.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-008
    fact(
        'ccma-clinical-care',
        'A patient loses consciousness briefly during a minor in-office procedure. What should the medical assistant do first?',
        'Lower the patient safely, check responsiveness and breathing, and summon help',
        [
            'Keep the patient upright by gripping the hair to prevent falling',
            'Offer solid food by mouth while the patient is unresponsive',
            'Leave the procedure room to finish charting before assisting',
        ],
        'Syncope requires airway and circulation assessment and prevention of injury from falling. Oral intake is unsafe until the patient is fully alert and swallowing normally.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-009
    fact(
        'ccma-clinical-care',
        "When applying a cold pack for a localized injury, how should the medical assistant protect the patient's skin?",
        'Place a cloth barrier between the skin and the cold source',
        [
            'Apply the iced pack directly to the skin for several hours continuously',
            'Use cold therapy over numb areas without inspecting the skin',
            'Ignore reports of burning or numbness at the application site',
        ],
        'Prolonged direct cold can cause frostbite, especially over areas with reduced sensation. Barriers and timed application follow safe thermal therapy practice.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-010
    fact(
        'ccma-clinical-care',
        'While assisting with a pelvic examination, how should draping be managed?',
        'Cover the patient to preserve privacy, warmth, and modesty',
        [
            'Leave the exam room door open to the busy hallway',
            'Remove all drapes quickly to shorten the visit time',
            'Discuss unrelated financial matters aloud during the exam',
        ],
        'Modesty and thermal comfort reduce anxiety and support cooperation during sensitive exams. Conversations should stay clinical and at a respectful volume.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-011
    fact(
        'ccma-clinical-care',
        'During a visual acuity screening in clinic, how should a patient who normally wears glasses or contacts be tested?',
        'Use the usual corrective lenses unless the provider gives different instructions',
        [
            'Require pinhole testing and leave prescribed lenses off for every line',
            'Keep one eye covered for the full test instead of alternating per protocol',
            'Measure acuity from a random distance using whichever wall chart is empty',
        ],
        'Screening should reflect how the patient sees day to day unless a specific protocol calls for uncorrected vision. Standardized distance and eye sequencing follow facility policy.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-012
    fact(
        'ccma-clinical-care',
        'Compared with a standard 12-lead electrocardiogram, adding posterior leads in a 15-lead study may improve detection of what?',
        'Posterior wall myocardial ischemia',
        [
            'Dental enamel decay',
            'Sensorineural hearing loss',
            'Skin turgor changes without other assessment',
        ],
        'Posterior ST changes can be subtle on a standard 12-lead tracing. Extra posterior leads increase sensitivity for occult ischemia behind the heart.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-013
    fact(
        'ccma-clinical-care',
        'While measuring vital signs, the medical assistant hears new expiratory wheezing in a patient with no prior documentation of wheezes. What action is appropriate?',
        'Promptly report the finding to the clinical team',
        [
            'Defer mention of wheezing until the next annual wellness visit',
            'Record the sound in a personal notebook instead of the chart',
            'Tell the patient to stop all respiratory medications without provider input',
        ],
        'New wheezing may reflect bronchospasm, aspiration, or another acute process. Timely communication allows the provider to examine the patient and adjust treatment.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-014
    fact(
        'ccma-clinical-care',
        'Why do clinical guidelines recommend routine foot examination for patients with diabetes?',
        'To identify ulcers, deformities, or loss of sensation early',
        [
            'To replace the need for annual dilated eye examinations',
            'To substitute for regular blood glucose self-monitoring',
            'To eliminate footwear recommendations from the care plan',
        ],
        'Peripheral neuropathy and poor healing put diabetic feet at high risk for limb-threatening infection. Foot checks complement, rather than replace, glucose control and eye care.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-015
    fact(
        'ccma-clinical-care',
        'Once a sterile field is opened for a procedure, how should the medical assistant maintain it?',
        'Keep the field in view and prevent contact with non-sterile surfaces or items',
        [
            'Save unused instruments on the field for use with the next patient',
            'Cover sterile instruments with a non-sterile clinic towel for storage',
            'Reach over the field with ungloved hands to adjust lighting',
        ],
        'Sterility is broken the moment a non-sterile object crosses above or touches the field. Fields are opened for one patient and one procedure episode.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-016
    fact(
        'ccma-clinical-care',
        'During routine venipuncture, how long should a tourniquet typically remain tied above the draw site?',
        'About one minute or less unless the protocol allows briefly longer',
        [
            'Five minutes while multiple difficult attempts are made',
            'Ten minutes until venous distention is maximal',
            'Until clotting at the puncture site is visible',
        ],
        'Extended tourniquet time can hemoconcentrate analytes such as potassium and falsely alter several chemistry results. Release the tourniquet as soon as blood flow is established.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-017
    fact(
        'ccma-clinical-care',
        'When teaching a patient about heat therapy at home, over which sites should the medical assistant caution against applying heat?',
        'Acute inflamed tissue, open wounds, or areas with diminished sensation',
        [
            'Chronic muscle spasm when heat is explicitly ordered',
            'Healed surgical scars when heat is part of the plan',
            'Stiff arthritic joints when the provider recommends warmth',
        ],
        'Heat increases blood flow and can worsen acute inflammation or burn insensate skin. Ordered heat for chronic spasm or stiffness is appropriate when the skin is intact and sensate.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-018
    fact(
        'ccma-clinical-care',
        'When assisting a provider with suture removal, which practice aligns with safe clinical care?',
        'Use hand hygiene and sterile or clean technique according to order and policy',
        [
            'Pull each suture knot without washing hands between patients',
            'Use non-sterile shears on purulent wounds without notifying the provider',
            'Remove every suture when one segment looks erythematous without reporting it',
        ],
        'Even closed wounds can harbor bacteria at suture lines. Hand hygiene, appropriate gloves, and reporting erythema or drainage help prevent secondary infection.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-019
    fact(
        'ccma-clinical-care',
        'Immediately before starting a sterile procedure, what should the medical assistant confirm about the patient?',
        'Identity with two identifiers and informed consent when required by policy',
        [
            'Room number by itself on the whiteboard',
            'Powdered latex gloves for a better instrument grip',
            'Recent oral intake regardless of whether fasting was ordered',
        ],
        'Wrong-patient procedures are preventable with two-identifier checks and documented consent. Room numbers and glove preferences do not verify who is receiving invasive care.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-020
    fact(
        'ccma-clinical-care',
        'Before the first venipuncture attempt, which verification step reduces wrong-patient laboratory errors?',
        'Match the patient to the order using two approved identifiers',
        [
            'Rely on the carpet color in the hallway outside the room',
            'Accept the insurance card alone as proof of identity',
            'Use the scheduled appointment start time as the sole identifier',
        ],
        'Laboratory specimens labeled for the wrong person can lead to harmful treatment decisions. Name and date of birth (or other approved pair) must match the requisition.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-021
    fact(
        'ccma-clinical-care',
        'Before giving a provider-ordered injection, which checks reflect medication safety standards?',
        'Correct patient, medication, dose, route, time, and documentation',
        [
            'Vial stopper color as the sole determinant of drug selection',
            'Room number posted on the door',
            'Pharmacy fax number on the label',
        ],
        'The six rights of medication administration guard against look-alike vials and transcription errors. Visual cues such as cap color are insufficient without reading the label against the order.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-022
    fact(
        'ccma-clinical-care',
        'During a minor office procedure, what is an appropriate role for the medical assistant?',
        'Maintain the sterile field and hand instruments to the provider',
        [
            'Close the incision independently without provider supervision',
            'Administer general anesthesia without anesthesia credentials',
            'Limit participation to unrelated billing documentation',
        ],
        'Medical assistants work within scope by anticipating needs and protecting sterility. Surgical closure and anesthesia require licensure beyond the MA role.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-023
    fact(
        'ccma-clinical-care',
        'Mid-draw during venipuncture the patient turns pale and diaphoretic. What should the medical assistant do immediately?',
        'Terminate the attempt and guard the patient from injury',
        [
            'Complete the blood collection before attending to symptoms',
            'Tighten the tourniquet to finish filling the tubes faster',
            'Leave the chair to search for help while the patient sits alone',
        ],
        'Vasovagal syncope during phlebotomy is common and can cause falls. Stopping the draw, lowering the head if tolerated, and calling for assistance follow standard reaction protocols.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-024
    fact(
        'ccma-clinical-care',
        'When irrigating a wound under provider direction, which supply choice supports aseptic technique?',
        'Sterile saline or another solution specified in the order, poured without contaminating the bottle tip',
        [
            'Unsterile tap water dipped from a utility sink without label review',
            'A communal scrub brush carried between multiple treatment rooms',
            'Full-strength alcohol instilled into deep wound cavities as routine practice',
        ],
        'Irrigation fluid and delivery equipment must stay free of environmental contaminants. Alcohol is not a routine deep-cavity irrigant and can damage healing tissue.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-025
    fact(
        'ccma-clinical-care',
        'When applying an elastic compression wrap for peripheral edema, in which direction should the bandage be wrapped?',
        'From distal to proximal with smooth, overlapping layers',
        [
            'From proximal to distal leaving deliberate gaps between turns',
            'In random directions with uneven tension on each pass',
            'Directly over open draining wounds without secondary dressing',
        ],
        'Distal-to-proximal wrapping promotes venous return and avoids tourniquet effect at the toes or fingers. Open wounds need primary dressings before compression.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'For adults, fever is often defined orally as a temperature above?',
        '100.4°F (38°C)',
        [
            '98.6°F in every adult always',
            '95°F',
            '104°F only at night',
        ],
        'Individual baselines vary, but 100.4°F oral is a common fever threshold in adults. Site of measurement changes expected values.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'High-alert medications such as insulin require?',
        'Independent double checks per policy when dispensing or administering',
        [
            'Single-person rush without label read',
            'Storage mixed with saline flushes unlabeled',
            'Dosing by memory without order',
        ],
        'Insulin and other high-alert drugs have narrow therapeutic windows. Independent checks catch decimal errors.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Holter monitoring is used to?',
        'Record ambulatory ECG over 24-48 hours',
        [
            'Replace all inpatient telemetry forever',
            'Measure intraocular pressure',
            'Culture throat swabs',
        ],
        'Continuous ambulatory ECG captures intermittent arrhythmias. Choosing Replace all inpatient telemetry forever is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'How should A medication error near-miss be assessed on the tracing?',
        'Documented and reported per facility policy for system improvement',
        [
            'Ignored if the patient was unharmed',
            'Only discussed verbally without a record',
            'Hidden to protect staff',
        ],
        'Reporting near-misses helps fix processes before patient harm occurs. Policies define nonpunitive reporting channels.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'How should A patient with suspected stroke be assessed on the tracing?',
        'Immediate emergency evaluation and rapid transport',
        [
            'Routine next-week appointment',
            'Only blood glucose without EMS',
            'Delayed imaging without triage',
        ],
        'Time-sensitive care improves outcomes. Choosing Routine next-week appointment is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'How should Urine dipstick protein detected in a nonfasting patient be assessed on the tracing?',
        'Documented and reported per protocol',
        [
            'Ignored if color is yellow',
            'Treated as lab error always',
            'Discarded without provider notice',
        ],
        'Abnormal POC results require follow-up per policy. Choosing Ignored if color is yellow is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'How should When measuring adult blood pressure, the cuff bladder width be assessed on the tracing?',
        '40% of the upper arm circumference',
        [
            '10% of the arm',
            'Equal to wrist width only',
            '80% of thigh length',
        ],
        'Proper cuff size prevents falsely high or low readings. Choosing 10% of the arm is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Incentive spirometry coaching encourages?',
        'Slow deep inhalation to expand lungs',
        [
            'Breath holding indefinitely',
            'Hyperventilation until dizziness',
            'Shallow rapid breaths only',
        ],
        'Deep breathing helps prevent atelectasis after surgery. Choosing Breath holding indefinitely is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Look-alike sound-alike (LASA) medications require?',
        'Tall-man lettering and extra verification steps',
        [
            'Storing all vials unlabeled',
            'Using only color of cap as sole identifier',
            'Skipping the second identifier check',
        ],
        'LASA pairs such as hydroxyzine and hydralazine need deliberate verification. Tall-man lettering highlights spelling differences.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Orthostatic vital sign measurement compares?',
        'Blood pressure and heart rate lying, sitting, and standing',
        [
            'Temperature only in each position',
            'Respiratory rate after exercise only',
            'Pain score without position change',
        ],
        'Orthostatic changes may indicate hypovolemia or autonomic dysfunction. Choosing Temperature only in each position is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Orthostatic vital signs are taken to assess?',
        'Positional blood pressure and heart rate changes',
        [
            'Fasting blood glucose trends only',
            'Peak expiratory flow during asthma attack',
            'Visual acuity with corrective lenses',
        ],
        'Orthostatic measurements compare blood pressure and pulse across positions to detect volume depletion or autonomic dysfunction. Glucose, peak flow, and vision tests do not assess positional cardiovascular changes.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Orthostatic vital signs compare measurements?',
        'Lying, sitting, and standing positions',
        [
            'Only during sleep',
            'Only after exercise always',
            'Without documenting position',
        ],
        'Position changes assess volume status and autonomic response. Choosing Only during sleep is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Peak expiratory flow is measured with the patient?',
        'Standing or sitting upright with maximal effort after full inspiration',
        [
            'Lying flat without instruction',
            'Holding breath for one minute first',
            'After vigorous exercise only',
        ],
        'PEF requires a forceful exhale into the meter. Poor effort or poor seal gives falsely low readings.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Peak flow meter testing primarily assesses?',
        'Expiratory airflow in asthma monitoring',
        [
            'Blood glucose',
            'Visual acuity',
            'Bone density',
        ],
        'Peak flow supports asthma action plans. Choosing Blood glucose is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Peak flow testing is used to monitor?',
        'Asthma-related expiratory airflow',
        [
            'Blood glucose trends in diabetes',
            'Resting heart rate variability alone',
            'Daily weight for fluid overload only',
        ],
        'Peak expiratory flow reflects bronchospasm and helps patients and clinicians track asthma control over time. Blood glucose and weight monitoring are important in other conditions but do not measure expiratory airflow.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Sterile technique is most critical when?',
        'Touching sterile fields or invasive devices',
        [
            'Greeting patients at reception',
            'Printing schedules',
            'Filing insurance cards',
        ],
        'Sterility prevents introduction of pathogens. Choosing Greeting patients at reception is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Suture removal on a healed wound typically uses?',
        'Clean technique with non-sterile gloves if policy allows',
        [
            'No hand hygiene',
            'Sterile gown always',
            'Suture scissors without cleaning',
        ],
        'Clean procedure is common for closed external wounds. Choosing No hand hygiene is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'What is When performing a visual acuity screening, standard distance?',
        '20 feet (or equivalent chart setup)',
        [
            '5 inches',
            '100 meters only',
            "At arm's length only for all ages",
        ],
        'Snellen charts use standardized testing distance. Choosing 5 inches is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When applying a blood pressure cuff, the bladder should encircle at least what percent of the arm?',
        '80% of the arm circumference',
        [
            '40% of the arm',
            '50% of the wrist only',
            '100% overlap is required',
        ],
        'An undersized cuff reads falsely high and an oversized cuff reads falsely low. Eighty percent arm coverage is the usual teaching standard for adults.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When applying a elastic bandage for edema control, wrap?',
        'From distal to proximal with even pressure',
        [
            'From proximal to distal tightly',
            'Over open draining wounds without dressing',
            'Loosely with gaps only',
        ],
        'Distal-to-proximal supports venous return. Choosing From proximal to distal tightly is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When applying elastic bandage compression, the MA should?',
        'Check distal circulation, sensation, and warmth after application',
        [
            'Wrap as tightly as possible without assessment',
            'Leave toes or fingers uncovered without checking color',
            'Reuse soiled bandages on another patient',
        ],
        'Circulation checks help prevent neurovascular compromise. Choosing Wrap as tightly as possible without assessment is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When assisting with a sterile procedure, the assistant should?',
        'Avoid reaching over the sterile field',
        [
            'Rest elbows on the sterile drape',
            'Adjust mask after scrub without regloving',
            'Pass nonsterile items over the field',
        ],
        'Only sterile items contact the sterile field. Choosing Rest elbows on the sterile drape is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When assisting with a wound dressing change, non-sterile gloves are appropriate when?',
        'Contact with intact skin and clean dressings only is expected',
        [
            'Entering a sterile body cavity',
            'Placing sutures',
            'Handling used sharps without a container',
        ],
        'Glove choice matches anticipated exposure. Choosing Entering a sterile body cavity is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When collecting a clean-catch urine specimen, instruct the patient to?',
        'Clean the meatus and discard first stream before collecting midstream',
        [
            'Collect the first drops only',
            'Use the same container for multiple days',
            'Skip hand hygiene',
        ],
        'Midstream clean-catch reduces contamination. Choosing Collect the first drops only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When measuring peak flow, the patient should?',
        'Use maximal effort after proper instruction',
        [
            'Hold breath for two minutes',
            'Measure while lying flat only',
            'Skip device cleaning',
        ],
        'Technique affects reproducibility. Choosing Hold breath for two minutes is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-clinical-care',
        'When removing sutures, use?',
        'Sterile technique per provider order and site assessment',
        [
            'Nonsterile scissors on infected tissue without gloves',
            'Pull knots without assessment',
            'Apply shared topical without label check',
        ],
        'Assess healing and use aseptic technique. Choosing Nonsterile scissors on infected tissue without gloves is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

