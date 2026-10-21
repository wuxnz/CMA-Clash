# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored venipuncture site and technique questions (topic phleb-site)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_REF = [S.CLSI_GP41, S.NHA_CPT]

FACTS: list[dict] = [
    fact(
        "phleb-site",
        "Before venipuncture, patient identification should use:",
        "At least two unique identifiers verified against the order",
        [
            "Room number alone when the door chart matches",
            "First name only when the patient verbally confirms",
            "A photograph on the wristband without speaking to the patient",
        ],
        "CLSI GP41 ties safe collection to positive patient identification before any puncture. "
        "Room number or a single name fails the two-identifier standard most facilities require.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "The median cubital vein is often the first antecubital choice because it:",
        "Is usually superficial, anchored, and away from major nerves",
        [
            "Runs deep beside the radial artery in every patient",
            "Is located on the dorsum of the hand by default",
            "Must be used even when thrombosed or hardened",
        ],
        "GP41 site selection favors accessible antecubital veins with lower complication risk. "
        "The median cubital is commonly large and stable, though individual anatomy still dictates the final site.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "When assessing a vein by palpation, the phlebotomist should evaluate:",
        "Size, depth, direction, and resilience without relying on color alone",
        [
            "Skin tone only because veins always show through equally",
            "Patient shoe size as a proxy for vessel diameter",
            "Insurance type to decide which arm to use",
        ],
        "Palpation confirms a bouncy, refillable vein before skin antisepsis. "
        "Visual inspection alone misses depth and sclerosis that GP41-style assessment is meant to catch.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "A tourniquet for routine venipuncture is typically placed:",
        "Three to four inches (about 8–10 cm) above the intended puncture site",
        [
            "Distal to the puncture site below the antecubital crease",
            "Around the neck when antecubital veins are flat",
            "Directly over the selected vein to hold it still",
        ],
        "Proximal placement distends the vein without compressing the puncture field. "
        "A distal tourniquet does not support venous filling the way GP41 venipuncture technique describes.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Tourniquet time during venipuncture should generally be limited to:",
        "About one minute, releasing sooner if possible",
        [
            "Five to ten minutes until every tube is labeled",
            "As long as needed even if petechiae appear",
            "Only removed after the needle is fully withdrawn in every case",
        ],
        "Prolonged venous stasis causes hemoconcentration and can falsely shift analytes such as potassium. "
        "GP41 emphasizes minimizing tourniquet time while still allowing successful vein entry.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "For standard superficial venipuncture, needle bevel orientation is usually:",
        "Up (bevel facing upward) per facility training",
        [
            "Down against the vein floor in every patient",
            "Sideways parallel to the skin without anchoring",
            "Random because bevel direction never affects entry",
        ],
        "Bevel-up entry is the conventional technique taught for straight needles and many butterfly sets. "
        "Facility policy may vary slightly, but bevel-down insertion is not the default GP41-aligned approach.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "The recommended needle insertion angle for venipuncture is typically:",
        "15 to 30 degrees with controlled advancement",
        [
            "90 degrees perpendicular through the entire forearm",
            "Parallel to the skin surface without entering the vein",
            "45 to 60 degrees aimed toward underlying bone",
        ],
        "A shallow angle reduces the chance of puncturing the posterior vein wall. "
        "Steep or tangential angles increase hematoma risk and failed draws per venipuncture best practice.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "After initial vein entry, lowering the angle of the needle helps:",
        "Advance along the lumen and stabilize the hub",
        [
            "Lift the vein away from surrounding tissue",
            "Stop blood flow so tubes fill more slowly",
            "Force the needle through the opposite wall intentionally",
        ],
        "Shallow advancement keeps the bevel within the vein lumen during multi-tube collection. "
        "Leaving a steep angle increases movement at the hub and contributes to rolling or perforation.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Anchoring the vein during venipuncture is done by:",
        "Drawing the skin taut distal to the puncture site with the non-dominant hand",
        [
            "Pressing directly over the needle hub during insertion",
            "Slapping the antecubital fossa to wake the vein",
            "Rotating the arm rapidly while the needle advances",
        ],
        "Distal traction stabilizes the vein and limits rolling during entry. "
        "Pressure over the hub or aggressive slapping does not substitute for proper anchoring in GP41 technique.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Butterfly (winged infusion) needle sets are especially useful when:",
        "Veins are fragile, small, or require precise control",
        [
            "Large-volume cultures must be drawn with the largest bore only",
            "Arterial blood gas sampling replaces venipuncture policy",
            "Tourniquet application can be skipped entirely",
        ],
        "Smaller-gauge butterflies can reduce trauma in difficult access situations when volume needs allow. "
        "They still require the same identification, site selection, and order-of-draw rules as straight needles.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Venipuncture should be avoided on an arm that has:",
        "An active IV infusion, dialysis access, or mastectomy-side restrictions per policy",
        [
            "A band-aid on an unrelated finger on the same hand",
            "Short fingernails on the draw hand",
            "A blood pressure cuff on the opposite arm earlier that day",
        ],
        "Drawing distal to running IV fluids dilutes specimens, and fistula or lymphedema precautions protect vulnerable arms. "
        "GP41 site-selection guidance directs collectors away from compromised circulation or lymphatic risk.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Blood collection from the same side as a mastectomy with lymphedema risk:",
        "Is generally contraindicated unless the provider and policy explicitly allow it",
        [
            "Is preferred because lymph nodes are already removed",
            "Requires only a single identifier before proceeding",
            "Eliminates the need to document the chosen arm",
        ],
        "Lymphedema risk after breast surgery makes the affected arm a last-resort site. "
        "Many facilities require provider approval and meticulous documentation when no alternative exists.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Venipuncture through or immediately adjacent to a dialysis fistula or graft:",
        "Is contraindicated on that vascular access arm",
        [
            "Is encouraged to monitor access patency during every draw",
            "Requires only alcohol without notifying the care team",
            "Replaces the need for dialysis nursing assessment",
        ],
        "Puncturing an access site can thrombose or damage the fistula. "
        "GP41 and dialysis safety policies reserve those vessels for treatment, not routine laboratory draws.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When IV fluids are infusing in one arm, venipuncture on that side should:",
        "Be avoided unless a written protocol specifies discard volume and site",
        [
            "Proceed distal to the catheter without notifying anyone",
            "Use the fluid line port as the primary collection site",
            "Ignore infusion status if the patient is fasting",
        ],
        "Infused fluids dilute analytes drawn below the IV site, producing falsely lowered values. "
        "CLSI-aligned practice uses the opposite extremity or an approved discard-draw procedure.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "The basilic vein may be selected when other antecubital veins are unavailable because it:",
        "Is often larger but lies close to the medial nerve and brachial artery",
        [
            "Has no adjacent structures and needs no anchoring",
            "Is always shallower than the cephalic vein in every patient",
            "Must be chosen before the median cubital in all adults",
        ],
        "Basilic access can succeed when safer options fail, but the proximity to nerve and artery demands careful technique. "
        "GP41 training stresses skilled palpation and stabilization when using this medial antecubital vein.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Hand veins for venipuncture are appropriate when:",
        "Antecubital sites are unavailable and institutional policy permits distal draws",
        [
            "They are always preferred over antecubital veins for comfort",
            "The patient has lymphedema precautions on that extremity",
            "Hand veins are mandatory whenever blood culture bottles are ordered",
        ],
        "Distal veins may be more painful and have higher complication rates than antecubital sites. "
        "GP41 allows hand draws as a secondary option when primary sites cannot be used safely.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Foot and ankle venipuncture in adults is generally:",
        "Avoided except when no safer site exists and policy permits it",
        [
            "The default first choice for outpatient chemistry panels",
            "Required for every coagulation collection",
            "Preferred over antecubital veins to reduce bruising",
        ],
        "Foot veins carry higher risk of thrombophlebitis and are difficult to stabilize. "
        "GP41 site hierarchy reserves lower-extremity draws for exceptional situations with documented justification.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Venipuncture through an area of edema should usually be:",
        "Deferred in favor of a non-edematous site when possible",
        [
            "Preferred because fluid makes veins easier to see",
            "Performed with a larger gauge to drain interstitial fluid",
            "Completed without tourniquet regardless of vein status",
        ],
        "Edema interferes with palpation, increases leakage, and can alter analyte concentration in the specimen. "
        "Selecting a dry, accessible site aligns with GP41 emphasis on reliable access and sample quality.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "A hardened or sclerosed vein from repeated venipuncture should be:",
        "Avoided when another viable vein is available",
        [
            "Chosen first because scar tissue prevents rolling",
            "Punctured with a larger needle to break through plaque",
            "Used without documentation if the patient recognizes the site",
        ],
        "Sclerosed veins have poor flow and higher failure rates, increasing patient trauma. "
        "GP41 site assessment includes recognizing veins that will not refill or yield adequate volume.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Venipuncture should not be performed through unhealed burns or extensive scar tissue because:",
        "Healing tissue is fragile and access is unreliable",
        [
            "Scar tissue always contains arterial blood only",
            "Antiseptics are unnecessary on damaged skin",
            "Tourniquets cannot be applied near scars",
        ],
        "Damaged skin increases infection risk and makes hemostasis unpredictable. "
        "When alternatives exist, GP41-aligned collectors choose intact skin away from burns and dense scars.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "If bright red, pulsatile blood appears during venipuncture, the collector should:",
        "Stop the procedure, withdraw, and apply prolonged direct pressure",
        [
            "Continue filling tubes because arterial samples improve chemistry",
            "Massage proximally to slow the pulsation",
            "Advance deeper to confirm vein entry",
        ],
        "Arterial puncture can cause rapid hematoma and nerve injury. "
        "GP41 response includes pressure, monitoring, and notifying the clinician per facility protocol.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "After the last tube fills, the tourniquet should be released:",
        "Before needle withdrawal in routine venipuncture practice",
        [
            "Only after the patient leaves the draw chair",
            "Never once it has been applied",
            "After needle removal while pressure is withheld",
        ],
        "Removing the tourniquet before withdrawal limits venous pressure and hematoma formation. "
        "Some facilities release after the final tube but still before needle exit; either way, prolonged tourniquet during withdrawal is avoided.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Post-venipuncture hemostasis should include:",
        "Firm pressure with a clean gauze pad until bleeding stops",
        [
            "Immediate heavy lifting with the draw arm",
            "Removing the dressing in the parking lot to air the site",
            "No pressure when the patient is on anticoagulants",
        ],
        "Adequate pressure prevents hematoma, especially in anticoagulated patients who may need longer hold times. "
        "GP41 aftercare includes patient instructions about keeping the bandage in place briefly and reporting ongoing bleeding.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "A warm compress proximal to a difficult venipuncture site may:",
        "Promote venodilation when ordered and policy allows",
        [
            "Replace skin antisepsis and hand hygiene",
            "Eliminate the need for a tourniquet in every patient",
            "Guarantee arterial blood for culture bottles",
        ],
        "Heat can improve venous filling when veins are collapsed from cold or dehydration. "
        "It supplements, rather than replaces, standard GP41 preparation and infection prevention steps.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "During venipuncture, the patient arm is best supported:",
        "Extended downward with the antecubital area supported on a surface when tolerated",
        [
            "Hyperflexed tightly with fist clenched the entire draw",
            "Held overhead above heart level to reduce bleeding",
            "Resting on a vibrating transport cart during tube changes",
        ],
        "Dependent positioning encourages venous filling without sustained muscle tension. "
        "A tight fist throughout the draw can falsely elevate potassium and is not recommended in GP41 technique.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Palpation for vein selection should occur:",
        "Before skin antisepsis so the prep site is not contaminated by assessment",
        [
            "Only after alcohol has fully dried to avoid feeling the vein",
            "Through the sterile field with the same gloved hand used on equipment",
            "After all tubes are filled to confirm successful entry",
        ],
        "Assessment identifies site and direction, then antiseptic is applied to the chosen area. "
        "Re-palpating a prepped site without policy guidance risks contaminating the puncture field.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "After applying alcohol or chlorhexidine, the prep site should:",
        "Be allowed to air-dry completely before venipuncture",
        [
            "Be wiped dry immediately with non-sterile gauze",
            "Be blown on to speed drying without waiting",
            "Be covered with lotion to reduce sting",
        ],
        "Wet antiseptic can carry organisms into the puncture tract and may cause stinging or hemolysis. "
        "GP41 infection-control steps include contact time and drying per manufacturer instructions.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Heel stick capillary sampling in infants is used for:",
        "Small-volume collections when policy and device limits allow",
        [
            "Multi-tube adult-style blood cultures in newborns",
            "Unlimited volume draws without warming the heel",
            "Routine venous-equivalent coagulation studies",
        ],
        "Heel sticks follow strict depth and site-rotation rules to protect bone and soft tissue. "
        "GP41 capillary guidance limits volume and requires appropriate warming and device selection.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Fingerstick capillary specimens are appropriate when:",
        "The ordered test is approved for capillary volume and device specifications",
        [
            "Multiple large culture bottles must be filled from a fingertip",
            "Coagulation studies require citrate tubes from a finger",
            "Any test ordered can be collected capillary without a manual check",
        ],
        "Capillary draws have volume and analyte limits defined by the laboratory and instrument manufacturer. "
        "GP41 directs collectors to confirm test suitability before choosing a fingerstick site.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Many laboratory two-attempt policies require that after two unsuccessful venipunctures:",
        "Another qualified collector or supervisor is consulted per policy",
        [
            "The same collector continues until success without limit",
            "The patient is discharged without notifying the provider",
            "A larger needle is mandated in the identical spot",
        ],
        "Limiting attempts reduces hematoma, nerve injury, and patient anxiety. "
        "GP41-aligned programs document attempts and escalate when access remains unsuccessful.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Needle gauge selection balances:",
        "Vein size, required volume, and minimizing hemolysis",
        [
            "Always using the largest bore regardless of vein fragility",
            "Choosing the smallest gauge that cannot yield required volume",
            "Random gauge assignment to train on every size each visit",
        ],
        "Large needles in small veins increase trauma and hemolysis; tiny needles may prolong draw time and clot in the line. "
        "GP41 training matches gauge to test requirements and vessel condition.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "If blood flow stops during a multi-tube draw, the first action is to:",
        "Gently reposition the needle or evaluate tourniquet tightness within policy",
        [
            "Forcefully advance the needle through the opposite vein wall",
            "Remove all tubes and abandon the order without documentation",
            "Increase tourniquet pressure until arterial flow appears",
        ],
        "Minor hub movement or vein collapse often restores flow without a new puncture. "
        "When flow cannot be re-established safely, GP41 practice favors stopping rather than repeated blind probing.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Venipuncture at a site with an existing hematoma should be:",
        "Avoided because blood extravasates and veins are difficult to palpate",
        [
            "Preferred because pooled blood makes veins visible",
            "Performed through the center of the bruise to drain it",
            "Completed without pressure afterward to assess leakage",
        ],
        "Hematoma indicates prior vessel injury and unreliable access. "
        "Selecting an uninjured site improves success and aligns with GP41 complication-prevention goals.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Chemotherapy or vesicant infusion history in an arm means venipuncture there should:",
        "Follow oncology and facility policy, often using the opposite extremity",
        [
            "Proceed routinely because prior drugs no longer matter",
            "Use only butterfly needles without provider input",
            "Skip patient identification if the oncology chart is available",
        ],
        "Compromised veins from prior vesicant exposure may extravasate easily or lack durable access. "
        "GP41 site selection integrates specialty precautions beyond standard antecubital assessment.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Drawing blood from an arm with a cast or splint covering the antecubital area:",
        "Requires provider approval and an alternative site outside the immobilized field",
        [
            "Is done by puncturing through the cast material",
            "Is impossible so the order should be canceled silently",
            "Uses the same arm without documenting the cast",
        ],
        "Casts block visualization, stabilization, and hemostasis monitoring. "
        "When access is urgent, clinicians authorize a safe alternative per GP41 and institutional rules.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Blind venipuncture without palpating or visualizing a vein is:",
        "Not acceptable standard practice for routine diagnostic collection",
        [
            "Encouraged in experienced collectors to save time",
            "Required for every stat order after hours",
            "Preferred when the patient is anxious about touch",
        ],
        "Successful venipuncture depends on deliberate site assessment and patient preparation. "
        "GP41 emphasizes visible or palpable vein confirmation before skin antisepsis and entry.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When petechiae appear above the tourniquet, the collector should:",
        "Release or loosen the tourniquet and reassess application",
        [
            "Tighten the tourniquet until petechiae disappear",
            "Ignore them because they always indicate infection",
            "Move the tourniquet distal to the puncture site",
        ],
        "Petechiae suggest excessive venous pressure or prolonged application. "
        "Adjusting or removing the tourniquet protects capillaries and keeps preanalytic conditions stable.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "The cephalic vein in the antecubital fossa is often chosen because it:",
        "Lies more laterally with relatively easy access in many patients",
        [
            "Is always the deepest antecubital vein",
            "Cannot be used if the median cubital is visible",
            "Runs with the ulnar nerve on the medial arm only",
        ],
        "Cephalic anatomy varies, but the lateral antecubital position is a common secondary option. "
        "GP41 training still requires palpation to confirm suitability before puncture.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Instructing a patient to pump the fist repeatedly during the entire draw:",
        "Should be avoided because it can falsely elevate potassium",
        [
            "Is required to keep every vein distended for ten minutes",
            "Replaces tourniquet application in obese patients",
            "Is mandatory for coagulation tube filling",
        ],
        "Intermittent fist clenching may help initial venous filling, but sustained pumping alters analytes. "
        "GP41 technique uses brief opening and closing of the hand rather than prolonged vigorous pumping.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When a patient reports syncope during venipuncture, the collector should:",
        "Safely abort or complete the draw per protocol, lower the patient, and summon help",
        [
            "Continue quickly before the patient fully loses consciousness",
            "Leave the patient unattended to fetch tubes",
            "Apply a tourniquet tighter to finish the last tube",
        ],
        "Vasovagal reactions are a known phlebotomy complication requiring injury prevention and monitoring. "
        "GP41 patient-care steps include positioning, reassurance, and documentation of the event.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Venipuncture on the same arm as a previous episode of thrombophlebitis should:",
        "Be avoided when another site is available",
        [
            "Be mandatory to monitor healing of the inflamed vein",
            "Use a larger gauge to break through the clot",
            "Proceed without documentation if the vein looks normal",
        ],
        "Inflamed veins are prone to recurrence and poor healing after additional trauma. "
        "GP41 site selection favors unused vessels on the contralateral arm when possible.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "For obese patients with deep antecubital veins, helpful techniques include:",
        "Proper positioning, palpation, and policy-approved adjuncts such as warmth",
        [
            "Skipping identification because veins are difficult",
            "Using a foot vein before attempting the arm",
            "Applying maximal tourniquet pressure for ten minutes",
        ],
        "Depth increases the need for careful palpation and stabilization, not shortcuts in safety steps. "
        "GP41 supports adjuncts and experienced collectors while maintaining identification and infection control.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Labeling tubes at the bedside immediately after collection:",
        "Reduces mislabeling risk before leaving the patient",
        [
            "Can wait until the end of the shift for batch labeling",
            "Should use pre-labeled tubes prepared for a different patient",
            "Is optional for stat orders when the lab is busy",
        ],
        "Bedside labeling ties the specimen to the identified patient at the point of care. "
        "GP41 preanalytic safety treats mislabeled tubes as a serious patient-identification error.",
        _REF,
        "beginner",
    ),
]
