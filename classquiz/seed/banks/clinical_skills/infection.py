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
            "Patients with visible respiratory symptoms in the waiting area",
            "Patients whose culture results are already positive in the chart",
            "Patients scheduled for surgical procedures but not for clinic visits",
        ],
        "Standard Precautions are the baseline for every encounter, including unrecognized colonization. Restricting precautions to labeled infections leaves gaps for blood and body fluid exposure.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-infection-002
    fact(
        "skill-infection",
        "What is the primary purpose of hand hygiene in healthcare settings?",
        "Reduce pathogen spread from hands to patients, surfaces, and staff",
        [
            "Replace glove use during venipuncture, wound care, and specimen collection",
            "Eliminate terminal cleaning of exam rooms between patients",
            "Shorten room turnover without disinfecting high-touch surfaces between visits",
        ],
        "Hands frequently carry organisms between patients and the environment. Gloves and environmental cleaning remain separate layers of infection prevention.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-infection-003
    fact(
        "skill-infection",
        "When is alcohol-based hand rub appropriate before touching a patient?",
        "When hands are not visibly soiled and product use follows facility policy",
        [
            "When hands are coated with blood before donning examination gloves",
            "After care for a patient with Clostridioides difficile diarrhea",
            "When hands are visibly dirty and soap and water are available at the sink",
        ],
        "Alcohol rub works on visibly clean hands but does not remove spores or heavy soil. Soap and water is preferred for C. difficile and visible contamination.",
        [S.CDC_HAND_HYGIENE, S.NHA_CCMA],
        "beginner",
    ),
    # skill-infection-004
    fact(
        "skill-infection",
        "Which moment in patient care requires hand hygiene even if gloves will be worn?",
        "Before clean or aseptic procedures and after body fluid exposure risk",
        [
            "After removing gloves without cleaning hands when gloves looked intact",
            "Before entering the break room while still wearing clinic scrubs",
            "After the patient leaves and the room door is closed without washing",
        ],
        "Gloves can develop microtears and do not replace hand cleaning at key moments. Break room entry is not a substitute for post-care hand hygiene.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-infection-005
    fact(
        "skill-infection",
        "What should staff do with used examination gloves after patient care?",
        "Remove gloves and perform hand hygiene before touching clean surfaces",
        [
            "Wipe gloves with alcohol and reuse them for the next patient",
            "Place gloves in the regular waste bin and chart without hand cleaning",
            "Don fresh gloves over soiled gloves to save time between tasks",
        ],
        "Gloves are single-patient barriers; reusing or layering them spreads contamination. Hand hygiene after removal protects keyboards, doors, and supply carts.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-infection-006
    fact(
        "skill-infection",
        "Which PPE sequence is commonly taught when both gown and gloves are required?",
        "Gown, then mask or respirator, then eye protection, then gloves",
        [
            "Gloves are donned first, then the gown is draped over the gloved hands",
            "Eye protection last after removing gloves used for dirty tasks",
            "Mask after gloves so it contacts the outer glove surface",
        ],
        "Donning order limits bare-skin contact with contaminated outer surfaces during removal. Gloves go on last so gown cuffs stay protected during patient care.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-007
    fact(
        "skill-infection",
        "How should contaminated PPE generally be removed after patient care?",
        "Gloves first, then eye protection, gown, and mask avoiding outer surfaces",
        [
            "Gown first while keeping soiled gloves on both hands until exiting the room",
            "Mask first by pulling the front elastic toward the eyes and nose during doffing",
            "All items removed together into a pocket for laundering at home after the shift",
        ],
        "Doffing sequence keeps hands away from contaminated outer layers. Home laundering of clinic PPE bypasses facility infection control processes.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-008
    fact(
        "skill-infection",
        "What do Transmission-Based Precautions add to Standard Precautions?",
        "Added measures for contact, droplet, or airborne spread when suspected",
        [
            "Permission to reuse needles and syringes between patients",
            "Removal of the hand hygiene requirement whenever a surgical mask is worn",
            "Routine room cleaning without EPA-registered disinfectants",
        ],
        "Transmission-Based layers address specific routes such as droplet nuclei or contact with resistant organisms. They do not relax injection safety or basic hygiene.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-009
    fact(
        "skill-infection",
        "Which patients typically require droplet precautions in addition to Standard Precautions?",
        "Patients with suspected or confirmed droplet-spread infection",
        [
            "Patients with intact skin and no draining wounds during a routine clinic visit",
            "Patients who are afebrile with no cough while seated in the waiting room today",
            "Patients who completed antibiotics three weeks ago without symptoms",
        ],
        "Droplet precautions target close-range splash of secretions from diseases such as influenza or pertussis when active. Healed distant infections without symptoms may not need isolation.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-010
    fact(
        "skill-infection",
        "Which engineering control is central to airborne infection isolation for diseases such as tuberculosis?",
        "Negative-pressure airborne infection isolation room with door closed",
        [
            "Positive-pressure hallway blowing air into the general waiting area continuously",
            "Standard exam room with a portable fan aimed at the reception desk during visits",
            "Open bay seating with six feet between chairs as the sole engineering control",
        ],
        "Airborne precautions rely on directed ventilation and appropriate respirator use. Fans toward public areas and open seating do not contain infectious aerosols.",
        [S.CDC_ISOLATION_2007],
        "advanced",
    ),
    # skill-infection-011
    fact(
        "skill-infection",
        "What is medical asepsis in ambulatory medical assisting practice?",
        "Techniques that reduce microbes and protect clean sites and supplies",
        [
            "Sterilization of every countertop with autoclave packs each morning shift",
            "Complete elimination of all bacteria on patient skin",
            "Sterile surgical fields for every blood pressure measurement",
        ],
        "Medical asepsis focuses on clean technique and barrier use rather than terminal sterilization of the entire environment. Routine vitals do not require a surgical sterile field.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-infection-012
    fact(
        "skill-infection",
        "How should a sterile field be handled once opened for a procedure?",
        "Keep edges within view and avoid reaching over or talking across the field",
        [
            "Rest nonsterile supply boxes on top of the inner drape surface within the margin",
            "Add dropped sterile items back onto the field after brushing visible debris off",
            "Turn your back to the field while reaching for instruments behind it",
        ],
        "Sterile fields are violated by nonsterile objects, below-waist levels, and airborne droplets from talking. Once compromised, items may need replacement per policy.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-013
    fact(
        "skill-infection",
        "What is the purpose of cleaning high-touch surfaces between patients in exam rooms?",
        "Remove soil and reduce bioburden before disinfectant contact time",
        [
            "Replace hand hygiene when staff wear gloves for the entire patient visit",
            "Eliminate the need for PPE during antecubital blood collection",
            "Allow reuse of single-use speculum covers on the next patient in the same room",
        ],
        "Cleaning removes organic matter so disinfectants can work. It does not substitute for gloves during exposure-prone tasks or for single-use device policies.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-infection-014
    fact(
        "skill-infection",
        "Which EPA-registered product claim should surface disinfectants used in clinics carry?",
        "Hospital disinfectant labeling effective against relevant pathogens",
        [
            "Labeling as a furniture polish safe for wood grain shine",
            "Labeling as a hand lotion with fragrance for staff comfort",
            "Labeling as a window cleaner without a hospital disinfectant claim listed",
        ],
        "Environmental disinfectants must match organism claims and contact times on the label. Household cleaners without healthcare claims may not meet infection control needs.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-015
    fact(
        "skill-infection",
        "How should regulated medical waste such as blood-soaked dressings be handled in most clinics?",
        "Place in labeled leak-proof biohazard containers for vendor pickup",
        [
            "Place in a sealed plastic bag inside the regular waste bin",
            "Hold at the nurse station in an open container for the end of the day",
            "Place in a rigid sharps container alongside the used needles",
        ],
        "Sharps and saturated waste have specific packaging and vendor pickup rules. Ordinary waste bins, open containers at the nurse station, and sharps containers reserved for needles all misroute contaminated material.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-016
    fact(
        "skill-infection",
        "What is the One & Only Campaign message for injection safety?",
        "One needle, one syringe, one patient for each injection and entry",
        [
            "One multi-dose vial shared between exam rooms if it looks intact",
            "One syringe reused with a new needle for the next patient waiting in line",
            "One bag of saline used as a common flush for several peripheral catheters",
        ],
        "Reusing connectors or vials between patients has caused large outbreak investigations. Each patient deserves a new sterile syringe and needle for injections.",
        [S.CDC_ONE_AND_ONLY, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-infection-017
    fact(
        "skill-infection",
        "When may a single-dose medication vial be entered more than once?",
        "When the label specifically permits multiple entries with aseptic technique",
        [
            "Whenever two patients need the same medication within the same clinic hour",
            "When the vial stopper looks clean after wiping with alcohol before each entry",
            "When the vial is kept in the medication room and returned to stock after use",
        ],
        "Single-dose containers are meant for one patient unless the label states otherwise. Appearance of the stopper does not override labeling, and a returned vial goes back into stock only if it was never entered for a patient.",
        [S.CDC_INJECTION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-infection-018
    fact(
        "skill-infection",
        "How should a multi-dose vial be labeled when it is first opened?",
        "With both the open date and the beyond-use date on the label",
        [
            "With the opening date and the initials of the staff member who opened it",
            "With no date at all while the vial stays refrigerated in the clinic",
            "With a discard date that is set by whoever notices it is empty",
        ],
        "Dating supports timely discard before contamination risk rises. Refrigeration does not extend beyond-use intervals, and the beyond-use date comes from the manufacturer or pharmacy rather than from an empty vial.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-infection-019
    fact(
        "skill-infection",
        "What should staff do if a sterile package is torn or wet before use?",
        "Discard the item and select an intact sterile replacement",
        [
            "Tape the tear shut with nonsterile clinic tape and proceed",
            "Wipe the outside with alcohol and treat the contents as sterile",
            "Use the item quickly before more air enters the package",
        ],
        "Packaging integrity is part of the sterility assurance. Surface wiping does not re-sterilize instruments inside a compromised peel pack.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-infection-020
    fact(
        "skill-infection",
        "Why is hand hygiene emphasized after removing gloves following wound care?",
        "Gloves can tear unnoticed and hands can be contaminated at the wrists",
        [
            "Gloves can tear unnoticed and the fingertips stay clean after removal",
            "Gloves shield the hands completely until the cuffs are pulled",
            "Hand hygiene after glove removal is needed when blood is visible",
        ],
        "Microtears and roll-back at the cuff can soil the hands during removal. Gloves do not shield the hands completely, and hygiene is needed even when no blood is visible, so hands are cleaned after every removal.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-infection-021
    fact(
        "skill-infection",
        "Which action supports respiratory hygiene in waiting areas during respiratory virus season?",
        "Provide tissues, hand hygiene supplies, and masks for coughing patients",
        [
            "Seat all coughing patients shoulder-to-shoulder to conserve chairs in the lobby",
            "Discourage covering coughs so staff can hear symptom descriptions during triage",
            "Remove alcohol rub dispensers because they dry skin during winter months",
        ],
        "Source control and hand hygiene reduce droplet spread in shared spaces. Crowding symptomatic patients increases transmission risk.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-infection-022
    fact(
        "skill-infection",
        "What is the purpose of contact precautions for patients with multidrug-resistant organisms on skin?",
        "Limit direct contact and require gown and gloves for body contact",
        [
            "Allow shared patient equipment without cleaning between uses",
            "Permit food trays to sit on the bedside table unwashed overnight",
            "Replace hand hygiene with a single pair of gloves for the whole shift",
        ],
        "Contact precautions add barriers for touch transmission of resistant bacteria. Shared uncleaned equipment and all-day gloves undermine the intent.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-023
    fact(
        "skill-infection",
        "How should reusable blood pressure cuffs be managed between patients?",
        "Clean and disinfect between patients following the contact time",
        [
            "Rotate among exam rooms and wipe the cuff with a dry towel between patients",
            "Wipe the cuff with a dry paper towel instead of a disinfectant",
            "Store the cuff in the soiled utility room until the end of the day",
        ],
        "Cuffs contact skin and can harbor pathogens, so they are disinfected between patients with the full contact time. Rotation, dry wiping, and storage in the soiled utility room all leave contamination behind.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-024
    fact(
        "skill-infection",
        "When should staff perform hand hygiene after touching a patient's intact skin during an exam?",
        "After the encounter when moving to clean tasks or another patient",
        [
            "Before palpating the skin while gloves remain in the box",
            "Mid-exam while adjusting the computer with gloved hands and no washing",
            "At the end of the week when leaving the clinical building",
        ],
        "Touches during care can transfer organisms to keyboards and supplies. Timely hygiene between patients breaks the chain of transmission.",
        [S.CDC_HAND_HYGIENE],
        "intermediate",
    ),
    # skill-infection-025
    fact(
        "skill-infection",
        "What does cleaning a spill of blood on the floor require before disinfecting?",
        "Wear PPE, absorb the spill, and clean visible organic material first",
        [
            "Mop with plain water and leave the area to air dry overnight",
            "Wipe with a dry paper towel and return to patient care without donning PPE",
            "Spray disinfectant on a large pool without containing the fluid or wearing PPE",
        ],
        "PPE protects staff from splashes during cleanup. Disinfectants need a cleaned surface to achieve labeled kill claims.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-infection-026
    fact(
        "skill-infection",
        "Which patient placement is appropriate for someone with active varicella in many outpatient settings?",
        "Isolation from susceptible individuals and airborne precautions",
        [
            "Seating in the general pediatric waiting area during rash onset and cough",
            "Rooming with an immunocompromised patient in the same exam room today",
            "Discharge home by public transit while the lesions stay open and weeping",
        ],
        "Varicella spreads by air and contact; susceptible contacts need protection. Public transport and shared waiting areas expose vulnerable people.",
        [S.CDC_ISOLATION_2007],
        "advanced",
    ),
    # skill-infection-027
    fact(
        "skill-infection",
        "Why should jewelry and artificial nails be limited per many hand hygiene policies?",
        "They harbor organisms and interfere with hand washing and rub coverage",
        [
            "They improve alcohol rub penetration under stone settings and long nails",
            "They replace the need for gloves during phlebotomy tasks",
            "They indicate senior staff who may bypass required hand hygiene",
        ],
        "Rings and long nails reduce mechanical cleaning at the nail bed. Glove use and seniority do not remove hand hygiene requirements.",
        [S.CDC_HAND_HYGIENE, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-028
    fact(
        "skill-infection",
        "What is the role of an alcohol hand rub dispenser at the room entrance?",
        "Prompt hand hygiene on entry and exit to reduce cross-contamination",
        [
            "Serve as the sole surface disinfectant for blood spills on the floor",
            "Replace contact precautions for patients with MRSA colonization",
            "Substitute for sterile technique inside a opened surgical pack",
        ],
        "Convenient dispensers increase compliance at care transitions. They do not replace environmental disinfectants or isolation precautions.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-infection-029
    fact(
        "skill-infection",
        "How should linen soiled with blood be handled in clinical areas?",
        "Handle with gloves and place in labeled leak-resistant laundry bags",
        [
            "Shake linen in the hallway to remove solids before placing it in laundry bags",
            "Take soiled linen home for washing when the hospital laundry service is busy",
            "Store blood-soiled linen in open hampers at the nurse station",
        ],
        "Minimal agitation reduces aerosolization of pathogens. Facility laundry services follow OSHA and state rules for contaminated textiles.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-030
    fact(
        "skill-infection",
        "What is the correct response when a sterile glove is torn during a procedure?",
        "Stop, remove the torn glove, perform hand hygiene, and reglove before continuing",
        [
            "Continue with one gloved hand because the other stayed clean",
            "Tape the tear with nonsterile tape and finish the procedure without regloving it",
            "Dip the torn glove in alcohol before continuing the procedure",
        ],
        "A tear breaks the sterile barrier and risks wound contamination. Regloving after hand hygiene restores protection.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-031
    fact(
        "skill-infection",
        "Which practice reduces risk when handling sharp instruments before disposal?",
        "Use a neutral zone or instrument tray instead of hand-to-hand passing",
        [
            "Pass uncapped needles directly between coworkers over the sterile field",
            "Recap needles using two hands while the patient holds the cap",
            "Place used sharps on the exam table for later batch pickup",
        ],
        "Neutral zones reduce stick injuries during busy procedures. Two-handed recapping and open-table storage are high-risk practices.",
        [S.CDC_INJECTION_SAFETY, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-infection-032
    fact(
        "skill-infection",
        "Why are vaccine vials and diluents stored separately from contaminated supplies?",
        "To prevent cross-contamination of injectable products with clinic waste",
        [
            "To keep refrigerators warmer than food storage guidelines allow",
            "To allow multi-dose flu vials to sit at room temperature all day",
            "To mix different manufacturers' vaccines in one syringe for convenience",
        ],
        "Clean medication storage protects potency and sterility. Room-temperature storage and pooling vaccines violate handling standards.",
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        "advanced",
    ),
    # skill-infection-033
    fact(
        "skill-infection",
        "What should staff do before entering the room of a patient on contact precautions?",
        "Don gown and gloves if contact with the patient or environment is anticipated",
        [
            "Enter in street clothes and glove after touching the bed rails",
            "Wear the same gown for three patients in a row to reduce laundry costs",
            "Rely on a surgical mask alone at the door without performing hand hygiene first",
        ],
        "PPE must be in place before contact with contaminated surfaces. Reusing gowns between patients spreads organisms room to room.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-034
    fact(
        "skill-infection",
        "How does surgical hand antisepsis differ from routine hand hygiene?",
        "It uses prescribed scrub or rub for a defined time before sterile procedures",
        [
            "It uses plain water without soap for two seconds before donning sterile gloves",
            "It replaces sterile gloves so bare hands may touch the inner sterile field",
            "It is performed once per month regardless of the procedure list",
        ],
        "Surgical antisepsis lowers skin flora before donning sterile attire. Brief rinses or bare-hand field contact do not meet operating room standards.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-infection-035
    fact(
        "skill-infection",
        "Which waste item belongs in a sharps container rather than red bag waste?",
        "A used phlebotomy needle still attached to the tube holder",
        [
            "A gauze pad with a small dot of dried blood from a healed nick",
            "An empty medication box with no visible contamination on the cardboard",
            "A sealed biohazard bag of saturated dressings from a wound change",
        ],
        "Sharps need puncture-resistant containers regardless of how much blood is visible. Saturated dressings belong in biohazard waste, not sharps boxes.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-infection-036
    fact(
        "skill-infection",
        "What is the purpose of negative airflow relative to the hallway in an airborne isolation room?",
        "To keep infectious aerosols inside the room instead of drifting into corridors",
        [
            "To blow room air into the waiting area for fresh ventilation during clinic hours",
            "To eliminate the need for respirators when the isolation room door stays open",
            "To warm the room above eighty degrees Fahrenheit for patient comfort during care",
        ],
        "Directed airflow contains tuberculosis and other airborne pathogens. Open doors and warm temperatures do not replace respiratory protection.",
        [S.CDC_ISOLATION_2007],
        "advanced",
    ),
    # skill-infection-037
    fact(
        "skill-infection",
        "When may food or drink be kept in a patient care refrigerator?",
        "When policy separates staff food from medications and specimens",
        [
            "When vaccines and staff lunches share one refrigerator shelf to save space",
            "When blood tubes are stored next to sandwiches in the same bin",
            "When the refrigerator has no thermometer to check the temperature",
        ],
        "Segregation prevents medication and specimen contamination by food spills. Shared bins and unmonitored temperatures jeopardize cold chain for vaccines.",
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-infection-038
    fact(
        "skill-infection",
        "How should staff respond when a patient with influenza is waiting near immunocompromised patients?",
        "Separate seating, offer a mask, move the patient to a room",
        [
            "Move the patient to a room without offering a mask first",
            "Offer a mask but keep the patient in the shared waiting area",
            "Ask the immunocompromised patients to wear masks instead",
        ],
        "Spatial separation and masks reduce droplet exposure in shared waiting areas. Moving the patient without a mask, leaving the patient in the lobby, or masking the immunocompromised patients instead each leave the droplet risk in place.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-infection-039
    fact(
        "skill-infection",
        "What does terminal cleaning of an exam room after a contact precautions patient involve?",
        "Disinfection of all high-touch surfaces and shared equipment in the room",
        [
            "A quick wipe of the door handle alone before the next patient enters",
            "Opening the windows without surface disinfection as the cleaning step",
            "Replacement of ceiling tiles while bed rails and counters stay untouched",
        ],
        "Terminal cleaning addresses all designated surfaces and devices used during the visit. Partial wipes leave viable organisms for the next patient.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # skill-infection-040
    fact(
        "skill-infection",
        "Why should staff avoid carrying pens and badges inside gown sleeves during isolation care?",
        "Contaminated outer gown surfaces can transfer organisms to personal items",
        [
            "Pens improve sterility when stored under the gown cuff during isolation care",
            "Badges sterilize hands when clipped to the outside of gloves during patient care",
            "Sleeve storage replaces hand hygiene at the end of the visit after doffing PPE",
        ],
        "Personal items can become fomites carried into clean areas. Hand hygiene remains required after doffing PPE regardless of where badges were worn.",
        [S.CDC_ISOLATION_2007],
        "intermediate",
    ),
    # skill-infection-041
    fact(
        "skill-infection",
        "Which hand hygiene method is preferred after caring for a patient with known C. difficile diarrhea?",
        "Soap and water because alcohol rubs do not reliably remove spores",
        [
            "Alcohol rub alone because it is faster when moving between room exits",
            "Glove change without washing because the gloves looked clean after removal",
            "Air drying hands without soap after removing the gown and contaminated gloves",
        ],
        "Spores survive alcohol rub and need mechanical removal with soap and water. Gloves alone do not clean hands contaminated at the wrists.",
        [S.CDC_HAND_HYGIENE, S.NHA_CCMA],
        "advanced",
    ),
    # skill-infection-042
    fact(
        "skill-infection",
        "What should a medical assistant do when unsure which isolation precautions apply?",
        "Follow protocol, ask the charge nurse, and wear PPE pending clarification",
        [
            "Enter without PPE to ask about travel history before calling the charge nurse",
            "Use Standard Precautions alone for every rash or draining wound",
            "Wait in the hallway until the patient leaves without notifying anyone",
        ],
        "Pending clarification, erring toward appropriate barriers protects staff and other patients. Unprotected entry and silent delays both increase exposure risk.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),

]
