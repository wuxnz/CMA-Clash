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
        "Which body fluids are covered by OSHA's Bloodborne Pathogens Standard in typical healthcare exposure?",
        "Blood and certain other potentially infectious materials such as semen and cerebrospinal fluid",
        [
            "Perspiration on intact skin with no visible blood mixing",
            "Tears and sweat in the absence of visible blood contamination",
            "Urine and feces unless clearly mixed with visible blood in routine outpatient care during the same clinic visit",
        ],
        "The standard targets fluids associated with bloodborne pathogen transmission. Ordinary sweat and urine without blood are generally not regulated body fluids.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-002
    fact(
        "skill-osha-bbp",
        "What is an employer's duty regarding hepatitis B vaccine under the Bloodborne Pathogens Standard?",
        "Offer the vaccine at no cost to employees with occupational exposure risk",
        [
            "Require vaccination for all visitors to the clinic waiting room",
            "Charge employees full retail price for the three-dose series",
            "Provide vaccine after a documented needlestick injury without prior offer",
        ],
        "At-risk staff must be offered HBV vaccination free of charge after training. Post-exposure-only offers miss primary prevention.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-003
    fact(
        "skill-osha-bbp",
        "What must be included in an exposure control plan for bloodborne pathogens?",
        "Exposure determination, engineering and work practice controls, PPE, and post-exposure procedures",
        [
            "Annual supply budget targets without task-specific hazard controls",
            "Staff vacation rotation schedules with no exposure determination",
            "General HIPAA brochure text copied without work-practice controls",
        ],
        "OSHA expects a written plan tying hazards to controls and follow-up care. Non-safety administrative content does not satisfy the standard.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-004
    fact(
        "skill-osha-bbp",
        "When should employees receive bloodborne pathogen training?",
        "At hire, annually thereafter, and when tasks or procedures change",
        [
            "Once in high school regardless of current job duties",
            "When a patient compliments the cleanliness of the waiting room",
            "Every ten years if no injuries have been reported in routine outpatient care",
        ],
        "Training must match current job tasks and be refreshed on schedule. Infrequent or unrelated triggers do not meet OSHA requirements.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-005
    fact(
        "skill-osha-bbp",
        "What is the purpose of engineering controls for sharps injury prevention?",
        "Remove or isolate the hazard with devices such as safety needles and sharps containers",
        [
            "Rely on faster hand motion to avoid needle contact in routine outpatient care during the same clinic visit",
            "Place sharps in desk drawers until the end of the month",
            "Use thicker gloves instead of safety-engineered needles",
        ],
        "Engineering controls reduce risk before PPE alone. Drawer storage and glove thickness do not replace safer devices.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-006
    fact(
        "skill-osha-bbp",
        "How should contaminated sharps be discarded under OSHA rules?",
        "Immediately in closable, puncture-resistant, labeled containers",
        [
            "In unsecured cardboard boxes beside the exam table",
            "In patient trash cans if the needle looks small in routine outpatient care",
            "On the instrument tray for sterilization with reusable clamps",
        ],
        "Approved sharps containers prevent needlesticks during disposal and transport. Household waste and open trays create predictable injuries.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-007
    fact(
        "skill-osha-bbp",
        "What PPE is required when blood splash to the eyes is reasonably anticipated?",
        "Eye protection such as goggles or face shield in addition to other needed PPE",
        [
            "Street eyeglasses alone without side shields or face protection",
            "A surgical mask with no eye covering during arterial blood spray",
            "Gloves alone while cleaning a bloody floor with a mop in routine outpatient care",
        ],
        "Mucous membrane exposure can transmit hepatitis and HIV. Gloves alone do not protect eyes from splashes.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-008
    fact(
        "skill-osha-bbp",
        "When may employers require employees to pay for their own hepatitis B vaccination series?",
        "They may not require payment when vaccination is offered due to occupational exposure",
        [
            "When the employee declines the vaccine in writing after the offer",
            "When the employee works part time fewer than twenty hours weekly",
            "When the clinic is privately owned rather than hospital based in routine outpatient care",
        ],
        "The standard prohibits charging for employer-offered HBV vaccine for at-risk workers. Declination is documented, but the offer remains free.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-009
    fact(
        "skill-osha-bbp",
        "What should an employee do immediately after a needlestick with a used patient needle?",
        "Wash the area, report promptly, and seek medical evaluation per exposure protocol",
        [
            "Squeeze the wound and return to patient care without telling anyone",
            "Cover with a dry bandage and complete the patient schedule before reporting",
            "Discard the needle in regular waste and document nothing in routine outpatient care",
        ],
        "Early reporting enables source testing and post-exposure prophylaxis when indicated. Concealing sticks delays potentially life-saving treatment.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-010
    fact(
        "skill-osha-bbp",
        "Who maintains records of sharps injury logs under OSHA?",
        "The employer maintains a sharps injury log in addition to OSHA 300 logs when required",
        [
            "The injured employee alone keeps a personal diary at home in routine outpatient care during the same clinic visit",
            "The patient whose blood was involved files the log with OSHA",
            "The needle manufacturer submits the log after each shipment",
        ],
        "Employers track device-related injuries to evaluate control effectiveness. Patients and vendors are not responsible for workplace injury logs.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-011
    fact(
        "skill-osha-bbp",
        "What does work practice control mean in the Bloodborne Pathogens Standard?",
        "Policies and behaviors such as no recapping and hand hygiene that reduce exposure",
        [
            "Using the fastest needle gauge regardless of patient vein size",
            "Storing food with blood tubes in the same refrigerator shelf",
            "Wearing jewelry that tears gloves during phlebotomy in routine outpatient care during the same clinic visit",
        ],
        "Work practices complement engineering controls with safe habits. Food storage with specimens and torn gloves increase exposure.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-012
    fact(
        "skill-osha-bbp",
        "When is recapping a needle by hand acceptable?",
        "When using a one-handed scoop technique or a engineered recapping device per policy",
        [
            "Whenever two hands make recapping faster between patients",
            "When the sharps container is full and cannot be replaced today",
            "When the patient asks to keep the needle as a souvenir in routine outpatient care during the same clinic visit",
        ],
        "Two-handed recapping is a leading cause of sticks. Full containers must be replaced, not used to justify unsafe recapping.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-013
    fact(
        "skill-osha-bbp",
        "How should biohazard-labeled laundry be handled before leaving the facility?",
        "Bagged without rinsing or sorting in a leak-resistant container for approved laundering",
        [
            "Rinsed in the clinic sink to remove blood before home washing",
            "Sorted by color in the staff break room for fabric care in routine outpatient care during the same clinic visit",
            "Ironed at high heat in the clinic to sterilize without a vendor",
        ],
        "Agitating bloody linen in sinks creates splash exposure. Licensed laundry services follow heat and chemical standards for contaminated textiles.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-osha-bbp-014
    fact(
        "skill-osha-bbp",
        "What information should post-exposure evaluation include after a blood splash to nonintact skin?",
        "Source patient status when available, employee baseline labs, and follow-up testing schedule",
        [
            "The employee's preferred antibiotic started before occupational health is contacted",
            "Copayment balance and insurance authorization numbers for the employee account",
            "Hallway bulletin post describing the incident with patient identifiers",
        ],
        "Medical follow-up documents exposure route and guides prophylaxis decisions. Self-selected drugs and public posts are not substitutes for clinical evaluation.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-osha-bbp-015
    fact(
        "skill-osha-bbp",
        "Which pathogens are commonly emphasized in bloodborne pathogen training?",
        "Human immunodeficiency virus, hepatitis B virus, and hepatitis C virus",
        [
            "Common cold coronavirus and seasonal pollen allergens",
            "Lactose intolerance enzyme deficiency in adults",
            "Vitamin D deficiency from limited sun exposure in routine outpatient care",
        ],
        "HBV, HCV, and HIV drive workplace exposure policies and vaccination offers. Allergens and nutritional issues are outside BBP scope.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-016
    fact(
        "skill-osha-bbp",
        "What does universal precautions mean in OSHA bloodborne pathogen context?",
        "Treat all blood and certain body fluids as potentially infectious",
        [
            "Test every patient for HIV before any hand hygiene is performed",
            "Wear a respirator for every blood pressure measurement",
            "Dispose of all clinic waste as biohazard regardless of contamination",
        ],
        "Universal precautions assume infectivity without waiting for diagnosis. Full respirators and universal biohazard disposal are not required for every task.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-osha-bbp-017
    fact(
        "skill-osha-bbp",
        "When must personal protective equipment be provided to employees?",
        "At no cost when needed for occupational exposure to blood or OPIM",
        [
            "When the employee purchases scrubs from a specific vendor",
            "After three needlestick injuries occur in the same year in routine outpatient care",
            "When the employee signs a waiver accepting all infection risk",
        ],
        "Employers supply appropriate PPE for covered tasks. Waivers and injury thresholds do not replace provision requirements.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-018
    fact(
        "skill-osha-bbp",
        "How should regulated waste be labeled for transport within the facility?",
        "With biohazard symbol and red bags or containers where required by policy",
        [
            "With smiley face stickers to reduce patient anxiety in hallways",
            "With patient portraits to identify whose waste is inside in routine outpatient care",
            "With grocery lists taped to the outside for janitorial staff",
        ],
        "Biohazard labeling warns handlers to use precautions. Patient photos and unrelated notes do not meet communication requirements.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-019
    fact(
        "skill-osha-bbp",
        "What is the role of hepatitis B surface antibody testing after vaccination?",
        "Document immune response when recommended for occupational health programs",
        [
            "Replace the need for any further infection control training",
            "Prove the employee can reuse needles between patients safely",
            "Eliminate gloves during all future phlebotomy procedures in routine outpatient care",
        ],
        "Titer checks confirm seroconversion in some high-risk programs. Immunity does not relax safe injection or PPE practices.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-osha-bbp-020
    fact(
        "skill-osha-bbp",
        "Why should employees avoid bending or shearing needles before disposal?",
        "Breaking needles increases splash and stick risk without a safety benefit",
        [
            "Bent needles sterilize themselves when stored in a drawer",
            "Shearing is required before placing needles in sharps containers",
            "Broken needles are easier for patients to recap safely in routine outpatient care",
        ],
        "Needle manipulation causes unpredictable fractures and aerosols. Intact disposal in sharps containers is the safe practice.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-021
    fact(
        "skill-osha-bbp",
        "What should happen to a sharps container when it is three-quarters full?",
        "Close and replace it before overfilling causes protruding sharps",
        [
            "Pack more needles in by pressing down with gloved hands in routine outpatient care",
            "Leave it open until environmental services return next month",
            "Empty sharps into a larger trash bag to reuse the same box",
        ],
        "Overfilled containers cause needlesticks during disposal. Repacking and dumping violate OSHA and clinic policies.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-022
    fact(
        "skill-osha-bbp",
        "Which surface should be used to transport sealed sharps containers?",
        "A closed cart or carrier that prevents spills in hallways",
        [
            "An open top basket balanced on one hand while walking",
            "A patient wheelchair with the container on the lap in routine outpatient care",
            "A rolling desk chair with containers stacked on the seat",
        ],
        "Closed transport contains leaks if a tube cracks. Hand-carried open baskets drop sharps in public corridors.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-023
    fact(
        "skill-osha-bbp",
        "What does occupational exposure mean under the standard?",
        "Reasonably anticipated skin, eye, mucous membrane, or parenteral contact with blood or OPIM",
        [
            "Walking past a patient with a bandage in the waiting room",
            "Hearing about bloodborne diseases in a community lecture in routine outpatient care during the same clinic visit",
            "Typing blood results into the EHR without patient contact",
        ],
        "Exposure determination focuses on job tasks with contact potential. Incidental hallway presence without contact is not occupational exposure.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-024
    fact(
        "skill-osha-bbp",
        "When may an employee decline hepatitis B vaccination offered by the employer?",
        "After receiving mandated training and signing a declination form",
        [
            "Without training or documentation whenever personal preference changes",
            "If the employee pays a fee to the human resources office",
            "After contracting hepatitis B from a community source",
        ],
        "Declination must be informed and documented; employers still maintain the offer. Payment and community acquisition are not declination requirements.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-025
    fact(
        "skill-osha-bbp",
        "How should blood on intact clinic flooring be cleaned?",
        "Don PPE, absorb spill, clean, then disinfect with an appropriate germicide",
        [
            "Mop with plain water and leave wet signs without disinfectant",
            "Ask patients to walk through it to avoid delaying the schedule",
            "Cover with paper and leave until the weekend deep clean crew in routine outpatient care",
        ],
        "OSHA expects prompt cleanup with PPE and EPA-registered disinfectants. Delayed or water-only cleaning leaves viable pathogens.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-osha-bbp-026
    fact(
        "skill-osha-bbp",
        "What is the purpose of safer medical device evaluation in facilities?",
        "Select and implement needles and sharps with engineered injury protections",
        [
            "Choose the cheapest needles regardless of safety features in routine outpatient care",
            "Delay device upgrades until ten injuries occur per quarter",
            "Purchase decorative pens that look like syringes for training",
        ],
        "Employers must solicit frontline input when adopting safer sharps. Cost alone cannot override feasible safer alternatives.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-osha-bbp-027
    fact(
        "skill-osha-bbp",
        "Which action violates work practice controls during phlebotomy?",
        "Placing used needles on the bedspread while changing tubes",
        [
            "Using a safety needle with audible activation after the draw",
            "Discarding the holder and needle as a unit when policy requires",
            "Performing hand hygiene after removing gloves post-draw",
        ],
        "Free needles on soft surfaces roll and stick staff. Safety devices and immediate disposal align with OSHA expectations.",
        [S.OSHA_BBP, S.CLSI_GP41],
        "intermediate",
    ),
    # skill-osha-bbp-028
    fact(
        "skill-osha-bbp",
        "How long must employers retain training records for bloodborne pathogens?",
        "At least three years from the training date",
        [
            "Until the employee deletes their email account",
            "For thirty days after the annual picnic event",
            "When OSHA inspectors call the day before a visit",
        ],
        "Training documentation demonstrates compliance during audits. Informal retention fails the three-year minimum.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-029
    fact(
        "skill-osha-bbp",
        "What should be done with PPE that is torn during a bloody procedure?",
        "Remove it, perform hand hygiene, and don intact PPE before continuing care",
        [
            "Tape the tear with nonsterile office tape and keep working in routine outpatient care",
            "Turn the gown inside out to conceal the hole from the patient",
            "Finish the procedure bare-handed because gloves were mostly intact",
        ],
        "Compromised barriers require replacement to prevent exposure. Tape and bare-hand completion defeat the purpose of PPE.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-030
    fact(
        "skill-osha-bbp",
        "Why are eating and drinking restricted in areas where blood specimens are processed?",
        "To prevent ingestion of pathogens from contaminated surfaces or aerosols",
        [
            "To keep refrigerator temperatures stable for staff lunch items",
            "To reduce talking among coworkers during busy shifts in routine outpatient care",
            "To improve the taste of coffee brewed in the break room",
        ],
        "Food and drink in work areas cross-contaminate with splashes on cups and hands. Break rooms separate eating from specimen handling.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-osha-bbp-031
    fact(
        "skill-osha-bbp",
        "What does parenteral exposure mean in needlestick context?",
        "Entry through piercing of the skin including needle puncture",
        [
            "Breathing room air near a patient with a cough in routine outpatient care",
            "Shaking hands with a patient after hand hygiene",
            "Reading a laboratory report on a computer monitor",
        ],
        "Parenteral routes bypass skin barriers directly into tissue or blood. Casual contact without percutaneous injury is a different exposure type.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-032
    fact(
        "skill-osha-bbp",
        "When should gloves be worn under the Bloodborne Pathogens Standard?",
        "When hand contact with blood, OPIM, mucous membranes, or nonintact skin is anticipated",
        [
            "During every telephone call to schedule appointments in routine outpatient care during the same clinic visit",
            "While filing clean paper charts in a dry storage room",
            "When greeting patients in the lobby without touching surfaces",
        ],
        "Glove use follows anticipated contact with infectious materials. Administrative tasks without contact do not require gloves.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-033
    fact(
        "skill-osha-bbp",
        "How should employers respond when an employee requests safer sharps devices?",
        "Evaluate and implement appropriate devices as part of the exposure control plan",
        [
            "Dismiss the request unless fifty injuries occur first",
            "Tell staff to buy their own needles from a pharmacy in routine outpatient care during the same clinic visit",
            "Document the request then discard it without review",
        ],
        "Frontline feedback informs device selection mandated by OSHA. Ignoring feasible safer options violates the standard.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-osha-bbp-034
    fact(
        "skill-osha-bbp",
        "What documentation accompanies hepatitis B vaccine declination?",
        "Signed statement that the employee understands risks and had the opportunity to vaccinate",
        [
            "Verbal nod recorded in the employee's personal journal without a form",
            "Text message to a friend saying vaccines are unnecessary in routine outpatient care during the same clinic visit",
            "Blank form with no signature kept in an unlocked public folder",
        ],
        "Written declination proves informed refusal after training. Informal messages do not satisfy record requirements.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-035
    fact(
        "skill-osha-bbp",
        "Which practice reduces risk when passing sharps between team members?",
        "Using a neutral zone or placing instruments on a tray instead of hand-to-hand transfer",
        [
            "Tossing capped needles across the room to save walking steps",
            "Handing uncapped needles point-first to the receiver's palm",
            "Leaving needles in the provider's coat pocket for later in routine outpatient care during the same clinic visit",
        ],
        "Neutral zones keep both hands visible and away from sharp tips. Throwing or pocket storage causes predictable injuries.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-osha-bbp-036
    fact(
        "skill-osha-bbp",
        "What is required when housekeeping staff handle regulated waste?",
        "Training on hazards and PPE consistent with their exposure risk",
        [
            "No training because waste is sealed in red bags",
            "Street clothes without gloves for all trash regardless of label",
            "Relying on a one-page orientation handout without documented competency",
        ],
        "All workers with exposure risk need training and PPE, including environmental services. Sealed bags can still leak or puncture.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-037
    fact(
        "skill-osha-bbp",
        "Why must exposure incidents be documented even when the source patient is unknown?",
        "Follow-up care and OSHA recordkeeping depend on timely incident reports",
        [
            "Documentation replaces medical evaluation when the patient left",
            "Unknown sources mean no washing or lab testing is indicated in routine outpatient care",
            "Reports are filed when HIV is confirmed in the source and not before",
        ],
        "Employees still need wound care and baseline labs after undocumented-source sticks. Delay waits for impossible certainty.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-osha-bbp-038
    fact(
        "skill-osha-bbp",
        "What color coding is commonly used for biohazard warning labels?",
        "Fluorescent orange or orange-red background with the biohazard symbol",
        [
            "Pastel blue labels without symbols for aesthetic calm",
            "Green labels meaning eco-friendly regardless of contents",
            "Black labels hiding text from patients walking past in routine outpatient care",
        ],
        "OSHA specifies orange-red biohazard labels for regulated waste and containers. Decorative colors without symbols fail to warn handlers.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-039
    fact(
        "skill-osha-bbp",
        "How should employers make the exposure control plan available to employees?",
        "Accessible at the worksite during work hours without unnecessary delay",
        [
            "Locked in a director's home safe until requested by mail",
            "Summarized orally once with no written copy on site in routine outpatient care",
            "Posted on a public website unrelated to the clinic domain",
        ],
        "Workers must be able to review the plan where they work. Remote or oral-only access does not meet readiness requirements.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-040
    fact(
        "skill-osha-bbp",
        "What additional step applies when blood splashes into the mouth during a procedure?",
        "Rinse mouth, report exposure, and seek medical evaluation per protocol",
        [
            "Swallow saliva and continue without reporting mucous membrane contact",
            "Brush teeth at home eight hours later without occupational health visit",
            "Rinse with soda to neutralize virus in the oral cavity",
        ],
        "Mucous membrane exposures warrant the same urgent reporting as needlesticks. Delayed home care without documentation misses prophylaxis windows.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-osha-bbp-041
    fact(
        "skill-osha-bbp",
        "Which employee task typically requires inclusion in the exposure determination list?",
        "Phlebotomy and handling of specimens with visible blood",
        [
            "Remote billing from a home office without patient contact",
            "Landscaping exterior flower beds without entering the clinic",
            "Teaching a community yoga class off site on weekends",
        ],
        "Tasks with reasonable anticipation of blood contact belong in the exposure determination. Off-site roles without patient contact are generally excluded.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-042
    fact(
        "skill-osha-bbp",
        "What should a medical assistant know about confidentiality after reporting a needlestick?",
        "Employer medical records are kept confidential separate from the general personnel file",
        [
            "The incident must be posted on the clinic bulletin board for all staff",
            "The employee must tell every coworker the source patient's full name",
            "OSHA forbids any medical follow-up after exposure reporting in routine outpatient care during the same clinic visit",
        ],
        "Occupational health separates clinical follow-up from punitive personnel files. Gossip and public posting violate privacy expectations.",
        [S.OSHA_BBP, S.HHS_HIPAA_PRIVACY],
        "advanced",
    ),

]
