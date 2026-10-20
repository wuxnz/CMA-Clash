# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

FACTS: list[dict] = [
    {
        "topic": "skill-injection",
        "stem": "Intramuscular (IM) injection angle is typically:",
        "correct": "90 degrees",
        "distractors": [
            "15 degrees",
            "45 degrees only",
            "Parallel to skin"
        ],
        "explanation": "IM delivers into muscle mass.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-injection",
        "stem": "Subcutaneous (SubQ) injection angle is commonly:",
        "correct": "45–90 degrees depending on site and tissue",
        "distractors": [
            "Always 90",
            "Always 15",
            "Through hair without prep"
        ],
        "explanation": "SubQ goes into adipose tissue.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-injection",
        "stem": "Intradermal (ID) injection angle is:",
        "correct": "5–15 degrees with bevel up",
        "distractors": [
            "90 degrees",
            "180 degrees",
            "Any angle"
        ],
        "explanation": "ID is for tests like TB skin test.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-injection",
        "stem": "Ventrogluteal IM site is preferred in many protocols because it:",
        "correct": "Avoids major nerves and vessels of dorsogluteal site",
        "distractors": [
            "Is on the arm only",
            "Requires no identification",
            "Is always lateral thigh"
        ],
        "explanation": "Landmark using iliac crest and greater trochanter.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-injection",
        "stem": "Vastus lateralis IM site in thigh is:",
        "correct": "Common for infants and self-injection training",
        "distractors": [
            "Forbidden in adults",
            "Only for IV drugs",
            "SubQ only"
        ],
        "explanation": "Large muscle away from major vessels.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-injection",
        "stem": "Before injection, verify:",
        "correct": "Medication, dose, route, expiration, and patient identity",
        "distractors": [
            "Only patient name verbally",
            "Color of vial cap only",
            "Room temperature only"
        ],
        "explanation": "Rights of medication administration reduce errors.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-injection",
        "stem": "Aspiration during IM injection policy:",
        "correct": "Follow facility policy; many no longer require routine aspiration",
        "distractors": [
            "Always aspirate 30 seconds",
            "Never use sterile technique",
            "Skip site rotation"
        ],
        "explanation": "Evidence and policy guide aspiration practice.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-injection",
        "stem": "Needle gauge for IM adult deltoid often is:",
        "correct": "22–25 gauge depending on viscosity",
        "distractors": [
            "18 gauge always",
            "30 gauge only",
            "No standard"
        ],
        "explanation": "Select gauge and length per medication and site.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-injection",
        "stem": "Rotate injection sites to:",
        "correct": "Prevent lipodystrophy and tissue damage",
        "distractors": [
            "Increase pain always",
            "Avoid absorption",
            "Skip documentation"
        ],
        "explanation": "Rotation preserves tissue integrity.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-injection",
        "stem": "Dispose of used syringe:",
        "correct": "Immediately in sharps container without recapping",
        "distractors": [
            "Recap with two hands",
            "Place in regular trash",
            "Reuse if needle looks clean"
        ],
        "explanation": "Sharps safety prevents needlestick.",
        "references": [
            "CDC",
            "OSHA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-injection",
        "stem": "Z-track technique for IM helps:",
        "correct": "Prevent medication leakage into subcutaneous tissue",
        "distractors": [
            "Speed injection without prep",
            "Eliminate need for gloves",
            "Is only for SubQ"
        ],
        "explanation": "Pull skin aside before injection then release.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "skill-injection",
        "stem": "After IM injection, massage site:",
        "correct": "Only if medication policy allows; some contraindicated",
        "distractors": [
            "Always vigorously",
            "Never document",
            "Skip observation"
        ],
        "explanation": "Some drugs specify no massage.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-vitals",
        "stem": "Normal adult resting pulse is commonly:",
        "correct": "60–100 beats per minute",
        "distractors": [
            "40–50 bpm always",
            "120–150 bpm",
            "Same as respiratory rate always"
        ],
        "explanation": "Rate varies with fitness, meds, and illness.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-vitals",
        "stem": "Blood pressure cuff bladder width should be:",
        "correct": "About 40% of arm circumference",
        "distractors": [
            "As narrow as possible",
            "Cover entire upper arm length only",
            "Smaller than arm always"
        ],
        "explanation": "Wrong cuff size skews readings.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-vitals",
        "stem": "Korotkoff phase I sound indicates:",
        "correct": "Systolic blood pressure",
        "distractors": [
            "Diastolic pressure",
            "Mean arterial only",
            "Pulse oximetry"
        ],
        "explanation": "First tapping sound marks systolic.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-vitals",
        "stem": "Orthostatic hypotension criteria often include:",
        "correct": "Systolic drop ≥20 mmHg or diastolic ≥10 after standing",
        "distractors": [
            "No change allowed",
            "Only heart rate drop",
            "Rise in BP when standing"
        ],
        "explanation": "Document symptoms like dizziness.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-vitals",
        "stem": "Oral temperature is contraindicated in:",
        "correct": "Patients who cannot cooperate, are NPO perioperative, or have facial oxygen",
        "distractors": [
            "All adults",
            "Every pediatric visit",
            "Hypertension only"
        ],
        "explanation": "Use rectal, axillary, or tympanic per order.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-vitals",
        "stem": "Pulse oximetry measures:",
        "correct": "Oxygen saturation via light absorption",
        "distractors": [
            "Invasive PaO2",
            "Blood pressure",
            "Respiratory rate always directly"
        ],
        "explanation": "Probe site must have good perfusion.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-vitals",
        "stem": "Apical pulse is counted at:",
        "correct": "Heart apex with stethoscope for one full minute if irregular",
        "distractors": [
            "Radial always for 5 seconds",
            "Carotid during exercise",
            "Popliteal only"
        ],
        "explanation": "Irregular rhythms need full minute apical.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-vitals",
        "stem": "Respiratory rate should be counted:",
        "correct": "Discreetly for full minute when possible",
        "distractors": [
            "Only after telling patient to breathe fast",
            "By asking patient only",
            "Once per week"
        ],
        "explanation": "Patients may alter breathing if aware.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-vitals",
        "stem": "A fever in adults is often defined as:",
        "correct": "Oral temperature ≥38°C (100.4°F)",
        "distractors": [
            "37°C exactly",
            "35°C",
            "39.5°C only"
        ],
        "explanation": "Use site-specific normal ranges.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-vitals",
        "stem": "Automated BP devices require:",
        "correct": "Proper cuff size and patient stillness",
        "distractors": [
            "Arm above head always",
            "Talking during measurement only",
            "Cuff over clothing always"
        ],
        "explanation": "Follow manufacturer and validate per policy.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-vitals",
        "stem": "Pain assessment should use:",
        "correct": "Validated scale appropriate to patient age and cognition",
        "distractors": [
            "Only yes/no without score",
            "Assumption of no pain",
            "Vital signs only"
        ],
        "explanation": "Pain is the fifth vital sign in many settings.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-vitals",
        "stem": "Documenting vitals includes:",
        "correct": "Values, time, position, site, and unusual findings",
        "distractors": [
            "Only if abnormal",
            "Patient gossip",
            "Unrelated labs"
        ],
        "explanation": "Complete records support clinical decisions.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-infection",
        "stem": "Hand hygiene is performed:",
        "correct": "Before and after patient contact and after removing gloves",
        "distractors": [
            "Only at lunch",
            "Instead of gloves always",
            "Once per week"
        ],
        "explanation": "Alcohol-based rub or soap and water per CDC.",
        "references": [
            "CDC"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-infection",
        "stem": "Standard Precautions treat:",
        "correct": "All blood and body fluids as potentially infectious",
        "distractors": [
            "Only known HIV patients",
            "Only in hospitals",
            "Only surgical patients"
        ],
        "explanation": "Assume all patients may harbor transmissible agents.",
        "references": [
            "CDC"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-infection",
        "stem": "Transmission-Based Precautions for airborne diseases may require:",
        "correct": "Negative pressure room and N95 or higher respirator",
        "distractors": [
            "Only gloves",
            "No mask",
            "Open door always"
        ],
        "explanation": "Examples include TB and measles per policy.",
        "references": [
            "CDC"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-infection",
        "stem": "Contact Precautions require:",
        "correct": "Gown and gloves for room entry; dedicated equipment when possible",
        "distractors": [
            "Only hand sanitizer",
            "Street clothes",
            "No signage"
        ],
        "explanation": "Use for MRSA, C. diff contact per policy.",
        "references": [
            "CDC"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-infection",
        "stem": "Droplet Precautions use:",
        "correct": "Surgical mask within 3–6 feet of patient",
        "distractors": [
            "N95 always",
            "No PPE",
            "Positive pressure room"
        ],
        "explanation": "Influenza and pertussis may need droplet.",
        "references": [
            "CDC"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-infection",
        "stem": "Sharps injury prevention includes:",
        "correct": "Not recapping needles and using safety devices",
        "distractors": [
            "Recapping with two hands",
            "Passing uncapped needles",
            "Bending needles"
        ],
        "explanation": "Engineering controls reduce risk.",
        "references": [
            "OSHA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-infection",
        "stem": "Cleaning visibly soiled surfaces uses:",
        "correct": "EPA-registered disinfectant per contact time",
        "distractors": [
            "Water only",
            "Air freshener",
            "UV wand only"
        ],
        "explanation": "Follow kill times on product label.",
        "references": [
            "CDC"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-infection",
        "stem": "Sterilization differs from disinfection because sterilization:",
        "correct": "Destroys all microbial life including spores",
        "distractors": [
            "Only reduces bacteria somewhat",
            "Is same as hand washing",
            "Works on living tissue"
        ],
        "explanation": "High-level disinfection has defined limits.",
        "references": [
            "CDC"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "skill-infection",
        "stem": "Biohazard bags are:",
        "correct": "Labeled and leak-resistant for regulated waste",
        "distractors": [
            "Regular trash bags",
            "Reused grocery bags",
            "Optional"
        ],
        "explanation": "Segregate contaminated waste.",
        "references": [
            "OSHA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-infection",
        "stem": "Personal items on counter during sterile procedure:",
        "correct": "Should not enter sterile field",
        "distractors": [
            "Improve sterility",
            "Replace hand hygiene",
            "Are encouraged"
        ],
        "explanation": "Non-sterile items break sterility.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-infection",
        "stem": "C. difficile spores may require:",
        "correct": "Contact precautions with soap and water hand washing emphasis",
        "distractors": [
            "Only alcohol rub",
            "No isolation",
            "Airborne room always"
        ],
        "explanation": "Alcohol may not remove spores well.",
        "references": [
            "CDC"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "skill-infection",
        "stem": "Vaccine storage in clinic requires:",
        "correct": "Temperature monitoring per CDC vaccine guidelines",
        "distractors": [
            "Room temperature always",
            "Freezer for all vaccines",
            "No documentation"
        ],
        "explanation": "Cold chain maintains potency.",
        "references": [
            "CDC"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-terminology",
        "stem": "The prefix \"hyper-\" means:",
        "correct": "Excessive or above normal",
        "distractors": [
            "Below normal",
            "Pain",
            "Inflammation"
        ],
        "explanation": "Hyperglycemia is high blood glucose.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "The suffix \"-ectomy\" means:",
        "correct": "Surgical removal",
        "distractors": [
            "Inflammation",
            "Enlargement",
            "Record or study"
        ],
        "explanation": "Appendectomy removes appendix.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Dyspnea\" means:",
        "correct": "Difficult or labored breathing",
        "distractors": [
            "Fast heart rate",
            "Joint pain",
            "Blurred vision"
        ],
        "explanation": "Common symptom in cardiopulmonary disease.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Pruritus\" means:",
        "correct": "Itching",
        "distractors": [
            "Bleeding",
            "Swelling",
            "Numbness"
        ],
        "explanation": "Reported in dermatologic conditions.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Hypertension\" is:",
        "correct": "High blood pressure",
        "distractors": [
            "Low blood pressure",
            "Fast breathing",
            "High blood sugar"
        ],
        "explanation": "Chronic elevation increases cardiovascular risk.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Tachycardia\" means:",
        "correct": "Rapid heart rate",
        "distractors": [
            "Slow heart rate",
            "Irregular rhythm only",
            "Stopped heart"
        ],
        "explanation": "Rate context defines clinical significance.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Cyanosis\" indicates:",
        "correct": "Bluish discoloration from deoxygenated hemoglobin",
        "distractors": [
            "Yellow skin",
            "Red rash",
            "White patches"
        ],
        "explanation": "Seen in lips and nail beds when severe.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"NPO\" means:",
        "correct": "Nothing by mouth",
        "distractors": [
            "New patient only",
            "Normal pulse observed",
            "Night post-op only"
        ],
        "explanation": "Orders restrict oral intake.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"BID\" on a prescription means:",
        "correct": "Twice daily",
        "distractors": [
            "Once daily",
            "Every hour",
            "As needed only"
        ],
        "explanation": "Latin abbreviations are being replaced with plain language.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Edema\" is:",
        "correct": "Swelling from fluid in tissues",
        "distractors": [
            "Bone fracture",
            "Hair loss",
            "Cough"
        ],
        "explanation": "Often noted in ankles with heart failure.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Contraindication\" means:",
        "correct": "Reason to avoid a treatment due to harm risk",
        "distractors": [
            "Required treatment",
            "Side effect only",
            "Allergic reaction always"
        ],
        "explanation": "Relative vs absolute contraindications exist.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-terminology",
        "stem": "\"Benign\" typically means:",
        "correct": "Not cancerous or mild in course",
        "distractors": [
            "Malignant",
            "Always fatal",
            "Infectious"
        ],
        "explanation": "Context matters; \"benign\" tumor is non-cancer.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "If a order reads 500 mg and tablets are 250 mg each, give:",
        "correct": "2 tablets",
        "distractors": [
            "1 tablet",
            "4 tablets",
            "0.5 tablet"
        ],
        "explanation": "Divide desired dose by strength per unit.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "A suspension labeled 200 mg/5 mL; dose 400 mg equals:",
        "correct": "10 mL",
        "distractors": [
            "5 mL",
            "2.5 mL",
            "20 mL"
        ],
        "explanation": "Set up ratio: 400/200 × 5 mL.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "Pediatric weight-based dosing requires:",
        "correct": "Accurate weight in kg and verification of calculation",
        "distractors": [
            "Age in months only",
            "Height only",
            "Guess if scale broken"
        ],
        "explanation": "Double-check high-alert meds with another staff.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "\"Rights\" of medication administration include:",
        "correct": "Right patient, drug, dose, route, time, documentation, reason, response",
        "distractors": [
            "Only right room",
            "Right color of pill only",
            "Right insurance"
        ],
        "explanation": "Systematic checks reduce errors.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "Insulin syringe units match:",
        "correct": "U-100 insulin concentration unless otherwise labeled",
        "distractors": [
            "Any insulin vial",
            "IV fluids",
            "Oral tablets only"
        ],
        "explanation": "Never use U-100 syringe for U-500 without training.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "A teaspoon household measure is NOT preferred because:",
        "correct": "It is inaccurate compared to metric mL measuring devices",
        "distractors": [
            "It is always 10 mL",
            "It is FDA preferred",
            "It replaces oral syringe"
        ],
        "explanation": "Use oral syringe or cup marked in mL.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "If 1 L IV fluid runs over 8 hours, hourly rate is:",
        "correct": "125 mL/hr",
        "distractors": [
            "250 mL/hr",
            "62.5 mL/hr",
            "500 mL/hr"
        ],
        "explanation": "1000 mL ÷ 8 h = 125 mL/h.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "Drops (gtt) calculation depends on:",
        "correct": "Drop factor of tubing (gtt/mL)",
        "distractors": [
            "Patient weight only",
            "Room temperature",
            "Syringe color"
        ],
        "explanation": "Macro vs micro drip sets differ.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "High-alert medications include:",
        "correct": "Insulin, anticoagulants, and opioids per ISMP list",
        "distractors": [
            "Multivitamins only",
            "Saline flush only",
            "Stool softeners only"
        ],
        "explanation": "Extra safeguards for high-alert drugs.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "Crushing enteric-coated tablets:",
        "correct": "Is contraindicated unless specifically ordered",
        "distractors": [
            "Is always safe",
            "Improves absorption always",
            "Required for all elderly"
        ],
        "explanation": "Coating protects drug or stomach.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "Topical medication application documentation should note:",
        "correct": "Site, amount, and patient response",
        "distractors": [
            "Only time",
            "Staff mood",
            "Weather"
        ],
        "explanation": "Some topicals have rotation sites.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-pharm-dosage",
        "stem": "A 0.5 mg dose from 2 mg/mL solution requires:",
        "correct": "0.25 mL",
        "distractors": [
            "1 mL",
            "2 mL",
            "0.5 mL"
        ],
        "explanation": "Dose/volume: 0.5/2 = 0.25 mL.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "A urine specimen for routine urinalysis is often:",
        "correct": "Clean-catch midstream",
        "distractors": [
            "First drop only",
            "From bedpan without label",
            "Mixed with water"
        ],
        "explanation": "Clean-catch reduces contamination.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "24-hour urine collection requires:",
        "correct": "Discarding first morning void then collecting all urine for 24 hours",
        "distractors": [
            "Saving only last void",
            "Adding preservative without order",
            "Room temperature only always"
        ],
        "explanation": "Follow lab instructions for preservatives.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Stool occult blood testing patient teaching includes:",
        "correct": "Avoid certain foods/meds per kit instructions",
        "distractors": [
            "Brush teeth with blood only",
            "Collect from toilet water freely",
            "Freeze sample unless directed"
        ],
        "explanation": "Diet restrictions reduce false positives.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Throat swab for strep should avoid:",
        "correct": "Touching tongue, teeth, and cheeks before tonsillar area",
        "distractors": [
            "Deep nasal only",
            "Saliva cup only",
            "Left ear"
        ],
        "explanation": "Swab posterior pharynx and tonsils.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Sputum culture specimen should be:",
        "correct": "Deep cough expectorate into sterile container",
        "distractors": [
            "Saliva only",
            "Nasal swab only",
            "Tap water rinse first"
        ],
        "explanation": "Morning specimen may be preferred.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Pregnancy urine test detects:",
        "correct": "hCG hormone in urine",
        "distractors": [
            "Progesterone only",
            "Blood type",
            "Glucose only"
        ],
        "explanation": "Follow kit timing and reading window.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Fasting lipid panel requires:",
        "correct": "Typically 9–12 hour fast per lab order",
        "distractors": [
            "Only water fast forbidden",
            "Full meal before draw",
            "No patient teaching"
        ],
        "explanation": "Preanalytic fasting affects triglycerides.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Blood glucose meter quality control includes:",
        "correct": "Running control solution per manufacturer schedule",
        "distractors": [
            "Never checking strips",
            "Using expired strips",
            "Sharing lancets"
        ],
        "explanation": "QC ensures device accuracy.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Chain of custody urine drug screen requires:",
        "correct": "Sealed container with witnessed collection per policy",
        "distractors": [
            "Patient takes cup home",
            "Open container transport",
            "No ID check"
        ],
        "explanation": "Forensic procedures differ from routine UA.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Prothrombin time specimen handling:",
        "correct": "Deliver promptly; avoid hemolysis and clot",
        "distractors": [
            "Freeze tube",
            "Shake vigorously",
            "Leave in sun"
        ],
        "explanation": "Coagulation assays are time-sensitive.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Microbiology culture transport may need:",
        "correct": "Appropriate temperature and media within stability window",
        "distractors": [
            "Hot car trunk long term",
            "Delayed days without media",
            "Unlabeled jar"
        ],
        "explanation": "Viability depends on timely processing.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-specimen-lab",
        "stem": "Point-of-care testing documentation includes:",
        "correct": "Result, time, device lot, and operator initials",
        "distractors": [
            "Only abnormal flagged",
            "Patient SSN on sticky note",
            "No QC log"
        ],
        "explanation": "POCT is regulated under CLIA in US.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-intake",
        "stem": "Patient intake begins with:",
        "correct": "Verifying identity and reason for visit",
        "distractors": [
            "Billing discussion only",
            "Random room assignment",
            "Skipping allergies"
        ],
        "explanation": "Accurate demographics and chief complaint anchor care.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-intake",
        "stem": "Chief complaint is:",
        "correct": "Patient's stated primary reason for visit in their words",
        "distractors": [
            "Physician diagnosis code",
            "Insurance plan name",
            "Staff schedule"
        ],
        "explanation": "Document briefly in quotes when appropriate.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-intake",
        "stem": "Medication reconciliation at intake collects:",
        "correct": "All prescriptions, OTC, and supplements currently used",
        "distractors": [
            "Only antibiotics",
            "Only vitamins",
            "Nothing if patient is young"
        ],
        "explanation": "Complete list prevents interactions.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-intake",
        "stem": "Allergy documentation must include:",
        "correct": "Substance and reaction type",
        "distractors": [
            "Only drug allergies",
            "\"NKDA\" without asking",
            "Guess if patient unsure"
        ],
        "explanation": "NKDA only after verified history.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-intake",
        "stem": "HIPAA Notice of Privacy Practices:",
        "correct": "Should be offered per facility policy at intake",
        "distractors": [
            "Is optional forever",
            "Allows free disclosure to media",
            "Replaces consent for surgery"
        ],
        "explanation": "Patients have privacy rights.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-intake",
        "stem": "Review of systems (ROS) is:",
        "correct": "Subjective symptoms by body system",
        "distractors": [
            "Physical exam findings only",
            "Lab data only",
            "Billing code only"
        ],
        "explanation": "MA may assist with structured questionnaires.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-intake",
        "stem": "Past medical history includes:",
        "correct": "Diagnoses, surgeries, hospitalizations",
        "distractors": [
            "Favorite hobbies only",
            "Staff names",
            "Parking spot"
        ],
        "explanation": "PMH informs risk and care planning.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-intake",
        "stem": "Social history may document:",
        "correct": "Tobacco, alcohol, occupation, and support",
        "distractors": [
            "Blood type only",
            "Shoe size",
            "IV gauge"
        ],
        "explanation": "Social determinants affect health.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-intake",
        "stem": "Informed consent for procedures requires:",
        "correct": "Disclosure, understanding, and voluntary agreement",
        "distractors": [
            "Only signature without discussion",
            "Guardian for all adults",
            "Verbal only always"
        ],
        "explanation": "Document teaching and questions answered.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "skill-intake",
        "stem": "Vital signs at intake help:",
        "correct": "Establish baseline and triage acuity",
        "distractors": [
            "Replace physician exam entirely",
            "Are optional always",
            "Only for inpatients"
        ],
        "explanation": "Abnormal vitals may need escalation.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-intake",
        "stem": "Insurance card copying at registration:",
        "correct": "Verifies coverage and demographic billing data",
        "distractors": [
            "Is illegal always",
            "Replaces ID verification",
            "Not needed in cash pay"
        ],
        "explanation": "Eligibility affects authorization.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "skill-intake",
        "stem": "Closing intake interview should:",
        "correct": "Confirm patient questions answered and next steps clear",
        "distractors": [
            "End without summary",
            "Share other patients' data",
            "Skip contact info update"
        ],
        "explanation": "Clear instructions improve satisfaction and safety.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    }
]
