# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""American Red Cross first aid question bank (Red Cross curriculum; not AHA BLS)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_RC = [S.RED_CROSS_FIRST_AID]

FACTS: list[dict] = [
    fact(
        "cpr-red-cross",
        "Beyond CPR skills, what topics do American Red Cross first aid courses cover?",
        "Bleeding control, burns, sudden illness, and environmental injury",
        [
            "Advanced cardiac procedures including 12-lead ECG interpretation",
            "Sterile surgical instrument processing in an operating room setting",
            "Vaccine cold-chain storage and lot-number documentation",
        ],
        "Red Cross first aid teaches bleeding, burns, sudden illness, and environmental emergencies "
        "alongside optional CPR certification. EKG interpretation, operating-room instrument "
        "processing, and vaccine cold-chain storage are outside typical Red Cross first aid scope.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "For minor external bleeding, what is the American Red Cross first aid priority?",
        "Apply direct pressure with a clean dressing over the wound",
        [
            "Pack ice directly into the open wound without a dressing",
            "Elevate the limb without holding pressure on the bleeding site",
            "Place a tourniquet high on the limb for a minor scrape",
        ],
        "Direct pressure helps clot formation at the skin surface. "
        "Ice inside the wound, elevation without pressure, or routine tourniquet use do not match Red Cross minor bleeding care.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "Which combination of findings most suggests anaphylaxis that needs emergency care per Red Cross first aid?",
        "Hives or swelling with wheezing, throat tightness, or signs of shock",
        [
            "One small hive at the sting site without breathing difficulty",
            "Mild itching after contact with laundry detergent alone",
            "Slow-onset dry skin rash without airway or circulation symptoms present",
        ],
        "Systemic allergic reaction can involve skin, airway, and circulation. "
        "Isolated mild itching or a single local hive without systemic signs is not treated as anaphylaxis.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "A worker has heavy sweating, weakness, and cool clammy skin after heat exposure. What Red Cross first aid is appropriate for suspected heat exhaustion?",
        "Move to a cool area, loosen clothing, and give fluids if fully awake",
        [
            "Continue strenuous work in the sun to build up heat tolerance over days",
            "Withhold fluids even when the person is alert and asking for water",
            "Immerse the person in ice water without monitoring their breathing",
        ],
        "Heat exhaustion care focuses on rest, cooling, and hydration when swallowing is safe. "
        "Ice-water immersion without monitoring is reserved for heat stroke protocols with EMS involvement.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "What is the American Red Cross priority when managing suspected hypothermia in the field?",
        "Gentle handling, remove wet clothing, insulate, and rewarm gradually",
        [
            "Vigorous rubbing of the cold extremities to restore circulation quickly",
            "Leave the wet clothing in place to trap body heat",
            "Force the person to run laps around the site until they feel warm",
        ],
        "Hypothermia care emphasizes gentle handling and gradual rewarming to limit afterdrop and arrhythmia risk. "
        "Rough massage, wet clothing, and strenuous exercise can worsen cold injury.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "During a generalized seizure, what should a Red Cross-trained first aid provider do while the person is actively seizing?",
        "Protect the head, clear nearby hazards, and time the seizure duration",
        [
            "Hold the person down firmly to stop the movements",
            "Place a spoon or other object between the teeth",
            "Pour small sips of water into the mouth during the active jerking movements",
        ],
        "Red Cross seizure care protects from injury and notes duration without restraint or mouth objects. "
        "Fluids during active jerking risk aspiration.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "When stroke is suspected, what does the American Red Cross FAST mnemonic prompt you to do?",
        "Call 911 right away if face, arm, or speech abnormalities are present",
        [
            "Wait twenty-four hours to see whether the symptoms resolve on their own",
            "Drive the person to a pharmacy for over-the-counter aspirin",
            "Give aspirin without activating EMS when speech is mildly slurred",
        ],
        "FAST highlights Face, Arm, Speech, and Time to call emergency services. "
        "Delayed activation or aspirin without EMS assessment can miss time-sensitive stroke treatment.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "What is appropriate American Red Cross first aid for a small thermal burn without charring?",
        "Cool the burn with running water and cover with a dry dressing",
        [
            "Apply butter or cooking oil to the surface of the burn",
            "Break blisters immediately to drain fluid",
            "Place ice directly on the skin instead of cooling with running water",
        ],
        "Cool running water limits depth of injury; a clean dressing protects afterward. "
        "Butter, ice directly on skin, and deliberate blister rupture increase infection and tissue damage risk.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "In American Red Cross soft-tissue injury care, what do RICE principles cover?",
        "Rest, ice, compression, and elevation for the injury",
        [
            "Radiograph, insulin, catheter, and epinephrine for a sprain",
            "Long-term cardiac rehabilitation planning before splinting",
            "Routine surgical sterilization of home first aid kits",
        ],
        "RICE addresses acute sprains and strains with rest, ice, compression, and elevation. "
        "It does not replace medical evaluation for severe injury or fracture suspicion.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "After a chemical splash to the eye, what does Red Cross first aid emphasize?",
        "Flush with clean water or saline for an extended time",
        [
            "Patch the eye closed without irrigating the surface",
            "Neutralize the chemical with household vinegar before the water flush",
            "Delay all flushing until the person reaches a clinic",
        ],
        "Immediate irrigation dilutes chemical injury, and prolonged flushing continues while help is "
        "arranged. Patching the eye, unverified neutralizers, and delayed rinsing allow continued "
        "ocular damage.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "A conscious diabetic adult is confused and diaphoretic. What Red Cross first aid may be appropriate if they can swallow safely?",
        "Give about fifteen grams of fast-acting carbohydrate and recheck",
        [
            "Give injectable insulin before checking the blood glucose result",
            "Withhold all sugar and observe the person for one hour",
            "Treat as heat stroke without ever considering the blood glucose",
        ],
        "Confusion with sweating suggests hypoglycemia; fast sugar is given only when the person is awake and can swallow. "
        "Insulin worsens low glucose, and withholding sugar delays treatment of symptomatic hypoglycemia.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "When is a tourniquet appropriate for extremity bleeding in American Red Cross first aid?",
        "When life-threatening limb bleeding does not stop with pressure",
        [
            "As the first step for minor paper cuts on the fingers and hands",
            "Placed distal to the wound on the forearm for an arm bleed",
            "Loosened every minute for patient comfort during the transport",
        ],
        "Tourniquets are a last resort for severe limb hemorrhage when pressure fails. "
        "They are not used for minor wounds, distal placement, or routine loosening that restarts bleeding.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "What is the focus of American Red Cross psychological first aid after a traumatic event?",
        "Promote safety, calm, connectedness, and hope without detailed interviews",
        [
            "Diagnose psychiatric disorders and prescribe sedatives on scene",
            "Require the person to recount the traumatic event in full detail right away",
            "Tell the person to avoid all follow-up mental health resources",
        ],
        "Psychological first aid supports immediate emotional safety and connection. "
        "It does not replace professional mental health care or medication prescribing.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "What safety step do American Red Cross first aid courses teach before approaching an ill or injured person?",
        "Check that the scene is safe for you, the patient, and bystanders",
        [
            "Run across traffic lanes before scanning for vehicles",
            "Assume the scene is safe if the patient is calling for help",
            "Begin hands-on care before looking for electrical or fire hazards",
        ],
        "Scene size-up identifies traffic, fire, electrical, and violence hazards before contact. "
        "Rushing in without scanning puts rescuers and patients at additional risk.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "While waiting for EMS after controlling bleeding from a hand laceration, what additional Red Cross step may help if no fracture is suspected?",
        "Elevate the injured extremity above heart level and hold pressure",
        [
            "Release the pressure every thirty seconds to air the wound",
            "Apply a tourniquet for a hand laceration even when bleeding is minor",
            "Soak the hand in warm water to constrict the blood vessels",
        ],
        "Elevation assists venous drainage when bones are not suspected to be broken and pressure is maintained. "
        "Intermittent pressure release or routine tourniquet use is not first-line for controlled lacerations.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "A hiker has confusion, hot dry skin, and a very high temperature after exertion in heat. What is the likely problem and Red Cross priority?",
        "Heat stroke; call 911 and cool the person while monitoring the airway",
        [
            "Heat exhaustion; encourage finishing the hike at a slower walking pace",
            "Hypothermia; wrap in wet towels without activating emergency help",
            "Mild sunburn; apply the lotion and return to the activity",
        ],
        "Altered mental status with hot dry skin suggests heat stroke, a medical emergency. "
        "Heat exhaustion typically includes heavy sweating and does not present with the same mental status change.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "After a deep nail puncture wound, what Red Cross documentation and follow-up matter once bleeding is controlled?",
        "Clean the area, dress the wound, and seek evaluation for tetanus",
        [
            "Ignore the tetanus history because puncture wounds look superficial",
            "Seal the puncture track with household super glue",
            "Soak the foot in hydrogen peroxide for hours before medical review",
        ],
        "Puncture wounds can introduce deep infection and tetanus risk. "
        "Medical review guides wound care and prophylaxis beyond home cleaning alone.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "Which snakebite first aid is consistent with American Red Cross guidance?",
        "Keep the person calm, keep the limb near heart level, and get medical care",
        [
            "Cut the wound and attempt to suck the venom out of the bite site",
            "Apply ice directly on the bite for a short period of time",
            "Place a tourniquet proximal to the bite even when the swelling is very limited",
        ],
        "Red Cross care emphasizes calm, limb positioning, and EMS evaluation. "
        "Cutting, suction, and routine tourniquet use are outdated or harmful approaches.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "For a nosebleed, why does American Red Cross first aid prefer leaning slightly forward?",
        "Forward lean keeps blood from draining into the stomach and causing nausea",
        [
            "Head-back position clears blood from the airway more quickly",
            "Swallowing blood is harmless and preferred",
            "Pinching the bony bridge of the nose without timing the pressure applied at all",
        ],
        "Leaning forward with pinch pressure on the soft nose reduces swallowed blood. "
        "Head-back positioning can cause gagging and does not replace sustained soft-tissue pinch.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "After bleeding is controlled on a minor scrape, what Red Cross wound care is appropriate?",
        "Wash the area gently and cover with a sterile dressing",
        [
            "Leave dirt in the wound to promote natural healing",
            "Apply a tight circumferential tourniquet above the scrape",
            "Ignore increasing redness because small wounds rarely become infected",
        ],
        "Cleaning and dressing reduce infection risk for superficial wounds. "
        "Tourniquets and ignored infection signs are not appropriate for minor abrasions.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "When applying direct pressure to bleeding, what material should be used per Red Cross first aid?",
        "A clean cloth or sterile dressing over the wound",
        [
            "Bare fingers pressed into an open wound without a barrier",
            "Steady pressure directly on a visibly embedded object",
            "Hot water immersion of the bleeding limb",
        ],
        "A barrier under pressure protects both patient and rescuer while promoting clotting. "
        "Pressure on embedded objects and hot water immersion are not standard bleeding control.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "Which anaphylaxis signs should prompt calling 911 in American Red Cross first aid?",
        "Difficulty breathing or swelling of the tongue or lips",
        [
            "One localized hive with no breathing change or swelling",
            "Dry skin with no airway symptoms or signs of shock",
            "A chronic eczema flare with no systemic signs present",
        ],
        "Airway and tongue or lip swelling signal systemic reaction needing emergency care. "
        "Mild localized skin findings alone are managed differently than anaphylaxis.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "For a suspected ankle sprain without deformity, what initial Red Cross care is often used?",
        "Rest, ice, compression, and elevation as tolerated",
        [
            "Apply heat immediately and resume full activity",
            "Ignore swelling and walk several miles to test the joint",
            "Wrap the joint so tightly that distal pulses disappear",
        ],
        "RICE limits pain and swelling after acute soft-tissue injury. "
        "Heat, forced activity, or circulatory compromise from excessive compression worsen outcomes.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "For life-threatening extremity bleeding when pressure fails, where should a tourniquet be placed per Red Cross teaching?",
        "High and tight on the limb proximal to the wound",
        [
            "Loosely around the ankle for bleeding in the upper arm",
            "Distal to the wound on the forearm",
            "Removed and retied every minute for comfort",
        ],
        "Proximal high placement occludes arterial inflow to the limb segment distal to the device. "
        "Distal or loose tourniquets fail to control hemorrhage and repeated loosening restarts bleeding.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "For chemical splash to the eye, how long should flushing continue in American Red Cross first aid while help is activated?",
        "At least fifteen minutes of flushing with clean water",
        [
            "A five-second rinse followed by patching the eye closed",
            "Neutralize with household vinegar before the water flush",
            "Wait until clinic arrival to begin irrigation",
        ],
        "Extended irrigation dilutes chemical injury; EMS may advise continued flushing in transit. "
        "Brief rinsing or unverified neutralizers leave residual chemical on the ocular surface.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "Which findings are most consistent with heat exhaustion rather than heat stroke in Red Cross teaching?",
        "Heavy sweating, weakness, and cool clammy skin after heat",
        [
            "Hot dry skin with confusion and very high temperature",
            "Shivering and low temperature after cold water immersion",
            "Crushing chest pain radiating to the jaw without heat exposure",
        ],
        "Heat exhaustion often includes sweating and clammy skin. "
        "Hot dry skin with altered mental status suggests heat stroke needing EMS and aggressive cooling.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "In American Red Cross stroke assessment, what does the T in FAST represent?",
        "Time to call 911 when face, arm, or speech signs are abnormal",
        [
            "Transport the patient yourself without calling emergency services",
            "Temperature measurement before EMS activation",
            "Tourniquet placement on the affected arm",
        ],
        "FAST ends with Time to activate emergency services for possible stroke. "
        "Self-transport delays hospital stroke pathways that depend on EMS notification.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "Which burn patterns should receive emergency medical evaluation per Red Cross first aid?",
        "Charred skin, circumferential burns, or burns on the face or airway",
        [
            "Small superficial redness treated with an ointment at home",
            "Circumferential limb burns monitored at home without calling for EMS",
            "All blisters popped immediately before a dressing is applied",
        ],
        "Deep, circumferential, or airway-involved burns risk fluid loss and swelling. Small "
        "superficial redness may be managed at home with cooling and medical advice per local "
        "protocol.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "During a nosebleed with the patient leaning slightly forward, how long should the soft part of the nose be pinched?",
        "About ten to fifteen minutes without releasing to check bleeding",
        [
            "About ten seconds with the head tilted fully backward",
            "Until blood stops after releasing pinch every thirty seconds",
            "The bony bridge is pinched while the person breathes through the mouth",
        ],
        "Sustained soft-tissue pinch with forward lean is standard Red Cross nosebleed care. "
        "Frequent release or bridge-only pinch fails to compress the bleeding vessels.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "For a bee sting with localized swelling and normal breathing, what Red Cross first aid is appropriate?",
        "Scrape the stinger, wash the area, and apply a cold pack",
        [
            "Pinch and squeeze the venom sac to pull the stinger out of the skin",
            "Apply heat to the sting site to disperse venom",
            "Ignore swelling even when breathing becomes noisy",
        ],
        "Scraping avoids injecting more venom; cold reduces local inflammation. "
        "Squeezing the sac and ignoring breathing changes miss worsening allergic reaction.",
        _RC,
        "beginner",
    ),
    fact(
        "cpr-red-cross",
        "What is the goal of splinting an injured extremity in American Red Cross first aid?",
        "Immobilize the joints above and below the suspected injury site",
        [
            "Immobilize the joint above the injury while moving the distal joint",
            "Repeatedly test range of motion to assess pain",
            "Wrap the limb until distal circulation is absent",
        ],
        "Splinting limits motion at both adjacent joints to prevent further soft-tissue or bone injury. "
        "Circulation checks should remain possible after splint application.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "When calling a poison control center about a possible ingestion, what information should you have ready?",
        "Substance name, estimated amount, time of exposure, and patient age",
        [
            "The patient insurance member identification number and group code",
            "The prescribing physician office fax number and after-hours line",
            "Whether the patient ate a meal earlier that day and their allergies",
        ],
        "Poison specialists need exposure details to guide first aid and referral. "
        "Insurance or fax data do not replace substance, dose, timing, and patient size information.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "For suspected electrical injury, what is the American Red Cross scene priority?",
        "Ensure scene safety, shut off power if possible, and activate EMS",
        [
            "Grab the patient while the electrical circuit is still energized",
            "Apply antibiotic ointment before de-energizing the power source safely",
            "Defer cardiac monitoring because the skin looks unburned",
        ],
        "Rescuers must not contact energized patients; power isolation precedes care. "
        "Electrical injury can cause internal arrhythmias even with minor external burns.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "A permanent tooth is knocked out. How should American Red Cross first aid prepare it for urgent dental care?",
        "Keep the tooth moist in milk or saline and seek urgent dental evaluation",
        [
            "Scrub the root with soap and water until clean",
            "Store the tooth dry in a pocket until the dentist opens",
            "Discard the tooth if it touched dirt without attempting reimplant guidance",
        ],
        "Moist storage protects periodontal ligament cells for possible reimplantation. "
        "Scrubbing, drying, or discarding reduces chances of successful dental reattachment.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "After significant trauma, which findings suggest shock per Red Cross first aid?",
        "Pale cool skin, rapid pulse, and confusion or anxiety",
        [
            "Flushed hot skin with a strong slow pulse by itself alone",
            "Isolated finger pain without other systemic signs",
            "Mild nervousness without injury or bleeding",
        ],
        "Shock may present with poor perfusion signs after blood loss or severe injury. "
        "Isolated finger pain or mild anxiety without perfusion changes does not define shock.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "A youth athlete has headache and dizziness after a head blow in a game. What Red Cross sports concussion care applies?",
        "Remove from play and seek medical evaluation before returning",
        [
            "Return to the game once the symptoms improve within five minutes",
            "Apply heat to the scalp and continue playing",
            "Ignore a next-day headache if no loss of consciousness occurred",
        ],
        "Concussion requires removal from play and medical clearance before return. "
        "Same-day return and ignored delayed symptoms increase second-impact risk.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "For an impaled object in the body, what does American Red Cross first aid teach?",
        "Stabilize the object in place and seek emergency care without removal",
        [
            "Remove the object quickly to let the wound bleed and drain freely",
            "Cut the object flush with the skin and leave the fragment in place",
            "Pack the wound with loose cotton and pull the object out at home later",
        ],
        "Impaled objects may tamponade bleeding; removal in the field can worsen hemorrhage. "
        "Stabilization and EMS transport allow controlled removal in the hospital.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "When spinal injury is suspected after a fall, what is the Red Cross approach before EMS arrives?",
        "Manual stabilization of the head and neck with minimal movement",
        [
            "Sit the person upright to ease breathing immediately",
            "Twist the neck to test whether pain is present",
            "Pull the person by the arms to move them off the road in a hurry",
        ],
        "Suspected spine injury requires limiting motion until trained providers immobilize. "
        "Sitting, twisting, or dragging increases spinal cord injury risk.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "Per American Red Cross adult choking care, what sequence is used for a conscious adult with severe airway obstruction?",
        "Alternate five back blows and five abdominal thrusts until the object clears",
        [
            "Abdominal thrusts with no back blows for a conscious adult",
            "One back blow then stop all care even if obstruction continues",
            "Chest compressions while the adult remains conscious and clutching the throat",
        ],
        "Red Cross responsive adult severe choking care cycles five back blows with five abdominal thrusts. "
        "AHA adult BLS emphasizes abdominal thrusts without that alternating back-blow cycle; this item tests Red Cross sequencing.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "How does American Red Cross choking care for a conscious child with severe obstruction differ from infant choking care?",
        "Back blows and abdominal thrusts sized to the child",
        [
            "Adult-style abdominal thrusts with no back blows for a child",
            "Infant back slaps and chest thrusts applied to a conscious child",
            "No maneuvers until the child becomes unresponsive on the floor",
        ],
        "Red Cross child choking uses back blows and age-appropriate abdominal thrusts. "
        "Infants receive back slaps and chest thrusts rather than abdominal thrusts.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "An American Red Cross-trained rescuer finds a conscious adult who cannot speak and has a silent ineffective cough after choking on food. What is the first Red Cross maneuver?",
        "Five back blows, then five abdominal thrusts, repeating cycles",
        [
            "Encourage forceful coughing because a cough can mean a mild airway blockage",
            "Wait for EMS on scene without back blows or abdominal thrusts",
            "Blind finger sweeps before the back blows or the abdominal thrusts",
        ],
        "Severe obstruction with poor air exchange starts with back blows followed by abdominal thrusts in Red Cross care. "
        "Effective cough with good air movement is monitored rather than immediate thrusts.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "After a Red Cross first aid seizure ends and the person is breathing, what positioning helps protect the airway?",
        "Place the person on their side in a recovery-style position",
        [
            "Leave the person flat on their back without monitoring the breathing",
            "Sit the person upright immediately and offer a large meal",
            "Restrain the arms tied to the bed rails until EMS arrives",
        ],
        "Side positioning helps keep the airway clear after a postictal period. "
        "Restraint and unmonitored supine positioning increase aspiration and injury risk.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "Which action is appropriate for a conscious person having a mild allergic reaction with only localized hives and no breathing difficulty?",
        "Monitor closely and activate EMS if breathing or swelling worsens",
        [
            "Give a second epinephrine auto-injector dose immediately without assessment",
            "Withhold observation because hives mean anaphylaxis",
            "Apply a tourniquet proximal to the hive site",
        ],
        "Localized hives without systemic signs are watched for progression per Red Cross and medical guidance. "
        "Epinephrine and tourniquets are not routine for isolated mild skin reaction.",
        _RC,
        "intermediate",
    ),
    fact(
        "cpr-red-cross",
        "In American Red Cross first aid, when may aspirin be considered for an adult with suspected heart attack?",
        "When the person is conscious, not allergic, and EMS advises aspirin",
        [
            "Automatically for a chest complaint without ever calling 911 for help",
            "For a child with chest pain as the first intervention",
            "Instead of activating EMS when nitroglycerin is available to give",
        ],
        "Chest pain with suspected heart attack requires EMS activation; aspirin is given only when appropriate and not contraindicated. "
        "Aspirin does not replace emergency evaluation or pediatric-specific protocols.",
        _RC,
        "advanced",
    ),
    fact(
        "cpr-red-cross",
        "What should you do for frostbite of fingers in American Red Cross field first aid?",
        "Move to a warm place, remove wet clothing, and seek medical care",
        [
            "Rub snow vigorously into the fingers to restore the color",
            "Immerse frostbitten tissue in hot water immediately without EMS guidance",
            "Ignore the numbness if the skin still looks pink at the fingertips",
        ],
        "Frostbite care uses gentle rewarming and medical evaluation; rubbing injured tissue causes further damage. "
        "Aggressive hot immersion without assessment can worsen injury.",
        _RC,
        "advanced",
    ),
]
