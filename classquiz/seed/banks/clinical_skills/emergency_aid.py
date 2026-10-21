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
            "Rush into a room with unknown hazards without reassessing vital signs afterward",
            "Begin hands-on care without gloves when blood is visible",
            "Leave the distressed patient unattended to find supplies",
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
            "Keep the patient seated upright with head forward without reassessing vital signs afterward",
            "Offer a large meal before assessing responsiveness",
            "Delay response until the end of the clinic session",
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
            "Into the gluteal muscle because it is largest",
            "Intravenously by the MA without a provider order",
            "Orally while waiting for EMS without reassessing vital signs afterward",
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
            "Raise systemic blood pressure with salt tablets",
            "Place a tourniquet for every minor cut without reassessing vital signs afterward",
            "Start oral antibiotics before applying pressure",
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
            "When the patient requests a refill one day early despite current facility protocol for the task",
            "When a routine vaccine causes brief sore arm before confirming allergy history in the chart",
            "When the printer jams during checkout without reassessing vital signs afterward even when the patient initially appears stable",
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
            "Scented lotion to mask skin redness before confirming allergy history in the chart",
            "Hot coffee to stimulate alertness without reassessing vital signs afterward",
            "A blanket without medication or monitoring equipment",
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
            "Send the patient to drive home alone immediately",
            "Apply a tight necklace to distract from itching",
            "Document hives without telling the provider without reassessing vital signs afterward",
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
            "Upper abdomen over the epigastrium without reassessing vital signs afterward",
            "Left lower rib cage tip without sternal contact",
            "Back of the neck while the patient stands",
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
            "Both pads stacked on the sternum crossing each other",
            "On wet skin while the patient stands in water without reassessing vital signs afterward",
            "Over medication patches without checking device instructions",
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
            "Back blows alone without alternating maneuvers when thrusts are indicated",
            "Finger sweeps blindly in the mouth of a conscious patient before confirming allergy history in the chart",
            "Wait several minutes before calling for help without reassessing vital signs afterward",
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
            "Personal opinions about patient behavior without reassessing vital signs afterward",
            "Unrelated billing codes without clinical summary",
            "Blank chart expecting EMS to enter all data",
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
            "Massage neck muscles vigorously and discharge home",
            "Place in a dark room without vital signs for days without reassessing vital signs afterward",
            "Provide acetaminophen and end the visit without escalation",
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
            "Tilt head far back to swallow blood without reassessing vital signs afterward",
            "Pack nostrils with unassessed objects from the desk despite current facility protocol for the task",
            "Dismiss anticoagulant medication history before confirming allergy history in the chart",
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
            "Using elevators during smoke conditions without reassessing vital signs afterward",
            "Leaving doors open to improve airflow through flames before confirming allergy history in the chart",
            "Securing paper charts in the burning room before exit",
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
            "Administer intramuscular glucagon before any glucose reading",
            "Offer a high-fat meal as the first intervention without reassessing vital signs afterward",
            "Withhold food despite confusion and diaphoresis",
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
            "30 compressions per minute with long pauses without reassessing vital signs afterward",
            "Compressions delivered over the upper abdomen",
            "Pausing five minutes between cycles to rest",
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
            "Oral antihistamine alone with immediate discharge without reassessing vital signs afterward",
            "Apply ice to the sting while the patient drives home",
            "Observe without airway assessment in the waiting room",
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
            "Abdominal thrusts identical to adult technique",
            "Blind finger sweeps in the mouth repeatedly without reassessing vital signs afterward",
            "Delay help activation while attempting home remedies",
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
            "Mild spotting with stable vital signs without reassessing vital signs afterward",
            "Improved energy despite large blood loss",
            "Isolated bradycardia with warm dry skin",
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
            "Delay reporting if the glove looked intact before confirming allergy history in the chart",
            "Squeeze wound and apply oral suction without reassessing vital signs afterward",
            "Wait one week before informing occupational health",
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
            "Stop all compressions for ten minutes while charging before confirming allergy history in the chart",
            "Remove AED pads after every shock permanently without reassessing vital signs afterward",
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
            "Abdominal bloating after meals without reassessing vital signs afterward",
            "Itchy eyes from seasonal allergies before confirming allergy history in the chart",
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
            "Discharge without reassessment of hemoglobin or blood pressure",
            "Tilt head back and send patient to strenuous exercise",
            "Apply ice to the forehead without nasal pressure without reassessing vital signs afterward",
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
            "Apply butter or prolonged direct ice to the skin",
            "Pop blisters immediately for drainage without reassessing vital signs afterward",
            "Dismiss cough or soot around the mouth after a fire",
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
            "Turn pump off without medical guidance and leave",
            "Encourage vigorous exercise to lower glucose without reassessing vital signs afterward",
            "Assume the pump corrects everything without assessment",
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
            "Cold air exposure as primary treatment without reassessing vital signs afterward",
            "Discharge without pulse oximetry or peak flow",
            "Label symptoms as panic without lung auscultation",
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
            "Force the limb straight without analgesia without reassessing vital signs afterward",
            "Apply heat packs and encourage immediate sports activity",
            "Wrap tightly with elastic bandage for weight bearing before confirming allergy history in the chart",
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
            "Scrub root with dry gauze to sterilize without reassessing vital signs afterward",
            "Store long term in plain tap water without guidance despite current facility protocol for the task",
            "Discard tooth and provide no counseling before confirming allergy history in the chart",
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
            "Simple anxiety without further assessment without reassessing vital signs afterward",
            "Exclusive reliance on finger pulse oximetry to rule out carboxyhemoglobin",
            "Return patient to the garage to finish chores",
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
            "One centimeter light pressure without sternal depression",
            "Half-inch depth to avoid rib injury at all costs without reassessing vital signs afterward",
            "Abdominal thrust rhythm instead of sternal compressions",
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
            "Insert tweezers deeply without visualization",
            "Flush with high-pressure syringe aimed blindly",
            "Plan removal at adulthood without symptoms without reassessing vital signs afterward",
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
            "Place tissue directly on dry ice touching skin despite current facility protocol for the task",
            "Soak in rubbing alcohol for hours without reassessing vital signs afterward even when the patient initially appears stable",
            "Discard tissue in sharps container before confirming allergy history in the chart",
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
            "Treat minor injuries first because they are calm",
            "Withhold communication from EMS without reassessing vital signs afterward",
            "Conceal patients from responding agencies",
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
            "Two inches in every newborn regardless of size without reassessing vital signs afterward",
            "Light skin pressure without compressing the chest",
            "Abdominal thrusts instead of chest compressions in pulseless arrest",
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
            "Assume death without assessment because lightning is fatal",
            "Give large oral fluids while unconscious without reassessing vital signs afterward",
            "Cluster many rescuers on wet ground during active lightning",
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
            "Staff opinions about patient personality",
            "Unrelated inventory counts without reassessing vital signs afterward",
            "Blank transfer because EMS will guess",
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
            "Remove dressings to air dry the limb without reassessing vital signs afterward",
            "Apply oral antibiotics before pressure",
            "Document bleeding without notifying the team",
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
            "Induce vomiting with finger stimulation before confirming allergy history in the chart",
            "Give milk to neutralize without poison center guidance",
            "Send patient home with mouthwash without reassessing vital signs afterward",
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
            "Discharge once hives fade without observing ten minutes",
            "Send patient to walk to the pharmacy alone without reassessing vital signs afterward",
            "Turn off oxygen if the patient feels anxious",
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
            "Discard gloves in personal bag without hand hygiene",
            "Refuse to document involvement in the event without reassessing vital signs afterward",
            "Decline emotional support resources offered by the clinic",
        ],
        "Incident reporting and hygiene protect staff wellbeing and quality improvement.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
]
