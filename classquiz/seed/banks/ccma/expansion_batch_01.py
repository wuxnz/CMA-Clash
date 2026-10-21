# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""CCMA expansion batch 01 (25 hand-authored items)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-exp-b01-001
    fact(
        "ccma-foundational",
        "Which suffix in a medical term typically indicates inflammation?",
        "-itis",
        ["-oma", "-ectomy", "-pathy"],
        "The suffix -itis denotes inflammation, as in tonsillitis. -oma suggests a tumor, which students often confuse with inflammatory conditions.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-002
    fact(
        "ccma-foundational",
        "What does the combining form \"leuko-\" refer to in medical terminology?",
        "White",
        ["Red", "Yellow", "Blue"],
        "Leuko- means white, as in leukocytes (white blood cells). Erythro- refers to red, which is a common mix-up on terminology items.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-003
    fact(
        "ccma-foundational",
        "Why are Standard Precautions applied to every patient encounter?",
        "Blood and body fluids may carry infection even when a diagnosis is unknown",
        [
            "They replace the need for hand hygiene after glove use",
            "They apply when visible bleeding is present",
            "They permit reuse of needles between roommates",
        ],
        "CDC Standard Precautions treat all patients as potentially infectious. Limiting precautions to visible blood misses asymptomatic or undiagnosed carriage.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-004
    fact(
        "ccma-foundational",
        "A clinic implements a new chemical disinfectant. What must the medical assistant review before use?",
        "The product label for contact time, dilution, and compatible surfaces",
        [
            "Social media reviews from other clinics",
            "The color of the bottle alone",
            "Whether patients prefer scented products",
        ],
        "EPA-registered disinfectants require label-directed contact times to kill pathogens. Dilution and surface compatibility affect both safety and effectiveness.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b01-005
    fact(
        "ccma-anatomy",
        "Which chamber of the heart receives oxygenated blood from the pulmonary veins?",
        "Left atrium",
        ["Right atrium", "Right ventricle", "Pulmonary artery"],
        "Oxygenated blood returns from the lungs via pulmonary veins into the left atrium. The right atrium receives venous systemic blood, which is a frequent reversal error.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-006
    fact(
        "ccma-anatomy",
        "Where does gas exchange between air and blood occur in the respiratory system?",
        "Alveoli of the lungs",
        ["Larynx", "Mainstem bronchi", "Pleural cavity"],
        "Alveoli provide the thin membrane needed for oxygen and carbon dioxide diffusion. Conducting airways move air but do not perform primary gas exchange.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-007
    fact(
        "ccma-anatomy",
        "Which hormone lowers blood glucose by promoting cellular uptake?",
        "Insulin",
        ["Glucagon", "Aldosterone", "Antidiuretic hormone"],
        "Insulin from pancreatic beta cells drives glucose into cells. Glucagon raises glucose, which is the paired distractor students often select.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-008
    fact(
        "ccma-anatomy",
        "A patient with right-sided heart failure may develop dependent edema because fluid backs up in which circulation?",
        "Systemic venous circulation",
        ["Pulmonary arterial circulation", "Coronary arterial circulation", "Lymphatic return from the lungs"],
        "Right heart failure increases venous hydrostatic pressure in the systemic veins, promoting peripheral edema. Pulmonary congestion is more typical of left-sided failure.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b01-009
    fact(
        "ccma-clinical-care",
        "Before measuring an adult's blood pressure, what should the medical assistant confirm?",
        "The patient has rested with the back supported and feet flat for several minutes",
        [
            "The cuff is placed over clothing for warmth",
            "The patient is talking continuously during inflation",
            "The arm is held above head level throughout the reading",
        ],
        "Rest and proper arm position stabilize readings. A cuff over thick clothing or active talking can falsely elevate results.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-010
    fact(
        "ccma-clinical-care",
        "Which site is commonly used for an intramuscular injection in an adult with adequate deltoid mass?",
        "Upper outer third of the deltoid muscle",
        ["Midline of the anterior thigh near the knee", "Over the sternum", "Plantar surface of the foot"],
        "CDC vaccine administration guidance places adult deltoid IM injections in the thick lateral shoulder. The vastus lateralis is preferred for many infants, not the sternum or foot.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-011
    fact(
        "ccma-clinical-care",
        "A patient scheduled for fasting blood work ate breakfast an hour ago. What is the appropriate action?",
        "Notify the provider and reschedule or follow lab protocol for the ordered test",
        [
            "Draw the sample and label it random without telling anyone",
            "Have the patient drink sugary soda before the draw",
            "Cancel the order permanently without documentation",
        ],
        "Fasting requirements depend on the ordered analyte. Proceeding without notifying the team can yield misleading glucose or lipid results.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-012
    fact(
        "ccma-clinical-care",
        "During a sterile dressing change, the assistant accidentally touches the inner sterile pad. What should happen next?",
        "Discard the contaminated item and replace it using sterile technique",
        [
            "Continue because the patient looks clean",
            "Fold the pad so the touched side faces the wound",
            "Rinse the pad under tap water and reuse it",
        ],
        "Sterility is event-based; contact with nonsterile surfaces requires replacement. Rinsing does not restore sterility for invasive wound care.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b01-013
    fact(
        "ccma-coordination",
        "When scheduling a follow-up visit, what information helps the care team prioritize timing?",
        "Clinical urgency, provider instructions, and patient availability",
        [
            "The color of the patient's clothing",
            "Whether the front desk prefers morning breaks",
            "Unrelated social media posts",
        ],
        "Scheduling should reflect medical need and ordered follow-up intervals. Cosmetic or staff convenience factors do not determine safe return intervals.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-014
    fact(
        "ccma-coordination",
        "What is the main purpose of teach-back when giving discharge instructions?",
        "To confirm the patient can restate key steps in their own words",
        [
            "To test reading speed for billing staff",
            "To replace provider prescriptions",
            "To document that the patient signed every form",
        ],
        "Teach-back uncovers misunderstandings before the patient leaves. Signature on forms does not prove comprehension of wound care or medication timing.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-015
    fact(
        "ccma-admin",
        "What does a Current Procedural Terminology (CPT) code primarily describe on a claim?",
        "A procedure or service performed",
        ["A patient address", "A nursing diagnosis narrative", "A medication allergy"],
        "CPT codes report professional services and procedures. Diagnoses are coded with ICD-10-CM, which students sometimes swap on billing items.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-016
    fact(
        "ccma-admin",
        "A payer denies a claim for missing prior authorization. What should the billing team do first?",
        "Review the denial reason and policy, then follow appeal or correction steps",
        [
            "Delete the patient chart",
            "Bill the patient for the full charge without review",
            "Post the denial on a public website",
        ],
        "Denials require structured follow-up per contract and regulation. Immediate full patient balance without review may violate policy and harm the patient relationship.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-017
    fact(
        "ccma-communication",
        "How should a medical assistant respond when a patient says they do not understand a medication instruction?",
        "Use plain language, chunk the steps, and ask the patient to repeat them back",
        [
            "Speak louder using the same complex terms",
            "Tell the patient to read the bottle later at home",
            "End the visit without involving the provider",
        ],
        "Health literacy strategies improve adherence and safety. Volume alone does not simplify concepts; unresolved confusion should involve the care team.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-018
    fact(
        "ccma-communication",
        "Which action best supports professional telephone communication in a medical office?",
        "Identify the clinic, yourself, and offer to help before requesting information",
        [
            "Ask for the Social Security number before greeting",
            "Discuss another patient's results to fill silence",
            "Refuse to give the clinic name for privacy",
        ],
        "Clear identification sets expectations and reduces callbacks. Requesting identifiers follows greeting and purpose; sharing other patients' data violates privacy rules.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-019
    fact(
        "ccma-law-ethics",
        "What are the core elements of valid informed consent for a procedure?",
        "Disclosure, comprehension, voluntariness, and capacity to decide",
        [
            "A signature obtained while the patient is sedated without prior discussion",
            "Payment in full before any explanation",
            "Staff preference for morning appointments",
        ],
        "Consent is a process, not just a form. Sedation without prior discussion undermines comprehension and voluntariness.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-020
    fact(
        "ccma-law-ethics",
        "A coworker asks you to document care you did not observe. What is the ethical response?",
        "Refuse and report per facility policy because falsification is fraudulent",
        [
            "Sign to avoid conflict and fix it later",
            "Add vague wording so no one can verify",
            "Chart for them because they are busy",
        ],
        "Accurate documentation is a legal record. Signing for unobserved care is falsification and exposes patients and staff to harm.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b01-021
    fact(
        "ccma-hipaa",
        "What does the HIPAA minimum necessary standard require when using protected health information?",
        "Limit access and disclosure to the amount needed for the current purpose",
        [
            "Share the entire chart with any vendor who requests it",
            "Post visit summaries on a public bulletin board",
            "Email full records to personal accounts for convenience",
        ],
        "Minimum necessary reduces privacy risk for treatment, payment, and operations. Broad sharing without role-based limits violates the Privacy Rule.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-022
    fact(
        "ccma-hipaa",
        "A patient requests a copy of their medical record. What should the office do?",
        "Follow HIPAA right-of-access procedures, including reasonable timelines and fees per policy",
        [
            "Deny all requests because charts are clinic property",
            "Give records to a neighbor without verifying authority",
            "Require the patient to delete their own diagnoses first",
        ],
        "Patients generally have a right to access their PHI with defined exceptions. Neighbors lack authority unless documented; outright denial conflicts with access rules.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b01-023
    fact(
        "ccma-transmission",
        "For which patient would Droplet Precautions be appropriate when infection is suspected?",
        "A patient with suspected pertussis with productive cough",
        [
            "A patient with C. difficile diarrhea",
            "A patient with airborne tuberculosis in a negative-pressure room",
            "A patient with intact skin and no infection",
        ],
        "Large-droplet illnesses such as pertussis require mask and spatial separation. C. difficile uses Contact Precautions; tuberculosis uses Airborne Precautions.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b01-024
    fact(
        "ccma-transmission",
        "An outpatient clinic triages a patient with fever and vesicular rash consistent with varicella. What precaution set is needed in addition to Standard Precautions?",
        "Airborne and Contact Precautions per policy, including isolation and PPE",
        [
            "Droplet Precautions with no mask",
            "No precautions because rash is visible",
            "Remove PPE before entering the room",
        ],
        "Varicella spreads by airborne and contact routes; combined precautions protect staff and other patients. Droplet alone is insufficient for varicella.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b01-025
    fact(
        "ccma-vaccines",
        "Where should most refrigerated vaccines be stored in the clinic?",
        "In a dedicated medical refrigerator with continuous temperature monitoring",
        [
            "In the staff lunch refrigerator next to food",
            "On a windowsill with direct sunlight",
            "In a freezer compartment for all products",
        ],
        "CDC storage guidance requires monitored, dedicated units to maintain the cold chain. Food refrigerators and freezing inappropriate products ruin potency.",
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        "beginner",
    ),
]
