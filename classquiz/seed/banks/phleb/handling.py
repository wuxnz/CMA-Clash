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
        "Patient identifiers, date and time of collection, and collector identification per policy",
        [
            "Tube color alone without patient name or medical record number",
            "Collector initials, with no date or time of collection",
            "A label with the room number and no medical record number",
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
            "Vigorous shaking for thirty seconds to froth the sample",
            "Centrifuging before inversion occurs",
            "Leaving tubes horizontal without mixing additive tubes",
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
            "Immediate freezing while still completely liquid",
            "Heating the tube to body temperature to accelerate clotting",
            "Dilution with saline to the fill line",
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
            "Whichever setting is fastest regardless of g-force",
            "Leaving outpatient specimens uncentrifuged",
            "Patient preference for spin duration",
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
            "Ambient room temperature for all specimens regardless of analyte stability",
        ],
        "Stability windows differ for enzymes, gases, and cells. "
        "GP41 emphasizes delivering or storing specimens within defined preanalytic limits.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What may light-sensitive analytes such as bilirubin or some vitamins require?",
        "Amber wrap or transport inside a light-blocking container",
        [
            "Exposure to UV light to stabilize pigments",
            "Clear plastic bags for visibility",
            "Room light exposure for at least one hour",
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
            "Prothrombin time without affecting electrolytes",
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
        "Recollection if the degree of hemolysis exceeds laboratory reject criteria",
        [
            "Reporting the value without comment to save time",
            "Diluting the sample with saline to mask hemolysis",
            "Adding citrate from another tube to fix electrolytes",
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
        "Single-patient use and discarded into an approved sharps container",
        [
            "Wiped with alcohol and reused on the next patient",
            "Shared in skills lab without policy between classmates",
            "Left uncapped on the counter between draws",
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
            "Overnight storage at room temperature on the nursing unit",
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
        "Approved collection devices and immediate processing per the test manual",
        [
            "A serum separator left upright for several hours",
            "Fingerstick into a citrate tube without verification",
            "Delayed spin because lactate increases with waiting",
        ],
        "Glycolysis and metabolism falsely lower measured lactate when processing lags. "
        "GP41 defers to laboratory-defined tubes, tourniquet time, and spin requirements for lactate.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What handling do arterial blood gas specimens need after collection?",
        "Immediate gentle mixing, ice when required, and analysis within stability limits",
        [
            "Clotting upright like a serum chemistry tube",
            "Storage in a vaccine refrigerator without mixing",
            "Leaving the syringe uncapped to balance oxygen",
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
            "Every routine complete blood count in outpatient clinics",
            "All urine dipsticks regardless of purpose",
            "Staff scheduling records in the laboratory",
        ],
        "Each transfer of a legal specimen is logged with seals and signatures. "
        "Routine clinical chemistry does not use chain of custody unless ordered for forensic analysis.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What steps should be included in the response when a tube shatters inside a centrifuge?",
        "Stopping the spin, using PPE, and following biohazard spill cleanup protocol",
        [
            "Reaching into the rotor while it is still moving",
            "Wiping shards with bare hands to save time",
            "Ignoring aerosols if the lid looks intact",
        ],
        "Broken glass and blood aerosols create sharps and exposure risk. "
        "GP41 and OSHA bloodborne pathogen procedures govern safe cleanup before reuse of equipment.",
        _REF_BBP,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What method should pneumatic tube system transport of blood specimens use?",
        "Leak-proof padded carriers approved by the laboratory for fragile tests",
        [
            "Uncapped tubes upright without secondary containment",
            "Mixed food and specimens in the same carrier",
            "Maximum launch speed for every chemistry panel",
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
            "Change glucose without affecting electrolytes",
            "Improve coagulation factor stability in serum",
            "Eliminate the need for a centrifuge step",
        ],
        "Cellular metabolism and leakage continue until separation. "
        "GP41 processing timelines specify maximum pre-centrifuge delay for serum electrolytes.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What actions are required when critical laboratory values are identified?",
        "Immediate notification to the responsible clinician per documented protocol",
        [
            "Batching results at month-end for efficiency",
            "Posting values on a public waiting-room board",
            "Ignoring if a repeat draw might happen later",
        ],
        "Timely communication enables treatment for life-threatening abnormalities. "
        "Accreditation standards and GP41 quality systems define read-back and documentation of critical calls.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What should outbound courier pickup of specimens ensure?",
        "Secure leak-proof packaging with required temperature monitors or ice",
        [
            "Open tubes grouped in an unlabeled plastic bag",
            "Delay beyond stability limits without notifying the lab",
            "Mixing patient specimens in one container to save space",
        ],
        "Couriers extend the preanalytic phase; conditions must match test stability tables. "
        "GP41 transport guidance applies from bedside through laboratory receipt.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What should point-of-care testing logs record?",
        "Operator identity, quality control, patient identifiers, and results",
        [
            "Outdoor temperature at the time of testing",
            "Arbitrary numbers instead of patient identifiers",
            "Lunch orders for staff working the meter",
        ],
        "CLIA-waived and moderate-complexity POC programs require traceable documentation. "
        "GP41-aligned POC workflows integrate device QC with patient-result linkage.",
        _REF_POC,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "If a specimen container breaks during transit, what should staff do?",
        "Notify the laboratory, document the incident, and recollect when necessary",
        [
            "Tape broken glass together and submit without note",
            "Relabel unknown shards with the next patient in line",
            "Hide damage to avoid delaying results",
        ],
        "Compromised containers risk exposure and uninterpretable results. "
        "GP41 incident management includes safety cleanup and communication about need for redraw.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How does aliquoting serum or plasma into secondary tubes help?",
        "Avoid repeated freeze-thaw cycles on the primary sample when policy requires",
        [
            "Eliminate all labeling requirements",
            "Replace centrifugation permanently",
            "Mix additives between incompatible tube types",
        ],
        "Separate aliquots preserve unstable analytes for send-out testing. "
        "Each aliquot still requires full identification under GP41 traceability rules.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "When does refrigerated storage after collection apply?",
        "Only to tests with defined cold stability in the laboratory manual",
        [
            "Identically to every tube type without reading the manual",
            "Not in any clinical laboratory",
            "When the patient requests cold samples",
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
            "Automatic refrigeration inside the tube",
            "Improved stability for all enzymes",
            "No change if tubes are labeled correctly",
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
            "Permanent freezing of glucose at room temperature",
            "Accurate glucose regardless of time when gray tops are used",
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
        "Coagulation studies because the blood-to-anticoagulant ratio is wrong",
        [
            "The complete blood count indices on the same draw",
            "The urinalysis dipstick reading from the same visit",
            "The ABG analysis drawn in a heparin syringe",
        ],
        "Citrate tubes must meet the manufacturer fill line for valid PT and aPTT results. "
        "GP41 volume requirements are part of preanalytic quality for coagulation testing.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "How does maintaining flow help when a butterfly set is used for multiple tubes?",
        "Prevent clot formation in the tubing and ensure proper tube fill",
        [
            "Allow air bubbles to replace blood in each tube",
            "Stop flow between every tube for five minutes",
            "Ignore underfilled tubes to save time",
        ],
        "Stasis in the line can activate coagulation and reduce volume delivered to additive tubes. "
        "GP41 multi-tube technique keeps the assembly patent until the last required tube is filled.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Why does time of collection on the label matter?",
        "Reference ranges and stability calculations often depend on draw time",
        [
            "It is decorative information for the courier",
            "It replaces the need for patient identification",
            "It determines the phlebotomist shift bonus",
        ],
        "Therapeutic drug monitoring and timed tests interpret results relative to dose and fasting clocks. "
        "GP41 labeling standards include collection date and time for preanalytic traceability.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "If the wrong tube type was collected for an ordered test, what should the collector do?",
        "Notify the laboratory and follow policy for recollection or add-on testing",
        [
            "Pour blood into the correct tube without documenting",
            "Freeze the wrong tube and assume the lab will adapt",
            "Discard the order without telling the patient or provider",
        ],
        "Incompatible additives cannot be corrected by transferring specimen after the fact. "
        "GP41 error management emphasizes disclosure and redraw when sample type invalidates the assay.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "What do STAT specimens still require despite urgency?",
        "The same identification, labeling, and handling rules as routine collections",
        [
            "Skipping labels to save minutes",
            "Ignoring temperature limits because the test is urgent",
            "Using another patient's prelabeled tubes to move faster",
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
            "Whichever is closest regardless of contamination risk",
            "Avoiding ice because all tests are kept at room temperature",
            "Patient preference between wet and dry cooling",
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
        "May cause cell morphology changes unless the manual requires chilling",
        [
            "Is required for every complete blood count",
            "Prevents all clotting in serum separator tubes",
            "Replaces gentle mixing after collection",
        ],
        "Cold can affect MCV and other indices on some analyzers. "
        "Unless the test manual specifies cold transport, GP41 default is room temperature delivery within stability limits.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "When batching multiple patients' specimens in one bag for courier pickup, what is required?",
        "Requires each tube to remain individually labeled and segregated per policy",
        [
            "Allows removing labels to save space",
            "Permits mixing serum and urine without secondary bags",
            "Eliminates temperature requirements for all contents",
        ],
        "Batch transport still demands patient-specific identification on every container. "
        "GP41 traceability extends through courier handoff with leak-proof secondary containment.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "How does rechecking the requisition against collected tubes before leaving the patient help?",
        "Catch missing tubes or wrong tests before the patient departs",
        [
            "Replace two-identifier patient verification",
            "Eliminate the need for laboratory accessioning",
            "Allow unlabeled tubes if the count matches",
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
            "Affects urine color without changing chemistry",
            "Improves accuracy by concentrating cells",
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
