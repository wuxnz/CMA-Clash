# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-infection)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-infection-001
    fact(
        "skill-infection",
        "Who is covered by CDC Standard Precautions in outpatient medical assisting care?",
        "All patients regardless of suspected or confirmed infection status",
        [
            "Patients with visible respiratory symptoms alone",
            "Patients who have a positive culture on the chart",
            "Patients in surgical suites but not exam rooms",
        ],
        "Standard Precautions are the baseline for every encounter. Limiting them to labeled infections misses unrecognized colonization and blood exposure risk.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-infection-002
    fact(
        "skill-infection",
        "What is the primary purpose of hand hygiene in healthcare settings?",
        "Reduce transmission of pathogens on hands to patients, surfaces, and staff",
        [
            "Replace the need for gloves during blood draws",
            "Eliminate the need to clean reusable equipment",
            "Shorten room turnover without surface cleaning",
        ],
        "Hands are a common vehicle for cross-contamination. Gloves and equipment reprocessing remain separate infection control layers.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-infection-003
    fact(
        "skill-infection",
        "When is alcohol-based hand rub an appropriate choice before touching a patient?",
        "When hands are not visibly soiled and the product is allowed by policy",
        [
            "When hands are covered in blood before gloving",
            "After providing care for a patient with Clostridioides difficile diarrhea",
            "When soap and water is available and hands are visibly dirty",
        ],
        "Alcohol rub works well on visibly clean hands. Spores and heavy soil need mechanical washing with soap and water.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-infection-004
    fact(
        "skill-infection",
        "After caring for a patient with suspected Clostridioides difficile, which hand hygiene method is preferred?",
        "Wash hands with soap and water",
        [
            "Use alcohol-based hand rub as the sole method",
            "Wipe hands with a dry paper towel without washing",
            "Apply lotion and don gloves without cleaning hands",
        ],
        "Alcohol does not reliably remove C. difficile spores from hands. Friction and rinsing with soap and water are needed.",
        [S.CDC_HAND_HYGIENE, S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-005
    fact(
        "skill-infection",
        "How should alcohol-based hand rub be applied for effective use?",
        "Cover all hand surfaces and rub until the product is completely dry",
        [
            "Apply to palms and wipe off after five seconds",
            "Rinse hands with water immediately after application",
            "Use a single drop on one finger for both hands",
        ],
        "Contact time depends on keeping the product on the skin until dry. Rinsing or wiping shortens antimicrobial effect.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-infection-006
    fact(
        "skill-infection",
        "Which activity requires hand hygiene even if gloves were worn during patient care?",
        "Before documenting, touching a keyboard, or leaving the room",
        [
            "Before entering the room while gloves remain on from the prior patient",
            "After removing gloves when hands look clean",
            "Before donning gloves after hand hygiene at the start of care",
        ],
        "Gloves can develop microtears and hands may become contaminated during removal. Cleaning hands after glove removal protects the environment and coworkers.",
        [S.CDC_HAND_HYGIENE, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-007
    fact(
        "skill-infection",
        "What does contact precautions aim to prevent?",
        "Spread of organisms by direct or indirect contact with the patient or environment",
        [
            "Spread of tuberculosis through ventilation ducts alone",
            "Exposure to ionizing radiation in the imaging suite",
            "Medication errors during prescription entry",
        ],
        "Contact precautions add gown and gloves for touch-related transmission. Airborne TB control and medication safety use different measures.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-008
    fact(
        "skill-infection",
        "Which PPE is typically added for contact precautions beyond Standard Precautions?",
        "Gown and gloves for all room entry and patient contact",
        [
            "Powered air-purifying respirator for every visit",
            "Sterile surgical mask for routine vital signs",
            "Lead apron during conversation at the doorway",
        ],
        "Gowns and gloves reduce transfer of resistant organisms from skin and surfaces. Respirators and lead aprons address unrelated hazards.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # skill-infection-009
    fact(
        "skill-infection",
        "When are droplet precautions indicated?",
        "For pathogens spread by large respiratory droplets at close range",
        [
            "For every patient with a runny nose in primary care",
            "For all patients who are ambulatory in the hallway",
            "For patients who need contact precautions for MRSA colonization",
        ],
        "Droplet precautions target specific organisms such as influenza or pertussis per policy. MRSA colonization usually warrants contact, not droplet, precautions.",
        [S.CDC_ISOLATION_2007],
        "beginner",
    ),
    # skill-infection-010
    fact(
        "skill-infection",
        "Which mask type is commonly used for droplet precautions during close patient care?",
        "Surgical or procedure mask that covers nose and mouth",
        [
            "Cloth face covering stored in a personal locker",
            "Oxygen nasal cannula without a mask",
            "Face shield worn without any mask",
        ],
        "Surgical masks block large droplets generated by coughs and sneezes. Shields alone leave gaps for inhalation of droplets.",
        [S.CDC_ISOLATION_2007],
        "beginner",
    ),
    # skill-infection-011
    fact(
        "skill-infection",
        "What patient placement is preferred for airborne precautions when a negative-pressure airborne infection isolation room is available?",
        "Private room with negative pressure and door closed",
        [
            "Semi-private room with curtain between beds",
            "Waiting room chair near the reception desk",
            "Hallway gurney with high-flow fans toward other patients",
        ],
        "Airborne precautions require containment of small particle aerosols. Shared air spaces increase exposure to others.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-012
    fact(
        "skill-infection",
        "Which respirator is used for airborne precautions such as suspected pulmonary tuberculosis?",
        "Fit-tested N95 or higher-level particulate respirator per policy",
        [
            "Loose surgical mask with gaps at the cheeks",
            "Simple cloth mask from home laundry",
            "Oxygen mask set at two liters per minute",
        ],
        "N95 respirators filter airborne particles when fit-checked. Surgical and cloth masks do not provide the same fitted filtration.",
        [S.CDC_ISOLATION_2007, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-infection-013
    fact(
        "skill-infection",
        "What is a key element of respiratory hygiene and cough etiquette in the waiting area?",
        "Provide tissues, hands-free waste containers, and hand hygiene supplies",
        [
            "Seat all coughing patients next to the reception printer",
            "Discourage mask use so speech is easier to hear",
            "Share pens and clipboards without cleaning between patients",
        ],
        "Source control and hand hygiene limit droplet spread in shared spaces. Clustering symptomatic patients increases exposure.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-infection-014
    fact(
        "skill-infection",
        "In what order should PPE generally be donned before entering an isolation room?",
        "Gown first, then mask or respirator, eye protection, then gloves",
        [
            "Gloves first, then gown over the gloves",
            "Mask after removing gloves at the doorway",
            "Eye protection before securing any gown or mask",
        ],
        "Sequencing keeps outer layers removable without contaminating clean skin. Gloves go on last so gown sleeves stay protected during donning.",
        [S.CDC_ISOLATION_2007],
        "beginner",
    ),
    # skill-infection-015
    fact(
        "skill-infection",
        "What is the safest sequence for removing PPE after patient care?",
        "Remove gloves first, then gown, eye protection, and mask or respirator, followed by hand hygiene",
        [
            "Pull off the mask first while gloves are still on",
            "Remove gown by rolling it inward while touching the outer contaminated side",
            "Leave all PPE on until the end of the shift",
        ],
        "Gloves are often most contaminated and should come off first. Hand hygiene after removal reduces self-inoculation.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-016
    fact(
        "skill-infection",
        "When should gloves be worn during routine patient care under Standard Precautions?",
        "When contact with blood, body fluids, mucous membranes, or nonintact skin is anticipated",
        [
            "During every phone call to the pharmacy",
            "While typing progress notes at a clean desk",
            "When walking patients in the hallway without touching them",
        ],
        "Gloves are task-based, not universal for all clinic activities. Administrative work without patient contact does not require gloves.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-infection-017
    fact(
        "skill-infection",
        "Why should gloves be changed between dirty and clean steps during one patient encounter?",
        "To prevent carrying organisms from contaminated surfaces to clean sites or equipment",
        [
            "To reduce glove cost by wearing one pair all day",
            "Because double gloving removes the need for hand hygiene",
            "Because clean gloves can be air-dried and reused later",
        ],
        "A single pair can transfer pathogens from a soiled area to a catheter hub or wound. Hand hygiene is still required after removal.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-018
    fact(
        "skill-infection",
        "A medical assistant finishes a blood draw, drops the used tube holder in the sharps container, and notices blood on the outside of the gloves. What is the best next step?",
        "Remove gloves, perform hand hygiene, and complete exposure documentation if skin was splashed",
        [
            "Wipe the gloves with alcohol and continue rooming the next patient",
            "Turn the gloves inside out and store them in a pocket for later",
            "Don a second pair over the soiled gloves without washing hands",
        ],
        "Visible contamination means gloves are no longer a barrier. Overgloving without hand hygiene spreads blood to the next task and patient.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-infection-019
    fact(
        "skill-infection",
        "How should a used needle and syringe be handled immediately after an injection?",
        "Dispose intact at the point of use in an approved sharps container without recapping",
        [
            "Recap with two hands before walking to the utility room",
            "Place the syringe in a regular trash bag if the dose was small",
            "Remove the needle and save the barrel for the next patient",
        ],
        "Point-of-use disposal lowers needlestick risk. Recapping and household trash disposal are common injury mechanisms.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-infection-020
    fact(
        "skill-infection",
        "When should a sharps container be closed and replaced?",
        "When contents reach the fill line indicated by the manufacturer",
        [
            "After the container is packed above the opening",
            "When the clinic closes for a holiday weekend",
            "When a staff member prefers a lighter container",
        ],
        "Overfilling increases sticks during disposal. Fill lines are set to keep needles contained during closure and transport.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-infection-021
    fact(
        "skill-infection",
        "What is the One and Only Campaign principle for needles and syringes?",
        "Use one needle and one syringe for one patient and dispose of them after use",
        [
            "Change needles weekly if they look sharp enough",
            "Share a syringe when drawing from the same medication vial",
            "Rinse syringes with tap water between patients",
        ],
        "Reusing injection equipment between patients can transmit bloodborne pathogens. Vial sharing without safe practices is a separate injection safety issue.",
        [S.CDC_ONE_AND_ONLY, S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-infection-022
    fact(
        "skill-infection",
        "How should a single-dose medication vial be managed after drawing a dose for one patient?",
        "Discard the vial and any unused contents for that patient",
        [
            "Recap and leave at the bedside for the next visit",
            "Store open vials in a purse for community outreach",
            "Combine leftover volumes from two patients into one syringe",
        ],
        "Single-dose containers are one patient per vial. Saving partial vials risks contamination and wrong-patient administration.",
        [S.CDC_ONE_AND_ONLY],
        "beginner",
    ),
    # skill-infection-023
    fact(
        "skill-infection",
        "What reduces risk when using a multi-dose vial for injections?",
        "Use a new sterile needle and syringe per entry and follow beyond-use dating per policy",
        [
            "Leave the rubber stopper wet with medication between patients",
            "Store opened vials in a personal locker without labeling",
            "Wipe the stopper once per month regardless of use",
        ],
        "Repeated entries with nonsterile technique can introduce organisms. Dating and labeling support safe reuse windows when policy allows.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-infection-024
    fact(
        "skill-infection",
        "Why should surfaces be cleaned before applying a hospital disinfectant?",
        "Organic debris can inactivate disinfectants and block contact with pathogens",
        [
            "Disinfectant works better on visible dust layers",
            "Cleaning is optional if the room looks tidy",
            "Air freshener can substitute for both steps",
        ],
        "Cleaning removes soil that shields microbes. Disinfection without cleaning may fail to reach viable organisms on the surface.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-025
    fact(
        "skill-infection",
        "What determines effective disinfection of an exam table between patients?",
        "Using an EPA-registered product with the full wet contact time on the label",
        [
            "Spraying disinfectant and wiping dry in two seconds",
            "Using the same cloth for the floor and the table without rinsing",
            "Opening windows instead of applying a disinfectant",
        ],
        "Kill claims depend on contact time listed by the manufacturer. Insufficient wet time leaves pathogens viable.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-026
    fact(
        "skill-infection",
        "How should noncritical patient care items such as a blood pressure cuff be handled between patients?",
        "Low-level disinfection or barrier protection per manufacturer and facility policy",
        [
            "Use on the next patient without cleaning if the prior patient seemed healthy",
            "Soak in plain water overnight instead of disinfectant",
            "Store in a staff break room without a cover",
        ],
        "Noncritical items touch intact skin but can harbor organisms. Appearance of wellness does not prove absence of colonization.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-infection-027
    fact(
        "skill-infection",
        "What should happen to linen soiled with blood or body fluids in the clinic?",
        "Handle with minimal agitation, bag at the point of use, and send for laundry per policy",
        [
            "Rinse in the patient restroom sink and reuse the same day",
            "Shake sheets in the hallway to remove dry debris",
            "Place wet linen in a regular paper recycling bin",
        ],
        "Agitation aerosolizes pathogens. Dedicated laundry workflows reduce environmental contamination.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "beginner",
    ),
    # skill-infection-028
    fact(
        "skill-infection",
        "How should regulated medical waste be segregated from regular office trash?",
        "Place blood-soaked items and sharps in labeled containers approved for biohazard waste",
        [
            "Combine all waste in one bag to reduce trips",
            "Discard small blood stains in unmarked wastebaskets",
            "Burn waste in a patient education pamphlet bin",
        ],
        "Color-coded and labeled containers protect housekeeping and waste handlers. Mixing streams increases exposure downstream.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-029
    fact(
        "skill-infection",
        "What is the first action after a needlestick involving patient blood?",
        "Wash the area with soap and water and report the exposure per the bloodborne pathogens plan",
        [
            "Squeeze the wound to force bleeding for several minutes",
            "Apply bleach directly to the puncture site",
            "Finish the clinic schedule before telling anyone",
        ],
        "Prompt washing and reporting allow timely source testing and prophylaxis evaluation. Delay and harsh chemicals worsen tissue injury.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-infection-030
    fact(
        "skill-infection",
        "A staff member splashes blood into their eye during a procedure. What sequence aligns with occupational exposure management?",
        "Irrigate eyes with water or saline, report immediately, and seek medical evaluation per the exposure control plan",
        [
            "Rub the eyes dry and continue the procedure without documentation",
            "Wait until the end of the shift to mention the splash if vision seems fine",
            "Apply alcohol-based hand rub to the eyes to disinfect them",
        ],
        "Mucous membrane exposures need irrigation and rapid assessment for HIV and hepatitis risk. Alcohol and delayed reporting reduce chances for timely prophylaxis.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-infection-031
    fact(
        "skill-infection",
        "Why does OSHA require employers to offer hepatitis B vaccination to at-risk healthcare personnel?",
        "Hepatitis B is efficiently transmitted by percutaneous exposure to infectious blood",
        [
            "Hepatitis B spreads mainly by casual conversation in hallways",
            "Vaccination replaces all need for Standard Precautions",
            "Vaccination is required solely for office managers who do not see patients",
        ],
        "Vaccination complements, rather than replaces, work practice controls. Blood exposure risk is tied to clinical duties, not administrative titles alone.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-032
    fact(
        "skill-infection",
        "During sterile specimen setup, a medical assistant touches the inside of a sterile bowl with a nonsterile glove. What is the correct response?",
        "Discard compromised supplies, reglove, and reestablish a sterile field before continuing",
        [
            "Turn the bowl upside down and use the outer base as sterile",
            "Wipe the inner surface with a dry paper towel",
            "Continue because the patient already signed consent",
        ],
        "Sterility is all-or-nothing once the interior is touched. Outer surfaces and quick wipes do not restore a sterile field.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-infection-033
    fact(
        "skill-infection",
        "A patient on contact precautions needs a fingerstick glucose check. What infection control approach is appropriate?",
        "Don gown and gloves, perform hand hygiene after removal, and disinfect the glucometer per policy",
        [
            "Use the same lancet device cap for multiple patients without cleaning",
            "Perform the test in the hallway to save gown supplies",
            "Omit hand hygiene because gloves were worn during the test",
        ],
        "Contact precautions add PPE for the encounter, and equipment still needs disinfection between patients. Shared lancet caps can transmit blood.",
        [S.CDC_ISOLATION_2007, S.CDC_HAND_HYGIENE],
        "advanced",
    ),
    # skill-infection-034
    fact(
        "skill-infection",
        "An exam room was used for a patient with influenza on droplet precautions. Which cleaning focus is most important before the next patient?",
        "High-touch surfaces such as doorknobs, chairs, and exam table where droplets may have landed",
        [
            "Ceiling tiles exclusively without wiping surfaces",
            "Outdoor parking lot pavement near the clinic entrance",
            "Staff lunch refrigerator in the break room",
        ],
        "Influenza virus can survive on surfaces near the patient. Distant areas unrelated to the encounter are lower priority than room touch points.",
        [S.CDC_ISOLATION_2007, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-infection-035
    fact(
        "skill-infection",
        "What does placing a surgical mask on a coughing patient in the waiting room accomplish?",
        "Source control that reduces droplet spread to others nearby",
        [
            "Sterilization of the air in the entire building",
            "Replacement for hand hygiene after tissue use",
            "Guarantee that staff can remove all other PPE",
        ],
        "Patient masking limits expelled droplets at the source. It supplements, rather than replaces, hand hygiene and staff PPE when indicated.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-infection-036
    fact(
        "skill-infection",
        "A clinic learns that a prefilled saline flush was used on more than one patient. What infection risk does this practice create?",
        "Bloodborne pathogen transmission between patients through shared injection equipment",
        [
            "Increased risk of latex allergy from glove powder alone",
            "Harmless sharing when the saline is preservative free",
            "Improved vein patency without microbiologic concern",
        ],
        "Even clear fluids can carry blood contamination when syringes are reused. Outbreak investigations have linked patient-to-patient hepatitis transmission to unsafe injection practices.",
        [S.CDC_INJECTION_SAFETY, S.CDC_ONE_AND_ONLY],
        "advanced",
    ),
    # skill-infection-037
    fact(
        "skill-infection",
        "Before transporting a patient on contact precautions to radiology, what should the medical assistant prepare?",
        "Clean wheelchair handles and ensure gown and gloves are available at the destination per policy",
        [
            "Remove all PPE in the hallway to speed transport",
            "Borrow equipment from another unit without cleaning it first",
            "Ask the patient to push the wheelchair bare-handed to avoid gown use",
        ],
        "Transport can contaminate shared equipment. Coordinating PPE and cleaning prevents cross-unit spread of resistant organisms.",
        [S.CDC_ISOLATION_2007],
        "advanced",
    ),
    # skill-infection-038
    fact(
        "skill-infection",
        "A staff member with weeping lesions on both hands is scheduled to perform venipuncture. What is the appropriate work adjustment?",
        "Follow occupational health and infection control guidance, which may restrict direct patient care until lesions heal or are covered per policy",
        [
            "Double glove and proceed without reporting the lesions",
            "Apply scented lotion and continue all procedures",
            "Wear a cloth wristband to cover a single lesion and leave the other open",
        ],
        "Nonintact skin on healthcare workers can both acquire and transmit pathogens. Reporting allows duty modification and patient protection.",
        [S.OSHA_BBP, S.CDC_HAND_HYGIENE],
        "advanced",
    ),
    # skill-infection-039
    fact(
        "skill-infection",
        "When entering the room of a patient on airborne precautions for suspected measles, which combination is required?",
        "Fit-tested respirator, gown, gloves, and eye protection per policy",
        [
            "Surgical mask alone with street clothes",
            "Gloves alone because measles is contact spread",
            "No PPE if the medical assistant had measles as a child",
        ],
        "Measles is airborne and highly contagious. Surgical masks and prior illness history do not replace respiratory protection and isolation PPE.",
        [S.CDC_ISOLATION_2007],
        "advanced",
    ),
    # skill-infection-040
    fact(
        "skill-infection",
        "After removing contaminated gloves, a medical assistant notices a tear and red skin under the nail bed. What is the priority?",
        "Stop patient care tasks, wash the area, and initiate exposure reporting even if bleeding is minimal",
        [
            "Apply a bandage and continue with the next patient without telling a supervisor",
            "Assume risk is zero because the patient looked healthy",
            "Disinfect the tear with hand rub and ignore documentation",
        ],
        "Nonintact skin under torn gloves is a potential blood exposure route. Reporting triggers evaluation even when the patient seems low risk.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-infection-041
    fact(
        "skill-infection",
        "A vaccine clinic runs low on hand hygiene supplies at the drawing station. What is the safest operational response?",
        "Pause setup until alcohol-based rub or soap and water is restocked at the point of care",
        [
            "Continue drawing doses and clean hands at lunch",
            "Use baby wipes from a personal bag as the sole method",
            "Rinse hands in a beverage cooler between patients",
        ],
        "Hand hygiene before vaccine preparation is an infection prevention requirement. Substitutes without antimicrobial action increase contamination risk.",
        [S.CDC_HAND_HYGIENE, S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-infection-042
    fact(
        "skill-infection",
        "Environmental services asks whether to use the same mop bucket for isolation and general clinic halls without changing solution. What guidance should infection control provide?",
        "Separate cleaning tools and change disinfectant solution per policy between isolation and general areas",
        [
            "Share one bucket to save time because disinfectant kills everything instantly",
            "Rinse the mop in plain water between rooms without disinfectant",
            "Defer isolation room cleaning until the end of the week to conserve supplies",
        ],
        "Cross-contamination can occur when mop water becomes loaded with organisms from isolation rooms. Instant kill claims still require proper concentration and contact time.",
        [S.CDC_ISOLATION_2007, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
]
