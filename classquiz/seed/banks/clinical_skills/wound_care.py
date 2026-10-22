# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-wound-care)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-wound-care-001
    fact(
        "skill-wound-care",
        "How should a sterile wound dressing package be opened so the pad stays sterile?",
        "Peel the wrapper open and handle the pad by its edges",
        [
            "Tear the wrapper open and handle the pad by its edges",
            "Peel the wrapper open and handle the pad by its center",
            "Tear the wrapper open and handle the pad by its center",
        ],
        "Sterile technique keeps pathogens off the surface that will touch the wound, so the wrapper is peeled at a corner and the pad is handled by its edges. Tearing the wrapper ruptures the sterile barrier, and touching the pad surface with gloved fingers transfers organisms from the hands.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-002
    fact(
        "skill-wound-care",
        "Which irrigation solution is most often ordered for a contaminated traumatic wound in clinic?",
        "Sterile normal saline",
        [
            "Hydrogen peroxide",
            "Full-strength povidone-iodine",
            "Sterile water",
        ],
        "Saline lavage clears debris with low tissue toxicity. Peroxide and full-strength iodine can irritate tissue, and water alone lacks the tonicity many protocols prefer for wound irrigation.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-003
    fact(
        "skill-wound-care",
        "Which set of findings most strongly suggests a wound infection that needs provider evaluation?",
        "Increasing pain, spreading redness, warmth, and purulent drainage",
        [
            "Macerated white skin with a soaking wet dressing and steady pain",
            "Dry intact scab with mild redness that fades when the leg is raised",
            "Healed pink scar tissue with no drainage and no new symptoms",
        ],
        "Spreading erythema with rising pain, warmth, and purulent drainage is the classic pattern of a wound infection that warrants provider evaluation. Macerated white skin points to moisture damage, redness that fades with elevation suggests venous congestion, and healed scar tissue describes a wound that closed normally.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-004
    fact(
        "skill-wound-care",
        "When removing sutures on a healing laceration, which technique best protects the wound edges from separating?",
        "Cut below the knot and withdraw each suture in the direction of the knot",
        [
            "Cut above the knot and withdraw each suture in the direction of the knot",
            "Cut below the knot and pull the knot back through the wound edges",
            "Cut above the knot and pull the knot back through the wound edges",
        ],
        "Sutures are cut below the knot and withdrawn in the direction of the knot so the tract is not pulled apart, which lowers the chance of dehiscence. Cutting above the knot leaves suture material in the tissue, and pulling the knot backward through the wound edges drags contaminated suture across the tract.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-005
    fact(
        "skill-wound-care",
        "Which measure best prevents pressure injuries in an immobile patient?",
        "Regular repositioning with support surfaces and moisture control",
        [
            "Regular repositioning with massage over reddened bony prominences",
            "Regular repositioning with a foam ring under the heels",
            "Regular repositioning with a rigid ring under the sacrum",
        ],
        "Offloading tissue restores blood flow to skin that has been under pressure, so scheduled repositioning, support surfaces, and moisture control are the core measures. Massage over reddened bony prominences can damage ischemic tissue, and ring devices concentrate pressure on the very area they are meant to relieve.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-006
    fact(
        "skill-wound-care",
        "A dressing change on a bleeding wound is planned. Which PPE set fits standard precautions?",
        "Gloves with a gown when blood may contact skin or clothing",
        [
            "Gloves with a mask when blood may contact skin or clothing",
            "A gown with eye protection when blood may contact skin or clothing",
            "Eye protection with a mask when blood may contact skin or clothing",
        ],
        "Gloves protect the hands that handle the wound and a gown protects skin and clothing when blood may soak through, which makes that combination the fit for this task. A mask does not shield clothing or skin, and eye protection or a mask on its own leaves the hands and clothing unprotected.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-wound-care-007
    fact(
        "skill-wound-care",
        "What is the first action to control bleeding from a small laceration before closure?",
        "Apply firm direct pressure with clean gauze over the wound",
        [
            "Apply a tourniquet proximal to the wound while help is called",
            "Cleanse the wound with saline and cover it with a dry pad",
            "Coat the wound with antibiotic ointment and apply a gauze pad",
        ],
        "Firm direct pressure with clean gauze supports platelet plugging and clot formation, which makes it the first action for a minor laceration. A tourniquet is reserved for life-threatening extremity hemorrhage, cleansing before pressure can disturb forming clot, and ointment does nothing to slow bleeding.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-008
    fact(
        "skill-wound-care",
        "Before applying an adhesive dressing, which history question is most useful?",
        "Ask about prior skin reactions to tape, latex, or adhesives",
        [
            "Ask about prior skin reactions to soaps, detergents, and bath products",
            "Ask about prior seizure, cardiac, and medication history",
            "Ask about prior dietary, sleep, and bowel routine at home",
        ],
        "Contact dermatitis from tape, latex, or topical adhesives is common and delays healing, so allergy history guides dressing selection. Reactions to soaps or detergents do not predict adhesive allergy, and seizure, cardiac, dietary, or bowel history does not change which dressing is chosen.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-wound-care-009
    fact(
        "skill-wound-care",
        "Which elements should accompany a clinical wound photograph entered in the record?",
        "Consent, the anatomic location, and a measurement scale",
        [
            "Consent, the anatomic location, and the patient's full face",
            "Consent, the anatomic location, and the provider's name badge",
            "Consent, the anatomic location, and the clinic room number",
        ],
        "A wound photograph is most useful and compliant when it records consent, the anatomic site, and a scale so the wound can be compared across visits. Including the patient's face or identifiers adds protected information without clinical value, and a provider badge or room number describes the setting rather than the wound.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-010
    fact(
        "skill-wound-care",
        "A patient with diabetes has a foot ulcer with malodorous drainage. Which additional finding most strongly suggests osteomyelitis?",
        "A positive probe-to-bone test through the ulcer base",
        [
            "A capillary refill of two seconds in the toes",
            "A dorsalis pedis pulse palpable on the affected side",
            "A warm ankle with visible edema at the end of the day",
        ],
        "A positive probe-to-bone test means the probe reaches bone through the ulcer base, which raises concern for osteomyelitis and calls for prompt provider notification. Good capillary refill, a palpable dorsalis pedis pulse, and dependent edema reflect perfusion and venous status rather than bone involvement.",
        [S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-011
    fact(
        "skill-wound-care",
        "During wound care intake, why does tetanus vaccination history matter for a dirty laceration?",
        "It guides booster decisions based on wound type and last dose date",
        [
            "It determines the amount of local anesthetic given before wound closure",
            "It selects the type of suture material used to close the wound edges",
            "It replaces the cleansing and irrigation needed to treat the wound",
        ],
        "Tetanus risk rises with contaminated puncture, crush, or soil-exposed wounds, so vaccine history determines whether a booster or the full series is needed. Local anesthetic dosing and suture selection are unrelated to immunity, and history never substitutes for cleansing and irrigation.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-012
    fact(
        "skill-wound-care",
        "Where should a suture needle used during wound care be discarded?",
        "Into a labeled sharps container at the point of use",
        [
            "Into a biohazard bag taped to the side of the procedure cart",
            "Into a rigid container in the clean supply room",
            "Into a waste basket lined for clinical waste",
        ],
        "Contaminated sharps go straight into a labeled puncture-resistant container where they are used, which keeps them from being handled a second time. A bag on the cart or a bin in the supply room leaves the sharps exposed to drop risk, and a lined waste basket offers no puncture protection.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-wound-care-013
    fact(
        "skill-wound-care",
        "How should a patient with a lower leg ulcer be positioned for a dressing change?",
        "Supine or reclined with the leg supported and easily visible",
        [
            "Standing on the affected leg while the dressing change is performed",
            "Seated with the leg dangling freely over the chair edge",
            "Prone with the affected leg flexed under the torso",
        ],
        "Supporting the leg in a supine or reclined position keeps the wound visible, limits movement, and lowers fall risk during the change. Standing on the affected leg increases venous pressure and swelling, dangling lets fluid pool in the lower leg, and a flexed prone position is hard to reach and uncomfortable.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-014
    fact(
        "skill-wound-care",
        "Which measure reduces procedural pain during wound cleansing without medication?",
        "Explain the steps and irrigate with room-temperature solution",
        [
            "Irrigate with chilled solution to numb the wound more quickly",
            "Begin the irrigation without warning to shorten the procedure",
            "Apply a tight circumferential wrap around the limb before irrigating",
        ],
        "Explaining each step and using room-temperature solution keeps the patient oriented and avoids the shock of cold fluid on open tissue. Chilled solution causes vasoconstriction that worsens discomfort, starting without warning increases startle and movement, and a tight wrap reduces circulation to the limb.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-wound-care-015
    fact(
        "skill-wound-care",
        "A patient brings an antibiotic ointment to a suture line visit. Before applying it, what does the MA verify?",
        "Allergies and the prescriber order for that agent",
        [
            "Allergies and the wound measurements from the prior visit",
            "The prescriber order and the wound measurements from the prior visit",
            "Allergies and the ointment stock in the supply room",
        ],
        "Medication safety for a topical antibiotic means confirming that the patient has no allergy to the agent and that a provider ordered that product for this wound. Wound measurements belong to the dressing change assessment and ointment stock belongs to inventory, so neither replaces the allergy and order checks.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-016
    fact(
        "skill-wound-care",
        "Which topics belong in home teaching for a patient at risk for pressure injuries?",
        "Repositioning schedule, support surfaces, and skin inspection",
        [
            "Repositioning schedule, donut cushions, and skin inspection",
            "Repositioning schedule, massaging reddened areas, and skin inspection",
            "Repositioning schedule, limiting salt intake, and skin inspection",
        ],
        "Teaching for pressure injury prevention centers on a repositioning schedule, the use of support surfaces, and regular skin checks that catch early changes. Donut cushions concentrate pressure instead of relieving it, massage can damage ischemic tissue, and salt restriction addresses fluid balance rather than pressure relief.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-017
    fact(
        "skill-wound-care",
        "A patient returns for scheduled suture removal. What should the MA do first?",
        "Confirm the removal order and check that the edges are healed",
        [
            "Cut each suture, then confirm the removal order with the patient",
            "Apply a fresh dressing, then check the wound edges for redness",
            "Trim the sutures short and leave them to absorb on their own",
        ],
        "Sutures come out on the date the provider ordered and only after the edges show adequate healing, so the order and the wound check come first. Cutting before confirming the order risks removing sutures too early, dressing the wound first leaves them in place, and absorbable sutures are not removed this way.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-018
    fact(
        "skill-wound-care",
        "During a dressing change, blood soaks through the outer bandage despite pressure. What is the best immediate action?",
        "Add gauze layers, keep pressure on, and notify the provider",
        [
            "Remove the soaked dressings and let the wound air dry uncovered",
            "Wrap a tight tourniquet above the wound and finish the dressing",
            "Apply a dry gauze pad over the soak and continue the visit",
        ],
        "Soak-through means the dressing plan is not holding the bleeding, so layered gauze with continued direct pressure supports hemostasis while the provider is notified. Removing dressings to air dry can restart bleeding, a tourniquet is reserved for life-threatening extremity hemorrhage, and covering the area with a dry pad leaves the bleeding uncontrolled and unreported.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-019
    fact(
        "skill-wound-care",
        "Which elements should serial wound measurements include so healing can be compared over time?",
        "Length, width, depth, and site measured the same way",
        [
            "Length, width, depth, and odor described at each visit",
            "Length, width, depth, and the date the wound first appeared",
            "Length, width, depth, and the name of the dressing used",
        ],
        "Trend data requires numeric length, width, and depth recorded with the anatomic site using the same method and scale at each visit. Odor, onset date, and dressing type belong to the assessment and treatment record, but they do not show whether the wound is shrinking or growing.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-020
    fact(
        "skill-wound-care",
        "A provider orders a wound culture on a chronic ulcer. How should the specimen be collected?",
        "From cleansed wound bed tissue or fluid by culture technique",
        [
            "From the outer surface of the dressing that covered the wound bed",
            "From intact periwound skin beside the ulcer margin",
            "From the wound bed after topical antibiotic has been applied",
        ],
        "A wound culture must sample the organisms living in the wound, so cleansed tissue or exudate from the bed is collected using the correct technique. A dressing swab picks up surface contaminants, periwound skin does not reflect organisms in the wound, and topical antibiotic can suppress growth and hide the pathogen.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-021
    fact(
        "skill-wound-care",
        "What does periwound maceration look like on examination?",
        "Whitish, softened, wrinkled skin around the wound edge",
        [
            "Dry, cracked skin with flaking away from the wound edge",
            "Firm, thickened skin with a yellow callus at the edge",
            "Erythematous, warm skin with a red margin at the edge",
        ],
        "Maceration is the whitish, softened, wrinkled skin that forms when moisture collects under a dressing and breaks down the skin barrier. Dry cracked skin is xerosis, firm yellow callus is hyperkeratosis, and red warm skin points to inflammation rather than moisture damage.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-022
    fact(
        "skill-wound-care",
        "Which statement correctly describes clean technique for a chronic wound dressing change?",
        "Clean gloves and clean supplies are used because the bed harbors flora",
        [
            "Sterile gloves and sterile supplies are used because the bed harbors flora",
            "Clean gloves and clean supplies are used because the wound is deep",
            "Sterile gloves and sterile supplies are used because the wound is deep",
        ],
        "Clean technique suits a chronic wound whose bed harbors colonizing flora, so clean gloves and clean supplies are used for the dressing change. Sterile gloves and sterile supplies define sterile technique for surgically closed or deep wounds, and neither the supply set nor the reason in the other options fits clean technique.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-023
    fact(
        "skill-wound-care",
        "Why might a silver-impregnated dressing appear on a wound treatment plan?",
        "It gives topical antimicrobial activity in a colonized wound",
        [
            "It replaces systemic antibiotics for an osteomyelitis infection",
            "It stops arterial bleeding from a ruptured vessel",
            "It prevents a skin reaction to the adhesive around the wound",
        ],
        "Silver dressings release ions with broad topical antimicrobial activity, so a provider may order them for a wound with heavy colonization. Silver does not replace systemic antibiotics for osteomyelitis, it does not control arterial bleeding, and it does not prevent adhesive skin reactions.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-024
    fact(
        "skill-wound-care",
        "In wound assessment, what is tunneling?",
        "A blind passage extending under intact skin from the wound bed",
        [
            "A band of tissue loss beneath the wound edge and surrounding margins",
            "A dry crust that adheres to the wound bed surface",
            "A raised ridge of new tissue around the wound edges",
        ],
        "Tunneling is a blind-ended passage that extends under intact skin from the wound base, so a probe can follow it away from the visible wound. Tissue loss under the wound margin is undermining, a dry crust is eschar, and a raised ridge of new tissue is hypergranulation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-025
    fact(
        "skill-wound-care",
        "What does undermining along a wound margin indicate?",
        "Tissue loss beneath intact skin at the wound edge",
        [
            "A blind tract running under the skin from the wound base",
            "A dry hard crust that covers part of the wound bed",
            "New tissue growing above the level of the surrounding skin",
        ],
        "Undermining describes tissue loss that runs horizontally under intact skin at the wound edge, which hides more damage than the surface shows and guides dressing choice and referral. A blind tract under the skin is tunneling, a dry hard crust is eschar, and tissue raised above the skin surface is hypergranulation.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-026
    fact(
        "skill-wound-care",
        "A chronic wound develops foul odor and thick purulent drainage. What should the MA do first?",
        "Notify the provider and get orders before changing the therapy",
        [
            "Apply an occlusive film dressing to contain the drainage and odor",
            "Soak the wound in peroxide to clear the odor before dressing it",
            "Change the dressing schedule and recheck the wound in two weeks",
        ],
        "Foul odor with purulent drainage points to infection or necrotic tissue that needs provider assessment and new orders before the dressing plan changes. An occlusive film traps moisture and organisms, peroxide damages granulation tissue, and delaying the recheck lets an infection progress.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-027
    fact(
        "skill-wound-care",
        "For which laceration is adhesive strip closure an appropriate closure method?",
        "A small superficial cut with edges that approximate",
        [
            "A deep cut with separated edges and visible subcutaneous fat",
            "A scalp cut with hair tangled in the wound edges",
            "A puncture with a contaminated base and visible dirt",
        ],
        "Adhesive strips work on shallow, low-tension lacerations whose edges come together on their own, so skin adhesive and strips support closure without sutures. A deep cut with separated edges needs suturing, scalp lacerations are commonly closed with staples, and a contaminated puncture needs irrigation and closure planning.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-wound-care-028
    fact(
        "skill-wound-care",
        "Which exposure risk do eye and face protection address during wound irrigation?",
        "Splash of blood or irrigation fluid reaching the eyes and mouth",
        [
            "Contact with blood that soaks through the operator's clothing",
            "Droplets of irrigation fluid settling on nearby sterile supplies",
            "Droplets of wound drainage reaching the operator's forearms",
        ],
        "Eye and face protection guard the mucous membranes of the eyes, nose, and mouth, which irrigation splash can reach along with blood and wound fluid. Clothing, supply surfaces, and forearms are protected by gloves, gowns, and drapes, so eye and face protection does not address those exposures.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-029
    fact(
        "skill-wound-care",
        "Which instruction should be part of the home wound care teaching?",
        "Call the clinic if redness, swelling, or drainage grows",
        [
            "Call the clinic if the dressing needs changing more often than planned",
            "Call the clinic if the scab becomes dry and cracks",
            "Call the clinic if the wound looks cleaner at the first check",
        ],
        "Teaching after a dressing change must name the changes that mean infection may be developing, which are increasing redness, swelling, and drainage. Changing dressings more often than planned, a drying cracked scab, and a cleaner looking wound are expected parts of healing rather than reasons to call.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-030
    fact(
        "skill-wound-care",
        "Which description best fits an arterial insufficiency ulcer on the lower leg?",
        "A painful ulcer on the toes with a pale base and thin pulses",
        [
            "A painless ulcer on the inner ankle with brown skin staining",
            "A round ulcer on the sole of the foot with heavy drainage",
            "A shallow ulcer over the heel bone with clean pink edges",
        ],
        "Arterial ulcers reflect poor blood flow, so they sit on the toes or lateral foot, have a pale or punched-out base, and hurt because of ischemia. A painless medial ankle ulcer with brown hemosiderin staining is venous, a round plantar ulcer with heavy drainage suggests a neuropathic diabetic ulcer, and a clean shallow ulcer over the heel describes another process.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-031
    fact(
        "skill-wound-care",
        "A patient with chronic venous disease has a shallow medial leg ulcer with irregular borders and moderate exudate. Which dressing goal fits this presentation?",
        "Control exudate, protect the skin, and continue compression",
        [
            "Keep the wound open to air, and reassess the compression plan",
            "Cover the wound with a rigid cast, and defer the compression plan",
            "Pack the wound firmly, and change the dressing each shift",
        ],
        "Venous ulcers weep from venous hypertension, so the dressing plan absorbs exudate, protects the surrounding skin with a barrier, and supports the compression therapy already in place. Leaving the wound open promotes maceration, casting without vascular assessment risks ischemia, and packing a shallow ulcer damages tissue.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-032
    fact(
        "skill-wound-care",
        "A wound has heavy surface colonization but no systemic signs of infection. Why might a provider order topical mupirocin?",
        "It reduces surface bacteria without systemic exposure",
        [
            "It reaches bone and treats osteomyelitis in the wound",
            "It replaces the need for debridement of necrotic tissue",
            "It provides the systemic coverage that oral antibiotics lack",
        ],
        "Topical mupirocin lowers the bacterial load on the wound surface, so it suits heavy colonization without systemic signs of infection. It does not penetrate to bone, it does not remove necrotic tissue that needs debridement, and a topical agent cannot supply the systemic coverage that oral or intravenous antibiotics provide.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-033
    fact(
        "skill-wound-care",
        "A clinic manager asks an MA to perform sharp debridement of a necrotic heel ulcer with a scalpel. What is the appropriate response?",
        "Decline and tell the provider this needs a licensed clinician",
        [
            "Accept the task after the manager confirms the patient gave consent",
            "Accept the task after watching a training video on the procedure",
            "Accept the task after the patient signs a consent form for it",
        ],
        "Sharp debridement removes necrotic tissue and stays outside MA scope, so the request goes back to the provider, who can perform it or assign it within a licensed scope. A manager request, a consent form, and a training video do not change scope, and none of them verifies the competency a clinician must document.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-034
    fact(
        "skill-wound-care",
        "How should blood-soaked wound dressings be discarded after a clinic dressing change?",
        "In a labeled biohazard container for regulated waste",
        [
            "In a sealed plastic bag inside the exam room waste bin",
            "In the regular trash once the blood has dried and folded",
            "In the laundry hamper with the soiled linens",
        ],
        "Blood-soaked dressings are regulated waste under OSHA rules and go into a labeled biohazard container so staff and housekeeping are not exposed. A sealed bag in a room bin or a dried dressing in the regular trash treats contaminated waste as ordinary trash, and the laundry hamper is for linen that a laundry service processes.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-wound-care-035
    fact(
        "skill-wound-care",
        "Which statement describes the sterile field during a bedside wound dressing change?",
        "The inner wrapper and tray rim define the sterile field",
        [
            "The bedside table and the patient linens define the field",
            "The patient's bed and the privacy curtain define the field",
            "The exam table surface and the supply cart define the field",
        ],
        "Once a sterile kit is opened, the inner surface of the wrapper and the rim of the tray form the sterile field, and anything crossing that rim is no longer sterile. The bedside table and supply cart are working surfaces outside the field, and the bed, curtain, exam table, and linens sit outside it as well.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-036
    fact(
        "skill-wound-care",
        "Which irrigation method removes debris from a dirty wound while limiting tissue trauma?",
        "Sterile saline delivered by syringe at controlled low pressure",
        [
            "Sterile saline delivered by high-pressure pulsatile lavage",
            "Sterile saline applied as a soaking wet-to-dry gauze pack",
            "Sterile saline sprayed as a pressurized mist over the wound bed",
        ],
        "Saline delivered by syringe at controlled low pressure flushes debris out while protecting granulation tissue. High-pressure lavage drives contaminants deeper and can damage tissue, wet-to-dry gauze strips away healthy tissue along with the debris, and a pressurized mist disperses organisms into the air around the wound.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-wound-care-037
    fact(
        "skill-wound-care",
        "Which findings meet the usual criteria for a surgical site infection?",
        "Purulent drainage from the incision with spreading redness or fever",
        [
            "Clear drainage from the incision with mild redness at the suture line",
            "Dry crusting along the incision with tenderness at day three",
            "Normal redness around the incision on the first postoperative day",
        ],
        "A surgical site infection is defined by purulent incision drainage or by spreading inflammation such as redness, with fever or an elevated white count supporting the diagnosis. Clear drainage with mild suture-line redness, dry crusting with early tenderness, and redness on the first postoperative day are expected healing findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-038
    fact(
        "skill-wound-care",
        "Why are non-adherent contact layers placed beneath absorbent outer dressings?",
        "They reduce trauma to granulation tissue at each change",
        [
            "They add extra absorbency so the outer pad holds more fluid",
            "They keep periwound skin dry by pulling moisture from the edge",
            "They hold the antibiotic in place against the wound bed",
        ],
        "A contact layer such as petrolatum gauze or silicone mesh keeps the outer absorbent pad from adhering, so removing the dressing pulls less on granulation tissue and causes less bleeding and pain. Adding absorbency, drawing moisture from periwound skin, and holding medication against the bed are purposes of other dressing components.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-039
    fact(
        "skill-wound-care",
        "For a shallow wound with light to moderate exudate, when is a hydrocolloid dressing selected?",
        "When moist healing and autolytic debridement are the goals",
        [
            "When the wound needs packing for deep tunneling and dead space",
            "When the wound has heavy drainage and needs a secondary pad",
            "When the wound bed is dry and needs an absorptive layer",
        ],
        "Hydrocolloids keep a moist environment, absorb light to moderate exudate, and support autolytic debridement of slough, which fits a shallow wound with mild drainage. Deep tunneling needs packing, heavy drainage needs a more absorbent dressing with a secondary layer, and a dry wound bed needs moisture added rather than sealed.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-040
    fact(
        "skill-wound-care",
        "When does a foam dressing best match wound needs?",
        "Moderate to heavy exudate that needs absorption and cushioning",
        [
            "A wound with heavy exudate that needs a transparent adhesive seal",
            "A wound with no exudate that needs a thin adherent film",
            "A wound with light exudate that needs a non-adherent contact layer",
        ],
        "Foam dressings absorb moderate to heavy exudate while cushioning the wound and the surrounding skin, which suits draining wounds that need protection. A transparent film seals a lightly exuding surface, a non-adherent contact layer protects tissue under an absorbent pad, and neither one manages heavy drainage the way foam does.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-041
    fact(
        "skill-wound-care",
        "For which wound presentation are calcium alginate dressings commonly chosen?",
        "Moderate to heavy exudate that gels with wound fluid",
        [
            "A wound bed with minimal exudate and dry, intact skin",
            "A wound with heavy exudate that needs a clear adhesive film",
            "A wound with light exudate that needs a dry gauze bolster",
        ],
        "Alginate dressings absorb moderate to heavy drainage and form a gel that keeps the wound bed moist, so they suit exudative wounds. Minimal exudate with dry skin needs moisture added instead, a clear film seals a lightly exuding surface, and a dry gauze bolster mainly absorbs soaking exudate and pulls away tissue.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-042
    fact(
        "skill-wound-care",
        "When is a transparent film dressing an appropriate primary layer?",
        "Shallow partial-thickness wounds with minimal exudate",
        [
            "Full-thickness wounds with heavy drainage and tissue slough",
            "Wounds with heavy drainage that need an absorbent foam pad",
            "Deep wounds with a tunnel that need packing and a secondary layer",
        ],
        "A transparent film keeps a shallow, lightly exuding wound moist while letting the provider see the bed through the dressing, so it works well as a primary layer on partial-thickness wounds. Heavy drainage needs an absorbent primary dressing such as foam or alginate, slough needs a dressing that manages moisture, and a deep tunnel needs packing and a secondary layer.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
