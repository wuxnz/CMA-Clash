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
        "90 degrees to the skin",
        [
            "45 degrees into adipose tissue",
            "15 degrees with the bevel sliding under the dermis",
            "30 degrees along the skin surface",
        ],
        "Intramuscular doses are meant to reach muscle belly; shallow angles mimic subcutaneous technique. Fifteen degrees is typical for intradermal tests, not routine IM sites.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-002
    fact(
        "skill-injection",
        "Which needle angle is appropriate for a subcutaneous injection into pinched adipose tissue on the abdomen?",
        "45 to 90 degrees by pinch depth and site",
        [
            "5 to 15 degrees to raise a wheal on the forearm",
            "90 degrees into the deltoid muscle belly for the same drug",
            "10 degrees parallel to the skin without a tissue fold",
        ],
        "Subcutaneous insulin and heparin use fat pads with varied pinch technique. Intradermal angles and deltoid IM placement target different layers.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-003
    fact(
        "skill-injection",
        "How should the syringe be held when placing a tuberculin skin test intradermally?",
        "5 to 15 degrees, bevel up, with a visible bleb",
        [
            "90 degrees into the vastus lateralis for the same antigen",
            "45 degrees into the ventrogluteal muscle for skin testing",
            "90 degrees through clothing on the deltoid for TB testing",
        ],
        "Mantoux tests must deposit antigen in the dermis for proper reading. Deep IM angles place drug below the layer where induration is measured.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-004
    fact(
        "skill-injection",
        "Why do many protocols prefer the ventrogluteal site over the dorsogluteal site for intramuscular injections?",
        "Landmarking reduces risk of sciatic nerve injury",
        [
            "It eliminates the need for two patient identifiers",
            "It is interchangeable with the deltoid for all adult volumes",
            "It is required for all intravenous push medications",
        ],
        "The ventrogluteal site uses bony landmarks that keep the needle away from the sciatic nerve. Identity checks still apply, and IV pushes use different routes.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-005
    fact(
        "skill-injection",
        "Which intramuscular site is commonly taught for infant vaccines and many thigh self-injections?",
        "Anterolateral thigh (vastus lateralis)",
        [
            "Upper outer quadrant of the buttock without landmarks",
            "Intradermal forearm for depot medications",
            "Neck over the sternocleidomastoid",
        ],
        "The vastus lateralis offers adequate muscle mass in infants and insulin teaching. Dorsogluteal sites need careful landmarking, and the neck is not a routine IM location.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-injection-006
    fact(
        "skill-injection",
        "Which verification steps belong in the medication rights before you draw up an injectable dose?",
        "Patient, drug, dose, route, time, and documentation",
        [
            "Drug name on the MAR matched to the vial label without patient ID",
            "Room number confirmed on the whiteboard",
            "First name repeated aloud without a second identifier",
        ],
        "Rights of administration prevent wrong-patient and wrong-drug errors. MAR-to-vial matching still requires patient identification per policy.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-injection-007
    fact(
        "skill-injection",
        "What should you do with a used needle and syringe immediately after giving an injection?",
        "Dispose intact in a sharps container without recapping",
        [
            "Recap with one hand before walking to the sharps box",
            "Place in a biohazard bag if the needle cap is missing",
            "Set on the counter for central supply to collect later",
        ],
        "OSHA work practice controls discourage recapping by hand. Sharps containers are puncture-resistant; biohazard bags and open counters increase stick risk.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-008
    fact(
        "skill-injection",
        "How often should you rotate subcutaneous injection sites for a patient on daily insulin?",
        "Each injection using a mapped rotation pattern",
        [
            "Weekly rotation regardless of injection count",
            "After lipodystrophy becomes painful",
            "When switching between rapid and long-acting insulin only",
        ],
        "Frequent rotation limits lipohypertrophy and erratic absorption. Waiting for pain or rotating by insulin type alone leaves high-use areas overused.",
        [S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-009
    fact(
        "skill-injection",
        "Which needle gauge is appropriate for a routine adult deltoid intramuscular vaccine?",
        "22 to 25 gauge for typical aqueous vaccines",
        [
            "18 gauge for every deltoid vaccine",
            "27 to 30 gauge for all intramuscular drugs",
            "25 gauge reserved for subcutaneous heparin only",
        ],
        "Deltoid IM vaccines use medium gauges that balance flow and tissue trauma. Very large bore needles are unnecessary; fine gauges are common for SubQ, not all IM doses.",
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
            "Save remainder in the refrigerator for a family member",
            "Leave uncapped at the medication cart until end of shift",
        ],
        "Single-dose containers are for one patient and one encounter. Room storage and sharing remainder doses break single-patient vial rules.",
        [S.CDC_ONE_AND_ONLY],
        "intermediate",
    ),
    # skill-injection-011
    fact(
        "skill-injection",
        "Under CDC injection safety guidance, when is it acceptable to enter the same multi-dose vial for multiple patients?",
        "When policy allows shared vials with safe handling and dating",
        [
            "Whenever the stopper appears intact after alcohol swabbing each time",
            "When refrigerator logs were signed once this month for the unit",
            "When patients in the same family share a household medicine cabinet",
        ],
        "Shared multidose vials require contamination controls and dating. Intact stoppers or family relationships do not replace labeling and beyond-use rules.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-injection-012
    fact(
        "skill-injection",
        "How should you time needle insertion after applying alcohol skin prep?",
        "Air dry until the skin is no longer wet per labeling",
        [
            "Insert while alcohol is still pooling on the skin surface",
            "Wipe dry immediately with a gauze pad before puncture",
            "Skip drying when sterile gloves are worn over wet prep",
        ],
        "Wet alcohol can sting and may not meet required contact time. Gloves do not replace drying before puncture.",
        [S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-013
    fact(
        "skill-injection",
        "When must hand hygiene occur in the injection preparation workflow?",
        "Before prep and after glove removal when gloves were used",
        [
            "After donning gloves without prior hand cleaning at the sink",
            "After patient contact but not before drawing medication from vials",
            "When the patient appears febrile but not before touching supplies",
        ],
        "CDC lists hand hygiene before preparation and after glove removal. Gloves alone do not clean hands before setup.",
        [S.CDC_HAND_HYGIENE, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-014
    fact(
        "skill-injection",
        "Where should most adult intramuscular vaccines be given in the upper extremity?",
        "Deltoid muscle of the upper arm",
        [
            "Gluteus maximus without landmarking",
            "Rectus femoris at the mid-calf",
            "Trapezius at the base of the neck",
        ],
        "CDC adult vaccine tables list deltoid for many IM products. Gluteal and thigh sites are used with landmarking and volume limits; mid-calf is not an IM landmark.",
        [S.CDC_VACCINE_ADMIN],
        "beginner",
    ),
    # skill-injection-015
    fact(
        "skill-injection",
        "A refrigerator alarm sounded overnight on the vaccine unit. What must you verify before drawing a dose?",
        "Expiration, temperature log, and no freeze for inactivated vaccines",
        [
            "Room-temperature equilibration on the counter for one hour before use",
            "Administer soonest expiring vial even if the log shows out of range",
            "Freeze vials to reset potency after a warm spell in the unit",
        ],
        "Cold chain breaks can inactivate biologics; logs and labels guide discard or use. Warming on the counter or refreezing does not restore vaccine potency.",
        [S.CDC_VACCINE_STORAGE, S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-016
    fact(
        "skill-injection",
        "Which pre-vaccination step is required before you administer a scheduled immunization?",
        "Screen for contraindications and precautions per CDC guidance",
        [
            "Proceed if the schedule is behind to catch up without a screen",
            "Use any open vial to avoid waste without checking the patient chart",
            "Give intradermally when the order reads intramuscular for the same dose",
        ],
        "Screening identifies deferrals and precautions. Catch-up scheduling and route changes still require screening and order match.",
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
            "Allows IV rate infusion through the same needle hub",
            "Documents the site without a MAR entry after administration",
        ],
        "Z-track limits subcutaneous tracking of irritating drugs. It does not change IV rules or documentation requirements.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-018
    fact(
        "skill-injection",
        "The prescriber ordered an IM drug, but the package insert lists the route as subcutaneous only. What should you do?",
        "Hold the dose and contact the prescriber to clarify route",
        [
            "Give IM in the deltoid because the order is written IM on the chart",
            "Give IV push to match clinic workflow for faster absorption",
            "Administer IM and note the package insert discrepancy later",
        ],
        "Route must match safe labeling and the order. IM administration against the insert is a high-risk error even when the order says IM.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-019
    fact(
        "skill-injection",
        "Two open multidose vaccine vials from the same lot are on the counter mid-clinic. What is the priority action?",
        "Label date/time opened and follow beyond-use policy per vial",
        [
            "Draw from whichever vial is nearest without labeling either container",
            "Pool remaining volumes into one unlabeled vial for the same lot",
            "Return both to the fridge without dates for use next clinic day",
        ],
        "Beyond-use dating and labeling prevent spoiled or contaminated product. Pooling and undated refrigeration break medication management rules.",
        [S.CDC_INJECTION_SAFETY],
        "advanced",
    ),
    # skill-injection-020
    fact(
        "skill-injection",
        "Five minutes after a flu shot, the patient develops wheezing and diffuse hives. What is your first action?",
        "Call for help and give IM epinephrine per protocol",
        [
            "Apply ice to the injection site and recheck symptoms in one hour",
            "Give oral diphenhydramine and observe in the waiting room only",
            "Document a local reaction and schedule next year's vaccine visit",
        ],
        "Wheezing with hives suggests systemic anaphylaxis, not a local reaction. Epinephrine and emergency activation precede antihistamine-only care.",
        [S.CDC_VACCINE_ADMIN, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-injection-021
    fact(
        "skill-injection",
        "Which bony landmarks define the ventrogluteal intramuscular injection site?",
        "Greater trochanter and anterior superior iliac spine",
        [
            "Umbilicus and symphysis pubis for gluteal IM injections",
            "Medial malleolus and lateral malleolus for thigh IM injections",
            "Acromion process and olecranon process for arm IM injections",
        ],
        "The ventrogluteal triangle sits between iliac crest and greater trochanter. Abdominal and ankle pairs describe unrelated regions used for other assessments.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-022
    fact(
        "skill-injection",
        "An obese adult needs a gluteal intramuscular injection. Which needle selection principle applies?",
        "Longer needle length to reach muscle based on tissue depth",
        [
            "Shorter needle to reduce patient discomfort regardless of depth",
            "Same length used for all adults without assessment",
            "Finest gauge available regardless of medication viscosity",
        ],
        "Inadequate length deposits drug in fat, reducing absorption. Comfort-focused short needles in large patients risk subcutaneous depot.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-023
    fact(
        "skill-injection",
        "Which elements belong in the medical record right after you give an injection?",
        "Medication, dose, route, site, time, and initial response",
        [
            "Time and nurse signature without drug name",
            "Patient chief complaint from intake only",
            "Vital signs from last month without the injection details",
        ],
        "MAR and nursing notes must show what was given and where for safety investigations. Chief complaint alone does not document administration.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-injection-024
    fact(
        "skill-injection",
        "A courier delivers prefilled syringes, but one barrel label is smeared and unreadable. What is the safest action?",
        "Quarantine the syringe and obtain a labeled replacement",
        [
            "Use it if the cap color matches another syringe in the same shipment",
            "Assume influenza vaccine because it is flu season in the clinic",
            "Relabel the barrel with a handwritten drug name from memory",
        ],
        "Unreadable labels prevent verifying drug, dose, and expiration. Cap color and season are unreliable; handwritten relabeling is not an approved identification method.",
        [S.CDC_INJECTION_SAFETY, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-025
    fact(
        "skill-injection",
        "Your facility no longer requires aspiration before routine deltoid vaccines. What evidence supports that change?",
        "Aspiration rarely changes care at routine IM vaccine sites",
        [
            "Aspiration detects every intravascular vaccine dose in the deltoid",
            "Aspiration replaces hand hygiene before vaccine preparation steps",
            "Aspiration is required for all subcutaneous insulin doses per CDC",
        ],
        "Guidelines note limited yield from aspiration during IM immunization. It does not substitute hand hygiene and is not a universal SubQ insulin rule.",
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
            "Labeling a multidose vial with patient name and open date",
            "Using a new sterile needle to withdraw each ordered dose",
        ],
        "A needle that contacted the patient can carry blood into the vial. Discarding bent needles and using new needles for draws are expected safe steps.",
        [S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-injection-027
    fact(
        "skill-injection",
        "What is a safe maximum volume for a single adult deltoid intramuscular injection?",
        "About 1 mL in deltoid; larger doses use thigh or gluteal site",
        [
            "Up to 5 mL in the deltoid for any medication ordered that day",
            "Up to 10 mL in the deltoid when the patient tolerates pain well",
            "Unlimited volume in the arm if the needle is long enough to reach",
        ],
        "Deltoid muscle mass limits volume; larger doses are split or given in bigger muscles. High deltoid volumes risk tissue injury and erratic absorption.",
        [S.NHA_CCMA, S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-028
    fact(
        "skill-injection",
        "You must give two vaccines that are not packaged as a combined product. How should they be administered?",
        "Separate syringes and injections at appropriate sites",
        [
            "Draw both vaccines into one syringe to reduce needle sticks",
            "Mix both vials in one cup then draw a single dose",
            "Place both vaccines in one intradermal bleb on the forearm",
        ],
        "Unless FDA-approved as a combined presentation, vaccines need separate syringes and sites. One-syringe mixing is off-label and risks dosing errors.",
        [S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-injection-029
    fact(
        "skill-injection",
        "A patient with prior anaphylaxis to gelatin is due for an MMR vaccine. What is the first step?",
        "Provider reviews vaccine ingredients and allergy history first",
        [
            "Administer MMR in the deltoid without reading the allergy chart",
            "Cancel all future immunizations without a consult note in the record",
            "Document vaccine given and monitor for rash only at home",
        ],
        "Component allergies may require deferral, observation, or alternate products. Giving MMR without review risks repeat anaphylaxis; blanket cancellation skips shared decision-making.",
        [S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-injection-030
    fact(
        "skill-injection",
        "Which intramuscular site is usually avoided in infants younger than 7 months?",
        "Deltoid muscle of the upper arm",
        [
            "Anterolateral thigh (vastus lateralis)",
            "Ventrogluteal muscle with landmarking",
            "Vastus lateralis with adequate muscle mass",
        ],
        "Infant deltoid mass is small for many IM volumes; thigh sites are preferred. Thigh and ventrogluteal sites remain appropriate when landmarked.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-031
    fact(
        "skill-injection",
        "After giving an injection with a safety needle, what should you do with the device?",
        "Activate the safety clip and discard in sharps",
        [
            "Deactivate the shield to save space in the sharps container box",
            "Place the capped needle in a regular waste bin at the nurse station",
            "Save the device in a drawer for the next patient in that room",
        ],
        "Safety needles must be activated before disposal to prevent sticks. Regular waste and reuse between patients violate sharps policy.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-injection-032
    fact(
        "skill-injection",
        "You are drawing up medication from a glass ampule. Which step limits glass in the syringe?",
        "Use a filter needle when transferring to the syringe",
        [
            "Snap the ampule with bare fingers over the bed linens",
            "Shake the ampule hard after it is open to mix the solution",
            "Reuse the same drawing needle on several ampules from the cart",
        ],
        "Filter devices trap glass shards during transfer. Bare-hand breaking and reused needles increase particles and contamination risk.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-injection-033
    fact(
        "skill-injection",
        "How should cloudy insulin suspension be mixed before withdrawal?",
        "Roll gently between palms until uniformly cloudy",
        [
            "Vigorously shake for two minutes before each dose",
            "Freeze the vial briefly to dissolve crystals",
            "Warm the vial on a hot plate before drawing",
        ],
        "Gentle rolling resuspends insulin without air bubbles that alter dose. Freezing and heating damage the product.",
        [S.CDC_DIABETES, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-injection-034
    fact(
        "skill-injection",
        "How long should most patients stay in the clinic after routine vaccination?",
        "About 15 minutes; longer if allergy or syncope history",
        [
            "No wait if the patient feels fine walking to the car",
            "Overnight observation for every injected vaccine",
            "Five minutes for injectables but not for oral vaccines",
        ],
        "CDC recommends brief observation for immediate reactions. Feeling well at discharge does not rule out early anaphylaxis; overnight stay is not routine.",
        [S.CDC_VACCINE_ADMIN],
        "intermediate",
    ),
    # skill-injection-035
    fact(
        "skill-injection",
        "The syringe label shows another patient's name. What is the correct action?",
        "Discard the syringe and prepare a new dose for the right patient",
        [
            "Give the dose if vitals are normal for your patient in the room",
            "Cross out the name and write the correct name in pen on the label",
            "Return the syringe to the medication refrigerator for the next nurse",
        ],
        "Wrong-label syringes cannot be verified for patient or drug. Pen relabeling without pharmacy verification perpetuates error; refrigerator storage does not fix identity.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-036
    fact(
        "skill-injection",
        "Where should an adult deltoid intramuscular injection be placed?",
        "Deltoid muscle in the upper arm below the acromion",
        [
            "Directly on the acromion process tip of the shoulder",
            "Antecubital fossa at the elbow crease for IM vaccines",
            "Radial artery at the wrist for intramuscular depot drugs",
        ],
        "Vaccines target deltoid belly inferior to the acromion. Elbow and wrist sites risk nerve and vessel injury and are not IM landmarks.",
        [S.CDC_VACCINE_ADMIN],
        "beginner",
    ),
    # skill-injection-037
    fact(
        "skill-injection",
        "Why should you avoid injecting into skin that is red, swollen, or broken?",
        "Absorption may vary and local infection may worsen",
        [
            "Needles cannot pass through inflamed epidermis at any depth",
            "Medication potency doubles in infected tissue at the site",
            "MAR documentation is waived on damaged skin per clinic policy",
        ],
        "Inflamed tissue alters uptake and may spread bacteria. Documentation is still required even when you choose another site.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-038
    fact(
        "skill-injection",
        "When should you mix a vaccine that requires reconstitution?",
        "At administration time per the vaccine package insert",
        [
            "During morning vaccine prep for every patient scheduled that clinic day",
            "When the multidose vial is first opened at the start of the vaccine season",
            "After diluent is drawn and refrigerated until the nurse has a free moment",
        ],
        "Potency drops quickly after reconstitution, so mixing must match the dose you will give now. Batch mixing at open or holding diluted vaccine for hours risks inactive product; mixing only after the visit misses the ordered immunization.",
        [S.CDC_VACCINE_ADMIN, S.CDC_VACCINE_STORAGE],
        "advanced",
    ),
    # skill-injection-039
    fact(
        "skill-injection",
        "How should clinic epinephrine auto-injectors be managed for emergencies?",
        "Labeled unit stock, checked for expiry, with staff trained to use it",
        [
            "Kept in the narcotic vault because epinephrine is a controlled substance",
            "Stored behind the pharmacy counter as patient-owned samples only",
            "Listed on the crash cart inventory without replacing expired clinic units",
        ],
        "Anaphylaxis needs immediate IM epinephrine any staff member can find. Vault-only or pharmacy-only storage adds delay; relying on personal auto-injectors or an outdated crash-cart list leaves gaps when stock expires.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-injection-040
    fact(
        "skill-injection",
        "A patient on warfarin has an IM antibiotic ordered. What should you do before injecting?",
        "Confirm with the provider whether IM is appropriate now",
        [
            "Proceed in the deltoid because the order is signed",
            "Change to IV push to match urgent clinic flow",
            "Hold the drug and chart patient refusal without calling",
        ],
        "Anticoagulation raises bleeding risk at IM sites. The prescriber may choose another route or timing; unilateral route changes are unsafe.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-injection-041
    fact(
        "skill-injection",
        "What is the correct hand hygiene and glove order for giving an injection?",
        "Hand hygiene, gloves if needed, care, remove gloves, hand hygiene",
        [
            "Don gloves first and skip hand cleaning afterward in the room",
            "Reuse gloves between patients after wiping with alcohol at the sink",
            "Remove gloves before drawing medication only, not after patient care",
        ],
        "CDC expects hand hygiene before and after glove use. Reused gloves and partial hygiene break Standard Precautions.",
        [S.CDC_HAND_HYGIENE],
        "beginner",
    ),
    # skill-injection-042
    fact(
        "skill-injection",
        "Ice packs in a vaccine cooler touch the syringe barrels during transport. What is the main risk?",
        "Accidental freezing can inactivate inactivated vaccines",
        [
            "Cold syringes are more potent when frozen solid",
            "Shared ice packs require sharing syringes between patients",
            "Frozen vaccine may be shaken and used without logging temps",
        ],
        "Many inactivated vaccines lose potency if frozen. Potency does not increase with freezing; temperature logs still matter after thaw.",
        [S.CDC_VACCINE_STORAGE],
        "advanced",
    ),
]
