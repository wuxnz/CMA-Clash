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
        "How should sterile dressing supplies be opened so the wound-contact surface stays clean?",
        "Peel packages without touching the inner dressing pad with non-sterile gloves",
        [
            "Set the inner pad on the floor while opening the wrapper",
            "Blow across the pad to remove visible dust before placement",
            "Touch the pad with bare hands to test stickiness without provider assessment or documented orders",
        ],
        "Sterile technique keeps pathogens off tissue that will contact the wound. Floor contact and ungloved handling break the sterile field.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-002
    fact(
        "skill-wound-care",
        "Which solution is commonly ordered to irrigate a contaminated traumatic wound in clinic?",
        "Sterile normal saline delivered at appropriate pressure",
        [
            "Undiluted household bleach poured into the wound cavity",
            "Hydrogen peroxide instilled deep in tissue without a provider order",
            "Unfiltered tap water as the routine agent for every deep wound",
        ],
        "Saline removes debris with minimal tissue injury. Harsh agents can delay healing unless specifically directed.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-003
    fact(
        "skill-wound-care",
        "Which findings most suggest a wound infection that needs provider evaluation?",
        "Increasing pain, spreading erythema, warmth, and purulent drainage",
        [
            "Cool pale skin at the site without tenderness without provider assessment or documented orders",
            "Steady decrease in pain with fever and purulence",
            "Complete epithelial closure within twelve hours of every injury",
        ],
        "Local inflammation plus purulence signals infection. Painless purulence can still be serious.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-004
    fact(
        "skill-wound-care",
        "When removing sutures per provider order, what technique reduces dehiscence risk?",
        "Use sterile technique and cut the suture below the knot as instructed",
        [
            "Pull the knot through the skin to speed removal",
            "Reuse the same office scissors on multiple patients without cleaning",
            "Remove alternating sutures on a tense wound without provider direction",
        ],
        "Cutting below the knot avoids pulling tissue apart. Shared unclean instruments spread bloodborne pathogens.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-005
    fact(
        "skill-wound-care",
        "Which nursing measure helps prevent pressure injuries in immobile patients?",
        "Regular repositioning with moisture and friction management",
        [
            "Vigorous massage of reddened bony prominences without provider assessment or documented orders",
            "Keeping the patient in one position all day for stability",
            "Placing doughnut rings under the sacrum as routine care",
        ],
        "Offloading tissue restores perfusion to compressed skin. Massage of non-blanchable erythema can worsen ischemic damage.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-006
    fact(
        "skill-wound-care",
        "During a dressing change with anticipated blood contact, which PPE combination is appropriate?",
        "Gloves plus gown or apron when splash or soak-through is likely",
        [
            "Street clothes with no hand coverage during irrigation without provider assessment or documented orders",
            "A surgical mask worn on the forehead without securing straps",
            "Reused exam gloves from the prior patient if they look dry",
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
            "Circumferential tourniquet placement for every small cut",
            "Oral antibiotic tablets before any pressure is applied",
        ],
        "Direct pressure supports platelet plugging and clot formation. Tourniquets are reserved for life-threatening extremity hemorrhage per protocol.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-008
    fact(
        "skill-wound-care",
        "Before applying adhesive dressings, what history question helps prevent allergic reactions?",
        "Prior skin reactions to tape, latex, or topical adhesives",
        [
            "Childhood favorite meals at fast food restaurants",
            "Number of siblings in the household without provider assessment or documented orders",
            "Preferred television programming genre",
        ],
        "Contact dermatitis from adhesives is common and delays healing. Unrelated social details do not guide dressing choice.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-wound-care-009
    fact(
        "skill-wound-care",
        "When photographing a wound for the electronic record, what step protects patient privacy?",
        "Confirm consent and crop images to clinical anatomy per policy",
        [
            "Include the patient's full face and name badge in every frame",
            "Store photos on a personal phone without encryption without provider assessment or documented orders",
            "Email images to staff personal accounts for quick sharing",
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
            "Dry intact skin on the opposite foot without ulcer without provider assessment or documented orders",
            "Callus on the heel without open tissue or drainage",
            "Mild tingling in toes without open wound or erythema",
        ],
        "Osteomyelitis and deep infection threaten limb viability. Contralateral dry skin is not an acute ulcer complication.",
        [S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-011
    fact(
        "skill-wound-care",
        "During wound care intake, why is tetanus vaccination history important for a dirty laceration?",
        "It guides need for prophylaxis based on wound type and last dose timing",
        [
            "It determines the color of suture material selected",
            "It replaces cleansing and irrigation of the wound without provider assessment or documented orders",
            "It eliminates the need to assess neurovascular status",
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
            "Standing on the affected leg for the entire procedure",
            "Prone with the leg tightly flexed under the torso",
            "Seated with the leg dangling without support without provider assessment or documented orders",
        ],
        "Supported positioning improves visualization and reduces fall risk. Dangling or weight-bearing can increase edema and discomfort.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-014
    fact(
        "skill-wound-care",
        "Which non-drug measure can reduce procedural pain during wound cleansing?",
        "Explain steps, use room temperature saline, and allow brief pauses",
        [
            "Rush through irrigation without warning the patient",
            "Use ice-cold solution to shock the tissue without provider assessment or documented orders",
            "Apply tight circumferential band before explaining care",
        ],
        "Preparation and comfortable irrigation temperature lower anxiety and pain. Sudden cold or restraint increases distress.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-wound-care-015
    fact(
        "skill-wound-care",
        "What should home wound care teaching include before discharge from a dressing change visit?",
        "Hand hygiene, dressing supplies, infection warning signs, and follow-up timing",
        [
            "Soaking the wound in a hot tub daily unless told otherwise",
            "Sharing dressings with household members to save cost without provider assessment or documented orders",
            "Treating increased pain at home without calling the clinic",
        ],
        "Patients manage wounds between visits and must recognize escalation signs. Shared supplies and untreated pain increase complication risk.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-016
    fact(
        "skill-wound-care",
        "Which description best fits an arterial insufficiency ulcer on the lower extremity?",
        "Painful ulcer on toes or lateral malleolus with pale base and poor pulses",
        [
            "Punched-out round ulcer on the plantar arch with heavy granulation",
            "Moist ulcer in the axilla with satellite pustules without provider assessment or documented orders",
            "Painless ulcer on the medial ankle with brown hemosiderin staining",
        ],
        "Arterial ulcers reflect ischemia and often hurt at rest. Venous and pressure injuries have different locations and bases.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-017
    fact(
        "skill-wound-care",
        "A 72-year-old with chronic venous disease has a shallow ulcer on the medial lower leg with irregular borders and moderate exudate. Which dressing goal matches this presentation?",
        "Manage exudate and protect periwound skin while compression therapy continues per plan",
        [
            "Apply rigid casting without vascular assessment without provider assessment or documented orders",
            "Leave the wound open to air without any dressing layer",
            "Select a dry non-absorbent film as the sole layer for heavy drainage",
        ],
        "Venous ulcers often weep and need absorption plus edema control. Heavy drainage overwhelms thin films without secondary layers.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-018
    fact(
        "skill-wound-care",
        "A provider orders topical mupirocin for a colonized wound. What must the MA verify before application?",
        "Documented allergy history and a prescription or standing order for that agent",
        [
            "That every laceration receives triple antibiotic ointment by default",
            "That multiple ointments are mixed in one jar for convenience",
            "That ophthalmic ointment is used on an arm laceration without provider assessment or documented orders",
        ],
        "Topical antibiotics carry allergy and indication requirements. Mixing products and wrong routes create harm.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-019
    fact(
        "skill-wound-care",
        "A clinic manager asks an MA to perform sharp debridement with a scalpel on a necrotic heel ulcer. What is the appropriate response within typical MA scope?",
        "Decline and notify the provider that debridement requires licensed scope and training",
        [
            "Proceed after watching an online video without facility credentialing",
            "Use a non-sterile craft blade to save time without provider assessment or documented orders",
            "Perform the task without pain control when the patient objects",
        ],
        "Invasive debridement is outside standard MA practice. Licensed clinicians follow orders, anesthesia, and competency verification.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-020
    fact(
        "skill-wound-care",
        "How should blood-soaked wound dressings be disposed after a clinic dressing change?",
        "Place them in a biohazard bag or container per OSHA and facility policy",
        [
            "Discard small dressings in regular trash if folded tightly",
            "Leave open soiled gauze on the counter until end of shift",
            "Rinse and reuse inner gauze pads between patients without provider assessment or documented orders",
        ],
        "Contaminated waste can expose staff and housekeeping to bloodborne pathogens. Reprocessing dressings is unsafe.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-wound-care-021
    fact(
        "skill-wound-care",
        "When opening sterile supplies at the bedside, how should the inner dressing be handled?",
        "Use sterile technique so surfaces touching the wound stay uncontaminated",
        [
            "Touch the pad with non-sterile gloved fingers to center it",
            "Place the pad on the bedside floor to keep it flat",
            "Blow on the pad to remove lint before application without provider assessment or documented orders",
        ],
        "Sterile fields are broken when non-sterile items cross the boundary. Floor contact introduces environmental organisms.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-022
    fact(
        "skill-wound-care",
        "Which irrigation method best removes debris from a dirty wound while limiting tissue trauma?",
        "Sterile saline with syringe or similar device at safe pressure per training",
        [
            "High-pressure tap water jet directly from a sink hose without provider assessment or documented orders",
            "Routine undiluted iodine lavage in deep cavities without orders",
            "Air dusting with unfiltered compressor air across the wound",
        ],
        "Controlled saline flow clears foreign material without crushing tissue. Harsh chemicals need explicit orders.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-wound-care-023
    fact(
        "skill-wound-care",
        "Which cluster of signs should prompt suspicion of a surgical site infection?",
        "Worsening pain, spreading redness, warmth, and purulent drainage at the incision",
        [
            "Cool skin without tenderness at a healing line",
            "Steady pain relief with fever and pus at the site",
            "Hair regrowth along the scar without erythema without provider assessment or documented orders",
        ],
        "Purulence and spreading erythema indicate infection. Fever with pus is not reassuring even if pain changes.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-024
    fact(
        "skill-wound-care",
        "Why are non-adherent contact layers used beneath absorbent outer dressings?",
        "They reduce trauma to granulation tissue when the outer layer is changed",
        [
            "They chemically sterilize the wound bed on contact",
            "They replace wound assessment and cleansing steps without provider assessment or documented orders",
            "They deliberately macerate periwound skin to soften eschar",
        ],
        "Non-stick layers minimize bleeding and pain at dressing changes. They do not substitute for cleaning or monitoring.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-025
    fact(
        "skill-wound-care",
        "For a shallow wound with light to moderate exudate, when might a hydrocolloid dressing be selected?",
        "When a moist environment and autolytic debridement of slough are treatment goals",
        [
            "When active spurting arterial bleeding is present",
            "When deep tunneling needs packing without orders without provider assessment or documented orders",
            "When full-thickness burns cover a large area without transfer",
        ],
        "Hydrocolloids suit low to moderate drainage and autolysis. Hemorrhage and complex wounds need higher-level care.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-026
    fact(
        "skill-wound-care",
        "When does a foam dressing best match wound needs?",
        "Moderate to heavy exudate requiring absorption and cushioning",
        [
            "A dry eschar-covered wound without drainage concerns",
            "Spurting arterial hemorrhage from a laceration",
            "Rigid immobilization of the limb like a cast without provider assessment or documented orders",
        ],
        "Foam manages fluid while protecting skin. Arterial bleeding needs direct pressure and escalation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-027
    fact(
        "skill-wound-care",
        "For which wound presentation are calcium alginate dressings commonly chosen?",
        "Moderate to heavy exudate that gels on contact with wound fluid",
        [
            "Completely dry wounds without measurable drainage",
            "Intact skin without an open wound without provider assessment or documented orders",
            "Third-degree burns managed without specialist input",
        ],
        "Alginates absorb fluid and maintain moisture balance. They are inappropriate on dry wound beds.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-028
    fact(
        "skill-wound-care",
        "When is a transparent film dressing an appropriate primary layer?",
        "Superficial partial-thickness wounds with minimal exudate where visualization is useful",
        [
            "Heavy draining abdominal wounds without a secondary absorber",
            "Wounds with thick purulent drainage pooling under the film",
            "Full-thickness pressure injuries with slough and odor without provider assessment or documented orders",
        ],
        "Films seal lightly exuding wounds and allow inspection. Heavy drainage needs more absorbent dressings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-029
    fact(
        "skill-wound-care",
        "Before applying prescribed topical antibiotic to a suture line, what checks are required?",
        "Allergy history and confirmation of prescriber order for that product",
        [
            "Application of triple antibiotic to every cut without assessment",
            "Mixing several ointments in one container for the week",
            "Instilling arm ointment into the conjunctival sac without provider assessment or documented orders",
        ],
        "Medication allergies and route matter for topical agents. Eyes need specific ophthalmic formulations.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-030
    fact(
        "skill-wound-care",
        "What pressure injury prevention topics belong in patient and caregiver education?",
        "Repositioning schedules, support surfaces, and moisture management",
        [
            "Massaging areas of non-blanchable redness vigorously",
            "Maintaining one position all day to reduce falls without provider assessment or documented orders",
            "Using doughnut cushions under the coccyx routinely",
        ],
        "Tissue needs periodic relief from pressure and dryness control. Massage and doughnuts do not offload ischemic areas.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-031
    fact(
        "skill-wound-care",
        "What is the safest approach when removing skin sutures on a healed laceration?",
        "Sterile technique with cuts below the knot per provider instructions",
        [
            "Pulling knots through the skin to finish faster without provider assessment or documented orders",
            "Using unclean scissors shared between patients without disinfection",
            "Removing every other suture on a gaping wound without orders",
        ],
        "Proper cutting limits wound separation. Shared dirty instruments transmit infection.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-032
    fact(
        "skill-wound-care",
        "During a dressing change, blood soaks through the outer bandage despite prior pressure. What is the best immediate action?",
        "Add more gauze layers, maintain direct pressure, and notify the provider",
        [
            "Remove all dressings to air dry the wound in the waiting area without provider assessment or documented orders",
            "Apply a circumferential tourniquet for every minor oozing scrape",
            "Continue the visit without telling the clinician about ongoing bleeding",
        ],
        "Layered pressure supports hemostasis while help is mobilized. Tourniquets are for severe extremity bleeding per protocol.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-033
    fact(
        "skill-wound-care",
        "Which elements should serial wound measurements include for trending?",
        "Length, width, depth, and anatomical location using a consistent method",
        [
            "The color of footwear worn to the visit without provider assessment or documented orders",
            "Staff break times recorded without numeric wound data",
            "A single adjective without numbers at each visit",
        ],
        "Numeric measurements track healing progress. Inconsistent descriptors obscure clinical change.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-034
    fact(
        "skill-wound-care",
        "A provider orders a wound culture on a chronic ulcer. How should the specimen be obtained?",
        "After appropriate cleansing, sample fluid or tissue from the wound bed per technique",
        [
            "Swab the outer bandage without exposing the wound without provider assessment or documented orders",
            "Rub triple antibiotic deep into tissue before sampling",
            "Culture intact skin several centimeters away from the edge",
        ],
        "Bed sampling reflects pathogens in the wound. Surface bandage swabs add contaminant organisms.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-035
    fact(
        "skill-wound-care",
        "What does periwound maceration look like on examination?",
        "Whitish, softened, wrinkled skin from excess moisture under the dressing",
        [
            "Dry fissured skin far from the dressing margin",
            "Black eschar covering the entire limb without provider assessment or documented orders",
            "Cool cyanotic toes without surrounding moisture",
        ],
        "Maceration weakens skin and enlarges wounds. Dry eschar and ischemic toes are different findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-036
    fact(
        "skill-wound-care",
        "How does clean technique differ from sterile technique for some chronic wound dressings?",
        "Clean technique uses washed hands, clean gloves, and clean supplies per policy",
        [
            "Chronic wounds need no hand hygiene because bacteria are expected",
            "Bare hands may routinely touch the wound bed without provider assessment or documented orders",
            "Inner dressings may be reused between patients",
        ],
        "Policy defines acceptable cleanliness for maintenance changes. Reuse and bare hands remain unsafe.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-037
    fact(
        "skill-wound-care",
        "Why might silver-impregnated dressings appear on a treatment plan?",
        "To provide topical antimicrobial activity in heavily colonized wounds per provider orders",
        [
            "To replace IV antibiotics for osteomyelitis without medical orders",
            "To seal arterial bleeding without applying pressure",
            "To remove the need to watch for contact dermatitis without provider assessment or documented orders",
        ],
        "Silver dressings are adjuncts within comprehensive care. Allergic skin reactions still require monitoring.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-038
    fact(
        "skill-wound-care",
        "What is tunneling in a wound assessment?",
        "A passageway under the skin extending from the wound bed",
        [
            "Superficial dryness without measurable depth",
            "Hair growth encircling a healed incision",
            "A type of monofilament suture material without provider assessment or documented orders",
        ],
        "Tunnel dimensions guide packing and referral. Confusing anatomy delays appropriate treatment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-039
    fact(
        "skill-wound-care",
        "What does undermining along a wound margin indicate?",
        "Horizontal tissue loss beneath intact skin at the edge",
        [
            "A dry scab forming on the surface without provider assessment or documented orders",
            "Visible suture knots above the epidermis",
            "Completed epithelialization across the defect",
        ],
        "Undermining signals more extensive damage than the surface suggests. It informs dressing and specialty referral.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-040
    fact(
        "skill-wound-care",
        "A chronic wound develops foul odor and thick purulent drainage. What should the MA do first?",
        "Notify the provider and obtain assessment orders before changing therapy alone",
        [
            "Mask odor with scented lotion and send the patient home",
            "Apply an occlusive film to trap drainage without assessment",
            "Swab the waiting room air instead of the wound without provider assessment or documented orders",
        ],
        "Odor and pus suggest infection or necrotic tissue needing medical evaluation. Empiric dressing changes need orders.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-041
    fact(
        "skill-wound-care",
        "For which laceration is adhesive strip closure appropriate?",
        "A small superficial cut with edges that approximate without tension",
        [
            "A gaping wound with visible subcutaneous fat without provider assessment or documented orders",
            "A scalp laceration that typically needs staples",
            "An infected ulcer with purulence before cleansing",
        ],
        "Strips close low-tension superficial cuts. Deep, infected, or high-tension wounds need other management.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-wound-care-042
    fact(
        "skill-wound-care",
        "Why is face and eye protection recommended during wound irrigation?",
        "Blood and saline can splash and expose mucous membranes",
        [
            "Small wounds cannot produce infectious spray without provider assessment or documented orders",
            "Coworkers standing nearby do not need protection",
            "Used masks may be worn for a week without replacement",
        ],
        "Splash exposure warrants barriers under Standard Precautions. Infectious material can aerosolize from modest wounds.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
]
