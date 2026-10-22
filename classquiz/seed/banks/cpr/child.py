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
        "In child BLS, what ratio of compressions to ventilations should a lone rescuer use?",
        "30 compressions followed by 2 ventilations (30:2) for child CPR",
        [
            "15 compressions followed by 2 ventilations when two rescuers are present",
            "5 compressions followed by 1 ventilation to shorten pauses between breaths",
            "Continuous compressions with no ventilations until EMS places an airway",
        ],
        "AHA pediatric BLS uses 30:2 when only one rescuer is available. Fifteen-to-two is reserved "
        "for two-rescuer child CPR so one person can maintain compressions. Compression-only care "
        "without breaths omits needed oxygenation in many hypoxic pediatric arrests.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "In child BLS, what chest compression rate do rescuers deliver for high-quality CPR?",
        "100 to 120 compressions per minute",
        [
            "90 to 100 compressions per minute",
            "120 to 140 compressions per minute",
            "140 to 160 compressions per minute",
        ],
        "Pediatric compressions follow the same rate target as adult BLS. Rates below 100 often fail "
        "to maintain coronary and cerebral perfusion. Very fast rates usually sacrifice depth and "
        "full recoil, reducing effectiveness.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-child",
        "Where should rescuers place the heel of one hand when performing chest compressions on a child?",
        "On the lower half of the sternum in the center of the chest",
        [
            "Directly over the xiphoid process at the distal tip of the sternum",
            "On the upper abdomen just below the costal margin",
            "On the left lateral chest wall over the cardiac apex",
        ],
        "Hand placement on the lower half of the sternum directs force through the heart. Compressing "
        "the xiphoid, epigastrium, or lateral chest is a frequent error that reduces effectiveness "
        "and increases injury risk during pediatric BLS.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "Why does AHA advise rescue breaths during child CPR when the rescuer can give them safely?",
        "Pediatric arrests begin with respiratory failure, so early breaths matter",
        [
            "Chest compressions are unnecessary once two effective rescue breaths are given",
            "Rescue breaths are optional when the child had a witnessed collapse on dry land",
            "Chest compressions without breaths are the preferred lay approach for children",
        ],
        "Hypoxia and respiratory failure are common pathways to pediatric cardiac arrest. "
        "Compressions remain essential, but ventilations address the underlying problem in many cases. "
        "Compression-only CPR is not preferred when full BLS ventilations can be delivered safely.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "You confirm scene safety at a playground where a child lies motionless. What is the first "
        "pediatric BLS action you should take?",
        "Check responsiveness by tapping the shoulders and shouting for a response",
        [
            "Begin chest compressions immediately without checking for responsiveness",
            "Search the area for an AED before touching or assessing the child",
            "Shake the torso repeatedly before checking responsiveness or calling for help",
        ],
        "Recognition of unresponsiveness triggers emergency activation and assessment of breathing "
        "and pulse. Starting compressions on a responsive child would be inappropriate. Scene safety "
        "and responsiveness checks precede device retrieval.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "At what point should an AED be attached during suspected cardiac arrest in a child?",
        "As soon as the device is available while high-quality CPR continues",
        [
            "After at least 10 minutes of uninterrupted chest compressions are finished",
            "When the child is older than 12 years and adult pads are the sole option",
            "After EMS arrives and takes over compressions exclusively at the bedside",
        ],
        "Early defibrillation improves survival in shockable rhythms. Delaying pad placement for an "
        "arbitrary time wastes the defibrillation link in the Chain of Survival. Children can "
        "benefit from AED use with appropriate pediatric pad systems when indicated.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "In child CPR, which description best matches high-quality chest compressions?",
        "Hard, fast compressions with full recoil and few interruptions",
        [
            "Soft compressions with the rescuer leaning on the chest between each push",
            "Fast compressions with no attention to depth, rate, or chest recoil quality",
            "Deep compressions held down without allowing the chest to return between pushes",
        ],
        "Depth, rate, recoil, and limited interruptions define high-quality CPR. Leaning on the chest "
        "blocks recoil and reduces perfusion. Holding compressions without release prevents diastolic "
        "filling of the heart.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-child",
        "A conscious 8-year-old begins choking while eating but coughs forcefully and can still speak "
        "in short sentences. What is the best immediate BLS care?",
        "Stay with the child, encourage coughing, and call EMS if the cough weakens",
        [
            "Deliver abdominal thrusts because a cough can signal severe obstruction",
            "Start CPR chest compressions in case the pulse is weak despite effective speech",
            "Lay the child flat and begin rescue breaths before assessing cough effectiveness",
        ],
        "A strong cough with air movement suggests mild airway obstruction. Abdominal thrusts are for "
        "severe obstruction when cough is ineffective. CPR is indicated for unresponsiveness and "
        "abnormal breathing, not for effective coughing with good air exchange.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "For a child in arrest without suspected trauma, which airway-opening maneuver should "
        "rescuers use?",
        "Head tilt-chin lift to open the airway without routine finger sweeps",
        [
            "Jaw thrust with slight head extension when no trauma is suspected",
            "Rolled towel under the neck to flex the spine before each ventilation",
            "Finger sweep of the mouth before each breath when no object is seen",
        ],
        "Head tilt-chin lift opens the airway in most medical pediatric arrests. Routine "
        "hyperextension is not needed and may be harmful if spine injury is possible. Blind finger "
        "sweeps are discouraged because they can push objects deeper.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "How should a rescuer deliver rescue breaths during two-rescuer child CPR at a 15:2 ratio?",
        "Give each breath over about 1 second until visible chest rise is confirmed",
        [
            "Deliver forceful breaths until the stomach distends after each 15:2 cycle",
            "Give very short puffs with no attempt to confirm visible chest rise occurs",
            "Provide breaths lasting at least 5 seconds each to maximize oxygen delivery",
        ],
        "Gentle ventilations that produce chest rise limit gastric inflation. Forceful breaths "
        "inflate the stomach and reduce effective ventilation. Prolonged breaths unnecessarily "
        "interrupt compressions.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "A trained lone rescuer finds an unresponsive child with no breathing and no pulse after EMS "
        "is called. What comes next?",
        "Begin CPR, starting with chest compressions per the CAB sequence",
        [
            "Wait on scene for EMS arrival before starting chest compressions",
            "Give two minutes of rescue breaths alone before compressions are started",
            "Place the child in a seated position and observe breathing without compressions",
        ],
        "Immediate CPR supports circulation and oxygen delivery until advanced care arrives. Waiting "
        "for EMS without compressions sacrifices perfusion. Breath-only care without compressions does "
        "not treat pulseless arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "How deep should compressions go for most child victims during BLS CPR?",
        "At least one third of the anterior-posterior chest diameter (about 2 inches)",
        [
            "Exactly 1 inch (2.5 cm) as the standard depth target for child CPR",
            "At least 3 inches (7.5 cm) for victims under 12 years even when smaller in size",
            "Visible chest motion without a specified minimum depth target",
        ],
        "Adequate depth generates blood flow while limiting injury from excessive force. One inch is "
        "too shallow for most children. A fixed deep depth without regard to body size is not "
        "recommended per AHA pediatric BLS guidance.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-child",
        "Where and for how long should a rescuer check for a pulse in an unresponsive child?",
        "Feel the carotid or femoral pulse for no more than about 10 seconds",
        [
            "Palpate the radial pulse at the wrist for up to two minutes before starting CPR",
            "Auscultate the apical pulse through clothing without exposing the chest",
            "Rely on agonal gasps alone and omit the pulse check before compressions",
        ],
        "Central pulses are easier to detect in children with poor perfusion. Brief checks limit "
        "harmful interruption of compressions. A prolonged radial check can falsely suggest perfusion "
        "when central pulses are absent.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-child",
        "An unresponsive child has occasional gasping breaths and no effective ventilation. What "
        "should rescuers do?",
        "Treat gasping as abnormal breathing and start CPR when no pulse is found",
        [
            "Consider gasping normal breathing and withhold CPR until EMS confirms arrest",
            "Provide supplemental oxygen by mask without chest compressions",
            "Perform abdominal thrusts before the pulse check or compressions",
        ],
        "Agonal gasps are not effective ventilation and may occur during cardiac arrest. Treating "
        "gasps as normal breathing delays CPR. Abdominal thrusts address foreign-body obstruction, "
        "not primary gasping in pulseless arrest.",
        _REF,
        "beginner",
    ),
    # --- intermediate (18) ---
    fact(
        "cpr-child",
        "Two trained rescuers are managing cardiac arrest in a 6-year-old after EMS activation. Which "
        "ratio should they use?",
        "15 compressions followed by 2 ventilations (15:2) for two rescuers",
        [
            "30 compressions followed by 2 ventilations when two trained rescuers are present",
            "5 compressions followed by 1 ventilation to minimize compression interruptions",
            "Continuous compressions with rescue breaths given every 30 seconds",
        ],
        "Two-rescuer pediatric BLS uses 15:2 so ventilations can be given more frequently while one "
        "rescuer focuses on compressions. The 30:2 ratio applies to single-rescuer CPR. The 5:1 "
        "ratio is not current AHA pediatric BLS.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A rescue breath in a child produces no visible chest rise. What should the rescuer do before "
        "the next breath?",
        "Reposition the airway with head tilt-chin lift and retry a one-second breath",
        [
            "Deliver the next breath with force over 5 seconds until resistance is felt",
            "End further ventilations for the arrest and continue chest compressions",
            "Perform blind finger sweeps of the mouth before every subsequent rescue breath",
        ],
        "Inadequate chest rise usually means the airway is not open or the breath volume was wrong. "
        "Repositioning and a one-second breath limits gastric inflation. Forceful prolonged breaths "
        "and blind sweeps are discouraged in AHA pediatric BLS.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A child collapses suddenly while running on a sports field and is unresponsive. What should "
        "the lone rescuer do about EMS activation and AED retrieval?",
        "Activate EMS and send for an AED for a suspected cardiac arrest",
        [
            "Complete five minutes of CPR before the call for help or the AED retrieval",
            "Defer EMS activation until a pulse check has lasted two full minutes",
            "Ask bystanders to wait until the child wakes before calling emergency services",
        ],
        "Witnessed sudden collapse in a child may represent a primary cardiac event where early "
        "defibrillation matters. Delaying EMS activation reduces the chance of timely AED use. CPR "
        "should not replace prompt emergency activation in this scenario.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "When should rescuers reassess pulse and rhythm during ongoing out-of-hospital child CPR?",
        "About every two minutes or whenever the AED prompts a rhythm analysis",
        [
            "Once at the beginning of the arrest before further compressions",
            "Every 15 seconds between individual compressions throughout the resuscitation",
            "After return of spontaneous circulation has been confirmed by EMS",
        ],
        "Periodic reassessment aligns with two-minute CPR cycles and AED analysis intervals. "
        "Checking every 15 seconds causes harmful compression interruptions. A single initial check "
        "misses rhythm changes that affect care.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "How should a team limit harmful pauses when an AED is integrated into child CPR?",
        "Resume chest compressions right after a shock or when no shock is advised",
        [
            "Stop compressions for two minutes after every AED voice prompt to rest the team",
            "Remove AED pads after the first shock and continue CPR without further analysis",
            "Wait until the child moves spontaneously before resuming compressions",
        ],
        "Minimizing post-shock pause preserves coronary perfusion pressure. Extended rest periods "
        "after AED prompts are not recommended. AED pads should remain in place for continued "
        "analysis during resuscitation.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A child becomes unresponsive while choking on a hot dog. After lowering the child safely to "
        "the ground, what BLS sequence is appropriate?",
        "Start CPR with compressions and look for a visible object before breaths",
        [
            "Continue abdominal thrusts on the unresponsive child until EMS arrives on scene",
            "Give repeated rescue breaths without chest compressions until the airway clears",
            "Perform blind finger sweeps after every compression cycle throughout CPR",
        ],
        "Unresponsive choking victims receive CPR; compressions may dislodge the object. Abdominal "
        "thrusts are for conscious severe obstruction. Blind finger sweeps can push material deeper "
        "and are not recommended.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "Pediatric AED pads or a dose-attenuating system is available for a child in cardiac arrest. "
        "How should rescuers use the device?",
        "Attach pediatric pads or an attenuator per instructions and follow AED prompts",
        [
            "Withhold defibrillation until the child reaches adult size in shockable rhythms",
            "Use full adult AED energy when pediatric pads or an attenuator are unavailable",
            "Place both AED pads on the abdomen because the anterior chest is too small",
        ],
        "Pediatric pads or attenuators deliver appropriate energy for smaller patients. Withholding "
        "defibrillation arbitrarily delays care. Abdominal pad placement does not treat ventricular "
        "fibrillation effectively.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "Should a lay rescuer who is trained and willing to give rescue breaths use compression-only "
        "CPR on a child in cardiac arrest?",
        "No; include ventilations in 30:2 CPR when breaths can be delivered safely",
        [
            "Yes; rescue breaths are not indicated for patients below 18 years of age",
            "Yes; compressions without breaths are preferred over ventilated CPR for children",
            "Breaths may be given when two trained rescuers are present at the scene",
        ],
        "Pediatric arrests are often hypoxic in origin, so ventilations are important when feasible. "
        "Compression-only CPR is not the preferred lay approach for children who need full BLS. "
        "Single rescuers still use 30:2 with breaths when able.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "During two-rescuer child CPR, how should rescuers divide tasks to maintain quality?",
        "One rescuer compresses while the other gives ventilations at a 15:2 ratio",
        [
            "Both rescuers compress opposite sides of the chest at the same time using 30:2",
            "One rescuer gives breaths while the other waits without compressing",
            "Rescuers alternate rescue breaths and delay compressions until EMS arrives",
        ],
        "Dedicated roles maintain compression quality and timely ventilations. Simultaneous dual "
        "compressions are not standard BLS. Breath-only care without compressions does not treat "
        "pulseless arrest.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A rescuer performing child CPR keeps partial weight on the sternum between compressions. "
        "Why does incomplete chest recoil reduce perfusion?",
        "Leaning on the chest prevents full diastolic filling before the next push",
        [
            "Leaning on the chest steadies hand placement and is encouraged for child CPR",
            "Incomplete recoil mainly lowers compression rate without changing filling",
            "Partial recoil is acceptable during prolonged CPR to conserve rescuer energy",
        ],
        "Full recoil permits cardiac filling during diastole so the next compression can perfuse the "
        "brain and myocardium. Leaning between compressions is a common high-quality CPR error. "
        "Partial recoil is not acceptable when effective BLS is the goal.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A lone rescuer without a phone has performed child CPR for about two minutes and EMS has not "
        "yet been contacted. What should the rescuer do next?",
        "Leave the child briefly to activate EMS and get an AED, then return to CPR",
        [
            "Continue CPR at the scene without leaving to activate emergency response",
            "Stop CPR at two minutes and wait for bystanders to call emergency services",
            "Transport the child in a private vehicle to the hospital without activating EMS",
        ],
        "After about two minutes of lone-rescuer CPR, activation and AED retrieval become priorities. "
        "Never activating EMS abandons the emergency response link. Stopping CPR at two minutes "
        "without a plan for help is inappropriate.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A tall adolescent looks adult-sized but is still managed with pediatric BLS in your course. "
        "When should rescuers use adult compression depth and hand-placement targets instead?",
        "When the victim is large enough for adult BLS technique after puberty",
        [
            "For a child older than one year even when the victim appears small for age",
            "When three trained rescuers are present and rotating compressor roles",
            "Whenever an AED is attached, using adult depth targets on all pediatric victims",
        ],
        "AHA pediatric BLS selects technique from victim size rather than age alone. One year of age "
        "does not automatically mandate adult depth. Attaching an AED does not change compression "
        "depth or hand-placement targets.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A conscious 7-year-old cannot speak, has a silent weak cough, and shows signs of severe "
        "airway obstruction. What is the best immediate BLS action?",
        "Give abdominal thrusts sized to the child and repeat until relief or collapse",
        [
            "Encourage forceful coughing and observe at the bedside without abdominal thrusts",
            "Begin chest compressions while the child remains conscious and upright",
            "Deliver back blows until the child loses consciousness, then start compressions",
        ],
        "Severe obstruction with ineffective cough requires active relief maneuvers, not observation "
        "alone. Abdominal thrusts are appropriate for a child with severe choking per AHA BLS. CPR "
        "compressions begin when the victim becomes unresponsive, not while still conscious.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "Which description best defines who should receive child BLS compression and ventilation "
        "guidelines during training and real events?",
        "Victims from about one year of age until puberty or adult body size is reached",
        [
            "Neonates under one month of age even when they appear school-age in size",
            "Patients from birth through 21 years of age without size assessment",
            "Children who weigh under 10 pounds even when they are clearly older than infancy",
        ],
        "Child algorithms bridge infant and adult BLS for victims who are not infants and not "
        "adult-sized. Neonates and young infants follow infant BLS. Weight alone without age and "
        "size context does not define the correct compression technique.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "After return of spontaneous circulation, a breathing child has no suspected spine injury and "
        "EMS is en route. What position and monitoring best support the airway?",
        "Place the child in a recovery position on the side and keep monitoring them",
        [
            "Keep the child flat supine with the head extended backward until EMS arrives",
            "Keep the child flat supine with the chin forced fully upward toward the ceiling",
            "Prop the child upright in a car seat without ongoing pulse or breathing checks",
        ],
        "The recovery position helps maintain airway patency in a breathing post-arrest patient. "
        "Routine maximal hyperextension is not indicated after ROSC without trauma concerns. "
        "Unmonitored positioning risks recurrent airway compromise or arrest.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "During CPR on a thin 9-year-old, feedback shows compressions are fast but barely indent the "
        "sternum. What depth target should the team prioritize?",
        "At least one third of the anterior-posterior chest diameter, about 2 inches",
        [
            "Shallow sternal indentation without reaching one third AP depth on each push",
            "At least 4 inches (10 cm) as the depth target for all pediatric CPR",
            "Deep enough to produce an audible rib click on every compression cycle",
        ],
        "Adequate depth generates perfusion while limiting injury from excessive force. Barely visible "
        "indentation is too shallow for most children. A fixed 4-inch depth may be excessive for a "
        "thin school-age victim.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "Two rescuers have provided high-quality child CPR for nearly two minutes and the compressor "
        "reports arm fatigue with slowing rate. What should the team do next?",
        "Switch compressors at two minutes or sooner if rate, depth, or recoil falls",
        [
            "Keep the same compressor until EMS arrives even if quality is declining",
            "Keep one compressor for the entire arrest without rotating roles",
            "Rotate compressors every 30 seconds even when rate and depth still meet targets",
        ],
        "Timely compressor switching limits fatigue-related shallow or slow compressions. Waiting only "
        "for EMS may allow poor quality for many two-minute cycles. Switching every 30 seconds is "
        "unnecessarily disruptive without quality benefit.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-child",
        "A rescuer finds an unresponsive victim and is unsure whether to use infant or child "
        "compressions on a small school-age patient. Which factor should drive the algorithm choice?",
        "Victim size and developmental stage using AHA age and size landmarks",
        [
            "Use infant compressions for a victim under 10 years of age without assessment",
            "Use adult compressions for a victim who can walk independently",
            "Choose infant versus child technique based on the rescuer's hand size alone",
        ],
        "Pediatric BLS distinguishes infant, child, and adult victims using size and age landmarks. "
        "Applying infant technique to all children under 10 is incorrect for many school-age victims. "
        "Rescuer hand size does not define which patient category applies.",
        _REF,
        "intermediate",
    ),
    # --- advanced (13) ---
    fact(
        "cpr-child",
        "A 7-year-old is pulled unresponsive from a swimming pool. After safe rescue and drying the "
        "face, the child is not breathing normally. What BLS sequence is most appropriate?",
        "Activate EMS, give breaths, then start 30:2 CPR if no pulse is found",
        [
            "Dry the body fully and wait for spontaneous breathing before giving breaths",
            "Perform abdominal thrusts before opening the airway for a person on land",
            "Give rescue breaths for 10 minutes before a pulse check or compressions",
        ],
        "Drowning arrests are often hypoxic, so ventilations are emphasized early after water rescue. "
        "Waiting for spontaneous breathing before assisting breaths sacrifices needed oxygenation. "
        "Abdominal thrusts are not the primary response for an unresponsive drowning victim.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A 5-year-old is lethargic with cold mottled skin, a palpable pulse of 50 per minute, and "
        "signs of poor perfusion. What is the appropriate BLS action?",
        "Begin compressions and ventilations per the pediatric bradycardia protocol",
        [
            "Monitor at the bedside because a palpable pulse excludes chest compressions",
            "Provide high-flow oxygen but withhold compressions until the pulse is absent",
            "Wait for a second rescuer to arrive before starting treatment for bradycardia",
        ],
        "Bradycardia with poor perfusion in children is treated as arrest-equivalent in BLS. A weak "
        "pulse with shock does not justify observation alone. Supplemental oxygen without compressions "
        "does not restore adequate systemic perfusion in this presentation.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "During child CPR after a suspected diving injury, cervical motion must be limited. How should "
        "rescuers open the airway for rescue breaths?",
        "Use a jaw thrust with minimal head tilt when spine injury cannot be ruled out",
        [
            "Apply full head tilt with neck hyperextension before each rescue breath cycle",
            "Perform routine blind finger sweeps of the mouth before each ventilation attempt",
            "Flex the neck forward and place a pillow under the shoulders to open the airway",
        ],
        "Jaw thrust opens the airway while limiting cervical movement when trauma is possible. Maximal "
        "hyperextension may worsen spine injury. Blind finger sweeps are discouraged in BLS airway "
        "management because they can push objects deeper.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "During two-rescuer child CPR, real-time feedback shows compression rate drifting above "
        "130 per minute while depth remains adequate. What team action best restores quality?",
        "Coach the compressor to hold 100 to 120 per minute and switch roles",
        [
            "Accept the faster rate because speed compensates for minor depth loss",
            "Stop compressions until the child moves spontaneously and the rate normalizes",
            "Switch to ventilations for two minutes while the compressor rests",
        ],
        "Pediatric compressions should stay within 100 to 120 per minute with adequate depth and "
        "recoil. Very fast rates often sacrifice depth and full recoil. Ventilation-only care does "
        "not treat pulseless arrest while waiting for rate to improve.",
        _HQ,
        "advanced",
    ),
    fact(
        "cpr-child",
        "An instructor asks why two-rescuer child CPR uses 15:2 instead of the lone rescuer 30:2 "
        "ratio. Which rationale best matches AHA pediatric BLS?",
        "15:2 gives more ventilations while one rescuer keeps compressing",
        [
            "15:2 reduces the total number of rescue breaths compared with 30:2",
            "30:2 is reserved for adults and is wrong for a pediatric arrest",
            "Two rescuers should compress and withhold ventilations during child CPR",
        ],
        "Shorter compression runs between breaths increase ventilation frequency compared with lone "
        "30:2, which matters when respiratory failure contributes to arrest. The ratio changes breath "
        "timing, not elimination of ventilations. Pediatric two-rescuer BLS still includes rescue breaths.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "EMS places an advanced airway in a child during resuscitation. How should ventilations be "
        "coordinated with compressions afterward?",
        "Continue compressions and deliver about one breath every six seconds",
        [
            "Pause compressions for five seconds before each breath through the tube",
            "Stop chest compressions once the advanced airway is successfully in place",
            "Give rescue breaths when the compressor asks for a pause in compressions",
        ],
        "After advanced airway placement, compressions should be continuous with asynchronous "
        "ventilations. Pausing compressions for each breath lowers coronary perfusion pressure. "
        "Stopping compressions when the airway is placed abandons circulation support.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "During ongoing child CPR, a bystander arrives with an AED while the lone compressor is "
        "mid-cycle. What division of tasks best limits compression pauses?",
        "The second rescuer attaches AED pads while compressions continue",
        [
            "Stop compressions for three minutes so the AED can be unpacked and applied",
            "Move the child to another room until circulation returns on its own",
            "Deliver shocks without clearing rescuers from contact with the patient",
        ],
        "Continuous compressions during pad preparation minimize perfusion gaps before rhythm analysis. "
        "Extended planned pauses for equipment setup harm coronary perfusion pressure. Rescuers must "
        "clear the patient during shock delivery to avoid injury and ensure effective energy transfer.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "After ROSC, a 10-year-old is breathing spontaneously but remains very lethargic and "
        "difficult to arouse while EMS is en route. What BLS priority applies?",
        "Maintain the airway, give supplemental oxygen, and monitor breathing and pulse",
        [
            "Discharge the child to the parents at the scene without EMS transport or oxygen",
            "Resume compressions immediately for lethargy without reassessing the pulse",
            "Give supplemental oxygen but stop monitoring the pulse until EMS arrives",
        ],
        "Post-ROSC patients require close monitoring for recurrent arrest and support of oxygenation. "
        "Automatic return to compressions without reassessment of pulse and breathing is inappropriate. "
        "Withholding oxygen when the child appears hypoxic ignores post-arrest respiratory risk.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A child with severe asthma collapses, becomes unresponsive, has agonal gasps, and has no "
        "palpable pulse after a 10-second check. What pediatric BLS approach addresses the likely "
        "hypoxic arrest mechanism?",
        "Provide full CPR with compressions and ventilations at the proper ratio",
        [
            "Give rescue ventilations alone because asthma makes chest compressions harmful",
            "Use chest compressions without breaths because asthma is a rhythm disorder",
            "Delay CPR until inhaled bronchodilator medication can be given",
        ],
        "Severe respiratory disease can progress to hypoxic pulseless arrest requiring compressions and "
        "ventilations together. Ventilation-only care does not treat absent perfusion when pulse is "
        "missing. Medication should not delay CPR when arrest criteria are met.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "During prolonged child CPR on a cool playground, the team has exposed the chest for "
        "compressions. What adjunct best supports the victim beyond compressions and ventilations?",
        "Cover the child with a dry blanket when possible while continuing CPR",
        [
            "Remove the shirt and leave the chest exposed to the air to cool faster",
            "Pause compressions for one minute each cycle so rescuers can warm their hands",
            "Focus on compressions and delay covering the child until EMS takes over",
        ],
        "Preventing hypothermia supports metabolic and resuscitation efforts during prolonged pediatric "
        "CPR. Leaving the chest exposed or pausing compressions to warm rescuers works against "
        "effective care in cool environments when a dry blanket can help maintain warmth.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "During two-rescuer child CPR at 15:2, the ventilation rescuer notes no chest rise despite a "
        "one-second breath attempt. What is the best next step before giving another breath?",
        "Reposition the airway with head tilt-chin lift or a jaw thrust and retry",
        [
            "Increase breath force until gastric distension shows on each ventilation",
            "Abandon all further ventilations for the remainder of the resuscitation attempt",
            "Perform blind finger sweeps of the oropharynx between every compression cycle",
        ],
        "Inadequate chest rise usually reflects airway position, obstruction, or a poor seal, not "
        "simply insufficient force. Forceful breaths promote gastric inflation and reduce effective "
        "ventilation. Blind finger sweeps are discouraged in AHA BLS airway management.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-child",
        "Which description best reflects the chest compression fraction goal during high-quality child "
        "resuscitation?",
        "Compress the chest for most of the event, keeping pauses under 10 seconds",
        [
            "Pause compressions for 30 seconds each minute to discuss roles and rest",
            "Limit active compressions to under 20 percent of the resuscitation time",
            "Stop compressions when the rescuer feels tired without switching compressors",
        ],
        "High compression fraction maintains coronary perfusion pressure throughout arrest care. "
        "Routine 30-second pauses for non-essential tasks harm outcomes. Deliberately minimizing "
        "compression time contradicts high-quality CPR principles.",
        _HQ,
        "advanced",
    ),
    fact(
        "cpr-child",
        "A child with suspected opioid exposure is unresponsive with agonal breathing and no pulse "
        "after a brief check; EMS has been activated. What care should a trained lay rescuer provide?",
        "Perform high-quality CPR with ventilations and give naloxone when available",
        [
            "Give naloxone and withhold compressions until the child is fully responsive",
            "Provide rescue breaths without compressions until toxicology confirms opioids",
            "Delay CPR until toxicology confirms which substance was ingested",
        ],
        "Opioids can cause respiratory depression progressing to pulseless arrest requiring CPR and "
        "ventilation support. Naloxone does not replace compressions when perfusion is absent. Waiting "
        "for toxicology confirmation inappropriately delays life-saving chest compressions.",
        _REF,
        "advanced",
    ),
]
