# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-emergency-aid)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [

    # skill-emergency-aid-001
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, the first step in any emergency in clinic is, which action is appropriate?",
        "Assess scene safety and use PPE as needed",
        [
            "Run into unknown hazards",
            "Begin treatment without gloves",
            "Leave the patient alone",
        ],
        "Provider safety enables continued care. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-emergency-aid-002
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, when a patient faints, the MA should, which action is appropriate?",
        "Lower patient to floor, elevate legs if no injury, and monitor airway",
        [
            "Seat patient upright immediately",
            "Offer large meal",
            "Ignore until end of shift",
        ],
        "Supine position improves cerebral perfusion. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-003
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, an epinephrine auto-injector is administered, which action is appropriate?",
        "Into the outer thigh through clothing if necessary per device instructions",
        [
            "Into the buttock not appropriate",
            "Intravenously by MA without order",
            "Orally",
        ],
        "IM thigh delivery is standard for anaphylaxis kits. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-emergency-aid-004
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, syncope with fall requires assessment for, which action is appropriate?",
        "Head injury and cervical spine precautions if trauma suspected",
        [
            "not appropriate blood glucose",
            "Immediate discharge",
            "No documentation",
        ],
        "Falls may cause intracranial injury. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-005
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, active bleeding from a laceration is initially controlled by, which action is appropriate?",
        "Direct pressure with clean gauze",
        [
            "Elevation of blood pressure",
            "Tourniquet for every minor cut",
            "Oral antibiotics first",
        ],
        "Pressure supports hemostasis while help arrives. Clinic teams should follow facility policy and document findings.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-006
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, a patient with chest pain and diaphoresis should trigger, which action is appropriate?",
        "Immediate provider notification and preparation for emergency response",
        [
            "Scheduling routine follow-up next month",
            "Ambulation in hallway",
            "Withholding oxygen without orders",
        ],
        "Acute coronary syndrome requires rapid escalation. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-007
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, seizure first aid includes, which action is appropriate?",
        "Protecting head, clearing nearby hazards, and timing the event",
        [
            "Restraining limbs tightly",
            "Placing objects in mouth",
            "Giving food during seizure",
        ],
        "Safety and timing guide post-ictal care. Clinic teams should follow facility policy and document findings.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-008
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, heat stroke is distinguished from heat exhaustion by, which action is appropriate?",
        "Hot dry skin or anhidrosis with altered mental status in severe cases",
        [
            "not appropriate mild sweating",
            "Normal temperature not appropriate",
            "Bradycardia without CNS changes",
        ],
        "Heat stroke is a medical emergency needing rapid cooling. Clinic teams should follow facility policy and document findings.",
        [S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-009
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, for chemical exposure on skin in clinic, which action is appropriate?",
        "Remove contaminated clothing and flush with water per SDS guidance",
        [
            "Neutralize with unknown chemicals",
            "Cover without rinsing",
            "Delay rinse for documentation",
        ],
        "Copious irrigation reduces tissue damage. Clinic teams should follow facility policy and document findings.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-010
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, emergency oxygen setup requires, which action is appropriate?",
        "Verifying order, flow rate, and delivery device per protocol",
        [
            "Smoking at bedside",
            "Max flow without humidification not appropriate",
            "Sharing cannula between patients",
        ],
        "Oxygen is a medication requiring orders and safety checks. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-011
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, a patient reporting suicidal ideation requires, which action is appropriate?",
        "Immediate notification of provider and not appropriate leaving patient alone unsupervised",
        [
            "Promise of confidentiality without telling anyone",
            "Scheduling routine visit",
            "Dismissing as attention seeking",
        ],
        "Suicide risk mandates escalation and safety planning. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-012
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, anaphylaxis after injection in clinic is treated with, which action is appropriate?",
        "Epinephrine, EMS activation, and monitoring per emergency protocol",
        [
            "Oral antihistamine not appropriate and discharge",
            "Delayed observation 5 minutes",
            "Heat packs to injection site",
        ],
        "Epinephrine is first-line for systemic reaction. Clinic teams should follow facility policy and document findings.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-013
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, eye injury from flying metal requires, which action is appropriate?",
        "Shielding eye, no pressure, and urgent ophthalmology/EMS referral",
        [
            "Rubbing eye to remove particle",
            "Flushing with caustic solution",
            "Removing embedded object in clinic",
        ],
        "Penetrating eye injuries need specialist care. Clinic teams should follow facility policy and document findings.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-014
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, back injury with suspected spinal trauma, which action is appropriate?",
        "Manual stabilization and avoid moving patient unless immediate danger",
        [
            "Log roll without training",
            "Standing patient to walk pain off",
            "Massage paraspinal muscles",
        ],
        "Spinal motion restriction reduces cord injury. Clinic teams should follow facility policy and document findings.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-015
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, hyperglycemic crisis signs may include, which action is appropriate?",
        "Polyuria, dehydration, fruity breath, and altered mental status",
        [
            "not appropriate mild hunger",
            "Bradycardia without symptoms",
            "Hypothermia not appropriate",
        ],
        "DKA/HHS require emergency treatment. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-016
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, a choking patient in clinic who becomes cyanotic needs, which action is appropriate?",
        "Age-appropriate airway maneuvers and activation of emergency response",
        [
            "Waiting for family",
            "Heimlich on all infants",
            "Blind finger sweeps",
        ],
        "Airway obstruction can progress to arrest quickly. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-017
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, emergency medication crash cart checks ensure, which action is appropriate?",
        "Defibrillator pads, airway devices, and drugs are present and not expired",
        [
            "not appropriate cosmetic organization",
            "Removal of epinephrine",
            "Shared vials between patients",
        ],
        "Routine checks support resuscitation readiness. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-018
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, postpartum hemorrhage simulation in MA training emphasizes, which action is appropriate?",
        "Rapid recognition, fundal massage per protocol, and provider notification",
        [
            "Delay for billing",
            "Withholding large-bore IV access preparation",
            "Discharging without vitals",
        ],
        "Obstetric emergencies need immediate team response. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-019
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, bites from humans or animals in clinic require, which action is appropriate?",
        "Wound cleansing, tetanus status review, and referral per protocol",
        [
            "Primary closure of all bite wounds not appropriate",
            "No documentation of species",
            "Ignoring rabies risk",
        ],
        "Bites have high infection and rabies considerations. Clinic teams should follow facility policy and document findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-020
    fact(
        "skill-emergency-aid",
        "During a clinic emergency within medical assisting scope, emergency evacuation of clinic uses, which action is appropriate?",
        "Posted routes, assistance for mobility-impaired patients, and roll call",
        [
            "Single exit not appropriate without plan",
            "Elevators during fire",
            "Leaving records unsecured in hallway",
        ],
        "Drills and plans reduce harm during disasters. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA, S.OSHA_BBP],
        "advanced",
    ),
    # skill-emergency-aid-021
    fact(
        "skill-emergency-aid",
        "For an adult with suspected cardiac arrest in clinic, high-quality CPR emphasizes:",
        "Hard, fast compressions at 100 to 120 per minute with minimal interruptions",
        [
            "Compressions two inches deep at thirty per minute",
            "Pausing five minutes between cycles to rest",
            "Compressing the upper abdomen",
        ],
        "AHA guidelines stress rate, depth, and recoil for perfusion. Abdominal compressions are not standard BLS.",
        [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
        "intermediate",
    ),
    # skill-emergency-aid-022
    fact(
        "skill-emergency-aid",
        "AED pads for an adult should be placed:",
        "On bare dry chest per device diagram, one upper right and one lower left side",
        [
            "Over medication patches without removal",
            "On wet skin while patient stands in a pool",
            "Crossed over each other on the sternum against instructions",
        ],
        "Proper pad placement and dry skin improve shock delivery. Medication patches may cause arcing if not managed per training.",
        [S.AHA_ADULT_BLS, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-023
    fact(
        "skill-emergency-aid",
        "Stroke recognition using FAST emphasizes:",
        "Face droop, arm weakness, speech difficulty, and time to call emergency services",
        [
            "Foot pain as the primary sign",
            "Abdominal distention",
            "Itchy eyes",
        ],
        "Time-sensitive reperfusion therapy depends on early activation of EMS.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-024
    fact(
        "skill-emergency-aid",
        "Nosebleed first aid includes:",
        "Sitting upright, leaning forward slightly, and pinching soft part of nose for ten to fifteen minutes",
        [
            "Head tilted far back swallowing blood",
            "Packing with unsterile objects without assessment",
            "Ignoring anticoagulant use history",
        ],
        "Forward lean prevents blood swallowing. Prolonged bleeding on anticoagulants needs escalation.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-025
    fact(
        "skill-emergency-aid",
        "Hypoglycemia in a conscious cooperative adult may be treated with:",
        "Fifteen grams fast-acting carbohydrate and recheck per protocol",
        [
            "High-fat meal as first step",
            "IM glucagon before checking glucose when patient can swallow",
            "Withholding food despite confusion and sweating",
        ],
        "Rapid sugar raises glucose; glucagon is for unable-to-swallow scenarios per orders.",
        [S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-026
    fact(
        "skill-emergency-aid",
        "Burn thermal injury first aid in clinic includes:",
        "Cool running water on small burns and removal of constricting jewelry",
        [
            "Applying butter or ice directly for long periods",
            "Popping all blisters immediately",
            "Ignoring inhalation injury signs after fire",
        ],
        "Cooling limits depth; circumferential burns may need escharotomy evaluation.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-027
    fact(
        "skill-emergency-aid",
        "A patient stung by a bee with tongue swelling needs:",
        "Emergency response activation and epinephrine per anaphylaxis protocol",
        [
            "Oral diphenhydramine alone with discharge",
            "Ice on the sting while sending patient to drive home",
            "Observation without airway assessment",
        ],
        "Airway angioedema can progress rapidly.",
        [S.RED_CROSS_FIRST_AID, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-emergency-aid-028
    fact(
        "skill-emergency-aid",
        "Infant choking with ineffective cough requires:",
        "Back blows and chest thrusts per pediatric BLS guidelines",
        [
            "Abdominal thrusts identical to adult technique",
            "Finger sweeps blindly in the mouth",
            "Waiting without activating help",
        ],
        "Age-specific maneuvers protect small airways.",
        [S.AHA_ADULT_BLS, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-029
    fact(
        "skill-emergency-aid",
        "Postpartum hemorrhage symptoms include:",
        "Heavy bleeding, hypotension, tachycardia, and altered mental status",
        [
            "Mild spotting alone as the sole concern",
            "Improved energy with blood loss",
            "Bradycardia with stable perfusion as classic sign",
        ],
        "Obstetric emergencies need rapid team response and fluid resuscitation.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-030
    fact(
        "skill-emergency-aid",
        "Needlestick injury in clinic first aid includes:",
        "Wash wound, report promptly, and follow post-exposure protocol",
        [
            "Ignore if glove appeared intact",
            "Squeeze wound and apply oral suction",
            "Wait one week before telling supervisor",
        ],
        "Early evaluation enables prophylaxis when indicated.",
        [S.OSHA_NEEDLESTICK, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-emergency-aid-031
    fact(
        "skill-emergency-aid",
        "Patient with sudden severe headache and neck stiffness needs:",
        "Immediate provider evaluation for possible meningitis or subarachnoid hemorrhage",
        [
            "Dark room rest without vital signs for three days",
            "Massage of neck muscles vigorously",
            "Discharge with acetaminophen alone",
        ],
        "Thunderclap headache with meningismus is an emergency presentation.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-032
    fact(
        "skill-emergency-aid",
        "Angulated forearm deformity after fall suggests:",
        "Fracture requiring immobilization and urgent imaging per protocol",
        [
            "Sprain requiring immediate weight bearing marathon",
            "No splint until next week",
            "Heat packs instead of immobilization",
        ],
        "Deformity implies bony injury; splint and elevate while arranging transport.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-033
    fact(
        "skill-emergency-aid",
        "Dental avulsion in a child within an hour may benefit from:",
        "Reimplantation attempts per protocol using appropriate storage solution and urgent dental referral",
        [
            "Scrubbing the root with dry gauze",
            "Storing tooth in tap water long term without guidance",
            "Discarding tooth without patient counseling",
        ],
        "Time-critical reimplantation may save the tooth when handled correctly.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-034
    fact(
        "skill-emergency-aid",
        "Carbon monoxide exposure suspicion warrants:",
        "Removing patient from source, oxygen, and emergency evaluation",
        [
            "Sending patient back to garage to finish chores",
            "Treating as anxiety without pulse oximetry limitations explained",
            "Standard pulse oximetry alone ruling out carboxyhemoglobin",
        ],
        "Pulse oximetry may read falsely normal; co-oximetry is definitive in hospital.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-035
    fact(
        "skill-emergency-aid",
        "Diabetic patient with insulin pump alarm and vomiting should:",
        "Receive provider notification and ketone or glucose assessment per protocol",
        [
            "Ignore pump because it is automatic",
            "Turn pump off without medical guidance and leave",
            "Exercise intensely to lower glucose",
        ],
        "Illness increases DKA risk even with pumps.",
        [S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-036
    fact(
        "skill-emergency-aid",
        "Thunderstorm asthma or severe wheeze in clinic requires:",
        "Provider evaluation, bronchodilator therapy per orders, and monitoring oxygenation",
        [
            "Discharge without peak flow or pulse oximetry",
            "Cold air exposure as treatment",
            "Assuming panic attack without auscultation",
        ],
        "Respiratory distress can progress to failure; objective assessment guides therapy.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-037
    fact(
        "skill-emergency-aid",
        "Amputated fingertip with clean wound should be:",
        "Wrapped in saline moist gauze, placed in bag on ice, and sent with patient to specialty care",
        [
            "Placed directly on dry ice touching tissue",
            "Soaked in antiseptic alcohol for hours",
            "Discarded in sharps container",
        ],
        "Proper cooling preserves tissue for possible reattachment.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-038
    fact(
        "skill-emergency-aid",
        "Lightning strike victim in parking lot should be:",
        "Moved to safety if scene remains dangerous, then assessed for cardiac arrest and burns",
        [
            "Touched simultaneously by many rescuers on wet ground during active storm",
            "Declared dead without assessment",
            "Given large oral fluids while unconscious",
        ],
        "Lightning victims may have recoverable rhythms; scene safety comes first.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-039
    fact(
        "skill-emergency-aid",
        "Foreign body in ear in a child should be:",
        "Managed by provider with appropriate tools; irrigation or removal without training risks tympanic perforation",
        [
            "Removed with tweezers blindly by front desk",
            "Flushed with high-pressure syringe without visualization",
            "Ignored until adulthood",
        ],
        "Ear foreign bodies need skill to avoid canal injury.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-040
    fact(
        "skill-emergency-aid",
        "Mass casualty incident triage in clinic parking lot uses:",
        "Simple triage tags to prioritize immediate life threats",
        [
            "Treatiest patients first regardless of survival chance",
            "No communication with EMS",
            "Hiding patients from responders",
        ],
        "Triage maximizes lives saved when resources are limited.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-041
    fact(
        "skill-emergency-aid",
        "Infant CPR compression depth is approximately:",
        "One-third the anterior-posterior diameter of the chest per pediatric guidelines",
        [
            "Two inches in every newborn regardless of size",
            "Light pressure without effective chest compression",
            "Abdominal thrusts instead of compressions",
        ],
        "Pediatric depth is proportion-based. Abdominal thrusts are for choking, not pulseless arrest.",
        [S.AHA_ADULT_BLS, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-042
    fact(
        "skill-emergency-aid",
        "After stabilizing an emergency patient for EMS handoff, documentation should include:",
        "Interventions, times, vital signs, and medications given",
        [
            "Staff opinions about patient personality",
            "Unrelated billing codes without clinical summary",
            "Blank chart to let EMS write everything",
        ],
        "Continuity of care depends on accurate handoff records.",
        [S.NHA_CCMA, S.AHA_ADULT_BLS],
        "beginner",
    ),
]
