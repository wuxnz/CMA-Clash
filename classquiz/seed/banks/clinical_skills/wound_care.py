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
        "How should sterile dressing packages be opened to keep the wound-contact surface clean?",
        "Peel wrappers without touching the inner pad with non-sterile gloves",
        [
            "Set the inner pad on the floor briefly while opening the outer wrapper",
            "Blow gently across the pad to remove visible lint before wound placement",
            "Test adhesive stickiness with bare fingers directly on the pad surface",
        ],
        "Sterile technique keeps pathogens off tissue that will contact the wound. Floor contact, blowing on supplies, and ungloved pad handling break the sterile field.",
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
        "Which findings most suggest a wound infection needing provider evaluation?",
        "Increasing pain, spreading erythema, warmth, and purulent drainage",
        [
            "Cool pale skin at the site without tenderness or spreading warmth",
            "Fever with purulence but steadily decreasing local pain at the margin",
            "Epithelial closure within hours of every minor skin injury",
        ],
        "Local inflammation plus purulence signals infection. Cool non-tender skin and rapid epithelial closure are not typical infection patterns. Fever with pus remains urgent even if pain changes.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-004
    fact(
        "skill-wound-care",
        "When removing sutures per provider order, which technique reduces dehiscence risk?",
        "Use sterile technique and cut the suture below the knot as instructed",
        [
            "Pull the knot through the skin to finish the removal faster",
            "Reuse the same scissors on multiple patients without cleaning between",
            "Remove alternating sutures on a tense wound without provider direction",
        ],
        "Cutting below the knot avoids pulling tissue apart. Pulling knots through skin and shared unclean instruments increase dehiscence and infection risk.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-005
    fact(
        "skill-wound-care",
        "Which nursing measure helps prevent pressure injuries in immobile patients?",
        "Regular repositioning with moisture and friction management",
        [
            "Vigorous massage of reddened bony prominences during each shift",
            "Keeping the patient in one fixed position all day for stability",
            "Placing doughnut rings under the sacrum as routine standard care",
        ],
        "Offloading tissue restores perfusion to compressed skin. Massage of non-blanchable erythema and doughnut devices can worsen ischemic damage.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-006
    fact(
        "skill-wound-care",
        "During a dressing change with anticipated blood contact, which PPE combination is appropriate?",
        "Gloves plus gown or apron when splash or soak-through is likely",
        [
            "Street clothes with no hand coverage during wound irrigation",
            "A surgical mask worn on the forehead without securing the straps",
            "Reused exam gloves from the prior patient if they still look dry",
        ],
        "Gloves and protective clothing reduce splash exposure under Standard Precautions. Reused gloves do not maintain barrier integrity.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-wound-care-007
    fact(
        "skill-wound-care",
        "What is the first-line method to control bleeding from a minor laceration before closure?",
        "Firm direct pressure with clean gauze over the wound",
        [
            "Elevation of systemic blood pressure with salt tablets",
            "Circumferential tourniquet placement for a small finger cut",
            "Oral antibiotic tablets before any pressure is applied",
        ],
        "Direct pressure supports platelet plugging and clot formation. Tourniquets are reserved for life-threatening extremity hemorrhage per protocol.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-008
    fact(
        "skill-wound-care",
        "Before applying adhesive dressings, which history question helps prevent allergic reactions?",
        "Prior skin reactions to tape, latex, or topical adhesives",
        [
            "Favorite childhood meals eaten at local fast food restaurants",
            "Total number of siblings currently living in the household",
            "Preferred television programming genre for leisure viewing",
        ],
        "Contact dermatitis from adhesives is common and delays healing. Diet, family size, and entertainment preferences do not guide dressing selection.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-wound-care-009
    fact(
        "skill-wound-care",
        "When photographing a wound for the electronic record, what step protects patient privacy?",
        "Confirm consent and crop images to clinical anatomy per policy",
        [
            "Include the patient full face and name badge in every clinical frame",
            "Store wound photos on a personal phone without encryption or consent",
            "Email images to staff personal email accounts for quick sharing",
        ],
        "Consent and de-identification align with HIPAA expectations. Personal devices and broad sharing risk unauthorized disclosure.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-010
    fact(
        "skill-wound-care",
        "Which finding in a diabetic foot ulcer warrants urgent provider notification?",
        "Malodorous drainage with probe-to-bone sensation or spreading cellulitis",
        [
            "Dry intact skin on the opposite foot without ulceration, drainage, or odor",
            "Heel callus without open tissue, drainage, spreading redness, or warmth",
            "Mild toe tingling without open wound, erythema, purulence, or spreading redness",
        ],
        "Osteomyelitis and deep infection threaten limb viability. Contralateral dry skin or mild neuropathy without ulcer is less acute.",
        [S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-011
    fact(
        "skill-wound-care",
        "During wound care intake, why is tetanus vaccination history important for a dirty laceration?",
        "It guides prophylaxis based on wound type and last dose timing",
        [
            "It determines the color and size of suture material selected",
            "It replaces cleansing, irrigation, and dressing of the dirty wound",
            "It eliminates the need to assess neurovascular status before closure",
        ],
        "Tetanus risk rises with contaminated puncture or crush wounds. Vaccine history informs booster decisions alongside wound management.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-012
    fact(
        "skill-wound-care",
        "Where should contaminated sharps used during wound care be discarded?",
        "An approved sharps container at the point of use",
        [
            "A regular waste basket if the needle looks small",
            "An open tray on the front desk for later collection",
            "A biohazard bag mixed with paper recycling",
        ],
        "Point-of-use disposal lowers needlestick risk. Open containers and household trash are unsafe for contaminated sharps.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "beginner",
    ),
    # skill-wound-care-013
    fact(
        "skill-wound-care",
        "How should a patient be positioned for a lower leg ulcer dressing change when tolerated?",
        "Supine or reclined with the leg supported and accessible",
        [
            "Standing on the affected leg for the entire dressing procedure",
            "Prone with the leg tightly flexed under the torso without support",
            "Seated with the leg dangling freely without support or elevation",
        ],
        "Supported positioning improves visualization and reduces fall risk. Dangling or weight-bearing can increase edema and discomfort.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-014
    fact(
        "skill-wound-care",
        "Which non-drug measure can reduce procedural pain during wound cleansing?",
        "Explain steps, use room-temperature saline, and allow brief pauses",
        [
            "Rush through irrigation without warning or explaining steps to the patient",
            "Use ice-cold irrigation solution to shock the tissue and numb pain",
            "Apply a tight circumferential band before explaining the procedure",
        ],
        "Preparation and comfortable irrigation temperature lower anxiety and pain. Sudden cold or restraint increases distress and movement.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-wound-care-015
    fact(
        "skill-wound-care",
        "Before applying prescribed topical antibiotic to a suture line, what checks are required?",
        "Allergy history and confirmation of prescriber order for that product",
        [
            "Application of triple antibiotic to every cut without allergy assessment",
            "Mixing several topical ointments in one container for the week",
            "Instilling arm wound ointment into the conjunctival sac",
        ],
        "Medication allergies and route matter for topical agents. Eyes need specific ophthalmic formulations.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-016
    fact(
        "skill-wound-care",
        "What pressure injury prevention topics belong in patient and caregiver education?",
        "Repositioning schedules, support surfaces, and moisture management",
        [
            "Massaging areas of non-blanchable redness vigorously each shift",
            "Maintaining one position all day to reduce falls and skin shear",
            "Using doughnut cushions under the coccyx routinely for all patients",
        ],
        "Tissue needs periodic relief from pressure and dryness control. Massage and doughnuts do not offload ischemic areas.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-017
    fact(
        "skill-wound-care",
        "What is the safest approach when removing skin sutures on a healed laceration?",
        "Sterile technique with cuts below the knot per provider instructions",
        [
            "Pulling knots through the skin to finish the removal faster",
            "Using unclean scissors shared between patients without disinfection",
            "Removing every other suture on a gaping wound without provider orders",
        ],
        "Proper cutting limits wound separation. Shared dirty instruments transmit infection.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-018
    fact(
        "skill-wound-care",
        "During a dressing change, blood soaks through the outer bandage despite prior pressure. What is the best immediate action?",
        "Add gauze layers, maintain direct pressure, and notify the provider",
        [
            "Remove all dressings to air dry the wound openly in the waiting area",
            "Apply a circumferential tourniquet for minor oozing on a finger",
            "Continue the visit without telling the clinician about ongoing bleeding",
        ],
        "Layered pressure supports hemostasis while help is mobilized. Tourniquets are for severe extremity bleeding per protocol.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-019
    fact(
        "skill-wound-care",
        "Which elements should serial wound measurements include for trending?",
        "Length, width, depth, and anatomical location using a consistent method",
        [
            "Patient pain report alone without measuring length, width, depth, or location",
            "Staff break times recorded without numeric wound measurement data at visits",
            "A single descriptive adjective without numbers or location at each visit",
        ],
        "Numeric measurements track healing progress. Inconsistent descriptors obscure clinical change.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-020
    fact(
        "skill-wound-care",
        "A provider orders a wound culture on a chronic ulcer. How should the specimen be obtained?",
        "After cleansing, sample fluid or tissue from the wound bed per culture technique",
        [
            "Swab only the outer bandage without exposing, cleansing, or preparing the wound bed",
            "Rub triple antibiotic ointment deep into tissue before collecting the culture",
            "Culture intact periwound skin several centimeters away from the ulcer margin",
        ],
        "Bed sampling reflects pathogens in the wound. Surface bandage swabs and antibiotic pretreatment add contaminant organisms.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-021
    fact(
        "skill-wound-care",
        "What does periwound maceration look like on examination?",
        "Whitish, softened, wrinkled skin from excess moisture under the dressing",
        [
            "Dry fissured skin far from the dressing margin without softening or wrinkling",
            "Black eschar covering the entire limb without surrounding moisture or maceration",
            "Cool cyanotic toes without surrounding moisture, warmth, or maceration changes",
        ],
        "Maceration weakens skin and enlarges wounds. Dry eschar and ischemic toes are different findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-022
    fact(
        "skill-wound-care",
        "How does clean technique differ from sterile technique for some chronic wound dressings?",
        "Clean technique uses washed hands, clean gloves, and clean supplies per policy",
        [
            "Chronic wounds need no hand hygiene because colonizing bacteria are always expected",
            "Bare hands may routinely touch the wound bed during dressing changes without gloves",
            "Inner dressings may be reused between patients when they still look clean and dry",
        ],
        "Policy defines acceptable cleanliness for maintenance changes. Reuse and bare hands remain unsafe.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-023
    fact(
        "skill-wound-care",
        "Why might silver-impregnated dressings appear on a treatment plan?",
        "Topical antimicrobial activity in heavily colonized wounds per provider orders",
        [
            "To replace IV antibiotics for osteomyelitis without any medical orders or assessment",
            "To seal spurting arterial bleeding without applying direct pressure or escalation",
            "To remove the need to watch for contact dermatitis, rash, or skin reactions",
        ],
        "Silver dressings are adjuncts within comprehensive care. Allergic skin reactions still require monitoring.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-024
    fact(
        "skill-wound-care",
        "What is tunneling in a wound assessment?",
        "A passageway under the skin extending from the wound bed",
        [
            "Superficial dryness on the surface without measurable depth",
            "Hair growth encircling a healed incision without a tract",
            "A type of monofilament suture material used for closure",
        ],
        "Tunnel dimensions guide packing and referral. Confusing anatomy delays appropriate treatment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-025
    fact(
        "skill-wound-care",
        "What does undermining along a wound margin indicate?",
        "Horizontal tissue loss beneath intact skin at the edge",
        [
            "A dry scab forming on the surface without tissue loss below",
            "Visible suture knots above the epidermis along the incision line",
            "Completed epithelialization across the defect without hidden loss",
        ],
        "Undermining signals more extensive damage than the surface suggests. It informs dressing choice and specialty referral.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-026
    fact(
        "skill-wound-care",
        "A chronic wound develops foul odor and thick purulent drainage. What should the MA do first?",
        "Notify the provider and obtain assessment orders before changing therapy alone",
        [
            "Mask odor with scented lotion and send the patient home without provider assessment",
            "Apply an occlusive film to trap drainage without provider assessment or orders",
            "Swab the waiting room air instead of the wound bed for culture sampling",
        ],
        "Odor and pus suggest infection or necrotic tissue needing medical evaluation. Empiric dressing changes need orders.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-027
    fact(
        "skill-wound-care",
        "For which laceration is adhesive strip closure appropriate?",
        "A small superficial cut with edges that approximate without tension",
        [
            "A gaping wound with visible subcutaneous fat and edge tension",
            "A scalp laceration with hair and bleeding that typically needs staples",
            "An infected ulcer with purulence before cleansing and assessment",
        ],
        "Strips close low-tension superficial cuts. Deep, infected, or high-tension wounds need other management.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-wound-care-028
    fact(
        "skill-wound-care",
        "Why is face and eye protection recommended during wound irrigation?",
        "Blood and saline can splash and expose mucous membranes",
        [
            "Small wounds cannot produce infectious spray during irrigation",
            "Coworkers standing nearby do not need splash protection",
            "Used masks may be worn for a week without replacement or cleaning",
        ],
        "Splash exposure warrants barriers under Standard Precautions. Infectious material can aerosolize from modest wounds.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-029
    fact(
        "skill-wound-care",
        "What should home wound care teaching include before discharge from a dressing change visit?",
        "Hand hygiene, dressing supplies, infection warning signs, and follow-up timing",
        [
            "Soaking the wound in a hot tub daily at home unless explicitly told otherwise",
            "Sharing dressings with household members to save cost between dressing changes",
            "Treating increased pain, redness, and fever at home without calling the clinic",
        ],
        "Patients manage wounds between visits and must recognize escalation signs. Shared supplies and untreated pain increase complication risk.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-030
    fact(
        "skill-wound-care",
        "Which description best fits an arterial insufficiency ulcer on the lower extremity?",
        "Painful ulcer on toes or lateral malleolus with pale base and poor pulses",
        [
            "Punched-out round ulcer on the plantar arch with heavy granulation tissue",
            "Moist ulcer in the axilla with satellite pustules and friction damage",
            "Painless ulcer on the medial ankle with brown hemosiderin staining",
        ],
        "Arterial ulcers reflect ischemia and often hurt at rest. Venous and pressure injuries have different locations and wound bases.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-031
    fact(
        "skill-wound-care",
        "A 72-year-old with chronic venous disease has a shallow medial leg ulcer with irregular borders and moderate exudate. Which dressing goal matches this presentation?",
        "Manage exudate, protect periwound skin, and continue compression therapy per plan",
        [
            "Apply rigid casting without vascular assessment, compression planning, or orders",
            "Leave the wound open to air without any dressing, moisture control, or protection",
            "Use a dry non-absorbent film as the sole layer for heavy drainage without absorption",
        ],
        "Venous ulcers often weep and need absorption plus edema control. Heavy drainage overwhelms thin films without secondary layers.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-032
    fact(
        "skill-wound-care",
        "A provider orders topical mupirocin for a colonized wound. What must the MA verify before application?",
        "Documented allergy history and a prescription or standing order for that agent",
        [
            "That every laceration receives triple antibiotic ointment by default without orders",
            "That multiple topical ointments are mixed in one jar for convenience",
            "That ophthalmic ointment is applied to an arm laceration without indication",
        ],
        "Topical antibiotics carry allergy and indication requirements. Mixing products and wrong routes create harm.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-033
    fact(
        "skill-wound-care",
        "A clinic manager asks an MA to perform sharp debridement with a scalpel on a necrotic heel ulcer. What is the appropriate response within typical MA scope?",
        "Decline and notify the provider that debridement requires licensed scope and training",
        [
            "Proceed after watching an online video without facility credentialing",
            "Use a non-sterile craft blade to save time",
            "Perform the task without pain control when the patient objects before confirming allergy history in the chart",
        ],
        "Invasive debridement is outside standard MA practice. Licensed clinicians follow orders, anesthesia, and competency verification.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-034
    fact(
        "skill-wound-care",
        "How should blood-soaked wound dressings be disposed after a clinic dressing change?",
        "Place them in a biohazard bag or container per OSHA and facility policy",
        [
            "Discard small blood-soaked dressings in regular trash if folded tightly",
            "Leave open soiled gauze on the counter until the end of the shift",
            "Rinse and reuse inner gauze pads between patients when they look dry",
        ],
        "Contaminated waste can expose staff and housekeeping to bloodborne pathogens. Reprocessing dressings is unsafe.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-wound-care-035
    fact(
        "skill-wound-care",
        "When opening sterile supplies at the bedside, how should the inner dressing be handled?",
        "Keep surfaces that touch the wound free of non-sterile contact",
        [
            "Center the pad with non-sterile gloved fingers on the wound side",
            "Place the pad on the bedside floor to keep it flat",
            "Blow on the pad to remove lint before application",
        ],
        "Sterile fields are broken when non-sterile items cross the boundary. Floor contact and mouth aerosols introduce organisms.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-036
    fact(
        "skill-wound-care",
        "Which irrigation method best removes debris from a dirty wound while limiting tissue trauma?",
        "Sterile saline with syringe or similar device at safe pressure per training",
        [
            "High-pressure tap water jet directly from a sink hose into the open wound",
            "Routine undiluted iodine lavage in deep wound cavities without provider orders",
            "Compressed air blown across the wound bed from an unfiltered unsterile source",
        ],
        "Controlled saline flow clears foreign material without crushing tissue. Harsh chemicals need explicit orders.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-wound-care-037
    fact(
        "skill-wound-care",
        "Which cluster of signs should prompt suspicion of a surgical site infection?",
        "Worsening pain, spreading redness, warmth, and purulent drainage at the incision",
        [
            "Cool skin without tenderness, warmth, or drainage along a healing incision line",
            "Steady pain relief with fever, warmth, and purulent drainage at the incision site",
            "Hair regrowth along the healed scar without erythema, warmth, or purulence",
        ],
        "Purulence and spreading erythema indicate infection. Fever with pus is not reassuring even if pain changes.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-038
    fact(
        "skill-wound-care",
        "Why are non-adherent contact layers used beneath absorbent outer dressings?",
        "They reduce trauma to granulation tissue when the outer layer is changed",
        [
            "They chemically sterilize the wound bed on contact without cleansing or assessment",
            "They replace wound assessment, cleansing, and dressing change steps entirely",
            "They deliberately macerate periwound skin to soften eschar quickly without monitoring",
        ],
        "Non-stick layers minimize bleeding and pain at dressing changes. They do not substitute for cleaning or monitoring.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-039
    fact(
        "skill-wound-care",
        "For a shallow wound with light to moderate exudate, when might a hydrocolloid dressing be selected?",
        "When moist healing and autolytic debridement of slough are treatment goals",
        [
            "When active spurting arterial bleeding is present at the wound base",
            "When deep tunneling needs packing and debridement without provider orders",
            "When full-thickness burns cover a large body area without specialist transfer",
        ],
        "Hydrocolloids suit low to moderate drainage and autolysis. Hemorrhage and complex wounds need higher-level care.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-040
    fact(
        "skill-wound-care",
        "When does a foam dressing best match wound needs?",
        "Moderate to heavy exudate requiring absorption and cushioning",
        [
            "A dry eschar-covered wound without drainage or exudate concerns",
            "Spurting arterial hemorrhage from a laceration needing direct pressure",
            "Rigid immobilization of the limb like a cast without wound care",
        ],
        "Foam manages fluid while protecting skin. Arterial bleeding needs direct pressure and escalation, not absorbent dressings alone.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-041
    fact(
        "skill-wound-care",
        "For which wound presentation are calcium alginate dressings commonly chosen?",
        "Moderate to heavy exudate that gels on contact with wound fluid",
        [
            "Completely dry wounds without measurable drainage or exudate",
            "Intact skin without an open wound or area of breakdown",
            "Third-degree burns managed without specialist input or referral",
        ],
        "Alginates absorb fluid and maintain moisture balance. They are inappropriate on dry wound beds or intact skin.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-042
    fact(
        "skill-wound-care",
        "When is a transparent film dressing an appropriate primary layer?",
        "Partial-thickness wounds with minimal exudate where visualization helps",
        [
            "Heavy draining abdominal wounds without a secondary absorbent dressing layer underneath",
            "Wounds with thick purulent drainage pooling under the transparent film dressing",
            "Full-thickness pressure injuries with slough, odor, and heavy exudate drainage",
        ],
        "Films seal lightly exuding wounds and allow inspection. Heavy drainage needs more absorbent dressings.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
