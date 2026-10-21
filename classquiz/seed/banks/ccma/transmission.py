# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-transmission)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-transmission-001
    fact(
        "ccma-transmission",
        "Before a visitor enters a room on Contact Precautions, the medical assistant should teach them to?",
        "Don gown and gloves on entry and clean hands before and after the visit",
        [
            "Wear a fit-tested N95 because contact illnesses spread through the air",
            "Share the patient's personal comb to inspect the scalp without gloves",
            "Defer hand hygiene when the visitor remains in the doorway without touching surfaces",
        ],
        "Contact Precautions block spread by touch and contaminated items. Respirators address airborne spread; they are not the primary barrier for typical contact pathogens such as lice or MRSA on surfaces.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-002
    fact(
        "ccma-transmission",
        "When a procedure may splash blood or body fluids into the face, eye protection belongs to?",
        "Standard Precautions",
        [
            "Airborne Precautions without eye protection when splashes are anticipated",
            "Droplet Precautions instead of gloves",
            "Contact Precautions without hand hygiene",
        ],
        "Standard Precautions match PPE to anticipated exposure for every patient. Transmission-Based Precautions add measures for specific routes but do not replace splash protection at the bedside.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-003
    fact(
        "ccma-transmission",
        "What is the primary infection-control goal of respiratory hygiene posters in waiting areas?",
        "Source control of respiratory secretions",
        [
            "Replacing alcohol-based hand rub stations with posters alone at entrances",
            "Using Droplet Precautions for every patient with a skin rash",
            "Reusing the same surgical mask for multiple patients in the waiting area",
        ],
        "Covering coughs and sneezes limits how far secretions travel. Hand hygiene remains essential, but posters do not eliminate the need for masks or isolation when a communicable respiratory illness is suspected.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-004
    fact(
        "ccma-transmission",
        "Transmission-Based Precautions are applied how in relation to Standard Precautions?",
        "In addition to Standard Precautions during patient care",
        [
            "In place of hand hygiene whenever gloves are worn",
            "In home care settings but not during hospital or clinic encounters",
            "For outpatients who deny symptoms at triage, without added barriers",
        ],
        "Standard Precautions are the baseline for all encounters. Contact, Droplet, or Airborne precautions layer on top when the organism or syndrome requires them.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-005
    fact(
        "ccma-transmission",
        "Which precautions are appropriate for uncomplicated head lice (pediculosis) per typical guidance?",
        "Contact Precautions and treatment of the infested person",
        [
            "Airborne Precautions in a negative-pressure room",
            "Droplet Precautions with a surgical mask at the door but no gown or gloves",
            "No precautions because lice jump between hosts like fleas",
        ],
        "Lice spread by direct contact with infested hair, clothing, and shared combs. They are not transmitted by airborne or droplet routes, so gown-and-glove contact barriers and treatment are appropriate.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-006
    fact(
        "ccma-transmission",
        "When caring for a patient on Contact Precautions, gown and gloves are worn?",
        "On room entry before touching the patient or environment",
        [
            "After leaving the room so the hallway shields the patient",
            "When Droplet Precautions already mandate an N95 respirator",
            "When the caregiver has current-season influenza vaccination documentation",
        ],
        "Donning PPE before contact keeps clothing and hands from carrying pathogens out of the room. Doffing and hand hygiene occur before exiting to the corridor.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-007
    fact(
        "ccma-transmission",
        "Posted instructions for Airborne Precautions should remind staff to?",
        "Wear a fit-tested respirator and keep the door closed when feasible",
        [
            "Use gown and gloves alone without any respiratory protection",
            "Wear a surgical mask without a respirator within three feet of the bed",
            "Leave doors open to increase positive-pressure airflow",
        ],
        "Airborne Precautions target small particles that can remain suspended. Fit-tested respirators and room engineering differ from the surgical masks and short-range focus of Droplet Precautions.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-008
    fact(
        "ccma-transmission",
        "A patient with suspected pulmonary tuberculosis should be placed on?",
        "Airborne Precautions with an N95 or higher respirator and negative-pressure room when available",
        [
            "Droplet Precautions with a surgical mask at the bedside without airborne isolation",
            "Contact Precautions with gown and gloves but no respiratory protection",
            "Standard Precautions unless the patient is actively coughing blood",
        ],
        "TB spreads via airborne droplet nuclei that can travel beyond conversational distance. Surgical masks and contact barriers alone do not replace respirators and airborne room placement.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-009
    fact(
        "ccma-transmission",
        "Alcohol-based hand rub is appropriate for routine hand hygiene when?",
        "Hands are not visibly soiled and the label contact time is followed",
        [
            "Hands are visibly soiled with stool or C. difficile spores without washing",
            "Gloves will be worn, so rub can replace cleaning after body-fluid contact",
            "The encounter is in outpatient care that prohibits all alcohol-based hand rub",
        ],
        "ABHR is effective for many routine healthcare contacts when hands are not soiled. Visible soil, spores, and some pathogens still require soap-and-water washing per CDC guidance.",
        [S.CDC_HAND_HYGIENE, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-010
    fact(
        "ccma-transmission",
        "An anteroom next to an isolation room is used primarily to?",
        "Don and doff PPE with less contamination of the corridor",
        [
            "Use the anteroom as break space without removing isolation PPE",
            "Defer environmental cleaning between patient contacts in the anteroom",
            "House clean equipment with used isolation supplies without disinfection",
        ],
        "Anterooms create a controlled transition space so PPE changes happen before staff re-enter public areas. They support workflow; they do not replace cleaning or safe storage rules.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-011
    fact(
        "ccma-transmission",
        "Infection control for Clostridioides difficile emphasizes?",
        "Contact Precautions plus soap-and-water hand hygiene when hands are soiled",
        [
            "Droplet Precautions with surgical mask but without gown, gloves, or soap-and-water hygiene",
            "Airborne Precautions with N95 respirator at the room door",
            "Alcohol-based hand rub alone without contact precautions or cleaning",
        ],
        "C. difficile spores resist alcohol and persist on surfaces. Gowns, gloves, dedicated equipment when possible, and washing remove spores; respiratory precautions do not address fecal-oral spread.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-012
    fact(
        "ccma-transmission",
        "Cohorting two patients with the same infectious organism may be appropriate when?",
        "A private isolation room is unavailable and facility policy allows cohorting",
        [
            "Cohorting to limit housekeeping rounds between infected patients",
            "One patient on Airborne Precautions and another on Contact Precautions in the same room",
            "Cohorting in place of hand hygiene for the entire unit",
        ],
        "Cohorting is a last-resort spacing strategy when single rooms are full. Patients must share the same precaution category, and cleaning and PPE rules still apply.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-013
    fact(
        "ccma-transmission",
        "Contact Precautions are indicated for which clinical example?",
        "MRSA colonization or infection with risk of contact spread",
        [
            "Measles in a febrile child with cough",
            "Influenza in the first 48 hours of symptoms",
            "Suspected pulmonary tuberculosis with productive cough",
        ],
        "MRSA on skin, wounds, or devices spreads by touch and contaminated surfaces. Measles and TB need Airborne Precautions; uncomplicated influenza typically needs Droplet Precautions.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-014
    fact(
        "ccma-transmission",
        "Contact Precautions are designed to reduce transmission by?",
        "Direct or indirect contact with the patient or contaminated surfaces",
        [
            "Airborne droplet nuclei that remain suspended for hours",
            "Large respiratory droplets within three to six feet of the face",
            "Mosquito-borne spread of bloodborne viruses without touch or surface contact",
        ],
        "Gowns and gloves interrupt hand and clothing contamination from the patient environment. Respirators and surgical masks target different respiratory routes, not primary contact spread.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-015
    fact(
        "ccma-transmission",
        "Droplet Precautions apply to illnesses spread by large respiratory droplets, such as?",
        "Influenza and pertussis",
        [
            "Draining MRSA wound on the extremity",
            "Varicella (chickenpox) with diffuse rash",
            "Norovirus vomiting with environmental contamination",
        ],
        "Influenza and pertussis spread when large droplets land on nearby mucous membranes. MRSA wounds and norovirus need Contact Precautions; varicella requires Airborne Precautions.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-016
    fact(
        "ccma-transmission",
        "Under Droplet Precautions, a surgical mask is worn when within about?",
        "3 feet (1 meter) of the patient",
        [
            "20 feet while using a fit-tested N95 for all room air",
            "In the hallway outside the closed door without entering the patient room",
            "Not indicated, because large droplets behave like suspended airborne nuclei",
        ],
        "Large droplets fall quickly and travel short distances. Airborne Precautions use respirators for smaller particles that can disperse farther; distance and mask type differ between categories.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-017
    fact(
        "ccma-transmission",
        "When to discontinue isolation precautions should be based on?",
        "Facility policy, clinical status, test results, and public health guidance",
        [
            "The patient's request to end precautions the same day symptoms improve",
            "A fixed 24-hour rule for every respiratory illness regardless of organism",
            "Discontinue when symptoms improve one day before cultures finalize",
        ],
        "Discontinuation depends on the pathogen, immune status, and culture or antigen results where applicable. Symptom improvement alone may not be sufficient for diseases with prolonged shedding.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-018
    fact(
        "ccma-transmission",
        "Outbreak control for norovirus gastroenteritis in a healthcare unit emphasizes?",
        "Contact Precautions with rigorous hand hygiene and environmental cleaning",
        [
            "Droplet Precautions with surgical mask without gown, gloves, or enhanced cleaning",
            "Airborne Precautions in negative-pressure rooms for all patients with vomiting",
            "Alcohol-based hand gel without glove use or environmental disinfection",
        ],
        "Norovirus spreads via fecal-oral contact and contaminated surfaces. It is not an airborne or droplet-only illness; contact barriers and cleaning with appropriate disinfectants are central.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-019
    fact(
        "ccma-transmission",
        "Under Standard Precautions, goggles or a face shield are needed when?",
        "Splashes or sprays of blood or other potentially infectious material are anticipated",
        [
            "Measuring oral temperature at the bedside without anticipated splashes",
            "Documenting in the EHR at the nurses station without patient contact",
            "Every conversation with a patient regardless of procedure risk",
        ],
        "Eye protection is selected for tasks with splash risk, such as suctioning or handling bloody linens. Routine conversation without anticipated splashes does not require a face shield.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-020
    fact(
        "ccma-transmission",
        "Which transmission-based precautions are indicated for a hospitalized patient with a draining MRSA wound?",
        "Contact Precautions in addition to Standard Precautions",
        [
            "Airborne Precautions in a negative-pressure room without gown or gloves",
            "Droplet Precautions with surgical mask but no gown or gloves",
            "No transmission-based precautions after antibiotics are started",
        ],
        "Wound drainage can contaminate dressings, linens, and hands. Contact barriers limit spread of resistant organisms; antibiotics do not immediately remove the need for precautions.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-021
    fact(
        "ccma-transmission",
        "Per OSHA guidance, a sharps container in patient care areas should be replaced when it is?",
        "No more than three-quarters full",
        [
            "Completely packed until items spill over the opening",
            "Emptied once per calendar year regardless of fill level",
            "Filled with general office waste to save disposal trips",
        ],
        "Overfilled sharps containers increase needlestick risk during disposal. Puncture-resistant containers must be closed and replaced before contents reach the top.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-022
    fact(
        "ccma-transmission",
        "When removing a sharps container from a room on isolation precautions, which practice should staff follow?",
        "Use the same PPE and precautions as for direct patient care",
        [
            "Carry the open container through the hallway without gloves",
            "Leave an overfilled box in the room until the patient is discharged",
            "Rinse and reuse the same container without disinfection",
        ],
        "Contaminated sharps may carry bloodborne pathogens present in the isolation room. PPE and hand hygiene protect staff and the environment during transport and replacement.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-023
    fact(
        "ccma-transmission",
        "The decision to discontinue isolation precautions should reflect?",
        "Clinical improvement, diagnostic results, and infection prevention policy",
        [
            "Patient preference alone without nurse or provider input",
            "Unit rotation that assigns isolation rooms by bed number each week",
            "Whichever precaution type is least expensive for the unit",
        ],
        "Infection preventionists and providers apply organism-specific criteria. Culture clearance, symptom duration, and public health rules guide safe discontinuation.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-024
    fact(
        "ccma-transmission",
        "Which precaution bundle is typical for a patient colonized with a multidrug-resistant organism (MDRO)?",
        "Contact Precautions plus communication with the care team about stewardship",
        [
            "Droplet Precautions with surgical mask instead of gowns",
            "Airborne Precautions for all MDROs regardless of site of colonization",
            "Shared unwiped stethoscopes between colonized and noncolonized patients",
        ],
        "MDROs such as MRSA or VRE often spread by contact with the patient or environment. Respiratory precautions apply only when the organism and syndrome warrant them.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-025
    fact(
        "ccma-transmission",
        "Mycobacterium tuberculosis is transmitted most often by?",
        "Airborne droplet nuclei from the respiratory tract",
        [
            "Casual handshake or intact skin contact alone",
            "Large respiratory droplets that settle within three feet without airborne spread",
            "Shared meal trays without any respiratory exposure",
        ],
        "TB bacilli ride in tiny particles that can remain airborne and be inhaled at a distance. Contact and droplet barriers alone do not replace Airborne Precautions for suspected pulmonary TB.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-026
    fact(
        "ccma-transmission",
        "Protective environment (neutropenic) precautions aim primarily to?",
        "Limit introduction of pathogens to severely immunocompromised patients",
        [
            "Use Contact Precautions in place of reverse-isolation room placement",
            "Allow fresh produce at the bedside when visitors bring it from home",
            "Rely on the patient mask alone without staff hand hygiene at entry",
        ],
        "Reverse isolation protects the host from environmental and visitor-borne organisms. It adds measures such as filtered air and restricted items; it does not eliminate baseline hand hygiene or Standard Precautions for staff.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-027
    fact(
        "ccma-transmission",
        "During a norovirus outbreak on a nursing unit, which action is appropriate for ill staff?",
        "Stay off duty per occupational health policy until cleared to return",
        [
            "Continue direct patient care while wearing a surgical mask at the nurses' station",
            "Rely on alcohol-based hand rub alone without environmental disinfection",
            "Cohort with influenza patients because both cause vomiting",
        ],
        "Norovirus is highly contagious and spreads on hands and surfaces. Excluding symptomatic workers and using contact precautions with appropriate disinfectants limits facility-wide transmission.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-028
    fact(
        "ccma-transmission",
        "When doffing PPE after Contact Precautions, gloves are generally removed?",
        "Before gown removal to keep contaminated glove surfaces off skin and clothing",
        [
            "After leaving the unit hallway so gloves protect the elevator buttons",
            "At the end of the shift regardless of recent patient contact",
            "Before entering the room while the gown remains in the corridor",
        ],
        "CDC sequences doffing to minimize self-contamination. Gloves are often removed first or early so hands can clean before touching the face or ungloved surfaces.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-029
    fact(
        "ccma-transmission",
        "Where should staff remove isolation PPE after caring for a patient on Transmission-Based Precautions?",
        "Inside the patient room, anteroom, or other designated doffing area",
        [
            "In the corridor immediately outside the patient room door",
            "At the nurses' station while finishing documentation",
            "In the clean supply room before discarding used PPE",
        ],
        "Doffing in a controlled space limits spread of pathogens to public corridors and clean supply areas. Hand hygiene between steps remains required.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-030
    fact(
        "ccma-transmission",
        "A typical CDC-recommended PPE donning sequence for isolation care places?",
        "Gown first, then mask or respirator, eye protection, and gloves last",
        [
            "Gloves first so bare hands avoid contact with the gown neckline",
            "Respirator after gloves to avoid fit-test documentation",
            "Don eye protection after exiting the isolation room",
        ],
        "Donning order keeps ungloved hands from contaminating the face and final barriers. Gloves go on last so earlier steps can be adjusted without tearing gloves.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-031
    fact(
        "ccma-transmission",
        "Before moving a patient on Contact Precautions to radiology, which step should the medical assistant take?",
        "Notify the receiving area and cover or contain draining wounds and equipment",
        [
            "Remove gown and gloves in the elevator to save PPE",
            "Assume transport staff need no precaution information if the trip is short",
            "Cancel the test without telling the provider or infection prevention",
        ],
        "Transport can expose hallways and staff who were not in the room. Communication and covering contaminated sites maintain precautions outside the isolation room.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-032
    fact(
        "ccma-transmission",
        "Crusted (Norwegian) scabies in a hospitalized patient warrants?",
        "Contact Precautions with emphasis on environmental cleaning and staff protection per policy",
        [
            "Droplet Precautions with surgical mask without gown, gloves, or environmental cleaning",
            "No linen precautions because mites die instantly on dry fabric",
            "Airborne Precautions in place of gown and glove use",
        ],
        "Scabies spreads through prolonged skin contact and heavily infested skin and bedding. Heavy infestation increases environmental load; contact barriers and laundry handling differ from respiratory isolation.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-033
    fact(
        "ccma-transmission",
        "To limit seasonal influenza transmission in an outpatient clinic, which bundle aligns with CDC guidance?",
        "Promote staff vaccination, respiratory hygiene, and separation of febrile patients when possible",
        [
            "Reuse the same surgical mask between patients without discarding",
            "Require symptomatic staff to staff the front desk throughout the shift",
            "Rely on recirculated unfiltered air as the sole control measure",
        ],
        "Influenza spreads by droplets and contaminated hands. Vaccination, source control, and spatial separation complement Droplet Precautions when patients are known or suspected to be infected.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-034
    fact(
        "ccma-transmission",
        "Assigning a private room for a patient on isolation precautions when available helps because it?",
        "Reduces shared air, surfaces, and equipment contact with other patients",
        [
            "Eliminates the need for hand hygiene at the room exit",
            "Allows unwashed shared equipment between isolation and general care patients",
            "Replaces Transmission-Based Precautions with Standard Precautions alone",
        ],
        "Single rooms are preferred for many isolation categories but do not replace PPE, cleaning, or hand hygiene. They lower the chance of cross-contamination between roommates.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-035
    fact(
        "ccma-transmission",
        "A patient on Airborne Precautions for measles still requires staff to follow?",
        "Standard Precautions including hand hygiene for every encounter",
        [
            "A fit-tested respirator without hand hygiene after glove removal",
            "Contact Precautions instead of any respiratory protection",
            "Droplet Precautions alone because measles particles do not require respirators",
        ],
        "Transmission-Based Precautions layer on Standard Precautions; they do not replace safe injection practices, hand hygiene, or splash protection when tasks warrant them.",
        [S.CDC_ISOLATION_2007, S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-036
    fact(
        "ccma-transmission",
        "When a multidrug-resistant organism is newly identified, Transmission-Based Precautions should begin?",
        "When clinical or laboratory evidence and facility policy indicate contact, droplet, or airborne needs",
        [
            "After every roommate has developed the same infection",
            "Delay precautions in outpatient clinics despite draining wounds",
            "Based on bed availability rather than organism, syndrome, and drainage risk",
        ],
        "Precaution category follows the pathogen and body site involved. Policy and infection prevention guide timing; delaying contact precautions for draining MRSA wounds increases spread risk.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-037
    fact(
        "ccma-transmission",
        "During intrahospital transport of a patient on Droplet Precautions, which measure should be used for the patient?",
        "Wear a surgical mask if tolerated and follow facility transport protocols",
        [
            "Remove the mask in the elevator to improve oxygen saturation",
            "Walk through the cafeteria without notifying staff in public areas",
            "Use a fit-tested N95 instead of a surgical mask for all droplet diseases",
        ],
        "Masking the patient during movement limits dispersion of large droplets. Staff near the patient wear masks per distance rules; N95s are for Airborne Precautions, not routine droplet transport.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-038
    fact(
        "ccma-transmission",
        "Hospitalized adults with disseminated varicella (chickenpox) require?",
        "Airborne plus Contact Precautions until lesions are crusted per policy",
        [
            "Droplet Precautions with gown and gloves but no respiratory protection",
            "Standard Precautions because varicella is a familiar childhood exanthem",
            "Contact Precautions without airborne room placement for all cases",
        ],
        "Varicella virus spreads through airborne and contact routes. Immunocompetent and immunocompromised hosts may need extended precautions; crusting guides discontinuation.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-039
    fact(
        "ccma-transmission",
        "Before a visitor enters a room on isolation precautions, the medical assistant should instruct them to?",
        "Perform hand hygiene and use PPE as directed by facility policy",
        [
            "Bring unwrapped toys from home without cleaning per infection prevention policy",
            "Consume food and beverages at the bedside during a prolonged visit",
            "Omit masks because household contacts were exposed before admission",
        ],
        "Visitors can acquire or carry pathogens between rooms. Education on hand hygiene, PPE, and limiting surfaces touched protects patients and the public corridor.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-040
    fact(
        "ccma-transmission",
        "Environmental cleaning for a patient on Contact Precautions should prioritize?",
        "Frequent disinfection of high-touch surfaces and dedicated equipment when possible",
        [
            "Annual floor waxing as the primary disinfection for high-touch surfaces",
            "One reusable cloth for all patient rooms without changing solution",
            "Deferring spill cleanup until the patient is discharged",
        ],
        "MDROs and enteric pathogens persist on bed rails, call buttons, and monitors. EPA-registered disinfectants and increased cleaning frequency lower indirect contact transmission.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-041
    fact(
        "ccma-transmission",
        "Preferred room placement for a patient on Droplet Precautions when a private room is unavailable is?",
        "Cohort with another patient with the same infection if policy allows, maintaining mask use near the bedside",
        [
            "Place next to a neutropenic patient in protective environment",
            "Seat in an open bay without masks because droplets fall within inches",
            "Room with a patient on Airborne Precautions for tuberculosis",
        ],
        "Droplet precautions use spatial separation and masks within about 3 feet. Cohorting requires matching infection type; mixing precaution categories increases risk.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-042
    fact(
        "ccma-transmission",
        "Immediately after removing gloves following patient care, what should the medical assistant do next?",
        "Perform hand hygiene because gloves may have undetected breaches",
        [
            "Document the encounter before cleaning hands because gloves guarantee sterility",
            "Apply alcohol to the outside of gloves and don them again for the next room",
            "Defer hand hygiene unless visible holes are seen in the glove material",
        ],
        "Gloves reduce hand contamination but microtears and slip-off during removal can soil skin. CDC requires hand hygiene after glove removal for Standard and Transmission-Based Precautions.",
        [S.CDC_HAND_HYGIENE, S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-043
    fact(
        "ccma-transmission",
        "The pressure monitor alarm sounds on an airborne infection isolation room while a patient with pulmonary tuberculosis rule-out is inside. Relative to the corridor, which airflow pattern should the room maintain?",
        "Lower air pressure in the room than in the corridor so air flows into the room",
        [
            "Higher air pressure in the room than in the corridor so air flows out into the hallway",
            "Equal air pressure between the room and corridor when the door stays closed",
            "Lower air pressure in the corridor than in adjacent standard patient rooms only",
        ],
        "A functioning AIIR keeps the isolation room at negative pressure so corridor air is not contaminated when the door opens. Positive or neutral pressure would allow infectious droplet nuclei to escape toward staff and other patients.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-044
    fact(
        "ccma-transmission",
        "When transporting a patient with suspected pulmonary tuberculosis outside the AIIR, which approach should be used for the patient?",
        "Wear a surgical mask if tolerated and minimize time in uncontrolled areas",
        [
            "Remove the mask so staff can assess lip color during the elevator ride",
            "Share transport with a patient colonized with MRSA on Contact Precautions",
            "Bypass infection prevention notification because the trip is under five minutes",
        ],
        "Surgical masks on the patient reduce emission of infectious particles during movement. Staff use Airborne Precautions and respirators per policy; transport routes should be planned.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-045
    fact(
        "ccma-transmission",
        "A fit-tested N95 (or higher) respirator is indicated for staff when?",
        "Caring for a patient on Airborne Precautions per facility policy",
        [
            "Performing every routine fingerstick glucose check in the clinic",
            "Answering telephone triage calls from home",
            "Measuring blood pressure on a Contact Precautions patient without added PPE",
        ],
        "Respirators filter small airborne particles and require fit testing. Standard clinical tasks without airborne risk use Standard Precautions; surgical masks suffice for Droplet Precautions.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-046
    fact(
        "ccma-transmission",
        "After caring for a patient with Clostridioides difficile diarrhea, which hand hygiene approach is appropriate?",
        "Soap and water when hands are visibly soiled or spore removal is needed per policy",
        [
            "Alcohol-based hand rub alone without contact precautions",
            "No cleaning if gloves appeared intact during the encounter",
            "Airborne Precautions with N95 instead of washing",
        ],
        "C. difficile spores resist alcohol and survive on surfaces. Contact Precautions plus mechanical washing when indicated complement environmental disinfection with sporicidal agents.",
        [S.CDC_HAND_HYGIENE, S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-047
    fact(
        "ccma-transmission",
        "A febrile patient with cough and a maculopapular rash after international travel is suspected to have measles. Staff entering the room need?",
        "Airborne Precautions including a fit-tested respirator",
        [
            "Contact Precautions with gown and gloves but no respiratory protection",
            "Droplet Precautions with surgical mask at the doorway without a respirator",
            "Standard Precautions because measles rash appears after contagion ends",
        ],
        "Measles is among the most contagious airborne viruses. Suspected cases are isolated immediately; susceptible staff without immunity should not care for the patient.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-048
    fact(
        "ccma-transmission",
        "For a hematology patient with severe neutropenia, which visitor practice aligns with protective environment guidance?",
        "Screen visitors for communicable illness and enforce hand hygiene before entry",
        [
            "Allow one visitor with a mild cough if they wear a surgical mask",
            "Permit dried floral arrangements without infection prevention review",
            "Reduce surface cleaning frequency to limit room disturbances",
        ],
        "Protective environments limit exogenous infection in patients who cannot mount a normal immune response. Policies may restrict plants, food, and ill contacts while maintaining cleaning and hand hygiene.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-049
    fact(
        "ccma-transmission",
        "During an aerosol-generating procedure on a patient in airborne isolation, staff should wear?",
        "A fit-tested N95 or higher respirator plus eye protection and other PPE per policy",
        [
            "A surgical mask because the aerosol-generating procedure is brief",
            "Gloves without eye protection when suctioning is performed",
            "Street clothes with a paper mask at the door",
        ],
        "Procedures such as intubation, suctioning, and bronchoscopy can aerosolize pathogens. Airborne Precautions and procedure-specific PPE reduce inhalation and splash exposure.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),

    # ccma-transmission-050
    fact(
        "ccma-transmission",
        "For which patient would Droplet Precautions be appropriate when infection is suspected?",
        "A patient with suspected pertussis with productive cough",
        [
            "A hospitalized patient with watery diarrhea and positive C. difficile toxin assay",
            "A patient with pulmonary tuberculosis managed in a negative-pressure airborne isolation room",
            "A patient with MRSA colonization of a draining extremity wound",
        ],
        "Large-droplet illnesses such as pertussis require mask and spatial separation. C. difficile uses Contact Precautions; tuberculosis uses Airborne Precautions.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-051
    fact(
        "ccma-transmission",
        "An outpatient clinic triages a patient with fever and vesicular rash consistent with varicella. What precaution set is needed in addition to Standard Precautions?",
        "Airborne and Contact Precautions per policy, including isolation and PPE",
        [
            "Droplet Precautions with gown and gloves but no respiratory protection",
            "Contact Precautions alone because the vesicular rash is clinically obvious",
            "Enter the room in street clothes after doffing all assigned PPE",
        ],
        "Varicella spreads by airborne and contact routes; combined precautions protect staff and other patients. Droplet alone is insufficient for varicella.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-transmission-052
    fact(
        "ccma-transmission",
        "Which PPE is added for Contact Precautions when entering the room?",
        "Gown and gloves for all room entry",
        [
            "Fit-tested N95 respirator for every room entry regardless of diagnosis",
            "Routine room entry in street clothes without performing hand hygiene",
            "Double gloves without gown for all patient contacts",
        ],
        "Contact isolation stops touch transmission of pathogens such as MRSA or C. difficile spores. N95 is for airborne precautions, not routine contact.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-transmission-053
    fact(
        "ccma-transmission",
        "Why is hand hygiene with soap and water emphasized for C. difficile prevention?",
        "Alcohol-based rubs do not reliably remove spores from hands",
        [
            "Soap increases C. difficile spore production on the skin",
            "Wearing gloves in place of hand hygiene after glove removal",
            "Spores are inactivated by passive air drying without washing",
        ],
        "C. difficile spores resist alcohol rubs; mechanical washing helps remove them. Gloves do not replace hand hygiene after doffing.",
        [S.CDC_HAND_HYGIENE, S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-054
    fact(
        "ccma-transmission",
        "When should an N95 respirator be used in addition to Standard Precautions?",
        "When Airborne Precautions are required and the user is fit tested",
        [
            "During every routine capillary blood glucose measurement in clinic",
            "While entering the employee break room between patient assignments",
            "In place of hand hygiene immediately after glove removal",
        ],
        "Fit-tested N95 filters small airborne particles for diseases such as tuberculosis. Routine point-of-care testing does not require respirators.",
        [S.CDC_ISOLATION_2007, S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-055
    fact(
        "ccma-transmission",
        "What distance guideline helps limit droplet transmission in clinic policy?",
        "Maintain spatial separation of about 3 to 6 feet when feasible",
        [
            "Stand within one inch of the patient without a mask during triage",
            "Seat febrile coughing patients in the main hallway for visibility",
            "Remove masks during conversation to improve speech clarity",
        ],
        "Large droplets fall quickly; distance and masks reduce exposure. Hallway placement and unmasked close contact increase spread.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-056
    fact(
        "ccma-transmission",
        "A patient with suspected influenza is placed on Droplet Precautions. Which mask is appropriate for staff entering the room?",
        "Surgical or medical mask covering nose and mouth",
        [
            "No mask when vaccinated against unrelated seasonal viruses",
            "Supplemental oxygen mask on the staff member instead of a surgical mask",
            "Cloth face covering worn under the chin during patient care",
        ],
        "Droplet precautions block large particles from coughs. Vaccination against other diseases does not remove mask need during infectious periods.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-057
    fact(
        "ccma-transmission",
        "When transporting a patient on Airborne Precautions, what additional step is required?",
        "Have the patient wear a mask if tolerated and notify receiving staff",
        [
            "Doff all PPE in the elevator before reaching the destination unit",
            "Discontinue airborne precautions once the patient leaves the isolation room",
            "Share a wheelchair between patients without cleaning between uses",
        ],
        "Transport plans maintain precautions along the route. Hallway travel without masks spreads particles.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
]
