# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""CCMA expansion batch 02 (25 hand-authored items)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-exp-b02-001
    fact(
        "ccma-foundational",
        "What plane divides the body into superior and inferior portions?",
        "Transverse (horizontal) plane",
        ["Sagittal plane", "Frontal plane", "Median plane"],
        "A transverse cut separates head from lower body regions. Sagittal planes divide right from left, which is a common plane mix-up.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-002
    fact(
        "ccma-foundational",
        "Which type of pathogen is a single-celled organism that may produce toxins?",
        "Bacterium",
        ["Virus", "Prion", "Vitamin"],
        "Bacteria are living cells that can multiply outside host cells. Viruses require host machinery, and prions are misfolded proteins without cells.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-003
    fact(
        "ccma-foundational",
        "A splash of blood lands on unbroken skin of a gloved hand during a procedure. What is the priority action after the event?",
        "Remove gloves, perform hand hygiene, and follow exposure protocol",
        [
            "Wipe with a dry paper towel and continue without reporting",
            "Apply lotion and return to the procedure room",
            "Ignore because the skin was intact",
        ],
        "OSHA bloodborne pathogen rules require prompt cleansing and evaluation after exposure. Intact skin still warrants protocol because permeability and microabrasions vary.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b02-004
    fact(
        "ccma-anatomy",
        "Which blood vessel carries deoxygenated blood from the right ventricle to the lungs?",
        "Pulmonary artery",
        ["Pulmonary vein", "Aorta", "Coronary sinus"],
        "Pulmonary arteries carry low-oxygen blood to the lungs for gas exchange. Pulmonary veins return oxygenated blood, reversing the everyday meaning of artery versus vein.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-005
    fact(
        "ccma-anatomy",
        "What is the primary function of the nephron in the kidney?",
        "Filter blood and form urine while regulating electrolytes",
        ["Pump blood to the systemic arteries", "Produce digestive enzymes", "Store bile for fat digestion"],
        "Nephrons filter plasma and adjust water and solute excretion. Cardiac pumping and bile storage belong to other organs.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-006
    fact(
        "ccma-anatomy",
        "Which structure prevents food from entering the trachea during swallowing?",
        "Epiglottis",
        ["Uvula", "Vocal cords at rest", "Hard palate"],
        "The epiglottis covers the glottis during swallowing. The uvula helps with speech and palatal closure but does not seal the airway alone.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-007
    fact(
        "ccma-anatomy",
        "A patient with a spinal cord injury at the cervical level may lose voluntary control of which function first?",
        "Diaphragmatic breathing and limb movement",
        ["Hearing and vision", "Hair growth rate", "Finger nail color"],
        "High cervical lesions can impair phrenic nerve function and major motor pathways. Sensory cranial functions and nail growth are not primary cervical motor concerns.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b02-008
    fact(
        "ccma-clinical-care",
        "When preparing a patient for a 12-lead EKG, why is hair clipped instead of shaved with a razor when needed?",
        "Clipping reduces skin abrasion that can irritate the site before electrode placement",
        ["Razor shaving improves ST segment accuracy on every patient", "Hair removal is unnecessary for any electrode", "Lotion should be applied under each pad"],
        "Gentle clipping improves contact without micro-cuts that sting or weep. Razors are reserved for orders because they can irritate skin and affect tracing quality.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-009
    fact(
        "ccma-clinical-care",
        "What is the correct order for donning personal protective equipment when both gown and gloves are required?",
        "Gown first, then mask or respirator, eye protection, then gloves",
        [
            "Gloves first, then gown over the gloves",
            "Eye protection after removing all other PPE",
            "Gown last so it stays outside the gloves",
        ],
        "CDC donning sequences keep glove cuffs overlapping the gown at the wrist. Gloves first tears the gown when removing equipment.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-010
    fact(
        "ccma-clinical-care",
        "A point-of-care glucose meter displays an error after a new test strip is inserted. What should the medical assistant do?",
        "Repeat quality control per manufacturer instructions before patient testing",
        [
            "Use the reading because the strip looks new",
            "Share strips between patients to save supplies",
            "Calibrate by wiping the strip with alcohol",
        ],
        "CLIA-waived devices still require control checks when errors occur. Patient strips are single use; alcohol can damage strip chemistry.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b02-011
    fact(
        "ccma-clinical-care",
        "Which action supports accurate pediatric weight measurement in an outpatient setting?",
        "Use a calibrated scale appropriate for the child's age and remove heavy outer clothing",
        [
            "Weigh the child while holding them without subtracting adult weight",
            "Place the scale on a thick carpet pad",
            "Estimate weight from shoe size",
        ],
        "Pediatric dosing and growth charts depend on accurate weight. Holding the child without taring adds adult mass; carpet throws off load cells.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-012
    fact(
        "ccma-coordination",
        "Why is closing the referral loop important after a specialist visit?",
        "It ensures consultation findings reach the primary team for ongoing care",
        [
            "It eliminates the need for future appointments",
            "It replaces the specialist's medical license",
            "It guarantees insurance payment without documentation",
        ],
        "Loop closure prevents lost results and medication changes from falling through. It does not remove follow-up needs or legal documentation requirements.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-013
    fact(
        "ccma-coordination",
        "A patient with limited English proficiency needs education about a new inhaler. What resource should be used?",
        "A qualified medical interpreter and translated materials when available",
        [
            "A bilingual receptionist unrelated to clinical care",
            "Hand gestures without involving the provider",
            "Written instructions in a language the patient does not read",
        ],
        "Qualified interpretation supports informed use of devices. Untrained staff or mismatched language materials increase error risk.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b02-014
    fact(
        "ccma-admin",
        "What is the purpose of an ICD-10-CM code on a health insurance claim?",
        "To report the patient's diagnosis or reason for the encounter",
        ["To list supply room inventory", "To document nursing shift hours", "To describe injection angle"],
        "ICD-10-CM codes justify medical necessity for services billed with CPT codes. They do not track staffing or technique details.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-015
    fact(
        "ccma-admin",
        "When verifying insurance eligibility, what key detail confirms active coverage on the date of service?",
        "Payer response showing plan status and effective dates for the patient",
        [
            "A verbal promise from the patient",
            "The color of the insurance card",
            "Whether the patient parked in the clinic lot",
        ],
        "Eligibility systems return structured benefit data tied to policy dates. Card appearance does not prove active enrollment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-016
    fact(
        "ccma-communication",
        "Which details belong in the Situation section of an SBAR handoff?",
        "A concise statement of the current problem and where the patient is located",
        [
            "A full social history back to childhood",
            "Billing codes for the last year",
            "Staff opinions about the patient's personality",
        ],
        "SBAR starts with the immediate clinical issue so the receiver can prioritize. Extensive social or financial data belong in Background when relevant.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-017
    fact(
        "ccma-communication",
        "A visibly upset patient speaks loudly in the waiting room. What is an appropriate first response?",
        "Move to a private area, lower your tone, and listen for the concern",
        [
            "Match their volume to assert control",
            "Ignore them until they leave",
            "Discuss other patients' wait times to distract them",
        ],
        "Privacy and calm communication support de-escalation. Public comparisons or shouting escalate tension and may breach confidentiality.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-018
    fact(
        "ccma-law-ethics",
        "What is the role of a medical assistant regarding scope of practice?",
        "Perform delegated tasks allowed by state law and supervising provider policy",
        [
            "Diagnose complex disease independently",
            "Prescribe schedule II opioids without oversight",
            "Interpret imaging studies for treatment plans",
        ],
        "MA scope is limited and supervised. Independent diagnosis and prescribing exceed typical MA authority in most states.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-019
    fact(
        "ccma-law-ethics",
        "A patient who is alert and oriented refuses a recommended blood draw. What should be documented?",
        "The refusal, education provided, and notification of the provider",
        [
            "That the patient was forced for their own good",
            "Nothing because refusal ends the visit",
            "Another patient's decision template",
        ],
        "Competent adults may refuse care; documentation supports continuity and legal clarity. Forced draws without due process violate autonomy.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b02-020
    fact(
        "ccma-hipaa",
        "Which disclosure is generally permitted without patient authorization for treatment purposes?",
        "Sharing relevant clinical information with another health care provider involved in care",
        [
            "Selling the diagnosis list to a marketing firm",
            "Posting photos of wounds on a personal blog",
            "Giving records to an employer for curiosity",
        ],
        "HIPAA permits TPO disclosures among involved professionals. Marketing and employer curiosity are not treatment purposes.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-021
    fact(
        "ccma-hipaa",
        "What is required before a business associate may handle electronic protected health information for a covered entity?",
        "A business associate agreement with required safeguards",
        [
            "A handshake in the parking lot",
            "Public posting of patient lists",
            "Shared employee social media passwords",
        ],
        "The Security Rule expects contractual obligations for vendors touching ePHI. Informal agreements do not replace BAAs.",
        [S.HHS_HIPAA_SECURITY, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b02-022
    fact(
        "ccma-transmission",
        "Which PPE is added for Contact Precautions when entering the room?",
        "Gown and gloves for all room entry",
        ["N95 respirator for every patient", "Street clothes with no hand hygiene", "Double gloves without gown"],
        "Contact isolation stops touch transmission of pathogens such as MRSA or C. difficile spores. N95 is for airborne precautions, not routine contact.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-023
    fact(
        "ccma-transmission",
        "Why is hand hygiene with soap and water emphasized for C. difficile prevention?",
        "Alcohol-based rubs do not reliably remove spores from hands",
        [
            "Soap increases spore production",
            "Gloves replace the need to clean hands after removal",
            "Spores are killed by air drying alone",
        ],
        "C. difficile spores resist alcohol rubs; mechanical washing helps remove them. Gloves do not replace hand hygiene after doffing.",
        [S.CDC_HAND_HYGIENE, S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b02-024
    fact(
        "ccma-vaccines",
        "Before giving an injectable vaccine, which \"right\" confirms the correct patient?",
        "Verify identity with at least two identifiers per facility policy",
        [
            "Use room number alone",
            "Ask the waiting room who wants a shot",
            "Rely on clothing color",
        ],
        "Two-identifier checks prevent wrong-patient immunization errors. Room numbers change and clothing is not unique.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b02-025
    fact(
        "ccma-vaccines",
        "A vaccine refrigerator alarm shows a temperature of 46°F (8°C) overnight. What is the first step?",
        "Document the event, relocate vaccines per protocol, and contact the immunization coordinator",
        [
            "Administer all vials immediately to avoid waste",
            "Silence the alarm and take no action",
            "Move vaccines to the freezer to cool faster",
        ],
        "Excursions require assessment before use; administering potentially compromised vaccine risks ineffective immunity. Freezing can destroy many products.",
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        "advanced",
    ),
]
