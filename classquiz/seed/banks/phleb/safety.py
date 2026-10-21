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
            "No gloves when the patient appears healthy",
            "Respirator alone without hand protection",
            "Street clothing with open wounds acceptable at the draw chair",
        ],
        "OSHA and CDC Standard Precautions treat all blood and body fluids as potentially infectious. "
        "Gloves protect both patient and collector; additional PPE follows the anticipated exposure.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-safety",
        "How should used phlebotomy needles be discarded?",
        "Immediately into an approved sharps container at the point of use",
        [
            "In a regular office waste basket lined with paper",
            "In a desk drawer until the end of the shift",
            "After bending and hand-recapping for transport",
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
            "Room number alone without speaking to the patient",
            "Assuming the occupant matches the bed label",
            "Insurance card photo without confirming identity verbally",
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
            "Left open on the counter for quick access",
            "Emptied into regular trash when full",
            "Stored on the floor unlocked in hallways",
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
            "Encouraged during active blood collection",
            "Allowed if tubes are capped nearby",
            "A substitute for hand hygiene between patients",
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
            "One pair may be worn all day for efficiency",
            "When a large visible hole appears in the glove",
            "Between draws in the same room during a batch",
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
            "Clean office paper and unsoiled packaging",
            "Patient personal belongings and clothing",
            "Sterile unused supplies in original boxes",
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
            "Stand for every draw regardless of history",
            "Be left alone immediately after the last tube is filled",
            "Keep a tight tourniquet on for the entire visit",
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
            "At the central lab bench without the patient present",
            "The next day if the draw was busy",
            "On every third tube to save time",
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
        "Cleaned with facility-approved disinfectant on a defined schedule",
        [
            "Wiped with water between every fifth patient",
            "Left untouched because gloves replace cleaning",
            "Sprayed with air freshener instead of disinfectant",
        ],
        "Environmental cleaning is part of Standard Precautions for blood contact areas. "
        "Spills of blood require immediate cleanup with appropriate disinfectant.",
        [S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    fact(
        "phleb-safety",
        "What should staff with open lesions on their hands do?",
        "Avoid patient contact or use approved barriers per occupational health policy",
        [
            "Perform draws without a covering when gloves are worn",
            "Use the same torn gloves for an entire week of draws",
            "Ignore small cuts because the bloodborne risk is zero",
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
            "At the end of the shift for reuse planning",
            "After the patient leaves, because activation increases hemolysis",
            "By another patient to demonstrate the feature",
        ],
        "OSHA expects feasible engineering controls to reduce sharps injuries. "
        "Passive or active safety features must be engaged before disposal.",
        [S.OSHA_NEEDLESTICK, S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What first aid should be provided if blood splashes into the eyes?",
        "Flush with water or saline and report per the exposure control plan",
        [
            "Rubbing the eyes until tearing stops",
            "Waiting until the end of the shift to tell a supervisor",
            "Ignoring minor splashes without documentation",
        ],
        "Mucous membrane exposures to blood require prompt irrigation and occupational health evaluation. "
        "Source-patient testing and prophylaxis follow institutional bloodborne pathogen protocols.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "Why is hand recapping used needles prohibited?",
        "Discouraged; use one-hand scoop or safety devices when recapping is unavoidable",
        [
            "Required before every disposal in sharps boxes",
            "Safer than safety-engineered needles in every case",
            "Recommended to speed multi-patient rounds",
        ],
        "Most needlestick injuries involve recapping or transfer between hands. "
        "OSHA work practice controls favor no recap or mechanical aids.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What must the employer exposure control plan for bloodborne pathogens include?",
        "Engineering controls, work practices, hepatitis B vaccination, and post-exposure follow-up",
        [
            "An annual payroll review with no clinical safety content in it",
            "Optional hepatitis B vaccination with no training requirement",
            "A promise to buy gloves with no written procedures on file",
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
            "Standard precautions without the added isolation PPE",
            "Leaving contaminated tubes in the hallway for later pickup",
            "Removing PPE inside the room before leaving it",
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
            "Ignoring injury if the needle looked clean",
            "Waiting one week to see if symptoms develop",
            "Completing all draws before documentation",
        ],
        "HIV post-exposure prophylaxis has time windows for effectiveness. "
        "OSHA requires employers to document exposures and offer appropriate follow-up testing.",
        [S.OSHA_NEEDLESTICK, S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "How should shared cloth tourniquets between patients be handled?",
        "Managed per facility policy, often disposable or disinfected between uses",
        [
            "Used on every patient without cleaning for speed",
            "Soaked in bleach while still on the patient's arm",
            "Shared with the cafeteria staff for other tasks",
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
            "Hemolysis in every tube that is collected",
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
            "Open tops so staff can add needles while walking",
            "Shaking containers to compact waste further",
            "Placing loose containers on an unsecured passenger seat",
        ],
        "Spills from tipped or overfilled sharps boxes create immediate stick hazards. "
        "Replace containers at the fill line before transport to central storage.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What is required after a blood spill on the phlebotomy floor?",
        "Donning PPE and cleaning with approved disinfectant per spill protocol",
        [
            "Wiping the spill with dry paper towels",
            "Waiting for housekeeping to arrive without placing a barrier",
            "Cleaning the area with bare hands when the volume looks small",
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
        "Not be left unattended; observation continues through and briefly after the procedure",
        [
            "Be acceptable if the patient's eyes are closed during the draw",
            "Be sent to the parking lot alone when the patient feels dizzy",
            "Be restrained without an order when the patient seems nervous",
        ],
        "Syncope can occur seconds after needle removal. "
        "Continuous observation protects patients who underestimate lightheadedness.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What should phlebotomy competency training include?",
        "Venipuncture technique, order of draw, identification, and safety regulations",
        [
            "Billing codes and insurance paperwork without hands-on practice",
            "Social media tips instead of the institutional policy content",
            "No documentation of the completed skills validation",
        ],
        "Employers must ensure staff are qualified before independent collection duties. "
        "CLSI and certification bodies expect documented skills assessment.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "When a patient becomes combative during venipuncture, what should the collector do?",
        "Stop and follow de-escalation and security policy to protect everyone",
        [
            "Force the draw quickly before behavior worsens",
            "Leave needles inserted while calling for help",
            "Use physical restraint without a provider order",
        ],
        "Patient and staff safety outweigh completing the collection in an unsafe moment. "
        "Involve nursing leadership or security per facility violence prevention plans.",
        [S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "What is the recommended approach to hepatitis B vaccination for phlebotomy staff?",
        "Offered by employers at no cost to employees with occupational exposure risk",
        [
            "Forbidden under the OSHA bloodborne pathogen rules",
            "Optional with no requirement to document a written declination",
            "Required for laboratory directors rather than for collectors",
        ],
        "The Bloodborne Pathogens Standard includes hepatitis B vaccine series at employer expense. "
        "Declinations must be documented but vaccination remains strongly recommended.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    fact(
        "phleb-safety",
        "How does privacy during phlebotomy support safety?",
        "Allowing accurate identification and reducing patient stress that can provoke syncope",
        [
            "Eliminating the need for two identifiers",
            "Permitting draws without consent in public hallways",
            "Replacing hand hygiene with privacy curtains",
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
            "Locked to prevent casual use",
            "Used for washing dishes in the break room",
            "Optional at outpatient draw stations that have no policy",
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
            "Changing the needle while reusing the barrel",
            "Sharing multi-dose vials without aseptic technique",
            "Skipping hand hygiene when gloves are available",
        ],
        "Reuse transmits hepatitis and HIV between patients. "
        "Single-use collection systems align with CDC One & Only campaigns for safe injections.",
        [S.WHO_INJECTION_SAFETY, S.CDC_ONE_AND_ONLY],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "How does a safety syringe with a retractable needle reduce risk?",
        "Covering the sharp immediately after use without hand proximity to the point",
        [
            "Eliminating the need for gloves during all draws",
            "Allowing manual recap with two hands faster",
            "Increasing the exposed sharp time after withdrawal",
        ],
        "Engineering controls remove the hazard rather than relying on behavior alone. "
        "OSHA's needlestick prevention rule prioritizes devices that isolate the needle after activation.",
        [S.OSHA_NEEDLESTICK, S.CDC_INJECTION_SAFETY],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What is source-patient testing after a blood exposure used for?",
        "Guide post-exposure prophylaxis and baseline serology for the employee",
        [
            "Punish the patient for the staff injury",
            "Replace wound washing and occupational health referral",
            "Determine billing codes without clinical use",
        ],
        "Knowing source status for HIV, HBV, and HCV shapes monitoring and medication offers. "
        "Consent and local law govern testing; protocols must be followed rapidly.",
        [S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What should central supply of safety lancets for fingersticks ensure?",
        "Single-patient use and activation of sharps injury protection before disposal",
        [
            "Shared lancet devices cleaned with alcohol between patients",
            "Leaving used lancets on the bedside table",
            "Disabling safety caps to speed collection",
        ],
        "Point-of-care devices still create sharps contaminated with blood. "
        "CLSI capillary collection standards align with OSHA controls for injury prevention.",
        [S.CLSI_GP41, S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "When gloves are visibly torn during a draw, what should the collector do?",
        "Stop, remove gloves, perform hand hygiene, and reglove before continuing safely",
        [
            "Finish the procedure because small holes do not matter",
            "Wiping gloves on the pants and keep drawing",
            "Double glove without washing hands underneath",
        ],
        "Visible breaches negate barrier protection and may have already contaminated hands. "
        "Hand hygiene between glove changes maintains Standard Precautions integrity.",
        [S.CDC_HAND_HYGIENE, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What does fire safety during mobile phlebotomy with oxygen in use require?",
        "Avoiding sparks and following facility oxygen precautions in the home or room",
        [
            "Allowing smoking near the cylinders to check airflow",
            "Using alcohol-based products freely on running oxygen tubing",
            "Storing oxygen cylinders horizontal without securing",
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
        "Support positioning and emotional safety while staff maintain aseptic technique",
        [
            "Replace two-identifier verification entirely",
            "Hold the child without collector instruction",
            "Eliminate the need for gloves on the collector",
        ],
        "Parents or guardians help immobilize safely when developmentally appropriate. "
        "Collectors remain responsible for identification, consent, and infection control.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "Which ergonomic practices help prevent injury for full-time phlebotomists?",
        "Adjustable chairs, neutral wrist position, and rotating high-volume tasks",
        [
            "Bending the wrist sharply during every insertion",
            "Drawing exclusively overhead without breaks",
            "Ignoring repetitive strain because gloves protect joints",
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
        "Removed from service and cleaned or discarded per infection control policy",
        [
            "Used on the next patient without cleaning",
            "Rinsed in tap water and air-dried in the lunchroom",
            "Stored in the sharps container",
        ],
        "Blood-soaked linens and equipment require handling as potentially infectious. "
        "Laundry and disinfection follow facility procedures separate from sharps disposal.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "What must annual bloodborne pathogen training for staff cover?",
        "Exposure risks, use of engineering controls, and post-exposure steps",
        [
            "Payroll direct deposit changes",
            "Social media marketing for the laboratory",
            "Parking assignments without clinical content",
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
            "Elimination of patient identification requirements",
            "Automatic correction of order-of-draw errors",
            "Removal of the need for gloves",
        ],
        "Butterfly sets remain a common injury source during connection and disposal. "
        "Safety versions with shields or retractors align with OSHA's hierarchy of controls.",
        [S.OSHA_NEEDLESTICK, S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-safety",
        "When a coworker is stuck with a contaminated needle, what should you do?",
        "Assist them to initiate washing and reporting while they seek occupational health care",
        [
            "Keep drawing patients before helping",
            "Hide the incident to avoid paperwork",
            "Test the coworker's blood instead of following protocol",
        ],
        "Peer support to start first aid and notification protects the injured worker's health. "
        "Exposure incidents are occupational injuries covered by the employer's control plan.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
]
