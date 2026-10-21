# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""CCMA expansion batch 05 (25 hand-authored items)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-exp-b05-001
    fact(
        "ccma-foundational",
        "What does the suffix \"-ectomy\" indicate in a surgical term?",
        "Surgical removal",
        ["Inflammation", "Enlargement", "Pertaining to"],
        "-ectomy means excision, as in appendectomy. -itis is inflammation; -megaly is enlargement.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-002
    fact(
        "ccma-foundational",
        "Which temperature route is considered core-adjacent for many adults when oral measurement is not possible?",
        "Rectal",
        ["Axillary", "Skin over the forearm", "Ear without probe cover"],
        "Rectal readings reflect core trends when oral is contraindicated. Axillary and uncovered probes are more variable.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-003
    fact(
        "ccma-foundational",
        "After a chemical splash to the eye in the clinic laboratory, what is the immediate priority?",
        "Flush the eye with water or saline per eyewash protocol for the recommended duration",
        [
            "Wait for symptoms before rinsing",
            "Apply contact lens solution and rub vigorously",
            "Document the event tomorrow",
        ],
        "Prompt irrigation dilutes caustic agents and limits corneal injury. Delay worsens chemical burns.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b05-004
    fact(
        "ccma-anatomy",
        "Where is cerebrospinal fluid primarily produced?",
        "Choroid plexus within the ventricles",
        ["Gallbladder mucosa", "Renal glomerulus", "Bone marrow cavity"],
        "Choroid plexus secretes CSF that circulates around the brain and spinal cord. Kidneys form urine, not CSF.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-005
    fact(
        "ccma-anatomy",
        "Which blood cell type is primarily responsible for hemostasis through plug formation?",
        "Platelets",
        ["Erythrocytes", "Lymphocytes", "Basophils"],
        "Platelets aggregate at injury sites to start clotting. Red cells carry oxygen; lymphocytes mediate adaptive immunity.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-006
    fact(
        "ccma-anatomy",
        "The adrenal cortex secretes hormones such as cortisol that help regulate:",
        "Metabolism and stress response",
        ["Red blood cell shape", "Pupil color", "Hair curl pattern"],
        "Cortisol influences glucose metabolism and anti-inflammatory pathways. RBC morphology and cosmetic traits are unrelated.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-007
    fact(
        "ccma-anatomy",
        "A patient with left-sided weakness and slurred speech is suspected of acute stroke. Which anatomic system is primarily affected?",
        "Central nervous system",
        ["Musculoskeletal system alone", "Integumentary system", "Reproductive system"],
        "Focal neuro deficits suggest brain or brainstem involvement. Skin or reproductive organs do not explain sudden unilateral weakness with speech change.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b05-008
    fact(
        "ccma-clinical-care",
        "When obtaining orthostatic vital signs, how many positions are typically compared?",
        "Supine, sitting, and standing",
        ["Standing once without baseline", "Prone underwater", "Trendelenburg for one hour"],
        "Orthostatic series detect postural blood pressure and pulse changes. A single standing reading without baseline lacks comparison.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-009
    fact(
        "ccma-clinical-care",
        "What is the correct angle for an intradermal injection such as a tuberculin skin test?",
        "5 to 15 degrees with bevel up",
        ["90 degrees into muscle", "45 degrees into subcutaneous fat of the abdomen", "180 degrees flat across bone"],
        "Intradermal tests form a bleb in the dermis. Ninety-degree angles are for typical IM vaccines, not Mantoux placement.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b05-010
    fact(
        "ccma-clinical-care",
        "Before assisting with suture removal, what assessment should occur?",
        "Inspect the wound for healing, drainage, and signs of infection",
        [
            "Pull every suture quickly without looking",
            "Soak the wound in hot coffee",
            "Reuse instruments from another patient without processing",
        ],
        "Providers evaluate readiness for suture removal. Infection or dehiscence requires different management than routine removal.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-011
    fact(
        "ccma-clinical-care",
        "When applying a heat pack, why is a cloth barrier placed between the pack and skin?",
        "To reduce risk of thermal burns",
        [
            "To keep the pack cold longer",
            "To measure blood glucose",
            "To sterilize the pack",
        ],
        "Thermal injuries occur quickly on sensitive or neuropathic skin. Barriers distribute temperature more safely.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-012
    fact(
        "ccma-coordination",
        "Why should patient education materials match literacy level?",
        "Plain language improves comprehension and adherence",
        [
            "Complex journal articles impress every patient",
            "Reading level is irrelevant to outcomes",
            "Pictures replace all verbal teaching",
        ],
        "Materials at appropriate literacy support self-care. Dense text without teach-back leaves gaps.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-013
    fact(
        "ccma-coordination",
        "A care plan for heart failure includes daily weight monitoring. What instruction supports the goal?",
        "Weigh at the same time each day on the same scale",
        [
            "Weigh once a year before holidays",
            "Switch scales randomly for variety",
            "Ignore two-pound changes",
        ],
        "Consistent technique detects fluid retention early. Infrequent or inconsistent weighing misses gradual gain.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-014
    fact(
        "ccma-admin",
        "What is coordination of benefits when a patient has two insurance plans?",
        "Rules that determine which plan pays first",
        [
            "A method to duplicate payment for the same service",
            "A nursing diagnosis code",
            "A type of surgical consent",
        ],
        "Primary and secondary payers follow contract order to avoid overpayment. It is not a clinical consent document.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-015
    fact(
        "ccma-admin",
        "When collecting a copayment, what receipt information helps the patient?",
        "Date, amount paid, and service location",
        [
            "Another patient's account number",
            "Staff home addresses",
            "Unrelated lab reference ranges",
        ],
        "Copay receipts support personal records and secondary billing. Other patients' identifiers must not appear.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-016
    fact(
        "ccma-communication",
        "Which behavior demonstrates empathy during intake?",
        "Acknowledging the patient's concern before moving to the next question",
        [
            "Interrupting to finish the script faster",
            "Staring at the computer without eye contact",
            "Dismissing worry as unimportant",
        ],
        "Brief empathetic statements build rapport and may reveal safety issues. Scripted rushing reduces disclosure.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-017
    fact(
        "ccma-communication",
        "During handoff to the provider, which Background detail is clinically useful for a patient with diabetes?",
        "Recent glucose readings and medication adherence",
        [
            "The color of the waiting room walls",
            "Unrelated celebrity news",
            "Parking validation codes",
        ],
        "Background supplies context for decision making. Environmental décor does not affect glycemic management.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-018
    fact(
        "ccma-law-ethics",
        "What is the purpose of an incident report after a patient fall?",
        "Support quality improvement and track safety trends",
        [
            "Assign blame in the medical record",
            "Replace required medical documentation",
            "Hide events from risk management",
        ],
        "Incident reports analyze systems; they do not substitute for charting care provided. Concealment violates policy and ethics.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-019
    fact(
        "ccma-law-ethics",
        "Accepting a large cash gift from a patient seeking preferential scheduling raises concerns about:",
        "Professional boundaries and undue influence",
        [
            "Improved infection control",
            "Better EKG electrode adhesion",
            "Accurate blood typing",
        ],
        "Gifts can compromise impartial care and violate policy. Clinical tests are unrelated to scheduling favors.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b05-020
    fact(
        "ccma-hipaa",
        "Which fax practice reduces misdirected protected health information?",
        "Verify the recipient number and use a confidentiality cover sheet",
        [
            "Send to the last number dialed without checking",
            "Include every diagnosis in the subject line shouted aloud",
            "Fax to the front desk printer in a public area without retrieval",
        ],
        "Confirmation and cover sheets limit wrong routing. Public unattended prints expose PHI.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-021
    fact(
        "ccma-hipaa",
        "A patient requests amendment of an error in their record. What is the covered entity's obligation?",
        "Review and respond per the Privacy Rule, accepting or denying with explanation",
        [
            "Ignore the request because charts are permanent",
            "Delete the entire chart",
            "Charge a fee to refuse automatically",
        ],
        "Patients have rights to request amendments with defined timelines. Wholesale deletion is not the pathway for correcting a single error.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b05-022
    fact(
        "ccma-transmission",
        "When transporting a patient on Airborne Precautions, what additional step is required?",
        "Have the patient wear a mask if tolerated and notify receiving staff",
        [
            "Remove all PPE in the elevator",
            "Discontinue precautions in the hallway",
            "Share a wheelchair without cleaning between patients",
        ],
        "Transport plans maintain precautions along the route. Hallway travel without masks spreads particles.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-023
    fact(
        "ccma-transmission",
        "Which action supports environmental cleaning after Contact Precautions discharge?",
        "Clean and disinfect high-touch surfaces per facility protocol",
        [
            "Leave linens for the next patient",
            "Delay room cleaning until the next week",
            "Store used PPE on the bed",
        ],
        "Pathogens such as C. difficile spores persist on surfaces. Visual tidiness does not equal disinfection.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b05-024
    fact(
        "ccma-vaccines",
        "Why is aspiration generally not recommended during routine vaccine injections?",
        "Vaccines are given intramuscularly where blood vessels are not routinely entered",
        [
            "Aspiration improves vaccine potency",
            "Aspiration is required for every deltoid injection",
            "Aspiration replaces the need for site rotation",
        ],
        "Current CDC administration guidance does not recommend aspiration for standard IM vaccines. Aspiration does not address site rotation or potency.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b05-025
    fact(
        "ccma-diabetes",
        "A patient brings a personal blood glucose log to clinic. How should the team use it?",
        "Review patterns with the patient and share relevant trends with the provider",
        [
            "Discard it without reading",
            "Post values on a public board",
            "Use it to bill without clinical review",
        ],
        "Home logs inform medication and lifestyle adjustments. Public display violates privacy; billing requires clinical relevance.",
        [S.NHA_CCMA],
        "beginner",
    ),
]
