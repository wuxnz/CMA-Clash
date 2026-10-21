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
