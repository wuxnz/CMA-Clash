# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-osha-bbp)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-osha-bbp-001
    fact(
        "skill-osha-bbp",
        "Which workplaces does OSHA's Bloodborne Pathogens Standard (29 CFR 1910.1030) cover?",
        "Employers where workers may have occupational exposure to blood or other potentially infectious materials",
        [
            "Office buildings with no patient contact",
            "Patients visiting clinics without employees",
            "Retail stores without regulated waste",
        ],
        "The standard targets job-related exposure risk, not casual public contact. Clinical and laboratory staff with blood contact fall under the rule.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-002
    fact(
        "skill-osha-bbp",
        "What is an exposure control plan under OSHA 1910.1030?",
        "A written plan describing how the employer prevents and manages occupational bloodborne pathogen exposures",
        [
            "A marketing brochure about hospital ratings",
            "A list of patient favorite foods",
            "An optional memo with no employee access",
        ],
        "The plan lists responsibilities, engineering controls, and post-exposure steps. It must be available to workers, not kept secret.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-003
    fact(
        "skill-osha-bbp",
        "What does treating all blood and certain body fluids as potentially infectious reflect?",
        "Universal precautions integrated into Standard Precautions for healthcare",
        [
            "Using gloves for patients who appear ill and skipping them for others",
            "Testing every patient for HIV before hand hygiene",
            "Disposing of all linens in sharps containers",
        ],
        "Risk is not visible on appearance; barriers apply based on anticipated contact. HIV testing is not a prerequisite for basic precautions.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-osha-bbp-004
    fact(
        "skill-osha-bbp",
        "Which engineering control reduces needlestick injuries?",
        "Safety-engineered sharps devices and puncture-resistant disposal containers",
        [
            "Hand recapping needles after every injection",
            "Storing used needles in desk drawers",
            "Reusing syringes after rinsing with water",
        ],
        "Engineering controls remove hazards at the source. Recapping and reuse increase stick and contamination risk.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "beginner",
    ),
    # skill-osha-bbp-005
    fact(
        "skill-osha-bbp",
        "What work practice does OSHA emphasize for needles after use?",
        "Do not bend, break, or recap needles by hand except when no alternative exists per medical protocol",
        [
            "Pass unsheathed needles between coworkers hand to hand",
            "Clip needle tips with office scissors at the desk",
            "Place loose needles on the exam table for later pickup",
        ],
        "One-handed scoop technique is allowed only when required; routine hand recapping is prohibited. Passing bare needles spreads injury risk.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-006
    fact(
        "skill-osha-bbp",
        "When must employers offer hepatitis B vaccination to at-risk workers who are not already immune?",
        "Within 10 working days of initial assignment to tasks with occupational exposure, at no cost to the employee",
        [
            "After three documented needlestick injuries",
            "One year after hire regardless of tasks",
            "With the employee paying full market price as a condition of employment",
        ],
        "OSHA requires timely free offer with declination process when declined. Waiting for injury defeats primary prevention.",
        [S.OSHA_BBP, S.CDC_VACCINE_ADMIN],
        "beginner",
    ),
    # skill-osha-bbp-007
    fact(
        "skill-osha-bbp",
        "Which personal protective equipment may be needed for anticipated blood or body fluid splashes?",
        "Gloves plus gown, mask, and eye protection matched to the exposure",
        [
            "Open-toed sandals and short sleeves",
            "Gloves alone when large-volume arterial spray is expected",
            "No barriers if the worker received hepatitis B vaccine",
        ],
        "PPE selection follows splash risk, not vaccination status. Vaccination does not replace barriers for wet procedures.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-osha-bbp-008
    fact(
        "skill-osha-bbp",
        "What should an employee do first after a needlestick with potential blood exposure?",
        "Wash the area with soap and water, report the incident promptly, and seek post-exposure evaluation",
        [
            "Squeeze the wound to bleed into a trash can",
            "Wait one week to see if symptoms develop before telling anyone",
            "Apply oral suction to the puncture site",
        ],
        "Immediate cleansing and reporting enable timely labs and prophylaxis. Delay and aggressive squeezing worsen outcomes.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "beginner",
    ),
    # skill-osha-bbp-009
    fact(
        "skill-osha-bbp",
        "What does a biohazard label on a container communicate?",
        "The contents include regulated medical waste or contaminated materials requiring special handling",
        [
            "The box holds clean office paper for recycling",
            "The bag contains patient lunch leftovers",
            "The jar stores nonsterile water for plants",
        ],
        "Labels warn handlers about infectious risk. Food and clean paper do not carry biohazard markings.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-010
    fact(
        "skill-osha-bbp",
        "How often must bloodborne pathogen training occur for at-risk employees?",
        "At initial assignment and at least annually, plus when tasks or procedures change risk",
        [
            "Once in a lifetime at high school graduation",
            "After each paycheck is issued",
            "When an injury occurs and at no other time",
        ],
        "Annual refresher maintains competency on the exposure control plan. Injury-only training misses prevention before exposure.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-011
    fact(
        "skill-osha-bbp",
        "How should laundry contaminated with blood be handled before washing?",
        "Place it in leak-proof bags with minimal agitation and follow facility laundering policy",
        [
            "Shake linens vigorously in the hallway to remove stains",
            "Send bags home with the patient for home washing without instructions",
            "Mix contaminated linens with clean towels in open hampers",
        ],
        "Gentle handling limits aerosolization and contact with skin. Home laundering of clinical linens bypasses regulated processing.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-osha-bbp-012
    fact(
        "skill-osha-bbp",
        "Why is hepatitis B considered more transmissible than HIV via needlestick?",
        "Higher viral load in blood and greater environmental stability of hepatitis B virus",
        [
            "Hepatitis B spreads through casual conversation",
            "HIV is transmitted by touching intact patient skin",
            "Neither virus can enter through percutaneous injury",
        ],
        "Percutaneous exposure risk varies by pathogen concentration. Casual touch without blood contact is not a typical HIV route.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-osha-bbp-013
    fact(
        "skill-osha-bbp",
        "When should a sharps container be replaced or emptied?",
        "When fill reaches the manufacturer mark and before items protrude from the opening",
        [
            "Once per calendar year regardless of fill level",
            "When needles spill onto the floor for easier pickup",
            "When the container is light enough to juggle",
        ],
        "Overfilled containers cause needle sticks during disposal. Calendar schedules ignore hazardous overflow.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-014
    fact(
        "skill-osha-bbp",
        "What must the exposure control plan describe regarding hepatitis B vaccination?",
        "How vaccination is offered, documented, and managed when an employee declines",
        [
            "How to charge employees triple cost for vaccine",
            "How to hide vaccine records from occupational health",
            "How patients administer vaccines to staff",
        ],
        "OSHA mandates free offer with declination statements. Concealing records or shifting cost to employees violates the standard.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-015
    fact(
        "skill-osha-bbp",
        "Which fluids are examples of other potentially infectious materials (OPIM) under OSHA?",
        "Semen, vaginal secretions, cerebrospinal fluid, and fluid visibly contaminated with blood",
        [
            "Tears and sweat in every situation without exception",
            "Intact skin flakes from routine dry brushing",
            "Plain drinking water in a patient cup",
        ],
        "OPIM lists specific body fluids; sweat is not included unless visibly bloody. Ordinary environmental dust is not OPIM.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-016
    fact(
        "skill-osha-bbp",
        "What documentation follows an employee's declination of hepatitis B vaccine?",
        "A signed declination form retained per OSHA requirements while preserving future offer",
        [
            "Termination of employment automatically",
            "Permanent waiver of all post-exposure care",
            "Public posting of the employee's name",
        ],
        "Declination is allowed but must be informed and documented. It does not eliminate exposure evaluation after incidents.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-017
    fact(
        "skill-osha-bbp",
        "How should contaminated broken glass be collected?",
        "Use mechanical means such as brush and dustpan, not bare hands",
        [
            "Pick up shards with gloved fingers pressed together",
            "Blow glass particles off the floor with compressed air toward coworkers",
            "Wrap shards in gauze and recap like a needle",
        ],
        "Mechanical pickup reduces cuts that could allow blood contact. Compressed air disperses hazardous particles.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-018
    fact(
        "skill-osha-bbp",
        "What is the employer's role after documenting a sharps injury?",
        "Provide timely post-exposure evaluation and follow-up at no cost to the employee",
        [
            "Require the employee to use personal vacation for all clinic visits",
            "Discourage reporting to keep injury logs low",
            "Delay evaluation until the next annual training",
        ],
        "OSHA expects prompt medical follow-up including source testing when feasible. Discouraging reports undermines prevention programs.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-019
    fact(
        "skill-osha-bbp",
        "Why maintain a sharps injury log?",
        "To track device types and trends so safer engineering controls can be selected",
        [
            "To replace employee medical records",
            "To publish patient names associated with injuries",
            "To eliminate the need for training updates",
        ],
        "Log analysis guides device purchases and work practice changes. It supplements, not replaces, individual health records.",
        [S.OSHA_NEEDLESTICK, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-020
    fact(
        "skill-osha-bbp",
        "When may regulated waste leave the facility?",
        "According to state and local rules with proper labeling, containment, and licensed transport when required",
        [
            "In personal vehicles without documentation",
            "Mixed with municipal recycling bins at curbside",
            "Burned in a clinic break room trash can",
        ],
        "Medical waste chains use licensed haulers and manifests where mandated. Household recycling and open burning are unsafe and illegal in most settings.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-021
    fact(
        "skill-osha-bbp",
        "How should gloves be managed after caring for a patient with visible blood on gloves?",
        "Remove gloves without contaminating skin, perform hand hygiene, and don new gloves before the next task",
        [
            "Wipe gloves on the uniform and reuse for the next patient",
            "Wash gloves with lotion and air dry for tomorrow",
            "Store used gloves in a pocket for later",
        ],
        "Gloves are single-patient barriers when soiled. Reuse spreads pathogens and violates Standard Precautions.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-022
    fact(
        "skill-osha-bbp",
        "What training content must bloodborne pathogen education include?",
        "Modes of transmission, use of engineering controls and PPE, and steps after an exposure incident",
        [
            "Restaurant menu planning for the cafeteria",
            "Social media marketing for the clinic",
            "Stock trading tips for employees",
        ],
        "Training aligns behavior with the exposure control plan. Unrelated business topics do not satisfy OSHA elements.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-023
    fact(
        "skill-osha-bbp",
        "How should eating and drinking be managed in work areas with reasonable likelihood of blood exposure?",
        "Prohibited in areas where contamination could transfer to the mouth",
        [
            "Encouraged at the same counter where specimens are labeled",
            "Required while processing bloody trays without gloves",
            "Allowed inside biohazard bags for convenience",
        ],
        "Separating food from contamination zones prevents ingestion of pathogens. Specimen areas are not break rooms.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-024
    fact(
        "skill-osha-bbp",
        "What does hepatitis B vaccine series completion aim to provide?",
        "Immunity documented by titer or completion per CDC schedule when indicated",
        [
            "Immunity to all bloodborne viruses including HIV",
            "Permission to reuse needles between patients",
            "Exemption from hand hygiene after patient care",
        ],
        "HBV vaccine targets hepatitis B, not HIV or HCV. Vaccination does not relax sharps safety or hygiene.",
        [S.OSHA_BBP, S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-osha-bbp-025
    fact(
        "skill-osha-bbp",
        "Which action violates OSHA work practices during phlebotomy cleanup?",
        "Placing used needles in a regular trash receptacle",
        [
            "Activating the safety device immediately after withdrawal",
            "Disposing of the intact needle assembly in a sharps container",
            "Wearing gloves when antiseptic is applied before the draw",
        ],
        "Sharps belong in approved containers, not solid waste. Safety devices and gloves align with the standard.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-026
    fact(
        "skill-osha-bbp",
        "How should employers review the exposure control plan?",
        "At least annually and when new devices or procedures change exposure risk",
        [
            "When an OSHA citation arrives and at no other time",
            "Every twenty years regardless of practice changes",
            "By deleting the plan after the first training session",
        ],
        "Annual review keeps engineering controls current. Reactive-only updates miss trends seen in injury logs.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-027
    fact(
        "skill-osha-bbp",
        "What should happen if PPE is torn or penetrated by blood during a procedure?",
        "Remove the compromised PPE, clean exposed skin, and report potential exposure per policy",
        [
            "Continue the procedure with torn gloves to save time",
            "Tape the tear and finish the day without hand washing",
            "Share the torn gloves with a colleague to reduce waste",
        ],
        "Broken barriers may constitute an exposure requiring evaluation. Continuing with torn PPE increases contact with blood.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-osha-bbp-028
    fact(
        "skill-osha-bbp",
        "Who should have access to the exposure control plan?",
        "Employees with occupational exposure and involved management or safety staff",
        [
            "Competitors and media by default",
            "Patients' visitors in the waiting room",
            "No employees; oral summaries are sufficient",
        ],
        "Workers need the written plan to follow post-exposure steps. Public release and oral-only versions do not meet accessibility requirements.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-029
    fact(
        "skill-osha-bbp",
        "How are specimens of blood or OPIM transported within the clinic?",
        "In closed, leak-proof containers labeled with biohazard warning when required",
        [
            "In open cups carried above the head",
            "In employee lunch bags without labeling",
            "By pouring samples into hand sanitizer bottles",
        ],
        "Leak-proof labeled containers protect handlers during internal transport. Food containers and open carriers risk spills.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-030
    fact(
        "skill-osha-bbp",
        "What is the purpose of source-patient testing after an occupational exposure?",
        "To guide post-exposure prophylaxis decisions when consent or legal authority allows testing",
        [
            "To publish the patient's HIV status in the staff lounge",
            "To deny care to the source patient",
            "To replace employee baseline labs",
        ],
        "Source status informs clinician recommendations for the exposed worker. Results remain confidential and do not replace employee follow-up labs.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-031
    fact(
        "skill-osha-bbp",
        "A new medical assistant starts phlebotomy duties Monday. When should hepatitis B vaccine be offered?",
        "Within 10 working days of assignment to tasks with occupational exposure unless already immune or previously offered",
        [
            "After the first documented needlestick injury",
            "Six months after hire if the employee requests pay",
            "Hepatitis B vaccine is optional with no employer offer required",
        ],
        "OSHA sets a clear deadline from assignment to at-risk tasks. Injury-triggered or employee-paid-only offers do not meet the standard.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-032
    fact(
        "skill-osha-bbp",
        "During a suture removal, blood splashes toward the MA's face. Which PPE combination was missing?",
        "Mask and eye protection in addition to gloves",
        [
            "Hairnet intended for food service",
            "Steel-toe boots for hallway walking",
            "Double gloves with no face shield for splash",
        ],
        "Mucous membrane exposure risk requires face protection during splash-prone tasks. Gloves alone leave eyes and mouth vulnerable.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-osha-bbp-033
    fact(
        "skill-osha-bbp",
        "An MA recaps a needle by hand after an IM injection because the sharps box is across the room. What is the safest correction?",
        "Activate the safety device if present, carry the used sharp to the container without recapping, and report container placement as a hazard",
        [
            "Continue hand recapping to save steps",
            "Leave the uncapped needle on the counter until end of shift",
            "Place the needle in a biohazard bag meant for soft waste",
        ],
        "Hand recapping is prohibited unless no safer alternative exists. Needles belong in sharps containers, not soft waste bags.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-osha-bbp-034
    fact(
        "skill-osha-bbp",
        "A housekeeper finds linens soaked with blood in a patient room. What handling aligns with OSHA laundry requirements?",
        "Wear gloves, bag minimally agitated linen in leak-proof bags, and send for processing per facility policy",
        [
            "Sort the linen with bare hands in the hallway",
            "Take the bag home to wash with household detergent",
            "Shake the linen outside to dry before the washer",
        ],
        "Gloved minimal handling reduces skin contact and aerosols. Home laundering bypasses regulated infection control processes.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-035
    fact(
        "skill-osha-bbp",
        "After a splash of blood into the eye during a procedure, what sequence matches post-exposure expectations?",
        "Flush mucous membranes with water, report immediately, and begin occupational health evaluation per protocol",
        [
            "Finish the procedure before mentioning the splash",
            "Apply contact lens solution as a substitute for reporting",
            "Wait for annual training to document the event",
        ],
        "Mucous membrane exposures need prompt irrigation and medical assessment. Delay reduces options for prophylaxis when indicated.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-osha-bbp-036
    fact(
        "skill-osha-bbp",
        "The sharps injury log shows repeated sticks from the same insulin syringe model. What employer action follows OSHA prevention hierarchy?",
        "Evaluate safer devices and update the exposure control plan with implementation dates",
        [
            "Tell staff to be more careful without changing devices",
            "Remove sharps containers to reduce clutter",
            "Stop reporting sticks to keep log numbers low",
        ],
        "Engineering control review is required when patterns emerge. Hiding injuries or removing containers increases risk.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-osha-bbp-037
    fact(
        "skill-osha-bbp",
        "A student observer in clinic is assigned to handle contaminated sharps. What training rule applies?",
        "Training must occur before assignment to tasks with occupational exposure at no cost during work hours",
        [
            "Observers are exempt from all bloodborne pathogen rules",
            "Training may be billed to the student after an injury",
            "Training is required after graduation from the program",
        ],
        "OSHA covers employees and includes trainees with exposure risk. Preplacement training prevents first-day injuries.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-038
    fact(
        "skill-osha-bbp",
        "Containers of regulated waste are stored in a utility room. What labeling is required?",
        "Biohazard label or color coding per OSHA on containers holding blood or OPIM waste",
        [
            "No label if staff memorize room layout",
            "Smiley face stickers to reduce anxiety",
            "Food-grade labels indicating contents are edible",
        ],
        "Labels communicate hazard to all handlers, including relief staff. Informal memory or misleading icons do not substitute.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-039
    fact(
        "skill-osha-bbp",
        "An employee declined hepatitis B vaccine last year but now wants the series after a near-miss exposure. What is appropriate?",
        "Provide the vaccine offer again at no cost and document acceptance per occupational health protocol",
        [
            "Refuse because declination is permanent for life",
            "Charge full price because of the prior declination",
            "Require the employee to obtain vaccine at a retail pharmacy without support",
        ],
        "Declination is not a permanent waiver of future offers. Employers still provide vaccination without penalty after reconsideration.",
        [S.OSHA_BBP, S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-osha-bbp-040
    fact(
        "skill-osha-bbp",
        "During training, staff ask whether cosmetic contact with intact patient skin requires the same PPE as blood draws. What answer reflects OSHA focus?",
        "PPE is selected based on reasonably anticipated contact with blood or OPIM, not casual intact skin touch",
        [
            "Full surgical garb is required for handshakes",
            "No hand hygiene is needed after any patient contact",
            "Gowns are required for every phone call with a patient",
        ],
        "Anticipated exposure drives PPE; intact skin contact without blood is addressed by hand hygiene per Standard Precautions. Overuse and underuse both miss the risk assessment.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-osha-bbp-041
    fact(
        "skill-osha-bbp",
        "A courier picks up red biohazard bags from the clinic. What documentation may be required off-site?",
        "Tracking forms or manifests per state rules for regulated medical waste transport",
        [
            "Patient social security numbers on the bag exterior",
            "Menu orders from the cafeteria",
            "Personal vacation requests of the driver",
        ],
        "Waste tracking ensures proper disposal chain of custody. PHI belongs inside secure records, not on waste exteriors.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-042
    fact(
        "skill-osha-bbp",
        "An MA with a fresh needlestick reports that the source patient left before identification. What employer obligation remains?",
        "Provide post-exposure evaluation, baseline labs for the employee, and follow protocol even when source is unknown",
        [
            "Dismiss the incident because the patient departed",
            "Wait until the patient returns next year for labs",
            "Document the stick but deny any medical follow-up",
        ],
        "Unknown source status still requires employee care pathways. Delaying evaluation forfeits timely prophylaxis options.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
]
