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
            "Skip hand hygiene if they remain standing in the doorway",
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
            "Airborne Precautions only",
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
        "Respiratory hygiene and cough etiquette posters in waiting areas promote?",
        "Source control of respiratory secretions",
        [
            "Replacing hand hygiene after every cough",
            "Using Droplet Precautions for all rashes",
            "Reusing surgical masks between patients without cleaning",
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
            "Instead of hand hygiene whenever gloves are worn",
            "Only in the patient's home, not in clinics",
            "Only for outpatients who deny symptoms",
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
            "Droplet Precautions with a surgical mask at the room door only",
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
            "Only after leaving the room to protect the hallway",
            "Only when an N95 is already required for Droplet Precautions",
            "Never if the caregiver received the seasonal influenza vaccine",
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
            "Wear only a surgical mask within three feet of the bed",
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
            "Droplet Precautions with a surgical mask at the bedside only",
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
            "The encounter occurred in outpatient care where rub is never permitted",
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
            "Store staff meals while wearing isolation gowns",
            "Skip environmental cleaning between patient contacts",
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
            "Droplet Precautions with surgical mask as the only extra measure",
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
            "Staff want to avoid any environmental cleaning between patients",
            "One patient needs Airborne Precautions and the other needs Contact only",
            "Cohorting replaces hand hygiene for the entire unit",
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
            "Mosquito vectors carrying bloodborne viruses only",
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
            "Only in the hallway outside the closed patient door",
            "Never, because large droplets behave like airborne nuclei",
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
            "Billing codes submitted for the encounter",
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
            "Droplet Precautions with surgical mask as the sole added measure",
            "Airborne Precautions in negative-pressure rooms for all vomiting patients",
            "Alcohol gel alone without glove use or surface disinfection",
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
            "Answering the clinic phone at the front desk",
            "Walking through the parking lot to escort a patient",
            "Every conversation with a patient regardless of procedure risk",
        ],
        "Eye protection is selected for tasks with splash risk, such as suctioning or handling bloody linens. Routine conversation without anticipated splashes does not require a face shield.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-020
    fact(
        "ccma-transmission",
        "A hospitalized patient with a draining methicillin-resistant Staphylococcus aureus (MRSA) wound requires?",
        "Contact Precautions in addition to Standard Precautions",
        [
            "Airborne Precautions with negative-pressure room only",
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
            "Emptied only once per calendar year",
            "Filled with general office waste to save disposal trips",
        ],
        "Overfilled sharps containers increase needlestick risk during disposal. Puncture-resistant containers must be closed and replaced before contents reach the top.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-022
    fact(
        "ccma-transmission",
        "When removing a sharps container from a room on isolation precautions, staff should?",
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
            "A random rotation so every room gets isolation once per week",
            "Whichever precaution type is least expensive for the unit",
        ],
        "Infection preventionists and providers apply organism-specific criteria. Culture clearance, symptom duration, and public health rules guide safe discontinuation.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-transmission-024
    fact(
        "ccma-transmission",
        "Care of a patient colonized with a multidrug-resistant organism (MDRO) typically includes?",
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
            "Large respiratory droplets that settle within three feet only",
            "Shared meal trays without any respiratory exposure",
        ],
        "TB bacilli ride in tiny particles that can remain airborne and be inhaled at a distance. Contact and droplet barriers alone do not replace Airborne Precautions for suspected pulmonary TB.",
        [S.CDC_ISOLATION_2007, S.NHA_CCMA],
        "intermediate",
    ),
    fact(
        'ccma-transmission',
        'Neutropenic precautions focus on?',
        'Protecting immunocompromised patients from pathogens',
        [
            'Increasing visitor crowding',
            'Serving raw unwashed produce always',
            'Disabling hand hygiene',
        ],
        'Protective environment reduces infection risk. Choosing Increasing visitor crowding is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Norovirus gastroenteritis typically requires?',
        'Contact Precautions plus careful environmental cleaning',
        [
            'Airborne isolation only',
            'No hand hygiene',
            'Sharing utensils between patients',
        ],
        'Norovirus spreads via fecal-oral and contact routes. Choosing Airborne isolation only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'PPE doffing sequence should?',
        'Prevent self-contamination of clothing and skin',
        [
            'Be random',
            'Occur in the hallway without hand hygiene',
            'Skip glove removal',
        ],
        'CDC describes safe donning and doffing order. Choosing Be random is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'PPE doffing should occur?',
        'Inside room or designated area with hand hygiene between steps',
        [
            'In busy waiting room',
            'While eating lunch',
            'Without hand hygiene',
        ],
        'Careful doffing prevents self-contamination. Choosing In busy waiting room is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'PPE donning order generally places?',
        'Gown before mask/respirator and eye protection before gloves',
        [
            'Gloves first always before any other step',
            'No order needed',
            'Shoes last only',
        ],
        'Sequence reduces contamination during donning. Choosing Gloves first always before any other step is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Patient transport under contact precautions requires?',
        'Notifying receiving unit and containing secretions or wounds',
        [
            'No communication',
            'Removing all PPE in elevator publicly',
            'Canceling all appointments silently',
        ],
        'Coordinate PPE and cleaning during transport. Choosing No communication is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Scabies infestation generally requires?',
        'Contact Precautions until treatment completed per policy',
        [
            'Airborne isolation only',
            'No linen handling precautions',
            'Sharing patient clothing',
        ],
        'Mites spread by prolonged skin contact. Choosing Airborne isolation only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Seasonal influenza spread in clinics is reduced by?',
        'Respiratory hygiene, vaccination, and isolating febrile patients when feasible',
        [
            'Recirculating air without filters only',
            'No sick leave policies',
            'Sharing masks between staff',
        ],
        'Combined measures limit droplet transmission. Choosing Recirculating air without filters only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Single-patient room assignment for isolation?',
        'Reduces cross-transmission when feasible',
        [
            'Is never helpful',
            'Eliminates need for hand hygiene',
            'Allows sharing linens without laundry',
        ],
        'Private rooms support isolation practices. Choosing Is never helpful is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Transmission-Based Precautions are used?',
        'In addition to Standard Precautions for specific pathogens',
        [
            'Instead of Standard Precautions',
            'Only in home care',
            'Only for surgical patients',
        ],
        'Isolation precautions supplement Standard Precautions for certain diseases. Choosing Instead of Standard Precautions is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'Transmission-based precautions are?',
        'Added to Standard Precautions based on suspected or confirmed infection',
        [
            'A replacement for hand hygiene',
            'Optional in all ICUs always',
            'Only for outpatients',
        ],
        'Layer additional PPE and room controls as indicated. Choosing A replacement for hand hygiene is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'Transporting a patient on Contact Precautions requires?',
        'Ensuring contaminated surfaces and equipment do not expose others',
        [
            'No communication with receiving unit',
            'Removing all PPE in elevator',
            'Skipping hand hygiene',
        ],
        'Coordinate transport to maintain precautions. Choosing No communication with receiving unit is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'Varicella (chickenpox) in a hospitalized patient typically requires?',
        'Airborne and Contact Precautions per CDC',
        [
            'Droplet Precautions only',
            'No precautions',
            'Standard Precautions without isolation',
        ],
        'Varicella virus spreads via airborne and contact routes. Choosing Droplet Precautions only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'What does Educating visitors under isolation include?',
        'Hand hygiene and PPE use per policy',
        [
            'Allowing unlimited toys without cleaning',
            'Ignoring cough etiquette',
            'Sharing patient utensils',
        ],
        'Visitors can carry pathogens in or out. Choosing Allowing unlimited toys without cleaning is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'What does Environmental cleaning for contact isolation include?',
        'Increased frequency of high-touch surfaces',
        [
            'Cleaning only floors annually',
            'Using single cloth for all rooms without disinfectant',
            'Ignoring spills',
        ],
        'Disinfection reduces environmental reservoirs. Choosing Cleaning only floors annually is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'What does Patient placement for droplet precautions often include?',
        'Private room or cohorting per facility policy',
        [
            'Open waiting room seating',
            'No mask for staff',
            'Shared equipment without cleaning',
        ],
        'Cohorting limits exposure when private rooms are unavailable. Choosing Open waiting room seating is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'What is After removing gloves following patient care, the next hand hygiene step?',
        'Perform hand hygiene because gloves may have microtears',
        [
            'Skip hygiene because gloves were worn',
            'Wipe gloves with alcohol and reuse',
            'Only wash if gloves tore visibly',
        ],
        'Gloves reduce but do not eliminate contamination of hands. Hand hygiene follows glove removal per CDC.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'A negative-pressure airborne infection isolation room (AIIR) is designed to?',
        'Prevent contaminated air from flowing to corridors',
        [
            'Increase humidity for comfort',
            'Store vaccines only',
            'Replace hand hygiene',
        ],
        'Negative pressure contains airborne pathogens. Choosing Increase humidity for comfort is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'Airborne Precautions require a patient with suspected tuberculosis to?',
        'Wear a surgical mask when transported and be placed in an airborne isolation room when available',
        [
            'Share a room with immunocompromised patients',
            'Remove mask in hallway',
            'Skip ventilation requirements',
        ],
        'Airborne isolation limits spread of small particles. Choosing Share a room with immunocompromised patients is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'An N95 respirator is required for?',
        'Airborne Precautions when indicated by policy and fit testing',
        [
            'All blood draws',
            'Every phone call',
            'Routine vitals',
        ],
        'Fit-tested respirators filter airborne particles. Choosing All blood draws is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'C. difficile prevention emphasizes?',
        'Contact Precautions and soap-and-water hand hygiene',
        [
            'Airborne isolation only',
            'Sharing commodes without cleaning',
            'No environmental cleaning',
        ],
        'Spores resist alcohol; contact precautions and cleaning are key. Choosing Airborne isolation only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'Measles requires?',
        'Airborne Precautions and respiratory protection when entering room',
        [
            'Contact Precautions only',
            'No mask for staff',
            'Negative pressure is optional always',
        ],
        'Measles is highly contagious via airborne spread. Choosing Contact Precautions only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'Neutropenic precautions (protective environment) focus on?',
        'Protecting immunocompromised patients from pathogens',
        [
            'Preventing all visitors permanently',
            'Eliminating Standard Precautions',
            'Using only droplet masks for TB',
        ],
        'Reverse isolation protects vulnerable hosts. Choosing Preventing all visitors permanently is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'What should When aerosol-generating procedures are performed on airborne isolation patients, staff use when measuring?',
        'Fit-tested N95 or higher respirator per policy',
        [
            'Surgical mask only always',
            'No eye protection',
            'Street clothing',
        ],
        'AGPs increase airborne exposure risk. Choosing Surgical mask only always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

