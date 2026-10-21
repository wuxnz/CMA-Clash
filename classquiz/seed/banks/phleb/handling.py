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
        "Minimum specimen label elements at collection typically include:",
        "Patient identifiers, date and time of collection, and collector identification per policy",
        [
            "Tube color alone without patient name or medical record number",
            "Collector initials only, with no date or time of collection",
            "Barcode from a previous visit reused to save labels",
        ],
        "Complete labels link the tube to the correct patient and collection event. "
        "GP41 preanalytic requirements align with laboratory accreditation standards for traceability.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Additive tubes such as EDTA and citrate should be mixed by:",
        "Gentle end-over-end inversion per manufacturer instructions",
        [
            "Vigorous shaking for thirty seconds to froth the sample",
            "Centrifuging before any inversion occurs",
            "Leaving tubes horizontal without mixing additive tubes",
        ],
        "Proper inversion distributes anticoagulant without hemolyzing cells. "
        "Over-mixing or skipping inversion causes clots or microclots that invalidate hematology and coagulation results.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Serum separator tubes for chemistry often require:",
        "Upright clotting for the laboratory-defined time before centrifugation",
        [
            "Immediate freezing while still completely liquid",
            "Heating to body temperature in a microwave",
            "Dilution with saline to the fill line",
        ],
        "Complete clot formation lets fibrin separate cleanly during spin. "
        "GP41 processing steps follow the test manual for clot time and centrifuge settings.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Centrifugation speed and time for serum or plasma separation should follow:",
        "The laboratory procedure manual for each test category",
        [
            "Whichever setting is fastest regardless of g-force",
            "Never centrifuging outpatient specimens",
            "Patient preference for spin duration",
        ],
        "Incorrect spin conditions leave residual cells or break gel barriers, altering analytes. "
        "CLSI-aligned labs document validated centrifuge protocols collectors must follow.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Transporting specimens to the laboratory should maintain:",
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
        "Light-sensitive analytes such as bilirubin or some vitamins may require:",
        "Amber wrap or transport inside a light-blocking container",
        [
            "Exposure to UV light to stabilize pigments",
            "Clear plastic bags only for visibility",
            "Room light exposure for at least one hour",
        ],
        "Photo-degradation can falsely lower concentrations before analysis. "
        "Laboratory manuals specify protection that GP41-compliant workflows incorporate at collection or handoff.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Visible hemolysis in a serum sample may falsely elevate:",
        "Potassium and several enzymes on chemistry panels",
        [
            "Only prothrombin time without affecting electrolytes",
            "Glucose upward in every assay",
            "Platelet count on an EDTA hematology sample only",
        ],
        "Lysed red cells release intracellular potassium and enzymes into serum or plasma. "
        "Gentle draw technique and timely processing reduce hemolysis per GP41 quality goals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "When hemolysis invalidates a potassium result, the usual response is:",
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
        "Fasting glucose specimens require documentation of:",
        "Fasting status and collection time relative to the order",
        [
            "A casual snack documented as fasting if the patient insists",
            "Only the phlebotomist lunch break time",
            "Verbal results without any tube label",
        ],
        "Interpretation depends on whether the patient was truly fasting for the ordered interval. "
        "GP41 preanalytic data include timing and patient preparation instructions.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Capillary puncture devices and lancets must be:",
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
        "Delayed delivery of citrate coagulation tubes can:",
        "Alter factor activity and prolong or shorten clotting assays",
        [
            "Improve accuracy by allowing extra clot formation in citrate",
            "Affect only complete blood counts in EDTA",
            "Have no preanalytic effect if tubes are labeled",
        ],
        "Coagulation specimens are time-sensitive even before centrifugation. "
        "GP41 stresses prompt transport and processing per coagulation manuals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Ammonia specimens often require:",
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
        "Lactate collection and handling require:",
        "Approved collection devices and immediate processing per the test manual",
        [
            "Any serum separator left upright for several hours",
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
        "Arterial blood gas specimens after collection need:",
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
        "Chain-of-custody documentation is required for:",
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
        "If a tube shatters inside a centrifuge, the response includes:",
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
        "Pneumatic tube system transport of blood specimens should use:",
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
        "Holding serum at room temperature too long before centrifugation can:",
        "Falsely elevate potassium as cells leak intracellular contents",
        [
            "Only change glucose without affecting electrolytes",
            "Improve coagulation factor stability in serum",
            "Eliminate the need for any centrifuge step",
        ],
        "Cellular metabolism and leakage continue until separation. "
        "GP41 processing timelines specify maximum pre-centrifuge delay for serum electrolytes.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Critical laboratory values require:",
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
        "Outbound courier pickup of specimens should ensure:",
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
        "Point-of-care testing logs should record:",
        "Operator identity, quality control, patient identifiers, and results",
        [
            "Only outdoor temperature at the time of testing",
            "Random numbers instead of patient identifiers",
            "Lunch orders for staff working the meter",
        ],
        "CLIA-waived and moderate-complexity POC programs require traceable documentation. "
        "GP41-aligned POC workflows integrate device QC with patient-result linkage.",
        _REF_POC,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "If a specimen container breaks during transit, staff should:",
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
        "Aliquoting serum or plasma into secondary tubes helps:",
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
        "Refrigerated storage after collection applies:",
        "Only to tests with defined cold stability in the laboratory manual",
        [
            "Identically to every tube type without reading the manual",
            "Never in any clinical laboratory",
            "Only when the patient requests cold samples",
        ],
        "Some analytes require refrigeration; others must not be chilled. "
        "GP41 directs collectors to follow test-specific stability rather than universal rules.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Exposure of blood tubes to extreme heat during summer transport may cause:",
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
        "Delayed centrifugation of fluoride/oxalate glucose tubes can still allow:",
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
        "Blood must not be poured or transferred between collection tubes because:",
        "Additive carryover contaminates tubes and invalidates results",
        [
            "It is faster and therefore encouraged for stat orders",
            "Only culture bottles are affected by transfer",
            "Transfer improves coagulation studies in citrate",
        ],
        "Each tube is filled directly from the patient with its intended additive load. "
        "GP41 order-of-draw and handling rules prohibit cross-transfer that would skew analyte concentrations.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Underfilled citrate (light-blue) tubes most threaten:",
        "Coagulation studies because the blood-to-anticoagulant ratio is wrong",
        [
            "Complete blood count indices only",
            "Urinalysis dipstick reading",
            "ABG analysis in a heparin syringe",
        ],
        "Citrate tubes must meet the manufacturer fill line for valid PT and aPTT results. "
        "GP41 volume requirements are part of preanalytic quality for coagulation testing.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "When a butterfly set is used for multiple tubes, maintaining flow helps:",
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
        "Time of collection on the label matters because:",
        "Reference ranges and stability calculations often depend on draw time",
        [
            "It is decorative information for the courier only",
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
        "If the wrong tube type was collected for an ordered test, the collector should:",
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
        "STAT specimens still require:",
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
        "Frozen aliquots for send-out testing should be:",
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
        "Wet ice versus gel packs for transport should be chosen based on:",
        "Laboratory instructions for the specific test and carrier design",
        [
            "Whichever is closest regardless of contamination risk",
            "Never using ice because all tests are room temperature",
            "Patient preference between wet and dry cooling",
        ],
        "Some specimens need wet ice; others tolerate insulated cool packs without free water exposure. "
        "GP41 transport sections defer to validated laboratory shipping methods.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Hand hygiene before handling filled collection tubes:",
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
        "Placing EDTA hematology tubes in direct contact with ice before CBC analysis:",
        "May cause cell morphology changes unless the manual requires chilling",
        [
            "Is always required for every complete blood count",
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
        "Batching multiple patients' specimens in one bag for courier pickup:",
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
        "Rechecking the requisition against collected tubes before leaving the patient helps:",
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
        "Delaying separation of plasma from cells in a heparin tube for ammonia-like assays:",
        "Can falsely change results as cells metabolize analytes",
        [
            "Only affects urine color without changing chemistry",
            "Improves accuracy by concentrating cells",
            "Is recommended for all routine electrolyte panels",
        ],
        "Cellular metabolism continues until centrifugation separates plasma. "
        "GP41 processing emphasizes prompt spin and aliquot for unstable plasma analytes.",
        _REF,
        "advanced",
    ),
]
