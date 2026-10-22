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
        'Before applying a topical antibiotic to an open wound in the clinic, what is the first action the medical assistant should take?',
        'Perform hand hygiene before touching the wound or medication supplies',
        [
            'Don clean gloves before performing hand hygiene for the dressing change',
            'Remove the soiled dressing and cleanse the wound before hand hygiene',
            'Apply topical antibiotic from the tube opening to the wound, then wash hands',
        ],
        'Hand hygiene is the first step before wound contact or handling topical agents. Gloves, wound cleansing, and ointment application follow once hands and the field are prepared per policy.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-002
    fact(
        'ccma-clinical-care',
        'When performing a capillary blood glucose check at the point of care, which supply practice reduces cross-contamination risk?',
        'Use a new lancet and an in-date test strip for each puncture',
        [
            'Wipe the lancet with alcohol and reuse it for the next patient in the session',
            'Use strips from a vial past expiration when the desiccant still looks intact',
            'Puncture the same fingertip repeatedly for serial checks without rotating sites',
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
            'Eat a light breakfast of toast and juice before the draw',
            'Withhold all fluids including water for 24 hours unless the order says otherwise',
            'Take morning diabetes medication with a small meal if the patient feels hungry',
        ],
        'Fasting requirements depend on the specific tests ordered, and a light breakfast or extra medication can invalidate results. Patients should follow the written order and ask the care team when instructions are unclear.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-004
    fact(
        'ccma-clinical-care',
        'Dense hair covers the skin where ECG electrodes will be placed. How should the medical assistant prepare the sites?',
        'Clip the hair close to the skin and shave only on provider order',
        [
            'Shave every electrode site with a razor before each routine 12-lead tracing',
            'Press electrodes through uncut hair when clipping would add extra setup time',
            'Apply conductive gel over thick hair instead of clipping or shaving the sites',
        ],
        'Good skin contact reduces artifact and improves tracing quality. Routine razor shaving can nick skin and is reserved for orders, whereas clipping is often sufficient.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-005
    fact(
        'ccma-clinical-care',
        'After changing a soiled wound dressing, how should the medical assistant dispose of the contaminated materials?',
        'Place them in the designated biohazard or regulated medical waste container',
        [
            'Discard them in regular waste after sealing them in a plastic liner bag',
            'Leave them at the bedside for housekeeping to sort without a biohazard label',
            'Return unused gauze from the dressing to the clean supply drawer for later use',
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
            'Finish rooming the next scheduled patient before alerting the clinical team',
            'Offer water and have the patient walk to the waiting area for fresh air',
            'Document the complaint at the end of clinic when symptoms may have settled',
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
            'Zero the clinic scale on thick carpet padding for patient comfort',
            'Use an uncertified home scale when the clinic scale is occupied',
            'Weigh the patient with shoes and a heavy coat to avoid undressing',
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
            'Keep the patient seated upright without lowering the head or calling for help',
            'Offer solid food by mouth while the patient is unresponsive',
            'Leave the procedure room to finish charting before assisting',
        ],
        'Syncope requires airway and circulation assessment and prevention of injury from falling. Oral intake is unsafe until the patient is fully alert and swallowing normally.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-009
    fact(
        'ccma-clinical-care',
        "When applying a cold pack for a localized injury, how should the medical assistant protect the patient's skin?",
        'Place a cloth barrier between the skin and the cold source',
        [
            'Apply ice directly to intact skin for the full ordered time',
            'Leave the pack in place after the patient reports numbness',
            'Rotate the same frozen gel pack between patients after wiping the plastic cover',
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
            'Leave the torso and hips uncovered until the speculum is inserted',
        ],
        'Modesty and thermal comfort reduce anxiety and support cooperation during sensitive exams. Conversations should stay clinical and at a respectful volume.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-011
    fact(
        'ccma-clinical-care',
        'During a visual acuity screening in clinic, how should a patient who normally wears glasses or contacts be tested?',
        'Use the usual corrective lenses unless the provider says otherwise',
        [
            'Test uncorrected vision for every line even when the patient wears daily lenses',
            'Cover both eyes together for the chart instead of alternating',
            'Use whichever wall chart is open at an unmeasured distance',
        ],
        'Screening should reflect how the patient sees day to day unless a specific protocol calls for uncorrected vision. Standardized distance and eye sequencing follow facility policy.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-012
    fact(
        'ccma-clinical-care',
        'Compared with a standard 12-lead electrocardiogram, adding posterior leads in a 15-lead study may improve detection of what?',
        'Posterior wall myocardial ischemia on the back of the heart',
        [
            'Right ventricular strain pattern from acute pulmonary embolism',
            'Anterior ST-segment elevation from left anterior descending occlusion',
            'Bundle branch block widening the QRS without posterior involvement',
        ],
        'Posterior ST changes can be subtle on a standard 12-lead tracing. Extra posterior leads increase sensitivity for occult ischemia behind the heart.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-013
    fact(
        'ccma-clinical-care',
        'While measuring vital signs, the medical assistant hears new expiratory wheezing in a patient with no prior documentation of wheezes. What action is appropriate?',
        'Promptly report the finding to the clinical team',
        [
            "Document wheezing at the next visit if the sound persists during rooming",
            "Note the finding in a personal notebook and mention it casually later",
            "Double the patient's rescue inhaler doses without notifying the provider",
        ],
        'New wheezing may reflect bronchospasm, aspiration, or another acute process. Timely communication allows the provider to examine the patient and adjust treatment.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-014
    fact(
        'ccma-clinical-care',
        'Why do clinical guidelines recommend routine foot examination for patients with diabetes?',
        'To identify ulcers, deformities, or loss of sensation early',
        [
            'To defer dilated eye screening when the feet appear normal on exam',
            'To reduce the need for home glucose logs when neuropathy is absent',
            'To omit footwear counseling once pedal pulses are palpable bilaterally',
        ],
        'Peripheral neuropathy and poor healing put diabetic feet at high risk for limb-threatening infection. Foot checks complement, rather than replace, glucose control and eye care.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-015
    fact(
        'ccma-clinical-care',
        'Once a sterile field is opened for a procedure, how should the medical assistant maintain it?',
        'Keep the field in view and free of contact with non-sterile items',
        [
            'Cover unused instruments with a nonsterile towel until the provider returns',
            'Reach across the field with gloved hands to reposition the overhead light',
            'Leave remaining sterile supplies on the open field for the next case today',
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
            'About three minutes while changing tube holders between difficult attempts',
            'Until every ordered tube is filled before releasing venous congestion',
            'Until clotting at the puncture site is visible through the skin',
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
            'Chronic muscle spasm when moist heat is part of the prescribed plan',
            'Healed linear scars when contrast therapy is ordered for rehabilitation',
            'Stiff arthritic joints when the provider recommends scheduled warm packs',
        ],
        'Heat increases blood flow and can worsen acute inflammation or burn insensate skin. Ordered heat for chronic spasm or stiffness is appropriate when the skin is intact and sensate.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-018
    fact(
        'ccma-clinical-care',
        'When assisting a provider with suture removal, which practice aligns with safe clinical care?',
        'Use hand hygiene and sterile or clean technique for the wound',
        [
            'Remove knots with the same gloves worn during the prior patient rooming',
            'Use nonsterile shears on purulent drainage without notifying the provider',
            'Clip every suture when one segment is erythematous without reporting it',
        ],
        'Even closed wounds can harbor bacteria at suture lines. Hand hygiene, appropriate gloves, and reporting erythema or drainage help prevent secondary infection.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-019
    fact(
        'ccma-clinical-care',
        'Immediately before starting a sterile procedure, what should the medical assistant confirm about the patient?',
        'Two patient identifiers plus informed consent when required',
        [
            "Printed full name on the schedule without verifying date of birth",
            "Wristband match to the room number posted on the hallway board",
            "Verbal consent from the patient's companion without reviewing the chart",
        ],
        'Wrong-patient procedures are preventable with two-identifier checks and documented consent. Room numbers and glove preferences do not verify who is receiving invasive care.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-020
    fact(
        'ccma-clinical-care',
        'Before the first venipuncture attempt, which verification step reduces wrong-patient laboratory errors?',
        'Match the patient to the order using two approved identifiers',
        [
            'Match the patient using the room number on the hallway board by itself',
            'Accept the insurance card alone as proof of identity',
            'Use the scheduled appointment start time as the sole identifier',
        ],
        'Laboratory specimens labeled for the wrong person can lead to harmful treatment decisions. Name and date of birth (or other approved pair) must match the requisition.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-021
    fact(
        'ccma-clinical-care',
        'Before giving a provider-ordered injection, which checks reflect medication safety standards?',
        'Correct patient, medication, dose, route, time, and documentation',
        [
            "Vial cap color matched to the prior patient's medication",
            "Room number on the door aligned with the scheduled appointment slot",
            "Pharmacy label compared to an outdated faxed order without the current order",
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
            'Complete rooming paperwork while the provider closes the incision alone',
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
            'Finish filling the current tube before lowering the patient or calling for help',
            'Loosen then retighten the tourniquet to complete the draw more quickly',
            'Step out to find staff while the patient sits with the needle in place',
        ],
        'Vasovagal syncope during phlebotomy is common and can cause falls. Stopping the draw, lowering the head if tolerated, and calling for assistance follow standard reaction protocols.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-024
    fact(
        'ccma-clinical-care',
        'When irrigating a wound under provider direction, which supply choice supports aseptic technique?',
        'Sterile irrigant poured without touching the spout to the field',
        [
            '0.9% saline drawn from a multi-dose vial opened earlier the same day',
            'Antiseptic wound cleanser used as the irrigating fluid per label',
            'Sterile water remaining in a bowl that sat open on the mayo stand for an hour',
        ],
        'Irrigation requires fluid and delivery that stay uncontaminated. Multi-dose vials and open bowls increase bioburden; antiseptics clean skin but are not routine primary irrigants for deep tissue flushing.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-025
    fact(
        'ccma-clinical-care',
        'When applying an elastic compression wrap for peripheral edema, in which direction should the bandage be wrapped?',
        'From distal to proximal with smooth, overlapping layers',
        [
            'From proximal to distal to anchor the bandage at the thigh or hip',
            'With maximal stretch on each turn to eliminate edema in a single layer',
            'Directly over open draining wounds without a primary absorbent dressing',
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
            'As normal because a single 98.6°F value defines health for every adult',
            'As hypothermia requiring immediate ice immersion',
            'As fever when the oral reading stays below 101°F on repeat checks',
        ],
        'Individual baselines vary, but oral temperatures above 100.4°F are widely treated as fever in adults. Measurement site and timing affect expected values and should be documented.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-027
    fact(
        'ccma-clinical-care',
        'The provider orders subcutaneous insulin from a high-alert medication drawer. Which practice aligns with medication safety policy?',
        'An independent double check of the order, label, and dose',
        [
            'Draw the dose from memory while moving quickly between rooms',
            'Store insulin vials unlabeled beside saline flushes in the same bin',
            'Verify cap color against the prior patient without reading the vial label',
        ],
        'High-alert medications such as insulin have narrow therapeutic windows. Independent double checks catch decimal and look-alike vial errors before injection.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-028
    fact(
        'ccma-clinical-care',
        'A patient wears a Holter monitor at home for intermittent palpitations. What does this device primarily record?',
        'Continuous ambulatory ECG activity over 24 to 48 hours',
        [
            'Continuous ambulatory blood pressure trends over 24 hours',
            'Symptom-triggered event recorder rhythm during palpitations',
            'Resting transthoracic echocardiography wall motion assessment',
        ],
        'Holter monitoring captures rhythm changes that may not appear during a brief office ECG. It supplements, rather than replaces, inpatient telemetry when symptoms occur away from the hospital.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-029
    fact(
        'ccma-clinical-care',
        'A medical assistant almost administers the wrong oral antibiotic but catches the error before the patient swallows the tablet. What is the appropriate next step?',
        'Document and report the near-miss through the facility safety process',
        [
            'Say nothing because no harm occurred',
            'Record the near-miss in a personal note without filing a safety report',
            'Correct the error silently and discard the mismatched vial',
        ],
        'Near-miss reporting helps teams fix labeling, storage, and workflow problems before a patient is harmed. Most policies use nonpunitive channels for honest safety reporting.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-030
    fact(
        'ccma-clinical-care',
        'In the waiting area a patient suddenly has facial droop and slurred speech. What should the medical assistant do first?',
        'Activate the emergency response plan and ensure rapid evaluation and transport',
        [
            'Schedule a routine follow-up visit in one week for reassessment',
            'Check capillary blood glucose and discharge without notifying the clinical team',
            'Wait for outpatient brain MRI scheduling before alerting the provider',
        ],
        'Suspected stroke is time-critical; rapid EMS activation and evaluation improve eligibility for reperfusion therapy. Delaying care for a future appointment risks permanent disability.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-031
    fact(
        'ccma-clinical-care',
        'A nonfasting patient’s urine dipstick shows 2+ protein at point of care. What should the medical assistant do with the result?',
        'Document the finding and notify the clinical team',
        [
            'Ignore the result because concentrated yellow urine is expected in every sample',
            'Discard the strip without charting to avoid alarming the patient',
            'Assume a false positive and withhold the information from the provider',
        ],
        'Proteinuria on dipstick may reflect kidney disease, infection, or other conditions requiring clinical follow-up. Abnormal point-of-care results are communicated and acted on per policy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-032
    fact(
        'ccma-clinical-care',
        'When selecting an adult blood pressure cuff, the inflatable bladder width should be about what proportion of the upper arm circumference?',
        'Approximately 40% of the upper arm circumference',
        [
            'About 10% of the arm circumference',
            'Sized to the patient’s wrist width for every adult arm measurement',
            'Roughly 80% of the thigh length',
        ],
        'Undersized cuffs tend to read falsely high and oversized cuffs falsely low. Width near 40% of arm circumference is the usual standard for adult arm cuffs.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-033
    fact(
        'ccma-clinical-care',
        'While coaching a postoperative patient to use an incentive spirometer, which breathing pattern should the medical assistant encourage?',
        'Slow, deep inhalation through the mouthpiece and a brief hold',
        [
            'Indefinite breath holding without exhaling',
            'Rapid shallow panting until the patient feels dizzy',
            'Quick sniffing breaths through the nose without deep lung expansion',
        ],
        'Deep inspiration expands alveoli and helps prevent atelectasis after surgery. Coaching focuses on controlled deep breaths rather than hyperventilation or breath holding alone.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-034
    fact(
        'ccma-clinical-care',
        'Two medication vials look alike and have similar names on the shelf. Which strategy reduces look-alike sound-alike (LASA) errors?',
        'Use tall-man lettering on labels and verify against the order',
        [
            'Store all vials without labels to speed retrieval',
            'Identify drugs by cap color alone without reading the label',
            'Omit the second patient identifier when the drug names sound similar',
        ],
        'LASA pairs such as hydroXYZINE and hydrALAZINE require deliberate label reading and separation strategies. Tall-man lettering highlights spelling differences during verification.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-035
    fact(
        'ccma-clinical-care',
        'A patient feels dizzy when standing after bed rest. Which vital sign series best evaluates orthostatic changes?',
        'Blood pressure and heart rate taken lying, sitting, and standing',
        [
            'Temperature alone in each position without pulse or pressure readings',
            'Respiratory rate after vigorous exercise in the hallway',
            'Pain score recorded without changing position',
        ],
        'Orthostatic hypotension or tachycardia may signal hypovolemia or autonomic dysfunction. Comparing pressure and pulse across positions with documented timing supports accurate interpretation.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-036
    fact(
        'ccma-clinical-care',
        'A patient with asthma uses a peak flow meter at home. Which technique yields the most reliable expiratory airflow reading?',
        'Sit upright, inhale fully, seal the lips, and blow out hard and fast',
        [
            'Lie flat and exhale gently without coaching',
            'Hold breath for one minute before a weak puff into the meter',
            'Record a single weak puff without a full inhalation or tight lip seal',
        ],
        'Peak expiratory flow reflects bronchospasm and supports asthma action plans. Maximal effort after full inspiration with a tight seal avoids falsely low values.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-037
    fact(
        'ccma-clinical-care',
        'During setup for a minor sterile procedure, when is strict sterile technique most essential for the medical assistant?',
        'Whenever hands or instruments contact the sterile field',
        [
            'While documenting vital signs on a patient with intact skin',
            'While applying an adhesive bandage to a closed abrasion',
            'While preparing a clean injection site for an intramuscular vaccine',
        ],
        'Sterile technique prevents introduction of pathogens into tissue or equipment that enters the body. Nonclinical tasks do not require maintenance of a sterile field.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-038
    fact(
        'ccma-clinical-care',
        'The provider asks the medical assistant to remove sutures from a well-healed linear incision with intact skin. Which approach is typical?',
        'Clean technique with hand hygiene and gloves, assessing the site first',
        [
            'Remove knots with bare hands because the epidermis appears fully closed',
            'Don a full sterile gown and gloves for every superficial suture removal',
            'Use the same scissors from another tray after wiping the blades with dry gauze',
        ],
        'Healed external closures are often managed with clean procedure rather than full surgical sterility. Erythema, drainage, or a separating wound requires provider evaluation before the sutures are removed.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-039
    fact(
        'ccma-clinical-care',
        'When screening distance visual acuity with a Snellen chart, at what testing distance should the chart be placed?',
        'Twenty feet, or an optically equivalent testing setup',
        [
            "Five inches from the patient's face for all ages",
            "One hundred meters regardless of chart calibration",
            "At bedside arm's length without a calibrated mirror system",
        ],
        'Standardized testing distance keeps acuity scores comparable across visits and clinicians. Equivalent mirror systems must be calibrated to the same effective distance.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-040
    fact(
        'ccma-clinical-care',
        'Before inflating a blood pressure cuff on an adult upper arm, how should the bladder length relate to arm circumference?',
        'The bladder should encircle about 80 percent of the arm',
        [
            'About 40% encirclement is sufficient for all adults',
            'Coverage based on wrist width for typical adult arms',
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
            'Distal capillary refill without checking sensation or warmth',
            'Proximal skin temperature while ignoring toe color and movement',
            'Wrap tension at the ankle without assessing distal pulses',
        ],
        'Excessive compression can compromise neurovascular status. Distal color, capillary refill, sensation, and warmth are checked after application and during wear per policy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-042
    fact(
        'ccma-clinical-care',
        'While scrubbed in to assist with a sterile procedure, how should the medical assistant move supplies to the provider?',
        'Stay within the sterile zone and avoid reaching over the field',
        [
            'Rest both forearms on the sterile drape while handing instruments',
            'Pass nonsterile outer packaging directly over open sterile instruments',
            'Adjust a loose mask with bare scrubbed hands without regloving afterward',
        ],
        'Only sterile surfaces and items may contact the field. Reaching over or resting on the drape contaminates instruments and breaks the sterile barrier.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-043
    fact(
        'ccma-clinical-care',
        'During a routine dressing change on a closed surgical wound with no anticipated fluid exposure, which glove choice is usually appropriate?',
        'Nonsterile gloves when clean dressings touch intact skin',
        [
            "Sterile surgical gloves for every superficial dressing change",
            "No gloves because the incision looks dry and fully epithelialized",
            "The same examination gloves worn during the prior patient's rooming",
        ],
        'Glove selection matches anticipated contact with blood, body fluids, or sterile tissue. Clean closed wounds often require only clean technique with nonsterile gloves per policy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-clinical-care-044
    fact(
        'ccma-clinical-care',
        'When teaching clean-catch midstream urine collection, what patient steps reduce contamination of the specimen?',
        'Cleanse the meatus, void first into the toilet, then collect midstream',
        [
            'Collect the first voided stream in the cup without perineal cleansing',
            'Store urine in the same container at home for several days before delivery',
            'Defer perineal cleansing to shorten the collection teaching',
        ],
        'Discarding the initial stream and using midstream urine lowers bacterial contamination from the urethra. Proper labeling and timely delivery to the laboratory follow facility protocol.',
        [S.NHA_CCMA],
        'advanced',
    ),

    # ccma-clinical-care-045
    fact(
        'ccma-clinical-care',
        'Before measuring an adult\'s blood pressure, what should the medical assistant confirm?',
        'The patient has rested with the back supported and feet flat',
        [
            'The patient is seated with legs crossed and the back unsupported',
            'The cuff is placed over a thin shirt sleeve to keep the arm warm',
            'The arm hangs below heart level while the patient talks during inflation',
        ],
        'Rest and proper arm position stabilize readings. A cuff over thick clothing or active talking can falsely elevate results.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-046
    fact(
        'ccma-clinical-care',
        'Which site is commonly used for an intramuscular injection in an adult with adequate deltoid mass?',
        'Upper outer third of the deltoid muscle in the adult',
        [
            'Middle third of the deltoid along the acromion edge in thin adults',
            'Vastus lateralis of the anterior thigh for routine adult influenza vaccine',
            'Dorsogluteal upper outer quadrant when deltoid mass is adequate',
        ],
        'CDC vaccine administration guidance places adult deltoid IM injections in the thick lateral shoulder. The vastus lateralis is preferred for many infants, not the sternum or foot.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-047
    fact(
        'ccma-clinical-care',
        'A patient scheduled for fasting blood work ate breakfast an hour ago. What is the appropriate action?',
        'Notify the provider and reschedule or follow lab protocol for the ordered test',
        [
            'Draw the sample and note nonfasting in small text without provider notification',
            'Tell the patient to go without lunch and proceed with the draw',
            'Discard the requisition and tell the patient to return later',
        ],
        'Fasting requirements depend on the ordered analyte. Proceeding without notifying the team can yield misleading glucose or lipid results.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-048
    fact(
        'ccma-clinical-care',
        'During a sterile dressing change, the assistant accidentally touches the inner sterile pad. What should happen next?',
        'Discard the contaminated pad and replace it with sterile technique',
        [
            'Continue the dressing change if the outer wrapper still looks clean',
            'Fold the pad so the contaminated side faces the wound',
            'Wipe the pad with alcohol and reuse it on the wound bed',
        ],
        'Sterility is event-based; contact with nonsterile surfaces requires replacement. Rinsing does not restore sterility for invasive wound care.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-049
    fact(
        'ccma-clinical-care',
        'When preparing a patient for a 12-lead EKG, why is hair clipped instead of shaved with a razor when needed?',
        'Clipping reduces skin abrasion before the electrode is placed',
        [
            'Razor shaving every electrode site improves ST-segment accuracy on all patients',
            'Hair may be left intact when the tracing quality looks acceptable',
            'Conductive lotion should be applied under each pad instead of trimming',
        ],
        'Gentle clipping improves contact without micro-cuts that sting or weep. Razors are reserved for orders because they can irritate skin and affect tracing quality.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-050
    fact(
        'ccma-clinical-care',
        'What is the correct order for donning personal protective equipment when both gown and gloves are required?',
        'Gown first, then mask or respirator, eye protection, then gloves',
        [
            'Gloves first, then pull the gown on over the glove cuffs',
            'Eye protection before the gown when minimal splash risk is expected',
            'Gown last so the sleeves remain outside the glove cuffs',
        ],
        'CDC donning sequences keep glove cuffs overlapping the gown at the wrist. Gloves first tears the gown when removing equipment.',
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-051
    fact(
        'ccma-clinical-care',
        'A point-of-care glucose meter displays an error after a new test strip is inserted. What should the medical assistant do?',
        'Repeat quality control before testing the patient',
        [
            "Repeat patient testing with another strip from the same lot",
            "Wipe the meter sensor with alcohol and proceed while the error code remains",
            "Use a strip from another patient's opened vial to complete the ordered check",
        ],
        'CLIA-waived devices still require control checks when errors occur. Patient strips are single use; alcohol can damage strip chemistry.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-052
    fact(
        'ccma-clinical-care',
        'When weighing a child in outpatient clinic, which practice supports the most accurate measurement?',
        "Use a calibrated scale for the child's age and remove outer clothing",
        [
            'Weigh the child while holding them without subtracting the adult weight',
            'Place the scale on a thick carpet pad',
            'Estimate weight from height percentile on the growth chart',
        ],
        'Pediatric dosing and growth charts depend on accurate weight. Holding the child without taring adds adult mass; carpet throws off load cells.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-053
    fact(
        'ccma-clinical-care',
        'For adult upper-arm blood pressure measurement, which patient position aligns with standard technique?',
        'Seated, feet flat, back supported, arm at heart level',
        [
            'Standing on one foot with the arm raised overhead at cuff level',
            'Prone with the blood pressure cuff on the ankle',
            'Supine with the legs dangling off the exam table',
        ],
        'Heart-level arm placement and supported seating align with guideline technique. Ankle cuffs in prone adults are not the routine upper-arm method.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-054
    fact(
        'ccma-clinical-care',
        'A patient feels faint during venipuncture. What should the medical assistant do first?',
        'Stop the procedure and lower the patient safely to prevent injury',
        [
            'Loosen the tourniquet and fill the last tube before addressing symptoms',
            'Ask the patient to stand and walk to the waiting area to improve circulation',
            'Continue the draw while paging staff from another floor for assistance',
        ],
        'Vasovagal reactions require stopping the draw and protecting from falls. Completing the tube risks syncope and injury.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-055
    fact(
        'ccma-clinical-care',
        'During a minor in-office procedure, the assistant notices the sterile field was touched by a nonsterile sleeve. What is correct?',
        'Set up a new sterile field before continuing',
        ['Turn the drape so the contaminated side faces the instruments',
        'Fan nonsterile air across open instruments to dry moisture',
        'Proceed after wiping the sleeve contact spot with nonsterile gauze'],
        'Sterility is lost once nonsterile items contact the field. Drying or flipping drapes does not restore asepsis.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-056
    fact(
        'ccma-clinical-care',
        'In asthma care, what does peak expiratory flow measurement primarily help clinicians monitor?',
        'Monitor bronchospasm and response to therapy over time',
        ['Track nocturnal oxygen saturation trends at home',
        'Quantify airway inflammation with fractional exhaled nitric oxide',
        'Measure inspiratory capacity during full pulmonary function testing'],
        'Peak flow reflects expiratory obstruction trends. Glucose, pressure, and vision use other devices and indications.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-057
    fact(
        'ccma-clinical-care',
        'When performing a snellen vision screening, how far is the chart typically placed?',
        '20 feet or equivalent simulated distance',
        ['Six inches from the nose at the bedside',
        'Twenty feet without verifying mirror or projector calibration',
        'At the doorway using a handheld card without standardized lighting'],
        'Standardized distance keeps letter size comparable to the 20/20 notation. Uncalibrated distances invalidate results.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-clinical-care-058
    fact(
        'ccma-clinical-care',
        'A provider orders a urine pregnancy test on a random cup collected without label. What should the assistant do?',
        'Reject the specimen and recollect after two-identifier labeling',
        [
            'Run the test on the unlabeled cup and add identifiers to the result afterward',
            'Label the cup with first name alone and run the test before full verification',
            'Add tap water to the specimen to reach the fill line on the container',
        ],
        'Mislabeled specimens risk wrong-patient results with major consequences. Dilution alters analyte concentration.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-059
    fact(
        'ccma-clinical-care',
        'Which technique helps prevent specimen hemolysis during capillary blood collection?',
        'Allow a free-flowing drop to form without excessive squeezing',
        [
            'Massage the puncture site firmly until a large drop appears on first squeeze',
            'Collect the sample while excess alcohol moisture still covers the fingertip',
            'Reuse the lancet on the next patient after wiping it with an alcohol pad',
        ],
        'Aggressive squeezing lyses cells, raising potassium falsely. Single-use lancets and dry sites protect sample integrity.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-060
    fact(
        'ccma-clinical-care',
        'When obtaining orthostatic vital signs, how many positions are typically compared?',
        'Supine, sitting, and standing positions',
        [
            'Supine and standing measurements without a sitting set',
            'Sitting and standing measurements without a supine baseline',
            'Supine, sitting, standing, then supine again in one continuous series',
        ],
        'Orthostatic series detect postural blood pressure and pulse changes. A single standing reading without baseline lacks comparison.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-061
    fact(
        'ccma-clinical-care',
        'What is the correct angle for an intradermal injection such as a tuberculin skin test?',
        '5 to 15 degrees with the bevel pointing up',
        [
            '90 degrees into deltoid muscle for Mantoux testing',
            '45 degrees into abdominal subcutaneous fat for tuberculin',
            'Intradermal injection pressed flat parallel to the skin surface',
        ],
        'Intradermal tests form a bleb in the dermis. Ninety-degree angles are for typical IM vaccines, not Mantoux placement.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-062
    fact(
        'ccma-clinical-care',
        'Before assisting with suture removal, what assessment should occur?',
        'Inspect the wound for healing, drainage, and signs of infection',
        ['Remove each suture in rapid sequence without inspecting the line',
        'Soak the incision in warm saline before removing sutures',
        'Reuse scissors from another tray without instrument processing'],
        'Providers evaluate readiness for suture removal. Infection or dehiscence requires different management than routine removal.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-clinical-care-063
    fact(
        'ccma-clinical-care',
        'When applying a heat pack, why is a cloth barrier placed between the pack and skin?',
        'To reduce the risk of thermal burns to the skin',
        [
            'To keep the pack colder against bare skin for longer intervals',
            'To monitor blood glucose through the insulating cloth layer',
            'To sterilize the reusable gel pack between patients without cleaning',
        ],
        'Thermal injuries occur quickly on sensitive or neuropathic skin. Barriers distribute temperature more safely.',
        [S.NHA_CCMA],
        'beginner',
    ),
]
