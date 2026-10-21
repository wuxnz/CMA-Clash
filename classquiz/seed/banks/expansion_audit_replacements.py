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
