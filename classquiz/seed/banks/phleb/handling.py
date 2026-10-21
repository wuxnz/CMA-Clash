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
        "Which elements must appear on a blood collection tube label at the time of draw according to standard preanalytic practice?",
        "Patient identifiers, date and time of collection, and collector identification as defined by policy",
        [
            "Patient identifiers without date, time, or collector information",
            "Tube color and stopper type without patient name or medical record number",
            "Room number and ward location without required patient identifiers",
        ],
        "Complete labels tie each tube to the correct patient and collection event for accessioning and reporting. "
        "CLSI GP41 preanalytic requirements align with accreditation standards that mandate traceability from bedside to result.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How should evacuated tubes containing EDTA or sodium citrate be mixed immediately after collection?",
        "Gentle end-over-end inversion per the tube manufacturer's instructions",
        [
            "Vigorous shaking for thirty seconds until the sample froths",
            "Immediate centrifugation before any manual mixing occurs",
            "Horizontal storage without inversion of additive tubes",
        ],
        "Proper inversion distributes anticoagulant throughout the sample without hemolyzing cells. "
        "Over-mixing or skipping inversion promotes clots and microclots that invalidate hematology and coagulation results.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What processing step do serum separator tubes for routine chemistry often require before centrifugation?",
        "Upright clotting for the laboratory-defined interval",
        [
            "Immediate freezing while the sample remains completely liquid",
            "Heating to body temperature in a microwave oven",
            "Dilution with normal saline to the manufacturer fill line",
        ],
        "Complete clot formation allows fibrin to contract so serum separates cleanly during centrifugation. "
        "GP41-aligned processing follows the test manual for clot time, temperature, and validated spin settings.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Which centrifuge speed and spin time should staff use when separating serum or plasma for ordered tests?",
        "The validated speed and duration specified in the laboratory procedure manual for each test",
        [
            "The fastest available rotor setting regardless of relative centrifugal force",
            "No centrifugation for any outpatient chemistry specimen",
            "A single default spin time applied to every tube type without consulting the manual",
        ],
        "Incorrect spin conditions leave residual cells in plasma or break gel barriers in serum separator tubes, altering analyte concentrations. "
        "CLSI-aligned laboratories document validated centrifuge protocols that collectors and processing staff must follow.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Which conditions must be maintained when transporting blood specimens from the collection site to the laboratory?",
        "Temperature and timing limits listed on the test requisition or in the procedure manual",
        [
            "Direct sunlight exposure to prevent condensation on tube exteriors",
            "Open caps to equalize ambient temperature during transit",
            "Room temperature storage for every specimen regardless of analyte stability",
        ],
        "Stability windows differ for enzymes, blood gases, and cellular components, so universal transport rules do not apply. "
        "GP41 emphasizes delivering or storing specimens within defined preanalytic limits from collection through receipt.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What additional protection may be required when collecting or transporting specimens for light-sensitive analytes such as bilirubin?",
        "Amber wrap or transport inside a light-blocking container per the test manual",
        [
            "Deliberate UV light exposure to stabilize pigment concentration",
            "Clear plastic bags only so contents remain visible in transit",
            "Prolonged room-light exposure for at least one hour before analysis",
        ],
        "Photo-degradation can falsely lower measured concentrations before the specimen reaches the analyzer. "
        "Laboratory procedure manuals specify light protection that GP41-compliant workflows apply at collection or handoff.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Which chemistry analytes are commonly falsely elevated when visible hemolysis is present in serum or plasma?",
        "Potassium and several intracellular enzymes released from lysed red cells",
        [
            "Prothrombin time only, without effect on electrolyte panels",
            "Glucose on every chemistry method regardless of hemolysis index",
            "Platelet count on an EDTA hematology specimen only",
        ],
        "Lysed erythrocytes release intracellular potassium and enzymes into the fluid phase of the sample. "
        "Gentle draw technique, appropriate tube fill, and timely processing reduce hemolysis in line with GP41 quality goals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What is the appropriate response when hemolysis exceeds laboratory reject criteria for a potassium order?",
        "Recollection of the specimen according to laboratory and provider policy",
        [
            "Reporting the numeric result without a hemolysis comment to save time",
            "Diluting the sample with saline to mask the hemolysis index",
            "Adding citrate anticoagulant from another tube to correct electrolytes",
        ],
        "Laboratories define hemolysis indices and reject rules so clinically misleading potassium values are not released silently. "
        "GP41 treats unacceptable preanalytic quality as grounds for redraw and documented communication rather than unqualified reporting.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Which documentation should accompany a fasting glucose specimen at the time of collection?",
        "Fasting status and collection time relative to the ordered preparation instructions",
        [
            "Collection time without documentation of actual fasting status",
            "Meal history recorded only in nursing notes, not on the requisition or label",
            "A label listing storage location but omitting fasting status and draw time",
        ],
        "Reference intervals and diagnostic thresholds for glucose depend on whether the patient met the ordered fasting interval. "
        "GP41 preanalytic data include patient preparation, timing, and collection details that support correct interpretation.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How must single-use capillary puncture devices and lancets be handled after patient use?",
        "Discarded immediately into an approved sharps container after one patient",
        [
            "Wiped with alcohol and stored for reuse on the next patient",
            "Placed in a general waste bin if the device appears clean",
            "Left uncapped on the work surface between successive patient collections",
        ],
        "Reusing skin puncture devices violates standard precautions and creates bloodborne pathogen exposure risk. "
        "OSHA bloodborne pathogen standards and GP41 infection-control expectations require immediate disposal after a single patient use.",
        _REF_BBP,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What preanalytic problem can delayed delivery or processing of sodium citrate coagulation tubes cause?",
        "Altered factor activity that falsely prolongs or shortens clotting assay results",
        [
            "Improved accuracy from prolonged clot formation inside citrate tubes",
            "Effects limited to complete blood counts collected in EDTA",
            "No preanalytic impact when collection tubes carry complete labels",
        ],
        "Coagulation specimens remain time-sensitive even before centrifugation because factor activity changes with delay and temperature. "
        "GP41 stresses prompt transport and processing intervals defined in coagulation procedure manuals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What special handling do blood specimens for ammonia testing typically require?",
        "Prompt chilling and analysis within strict stability limits defined by the laboratory",
        [
            "Overnight storage at room temperature on the nursing unit",
            "Freezing in an unvalidated household freezer without laboratory protocol",
            "Room-air exposure with the cap removed to allow gas equilibration",
        ],
        "Plasma ammonia rises rapidly as blood metabolizes at room temperature, producing falsely elevated results. "
        "Laboratory procedures aligned with GP41 specify ice transport, minimal delay, and validated processing before analysis.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Which collection and processing requirements apply to blood lactate specimens?",
        "Approved collection devices and immediate processing per the test procedure manual",
        [
            "Routine serum separator tubes clotting upright for several hours",
            "Capillary blood collected into citrate coagulation tubes without order verification",
            "Extended room-temperature holding because delayed spin does not affect lactate",
        ],
        "Continued glycolysis and cellular metabolism falsely lower measured lactate when processing is delayed. "
        "GP41 defers to laboratory-defined devices, tourniquet time limits, and spin requirements specific to lactate orders.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Which handling steps are required immediately after arterial blood gas specimen collection?",
        "Gentle mixing, ice transport when specified, and analysis within stability limits",
        [
            "Upright clotting like a routine serum chemistry tube",
            "Storage in a vaccine refrigerator without mixing the syringe",
            "Leaving the syringe uncapped to balance dissolved oxygen with room air",
        ],
        "Air bubbles and processing delay change pO2, pCO2, and pH values before analysis. "
        "GP41 and arterial blood gas procedure manuals require rapid transport, gentle mixing, and exclusion of air from the sample.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "For which type of specimen is formal chain-of-custody documentation required?",
        "Forensic or legal specimens for which possession must remain traceable",
        [
            "Every routine complete blood count collected in outpatient clinics",
            "All urine dipstick screenings regardless of clinical purpose",
            "Internal laboratory staff scheduling and shift assignment records",
        ],
        "Each transfer of a legal specimen is logged with seals, signatures, and continuity of possession. "
        "Routine clinical chemistry does not use chain-of-custody forms unless the order specifies forensic or legal analysis.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Which steps should staff take when a blood tube shatters inside a centrifuge during a spin?",
        "Stop the rotor, don appropriate PPE, and follow biohazard spill cleanup protocol",
        [
            "Reach into the rotor while it is still decelerating to remove glass",
            "Wipe broken shards with bare hands to minimize equipment downtime",
            "Ignore potential aerosols if the centrifuge lid appears intact",
        ],
        "Broken glass and blood aerosols create sharps injury and bloodborne pathogen exposure risk. "
        "GP41 and OSHA bloodborne pathogen procedures govern safe cleanup and inspection before the centrifuge returns to service.",
        _REF_BBP,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "How should blood specimens be packaged for transport through an approved pneumatic tube system?",
        "In leak-proof padded carriers validated by the laboratory for fragile tests",
        [
            "As uncapped tubes standing upright without secondary containment",
            "Mixed with non-specimen items in the same carrier to reduce trips",
            "At maximum launch speed for every chemistry panel regardless of analyte",
        ],
        "Acceleration and deceleration during tube-system transport can hemolyze cells or disrupt gel barriers in separator tubes. "
        "Laboratories validate which tests may use pneumatic carriers under GP41 transport quality standards.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What analytical problem can result from holding serum at room temperature too long before centrifugation?",
        "Falsely elevated potassium as red cells leak intracellular contents",
        [
            "Changes confined to glucose without any effect on electrolytes",
            "Improved stability of coagulation factors in serum",
            "Elimination of the need for any centrifugation step",
        ],
        "Cellular metabolism and passive leakage continue until centrifugation separates serum from clot or cells. "
        "GP41 processing timelines specify maximum pre-centrifuge delay for serum electrolytes and related analytes.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What action is required when the laboratory identifies a critical (panic) test value?",
        "Immediate notification of the responsible clinician per documented protocol",
        [
            "Batching critical results for monthly summary distribution",
            "Posting values on a public waiting-room display board",
            "Deferring notification because a repeat draw may occur later",
        ],
        "Timely communication enables treatment for life-threatening abnormalities before the patient leaves the care setting. "
        "Accreditation standards and GP41 quality systems define read-back, documentation, and escalation for critical result calls.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What must outbound courier pickup of patient specimens ensure before handoff?",
        "Secure leak-proof packaging with required temperature monitors or ice when indicated",
        [
            "Open tubes grouped in an unlabeled plastic bag for speed",
            "Delay beyond published stability limits without notifying the laboratory",
            "Pooling multiple patients' specimens in one container to save space",
        ],
        "Courier transport extends the preanalytic phase, so temperature and timing must match test stability tables. "
        "GP41 transport guidance applies from bedside collection through verified laboratory receipt.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Which elements should point-of-care testing logs record for each patient test?",
        "Operator identity, quality control results, patient identifiers, and test results",
        [
            "Ambient outdoor temperature at the time of testing only",
            "Random numeric codes instead of patient identifiers",
            "Equipment serial number without operator, QC, or patient linkage",
        ],
        "CLIA-waived and moderate-complexity point-of-care programs require traceable documentation for every patient result. "
        "GP41-aligned POC workflows integrate device quality control with patient identification and recorded outcomes.",
        _REF_POC,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What should staff do when a specimen container breaks during transit to the laboratory?",
        "Notify the laboratory, document the incident, and recollect when policy requires",
        [
            "Tape broken glass together and submit the specimen without comment",
            "Relabel unknown fragments using the next patient in the draw queue",
            "Conceal container damage to avoid delaying result reporting",
        ],
        "Compromised containers risk exposure to bloodborne pathogens and produce uninterpretable or contaminated results. "
        "GP41 incident management includes safe cleanup, laboratory notification, and documented decisions about recollection.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Why do laboratories aliquot serum or plasma into secondary tubes after primary centrifugation?",
        "To avoid repeated freeze-thaw cycles on the primary sample when send-out testing requires it",
        [
            "To eliminate all secondary labeling requirements on split samples",
            "To replace centrifugation for every downstream test permanently",
            "To transfer additives between incompatible primary tube types",
        ],
        "Separate aliquots preserve labile analytes when reference laboratories require frozen or split material. "
        "Each aliquot still requires full patient identification and traceability under GP41 labeling rules.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "When should collected blood specimens be placed in refrigerated storage after collection?",
        "Only for tests with defined cold stability in the laboratory procedure manual",
        [
            "For every tube type identically without reading the test manual",
            "Never under any circumstances in a clinical laboratory workflow",
            "Based solely on courier arrival time rather than analyte stability tables",
        ],
        "Some analytes require refrigeration after collection; others must remain at room temperature to avoid false results. "
        "GP41 directs collectors to follow test-specific stability guidance rather than applying one temperature rule to all tubes.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What preanalytic damage can occur when blood tubes are exposed to extreme heat during summer transport?",
        "Red cell lysis and degradation of temperature-labile analytes",
        [
            "Automatic internal refrigeration within the evacuated tube",
            "Improved enzymatic stability for all chemistry analytes",
            "No change in specimen quality when tubes remain correctly labeled",
        ],
        "Heat accelerates in vitro metabolism and can hemolyze erythrocytes before the laboratory processes the sample. "
        "Insulated transport containers and validated summer collection protocols are part of GP41-aligned preanalytic programs.",
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
        "What underfilled citrate (light-blue) tubes most threaten what results?",
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
        "When a butterfly set is used for multiple tubes, maintaining flow helps?",
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
        "Why time of collection on the label matters for what reason?",
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
        "If the wrong tube type was collected for an ordered test, the collector should?",
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
        "What rechecking the requisition against collected tubes before leaving the patient helps how?",
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
