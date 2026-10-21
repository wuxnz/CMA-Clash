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
        "What is the first priority before collecting any laboratory specimen?",
        "Match two patient identifiers to the order before collecting",
        [
            "Label tubes at the centrifuge bench after leaving the bedside area",
            "Select the largest visible vein before opening the paper requisition",
            "Use the stated name alone without comparing armband and chart identifiers",
        ],
        "Wrong-patient specimens cause harmful treatment decisions. Labels and orders must match the person present before skin is broken.",
        [S.CLSI_GP41, S.NHA_CPT, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-002
    fact(
        "skill-specimen-lab",
        "Which tube additive is used for most chemistry and serology tests in a gold-top serum separator tube?",
        "Clot activator and gel separator without anticoagulant for serum",
        [
            "EDTA anticoagulant for whole-blood chemistry and serology panels",
            "Sodium citrate anticoagulant for routine chemistry and serology panels",
            "Lithium heparin anticoagulant for routine chemistry and serology panels",
        ],
        "SST tubes yield serum after clotting for many chemistry assays. EDTA, citrate, and heparin tubes serve hematology and coagulation, not routine chemistry.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-003
    fact(
        "skill-specimen-lab",
        "Which tube is typically drawn for a complete blood count with automated differential?",
        "Lavender-top tube with EDTA anticoagulant",
        [
            "Light blue-top tube with sodium citrate for platelet count",
            "Red-top serum tube without additive for hematocrit and WBC",
            "Gray-top fluoride tube with anticoagulant for white cell count",
        ],
        "EDTA preserves cell morphology for hematology analyzers. Citrate is for coagulation, and fluoride tubes target glucose preservation.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    # skill-specimen-lab-004
    fact(
        "skill-specimen-lab",
        "Which tube is required for most coagulation tests such as prothrombin time?",
        "Light blue-top tube filled to exact volume with sodium citrate additive",
        [
            "Green-top heparin tube filled halfway for PT and INR coagulation testing",
            "Gold serum separator tube clotted ten minutes on the counter before fill",
            "Lavender EDTA tube inverted three times for coagulation studies and PT",
        ],
        "Citrate binds calcium to prevent clotting before the lab adds reagents. Incorrect fill ratio invalidates coagulation results.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-005
    fact(
        "skill-specimen-lab",
        "Why must blood culture bottles be drawn before other tubes in many order-of-draw schemes?",
        "To reduce contamination of cultures by additives from earlier tubes",
        [
            "To let chemistry additives sterilize culture media before inoculation",
            "Because culture bottles require the smallest draw volume in the sequence",
            "Because lavender additive must contact residual alcohol on the skin",
        ],
        "Sterile culture technique is vulnerable to skin flora and carryover additives. Culture priority protects the most contamination-sensitive specimen.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-006
    fact(
        "skill-specimen-lab",
        "How many times should additive tubes be gently inverted after collection?",
        "Five to ten gentle inversions of the tube after the draw",
        [
            "Vigorous shaking for thirty seconds to mix cells and clot",
            "No inversion because gravity distributes the additive within the hour",
            "One inversion because excess mixing lyses all red cells",
        ],
        "Gentle inversion distributes anticoagulant without hemolyzing cells. Shaking can destroy samples and ruin analyte integrity.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-007
    fact(
        "skill-specimen-lab",
        "What is hemolysis in a blood specimen and why does it matter?",
        "Red cell breakdown releasing potassium and intracellular contents into plasma",
        [
            "Clot formation in an EDTA tube intended for hematology cell counts on the analyzer",
            "Bacterial overgrowth in a culture bottle during prolonged incubator storage time",
            "Label smearing on the tube making the patient name hard to read at the laboratory bench",
        ],
        "Hemolysis falsely elevates potassium and other intracellular analytes. Clots in EDTA and label issues are separate preanalytic problems.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-008
    fact(
        "skill-specimen-lab",
        "Which tourniquet practice reduces erroneous potassium and hemolysis risk?",
        "Limit tourniquet time to about one minute and release if draw is delayed",
        [
            "Leave the tourniquet tight for five minutes to distend every accessible vein",
            "Have the patient pump the fist vigorously for two minutes before needle insertion",
            "Apply the tourniquet after the needle is already seated in the vein lumen",
        ],
        "Prolonged venous stasis concentrates analytes and increases hemolysis risk. Fist pumping also raises potassium artifactually.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-009
    fact(
        "skill-specimen-lab",
        "At what angle should a needle enter the vein for routine venipuncture?",
        "About 15 to 30 degrees with bevel up in standard technique",
        [
            "About 90 degrees perpendicular through muscle to reach deep basilic veins",
            "Parallel to the skin surface sliding along the epidermis without depth",
            "About 45 degrees into the artery beside the intended venipuncture site",
        ],
        "Shallow angles reduce perforation of the opposite vein wall. Deep perpendicular angles and arterial sticks are not routine venipuncture goals.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    # skill-specimen-lab-010
    fact(
        "skill-specimen-lab",
        "When should tubes be labeled relative to the draw?",
        "At the bedside right after collection while the patient is still present",
        [
            "At the central laboratory bench after pooling tubes from several patients",
            "The next morning when batch labels print from the billing system queue",
            "After centrifugation when the patient has already left the collection room",
        ],
        "Bedside labeling ties the tube to the person who gave the sample. Batch labeling away from the patient raises wrong-specimen risk.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-011
    fact(
        "skill-specimen-lab",
        "What information must appear on a primary specimen label in most laboratories?",
        "Patient name, identifier, collection date and time, and collector when required",
        [
            "Nursing unit room color code without patient name or medical record number on the tube",
            "Ordering provider home address to route questions about pending laboratory results",
            "Insurance group number in place of medical record number and collection date-time",
        ],
        "Accurate identifiers let the lab match results to the correct chart. Room colors and billing numbers do not uniquely identify the patient.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-012
    fact(
        "skill-specimen-lab",
        "How should a timed glucose tolerance blood sample be handled?",
        "Drawn at the ordered minute mark and processed per laboratory test instructions",
        [
            "Drawn whenever the phlebotomist returns from break without timing the ordered interval",
            "Combined with the fasting sample in one tube to save venipunctures on the patient",
            "Left at room temperature for six hours before centrifugation and courier transport",
        ],
        "GTT protocols depend on precise timing and handling for valid interpretation. Combined tubes and delayed processing invalidate curves.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    # skill-specimen-lab-013
    fact(
        "skill-specimen-lab",
        "Which urine specimen is required for most routine urinalysis and culture orders?",
        "Clean-catch midstream urine after cleansing the urethral meatus",
        [
            "First-void morning urine collected in an open cup on the counter",
            "Urine from the drainage bag connected to an indwelling catheter",
            "Saliva mixed with water when the patient cannot void on command",
        ],
        "Midstream after cleansing reduces periurethral contamination. Bag urine and non-urine fluids do not meet standard UA and culture requirements.",
        [S.NHA_CPT, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-014
    fact(
        "skill-specimen-lab",
        "How soon should most urine cultures be refrigerated or transported after collection?",
        "Within thirty minutes to two hours per laboratory policy unless additive is present",
        [
            "After twenty-four hours at room temperature to maximize bacterial colony growth",
            "After boiling the sample to sterilize it before courier transport to the laboratory",
            "After leaving the collection cup in direct sunlight to warm the urine specimen",
        ],
        "Bacteria multiply or die outside optimal conditions, skewing culture results. Heat and prolonged room storage distort colony counts.",
        [S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-015
    fact(
        "skill-specimen-lab",
        "What is the purpose of a 24-hour urine collection container?",
        "Measure total daily excretion of analytes such as protein or creatinine",
        [
            "Provide a single random spot check of urine color at one void",
            "Replace blood creatinine when venipuncture is inconvenient for the patient",
            "Store urine at body temperature for comfort during the collection period",
        ],
        "Timed total volume collections integrate renal output over a day. Random cups cannot quantify twenty-four-hour excretion rates.",
        [S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-016
    fact(
        "skill-specimen-lab",
        "When collecting sputum for acid-fast bacilli testing, what patient instruction is key?",
        "Produce deep cough specimen from the lungs, not saliva from the mouth",
        [
            "Rinse with mouthwash and submit the first saliva spit into the cup",
            "Collect nasal drainage swabbed from the anterior nares instead of sputum",
            "Submit postnasal drip on a throat swab without a productive cough",
        ],
        "Saliva and nasal swabs lack lower respiratory material needed for AFB smears. Deep cough samples target bronchial secretions.",
        [S.NHA_CPT, S.NHA_CCMA],
        "advanced",
    ),
    # skill-specimen-lab-017
    fact(
        "skill-specimen-lab",
        "How should a stool specimen for occult blood be collected when using kit cards?",
        "Small samples from multiple bowel movements on card windows per kit directions",
        [
            "One large watery sample filling the entire occult blood card without separate smears",
            "Stool mixed with toilet bowl water before scooping into the collection vial",
            "Rectal exam glove tip sent without visible stool on the collection card surface",
        ],
        "Kit instructions specify sample size and number of smears for sensitivity. Toilet water dilutes blood and invalidates the test.",
        [S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-018
    fact(
        "skill-specimen-lab",
        "What patient preparation is often required before a fasting lipid panel blood draw?",
        "No caloric intake for nine to twelve hours unless the order states otherwise",
        [
            "High-fat breakfast one hour before the draw to test dietary fat absorption",
            "Continuous snacking overnight to keep glucose stable for lipid panel testing",
            "Alcohol intake the night before to relax the patient for venipuncture access",
        ],
        "Triglycerides rise after meals and can affect calculated LDL on some panels. Orders may waive fasting, but default lipid prep is empty stomach.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    # skill-specimen-lab-019
    fact(
        "skill-specimen-lab",
        "Why is the order of draw sequence taught during multi-tube venipuncture?",
        "To prevent additive carryover that can alter results in subsequent tubes",
        [
            "To match tube colors to the phlebotomist uniform for visual consistency",
            "To draw the smallest tubes first because they weigh less on transport scales",
            "To finish with culture bottles so alcohol remains in the needle hub",
        ],
        "EDTA or clot activator from an earlier tube can contaminate coagulation or chemistry samples. Sequence rules minimize cross-tube interference.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-020
    fact(
        "skill-specimen-lab",
        "What should be done if blood stops flowing while drawing a light blue coagulation tube?",
        "Adjust the needle position gently or redraw at another site",
        [
            "Fill the citrate tube halfway and dilute with saline from an IV flush syringe",
            "Switch to a lavender tube and send that tube for PT and INR testing instead",
            "Shake the partial tube vigorously to reach the fill line printed on the label",
        ],
        "Coagulation tubes need correct blood-to-additive ratio. Substituting tube types or diluting ruins clotting assay validity.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-021
    fact(
        "skill-specimen-lab",
        "How should sharps be disposed immediately after venipuncture?",
        "Activate safety device and place the intact needle in an approved sharps container",
        [
            "Recap with two hands and place the uncapped needle in the biohazard red bag",
            "Break the needle off into the regular trash can to save sharps container space",
            "Leave the used needle on the bed for environmental services staff to collect later",
        ],
        "Point-of-use sharps disposal prevents needlestick injuries. Recapping and red-bag needles violate OSHA and clinic policy.",
        [S.OSHA_BBP, S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-022
    fact(
        "skill-specimen-lab",
        "What is the purpose of centrifuging serum separator tubes before chemistry testing?",
        "Separate serum from cells so analyzers measure cell-free supernatant",
        [
            "Heat inactivate viruses in the tube before staff transport to the lab",
            "Mix EDTA evenly for potassium measurement on chemistry instruments",
            "Clot lavender tubes faster for hematology cell counts on the chemistry line",
        ],
        "Centrifugation yields serum or plasma appropriate to the test menu. EDTA tubes and heat steps are not substitutes for proper tube type.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-023
    fact(
        "skill-specimen-lab",
        "A peripheral IV is infusing in the patient's right forearm and venous blood is ordered. What is the best venipuncture plan?",
        "Draw from the opposite arm or from a site proximal to the catheter",
        [
            "Draw from a vein distal to the IV on the same arm",
            "Collect the sample through the IV hub without a separate venipuncture",
            "Pause the infusion and use any visible hand vein on the same arm",
        ],
        "Blood drawn distal to a running IV is often diluted by infusate. The opposite extremity or a proximal site may be ordered when a distal stick would falsify results.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    # skill-specimen-lab-024
    fact(
        "skill-specimen-lab",
        "Which vein is often first choice for adult venipuncture when accessible?",
        "Median cubital vein in the antecubital fossa",
        [
            "Basilic vein crossing tendons without assessing depth or nerve proximity",
            "Dorsal hand vein in a patient with poor oral intake and dehydration",
            "Femoral vein at the groin for routine outpatient chemistry panels",
        ],
        "The antecubital area offers stable superficial veins with lower nerve injury risk. Hand and femoral sites are reserved for special situations.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    # skill-specimen-lab-025
    fact(
        "skill-specimen-lab",
        "What action reduces patient injury risk if venipuncture fails after one careful attempt?",
        "Stop, apply pressure, and seek experienced help or another site",
        [
            "Probe deeply through muscle until blood returns in the syringe barrel",
            "Switch to a larger gauge needle in the same puncture hole without pressure",
            "Ask the patient to pump the fist until bruising spreads for vein visualization",
        ],
        "Repeated traumatic attempts cause hematoma and nerve injury. Escalation and site change follow facility limits on attempts.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-026
    fact(
        "skill-specimen-lab",
        "How should a glucose gray-top fluoride tube be processed for plasma glucose?",
        "Invert gently, chill or centrifuge per lab manual to inhibit glycolysis",
        [
            "Leave at room temperature all day because fluoride is unnecessary for glucose",
            "Freeze whole blood uncentrifuged for transport in a lunch cooler",
            "Clot upright for thirty minutes like a red-top serum separator tube",
        ],
        "Fluoride slows red cell metabolism of glucose ex vivo. Delayed processing falsely lowers or raises glucose depending on timing.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-027
    fact(
        "skill-specimen-lab",
        "What does a requisition form communicate to the laboratory?",
        "Ordered tests, clinical information, collection time, and patient identifiers",
        [
            "Phlebotomy station phone extensions for the nursing unit assigned that collection day",
            "Patient appointment reminder scripts for front-desk scheduling staff to read aloud",
            "Waiting room chair inventory colors for facilities maintenance department weekly tracking",
        ],
        "Requisitions link physical specimens to the correct test battery on the analyzer. Administrative trivia does not direct laboratory work.",
        [S.NHA_CPT, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-028
    fact(
        "skill-specimen-lab",
        "Why must specimens with biohazard risk be transported in leak-proof bags?",
        "To protect handlers from exposure if tubes break during transit",
        [
            "To keep specimens warm for bacterial culture on chemistry autoanalyzers",
            "To allow pooling of multiple patients' tubes in one outer transport sack",
            "To display patient Social Security numbers through clear plastic windows",
        ],
        "Secondary containers contain spills during courier or pneumatic tube transport. Pooling patient samples is a critical identification error.",
        [S.CLSI_GP41, S.OSHA_BBP],
        "beginner",
    ),
    # skill-specimen-lab-029
    fact(
        "skill-specimen-lab",
        "What is the correct response when a tube is underfilled for coagulation testing?",
        "Discard the tube and redraw with correct fill to preserve citrate ratio",
        [
            "Top off with saline from an IV line to the mark on the tube",
            "Send the short draw with a note that the lab should mathematically correct",
            "Invert vigorously until clot forms and then centrifuge for plasma",
        ],
        "Citrate volume is calibrated to a fixed blood volume; dilution invalidates PT and PTT. Labs cannot reliably correct underfilled citrate tubes.",
        [S.CLSI_GP41],
        "advanced",
    ),
    # skill-specimen-lab-030
    fact(
        "skill-specimen-lab",
        "When is a heel stick capillary collection preferred over venipuncture?",
        "For small volume infant tests when policy allows capillary sampling",
        [
            "For routine adult cholesterol panels requiring large serum volume",
            "For blood cultures in febrile neonates as the first-line collection method",
            "For coagulation studies requiring precise citrate fill ratios in adults",
        ],
        "Capillary samples suit limited-volume neonatal screens. Adults and coagulation studies need venous volumes and tube types capillary cannot provide.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-031
    fact(
        "skill-specimen-lab",
        "How should alcohol skin prep dry before venipuncture needle insertion?",
        "Allow complete drying to reduce sting and limit hemolysis from residual alcohol",
        [
            "Wipe wet alcohol forward into the intended venipuncture puncture site before insertion",
            "Blow on the prep site to mix alcohol with surface dirt for better needle grip",
            "Insert the collection needle while alcohol is still pooling on the prepared skin",
        ],
        "Wet alcohol can hemolyze cells and cause patient discomfort. Proper prep uses a single outward spiral and air drying.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-032
    fact(
        "skill-specimen-lab",
        "What should staff document when a specimen cannot be collected as ordered?",
        "Reason for cancellation, patient status, and provider notification",
        [
            "Nothing, since the lab assumes the draw is already in transit",
            "A time stamp that matches the scheduled collection window",
            "The specimen label with the draw time crossed out and no added note",
        ],        "Providers need accurate cancellation data to reorder or change care. False documentation delays diagnosis and treatment.",
        [S.NHA_CPT, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-specimen-lab-033
    fact(
        "skill-specimen-lab",
        "Which tube top color is used for EDTA anticoagulant in hematology collections?",
        "Lavender (purple) top",
        [
            "Light blue (citrate) top",
            "Green (heparin) top",
            "Gray (fluoride) top",
        ],
        "Lavender or purple tops contain EDTA for CBC and many whole-blood hematology tests. Light blue is citrate for coagulation, green is heparin for plasma chemistry, and gray is fluoride for glucose preservation.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    # skill-specimen-lab-034
    fact(
        "skill-specimen-lab",
        "Why should specimens for potassium be protected from hemolysis during transport?",
        "Intracellular potassium release falsely elevates serum or plasma potassium results",
        [
            "Potassium leaks out of tubes that are labeled with the wrong color cap on the tube",
            "Refrigeration removes all potassium from the blood sample overnight in storage",
            "Shaking tubes mixes sodium into potassium channels printed on the tube label",
        ],
        "Lysed red cells pour potassium into the liquid phase. Handling and tube type matter more than label hue alone.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-035
    fact(
        "skill-specimen-lab",
        "What is chain of custody documentation used for in toxicology specimen collection?",
        "Tracks each handler of a legal or forensic sample from collection through storage",
        [
            "Lists grocery items the patient ate before a routine fasting cholesterol blood test",
            "Replaces patient identifiers on standard chemistry tubes processed in the laboratory",
            "Records parking receipts for outpatient phlebotomy visits at the clinic entrance",
        ],
        "Forensic chains prevent tampering disputes in workplace or legal testing. Routine chemistry does not use the same custody forms.",
        [S.NHA_CPT],
        "advanced",
    ),
    # skill-specimen-lab-036
    fact(
        "skill-specimen-lab",
        "How should a patient be positioned for routine venipuncture in a chair?",
        "Seated with arm extended and supported on a stable surface",
        [
            "Standing with arm dangling to maximize venous distension for hours",
            "Supine with tourniquet on the ankle for antecubital draws",
            "Prone on the floor while staff kneel behind the patient unseen",
        ],
        "Supported extension stabilizes the vein and reduces needle movement. Unsupported dangling arms and wrong limb tourniquet placement increase injury risk.",
        [S.CLSI_GP41],
        "beginner",
    ),
    # skill-specimen-lab-037
    fact(
        "skill-specimen-lab",
        "When must blood alcohol specimens follow special collection and preservation rules?",
        "When legal or workplace testing requires sealed kits and witnessed blood collection",
        [
            "Whenever a chemistry panel includes liver enzymes listed on the laboratory requisition",
            "Whenever the patient drank water in the waiting room before the venipuncture draw",
            "Whenever gray-top fluoride tubes are unavailable for routine glucose testing",
        ],
        "Evidentiary alcohol testing uses controlled kits, not routine serum draws. Liver panels and glucose tubes follow different standards.",
        [S.NHA_CPT],
        "advanced",
    ),
    # skill-specimen-lab-038
    fact(
        "skill-specimen-lab",
        "What does STAT on a laboratory order indicate to collection staff?",
        "Urgent processing for patient care; prioritize specimen collection and transport",
        [
            "The test may be collected next week when the central laboratory is less busy",
            "The patient should fast for three days before any blood sample is taken",
            "The specimen can remain at the bedside unattended until the end of the nursing shift",
        ],
        "STAT signals time-sensitive results such as critical electrolytes or crossmatch. Delayed collection defeats the purpose of the urgent order.",
        [S.NHA_CPT, S.NHA_CCMA],
        "beginner",
    ),
    # skill-specimen-lab-039
    fact(
        "skill-specimen-lab",
        "Why should tourniquets be sanitized or single-patient per policy?",
        "Reusable bands can carry blood and skin flora between patients",
        [
            "Sanitizing tourniquets removes the need for hand hygiene after draws",
            "Single-patient tourniquets replace two-identifier verification rules",
            "Shared tourniquets improve vein distension by transferring blood between arms",
        ],
        "Infection control applies to accessories that contact skin. Identification and hand hygiene remain mandatory with any tourniquet policy.",
        [S.CDC_STANDARD_PRECAUTIONS, S.CLSI_GP41],
        "intermediate",
    ),
    # skill-specimen-lab-040
    fact(
        "skill-specimen-lab",
        "What should be done with a specimen that cannot be linked to a patient after labeling error?",
        "Discard the specimen and recollect after confirming identity",
        [
            "Run the analyzer and attach the results to the busiest chart",
            "Store the tube in the refrigerator until the correct patient is found",
            "Ask the staff on shift to identify which patient was in that room",
        ],
        "Unlabeled or mismatched tubes are unsuitable for clinical decisions. Safe practice requires discard and redraw with verified identity.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "advanced",
    ),
    # skill-specimen-lab-041
    fact(
        "skill-specimen-lab",
        "How does fasting affect a capillary glucose measurement compared with post-meal testing?",
        "Fasting values reflect baseline glucose without recent carbohydrate food intake",
        [
            "Fasting raises glucose because the body stops insulin production entirely after sleep",
            "Meals have no effect on capillary glucose readings within eight hours of eating",
            "Fasting requires using a red-top serum tube instead of a capillary meter strip",
        ],
        "Recent meals elevate capillary glucose for screening and monitoring comparisons. Fasting protocols standardize interpretation against reference ranges.",
        [S.CDC_DIABETES_BASICS, S.NHA_CPT],
        "intermediate",
    ),
    # skill-specimen-lab-042
    fact(
        "skill-specimen-lab",
        "What is the primary reason for mixing additive tubes immediately after blood enters the tube?",
        "To distribute anticoagulant or clot activator before cells clot or aggregate",
        [
            "To warm the blood sample to body temperature for immediate oral patient drinking trials",
            "To remove hemoglobin from plasma by shaking red cells out of liquid suspension phase",
            "To let air bubbles rise so the additive tube can be underfilled safely without redraw",
        ],
        "Delayed mixing causes microclots and rejected hematology specimens. Mixing is not a substitute for correct fill volume.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),

]
