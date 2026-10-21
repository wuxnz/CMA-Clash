# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored order-of-draw and collection sequence questions (topic phleb-order-draw)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    fact(
        "phleb-order-draw",
        "Why does CLSI GP41 specify a collection sequence when multiple vacuum tubes are filled from one venipuncture?",
        "To limit additive carryover that can invalidate coagulation, chemistry, and hematology testing",
        [
            "To match tube fill order to decreasing stopper diameter on the tray",
            "To keep the tourniquet inflated until every ordered tube is completely filled",
            "Because stopper color codes storage location rather than draw sequence",
        ],
        "Additive from an earlier tube can enter the next tube and skew assays such as PT/INR or calcium. "
        "Choosing sequence by tube size or convenience ignores the cross-contamination risk CLSI documents for multi-tube draws.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "When blood cultures and routine venous tubes are collected on the same stick, when should culture bottle(s) be filled?",
        "Before non-culture tubes, using sterile technique at the start of the draw",
        [
            "After gray-top fluoride tubes because they complete the CLSI sequence",
            "After all chemistry and gel separator tubes to reduce hemolysis in cultures",
            "In any convenient order because tube sequence does not alter culture accuracy",
        ],
        "CLSI prioritizes culture collection early to limit skin-flora and additive contamination. "
        "Drawing routine tubes first is a common error that can produce false-positive cultures.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "In the CLSI multi-tube venipuncture sequence, which tube type typically follows blood cultures?",
        "Light blue sodium citrate used for coagulation testing",
        [
            "Gold or tiger-top serum separator tube ahead of any citrate tube",
            "Lavender EDTA tube before any other additive tube on the same stick",
            "Gray sodium fluoride tube placed ahead of light blue citrate",
        ],
        "Citrate follows cultures so EDTA, oxalate, or gel additives do not carry into coagulation specimens. "
        "Drawing serum separator or lavender tubes before citrate is a frequent order-of-draw error on PT/INR panels.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "Where does a light blue sodium citrate tube belong in a standard multi-tube venipuncture?",
        "Immediately after blood cultures and before serum, heparin, EDTA, and gray tubes",
        [
            "As the final tube after the gray fluoride collection tube",
            "Before blood cultures whenever a prothrombin time is on the requisition",
            "Excluded from multi-tube draws and limited to solitary citrate orders",
        ],
        "Citrate must follow cultures and precede serum and other additives that can carry into the coagulation tube. "
        "Drawing citrate last or before cultures misstates the CLSI sequence used in practice.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "Relative to light blue citrate and serum tubes, where do green-top heparin tubes belong in the CLSI teaching order?",
        "After citrate and serum or SST tubes in the multi-tube sequence",
        [
            "Before light blue citrate to keep blood from clotting in the needle",
            "Before sterile blood cultures to stabilize electrolytes in the line",
            "After gray-top fluoride tubes in every hospital protocol",
        ],
        "Heparin is positioned after citrate so coagulation studies in the citrate tube are not contaminated. "
        "Placing green before blue reflects a common misconception that heparin must enter the line first to prevent clots.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "In the CLSI teaching order of draw, when are lavender EDTA tubes for hematology typically collected?",
        "After green heparin tubes and before gray-top additive tubes",
        [
            "Before light blue citrate to protect platelets from clumping",
            "As the first tube collected right after tourniquet application",
            "After gray-top tubes as the absolute last container on the stick",
        ],
        "EDTA belongs late in the sequence because its calcium chelation can ruin coagulation and some chemistry assays if drawn too early. "
        "Many students wrongly place lavender immediately after cultures.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "When are gray-top sodium fluoride or potassium oxalate tubes typically drawn in the CLSI sequence?",
        "Last among the routine evacuated tubes in the order of draw",
        [
            "First to preserve glucose before other additives enter the line",
            "Before lavender EDTA when a complete blood count is ordered",
            "Right after blood cultures and ahead of light blue citrate",
        ],
        "Fluoride and oxalate can interfere with numerous assays if carried into earlier tubes, so CLSI places gray last. "
        "Drawing gray early is sometimes confused with collecting glucose tubes before other chemistry.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "You poured blood from one tube into another to top off a short fill. What is the appropriate response?",
        "Do not use either tube for testing; recollect per laboratory policy and document the error",
        [
            "Invert both tubes gently and submit them because additives will equilibrate",
            "Add sterile saline to the underfilled tube until it reaches the mark",
            "Centrifuge the overfilled tube and send the plasma portion alone",
        ],
        "Pouring between tubes cross-contaminates additives and invalidates results. "
        "Saline top-off or selective plasma submission destroys the defined blood-to-additive ratios CLSI requires.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "After filling an EDTA or citrate tube, what mixing technique does CLSI generally recommend?",
        "Gentle end-over-end inversion per manufacturer instructions, often about 5 to 10 times",
        [
            "Vigorous shaking for 30 seconds to prevent red-cell hemolysis",
            "No mixing; allow blood to layer until the tube reaches centrifugation",
            "Horizontal rolling of the tube for several minutes without inversion",
        ],
        "Incomplete mixing can micro-clot EDTA tubes, while violent shaking hemolyzes specimens. "
        "Delaying inversion until central laboratory processing fails CLSI preanalytic mixing guidance for anticoagulated blood.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "According to injection safety and OSHA bloodborne pathogen guidance, how should phlebotomy needles be used?",
        "One patient, one use, with immediate disposal in an approved sharps container",
        [
            "Wiped with alcohol between patients when the hub appears clean",
            "Recapped by hand and stored in a drawer for the next venipuncture on another patient",
            "Bent to break the bevel and placed in a regular waste container between uses",
        ],
        "The One & Only Campaign and OSHA rules require single-patient use of sharps with puncture-resistant disposal. "
        "Cleaning, recapping, or reusing needles between patients increases needlestick transmission risk for bloodborne pathogens.",
        [S.WHO_INJECTION_SAFETY, S.OSHA_BBP, S.CDC_ONE_AND_ONLY],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "Before attaching evacuated tubes during venipuncture, what patient safety step is required?",
        "Verify identity with at least two identifiers per facility policy",
        [
            "Choose tube colors from the requisition without confirming the patient name",
            "Accept the bedmate's stated name when the intended patient is drowsy",
            "Use room number and bed label when the patient cannot speak",
        ],
        "Wrong-patient draws are serious sentinel events, and CLSI collection standards assume verified identity before collection. "
        "Relying on room number or an unverified name bypasses the step that prevents mislabeled specimens.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "When an evacuated tube shows a fill-to mark, especially on citrate, what fill practice is required?",
        "Fill to the mark so the blood-to-additive ratio meets manufacturer specifications",
        [
            "Any visible blood volume is acceptable for coagulation and chemistry testing",
            "Fill above the mark to guarantee enough plasma for repeat analysis",
            "Underfill on difficult veins and send without notifying the laboratory",
        ],
        "Citrate tubes depend on a fixed blood-to-anticoagulant ratio; underfills dilute anticoagulant relative to plasma. "
        "Overfilling seems helpful for repeat testing but is equally invalid under CLSI coagulation guidance.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "When should tube labels be applied relative to venipuncture and leaving the patient?",
        "At the bedside during or immediately after collection per laboratory policy",
        [
            "After centrifugation at the central laboratory processing area",
            "On the following shift when the draw area is less busy",
            "Before identity verification to reduce time at the bedside",
        ],
        "Bedside labeling while the patient is present reduces swap errors in busy draw areas. "
        "Delaying labels invites misassignment, and labeling before identity verification reverses the safety sequence.",
        [S.CLSI_GP41, S.NHA_CPT],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "If a single lavender EDTA tube is the sole collection on a stick, when do CLSI order-of-draw rules chiefly matter?",
        "When multiple tubes or prior additive exposure occur on the same needle stick",
        [
            "On every venipuncture even when just one tube is ordered",
            "For arterial collections but not for routine peripheral venous draws",
            "For pediatric heel sticks but not for adult antecubital venipuncture",
        ],
        "Carryover requires more than one tube in the set; a solitary EDTA draw has no prior additive in the line. "
        "Over-applying order rules can delay urgent single-tube collections without improving specimen quality.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "Coagulation tests are ordered without serum tubes. Why might a non-additive discard tube precede light blue citrate?",
        "To clear needle and holder dead space so tissue thromboplastin does not falsely shorten clotting times",
        [
            "Because citrate tubes are prohibited from being first on any draw list",
            "To dilute citrate anticoagulant so mixing is easier in underfilled tubes",
            "Because discard tubes contain EDTA to prevent clotting in the adapter",
        ],
        "Dead-space contamination falsely shortens PT and aPTT; a discard tube clears tissue thromboplastin without adding anticoagulant. "
        "Believing citrate can never be first ignores CLSI discard-tube protocols used on coagulation-only draws.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "A light blue citrate tube is filled to about 60% of the indicated volume. Which analyte result is most likely invalid?",
        "Prothrombin time or INR from excess anticoagulant relative to blood volume",
        [
            "Hemoglobin measured in that same tube because citrate chelates iron like EDTA",
            "Blood culture growth in an aerobic bottle collected on the same patient visit",
            "Serum sodium if the underfilled tube is centrifuged within one hour",
        ],
        "Underfilled citrate dilutes the specimen and prolongs clotting times artifactually. "
        "Associating the error with hemoglobin confuses citrate coagulation tubes with lavender hematology tubes.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "During a multi-tube draw, lavender EDTA is attached before light blue citrate. What coagulation error is most likely?",
        "Falsely prolonged clotting times from EDTA carryover into the citrate specimen",
        [
            "Falsely shortened prothrombin time from fluoride carryover into citrate",
            "No meaningful change because EDTA and citrate neutralize each other in the hub",
            "Spuriously high glucose on the citrate tube from EDTA glycolysis",
        ],
        "EDTA chelates calcium and can carry through the needle hub into the next tube. "
        "Assuming anticoagulants neutralize each other dismisses the most common CLSI-documented order-of-draw failure on coagulation panels.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "If a green heparin tube is drawn before light blue citrate on one stick, what is the primary risk?",
        "Heparin carryover that interferes with subsequent citrate coagulation testing",
        [
            "Immediate hemolysis confined to a later gray glucose tube on the same stick",
            "False-positive blood culture bottles filled after the heparin tube",
            "Mandatory invalidation of a urine culture unrelated to the venipuncture",
        ],
        "Even trace heparin alters clotting assays, which is why CLSI places heparin after citrate. "
        "Blaming a later gray glucose tube misses that heparin carryover disturbs PT and aPTT interpretation.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "During butterfly collection of multiple evacuated tubes, why maintain blood flow between tube changes?",
        "To reduce stasis, clot formation in the tubing, and underfilled additive tubes",
        [
            "To draw air into the tubing so vacuum tubes fill more quickly",
            "To keep the tourniquet maximally tight until the final tube disconnects",
            "To dry the needle bore between tubes and reduce hub contamination",
        ],
        "Paused flow lets micro-clots form that plug the set and prevent proper citrate fills. "
        "Introducing air or drying the needle increases hemolysis and failed draws rather than improving fill quality.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Blood is collected with a syringe and transferred through a safety transfer device. What does CLSI require?",
        "The same order of draw and fill-volume rules as direct vacuum collection",
        [
            "Any transfer sequence because syringe plastic binds additive chemicals",
            "Serum tubes after all additive tubes regardless of which tests are ordered",
            "Citrate first after cultures even when transfer delays exceed several minutes",
        ],
        "Syringe technique does not waive ratio or sequence requirements; citrate still needs proper fill and placement. "
        "Believing syringes neutralize additives ignores carryover through the transfer needle hub.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "How many gentle inversions are commonly recommended for citrate and EDTA tubes right after collection?",
        "About 5 to 10 end-over-end inversions per manufacturer directions, without vigorous shaking",
        [
            "Exactly one inversion for every anticoagulated tube type",
            "Twenty to thirty rapid shakes to activate clot factors in gel tubes",
            "No inversion until processing staff mix the tube in the central laboratory",
        ],
        "Under-mixing leaves microclots in EDTA specimens, while over-shaking hemolyzes cells. "
        "A single inversion or delayed mixing at the laboratory fails CLSI preanalytic mixing guidance for anticoagulated blood.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "During a stat draw, the phlebotomist is unsure of the institutional tube color sequence. What is the best immediate action?",
        "Consult the laboratory manual or supervisor and document any deviation from policy",
        [
            "Follow the sequence remembered from a prior week to avoid delaying the draw",
            "Collect one tube and cancel the remaining ordered tests on the requisition",
            "Defer patient identification until after tubes are filled to save time",
        ],
        "CLSI defers to validated local procedures when stopper colors differ by vendor. "
        "Guessing from memory propagates carryover errors, and deferring identification trades a minor delay for a major patient-safety breach.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Pediatric blood is collected into microtainer tubes on one puncture. What sequence rule still applies?",
        "A laboratory-approved order of draw to limit additive carryover between microcontainers",
        [
            "No sequence rules because pediatric microvolumes are too small for carryover",
            "Culture tubes last on the stick even when sterile cultures were filled first elsewhere",
            "Lavender EDTA before citrate because infants clot more quickly than adults",
        ],
        "Small volumes magnify ratio errors, and microtainers follow the same carryover principles as adult evacuated tubes. "
        "Assuming volume exempts pediatrics from sequence is a common teaching gap on CLSI-aligned order-of-draw charts.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Tubes for a coagulation and CBC panel were filled in reverse order. What should the phlebotomist do?",
        "Notify the laboratory promptly and recollect per policy when results may be affected",
        [
            "Relabel tubes to reflect the intended order and submit them for testing",
            "Add saline to the citrate tube to restore the blood-to-anticoagulant ratio",
            "Freeze all tubes immediately to halt further additive interaction",
        ],
        "Relabeling does not remove additive contamination already present in the specimens. "
        "Saline dilution or freezing cannot restore valid coagulation ratios once carryover occurs.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Why should routine non-culture tubes not be filled before blood cultures when both are required on one stick?",
        "Non-sterile hub flow can introduce skin organisms that produce false-positive culture results",
        [
            "Culture bottles cannot withstand vacuum pressure from evacuated tubes",
            "Routine additive tubes contain broth that sterilizes organisms in culture media",
            "CLSI limits blood cultures to arterial puncture sites rather than peripheral veins",
        ],
        "Sterile culture technique requires filling bottles before hub contamination from other tubes. "
        "Believing routine tubes protect cultures or that cultures must be arterial misstates CLSI venipuncture practice.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'Why vigorous shaking of a filled EDTA tube right after collection is problematic for what reason?',
        'Can hemolyze red cells and falsely elevate potassium and other analytes',
        [
            'Improves platelet clumping for accurate counts',
            'Is required to activate clot accelerator in lavender tubes',
            'Prevents citrate from binding calcium',
        ],
        "Hemolysis releases intracellular potassium; gentle inversion is sufficient for EDTA. Shaking to 'fix clumping' confuses lavender tubes with serum clot activator tubes.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'When should gold SST tubes be filled during a standard CLSI venipuncture that includes citrate and EDTA?',
        'After light blue citrate and before green heparin or lavender EDTA',
        [
            'Before blood cultures to clot blood faster',
            'Before light blue citrate whenever a chemistry panel is ordered',
            'Before light blue when prothrombin time is not ordered',
        ],
        "SST belongs after cultures and citrate so gel and clot activator do not contaminate coag specimens. Universal 'always after gray' rules ignore institutional charts that place SST with serum group.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'When prothrombin time is the only test ordered, is drawing a single properly filled citrate tube without earlier additive tubes acceptable?',
        'Acceptable because order-of-draw concerns mainly apply to multiple additive tubes in one stick',
        [
            'Never acceptable, lavender must always precede citrate',
            'Acceptable only if a gray tube is drawn first',
            'Forbidden in outpatient settings',
        ],
        'Single-tube coag draws do not have prior additive carryover in the set. Mandatory lavender-first is a misapplication of multi-tube sequencing rules.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'When pink-top EDTA blood bank tubes are included in a composite draw, when are they usually filled?',
        'According to the facility blood bank order chart, often after initial culture/citrate/serum steps',
        [
            'Always before cultures to preserve typing antigens',
            'Only from arterial lines, never venous',
            'After gray fluoride because ABO typing needs fluoride',
        ],
        'Blood bank SOPs define pink placement; it is not interchangeable with routine lavender timing. Drawing pink before sterile cultures risks contamination misinterpreted as transfusion workup error.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'What prolonged tourniquet application while struggling through a long order of tube changes can cause what problems?',
        'Cause hemoconcentration and artifactual elevation of protein-bound analytes and potassium',
        [
            'Improve citrate mixing so PT is more accurate',
            'Have no preanalytic effect if tubes are labeled',
            'Only affect urine drug screens collected later',
        ],
        'CLSI recommends limiting tourniquet time; extended stasis alters several chemistry results. Believing tourniquet time only matters for urine ignores venous stasis effects during multi-tube phlebotomy.',
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'If the needle hub contains visible clot during a multi-tube draw, the phlebotomist should?',
        'Stop, discard the line per policy, and recollect rather than continue the ordered sequence',
        [
            'Flush the clot into the next lavender tube to avoid wasting tubes',
            'Add more vacuum tubes until the clot passes',
            'Ignore it if the citrate tube already filled correctly',
        ],
        'Clot in the hub invalidates hematology and may block proper fills; flushing into EDTA contaminates the CBC. Continuing after a compromised citrate fill risks cascading erroneous results.',
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'What transfer devices that pierce tube stoppers must be used with what precautions?',
        'A new sterile device per patient and tube set to maintain closed-system safety',
        [
            'The same transfer needle for multiple patients if gloves are changed',
            'Only glass tubes because plastic stoppers cannot be pierced',
            'Alcohol rinsing between patients when busy',
        ],
        'OSHA and injection safety require single-patient sharps; reusing transfer needles is a bloodborne pathogen exposure risk. Plastic stoppers are designed for piercing with single-use transfer devices.',
        [S.OSHA_BBP, S.WHO_INJECTION_SAFETY, S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        'What in the ED, a phlebotomist fills lavender EDTA before light blue citrate for a trauma panel. The laboratory should interpret PT/INR from that citrate tube as what?',
        'Suspect invalid due to EDTA carryover; recollection is likely required',
        [
            'Valid if the citrate tube was inverted eight times',
            'Valid only if the patient is not on anticoagulants',
            'Valid if the gold SST was drawn between them',
        ],
        'EDTA in the hub falsifies coagulation even with correct inversion; intermediate tubes do not retroactively remove chelated calcium. Assuming anticoagulant therapy explains abnormal PT delays critical error recognition.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'A difficult antecubital draw yields a citrate tube at 70% of the fill line while other tubes are adequate. What is the best next step?',
        'Notify the laboratory and recollect coagulation specimens per policy; do not send the underfilled citrate tube as definitive',
        [
            'Send it with a note that the patient has small veins',
            'Top off with saline to the mark',
            'Invert vigorously to compress plasma volume',
        ],
        'Ratio error prolongs clotting times independent of vein quality; saline top-off invalidates the specimen. Vigorous mixing cannot correct anticoagulant dilution from low fill volume.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'A fasting patient needs aerobic/anaerobic cultures, PT/INR, comprehensive metabolic panel on SST, CBC, and fluoride glucose in one stick. Which sequence aligns with CLSI principles?',
        'Cultures first, then citrate, SST or serum, heparin if ordered, EDTA, gray last',
        [
            'Gray first for glucose, then cultures, then citrate, then lavender',
            'Lavender, cultures, citrate, SST, gray',
            'SST before cultures because chemistry is stat',
        ],
        'Glucose gray belongs last; cultures need sterile priority; citrate precedes EDTA to protect coagulation. Drawing gray or lavender before cultures trades convenience for contaminated bottles and carryover.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'Using a butterfly with a safety valve, the phlebotomist notes sluggish flow and a fibrin strand in the tubing before attaching the citrate tube. What action best protects coagulation results?',
        'Discontinue the draw, dispose of the set, and restart with new equipment following order of draw',
        [
            'Push saline through the valve to clear the strand into the waste tube',
            'Attach citrate anyway and invert longer',
            'Switch to a larger needle but keep the same tubing',
        ],
        'Fibrin and hemolysis in the line invalidate coagulation; saline flushing introduces non-blood fluid. Reusing contaminated tubing preserves the clot risk CLSI aims to avoid with fresh sets.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'After syringe collection, the physician pushes blood through a transfer device in the order: citrate, SST, lavender. Which issue remains most critical to verify before sending specimens?',
        'Each tube met fill-volume requirements during transfer, especially the citrate ratio',
        [
            'All tubes were labeled before the draw began',
            'The syringe was heparin-coated for chemistry',
            'Cultures were omitted because syringes cannot fill bottles',
        ],
        'Transfer technique still demands full citrate tubes; syringe method does not relax ratio rules. Pre-draw labeling without ID check or heparin-coated syringes without orders are separate errors but ratio is paramount for PT.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'A phlebotomist sustains a needlestick after filling the first of six tubes. According to OSHA bloodborne pathogen requirements, what must occur in addition to completing safe disposal of the used sharp?',
        'Wash the wound, report immediately, and follow employer exposure evaluation and follow-up protocol',
        [
            'Finish the remaining tubes before telling anyone to avoid wasting specimens',
            'Apply a bandage only if blood is visible on the skin',
            'Wait 24 hours to see if symptoms develop before reporting',
        ],
        'OSHA 29 CFR 1910.1030 mandates prompt reporting and medical evaluation after sharps injuries. Delaying report to finish the draw increases PEP delay; silent waiting forfeits post-exposure prophylaxis windows.',
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'An outpatient lab collects SST and lavender but realizes cultures were ordered after both tubes were filled from the same venipuncture. Best corrective action?',
        'Notify the provider/lab; obtain a new culture collection with sterile technique rather than using the existing line',
        [
            'Add culture bottles to the same needle if it is still in the vein without restarting sterile prep',
            'Cancel cultures because earlier tubes contaminated the patient',
            'Send SST as a culture substitute',
        ],
        'Once non-sterile flow occurred, culture contamination risk is high; sterile re-collection is required. Reattaching bottles to the same un-prepped line perpetuates false positives.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'What two light blue citrate tubes are ordered for a lupus anticoagulant panel. Facility policy requires a discard tube when drawing multiple citrate tubes. The phlebotomist should be done how?',
        'Fill a non-additive discard tube first, then fill both citrate tubes to the line in sequence',
        [
            'Fill only one citrate tube and split it after centrifugation',
            'Use lavender as discard because it is also anticoagulated',
            'Skip discard because both tubes are the same color',
        ],
        'Discard clears tissue thromboplastin without introducing EDTA; lavender discard would chelate calcium and ruin coagulation. Splitting one tube post hoc breaks volume and mixing requirements.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'During a long butterfly draw with the tourniquet left on, potassium and phosphate on the heparin plasma tube return markedly high with hemolysis flags. Which preanalytic factor most likely contributed?',
        'Prolonged venous stasis and hemolysis from difficult flow during extended tube changes',
        [
            'Correct order of draw automatically prevents hemolysis regardless of tourniquet time',
            'Heparin additive always raises potassium independent of collection technique',
            'Gray tube drawn last back-flushed into the green tube',
        ],
        'Stasis and trauma hemolyze cells even when order is correct; heparin does not intrinsically spike potassium. Blaming order alone misses tourniquet time and line trauma documented in CLSI preanalytic guidance.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'The first tube attached was lavender instead of gold SST for a BMP on a patient with a citrate tube also on the requisition. The phlebotomist notices before filling other tubes. Best response?',
        'Stop, discard the lavender, and restart the venipuncture following order with a new needle set per policy',
        [
            'Continue because EDTA will not affect serum chemistry on SST drawn second',
            'Send lavender for BMP because calcium is the same assay',
            'Continue the draw and submit the lavender tube for serum BMP chemistry',
        ],
        'EDTA invalidates many chemistry analytes and contaminates the hub for subsequent tubes; continuing wastes the coag tube too. BMP on lavender is not interchangeable with serum methods.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'A NICU nurse collects a capillary heel stick into microtainers for bilirubin (serum) and CBC. Order of draw should be guided by?',
        'Hospital laboratory microcollection order, typically serum/non-additive before EDTA unless policy states otherwise',
        [
            'Always EDTA first because infants have higher hematocrit',
            'Random order because capillary specimens are exempt from all CLSI rules',
            'Gray fluoride before all other microtainers for every neonate',
        ],
        'Neonatal microcollection still prevents additive carryover; bilirubin and CBC have conflicting needs if order is wrong. Universal EDTA-first or fluoride-first rules ignore test-specific lab manuals.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'Home health collects via syringe from fragile veins; citrate and SST are both 30% underfilled while lavender is full. Which decision aligns with CLSI and patient safety?',
        'Recollect coagulation and chemistry tubes; do not submit underfilled citrate or compromised SST volumes',
        [
            'Submit all tubes because partial data is better than none',
            'Combine SST and citrate into one tube to reach volume',
            'Add heel-stick capillary blood to top off the citrate tube',
        ],
        'Underfilled citrate and inadequate serum volumes invalidate results; combining specimens cross-contaminates additives. Capillary top-off breaks ratio control and introduces tissue fluid.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'What only a lavender EDTA is available for an ionized calcium test that the laboratory requires on serum. The phlebotomist should be done how?',
        'Stop and obtain the correct tube per laboratory manual before collecting; EDTA is inappropriate for ionized calcium',
        [
            'Proceed because all calcium tests use the same tube',
            "Draw lavender and request the lab to 'correct' for EDTA mathematically",
            'Draw gray fluoride because it stabilizes calcium',
        ],
        'EDTA chelates calcium and makes ionized calcium uninterpretable; gray fluoride does not fix that error. Mathematical correction is not a CLSI-approved substitute for proper tube selection.',
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        'After a power outage, a clinic must draw cultures, PT, and glucose on one patient with one butterfly set. The nurse documents deviation because only a winged set without holder was available, delaying citrate fill. Priority documentation should include?',
        'Time of draw, tubes collected, order used, equipment limitation, and notification to the laboratory for result interpretation',
        [
            "Only the patient's allergy list",
            'A note that CLSI does not apply during outages',
            'The color of the tourniquet used',
        ],
        'Laboratories need context to judge compromised coag or culture specimens; CLSI deviations require traceability. Claiming standards do not apply during outages avoids accountability for invalid results.',
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
]
