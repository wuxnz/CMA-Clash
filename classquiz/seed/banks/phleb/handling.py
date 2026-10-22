# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored specimen handling and processing questions (topic phleb-handling)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_REF = [S.CLSI_GP41, S.NHA_CPT]
_REF_POC = [S.CLSI_GP41, S.FDA_CLIA_WAIVED, S.NHA_CPT]
_REF_BBP = [S.CLSI_GP41, S.OSHA_BBP, S.NHA_CPT]

FACTS: list[dict] = [
    fact(
        "phleb-handling",
        "What minimum specimen label elements at collection are required?",
        "Patient identifiers, date and time of collection, and collector name",
        [
            "Tube color alone without the patient name or medical record number at all",
            "The collector initials, with no date or time of collection",
            "A label with the room number and no medical record number on it",
        ],
        "Complete labels link the tube to the correct patient and collection event. "
        "GP41 preanalytic requirements align with laboratory accreditation standards for traceability.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How should additive tubes such as EDTA and citrate be mixed?",
        "Gentle end-over-end inversion per manufacturer instructions",
        [
            "Vigorous shaking for thirty seconds to froth the sample up",
            "Centrifuging before inversion occurs",
            "Leaving the tubes horizontal without mixing the additive tubes",
        ],
        "Proper inversion distributes anticoagulant without hemolyzing cells. "
        "Over-mixing or skipping inversion causes clots or microclots that invalidate hematology and coagulation results.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What do serum separator tubes for chemistry often require?",
        "Upright clotting for the laboratory-defined time before centrifugation",
        [
            "Immediate freezing while the tube is still completely liquid inside it",
            "Heating the tube to body temperature to accelerate the clot formation",
            "Dilution with saline up to the fill line",
        ],
        "Complete clot formation lets fibrin separate cleanly during spin. "
        "GP41 processing steps follow the test manual for clot time and centrifuge settings.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What centrifugation speed and time should be followed for serum or plasma separation?",
        "The laboratory procedure manual for each test category",
        [
            "Whichever setting is fastest with no regard to g-force",
            "Leaving the outpatient specimens uncentrifuged",
            "The patient preference for the spin duration",
        ],
        "Incorrect spin conditions leave residual cells or break gel barriers, altering analytes. "
        "CLSI-aligned labs document validated centrifuge protocols collectors must follow.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What should transport of specimens to the laboratory maintain?",
        "Temperature and timing limits listed on the test requisition or manual",
        [
            "Direct sunlight exposure to prevent condensation",
            "Open caps to equalize temperature during transit",
            "Room temperature for all specimens with no regard for analyte stability",
        ],
        "Stability windows differ for enzymes, gases, and cells. "
        "GP41 emphasizes delivering or storing specimens within defined preanalytic limits.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What may light-sensitive analytes such as bilirubin or some vitamins require?",
        "Amber wrap or a light-blocking transport container",
        [
            "Exposure to the UV light to stabilize the pigment levels",
            "The clear plastic bags for visibility",
            "The room light exposure for at least one hour",
        ],
        "Photo-degradation can falsely lower concentrations before analysis. "
        "Laboratory manuals specify protection that GP41-compliant workflows incorporate at collection or handoff.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What visible hemolysis in a serum sample may falsely elevate?",
        "Potassium and several enzymes on chemistry panels",
        [
            "The prothrombin time without affecting the electrolytes",
            "Glucose upward in every assay",
            "Platelet count on an EDTA hematology sample",
        ],
        "Lysed red cells release intracellular potassium and enzymes into serum or plasma. "
        "Gentle draw technique and timely processing reduce hemolysis per GP41 quality goals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What is the usual response when hemolysis invalidates a potassium result?",
        "Recollection if the hemolysis exceeds the laboratory reject criteria",
        [
            "Reporting the value without a comment to save the time",
            "Diluting the sample with saline to mask the hemolysis",
            "Adding the citrate from another tube to fix the electrolytes in the sample",
        ],
        "Labs define hemolysis indices and reject rules to protect patient safety. "
        "GP41 treats unacceptable preanalytic quality as grounds for redraw rather than silent release.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What documentation do fasting glucose specimens require?",
        "Fasting status and collection time relative to the order",
        [
            "A casual snack documented as fasting if the patient insists",
            "The phlebotomist lunch break time",
            "Verbal results without a tube label",
        ],
        "Interpretation depends on whether the patient was truly fasting for the ordered interval. "
        "GP41 preanalytic data include timing and patient preparation instructions.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How must capillary puncture devices and lancets be handled?",
        "Single-patient use and discarded into a sharps container",
        [
            "Wiped with the alcohol and reused on the next patient",
            "Shared in the skills lab without a policy between classmates",
            "Left uncapped on the counter between the draws",
        ],
        "Reusable skin puncture devices violate standard precautions for blood exposure. "
        "OSHA and GP41 infection-control expectations require immediate disposal after one patient.",
        _REF_BBP,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What problems can delayed delivery of citrate coagulation tubes cause?",
        "Alter factor activity and prolong or shorten clotting assays",
        [
            "Improve accuracy by allowing extra clot formation in citrate",
            "Affect complete blood counts in EDTA",
            "Have no preanalytic effect if tubes are labeled",
        ],
        "Coagulation specimens are time-sensitive even before centrifugation. "
        "GP41 stresses prompt transport and processing per coagulation manuals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What do ammonia specimens often require?",
        "Prompt chilling and analysis within strict stability limits",
        [
            "Overnight storage at the room temperature on the nursing unit",
            "Freezing in a household freezer without protocol",
            "Exposure to room air with cap removed for equilibration",
        ],
        "Ammonia rises rapidly as blood sits at room temperature. "
        "Laboratory procedures aligned with GP41 specify ice transport and minimal delay.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What special handling do lactate specimens require?",
        "Approved collection devices and immediate processing per protocol",
        [
            "A serum separator tube left upright for several hours",
            "A fingerstick into a citrate tube without the verification",
            "The delayed spin because the lactate increases with the waiting time",
        ],
        "Glycolysis and metabolism falsely lower measured lactate when processing lags. "
        "GP41 defers to laboratory-defined tubes, tourniquet time, and spin requirements for lactate.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What handling do arterial blood gas specimens need after collection?",
        "Immediate mixing, ice when required, and analysis within limits",
        [
            "Clotting upright like a serum chemistry tube on the bench top of it",
            "The storage in a vaccine refrigerator without the mixing",
            "Leaving the syringe uncapped to balance the oxygen",
        ],
        "Air bubbles and delay change pO2, pCO2, and pH values. "
        "GP41 and blood gas manuals define rapid transport and exclusion of air from the sample.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "For what purpose is chain-of-custody documentation required?",
        "Forensic or legal specimens where possession must be traceable",
        [
            "Every routine complete blood count done in the outpatient clinics",
            "The urine dipsticks of every kind and purpose",
            "The staff scheduling records kept in the laboratory",
        ],
        "Each transfer of a legal specimen is logged with seals and signatures. "
        "Routine clinical chemistry does not use chain of custody unless ordered for forensic analysis.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What steps should be included in the response when a tube shatters inside a centrifuge?",
        "Stopping the spin, using PPE, and following the spill protocol",
        [
            "Reaching into the rotor while the rotor is still moving",
            "Wiping the shards with the bare hands to save the time",
            "Ignoring the aerosols if the centrifuge lid looks still intact",
        ],
        "Broken glass and blood aerosols create sharps and exposure risk. "
        "GP41 and OSHA bloodborne pathogen procedures govern safe cleanup before reuse of equipment.",
        _REF_BBP,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What method should pneumatic tube system transport of blood specimens use?",
        "Leak-proof padded carriers approved by the laboratory",
        [
            "The uncapped tubes upright without the secondary containment bags",
            "The mixed food and the specimens in the same carrier",
            "The maximum launch speed for each chemistry panel",
        ],
        "Acceleration and deceleration can hemolyze cells or break gel barriers. "
        "Labs validate which tests may use tube systems under GP41 transport quality standards.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What problems can holding serum at room temperature too long before centrifugation cause?",
        "Falsely elevate potassium as cells leak intracellular contents",
        [
            "Change the glucose value without affecting the electrolyte results",
            "Improve the coagulation factor stability in the serum sample",
            "Eliminate the need for the centrifuge step",
        ],
        "Cellular metabolism and leakage continue until separation. "
        "GP41 processing timelines specify maximum pre-centrifuge delay for serum electrolytes.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What actions are required when critical laboratory values are identified?",
        "Immediate notification to the responsible clinician per protocol",
        [
            "Batching the results at the month-end for the efficiency",
            "Posting the values on a public waiting-room board in the clinic lobby",
            "Ignoring the value if a repeat draw might happen later",
        ],
        "Timely communication enables treatment for life-threatening abnormalities. "
        "Accreditation standards and GP41 quality systems define read-back and documentation of critical calls.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What should outbound courier pickup of specimens ensure?",
        "Secure leak-proof packaging with temperature monitors or ice",
        [
            "The open tubes grouped in an unlabeled plastic bag",
            "The delay beyond the stability limits without notifying the lab",
            "Mixing the patient specimens in one container to save space",
        ],
        "Couriers extend the preanalytic phase; conditions must match test stability tables. "
        "GP41 transport guidance applies from bedside through laboratory receipt.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What should point-of-care testing logs record?",
        "Operator identity, quality control, patient identifiers, results",
        [
            "The outdoor temperature at the time of the testing",
            "The arbitrary numbers instead of the patient identifiers in the log",
            "The lunch orders for the staff working the meter",
        ],
        "CLIA-waived and moderate-complexity POC programs require traceable documentation. "
        "GP41-aligned POC workflows integrate device QC with patient-result linkage.",
        _REF_POC,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "If a specimen container breaks during transit, what should staff do?",
        "Notify the laboratory, document the incident, and recollect",
        [
            "Tape the broken glass together and submit it without a note",
            "Relabel the unknown shards with the next patient in line",
            "Hide the damage to avoid delaying the results",
        ],
        "Compromised containers risk exposure and uninterpretable results. "
        "GP41 incident management includes safety cleanup and communication about need for redraw.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How does aliquoting serum or plasma into secondary tubes help?",
        "Avoid repeated freeze-thaw cycles on the primary sample",
        [
            "Eliminate all of the labeling requirements",
            "Replace the centrifugation permanently",
            "Mix the additives between the incompatible tube types on the tray",
        ],
        "Separate aliquots preserve unstable analytes for send-out testing. "
        "Each aliquot still requires full identification under GP41 traceability rules.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "When does refrigerated storage after collection apply?",
        "Only tests with defined cold stability in the lab manual",
        [
            "Identically for each tube type without reading the manual",
            "Not in any of the clinical laboratories",
            "When the patient requests the cold samples",
        ],
        "Some analytes require refrigeration; others must not be chilled. "
        "GP41 directs collectors to follow test-specific stability rather than universal rules.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What can exposure of blood tubes to extreme heat during summer transport cause?",
        "Cell lysis and degradation of temperature-labile analytes",
        [
            "The automatic refrigeration inside the collection tube",
            "The improved stability for all of the enzymes in the panel",
            "No change if the tubes are labeled correctly on the chart",
        ],
        "Heat accelerates metabolism and can hemolyze cells in transit. "
        "Insulated transport containers are part of GP41-aligned summer collection programs.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What can delayed centrifugation of fluoride or oxalate glucose tubes still allow?",
        "Continued in vitro glycolysis if processing waits too long",
        [
            "The permanent freezing of the glucose at the room temperature",
            "Accurate glucose with no time limit when gray tops are used",
            "Elevation of INR in the same tube",
        ],
        "Fluoride inhibits enolase but does not instantly stop all metabolism. "
        "GP41 still recommends timely delivery and processing per glucose stability tables.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Why must blood not be poured or transferred between collection tubes?",
        "Additive carryover contaminates tubes and invalidates results",
        [
            "It is faster and therefore encouraged for stat orders",
            "Culture bottles are affected by transfer while other tubes are not",
            "Transfer improves coagulation studies in citrate",
        ],
        "Each tube is filled directly from the patient with its intended additive load. "
        "GP41 order-of-draw and handling rules prohibit cross-transfer that would skew analyte concentrations.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What results are most threatened by underfilled citrate tubes?",
        "Coagulation studies because the blood-to-anticoagulant ratio is off",
        [
            "The complete blood count indices on the same venipuncture order set",
            "The urinalysis dipstick result from the same clinic visit time",
            "The ABG analysis drawn in a heparin syringe at the chair",
        ],
        "Citrate tubes must meet the manufacturer fill line for valid PT and aPTT results. "
        "GP41 volume requirements are part of preanalytic quality for coagulation testing.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "How does maintaining flow help when a butterfly set is used for multiple tubes?",
        "Prevent clot formation in the tubing and ensure tube fill",
        [
            "Allow the air bubbles to replace the blood in each collection tube",
            "Stop the flow between every tube for five full minutes",
            "Ignore the underfilled tubes to save the time",
        ],
        "Stasis in the line can activate coagulation and reduce volume delivered to additive tubes. "
        "GP41 multi-tube technique keeps the assembly patent until the last required tube is filled.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Why does time of collection on the label matter?",
        "Reference ranges and stability limits often depend on draw time",
        [
            "It is decorative information for the courier on the transport route",
            "It replaces the need for the patient identification",
            "It determines the phlebotomist shift bonus for the week",
        ],
        "Therapeutic drug monitoring and timed tests interpret results relative to dose and fasting clocks. "
        "GP41 labeling standards include collection date and time for preanalytic traceability.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "If the wrong tube type was collected for an ordered test, what should the collector do?",
        "Notify the laboratory and follow policy for recollection",
        [
            "Pour the blood into the correct tube without documenting it",
            "Freeze the wrong tube and assume the lab will adapt to it",
            "Discard the order without telling the patient or the provider",
        ],
        "Incompatible additives cannot be corrected by transferring specimen after the fact. "
        "GP41 error management emphasizes disclosure and redraw when sample type invalidates the assay.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What do STAT specimens still require despite urgency?",
        "The same identification, labeling, and handling rules as routine work",
        [
            "Skipping the labels to save the minutes",
            "Ignoring the temperature limits because the test is urgent for the care",
            "Using another patient prelabeled tubes to move faster",
        ],
        "Urgency does not waive patient safety or preanalytic quality controls. "
        "GP41 prioritizes rapid transport while maintaining complete labels and stability requirements.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How should frozen aliquots for send-out testing be stored and handled?",
        "Frozen per manual using appropriate containers and thaw protocols",
        [
            "Frozen in the primary EDTA tube without centrifuging when policy forbids it",
            "Thawed repeatedly at room temperature without limit",
            "Stored in formalin for long-term chemistry",
        ],
        "Incorrect freeze-thaw handling destroys labile analytes. "
        "Laboratory manuals aligned with GP41 define when to spin, separate, and freeze specific tests.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "How should wet ice versus gel packs for transport be chosen?",
        "Laboratory instructions for the specific test and carrier design",
        [
            "Whichever is closest with no concern for contamination risk",
            "Avoiding the ice because all of the tests are kept at room temperature",
            "The patient preference between the wet and dry cooling",
        ],
        "Some specimens need wet ice; others tolerate insulated cool packs without free water exposure. "
        "GP41 transport sections defer to validated laboratory shipping methods.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Why is hand hygiene required before handling filled collection tubes?",
        "Reduces cross-contamination after patient contact",
        [
            "Is unnecessary if gloves were worn during the draw",
            "Replaces the need to label tubes",
            "Should be skipped for stat specimens",
        ],
        "Gloves protect during venipuncture but hands may contact contaminated surfaces afterward. "
        "GP41 infection prevention includes hand hygiene when moving from patient care to paperwork and transport.",
        [S.CLSI_GP41, S.CDC_HAND_HYGIENE, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What can happen when EDTA hematology tubes are placed in direct contact with ice before CBC analysis?",
        "May cause cell morphology changes unless the manual requires it",
        [
            "Is the standard requirement for a complete blood count",
            "Prevents all of the clotting in the serum separator tubes after the spin",
            "Replaces the gentle mixing after the collection",
        ],
        "Cold can affect MCV and other indices on some analyzers. "
        "Unless the test manual specifies cold transport, GP41 default is room temperature delivery within stability limits.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "When batching multiple patients' specimens in one bag for courier pickup, what is required?",
        "Requires each tube to remain labeled and segregated per policy",
        [
            "Allows the removing of labels to save the space",
            "Permits the mixing of serum and urine without the secondary bags",
            "Eliminates the temperature requirements for all of the contents",
        ],
        "Batch transport still demands patient-specific identification on every container. "
        "GP41 traceability extends through courier handoff with leak-proof secondary containment.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "How does rechecking the requisition against collected tubes before leaving the patient help?",
        "Catch missing tubes or wrong tests before the patient goes",
        [
            "Replaces the two-identifier patient verification in the clinic",
            "Eliminate the need for the laboratory accessioning step",
            "Allow the unlabeled tubes if the count matches",
        ],
        "A brief reconciliation reduces callbacks and repeat venipunctures. "
        "GP41 quality practices combine identification, order match, and correct tube type at the bedside.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Why is delaying plasma separation from cells in a heparin tube problematic for ammonia-like assays?",
        "Can falsely change results as cells metabolize analytes",
        [
            "Affects the urine color without changing the chemistry panel",
            "Improves the accuracy by concentrating the cells",
            "Is recommended for all routine electrolyte panels",
        ],
        "Cellular metabolism continues until centrifugation separates plasma. "
        "GP41 processing emphasizes prompt spin and aliquot for unstable plasma analytes.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "After filling a lavender EDTA tube at the bedside, how many gentle inversions does CLSI typically recommend?",
        "8 to 10 gentle end-over-end inversions",
        [
            "3 to 4 gentle end-over-end inversions",
            "5 gentle end-over-end inversions",
            "No inversion before the tube reaches the laboratory",
        ],
        "Lavender EDTA tubes need thorough gentle mixing, typically about eight to ten inversions. "
        "Citrate or SST mixing counts are common confusions that leave hematology specimens under-mixed.",
        _REF,
        "beginner",
    ),

]
