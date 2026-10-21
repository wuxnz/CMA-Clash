# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-injection)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-injection-001
    fact(
        "skill-injection",
        "At what angle should an intramuscular injection usually be inserted into well-developed muscle?",
        "90 degrees to the skin surface",
        [
            "15 degrees along the skin plane",
            "45 degrees into subcutaneous fat",
            "180 degrees through folded skin",
        ],
        "IM injections target muscle tissue below the subcutaneous layer. A shallow angle risks depositing medication in fat rather than muscle.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-002
    fact(
        "skill-injection",
        "Which angle range is commonly used for a subcutaneous injection in an area with adequate adipose tissue?",
        "45 to 90 degrees, per site and tissue depth",
        [
            "5 to 15 degrees with bevel up",
            "90 degrees into the deltoid belly",
            "Parallel to the skin without lifting tissue",
        ],
        "Subcutaneous injections are placed into fat, and angle varies with pinch technique and site. Intradermal angles and deltoid IM technique do not match subcutaneous goals.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-003
    fact(
        "skill-injection",
        "How should the syringe be positioned for an intradermal injection such as a tuberculin skin test?",
        "5 to 15 degrees with the bevel facing up, forming a small bleb",
        [
            "90 degrees into the vastus lateralis",
            "45 degrees deep into the gluteus medius",
            "Through clothing into the ventrogluteal site",
        ],
        "Intradermal injections create a visible wheal in the dermis. Deep muscle angles deliver medication below the skin layers where the test is read.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-004
    fact(
        "skill-injection",
        "Why is the ventrogluteal site often preferred over the dorsogluteal site for intramuscular injections?",
        "It lies away from the sciatic nerve when landmarks are used correctly",
        [
            "It requires no patient identification before injection",
            "It is the same landmark as the deltoid in adults",
            "It is used exclusively for intravenous bolus doses",
        ],
        "Landmarks at the ventrogluteal site reduce risk of sciatic nerve injury compared with the upper outer quadrant of the buttock. Identity checks and IV bolus administration are unrelated to site selection.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-005
    fact(
        "skill-injection",
        "Which site is frequently used for intramuscular injections in infants and for many insulin self-injection teachings?",
        "Vastus lateralis in the anterolateral thigh",
        [
            "Dorsogluteal muscle without landmarking",
            "Intradermal skin of the forearm",
            "Carotid triangle at the neck",
        ],
        "The vastus lateralis offers a large muscle mass with limited proximity to major vessels in young patients. Neck and intradermal sites are not routine IM locations.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-006
    fact(
        "skill-injection",
        "Before preparing or giving an injection, which checks align with medication administration safety?",
        "Right patient, medication, dose, route, time, and documentation",
        [
            "Vial cap color matched to the patient's room",
            "Ambient room temperature recorded on the MAR",
            "Verbal first name without a second identifier",
        ],
        "The rights framework targets preventable administration errors. Cap color and room temperature do not verify drug identity or patient matching.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-injection-007
    fact(
        "skill-injection",
        "What is the appropriate action for a used needle and syringe after an injection?",
        "Place them intact in an approved sharps container without recapping",
        [
            "Recap the needle using two hands for transport",
            "Place the syringe in a regular wastebasket if the volume was small",
            "Rinse the needle under tap water for reuse on the next patient",
        ],
        "OSHA and CDC guidance emphasize immediate disposal in sharps containers to prevent needlesticks. Recapping and household-style disposal increase injury risk.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-008
    fact(
        "skill-injection",
        "When should injection sites be rotated for a patient receiving repeated subcutaneous medications?",
        "At each administration using a documented pattern for that medication",
        [
            "Once per year regardless of injection frequency",
            "Once per year regardless of injection frequency",
            "When switching from insulin to an oral drug without site change",
        ],
        "Rotation reduces lipohypertrophy and erratic absorption. Waiting until damage is severe defeats preventive purpose.",
        [S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-009
    fact(
        "skill-injection",
        "Which needle gauge range is typical for an adult intramuscular deltoid injection of routine aqueous medication?",
        "22 to 25 gauge, matched to viscosity and site",
        [
            "10 gauge for all deltoid injections",
            "30 gauge for every intramuscular dose",
            "18 gauge required for subcutaneous heparin",
        ],
        "Gauge selection balances tissue trauma with medication flow. Extremely large or fine gauges are not standard for routine adult IM deltoid doses.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-010
    fact(
        "skill-injection",
        "After drawing medication from a single-dose vial for one patient, what should happen to the vial?",
        "Discard the vial and any unused contents for that patient",
        [
            "Recap and store at the bedside for the next visit",
            "Share remaining volume with a sibling in the same room",
            "Leave the vial open at the nursing station overnight",
        ],
        "Single-dose containers are one patient per vial. Shared or stored partially used vials raise contamination and cross-patient exposure risk.",
        [S.CDC_ONE_AND_ONLY],
        "intermediate",
    ),
    # skill-injection-011
    fact(
        "skill-injection",
        "When may a multi-dose vial be used for more than one patient?",
        "Only when dedicated to a single patient or when policy and labeling support safe multi-patient use",
        [
            "Whenever the rubber stopper looks intact",
            "Whenever the refrigerator temperature was checked once last year",
            "Whenever the patient supplies their own alcohol swabs",
        ],
        "CDC injection safety stresses limiting multidose vials and preventing contamination. Stopper appearance alone does not ensure sterility between patients.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-injection-012
    fact(
        "skill-injection",
        "How long should alcohol or chlorhexidine on the skin dry before needle insertion when used as prep?",
        "Until the skin is dry per product instructions",
        [
            "Inject while the skin is still wet with alcohol",
            "Wipe off all antiseptic immediately with gauze",
            "Skin prep omitted whenever gloves are worn",
        ],
        "Wet antiseptic can irritate tissue and may affect contact time needed for microbial reduction. Gloves do not replace antiseptic drying time.",
        [S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-013
    fact(
        "skill-injection",
        "What hand hygiene is expected before vaccine or medication injection preparation?",
        "Hand hygiene with soap and water or alcohol-based rub per CDC and facility policy",
        [
            "Gloves alone without hand hygiene before donning",
            "Hand hygiene after needlesticks but not before preparation",
            "Hand hygiene when the patient appears ill without prep steps",
        ],
        "CDC lists hand hygiene before preparation and administration. Gloves supplement but do not replace cleaning hands before setup.",
        [S.CDC_HAND_HYGIENE, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-014
    fact(
        "skill-injection",
        "Which muscle is the recommended intramuscular site for many adult vaccine doses in the upper arm?",
        "Deltoid in the arm",
        [
            "Gluteus maximus without landmarking",
            "Rectus femoris at the ankle",
            "Sternocleidomastoid at the neck",
        ],
        "CDC vaccine administration tables specify deltoid for many adult IM vaccines. Lower leg and neck are not standard vaccine IM landmarks.",
        [S.CDC_VACCINE_ADMIN],
        "beginner",
    ),
    # skill-injection-015
    fact(
        "skill-injection",
        "How should refrigerated vaccines be handled immediately before administration?",
        "Verify expiration and follow cold chain storage until drawn up per CDC and manufacturer guidance",
        [
            "Warm vials on a windowsill until labels fade",
            "Use product past expiration if refrigerator was full",
            "Freeze all liquid vaccines to extend shelf life",
        ],
        "Vaccine potency depends on maintained temperature ranges. Freezing or using expired vials can destroy immunogenicity.",
        [S.CDC_VACCINE_STORAGE, S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-016
    fact(
        "skill-injection",
        "Before giving a vaccine, what screening step is required?",
        "Review contraindications and precautions using current CDC guidance and orders",
        [
            "Defer screening when the patient is late for work",
            "Administer any vial in the fridge to reduce waste",
            "Choose intradermal route for all intramuscular vaccines",
        ],
        "Screening prevents administration when risk outweighs benefit. Schedule pressure does not override medical screening.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-017
    fact(
        "skill-injection",
        "What is the purpose of the Z-track intramuscular technique for some irritating medications?",
        "Displace skin and subcutaneous tissue so the track closes after injection, limiting surface leakage",
        [
            "Insert the needle at 15 degrees into the dermis",
            "Eliminate the need to document the injection site",
            "Deliver medication into a peripheral vein quickly",
        ],
        "Z-track seals the path through subcutaneous tissue. It is not an intradermal or intravenous method and still requires documentation.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-018
    fact(
        "skill-injection",
        "A medical assistant is asked to inject a medication whose package insert contraindicates IM use. What is the correct response?",
        "Clarify the order with the prescriber and do not administer until route and dose are confirmed",
        [
            "Give the dose IM anyway because the deltoid is convenient",
            "Switch to IV push without a new order",
            "Document the injection as given and discard the vial secretly",
        ],
        "Route must match the order and safe practice. Changing route without clarification is a medication error.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-019
    fact(
        "skill-injection",
        "During a busy clinic session, two multidose vials of the same vaccine lot sit open on the counter. What is the safest practice?",
        "Follow facility policy for beyond-use dating, labeling, and whether vials remain dedicated to one patient",
        [
            "Draw from whichever vial is closest without labeling",
            "Combine partial vials into one unlabeled container",
            "Return open vials to the refrigerator without dates for reuse next week",
        ],
        "Open multidose vials need dating and contamination controls. Pooling and unlabeled storage increase wrong-patient and spoilage risk.",
        [S.CDC_INJECTION_SAFETY],
        "advanced",
    ),
    # skill-injection-020
    fact(
        "skill-injection",
        "An adult patient reports immediate hives and wheezing within minutes after a vaccine injection. What is the first priority?",
        "Activate emergency response and administer epinephrine per protocol while monitoring airway",
        [
            "Apply a heat pack to the injection site and observe for one hour",
            "Give oral antihistamine alone and send the patient home by bus",
            "Document the reaction and schedule a booster for next week",
        ],
        "Systemic allergic symptoms suggest anaphylaxis, which requires epinephrine and emergency care. Delayed outpatient measures are unsafe first steps.",
        [S.CDC_VACCINE_ADMIN, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-injection-021
    fact(
        "skill-injection",
        "Which landmark pair is used to locate the ventrogluteal intramuscular site?",
        "Greater trochanter and anterior superior iliac spine",
        [
            "Umbilicus and xiphoid process",
            "Medial malleolus and patella",
            "Acromion tip and olecranon without deltoid belly",
        ],
        "The ventrogluteal site is found between the greater trochanter and iliac crest landmarks. Abdominal and ankle landmarks describe unrelated regions.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-022
    fact(
        "skill-injection",
        "When selecting needle length for an intramuscular gluteal injection in a large adult, what factor matters most?",
        "Body habitus and tissue depth to reach muscle without subcutaneous underdosing",
        [
            "Color of the syringe barrel",
            "Whether the patient prefers left or right handed documentation",
            "Day of the week the vial was delivered",
        ],
        "Needle length must penetrate muscle in heavier patients. Cosmetic syringe features do not determine depth.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-023
    fact(
        "skill-injection",
        "What should be documented after administering an injectable medication?",
        "Drug name, dose, route, site, time, and patient response per policy",
        [
            "That the patient left the building without drug details",
            "Staff break schedule for the clinic",
            "Parking spot number assigned to the patient",
        ],
        "The medical record must show what was given and where for continuity and adverse event tracking. Nonclinical details do not substitute.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-injection-024
    fact(
        "skill-injection",
        "A prefilled syringe arrives without a readable label on the barrel. What should the medical assistant do?",
        "Do not use the syringe; obtain a properly labeled product per policy",
        [
            "Assume it is influenza vaccine based on season",
            "Use it if the cap color matches another vial nearby",
            "Transfer contents into an unlabeled tuberculin syringe",
        ],
        "Unlabeled syringes cannot be verified for drug, dose, or expiration. Guessing by cap color risks wrong-drug administration.",
        [S.CDC_INJECTION_SAFETY, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-025
    fact(
        "skill-injection",
        "Why is aspiration during intramuscular injection no longer routinely required in many protocols?",
        "Evidence showed limited benefit for identifying intravascular placement in typical vaccine and IM sites",
        [
            "Aspiration guarantees blood return in every deltoid injection",
            "Aspiration replaces the need for hand hygiene",
            "Aspiration is required for every subcutaneous insulin dose by CDC",
        ],
        "Many guidelines de-emphasize routine aspiration for IM vaccines while emphasizing site and technique. Aspiration does not replace hygiene or apply as a universal subcutaneous rule.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-026
    fact(
        "skill-injection",
        "Which action violates safe injection practices regarding medication vials?",
        "Inserting a syringe that was used on a patient back into a shared vial",
        [
            "Discarding a bent needle in a sharps container",
            "Labeling a patient-specific multidose vial with name and date",
            "Using a new sterile needle to draw each dose",
        ],
        "Re-entering a vial with a patient-used syringe can transfer bloodborne pathogens. New needles and labeled vials support safety.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-injection-027
    fact(
        "skill-injection",
        "What is the maximum recommended volume for a single intramuscular injection site in most adults?",
        "About 2 to 5 mL depending on site and muscle mass",
        [
            "20 mL in the deltoid for any drug",
            "Unlimited volume if the patient consents verbally",
            "0.1 mL in the ventrogluteal site for all medications",
        ],
        "Large volumes split across sites reduce pain and tissue damage. Deltoid capacity is much lower than large gluteal or thigh muscles.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-028
    fact(
        "skill-injection",
        "When mixing two vaccines that are not licensed as a combined product, what is required?",
        "Separate syringes and separate injections unless FDA-approved for combined administration",
        [
            "Draw both products into one syringe to save time",
            "Mix vials in one cup at the bedside",
            "Administer both into the same intradermal bleb",
        ],
        "Unless specifically approved, vaccines need separate administration routes and syringes. Ad hoc mixing is unsafe and off-label.",
        [S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-injection-029
    fact(
        "skill-injection",
        "A patient with a history of anaphylaxis to a vaccine component presents for another immunization. What should occur first?",
        "Provider review of ingredients, risk, and whether vaccination can proceed with precautions",
        [
            "Immediate injection without reading the record",
            "Defer all vaccines permanently without discussion",
            "Substitute oral placebo documented as vaccine",
        ],
        "Contraindications and precautions are individualized. Permanent deferral without evaluation may leave the patient unprotected when alternatives exist.",
        [S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-injection-030
    fact(
        "skill-injection",
        "Which site is generally avoided for routine intramuscular injections in infants under 7 months old?",
        "Deltoid muscle",
        [
            "Vastus lateralis",
            "Ventrogluteal with proper landmarks",
            "Anterolateral thigh with adequate muscle",
        ],
        "Deltoid muscle mass is small in young infants; thigh sites are preferred. Other listed sites remain acceptable when landmarked.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-031
    fact(
        "skill-injection",
        "What should be done with a safety-engine needle device after injection?",
        "Activate the safety feature immediately and dispose in a sharps container",
        [
            "Disable the shield to fit more needles in the box",
            "Place the activated device in regular office waste",
            "Store the device in a drawer for the next patient",
        ],
        "Safety devices prevent needlesticks after use. Disabling or reusing them defeats engineering controls.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-032
    fact(
        "skill-injection",
        "When drawing medication from an ampule, which technique reduces glass particle contamination?",
        "Use a filter needle or straw per policy when transferring from ampule to syringe",
        [
            "Break the ampule with bare hands over the patient's bed",
            "Shake the ampule vigorously after opening",
            "Reuse the same syringe needle on multiple ampules without changing",
        ],
        "Filter needles trap glass shards. Bare-hand breaking and needle reuse increase particle and contamination risk.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-033
    fact(
        "skill-injection",
        "How should insulin be rolled when it is a suspension requiring mixing?",
        "Gently roll between palms; do not shake vigorously unless product labeling directs otherwise",
        [
            "Shake hard for two minutes before every dose",
            "Freeze the vial to dissolve crystals",
            "Warm on a stove before drawing",
        ],
        "Gentle rolling resuspends insulin without creating bubbles that affect dosing. Heat and freezing destroy biologic products.",
        [S.CDC_DIABETES, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-injection-034
    fact(
        "skill-injection",
        "Which observation period after vaccination is commonly recommended in clinic settings?",
        "About 15 minutes for most patients, longer if history of syncope or allergy",
        [
            "No observation if the parking lot is full",
            "24 hours of inpatient monitoring for every injection",
            "Observation limited to oral medications without injections",
        ],
        "Brief post-vaccine observation allows recognition of immediate reactions. Universal inpatient monitoring is not required for routine vaccines.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-035
    fact(
        "skill-injection",
        "A medical assistant notices the wrong patient's label on a prefilled syringe on the tray. What is the correct action?",
        "Remove the syringe from use, verify orders, and prepare a new labeled dose for the correct patient",
        [
            "Administer quickly before anyone notices",
            "Relabel the syringe with a marker without verifying contents",
            "Return the syringe to a communal bin for later use",
        ],
        "Wrong-patient labels require stopping the process and re-preparing. Marker relabeling without verification perpetuates error.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-036
    fact(
        "skill-injection",
        "What is the appropriate deltoid intramuscular landmark in an adult?",
        "Fully expose the upper arm and locate the thickest portion of deltoid below the acromion",
        [
            "Inject at the acromion tip itself",
            "Use the antecubital fossa crease",
            "Place the needle at the wrist pulse",
        ],
        "Deltoid injections target muscle belly inferior to the acromion. Antecubital and wrist sites risk nerve and vessel injury.",
        [S.CDC_VACCINE_ADMIN],
        "beginner",
    ),
    # skill-injection-037
    fact(
        "skill-injection",
        "Why should intramuscular injections avoid sites with active infection, edema, or lesions?",
        "Absorption may be unpredictable and local infection can spread",
        [
            "Needles cannot penetrate inflamed skin",
            "Medication becomes stronger in infected tissue",
            "Documentation is unnecessary on damaged skin",
        ],
        "Compromised tissue alters drug uptake and may worsen local infection. Documentation remains required.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-038
    fact(
        "skill-injection",
        "When a vaccine requires reconstitution, when should diluent and powder be mixed?",
        "Immediately before administration using manufacturer directions",
        [
            "At the start of the clinic week for all patients",
            "After the vial has sat at room temperature for one month",
            "After the patient leaves without mixing per directions",
        ],
        "Reconstituted vaccines have limited stability once mixed. Early mixing risks potency loss and dosing errors.",
        [S.CDC_VACCINE_ADMIN, S.CDC_VACCINE_STORAGE],
        "advanced",
    ),
    # skill-injection-039
    fact(
        "skill-injection",
        "Which practice supports safe handling of prefilled epinephrine auto-injectors in the clinic?",
        "Store in an accessible location, check expiration dates during routine inventory, and train staff on use",
        [
            "Lock devices where no staff knows the location",
            "Remove labels to save shelf space",
            "Share one patient-specific device among all exam rooms without tracking",
        ],
        "Timely access and training support anaphylaxis response. Hidden or unlabeled devices delay care.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-040
    fact(
        "skill-injection",
        "A patient receiving anticoagulant therapy needs an intramuscular injection ordered. What should the medical assistant do first?",
        "Confirm the order with the provider and follow facility guidance on IM use in anticoagulated patients",
        [
            "Inject into the deepest muscle without telling the provider",
            "Switch to intravenous push independently",
            "Withhold the dose and chart refusal without prescriber contact",
        ],
        "Anticoagulation raises bleeding risk at IM sites. Route and timing need prescriber guidance rather than unilateral changes.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-041
    fact(
        "skill-injection",
        "What is the correct sequence when combining hand hygiene and gloves for injection?",
        "Perform hand hygiene, don gloves if indicated, prepare and administer, then remove gloves and perform hand hygiene again",
        [
            "Don gloves first without cleaning hands before or after",
            "Reuse the same gloves between patients without cleaning hands",
            "Remove gloves before preparing medication but not after patient contact",
        ],
        "CDC hand hygiene bookends glove use when gloves are worn. Reused gloves between patients break Standard Precautions.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-injection-042
    fact(
        "skill-injection",
        "During a mass vaccination clinic, ice packs touch vaccine syringes in a transport cooler. What concern should prompt action?",
        "Freezing inactivated vaccines can destroy potency even if vials later thaw",
        [
            "Cold vaccines are safer when frozen solid",
            "Ice contact means doses can be shared between unrelated patients",
            "Frozen vaccines should be shaken and used without logging temperature",
        ],
        "Accidental freezing is a cold-chain failure for many products. Sharing syringes and skipping logs are separate unsafe practices.",
        [S.CDC_VACCINE_STORAGE],
        "advanced",
    ),
]
