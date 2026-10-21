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
        'Sterile irrigant from a new container, poured without touching the pour spout to the field',
        [
            '0.9% saline drawn into a syringe from a multi-dose vial opened earlier the same day',
            'Antiseptic wound cleanser used as the irrigating fluid per label',
            'Sterile water remaining in a bowl that sat open on the mayo stand for an hour',
        ],
        'Irrigation requires fluid and delivery that stay uncontaminated. Multi-dose vials and open bowls increase bioburden; antiseptics clean skin but are not routine primary irrigants for deep tissue flushing.',
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
    # ccma-clinical-care-026
    fact(
        'ccma-clinical-care',
        'An adult patient has an oral temperature of 101.0°F (38.3°C) with no baseline documented. How should the medical assistant classify this reading for triage?',
        'As fever using the common adult oral threshold above 100.4°F (38°C)',
        [
            'As normal because 98.6°F is the only acceptable adult value',
            'As hypothermia requiring immediate ice immersion',
            'As fever only when the reading exceeds 104°F at night',
        ],
        'Individual baselines vary, but oral temperatures above 100.4°F are widely treated as fever in adults. Measurement site and timing affect expected values and should be documented.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-027
    fact(
        'ccma-clinical-care',
        'The provider orders subcutaneous insulin from a high-alert medication drawer. Which practice aligns with medication safety policy?',
        'An independent double check of the order, label, dose, and syringe marking before administration',
        [
            'Draw the dose from memory while rushing between rooms',
            'Store insulin vials unlabeled beside saline flushes in the same bin',
            'Skip label verification when the cap color matches the prior patient',
        ],
        'High-alert medications such as insulin have narrow therapeutic windows. Independent double checks catch decimal and look-alike vial errors before injection.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-028
    fact(
        'ccma-clinical-care',
        'A patient wears a Holter monitor at home for intermittent palpitations. What does this device primarily record?',
        'Continuous ambulatory electrocardiogram activity over 24 to 48 hours',
        [
            'Intraocular pressure trends during sleep',
            'Throat culture growth on agar plates',
            'Permanent replacement of all inpatient telemetry units',
        ],
        'Holter monitoring captures rhythm changes that may not appear during a brief office ECG. It supplements, rather than replaces, inpatient telemetry when symptoms occur away from the hospital.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-029
    fact(
        'ccma-clinical-care',
        'A medical assistant almost administers the wrong oral antibiotic but catches the error before the patient swallows the tablet. What is the appropriate next step?',
        'Document and report the near-miss through the facility safety process',
        [
            'Say nothing because no harm occurred',
            'Discuss the event only in the break room without a record',
            'Hide the incident to avoid disciplinary action',
        ],
        'Near-miss reporting helps teams fix labeling, storage, and workflow problems before a patient is harmed. Most policies use nonpunitive channels for honest safety reporting.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-030
    fact(
        'ccma-clinical-care',
        'In the waiting area a patient suddenly has facial droop and slurred speech. What should the medical assistant do first?',
        'Activate the emergency response plan and ensure rapid evaluation and transport',
        [
            'Schedule a routine follow-up visit next week',
            'Check only capillary blood glucose and send the patient home',
            'Delay notification until imaging can be arranged next month',
        ],
        'Suspected stroke is time-critical; rapid EMS activation and evaluation improve eligibility for reperfusion therapy. Delaying care for a future appointment risks permanent disability.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-031
    fact(
        'ccma-clinical-care',
        'A nonfasting patient’s urine dipstick shows 2+ protein at point of care. What should the medical assistant do with the result?',
        'Document the finding and notify the clinical team per protocol',
        [
            'Ignore the result because yellow urine is always normal',
            'Discard the strip without charting to avoid alarming the patient',
            'Assume a false positive and withhold the information from the provider',
        ],
        'Proteinuria on dipstick may reflect kidney disease, infection, or other conditions requiring clinical follow-up. Abnormal point-of-care results are communicated and acted on per policy.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-032
    fact(
        'ccma-clinical-care',
        'When selecting an adult blood pressure cuff, the inflatable bladder width should be about what proportion of the upper arm circumference?',
        'Approximately 40% of the upper arm circumference',
        [
            'About 10% of the arm circumference',
            'Equal to the patient’s wrist width only',
            'Roughly 80% of the thigh length',
        ],
        'Undersized cuffs tend to read falsely high and oversized cuffs falsely low. Width near 40% of arm circumference is the usual standard for adult arm cuffs.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-033
    fact(
        'ccma-clinical-care',
        'While coaching a postoperative patient to use an incentive spirometer, which breathing pattern should the medical assistant encourage?',
        'Slow, deep inhalation through the mouthpiece followed by a brief hold if ordered',
        [
            'Indefinite breath holding without exhaling',
            'Rapid shallow panting until the patient feels dizzy',
            'Only quick sniffing breaths without lung expansion',
        ],
        'Deep inspiration expands alveoli and helps prevent atelectasis after surgery. Coaching focuses on controlled deep breaths rather than hyperventilation or breath holding alone.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-034
    fact(
        'ccma-clinical-care',
        'Two medication vials look alike and have similar names on the shelf. Which strategy reduces look-alike sound-alike (LASA) errors?',
        'Use tall-man lettering on labels and perform extra verification against the order',
        [
            'Store all vials without labels to speed retrieval',
            'Identify drugs by cap color alone without reading the label',
            'Skip the second patient identifier when the names sound similar',
        ],
        'LASA pairs such as hydroXYZINE and hydrALAZINE require deliberate label reading and separation strategies. Tall-man lettering highlights spelling differences during verification.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-035
    fact(
        'ccma-clinical-care',
        'A patient feels dizzy when standing after bed rest. Which vital sign series best evaluates orthostatic changes?',
        'Blood pressure and heart rate measured lying, sitting, and standing with position documented',
        [
            'Temperature alone in each position without pulse or pressure',
            'Respiratory rate only after vigorous exercise',
            'Pain score recorded without changing position',
        ],
        'Orthostatic hypotension or tachycardia may signal hypovolemia or autonomic dysfunction. Comparing pressure and pulse across positions with documented timing supports accurate interpretation.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-036
    fact(
        'ccma-clinical-care',
        'A patient with asthma uses a peak flow meter at home. Which technique yields the most reliable expiratory airflow reading?',
        'Sit or stand upright, inhale fully, seal the lips around the mouthpiece, and blow out as hard and fast as possible',
        [
            'Lie flat and exhale gently without coaching',
            'Hold breath for one minute before a weak puff into the meter',
            'Measure only immediately after sprinting upstairs',
        ],
        'Peak expiratory flow reflects bronchospasm and supports asthma action plans. Maximal effort after full inspiration with a tight seal avoids falsely low values.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-037
    fact(
        'ccma-clinical-care',
        'During setup for a minor sterile procedure, when is strict sterile technique most essential for the medical assistant?',
        'Whenever hands or instruments contact the sterile field or invasive device pathways',
        [
            'While greeting patients at the front desk',
            'While printing the daily schedule at the workstation',
            'While filing insurance cards in the records room',
        ],
        'Sterile technique prevents introduction of pathogens into tissue or equipment that enters the body. Nonclinical tasks do not require maintenance of a sterile field.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-038
    fact(
        'ccma-clinical-care',
        'The provider asks the medical assistant to remove sutures from a well-healed linear incision with intact skin. Which approach is typical?',
        'Clean technique with hand hygiene and gloves per policy, assessing the site before removal',
        [
            'Remove knots without hand hygiene because the wound looks closed',
            'Don a full sterile gown for every superficial suture removal',
            'Use scissors that were not cleaned between patients without reporting concerns',
        ],
        'Healed external closures are often managed with clean procedure rather than full surgical sterility, though erythema or drainage requires provider evaluation before removal.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-039
    fact(
        'ccma-clinical-care',
        'When screening distance visual acuity with a Snellen chart, at what testing distance should the chart be placed?',
        '20 feet, or an optically equivalent setup per facility protocol',
        [
            'Five inches from the patient’s face for all ages',
            'One hundred meters regardless of chart calibration',
            "At arm's length only for every adult and child",
        ],
        'Standardized testing distance keeps acuity scores comparable across visits and clinicians. Equivalent mirror systems must be calibrated to the same effective distance.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-040
    fact(
        'ccma-clinical-care',
        'Before inflating a blood pressure cuff on an adult upper arm, how should the bladder length relate to arm circumference?',
        'The bladder should encircle at least about 80% of the arm circumference',
        [
            'About 40% encirclement is sufficient for all adults',
            'Only the wrist width needs to be covered',
            'The bladder must overlap itself completely around the arm',
        ],
        'Cuff length that wraps most of the arm prevents leakage and artifact. Together with proper bladder width, adequate encirclement reduces falsely elevated or depressed readings.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-041
    fact(
        'ccma-clinical-care',
        'After applying an elastic compression wrap for peripheral edema, what should the medical assistant assess on the distal extremity?',
        'Circulation, sensation, and warmth in toes or fingers',
        [
            'Wrap as tightly as possible without any distal check',
            'Leave digits pale and cold without notifying the provider',
            'Reuse the same soiled wrap on the next patient',
        ],
        'Excessive compression can compromise neurovascular status. Distal color, capillary refill, sensation, and warmth are checked after application and during wear per policy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-042
    fact(
        'ccma-clinical-care',
        'While scrubbed in to assist with a sterile procedure, how should the medical assistant move supplies to the provider?',
        'Stay within the sterile zone and never reach over or lean on the sterile field',
        [
            'Rest both elbows on the sterile drape for stability',
            'Pass nonsterile packaging directly over open instruments',
            'Adjust a loose mask with bare hands after scrub without regloving',
        ],
        'Only sterile surfaces and items may contact the field. Reaching over or resting on the drape contaminates instruments and breaks the sterile barrier.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-043
    fact(
        'ccma-clinical-care',
        'During a routine dressing change on a closed surgical wound with no anticipated fluid exposure, which glove choice is usually appropriate?',
        'Nonsterile examination gloves when only intact skin and clean dressings will be touched',
        [
            'Sterile surgical gloves required for every superficial dressing change',
            'No gloves because the incision looks healed',
            'The same gloves worn during a prior patient’s wound care',
        ],
        'Glove selection matches anticipated contact with blood, body fluids, or sterile tissue. Clean closed wounds often require only clean technique with nonsterile gloves per policy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-044
    fact(
        'ccma-clinical-care',
        'When teaching clean-catch midstream urine collection, what patient steps reduce contamination of the specimen?',
        'Perform hand hygiene, cleanse the urinary meatus, void the first portion into the toilet, then collect midstream in the container',
        [
            'Capture only the first few drops in the cup without cleansing',
            'Store urine in the same container at home for several days',
            'Skip perineal cleansing to save time',
        ],
        'Discarding the initial stream and using midstream urine lowers bacterial contamination from the urethra. Proper labeling and timely delivery to the laboratory follow facility protocol.',
        [S.NHA_CCMA],
        'advanced',
    ),

    # ccma-clinical-care-045
    fact(
        'ccma-clinical-care',
        'Before measuring an adult\'s blood pressure, what should the medical assistant confirm?',
        'The patient has rested with the back supported and feet flat for several minutes',
        ['The cuff is placed over clothing for warmth',
        'The patient is talking continuously during inflation',
        'The arm is held above head level throughout the reading'],
        'Rest and proper arm position stabilize readings. A cuff over thick clothing or active talking can falsely elevate results.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-046
    fact(
        'ccma-clinical-care',
        'Which site is commonly used for an intramuscular injection in an adult with adequate deltoid mass?',
        'Upper outer third of the deltoid muscle',
        ['Midline of the anterior thigh near the knee',
        'Over the sternum',
        'Plantar surface of the foot'],
        'CDC vaccine administration guidance places adult deltoid IM injections in the thick lateral shoulder. The vastus lateralis is preferred for many infants, not the sternum or foot.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-047
    fact(
        'ccma-clinical-care',
        'A patient scheduled for fasting blood work ate breakfast an hour ago. What is the appropriate action?',
        'Notify the provider and reschedule or follow lab protocol for the ordered test',
        ['Draw the sample and label it random without telling anyone',
        'Have the patient drink sugary soda before the draw',
        'Cancel the order permanently without documentation'],
        'Fasting requirements depend on the ordered analyte. Proceeding without notifying the team can yield misleading glucose or lipid results.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-048
    fact(
        'ccma-clinical-care',
        'During a sterile dressing change, the assistant accidentally touches the inner sterile pad. What should happen next?',
        'Discard the contaminated item and replace it using sterile technique',
        ['Continue because the patient looks clean',
        'Fold the pad so the touched side faces the wound',
        'Rinse the pad under tap water and reuse it'],
        'Sterility is event-based; contact with nonsterile surfaces requires replacement. Rinsing does not restore sterility for invasive wound care.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-049
    fact(
        'ccma-clinical-care',
        'When preparing a patient for a 12-lead EKG, why is hair clipped instead of shaved with a razor when needed?',
        'Clipping reduces skin abrasion that can irritate the site before electrode placement',
        ['Razor shaving improves ST segment accuracy on every patient',
        'Hair removal is unnecessary for any electrode',
        'Lotion should be applied under each pad'],
        'Gentle clipping improves contact without micro-cuts that sting or weep. Razors are reserved for orders because they can irritate skin and affect tracing quality.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-050
    fact(
        'ccma-clinical-care',
        'What is the correct order for donning personal protective equipment when both gown and gloves are required?',
        'Gown first, then mask or respirator, eye protection, then gloves',
        ['Gloves first, then gown over the gloves',
        'Eye protection after removing all other PPE',
        'Gown last so it stays outside the gloves'],
        'CDC donning sequences keep glove cuffs overlapping the gown at the wrist. Gloves first tears the gown when removing equipment.',
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-051
    fact(
        'ccma-clinical-care',
        'A point-of-care glucose meter displays an error after a new test strip is inserted. What should the medical assistant do?',
        'Repeat quality control per manufacturer instructions before patient testing',
        ['Use the reading because the strip looks new',
        'Share strips between patients to save supplies',
        'Calibrate by wiping the strip with alcohol'],
        'CLIA-waived devices still require control checks when errors occur. Patient strips are single use; alcohol can damage strip chemistry.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-052
    fact(
        'ccma-clinical-care',
        'Which action supports accurate pediatric weight measurement in an outpatient setting?',
        'Use a calibrated scale appropriate for the child\'s age and remove heavy outer clothing',
        ['Weigh the child while holding them without subtracting adult weight',
        'Place the scale on a thick carpet pad',
        'Estimate weight from shoe size'],
        'Pediatric dosing and growth charts depend on accurate weight. Holding the child without taring adds adult mass; carpet throws off load cells.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-053
    fact(
        'ccma-clinical-care',
        'What patient position is standard for measuring adult blood pressure at the upper arm?',
        'Seated with back supported, feet flat, and arm at heart level',
        ['Standing on one foot with arm raised overhead',
        'Prone with cuff on the ankle',
        'Supine with legs dangling off the exam table'],
        'Heart-level arm placement and supported seating align with guideline technique. Ankle cuffs in prone adults are not the routine upper-arm method.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-054
    fact(
        'ccma-clinical-care',
        'A patient feels faint during venipuncture. What should the medical assistant do first?',
        'Stop the procedure and lower the patient safely to prevent injury',
        ['Tighten the tourniquet to finish quickly',
        'Leave the patient alone to recover privacy',
        'Continue drawing while the patient stands'],
        'Vasovagal reactions require stopping the draw and protecting from falls. Completing the tube risks syncope and injury.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-055
    fact(
        'ccma-clinical-care',
        'During a minor in-office procedure, the assistant notices the sterile field was touched by a nonsterile sleeve. What is correct?',
        'Set up a new sterile field before continuing',
        ['Turn the drape so the wet side faces up',
        'Blow on instruments to dry them',
        'Proceed because the patient is cooperative'],
        'Sterility is lost once nonsterile items contact the field. Drying or flipping drapes does not restore asepsis.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-056
    fact(
        'ccma-clinical-care',
        'What is the purpose of peak expiratory flow measurement in asthma care?',
        'Monitor bronchospasm and response to therapy over time',
        ['Diagnose diabetes from a fingerstick',
        'Measure blood pressure in the ankle',
        'Assess visual acuity'],
        'Peak flow reflects expiratory obstruction trends. Glucose, pressure, and vision use other devices and indications.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-057
    fact(
        'ccma-clinical-care',
        'When performing a snellen vision screening, how far is the chart typically placed?',
        '20 feet or equivalent simulated distance',
        ['6 inches from the nose',
        'Across the parking lot without calibration',
        'Behind the patient'],
        'Standardized distance keeps letter size comparable to the 20/20 notation. Uncalibrated distances invalidate results.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-058
    fact(
        'ccma-clinical-care',
        'A provider orders a urine pregnancy test on a random cup collected without label. What should the assistant do?',
        'Reject the specimen and recollect after two-identifier labeling',
        ['Run the test anonymously',
        'Use another patient\'s label to save time',
        'Dilute the sample with water'],
        'Mislabeled specimens risk wrong-patient results with major consequences. Dilution alters analyte concentration.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-059
    fact(
        'ccma-clinical-care',
        'Which technique helps prevent specimen hemolysis during capillary blood collection?',
        'Allow a free-flowing drop to form without excessive squeezing',
        ['Milk the fingertip vigorously many times',
        'Reuse the lancet on the next patient',
        'Wipe alcohol and test while skin is dripping wet'],
        'Aggressive squeezing lyses cells, raising potassium falsely. Single-use lancets and dry sites protect sample integrity.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-060
    fact(
        'ccma-clinical-care',
        'When obtaining orthostatic vital signs, how many positions are typically compared?',
        'Supine, sitting, and standing',
        ['Standing once without baseline',
        'Prone underwater',
        'Trendelenburg for one hour'],
        'Orthostatic series detect postural blood pressure and pulse changes. A single standing reading without baseline lacks comparison.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-061
    fact(
        'ccma-clinical-care',
        'What is the correct angle for an intradermal injection such as a tuberculin skin test?',
        '5 to 15 degrees with bevel up',
        ['90 degrees into muscle',
        '45 degrees into subcutaneous fat of the abdomen',
        '180 degrees flat across bone'],
        'Intradermal tests form a bleb in the dermis. Ninety-degree angles are for typical IM vaccines, not Mantoux placement.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-062
    fact(
        'ccma-clinical-care',
        'Before assisting with suture removal, what assessment should occur?',
        'Inspect the wound for healing, drainage, and signs of infection',
        ['Pull every suture quickly without looking',
        'Soak the wound in hot coffee',
        'Reuse instruments from another patient without processing'],
        'Providers evaluate readiness for suture removal. Infection or dehiscence requires different management than routine removal.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-063
    fact(
        'ccma-clinical-care',
        'When applying a heat pack, why is a cloth barrier placed between the pack and skin?',
        'To reduce risk of thermal burns',
        ['To keep the pack cold longer',
        'To measure blood glucose',
        'To sterilize the pack'],
        'Thermal injuries occur quickly on sensitive or neuropathic skin. Barriers distribute temperature more safely.',
        [S.NHA_CCMA],
        'beginner',
    ),
]
