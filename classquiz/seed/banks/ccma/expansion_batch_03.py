# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""CCMA expansion batch 03 (25 hand-authored items)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-exp-b03-001
    fact(
        "ccma-foundational",
        "What does the prefix \"hyper-\" mean in a medical term such as hypertension?",
        "Above normal or excessive",
        ["Below normal", "Painful", "Slow"],
        "Hyper- indicates increase, as in high blood pressure. Hypo- means deficient, which pairs as the classic terminology distractor.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-002
    fact(
        "ccma-foundational",
        "Medical asepsis differs from surgical asepsis because medical asepsis aims to:",
        "Reduce the number and spread of microorganisms",
        [
            "Eliminate every microorganism on all surfaces in the building",
            "Replace hand hygiene with perfume",
            "Sterilize lunchroom utensils for patients",
        ],
        "Clean technique lowers bioburden for noninvasive care. Sterility targets absence of microbes on instruments entering sterile fields.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-003
    fact(
        "ccma-foundational",
        "An employee reports a needlestick with a contaminated hollow-bore needle. What must happen immediately?",
        "Wash the area, report the exposure, and begin post-exposure evaluation per policy",
        [
            "Finish the clinic day before telling anyone",
            "Squeeze the wound until bleeding stops without cleansing",
            "Document as a patient allergy",
        ],
        "OSHA requires prompt reporting and medical follow-up for sharps injuries. Delayed care reduces prophylaxis options for bloodborne viruses.",
        [S.OSHA_NEEDLESTICK, S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b03-004
    fact(
        "ccma-anatomy",
        "Which organ produces bile that is stored in the gallbladder?",
        "Liver",
        ["Pancreas", "Spleen", "Appendix"],
        "Hepatocytes secrete bile; the gallbladder concentrates and releases it during fat digestion. The pancreas produces digestive enzymes and bicarbonate.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-005
    fact(
        "ccma-anatomy",
        "What is the main function of hemoglobin in red blood cells?",
        "Bind and transport oxygen",
        ["Produce antibodies", "Initiate blood clotting", "Destroy bacteria by phagocytosis"],
        "Hemoglobin carries oxygen from lungs to tissues. Platelets and white cells perform clotting and immune roles respectively.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-006
    fact(
        "ccma-anatomy",
        "Which valve separates the left atrium and left ventricle?",
        "Mitral (bicuspid) valve",
        ["Tricuspid valve", "Pulmonic valve", "Aortic valve"],
        "The mitral valve guards the left AV opening. Tricuspid is right-sided; pulmonic and aortic are semilunar valves leaving the ventricles.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-007
    fact(
        "ccma-anatomy",
        "A patient with dehydration may present with tachycardia and hypotension because:",
        "Lower circulating volume reduces venous return and stroke volume",
        [
            "Excess fluid expands the arteries without symptoms",
            "Heart rate slows to conserve oxygen",
            "Blood pressure rises from overhydration",
        ],
        "Hypovolemia decreases preload, triggering compensatory tachycardia while pressure falls. Overhydration typically raises volume, not the pattern described.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b03-008
    fact(
        "ccma-clinical-care",
        "When applying an elastic compression wrap for edema, in which direction should the wrap be applied?",
        "Distal to proximal with even overlap",
        [
            "Proximal to distal with gaps between layers",
            "Circular turns around the toes without covering the foot",
            "Random pattern to allow swelling",
        ],
        "Distal-to-proximal wrapping supports venous return. Gaps and reverse direction can create a tourniquet effect distally.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-009
    fact(
        "ccma-clinical-care",
        "What patient position is standard for measuring adult blood pressure at the upper arm?",
        "Seated with back supported, feet flat, and arm at heart level",
        [
            "Standing on one foot with arm raised overhead",
            "Prone with cuff on the ankle",
            "Supine with legs dangling off the exam table",
        ],
        "Heart-level arm placement and supported seating align with guideline technique. Ankle cuffs in prone adults are not the routine upper-arm method.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-010
    fact(
        "ccma-clinical-care",
        "A patient feels faint during venipuncture. What should the medical assistant do first?",
        "Stop the procedure and lower the patient safely to prevent injury",
        [
            "Tighten the tourniquet to finish quickly",
            "Leave the patient alone to recover privacy",
            "Continue drawing while the patient stands",
        ],
        "Vasovagal reactions require stopping the draw and protecting from falls. Completing the tube risks syncope and injury.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-011
    fact(
        "ccma-clinical-care",
        "During a minor in-office procedure, the assistant notices the sterile field was touched by a nonsterile sleeve. What is correct?",
        "Set up a new sterile field before continuing",
        [
            "Turn the drape so the wet side faces up",
            "Blow on instruments to dry them",
            "Proceed because the patient is cooperative",
        ],
        "Sterility is lost once nonsterile items contact the field. Drying or flipping drapes does not restore asepsis.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b03-012
    fact(
        "ccma-coordination",
        "What should a transition-of-care document include for safe handoffs?",
        "Medication list, allergies, pending tests, and follow-up plan",
        [
            "Staff lunch orders",
            "Unrelated marketing flyers",
            "Social security numbers of visitors",
        ],
        "Accurate med and allergy data prevent errors after discharge. Nonclinical identifiers do not support continuity.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-013
    fact(
        "ccma-coordination",
        "A recall notice identifies patients overdue for mammography screening. What is the goal of outreach?",
        "Prompt preventive care within guideline intervals",
        [
            "Increase duplicate testing without indication",
            "Replace shared decision making",
            "Bill for services that were not provided",
        ],
        "Recall systems close gaps in prevention. They should follow evidence-based intervals, not drive unnecessary duplicate imaging.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-014
    fact(
        "ccma-admin",
        "What is a deductible in a commercial health plan?",
        "The amount the patient pays for covered services before the plan begins sharing cost",
        [
            "A fixed copay collected at every visit",
            "The clinic's wholesale supply budget",
            "A code describing surgical procedures",
        ],
        "Deductibles are annual patient responsibility thresholds. Copays are per-visit amounts; CPT codes describe services, not plan design.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-015
    fact(
        "ccma-admin",
        "Why is accurate demographic data entry important at registration?",
        "It links results, bills, and correspondence to the correct individual",
        [
            "It allows sharing records with random callers",
            "It removes the need for patient identification later",
            "It guarantees clinical outcomes",
        ],
        "Wrong demographics cause merged charts and misdirected PHI. Identification and clinical quality still require ongoing verification.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-016
    fact(
        "ccma-communication",
        "Which elements belong in the chart note for a patient telephone call?",
        "Caller identity, symptoms discussed, advice given, and follow-up plan",
        [
            "Gossip about other staff members",
            "Credit card numbers in free text",
            "Unrelated patient names from the waiting room",
        ],
        "Objective triage notes support liability and continuity. Financial and third-party identifiers belong in secure payment workflows, not open chart text.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-017
    fact(
        "ccma-communication",
        "How can a medical assistant show respect for cultural differences during intake?",
        "Ask about preferences that affect care while maintaining safety standards",
        [
            "Refuse to use interpreters to save time",
            "Assume all patients share the same beliefs",
            "Dismiss dietary practices without discussion",
        ],
        "Cultural humility improves trust without abandoning evidence-based safety. Assumptions and dismissal erode engagement.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b03-018
    fact(
        "ccma-law-ethics",
        "What is fidelity in health care ethics?",
        "Keeping promises and being faithful to professional duties",
        [
            "Maximizing revenue regardless of need",
            "Sharing confidential information for entertainment",
            "Performing tasks outside training without telling anyone",
        ],
        "Fidelity supports reliability and trust in the patient relationship. Revenue focus or unauthorized practice violates ethical duties.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-019
    fact(
        "ccma-law-ethics",
        "Which situation may trigger mandatory reporting obligations?",
        "Reasonable suspicion of child abuse based on exam findings",
        [
            "A patient arriving late to an appointment",
            "Disagreement about copay amount",
            "Request for a different brand of bandage",
        ],
        "State laws require reporting suspected abuse of vulnerable populations. Scheduling and supply preferences are not reportable events.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-020
    fact(
        "ccma-hipaa",
        "Where should patient conversations about diagnoses occur to protect privacy?",
        "In private treatment areas away from public corridors",
        [
            "In a crowded elevator with visitors present",
            "At the front desk microphone",
            "In the cafeteria during lunch rush",
        ],
        "HIPAA safeguards oral disclosures; public areas risk incidental exposure. Private rooms or lowered voices in enclosed spaces reduce breaches.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-021
    fact(
        "ccma-hipaa",
        "A workforce member accesses a celebrity's chart out of curiosity without a job reason. What risk does this create?",
        "A privacy violation that may require investigation and sanction",
        [
            "Improved public relations for the clinic",
            "Automatic HIPAA waiver for all staff",
            "Permission to share records on social media",
        ],
        "Minimum necessary and role-based access prohibit curiosity browsing. Sanctions and breach analysis may follow unauthorized access.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b03-022
    fact(
        "ccma-transmission",
        "When should an N95 respirator be used in addition to Standard Precautions?",
        "When Airborne Precautions are required and the user is fit tested",
        [
            "For every routine blood glucose check",
            "When entering the break room",
            "Instead of hand hygiene after glove removal",
        ],
        "Fit-tested N95 filters small airborne particles for diseases such as tuberculosis. Routine point-of-care testing does not require respirators.",
        [S.CDC_ISOLATION_2007, S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-023
    fact(
        "ccma-transmission",
        "What distance guideline helps limit droplet transmission in clinic policy?",
        "Maintain spatial separation of about 3 to 6 feet when feasible",
        [
            "Stand within one inch without a mask",
            "Place infectious patients in the hallway",
            "Remove masks to improve hearing",
        ],
        "Large droplets fall quickly; distance and masks reduce exposure. Hallway placement and unmasked close contact increase spread.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b03-024
    fact(
        "ccma-vaccines",
        "Which documentation is required after administering a vaccine?",
        "Vaccine name, lot number, site, route, and administrator per policy",
        [
            "Patient favorite meal",
            "Parking spot number",
            "Unrelated vital signs from last year",
        ],
        "Immunization records support recall and adverse event investigation. Nonclinical trivia does not meet registry or legal documentation needs.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b03-025
    fact(
        "ccma-diabetes",
        "Why should a patient with diabetes inspect feet daily?",
        "Neuropathy can hide injury until infection develops",
        [
            "Foot exams replace HbA1c testing",
            "Shoes are unnecessary if vision is normal",
            "Glucose monitoring becomes optional",
        ],
        "Peripheral neuropathy reduces sensation, delaying wound care. Foot checks complement, not replace, glycemic monitoring and eye care.",
        [S.NHA_CCMA],
        "intermediate",
    ),
]
