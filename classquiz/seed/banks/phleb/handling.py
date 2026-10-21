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
        "Patient identifiers, draw date-time, and collector ID per policy",
        [
            "Patient identifiers without collection date, time, or collector ID",
            "Tube color and additive type without patient name or medical record number",
            "Room and ward location without the required patient identifiers",
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
            "Vigorous shaking until foam appears on the blood sample",
            "Immediate centrifugation before manual mixing of additive tubes",
            "Horizontal storage without inverting EDTA or citrate tubes",
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
            "Immediate centrifugation without allowing clot formation to complete",
            "Eight to ten inversions followed by refrigeration before centrifugation",
            "Horizontal storage on ice while the clot forms inside the tube",
        ],
        "Complete clot formation allows fibrin to contract so serum separates cleanly during centrifugation. "
        "GP41-aligned processing follows the test manual for clot time, temperature, and validated spin settings.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Which centrifuge speed and spin time should staff use when separating serum or plasma for ordered tests?",
        "Validated RCF and spin time from the laboratory procedure manual for that test",
        [
            "Fastest rotor speed available without matching the test RCF requirement",
            "No centrifugation for outpatient chemistry specimens",
            "One default spin setting for all tube types without checking the manual",
        ],
        "Incorrect spin conditions leave residual cells in plasma or break gel barriers in serum separator tubes, altering analyte concentrations. "
        "CLSI-aligned laboratories document validated centrifuge protocols that collectors and processing staff must follow.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Which conditions must be maintained when transporting blood specimens from the collection site to the laboratory?",
        "Transport temperature and timing per the requisition or procedure manual",
        [
            "Transport in an uncooled vehicle trunk without documenting elapsed time",
            "Open caps to equalize ambient temperature during transit",
            "Ambient room temperature for all specimens without checking stability limits",
        ],
        "Stability windows differ for enzymes, blood gases, and cellular components, so universal transport rules do not apply. "
        "GP41 emphasizes delivering or storing specimens within defined preanalytic limits from collection through receipt.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What additional protection may be required when collecting or transporting specimens for light-sensitive analytes such as bilirubin?",
        "Amber wrap or light-blocking transport per the test manual",
        [
            "Routine fluorescent light exposure with no amber wrap when bilirubin is ordered",
            "Clear plastic bags so tube contents stay visible during transit",
            "One hour of room-light exposure before the specimen is analyzed",
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
            "Prothrombin time without false elevation of routine electrolytes",
            "Serum glucose on chemistry methods unaffected by the hemolysis index",
            "Platelet count on an EDTA hematology tube with hemolyzed plasma",
        ],
        "Lysed erythrocytes release intracellular potassium and enzymes into the fluid phase of the sample. "
        "Gentle draw technique, appropriate tube fill, and timely processing reduce hemolysis in line with GP41 quality goals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What is the appropriate response when hemolysis exceeds laboratory reject criteria for a potassium order?",
        "Specimen recollection per laboratory and provider policy",
        [
            "Reporting the numeric potassium result without a hemolysis comment",
            "Reporting the potassium with a hemolysis note while skipping laboratory recollect policy",
            "Citrate anticoagulant added from another tube to correct electrolytes",
        ],
        "Laboratories define hemolysis indices and reject rules so clinically misleading potassium values are not released silently. "
        "GP41 treats unacceptable preanalytic quality as grounds for redraw and documented communication rather than unqualified reporting.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Which documentation should accompany a fasting glucose specimen at the time of collection?",
        "Documented fasting status and collection time per preparation orders",
        [
            "Collection time documented without the patient's actual fasting status",
            "Meal history kept in nursing notes but omitted from the requisition",
            "Storage location on the label without fasting status or draw time",
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
            "Improved coagulation accuracy from delayed citrate tube processing",
            "Preanalytic effects limited to EDTA complete blood count specimens",
            "No preanalytic effect when tube labels are complete at collection",
        ],
        "Coagulation specimens remain time-sensitive even before centrifugation because factor activity changes with delay and temperature. "
        "GP41 stresses prompt transport and processing intervals defined in coagulation procedure manuals.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "What special handling do blood specimens for ammonia testing typically require?",
        "Prompt chilling and analysis within laboratory stability limits",
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
        "Gentle mixing, ice when required, and analysis within stability limits",
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
            "Routine complete blood counts collected in outpatient clinics",
            "Urine dipstick screenings for routine outpatient wellness visits",
            "Outpatient chemistry panels sent to reference labs without custody seals",
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
            "Uncapped tubes standing upright without secondary containment",
            "Non-specimen items mixed in the same carrier to reduce trips",
            "Maximum launch speed for chemistry panels without analyte-specific validation",
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
            "False glucose elevation without change in serum potassium",
            "Stable coagulation factor levels in uncentrifuged serum",
            "Complete serum separation without a centrifugation step",
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
        "Operator, QC, patient identifiers, and result for each patient test",
        [
            "Device serial number recorded without operator, QC, or patient linkage",
            "Random numeric codes substituted for patient identifiers",
            "Batch lot number logged once per shift without per-patient operator or result entries",
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
        "Limiting freeze-thaw on the primary sample when send-out testing requires splits",
        [
            "To remove secondary labeling requirements on split samples",
            "To replace centrifugation for downstream send-out tests",
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
        "Refrigeration when the procedure manual defines cold stability for that test",
        [
            "Identical refrigeration for all tube types without reading the test manual",
            "Avoidance of refrigeration in routine clinical laboratory workflows",
            "Courier arrival time used instead of analyte stability tables",
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
            "Stable analyte concentrations when capped tubes sit in direct summer sun",
            "Improved enzymatic stability for temperature-sensitive chemistry analytes",
            "Unchanged specimen quality when tube labels remain complete",
        ],
        "Heat accelerates in vitro metabolism and can hemolyze erythrocytes before the laboratory processes the sample. "
        "Insulated transport containers and validated summer collection protocols are part of GP41-aligned preanalytic programs.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Even when gray-top fluoride or oxalate tubes are used, what can still occur if centrifugation or laboratory processing is delayed beyond stability limits?",
        "Continued in vitro glycolysis that falsely lowers measured glucose",
        [
            "Stable plasma glucose for seventy-two hours at room temperature without timely centrifugation",
            "Complete inhibition of glycolysis the moment the gray tube is filled to the line",
            "False elevation of serum potassium from fluoride binding in the same collection tube",
        ],
        "Fluoride inhibits enolase but does not instantly stop all metabolism. "
        "GP41 still recommends timely delivery and processing per glucose stability tables.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Why does CLSI GP41 prohibit pouring or transferring blood between evacuated collection tubes after the draw?",
        "Additive carryover contaminates the destination tube and invalidates ordered assays",
        [
            "Pouring into an underfilled citrate tube restores the correct blood-to-anticoagulant ratio",
            "Cross-transfer affects culture bottles but not chemistry or coagulation vacuum tubes",
            "Transferring serum into a citrate tube shortens prothrombin time on underfilled specimens",
        ],
        "Each tube is filled directly from the patient with its intended additive load. "
        "GP41 order-of-draw and handling rules prohibit cross-transfer that would skew analyte concentrations.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What is the primary analytic risk when a light-blue sodium citrate tube is filled below the manufacturer fill line?",
        "Invalid coagulation results because the blood-to-anticoagulant ratio is incorrect",
        [
            "Falsely elevated hematology indices when the same underfilled tube is run on a CBC analyzer",
            "Distorted chemistry electrolytes when citrate plasma is spun from a partially filled tube",
            "Acceptable prothrombin time when the laboratory recentrifuges plasma from an underfilled tube",
        ],
        "Citrate tubes must meet the manufacturer fill line for valid PT and aPTT results. "
        "GP41 volume requirements are part of preanalytic quality for coagulation testing.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "When a butterfly infusion set is used to fill multiple vacuum tubes on one venipuncture, why should blood flow be kept continuous between tubes?",
        "To limit clot formation in the tubing and deliver adequate volume to each additive tube",
        [
            "To clamp the tubing between each tube until the hub stops oozing before advancing",
            "To pause flow for several minutes after each tube so air clears from the adapter",
            "To accept underfilled citrate and EDTA tubes rather than restarting the line",
        ],
        "Stasis in the line can activate coagulation and reduce volume delivered to additive tubes. "
        "GP41 multi-tube technique keeps the assembly patent until the last required tube is filled.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Why must collection date and time appear on the blood tube label according to GP41 preanalytic labeling standards?",
        "Reference intervals, stability windows, and timed tests are interpreted relative to draw time",
        [
            "Collection time is optional when accessioning scans a barcode at laboratory receipt",
            "Draw time is required for therapeutic drug monitoring but not for routine chemistry panels",
            "Stat specimens may omit tube draw time when the requisition lists the order time",
        ],
        "Therapeutic drug monitoring and timed tests interpret results relative to dose and fasting clocks. "
        "GP41 labeling standards include collection date and time for preanalytic traceability.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "If the wrong tube type was collected for an ordered test, what should the phlebotomist do according to preanalytic error policy?",
        "Notify the laboratory and follow facility policy for recollection or approved add-on testing",
        [
            "Pour the specimen into the correct tube type without documenting the error",
            "Send the mismatched tube frozen and expect the laboratory to validate the assay",
            "Discard the tubes and cancel the order without notifying the patient or provider",
        ],
        "Incompatible additives cannot be corrected by transferring specimen after the fact. "
        "GP41 error management emphasizes disclosure and redraw when sample type invalidates the assay.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Which preanalytic requirements apply to STAT blood specimens despite the urgency of the order?",
        "The same patient identification, complete labeling, and stability handling as routine collections",
        [
            "Abbreviated labeling with patient name only when the requisition carries a barcode",
            "Relaxed transport temperature limits because the test is marked stat on the order",
            "Use of prelabeled tubes prepared for the next scheduled patient to shorten draw time",
        ],
        "Urgency does not waive patient safety or preanalytic quality controls. "
        "GP41 prioritizes rapid transport while maintaining complete labels and stability requirements.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "How should serum or plasma aliquots destined for send-out testing be frozen, stored, and thawed?",
        "Per the test procedure manual using validated containers, freezer conditions, and one-time thaw steps",
        [
            "Frozen in the primary lavender EDTA tube without centrifuging when the manual requires separation",
            "Thawed and refrozen at room temperature between reference-lab shipments without a limit",
            "Held at room temperature until courier pickup when no on-site freezer is immediately available",
        ],
        "Incorrect freeze-thaw handling destroys labile analytes. "
        "Laboratory manuals aligned with GP41 define when to spin, separate, and freeze specific tests.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "When packaging blood specimens for courier transport, how should staff choose between wet ice and insulated gel packs?",
        "According to laboratory shipping instructions for the ordered tests and the approved carrier design",
        [
            "Use whichever cold pack is stocked nearest the draw station that shift",
            "Use gel packs for all chemistry specimens because wet ice is prohibited in the lab",
            "Use crushed dry ice for routine outpatient chemistry panels without checking stability tables",
        ],
        "Some specimens need wet ice; others tolerate insulated cool packs without free water exposure. "
        "GP41 transport sections defer to validated laboratory shipping methods.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "Why is hand hygiene required before handling filled collection tubes after venipuncture?",
        "It reduces cross-contamination of tubes, forms, and transport carriers after patient contact",
        [
            "It is unnecessary when clean examination gloves were worn throughout the venipuncture",
            "It replaces bedside labeling when the collector will transport tubes immediately",
            "It may be deferred on stat specimens until after the pneumatic tube launch",
        ],
        "Gloves protect during venipuncture but hands may contact contaminated surfaces afterward. "
        "GP41 infection prevention includes hand hygiene when moving from patient care to paperwork and transport.",
        [S.CLSI_GP41, S.CDC_HAND_HYGIENE, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-handling",
        "What can happen when lavender EDTA tubes for hematology are transported on direct wet ice before CBC analysis?",
        "Altered red-cell morphology and indices unless the test manual specifies cold transport",
        [
            "Improved platelet clumping control on every complete blood count before analysis",
            "Prevention of clot formation in serum separator tubes during the same courier bag",
            "Elimination of the need for gentle inversion mixing immediately after collection",
        ],
        "Cold can affect MCV and other indices on some analyzers. "
        "Unless the test manual specifies cold transport, GP41 default is room temperature delivery within stability limits.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-handling",
        "When multiple patients' specimens are batched in one courier bag, which packaging rules still apply?",
        "Each container remains individually labeled with leak-proof secondary segregation per policy",
        [
            "Patient labels may be removed inside the shared bag when tube colors differ",
            "Serum, plasma, and urine from different patients may share one open pouch",
            "Temperature monitors and ice requirements do not apply once specimens are batched together",
        ],
        "Batch transport still demands patient-specific identification on every container. "
        "GP41 traceability extends through courier handoff with leak-proof secondary containment.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-handling",
        "Why should staff reconcile the requisition against collected tubes before leaving the patient?",
        "To catch missing tubes, wrong tests, or tube-type errors before the patient leaves the care area",
        [
            "To substitute for two-identifier verification when the patient confirms their name aloud",
            "To bypass laboratory accessioning when every ordered tube color is present in the carrier",
            "To permit unlabeled tubes when the number of tubes matches the requisition line count",
        ],
        "A brief reconciliation reduces callbacks and repeat venipunctures. "
        "GP41 quality practices combine identification, order match, and correct tube type at the bedside.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-handling",
        "Why is delaying plasma separation from cells in a heparin or green-top tube problematic for ammonia and similar unstable assays?",
        "Cellular metabolism in whole blood falsely changes plasma analyte concentrations before analysis",
        [
            "Delay affects urine color on paired specimens but not plasma chemistry concentrations",
            "Prolonged contact with cells improves ammonia accuracy by concentrating erythrocyte metabolites",
            "Delayed spin is acceptable for routine electrolyte panels when the tube remains capped",
        ],
        "Cellular metabolism continues until centrifugation separates plasma. "
        "GP41 processing emphasizes prompt spin and aliquot for unstable plasma analytes.",
        _REF,
        "advanced",
    ),
]
