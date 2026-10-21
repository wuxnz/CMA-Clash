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
        "Before venipuncture, how should the phlebotomist verify patient identity per CLSI-aligned practice?",
        "Use at least two unique identifiers verified against the order",
        [
            "Use the room number alone when the door chart appears to match",
            "Use the first name alone when the patient verbally confirms identity",
            "Use the wristband photograph alone without speaking to the patient",
        ],
        "CLSI GP41 ties safe collection to positive patient identification before any puncture. "
        "Room number or a single name fails the two-identifier standard most facilities require.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Why is the median cubital vein often selected as the primary antecubital venipuncture site?",
        "It is usually superficial, anchored, and positioned away from major nerves",
        [
            "It runs deep beside the radial artery in essentially every patient",
            "It is located on the dorsum of the hand rather than the antecubital fossa",
            "It must be used even when the vein is thrombosed or sclerosed",
        ],
        "GP41 site selection favors accessible antecubital veins with lower complication risk. "
        "The median cubital is commonly large and stable, though individual anatomy still dictates the final site.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "When assessing a candidate vein by palpation before venipuncture, what should the phlebotomist evaluate?",
        "Vein size, depth, direction, and resilience without relying on skin color alone",
        [
            "Skin tone alone because superficial veins appear equally in all patients",
            "Patient shoe size as a reliable proxy for antecubital vessel diameter",
            "Insurance coverage type to determine which arm may be used for collection",
        ],
        "Palpation confirms a bouncy, refillable vein before skin antisepsis. "
        "Visual inspection alone misses depth and sclerosis that GP41-style assessment is meant to catch.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Where should a tourniquet be placed for routine venipuncture?",
        "Three to four inches (about 8–10 cm) proximal to the intended puncture site",
        [
            "Distal to the puncture site below the antecubital crease on the forearm",
            "Around the neck when antecubital veins appear flat or difficult to palpate",
            "Directly over the selected vein to hold the vessel stationary during entry",
        ],
        "Proximal placement distends the vein without compressing the puncture field. "
        "A distal tourniquet does not support venous filling the way GP41 venipuncture technique describes.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "How long should a tourniquet generally remain applied during venipuncture?",
        "About one minute, releasing sooner when the draw allows",
        [
            "Five to ten minutes until every tube is labeled and capped at the chair",
            "As long as needed even when petechiae or hemoconcentration signs appear",
            "Until after the needle is fully withdrawn in every collection scenario",
        ],
        "Prolonged venous stasis causes hemoconcentration and can falsely shift analytes such as potassium. "
        "GP41 emphasizes minimizing tourniquet time while still allowing successful vein entry.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "For standard superficial venipuncture with a straight needle, how is the bevel typically oriented on insertion?",
        "Facing upward (bevel up) per facility training and manufacturer guidance",
        [
            "Facing downward against the vein floor for every adult patient",
            "Parallel to the skin surface without anchoring or stabilizing the vein",
            "In any direction because bevel orientation does not affect venipuncture success",
        ],
        "Bevel-up entry is the conventional technique taught for straight needles and many butterfly sets. "
        "Facility policy may vary slightly, but bevel-down insertion is not the default GP41-aligned approach.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "What needle insertion angle is typically recommended for venipuncture?",
        "15 to 30 degrees with slow, controlled advancement into the vein",
        [
            "90 degrees perpendicular through the full thickness of the forearm",
            "Parallel to the skin without penetrating the vein lumen",
            "45 to 60 degrees aimed toward underlying bone and nerve structures",
        ],
        "A shallow angle reduces the chance of puncturing the posterior vein wall. "
        "Steep or tangential angles increase hematoma risk and failed draws per venipuncture best practice.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "After initial vein entry during venipuncture, why should the needle angle be lowered?",
        "To advance along the lumen and stabilize the hub during multi-tube collection",
        [
            "To lift the vein away from surrounding tissue and increase tourniquet pressure",
            "To stop blood flow so vacuum tubes fill more slowly and reduce hemolysis",
            "To intentionally puncture the opposite vein wall and confirm depth of placement",
        ],
        "Shallow advancement keeps the bevel within the vein lumen during multi-tube collection. "
        "Leaving a steep angle increases movement at the hub and contributes to rolling or perforation.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "How should the vein be anchored during venipuncture?",
        "By drawing the skin taut distal to the puncture site with the non-dominant hand",
        [
            "By pressing directly over the needle hub while the needle advances into the vein",
            "By slapping the antecubital fossa firmly to stimulate venous filling",
            "By rotating the arm rapidly while the needle is advanced through the skin",
        ],
        "Distal traction stabilizes the vein and limits rolling during entry. "
        "Pressure over the hub or aggressive slapping does not substitute for proper anchoring in GP41 technique.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "When are butterfly (winged infusion) needle sets especially useful for venipuncture?",
        "When veins are fragile, small, or require precise control of needle placement",
        [
            "When large-volume blood cultures must always be drawn with the largest bore needle",
            "When arterial blood gas policy replaces standard venipuncture site selection rules",
            "When tourniquet application may be omitted entirely for outpatient chemistry draws",
        ],
        "Smaller-gauge butterflies can reduce trauma in difficult access situations when volume needs allow. "
        "They still require the same identification, site selection, and order-of-draw rules as straight needles.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Venipuncture should be avoided on an arm with which of the following conditions?",
        "An active IV infusion, dialysis vascular access, or mastectomy-side restrictions per policy",
        [
            "A bandage on an unrelated finger on the same hand without arm precautions",
            "Short fingernails on the hand used to stabilize the venipuncture site",
            "A blood pressure measurement on the opposite arm earlier the same day",
        ],
        "Drawing distal to running IV fluids dilutes specimens, and fistula or lymphedema precautions protect vulnerable arms. "
        "GP41 site-selection guidance directs collectors away from compromised circulation or lymphatic risk.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "How should venipuncture on the same side as a mastectomy with lymphedema risk be handled?",
        "It is generally contraindicated unless the provider and facility policy explicitly authorize that arm",
        [
            "It is preferred because lymph nodes have already been removed from that side",
            "It requires only a single patient identifier before proceeding with collection",
            "It eliminates the need to document arm selection in the medical record",
        ],
        "Lymphedema risk after breast surgery makes the affected arm a last-resort site. "
        "Many facilities require provider approval and meticulous documentation when no alternative exists.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Why should venipuncture through or immediately adjacent to a dialysis fistula or graft be avoided?",
        "Puncture can thrombose or permanently damage the vascular access used for dialysis",
        [
            "Routine laboratory draws through the access are encouraged to monitor patency",
            "Alcohol prep alone is sufficient without notifying the dialysis care team",
            "Venipuncture at the access site replaces formal dialysis nursing assessment",
        ],
        "Puncturing an access site can thrombose or damage the fistula. "
        "GP41 and dialysis safety policies reserve those vessels for treatment, not routine laboratory draws.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When IV fluids are infusing in one arm, what is the appropriate approach to venipuncture on that side?",
        "Avoid that arm unless a written protocol specifies discard volume and collection site",
        [
            "Proceed distal to the catheter without notifying the nurse or provider",
            "Use the IV fluid line port as the primary blood collection site",
            "Ignore infusion status when the patient is fasting for laboratory testing",
        ],
        "Infused fluids dilute analytes drawn below the IV site, producing falsely lowered values. "
        "CLSI-aligned practice uses the opposite extremity or an approved discard-draw procedure.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Why may the basilic vein be selected when other antecubital veins are unavailable?",
        "It is often larger but lies close to the medial nerve and brachial artery",
        [
            "It has no adjacent nerves or arteries and requires no anchoring technique",
            "It is always more superficial than the cephalic vein in every patient",
            "It must be chosen before the median cubital vein in all adult venipuncture",
        ],
        "Basilic access can succeed when safer options fail, but the proximity to nerve and artery demands careful technique. "
        "GP41 training stresses skilled palpation and stabilization when using this medial antecubital vein.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "When are hand veins an appropriate venipuncture site?",
        "When antecubital sites are unavailable and institutional policy permits distal collection",
        [
            "When they are always preferred over antecubital veins for patient comfort",
            "When the patient has lymphedema precautions on that same extremity",
            "When hand veins are mandatory whenever blood culture bottles are ordered",
        ],
        "Distal veins may be more painful and have higher complication rates than antecubital sites. "
        "GP41 allows hand draws as a secondary option when primary sites cannot be used safely.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "How should foot and ankle venipuncture in adults be handled under typical CLSI-aligned site hierarchy?",
        "Avoid foot and ankle draws except when no safer site exists and policy permits lower-extremity collection",
        [
            "Use foot veins as the default first choice for routine outpatient chemistry panels",
            "Require foot venipuncture for every coagulation specimen regardless of arm access",
            "Prefer foot veins over antecubital veins to minimize visible bruising on the arms",
        ],
        "Foot veins carry higher risk of thrombophlebitis and are difficult to stabilize. "
        "GP41 site hierarchy reserves lower-extremity draws for exceptional situations with documented justification.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When the only visible veins lie within edematous tissue, venipuncture at that site should be?",
        "Deferred in favor of a non-edematous site when another option exists",
        [
            "Preferred because interstitial fluid distends superficial veins",
            "Performed with a larger bore needle to reduce draw time",
            "Completed without a tourniquet to limit capillary pressure",
        ],
        "Edema obscures depth and direction on palpation and increases the risk of extravasation and specimen error. "
        "GP41 site selection favors dry, refillable veins that can be stabilized for reliable collection.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "During site assessment, a hardened or sclerosed vein from prior venipuncture should be?",
        "Avoided when another viable vein is available",
        [
            "Selected first because scar tissue keeps the vein from rolling",
            "Cannulated with a larger gauge to penetrate the fibrotic wall",
            "Used routinely if the patient points to that familiar site",
        ],
        "Sclerosed veins often fail to refill and yield inadequate or hemolyzed specimens despite repeated attempts. "
        "GP41 assessment includes recognizing non-viable vessels and rotating to healthier access when possible.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Venipuncture through unhealed burns or dense scar tissue should be avoided primarily because?",
        "Healing tissue is fragile and reliable vein access is unlikely",
        [
            "Scar tissue prevents antiseptic contact with the skin surface",
            "A tourniquet cannot be applied proximal to damaged skin",
            "Only capillary specimens are permitted over scarred areas",
        ],
        "Compromised skin breaks down easily under needle entry and may not seal predictably after withdrawal. "
        "When intact skin is available elsewhere, GP41-aligned practice selects a stable site away from burns and heavy scarring.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "If bright red, pulsatile blood appears during venipuncture, the collector should?",
        "Stop, withdraw the needle, and apply firm prolonged direct pressure",
        [
            "Continue collecting because arterial flow fills tubes faster",
            "Massage proximally along the vessel to slow the pulsation",
            "Advance the needle deeper to confirm entry in the vein lumen",
        ],
        "Pulsatile bright-red flow suggests arterial puncture, which can produce a rapid expanding hematoma. "
        "GP41 response includes sustained pressure, patient monitoring, and notifying the clinician per facility protocol.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "After the final tube fills during routine venipuncture, the tourniquet should typically be released?",
        "Before the needle is withdrawn from the vein",
        [
            "Only after the patient has left the phlebotomy chair",
            "After needle removal while direct pressure is delayed",
            "Left in place until every tube label is applied at the desk",
        ],
        "Releasing the tourniquet while the needle is still seated reduces venous back-pressure at the puncture site. "
        "Facility policy may vary slightly on timing relative to the last tube, but prolonged tourniquet during withdrawal is avoided.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Standard post-venipuncture hemostasis includes which immediate step?",
        "Firm direct pressure with clean gauze until bleeding stops",
        [
            "Prompt heavy use of the draw arm to restore circulation",
            "Peeling the dressing off within seconds to inspect the skin",
            "Withholding pressure when the patient takes anticoagulants",
        ],
        "Steady pressure helps the vein wall seal and limits hematoma formation, especially in anticoagulated patients. "
        "GP41 aftercare also covers bandage placement and instructions to report continued oozing or swelling.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "A warm compress applied proximal to a difficult draw site may help by?",
        "Promoting venodilation when ordered and permitted by policy",
        [
            "Replacing hand hygiene and skin antisepsis before puncture",
            "Removing the need for a tourniquet in most adult draws",
            "Ensuring culture bottles receive adequately aerobic blood",
        ],
        "Gentle heat can improve venous filling when veins are collapsed from cold or dehydration. "
        "It is an adjunct to—not a substitute for—GP41 identification, site assessment, and infection-control steps.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "For venipuncture, the patient's arm is best positioned when it is?",
        "Extended with the antecubital fossa supported and slightly dependent when tolerated",
        [
            "Acutely flexed with a tight fist held throughout the draw",
            "Elevated well above heart level to minimize post-stick bleeding",
            "Unsupported and moving freely during each tube change",
        ],
        "Dependent support encourages venous filling without sustained isometric muscle contraction in the forearm. "
        "Maintaining a clenched fist for the entire procedure can falsely elevate potassium and is discouraged in GP41 technique.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "Palpation to select a venipuncture site should be performed?",
        "Before skin antisepsis on the intended puncture area",
        [
            "Only after antiseptic has dried so the vein is not touched",
            "Through the prepped field using gloves that contacted tubes",
            "After all tubes fill to verify the needle remained in the lumen",
        ],
        "Site and direction are confirmed first; antiseptic is then applied to the chosen location. "
        "Re-palpating a prepped area without policy guidance can contaminate the field GP41 treats as the puncture zone.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "After alcohol or chlorhexidine is applied for venipuncture prep, the site should be?",
        "Allowed to air-dry completely before needle entry",
        [
            "Blotted dry immediately with a non-sterile gauze pad",
            "Fanning with ungloved hands to shorten the drying interval",
            "Coated with lotion to reduce patient discomfort from prep",
        ],
        "Incomplete drying can carry skin flora into the tract and may contribute to stinging or hemolysis in the specimen. "
        "GP41 infection-control practice follows manufacturer contact-time and drying requirements for the chosen antiseptic.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Heel-stick capillary sampling in infants is appropriate for?",
        "Small-volume tests when device depth and policy limits are met",
        [
            "Multi-tube adult-volume blood cultures on every newborn",
            "Unlimited volume collection without heel warming",
            "Full coagulation panels equivalent to large citrate tubes",
        ],
        "Heel sticks require controlled depth, site rotation, and warming to protect bone and soft tissue. "
        "GP41 capillary guidance caps volume and ties device choice to the ordered tests and patient size.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "A fingerstick capillary collection is appropriate when?",
        "The ordered test is validated for capillary volume on that device",
        [
            "Several large-volume culture bottles must be filled from one fingertip",
            "Citrate coagulation studies require a fingerstick by default",
            "Any laboratory order may be collected capillary without chart review",
        ],
        "Capillary specimens have strict volume and analyte limits set by the laboratory and instrument manufacturer. "
        "GP41 directs collectors to confirm test suitability in the manual or policy before selecting a fingerstick site.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Under many two-attempt venipuncture policies, after two unsuccessful sticks the next step is to?",
        "Obtain help from another qualified collector or a supervisor per policy",
        [
            "Continue attempts with the same collector until blood is obtained",
            "Discharge the patient without notifying the ordering provider",
            "Re-puncture the identical site with the next larger needle gauge",
        ],
        "Limiting attempts reduces hematoma, nerve injury, and patient distress from repeated trauma. "
        "GP41-aligned programs document each attempt and escalate when safe access cannot be established.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "Needle gauge for venipuncture should be chosen to balance?",
        "Vein size, required draw volume, and risk of hemolysis",
        [
            "Using the largest available bore regardless of vein fragility",
            "Selecting the smallest gauge even when volume cannot be met",
            "Rotating randomly among gauges to build technique on each visit",
        ],
        "Oversized needles in delicate veins increase trauma and hemolysis; undersized needles may slow flow and clot in the hub. "
        "GP41 training matches gauge to vessel condition and the volume requirements of the ordered tubes.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-site",
        "If blood flow stops during a multi-tube venipuncture, the first response within policy is to?",
        "Gently adjust needle position or reassess tourniquet application",
        [
            "Advance the needle forcefully through the posterior vein wall",
            "Discard the partial draw and leave without documenting the attempt",
            "Maximize tourniquet pressure until pulsatile flow returns",
        ],
        "Minor hub repositioning or correcting a loose tourniquet often restores flow without a new skin puncture. "
        "When flow cannot be re-established safely, GP41 practice favors stopping rather than repeated blind probing.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Venipuncture through an area that already shows a hematoma should be?",
        "Avoided because extravasation is likely and veins are hard to palpate",
        [
            "Preferred because pooled blood outlines the vessel for entry",
            "Performed through the center of the bruise to evacuate trapped blood",
            "Completed with minimal post-stick pressure to observe oozing",
        ],
        "An existing hematoma signals prior vessel injury and unreliable access at that location. "
        "Choosing intact skin on another site improves success rates and aligns with GP41 goals for complication prevention.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "When an arm has a history of chemotherapy or vesicant infusion, venipuncture on that extremity should?",
        "Follow oncology and facility policy, often favoring the opposite arm",
        [
            "Proceed as usual because prior infusions no longer affect the veins",
            "Use a butterfly needle alone without consulting the care team",
            "Skip bedside identification when the oncology record is on the chart",
        ],
        "Veins damaged by vesicants may extravasate easily or lack durable lumens for laboratory volume. "
        "GP41 site selection integrates oncology precautions alongside standard antecubital assessment.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Blood collection from an arm immobilized by a cast or splint over the antecubital area requires?",
        "Provider-approved planning and a site outside the immobilized field",
        [
            "Puncturing through a window cut in the cast material at the fossa",
            "Canceling the laboratory order without informing the clinical team",
            "Using the same arm while omitting cast documentation on the requisition",
        ],
        "Casts and splints block visualization, anchoring, and monitoring of hemostasis at the puncture site. "
        "When collection is urgent, clinicians authorize an alternative access plan consistent with GP41 and institutional rules.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Routine diagnostic venipuncture without palpating or visualizing a target vein is?",
        "Not acceptable standard practice for scheduled collection",
        [
            "Encouraged for experienced staff to shorten room time",
            "Required for every stat draw after routine laboratory hours",
            "Preferred when the patient is anxious about being touched",
        ],
        "Deliberate site assessment confirms a palpable or visible vein before antisepsis and needle entry. "
        "GP41 emphasizes preparation and vein confirmation rather than blind insertion on routine orders.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When petechiae appear on the skin proximal to an applied tourniquet, the collector should?",
        "Release or loosen the tourniquet and reassess placement and timing",
        [
            "Increase tourniquet tension until the petechiae fade from view",
            "Continue the draw because petechiae indicate adequate venous stasis",
            "Move the tourniquet distal to the intended puncture site",
        ],
        "Petechiae suggest capillary injury from excessive or prolonged venous congestion under the band. "
        "Adjusting the tourniquet limits hemoconcentration artifacts and protects fragile skin during the draw.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "The cephalic vein in the antecubital fossa is often selected because it?",
        "Occupies a lateral position with relatively accessible anatomy in many patients",
        [
            "Lies deeper than the basilic vein in virtually every adult",
            "Must not be used when the median cubital vein is visible",
            "Courses with the ulnar nerve along the medial upper arm",
        ],
        "Individual anatomy varies, but the lateral antecubital cephalic vein is a common secondary option after the median cubital. "
        "GP41 still requires palpation for size, depth, and stability before puncture at any antecubital site.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-site",
        "During venipuncture, sustained repetitive fist pumping by the patient should be avoided because it?",
        "Can falsely elevate serum potassium and other muscle-related analytes",
        [
            "Prevents adequate venous distension throughout a long tourniquet time",
            "Eliminates the need for a proximal tourniquet in obese adults",
            "Is required to fill citrate coagulation tubes completely",
        ],
        "Brief opening and closing of the hand may assist initial filling, but vigorous pumping throughout the draw alters results. "
        "GP41 technique limits fist exercise to short intervals rather than continuous pumping during tube collection.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When a patient becomes faint during venipuncture, the collector's priority is to?",
        "Secure the needle and patient per protocol, lower them safely, and get help",
        [
            "Finish filling remaining tubes before the patient slumps in the chair",
            "Step away from the patient briefly to retrieve additional supplies",
            "Tighten the tourniquet to complete the last tube quickly",
        ],
        "Vasovagal syncope is a recognized phlebotomy complication that risks injury from falls or needlesticks. "
        "GP41 patient-care steps include safe positioning, monitoring, and documenting the reaction per facility policy.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "Venipuncture on an arm with a recent history of thrombophlebitis should be?",
        "Avoided when a usable site exists on another extremity",
        [
            "Performed on the inflamed segment to monitor healing of the vein",
            "Attempted with a larger gauge to traverse residual clot",
            "Done without documentation if the vein appears normal on inspection",
        ],
        "Previously inflamed veins are prone to recurrence, pain, and poor healing after additional cannulation trauma. "
        "GP41 site selection favors unused vessels on the contralateral arm when policy and anatomy allow.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-site",
        "When antecubital veins are deep in an obese patient, helpful techniques include?",
        "Proper arm support, careful palpation, and policy-approved warmth when indicated",
        [
            "Deferring patient identification until after a successful stick",
            "Choosing a foot vein before any attempt at the upper extremity",
            "Applying maximal tourniquet pressure for several minutes",
        ],
        "Increased adipose depth demands thorough palpation and stabilization, not omission of safety or identification steps. "
        "GP41 supports adjuncts such as positioning and heat while maintaining infection control and positive patient ID.",
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
