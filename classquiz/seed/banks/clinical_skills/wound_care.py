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
        "In outpatient wound care, sterile dressing changes require the MA to, which action is appropriate?",
        "Open packages without contaminating inner surfaces",
        [
            "Touch sterile field with non-sterile gloves",
            "Reuse dressings from prior patient",
            "Blow on wound to dry",
        ],
        "Aseptic technique protects healing tissue. Clinic teams should follow facility policy and document findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-002
    fact(
        "skill-wound-care",
        "In outpatient wound care, irrigation of a dirty wound typically uses, which action is appropriate?",
        "Sterile normal saline under appropriate pressure",
        [
            "Hydrogen peroxide routinely inside deep wounds",
            "Unfiltered tap water not appropriate not appropriate",
            "Alcohol poured directly into cavity",
        ],
        "Saline irrigation removes debris with minimal tissue harm. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-003
    fact(
        "skill-wound-care",
        "In outpatient wound care, signs of wound infection include, which action is appropriate?",
        "Increased pain, erythema, warmth, and purulent drainage",
        [
            "Decreased pain not appropriate",
            "Cool pale skin at site not appropriate",
            "Complete healing at 24 hours not appropriate",
        ],
        "Infection requires provider evaluation. Clinic teams should follow facility policy and document findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-004
    fact(
        "skill-wound-care",
        "In outpatient wound care, when removing sutures, the MA should, which action is appropriate?",
        "Use sterile technique and cut as instructed below knot",
        [
            "Pull knot through skin",
            "Use non-sterile office scissors on multiple patients without cleaning",
            "Leave every other suture without order",
        ],
        "Proper technique reduces dehiscence risk. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-005
    fact(
        "skill-wound-care",
        "In outpatient wound care, pressure injury prevention includes, which action is appropriate?",
        "Regular repositioning and moisture management",
        [
            "Massaging bony prominences over reddened skin",
            "Keeping patient in one position all day",
            "Using doughnut rings routinely",
        ],
        "Offloading tissue reduces ischemic injury. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-006
    fact(
        "skill-wound-care",
        "In outpatient wound care, a hydrocolloid dressing is selected when, which action is appropriate?",
        "Light to moderate exudate and autolytic debridement are desired",
        [
            "Heavy arterial bleeding is present",
            "Deep tunneling without packing order",
            "Third-degree burns cover entire back",
        ],
        "Dressing choice matches exudate and wound bed. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-007
    fact(
        "skill-wound-care",
        "In outpatient wound care, documenting wound measurements should include, which action is appropriate?",
        "Length, width, depth, and location using consistent method",
        [
            "Color of patient shoes",
            "not appropriate verbal description without numbers",
            "Staff lunch time",
        ],
        "Serial measurements track healing. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-008
    fact(
        "skill-wound-care",
        "In outpatient wound care, non-adherent contact layers help, which action is appropriate?",
        "Prevent dressing from sticking to granulation tissue",
        [
            "Increase maceration not appropriate",
            "Replace need for cleansing",
            "Sterilize wound bed chemically",
        ],
        "Non-stick layers reduce trauma at dressing changes. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-009
    fact(
        "skill-wound-care",
        "In outpatient wound care, bleeding through a dressing requires, which action is appropriate?",
        "Adding more dressings and pressure while notifying provider",
        [
            "Removing all dressings to air dry",
            "Tight circumferential tape not appropriate",
            "Ignoring if patient is calm",
        ],
        "Escalation prevents hemorrhagic shock. Clinic teams should follow facility policy and document findings.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-010
    fact(
        "skill-wound-care",
        "In outpatient wound care, wound cultures are obtained, which action is appropriate?",
        "Per provider order using appropriate technique after cleansing",
        [
            "From outer dressing not appropriate",
            "After applying triple antibiotic without cleaning",
            "By swabbing intact skin far from wound",
        ],
        "Accurate sampling guides antibiotic therapy. Clinic teams should follow facility policy and document findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-011
    fact(
        "skill-wound-care",
        "In outpatient wound care, negative pressure wound therapy machines require, which action is appropriate?",
        "Seal check, canister disposal per biohazard policy, and ordered settings",
        [
            "House vacuum cleaner attachment",
            "Shared canisters between patients",
            "No documentation of pressure setting",
        ],
        "NPWT is a provider-ordered modality with safety checks. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-012
    fact(
        "skill-wound-care",
        "In outpatient wound care, latex allergy during dressing change is managed by, which action is appropriate?",
        "Using non-latex gloves and supplies",
        [
            "Using latex anyway",
            "Ignoring urticaria",
            "not appropriate documenting after anaphylaxis",
        ],
        "Alternative products prevent allergic reactions. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-wound-care-013
    fact(
        "skill-wound-care",
        "In outpatient wound care, a full-thickness wound may appear, which action is appropriate?",
        "Dry eschar or visible subcutaneous fat without epidermis",
        [
            "not appropriate a scratch with petechiae",
            "not appropriate non-draining",
            "Healed with epithelialization in hours",
        ],
        "Depth classification guides treatment and referral. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-014
    fact(
        "skill-wound-care",
        "In outpatient wound care, packing a wound cavity is done, which action is appropriate?",
        "Lightly, without overstuffing, per provider order",
        [
            "Tightly to prevent all drainage",
            "With non-sterile cotton from home",
            "Without measuring tunnel length",
        ],
        "Overpacking impairs perfusion. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-015
    fact(
        "skill-wound-care",
        "In outpatient wound care, patient education for home wound care includes, which action is appropriate?",
        "Hand hygiene, signs of infection, and follow-up timing",
        [
            "Ignoring increased pain",
            "Soaking in hot tub daily unless told",
            "Sharing dressings with family",
        ],
        "Education supports safe healing at home. Clinic teams should follow facility policy and document findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-016
    fact(
        "skill-wound-care",
        "In outpatient wound care, arterial insufficiency ulcers often occur, which action is appropriate?",
        "On toes and lateral malleoli with pale base and painful margins",
        [
            "not appropriate in axilla",
            "With heavy granulation and low pain not appropriate",
            "not appropriate in infants",
        ],
        "Vascular status affects healing plan. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-017
    fact(
        "skill-wound-care",
        "In outpatient wound care, venous stasis ulcers commonly appear, which action is appropriate?",
        "On medial lower leg with irregular borders and moderate exudate",
        [
            "On palms not appropriate",
            "With punched-out round shape not appropriate",
            "Without edema ever",
        ],
        "Compression therapy may be part of plan. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-018
    fact(
        "skill-wound-care",
        "In outpatient wound care, before applying topical antibiotic ointment, which action is appropriate?",
        "Confirm allergy history and provider order",
        [
            "Use on all wounds without assessment",
            "Mix multiple tubes for cost savings",
            "Apply inside eyes",
        ],
        "Medication allergies and indications matter. Clinic teams should follow facility policy and document findings.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-019
    fact(
        "skill-wound-care",
        "In outpatient wound care, sharp debridement in clinic is performed, which action is appropriate?",
        "not appropriate by trained licensed clinicians per scope and order",
        [
            "By any MA without training",
            "Using non-sterile craft knife",
            "Without anesthesia when painful",
        ],
        "Invasive debridement is outside typical MA scope. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-020
    fact(
        "skill-wound-care",
        "In outpatient wound care, disposal of contaminated wound dressings requires, which action is appropriate?",
        "Biohazard bag per OSHA and facility policy",
        [
            "Regular trash if small",
            "Open container at front desk",
            "Reprocessing for next patient",
        ],
        "Infectious waste handling protects staff and public. Clinic teams should follow facility policy and document findings.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-wound-care-021
    fact(
        "skill-wound-care",
        "When opening sterile dressing supplies at the bedside, the inner contents should be handled how?",
        "With sterile technique so the dressing surface touching the wound stays uncontaminated",
        [
            "By touching the pad with non-sterile gloved fingers",
            "By placing the pad on the floor to air dry",
            "By blowing on the pad to remove dust",
        ],
        "Sterile fields are considered contaminated when non-sterile items cross the boundary. Floor contact and ungloved handling introduce pathogens.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-022
    fact(
        "skill-wound-care",
        "Which solution is commonly used to irrigate a contaminated traumatic wound in clinic when ordered?",
        "Sterile normal saline at appropriate pressure",
        [
            "Undiluted household bleach poured into the cavity",
            "Hydrogen peroxide instilled routinely in deep wounds without orders",
            "Unfiltered tap water as the sole agent for every deep wound",
        ],
        "Saline removes debris with minimal tissue injury. Harsh agents can delay healing without provider direction.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-wound-care-023
    fact(
        "skill-wound-care",
        "Signs suggesting a surgical site infection include:",
        "Increasing pain, spreading erythema, warmth, and purulent drainage",
        [
            "Cool pale skin with no tenderness",
            "Complete epithelialization within twelve hours of every procedure",
            "Decreased pain with fever and purulence",
        ],
        "Local and systemic inflammatory signs warrant provider evaluation. Painless purulence is still concerning.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-024
    fact(
        "skill-wound-care",
        "Non-adherent contact layers in wound dressings primarily help:",
        "Reduce trauma to granulation tissue when the outer dressing is changed",
        [
            "Sterilize the wound bed chemically",
            "Replace cleansing and assessment",
            "Increase maceration of periwound skin as a goal",
        ],
        "Non-stick layers minimize bleeding and pain at changes. They do not replace cleaning or clinical monitoring.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-025
    fact(
        "skill-wound-care",
        "A hydrocolloid dressing is often chosen for wounds with:",
        "Light to moderate exudate where autolytic debridement is desired",
        [
            "Active arterial bleeding requiring hemostasis",
            "Deep tunneling without packing orders",
            "Full-thickness burns covering large body surface areas without transfer",
        ],
        "Dressing selection matches exudate level and wound goals. Heavy bleeding and complex wounds need higher-level care.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-026
    fact(
        "skill-wound-care",
        "Foam dressings are useful when the wound has:",
        "Moderate to heavy exudate needing absorption and cushioning",
        [
            "No drainage and a dry eschar without other concerns",
            "Active spurting arterial blood",
            "A need for rigid cast immobilization of the limb",
        ],
        "Foam manages fluid while protecting periwound skin. Arterial hemorrhage requires direct pressure and escalation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-027
    fact(
        "skill-wound-care",
        "Alginate dressings derived from seaweed are indicated for:",
        "Moderate to heavy exudate that forms a gel on contact",
        [
            "Completely dry wounds without drainage",
            "Intact uninfected skin without a wound",
            "Third-degree burns managed without specialist input",
        ],
        "Alginates absorb fluid and maintain a moist healing environment. They are inappropriate on dry wounds.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-028
    fact(
        "skill-wound-care",
        "Transparent film dressings are appropriate for:",
        "Superficial partial-thickness wounds with minimal exudate and a need to visualize the site",
        [
            "Heavy draining abdominal wounds without secondary layers",
            "Wounds with thick purulent drainage pooling under the film",
            "Full-thickness pressure injuries with slough and odor",
        ],
        "Films seal lightly exuding wounds and allow inspection. Heavy drainage needs more absorbent dressings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-029
    fact(
        "skill-wound-care",
        "Before applying topical antibiotic ointment to a wound, the MA should:",
        "Confirm allergy history and prescriber order for the product",
        [
            "Apply triple antibiotic to every laceration without assessment",
            "Mix multiple ointments in one jar for cost savings",
            "Instill ointment into the eye when the wound is on the arm",
        ],
        "Medication allergies and indications guide topical therapy. Eyes require specific ophthalmic products.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-030
    fact(
        "skill-wound-care",
        "Pressure injury prevention in clinic education emphasizes:",
        "Regular repositioning, support surfaces, and moisture management",
        [
            "Massaging reddened bony prominences vigorously",
            "Keeping patients in one position all day for stability",
            "Using doughnut rings under the sacrum routinely",
        ],
        "Offloading tissue reduces ischemic injury. Massage of non-blanchable erythema can worsen damage.",
        [S.NHA_CCMA, S.MEDLINEPLUS_HAND_HYGIENE],
        "intermediate",
    ),
    # skill-wound-care-031
    fact(
        "skill-wound-care",
        "When removing sutures per order, the MA should:",
        "Use sterile technique and cut below the knot as instructed",
        [
            "Pull the knot through the skin to speed removal",
            "Use the same non-sterile scissors on multiple patients without cleaning",
            "Remove alternating sutures without provider direction on a tense wound",
        ],
        "Proper cutting reduces dehiscence risk. Reusing unclean instruments spreads infection.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-wound-care-032
    fact(
        "skill-wound-care",
        "Bleeding through an outer dressing should prompt:",
        "Additional dressings with direct pressure and provider notification",
        [
            "Removing all layers to air dry the wound in the waiting room",
            "Circumferential tape tourniquet on every minor scrape",
            "Ignoring oozing if the patient appears calm",
        ],
        "Layered pressure supports hemostasis while help is mobilized. Tourniquets are reserved for life-threatening extremity bleeding per protocol.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-033
    fact(
        "skill-wound-care",
        "Documenting wound measurements should include:",
        "Length, width, depth, and anatomical location using a consistent method",
        [
            "The color of the patient's footwear",
            "Staff break times without numeric values",
            "A single word description without numbers each visit",
        ],
        "Serial numeric measurements track healing trends. Inconsistent methods obscure progress.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-034
    fact(
        "skill-wound-care",
        "Wound cultures are obtained:",
        "Per provider order after appropriate cleansing using proper technique",
        [
            "By swabbing the outer bandage without touching the wound",
            "After rubbing triple antibiotic deep into tissue without cleaning",
            "From intact skin several centimeters away from the edge",
        ],
        "Accurate sampling of wound bed fluid or tissue guides therapy. Surface contaminants mislead results.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-035
    fact(
        "skill-wound-care",
        "Signs of maceration around a wound include:",
        "Whitish, softened, wrinkled periwound skin from excess moisture",
        [
            "Dry cracking skin far from the dressing edge",
            "Black eschar across the entire limb",
            "Cool cyanotic toes without moisture",
        ],
        "Maceration breaks down skin barrier and enlarges the wound. Dressing changes may need more absorption.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-036
    fact(
        "skill-wound-care",
        "A clean technique dressing change differs from sterile technique in that clean technique:",
        "Uses sanitized hands and clean gloves with clean supplies for some chronic wounds per policy",
        [
            "Requires no hand hygiene because the wound is chronic",
            "Permits touching the wound bed with bare hands routinely",
            "Reuses inner dressings between patients",
        ],
        "Policy defines acceptable cleanliness levels for maintenance dressings. Reuse and bare hands remain unsafe.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-037
    fact(
        "skill-wound-care",
        "Silver-impregnated dressings may be selected to:",
        "Provide antimicrobial activity in heavily colonized wounds per provider plan",
        [
            "Replace systemic antibiotics for osteomyelitis without orders",
            "Seal arterial bleeding without pressure",
            "Eliminate the need to monitor for allergic contact dermatitis",
        ],
        "Topical antimicrobials are adjuncts within a comprehensive plan. Allergic reactions still require monitoring.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-wound-care-038
    fact(
        "skill-wound-care",
        "Tunneling in a wound refers to:",
        "A passageway under the skin surface extending from the wound bed",
        [
            "Superficial dryness without depth",
            "Hair growth around the incision",
            "A type of suture material",
        ],
        "Tunnel length and direction guide packing and referral. Misidentifying anatomy delays appropriate treatment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-039
    fact(
        "skill-wound-care",
        "Undermining at a wound edge means:",
        "Tissue destruction extending horizontally beneath intact skin along the margin",
        [
            "A scab forming on the surface",
            "Suture knots visible above the skin",
            "Complete healing with epithelialization",
        ],
        "Undermining indicates more extensive tissue loss than seen on the surface. Measurement informs dressing strategy.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-wound-care-040
    fact(
        "skill-wound-care",
        "When a wound has foul odor with purulence, the MA should:",
        "Notify the provider and obtain wound assessment orders before changing therapy alone",
        [
            "Mask odor with scented lotion and discharge the patient",
            "Apply occlusive film to trap drainage without assessment",
            "Culture the waiting room air instead of the wound",
        ],
        "Odor and purulence suggest infection or necrotic tissue needing medical evaluation. Empiric changes require orders.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-wound-care-041
    fact(
        "skill-wound-care",
        "Butterfly closures or adhesive strips are appropriate for:",
        "Small superficial lacerations with edges that approximate without tension",
        [
            "Gaping deep wounds with fat visible",
            "Bleeding scalp wounds requiring staples",
            "Infected purulent ulcers without cleansing",
        ],
        "Tissue adhesive and strips close low-tension superficial cuts. Deep or infected wounds need different management.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-wound-care-042
    fact(
        "skill-wound-care",
        "Irrigation splash during wound care requires:",
        "Face protection and gloves because blood and fluid may aerosolize",
        [
            "No PPE if the wound looks small",
            "Turning toward coworkers without shields",
            "Reusing masks for a week without cleaning",
        ],
        "Splash exposure risk warrants eye and face protection per Standard Precautions. Small wounds can still spray infectious material.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
]
