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
        "To limit additive carryover that spoils coagulation, chemistry, and hematology results",
        [
            "To match tube order to stopper size on the collection tray",
            "To keep the tourniquet on until every tube is completely filled",
            "Because stopper color shows storage shelf rather than draw sequence",
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
        "Right after blood cultures and before serum, heparin, EDTA, and gray tubes",
        [
            "As the last tube after the gray fluoride tube in the teaching order",
            "Before blood cultures when prothrombin time is ordered",
            "Only on solitary citrate draws with no other tubes on the stick",
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
            "After gray-top fluoride tubes before serum or heparin tubes",
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
        "Do not use either tube for testing; recollect per policy and document the error",
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
        "After filling a light blue sodium citrate tube, how many gentle inversions does CLSI typically recommend?",
        "3 to 4 gentle end-over-end inversions",
        [
            "8 to 10 gentle end-over-end inversions",
            "5 gentle end-over-end inversions",
            "No inversion before the tube reaches the laboratory",
        ],
        "Citrate coagulation tubes usually need about three to four inversions to mix anticoagulant without hemolysis. "
        "EDTA mixing counts and delayed laboratory mixing are common confusions on coagulation specimens.",
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
            "Any visible blood in the tube meets fill requirements for coagulation testing",
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
        "At the bedside during or after collection per policy",
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
            "False-positive blood culture bottles filled after the heparin tube on the same venipuncture",
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
            "Serum tubes after all additive tubes when coagulation and chemistry share one stick",
            "Citrate first after cultures even when transfer delays exceed several minutes",
        ],
        "Syringe technique does not waive ratio or sequence requirements; citrate still needs proper fill and placement. "
        "Believing syringes neutralize additives ignores carryover through the transfer needle hub.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "After filling a lavender EDTA tube for hematology, how many gentle inversions does CLSI typically recommend?",
        "8 to 10 gentle end-over-end inversions",
        [
            "3 to 4 gentle end-over-end inversions",
            "5 gentle end-over-end inversions",
            "No inversion before the tube reaches the laboratory",
        ],
        "Lavender EDTA tubes need thorough gentle mixing, typically about eight to ten inversions. "
        "Citrate tube counts or skipping bedside mixing cause microclots and rejected hematology specimens.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "After filling a green-top heparin tube for plasma chemistry, how many gentle inversions does CLSI typically recommend?",
        "8 to 10 gentle end-over-end inversions",
        [
            "3 to 4 gentle end-over-end inversions",
            "5 gentle end-over-end inversions",
            "No inversion before the tube reaches the laboratory",
        ],
        "Heparin plasma tubes need thorough gentle mixing, typically about eight to ten inversions. "
        "Citrate or SST inversion counts are common confusions that leave heparin specimens under-mixed.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "After filling a gold serum separator tube, how many gentle inversions does CLSI typically recommend?",
        "5 gentle end-over-end inversions",
        [
            "3 to 4 gentle end-over-end inversions",
            "8 to 10 gentle end-over-end inversions",
            "No inversion before the tube reaches the laboratory",
        ],
        "Serum separator tubes are mixed with about five gentle inversions to distribute clot activator without hemolysis. "
        "EDTA or citrate mixing counts do not apply to gold SST collection technique.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "During a stat draw, the phlebotomist is unsure of the institutional tube color sequence. What is the best immediate action?",
        "Consult the laboratory manual or supervisor; document deviations per policy",
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
        "After filling a lavender EDTA tube, a student shakes it vigorously for about 30 seconds. Why is that mixing technique inappropriate?",
        "It can hemolyze red cells and falsely elevate potassium and other cell-bound analytes",
        [
            "It can hemolyze red cells and falsely lower potassium while platelets clump in fibrin strands",
            "It improves platelet dispersion so automated counts match manual smear differentials",
            "It is required because lavender tubes contain clot activator for serum separation",
        ],
        "Hemolysis releases intracellular potassium and other analytes; CLSI recommends gentle inversion for EDTA, not violent shaking. "
        "Believing lavender needs clot activator or that mixing is optional confuses hematology tubes with gold serum separator tubes.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "On one venipuncture you must collect blood cultures, light blue citrate, gold SST, green heparin, and lavender EDTA. "
        "When should the gold SST tube be filled relative to citrate and the heparin or lavender tubes?",
        "After light blue citrate and before green heparin or lavender EDTA",
        [
            "Before sterile blood cultures so serum clots before other additives enter the line",
            "Before light blue citrate whenever a comprehensive chemistry panel is on the requisition",
            "Immediately after gray-top fluoride tubes in the standard teaching sequence",
        ],
        "SST belongs after cultures and citrate so gel and clot activator do not carry into coagulation specimens. "
        "Drawing SST before cultures or citrate, or assuming gray must precede SST, misapplies the CLSI serum group placement.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Prothrombin time is the only test ordered, and you plan one properly filled light blue citrate tube with no other tubes on that needle stick. "
        "Is that collection acceptable under CLSI order-of-draw principles?",
        "Yes, because carryover rules apply when multiple additive tubes share one needle stick",
        [
            "No, lavender EDTA must precede citrate on every venipuncture requisition",
            "Yes, but a gray-top fluoride tube must be collected first to stabilize the specimen",
            "No, citrate cannot serve as the solitary tube during outpatient phlebotomy",
        ],
        "A single citrate draw has no prior additive in the line, so multi-tube sequencing rules do not apply. "
        "Requiring lavender or gray before a lone citrate tube misextends carryover guidance from composite draws.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "When pink-top EDTA blood bank tubes are included in a multi-tube venipuncture, when are they typically filled?",
        "Per facility blood bank chart, often after culture, citrate, and serum steps",
        [
            "Before sterile blood cultures to preserve ABO and Rh typing antigens in the bottle",
            "From arterial catheters exclusively rather than routine peripheral venipuncture sites",
            "After gray-top fluoride tubes because ABO typing requires fluoride preservative",
        ],
        "Blood bank SOPs define pink placement; it is not interchangeable with routine lavender timing on the same chart. "
        "Drawing pink before sterile cultures or assuming fluoride stabilizes typing risks contamination and misinterpreted transfusion workups.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "During a difficult multi-tube draw you leave the tourniquet inflated while changing several evacuated tubes. "
        "Which preanalytic change is most likely on chemistry results?",
        "Hemoconcentration with artifactually elevated protein-bound analytes and potassium",
        [
            "Improved citrate mixing that makes prothrombin time more representative of in vivo clotting",
            "No measurable preanalytic effect once bedside labels are applied to each tube",
            "Selective distortion of urine drug screens collected later the same day",
        ],
        "CLSI recommends limiting tourniquet time because extended venous stasis concentrates analytes in the limb. "
        "Assuming labels fix stasis effects or that tourniquet time affects urine but not venous chemistry ignores documented hemoconcentration.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Midway through a multi-tube venipuncture you see clot in the needle hub. What is the appropriate next step?",
        "Stop, discard the collection set per policy, and recollect instead of continuing",
        [
            "Flush the visible clot into the next lavender EDTA tube to avoid wasting vacuum tubes",
            "Attach additional vacuum tubes until the clot passes and flow resumes normally",
            "Continue the draw if the light blue citrate tube already reached the fill mark",
        ],
        "Clot in the hub invalidates hematology specimens and may prevent proper fills on remaining tubes. "
        "Flushing clot into EDTA contaminates the CBC, and continuing after a compromised line risks cascading erroneous results.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "When transferring blood from a syringe through a device that pierces tube stoppers, what injection-safety rule applies to that transfer device?",
        "Use a new sterile device for each patient and tube set to maintain closed-system safety",
        [
            "Reuse the same transfer needle on multiple patients when gloves are changed between sticks",
            "Reserve transfer devices for glass tubes because plastic stoppers cannot be pierced safely",
            "Rinse the transfer needle with alcohol between patients during busy outpatient sessions",
        ],
        "OSHA and WHO injection-safety guidance require single-patient use of sharps, including transfer needles. "
        "Plastic stoppers are designed for piercing with single-use transfer devices; alcohol rinsing does not restore sterility between patients.",
        [S.OSHA_BBP, S.WHO_INJECTION_SAFETY, S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "In the emergency department you filled lavender EDTA before light blue citrate for a trauma coagulation panel. "
        "How should the laboratory treat prothrombin time from that citrate tube?",
        "Treat results as suspect for EDTA carryover and likely require recollection per policy",
        [
            "Accept results as valid if the citrate tube was inverted the recommended number of times",
            "Accept results as valid when the patient is not taking prescribed anticoagulant medication",
            "Accept results as valid if a gold SST tube was collected between the lavender and citrate tubes",
        ],
        "EDTA in the needle hub chelates calcium and falsifies coagulation even with correct inversion technique. "
        "An intermediate SST tube does not remove EDTA already in the line, and attributing abnormal PT to anticoagulant therapy delays error recognition.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "A light blue citrate tube fills to about 70% of the manufacturer mark while other tubes on the stick fill adequately. "
        "What is the best next step?",
        "Discard the underfilled citrate tube and recollect coagulation per policy",
        [
            "Send the underfilled citrate with a difficult-vein comment on the form",
            "Add sterile saline to the fill mark before inverting the citrate tube",
            "Invert the citrate tube vigorously to concentrate plasma for testing",
        ],
        "Citrate coagulation testing depends on a fixed blood-to-anticoagulant ratio; underfill dilutes the specimen and prolongs clotting times. "
        "Saline top-off or aggressive mixing cannot restore a valid ratio once the tube is underfilled.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "A fasting patient needs aerobic and anaerobic cultures, PT/INR, a comprehensive metabolic panel on SST, CBC, and fluoride glucose on one stick. "
        "Which collection sequence aligns with CLSI principles?",
        "Cultures first, then citrate, SST or serum, heparin if ordered, EDTA, then gray fluoride last",
        [
            "Gray fluoride first for glucose, then cultures, citrate, lavender, and SST",
            "Lavender EDTA, cultures, citrate, SST, and gray fluoride in that order",
            "SST before cultures because the chemistry panel is marked stat on the requisition",
        ],
        "Sterile cultures take priority, citrate precedes EDTA to protect coagulation, and gray fluoride belongs last to limit additive carryover. "
        "Drawing gray, lavender, or SST before cultures trades convenience for contaminated bottles and invalid coagulation or chemistry specimens.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "Using a butterfly with a safety valve, you note sluggish flow and a fibrin strand in the tubing before attaching the light blue citrate tube. "
        "What action best protects coagulation results?",
        "Discontinue the draw, dispose of the set, and restart with new equipment following order of draw",
        [
            "Push sterile saline through the valve to flush the fibrin strand into a waste tube",
            "Attach the citrate tube anyway and increase inversion time after collection",
            "Switch to a larger-gauge needle but continue using the same tubing set",
        ],
        "Fibrin and micro-clots in the line invalidate coagulation specimens and may prevent proper citrate fill. "
        "Saline flushing introduces non-blood fluid, and reusing contaminated tubing preserves the clot risk CLSI avoids with a fresh set.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "After syringe collection, blood is pushed through a transfer device in this order: citrate, SST, lavender. "
        "Which issue remains most critical to verify before sending the specimens?",
        "Verify each tube met fill volume during transfer, especially citrate blood-to-additive ratio",
        [
            "That all tubes were labeled with the patient name before venipuncture began at the bedside",
            "That the collection syringe was heparin-coated to stabilize chemistry analytes during transfer",
            "That blood cultures were omitted because syringes cannot fill culture bottles",
        ],
        "Syringe transfer does not relax citrate fill requirements; ratio errors invalidate PT and aPTT regardless of collection method. "
        "Pre-draw labeling without identity verification and unordered heparin-coated syringes are separate errors, but citrate volume remains paramount.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "A phlebotomist sustains a needlestick after filling the first of six ordered tubes. "
        "According to OSHA bloodborne pathogen requirements, what must occur in addition to safe disposal of the used sharp?",
        "Wash the wound, report the exposure promptly, and follow the employer exposure evaluation protocol",
        [
            "Finish the remaining tube draws first, then wash the wound and report when the patient leaves",
            "Apply a bandage when blood is visible, discard the sharp, and defer occupational health notification",
            "Wait twenty-four hours for symptoms, then report and request follow-up if illness develops",
        ],
        "OSHA 29 CFR 1910.1030 requires prompt reporting and medical evaluation after sharps injuries. "
        "Delaying notification to finish the draw or waiting for symptoms can forfeit timely post-exposure prophylaxis and source-patient testing.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "An outpatient lab fills SST and lavender EDTA from one venipuncture, then discovers blood cultures were also ordered. "
        "What is the best corrective action?",
        "Obtain new cultures with sterile technique instead of attaching bottles to the used needle line",
        [
            "Notify the laboratory and attach culture bottles to the existing needle without repeating sterile skin prep",
            "Cancel the culture order permanently and document that routine tubes contaminated the patient",
            "Submit the SST aliquot for culture incubation because both containers hold patient blood",
        ],
        "Once non-sterile hub flow occurred, skin organisms can produce false-positive cultures if bottles are attached late. "
        "Sterile re-collection is required; reattaching bottles without fresh prep perpetuates contamination risk.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "Two light blue citrate tubes are ordered for a lupus anticoagulant panel, and facility policy requires a discard tube when drawing multiple citrate tubes. "
        "How should the phlebotomist proceed?",
        "Fill a non-additive discard tube first, then fill both citrate tubes to the line in sequence",
        [
            "Fill one citrate tube and split the specimen after centrifugation in the laboratory",
            "Use a lavender EDTA tube as discard because it is also an anticoagulant tube",
            "Omit the discard tube because both citrate tubes share the same stopper color",
        ],
        "A non-additive discard clears tissue thromboplastin from dead space without introducing chelating anticoagulant. "
        "Lavender discard would carry EDTA into coagulation testing, and splitting one tube post hoc breaks volume and mixing requirements.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "During a long butterfly draw with the tourniquet left on, potassium and phosphate on a green heparin plasma tube return markedly high with hemolysis flags. "
        "Which preanalytic factor most likely contributed?",
        "Prolonged venous stasis and hemolysis from difficult flow during extended tube changes",
        [
            "Correct order of draw prevents hemolysis even when tourniquet time exceeds recommended limits",
            "Heparin additive independently raises plasma potassium without regard to collection technique",
            "Gray fluoride drawn last back-flushed into the green heparin tube on the same stick",
        ],
        "Extended stasis and line trauma hemolyze cells even when tube sequence is correct; heparin does not intrinsically spike potassium. "
        "Blaming order of draw alone misses tourniquet time and difficult-flow hemolysis documented in CLSI preanalytic guidance.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "The first tube attached for a BMP and coagulation panel was lavender EDTA instead of gold SST, and you notice before attaching additional tubes. "
        "What is the best response?",
        "Stop, discard the lavender tube, and restart with a new needle set following order of draw per policy",
        [
            "Continue because EDTA in the hub will not affect serum chemistry on an SST tube drawn second on the stick",
            "Send the lavender tube for BMP because total calcium uses the same tube type as serum calcium",
            "Continue the draw and submit the lavender tube for serum BMP methods to save a needle stick",
        ],
        "EDTA chelates calcium and contaminates the hub for subsequent tubes, compromising both chemistry and coagulation on the same stick. "
        "Serum BMP methods are not interchangeable with EDTA whole blood; continuing wastes the citrate tube as well.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "A NICU nurse collects a capillary heel stick into microtainers for total bilirubin on serum and a CBC on EDTA. "
        "What should guide the order those microcontainers are filled?",
        "Hospital microcollection chart, typically serum or non-additive before EDTA unless policy differs",
        [
            "Lavender EDTA first on every neonate because infants have higher hematocrit than adults on heel sticks",
            "Any fill sequence because capillary specimens are exempt from CLSI order-of-draw guidance for neonates",
            "Gray fluoride before lavender EDTA on newborn screening heel-stick collections",
        ],
        "Neonatal microcollection still limits additive carryover between tiny volumes; wrong order can ruin bilirubin or hematology on the same puncture. "
        "Universal EDTA-first or fluoride-first rules ignore test-specific laboratory manuals for microtainers.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "Home health collects blood by syringe from fragile veins; citrate and SST tubes are about thirty percent underfilled while lavender EDTA is full. "
        "Which decision aligns with CLSI principles and patient safety?",
        "Recollect coagulation and chemistry tubes and do not submit the underfilled citrate or compromised SST volumes",
        [
            "Submit all tubes because partial laboratory data is better than reporting no results",
            "Combine SST and citrate blood into one tube to reach the required fill volume",
            "Top off the citrate tube with capillary heel-stick blood to reach the manufacturer mark",
        ],
        "Underfilled citrate and inadequate SST volumes invalidate coagulation and chemistry ratios; partial submission risks clinical decisions on bad data. "
        "Combining tubes cross-contaminates additives, and capillary top-off breaks ratio control and introduces tissue fluid.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "Ionized calcium is ordered, the laboratory manual requires serum, and only a lavender EDTA tube is available in the draw kit. "
        "What should the phlebotomist do before collecting blood?",
        "Obtain the correct tube per the laboratory manual and defer collection until serum tubes are available",
        [
            "Collect in lavender EDTA because all calcium assays use the same anticoagulant tube type on the tray",
            "Collect in lavender EDTA and ask the laboratory to mathematically correct for EDTA chelation of calcium",
            "Collect in gray sodium fluoride because fluoride stabilizes ionized calcium measurements on the draw",
        ],
        "EDTA chelates calcium and makes ionized calcium uninterpretable on the wrong tube type. "
        "Gray fluoride does not reverse EDTA chelation, and laboratories cannot reliably mathematically correct ionized calcium after improper collection.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "After a power outage, a clinic draws cultures, PT, and glucose on one patient using a single butterfly set. "
        "The nurse documents a deviation because only a winged set without a holder was available, delaying citrate fill. "
        "Which details are priority to document for the laboratory?",
        "Time of draw, tubes collected, order used, equipment limitation, and notification to the laboratory for interpretation",
        [
            "The patient allergy list without reference to tubes collected or draw sequence",
            "A statement that CLSI standards do not apply during facility power outages",
            "The color of the tourniquet applied during venipuncture without tube or timing details",
        ],
        "Laboratories need draw context to judge compromised coagulation or culture specimens when equipment or sequence deviates from policy. "
        "Claiming standards do not apply during outages or omitting tube and timing data prevents appropriate result flagging and recollection decisions.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "A patient pulls away after a citrate tube is half filled and remaining ordered tubes are not collected. "
        "What should you do with that citrate tube?",
        "Discard the partial citrate tube and recollect coagulation per policy",
        [
            "Submit the partial tube for a screening prothrombin time",
            "Top off the tube from a second venipuncture using the same partial fill",
            "Finish other tubes on a second stick and send the partial citrate for testing",
        ],
        "Partial citrate fill breaks the blood-to-anticoagulant ratio and invalidates coagulation results. "
        "Topping off from another stick or mixing tubes from separate punctures introduces uncontrolled ratio and carryover errors.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "Trace-element testing on royal blue EDTA is ordered with routine lavender CBC and chemistry on SST from one venipuncture. "
        "How should tube sequence typically be handled?",
        "Follow the laboratory trace-element chart, often drawing dedicated royal blue tubes early with minimal contact to other additive tubes",
        [
            "Draw lavender CBC first because hematology is the most time-sensitive result on the requisition",
            "Draw SST chemistry first so clotting does not delay transport of the royal blue tube",
            "Fill royal blue tubes last because trace metals concentrate in the final tube on the stick",
        ],
        "Trace-element specimens are vulnerable to metal contamination from needles, hubs, and prior additive tubes. "
        "Laboratory manuals usually specify dedicated sequence and sometimes dedicated collection supplies rather than routine order-of-draw alone.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "Before venipuncture, the patient repeatedly pumps their fist while the tourniquet is applied to make veins easier to see. "
        "Which laboratory results are most likely to be affected on tubes collected during that draw?",
        "Potassium and other intracellular analytes may rise from hemolysis and local stasis artifact",
        [
            "ABO and Rh typing on a pink blood bank tube drawn later in the same sequence",
            "Prothrombin time on a properly filled citrate tube drawn first after cultures",
            "Fluoride glucose on a gray tube drawn last in the sequence",
        ],
        "Fist pumping with an inflated tourniquet increases venous pressure and hemolysis risk, elevating potassium and related flags. "
        "Assuming fist pumping helps coagulation or spares glucose while sparing chemistry is a common preanalytic error in busy draw areas.",
        [S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-order-draw",
        "A student collects a stat coagulation panel using a syringe and waits three minutes before transferring blood into the citrate tube while labeling other specimens. "
        "What is the primary concern with that delay before citrate fill?",
        "Clot formation in the syringe can consume coagulation factors and invalidate PT and aPTT on the citrate tube",
        [
            "Citrate anticoagulant loses potency after three minutes of room-air exposure in the syringe barrel",
            "Delayed transfer improves mixing so clotting times better reflect in vivo hemostasis",
            "The delay chiefly affects lavender EDTA counts but not citrate coagulation specimens",
        ],
        "Blood begins to clot in a syringe when transfer is delayed, depleting factors before the citrate tube is filled. "
        "Citrate does not reverse clotting that already occurred in the syringe, and EDTA timing rules do not replace citrate transfer urgency.",
        [S.CLSI_GP41],
        "advanced",
    ),
]
