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
        "At what angle should a needle enter well-developed muscle for a routine intramuscular injection?",
        "90 degrees to the skin surface",
        [
            "45 degrees into the subcutaneous fat layer",
            "15 degrees with bevel up to raise a bleb",
            "30 degrees sliding along the skin surface",
        ],
        "Routine intramuscular technique uses a perpendicular entry so the tip reaches muscle belly. Shallow angles deposit drug in fat or dermis, where absorption differs from IM goals.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-002
    fact(
        "skill-injection",
        "Which needle angle is appropriate for a subcutaneous injection into pinched adipose tissue on the abdomen?",
        "45 to 90 degrees with a pinched abdominal fold",
        [
            "5 to 15 degrees to form an intradermal wheal on the forearm",
            "90 degrees into the deltoid muscle belly for the same drug",
            "45 degrees without pinching the skin and fat at the site",
        ],
        "Subcutaneous insulin and heparin target adipose with a fold that lifts tissue away from muscle. Intradermal angles and deltoid IM placement deliver to different layers than subcutaneous fat.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-003
    fact(
        "skill-injection",
        "How should the syringe be held when placing a tuberculin skin test intradermally?",
        "5 to 15 degrees, bevel up, with a visible bleb",
        [
            "90 degrees into the vastus lateralis thigh muscle",
            "45 degrees into the ventrogluteal gluteal muscle",
            "10 to 15 degrees without raising a visible bleb",
        ],
        "Mantoux testing requires antigen in the dermis, shown by a small bleb. Deep muscle angles place the dose below the layer where induration is read at 48 to 72 hours.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-004
    fact(
        "skill-injection",
        "Why do many protocols prefer the ventrogluteal site over the dorsogluteal site for intramuscular injections?",
        "Bony landmarks keep the needle away from the sciatic nerve",
        [
            "It removes the need for two patient identifiers before injection",
            "It allows a larger adult IM volume in the deltoid muscle",
            "It is required for all intravenous push medications",
        ],
        "The ventrogluteal triangle is defined by the greater trochanter and iliac crest, reducing sciatic nerve injury risk. Identity checks still apply, and IV pushes use a different route than IM gluteal sites.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-005
    fact(
        "skill-injection",
        "Which intramuscular site is commonly taught for infant vaccines and many thigh self-injections?",
        "Anterolateral thigh (vastus lateralis)",
        [
            "Dorsogluteal upper outer quadrant without landmarks",
            "Intradermal forearm for depot medications",
            "Deltoid muscle for all infant IM vaccine volumes",
        ],
        "The vastus lateralis has adequate muscle mass in infants and is standard for many thigh injections. Unlandmarked dorsogluteal sites and small infant deltoids are poor choices for routine IM volumes.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-006
    fact(
        "skill-injection",
        "Which verification steps belong in the medication rights before you draw up an injectable dose?",
        "Right patient, drug, dose, route, time, and documentation",
        [
            "Drug on the MAR matched to the vial label without patient ID",
            "Room number and bed label confirmed on the unit board",
            "Patient states first name without a second identifier",
        ],
        "Rights of administration require confirming the patient and every element of the order before withdrawal. MAR-to-vial matching alone, room labels, or a single name do not verify the correct recipient.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-injection-007
    fact(
        "skill-injection",
        "What should you do with a used needle and syringe immediately after giving an injection?",
        "Dispose intact in sharps without recapping by hand",
        [
            "Recap with one hand before walking to the sharps box",
            "Place in a biohazard bag when the sharps box is full",
            "Set on the counter until central supply collects them",
        ],
        "OSHA work practice controls discourage hand recapping because of stick risk. Puncture-resistant sharps containers are required; soft bags and open counters do not protect staff from needlesticks.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-008
    fact(
        "skill-injection",
        "How often should you rotate subcutaneous injection sites for a patient on daily insulin?",
        "Rotate to a new site on each injection using a pattern",
        [
            "Rotate sites once weekly regardless of injection count",
            "Rotate sites when lipohypertrophy becomes painful or visible",
            "Rotate when switching between rapid and long-acting insulin",
        ],
        "Frequent rotation limits lipohypertrophy and keeps absorption predictable. Weekly-only, pain-driven, or insulin-type rotation leaves high-use areas overused between changes.",
        [S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-009
    fact(
        "skill-injection",
        "Which needle gauge is appropriate for a routine adult deltoid intramuscular vaccine?",
        "22 to 25 gauge for typical aqueous vaccines",
        [
            "18 gauge for every routine deltoid vaccine",
            "27 to 30 gauge for all intramuscular medications",
            "27 to 30 gauge for subcutaneous injections such as heparin",
        ],
        "Adult deltoid vaccines use medium gauges that balance flow and tissue trauma. Very large bore needles add unnecessary pain; fine gauges are common for subcutaneous doses, not all IM products.",
        [S.NHA_CCMA, S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-010
    fact(
        "skill-injection",
        "What should happen to a single-dose vial after you withdraw the ordered amount for one patient?",
        "Discard the vial and any remaining contents",
        [
            "Recap and store in the patient room for the next nurse",
            "Return unused volume to the ward stock multi-dose vial",
            "Refrigerate the capped vial for use on the next shift",
        ],
        "Single-dose containers are for one patient and one encounter. Room storage, pooling into stock vials, or shift-to-shift reuse breaks single-patient vial rules and risks contamination.",
        [S.CDC_ONE_AND_ONLY],
        "intermediate",
    ),
    # skill-injection-011
    fact(
        "skill-injection",
        "Under CDC injection safety guidance, when is it acceptable to enter the same multi-dose vial for multiple patients?",
        "Open, date, and draw the vial in a dedicated medication area",
        [
            "Whenever the stopper looks intact after alcohol swabbing each time",
            "When the patients booked that morning share the same clinic session",
            "When the vial stayed in the refrigerator between patient rooms",
        ],
        "Shared multidose vials need controlled prep, dating, and aseptic technique, not intact rubber alone or shared scheduling. Refrigeration between rooms does not replace beyond-use dating and dedicated prep space.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-injection-012
    fact(
        "skill-injection",
        "How should you time needle insertion after applying alcohol skin prep?",
        "Let the prep air-dry until the skin is no longer wet",
        [
            "Insert while alcohol is still pooling on the skin",
            "Wipe the site dry with gauze immediately after the swab",
            "Insert at once because sterile gloves cover wet prep",
        ],
        "Wet alcohol can sting and may not meet required contact time before puncture. Blotting can remove disinfectant, and gloves do not replace drying the skin.",
        [S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-013
    fact(
        "skill-injection",
        "When must hand hygiene occur in the injection preparation workflow?",
        "Before prep and after glove removal when gloves were used",
        [
            "After donning gloves without cleaning hands at the sink first",
            "After patient contact but not before opening medication vials",
            "When the patient is febrile but not before touching supplies",
        ],
        "CDC expects hand hygiene before medication setup and after gloves come off. Gloves alone do not clean hands before prep, and fever does not waive pre-procedure hygiene.",
        [S.CDC_HAND_HYGIENE, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-014
    fact(
        "skill-injection",
        "Where should most adult intramuscular vaccines be given in the upper extremity?",
        "Deltoid muscle of the upper arm",
        [
            "Gluteus maximus without bony landmarking",
            "Rectus femoris at the mid-calf level",
            "Trapezius at the base of the neck",
        ],
        "CDC adult vaccine guidance lists the deltoid for many IM products. Gluteal and thigh sites need landmarking and volume limits; mid-calf and neck placements are not standard IM landmarks.",
        [S.CDC_VACCINE_ADMIN],
        "beginner",
    ),
    # skill-injection-015
    fact(
        "skill-injection",
        "A refrigerator alarm sounded overnight on the vaccine unit. What must you verify before drawing a dose?",
        "Check expiration, temperature log, and freeze status of vials",
        [
            "Room-temperature rest on the counter for one hour before drawing",
            "Use the soonest-expiring vial despite an out-of-range log entry",
            "Administer if the vial feels cool when held in the hand",
        ],
        "Cold-chain breaks can inactivate biologics; logs and labels guide discard or use. Counter warming, ignoring logs, or touch alone do not confirm safe potency.",
        [S.CDC_VACCINE_STORAGE, S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-016
    fact(
        "skill-injection",
        "Which pre-vaccination step is required before you administer a scheduled immunization?",
        "Screen for contraindications and precautions before the dose",
        [
            "Give the dose to catch up when the immunization schedule is behind",
            "Use an open vial first to limit waste without chart review",
            "Give intradermally when the order lists intramuscular route",
        ],
        "Screening identifies deferrals, precautions, and component allergies before the needle enters skin. Catch-up urgency, open-vial convenience, and route changes still require screening and order match.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-017
    fact(
        "skill-injection",
        "You must give an irritating IM antibiotic that protocol lists for Z-track technique. What does Z-track accomplish?",
        "Traps drug in muscle by displacing skin before injection",
        [
            "Replaces aspiration for all deltoid vaccines in the clinic",
            "Allows IV infusion through the same needle hub used for IM",
            "Documents the injection site without a MAR entry afterward",
        ],
        "Z-track limits subcutaneous tracking of irritating drugs into skin. It does not change IV administration rules, aspiration policy for vaccines, or documentation requirements.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-018
    fact(
        "skill-injection",
        "The prescriber ordered an IM drug, but the package insert lists the route as subcutaneous only. What should you do?",
        "Hold the dose and contact the prescriber to clarify route",
        [
            "Give IM in the deltoid because the chart order says IM",
            "Give IV push to match clinic workflow for faster absorption",
            "Give IM now and document the package insert mismatch later",
        ],
        "Route must match safe labeling and the signed order. Administering IM against the insert is a high-risk error even when the order text says intramuscular.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-019
    fact(
        "skill-injection",
        "Two open multidose vaccine vials from the same lot are on the counter mid-clinic. What is the priority action?",
        "Date and time each open vial and follow beyond-use rules",
        [
            "Draw from whichever vial is nearest without labeling either container",
            "Combine remaining volumes into one unlabeled vial for the same lot",
            "Return both to the fridge without dates for the next clinic day",
        ],
        "Beyond-use dating and labeling prevent use of spoiled or contaminated product. Unlabeled draws, pooling, and undated refrigeration break medication management and infection control rules.",
        [S.CDC_INJECTION_SAFETY],
        "advanced",
    ),
    # skill-injection-020
    fact(
        "skill-injection",
        "Five minutes after a flu shot, the patient develops wheezing and diffuse hives. What is your first action?",
        "Call for help and give IM epinephrine right away",
        [
            "Apply ice to the injection site and recheck symptoms in one hour",
            "Give oral diphenhydramine and observe in the waiting room",
            "Document a local reaction and schedule next year's vaccine visit",
        ],
        "Wheezing with diffuse hives suggests systemic anaphylaxis, not a local injection reaction. Epinephrine and emergency activation come before ice, antihistamine-only care, or routine follow-up scheduling.",
        [S.CDC_VACCINE_ADMIN, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-injection-021
    fact(
        "skill-injection",
        "Which bony landmarks define the ventrogluteal intramuscular injection site?",
        "Greater trochanter and anterior superior iliac spine",
        [
            "Umbilicus and symphysis pubis for gluteal IM sites",
            "Medial and lateral malleolus for thigh IM injections",
            "Acromion process and olecranon for arm IM injections",
        ],
        "The ventrogluteal triangle lies between the iliac crest region and greater trochanter. Abdominal, ankle, and elbow landmark pairs describe other regions, not the ventrogluteal IM site.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-022
    fact(
        "skill-injection",
        "An obese adult needs a gluteal intramuscular injection. Which needle selection principle applies?",
        "Use a longer needle length based on tissue depth",
        [
            "Use a shorter needle to limit discomfort regardless of depth",
            "Use the same needle length for all adults without assessment",
            "Use the finest gauge available regardless of drug viscosity",
        ],
        "Inadequate length deposits drug in adipose tissue and reduces reliable absorption. Comfort-only short needles and one-size-fits-all length ignore adipose depth in larger patients.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-023
    fact(
        "skill-injection",
        "Which elements belong in the medical record right after you give an injection?",
        "Drug, dose, route, site, time, and initial patient response",
        [
            "Time and nurse signature without the medication or dose name",
            "Chief complaint from intake without injection details",
            "Vital signs from the last visit without this administration",
        ],
        "The MAR and nursing note must show what was given, where, and when for safety investigations. Time alone, intake complaints, or old vitals do not document this administration.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-injection-024
    fact(
        "skill-injection",
        "A courier delivers prefilled syringes, but one barrel label is smeared and unreadable. What is the safest action?",
        "Quarantine the syringe and obtain a properly labeled replacement",
        [
            "Use it when the hub color matches another syringe in the shipment",
            "Administer as influenza vaccine because it is flu season",
            "Proceed after the patient names the vaccine they expected",
        ],
        "Unreadable labels prevent verifying drug, dose, and expiration. Hub color, season, and patient recall are not reliable identification before injection.",
        [S.CDC_INJECTION_SAFETY, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-025
    fact(
        "skill-injection",
        "Your facility no longer requires aspiration before routine deltoid vaccines. What evidence supports that change?",
        "Aspiration rarely changes management at routine IM vaccine sites",
        [
            "Aspiration detects every intravascular vaccine dose in the deltoid",
            "Aspiration replaces hand hygiene before vaccine preparation",
            "Aspiration is required for all subcutaneous insulin doses",
        ],
        "Guidelines note limited yield from aspiration during IM immunization in typical sites. Aspiration does not substitute hand hygiene and is not a universal subcutaneous insulin requirement.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-026
    fact(
        "skill-injection",
        "Which practice breaks safe use of a shared medication vial?",
        "Reinserting a used needle into the shared vial",
        [
            "Discarding a bent needle in a sharps container after use",
            "Labeling a multidose vial with open date and initials",
            "Using a new sterile needle to withdraw each ordered dose",
        ],
        "A needle that contacted the patient can carry blood into the vial and expose the next draw. Discarding bent needles, dating vials, and new needles for each withdrawal are expected safe steps.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-injection-027
    fact(
        "skill-injection",
        "What is a safe maximum volume for a single adult deltoid intramuscular injection?",
        "About 1 mL per deltoid; use thigh or gluteal for larger volumes",
        [
            "Up to 5 mL in the deltoid for a medication ordered that clinic day",
            "Up to 10 mL in the deltoid when the patient tolerates pain well",
            "No volume limit in the arm if the needle is long enough to reach muscle",
        ],
        "Deltoid muscle mass limits how much fluid one site can accept safely. Multi-milliliter deltoid doses risk tissue injury and erratic absorption compared with larger muscle groups.",
        [S.NHA_CCMA, S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-028
    fact(
        "skill-injection",
        "You must give two vaccines that are not packaged as a combined product. How should they be administered?",
        "Give each vaccine in its own syringe and at its own site",
        [
            "Draw both vaccines into one syringe to reduce needle sticks",
            "Mix both vials in one cup and withdraw a single combined dose",
            "Place both vaccines in one intradermal bleb on the forearm",
        ],
        "Unless FDA-approved as a combined presentation, each vaccine needs its own syringe, dose, and site. One-syringe mixing risks dosing errors and is not standard administration.",
        [S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-injection-029
    fact(
        "skill-injection",
        "A patient with prior anaphylaxis to gelatin is due for an MMR vaccine. What is the first step?",
        "Provider reviews vaccine ingredients and allergy history first",
        [
            "Administer MMR in the deltoid after standard site preparation",
            "Cancel all future immunizations without a provider consult note",
            "Give MMR and instruct the patient to monitor rash at home",
        ],
        "Component allergies may require deferral, observation, or an alternate product. Giving MMR without review risks repeat anaphylaxis; blanket cancellation skips shared decision-making with the provider.",
        [S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-injection-030
    fact(
        "skill-injection",
        "Which intramuscular site is usually avoided in infants younger than 7 months?",
        "Deltoid muscle of the upper arm",
        [
            "Anterolateral thigh in the middle third of the leg",
            "Ventrogluteal muscle with bony landmarking",
            "Vastus lateralis with adequate muscle mass palpated",
        ],
        "Infant deltoid mass is small for many IM volumes, so thigh sites are preferred. Thigh and ventrogluteal sites remain appropriate when landmarked and muscle is adequate.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-031
    fact(
        "skill-injection",
        "After giving an injection with a safety needle, what should you do with the device?",
        "Activate the safety clip and discard in a sharps container",
        [
            "Leave the shield off until the sharps box has more empty space",
            "Place the device in regular waste at the nurse station",
            "Wipe the hub and store the device for the next patient in the room",
        ],
        "Safety needles must be activated before disposal to prevent needlesticks. Delaying activation, regular trash, and reuse between patients violate sharps and infection control policy.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-032
    fact(
        "skill-injection",
        "You are drawing up medication from a glass ampule. Which step limits glass in the syringe?",
        "Use a filter needle when transferring into the syringe",
        [
            "Snap the ampule with bare fingers over the bed linens",
            "Shake the open ampule hard to mix the solution evenly",
            "Reuse the same drawing needle on several ampules at the cart",
        ],
        "Filter devices trap glass shards during transfer from the ampule. Bare-hand breaking, vigorous shaking, and reused needles increase particles and contamination risk.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-033
    fact(
        "skill-injection",
        "How should cloudy insulin suspension be mixed before withdrawal?",
        "Roll gently between palms until uniformly cloudy",
        [
            "Shake the vial vigorously for two minutes before each dose",
            "Invert and tap hard until all particles fully dissolve",
            "Draw the dose immediately without mixing when it looks cloudy",
        ],
        "Gentle rolling resuspends insulin without air bubbles that can alter dose accuracy. Vigorous shaking and skipping mixing leave uneven suspension; hard tapping does not replace proper rolling.",
        [S.CDC_DIABETES, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-injection-034
    fact(
        "skill-injection",
        "How long should most patients stay in the clinic after routine vaccination?",
        "About 15 minutes; longer if allergy or syncope history",
        [
            "No wait if the patient feels fine walking out to the car",
            "Overnight observation for every injected vaccine dose given in clinic",
            "Five minutes for injectables but not for oral vaccines in the same visit",
        ],
        "CDC recommends brief observation for immediate reactions such as anaphylaxis or fainting. Feeling well at discharge does not rule out early systemic reaction; overnight stay is not routine.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-035
    fact(
        "skill-injection",
        "The syringe label shows another patient's name. What is the correct action?",
        "Discard the syringe and draw a new dose for the correct patient",
        [
            "Give the dose if vitals are normal for the patient in the room",
            "Cross out the name and write the correct name on the label in pen",
            "Return the syringe to the medication refrigerator for later use",
        ],
        "Wrong-label syringes cannot be verified for patient, drug, or dose. Normal vitals, pen relabeling, and refrigerator storage do not correct a patient identity mismatch.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-036
    fact(
        "skill-injection",
        "Where should an adult deltoid intramuscular injection be placed?",
        "Deltoid muscle in the upper arm below the acromion",
        [
            "Directly on the acromion process at the shoulder tip",
            "Antecubital fossa at the elbow crease for IM vaccines",
            "Radial artery at the wrist for intramuscular depot drugs",
        ],
        "Vaccines target deltoid belly inferior to the acromion. The shoulder tip, antecubital fossa, and radial artery risk nerve, vessel, and tendon injury and are not IM landmarks.",
        [S.CDC_VACCINE_ADMIN],
        "beginner",
    ),
    # skill-injection-037
    fact(
        "skill-injection",
        "Why should you avoid injecting into skin that is red, swollen, or broken?",
        "Absorption may vary and local infection may worsen",
        [
            "Inflamed skin is unsuitable for injection at a shallow depth",
            "Drug potency increases in infected tissue at the injection site",
            "Documentation is optional when you choose another intact site",
        ],
        "Inflamed or broken skin alters uptake and may spread bacteria into deeper tissue. Needles can still penetrate redness, potency does not increase in infection, and documentation remains required.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-038
    fact(
        "skill-injection",
        "When should you mix a vaccine that requires reconstitution?",
        "Immediately before administration for the dose you will give",
        [
            "During morning prep for the patients scheduled that clinic day",
            "When the multidose vial is first opened at the start of season",
            "After drawing diluent and holding it refrigerated until later",
        ],
        "Potency drops quickly after reconstitution, so mixing must match the dose you will give now. Batch morning mixing or holding diluted vaccine for hours risks inactive product.",
        [S.CDC_VACCINE_ADMIN, S.CDC_VACCINE_STORAGE],
        "advanced",
    ),
    # skill-injection-039
    fact(
        "skill-injection",
        "How should clinic epinephrine auto-injectors be managed for emergencies?",
        "Unit stock, checked for expiry, with staff trained to use them",
        [
            "Locked in the narcotic vault because epinephrine is controlled",
            "Kept as patient-owned samples behind the pharmacy counter",
            "Listed on the crash cart without replacing expired clinic units",
        ],
        "Anaphylaxis needs immediate intramuscular epinephrine that any trained staff can access. Vault-only or pharmacy-only storage adds delay; crash-cart lists do not replace current clinic stock.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-040
    fact(
        "skill-injection",
        "A patient on warfarin has an IM antibiotic ordered. What should you do before injecting?",
        "Confirm with the provider whether IM is appropriate at this time",
        [
            "Proceed in the deltoid because the order is already signed",
            "Change to IV push to match urgent clinic workflow today",
            "Hold the drug and chart patient refusal without contacting anyone",
        ],
        "Anticoagulation raises bleeding and hematoma risk at IM sites. The prescriber may choose another route or timing; unilateral route changes or silent holds are unsafe.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-041
    fact(
        "skill-injection",
        "What is the correct hand hygiene and glove order for giving an injection?",
        "Hand hygiene, gloves if needed, care, remove gloves, hand hygiene",
        [
            "Don gloves first and clean hands afterward in the room",
            "Reuse gloves between patients after wiping with alcohol at the sink",
            "Remove gloves before drawing medication but not after patient care",
        ],
        "CDC expects hand hygiene before and after glove use during patient care. Reused gloves and partial hygiene break Standard Precautions for injection workflows.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-injection-042
    fact(
        "skill-injection",
        "Ice packs in a vaccine cooler touch the syringe barrels during transport. What is the main risk?",
        "Accidental freezing can inactivate inactivated vaccines",
        [
            "Cold syringes deliver higher potency when barrels freeze solid",
            "Shared ice packs require sharing syringes between patients",
            "Thawed frozen vaccine may be used without checking the log",
        ],
        "Many inactivated vaccines lose potency if frozen. Freezing does not increase potency; temperature logs and discard rules still apply after a freeze event.",
        [S.CDC_VACCINE_STORAGE],
        "advanced",
    ),
]
