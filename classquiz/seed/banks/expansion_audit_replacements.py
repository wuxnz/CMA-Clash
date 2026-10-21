# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Unique replacement items added after audit deduplication of growth bank."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_RAW: tuple[
    tuple[str, str, str, tuple[str, str, str], str, tuple[str, ...]],
    ...,
] = (
    # CCMA (19)
    (
        "ccma-clinical-care",
        "When applying a blood pressure cuff, the bladder should encircle at least what percent of the arm?",
        "80% of the arm circumference",
        ("40% of the arm", "50% of the wrist only", "100% overlap is required"),
        "An undersized cuff reads falsely high and an oversized cuff reads falsely low. Eighty percent arm coverage is the usual teaching standard for adults.",
        (S.NHA_CCMA, S.CDC_HBP),
    ),
    (
        "ccma-transmission",
        "Alcohol-based hand rub is appropriate when hands are not visibly soiled and:",
        "You follow product contact time on the label",
        ("You skip rub if gloves will be worn", "Waterless rub replaces cleaning after body fluid contact", "Rub is never used in outpatient care"),
        "CDC allows ABHR for routine decontamination when hands are not soiled. Visible soil or certain exposures still require soap and water.",
        (S.CDC_HAND_HYGIENE, S.NHA_CCMA),
    ),
    (
        "ccma-clinical-care",
        "A medication error near-miss should be:",
        "Documented and reported per facility policy for system improvement",
        ("Ignored if the patient was unharmed", "Only discussed verbally without a record", "Hidden to protect staff"),
        "Reporting near-misses helps fix processes before patient harm occurs. Policies define nonpunitive reporting channels.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
    (
        "ccma-law-ethics",
        "A minor requests STI testing where state law allows confidential care. The medical assistant should:",
        "Follow state minor-consent rules and clinic privacy policy",
        ("Tell the parent every detail without checking law", "Refuse all testing for minors", "Post results on social media"),
        "Confidential adolescent services depend on state statute and scope. HIPAA still requires safeguarding PHI.",
        (S.HHS_HIPAA_PRIVACY, S.NHA_CCMA),
    ),
    (
        "ccma-communication",
        "Teach-back is used to:",
        "Confirm the patient understands instructions in their own words",
        ("Speed up visits by skipping questions", "Test reading level of the clinician", "Replace interpreter services"),
        "Teach-back checks understanding without shaming the patient. It is not a literacy test of the staff member.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-anatomy",
        "The left ventricle pumps blood into the:",
        "Aorta",
        ("Pulmonary artery", "Superior vena cava", "Right atrium"),
        "The left ventricle supplies the systemic circulation through the aorta. The pulmonary artery carries blood from the right ventricle to the lungs.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-foundational",
        "The prefix \"brady-\" means:",
        "Slow",
        ("Fast", "Pain", "Above normal"),
        "Brady- indicates a slower rate, such as bradycardia. Tachy- indicates a faster rate.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-coordination",
        "Prior authorization for a procedure typically requires:",
        "Clinical documentation sent to the payer before service",
        ("Only a verbal promise from the patient", "Posting the order on a public website", "Skipping insurance contact"),
        "Payers often need diagnosis and procedure codes with supporting notes. Starting without approval can lead to denied claims.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-clinical-care",
        "Peak expiratory flow is measured with the patient:",
        "Standing or sitting upright with maximal effort after full inspiration",
        ("Lying flat without instruction", "Holding breath for one minute first", "After vigorous exercise only"),
        "PEF requires a forceful exhale into the meter. Poor effort or poor seal gives falsely low readings.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-transmission",
        "Sharps containers should be replaced when they are:",
        "Three-quarters full per OSHA guidance",
        ("Completely overflowing", "Empty only at year end", "Filled with nonsharp trash to save space"),
        "Overfilling increases needlestick risk during disposal. OSHA addresses fill level and puncture-resistant containers.",
        (S.OSHA_BBP, S.NHA_CCMA),
    ),
    (
        "ccma-clinical-care",
        "Look-alike sound-alike (LASA) medications require:",
        "Tall-man lettering and extra verification steps",
        ("Storing all vials unlabeled", "Using only color of cap as sole identifier", "Skipping the second identifier check"),
        "LASA pairs such as hydroxyzine and hydralazine need deliberate verification. Tall-man lettering highlights spelling differences.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
    (
        "ccma-law-ethics",
        "Mandatory reporting of suspected abuse generally:",
        "Requires reporting to designated authorities per state law",
        ("Is optional if the patient is wealthy", "Can be delayed until next holiday", "Applies only in hospitals never clinics"),
        "Healthcare workers must know local reporting statutes and agency contacts. Failure to report can carry legal penalties.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-communication",
        "When using an interpreter, the medical assistant should:",
        "Allow the patient to speak freely and face the patient while the interpreter works",
        ("Ask the child to interpret confidential history", "Speak only to the interpreter and ignore the patient", "Use a family member for sensitive abuse disclosure"),
        "Qualified interpreters protect accuracy and privacy. Speaking to the patient maintains rapport.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-anatomy",
        "Insulin is produced by pancreatic:",
        "Beta cells in the islets of Langerhans",
        ("Alpha cells only", "Acinar cells that secrete digestive enzymes", "Hepatocytes"),
        "Beta cells release insulin to lower blood glucose. Alpha cells release glucagon.",
        (S.NHA_CCMA, S.CDC_DIABETES),
    ),
    (
        "ccma-foundational",
        "Standard Precautions treat which body fluids as potentially infectious?",
        "All blood and body fluids except sweat unless visibly contaminated",
        ("Only fluids from patients with known HIV", "Only inpatient blood", "Saliva in every dental visit without exception"),
        "Standard Precautions apply to all patient encounters in healthcare. Risk is not limited to known diagnoses.",
        (S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA),
    ),
    (
        "ccma-coordination",
        "A referral is considered closed when:",
        "The consulting report is received and communicated to the ordering provider",
        ("The patient books a vacation", "The front desk changes the wallpaper", "No follow-up is documented"),
        "Closing the loop ensures results and recommendations reach the care team. Open loops risk missed diagnoses.",
        (S.NHA_CCMA,),
    ),
    (
        "ccma-clinical-care",
        "For adults, fever is often defined orally as a temperature above:",
        "100.4°F (38°C)",
        ("98.6°F in every adult always", "95°F", "104°F only at night"),
        "Individual baselines vary, but 100.4°F oral is a common fever threshold in adults. Site of measurement changes expected values.",
        (S.NHA_CCMA, S.MEDLINEPLUS_HAND_HYGIENE),
    ),
    (
        "ccma-transmission",
        "After removing gloves following patient care, the next hand hygiene step is:",
        "Perform hand hygiene because gloves may have microtears",
        ("Skip hygiene because gloves were worn", "Wipe gloves with alcohol and reuse", "Only wash if gloves tore visibly"),
        "Gloves reduce but do not eliminate contamination of hands. Hand hygiene follows glove removal per CDC.",
        (S.CDC_HAND_HYGIENE, S.NHA_CCMA),
    ),
    (
        "ccma-clinical-care",
        "High-alert medications such as insulin require:",
        "Independent double checks per policy when dispensing or administering",
        ("Single-person rush without label read", "Storage mixed with saline flushes unlabeled", "Dosing by memory without order"),
        "Insulin and other high-alert drugs have narrow therapeutic windows. Independent checks catch decimal errors.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
    # Clinical skills (29)
    (
        "skill-vitals",
        "When counting respirations, it helps to:",
        "Count without telling the patient you are counting breaths",
        ("Ask the patient to breathe rapidly", "Count only while the patient exercises", "Estimate without observing the chest"),
        "Awareness can alter breathing rate. Observe chest rise while appearing to take the pulse if needed.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-injection",
        "Before any injection, verify the:",
        "Six rights including patient, drug, dose, route, time, and documentation",
        ("Color of the patient's shoes", "Weather forecast", "Parking spot number"),
        "Six rights reduce wrong-patient and wrong-drug errors. The order and MAR must match the vial label.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
    (
        "skill-injection",
        "The Z-track method for intramuscular injection helps:",
        "Prevent medication leakage into subcutaneous tissue",
        ("Increase pain on purpose", "Inject into intravenous line", "Skip site rotation"),
        "Displacing tissue before injection traps depot medication in muscle. Leakage can irritate skin and reduce absorption.",
        (S.NHA_CCMA, S.CDC_INJECTION_SAFETY),
    ),
    (
        "skill-specimen-lab",
        "Order of draw for venipuncture with a winged set begins with:",
        "Blood culture bottles before sodium citrate when cultures are ordered",
        ("EDTA tube before cultures", "Serum separator before cultures", "Any tube in random order"),
        "CLSI GP41 places blood cultures first to limit contamination. Citrate, serum, heparin, EDTA, and glycolytic inhibitor follow the published sequence.",
        (S.CLSI_GP41, S.NHA_CPT),
    ),
    (
        "skill-specimen-lab",
        "A light-blue sodium citrate tube is used primarily for:",
        "Coagulation studies such as PT/INR",
        ("Chemistry panels only", "Blood bank crossmatch without anticoagulant", "Routine CBC without additive"),
        "Citrate binds calcium to prevent clotting for coagulation tests. Fill to the line because excess anticoagulant dilutes the sample.",
        (S.CLSI_GP41, S.NHA_CPT),
    ),
    (
        "skill-specimen-lab",
        "Gently inverting an EDTA tube after collection:",
        "Mixes anticoagulant without hemolyzing the sample",
        ("Shakes vigorously until foam forms", "Is never needed for purple tubes", "Replaces labeling requirements"),
        "Gentle mixing prevents microclots in CBC samples. Vigorous shaking can hemolyze cells and alter potassium.",
        (S.CLSI_GP41, S.NHA_CPT),
    ),
    (
        "skill-wound-care",
        "An increasing ring of erythema with purulent drainage suggests:",
        "Wound infection needing clinician evaluation",
        ("Normal healing in every case", "Improved perfusion always", "No documentation needed"),
        "Spreading redness and pus are infection warning signs. Timely assessment may require culture or antibiotics.",
        (S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA),
    ),
    (
        "skill-terminology",
        "The suffix \"-ectomy\" means:",
        "Surgical removal",
        ("Inflammation", "Enlargement only", "Slow heart rate"),
        "-ectomy denotes excision, such as appendectomy. -itis denotes inflammation.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-pharm-dosage",
        "High-alert medications in ambulatory care include:",
        "Insulin, anticoagulants, and concentrated electrolytes",
        ("Multivitamins only", "Saline flush without label", "Placebo tablets routinely"),
        "ISMP lists high-alert drugs with heightened harm if misused. Extra safeguards apply to insulin and anticoagulants.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
    (
        "skill-vitals",
        "Orthostatic hypotension is suggested when systolic pressure drops at least:",
        "20 mmHg or diastolic drops 10 mmHg within 3 minutes of standing",
        ("2 mmHg after standing", "No change after standing", "Only diastolic rise of 20 mmHg"),
        "A 20/10 drop after position change supports orthostatic hypotension. Symptoms such as dizziness may accompany the change.",
        (S.CDC_HBP, S.NHA_CCMA),
    ),
    (
        "skill-life-stages",
        "Infant CPR compression depth is about:",
        "One-third the anterior-posterior chest diameter",
        ("Two inches in every newborn regardless of size", "No compressions until age one", "Four inches always"),
        "AHA pediatric BLS uses one-third AP diameter for infants. Excessive depth can injure small chests.",
        (S.AHA_ADULT_BLS, S.NHA_CCMA),
    ),
    (
        "skill-emergency-aid",
        "For a conscious adult with severe bleeding, first apply:",
        "Direct pressure over the wound",
        ("A tourniquet before any pressure for every scrape", "Elevation without pressure", "Remove embedded objects immediately"),
        "Direct pressure controls most external bleeding. Tourniquets are reserved for life-threatening extremity bleeding when pressure fails.",
        (S.RED_CROSS_FIRST_AID,),
    ),
    (
        "skill-specimen-lab",
        "A gray-top fluoride tube is drawn when:",
        "Glycolysis must be inhibited for glucose testing",
        ("CBC is the only ordered test", "Coagulation is ordered", "Blood culture is the first priority"),
        "Fluoride/oxalate tubes preserve glucose for chemistry. They are drawn after EDTA in the standard CLSI order when required.",
        (S.CLSI_GP41, S.NHA_CPT),
    ),
    (
        "skill-injection",
        "Intramuscular deltoid injections use a needle length typically appropriate for:",
        "Adults with adequate muscle mass after site assessment",
        ("All infants without site check", "Intravenous bolus administration", "Subcutaneous insulin only"),
        "Deltoid IM requires sufficient muscle bulk; ventrogluteal or vastus lateralis may be chosen instead. Needle gauge and length follow policy.",
        (S.CDC_INJECTION_SAFETY, S.NHA_CCMA),
    ),
    (
        "skill-vitals",
        "Pulse oximetry readings can be falsely low with:",
        "Cold extremities or poor perfusion",
        ("Warm well-perfused fingers only", "Normal room air always", "Proper probe placement only"),
        "Vasoconstriction and motion artifact reduce signal quality. Warm the site or use an alternate probe location per protocol.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-wound-care",
        "Pressure injury prevention for bedbound patients includes:",
        "Scheduled repositioning and moisture management",
        ("Keeping one bony area loaded all day", "Skipping skin inspection", "Tight wrinkles under the body"),
        "Repositioning redistributes pressure. Moisture from incontinence increases maceration risk.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-terminology",
        "The prefix \"hypo-\" means:",
        "Below or deficient",
        ("Above normal", "Pain", "Resection"),
        "Hypo- indicates deficiency, such as hypoglycemia. Hyper- indicates excess.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-pharm-dosage",
        "Pediatric weight-based dosing requires:",
        "Current weight in kilograms and a double-check of calculations",
        ("Adult maximum dose for every child", "Guessing weight from shoe size", "Skipping unit conversion"),
        "Milligram-per-kilogram orders need accurate weight and math verification. A small decimal error can be toxic in children.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
    (
        "skill-life-stages",
        "Older adults are at higher fall risk because of:",
        "Polypharmacy, gait changes, and vision deficits combined",
        ("Improved balance in every case", "Lower medication use always", "Mandatory bed rest"),
        "Falls are multifactorial. Medication review and home safety reduce risk.",
        (S.NHA_CCMA, S.FDA_MEDICATION_SAFETY),
    ),
    (
        "skill-emergency-aid",
        "Anaphylaxis with throat tightness is treated with:",
        "Intramuscular epinephrine and activation of EMS",
        ("Oral antihistamine alone as sole therapy", "Observation at home without EMS", "Exercise to distract"),
        "Epinephrine is first-line for anaphylaxis. A second dose may be needed while awaiting EMS.",
        (S.RED_CROSS_FIRST_AID,),
    ),
    (
        "skill-specimen-lab",
        "Hemolysis from rough handling most often falsely elevates:",
        "Potassium and some enzymes on chemistry panels",
        ("Sodium only downward always", "INR on citrate tubes", "Glucose in fluoride tubes only downward"),
        "Ruptured red cells leak potassium into serum. Gentle mixing and prompt processing limit hemolysis.",
        (S.CLSI_GP41, S.NHA_CPT),
    ),
    (
        "skill-injection",
        "Subcutaneous heparin is commonly injected into the:",
        "Abdomen at least two inches from the umbilicus",
        ("Deltoid IM site", "Intravenous port", "Earlobe"),
        "Abdominal SC sites rotate to reduce bruising. Avoid umbilicus and surgical scars per order.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-vitals",
        "Manual blood pressure measurement records should include:",
        "Position, arm used, cuff size, and time if protocol requires",
        ("Only a smiley face icon", "Patient favorite color", "Unrelated insurance code"),
        "Context helps clinicians interpret trends. Wrong cuff size or arm position skews results.",
        (S.CDC_HBP, S.NHA_CCMA),
    ),
    (
        "skill-wound-care",
        "Thermal burn first aid with cool running water:",
        "Limits depth of burn when started promptly for minor burns",
        ("Should use butter coating", "Requires ice packed directly for 30 minutes", "Replaces EMS for major burns"),
        "Cool water removes heat from tissue. Major burns still need emergency care and airway assessment.",
        (S.RED_CROSS_FIRST_AID,),
    ),
    (
        "skill-terminology",
        "The suffix \"-itis\" means:",
        "Inflammation",
        ("Surgical removal", "Slow", "New opening"),
        "Dermatitis is inflamed skin. -otomy means cutting into.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-pharm-dosage",
        "A trailing zero in drug documentation (for example 1.0 mg) should be:",
        "Avoided because it can be misread as ten milligrams",
        ("Encouraged for all doses", "Used only for insulin without concern", "Required on every MAR"),
        "ISMP recommends no trailing zeros on whole numbers. Leading zeros before decimals (0.5 mg) clarify small doses.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
    (
        "skill-life-stages",
        "Neonatal jaundice monitoring focuses on:",
        "Bilirubin level and feeding adequacy",
        ("Adult blood pressure only", "Ignoring skin color", "Stopping all feeds without orders"),
        "Rising bilirubin can cause kernicterus if untreated. Phototherapy or exchange may be ordered based on level and age.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-emergency-aid",
        "Stroke recognition using FAST emphasizes:",
        "Face droop, arm weakness, speech difficulty, and time to call EMS",
        ("Foot pain only", "Allergic rash", "Normal speech delay"),
        "Time last known well guides eligibility for reperfusion therapy. EMS transport is preferred over private car when possible.",
        (S.RED_CROSS_FIRST_AID,),
    ),
    (
        "skill-specimen-lab",
        "Fasting glucose specimens typically require:",
        "No caloric intake for about 8 to 12 hours unless the lab specifies otherwise",
        ("Only one hour without food", "High-sugar meal immediately before draw", "Exercise sprint right before venipuncture"),
        "Nonfasting samples can elevate triglycerides and glucose. Confirm lab instructions with the patient.",
        (S.CLSI_GP41, S.NHA_CPT),
    ),
    # EKG (6)
    # Phlebotomy (13)













    (
        "ccma-admin",
        "Under CLIA, a waived laboratory test is one that:",
        "Is simple and has low risk of error as defined by FDA waiver criteria",
        ("Requires a pathologist on site for every sample", "Is exempt from any quality standards", "May be run without manufacturer instructions"),
        "Waived tests still need controlled procedures and personnel training. Complexity is not the same as no oversight.",
        (S.FDA_CLIA_WAIVED, S.NHA_CCMA),
    ),
    (
        "skill-intake",
        "Documenting vital signs in the EHR should include:",
        "Values, time, position, and any factors that affect accuracy",
        ("Only a check mark without numbers", "Another patient's data to save time", "Values from last year"),
        "Complete entries support clinical decisions and legal records. Missing context can mislead providers.",
        (S.NHA_CCMA,),
    ),
    (
        "skill-osha-bbp",
        "Engineering controls for bloodborne pathogen exposure include:",
        "Safety-engineered needles and sharps containers",
        ("Reusable unshielded needles without disposal", "Bending needles after use", "Sharing personal protective equipment"),
        "OSHA prioritizes engineering controls before work practice controls. Safer devices reduce needlesticks.",
        (S.OSHA_BBP,),
    ),
    (
        "skill-poct",
        "Before running a CLIA-waived glucose meter, staff should:",
        "Perform quality control checks per manufacturer and facility policy",
        ("Skip controls if busy", "Use expired strips without note", "Share lancets between patients"),
        "QC verifies meter accuracy. Infection control requires single-use lancets and hand hygiene.",
        (S.FDA_CLIA_WAIVED, S.CDC_DIABETES),
    ),




    (
        "ccma-hipaa",
        "Minimum necessary under HIPAA means disclosing:",
        "Only the PHI needed for the current task",
        ("Entire medical record to any caller", "Passwords in email", "Social security numbers on a whiteboard"),
        "Staff limit access to what each role requires. Overdisclosure violates privacy even without malice.",
        (S.HHS_HIPAA_PRIVACY, S.NHA_CCMA),
    ),
    (
        "skill-med-safety",
        "Before crushing a medication not labeled as crushable, the assistant should:",
        "Check with the pharmacist or provider because some formulations are unsafe to crush",
        ("Crush all tablets to speed absorption", "Mix crushed drugs in unlabeled cups for later", "Crush enteric-coated tablets routinely"),
        "Extended-release and enteric coatings can cause overdose or irritation if crushed. Policy may require alternate forms.",
        (S.FDA_MEDICATION_SAFETY, S.NHA_CCMA),
    ),
)

FACTS: list[dict] = [
    fact(topic, stem, correct, list(distractors), explanation, list(refs))
    for topic, stem, correct, distractors, explanation, refs in _RAW
]
