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
        "What is the first priority when any clinic emergency begins?",
        "Ensure scene safety and don appropriate PPE before patient contact",
        [
            "Rush into a room with unknown hazards before assessing scene safety",
            "Begin hands-on care without gloves when blood or body fluids are visible",
            "Leave the distressed patient unattended while searching the clinic for supplies",
        ],
        "Provider safety preserves the ability to help others. Blood exposure requires barrier protection under Standard Precautions.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-emergency-aid-002
    fact(
        "skill-emergency-aid",
        "When an ambulatory patient faints in the hallway, what initial positioning is appropriate if no trauma is suspected?",
        "Lower the patient to the floor and elevate legs while monitoring airway",
        [
            "Keep the patient seated upright with head forward instead of lying supine",
            "Offer a large meal before checking responsiveness, pulse, and airway patency",
            "Delay any response until the end of the clinic session when the schedule clears",
        ],
        "Supine positioning with leg elevation improves cerebral perfusion. Food before assessment risks aspiration if consciousness is altered.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-003
    fact(
        "skill-emergency-aid",
        "Where should an epinephrine auto-injector be administered for suspected anaphylaxis per device instructions?",
        "Into the anterolateral thigh, through clothing if needed",
        [
            "Into the gluteal muscle because it is the largest muscle mass",
            "Intravenously by the MA without a provider order or pharmacy label",
            "Orally by mouth while waiting for EMS to arrive at the clinic",
        ],
        "Intramuscular thigh delivery is standard for auto-injectors. IV epinephrine is not an MA task.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-emergency-aid-004
    fact(
        "skill-emergency-aid",
        "After syncope with a witnessed fall, what injury concern should be assessed first?",
        "Head and cervical spine trauma when mechanism suggests impact",
        [
            "Blood glucose level as the sole focus without neurologic check",
            "Immediate discharge without documentation",
            "Charting completed before any vital signs",
        ],
        "Falls can cause intracranial injury or spine fracture. Glucose may be relevant but does not replace trauma assessment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-005
    fact(
        "skill-emergency-aid",
        "How should active bleeding from a superficial laceration be managed initially?",
        "Apply direct pressure with clean gauze and elevate the limb when practical",
        [
            "Raise systemic blood pressure with salt tablets before any local pressure",
            "Place a tourniquet proximally for every minor cut regardless of bleeding severity",
            "Start broad oral antibiotics before applying direct pressure to the wound",
        ],
        "Direct pressure promotes hemostasis while definitive care is arranged. Tourniquets are for severe extremity bleeding per protocol.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-006
    fact(
        "skill-emergency-aid",
        "When should the MA activate the clinic emergency response or call EMS?",
        "When the patient has altered mental status, trouble breathing, chest pain, or uncontrolled bleeding",
        [
            "When the patient requests an early medication refill but remains alert with stable vitals and no distress",
            "When a routine vaccine causes brief arm soreness without hives, wheeze, or systemic symptoms",
            "When the printer jams during checkout while the patient remains stable and asymptomatic",
        ],
        "Life-threatening signs require rapid escalation. Administrative inconveniences are not emergencies.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-007
    fact(
        "skill-emergency-aid",
        "A patient develops hives and wheezing minutes after a vaccine. What supplies should be gathered first while help is called?",
        "Epinephrine auto-injector, airway equipment per protocol, and oxygen if available",
        [
            "Scented lotion to mask skin redness without epinephrine or airway supplies",
            "Hot coffee to stimulate alertness instead of monitoring breathing and blood pressure",
            "A warm blanket without epinephrine, oxygen, or other resuscitation equipment",
        ],
        "Anaphylaxis treatment centers on epinephrine and airway support. Comfort items do not reverse bronchospasm or shock.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-008
    fact(
        "skill-emergency-aid",
        "How should a patient with hives but stable breathing be managed pending provider evaluation?",
        "Monitor airway and vitals while notifying the clinician per protocol",
        [
            "Send the patient to drive home alone immediately without provider evaluation",
            "Apply a tight necklace or scarf around the neck to distract from itching",
            "Document hives in the chart without notifying the provider or monitoring vitals",
        ],
        "Even stable hives can progress to airway compromise. Monitoring and communication are essential.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-009
    fact(
        "skill-emergency-aid",
        "What is the correct hand placement for adult chest compressions during CPR?",
        "Lower half of the sternum with heel of one hand overlapped by the other",
        [
            "Upper abdomen over the epigastrium instead of the lower half of the sternum",
            "Left lower rib cage tip without sternal contact during chest compressions",
            "Back of the neck while the patient stands upright without any torso support",
        ],
        "Compressions must depress the sternum to pump blood. Abdominal and neck pressure do not provide effective circulation.",
        [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
        "beginner",
    ),
    # skill-emergency-aid-010
    fact(
        "skill-emergency-aid",
        "When using an AED on an adult, where should pads be placed?",
        "Upper right chest and lower left side below the armpit per diagram",
        [
            "Both pads stacked on the sternum crossing each other against device labeling",
            "On wet skin while the patient stands in water without drying the chest",
            "Over medication patches without removing them or checking device instructions",
        ],
        "Correct pad placement and dry skin improve shock success. Wet environments require moving the patient to safety first.",
        [S.AHA_ADULT_BLS, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-011
    fact(
        "skill-emergency-aid",
        "How should a choking adult with ineffective cough and severe airway obstruction be treated?",
        "Abdominal thrusts per current BLS guidelines until obstruction clears or patient becomes unresponsive",
        [
            "Back blows alone without alternating abdominal thrusts when severe obstruction is present",
            "Finger sweeps blindly in the mouth of a conscious patient with a partial airway obstruction",
            "Wait several minutes before activating the emergency response team or calling for any additional help",
        ],
        "Severe obstruction needs immediate thrusts and EMS activation. Blind finger sweeps can push objects deeper.",
        [S.AHA_ADULT_BLS, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-012
    fact(
        "skill-emergency-aid",
        "What documentation is required after assisting with an in-clinic emergency?",
        "Objective findings, interventions, times, and medications given",
        [
            "Personal opinions about patient behavior without objective clinical findings",
            "Unrelated billing codes without any summary of interventions or vital signs",
            "Blank chart expecting EMS to enter all data without a structured handoff",
        ],
        "Accurate records support continuity when care transfers to EMS or the hospital.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-013
    fact(
        "skill-emergency-aid",
        "How should a patient with sudden severe headache and neck stiffness be managed before transfer?",
        "Notify the provider immediately and prepare for urgent evaluation",
        [
            "Massage neck muscles vigorously and discharge home without vital signs",
            "Place in a dark room without vital signs or neurologic checks for days",
            "Provide acetaminophen alone and end the visit without notifying the provider",
        ],
        "Thunderclap headache with meningismus may indicate meningitis or subarachnoid hemorrhage.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-014
    fact(
        "skill-emergency-aid",
        "What first aid is appropriate for a nosebleed that is not from major trauma?",
        "Sit upright, lean slightly forward, and pinch soft part of nose for ten to fifteen minutes",
        [
            "Tilt head far back to swallow blood instead of leaning forward with sustained pinching",
            "Pack nostrils with unsterile objects from the desk without continuous pressure monitoring",
            "Dismiss anticoagulant medication history and send the patient home without a pressure hold",
        ],
        "Forward lean prevents blood swallowing and aspiration. Anticoagulants prolong bleeding and need clinician awareness.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-015
    fact(
        "skill-emergency-aid",
        "Which steps belong in the clinic fire emergency plan the MA should know?",
        "Alarm activation, evacuation routes, patient assistance, and assembly point roll call",
        [
            "Using elevators during smoke conditions instead of posted stairwell evacuation routes",
            "Leaving doors open to improve airflow through active flames during evacuation",
            "Securing paper charts in the burning room before exit instead of assisting patients out",
        ],
        "Evacuation routes and accountability protect patients and staff. Elevators and reentry into fire areas are unsafe.",
        [S.NHA_CCMA, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-emergency-aid-016
    fact(
        "skill-emergency-aid",
        "How should a conscious adult with suspected hypoglycemia be treated when they can swallow safely?",
        "Give fifteen grams fast-acting carbohydrate and recheck glucose per protocol",
        [
            "Administer intramuscular glucagon before any glucose reading when swallowing is intact",
            "Offer a high-fat meal as the first intervention before checking blood glucose",
            "Withhold all food and drink despite confusion, diaphoresis, and suspected hypoglycemia",
        ],
        "Rapid sugar raises glucose when swallowing is intact. Glucagon is for unable-to-swallow scenarios per orders.",
        [S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-017
    fact(
        "skill-emergency-aid",
        "During high-quality CPR on an adult, what compression rate is recommended?",
        "100 to 120 compressions per minute with full chest recoil",
        [
            "30 compressions per minute with long pauses between each compression cycle",
            "Compressions delivered over the upper abdomen instead of the lower sternum",
            "Pausing five full minutes between compression cycles to let rescuers rest",
        ],
        "Adequate rate and recoil maintain coronary perfusion. Abdominal compressions are not standard BLS.",
        [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
        "intermediate",
    ),
    # skill-emergency-aid-018
    fact(
        "skill-emergency-aid",
        "A patient with tongue swelling after a bee sting becomes hoarse. What is the priority response?",
        "Activate emergency response and administer epinephrine per anaphylaxis protocol",
        [
            "Oral antihistamine alone with immediate discharge before reassessing the airway",
            "Apply ice only to the sting while the patient drives home without monitoring",
            "Observe in the waiting room without pulse oximetry or repeated airway assessment",
        ],
        "Airway angioedema can progress to obstruction rapidly. Epinephrine is first-line for anaphylaxis.",
        [S.RED_CROSS_FIRST_AID, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-emergency-aid-019
    fact(
        "skill-emergency-aid",
        "An infant is choking with weak ineffective cough and cyanosis. What maneuver sequence applies?",
        "Back blows and chest thrusts per pediatric BLS guidelines",
        [
            "Abdominal thrusts using identical adult technique on the infant abdomen",
            "Blind finger sweeps in the mouth repeatedly before back blows or chest thrusts",
            "Delay emergency activation while attempting unproven home remedy techniques",
        ],
        "Infants need age-specific airway maneuvers. Abdominal thrusts are not used in young infants.",
        [S.AHA_ADULT_BLS, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-020
    fact(
        "skill-emergency-aid",
        "A postpartum patient in clinic suddenly soaks through pads with blood and feels dizzy. What findings cluster with hemorrhagic shock?",
        "Heavy bleeding, tachycardia, hypotension, and altered mental status",
        [
            "Mild spotting with stable vital signs, normal heart rate, and clear orientation",
            "Improved energy and alertness despite heavy ongoing vaginal bleeding",
            "Isolated bradycardia with warm dry skin despite profuse uterine hemorrhage",
        ],
        "Obstetric hemorrhage is an emergency requiring rapid team response and fluids per protocol.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-021
    fact(
        "skill-emergency-aid",
        "What immediate steps follow a needlestick injury during an emergency procedure?",
        "Wash the area, report promptly, and begin post-exposure evaluation per protocol",
        [
            "Delay reporting to occupational health if the glove looked intact despite a puncture",
            "Squeeze the wound vigorously and apply oral suction to the puncture site",
            "Wait one week before informing occupational health or employee health services",
        ],
        "Early evaluation enables prophylaxis when indicated. Oral suction is not recommended.",
        [S.OSHA_NEEDLESTICK, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-emergency-aid-022
    fact(
        "skill-emergency-aid",
        "How should chest compressions and AED use be coordinated during a cardiac arrest?",
        "Minimize pauses by continuing compressions around pad placement and shock delivery per training",
        [
            "Stop all chest compressions for ten full minutes while the AED charges between every shock cycle",
            "Remove AED pads after every shock permanently",
            "Assign one rescuer to leave the building without calling EMS",
        ],
        "Short interruptions preserve perfusion. AEDs prompt rhythm analysis between cycles.",
        [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
        "intermediate",
    ),
    # skill-emergency-aid-023
    fact(
        "skill-emergency-aid",
        "What does the FAST mnemonic help staff recognize for stroke?",
        "Face droop, arm weakness, speech difficulty, and time to call emergency services",
        [
            "Foot pain as the primary stroke symptom",
            "Abdominal bloating after meals",
            "Itchy eyes from seasonal allergies as the only explanation without neurologic screening",
        ],
        "Stroke therapies are time sensitive; early EMS activation improves outcomes.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-024
    fact(
        "skill-emergency-aid",
        "For a nosebleed on warfarin with ongoing oozing after first aid, what is appropriate?",
        "Continue pressure, notify provider, and prepare for escalation per protocol",
        [
            "Discharge without reassessing blood pressure, pulse, or hemoglobin after prolonged oozing",
            "Tilt the head fully back and send the patient to strenuous exercise immediately",
            "Apply ice only to the forehead while omitting continuous direct nasal pinching",
        ],
        "Anticoagulation prolongs bleeding and may need reversal or packing in clinic or ED.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-025
    fact(
        "skill-emergency-aid",
        "What first aid is appropriate for a small thermal burn on the forearm?",
        "Cool running water and removal of constricting jewelry near the burn",
        [
            "Apply butter or prolonged direct ice directly on blistered skin over the burn",
            "Pop any blisters immediately for drainage before cooling under running water",
            "Ignore cough, singed nasal hairs, or soot around the mouth after a confined fire",
        ],
        "Cooling limits depth; jewelry can strangulate swollen tissue. Inhalation injury signs need escalation.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-026
    fact(
        "skill-emergency-aid",
        "How should a diabetic patient with insulin pump alarm, vomiting, and ketones on dipstick be managed?",
        "Notify provider, assess glucose and ketones per protocol, and monitor for dehydration",
        [
            "Turn the insulin pump off without medical guidance and send the patient home",
            "Encourage vigorous exercise to lower glucose despite vomiting and positive ketones",
            "Assume the insulin pump alone corrects glucose and ketones without any further assessment",
        ],
        "Illness increases diabetic ketoacidosis risk even with pump therapy.",
        [S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-027
    fact(
        "skill-emergency-aid",
        "When a patient has audible wheezing and retractions after allergen exposure, what is the clinic priority?",
        "Provider evaluation with bronchodilator therapy and oxygen monitoring per orders",
        [
            "Cold outdoor air exposure alone as the primary bronchodilator treatment strategy",
            "Discharge without pulse oximetry, peak flow, or provider auscultation of the lungs",
            "Label symptoms as panic disorder without lung exam, oxygen check, or peak flow",
        ],
        "Respiratory distress can progress to failure; objective assessment guides therapy.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-028
    fact(
        "skill-emergency-aid",
        "A child falls and the forearm appears angulated with severe pain. What management is appropriate within first aid scope?",
        "Immobilize in position found, apply splint support, and arrange urgent imaging per protocol",
        [
            "Force the angulated limb straight without analgesia or splinting before transport",
            "Apply heat packs and encourage immediate sports activity on the injured forearm",
            "Wrap tightly with elastic bandage for immediate full weight bearing on the angulated forearm",
        ],
        "Suspected fracture needs immobilization and imaging. Forcing alignment can damage nerves and vessels.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-029
    fact(
        "skill-emergency-aid",
        "A knocked-out permanent tooth is recovered within thirty minutes. How should it be handled before dental referral?",
        "Rinse gently, store in appropriate solution or saline per protocol, and seek urgent dental care",
        [
            "Scrub the tooth root aggressively with dry gauze to sterilize it before placing any transport solution",
            "Store long term in plain tap water without dental or poison center guidance on transport",
            "Discard the tooth and provide no counseling about urgent dental reimplantation options",
        ],
        "Timely reimplantation may save the tooth when handled correctly.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-030
    fact(
        "skill-emergency-aid",
        "Several staff report headache and nausea after a patient arrives from a house with a faulty furnace. What exposure is suspected?",
        "Carbon monoxide toxicity requiring removal from source and emergency evaluation",
        [
            "Simple situational anxiety without environmental assessment or pulse oximetry",
            "Exclusive reliance on finger pulse oximetry alone to rule out carboxyhemoglobin poisoning",
            "Send the patient back to the garage to finish chores while symptoms are worsening",
        ],
        "Pulse oximetry may read falsely normal; co-oximetry in hospital confirms diagnosis.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-031
    fact(
        "skill-emergency-aid",
        "What is the recommended compression depth for adult CPR?",
        "At least two inches with full recoil between compressions",
        [
            "One centimeter light pressure without sternal depression during compressions",
            "Half-inch depth to avoid rib injury at all costs during adult cardiac arrest",
            "Abdominal thrust rhythm instead of sternal compressions during pulseless arrest",
        ],
        "Adequate depth generates blood flow. Shallow compressions are ineffective.",
        [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
        "beginner",
    ),
    # skill-emergency-aid-032
    fact(
        "skill-emergency-aid",
        "A toddler pulls a bead into the ear canal in the waiting room. What should the MA do?",
        "Notify provider for removal with proper tools; untrained probing risks perforation",
        [
            "Insert tweezers deeply into the canal without visualization or provider supervision",
            "Flush with a high-pressure syringe aimed blindly into the ear canal opening",
            "Defer all removal attempts until adulthood even when pain and blockage are present",
        ],
        "Ear foreign bodies need skill to avoid canal or tympanic injury.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-033
    fact(
        "skill-emergency-aid",
        "How should an amputated fingertip with clean edges be transported with the patient?",
        "Wrap in saline-moistened gauze, place in a waterproof bag, and cool on ice without direct ice contact",
        [
            "Place amputated tissue directly on dry ice where it touches skin continuously during ambulance transport",
            "Soak the fingertip in rubbing alcohol for several hours while awaiting specialty referral",
            "Discard the tissue in a sharps container instead of sending it with the patient to the ED",
        ],
        "Proper cooling preserves tissue for possible reattachment.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-034
    fact(
        "skill-emergency-aid",
        "During a mass casualty incident near the clinic entrance, what triage principle applies?",
        "Prioritize patients with immediate life threats using simple triage tags",
        [
            "Treat calm patients with minor abrasions first because they are easier to reassure",
            "Withhold all communication from EMS about patient locations and triage categories",
            "Conceal injured patients from responding agencies to reduce clinic liability concerns",
        ],
        "Triage maximizes survival when resources are limited.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-035
    fact(
        "skill-emergency-aid",
        "What compression depth target applies to infant CPR?",
        "About one-third the anterior-posterior chest diameter per pediatric guidelines",
        [
            "Two inches sternal depth in every newborn regardless of chest size or gestational age",
            "Light skin-level pressure without compressing the anterior-posterior chest diameter",
            "Abdominal thrusts substituted for chest compressions during infant pulseless arrest",
        ],
        "Pediatric depth is proportion based. Compressions, not thrusts, treat cardiac arrest.",
        [S.AHA_ADULT_BLS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-036
    fact(
        "skill-emergency-aid",
        "A lightning strike victim is found pulseless in the lot after the storm passes. What sequence is appropriate?",
        "Ensure scene safety, then begin CPR and use AED if available while activating EMS",
        [
            "Assume death without any assessment because lightning strikes are always immediately fatal",
            "Give large oral fluid boluses while the patient remains unconscious, pulseless, and unmonitored",
            "Cluster many rescuers together on wet ground while lightning may still be active nearby",
        ],
        "Lightning victims may have recoverable rhythms; CPR and AED follow scene safety.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-037
    fact(
        "skill-emergency-aid",
        "When handing a stabilized emergency patient to EMS, what information should be communicated?",
        "Events, interventions, times, allergies, and last vital signs",
        [
            "Staff opinions about patient personality traits without any clinical event chronology or times",
            "Unrelated clinic supply inventory counts instead of allergies, medications, and last vital signs",
            "Provide no handoff information because EMS will guess the entire clinical course without data",
        ],
        "Structured handoff reduces errors during transport.",
        [S.NHA_CCMA, S.AHA_ADULT_BLS],
        "beginner",
    ),
    # skill-emergency-aid-038
    fact(
        "skill-emergency-aid",
        "How should severe external bleeding from a limb be managed when direct pressure fails and life is threatened?",
        "Apply tourniquet proximal to wound per training and activate EMS immediately",
        [
            "Remove all dressings to air-dry the limb while severe bleeding continues briskly unchecked",
            "Start oral antibiotics before applying direct pressure, elevation, or any hemostatic dressing",
            "Document ongoing hemorrhage in the chart without notifying the provider, team, or activating EMS",
        ],
        "Tourniquets are a last resort for extremity hemorrhage when pressure is insufficient.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-039
    fact(
        "skill-emergency-aid",
        "A patient in pulseless arrest receives CPR from trained staff. What ventilation-to-compression ratio applies for adult BLS with breaths?",
        "30 compressions to 2 breaths per current guidance",
        [
            "15 compressions to 2 breaths for all adults in every setting",
            "5 compressions to 1 breath continuously",
            "Compressions without any pauses for breaths",
        ],
        "Standard ratios balance perfusion and oxygenation during trained single-rescuer or two-rescuer CPR.",
        [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
        "intermediate",
    ),
    # skill-emergency-aid-040
    fact(
        "skill-emergency-aid",
        "A patient ingests a caustic household cleaner and drools with mouth pain. What is appropriate pending EMS?",
        "Keep NPO, monitor airway, and bring container information for poison control",
        [
            "Induce vomiting with finger stimulation before poison control or EMS is contacted",
            "Give milk to neutralize without poison center guidance",
            "Send patient home with mouthwash",
        ],
        "Caustic ingestions risk airway edema and perforation; vomiting can worsen injury.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-041
    fact(
        "skill-emergency-aid",
        "During anaphylaxis after epinephrine, what monitoring is needed while awaiting EMS?",
        "Repeat vitals, watch airway and breathing, and prepare second dose per protocol",
        [
            "Discharge once hives fade without the minimum post-epinephrine observation period required",
            "Send the patient to walk alone to the pharmacy for refills during the EMS observation window",
            "Turn off supplemental oxygen whenever the patient reports anxiety, mild tachycardia, or wheeze",
        ],
        "Biphasic reactions can occur; observation and readiness for repeat epinephrine are standard.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-042
    fact(
        "skill-emergency-aid",
        "After assisting with CPR until EMS arrives, what should the MA do for occupational health?",
        "Debrief per facility policy and complete any required incident reporting",
        [
            "Discard used gloves in a personal bag without performing hand hygiene afterward in the clinic",
            "Refuse to document your involvement in the resuscitation when incident review or OSHA follow-up occurs",
            "Decline any debriefing, counseling, or emotional support resources offered after the code event",
        ],
        "Incident reporting and hygiene protect staff wellbeing and quality improvement.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
]
