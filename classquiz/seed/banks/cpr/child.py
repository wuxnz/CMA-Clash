# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored child pediatric BLS question bank (AHA 2020+ aligned)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_REF = [S.AHA_WHAT_IS_CPR, S.AHA_ADULT_BLS]
_HQ = [S.AHA_WHAT_IS_CPR, S.AHA_HQ_CPR, S.AHA_ADULT_BLS]

FACTS: list[dict] = [
    # --- beginner (14) ---
    fact(
        "cpr-child",
        "A single lay rescuer is performing BLS on a school-age child in cardiac arrest. "
        "Which compression-to-ventilation ratio should they use?",
        "30 compressions followed by 2 ventilations",
        [
            "15 compressions followed by 2 ventilations",
            "5 compressions followed by 1 ventilation",
            "Continuous chest compressions with no ventilations for the entire arrest",
        ],
        "AHA pediatric BLS uses 30:2 when only one rescuer is available. The 15:2 ratio is reserved "
        "for two-rescuer child CPR so one person can focus on compressions. Continuous compressions "
        "without breaths omit needed oxygenation in many pediatric arrests.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "During high-quality child CPR, what chest compression rate should rescuers target?",
        "100 to 120 compressions per minute",
        [
            "60 to 80 compressions per minute",
            "140 to 160 compressions per minute",
            "As slow as possible to reduce rib injury",
        ],
        "Pediatric compressions follow the same rate target as adult BLS. A rate of 60 to 80 is too "
        "slow to maintain adequate coronary and cerebral perfusion. Extremely fast compressions "
        "prevent full recoil and reduce effectiveness.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-child",
        "Where should the heel of the hand be placed for chest compressions on a child?",
        "Center of the chest on the lower half of the sternum",
        [
            "Directly over the xiphoid process with maximal force",
            "Upper abdomen just below the rib cage",
            "Left nipple line over the cardiac apex only",
        ],
        "Compressions over the lower sternum generate forward blood flow with the least risk of "
        "injury. Pressing on the xiphoid can cause fracture and does not compress the heart "
        "effectively. Abdominal compressions do not substitute for sternal compressions.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "Why does AHA emphasize rescue ventilations for many pediatric arrests when rescuers are "
        "willing and able to give breaths?",
        "Children often arrest from respiratory causes, so early oxygenation and ventilation matter",
        [
            "Children never need chest compressions once breaths are given",
            "Ventilations are optional for all children over age 5",
            "Compression-only CPR is preferred for every pediatric age group",
        ],
        "Hypoxia and respiratory failure are common pathways to pediatric cardiac arrest. "
        "Compressions remain essential, but breaths address the underlying problem in many cases. "
        "Compression-only CPR is not the preferred approach when ventilations can be delivered safely.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "You approach a playground where a child is lying motionless. What is the first BLS action "
        "after confirming scene safety?",
        "Check responsiveness by tapping shoulders and shouting",
        [
            "Begin chest compressions before checking for response",
            "Search the area for an AED before touching the child",
            "Pour water on the child to test for reaction",
        ],
        "Recognition of unresponsiveness triggers activation of emergency response and assessment of "
        "breathing and pulse. Starting compressions on a responsive child would be inappropriate. "
        "Scene safety and responsiveness checks precede device retrieval.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "When should an AED be applied to a child in suspected cardiac arrest?",
        "As soon as it becomes available while high-quality CPR continues",
        [
            "Only after 10 minutes of compressions have been completed",
            "Only if the child is older than 12 years",
            "After EMS arrives and takes over compressions exclusively",
        ],
        "Early defibrillation improves survival in shockable rhythms. Delaying pad placement for a "
        "fixed time wastes the defibrillation link in the Chain of Survival. Pediatric patients can "
        "benefit from AED use with appropriate pad systems when indicated.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "Which combination best describes high-quality chest compressions during child CPR?",
        "Hard, fast compressions with full chest recoil and minimal pauses",
        [
            "Soft compressions with the rescuer leaning on the chest between pushes",
            "Fast compressions with no attention to depth or recoil",
            "Deep compressions held without allowing the chest to return",
        ],
        "Depth, rate, recoil, and limited interruptions define high-quality CPR. Leaning on the chest "
        "blocks recoil and reduces perfusion. Holding compressions without release prevents diastolic "
        "filling of the heart.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-child",
        "A conscious 8-year-old is eating when he begins coughing forcefully and can still speak in "
        "short sentences. What is the best immediate care?",
        "Stay with him, encourage coughing, and be ready to activate EMS if breathing worsens",
        [
            "Deliver abdominal thrusts immediately",
            "Start CPR compressions in case his pulse is weak",
            "Lay him flat and begin rescue breaths",
        ],
        "A strong cough with air movement suggests mild airway obstruction. Abdominal thrusts are for "
        "severe obstruction when cough is ineffective. CPR is indicated for unresponsiveness and "
        "abnormal breathing, not for effective coughing.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "When opening the airway for child CPR and significant trauma is not suspected, which "
        "maneuver is standard?",
        "Head tilt-chin lift",
        [
            "Jaw thrust with deliberate maximal neck hyperextension",
            "Placement of a rolled towel under the neck to flex the spine",
            "Finger sweep of the oropharynx before every ventilation",
        ],
        "Head tilt-chin lift opens the airway in most medical arrests. Routine hyperextension is not "
        "needed and may be harmful if spine injury is possible. Blind finger sweeps are discouraged "
        "because they can push objects deeper.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "How should rescue breaths be delivered during two-rescuer child CPR?",
        "Each breath over about one second until visible chest rise, without excessive volume",
        [
            "Forceful breaths until the stomach is fully distended",
            "Very short puffs with no attempt to see chest rise",
            "Breaths lasting at least five seconds each",
        ],
        "Gentle ventilations that produce chest rise limit gastric inflation. Forceful breaths "
        "inflate the stomach and reduce effective ventilation. Prolonged breaths interrupt "
        "compressions unnecessarily.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "After EMS has been activated, an unresponsive child is not breathing normally and has no "
        "pulse. What should a trained lone rescuer do next?",
        "Begin CPR, starting with chest compressions in most lay BLS programs",
        [
            "Wait for EMS on scene before starting any compressions",
            "Give two minutes of rescue breaths before any compressions",
            "Place the child in a seated position and observe breathing",
        ],
        "Immediate CPR supports circulation and oxygen delivery until advanced care arrives. Waiting "
        "for EMS without compressions sacrifices perfusion. Breath-only care without compressions does "
        "not treat pulseless arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "For most child victims during BLS CPR, what compression depth is recommended?",
        "At least one third of the anterior-posterior chest diameter, or about 2 inches (5 cm)",
        [
            "Exactly 1 inch (2.5 cm) regardless of child size",
            "At least 3 inches (7.5 cm) for every child under 12",
            "Depth does not matter if the compression rate is fast enough",
        ],
        "Adequate depth generates blood flow while limiting injury from excessive force. One inch is "
        "too shallow for most children. A fixed deep depth without regard to body size is not "
        "recommended.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-child",
        "During a pulse check on an unresponsive child, which sites are appropriate?",
        "Carotid or femoral pulse, felt for no more than 10 seconds",
        [
            "Radial pulse at the wrist for up to two minutes",
            "Apical pulse only through clothing without exposing the chest",
            "No pulse assessment is performed in pediatric BLS",
        ],
        "Central pulses are easier to detect in children with poor perfusion. Brief checks limit "
        "interruption of compressions. A prolonged radial check can falsely suggest perfusion when "
        "central pulses are absent.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "An unresponsive child has only occasional gasping breaths. How should you treat this "
        "pattern?",
        "Recognize it as abnormal breathing and provide CPR if no pulse is detected",
        [
            "Consider gasping normal breathing and withhold CPR",
            "Give supplemental oxygen only without compressions",
            "Perform abdominal thrusts before checking pulse",
        ],
        "Agonal gasps are not effective ventilation and may occur during cardiac arrest. Treating "
        "gasps as normal breathing delays CPR. Abdominal thrusts address foreign-body obstruction, "
        "not primary gasping in arrest.",
        _REF,
        "beginner",
    ),
    # --- intermediate (18) ---
    fact(
        "cpr-child",
        "Two trained rescuers are managing cardiac arrest in a 6-year-old after EMS activation. "
        "What compression-to-ventilation ratio should they use?",
        "15 compressions to 2 ventilations",
        [
            "30 compressions to 2 ventilations",
            "5 compressions to 1 ventilation",
            "Continuous compressions with breaths every 30 seconds only",
        ],
        "Two-rescuer pediatric BLS uses 15:2 so ventilations can be given more frequently while one "
        "rescuer focuses on compressions. The 30:2 ratio applies to single-rescuer CPR. The 5:1 "
        "ratio is not current AHA pediatric BLS.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "How should ventilations be delivered during child CPR to balance oxygenation and "
        "compression time?",
        "Breaths just large enough for visible chest rise, delivered in about one second each",
        [
            "Large breaths held for five seconds to maximize oxygen",
            "Tiny breaths with no visible chest movement",
            "Breaths only after every fifth compression cycle regardless of chest rise",
        ],
        "Visible chest rise indicates adequate tidal volume without overpressurizing the stomach. "
        "Five-second breaths excessively interrupt compressions. Breaths without chest rise do not "
        "provide effective ventilation.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A child collapses suddenly while running on a sports field and is unresponsive. What should "
        "the lone rescuer do about EMS activation?",
        "Call EMS and send for an AED immediately because witnessed collapse may be cardiac",
        [
            "Complete five minutes of CPR before any call for help",
            "Defer activation until a pulse check lasts two full minutes",
            "Ask bystanders to wait until the child wakes up before calling",
        ],
        "Witnessed sudden collapse in a child may represent a primary cardiac event where early "
        "defibrillation matters. Delaying EMS activation reduces the chance of timely AED use. CPR "
        "should not replace prompt emergency activation in this scenario.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "When should rescuers reassess pulse and rhythm during ongoing child CPR in the out-of-"
        "hospital setting?",
        "About every two minutes or when the AED prompts a rhythm check",
        [
            "Only once at the beginning of the arrest",
            "Every 15 seconds between every compression",
            "After ROSC has been confirmed by EMS only",
        ],
        "Periodic reassessment aligns with two-minute CPR cycles and AED analysis intervals. "
        "Checking every 15 seconds causes harmful compression interruptions. A single initial check "
        "misses changes that affect care.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "Which action best limits harmful pauses during child CPR when an AED is used?",
        "Resume compressions immediately after shock delivery or when no shock is advised",
        [
            "Stop compressions for two minutes after every AED prompt to rest",
            "Remove AED pads after the first shock and continue CPR without the device",
            "Wait for the child to move before resuming compressions after analysis",
        ],
        "Minimizing post-shock pause preserves coronary perfusion pressure. Extended rest periods "
        "after prompts are not recommended. AED pads should remain in place for continued analysis "
        "during resuscitation.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A child becomes unresponsive while choking on a hot dog. After lowering the child safely to "
        "the ground, what BLS sequence is appropriate?",
        "Begin CPR with compressions and look in the mouth for a visible object before breaths",
        [
            "Continue abdominal thrusts on an unresponsive patient",
            "Give rescue breaths repeatedly without compressions",
            "Perform blind finger sweeps after every compression",
        ],
        "Unresponsive choking victims receive CPR; compressions may dislodge the object. Abdominal "
        "thrusts are for conscious severe obstruction. Blind finger sweeps can push material deeper "
        "and are not recommended.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "When pediatric AED pads or a dose-attenuating system is available for a child in arrest, "
        "how should rescuers use it?",
        "Attach pediatric equipment per manufacturer instructions and follow AED prompts",
        [
            "Withhold the AED until the child reaches adult size",
            "Use adult energy without pediatric pads in every case",
            "Place both pads on the abdomen because the chest is small",
        ],
        "Pediatric pads or attenuators deliver appropriate energy for smaller patients. Withholding "
        "defibrillation arbitrarily delays care. Abdominal pad placement does not treat ventricular "
        "fibrillation effectively.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "Is compression-only CPR recommended for a lay rescuer who is trained and willing to give "
        "rescue breaths to a child in cardiac arrest?",
        "No; ventilations should be included when the rescuer can provide them safely",
        [
            "Yes; breaths are never indicated below age 18",
            "Yes; compressions alone are always preferred for children",
            "Only if two rescuers are present may breaths be considered",
        ],
        "Pediatric arrests are often hypoxic in origin, so ventilations are important when feasible. "
        "Compression-only CPR is not the preferred lay approach for children who need full BLS. "
        "Single rescuers still use 30:2 with breaths when able.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "During two-rescuer child CPR, how should rescuers organize roles?",
        "One rescuer performs compressions while the other gives ventilations at a 15:2 ratio",
        [
            "Both rescuers compress opposite sides of the chest simultaneously at 30:2",
            "One rescuer gives breaths only while the other waits without compressing",
            "Rescuers alternate breaths but nobody performs compressions until EMS arrives",
        ],
        "Dedicated roles maintain compression quality and timely ventilations. Simultaneous dual "
        "compressions are not standard BLS. Breath-only care without compressions does not treat "
        "pulseless arrest.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "What is required for adequate chest recoil between compressions on a child?",
        "Allow the chest to return fully without leaning on it between pushes",
        [
            "Keep downward pressure on the sternum between compressions",
            "Compress only the upper ribs without sternal contact",
            "Use partial recoil to save energy during prolonged CPR",
        ],
        "Full recoil permits cardiac filling during diastole. Leaning on the chest between compressions "
        "is a common error that reduces perfusion. Partial recoil is not high-quality CPR.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A lone rescuer without a phone has been performing child CPR for about two minutes. EMS "
        "has not yet been contacted. What should the rescuer do next?",
        "Leave briefly to activate EMS and obtain an AED if possible, then return to the child",
        [
            "Continue CPR indefinitely without ever leaving to call for help",
            "Stop CPR entirely once two minutes have elapsed",
            "Transport the child in a private vehicle without calling EMS",
        ],
        "After about two minutes of lone-rescuer CPR, activation and AED retrieval become priorities. "
        "Never activating EMS abandons the emergency response link. Stopping CPR at two minutes "
        "without a plan for help is inappropriate.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "When should a rescuer switch to adult compression depth guidelines for a pediatric patient?",
        "When the child is large enough that adult technique is appropriate, often after puberty",
        [
            "For every child older than one year regardless of size",
            "Only when three rescuers are present",
            "Whenever an AED is attached, regardless of patient size",
        ],
        "AHA bases technique on victim size rather than age alone. One year of age alone does not "
        "mandate adult depth. AED attachment does not change compression depth targets.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A conscious child with severe choking cannot speak and has a weak ineffective cough. What "
        "is appropriate BLS care?",
        "Abdominal thrusts appropriate to the child's size until relief or unresponsiveness",
        [
            "Encourage coughing only because any cough means mild obstruction",
            "Begin CPR compressions immediately while the child is still standing",
            "Deliver back blows only until the child loses consciousness",
        ],
        "Severe obstruction requires abdominal thrusts sized to the child per AHA BLS. A weak cough "
        "indicates ineffective air exchange, not mild obstruction. CPR compressions are for unresponsive "
        "victims, not conscious severe choking.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "Which patients are generally managed with child BLS compression and ventilation guidelines?",
        "From about one year of age until puberty or until adult size is reached",
        [
            "Only neonates under one month of age",
            "All patients from birth through 21 years without exception",
            "Only children who weigh less than 10 pounds",
        ],
        "Child guidelines apply to pediatric victims who are not infants and not adult-sized. Neonates "
        "follow infant BLS. Weight alone without age and size context does not define the algorithm.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "After return of spontaneous circulation in a child without suspected spine injury, what "
        "position supports the airway while awaiting EMS?",
        "Recovery position on the side with continued monitoring of breathing and pulse",
        [
            "Flat supine with head fully extended backward",
            "Prone position with face buried in a pillow",
            "Sitting upright while unattended in another room",
        ],
        "The recovery position helps maintain airway patency in a breathing patient. Maximal "
        "hyperextension is not routine post-ROSC care. Unmonitored positioning risks recurrent "
        "compromise.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "How deep should compressions be for a thin 9-year-old during BLS CPR?",
        "About one third of the chest's front-to-back diameter, roughly 2 inches (5 cm)",
        [
            "Barely indenting the skin without sternal movement",
            "At least 4 inches (10 cm) for every pediatric patient",
            "Only deep enough to hear a click from the ribs each time",
        ],
        "One-third AP diameter balances perfusion and injury risk. Barely visible indentation is too "
        "shallow. A fixed 4-inch depth may be excessive for a small child.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "During child CPR, when should rescuers switch the person performing compressions?",
        "About every two minutes or sooner if compression quality falls",
        [
            "Only after EMS takes over on arrival",
            "Never switch roles to avoid confusion",
            "Every 30 seconds regardless of fatigue",
        ],
        "Compressor switching limits fatigue-related shallow compressions. Waiting only for EMS may "
        "allow poor quality for many cycles. Switching every 30 seconds is unnecessarily disruptive.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A bystander is unsure whether a toddler or a small school-age child needs infant versus "
        "child compressions. Which factor matters most in BLS training?",
        "Victim size and developmental stage per local protocol, not the bystander's guess alone",
        [
            "Always use infant technique for anyone under 10 years old",
            "Always use adult technique for anyone who can walk",
            "Choose technique based on the rescuer's hand size only",
        ],
        "Algorithms distinguish infant, child, and adult victims by size and age landmarks. Applying "
        "infant technique to all under 10 is incorrect for school-age children. Rescuer hand size "
        "does not define patient category.",
        _REF,
        "intermediate",
    ),
    # --- advanced (13) ---
    fact(
        "cpr-child",
        "A 7-year-old is pulled unresponsive from a swimming pool. After safe rescue from the water, "
        "what BLS sequence is most appropriate?",
        "Activate EMS, open the airway, give rescue breaths if not breathing, and start 30:2 CPR if "
        "no pulse after a brief check",
        [
            "Dry the child completely and wait for normal breathing before any breaths",
            "Perform abdominal thrusts as the first step for every drowning victim",
            "Begin compressions only after 10 minutes of rescue breaths without pulse check",
        ],
        "Drowning arrests are often hypoxic; ventilations are emphasized early after rescue. Delaying "
        "breaths while waiting for spontaneous breathing sacrifices oxygenation. Abdominal thrusts "
        "are not the primary drowning response for unresponsive victims.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A 5-year-old has a palpable pulse of 50 per minute, lethargy, and poor skin perfusion. "
        "What is the appropriate BLS action?",
        "Begin chest compressions and provide ventilations per pediatric BLS protocol",
        [
            "Monitor only because any palpable pulse means CPR is contraindicated",
            "Give high-flow oxygen but withhold compressions until pulse is absent",
            "Wait for a second rescuer before treating bradycardia",
        ],
        "Bradycardia with signs of poor perfusion in children is treated as arrest-equivalent. A weak "
        "pulse with shock does not justify observation alone. Oxygen without compressions does not "
        "restore adequate systemic perfusion in this scenario.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "During child CPR after a diving injury, spinal motion must be minimized. How should the "
        "airway be opened for ventilations?",
        "Jaw thrust without excessive head tilt when trauma cannot be ruled out",
        [
            "Maximal head tilt with neck hyperextension every cycle",
            "Routine blind finger sweeps before each breath",
            "Flex the neck forward with a pillow under the shoulders",
        ],
        "Jaw thrust limits cervical movement while opening the airway. Maximal hyperextension may "
        "worsen spine injury. Blind finger sweeps are not recommended in BLS airway management.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "Two rescuers are performing child CPR and the compressor's depth has become inadequate. "
        "What team action best restores quality?",
        "Coach hand placement and switch compressors at the next two-minute mark if needed",
        [
            "Stop all compressions until the child moves spontaneously",
            "Switch to ventilations only until depth improves on its own",
            "Continue shallow compressions because any activity is sufficient",
        ],
        "Fatigue and poor technique reduce coronary perfusion; coaching and role switching address "
        "this. Ventilation-only care does not support pulseless arrest. Accepting shallow compressions "
        "is not high-quality CPR.",
        _HQ,
        "advanced",
    ),
    fact(
        "cpr-child",
        "Why does AHA recommend a 15:2 ratio for two-rescuer child CPR instead of 30:2?",
        "More frequent ventilations address common pediatric respiratory causes of arrest while one "
        "rescuer maintains compressions",
        [
            "15:2 reduces the number of breaths compared with 30:2",
            "30:2 is only used for adults and never for children",
            "Two rescuers should never give ventilations during pediatric arrest",
        ],
        "Fifteen compressions between breaths increase ventilation rate compared with lone 30:2. "
        "The ratio does not reduce breaths; it changes their frequency. Pediatric two-rescuer BLS "
        "still includes ventilations.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "EMS places an advanced airway in a child during ongoing resuscitation. How should "
        "ventilations be coordinated with compressions afterward?",
        "Continue compressions without pausing for breaths and give about one breath every six "
        "seconds",
        [
            "Pause compressions for five seconds before every breath",
            "Stop compressions entirely once the airway is in place",
            "Give breaths only when the compressor requests a break",
        ],
        "With an advanced airway, compressions should be continuous with asynchronous ventilations. "
        "Pausing compressions for each breath lowers perfusion pressure. Stopping compressions after "
        "airway placement abandons circulation support.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A child in cardiac arrest has no pulse, and chest compressions are in progress. When an AED "
        "arrives, what is the best integration with ongoing CPR?",
        "Apply pads with minimal pause, follow prompts, and resume compressions immediately after "
        "shock or no-shock advice",
        [
            "Remove the child from the AED area until ROSC occurs",
            "Wait until compressions have continued for 15 minutes before attaching pads",
            "Deliver shocks without clearing rescuers from the patient",
        ],
        "Rapid pad placement and immediate post-shock CPR preserve perfusion. Arbitrary delays before "
        "AED use weaken defibrillation benefit. Failing to clear the patient before shock risks "
        "rescuer injury and ineffective delivery.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "After ROSC, a 10-year-old child is breathing but remains very lethargic. What BLS-level "
        "priority applies while awaiting EMS?",
        "Maintain airway, provide oxygen if trained and available, and monitor breathing and pulse",
        [
            "Discharge the child to parents without EMS evaluation",
            "Resume CPR compressions because lethargy always means recurrent arrest",
            "Withhold oxygen even if the child appears cyanotic",
        ],
        "Post-ROSC patients need close monitoring for recurrence and support of oxygenation. "
        "Automatic return to compressions without reassessment is inappropriate. Withholding oxygen "
        "when indicated ignores post-arrest hypoxia risk.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A child with severe asthma collapses and is unresponsive with agonal gasps. Pulse is absent. "
        "How does pediatric BLS address the likely hypoxic mechanism?",
        "Provide full CPR with compressions and ventilations at the appropriate ratio for rescuer "
        "number",
        [
            "Give ventilations only because asthma means compressions are harmful",
            "Use compression-only CPR because asthma is a cardiac disease",
            "Wait for bronchodilator medication before starting any CPR",
        ],
        "Respiratory disease can lead to hypoxic arrest requiring compressions and ventilations. "
        "Breath-only care does not treat pulseless arrest. Medication delay should not postpone CPR "
        "when arrest is present.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "During prolonged child CPR in a cool outdoor environment, what adjunct supports the child "
        "beyond compressions and ventilations?",
        "Cover the child with a dry blanket after exposing the chest for compressions when possible",
        [
            "Immerse the child in cold water to prevent fever",
            "Remove all clothing and leave the child uncovered in wind",
            "Stop CPR every five minutes to warm hands only",
        ],
        "Preventing hypothermia supports resuscitation efforts in children. Cold water immersion is "
        "harmful during active CPR. Uncovered exposure increases heat loss unnecessarily.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A school-age child receives CPR, and the compressor notes the chest does not rise with "
        "rescue breaths. What is the best next step before additional breaths?",
        "Reopen the airway with head tilt-chin lift or jaw thrust if trauma is suspected and "
        "reattempt a gentle breath",
        [
            "Increase breath force until gastric distension is obvious",
            "Abandon all ventilations for the remainder of the arrest",
            "Perform blind finger sweeps between every compression",
        ],
        "Poor chest rise usually reflects airway position or seal, not insufficient force. Forceful "
        "breaths cause gastric inflation. Blind sweeps are discouraged in BLS.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "Which description best reflects chest compression fraction goals during child resuscitation?",
        "Compressing the chest for most of the resuscitation period with pauses under about 10 "
        "seconds for pulse checks and defibrillation",
        [
            "Pausing compressions for at least 30 seconds each minute for team discussion",
            "Limiting compressions to less than 20 percent of total resuscitation time",
            "Stopping compressions whenever the rescuer feels tired without switching roles",
        ],
        "High compression fraction maintains coronary perfusion pressure. Thirty-second routine pauses "
        "are harmful. Deliberately limiting compression time contradicts high-quality CPR principles.",
        _HQ,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A child has a suspected opioid exposure and is unresponsive with absent pulse after a brief "
        "check. EMS is activated. What BLS care remains appropriate for the lay rescuer?",
        "High-quality CPR with ventilations if trained, and naloxone per local protocol if available",
        [
            "Naloxone only without compressions until the child wakes up",
            "Rescue breaths only because opioids never cause cardiac arrest in children",
            "Delay CPR until toxicology confirms the substance",
        ],
        "Opioids can cause respiratory arrest progressing to pulseless arrest; CPR and ventilation "
        "support circulation and oxygenation. Naloxone does not replace CPR when pulse is absent. "
        "Waiting for toxicology delays life-saving compressions.",
        _REF,
        "advanced",
    ),
]
