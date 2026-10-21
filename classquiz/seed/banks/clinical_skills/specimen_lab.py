# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-specimen-lab)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-specimen-lab-001
    fact(
        "skill-specimen-lab",
        "Which vacuum tube is routinely used for a complete blood count with automated hematology analyzers?",
        "Lavender top with EDTA anticoagulant",
        [
            "Light blue top with sodium citrate",
            "Red top without additive for serum",
            "Gray top with sodium fluoride intended for coagulation",
        ],
        "EDTA in lavender tubes prevents clotting while preserving cell morphology for CBC testing. Citrate and plain red tubes serve coagulation and chemistry pathways instead.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-002
    fact(
        "skill-specimen-lab",
        "Which tube color is associated with sodium citrate anticoagulant for prothrombin time testing?",
        "Light blue top",
        [
            "Green top with lithium heparin",
            "Gold speckled serum separator",
            "Lavender top with EDTA",
        ],
        "Citrate binds calcium to yield plasma for coagulation assays with a controlled blood-to-additive ratio. EDTA and heparin tubes interfere with clot-based PT methods.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-003
    fact(
        "skill-specimen-lab",
        "Which container is commonly used when serum is needed after clotting for many chemistry tests?",
        "Red top tube without anticoagulant",
        [
            "Lavender EDTA tube",
            "Light blue citrate tube filled below the line",
            "Sterile urine cup without preservative for blood",
        ],
        "Red-top tubes allow blood to clot so serum can be separated. Anticoagulated tubes keep whole blood fluid and are chosen for other test menus.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-004
    fact(
        "skill-specimen-lab",
        "What is the primary purpose of a gold speckled serum separator tube (SST)?",
        "Collect serum and separate cells from serum with a gel barrier after clotting and centrifugation",
        [
            "Anticoagulate whole blood for platelet counts",
            "Preserve glucose without clotting for CBC",
            "Draw blood cultures before all other tubes",
        ],
        "SST tubes clot like red tops, then gel aids serum separation in the lab. They are not substitutes for EDTA hematology tubes or citrate coagulation tubes.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-005
    fact(
        "skill-specimen-lab",
        "Gray-top tubes with sodium fluoride are often selected for which type of testing?",
        "Glucose measurement when glycolysis must be slowed",
        [
            "Routine prothrombin time",
            "Type and crossmatch in the blood bank",
            "Routine throat culture plating",
        ],
        "Fluoride inhibits enolase to reduce in vitro glucose consumption in whole blood samples. Coagulation and immunohematology use different additives and tube colors.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-006
    fact(
        "skill-specimen-lab",
        "Green-top tubes with lithium heparin are often used for what kind of laboratory testing?",
        "Plasma chemistry when rapid anticoagulation is needed",
        [
            "EDTA-dependent complete blood count",
            "Citrate-dependent INR on undiluted plasma",
            "Stool ova and parasite wet mount",
        ],
        "Heparin anticoagulates plasma for selected chemistry panels. CBC and PT require EDTA and citrate respectively under CLSI venous blood collection guidance.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-007
    fact(
        "skill-specimen-lab",
        "When should a blood collection tube be labeled with patient identifiers?",
        "At the bedside or chair immediately after collection while the patient is present",
        [
            "After tubes sit in the break room for an hour",
            "In the lab without comparing to the requisition",
            "Before the draw while tubes are still empty on the cart",
        ],
        "CLSI GP41 emphasizes labeling in the presence of the patient to reduce misidentification. Delayed or remote labeling raises wrong-patient result risk.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-008
    fact(
        "skill-specimen-lab",
        "What fasting instruction is commonly given before a fasting lipid panel unless the order states otherwise?",
        "No food for about 9 to 12 hours; water is usually permitted",
        [
            "High-fat breakfast immediately before the draw",
            "Alcohol encouraged the night before testing",
            "No fluids including water for 24 hours",
        ],
        "Fasting lipids compare triglycerides and certain fractions without recent meal interference. Plain water during the fast is commonly allowed per lab and order instructions.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-009
    fact(
        "skill-specimen-lab",
        "For a routine clean-catch midstream urine, what patient step reduces contamination from skin flora?",
        "Clean the urinary opening, begin voiding, then collect midstream into the sterile cup",
        [
            "Collect the first few drops without cleaning",
            "Void directly into the toilet and scoop water afterward",
            "Rinse the cup with soap and leave it wet inside",
        ],
        "Discarding the initial stream clears urethral contaminants before the midstream portion enters the cup. Toilet water and soap residue can invalidate culture results.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-010
    fact(
        "skill-specimen-lab",
        "Why should specimens reach the laboratory within stability times listed on the test directory?",
        "Analytes and cells degrade when storage exceeds allowed temperature and time limits",
        [
            "Delays make every result falsely normal",
            "Transport is optional for chemistry panels",
            "Room temperature storage is correct for every tube type",
        ],
        "CLSI guidance ties preanalytic quality to time and temperature limits. Exceeding them can hemolyze, clot, or consume glucose before analysis.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-011
    fact(
        "skill-specimen-lab",
        "Before venipuncture or capillary collection, which infection prevention step is expected?",
        "Perform hand hygiene and follow Standard Precautions for blood exposure",
        [
            "Reuse gloves between patients without cleaning hands",
            "Palpate veins with unwashed hands after a prior blood spill",
            "Place used needles on the counter for later",
        ],
        "CDC Standard Precautions apply to all blood collection activities. Hand hygiene and appropriate barriers reduce pathogen transmission between patients and staff.",
        [S.CDC_STANDARD_PRECAUTIONS, S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-012
    fact(
        "skill-specimen-lab",
        "Pink-top EDTA tubes in many blood bank workflows are used for which purpose?",
        "Immunohematology testing such as type and screen when required by SOP",
        [
            "Therapeutic drug monitoring of lithium",
            "Sputum acid-fast bacillus staining",
            "Fasting glucose on plasma separator gel",
        ],
        "Pink tops still use EDTA anticoagulant but follow blood bank pathways distinct from routine lavender CBC tubes. Other distractors describe unrelated specimen types.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-013
    fact(
        "skill-specimen-lab",
        "Which container is appropriate for a urine culture when the order requests bacterial identification?",
        "Sterile urine cup with tight lid collected per clean-catch instructions",
        [
            "Open bedpan without lid for convenience",
            "Nonsterile hat left at the bedside overnight",
            "Red-top blood tube filled with voided urine",
        ],
        "Culture work requires sterile collection and prompt handling to limit contamination. Nonsterile containers and blood tubes are unacceptable for urine microbiology.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-014
    fact(
        "skill-specimen-lab",
        "Why must light blue citrate tubes be filled to the marked volume line?",
        "The fixed blood-to-citrate ratio must be maintained for valid coagulation results",
        [
            "Underfilling concentrates EDTA and raises platelet counts",
            "Overfilling adds extra heparin from the needle hub",
            "Volume does not affect prothrombin time",
        ],
        "Citrate anticoagulation depends on a precise ratio of blood to additive. Short draws dilute citrate excessively and can falsely prolong clotting times.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-015
    fact(
        "skill-specimen-lab",
        "After filling an EDTA tube, what mixing step helps prevent microclots in hematology samples?",
        "Gently invert the tube the number of times specified by the manufacturer, often about 8 to 10 inversions",
        [
            "Vigorously shake the tube for one minute",
            "Freeze the tube immediately on dry ice",
            "Centrifuge before labeling at the bedside",
        ],
        "Gentle inversion distributes anticoagulant without hemolysis. Shaking or premature centrifugation can destroy cells needed for a valid CBC.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-016
    fact(
        "skill-specimen-lab",
        "A blood tube arrives in the laboratory without a patient name or identification number. What is the usual disposition?",
        "Reject the specimen and recollect following identification policy",
        [
            "Run tests and guess the patient from tube color",
            "Assign the next chart number in sequence",
            "Pool it with another patient's sample to save volume",
        ],
        "Unlabeled tubes cannot be linked safely to a person. CLSI preanalytic standards require rejection and repeat collection with proper bedside labeling.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-specimen-lab-017
    fact(
        "skill-specimen-lab",
        "When laboratory policy flags a grossly hemolyzed potassium sample, what may be required clinically?",
        "Recollection because hemolysis releases intracellular potassium and skews results",
        [
            "Report the value without comment every time",
            "Dilute the sample secretly to hide hemolysis",
            "Add anticoagulant to fix the color",
        ],
        "Hemolysis elevates potassium from lysed red cells. Reporting without note or tampering with the specimen compromises clinical decisions described in collection standards.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-018
    fact(
        "skill-specimen-lab",
        "Chain-of-custody documentation for forensic specimens requires which practice?",
        "Seal the container, record each transfer with signature, date, and time",
        [
            "Leave cups open on the counter for ventilation",
            "Let multiple staff sign at once without dates",
            "Transport in a personal backpack without log",
        ],
        "Forensic and legal specimens need tamper-evident seals and a continuous log of handlers. Gaps in the chain can invalidate evidence in court or workplace testing.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-specimen-lab-019
    fact(
        "skill-specimen-lab",
        "A 24-hour urine collection often includes what patient instruction about the preservative in the container?",
        "Keep the collection jug refrigerated or on ice as directed and void completely into the container",
        [
            "Discard the first morning void without recording time",
            "Add tap water each hour to dilute the sample",
            "Store the jug in direct sunlight to prevent growth",
        ],
        "Timed urine collections depend on complete voids and proper preservative temperature to stabilize analytes. Missing voids or diluting the pool invalidates the test.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-020
    fact(
        "skill-specimen-lab",
        "For a sputum culture, which sample type should the patient provide?",
        "Deep cough expectorate from the lower airways, not saliva from the mouth",
        [
            "Saliva pooled after chewing gum",
            "Nasal mucus wiped onto a dry tissue",
            "Tap water gargle poured into the cup",
        ],
        "Saliva and upper airway secretions contaminate cultures meant for lower respiratory pathogens. Coaching a deep cough improves specimen quality.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-021
    fact(
        "skill-specimen-lab",
        "Before drawing blood cultures, what skin preparation step reduces contamination?",
        "Use the antiseptic sequence in the facility protocol and allow adequate drying time",
        [
            "Wipe once with plain water and draw immediately",
            "Palpate vigorously after antisepsis without re-cleaning",
            "Reuse the culture needle between two patients",
        ],
        "Proper antisepsis and dry time lower skin flora in the bottle. Reusing needles between patients violates Standard Precautions and CDC blood collection safety expectations.",
        [S.CLSI_GP41, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-specimen-lab-022
    fact(
        "skill-specimen-lab",
        "A chemistry requisition states serum should be refrigerated if not centrifuged within one hour. What does that instruction address?",
        "Slow glycolysis and degradation before the lab separates and tests the sample",
        [
            "Increase hemolysis for better color",
            "Eliminate the need for patient identification",
            "Replace the requirement for calibrated pipettes",
        ],
        "Preanalytic stability charts define temperature holds until processing. Ignoring them can change glucose and enzyme results even when collection technique was correct.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-023
    fact(
        "skill-specimen-lab",
        "When should an outpatient serum sample be centrifuged according to many chemistry protocols?",
        "After clotting completes and within the time window defined by the laboratory manual",
        [
            "Before the needle leaves the vein during venipuncture",
            "One week after collection at room temperature",
            "Without balancing paired tubes in the rotor",
        ],
        "Centrifugation separates serum or plasma once clotting finishes, but delay or imbalance can hemolyze or break equipment. On-needle centrifugation is not performed in routine phlebotomy.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-024
    fact(
        "skill-specimen-lab",
        "Which patient preparation statement is appropriate before a fasting glucose draw when water is allowed?",
        "Consume no caloric foods or beverages except plain water for the ordered fasting interval",
        [
            "Drink sweetened coffee with cream during the fast",
            "Chew sugar gum throughout the morning",
            "Eat a large meal two hours before the draw when fasting is ordered",
        ],
        "Caloric intake raises blood glucose and defeats fasting orders. Plain water without calories is commonly permitted unless the provider gives different instructions.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-specimen-lab-025
    fact(
        "skill-specimen-lab",
        "Fecal occult blood test kits often instruct patients to limit certain foods or medications. Why is that teaching important?",
        "Some diets and drugs cause false-positive or false-negative chemical reactions on the card",
        [
            "Food choices change the patient's blood type on the card",
            "Red meat turns the card blue for every person",
            "Medications have no effect on guaiac-based testing",
        ],
        "Peroxidase-like activity in foods and some supplements can mimic blood on guaiac tests. Following kit directions improves result interpretation.",
        [S.CLSI_GP41, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-specimen-lab-026
    fact(
        "skill-specimen-lab",
        "A first morning urine sample is often requested for pregnancy testing because it tends to have what property?",
        "Higher concentrated human chorionic gonadotropin after overnight fluid restriction",
        [
            "Lower specific gravity than random afternoon urine every time",
            "No need for patient identification on the cup",
            "Guaranteed sterility without clean-catch technique",
        ],
        "Concentrated early morning urine can detect lower hormone levels on some assays. It still requires proper labeling and collection technique.",
        [S.NHA_CCMA, S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-027
    fact(
        "skill-specimen-lab",
        "When collecting stool for ova and parasite examination, which practice is incorrect?",
        "Submitting a specimen mixed with toilet bowl water or urine",
        [
            "Transferring a walnut-sized sample into the container with the provided spoon",
            "Labeling the container with two identifiers at collection",
            "Delivering the sample within the time frame on the requisition",
        ],
        "Toilet water and urine dilute or kill parasites and confound microscopy. Proper amount, labeling, and timely delivery support valid ova and parasite results.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-028
    fact(
        "skill-specimen-lab",
        "A light blue tube arrives underfilled for coagulation testing. What is the typical laboratory response?",
        "Reject as quantity not sufficient and recollect to the fill line",
        [
            "Dilute with saline to the line",
            "Run PT anyway without comment",
            "Add EDTA from a lavender tube to compensate",
        ],
        "Short citrate tubes break the required ratio and invalidate clotting assays. Adding wrong anticoagulants further distorts results.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-029
    fact(
        "skill-specimen-lab",
        "During transport to a reference laboratory, why might an ice pack or insulated cooler be used?",
        "Maintain specimens within required temperature ranges on the stability chart",
        [
            "Freeze all tubes solid for convenience",
            "Replace chain-of-custody seals on forensic cups",
            "Allow staff to store lunches beside patient samples",
        ],
        "Temperature-controlled transport protects unstable analytes during transit. Freezing many serum samples or mixing food with patient specimens violates safety and quality rules.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-030
    fact(
        "skill-specimen-lab",
        "A urine culture cannot be plated immediately. What handling step is commonly required within about one hour?",
        "Refrigerate the sealed specimen unless the lab specifies room temperature hold",
        [
            "Leave the cup open at the nursing station",
            "Heat the sample to 100 degrees Fahrenheit",
            "Add bleach to prevent odor",
        ],
        "Brief refrigeration slows bacterial overgrowth from contamination while awaiting processing. Open containers and disinfectants destroy organisms needed for culture.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-031
    fact(
        "skill-specimen-lab",
        "You notice a colleague about to label tubes before entering the patient's room. What concern should you raise?",
        "Pre-labeling empty tubes increases risk of wrong-patient identification if the draw is delayed or interrupted",
        [
            "Labels should include the room number for speed",
            "Tubes should be labeled in the lab after centrifugation",
            "Patient presence is irrelevant to identification",
        ],
        "CLSI GP41 ties labeling to the phlebotomy encounter with the patient present. Pre-labeled tubes may be applied to the wrong person if the cart order changes.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "advanced",
    ),
    # skill-specimen-lab-032
    fact(
        "skill-specimen-lab",
        "A workplace drug screen requires chain of custody. The donor refuses to initial the seal after providing the specimen. What is the appropriate action?",
        "Document the refusal and follow the testing vendor protocol, which may void the collection",
        [
            "Seal the cup without documentation to save time",
            "Ask another patient to sign instead",
            "Discard the specimen without notifying the supervisor",
        ],
        "Forensic and employment testing protocols define how refusals are recorded. Missing signatures break the legal chain even if the urine volume is adequate.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-033
    fact(
        "skill-specimen-lab",
        "For adult blood cultures, many protocols recommend drawing how much volume into each bottle when using standard aerobic and anaerobic pairs?",
        "Approximately 8 to 10 mL per bottle unless pediatric bottles are ordered",
        [
            "1 mL per bottle for every adult",
            "Fill bottles halfway with saline diluent",
            "Draw cultures after all chemistry tubes without antisepsis",
        ],
        "Adequate blood volume improves pathogen recovery in culture systems. Tiny volumes and saline dilution reduce sensitivity; skin antisepsis remains mandatory.",
        [S.CLSI_GP41, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-specimen-lab-034
    fact(
        "skill-specimen-lab",
        "A chemistry requisition notes lipemic serum may be rejected for certain tests. What collection factor can contribute to lipemia?",
        "Recent high-fat meal before a nonfasting draw",
        [
            "Proper fasting for 10 hours with water allowed",
            "Gentle inversion of EDTA tubes",
            "Labeling at the bedside with two identifiers",
        ],
        "Triglyceride-rich lipoproteins rise after fatty meals and can interfere with some assays or trigger recollection. Fasting and gentle technique reduce other preanalytic errors.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-035
    fact(
        "skill-specimen-lab",
        "A cortisol level ordered for 8 AM requires what special collection consideration?",
        "Document the actual draw time because diurnal variation affects interpretation",
        [
            "Draw at midnight without noting time",
            "Pool two days of random urines into one tube",
            "Collect after vigorous exercise without recording activity",
        ],
        "Cortisol follows a circadian pattern, so the clock time is part of the result. Missing time documentation makes the value hard for clinicians to interpret.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-036
    fact(
        "skill-specimen-lab",
        "Gray-top fluoride tubes for glucose should be processed how soon in many outpatient settings?",
        "Mixed gently after fill and transported to the lab within stability limits on the test chart",
        [
            "Left unmixed at room temperature for 24 hours",
            "Centrifuged before clotting like a red top",
            "Drawn into a citrate tube instead for convenience",
        ],
        "Fluoride slows glycolysis but does not remove the need for timely testing. Wrong tube type or delayed mixing allows glucose consumption in transit.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-037
    fact(
        "skill-specimen-lab",
        "A CLIA-waived point-of-care glucose meter requires quality control. What must staff do on the schedule in the procedure manual?",
        "Run control solutions at required intervals and document results before patient testing when indicated",
        [
            "Use expired control fluid to save supplies",
            "Document controls after patient complaints",
            "Disable lockout features to speed testing",
        ],
        "Waived testing still demands documented QC and operator training under CLIA rules. Expired controls and disabled safeguards undermine result reliability.",
        [S.FDA_CLIA_WAIVED, S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-038
    fact(
        "skill-specimen-lab",
        "Cold agglutinin testing may require what special handling after collection?",
        "Keep the sample warm during transport per laboratory instructions to prevent artifactual agglutination",
        [
            "Freeze the EDTA tube immediately",
            "Shake the tube vigorously for five minutes",
            "Expose the sample to direct ice immersion without guidance",
        ],
        "Cold agglutinins can clump red cells when chilled, falsely lowering counts. Laboratories issue temperature-specific handling that differs from routine refrigerated transport.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-039
    fact(
        "skill-specimen-lab",
        "Plasma ammonia samples often require placement on ice immediately after draw. What problem does rapid cooling address?",
        "Continued metabolism and ammonia generation in red cells at room temperature",
        [
            "Excessive citrate anticoagulation in lavender tubes",
            "Loss of fluoride from gray tops",
            "Clot formation in sodium heparin plasma",
        ],
        "Ammonia rises quickly in improperly handled specimens, leading to falsely high results. Ice transport follows specialized stability instructions outside routine CBC handling.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-040
    fact(
        "skill-specimen-lab",
        "A lavender EDTA tube arrives with a visible clot. What is the expected laboratory action for hematology orders?",
        "Reject and recollect because clots invalidate cell counts and morphology",
        [
            "Vortex the clot and run the CBC",
            "Switch to serum chemistry without notifying anyone",
            "Add liquid citrate to dissolve the clot",
        ],
        "Clotted EDTA specimens cannot produce reliable CBC results on analyzers expecting anticoagulated whole blood. Recollection with proper mixing is required.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-041
    fact(
        "skill-specimen-lab",
        "Urine from an indwelling catheter should be collected for culture from where?",
        "A fresh sample from the catheter sampling port after disinfecting the port, not the drainage bag",
        [
            "Stagnant urine pooled in the drainage bag from yesterday",
            "The floor drain after accidental spill",
            "Saline flush pushed backward into the bag without port disinfection",
        ],
        "Bag urine harbors colonized flora unrelated to infection. Port disinfection and a new aspirate reflect CLSI-aligned infection control for catheter specimens.",
        [S.CLSI_GP41, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-specimen-lab-042
    fact(
        "skill-specimen-lab",
        "You receive tubes where the requisition lists two patients but every label shows the same name. What is the correct response?",
        "Stop processing, quarantine the specimens, and resolve identification with the draw team before testing",
        [
            "Run all tests under the first name on the list",
            "Split volumes between the two charts to save blood",
            "Remove labels and guess based on tube color",
        ],
        "Duplicate mislabeling is a serious patient safety event requiring hold and investigation. Testing or splitting specimens perpetuates wrong-patient results.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "advanced",
    ),
]
