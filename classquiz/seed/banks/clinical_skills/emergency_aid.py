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
        "What is the first priority when a clinic emergency begins?",
        "Confirm the scene is safe and use barrier protection before contact",
        [
            "Begin hands-on care and add gloves once blood or fluid is seen",
            "Open the emergency cart and check the AED before approaching the patient",
            "Take the history and vital signs before checking the surroundings",
        ],
        "A responder who is injured or exposed cannot continue the response, so scene safety and barrier protection come before touching the patient. Starting hands-on care before gloving, opening the cart first, and taking a history first all risk the staff member and delay the response.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-emergency-aid-002
    fact(
        "skill-emergency-aid",
        "An ambulatory patient faints in the clinic hallway. What position should the medical assistant use if no injury is suspected?",
        "Lay the patient supine and elevate the legs while checking the airway",
        [
            "Seat the patient upright with the head tilted down toward the knees",
            "Place the patient in a chair with the legs propped up above the heart",
            "Keep the patient seated in a wheelchair with the feet on a stool",
        ],
        "A patient who faints without injury is placed supine with the legs raised, which returns blood toward the brain and keeps the airway visible for monitoring. Sitting the patient forward or in a chair, and propping the feet up from a seated position, do not restore cerebral perfusion the same way.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-003
    fact(
        "skill-emergency-aid",
        "Where should an epinephrine auto-injector be given for suspected anaphylaxis?",
        "Into the middle third of the anterolateral thigh",
        [
            "Into the outer upper arm, positioned well above the elbow",
            "Into the fleshy center of the abdomen, just above the navel",
            "Into the front of the thigh, positioned close to the knee",
        ],
        "The anterolateral thigh provides a large muscle mass with fast absorption, and an auto-injector can be used through clothing when a line of clothing is in the way. The outer arm, the abdomen, and the area near the knee are not recommended sites for an epinephrine auto-injector.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-emergency-aid-004
    fact(
        "skill-emergency-aid",
        "After a syncopal event with a witnessed fall, which injury concern should be assessed first?",
        "Head and cervical spine injury from the fall",
        [
            "Hip fracture from landing on the outstretched hand",
            "Wrist deformity from bracing the hand against the floor",
            "Knee contusion from landing on both knees during the fall",
        ],
        "After a witnessed fall with syncope, head and cervical spine injury takes priority because the patient may have struck the head or the neck. Hip fracture, wrist deformity, and knee contusion are also possible fall injuries, but each one is assessed after the head, neck, and airway have been checked.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-005
    fact(
        "skill-emergency-aid",
        "How should active bleeding from a small laceration be managed first in clinic?",
        "Apply firm direct pressure with clean gauze until the bleeding slows",
        [
            "Rinse the wound with antiseptic, then cover it with a dry dressing",
            "Wrap the limb in a tight elastic bandage to compress the wound edges",
            "Apply antibiotic ointment over the wound and bandage it in place",
        ],
        "Direct pressure with clean gauze is the first step for bleeding because it compresses the vessel while the wound is examined. Antiseptic rinsing and ointment belong to wound cleaning rather than bleeding control, and an elastic wrap applied without direct pressure does not control superficial bleeding.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-006
    fact(
        "skill-emergency-aid",
        "Which finding should prompt the medical assistant to activate the clinic emergency response and call EMS?",
        "Sudden chest pressure with shortness of breath and diaphoresis",
        [
            "Mild sore throat and hoarseness that improved before the visit",
            "Stable blood pressure with mild seasonal allergy symptoms",
            "Localized ankle pain after a small stumble on the clinic steps",
        ],
        "Sudden chest pressure with breathlessness and sweating suggests a cardiac emergency, so the clinic emergency response and EMS activation begin at once. Mild sore throat, seasonal allergy symptoms, and a minor ankle injury after a stumble are handled through normal clinic workflow and do not meet activation criteria.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-007
    fact(
        "skill-emergency-aid",
        "A patient develops hives and wheezing minutes after a vaccine. Which emergency supply set should the medical assistant bring to the room?",
        "Epinephrine auto-injector, airway supplies, and an oxygen source",
        [
            "Antihistamine tablets, a decongestant spray, and a nasal cannula",
            "A nebulizer and inhaler, an oral steroid, and a humidified mask",
            "A blood pressure cuff, a pulse oximeter, and a cardiac monitor",
        ],
        "Suspected anaphylaxis is treated with intramuscular epinephrine plus airway support and oxygen, so those supplies go to the room immediately. Antihistamines, inhaled bronchodilators, and oral steroids act more slowly, and monitoring equipment by itself does not reverse bronchospasm or shock.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-008
    fact(
        "skill-emergency-aid",
        "A patient with hives and stable breathing is waiting for provider evaluation. What should the medical assistant do?",
        "Monitor airway and vital signs and notify the clinician",
        [
            "Have the patient wait in the lobby while the schedule catches up",
            "Recheck the skin every fifteen minutes and record the findings",
            "Give an oral antihistamine and send the patient home to rest",
        ],
        "Hives with stable breathing can still progress to airway swelling, so the airway and vital signs are monitored and the clinician is notified right away. Waiting in the lobby, rechecking the skin without notifying anyone, and sending the patient home on an oral antihistamine all leave that progression unwatched.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-009
    fact(
        "skill-emergency-aid",
        "A patient collapses in the clinic and is unresponsive with no normal breathing. Which statement describes the compressions trained staff should perform?",
        "Press on the lower half of the sternum with one hand over the other",
        [
            "Press on the upper chest below the collarbones with both hands overlapping",
            "Press over the upper abdomen with both hands stacked side by side",
            "Press on the left side of the chest with the fingers spread apart",
        ],
        "Adult compressions are delivered on the lower half of the sternum with one heel of the hand over the other, which drives blood through the heart. Upper sternal, abdominal, and lateral chest placements do not generate the blood flow that CPR depends on.",
        [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
        "beginner",
    ),
    # skill-emergency-aid-010
    fact(
        "skill-emergency-aid",
        "A patient begins a seizure in the clinic. What should the medical assistant do while the seizure continues?",
        "Clear hazards and time the seizure without restraining the patient",
        [
            "Hold the patient's arms and legs firmly to stop the muscle movements",
            "Place a padded object between the teeth to protect the tongue",
            "Lift the patient's head and shoulders to keep the airway open",
        ],
        "Most seizures stop on their own, so the priorities are protecting the patient from injury and timing the event. Restraining the limbs, placing objects in the mouth, and lifting the head during movements can injure the patient or the person providing care.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-011
    fact(
        "skill-emergency-aid",
        "A conscious adult in the clinic cannot speak and coughs silently. What sequence should the medical assistant follow?",
        "Deliver five back blows, then five abdominal thrusts, and repeat",
        [
            "Encourage forceful coughing and sips of water to clear the object",
            "Wait for EMS to arrive before attempting airway clearance maneuvers",
            "Sweep the mouth with a finger to remove the object that is stuck",
        ],
        "A conscious adult with severe airway obstruction needs five back blows followed by five abdominal thrusts, repeated until the object clears or the patient becomes unresponsive. Encouraging cough and water applies to mild obstruction, waiting for EMS delays care, and blind finger sweeps can push the object deeper.",
        [S.AHA_ADULT_BLS, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-012
    fact(
        "skill-emergency-aid",
        "What belongs in the medical assistant's note after assisting with an in-clinic emergency?",
        "Objective findings, times, interventions, and medications given",
        [
            "A summary of how the patient usually behaves and their long history",
            "The clinic supply inventory and the staff schedule for that day",
            "The billing code used and the date of the next appointment",
        ],
        "An emergency note records what was observed, when it happened, what was done, and what was given, so the next caregiver can follow the sequence. Background habits, supply inventories, and billing details do not tell the receiving team what happened to the patient.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-013
    fact(
        "skill-emergency-aid",
        "A patient reports a sudden severe headache with neck stiffness and fever. What is the appropriate clinic response?",
        "Notify the provider immediately and prepare for urgent evaluation",
        [
            "Give an over-the-counter analgesic and schedule a follow-up in two weeks",
            "Ask the patient to lie flat with the head elevated and recheck in an hour",
            "Massage the neck muscles and continue with the scheduled appointments",
        ],
        "A sudden severe headache with neck stiffness and fever suggests meningitis or subarachnoid hemorrhage, so the provider is notified at once for urgent evaluation. Pain medication with a delayed follow-up, watching the patient without notifying anyone, and neck massage all delay care for a time-critical condition.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-014
    fact(
        "skill-emergency-aid",
        "What first aid is appropriate for a nosebleed in a patient without significant facial trauma?",
        "Sit the patient up, lean forward, and pinch the nose for ten to fifteen minutes",
        [
            "Sit the patient up, lean forward, and pinch the soft nose for one to two minutes",
            "Lie the patient flat, tilt the head back, and pinch the soft nose",
            "Seat the patient up, lean forward, and place a cold compress on the nose bridge",
        ],
        "Sitting up and leaning forward with steady pressure on the soft part of the nose for ten to fifteen minutes controls most nosebleeds and keeps blood out of the stomach. A one to two minute hold is too short, tilting the head back sends blood down the throat, and a cold compress alone does not press on the bleeding site.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-015
    fact(
        "skill-emergency-aid",
        "The fire alarm sounds in the clinic. What should the medical assistant do first?",
        "Check rooms for patients who need help and move them to posted exits",
        [
            "Call each scheduled patient by phone to confirm they heard the alarm",
            "Collect the medication charts for the patients who are being evacuated",
            "Record the alarm code and the time of the alarm in the daily clinic log",
        ],
        "People come first when the alarm sounds: find anyone who needs assistance and move them to a posted exit route. Calling patients who are not in the building, gathering paperwork, and writing in the log can happen after everyone is out of the building.",
        [S.NHA_CCMA, S.OSHA_BBP],
        "intermediate",
    ),
    # skill-emergency-aid-016
    fact(
        "skill-emergency-aid",
        "A conscious adult in the clinic has signs of hypoglycemia and can swallow safely. What treatment is appropriate?",
        "Give fifteen grams of fast-acting carbohydrate and recheck in fifteen minutes",
        [
            "Give fifteen grams of fast-acting carbohydrate and recheck in an hour",
            "Give a high-fat meal and then recheck the blood glucose in fifteen minutes",
            "Give glucagon and recheck the blood glucose in fifteen minutes after giving it",
        ],
        "Fifteen grams of fast-acting carbohydrate raises the blood sugar fastest when the patient is awake and swallowing safely, and the glucose is rechecked in fifteen minutes to confirm the response. A high-fat meal slows absorption, glucagon is for patients who cannot swallow safely, and waiting an hour leaves the patient hypoglycemic.",
        [S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-017
    fact(
        "skill-emergency-aid",
        "During a clinic code, which observation tells the medical assistant that compressions are not high quality?",
        "The chest does not fully recoil between compressions",
        [
            "The compression rate stays between 100 and 120 per minute",
            "The compressing rescuer switches roles every two minutes",
            "The AED analyzes the rhythm and advises a shock",
        ],
        "Full recoil lets the heart refill between compressions, so a chest that stays compressed points to a quality problem that needs coaching. A rate of 100 to 120, switching compressors about every two minutes, and an AED shock prompt all describe recommended actions rather than deficits.",
        [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
        "intermediate",
    ),
    # skill-emergency-aid-018
    fact(
        "skill-emergency-aid",
        "A patient develops tongue swelling and hoarseness within minutes of a bee sting. What is the priority response?",
        "Give epinephrine and activate emergency medical services",
        [
            "Give an oral antihistamine and recheck the patient in twenty minutes",
            "Apply a cold pack to the sting site and watch for spreading hives",
            "Give an oral corticosteroid and recheck the patient in twenty minutes",
        ],
        "Tongue swelling and hoarseness signal airway angioedema, and epinephrine with EMS activation comes first because the airway can close quickly. Antihistamines, cold packs, and oral steroids work too slowly to protect the airway from swelling.",
        [S.RED_CROSS_FIRST_AID, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-emergency-aid-019
    fact(
        "skill-emergency-aid",
        "A runner is brought into the clinic with a high temperature, confusion, and vomiting. What is the priority response?",
        "Begin rapid cooling with cold water or ice packs and activate EMS",
        [
            "Give oral sports drinks and have the patient rest in the waiting area",
            "Apply warm blankets and recheck the temperature after twenty minutes",
            "Give an oral antihistamine and monitor the temperature every fifteen minutes",
        ],
        "Confusion with a high temperature and vomiting points to heat stroke, which needs immediate cooling and EMS transport. Sports drinks do not lower core temperature, warm blankets trap heat inside the body, and antihistamines do not treat heat illness.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-020
    fact(
        "skill-emergency-aid",
        "A postpartum patient suddenly soaks through pads with blood and feels dizzy. Which findings cluster with hemorrhagic shock?",
        "Heavy bleeding, tachycardia, hypotension, and altered mental status",
        [
            "Light spotting with stable vital signs, normal pulse, and clear thinking",
            "Improved energy and alertness despite heavy ongoing vaginal bleeding",
            "Isolated bradycardia with warm dry skin despite heavy uterine bleeding",
        ],
        "Obstetric hemorrhage with a fast pulse, low blood pressure, and confusion indicates hemorrhagic shock and calls for immediate team response and fluids. Light spotting with stable vitals, alertness despite heavy bleeding, and bradycardia with warm dry skin do not match the shock pattern.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-021
    fact(
        "skill-emergency-aid",
        "During a clinic emergency, a needlestick occurs while the medical assistant is assisting with care. What should happen next?",
        "Wash the area, report it promptly, and begin post-exposure evaluation",
        [
            "Wash the area, finish the task, and report the stick before the shift ends",
            "Squeeze the wound hard and apply antiseptic at the end of the clinic day",
            "Record the injury in the chart and wait for a provider to ask about it",
        ],
        "Washing the site and reporting the exposure right away starts the post-exposure evaluation timeline, which is what opens the prophylaxis window. Reporting at the end of the shift, delaying the wash, and charting the injury without reporting it each lose that time.",
        [S.OSHA_NEEDLESTICK, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-emergency-aid-022
    fact(
        "skill-emergency-aid",
        "During a clinic cardiac arrest, how should chest compressions and the AED be coordinated?",
        "Pause for pad placement and rhythm analysis, then resume compressions",
        [
            "Pause compressions for a full minute while the AED analyzes the rhythm",
            "Continue compressions through every rhythm analysis and shock delivery",
            "Remove the AED pads after each shock and reapply them later",
        ],
        "Compressions continue except for brief pauses to attach the pads and for rhythm analysis, while trained staff cycle 30 compressions to 2 breaths between analyses. Pausing for a full minute, compressing through the analysis and shock, and removing the pads after each shock all delay defibrillation.",
        [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
        "intermediate",
    ),
    # skill-emergency-aid-023
    fact(
        "skill-emergency-aid",
        "A patient shows new facial droop and slurred speech during a clinic visit. What is the appropriate response?",
        "Note the last known well time and activate EMS for immediate transport",
        [
            "Give the patient aspirin and let them rest before arranging transport",
            "Schedule a follow-up visit to recheck the symptoms in one week",
            "Recheck the symptoms in thirty minutes and decide whether to call for help",
        ],
        "New facial droop and slurred speech suggest stroke, so the last known well time is documented and EMS is activated for immediate transport because treatment is time sensitive. Aspirin without transport, a scheduled follow-up, and waiting thirty minutes all delay care.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-emergency-aid-024
    fact(
        "skill-emergency-aid",
        "A patient on warfarin has a nosebleed that continues after fifteen minutes of correct first aid. What is the appropriate response?",
        "Keep pressure on the nose and notify the provider right away",
        [
            "Tilt the head back and apply a cold compress to the forehead",
            "Let the patient drive home and return if the bleeding continues",
            "Pack the nostril firmly and recheck in an hour before calling",
        ],
        "Anticoagulation makes a nosebleed harder to control, so the pressure hold continues and the provider is notified because reversal or nasal packing may be needed. Tilting the head back sends blood down the throat, sending the patient home without supervision risks further blood loss, and packing without guidance can injure the nose.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-025
    fact(
        "skill-emergency-aid",
        "What first aid is appropriate for a small thermal burn on the forearm?",
        "Cool the burn under running water and remove any nearby jewelry",
        [
            "Cool the burn under running water and leave the jewelry in place",
            "Ice the burn directly for twenty minutes and leave it uncovered",
            "Apply butter to the burn and wrap it loosely in a clean towel",
        ],
        "Cooling a small thermal burn under cool running water limits the depth of injury, and rings or bracelets come off before swelling starts. Leaving jewelry in place risks strangulation of swollen tissue, direct ice can damage skin, and butter or ointment traps heat in the tissue.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-026
    fact(
        "skill-emergency-aid",
        "A patient on an insulin pump has vomiting and positive urine ketones. What is the appropriate response?",
        "Notify the provider, check the glucose, and arrange urgent transport",
        [
            "Stop the insulin pump and send the patient home to rest for the day",
            "Encourage vigorous exercise and extra water before the next scheduled meal",
            "Give a sugary drink and recheck the urine ketones in an hour",
        ],
        "Vomiting with positive ketones suggests diabetic ketoacidosis, which needs provider notification, a glucose check, and urgent transfer rather than home care. Stopping the pump removes insulin delivery, exercise worsens the metabolic state, and a sugary drink does not clear the ketones.",
        [S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-027
    fact(
        "skill-emergency-aid",
        "A patient has audible wheezing and retractions after an allergen exposure. What is the clinic priority?",
        "Immediate provider evaluation with oxygen and bronchodilator treatment",
        [
            "Ask the patient to sit quietly and repeat the peak flow in an hour",
            "Give an oral antihistamine and recheck the wheezing after thirty minutes",
            "Send the patient home with an inhaler and recheck by phone in two days",
        ],
        "Wheezing with retractions signals respiratory distress that can progress to failure, so the provider evaluates the patient and oxygen with bronchodilator therapy starts under orders. Resting quietly, an oral antihistamine alone, and a phone follow-up in two days all leave a worsening airway unobserved.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "intermediate",
    ),
    # skill-emergency-aid-028
    fact(
        "skill-emergency-aid",
        "A child falls and the forearm is visibly angulated with severe pain. What first aid is appropriate?",
        "Splint the arm as found, control the pain, and arrange urgent imaging",
        [
            "Straighten the arm to the normal position and apply a cold pack",
            "Apply a tight elastic wrap and have the child use the arm normally",
            "Massage the elbow and have the child return to sports practice the same day",
        ],
        "A suspected fracture is splinted in the position found with pain control and prompt imaging, because forcing the limb straight can damage nerves and vessels. Straightening the arm, wrapping it tightly for normal use, and massaging the joint all make the injury worse.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-029
    fact(
        "skill-emergency-aid",
        "An avulsed permanent tooth is recovered within thirty minutes. How should it be handled before dental referral?",
        "Hold the tooth by the crown and store it in milk or saline",
        [
            "Hold the tooth by the crown and store it in dry paper towels",
            "Scrub the root clean and store the tooth in a sterile tray",
            "Rinse the root with alcohol and store the tooth in saline",
        ],
        "An avulsed tooth that is replanted quickly has the best chance of surviving, so the root is handled by the crown and kept moist in milk or saline. Dry paper towels, scrubbing, and alcohol all destroy the periodontal ligament cells that the tooth needs to reattach.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-030
    fact(
        "skill-emergency-aid",
        "Several staff and a patient have headache and nausea after being in a house with a faulty furnace. What response is appropriate?",
        "Move everyone to fresh air and arrange emergency medical evaluation",
        [
            "Give oxygen by nasal cannula and send the staff home to rest",
            "Have everyone drink fluids and reassess the symptoms again in an hour",
            "Open the windows and keep working in the area until symptoms pass",
        ],
        "Headache and nausea in several people who shared an enclosed space with a faulty furnace point to carbon monoxide exposure, so everyone leaves for fresh air and needs emergency evaluation. Oxygen without leaving the source continues the exposure, fluids do not remove the gas, and staying in the area prolongs it.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-031
    fact(
        "skill-emergency-aid",
        "What first aid is appropriate for a mild ankle sprain in the clinic?",
        "Rest the limb, apply ice for about twenty minutes, and elevate it",
        [
            "Apply heat for twenty minutes and massage the joint firmly right away",
            "Wrap the joint snugly and have the patient keep walking the day",
            "Apply ice for an hour and stretch the joint firmly right after",
        ],
        "Rest, ice, and elevation limit swelling and pain during the first hours after a sprain. Heat and early massage increase bleeding into the injury, wrapping without rest lets swelling build, and an hour of ice followed by stretching delays healing.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "beginner",
    ),
    # skill-emergency-aid-032
    fact(
        "skill-emergency-aid",
        "A toddler pulls a bead into the ear canal while waiting in the clinic. What should the medical assistant do?",
        "Ask the provider to remove it with the proper tools and lighting",
        [
            "Insert tweezers into the canal and pull the bead out by feel",
            "Flush the canal with a high-pressure syringe aimed into the opening",
            "Leave the bead in place and recheck it during a later visit",
        ],
        "Ear foreign bodies need direct visualization and the right instruments, so the provider removes the bead. Tweezers inserted without visualization can perforate the eardrum, high-pressure flushing can drive the object deeper, and leaving it in place risks further injury and infection.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-emergency-aid-033
    fact(
        "skill-emergency-aid",
        "An amputated fingertip with clean edges is ready for transport with the patient. How should it be handled?",
        "Wrap it in saline-moistened gauze, seal it in a bag, and place it on ice",
        [
            "Wrap it in saline-moistened gauze, seal it in a bag, and freeze it solid",
            "Place it directly in ice water and seal the container for transport",
            "Wrap it in dry gauze, seal it in a bag, and keep it at room temperature",
        ],
        "Tissue for possible reattachment is kept cool and moist, wrapped in saline-soaked gauze and sealed in a waterproof bag that sits over ice water without direct contact. Freezing the tissue, immersing it directly in ice water, and keeping it dry at room temperature all destroy the cells the surgeon needs.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-034
    fact(
        "skill-emergency-aid",
        "A mass casualty incident occurs near the clinic entrance. What triage principle should staff follow?",
        "Prioritize patients with immediate life threats and tag them for responders",
        [
            "Treat the patients with minor injuries first because they are quicker to help",
            "Wait for a triage officer from EMS before approaching a patient",
            "Move every patient inside the clinic before sorting them by condition",
        ],
        "When resources are limited, triage sorts patients by the severity of their injuries so those with immediate life threats are treated first and everyone is accounted for. Treating minor injuries first, waiting for outside direction before starting, and moving people indoors without sorting all reduce the chance of survival.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-035
    fact(
        "skill-emergency-aid",
        "A patient is found outside in cold weather with confusion and slow, shallow breathing. What is the priority response?",
        "Activate EMS, remove the wet clothing, and begin gentle warming with blankets",
        [
            "Give hot drinks by mouth and rub the limbs vigorously to restore circulation",
            "Immerse the body in a hot bath and keep the patient active until help arrives",
            "Place the patient under a heating blanket and give hot drinks by mouth",
        ],
        "Confusion with slow, shallow breathing suggests significant hypothermia, so EMS activation, removal of wet clothing, and gradual warming with blankets are appropriate. Hot drinks by mouth risk aspiration in a confused patient, vigorous rubbing and hot baths can trigger arrhythmias, and warming without EMS leaves deterioration unmonitored.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-036
    fact(
        "skill-emergency-aid",
        "A lightning strike victim is found pulseless in the parking lot after the storm. What is the appropriate response?",
        "Confirm the scene is safe, then start CPR and attach the AED",
        [
            "Wait for the storm to pass completely before approaching the victim",
            "Cover the victim with blankets and wait for the person to wake on their own",
            "Lay the victim flat with the legs raised to restore circulation",
        ],
        "A struck patient is safe to touch once the strike has ended and many survive with good resuscitation, so CPR and the AED start right away after the scene is checked. Waiting for the storm to end delays lifesaving care, covering the victim and waiting forfeits resuscitation, and raising the legs does not treat cardiac arrest.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-037
    fact(
        "skill-emergency-aid",
        "Which information should the medical assistant give EMS when handing off a stabilized emergency patient?",
        "Onset time, interventions given, allergies, and the most recent vital signs",
        [
            "Onset time, interventions given, insurance status, and vital signs",
            "Onset time, room assignment, allergies, and the most recent vital signs",
            "Onset time, interventions given, allergies, and the most recent supply count",
        ],
        "EMS needs the timeline, what was done, what the patient reacts to, and the most recent objective findings to continue care safely. Insurance status, the room assignment, and a supply count do not change the clinical management in transit.",
        [S.NHA_CCMA, S.AHA_ADULT_BLS],
        "beginner",
    ),
    # skill-emergency-aid-038
    fact(
        "skill-emergency-aid",
        "Life-threatening bleeding from the patient's leg continues despite firm direct pressure. What is the appropriate next step?",
        "Apply a tourniquet proximal to the wound and activate emergency services",
        [
            "Wrap the leg in a compression bandage and reassess the bleeding later",
            "Keep the leg at heart level and reapply gauze every few minutes",
            "Give oral antibiotics and check the bleeding again at the next clinic visit",
        ],
        "When direct pressure cannot control life-threatening extremity bleeding, a tourniquet placed proximal to the wound stops the flow while EMS is activated. A compression wrap and more gauze repeat measures that already failed, and antibiotics do nothing for active hemorrhage.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-039
    fact(
        "skill-emergency-aid",
        "A cleaning chemical splashes into a patient's eye at work. What first aid is appropriate?",
        "Flush the eye with clean lukewarm water for at least fifteen minutes",
        [
            "Flush the eye with clean lukewarm water for about fifteen seconds",
            "Rub the eye gently and apply antibiotic ointment after a brief rinse",
            "Apply a cold compress over the closed eye and recheck in an hour",
        ],
        "Chemical eye burns are washed out with continuous lukewarm water for at least fifteen minutes, and the patient needs emergency evaluation afterward. A fifteen-second rinse leaves the chemical on the eye, ointment traps the agent, and a cold compress does nothing to remove it.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-040
    fact(
        "skill-emergency-aid",
        "A patient swallowed a caustic household cleaner and is drooling with mouth pain. What is appropriate while waiting for EMS?",
        "Keep the patient from eating or drinking, watch the airway, keep the container",
        [
            "Give milk or water to dilute it and wait for the ambulance",
            "Induce vomiting so the chemical leaves the stomach quickly at home",
            "Rinse the mouth with mouthwash and give the patient a soft snack to eat at once",
        ],
        "Caustic ingestion risks airway swelling and perforation, so the patient takes nothing by mouth, the airway is watched, and the container goes to EMS for the poison center. Diluting with milk or water, inducing vomiting, and giving food or mouthwash all increase the injury.",
        [S.RED_CROSS_FIRST_AID, S.NHA_CCMA],
        "advanced",
    ),
    # skill-emergency-aid-041
    fact(
        "skill-emergency-aid",
        "What monitoring is needed after epinephrine is given for anaphylaxis while EMS is on the way?",
        "Repeat vital signs, watch the airway, and keep a second dose available",
        [
            "Repeat vital signs, watch the airway, and discharge once the hives fade",
            "Repeat vital signs once, then send the patient home with a refill",
            "Repeat vital signs, watch the airway, and prepare the discharge paperwork",
        ],
        "Symptoms can return after epinephrine wears off, so vital signs, breathing, and the airway are watched, a second dose stays ready, and the patient remains for observation. Discharging when the hives fade, sending the patient home with a refill, and preparing discharge paperwork leave a possible biphasic reaction unmonitored.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-emergency-aid-042
    fact(
        "skill-emergency-aid",
        "After assisting with a clinic code, which follow-up steps belong to the medical assistant?",
        "File the incident report, join the debrief, and disinfect the equipment",
        [
            "File the incident report, join the debrief, and reuse the used gloves",
            "File the incident report, join the debrief, and discard the reusable equipment",
            "File the incident report, join the debrief, and rinse the equipment with water",
        ],
        "After a code, staff file the incident report, take part in the debrief, and disinfect the equipment so patients and the next team are protected. Reusing gloves spreads contamination, discarding reusable equipment wastes gear that can be reprocessed, and a water rinse does not disinfect.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
]
