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
            "30 to 40 beats per minute at rest",
            "120 to 160 beats per minute at rest",
            "Equal to the respiratory rate in every adult",
        ],
        "Resting tachycardia and bradycardia fall outside this typical range. Respiratory rate is a separate vital sign.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-002
    fact(
        "skill-vitals",
        "How wide should the blood pressure cuff bladder be relative to the upper arm circumference?",
        "About 40 percent of the arm circumference",
        [
            "About 10 percent of the arm length",
            "Equal to the wrist circumference",
            "Twice the length of the upper arm",
        ],
        "CDC blood pressure guidance ties cuff width to arm size. Undersized cuffs falsely elevate readings.",
        [S.CDC_HBP],
        "beginner",
    ),
    # skill-vitals-003
    fact(
        "skill-vitals",
        "Why should the patient's arm be supported at heart level during blood pressure measurement?",
        "To reduce systematic error from hydrostatic pressure differences",
        [
            "To eliminate the need for a stethoscope",
            "To raise diastolic pressure for a higher reading",
            "To shorten the measurement to five seconds",
        ],
        "An arm below or above the heart changes transmitted pressure. Stethoscope use and timing are unrelated to arm height.",
        [S.CDC_HBP],
        "beginner",
    ),
    # skill-vitals-004
    fact(
        "skill-vitals",
        "How long should a patient rest quietly before a clinic blood pressure reading when feasible?",
        "About five minutes with feet supported",
        [
            "No rest; measure immediately after stairs",
            "At least two hours of bed rest",
            "Ten seconds while talking about symptoms",
        ],
        "Brief rest reduces transient elevations from activity or talking. Prolonged bed rest is not required for routine clinic measurement.",
        [S.CDC_HBP],
        "beginner",
    ),
    # skill-vitals-005
    fact(
        "skill-vitals",
        "What does the first Korotkoff sound during manual blood pressure measurement represent?",
        "Systolic blood pressure",
        [
            "Diastolic blood pressure",
            "Mean arterial pressure directly",
            "Pulse oximetry saturation",
        ],
        "The initial tapping sound marks systolic pressure; muffling and disappearance mark diastolic phases. Pulse oximetry is a different device.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-006
    fact(
        "skill-vitals",
        "Which cuff size error most often causes falsely elevated blood pressure readings?",
        "A cuff bladder that is too narrow for the arm",
        [
            "A cuff bladder that is too wide for the arm",
            "A cuff placed on the forearm per policy",
            "A cuff with the label facing the patient",
        ],
        "Undersized cuffs read high; oversized cuffs tend to read low. Label orientation alone does not systematically raise pressure.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-007
    fact(
        "skill-vitals",
        "When counting an irregular apical pulse, how long should auscultation last?",
        "A full 60 seconds at the cardiac apex",
        [
            "Five seconds at the radial artery",
            "Fifteen seconds while the patient exercises",
            "Until the patient reports dizziness",
        ],
        "Irregular rhythms need a full minute for accuracy at the apex. Brief radial counts miss beat-to-beat variation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-008
    fact(
        "skill-vitals",
        "Where is the apical pulse auscultated on an adult with typical anatomy?",
        "Fifth intercostal space at the midclavicular line",
        [
            "Radial artery at the wrist",
            "Popliteal fossa behind the knee",
            "Carotid triangle with firm pressure",
        ],
        "The apex is heard over the left ventricular area at the midclavicular line. Peripheral pulses do not replace apical rate when irregular.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-009
    fact(
        "skill-vitals",
        "What vital sign documentation should include when technique affects interpretation?",
        "Time, measurement site or route, and patient position when relevant",
        [
            "Numeric values without context",
            "Abnormal results without numeric values",
            "Provider signature in place of values",
        ],
        "Position and site explain changes such as orthostatic differences. Values alone omit clinical context.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-010
    fact(
        "skill-vitals",
        "Pulse oximetry estimates oxygen saturation by measuring what at the probe site?",
        "Light absorption through pulsatile arterial blood",
        [
            "Direct arterial blood gas sampling",
            "Chest wall impedance alone",
            "Noninvasive blood pressure oscillation",
        ],
        "SpO2 devices use spectrophotometry at a peripheral site. Arterial blood gas requires a blood sample.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-011
    fact(
        "skill-vitals",
        "Which factor commonly lowers pulse oximetry accuracy?",
        "Poor peripheral perfusion or patient motion at the probe",
        [
            "Patient shoe size",
            "Room wall color",
            "Stethoscope tubing length",
        ],
        "Cold extremities, hypotension, and motion artifact weaken the signal. Room decor does not alter oximeter physics.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-012
    fact(
        "skill-vitals",
        "When is oral temperature measurement inappropriate?",
        "When the patient cannot cooperate, is receiving perioral oxygen, or is NPO per procedure orders",
        [
            "For every adult wellness visit",
            "Whenever tympanic thermometers are available",
            "When the patient prefers rectal route without order",
        ],
        "Oral probes need a sealed mouth and lack of interfering oxygen flow. Preference alone does not override contraindications.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-013
    fact(
        "skill-vitals",
        "How should respiratory rate ideally be obtained?",
        "Counted discreetly for a full minute while observing chest movement",
        [
            "Ask the patient to breathe rapidly for ten seconds",
            "Estimate rate while discussing symptoms without watching chest rise",
            "Measure once per week during long-term care",
        ],
        "Patients may alter breathing when they know they are being watched; discreet observation improves accuracy.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-014
    fact(
        "skill-vitals",
        "Orthostatic vital signs compare measurements taken in which positions?",
        "Supine, sitting, and standing blood pressure and pulse",
        [
            "Left lateral decubitus position without blood pressure",
            "Temperature in axilla and rectum simultaneously",
            "Respiratory rate without blood pressure",
        ],
        "Orthostatic testing tracks cardiovascular response to position change. Temperature routes alone do not assess orthostasis.",
        [S.CDC_HBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-015
    fact(
        "skill-vitals",
        "A drop of at least 20 mmHg systolic or 10 mmHg diastolic within three minutes of standing suggests what finding?",
        "Orthostatic hypotension when paired with symptoms",
        [
            "Normal postural response in every patient",
            "Primary hypertension diagnosis by itself",
            "Faulty thermometer calibration",
        ],
        "Orthostatic criteria use blood pressure change with position. Diagnosis requires clinical correlation, not temperature equipment.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-016
    fact(
        "skill-vitals",
        "Why should the blood pressure cuff bladder length cover most of the upper arm?",
        "The bladder length should cover about 80 percent of the arm circumference for accurate measurement",
        [
            "Length matched to wrist width regardless of arm size",
            "Length should stop at the elbow crease regardless of arm size",
            "Length is irrelevant if the velcro closes",
        ],
        "CDC guidance pairs bladder width and length with arm size. Closing velcro on an undersized bladder still skews results.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-017
    fact(
        "skill-vitals",
        "A patient has bilateral mastectomy with lymph node dissection. Which blood pressure site requires provider guidance?",
        "The arm on the affected side may be contraindicated for cuff placement",
        [
            "Both legs are forbidden for any cuff use",
            "Oral temperature is mandatory on the affected side",
            "Pulse oximetry cannot be used on any finger",
        ],
        "Lymphedema risk limits ipsilateral arm pressures; alternative sites follow orders. Leg and finger options remain when appropriate.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-018
    fact(
        "skill-vitals",
        "An automated blood pressure device repeatedly reads error messages on an obese patient with a standard cuff. What is the best first step?",
        "Select an appropriately sized large adult or thigh cuff per policy",
        [
            "Document a normal pressure without measuring",
            "Place the standard cuff on the forearm without validation",
            "Repeat the reading while the patient holds their breath for two minutes",
        ],
        "Cuff size mismatch causes failed or inaccurate cycles on devices. Forearm use requires validated protocols.",
        [S.CDC_HBP],
        "advanced",
    ),
    # skill-vitals-019
    fact(
        "skill-vitals",
        "A clinic patient drank caffeinated coffee in the waiting room minutes before blood pressure measurement. How should the medical assistant proceed?",
        "Note recent caffeine intake and follow policy on resting or rescheduling measurement",
        [
            "Ignore intake because caffeine has no cardiovascular effect",
            "Add 40 mmHg to the systolic value automatically",
            "Switch to tympanic temperature instead of blood pressure",
        ],
        "Caffeine can transiently raise pressure; documentation and timing affect interpretation. Arbitrary numeric adjustment is unsafe.",
        [S.CDC_HBP],
        "advanced",
    ),
    # skill-vitals-020
    fact(
        "skill-vitals",
        "Radial pulse is counted for 30 seconds when the rhythm is regular. What documentation practice follows?",
        "Multiply the 30-second count by two unless policy requires a full minute",
        [
            "Record the 30-second count as the final rate without adjustment",
            "Double the diastolic blood pressure instead",
            "Omit pulse rate when rhythm is regular",
        ],
        "Regular rhythms allow doubling a half-minute count per many protocols. Blood pressure components are separate values.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-021
    fact(
        "skill-vitals",
        "Which pain rating scale is often used for adults who can self-report?",
        "0 to 10 numeric rating scale",
        [
            "FLACC behavioral scale for all adults",
            "Apgar score at every visit",
            "Glasgow Coma Scale for routine sore throat",
        ],
        "Numeric scales suit verbal adults; FLACC targets nonverbal patients. Apgar and GCS address other clinical domains.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-022
    fact(
        "skill-vitals",
        "Tympanic temperature measurement requires which technique element?",
        "Proper probe insertion aimed at the tympanic membrane per manufacturer instructions",
        [
            "Probe held against the forehead without touching skin",
            "Probe inserted while the patient chews gum vigorously",
            "Probe shared between patients without cleaning",
        ],
        "Ear canal placement affects accuracy; forehead noncontact devices differ. Shared probes without cleaning violate infection control.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-023
    fact(
        "skill-vitals",
        "What is a typical normal adult respiratory rate at rest?",
        "12 to 20 breaths per minute",
        [
            "4 to 6 breaths per minute",
            "30 to 40 breaths per minute at rest",
            "Identical to pulse rate in every healthy adult",
        ],
        "Tachypnea at rest exceeds this range. Pulse and respiratory rate are related but not identical numbers.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-024
    fact(
        "skill-vitals",
        "When a manual blood pressure cannot be heard, what should be documented?",
        "The value as palpated systolic pressure or note inability to auscultate with technique used",
        [
            "A fabricated diastolic value of 80 mmHg",
            "Patient refusal without attempting measurement",
            "Temperature instead of blood pressure",
        ],
        "Palpated systolic or clear documentation of failed auscultation maintains honesty in the record. Invented numbers are unsafe.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-025
    fact(
        "skill-vitals",
        "A patient with atrial fibrillation needs a pulse for medication dosing. Which site and duration are preferred?",
        "Apical pulse for a full minute",
        [
            "Radial pulse for five seconds doubled",
            "Carotid pulse pressed firmly for 15 seconds",
            "Popliteal pulse while walking in the hall",
        ],
        "Irregularly irregular rhythms need apical auscultation for a minute. Brief radial counts and carotid pressure are unreliable or unsafe.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-026
    fact(
        "skill-vitals",
        "Blood pressure measured with the cuff over clothing when policy requires bare arm may produce what result?",
        "Falsely elevated or inconsistent readings",
        [
            "More accurate readings than on bare skin",
            "No effect on any patient size",
            "Lower readings in every hypertensive patient",
        ],
        "Fabric thickness interferes with bladder compression. Policies usually require bare arm or standardized thin sleeve.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-027
    fact(
        "skill-vitals",
        "Which step reduces talking-related error during blood pressure measurement?",
        "Keep the patient quiet during the reading",
        [
            "Ask detailed history questions during inflation",
            "Have the patient count aloud backward from 100",
            "Instruct the patient to perform leg raises during measurement",
        ],
        "Talking and exertion raise pressure transiently. Quiet rest improves reproducibility.",
        [S.CDC_HBP],
        "beginner",
    ),
    # skill-vitals-028
    fact(
        "skill-vitals",
        "Height and weight obtained at the same visit support which clinical calculation?",
        "Body mass index when policy includes it in vitals flow",
        [
            "Glasgow Coma Score automatically",
            "INR without laboratory testing",
            "Peak flow without a meter",
        ],
        "BMI uses height and weight; other listed measures need different tools or assessments.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-029
    fact(
        "skill-vitals",
        "A pediatric patient needs blood pressure measurement. Which cuff principle applies?",
        "Use a pediatric or small adult cuff matched to arm size, not an adult large cuff on a small arm",
        [
            "Use the largest cuff available for every child",
            "Defer blood pressure until age 21 for every child",
            "Place the adult cuff on the calf without orders",
        ],
        "Pediatric arms need size-appropriate cuffs for valid pressures. Age alone does not eliminate measurement need when ordered.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-030
    fact(
        "skill-vitals",
        "What does a widening pulse pressure (large difference between systolic and diastolic) sometimes prompt?",
        "Provider notification when marked or symptomatic, because causes vary",
        [
            "Automatic discharge without assessment",
            "Documentation as a normal finding in every elderly patient",
            "Replacement of temperature measurement with pulse pressure",
        ],
        "Wide pulse pressure can reflect several conditions and needs clinical context. It is not universally normal or ignored.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-031
    fact(
        "skill-vitals",
        "When measuring blood pressure in a patient with an arteriovenous fistula for dialysis, where should the cuff be placed?",
        "On the arm without the fistula unless provider orders otherwise",
        [
            "Directly over the fistula thrill",
            "On the leg while compressing the fistula",
            "On whichever arm has the highest historical reading",
        ],
        "Pressure over a fistula can damage access. The nonfistula arm is standard unless directed otherwise.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-032
    fact(
        "skill-vitals",
        "Fever is commonly defined in adults as oral temperature at or above what level?",
        "38 degrees Celsius or 100.4 degrees Fahrenheit",
        [
            "35 degrees Celsius exactly",
            "37 degrees Celsius in every patient at night",
            "40 degrees Fahrenheit as the fever threshold for all children",
        ],
        "Standard fever thresholds use 38 C or 100.4 F. Lower values may be normal variation.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-vitals-033
    fact(
        "skill-vitals",
        "Axillary temperature readings compared with oral measurements tend to read how?",
        "About 0.5 to 1 degree Fahrenheit lower than oral",
        [
            "Identical to core pulmonary artery temperature",
            "Higher than rectal temperature",
            "Unrelated to site selection",
        ],
        "Site differences require consistent route documentation. Axillary is not interchangeable with oral without interpretation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-034
    fact(
        "skill-vitals",
        "A patient on contact precautions still needs vitals. What infection control step applies?",
        "Don and doff PPE per transmission-based precautions while performing measurement",
        [
            "Omit vitals to avoid donning gloves",
            "Use the same cuff on all patients without cleaning",
            "Document vitals from the doorway without entering",
        ],
        "Vitals are part of care and require appropriate PPE. Shared uncleaned equipment spreads organisms.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-vitals-035
    fact(
        "skill-vitals",
        "Which finding during vital signs should prompt immediate provider notification in an outpatient setting?",
        "Chest pain with diaphoresis and hypotension",
        [
            "Mild anxiety before an injection",
            "History of seasonal allergies without symptoms",
            "Prior knee surgery ten years ago",
        ],
        "Acute coronary symptoms with hemodynamic change need urgent escalation. Stable history items are not emergencies alone.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-036
    fact(
        "skill-vitals",
        "When serial blood pressures are ordered every 15 minutes, what practice supports accurate comparison?",
        "Use the same arm, cuff size, and position each time unless contraindicated",
        [
            "Alternate arms randomly without documentation",
            "Change cuff size each reading for variety",
            "Measure in standing position for every serial reading",
        ],
        "Consistency reduces artifact from arm or position switches. Random changes obscure true trends.",
        [S.CDC_HBP],
        "intermediate",
    ),
    # skill-vitals-037
    fact(
        "skill-vitals",
        "A home blood pressure log brought to clinic shows wide variability. What should the medical assistant do?",
        "Review technique, cuff size, timing, and bring concerns to the provider",
        [
            "Discard the log as unreliable without review",
            "Average the highest and lowest values without context",
            "Tell the patient to stop measuring at home permanently",
        ],
        "Technique and device issues explain variability; provider review guides therapy. Discarding data loses useful trends.",
        [S.CDC_HBP],
        "advanced",
    ),
    # skill-vitals-038
    fact(
        "skill-vitals",
        "Capnography end-tidal CO2 monitoring in some settings reflects primarily what physiology?",
        "Ventilation and airway patency trends",
        [
            "Hemoglobin A1c over 90 days",
            "Renal creatinine clearance directly",
            "Intraocular pressure",
        ],
        "EtCO2 tracks ventilation; diabetes and renal labs need other tests.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-039
    fact(
        "skill-vitals",
        "Before applying a reusable blood pressure cuff, what infection control step is expected?",
        "Clean and disinfect the cuff surface per manufacturer and facility policy between patients",
        [
            "Wipe with the same cloth used for floors",
            "Store cuff in a soiled linen hamper",
            "Rotate cuffs without cleaning if patients look well",
        ],
        "Noncritical equipment still needs low-level disinfection between patients. Appearance of wellness does not rule out colonization.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-vitals-040
    fact(
        "skill-vitals",
        "Which respiration pattern with increasing depth followed by apnea may indicate neurologic or metabolic disease?",
        "Cheyne-Stokes respirations",
        [
            "Kussmaul respirations with steady rate",
            "Bradypnea below eight per minute during sleep as normal",
            "Sighing respirations once per hour in every healthy adult",
        ],
        "Cheyne-Stokes shows cyclic depth changes and pauses. Kussmaul is deep and rapid without the same apnea pattern.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-vitals-041
    fact(
        "skill-vitals",
        "A patient reports dizziness when vitals show orthostatic blood pressure drop and tachycardia. What action aligns with scope?",
        "Assist patient to safe position, recheck as ordered, and notify the provider",
        [
            "Send the patient to drive home alone",
            "Ignore symptoms if temperature is normal",
            "Repeat respiratory rate and discharge without notifying provider",
        ],
        "Symptoms with orthostatic changes need provider awareness and fall prevention. Driving with active dizziness is unsafe.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-vitals-042
    fact(
        "skill-vitals",
        "Why document whether blood pressure was taken manually or by automated device?",
        "Method affects how subsequent readings should be compared and repeated",
        [
            "Automated devices are inaccurate in clinics by design",
            "Manual readings require no cuff size rules",
            "Automated readings cannot be repeated on the same visit",
        ],
        "Consistency in method supports trend interpretation. Both manual and automated techniques require proper cuff sizing.",
        [S.CDC_HBP, S.NHA_CCMA],
        "intermediate",
    ),
]
