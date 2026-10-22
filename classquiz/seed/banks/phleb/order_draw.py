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
        "To limit additive carryover that spoils coagulation and chemistry results",
        [
            "To match the tube order to the stopper size on the collection tray",
            "To keep the tourniquet on until every one of the tubes is filled",
            "Because the stopper color shows the storage shelf rather than the draw sequence",
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
            "In a convenient order because the tube sequence does not alter cultures",
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
            "Gold or tiger-top serum separator tube ahead of the citrate tube",
            "Lavender EDTA tube before the other additive tubes on the same stick",
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
        "Right after blood cultures and before the serum and additive tubes",
        [
            "As the last tube after the gray fluoride tube in the teaching order used",
            "Before blood cultures when prothrombin time is ordered",
            "Used on solitary citrate draws with no other tubes on the same stick",
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
        "Do not use either tube; recollect the specimens and document the error",
        [
            "Invert both tubes gently and submit them because additives will equilibrate",
            "Add the sterile saline to the underfilled tube until it reaches the mark",
            "Centrifuge the overfilled tube and send the plasma portion of it alone",
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
        "One patient, one use, with disposal in an approved sharps container",
        [
            "Wiped with alcohol between patients when the hub appears clean",
            "Recapped by hand and stored in a drawer for the next draw",
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
        "Verify identity with at least two identifiers at the bedside",
        [
            "Choose tube colors from the requisition without confirming the name",
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
        "Fill to the mark so the blood-to-additive ratio is correct",
        [
            "Visible blood in the tube meets the fill requirement for coagulation testing",
            "Fill above the mark to guarantee enough plasma for the repeat analysis",
            "Underfill on the difficult veins and send it without notifying the laboratory",
        ],
        "Citrate tubes depend on a fixed blood-to-anticoagulant ratio; underfills dilute anticoagulant relative to plasma. "
        "Overfilling seems helpful for repeat testing but is equally invalid under CLSI coagulation guidance.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "When should tube labels be applied relative to venipuncture and leaving the patient?",
        "At the bedside during or right after the collection",
        [
            "After centrifugation at the central laboratory bench",
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
        "When several tubes or prior additive exposure share one needle stick",
        [
            "On every venipuncture even when just a single tube is ordered",
            "For the arterial collections but not for the routine peripheral venous draws",
            "For the pediatric heel sticks but not for the adult antecubital venipuncture",
        ],
        "Carryover requires more than one tube in the set; a solitary EDTA draw has no prior additive in the line. "
        "Over-applying order rules can delay urgent single-tube collections without improving specimen quality.",
        [S.CLSI_GP41],
        "beginner",
    ),
    fact(
        "phleb-order-draw",
        "Coagulation tests are ordered without serum tubes. Why might a non-additive discard tube precede light blue citrate?",
        "To clear dead space so tissue thromboplastin does not shorten clotting times",
        [
            "Because the citrate tubes are prohibited from being first on the draw list",
            "To dilute the citrate anticoagulant so the mixing is easier in underfilled tubes",
            "Because the discard tubes contain EDTA to prevent clotting in the adapter",
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
        "Heparin carryover that interferes with the citrate coagulation tests",
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
        "To reduce stasis, clot formation in the tubing, and underfilled tubes",
        [
            "To draw the air into the tubing so the vacuum tubes fill more quickly",
            "To keep the tourniquet maximally tight until the final tube disconnects from it",
            "To dry the needle bore between the tubes and reduce the hub contamination",
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
            "A convenient transfer sequence because the syringe plastic binds the additives",
            "Serum tubes after the additive tubes when the tests share one stick",
            "Citrate first after the cultures even when the transfer delay is long",
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
        "Consult the laboratory manual or supervisor; document the deviation",
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
        "A laboratory-approved order of draw to limit additive carryover",
        [
            "No sequence rules because the pediatric microvolumes are too small for carryover",
            "Culture tubes last on the stick even when the sterile cultures were filled first",
            "Lavender EDTA before the citrate because the infants clot more quickly",
        ],
        "Small volumes magnify ratio errors, and microtainers follow the same carryover principles as adult evacuated tubes. "
        "Assuming volume exempts pediatrics from sequence is a common teaching gap on CLSI-aligned order-of-draw charts.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Tubes for a coagulation and CBC panel were filled in reverse order. What should the phlebotomist do?",
        "Notify the laboratory promptly and recollect the affected specimens",
        [
            "Relabel the tubes to reflect the intended order and submit them for testing",
            "Add the saline to the citrate tube to restore the blood-to-anticoagulant ratio",
            "Freeze all of the tubes immediately to halt the further additive interaction",
        ],
        "Relabeling does not remove additive contamination already present in the specimens. "
        "Saline dilution or freezing cannot restore valid coagulation ratios once carryover occurs.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Why should routine non-culture tubes not be filled before blood cultures when both are required on one stick?",
        "Non-sterile hub flow can introduce skin organisms and false-positive cultures",
        [
            "The culture bottles cannot withstand the vacuum pressure from the tubes",
            "The routine additive tubes contain broth that sterilizes organisms in the media",
            "CLSI limits the blood cultures to arterial puncture sites",
        ],
        "Sterile culture technique requires filling bottles before hub contamination from other tubes. "
        "Believing routine tubes protect cultures or that cultures must be arterial misstates CLSI venipuncture practice.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "After filling a lavender EDTA tube, a student shakes it vigorously for about 30 seconds. Why is that mixing technique inappropriate?",
        "It can hemolyze red cells and falsely elevate potassium and other analytes",
        [
            "It can hemolyze the red cells and falsely lower the potassium",
            "It improves the platelet dispersion so the automated counts match the smears",
            "It is required because the lavender tubes contain clot activator for the serum",
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
            "Before the sterile blood cultures so the serum clots before other additives",
            "Before the light blue citrate whenever a chemistry panel is on the requisition",
            "Immediately after the gray-top fluoride tubes in the standard teaching sequence",
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
        "Yes, because carryover rules apply when several tubes share a stick",
        [
            "No, the lavender EDTA must precede the citrate on every venipuncture",
            "Yes, but a gray-top fluoride tube must be collected first to stabilize it",
            "No, the citrate cannot serve as the solitary tube during outpatient draws",
        ],
        "A single citrate draw has no prior additive in the line, so multi-tube sequencing rules do not apply. "
        "Requiring lavender or gray before a lone citrate tube misextends carryover guidance from composite draws.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "When pink-top EDTA blood bank tubes are included in a multi-tube venipuncture, when are they typically filled?",
        "On the facility blood bank chart, after culture, citrate, and serum steps",
        [
            "Before the sterile blood cultures to preserve the ABO typing antigens",
            "From the arterial catheters exclusively rather than the routine venipuncture",
            "After the gray-top fluoride tubes because the ABO typing needs it",
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
        "Hemoconcentration with artifactually elevated protein-bound analytes",
        [
            "Improved citrate mixing that makes the PT reflect the in vivo clotting",
            "No measurable preanalytic effect once the bedside labels are applied",
            "The selective distortion of the urine drug screens collected later the same day",
        ],
        "CLSI recommends limiting tourniquet time because extended venous stasis concentrates analytes in the limb. "
        "Assuming labels fix stasis effects or that tourniquet time affects urine but not venous chemistry ignores documented hemoconcentration.",
        [S.CLSI_GP41],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "Midway through a multi-tube venipuncture you see clot in the needle hub. What is the appropriate next step?",
        "Stop, discard the collection set, and recollect the specimens",
        [
            "Flush the visible clot forward into the next lavender EDTA tube",
            "Attach more vacuum tubes until the clot passes and flow resumes",
            "Continue the draw if the light blue citrate tube already reached the mark",
        ],
        "Clot in the hub invalidates hematology specimens and may prevent proper fills on remaining tubes. "
        "Flushing clot into EDTA contaminates the CBC, and continuing after a compromised line risks cascading erroneous results.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-order-draw",
        "When transferring blood from a syringe through a device that pierces tube stoppers, what injection-safety rule applies to that transfer device?",
        "Use a new sterile device for each patient and tube set",
        [
            "Reuse the same transfer needle on multiple patients between the sticks",
            "Reserve the transfer devices for the glass tubes, not the plastic stoppers",
            "Rinse the transfer needle with the alcohol between the patients",
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
        "Treat results as suspect for EDTA carryover and require recollection",
        [
            "Accept the results as valid if the citrate tube was inverted enough times",
            "Accept the results as valid when the patient is not taking an anticoagulant",
            "Accept the results as valid if a gold SST tube was drawn between the tubes",
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
        "Discard the underfilled citrate tube and recollect coagulation studies",
        [
            "Send the underfilled citrate with a difficult-vein comment on the request",
            "Add the sterile saline to the fill mark before inverting the citrate tube",
            "Invert the citrate tube vigorously to concentrate the plasma for testing",
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
        "Cultures, then citrate, SST or serum, heparin, EDTA, and gray fluoride last",
        [
            "The gray fluoride first for glucose, then cultures, citrate, lavender, and SST",
            "The lavender EDTA, cultures, citrate, SST, and gray fluoride in that order",
            "The SST before the cultures because the chemistry panel is marked stat",
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
        "Discontinue the draw, dispose of the set, and restart with new equipment",
        [
            "Push the sterile saline through the valve to flush the fibrin into a waste tube",
            "Attach the citrate tube anyway and increase the inversion time after the draw",
            "Switch to a larger-gauge needle but keep using the same tubing set",
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
        "Verify each tube met fill volume, especially the citrate ratio",
        [
            "That all of the tubes were labeled with the patient name before the venipuncture",
            "That the collection syringe was heparin-coated to stabilize the chemistry",
            "That the blood cultures were omitted because syringes cannot fill the bottles",
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
        "Wash the wound, report the exposure promptly, and follow the exposure protocol",
        [
            "Finish the remaining tube draws first, then wash the wound and report it later",
            "Apply a bandage when the blood is visible and defer the health notice",
            "Wait twenty-four hours for the symptoms, then report and request the follow-up",
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
        "Obtain new cultures with sterile technique instead of using the used needle",
        [
            "Notify the laboratory and attach the bottles to the existing needle",
            "Cancel the culture order and document that the routine tubes contaminated it",
            "Submit the SST aliquot for the culture incubation because it holds blood",
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
        "Fill a non-additive discard tube first, then fill both citrate tubes",
        [
            "Fill one citrate tube and split the specimen after the centrifugation",
            "Use a lavender EDTA tube as the discard because it is also an anticoagulant",
            "Omit the discard tube because both citrate tubes share the stopper color",
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
        "Prolonged venous stasis and hemolysis from the difficult flow",
        [
            "The correct order of draw prevents the hemolysis even with a long tourniquet",
            "The heparin additive independently raises the plasma potassium without regard",
            "The gray fluoride drawn last and back-flushed into the green tube",
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
        "Stop, discard the lavender tube, and restart with a new needle set",
        [
            "Continue because the EDTA in the hub will not affect the SST chemistry",
            "Send the lavender tube for the BMP because the calcium uses the same tube type",
            "Continue the draw and submit the lavender tube for the serum BMP methods",
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
        "Hospital microcollection chart, with serum filled before EDTA",
        [
            "The lavender EDTA first because the neonate has a higher hematocrit",
            "A convenient sequence because capillary specimens are exempt from rules",
            "The gray fluoride before the lavender EDTA on the newborn screening sticks",
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
        "Recollect the coagulation and chemistry tubes, do not submit them",
        [
            "Submit all of the tubes because the partial data is better than no results",
            "Combine the SST and the citrate blood into one tube to reach the fill volume",
            "Top off the citrate tube with the capillary heel-stick blood to reach the mark",
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
        "Obtain the correct tube per the lab manual and defer the collection",
        [
            "Collect in the lavender EDTA because all of the calcium assays use that tube",
            "Collect in the lavender EDTA and ask the lab to correct the calcium chelation",
            "Collect in the gray sodium fluoride because it stabilizes the ionized calcium",
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
        "Time of draw, tubes collected, order used, and lab notification",
        [
            "The patient allergy list with no reference to the tubes or the sequence",
            "A statement that the CLSI standards do not apply during the facility outages",
            "The color of the tourniquet applied during the venipuncture alone",
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
        "Discard the partial citrate tube and recollect coagulation studies",
        [
            "Submit the partial tube for a screening prothrombin time result",
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
        "Follow the laboratory trace-element chart for the royal blue tubes",
        [
            "Draw the lavender CBC first because the hematology is most time-sensitive",
            "Draw the SST chemistry first so the clotting does not delay the royal blue tube",
            "Fill the royal blue tubes last because the trace metals concentrate in it",
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
        "Potassium and other intracellular analytes may rise from hemolysis",
        [
            "The ABO and Rh typing on a pink blood bank tube drawn later in the sequence",
            "The prothrombin time on a properly filled citrate tube drawn first",
            "The fluoride glucose on a gray tube drawn last in the sequence",
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
        "Clot formation in the syringe can consume the coagulation factors",
        [
            "The citrate anticoagulant loses potency after three minutes of the room air",
            "The delayed transfer improves the mixing so the clotting times reflect more",
            "The delay chiefly affects the lavender EDTA counts but not the citrate tubes",
        ],
        "Blood begins to clot in a syringe when transfer is delayed, depleting factors before the citrate tube is filled. "
        "Citrate does not reverse clotting that already occurred in the syringe, and EDTA timing rules do not replace citrate transfer urgency.",
        [S.CLSI_GP41],
        "advanced",
    ),
]
