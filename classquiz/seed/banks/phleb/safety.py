# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored phlebotomy safety and infection control bank (OSHA/CDC/CLSI)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_REF = [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS, S.CLSI_GP41]

FACTS: list[dict] = [
    fact(
        "phleb-safety",
        "What minimum PPE is required for routine venipuncture?",
        "Clean gloves; add gown or eye protection if splash risk exists",
        [
            "No gloves when the patient appears healthy and free of risk",
            "A respirator alone with no hand protection for the draw",
            "Street clothing with open wounds is acceptable at the draw chair",
        ],
        "OSHA and CDC Standard Precautions treat all blood and body fluids as potentially infectious. "
        "Gloves protect both patient and collector; additional PPE follows the anticipated exposure.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-safety",
        "How should used phlebotomy needles be discarded?",
        "Immediately into an approved sharps container at the bedside",
        [
            "In a regular office waste basket lined with a paper bag",
            "In a desk drawer until the end of the clinical shift",
            "After bending and hand-recapping it for transport to the lab area",
        ],
        "OSHA requires puncture-resistant sharps disposal without recapping, bending, or breaking needles by hand. "
        "Delaying disposal increases needlestick risk to staff and housekeeping.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "Why is hand hygiene after removing gloves required?",
        "Gloves may have microtears and hands can still be contaminated",
        [
            "Gloves sterilize the hands so washing is unnecessary",
            "Alcohol-based rub is banned in healthcare settings",
            "The first patient of the day is the one who needs hand hygiene",
        ],
        "CDC hand hygiene guidance applies before patient contact and after glove removal. "
        "Microscopic defects and handling of contaminated surfaces leave pathogens on skin.",
        [S.CDC_HAND_HYGIENE, S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "Which identifiers should be used to verify patient identity before phlebotomy?",
        "Active verification such as spelling name and date of birth",
        [
            "Room number alone without speaking with the patient first",
            "Assuming that the occupant matches the bed label",
            "An insurance card photo without confirming identity verbally",
        ],
        "CLSI patient safety steps require positive identification at the bedside before collection. "
        "Wrong-patient draws are serious sentinel events with clinical and legal consequences.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "How must sharps containers be handled?",
        "Puncture-resistant, labeled, closable, and not overfilled",
        [
            "Left open on the counter for quick access during draws",
            "Emptied into regular trash when the container is full",
            "Stored on the floor and unlocked in the hallways of the unit",
        ],
        "Overfilled or open containers defeat engineering controls mandated by OSHA. "
        "Replace containers before contents reach the fill line indicated by the manufacturer.",
        [S.OSHA_BBP],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "How should eating or drinking in the phlebotomy work area be handled?",
        "Prohibited to reduce contamination and exposure risk",
        [
            "Encouraged during active blood collection in the room",
            "Allowed if the tubes nearby have been capped",
            "A substitute for hand hygiene between the patients",
        ],
        "Food and beverages can contact blood splashes or contaminated surfaces. "
        "Separate break areas support Standard Precautions in the collection zone.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "Why is transporting uncapped needles between rooms unsafe?",
        "Unsafe and prohibited by work practice controls",
        [
            "Accepted practice that saves walking time",
            "Required when the sharps box is down the hall",
            "Acceptable if the patient watches the collector walk",
        ],
        "Needlesticks often occur during carrying and transfer of unprotected sharps. "
        "Activate safety devices and dispose at the bedside whenever possible.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "When should gloves be changed?",
        "Moving from a contaminated task to a clean task or between patients",
        [
            "One pair may be worn all day for the sake of collector efficiency",
            "When a large visible hole appears in the glove material on the hand",
            "Between draws in the same room during a batch run of tubes",
        ],
        "Cross-contamination between patients and surfaces spreads bloodborne pathogens. "
        "Change gloves after blood contact before touching keyboards, phones, or clean supplies.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "What are biohazard waste bags used for?",
        "Items contaminated with blood or other potentially infectious material",
        [
            "Clean office paper and unsoiled packaging materials",
            "Patient personal belongings and clothing left behind in the draw chair area",
            "Sterile unused supplies in their original boxes",
        ],
        "OSHA defines regulated waste that requires labeled biohazard containment. "
        "Segregation prevents accidental exposure during disposal and transport.",
        [S.OSHA_BBP],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "What should be done for patients at risk of fainting during phlebotomy?",
        "Be drawn seated with observation during and after the procedure",
        [
            "Stand for the draw without regard to the previous history",
            "Be left alone immediately after the last tube has been filled",
            "Keep a tight tourniquet on for the entire length of the whole visit",
        ],
        "Seated positioning and post-draw observation lower fall injury from vasovagal events. "
        "CLSI supports accommodating patients with prior syncope or anxiety.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "When should blood tubes be labeled?",
        "At the bedside immediately after collection per policy",
        [
            "At the central lab bench without the patient present nearby",
            "The next day if the draw on the unit was busy",
            "On every third tube in the rack to save time",
        ],
        "Bedside labeling ties the specimen to the identified patient and reduces mislabel errors. "
        "Pre-labeled tubes before draw are a common source of wrong-patient results.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "How should specimens transported in bags be handled?",
        "Sealed in leak-proof secondary containment",
        [
            "Carried uncapped in a coat pocket",
            "Mixed from different patients in one open tray",
            "Left at nurses' station without biohazard labeling",
        ],
        "Leaks expose staff and couriers to bloodborne pathogens during transport. "
        "CLSI transport practices require secure upright carriage in approved bags.",
        [S.CLSI_GP41, S.OSHA_BBP],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "How should horizontal work surfaces between patients be handled?",
        "Cleaned with facility-approved disinfectant on a schedule",
        [
            "Wiped with plain water between every fifth patient in the clinic",
            "Left untouched because gloves take the place of cleaning",
            "Sprayed with air freshener instead of the disinfectant",
        ],
        "Environmental cleaning is part of Standard Precautions for blood contact areas. "
        "Spills of blood require immediate cleanup with appropriate disinfectant.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "What should staff with open lesions on their hands do?",
        "Avoid patient contact or use barriers per occupational health policy",
        [
            "Perform the draws without a covering when gloves are worn",
            "Use the same torn gloves for an entire week of patient draws in the clinic",
            "Ignore the small cuts because the bloodborne risk is zero",
        ],
        "Breaks in skin increase worker susceptibility and can transmit organisms to patients. "
        "Cover lesions and follow return-to-work guidance from infection control.",
        [S.CDC_STANDARD_PRECAUTIONS, S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "When should safety-engineered phlebotomy devices be activated?",
        "Immediately after use according to manufacturer and facility policy",
        [
            "At the end of the clinical shift for the purpose of reuse planning",
            "After the patient leaves, because the activation increases hemolysis",
            "By a coworker to demonstrate how the safety feature works",
        ],
        "OSHA expects feasible engineering controls to reduce sharps injuries. "
        "Passive or active safety features must be engaged before disposal.",
        [S.OSHA_NEEDLESTICK, S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What first aid should be provided if blood splashes into the eyes?",
        "Flush with water or saline, then report the exposure",
        [
            "Rubbing the eyes until the tearing stops on its own",
            "Waiting until the end of the shift to tell the supervisor",
            "Ignoring the minor splashes and recording nothing for the file",
        ],
        "Mucous membrane exposures to blood require prompt irrigation and occupational health evaluation. "
        "Source-patient testing and prophylaxis follow institutional bloodborne pathogen protocols.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "Why is hand recapping used needles prohibited?",
        "Discouraged; use a one-hand scoop or safety device if needed",
        [
            "Required before every disposal into the sharps boxes",
            "Safer than safety-engineered needles in most clinical situations",
            "Recommended to speed up the multi-patient rounds",
        ],
        "Most needlestick injuries involve recapping or transfer between hands. "
        "OSHA work practice controls favor no recap or mechanical aids.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What must the employer exposure control plan for bloodborne pathogens contain?",
        "Engineering controls, work practices, hepatitis B vaccination, and follow-up",
        [
            "An annual payroll review with no clinical safety content in it at all",
            "Optional hepatitis B vaccination with no training requirement attached",
            "A promise to buy gloves with no written procedures on file at the clinic site",
        ],
        "OSHA 29 CFR 1910.1030 requires a written plan reviewed annually. "
        "Phlebotomists must know reporting steps and their rights to free post-exposure care.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What is required when drawing blood in an isolation room?",
        "Isolation PPE and exit procedures per the patient's precautions",
        [
            "Standard precautions without the added isolation PPE in place",
            "Leaving contaminated tubes in the hallway for a later pickup by staff",
            "Removing the PPE inside the room before leaving it",
        ],
        "CDC isolation guidance matches transmission risk (contact, droplet, airborne). "
        "Incorrect doffing spreads pathogens to clean areas and other patients. "
        "Using standard precautions alone, leaving tubes in the hallway, and removing PPE inside the room each break the isolation workflow.",
        [S.CDC_ISOLATION_2007, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What action should a needlestick with unknown source HIV status prompt?",
        "Immediate wound care and urgent occupational health evaluation",
        [
            "Ignoring the injury if the needle looked clean at the time of the stick",
            "Waiting one week to see if the symptoms develop",
            "Completing all of the draws before the documentation",
        ],
        "HIV post-exposure prophylaxis has time windows for effectiveness. "
        "OSHA requires employers to document exposures and offer appropriate follow-up testing.",
        [S.OSHA_NEEDLESTICK, S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "How should shared cloth tourniquets between patients be handled?",
        "Managed per policy, often disposable or disinfected between uses",
        [
            "Used on each patient without cleaning to save time",
            "Soaked in bleach while it is still on the patient arm",
            "Shared with the cafeteria staff for their other daily tasks on the unit",
        ],
        "Tourniquets can harbor organisms when blood contacts the surface. "
        "Single-patient disposable barriers or documented cleaning reduce cross-contamination.",
        [S.CDC_STANDARD_PRECAUTIONS, S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "Patients on anticoagulant therapy have an increased risk of what?",
        "Bleeding and bruising at the venipuncture site",
        [
            "Hemolysis of the red cells in each collected tube",
            "No bleeding despite therapeutic anticoagulation",
            "Higher serum sodium from the tourniquet",
        ],
        "Medications prolong hemostasis at the skin puncture. "
        "Longer pressure and clear aftercare instructions improve safety for these patients.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What should be used to transport filled sharps containers?",
        "Closed containers kept upright and secured during movement",
        [
            "Open tops so staff can add the needles while walking",
            "Shaking the containers to compact the waste further",
            "Placing loose containers on an unsecured passenger seat in the car",
        ],
        "Spills from tipped or overfilled sharps boxes create immediate stick hazards. "
        "Replace containers at the fill line before transport to central storage.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What is required after a blood spill on the phlebotomy floor?",
        "Donning PPE and cleaning with approved disinfectant per protocol",
        [
            "Wiping the spill with dry paper towels taken from the supply shelf",
            "Waiting for housekeeping to arrive without placing a barrier sign",
            "Cleaning the area with bare hands when the blood volume looks small",
        ],
        "Bloodborne pathogen standards require prompt decontamination of OPIM spills. "
        "Follow contact time on the disinfectant label and dispose of materials as biohazard waste. "
        "Dry towels, waiting for housekeeping, and cleaning without protection each leave blood exposed in the work area.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What is the expectation for patients left unattended in the draw chair?",
        "Not be left unattended; observation continues during and after the draw",
        [
            "Be acceptable if the patient eyes are closed during the draw",
            "Be sent out to the parking lot alone when the patient feels dizzy",
            "Be restrained without a written provider order when the patient seems nervous",
        ],
        "Syncope can occur seconds after needle removal. "
        "Continuous observation protects patients who underestimate lightheadedness.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What should phlebotomy competency training cover?",
        "Venipuncture technique, order of draw, identification, and safety rules",
        [
            "Billing codes and insurance paperwork in place of hands-on practice",
            "Social media tips instead of the institutional policy content taught in class",
            "No documentation of the completed skills validation for the file",
        ],
        "Employers must ensure staff are qualified before independent collection duties. "
        "CLSI and certification bodies expect documented skills assessment.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "When a patient becomes combative during venipuncture, what should the collector do?",
        "Stop and follow de-escalation and security policy for safety",
        [
            "Force the draw quickly before the patient behavior changes further",
            "Leave the needles inserted while calling for security help",
            "Use the physical restraint without a provider order in place",
        ],
        "Patient and staff safety outweigh completing the collection in an unsafe moment. "
        "Involve nursing leadership or security per facility violence prevention plans.",
        [S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What is the recommended approach to hepatitis B vaccination for phlebotomy staff?",
        "Offered by employers at no cost to staff with exposure risk",
        [
            "Forbidden under the OSHA bloodborne pathogen rules for staff",
            "Optional with no requirement to document a written declination form",
            "Required for laboratory directors rather than for the collectors",
        ],
        "The Bloodborne Pathogens Standard includes hepatitis B vaccine series at employer expense. "
        "Declinations must be documented but vaccination remains strongly recommended.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "How does privacy during phlebotomy support safety?",
        "Allowing accurate identification and reducing patient stress",
        [
            "Removing the requirement for the two patient identifiers",
            "Permitting the draws without consent in the public hallways of the clinic",
            "Replacing the hand hygiene steps with privacy curtains",
        ],
        "HIPAA-aligned privacy helps patients speak freely to confirm identity and allergies. "
        "Calmer patients tolerate procedures better with fewer movement-related sticks.",
        [S.HHS_HIPAA_PRIVACY, S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What is required for a patient with a latex allergy?",
        "Using non-latex gloves and equipment per supply policy",
        [
            "Using latex gloves because they stretch more",
            "Continuing with latex if the reaction was mild years ago",
            "Switching to powdered latex for easier donning",
        ],
        "Allergic reactions can progress to anaphylaxis during procedures. "
        "Facilities stock latex-free alternatives for at-risk individuals. "
        "Stretchability, a remote mild reaction, and powdered latex for easier donning each leave the patient exposed during the draw.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "How should eyewash stations where chemical or splash risk exists be handled?",
        "Accessible and known to staff per OSHA first-aid requirements",
        [
            "Locked to prevent the casual use by visitors",
            "Used for washing the dishes in the break room area",
            "Optional at outpatient draw stations that have no written policy",
        ],
        "Rapid irrigation limits damage from splashes of disinfectants or blood. "
        "Orientation and drills ensure staff reach eyewash within seconds.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "When should needlestick incidents be reported?",
        "Immediately so post-exposure evaluation can begin",
        [
            "When the patient is known to be HIV positive",
            "At the annual performance review",
            "When the patient has a confirmed bloodborne infection",
        ],
        "Delay reduces options for prophylaxis and compromises surveillance data. "
        "OSHA prohibits retaliation against employees who report exposures promptly.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What do WHO injection safety principles applied to phlebotomy stress?",
        "One sterile needle and syringe or set per patient procedure",
        [
            "Changing the needle while reusing the same barrel",
            "Sharing the multi-dose vials without the aseptic technique in place",
            "Skipping the hand hygiene steps when gloves are available",
        ],
        "Reuse transmits hepatitis and HIV between patients. "
        "Single-use collection systems align with CDC One & Only campaigns for safe injections.",
        [S.WHO_INJECTION_SAFETY, S.CDC_ONE_AND_ONLY],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "How does a safety syringe with a retractable needle reduce risk?",
        "Covering the sharp right after use without the hand near the point",
        [
            "Removing the need for gloves during all of the patient draws on the unit",
            "Allowing the manual recap with two hands for speed",
            "Leaving the needle exposed after it is withdrawn from the patient",
        ],
        "Engineering controls remove the hazard rather than relying on behavior alone. "
        "OSHA's needlestick prevention rule prioritizes devices that isolate the needle after activation.",
        [S.OSHA_NEEDLESTICK, S.CDC_INJECTION_SAFETY],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What is source-patient testing after a blood exposure used for?",
        "Guide post-exposure prophylaxis and baseline serology for staff",
        [
            "Punish the source patient for the staff injury",
            "Replace the wound washing and the occupational health referral visit",
            "Determine the billing codes with no clinical use in the plan",
        ],
        "Knowing source status for HIV, HBV, and HCV shapes monitoring and medication offers. "
        "Consent and local law govern testing; protocols must be followed rapidly.",
        [S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What should central supply of safety lancets for fingersticks ensure?",
        "Single-patient use and activation of sharps protection before disposal",
        [
            "Shared lancet devices cleaned with alcohol between each of the patients",
            "Leaving the used lancets on the bedside table",
            "Disabling the safety caps to speed up the collection",
        ],
        "Point-of-care devices still create sharps contaminated with blood. "
        "CLSI capillary collection standards align with OSHA controls for injury prevention.",
        [S.CLSI_GP41, S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "When gloves are visibly torn during a draw, what should the collector do?",
        "Stop, remove the gloves, do hand hygiene, and reglove",
        [
            "Finish the procedure because the small holes do not affect safety",
            "Wiping the gloves on the pants and then keep drawing",
            "Double the gloves without washing the hands underneath",
        ],
        "Visible breaches negate barrier protection and may have already contaminated hands. "
        "Hand hygiene between glove changes maintains Standard Precautions integrity.",
        [S.CDC_HAND_HYGIENE, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What does fire safety during mobile phlebotomy with oxygen in use require?",
        "Avoiding sparks and following facility oxygen precautions in the home",
        [
            "Allowing smoking near the cylinders to check the airflow",
            "Using alcohol-based products freely on the running oxygen tubing at the bedside",
            "Storing the oxygen cylinders horizontal without securing them",
        ],
        "Oxygen-enriched environments lower ignition thresholds for flammable vapors including alcohol prep. "
        "Follow home health and hospital policies for oxygen and electrical equipment near patients. "
        "Smoking nearby, using alcohol products freely on oxygen tubing, and leaving cylinders unsecured each raise the chance of an ignition event.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What is a chaperone often required for during pediatric phlebotomy?",
        "Support positioning and emotional safety with aseptic technique kept",
        [
            "Replace the two-identifier verification step for the draw",
            "Hold the child in position with no instruction from the collector",
            "Eliminate the need for the gloves worn by the phlebotomist at the chair",
        ],
        "Parents or guardians help immobilize safely when developmentally appropriate. "
        "Collectors remain responsible for identification, consent, and infection control.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "Which ergonomic practices help prevent injury for full-time phlebotomists?",
        "Adjustable chairs, neutral wrist position, and rotating busy tasks",
        [
            "Bending the wrist sharply during every needle insertion",
            "Drawing exclusively overhead without scheduled breaks",
            "Ignoring the repetitive strain because gloves protect the joints of the hand",
        ],
        "Musculoskeletal disorders end careers when posture and workload are unmanaged. "
        "OSHA general duty concepts support engineering and administrative controls for repetitive motion.",
        [S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "How should a patient refusal of phlebotomy be managed?",
        "Respected and documented with provider notification per policy",
        [
            "Completed anyway after verbal reassurance from a family member",
            "Deferred until the next shift without notifying the provider",
            "Documented as completed even when the patient declined",
        ],
        "Informed refusal is an ethical and legal right except in specific emergent circumstances defined by policy. "
        "Document the conversation and inform the care team so alternative plans can be made.",
        [S.NHA_CPT, S.HHS_HIPAA_PRIVACY],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "How should reusable tourniquets suspected of blood contamination be handled?",
        "Removed from service and cleaned or discarded per policy",
        [
            "Used on the next patient with no cleaning between the two draws",
            "Rinsed in tap water and air-dried in the staff lunchroom",
            "Stored in the sharps container for the unit supply",
        ],
        "Blood-soaked linens and equipment require handling as potentially infectious. "
        "Laundry and disinfection follow facility procedures separate from sharps disposal.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What must annual bloodborne pathogen training for staff cover?",
        "Exposure risks, engineering controls, and post-exposure steps",
        [
            "Payroll direct deposit changes for the staff roster",
            "Social media marketing for the laboratory services",
            "Parking assignments with no clinical safety content in the training",
        ],
        "OSHA requires training at hire and at least annually when job duties involve OPIM. "
        "Training must be in a language and vocabulary workers understand.",
        [S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "How does selecting a safety winged infusion set over a plain needle primarily improve safety?",
        "Sharps injury protection during high-risk butterfly collections",
        [
            "Elimination of the patient identification requirements for the draw order",
            "Automatic correction of the order-of-draw errors",
            "Removal of the need for the gloves",
        ],
        "Butterfly sets remain a common injury source during connection and disposal. "
        "Safety versions with shields or retractors align with OSHA's hierarchy of controls.",
        [S.OSHA_NEEDLESTICK, S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "When a coworker is stuck with a contaminated needle, what should you do?",
        "Assist them to start washing and reporting while they seek care",
        [
            "Keep drawing the patients before helping the coworker",
            "Hide the incident to avoid the paperwork involved",
            "Test the blood of the coworker instead of following the protocol",
        ],
        "Peer support to start first aid and notification protects the injured worker's health. "
        "Exposure incidents are occupational injuries covered by the employer's control plan.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
]
