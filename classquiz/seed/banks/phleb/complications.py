# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored phlebotomy complications question bank (CLSI GP41)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_REF = [S.CLSI_GP41, S.NHA_CPT]

FACTS: list[dict] = [
    fact(
        "phleb-complications",
        "How is a hematoma after venipuncture best prevented?",
        "Firm direct pressure after needle removal and careful needle technique",
        [
            "Massaging the puncture site vigorously right after needle withdrawal",
            "Bending the arm tightly without holding gauze over the site",
            "Applying ice briefly and releasing the arm without holding pressure",
        ],
        "CLSI emphasizes holding steady pressure on the site until bleeding stops so blood does not pool under the skin. "
        "Massaging the site, bending the arm tightly, and applying ice while releasing the arm can each restart bleeding and enlarge the bruise.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "What is blood pooling under the skin after venipuncture called?",
        "Hematoma",
        [
            "Syncope",
            "Hemolysis of red cells inside the collection tube",
            "Arterial spasm without bruising",
        ],
        "A hematoma is localized bleeding into tissues from vein wall trauma during or after the stick. "
        "It is not the same as fainting (syncope) or red-cell breakdown in the tube (hemolysis).",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "How long should routine venipuncture site pressure usually be held?",
        "At least 2 to 3 minutes, longer if the patient bleeds easily",
        [
            "About 5 seconds unless the patient requests more time",
            "No pressure if the needle was small gauge",
            "Until the gauze looks clean, with no set holding time",
        ],
        "Adequate pressure time lets the vein wall seal before the patient moves the arm. "
        "Anticoagulated or thrombocytopenic patients often need longer pressure per facility policy.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "How is infection at a venipuncture site best prevented?",
        "Hand hygiene and aseptic skin preparation before the stick",
        [
            "Reusing a cloth tourniquet on every patient without cleaning",
            "Palpating veins with bare hands that were not washed before the draw",
            "Blowing on the skin to dry disinfectant faster",
        ],
        "CLSI ties reliable results to proper skin antisepsis and clean technique that limits introduction of skin flora. "
        "Shared uncleaned equipment and skipped hand hygiene raise the risk of local cellulitis.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "What does repeated venipuncture at the same antecubital site increase the risk of?",
        "Sclerosis, scarring, and harder future access",
        [
            "Permanent enlargement of the vein for easier draws",
            "Automatic improvement in specimen quality",
            "No effect on vein integrity over time",
        ],
        "Scar tissue and sclerosis make veins cord-like and difficult to cannulate. "
        "Rotating sites when possible protects long-term access and reduces patient discomfort.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "How does a thrombosed or sclerosed vein feel on palpation?",
        "Hard, cord-like, and non-compressible",
        [
            "Soft, bouncy, and easily refillable",
            "Pulsatile like a normal artery",
            "Absent on both arms in every patient",
        ],
        "Thrombosed veins should not be used for venipuncture because they will not provide reliable flow. "
        "Pulsatile vessels suggest arterial anatomy and require a different site.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "If the patient reports tingling or an electric shock sensation during the draw, what should the collector do?",
        "Stop the procedure and assess for possible nerve contact",
        [
            "Advance the needle deeper to secure the vein",
            "Continue the draw and finish the remaining tubes quickly",
            "Tighten the tourniquet until the sensation stops",
        ],
        "Tingling or shooting pain may mean the needle is near a nerve, so advancing deeper, tightening the tourniquet, or rushing to fill the remaining tubes each raise injury risk. "
        "CLSI supports stopping, removing the needle, and selecting another site per policy.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "When a patient begins to faint during phlebotomy, what is the first priority?",
        "Stop the draw and lower the patient safely to prevent injury",
        [
            "Complete the last tube while the patient remains standing",
            "Leave the patient sitting on the floor without observation",
            "Continue holding the needle in the vein until tubes are full",
        ],
        "Vasovagal syncope can cause rapid loss of consciousness and fall injury. "
        "Lay the patient supine, protect the head, and monitor per protocol rather than finishing the collection.",
        [S.CLSI_GP41, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    fact(
        "phleb-complications",
        "What do petechiae appearing above the tourniquet often suggest?",
        "Prolonged or excessive tourniquet pressure",
        [
            "A successful draw with no technique concern",
            "Hyperglycemia caused by the tourniquet pressure",
            "A normal finding that does not call for assessment",
        ],
        "Capillary rupture from stasis or high pressure can cause pinpoint hemorrhages. "
        "Release or reposition the tourniquet and document unexpected bleeding signs.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "Why do most facilities limit the number of venipuncture attempts?",
        "Repeated sticks raise pain, hematoma, and nerve injury risk",
        [
            "Unlimited attempts are safer for the patient than a set limit",
            "A second qualified collector is not brought in, whatever the patient's distress",
            "Attempt limits apply to pediatric patients rather than to adults",
        ],
        "CLSI and employer policies cap attempts before another qualified collector steps in. "
        "Unlimited attempts, withholding a second collector, and applying the cap to children alone each raise pain, hematoma, and nerve injury risk. "
        "Documentation of attempts guides safer recollection planning.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "What action should visible spreading redness with warmth at a prior stick site prompt?",
        "Stopping reuse of that area and notifying the care team",
        [
            "Another stick in the same inflamed spot for speed",
            "Waiting for a fever before reporting the symptoms",
            "Applying occlusive tape over the area without clinical notification",
        ],
        "These findings may indicate cellulitis needing medical evaluation. "
        "Drawing through infected tissue, waiting for a fever, and covering the area with tape instead of notifying the care team each delay treatment. "
        "Reusing the same site is not appropriate.",
        [S.CLSI_GP41, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    fact(
        "phleb-complications",
        "What does a large enlarging bruise right after venipuncture despite pressure suggest?",
        "Continued bleeding under the skin needing prolonged pressure and monitoring",
        [
            "Normal healing that does not call for reassessment",
            "Hemolysis in the tube from gentle technique",
            "Proof that the tourniquet was too loose during the entire draw",
        ],
        "Expanding hematoma may mean inadequate hemostasis or a through-and-through puncture. "
        "Hold pressure longer, elevate the arm if tolerated, and escalate per facility policy.",
        _REF,
        "beginner",
    ),
    fact(
        "phleb-complications",
        "What may leaving a tourniquet on too long during venipuncture cause?",
        "Hemoconcentration and falsely altered analyte levels",
        [
            "Improved glucose accuracy in patients with diabetes",
            "Hemolysis that occurs without an effect of stasis",
            "No change in plasma constituents",
        ],
        "CLSI recommends limiting tourniquet time to about one minute when possible. "
        "Prolonged stasis concentrates proteins and cells and can falsely shift chemistry and hematology values.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What does excessive needle probing at one site increase the risk of?",
        "Nerve injury, pain, and hematoma formation",
        [
            "Higher patient satisfaction scores for the collector",
            "Guaranteed success on the second insertion attempt",
            "Improved blood culture purity with no change in technique",
        ],
        "Multiple redirects traumatize tissue and make veins harder to find. "
        "One careful attempt or escalation per policy is safer than digging at a single site.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What does bright red pulsatile blood during antecubital venipuncture suggest?",
        "Possible arterial puncture requiring withdrawal and prolonged pressure",
        [
            "Normal venous flow that should be collected faster",
            "Successful vein access that needs no change in technique",
            "Hemoconcentration from a loose tourniquet",
        ],
        "Arterial blood is higher pressure and oxygenated compared with typical venous flow. "
        "Remove the needle, apply extended pressure, monitor the site, and notify the clinician per CLSI guidance.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "Which laboratory values may hemolysis during a difficult draw falsely elevate?",
        "Potassium and some enzymes released from lysed red cells",
        [
            "Sodium values, in the absence of release from ruptured cells",
            "Patient blood pressure at the cuff site",
            "Room temperature in the collection area",
        ],
        "Ruptured erythrocytes spill intracellular potassium and other analytes into serum or plasma. "
        "Gentle technique, proper needle gauge, and avoiding forceful aspiration reduce hemolysis.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What reduces nerve injury risk during venipuncture?",
        "Using appropriate anatomy, gauge, and depth without lateral probing",
        [
            "Bouncing the needle to find the vein by feel",
            "Using the largest bore needle in hand veins as routine practice",
            "Leaving the vein unanchored during insertion",
        ],
        "Shallow antecubital veins lie near nerves and arteries; controlled insertion limits trauma. "
        "Deep probing or oversized needles in small veins increase persistent numbness or pain risk.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "Which findings suggest infection at a venipuncture site?",
        "Redness, warmth, swelling, pain, or purulent drainage",
        [
            "A flat bruise color with neither warmth nor swelling",
            "Immediate clotting inside the collection tube",
            "Higher HDL cholesterol on the lab report",
        ],
        "Local infection is a clinical complication separate from a simple bruise. "
        "Spreading cellulitis needs medical evaluation rather than another stick at the same spot.",
        [S.CLSI_GP41, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "How should a delayed faint several minutes after the draw be managed?",
        "Assisting the patient supine, monitoring vitals, and documenting the event",
        [
            "Allowing the patient to drive home immediately if they insist",
            "Dismissing symptoms if initial vitals looked normal",
            "Giving stimulants without assessment or observation",
        ],
        "Late vasovagal reactions occur after the patient stands or walks. "
        "Observation after phlebotomy and safe positioning reduce fall and injury risk.",
        [S.CLSI_GP41, S.NHA_CPT],
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What can drawing from an arm with an active IV infusion cause?",
        "Diluted or contaminated specimens and fluid interference",
        [
            "More accurate electrolytes when the draw is taken below the IV site",
            "No effect on results when the IV solution is normal saline",
            "An improvement in coagulation studies",
        ],
        "Blood below an infusing line may not reflect the patient's true values. "
        "CLSI advises avoiding phlebotomy on that arm when another site is available per policy.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "If blood flow stops during tube fill with a butterfly set, what is a common cause?",
        "Clot formation in the line from slow flow or stasis",
        [
            "A correct order of draw with full tubes",
            "Patient identification completed at bedside",
            "Gentle tube inversion after collection",
        ],
        "Line clots block flow and may force another venipuncture. "
        "Maintain steady flow, use appropriate gauge, and follow lab policy for difficult collections.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "When should venipuncture through markedly edematous tissue generally be avoided?",
        "Avoided when another site is available",
        [
            "Preferred because veins are easier to see",
            "Required for every inpatient regardless of swelling",
            "Performed without documenting the site that was chosen",
        ],
        "Fluid in tissues distorts anatomy and can yield unreliable specimens. "
        "Choose a dry accessible site when possible to protect sample integrity and hemostasis.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What do patients taking anticoagulants often need after venipuncture?",
        "Longer pressure and closer monitoring for bleeding or bruising",
        [
            "No pressure because medication prevents all bleeding",
            "Shorter pressure time than patients who are not anticoagulated",
            "Immediate strenuous exercise of the draw arm",
        ],
        "Anticoagulation prolongs clotting at the skin puncture site. "
        "Extended pressure and patient education about bruising reduce hematoma risk.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What should failed venipuncture documentation include?",
        "Number of attempts, patient response, and plan for recollection",
        [
            "Successful collections with no mention of the failed attempts",
            "Unrelated billing codes without clinical detail",
            "Blank forms to save time",
        ],
        "Accurate records support safety limits and communication with nurses and the laboratory. "
        "CLSI ties quality collection to traceable documentation of what occurred at the bedside.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "How can hemolysis from rough handling falsely affect a bilirubin result?",
        "Releasing intracellular pigments and altering chemistry interpretation",
        [
            "Lowering bilirubin when the tubes are kept away from light",
            "Having no effect on a liver chemistry analyte",
            "Improving the accuracy of ammonia testing on the same draw",
        ],
        "Lysed cells contaminate serum with substances that mimic or mask true levels. "
        "Reject hemolyzed specimens per laboratory criteria and redraw with gentle technique when ordered.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "When may bilirubin specimens be falsely lowered because of tube handling?",
        "Exposed to bright light without protection per lab policy",
        [
            "Labeled immediately at the bedside",
            "Transported upright in a leak-proof bag",
            "Mixed gently after fill per manufacturer instructions",
        ],
        "Light-sensitive analytes degrade during transport if not shielded. "
        "Follow laboratory instructions for protection from photodegradation.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What can anxiety-related hyperventilation before phlebotomy contribute to?",
        "Lightheadedness or vasovagal symptoms during the procedure",
        [
            "Hemolysis in every tube that is collected",
            "Permanent nerve damage even without needle contact",
            "A higher platelet count on the CBC alone",
        ],
        "Stress and rapid breathing reduce cerebral perfusion and can trigger syncope. "
        "A calm environment, seated position, and communication help prevent complications.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What may drawing above a hematoma from an earlier attempt cause?",
        "Further tissue trauma and unreliable specimen quality",
        [
            "Faster healing through the same puncture track",
            "A requirement to use arterial blood for chemistry",
            "Elimination of bruising when the needle is larger",
        ],
        "Collecting through injured tissue increases pain and bleeding. "
        "Select an untouched site on the same or opposite limb when feasible.",
        _REF,
        "intermediate",
    ),
    fact(
        "phleb-complications",
        "What is required after a needlestick with exposure to patient blood?",
        "Immediate wound washing and activation of the bloodborne pathogen protocol",
        [
            "Applying a bandage and documenting the stick at the end of the shift",
            "Completing the remaining draws before reporting the exposure",
            "Washing the site with a disinfectant and resuming patient care",
        ],
        "OSHA's Bloodborne Pathogens Standard requires prompt reporting and medical follow-up. "
        "Source-patient testing and post-exposure prophylaxis may be time-sensitive for HIV and hepatitis risk, so bandaging and waiting until shift end, finishing the remaining draws first, or disinfecting and returning to patient care all delay evaluation.",
        [S.OSHA_BBP, S.CLSI_GP41],
        "advanced",
    ),
    fact(
        "phleb-complications",
        "What reduces air embolism risk during venipuncture?",
        "Keeping the collection system below the heart and avoiding air in the line",
        [
            "Drawing a deliberate air bolus before tubes",
            "Holding the syringe hub highest above the patient",
            "Shaking the line to mix air with blood",
        ],
        "Air introduced into a vein under pressure can become an embolism, especially with central access. "
        "CLSI stresses closed systems and proper positioning for line collections per institutional policy.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "What is required when a vesicant medication extravasates near a phlebotomy attempt?",
        "Stopping the procedure and immediate notification of the nurse or provider",
        [
            "Continuing the venipuncture to finish the remaining tubes",
            "Applying warm compresses without escalating to the clinician",
            "Continuing the draw when blood was obtained and swelling appears",
        ],
        "Vesicants can cause tissue necrosis if they leak into surrounding tissue. "
        "Finishing the draw, applying compresses alone, and treating new swelling as incidental each delay the assessment that prevents tissue damage. "
        "Prompt assessment and intervention follow institutional chemotherapy and IV therapy protocols.",
        [S.CLSI_GP41, S.NHA_CPT],
        "advanced",
    ),
    fact(
        "phleb-complications",
        "How should pressure be applied after a suspected arterial nick at the antecubital fossa?",
        "Prolonged with clinician evaluation for continued bleeding",
        [
            "Omitted because arteries seal themselves once pressure stops",
            "Limited to five seconds before patient ambulation",
            "Replaced by massage to increase flow",
        ],
        "Arterial bleeding can be brisk and recur when pressure is removed too soon. "
        "Extended direct pressure and medical assessment reduce hematoma and compartment concerns.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "What policy should phlebotomy on the arm affected by mastectomy or lymph node removal follow?",
        "Surgeon and facility policy because of lymphedema and trauma risk",
        [
            "Using the surgical side first because the veins are easier to see",
            "Ignoring lymphedema risk when the veins look healthy",
            "Routine blood pressure and draws without documentation",
        ],
        "Limb protection limits infection and chronic swelling after lymphatic disruption. "
        "Many policies restrict venipuncture, BP, and IV access on the at-risk arm.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "What can collecting blood from a central venous catheter without policy training cause?",
        "Line contamination, air embolism, or hemolysis from high draw rates",
        [
            "Cleaner specimens than a peripheral stick because the line is already sterile",
            "Lower infection risk because the puncture site is already prepped",
            "Exemption from the order-of-draw rules for catheter collections",
        ],
        "Central line draws require specific flush, discard, and volume protocols. "
        "Untrained access increases catheter-related bloodstream infection and sample error risk. "
        "Assuming a clean line yields clean specimens, a prepped site lowers infection risk, or catheter draws bypass the order of draw each leave the patient unprotected.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "How should persisting numbness or weakness after venipuncture be managed?",
        "Documented and referred for clinical evaluation per policy",
        [
            "Treated as an expected finding for every patient",
            "Managed with ice and no notification to the provider",
            "Set aside when the collected tubes were labeled correctly",
        ],
        "Nerve injury may be transient or lasting; early documentation supports care and follow-up. "
        "CLSI quality programs expect reporting of significant adverse events from collection.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "When can hemolysis falsely elevate cardiac troponin or LDH results?",
        "Cellular contents leak into serum from traumatic collection",
        [
            "Tubes are filled to the correct volume on the draw",
            "The order of draw follows the CLSI sequence exactly",
            "Specimens are refrigerated immediately after the draw",
        ],
        "Intracellular enzymes and proteins rise with red-cell destruction in the tube. "
        "Clinicians may misinterpret hemolyzed samples unless the laboratory flags interference.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "Drawing from an AV fistula arm used for dialysis is generally considered what?",
        "Contraindicated except under explicit provider orders and protocol",
        [
            "Preferred because blood flow through the fistula is fastest",
            "Required for routine CBC on every dialysis patient",
            "Safe without extra training when a tight tourniquet is used",
        ],
        "Fistula trauma can threaten vascular access needed for dialysis. "
        "Use alternative peripheral sites unless the care team directs a controlled fistula draw.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "What does a rapid large-volume blood draw in a small pediatric patient increase the risk of?",
        "Hypovolemic symptoms such as dizziness or vasovagal collapse",
        [
            "Hypernatremia that appears in every infant after the draw",
            "Permanent loss of venous access in the sampled limb",
            "Improved tolerance when the child stands for the entire draw",
        ],
        "Children have smaller blood volume relative to draw size; limits follow age and laboratory guidance. "
        "Combine microcollection, seated positioning, and observation to prevent syncope.",
        _REF,
        "advanced",
    ),
    fact(
        "phleb-complications",
        "What does contamination of a peripheral draw with IV fluid from a proximal line cause?",
        "Dilution errors that may delay critical treatment decisions",
        [
            "Higher fidelity coagulation results on the same specimen",
            "No impact on chemistry if the fluid is saline",
            "Automatic rejection by the label printer at the bench",
        ],
        "Even isotonic fluids alter sodium, glucose, and other analytes when mixed with patient blood. "
        "Draw from a opposite limb or below a stopped infusion per CLSI and hospital policy.",
        _REF,
        "advanced",
    ),
]
