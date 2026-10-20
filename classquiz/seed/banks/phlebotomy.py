# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

FACTS: list[dict] = [
    {
        "topic": "phleb-order-draw",
        "stem": "CLSI recommended order of draw after blood cultures is often:",
        "correct": "Light blue (citrate) before serum/green/lavender/gray tubes",
        "distractors": [
            "Gray before lavender",
            "Green before light blue",
            "Any order if using syringe only"
        ],
        "explanation": "Correct order prevents additive carryover.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "Blood culture bottles should be collected:",
        "correct": "First when cultures are ordered",
        "distractors": [
            "After gray top last always",
            "Only after coagulation tube",
            "Never in outpatient care"
        ],
        "explanation": "Sterile technique reduces contamination.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "The light blue (citrate) tube is drawn early because:",
        "correct": "Citrate can be contaminated by other additives",
        "distractors": [
            "It contains EDTA",
            "It is for glucose only",
            "It clots serum"
        ],
        "explanation": "Citrate anticoagulant affects coagulation tests if contaminated.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "Serum tubes (red/gold SST) are typically drawn:",
        "correct": "After light blue and before heparin/lavender in standard order",
        "distractors": [
            "Before blood cultures always",
            "After gray top first",
            "Only with needle change each time"
        ],
        "explanation": "Order prevents erroneous coagulation and chemistry.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "Heparin (green) tubes should be drawn:",
        "correct": "After serum tubes in standard multi-tube draws",
        "distractors": [
            "Before citrate always",
            "Only last after gray",
            "Before cultures"
        ],
        "explanation": "Heparin carryover can affect some assays.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "EDTA (lavender) tubes are drawn:",
        "correct": "After green in common teaching order",
        "distractors": [
            "Before all tubes",
            "Only with cultures",
            "Before light blue"
        ],
        "explanation": "EDTA affects many tests if carried into other tubes.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "Gray (fluoride/oxalate) tubes are usually drawn:",
        "correct": "Last in standard order of draw",
        "distractors": [
            "First after tourniquet",
            "Before light blue",
            "Instead of lavender"
        ],
        "explanation": "Oxalate/fluoride prevents glycolysis for glucose.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "If only a light blue tube is ordered, a:",
        "correct": "Discard tube may be drawn first per policy to clear dead space",
        "distractors": [
            "Gray tube must be drawn first",
            "Culture is mandatory",
            "Green tube is required"
        ],
        "explanation": "Discard tubes reduce tissue thromboplastin contamination.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "Using a syringe transfer to tubes requires:",
        "correct": "Maintaining proper fill volumes and order of draw",
        "distractors": [
            "Ignoring fill lines",
            "Pouring blood between tubes",
            "Shaking tubes vigorously"
        ],
        "explanation": "Underfilled citrate tubes invalidate coag studies.",
        "references": [
            "CLSI"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "Drawing EDTA before citrate may cause:",
        "correct": "Falsely prolonged clotting times",
        "distractors": [
            "Hyperglycemia on tube label",
            "Hemolysis only in gray",
            "No effect ever"
        ],
        "explanation": "Additive carryover is a common preanalytic error.",
        "references": [
            "CLSI"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "When cultures and routine tubes are needed:",
        "correct": "Culture first, then follow order of draw for others",
        "distractors": [
            "Routine tubes before cultures",
            "Only one tube total",
            "Random order"
        ],
        "explanation": "Minimize contamination and additive errors.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-order-draw",
        "stem": "Documenting order of draw errors should:",
        "correct": "Notify lab and recollect if results may be affected",
        "distractors": [
            "Hide the error",
            "Dilute sample with saline",
            "Freeze tube"
        ],
        "explanation": "Preanalytic errors can invalidate results.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-additives",
        "stem": "Lavender-top tubes contain:",
        "correct": "EDTA anticoagulant",
        "distractors": [
            "Citrate",
            "Heparin",
            "Sodium fluoride only"
        ],
        "explanation": "EDTA is for hematology such as CBC.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-additives",
        "stem": "Light blue tubes contain:",
        "correct": "Sodium citrate for coagulation studies",
        "distractors": [
            "EDTA",
            "Gel separator only",
            "Oxalate"
        ],
        "explanation": "Citrate binds calcium to prevent clotting.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-additives",
        "stem": "Green-top tubes often contain:",
        "correct": "Lithium or sodium heparin",
        "distractors": [
            "EDTA",
            "Citrate",
            "Fluoride"
        ],
        "explanation": "Heparin tubes are used for plasma chemistry.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-additives",
        "stem": "Gray-top tubes often contain:",
        "correct": "Sodium fluoride and potassium oxalate",
        "distractors": [
            "Citrate only",
            "Clot activator only",
            "EDTA"
        ],
        "explanation": "Fluoride inhibits glycolysis; oxalate anticoagulates.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-additives",
        "stem": "Gold SST tubes may contain:",
        "correct": "Clot activator and gel separator",
        "distractors": [
            "EDTA",
            "Citrate",
            "No additive"
        ],
        "explanation": "Serum separator tubes yield serum after clotting.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-additives",
        "stem": "A CBC is most commonly collected in a:",
        "correct": "Lavender EDTA tube",
        "distractors": [
            "Red serum tube",
            "Light blue citrate tube",
            "Gray fluoride tube"
        ],
        "explanation": "EDTA preserves cell morphology for hematology.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-additives",
        "stem": "PT/INR testing typically uses:",
        "correct": "Light blue citrate tube filled to proper ratio",
        "distractors": [
            "Lavender tube",
            "Green heparin",
            "Gray tube"
        ],
        "explanation": "Citrate must be filled to marked volume.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-additives",
        "stem": "Blood glucose in gray tube is:",
        "correct": "Protected from in vitro glycolysis by fluoride",
        "distractors": [
            "Always serum only",
            "Collected in citrate",
            "Invalid in lavender"
        ],
        "explanation": "Gray tubes stabilize glucose for transport delays.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-additives",
        "stem": "Heparin plasma may be required for:",
        "correct": "Some chemistry analytes per lab method",
        "distractors": [
            "All coagulation tests",
            "CBC only",
            "Blood culture"
        ],
        "explanation": "Lab requisitions specify tube type.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-additives",
        "stem": "Underfilled citrate tubes cause:",
        "correct": "Diluted anticoagulant and invalid coag results",
        "distractors": [
            "Hyperkalemia always",
            "Hemolysis only in CBC",
            "No issue"
        ],
        "explanation": "Maintain 9:1 blood to anticoagulant ratio.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-additives",
        "stem": "Clot activator in red-top tubes helps:",
        "correct": "Serum formation for many chemistry tests",
        "distractors": [
            "Prevent clotting",
            "Measure INR",
            "Inhibit bacteria"
        ],
        "explanation": "Allow clotting before centrifugation if required.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-additives",
        "stem": "Gel separator after centrifugation:",
        "correct": "Separates serum/plasma from cells",
        "distractors": [
            "Activates platelets",
            "Replaces EDTA",
            "Is used for blood cultures"
        ],
        "explanation": "Separator reduces analyte interference from cells.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-site",
        "stem": "The median cubital vein is often preferred because it:",
        "correct": "Is usually anchored and accessible with low complication risk",
        "distractors": [
            "Is always deepest",
            "Cannot be used in adults",
            "Requires arterial puncture"
        ],
        "explanation": "Antecubital fossa veins are common venipuncture sites.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-site",
        "stem": "The tourniquet should be applied:",
        "correct": "3–4 inches above puncture site, not too tight",
        "distractors": [
            "Distal to the puncture site",
            "Left on indefinitely",
            "Tight enough to stop arterial flow"
        ],
        "explanation": "Venous distension aids vein selection; avoid arterial occlusion.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-site",
        "stem": "The bevel of the needle should face:",
        "correct": "Up when using standard superficial venipuncture technique",
        "distractors": [
            "Down always",
            "Sideways only",
            "Away from skin"
        ],
        "explanation": "Facility training defines technique; bevel orientation affects comfort.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-site",
        "stem": "The angle of needle insertion for venipuncture is typically:",
        "correct": "15–30 degrees with the bevel up",
        "distractors": [
            "90 degrees always",
            "Parallel to skin surface",
            "Through bone"
        ],
        "explanation": "Shallow angle reduces perforation of opposite vein wall.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-site",
        "stem": "After vein entry, lowering the angle helps:",
        "correct": "Advance the needle along the vein lumen",
        "distractors": [
            "Increase pain always",
            "Cause hematoma",
            "Stop blood flow"
        ],
        "explanation": "Stabilize hub and prevent vein rolling.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-site",
        "stem": "Anchor the vein by:",
        "correct": "Pulling skin taut distal to puncture",
        "distractors": [
            "Pressing directly over needle hub",
            "Punching the site",
            "Rotating arm rapidly"
        ],
        "explanation": "Stabilization prevents rolling during insertion.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-site",
        "stem": "Butterfly (winged infusion) sets are useful for:",
        "correct": "Fragile veins and precise control",
        "distractors": [
            "Arterial lines only",
            "Always large bore draws only",
            "Culture bottles only"
        ],
        "explanation": "Smaller gauge may reduce trauma.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-site",
        "stem": "Palpation of the vein should assess:",
        "correct": "Size, depth, and resilience",
        "distractors": [
            "Only color of skin",
            "Patient shoe size",
            "Insurance type"
        ],
        "explanation": "Palpation is more reliable than sight alone.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-site",
        "stem": "Avoid venipuncture on an arm with:",
        "correct": "IV infusion, mastectomy side restrictions, or dialysis fistula on that side",
        "distractors": [
            "A bandage on finger",
            "Short nails",
            "Light clothing"
        ],
        "explanation": "Site restrictions reduce complications.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-site",
        "stem": "After successful draw, release tourniquet:",
        "correct": "Before removing needle per policy, often after last tube",
        "distractors": [
            "Never",
            "After needle is fully removed only always",
            "Before needle insertion"
        ],
        "explanation": "Early release reduces hematoma risk.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-site",
        "stem": "Apply pressure after venipuncture for:",
        "correct": "Several minutes or per anticoagulant use",
        "distractors": [
            "One second",
            "No pressure needed",
            "Only if patient asks"
        ],
        "explanation": "Adequate pressure prevents bleeding and hematoma.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-site",
        "stem": "Warm packs proximal to site may:",
        "correct": "Dilate veins for difficult draws",
        "distractors": [
            "Cause hemolysis always",
            "Replace hand hygiene",
            "Eliminate need for tourniquet"
        ],
        "explanation": "Warmth can improve venous filling.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-handling",
        "stem": "Specimen labels must include at minimum:",
        "correct": "Patient identifiers and collection time per policy",
        "distractors": [
            "Staff lunch order",
            "Unrelated ICD codes only",
            "Social security number in waiting room"
        ],
        "explanation": "Accurate labels prevent wrong-patient results.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-handling",
        "stem": "Hemolysis may falsely elevate:",
        "correct": "Potassium and some enzymes on chemistry panels",
        "distractors": [
            "Only glucose downward",
            "INR only",
            "Platelet count only"
        ],
        "explanation": "Gentle handling reduces hemolysis.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-handling",
        "stem": "Tubes should be mixed by:",
        "correct": "Gentle inversion per tube manufacturer instructions",
        "distractors": [
            "Vigorous shaking",
            "Freezing immediately",
            "Leaving horizontal always"
        ],
        "explanation": "Proper mixing ensures additive contact without hemolysis.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-handling",
        "stem": "Centrifugation timing should follow:",
        "correct": "Laboratory procedures for serum/plasma separation",
        "distractors": [
            "Random choice",
            "Never centrifuge",
            "Patient preference"
        ],
        "explanation": "Separation within stability limits preserves analyte integrity.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-handling",
        "stem": "Serum separator tubes often require:",
        "correct": "Clotting upright for recommended time before centrifuge",
        "distractors": [
            "Immediate freezing without clot",
            "Heating to 100°C",
            "Dilution with saline"
        ],
        "explanation": "Complete clotting reduces fibrin interference.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-handling",
        "stem": "Transport to lab should maintain:",
        "correct": "Temperature requirements on test requisition",
        "distractors": [
            "Direct sunlight exposure",
            "Horizontal agitation only",
            "Open caps"
        ],
        "explanation": "Stability windows depend on analyte.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-handling",
        "stem": "Light-sensitive specimens may need:",
        "correct": "Protection from light in amber wrap or covered transport",
        "distractors": [
            "Exposure to UV",
            "Room light only always",
            "Microwave warming"
        ],
        "explanation": "Examples include some vitamins and bilirubin specimens.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-handling",
        "stem": "Chain of custody applies to:",
        "correct": "Forensic or legal specimens per protocol",
        "distractors": [
            "Every routine CBC",
            "All urine dips",
            "Staff scheduling"
        ],
        "explanation": "Document transfers for legal integrity.",
        "references": [
            "CLSI"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "phleb-handling",
        "stem": "Reject criteria for hemolyzed potassium sample may include:",
        "correct": "Recollection if degree of hemolysis invalidates result",
        "distractors": [
            "Automatic reporting without note",
            "Diluting sample",
            "Adding citrate"
        ],
        "explanation": "Lab defines acceptable hemolysis indices.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-handling",
        "stem": "Fasting glucose specimens require:",
        "correct": "Patient fasting status documented per order",
        "distractors": [
            "Random snack documented as fasting",
            "No label",
            "Only verbal report"
        ],
        "explanation": "Preanalytic fasting affects interpretation.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-handling",
        "stem": "Capillary collection devices must be:",
        "correct": "Single-patient use and disposed per sharps policy",
        "distractors": [
            "Reused after alcohol wipe",
            "Shared in classroom without policy",
            "Left open on counter"
        ],
        "explanation": "Sharps safety reduces bloodborne pathogen risk.",
        "references": [
            "CLSI",
            "CDC"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-handling",
        "stem": "Delayed processing of coagulation samples can:",
        "correct": "Affect clotting factor activity and results",
        "distractors": [
            "Improve accuracy always",
            "Only affect CBC",
            "Have no preanalytic effect"
        ],
        "explanation": "Timely delivery is critical for coag tests.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "A hematoma after venipuncture is often due to:",
        "correct": "Blood leaking into tissues from vein wall trauma",
        "distractors": [
            "Tourniquet too loose",
            "Patient talking",
            "Correct tube order"
        ],
        "explanation": "Apply firm pressure and elevate arm.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-complications",
        "stem": "Prolonged tourniquet application may cause:",
        "correct": "Hemoconcentration and falsely altered analytes",
        "distractors": [
            "Improved glucose always",
            "No lab effect",
            "Automatic hemolysis only"
        ],
        "explanation": "Release within recommended time limits.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "Arterial puncture signs may include:",
        "correct": "Rapid pulsatile blood flow and pain",
        "distractors": [
            "Slow steady venous flow always",
            "No blood",
            "Only bruising days later"
        ],
        "explanation": "Withdraw and apply prolonged pressure; notify provider.",
        "references": [
            "CLSI"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "phleb-complications",
        "stem": "Nerve injury risk is reduced by:",
        "correct": "Not probing deeply and using appropriate gauge",
        "distractors": [
            "Bouncing the needle",
            "Large bore in hand veins always",
            "No anchoring"
        ],
        "explanation": "Anatomy knowledge guides safe site choice.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "Syncope during draw requires:",
        "correct": "Stopping procedure and protecting patient from fall",
        "distractors": [
            "Continuing draw",
            "Trendelenburg only without assessment",
            "Leaving patient standing"
        ],
        "explanation": "Treat as medical event per protocol.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "Petechiae above tourniquet may suggest:",
        "correct": "Capillary fragility or platelet issues",
        "distractors": [
            "Normal finding always",
            "Infection at site",
            "Successful draw only"
        ],
        "explanation": "Assess and report unexpected bleeding signs.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "Infection at puncture site prevention includes:",
        "correct": "Hand hygiene and aseptic technique",
        "distractors": [
            "Reusing tourniquets without cleaning",
            "No gloves",
            "Blowing on skin"
        ],
        "explanation": "Clean technique lowers skin flora introduction.",
        "references": [
            "CLSI",
            "CDC"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-complications",
        "stem": "Repeated venipuncture at same site increases:",
        "correct": "Scarring and difficulty accessing vein",
        "distractors": [
            "Healing speed always",
            "Vein size permanently",
            "No risk"
        ],
        "explanation": "Rotate sites when possible.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-complications",
        "stem": "Hemolysis during difficult draw may result from:",
        "correct": "Excessive probing and forceful aspiration",
        "distractors": [
            "Gentle technique",
            "Proper fill",
            "Correct order"
        ],
        "explanation": "Technique affects sample quality.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "Failed venipuncture attempts policy often limits:",
        "correct": "Number of attempts before seeking experienced help",
        "distractors": [
            "Unlimited attempts",
            "Only one try ever",
            "No documentation"
        ],
        "explanation": "Patient safety drives attempt limits.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "Bilirubin falsely lowered may occur with:",
        "correct": "Exposure to light if not protected",
        "distractors": [
            "Correct mixing",
            "Immediate labeling",
            "Ice transport"
        ],
        "explanation": "Protect light-sensitive tubes.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-complications",
        "stem": "Thrombosed vein feels:",
        "correct": "Hard, cord-like, and non-compressible",
        "distractors": [
            "Bouncy and full",
            "Absent always",
            "Pulsatile"
        ],
        "explanation": "Choose another site.",
        "references": [
            "CLSI"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-safety",
        "stem": "Needlestick injury first steps include:",
        "correct": "Wash area, report immediately, and seek post-exposure evaluation",
        "distractors": [
            "Ignore if small",
            "Squeeze and suck wound",
            "Finish all draws first"
        ],
        "explanation": "Timely evaluation may include PEP for HIV risk.",
        "references": [
            "CDC",
            "OSHA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-safety",
        "stem": "Sharps containers must be:",
        "correct": "Puncture-resistant, labeled, and not overfilled",
        "distractors": [
            "Open on top",
            "Reused after emptying into trash",
            "Placed on floor unlocked"
        ],
        "explanation": "OSHA requires safe sharps disposal.",
        "references": [
            "OSHA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-safety",
        "stem": "PPE for routine venipuncture includes:",
        "correct": "Gloves at minimum; additional PPE per exposure risk",
        "distractors": [
            "No gloves if careful",
            "Gown always for every fingerstick",
            "Respirator only"
        ],
        "explanation": "Standard Precautions guide PPE.",
        "references": [
            "CDC"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-safety",
        "stem": "Hand hygiene before phlebotomy should be performed:",
        "correct": "Before patient contact and after glove removal",
        "distractors": [
            "Only at end of shift",
            "Never with alcohol gel available",
            "After lunch only"
        ],
        "explanation": "Hand hygiene is the most basic infection control.",
        "references": [
            "CDC"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-safety",
        "stem": "Blood splash to mucous membranes requires:",
        "correct": "Immediate flushing and incident reporting",
        "distractors": [
            "Waiting until end of day",
            "No action",
            "Only bandage"
        ],
        "explanation": "Source patient testing and follow-up per policy.",
        "references": [
            "CDC"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-safety",
        "stem": "Work practice controls include:",
        "correct": "Using safety-engineered devices when available",
        "distractors": [
            "Recapping needles by hand routinely",
            "Passing uncapped needles",
            "Bending needles before disposal"
        ],
        "explanation": "Engineered sharps reduce injuries.",
        "references": [
            "OSHA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-safety",
        "stem": "Patient identification before phlebotomy requires:",
        "correct": "Active identification using two identifiers",
        "distractors": [
            "Asking roommates",
            "Assuming bed label only",
            "First name only"
        ],
        "explanation": "Wrong-patient draws are serious errors.",
        "references": [
            "CLSI",
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-safety",
        "stem": "Biohazard spill cleanup uses:",
        "correct": "Facility-approved disinfectant and PPE",
        "distractors": [
            "Paper towels only",
            "Bare hands",
            "Air freshener"
        ],
        "explanation": "Follow blood spill protocol.",
        "references": [
            "CDC"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-safety",
        "stem": "Horizontal surface disinfection between patients:",
        "correct": "Reduces cross-contamination",
        "distractors": [
            "Is unnecessary",
            "Replaces gloves",
            "Eliminates need for hand hygiene"
        ],
        "explanation": "Clean tourniquets and surfaces per policy.",
        "references": [
            "CDC"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-safety",
        "stem": "Transport of specimens in bags should:",
        "correct": "Prevent leaks with secondary containment",
        "distractors": [
            "Leave tubes uncapped",
            "Mix patient specimens",
            "Carry in pocket"
        ],
        "explanation": "Leak-proof bags protect handlers.",
        "references": [
            "CLSI"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "phleb-safety",
        "stem": "Refusing phlebotomy on combative patient should:",
        "correct": "Prioritize safety and involve provider/security per policy",
        "distractors": [
            "Force restraint without order",
            "Proceed quickly",
            "Leave needles in place"
        ],
        "explanation": "Safety for patient and staff comes first.",
        "references": [
            "NHA CCMA"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "phleb-safety",
        "stem": "Training for phlebotomy competency includes:",
        "correct": "Technique, order of draw, and safety regulations",
        "distractors": [
            "Only billing codes",
            "No hands-on practice",
            "Social media tips"
        ],
        "explanation": "Competency validation is required by employers.",
        "references": [
            "CLSI",
            "NHA CCMA"
        ],
        "difficulty": "beginner"
    }
]
