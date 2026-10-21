# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""CCMA expansion batch 04 (25 hand-authored items)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-exp-b04-001
    fact(
        "ccma-foundational",
        "Which term describes a body position lying face up?",
        "Supine",
        ["Prone", "Lithotomy", "Trendelenburg"],
        "Supine means anterior surface up. Prone is face down; lithotomy involves raised legs for pelvic exams.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-002
    fact(
        "ccma-foundational",
        "What is the reservoir in the chain of infection?",
        "The place where pathogens live and multiply",
        ["The handwashing sink", "The billing computer", "The waiting room chair fabric"],
        "Reservoirs include humans, animals, or the environment where microbes persist. Equipment can transmit but is not the biologic reservoir itself.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-003
    fact(
        "ccma-foundational",
        "A clinic switches to a new EPA-registered surface disinfectant after a norovirus outbreak in the community. What training should staff receive?",
        "Proper dilution, contact time, and PPE for the new product",
        [
            "How to mix disinfectant with patient beverages",
            "That any cleaner works the same without reading labels",
            "How to store disinfectant in exam rooms unlocked",
        ],
        "Label instructions define kill claims and safe use. Misuse leaves viable viruses on surfaces and risks chemical exposure.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b04-004
    fact(
        "ccma-anatomy",
        "Which structure connects the pharynx to the stomach?",
        "Esophagus",
        ["Trachea", "Ureter", "Eustachian tube"],
        "The esophagus carries swallowed food and liquid. The trachea is an airway; ureters transport urine.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-005
    fact(
        "ccma-anatomy",
        "What is the primary role of the sinoatrial node?",
        "Initiate normal electrical impulses for heart rhythm",
        ["Filter blood before it enters the ventricles", "Produce red blood cells", "Secrete insulin"],
        "The SA node is the heart's intrinsic pacemaker. Filtration and insulin production occur in kidneys and pancreas.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-006
    fact(
        "ccma-anatomy",
        "Lymph nodes function mainly to:",
        "Filter lymph and support immune responses",
        ["Pump oxygenated blood to the brain", "Store bile between meals", "Produce cerebrospinal fluid"],
        "Lymph nodes trap antigens and house immune cells. Bile and CSF belong to hepatobiliary and central nervous systems.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-007
    fact(
        "ccma-anatomy",
        "An elderly patient with chronic obstructive pulmonary disease sits upright and leans forward to breathe. Which muscle group is working harder to expand the thoracic cavity?",
        "Accessory muscles of respiration including sternocleidomastoid and scalenes",
        [
            "Gastrocnemius in the calf",
            "Biceps brachii in the upper arm",
            "Orbicularis oculi around the eye",
        ],
        "Tripod positioning recruits neck and chest accessory muscles when diaphragm effort is insufficient. Limb and facial muscles do not expand the rib cage for ventilation.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b04-008
    fact(
        "ccma-clinical-care",
        "What is the purpose of peak expiratory flow measurement in asthma care?",
        "Monitor bronchospasm and response to therapy over time",
        [
            "Diagnose diabetes from a fingerstick",
            "Measure blood pressure in the ankle",
            "Assess visual acuity",
        ],
        "Peak flow reflects expiratory obstruction trends. Glucose, pressure, and vision use other devices and indications.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-009
    fact(
        "ccma-clinical-care",
        "When performing a snellen vision screening, how far is the chart typically placed?",
        "20 feet or equivalent simulated distance",
        ["6 inches from the nose", "Across the parking lot without calibration", "Behind the patient"],
        "Standardized distance keeps letter size comparable to the 20/20 notation. Uncalibrated distances invalidate results.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-010
    fact(
        "ccma-clinical-care",
        "A provider orders a urine pregnancy test on a random cup collected without label. What should the assistant do?",
        "Reject the specimen and recollect after two-identifier labeling",
        [
            "Run the test anonymously",
            "Use another patient's label to save time",
            "Dilute the sample with water",
        ],
        "Mislabeled specimens risk wrong-patient results with major consequences. Dilution alters analyte concentration.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b04-011
    fact(
        "ccma-clinical-care",
        "Which technique helps prevent specimen hemolysis during capillary blood collection?",
        "Allow a free-flowing drop to form without excessive squeezing",
        [
            "Milk the fingertip vigorously many times",
            "Reuse the lancet on the next patient",
            "Wipe alcohol and test while skin is dripping wet",
        ],
        "Aggressive squeezing lyses cells, raising potassium falsely. Single-use lancets and dry sites protect sample integrity.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-012
    fact(
        "ccma-coordination",
        "What is the benefit of using a patient portal for routine refill requests?",
        "Secure messaging that documents requests for the care team",
        [
            "Public posting of medication lists",
            "Automatic approval without provider review",
            "Sharing passwords among family members",
        ],
        "Portals create auditable threads within HIPAA controls. Refills still require clinical review; shared passwords undermine security.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-013
    fact(
        "ccma-coordination",
        "When coordinating home health services, which document must align with payer rules?",
        "Signed orders describing skilled needs and frequency",
        [
            "A handwritten grocery list",
            "Unrelated school transcripts",
            "Social media screenshots",
        ],
        "Payers require authorized plans of care. Nonclinical documents do not establish medical necessity for home visits.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-014
    fact(
        "ccma-admin",
        "What does accounts receivable aging track?",
        "How long patient and payer balances have remained unpaid",
        [
            "Vaccine refrigerator temperature trends",
            "Employee vacation accrual",
            "Suture removal dates",
        ],
        "AR aging supports collection workflows and cash flow analysis. Clinical device logs track different quality metrics.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-015
    fact(
        "ccma-admin",
        "A workers' compensation visit requires which registration detail?",
        "Employer name, injury date, and mechanism when known",
        [
            "Patient shoe size for billing",
            "Favorite television show",
            "Unrelated family member income",
        ],
        "Occupational claims need injury context for adjusters. Personal preferences do not satisfy regulatory billing fields.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-016
    fact(
        "ccma-communication",
        "What is an appropriate way to clarify a provider order that seems unclear?",
        "Repeat the order back and ask for clarification before acting",
        [
            "Guess the intent to save time",
            "Perform the task and chart later",
            "Ask another patient what they think",
        ],
        "Closed-loop communication prevents wrong-site or wrong-dose errors. Guessing bypasses the delegating provider's intent.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-017
    fact(
        "ccma-communication",
        "When serving patients with hearing loss, which strategy improves understanding?",
        "Face the patient and reduce background noise when possible",
        [
            "Turn away while speaking quickly",
            "Cover your mouth while talking",
            "Shout medical jargon from the doorway",
        ],
        "Visual cues and quiet environments aid lip reading and comprehension. Shouting from a distance adds noise without clarity.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-018
    fact(
        "ccma-law-ethics",
        "What does justice mean in health care ethics?",
        "Fair distribution of benefits and burdens of care",
        [
            "Treating friends before other patients regardless of need",
            "Hiding errors to protect the clinic image",
            "Charging random fees without policy",
        ],
        "Justice supports equitable access and triage by need. Favoritism and concealment violate ethical principles.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-019
    fact(
        "ccma-law-ethics",
        "A patient signs an advance directive refusing mechanical ventilation. The family demands intubation anyway. What guides the team?",
        "The patient's documented wishes if valid under state law",
        [
            "The loudest family member's preference",
            "Staff convenience",
            "Billing potential",
        ],
        "Valid advance directives express patient autonomy. Family wishes matter for surrogate decisions when the patient lacks capacity, but documented refusals control when applicable.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b04-020
    fact(
        "ccma-hipaa",
        "Which action helps secure electronic health record workstations?",
        "Log off or lock sessions when leaving the desk",
        [
            "Share login credentials with float staff",
            "Leave charts open in public view",
            "Disable passwords for speed",
        ],
        "Automatic timeouts and unique credentials protect ePHI under the Security Rule. Shared logins break audit trails.",
        [S.HHS_HIPAA_SECURITY, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-021
    fact(
        "ccma-hipaa",
        "A patient authorizes release of records to a specific attorney. What should be verified before sending?",
        "The authorization is signed, dated, and lists the correct recipient",
        [
            "The attorney's favorite sport",
            "Whether the mailroom is busy",
            "Other patients with similar names",
        ],
        "Valid authorizations specify who may receive PHI. Similar names require identity checks to avoid misdirected disclosures.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-exp-b04-022
    fact(
        "ccma-transmission",
        "Why are Transmission-Based Precautions used in addition to Standard Precautions?",
        "Certain diseases need extra barriers beyond routine practices",
        [
            "They eliminate the need for hand hygiene",
            "They apply to billing staff at home",
            "They replace cleaning of shared equipment",
        ],
        "Airborne, droplet, and contact precautions add PPE or placement steps. Standard Precautions and environmental cleaning remain baseline.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-exp-b04-023
    fact(
        "ccma-transmission",
        "A patient with suspected influenza is placed on Droplet Precautions. Which mask is appropriate for staff entering the room?",
        "Surgical or medical mask covering nose and mouth",
        [
            "No mask if vaccinated against unrelated diseases",
            "Oxygen mask on the staff member",
            "Cloth face covering worn under the chin",
        ],
        "Droplet precautions block large particles from coughs. Vaccination against other diseases does not remove mask need during infectious periods.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-024
    fact(
        "ccma-vaccines",
        "What should be done with a multidose vial after the beyond-use date on the label?",
        "Discard per policy even if liquid remains",
        [
            "Pool remaining doses for multiple patients",
            "Store at room temperature indefinitely",
            "Transfer to a food refrigerator",
        ],
        "Opened vials have limited stability to prevent bacterial growth and potency loss. Pooling doses between patients violates injection safety.",
        [S.CDC_INJECTION_SAFETY, S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-exp-b04-025
    fact(
        "ccma-diabetes",
        "Which finding during a foot exam should be reported promptly to the provider?",
        "A new open ulcer with surrounding erythema",
        [
            "Trimmed toenails from last week",
            "Normal skin temperature symmetry",
            "Presence of socks",
        ],
        "Open lesions with inflammation suggest infection risk in diabetes. Routine grooming or symmetric warmth are not acute warning signs.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
