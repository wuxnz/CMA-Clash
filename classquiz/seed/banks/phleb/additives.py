# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored tube additive and specimen-type questions (topic phleb-additives)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    fact(
        "phleb-additives",
        "Which anticoagulant is inside a standard lavender-top vacuum tube used for most complete blood counts?",
        "Potassium EDTA (K2EDTA or K3EDTA)",
        [
            "Sodium citrate for coagulation testing",
            "Lithium heparin for plasma chemistry",
            "Sodium fluoride with potassium oxalate",
        ],
        "EDTA chelates calcium to keep whole blood fluid while preserving cell morphology for hematology. "
        "Citrate, heparin, and fluoride tubes serve other disciplines and will not yield a valid automated CBC.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "Which anticoagulant is in light blue-top vacuum tubes collected for prothrombin time and related coagulation studies?",
        "Sodium citrate",
        [
            "Potassium EDTA for hematology",
            "Lithium heparin for plasma electrolytes",
            "Potassium oxalate without sodium fluoride",
        ],
        "Citrate binds calcium so plasma stays fluid for PT, INR, and other clotting assays. "
        "Substituting lavender EDTA or green heparin invalidates coagulation results on most platforms.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "Which additive is typically present in green-top vacuum tubes used for selected plasma chemistry assays?",
        "Lithium or sodium heparin",
        [
            "Potassium EDTA for cell counts",
            "Sodium citrate for prothrombin time",
            "Sodium fluoride and potassium oxalate for glucose",
        ],
        "Heparin potentiates antithrombin to inhibit thrombin and factor Xa, yielding plasma for method-validated tests. "
        "Green and light blue tubes both anticoagulate blood, but they are not interchangeable on the requisition.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "Which additives are commonly combined in gray-top tubes used to preserve glucose during transport delay?",
        "Sodium fluoride with potassium oxalate",
        [
            "Sodium citrate alone for coagulation ratios",
            "Clot activator and inert gel separator",
            "Liquid broth media for organism growth",
        ],
        "Fluoride inhibits enolase to slow in vitro glycolysis while oxalate anticoagulates for plasma glucose testing. "
        "Citrate or serum separator tubes do not provide equivalent glucose stabilization.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "How does a plain red-top tube without gel or separator differ from lavender EDTA tubes?",
        "It contains no anticoagulant; blood clots so serum can be collected after centrifugation",
        [
            "It contains EDTA to preserve platelets for hematology",
            "It contains sodium citrate for INR testing",
            "It contains heparin for immediate plasma electrolytes",
        ],
        "Routine chemistry methods often require serum free of EDTA interference. "
        "Collecting a chemistry panel in lavender whole blood is a common certification error unless the lab validates plasma.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "Which additives are present in gold speckled serum separator (SST) vacuum tubes?",
        "Clot activator plus an inert gel barrier that forms after centrifugation",
        [
            "Potassium EDTA anticoagulant for hematology",
            "Sodium citrate for coagulation studies",
            "Sodium fluoride to inhibit bacterial metabolism",
        ],
        "The gel physically separates serum from cells during storage and transport after clotting. "
        "EDTA or citrate would prevent the clot formation SST processing requires.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "Which evacuated tube is the standard choice for an automated complete blood count with differential?",
        "Lavender-top potassium EDTA",
        [
            "Light blue sodium citrate for coagulation",
            "Green-top lithium heparin for plasma",
            "Plain red-top tube without anticoagulant",
        ],
        "Hematology analyzers expect EDTA-anticoagulated whole blood with intact cell morphology. "
        "Citrate dilutes the specimen for ratio-controlled coagulation testing; clotted red-top blood is not a routine CBC source.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "For a prothrombin time with INR, which collection container meets CLSI ratio requirements?",
        "Light blue sodium citrate tube filled to the manufacturer volume line",
        [
            "Lavender potassium EDTA whole-blood tube",
            "Green lithium heparin plasma tube",
            "Gray sodium fluoride tube for glucose preservation",
        ],
        "PT and INR require citrated plasma at the validated blood-to-anticoagulant ratio. "
        "EDTA and heparin interfere with clotting assays; gray fluoride tubes stabilize glucose, not coagulation factors.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "The laboratory orders plasma glucose with possible transport delay. Which tube additive best limits in vitro glycolysis?",
        "Sodium fluoride in a gray-top tube, often paired with potassium oxalate",
        [
            "Sodium citrate in a light blue-top tube",
            "Clot activator in a plain red-top tube",
            "Broth media in a blood culture bottle",
        ],
        "Fluoride inhibits enolase, slowing glucose consumption by cells and bacteria after collection. "
        "Serum from red tops or citrate plasma lacks the same glycolysis protection unless the method specifies otherwise.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "How do sterile blood culture bottles differ from routine additive vacuum tubes in purpose and contents?",
        "They contain liquid growth media for aerobic or anaerobic organisms, not routine chemistry anticoagulants",
        [
            "They contain EDTA to keep blood fluid during incubation",
            "They contain fluoride primarily to preserve glucose in cultures",
            "They contain gel separator to isolate bacteria after spin",
        ],
        "Culture systems nourish microbes under sterile technique; vacuum tube additives do not replace broth bottles. "
        "Treating culture bottles like another color-coded chemistry tube risks contamination and false-positive results.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "After clotting and centrifugation when required, serum for many chemistry panels is obtained from which tubes?",
        "Plain red-top or gold serum separator (SST) tubes",
        [
            "Lavender EDTA whole blood without processing",
            "Light blue citrate plasma drawn straight to the lab",
            "Blood culture bottles after incubator growth",
        ],
        "Many chemistry methods require serum without EDTA chelation of calcium and other analytes. "
        "Lavender whole blood supports hematology; citrate plasma is reserved for coagulation unless the lab directs otherwise.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "Under what condition may electrolytes be measured on heparinized plasma from a green-top tube?",
        "The laboratory method and reference intervals are validated for heparinized plasma",
        [
            "Green tubes may replace serum for every chemistry test on the menu",
            "Prothrombin time and INR may run on the same heparin specimen",
            "Blood cultures may be inoculated from leftover green-top plasma",
        ],
        "Heparinized plasma is acceptable only when the assay and reporting range are validated for that matrix. "
        "Coagulation studies require citrate; assuming tube interchangeability ignores CLSI preanalytic requirements.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "Which anticoagulant is in pink-top EDTA tubes used for blood bank immunohematology collections?",
        "Potassium EDTA (K2EDTA) per blood bank standard operating procedure",
        [
            "Sodium citrate dedicated to crossmatch plasma",
            "Lithium heparin for ABO forward typing",
            "Sodium fluoride for antibody screen stability",
        ],
        "Pink tops remain EDTA whole blood but may follow a different testing pathway than routine lavender CBC tubes. "
        "Citrate or heparin would break immunohematology protocols that require EDTA-preserved cells and plasma.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "By which mechanism does sodium citrate in light blue tubes prevent clotting?",
        "Binding ionized calcium required for coagulation factor activation",
        [
            "Lysing erythrocytes to release stored calcium into plasma",
            "Activating platelets to accelerate fibrin polymerization",
            "Inhibiting enolase the same way sodium fluoride does",
        ],
        "Calcium binding keeps citrated plasma fluid for PT and aPTT. "
        "Confusing citrate with fluoride's enolase block mixes coagulation testing with glucose preservation roles.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "Why is EDTA anticoagulation preferred for hematology cell counts and differentials?",
        "It chelates calcium to prevent clotting while preserving red cell and leukocyte morphology",
        [
            "It accelerates fibrin formation so serum separates quickly",
            "It neutralizes therapeutic heparin already in the patient's circulation",
            "It stabilizes glucose for days without sodium fluoride",
        ],
        "Morphology and accurate differentials require fluid whole blood without fibrin trapping cells. "
        "EDTA does not replace fluoride for glucose stability or reverse patient anticoagulant therapy.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "How does heparin in green-top tubes prevent clot formation?",
        "It enhances antithrombin III inhibition of thrombin and factor Xa",
        [
            "It chelates calcium ions the way sodium citrate does",
            "It activates thrombin to polymerize fibrin into serum",
            "It precipitates fibrinogen with potassium oxalate",
        ],
        "Heparin's antithrombin-mediated effect differs from calcium chelation or oxalate precipitation. "
        "Mechanism distinctions between green, blue, and gray additives appear frequently on certification exams.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "How does sodium fluoride in gray-top tubes help stabilize measured glucose after collection?",
        "It inhibits enolase, slowing glycolytic consumption of glucose in vitro",
        [
            "It binds calcium to keep plasma fluid like sodium citrate",
            "It sterilizes the specimen so culture bacteria cannot metabolize glucose",
            "It forms a gel barrier between cells and plasma after centrifugation",
        ],
        "Enolase inhibition slows the post-draw glucose drop in gray tubes; calcium binding belongs to oxalate and citrate. "
        "Gel separators address serum separation, not glycolysis in fluoride-anticoagulated whole blood.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "What anticoagulant role does potassium oxalate play in many gray-top glucose tubes?",
        "It precipitates calcium as calcium oxalate so blood cannot clot",
        [
            "It activates factor VII to shorten clotting time",
            "It chelates iron so erythrocytes lyse for hematology",
            "It neutralizes EDTA carried over from an earlier tube",
        ],
        "Oxalate removes free calcium and complements fluoride for plasma glucose specimens. "
        "Factor activation would promote clotting—the opposite of the gray tube's anticoagulant purpose.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "After centrifugation, what is the primary function of the gel in serum separator tubes?",
        "Form a physical barrier between serum and cells during storage and transport",
        [
            "Chelate calcium the way potassium EDTA does in lavender tubes",
            "Replace broth media to prevent bacterial growth in the tube",
            "Convert residual heparin into sodium citrate for coagulation testing",
        ],
        "The inert gel reduces cell leakage into serum during handling; it is not an anticoagulant chemical. "
        "Expecting gel to sterilize specimens or alter coagulation confuses SST tubes with culture systems.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "Which anticoagulant coating is standard on arterial blood gas syringes used for pH and blood gas analysis?",
        "Balanced dry or liquid heparin matched to the syringe volume",
        [
            "Potassium EDTA to preserve erythrocyte morphology",
            "Sodium fluoride without heparin for electrolyte stability",
            "No anticoagulant because ABG specimens must clot first",
        ],
        "Balanced heparin prevents clotting without excessive dilution that would skew pO2, pCO2, and electrolytes. "
        "EDTA is unsuitable for blood gas measurements; uncoated syringes would clot before analysis.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "A light blue citrate tube arrives underfilled below the fill line. Why are coagulation results unreliable?",
        "Excess citrate relative to blood distorts the required approximately 9:1 blood-to-anticoagulant ratio",
        [
            "Underfill automatically introduces EDTA from the needle hub",
            "Sodium fluoride evaporates from citrate tubes that are not full",
            "Serum separator gel migrates into citrate when volume is low",
        ],
        "Too much anticoagulant for the blood volume prolongs clotting times on PT and aPTT. "
        "The primary failure is ratio distortion, not fluoride loss or gel contamination in a properly collected citrate tube.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "A lavender EDTA tube with visible clot is submitted for an automated platelet count. What result pattern is likely?",
        "Falsely decreased platelets because clots trap platelets and block the analyzer",
        [
            "Falsely increased platelets from sodium fluoride in the lavender stopper",
            "Accurate counts if the tube was refrigerated overnight before testing",
            "Unchanged counts when the bedside label matches the requisition",
        ],
        "Platelets aggregate in fibrin clots and may be undercounted or flagged as clumps. "
        "Refrigeration does not reverse clotting; fluoride is not the additive in lavender hematology tubes.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "Lavender EDTA was drawn before serum tubes on the same stick. Which chemistry results may be falsely affected on serum?",
        "Depressed calcium and sometimes alkaline phosphatase from EDTA chelation carryover",
        [
            "Elevated INR measured on the same serum aliquot",
            "Elevated glucose from EDTA inhibiting glycolysis like fluoride",
            "Improved blood culture yield from EDTA in the chemistry tube",
        ],
        "EDTA carryover removes measurable ionized and total calcium on many chemistry platforms. "
        "INR requires citrate plasma; EDTA does not mimic fluoride's enolase inhibition for glucose.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "What is the main practical difference between K2EDTA and K3EDTA in lavender hematology tubes?",
        "They are different potassium salt forms of EDTA, slightly changing specimen dilution for hematocrit",
        [
            "K2EDTA is for coagulation testing and K3EDTA is for glucose preservation",
            "K3EDTA is the citrate salt used in light blue prothrombin tubes",
            "K2EDTA contains lithium heparin for plasma chemistry",
        ],
        "Both forms chelate calcium for hematology; the salt form nudges dilution enough to matter on hematocrit. "
        "Assigning coagulation or glucose roles to K2 versus K3 confuses distinct anticoagulant families.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "What is the purpose of clot activator beads or powder in plain red-top and SST tubes?",
        "Accelerate fibrin clot formation so serum can be separated after incubation and centrifugation",
        [
            "Provide permanent anticoagulation comparable to lithium heparin",
            "Suppress platelet clumping for automated CBC differentials",
            "Maintain sterile conditions equivalent to blood culture broth",
        ],
        "Clot activators shorten the clotting phase for serum chemistry; they do not anticoagulate like heparin or preserve cells like EDTA. "
        "Culture sterility requires dedicated sterile bottle systems, not chemistry tube additives.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'What ammonia testing often requires what?',
        'A laboratory-specified tube, immediate chilling, and rapid transport/processing',
        [
            'Any lavender tube stored at room temperature for 24 hours',
            'Fluoride gray tube without ice because fluoride fixes ammonia',
            'Culture media to prevent ammonia loss',
        ],
        'Ammonia is volatile and labile; arbitrary EDTA room-temperature storage yields falsely low or high results. Fluoride gray is for glucose, not a universal ammonia substitute without lab validation.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'What erythrocyte sedimentation rate (ESR) kits may use what anticoagulant?',
        'Citrate-diluted blood per manufacturer rather than a standard lavender EDTA tube',
        [
            'Serum separator gel tubes exclusively',
            'Fluoride gray tubes for all ESR methods',
            'Plain red-top serum without dilution',
        ],
        'ESR methods are instrument-specific; citrate dilution is common on Westergren systems. Assuming any CBC tube works ignores manufacturer requirements cited in CLSI preanalytics.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'What special handling do therapeutic drug monitoring specimens require?',
        'The exact serum, plasma, or whole blood tube and timing (peak/trough) defined by the laboratory',
        [
            'Any green tube because heparin is universal for drugs',
            'Urine cups for all oral medications',
            'Culture bottles to prevent drug metabolism',
        ],
        'Drug assays vary by matrix; heparin plasma is not universal. Urine or culture containers do not replace validated blood collection tubes for TDM.',
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'Which laboratory values does hemolysis during collection most often artifactually elevate?',
        'Potassium and lactate dehydrogenase among other intracellular analytes',
        [
            'Sodium due to EDTA chelation',
            'INR on a properly filled citrate tube without carryover',
            'Blood culture time-to-positivity solely from hemolysis',
        ],
        'Red cell rupture spills K+ and LDH; sodium changes are not the classic hemolysis pattern. INR rises from ratio or heparin problems, not hemolysis alone in isolation.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'What rapid serum tubes (e.g., thrombin-based orange or speckled variants) achieve clotting by what mechanism?',
        'Adding thrombin or similar clot activator to shorten serum formation time',
        [
            'Adding EDTA to stabilize clot',
            'Using fluoride to clot blood rapidly',
            'Removing all calcium with citrate',
        ],
        'Thrombin accelerates clotting for rapid serum chemistry; EDTA or citrate would prevent the clot needed. Fluoride does not clot specimens, it inhibits enzymes.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'A provider orders ionized calcium, but the only tube on the tray is lavender EDTA. Why must the phlebotomist obtain a different tube before sticking the patient?',
        'EDTA chelates calcium and makes ionized and total calcium results uninterpretable on that specimen',
        [
            'EDTA only affects sodium levels',
            'Ionized calcium requires fluoride gray tubes exclusively',
            'Lavender is preferred for all electrolytes',
        ],
        'Chelation binds calcium in vitro; no amount of mixing restores physiologic ionized calcium. Gray fluoride does not undo EDTA binding, proper tubeless serum or specific ionized calcium tube is required.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'The laboratory validates electrolytes on lithium heparin plasma but potassium returns markedly elevated with a hemolysis index. Which preanalytic issue is most likely despite the correct tube additive?',
        'Traumatic draw, prolonged tourniquet, or vigorous mixing hemolyzed cells even though heparin anticoagulation was correct',
        [
            'Wrong anticoagulant, heparin always raises potassium without hemolysis',
            'Citrate carryover from drawing blue after green',
            'Fluoride inhibition falsely increasing potassium',
        ],
        'Hemolysis releases intracellular potassium; correct heparin cannot neutralize lysed cells. Blaming heparin chemistry or fluoride ignores the hemolysis flag tying to collection trauma.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "A warfarin patient's citrate tube arrives at 50% fill after a difficult draw. What should the coagulation technologist do?",
        'Reject the specimen for ratio error and request recollection before reporting INR',
        [
            'Report INR after multiplying by a fixed correction factor',
            'Dilute with more citrate to reach the line',
            'Run the test on heparin plasma instead',
        ],
        'There is no valid correction factor for half-filled citrate under CLSI coagulation standards. Adding citrate or switching to heparin plasma changes the assay matrix entirely.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A patient on IV heparin has an aPTT drawn in a blue citrate tube while heparin is infusing in the same arm. Which interpretation concern is most important?',
        'Venous specimen may contain therapeutic heparin, prolonging aPTT independent of tube additive ratio',
        [
            'Citrate will neutralize all circulating heparin',
            'EDTA tube is required to cancel heparin effect',
            'Fluoride gray must be drawn first to bind heparin',
        ],
        'Tube citrate does not remove systemic anticoagulant; arm with infusion contaminates results. Switching to EDTA or fluoride does not solve arm-selection contamination.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A gray fluoride/oxalate tube is collected for fasting glucose, but the patient also needs a plasma lactate on the same visit. The phlebotomist should?',
        'Consult the laboratory manual, lactate often needs a separate sodium fluoride tube without oxalate or a specific preservative tube, not assume one gray tube serves both',
        [
            'Use the same gray tube because fluoride stabilizes all substrates',
            'Use lavender because lactate is a cell count',
            'Add citrate to the gray tube to preserve lactate',
        ],
        'Fluoride chemistry differs by analyte; oxalate and tube type may invalidate lactate methods. Assuming one gray tube fits all stabilized analytes risks erroneous lactate reporting.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A blood culture turns positive with skin flora after routine tubes were drawn before bottles without new sterile prep. Which additive misconception contributed operationally?',
        'Treating culture bottles like routine vacuum tubes without sterile priority, not an additive interaction but a collection-sequence error tied to specimen type knowledge',
        [
            'Citrate in blue tubes sterilized the hub',
            'EDTA in lavender killed contaminants',
            'Fluoride in gray prevented culture growth so bottles were drawn last',
        ],
        'Sterile technique for cultures is independent of tube anticoagulant chemistry; drawing cultures late without prep increases contamination. Fluoride does not sterilize venipuncture sites or hubs.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'CBC shows marked thrombocytopenia on EDTA, but a smear reveals platelet clumping. Next step consistent with additive-related pseudothrombocytopenia workup?',
        'Collect an alternative anticoagulant specimen (e.g., sodium citrate) per hematology protocol to verify true platelet count',
        [
            'Repeat the same lavender tube and shake harder',
            'Switch to red-top serum for platelet count on automated counter',
            'Add heparin to the EDTA tube after collection',
        ],
        'EDTA-dependent agglutination is a known entity; citrate or other validated tube may be required. Serum clotted tubes cannot be run as CBC; post-hoc heparin addition invalidates specimen integrity.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'An ammonia level is ordered stat, but the specimen arrives warm three hours after collection in a lavender tube. Likely result impact?',
        'Falsely altered ammonia because lavender is not the validated matrix and delay without ice allows volatile loss or metabolism',
        [
            'Accurate because EDTA fixes ammonia like fluoride fixes glucose',
            'Spuriously low INR due to EDTA',
            'No effect if the centrifuge is fast',
        ],
        'Ammonia requires strict preanalytics; EDTA does not stabilize ammonia, and warm delay degrades analyte. Confusing EDTA with fluoride stabilization is a common tube-additive error.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A phlebotomist inverts an EDTA tube only twice, and the hematology lab reports microclots and rejected specimen. Best educational point?',
        'Insufficient mixing left fibrin formation despite EDTA; full gentle inversion per manufacturer prevents clots that trap cells and platelets',
        [
            'EDTA tubes should never be inverted',
            'More fluoride should be added to prevent clotting',
            'Citrate ratio was wrong in the lavender tube',
        ],
        'EDTA prevents clotting only when properly mixed; double inversion is inadequate. Fluoride or citrate comments reveal misunderstanding of lavender versus blue additives.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'What serum separator gel from an SST interferes with a particular drug immunoassay on a send-out test. Laboratory policy switches to red-top without gel. This illustrates what principle?',
        'Additive and separator materials, not just anticoagulants, must match validated methods for analytes such as therapeutic drugs',
        [
            'All drugs must be collected in citrate',
            'Gel improves all drug levels by purifying serum',
            'Culture broth is preferred for drug monitoring',
        ],
        'Gel can adsorb or interfere with some drugs; red-top serum may be required. Citrate or culture media are not default TDM solutions.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'What while capping tubes, a phlebotomist drops a filled lavender tube; blood aerosols onto intact skin with no cuts. According to OSHA BBP practice, the employee should be done how?',
        'Wash the exposure site promptly and report per facility bloodborne pathogen exposure policy even if skin appears intact',
        [
            'Ignore because intact skin never requires action',
            'Reuse gloves for the next patient without hand hygiene',
            'Recap the broken tube with both hands before disposal',
        ],
        'OSHA expects reporting and follow-up evaluation for occupational exposures; intact skin still gets washed. Double-hand recapping increases sharps injury risk contrary to OSHA guidance.',
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "A student claims heparin and EDTA are interchangeable because both 'stop clotting.' Which distinguishing clinical consequence best refutes that claim?",
        'PT/INR must run on citrate plasma, while CBC requires EDTA, swapping anticoagulants makes each test unreportable',
        [
            'Both tubes produce identical plasma for all chemistry',
            'Heparin tubes are used for blood cultures',
            'EDTA is the only additive that causes hemolysis',
        ],
        "Mechanism overlap at 'no clot' hides test-specific requirements; coagulation is not valid on EDTA or heparin unless method says so. Heparin cultures and universal chemistry claims are factually wrong teaching shortcuts.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
]
