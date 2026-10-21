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
        "Sodium citrate anticoagulant for coagulation testing",
        [
            "Potassium EDTA anticoagulant for hematology cell counts",
            "Lithium heparin anticoagulant for plasma chemistry assays",
            "Potassium oxalate with sodium fluoride for glucose preservation",
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
            "It contains sodium citrate for INR testing when validating plasma versus serum collection requirements",
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
            "Sodium citrate for coagulation studies when validating plasma versus serum collection requirements",
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
            "Green lithium heparin plasma tube for chemistry versus hematology versus coagulation testing",
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
            "Broth media in a blood culture bottle when validating plasma versus serum collection requirements",
        ],
        "Fluoride inhibits enolase, slowing glucose consumption by cells and bacteria after collection. "
        "Serum from red tops or citrate plasma lacks the same glycolysis protection unless the method specifies otherwise.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-additives",
        "How do sterile blood culture bottles differ from routine additive vacuum tubes in purpose and contents?",
        "They contain broth media for aerobic or anaerobic growth, not routine tube anticoagulants",
        [
            "They contain EDTA to keep blood fluid during incubation when validating plasma versus serum collection requirements",
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
            "Prothrombin time and INR may run on the same heparin specimen when the tube color must match the ordered assay",
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
            "Lithium heparin for ABO forward typing when validating plasma versus serum collection requirements",
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
            "Inhibiting enolase the same way sodium fluoride does when the tube color must match the ordered assay",
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
            "It stabilizes glucose for days without sodium fluoride for chemistry versus hematology versus coagulation testing",
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
            "It precipitates fibrinogen with potassium oxalate when validating plasma versus serum collection requirements",
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
            "It activates factor VII to shorten clotting time when the tube color must match the ordered assay",
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
            "Chelate calcium and form a chemical gel barrier between cells and plasma after centrifugation",
            "Sterilize serum and prevent bacterial growth during transport like blood culture broth",
            "Convert residual heparin into sodium citrate for downstream coagulation testing",
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
            "Potassium EDTA to preserve erythrocyte morphology for chemistry versus hematology versus coagulation testing",
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
        "Excess citrate relative to blood distorts the required about 9:1 blood-to-anticoagulant ratio",
        [
            "Underfill automatically introduces EDTA from the needle hub for chemistry versus hematology versus coagulation testing",
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
            "Unchanged counts when the bedside label matches the requisition for chemistry versus hematology versus coagulation testing",
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
            "Elevated INR measured on the same serum aliquot for chemistry versus hematology versus coagulation testing",
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
            "K2EDTA contains lithium heparin for plasma chemistry when the tube color must match the ordered assay",
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
            "Suppress platelet clumping for automated CBC differentials if lavender, green, or blue tubes are confused on the tray",
            "Maintain sterile conditions equivalent to blood culture broth",
        ],
        "Clot activators shorten the clotting phase for serum chemistry; they do not anticoagulate like heparin or preserve cells like EDTA. "
        "Culture sterility requires dedicated sterile bottle systems, not chemistry tube additives.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "Which preanalytic handling does stat ammonia testing typically require?",
        "Laboratory-specified tube, immediate chilling, and rapid transport",
        [
            "Lavender EDTA at room temperature for twenty-four hours before testing",
            "Gray fluoride at room temperature because fluoride stabilizes ammonia",
            "Blood culture broth as the collection container for stat ammonia",
        ],
        "Ammonia is labile; prolonged room-temperature storage in the wrong tube yields unreliable results. "
        "Gray fluoride preserves glucose and is not a default ammonia substitute without laboratory validation.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "Which anticoagulant system do many Westergren-style erythrocyte sedimentation rate kits use?",
        "Citrate-diluted blood per manufacturer instructions rather than standard lavender EDTA",
        [
            "Serum separator gel tubes with clot activator for standard ESR",
            "Gray sodium fluoride tubes without citrate dilution for standard ESR",
            "Plain red-top clotted serum without anticoagulant dilution when the tube color must match the ordered assay",
        ],
        'ESR methods are instrument-specific; citrate dilution is common on Westergren systems. Assuming any CBC tube works ignores manufacturer requirements cited in CLSI preanalytics.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'What special handling do therapeutic drug monitoring specimens require?',
        "Laboratory-defined collection tube matrix and peak or trough draw timing",
        [
            "Any green-top heparin tube for therapeutic drug monitoring assays",
            "Urine cups for oral medication monitoring orders if lavender, green, or blue tubes are confused on the tray",
            "Culture bottles to prevent in vitro drug metabolism",
        ],
        'Drug assays vary by matrix; heparin plasma is not universal. Urine or culture containers do not replace validated blood collection tubes for TDM.',
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'Which laboratory values does hemolysis during collection most often artifactually elevate?',
        'Potassium and lactate dehydrogenase and other intracellular analytes',
        [
            "Depressed sodium from EDTA carryover during the draw when validating plasma versus serum collection requirements",
            "Elevated INR on a properly filled citrate tube without carryover",
            "Shortened blood culture time-to-positivity from hemolysis alone",
        ],
        'Red cell rupture spills K+ and LDH; sodium changes are not the classic hemolysis pattern. INR rises from ratio or heparin problems, not hemolysis alone in isolation.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        'What rapid serum tubes (e.g., thrombin-based orange or speckled variants) achieve clotting by what mechanism?',
        'Thrombin or similar clot activator to shorten serum formation time',
        [
            'Adding EDTA to stabilize clot when validating plasma versus serum collection requirements',
            'Using fluoride to clot blood rapidly',
            "Removing ionized calcium with citrate anticoagulation",
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
            "EDTA raises measured sodium and does not bind calcium in the specimen",
            "Ionized calcium requires gray fluoride tubes by default when validating plasma versus serum collection requirements",
            "Lavender EDTA is preferred for routine electrolyte panels",
        ],
        'Chelation binds calcium in vitro; no amount of mixing restores physiologic ionized calcium. Gray fluoride does not undo EDTA binding, proper tubeless serum or specific ionized calcium tube is required.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "The laboratory validates electrolytes on lithium heparin plasma but potassium is elevated with a hemolysis index. "
        "Which preanalytic issue is most likely despite the correct tube additive?",
        "Traumatic draw, prolonged tourniquet, or vigorous mixing that hemolyzed cells despite correct heparin anticoagulation",
        [
            "Heparin anticoagulation alone as the cause of high potassium without hemolysis",
            "Citrate carryover from drawing the blue tube after the green tube when validating plasma versus serum collection requirements",
            "Fluoride inhibition falsely increasing potassium on the plasma specimen",
        ],
        'Hemolysis releases intracellular potassium; correct heparin cannot neutralize lysed cells. Blaming heparin chemistry or fluoride ignores the hemolysis flag tying to collection trauma.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "A warfarin patient's citrate tube arrives at 50% fill after a difficult draw. What should the coagulation technologist do?",
        "Reject the specimen for citrate ratio error and request recollection before reporting INR",
        [
            "Report INR after applying a fixed mathematical correction factor",
            "Add citrate to the tube until the fill line is reached when the tube color must match the ordered assay",
            "Run INR on heparin plasma from a green-top tube instead",
        ],
        "There is no valid correction factor for half-filled citrate under CLSI coagulation standards. "
        "Adding citrate or switching to heparin plasma changes the coagulation assay matrix.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A patient on IV heparin has an aPTT drawn in a blue citrate tube while heparin is infusing in the same arm. Which interpretation concern is most important?',
        "Draw-site blood may contain therapeutic heparin that prolongs aPTT beyond tube citrate ratio effects",
        [
            "Citrate neutralizes circulating therapeutic heparin in the draw site",
            "Lavender EDTA is required to cancel systemic heparin before aPTT",
            "Gray fluoride must be drawn first to bind circulating heparin when validating plasma versus serum collection requirements",
        ],
        'Tube citrate does not remove systemic anticoagulant; arm with infusion contaminates results. Switching to EDTA or fluoride does not solve arm-selection contamination.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A gray fluoride/oxalate tube is collected for fasting glucose, but the patient also needs a plasma lactate on the same visit. The phlebotomist should?',
        "Check the laboratory manual because lactate may need its own preservative tube separate from the gray glucose tube",
        [
            "Use the same gray tube because fluoride stabilizes glucose and lactate alike",
            "Use lavender EDTA because lactate is measured on the CBC analyzer when the tube color must match the ordered assay",
            "Add sodium citrate to the gray tube to preserve plasma lactate when the tube color must match the ordered assay",
        ],
        "Fluoride chemistry differs by analyte; oxalate and tube type may invalidate lactate methods. "
        "One gray tube does not automatically satisfy separate glucose and lactate validation requirements.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A blood culture turns positive with skin flora after routine tubes were drawn before bottles without new sterile prep. Which additive misconception contributed operationally?',
        "Treating culture bottles like color-coded vacuum tubes without culture-first sterile technique",
        [
            'Citrate in blue tubes sterilized the hub',
            'EDTA in lavender killed contaminants for chemistry versus hematology versus coagulation testing',
            'Fluoride in gray prevented culture growth so bottles were drawn last',
        ],
        'Sterile technique for cultures is independent of tube anticoagulant chemistry; drawing cultures late without prep increases contamination. Fluoride does not sterilize venipuncture sites or hubs.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "CBC shows thrombocytopenia on EDTA, but a smear reveals platelet clumping. "
        "What is the next step for additive-related pseudothrombocytopenia workup?",
        "Collect a sodium citrate tube per hematology protocol to verify the platelet count",
        [
            'Repeat the same lavender tube and shake harder',
            'Switch to red-top serum for platelet count on automated counter',
            'Add heparin to the EDTA tube after collection for chemistry versus hematology versus coagulation testing',
        ],
        'EDTA-dependent agglutination is a known entity; citrate or other validated tube may be required. Serum clotted tubes cannot be run as CBC; post-hoc heparin addition invalidates specimen integrity.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "An ammonia level is ordered stat, but the specimen arrives warm three hours after collection in a lavender EDTA tube. "
        "What effect is most likely on the ammonia result?",
        "Falsely elevated ammonia from warm delay in a non-validated lavender matrix",
        [
            "Falsely low ammonia from EDTA chelation binding ammonia in the specimen",
            "Accurate ammonia if lavender EDTA is centrifuged within four hours of collection",
            "Falsely elevated ammonia from hemolysis without warm delay or wrong-matrix handling",
        ],
        "Ammonia is labile and requires a laboratory-specified tube, chilling, and rapid transport. "
        "Warm delay in lavender does not stabilize ammonia; hemolysis can add artifact, but delay and wrong matrix "
        "still drive falsely high results on stat orders.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        'A phlebotomist inverts an EDTA tube only twice, and the hematology lab reports microclots and rejected specimen. Best educational point?',
        "Insufficient mixing allowed fibrin to form despite EDTA anticoagulation",
        [
            "EDTA tubes need no inversion because the additive mixes itself during draw",
            "Sodium fluoride should be added to the lavender tube to prevent clotting",
            "The citrate ratio was wrong in the lavender EDTA tube",
        ],
        "EDTA prevents clotting after proper mixing; double inversion is inadequate. "
        "Fluoride or citrate comments reveal misunderstanding of lavender versus blue additives.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "Serum separator gel from an SST interferes with a send-out drug immunoassay, so the laboratory switches to plain red-top without gel. Which principle does this illustrate?",
        "Tube additives and separator gel must match validated methods for the ordered analyte",
        [
            "Therapeutic drugs must be collected in sodium citrate tubes",
            "Gel separator improves drug recovery by purifying serum aliquots",
            "Culture broth is the default container for drug monitoring when validating plasma versus serum collection requirements",
        ],
        'Gel can adsorb or interfere with some drugs; red-top serum may be required. Citrate or culture media are not default TDM solutions.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "While capping tubes, a phlebotomist drops a filled lavender tube and blood aerosols onto intact skin with no cuts. Per OSHA bloodborne pathogen practice, what should the employee do?",
        "Wash the exposure site and report per facility bloodborne pathogen exposure policy",
        [
            "Ignore the splash because intact skin needs no washing or occupational reporting",
            "Reuse gloves for the next patient without hand hygiene",
            "Recap the broken tube with both hands before disposal when validating plasma versus serum collection requirements",
        ],
        'OSHA expects reporting and follow-up evaluation for occupational exposures; intact skin still gets washed. Double-hand recapping increases sharps injury risk contrary to OSHA guidance.',
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "A student claims heparin and EDTA are interchangeable because both 'stop clotting.' Which distinguishing clinical consequence best refutes that claim?",
        "PT and INR require citrate plasma while CBC requires EDTA, so swapped tubes yield unreportable results",
        [
            "Both tube types yield identical plasma suitable for the chemistry menu",
            "Green heparin tubes are the standard container for blood cultures if lavender, green, or blue tubes are confused on the tray",
            "Lavender EDTA is the usual cause of hemolysis on chemistry specimens",
        ],
        "Mechanism overlap at 'no clot' hides test-specific requirements; coagulation is not valid on EDTA or heparin unless method says so. Heparin cultures and universal chemistry claims are factually wrong teaching shortcuts.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "What is the main practical distinction between sodium heparin and lithium heparin in green-top plasma collection tubes?",
        "Both use antithrombin, but the cation salt differs and may affect validated chemistry methods",
        [
            "Sodium heparin is reserved for hematology CBCs and lithium heparin is reserved for coagulation PT",
            "Lithium heparin chelates calcium the way sodium citrate does in light blue tubes",
            "Sodium heparin tubes contain clot activator and lithium heparin tubes contain EDTA",
        ],
        "Green tubes may specify lithium or sodium heparin depending on manufacturer and assay validation. "
        "The anticoagulant mechanism is similar, but laboratories treat the plasma matrix as method-specific, not interchangeable by cation alone.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "Royal blue-top vacuum tubes with EDTA are used primarily for which class of laboratory testing?",
        "Trace element and heavy metal analysis where standard additives would contaminate the specimen",
        [
            "Routine automated complete blood counts with platelet differentials",
            "Prothrombin time and INR on citrated plasma at a fixed ratio when the tube color must match the ordered assay",
            "Blood bank crossmatch and antibody identification on pink EDTA",
        ],
        "Trace-element tubes minimize lead and other metal contamination from standard stoppers and additives. "
        "They are not substitutes for lavender hematology, light blue coagulation, or pink blood bank EDTA workflows.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "CTAD (citrate, theophylline, adenosine, dipyridamole) additive tubes are collected primarily to preserve which analyte during platelet activation?",
        "Platelet function assays by limiting ex vivo platelet degranulation",
        [
            "Fasting plasma glucose by inhibiting enolase like sodium fluoride gray tubes",
            "Ionized calcium by chelating divalent cations like potassium EDTA",
            "Arterial pH and pCO2 on plain syringes without CTAD additives",
        ],
        "CTAD stabilizes platelet activity for specialized testing rather than serving routine chemistry or hematology. "
        "Confusing CTAD with fluoride glucose preservation or EDTA calcium binding misassigns tube roles on certification items.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "How does acid citrate dextrose (ACD) solution for blood bank collections differ from pink-top potassium EDTA tubes?",
        "ACD anticoagulates with citrate and dextrose for donor or component processing, whereas pink EDTA preserves patient specimens for immunohematology",
        [
            "ACD contains potassium EDTA and pink tops contain sodium citrate at the PT ratio for chemistry versus hematology versus coagulation testing",
            "ACD is used for automated CBC differentials and pink tops are for glucose preservation for chemistry versus hematology versus coagulation testing",
            "Both are identical additives interchangeable for crossmatch and type and screen if lavender, green, or blue tubes are confused on the tray when validating plasma versus serum collection requirements",
        ],
        "Blood bank workflows distinguish donor or component anticoagulants from patient EDTA tubes used in typing and screening. "
        "Swapping ACD and patient EDTA breaks standard operating procedures and can invalidate immunohematology results.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "After collecting blood in a clot activator tube for serum chemistry, what preanalytic timing is most important before centrifugation?",
        "Allow complete clot formation per manufacturer time, then centrifuge within stability limits",
        [
            "Centrifuge immediately without clotting because activator replaces fibrin formation",
            "Refrigerate unclotted blood for 24 hours before any centrifugation step for chemistry versus hematology versus coagulation testing",
            "Mix with EDTA after collection to stabilize the clot activator reaction",
        ],
        "Serum cannot be separated until fibrin clot forms; rushing centrifugation yields fibrin contamination and rejected aliquots. "
        "Cold storage of unclotted specimens or post-hoc EDTA addition violates validated serum processing pathways.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "Why may potassium differ between serum from a red-top tube and lithium heparin plasma from the same patient if collection is traumatic?",
        "Hemolysis and tourniquet stasis release intracellular potassium; matrix choice does not cancel hemolysis",
        [
            "Heparin lowers measured potassium compared with serum on a clean draw when validating plasma versus serum collection requirements",
            "Serum potassium rises because clot activator lyses red cells during clotting",
            "Plasma potassium stays accurate in green tubes with visible hemolysis",
        ],
        "Potassium is a classic hemolysis and stasis marker in both serum and plasma. "
        "Correct tube additive does not cancel lysed red cells; preanalytic technique and hemolysis index review remain essential.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-additives",
        "What is the primary reason coagulation laboratories specify 3.2% versus 3.8% sodium citrate concentration "
        "rather than treating light blue tubes as interchangeable?",
        "Anticoagulant concentration changes the blood-to-citrate ratio and validated PT/aPTT results for that reagent system",
        [
            "3.8% citrate is for hematology and 3.2% is for glucose preservation for chemistry versus hematology versus coagulation testing",
            "The percentage labels describe stopper color alone without changing coagulation reagents",
            "3.2% citrate contains EDTA and 3.8% citrate contains heparin for plasma chemistry",
        ],
        "Coagulation assays depend on a fixed citrate concentration matched to fill volume and instrument reagents. "
        "Mixing 3.2% and 3.8% tubes or assuming concentration is cosmetic distorts clotting times and INR reporting.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-additives",
        "When serum separator gel interferes with an analyte on a send-out assay, what collection change best addresses the preanalytic problem?",
        "Recollect in a gel-free validated tube instead of reporting gel-contaminated serum",
        [
            "Centrifuge the SST again at higher speed to force the gel through the serum aliquot",
            "Add sodium citrate to the SST aliquot to neutralize gel binding of the analyte",
            "Switch to lavender EDTA whole blood because EDTA removes gel interference",
        ],
        "Gel may adsorb drugs, hormones, or other analytes; laboratories specify gel-free serum when methods require it. "
        "Re-spinning, citrate addition, or EDTA substitution does not restore a validated matrix after gel exposure.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
]
