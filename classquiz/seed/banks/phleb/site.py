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
        "Which identifiers should be used for patient identification before venipuncture?",
        "At least two unique identifiers verified against the order",
        [
            "Room number alone when the door chart matches",
            "First name when the patient verbally confirms",
            "A photograph on the wristband without speaking to the patient",
        ],
        "CLSI GP41 ties safe collection to positive patient identification before any puncture. "
        "Room number or a single name fails the two-identifier standard most facilities require.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Why is the median cubital vein often the first antecubital choice?",
        "Is superficial, anchored, and away from major nerves",
        [
            "Runs deep beside the radial artery in a smaller group of patients",
            "Is located on the dorsum of the hand in most patients",
            "Must be used even when the vein is thrombosed or hardened",
        ],
        "GP41 site selection favors accessible antecubital veins with lower complication risk. "
        "The median cubital is commonly large and stable, though individual anatomy still dictates the final site.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "When assessing a vein by palpation, the phlebotomist should evaluate?",
        "Size, depth, direction, and resilience without relying on color alone",
        [
            "Skin tone because veins show through with the same clarity in each patient",
            "Patient shoe size as a proxy for vessel diameter in the arm",
            "Insurance type to decide which arm should be used for the draw",
        ],
        "Palpation confirms a bouncy, refillable vein before skin antisepsis. "
        "Visual inspection alone misses depth and sclerosis that GP41-style assessment is meant to catch.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Where is a tourniquet for routine venipuncture typically placed?",
        "Three to four inches (about 8, 10 cm) above the intended puncture site",
        [
            "Placed distal to the puncture site below the antecubital crease of the arm",
            "Placed around the neck when the antecubital veins are flat",
            "Placed directly over the selected vein to hold it still",
        ],
        "Proximal placement distends the vein without compressing the puncture field. "
        "A distal tourniquet does not support venous filling the way GP41 venipuncture technique describes.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "What tourniquet time during venipuncture should generally be limited to what duration?",
        "About one minute, releasing sooner if possible",
        [
            "Five to ten minutes until every tube is labeled",
            "As long as needed even if petechiae appear",
            "Removed after the needle is fully withdrawn in every case",
        ],
        "Prolonged venous stasis causes hemoconcentration and can falsely shift analytes such as potassium. "
        "GP41 emphasizes minimizing tourniquet time while still allowing successful vein entry.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "For standard superficial venipuncture, what is the usual needle bevel orientation?",
        "Up, with the bevel facing upward during entry",
        [
            "Down against the vein floor as the default approach",
            "Sideways parallel to the skin surface without anchoring",
            "An arbitrary choice because bevel direction does not matter",
        ],
        "Bevel-up entry is the conventional technique taught for straight needles and many butterfly sets. "
        "Bevel-down insertion against the vein floor, a sideways approach without anchoring, and treating the direction as arbitrary are not the taught technique.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What is the recommended needle insertion angle for venipuncture?",
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
        "After initial vein entry, how does lowering the angle of the needle help?",
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
        "How is the vein anchored during venipuncture?",
        "Drawing the skin taut distal to the puncture site with the free hand",
        [
            "Pressing directly over the needle hub during the initial venipuncture insertion",
            "Slapping the antecubital fossa to wake up the vein",
            "Rotating the arm rapidly while the needle is advancing",
        ],
        "Distal traction stabilizes the vein and limits rolling during entry. "
        "Pressure over the hub or aggressive slapping does not substitute for proper anchoring in GP41 technique.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "What butterfly (winged infusion) needle sets are especially useful when?",
        "Veins are fragile, small, or require precise control",
        [
            "Large-volume cultures must be drawn with the largest bore",
            "Arterial blood gas sampling replaces venipuncture policy",
            "Tourniquet application can be skipped during the draw",
        ],
        "Smaller-gauge butterflies can reduce trauma in difficult access situations when volume needs allow. "
        "They still require the same identification, site selection, and order-of-draw rules as straight needles.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What venipuncture should be avoided on an arm that has what conditions?",
        "An active IV infusion, dialysis access, or mastectomy-side restrictions",
        [
            "A small adhesive bandage on another digit of the hand used for the draw",
            "Short-trimmed nails on the hand used for the venipuncture",
            "A blood pressure cuff on the opposite arm earlier in the day",
        ],
        "Drawing distal to running IV fluids dilutes specimens, and fistula or lymphedema precautions protect vulnerable arms. "
        "GP41 site-selection guidance directs collectors away from compromised circulation or lymphatic risk.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "How should blood collection from the same side as a mastectomy with lymphedema risk be handled?",
        "Is contraindicated unless the provider and policy explicitly allow it",
        [
            "Is preferred because the axillary lymph nodes have already been removed",
            "Requires a single identifier before the procedure proceeds",
            "Eliminates the need to document the arm that was used",
        ],
        "Lymphedema risk after breast surgery makes the affected arm a last-resort site. "
        "Many facilities require provider approval and meticulous documentation when no alternative exists.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Why should venipuncture through or immediately adjacent to a dialysis fistula or graft be avoided?",
        "Is contraindicated on that vascular access arm",
        [
            "Is encouraged to monitor access patency during every draw",
            "Requires alcohol prep without notifying the care team",
            "Replaces the need for dialysis nursing assessment",
        ],
        "Puncturing an access site can thrombose or damage the fistula. "
        "GP41 and dialysis safety policies reserve those vessels for treatment, not routine laboratory draws.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When IV fluids are infusing in one arm, how should venipuncture on that side be handled?",
        "Be avoided unless a written protocol specifies discard volume and site",
        [
            "Proceed distal to the catheter without notifying the nursing staff on the unit",
            "Use the fluid line port as the primary collection site for the draw",
            "Ignore the infusion status if the patient is fasting for labs",
        ],
        "Infused fluids dilute analytes drawn below the IV site, producing falsely lowered values. "
        "CLSI-aligned practice uses the opposite extremity or an approved discard-draw procedure.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Why may the basilic vein be selected when other antecubital veins are unavailable?",
        "Is larger but lies close to the medial nerve and artery",
        [
            "Has no adjacent structures nearby and needs no anchoring",
            "Is usually shallower than the cephalic vein in most adult patients",
            "Must be chosen before the median cubital vein in most adults",
        ],
        "Basilic access can succeed when safer options fail, but the proximity to nerve and artery demands careful technique. "
        "GP41 training stresses skilled palpation and stabilization when using this medial antecubital vein.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What hand veins for venipuncture are appropriate when?",
        "Antecubital sites are unavailable and policy permits distal draws",
        [
            "They are usually preferred over antecubital veins for patient comfort",
            "The patient has lymphedema precautions in place on that extremity",
            "Hand veins are required whenever blood culture bottles are ordered on the unit",
        ],
        "Distal veins may be more painful and have higher complication rates than antecubital sites. "
        "GP41 allows hand draws as a secondary option when primary sites cannot be used safely.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What foot and ankle venipuncture in adults is generally handled how?",
        "Avoided except when no safer site exists and policy permits it",
        [
            "The default first choice for routine outpatient chemistry panels",
            "Required for coagulation collections in difficult draws",
            "Preferred over antecubital veins because they bruise less often",
        ],
        "Foot veins carry higher risk of thrombophlebitis and are difficult to stabilize. "
        "GP41 site hierarchy reserves lower-extremity draws for exceptional situations with documented justification.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "What venipuncture through an area of edema should usually be avoided when?",
        "Deferred in favor of a non-edematous site when possible",
        [
            "Preferred because pooled fluid makes the veins easier to see",
            "Performed with a larger gauge to drain the interstitial fluid",
            "Completed without a tourniquet no matter the vein status",
        ],
        "Edema interferes with palpation, increases leakage, and can alter analyte concentration in the specimen. "
        "Selecting a dry, accessible site aligns with GP41 emphasis on reliable access and sample quality.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "How should a hardened or sclerosed vein from repeated venipuncture be managed?",
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
        "Why venipuncture should not be performed through unhealed burns or extensive scar tissue for what reason?",
        "Healing tissue is fragile and access is unreliable",
        [
            "Scar tissue is highly vascular so the puncture is safer",
            "Antiseptics are unnecessary on damaged or burned skin",
            "Tourniquets cannot be applied near areas of scar tissue",
        ],
        "Damaged skin increases infection risk and makes hemostasis unpredictable. "
        "When alternatives exist, GP41-aligned collectors choose intact skin away from burns and dense scars.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "If bright red, pulsatile blood appears during venipuncture, what should the collector do?",
        "Stop the procedure, withdraw, and apply prolonged direct pressure",
        [
            "Continue filling the tubes because arterial samples improve the chemistry",
            "Massage proximally to slow the pulsation of the vessel",
            "Advance deeper to confirm that the vein was entered",
        ],
        "Arterial puncture can cause rapid hematoma and nerve injury. "
        "GP41 response includes pressure, monitoring, and notifying the clinician per facility protocol.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "After the last tube fills, the tourniquet should be released?",
        "Before needle withdrawal in routine venipuncture practice",
        [
            "After the patient leaves the draw chair and is discharged",
            "At the point when it has been applied and not at an earlier time",
            "After needle removal while direct pressure is withheld",
        ],
        "Removing the tourniquet before withdrawal limits venous pressure and hematoma formation. "
        "Some facilities release after the final tube but still before needle exit; either way, prolonged tourniquet during withdrawal is avoided.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "What post-venipuncture hemostasis should include what steps?",
        "Firm pressure with a clean gauze pad until bleeding stops",
        [
            "Immediate heavy lifting with the arm used for the draw",
            "Removing the dressing in the parking lot to air out the site",
            "No pressure when the patient takes anticoagulant medication",
        ],
        "Adequate pressure prevents hematoma, especially in anticoagulated patients who may need longer hold times. "
        "GP41 aftercare includes patient instructions about keeping the bandage in place briefly and reporting ongoing bleeding.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "A warm compress proximal to a difficult venipuncture site may?",
        "Promote venodilation when ordered and policy allows",
        [
            "Replace the skin antisepsis and hand hygiene steps",
            "Eliminate the need for a tourniquet in most patients",
            "Guarantee arterial blood for the culture bottle draws",
        ],
        "Heat can improve venous filling when veins are collapsed from cold or dehydration. "
        "It supplements, rather than replaces, standard GP41 preparation and infection prevention steps.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "During venipuncture, the patient arm is best supported?",
        "Extended downward with the antecubital area supported when tolerated",
        [
            "Hyperflexed tightly with the fist clenched throughout the entire draw",
            "Held overhead above heart level to reduce the bleeding at the site",
            "Resting on a vibrating transport cart during the tube changes",
        ],
        "Dependent positioning encourages venous filling without sustained muscle tension. "
        "A tight fist throughout the draw can falsely elevate potassium and is not recommended in GP41 technique.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "When should palpation for vein selection take place?",
        "Before skin antisepsis so the prep site stays uncontaminated",
        [
            "After the alcohol has fully dried to avoid feeling the vein",
            "Through the sterile field with the same gloved hand used on equipment",
            "After all of the tubes are filled to confirm successful entry",
        ],
        "Assessment identifies site and direction, then antiseptic is applied to the chosen area. "
        "Re-palpating a prepped site without policy guidance risks contaminating the puncture field.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "After applying alcohol or chlorhexidine, how should the prep site be handled?",
        "Be allowed to air-dry completely before venipuncture",
        [
            "Be wiped dry immediately with non-sterile gauze square pads",
            "Be blown on to speed the drying without waiting",
            "Be covered with lotion to reduce the sting at the site",
        ],
        "Wet antiseptic can carry organisms into the puncture tract and may cause stinging or hemolysis. "
        "GP41 infection-control steps include contact time and drying per manufacturer instructions.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What heel stick capillary sampling in infants is used for what?",
        "Small-volume collections when policy and device limits allow",
        [
            "Multi-tube adult-style blood culture sets in newborn infants",
            "Unlimited volume draws without warming the heel site first",
            "Routine venous-equivalent coagulation studies in young infants",
        ],
        "Heel sticks follow strict depth and site-rotation rules to protect bone and soft tissue. "
        "GP41 capillary guidance limits volume and requires appropriate warming and device selection.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What fingerstick capillary specimens are appropriate when?",
        "The ordered test is approved for capillary volume and device limits",
        [
            "Multiple large culture bottles must be filled from the fingertip site",
            "Coagulation studies require the citrate tubes from a finger",
            "An ordered test can be collected by capillary without a manual check",
        ],
        "Capillary draws have volume and analyte limits defined by the laboratory and instrument manufacturer. "
        "GP41 directs collectors to confirm test suitability before choosing a fingerstick site.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What do many laboratory two-attempt policies require after two unsuccessful venipunctures?",
        "Another qualified collector or supervisor takes over the draw",
        [
            "The same collector continues until success without a set attempt limit",
            "The patient is discharged without notifying the ordering provider",
            "A larger needle is mandated for the identical puncture site",
        ],
        "Limiting attempts reduces hematoma, nerve injury, and patient anxiety. "
        "GP41-aligned programs document attempts and escalate when access remains unsuccessful.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What needle gauge selection balances what factors?",
        "Vein size, required volume, and minimizing hemolysis",
        [
            "Using the largest bore even when the vein is fragile",
            "Choosing the smallest gauge that cannot yield the required volume",
            "An arbitrary gauge assignment to train on each size at each visit",
        ],
        "Large needles in small veins increase trauma and hemolysis; tiny needles may prolong draw time and clot in the line. "
        "GP41 training matches gauge to test requirements and vessel condition.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "If blood flow stops during a multi-tube draw, what should the collector do first?",
        "Gently reposition the needle or check the tourniquet tightness",
        [
            "Forcefully advance the needle through the opposite wall of the vein",
            "Remove all of the tubes and abandon the order without documentation",
            "Increase the tourniquet pressure until arterial flow appears",
        ],
        "Minor hub movement or vein collapse often restores flow without a new puncture. "
        "When flow cannot be re-established safely, GP41 practice favors stopping rather than repeated blind probing.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "How should venipuncture at a site with an existing hematoma be managed?",
        "Avoided because blood leaks out and veins are hard to palpate",
        [
            "Preferred because the pooled blood makes the veins easier to see",
            "Performed through the center of the bruise to drain the blood",
            "Completed without pressure afterward to assess for leakage",
        ],
        "Hematoma indicates prior vessel injury and unreliable access. "
        "Selecting an uninjured site improves success and aligns with GP41 complication-prevention goals.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "What does a chemotherapy or vesicant infusion history in an arm mean for venipuncture there?",
        "Draw from the opposite arm under the oncology policy",
        [
            "Proceed routinely because the prior drugs no longer matter",
            "Use butterfly needles without provider input or guidance",
            "Continue without the identification step if the chart is available",
        ],
        "Compromised veins from prior vesicant exposure may extravasate easily or lack durable access. "
        "GP41 site selection integrates specialty precautions beyond standard antecubital assessment.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "How should blood be collected from an arm with a cast or splint covering the antecubital area?",
        "Requires provider approval and a site outside the immobilized field",
        [
            "Is done by puncturing directly through the cast material",
            "Is impossible so the order should be canceled without a comment to anyone",
            "Uses the same arm without documenting the cast in the chart",
        ],
        "Casts block visualization, stabilization, and hemostasis monitoring. "
        "When access is urgent, clinicians authorize a safe alternative per GP41 and institutional rules.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "How is blind venipuncture without palpating or visualizing a vein regarded?",
        "Not an acceptable approach for routine collection",
        [
            "Encouraged in experienced collectors to save collection time",
            "Required for stat orders placed after hours in the unit",
            "Preferred when the patient is anxious about the touch",
        ],
        "Successful venipuncture depends on deliberate site assessment and patient preparation. "
        "GP41 emphasizes visible or palpable vein confirmation before skin antisepsis and entry.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When petechiae appear above the tourniquet, what should the collector do?",
        "Release or loosen the tourniquet and reassess application",
        [
            "Tighten the tourniquet until the petechiae disappear",
            "Ignore them because they indicate an active infection in the arm",
            "Move the tourniquet distal to the puncture site for the draw",
        ],
        "Petechiae suggest excessive venous pressure or prolonged application. "
        "Adjusting or removing the tourniquet protects capillaries and keeps preanalytic conditions stable.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "The cephalic vein in the antecubital fossa is often chosen because it?",
        "Lies more laterally with relatively easy access in many people",
        [
            "Is typically the deepest of the antecubital veins",
            "Cannot be used when the median cubital vein is visible and usable",
            "Runs with the ulnar nerve along the medial arm of the patient",
        ],
        "Cephalic anatomy varies, but the lateral antecubital position is a common secondary option. "
        "GP41 training still requires palpation to confirm suitability before puncture.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Why should patients avoid pumping the fist repeatedly during the entire draw?",
        "Should be avoided because it can falsely elevate potassium",
        [
            "Is required to keep the veins distended for the full ten minutes",
            "Replaces the tourniquet application in obese patients",
            "Is mandatory for the coagulation tube filling",
        ],
        "Intermittent fist clenching may help initial venous filling, but sustained pumping alters analytes. "
        "GP41 technique uses brief opening and closing of the hand rather than prolonged vigorous pumping.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When a patient reports syncope during venipuncture, what should the collector do?",
        "Abort or complete the draw, lower the patient, and summon help",
        [
            "Continue the draw quickly before the patient fully loses consciousness",
            "Leave the patient unattended while the collector fetches the tubes and gloves",
            "Apply a tourniquet tighter to finish filling the last tube of the order",
        ],
        "Vasovagal reactions are a known phlebotomy complication requiring injury prevention and monitoring. "
        "GP41 patient-care steps include positioning, reassurance, and documentation of the event.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "What venipuncture on the same arm as a previous episode of thrombophlebitis should be done how?",
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
        "Which techniques help when antecubital veins are deep in obese patients?",
        "Proper positioning, palpation, and approved adjuncts such as warmth",
        [
            "Skipping the identification step because the veins are difficult to find",
            "Using a foot vein before attempting the arm for access",
            "Applying heavy tourniquet pressure for ten full minutes",
        ],
        "Depth increases the need for careful palpation and stabilization, not shortcuts in safety steps. "
        "GP41 supports adjuncts and experienced collectors while maintaining identification and infection control.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Why should tubes be labeled at the bedside immediately after collection?",
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
