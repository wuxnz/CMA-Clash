# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-vitals)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [

    # skill-vitals-001
    fact(
        "skill-vitals",
        "What is the commonly cited normal range for an adult resting pulse rate?",
        "60 to 100 beats per minute",
        [
            "40 to 50 beats per minute at rest in every adult",
            "110 to 130 beats per minute at rest without exertion",
            "Exactly equal to the respiratory rate in all adults",
        ],
        "Resting rates outside this band suggest bradycardia or tachycardia until context is reviewed. Respiratory rate is measured separately and does not define pulse norms.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-002
    fact(
        "skill-vitals",
        "How wide should the blood pressure cuff bladder be for an upper arm measurement?",
        "About 40 percent of the upper arm circumference",
        [
            "About 15 percent of the forearm length from wrist to elbow",
            "Matched to wrist circumference for brachial artery compression",
            "About 80 percent of the distance from shoulder to elbow",
        ],
        "CDC guidance links cuff bladder width to arm size for accurate brachial occlusion. Undersized cuffs tend to overestimate pressure; wrist sizing is not the standard for arm cuffs.",
        [S.CDC_HBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-003
    fact(
        "skill-vitals",
        "Why should the patient's arm be supported at heart level during blood pressure measurement?",
        "To limit hydrostatic error from arm position above or below the heart",
        [
            "To remove the need for a stethoscope during manual auscultation",
            "To raise the recorded diastolic value for trending charts",
            "To shorten each measurement cycle to about ten seconds in routine outpatient care",
        ],
        "Gravity shifts transmitted pressure when the arm hangs low or sits high. Stethoscope use and measurement duration are independent of arm height.",
        [S.CDC_HBP],
        "beginner",
    ),
    # skill-vitals-004
    fact(
        "skill-vitals",
        "How long should a patient rest quietly before a routine clinic blood pressure reading when feasible?",
        "About five minutes with feet flat on the floor",
        [
            "No rest; measure immediately after climbing stairs to the room",
            "At least two hours of strict bed rest before any cuff inflation",
            "About ten seconds while the patient describes active symptoms aloud",
        ],
        "Brief quiet rest reduces transient elevations from activity or conversation. Prolonged bed rest is not required for outpatient screening, and talking during inflation can skew results.",
        [S.CDC_HBP],
        "beginner",
    ),
    # skill-vitals-005
    fact(
        "skill-vitals",
        "What does the first distinct Korotkoff sound during manual blood pressure auscultation represent?",
        "Systolic blood pressure when flow first returns under the cuff",
        [
            "Diastolic pressure when sounds disappear at full deflation",
            "Mean arterial pressure read directly from the gauge dial",
            "Pulse oximetry saturation at the fingertip sensor site in routine outpatient care",
        ],
        "The initial tapping marks systolic pressure; later muffling and silence mark diastolic phases. Pulse oximetry is a separate device and does not define Korotkoff phases.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-006
    fact(
        "skill-vitals",
        "When auscultating blood pressure manually, what do muffling and then silence of Korotkoff sounds indicate?",
        "Diastolic blood pressure at the point sounds disappear",
        [
            "Systolic pressure at the first audible tap under the cuff",
            "Central venous pressure estimated from the brachial artery",
            "Respiratory rate counted during cuff deflation at the bedside",
        ],
        "Diastolic is taken at sound disappearance in standard adult technique. The first tap is systolic, and venous pressure is not measured through a brachial cuff.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-007
    fact(
        "skill-vitals",
        "What is a typical normal respiratory rate range for a healthy resting adult?",
        "12 to 20 breaths per minute",
        [
            "4 to 6 breaths per minute without sleep or sedation",
            "28 to 36 breaths per minute at rest in the exam room",
            "Matched one-to-one with pulse rate in every adult patient",
        ],
        "Rates below or above this range may signal respiratory or metabolic problems. Pulse and respiration are related clinically but do not have a fixed one-to-one ratio.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-008
    fact(
        "skill-vitals",
        "What oral temperature range is often taught as normal for a healthy adult?",
        "About 97.0 to 99.0 degrees Fahrenheit",
        [
            "89.0 to 91.0 degrees Fahrenheit without hypothermia symptoms",
            "101.5 to 103.0 degrees Fahrenheit without reported illness",
            "Exactly 100.0 degrees Fahrenheit at every morning visit",
        ],
        "Individual baselines vary slightly across the day and by site. Sustained readings above roughly 100.4 F often define fever, not the entire normal span.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-009
    fact(
        "skill-vitals",
        "Why might tympanic temperature readings differ from oral readings on the same patient?",
        "Ear canal placement and cerumen can skew infrared ear measurements",
        [
            "Tympanic probes measure blood glucose in the external canal in routine outpatient care",
            "Oral thermometers bypass the hypothalamic set point entirely",
            "Ear and oral sites share identical heat transfer in every patient",
        ],
        "Poor probe aim or wax blocks the tympanic membrane target. Site differences matter when trending fever, so document method consistently.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-010
    fact(
        "skill-vitals",
        "How does a properly taken axillary temperature usually compare with oral temperature?",
        "It tends to read about one degree Fahrenheit lower than oral",
        [
            "It runs about two degrees higher than rectal core temperature",
            "It matches tympanic readings within 0.1 degree every time",
            "It replaces the need to report measurement site in the chart",
        ],
        "Axillary readings reflect cooler surface tissue. Charting should still note site so providers interpret trends without mixing incompatible methods.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-011
    fact(
        "skill-vitals",
        "What pulse oximetry saturation is commonly cited as normal for a healthy adult on room air?",
        "About 95 to 100 percent",
        [
            "About 70 to 80 percent without supplemental oxygen",
            "About 88 to 90 percent at rest without lung disease",
            "Exactly 100 percent required at every routine vitals check",
        ],
        "Values persistently below roughly 90 percent on room air warrant clinical review. Mild variation within the normal band can occur with probe placement and perfusion.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-012
    fact(
        "skill-vitals",
        "Which finding on pulse oximetry should prompt urgent reassessment and provider notification per many protocols?",
        "Saturation near or below 90 percent on room air with symptoms",
        [
            "Saturation of 96 percent with warm hands and good waveform",
            "Probe on the same finger used for prior capillary glucose testing",
            "Reading taken while the patient is speaking in full sentences",
        ],
        "Hypoxemia with distress needs rapid evaluation and may require oxygen or escalation. Mildly reduced saturation with good waveform still needs context, not automatic dismissal.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-013
    fact(
        "skill-vitals",
        "What effect does an undersized blood pressure cuff typically have on the recorded reading?",
        "It tends to falsely elevate systolic and diastolic values",
        [
            "It tends to falsely lower both systolic and diastolic values",
            "It removes Korotkoff sounds so diastolic cannot be heard",
            "It eliminates the need to support the arm at heart level",
        ],
        "A narrow bladder needs extra inflation to occlude a larger arm, pushing numbers upward. Arm position and auscultation technique still matter with any cuff size.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-014
    fact(
        "skill-vitals",
        "What effect does an oversized blood pressure cuff typically have on the recorded reading?",
        "It tends to falsely lower systolic and diastolic values",
        [
            "It tends to falsely raise both systolic and diastolic values",
            "It guarantees Korotkoff sounds audible at very low cuff pressure",
            "It replaces two-patient identifier checks before measurement",
        ],
        "A bladder that is too long for the arm may not fully compress the brachial artery. Identity verification remains required regardless of cuff fit.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-015
    fact(
        "skill-vitals",
        "Which patient identifiers should be confirmed before recording vital signs?",
        "At least two independent identifiers such as name and date of birth",
        [
            "Room number posted on the door without spoken confirmation in routine outpatient care",
            "First name alone when the patient appears familiar to staff",
            "Insurance member ID number read from the wallet card alone",
        ],
        "Two identifiers reduce wrong-chart errors during busy clinic flow. Room numbers change with seating, and familiarity is not a safety substitute.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-016
    fact(
        "skill-vitals",
        "Which details belong in vital sign documentation for a blood pressure entry?",
        "Value, arm used, patient position, cuff size, and time of measurement",
        [
            "Systolic number alone without diastolic or position noted",
            "Operator home phone number for callback about the reading",
            "Cuff brand name without the numeric result in the record in routine outpatient care",
        ],
        "Complete entries support trending and repeat measurement decisions. Partial data or personal contact details do not meet clinical documentation standards.",
        [S.CDC_HBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-017
    fact(
        "skill-vitals",
        "How is orthostatic blood pressure testing defined in many outpatient protocols?",
        "Compare supine or sitting pressure with standing pressure after position change",
        [
            "Measure both arms simultaneously without a position change in routine outpatient care",
            "Record one standing pressure without a baseline seated value",
            "Inflate the cuff to maximum pressure before any reading is taken",
        ],
        "Orthostatic testing looks for a drop after standing from rest. Single-position readings or maximal inflation techniques do not define orthostatic change.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-018
    fact(
        "skill-vitals",
        "How long should staff usually wait after a patient stands before the standing blood pressure reading?",
        "About one to three minutes before inflating the cuff again",
        [
            "Immediately upon standing while the patient is still rising",
            "At least thirty minutes of quiet walking in the hallway",
            "No waiting when the patient denies dizziness on questioning",
        ],
        "A brief stand time allows hemodynamic adjustment before the second reading. Immediate or prolonged delays miss or distort the orthostatic window.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-019
    fact(
        "skill-vitals",
        "Where is the apical pulse most commonly auscultated on the chest?",
        "At the fifth intercostal space near the midclavicular line",
        [
            "At the second intercostal space along the sternal border",
            "Over the carotid artery at the anterior neck midline",
            "At the popliteal fossa behind the flexed knee in routine outpatient care",
        ],
        "The apex of the heart underlies this anterior chest site. Carotid and popliteal locations assess peripheral pulses, not the apical impulse.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-020
    fact(
        "skill-vitals",
        "When is counting an apical pulse for a full minute preferred over a brief radial count?",
        "When the radial pulse is irregular or the patient has cardiac disease",
        [
            "When the patient is normotensive and denies chest symptoms in routine outpatient care",
            "When a pulse oximeter waveform is present on the finger probe",
            "When the clinic schedule requires vitals in under fifteen seconds",
        ],
        "Irregular rhythms are undercounted with short peripheral sampling. Schedule pressure does not override accurate rate assessment when rhythm is abnormal.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-021
    fact(
        "skill-vitals",
        "How should pulse rate be counted when the rhythm feels irregular at the radial artery?",
        "Auscultate or palpate for a full sixty seconds before recording",
        [
            "Multiply a fifteen-second peripheral count by four without listening",
            "Record the rate from the blood pressure machine display alone",
            "Estimate rate from respiratory rate divided by two at the bedside",
        ],
        "A full minute captures missed beats in atrial fibrillation and other arrhythmias. Short counts and surrogate estimates systematically underestimate irregular rates.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-022
    fact(
        "skill-vitals",
        "Which temperature finding commonly defines fever in an adult oral measurement?",
        "100.4 degrees Fahrenheit or higher",
        [
            "99.0 degrees Fahrenheit after drinking cold water minutes earlier",
            "97.5 degrees Fahrenheit in the morning without symptoms",
            "98.0 degrees Fahrenheit when measured in the axilla",
        ],
        "Fever thresholds depend on site and clinical context. A single borderline reading after cold intake needs repeat measurement rather than automatic fever labeling.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-023
    fact(
        "skill-vitals",
        "What does a zero-to-ten numeric pain rating scale ask the patient to report?",
        "Subjective pain intensity with zero as no pain and ten as worst imaginable",
        [
            "Objective tissue damage measured in millimeters on imaging",
            "Blood pressure change expected during painful procedures in routine outpatient care",
            "Respiratory rate counted while the patient is distracted",
        ],
        "Numeric scales capture the patient's perceived severity for trending and treatment. They do not replace physical exam or imaging findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-024
    fact(
        "skill-vitals",
        "How does a typical resting pulse rate in a healthy infant compare with a healthy adult?",
        "Infant resting rates are faster than adult resting rates",
        [
            "Infant resting rates are slower than adult resting rates",
            "Infant and adult resting rates share the same numeric range",
            "Infant rates are taken from the carotid artery at the neck alone",
        ],
        "Pediatric norms run higher because of smaller stroke volume and higher metabolic demand. Apical or brachial sites are common in infants, not carotid alone.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-025
    fact(
        "skill-vitals",
        "What respiratory rate range is often taught for a resting infant without respiratory distress?",
        "About 30 to 60 breaths per minute",
        [
            "About 8 to 12 breaths per minute while awake and calm",
            "About 20 to 25 breaths per minute matching adult norms exactly",
            "About 70 to 90 breaths per minute without retractions or cyanosis",
        ],
        "Faster baseline rates are normal in infancy but very high rates with distress need escalation. Adult ranges do not apply to newborn and infant assessment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-026
    fact(
        "skill-vitals",
        "Why should clinical scales be calibrated per manufacturer instructions?",
        "Inaccurate weight affects drug dosing and growth chart interpretation",
        [
            "Calibration removes the need to remove shoes before weighing in routine outpatient care",
            "Calibration converts height measures into blood pressure values",
            "Calibration replaces documenting whether the patient ate breakfast",
        ],
        "Weight errors propagate into medication and nutritional decisions. Shoe policy and meal timing remain separate parts of the intake assessment.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-027
    fact(
        "skill-vitals",
        "How should standing height be measured for accurate growth and BMI data?",
        "Patient stands straight against a stadiometer with heels together and head level",
        [
            "Patient sits on the exam table while staff estimates height visually",
            "Patient stands on tiptoes to maximize the recorded centimeters in routine outpatient care",
            "Patient lies supine while tape measure follows the mattress curve",
        ],
        "Stadiometer technique standardizes posture for serial comparisons. Visual guesses and mattress curves introduce systematic error in charts.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-028
    fact(
        "skill-vitals",
        "How is body mass index calculated from height and weight in US customary units?",
        "Weight in pounds divided by height in inches squared, then multiplied by 703",
        [
            "Height in inches divided by weight in pounds without conversion in routine outpatient care",
            "Weight in kilograms multiplied by height in meters without squaring",
            "Waist circumference divided by hip circumference for the BMI value",
        ],
        "BMI uses squared height in the denominator to scale mass to stature. Waist-to-hip ratio is a different anthropometric measure.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-029
    fact(
        "skill-vitals",
        "What is a key limitation of many automated office blood pressure devices?",
        "Irregular heart rhythms can reduce accuracy compared with manual auscultation",
        [
            "They cannot display systolic and diastolic numbers on the screen in routine outpatient care",
            "They require cuff placement on the ankle for every adult patient",
            "They eliminate the need to select cuff size based on arm circumference",
        ],
        "Oscillometric devices may misread during arrhythmia; manual confirmation may be needed. Cuff sizing rules still apply to automated cuffs on the arm.",
        [S.CDC_HBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-030
    fact(
        "skill-vitals",
        "Where should the stethoscope diaphragm be placed for manual brachial blood pressure measurement?",
        "Over the brachial artery at the antecubital fossa inside the cuff edge",
        [
            "Over the radial artery at the wrist distal to the cuff bladder in routine outpatient care",
            "Over the apex of the heart while the cuff is on the opposite arm",
            "Over the carotid pulse while the cuff remains deflated on the leg",
        ],
        "Korotkoff sounds are auscultated at the brachial artery under the cuff margin. Radial, apical, and carotid sites do not substitute for this placement.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-031
    fact(
        "skill-vitals",
        "Why do many guidelines ask patients to avoid smoking before blood pressure measurement?",
        "Nicotine can transiently raise blood pressure and heart rate",
        [
            "Smoking removes the need to rest quietly before cuff inflation",
            "Smoking guarantees falsely low diastolic readings on every visit",
            "Smoking converts manual auscultation into oscillometric mode",
        ],
        "Stimulant effects can mask resting hypertension or create false elevations. Rest periods and technique remain required regardless of tobacco use.",
        [S.CDC_HBP],
        "advanced",
    ),
    # skill-vitals-032
    fact(
        "skill-vitals",
        "How can a full bladder affect seated blood pressure readings?",
        "It may elevate readings until the patient voids",
        [
            "It lowers systolic pressure by increasing vagal tone every time",
            "It removes audible Korotkoff sounds at normal cuff pressures",
            "It replaces orthostatic testing with a single supine value",
        ],
        "Bladder distention can raise pressure through discomfort and autonomic responses. Voiding before repeat measurement can clarify true resting values.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-033
    fact(
        "skill-vitals",
        "Why is pain often documented as a fifth vital sign in ambulatory care?",
        "Unrelieved pain affects recovery, function, and quality of life",
        [
            "Pain scores replace temperature when thermometers are unavailable",
            "Pain ratings determine insurance authorization without provider input",
            "Pain documentation removes the need to assess mental status",
        ],
        "Tracking pain supports treatment and reassessment like other vitals. It complements rather than replaces temperature checks or behavioral assessment.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-034
    fact(
        "skill-vitals",
        "Which action is inappropriate when obtaining routine vital signs in an outpatient exam room?",
        "Placing every patient in steep head-down tilt for all measurements",
        [
            "Supporting the arm at heart level during blood pressure in routine outpatient care",
            "Confirming two identifiers before attaching monitoring devices",
            "Recording the measurement site when documenting temperature",
        ],
        "Routine vitals do not require Trendelenburg positioning, which is reserved for specific clinical scenarios. Standard arm support and identification remain appropriate.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-035
    fact(
        "skill-vitals",
        "Among common outpatient temperature sites, which tends to reflect core temperature most closely when technique is correct?",
        "Rectal measurement in appropriate patients and settings",
        [
            "Forehead skin swipe without hair pulled from the sensor path",
            "Axillary placement with the probe loosely touching clothing",
            "Tympanic scan aimed at the ear canal wall away from the membrane",
        ],
        "Rectal readings approximate core heat when policy allows the site. Poorly aimed infrared or axillary techniques lag core changes.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-036
    fact(
        "skill-vitals",
        "Why have mercury-in-glass clinical thermometers largely been replaced in US clinics?",
        "Mercury spills pose toxicity risk and many sites ban their use",
        [
            "Mercury thermometers cannot measure below body temperature",
            "Mercury devices require daily calibration with liquid nitrogen",
            "Mercury readings are less accurate than palm placement estimates",
        ],
        "Environmental and employee safety drove adoption of digital and disposable thermometers. Modern devices still need correct site technique and battery checks.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-037
    fact(
        "skill-vitals",
        "What limitation should staff remember when using non-contact forehead thermometers?",
        "Sweat, drafts, and recent face coverings can skew surface readings",
        [
            "They directly sample pulmonary artery temperature on every scan",
            "They eliminate fever workups when the screen shows green text in routine outpatient care",
            "They replace oral thermometers for all sterile field procedures",
        ],
        "Skin surface temperature trails core fever, especially with perspiration or cooling. Abnormal screens still need confirmatory measurement per protocol.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-038
    fact(
        "skill-vitals",
        "What does delayed capillary refill longer than about two seconds in an adult finger suggest?",
        "Possible poor peripheral perfusion needing further assessment",
        [
            "Normal hydration with brisk central pulses at the carotid in routine outpatient care",
            "Accurate core temperature without checking measurement site",
            "Complete relief of pain after analgesic medication dosing",
        ],
        "Cap refill is a quick perfusion screen at the nail bed. It does not confirm core temperature or pain control without other findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-039
    fact(
        "skill-vitals",
        "How is mean arterial pressure estimated from systolic and diastolic blood pressure?",
        "Diastolic plus one third of the pulse pressure difference",
        [
            "Systolic minus diastolic without further calculation steps",
            "Systolic multiplied by diastolic then divided by heart rate",
            "Diastolic multiplied by two then added to systolic without dividing",
        ],
        "MAP weights diastolic pressure because the cardiac cycle spends more time in diastole. Simple subtraction or heart rate products are not the taught formula.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-040
    fact(
        "skill-vitals",
        "Which blood pressure reading pattern should prompt urgent evaluation per common emergency protocols?",
        "Systolic above 180 or diastolic above 120 with symptoms",
        [
            "Systolic 128 and diastolic 78 without headache or vision change",
            "Systolic 118 and diastolic 72 after five minutes of quiet rest",
            "Systolic 135 and diastolic 85 in a patient taking prescribed antihypertensives",
        ],
        "Hypertensive emergency ranges with end-organ symptoms need rapid provider involvement. Mildly elevated or well-controlled values still need context but not the same urgency.",
        [S.CDC_HBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-041
    fact(
        "skill-vitals",
        "How should a resting pulse near 50 beats per minute in an asymptomatic athlete be interpreted?",
        "It may be a normal training effect if rhythm is regular and perfusion is good",
        [
            "It requires immediate defibrillation in every outpatient setting",
            "It proves hypothyroidism without laboratory confirmation in routine outpatient care",
            "It indicates mandatory hospital admission before any further vitals",
        ],
        "Conditioned bradycardia differs from symptomatic bradycardia with dizziness or hypotension. Context, rhythm, and symptoms guide escalation beyond a single number.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-042
    fact(
        "skill-vitals",
        "When should abnormal vital signs be communicated promptly to the supervising clinician?",
        "When values fall outside expected limits or match protocol-defined critical thresholds",
        [
            "When the patient prefers not to hear the numbers at the bedside",
            "After all scheduled appointments finish regardless of severity in routine outpatient care",
            "When the reading matches yesterday's value without new symptoms",
        ],
        "Timely reporting allows treatment of hypotension, hypoxia, or hypertensive crisis. Delaying notification for convenience or stable trends without policy guidance risks harm.",
        [S.NHA_CCMA],
        "intermediate",
    ),

]
