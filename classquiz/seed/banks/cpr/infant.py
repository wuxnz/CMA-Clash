# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored infant pediatric BLS question bank (AHA 2020+ aligned)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_REF = [S.AHA_WHAT_IS_CPR, S.AHA_ADULT_BLS]
_HQ = [S.AHA_WHAT_IS_CPR, S.AHA_HQ_CPR, S.AHA_ADULT_BLS]

FACTS: list[dict] = [
    # --- beginner (14) ---
    fact(
        "cpr-infant",
        "A lone rescuer is performing BLS on an infant in cardiac arrest. Which compression-to-"
        "ventilation ratio should they use?",
        "30 compressions followed by 2 ventilations",
        [
            "15 compressions followed by 2 ventilations",
            "5 compressions followed by 1 ventilation",
            "Continuous compressions without any ventilations",
        ],
        "Single-rescuer infant BLS uses 30:2. The 15:2 ratio applies when two rescuers are present. "
        "Skipping ventilations ignores the frequent respiratory cause of infant arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "What chest compression rate should rescuers deliver during infant CPR?",
        "100 to 120 compressions per minute",
        [
            "60 to 80 compressions per minute",
            "150 to 180 compressions per minute",
            "As slow as possible to protect the infant rib cage",
        ],
        "Infant compressions use the same rate target as other BLS victims. A rate of 60 to 80 is "
        "inadequate for perfusion. Excessive speed prevents full chest recoil.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "Where should two-finger compressions be placed during single-rescuer infant CPR?",
        "Lower half of the sternum, just below the nipple line",
        [
            "Upper abdomen over the stomach",
            "Directly on the xiphoid with maximal pressure",
            "Over the infant's back while the infant lies prone",
        ],
        "Sternal compressions generate blood flow; the lower half of the sternum is the standard "
        "landmark. Abdominal compression does not compress the heart effectively. Prone compressions "
        "on the back are not standard BLS.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "How should rescue breaths be given to an infant during CPR?",
        "Seal the mouth and nose and deliver a gentle breath over about one second watching for chest rise",
        [
            "Pinch the nose closed and blow only into the mouth as for an adult",
            "Deliver large breaths until the abdomen is markedly distended",
            "Blow air across the face without forming a seal",
        ],
        "Infants need a mouth-and-nose seal with modest tidal volume. Pinching the nose is an adult "
        "technique. Overventilation causes gastric inflation and reduces effective ventilation.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "During a pulse check on an unresponsive infant, which site is preferred?",
        "Brachial artery on the inside of the upper arm",
        [
            "Radial artery at the wrist as the only acceptable site",
            "Carotid pulse with heavy pressure on the neck",
            "Apical pulse through multiple layers of clothing only",
        ],
        "The brachial pulse is accessible and reliable in infants during BLS assessment. Radial pulses "
        "may be difficult to feel in infants with poor perfusion. Excessive neck pressure is "
        "unnecessary when the brachial site is available.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "You find an infant unresponsive in a crib after confirming scene safety. What should you do "
        "immediately after checking responsiveness?",
        "Shout for help and activate emergency response if others are present",
        [
            "Begin compressions without ever calling for help",
            "Leave the infant alone to search a distant building for an AED",
            "Give water by bottle to test swallowing",
        ],
        "Early activation brings EMS and equipment while assessment continues. Compressions may follow "
        "quick activation, but ignoring help entirely delays advanced care. Oral fluids are not part "
        "of arrest assessment.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "What compression depth target is appropriate for most infants during BLS CPR?",
        "About one third of the anterior-posterior chest diameter, roughly 1.5 inches (4 cm)",
        [
            "Barely visible skin indentation without sternal movement",
            "At least 3 inches (7.5 cm) for every infant",
            "Depth is unimportant if the rate exceeds 140 per minute",
        ],
        "One-third AP diameter balances perfusion with injury risk in small patients. Barely visible "
        "indentation is too shallow. A fixed deep depth for all infants may cause injury.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "An infant has only weak gasping breaths and is unresponsive. How should rescuers interpret "
        "this breathing?",
        "As abnormal breathing that may indicate cardiac arrest if pulse is absent",
        [
            "As normal sleep breathing that never requires CPR",
            "As a sign to give oral fluids only",
            "As mild choking requiring abdominal thrusts first",
        ],
        "Agonal gasps are not effective ventilation. Normal sleep breathing does not accompany "
        "unresponsiveness in arrest. Abdominal thrusts are not used for infants and are not the "
        "first step for gasping in arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "When should an AED be considered for an infant in suspected cardiac arrest?",
        "As soon as a device is available, using pediatric equipment when possible",
        [
            "Only after the infant reaches 12 months of age",
            "Never for patients under 10 kg",
            "Only in the hospital after physician approval",
        ],
        "AED use is part of pediatric resuscitation when arrest is present. Age alone should not "
        "arbitrarily exclude defibrillation when indicated. Lay BLS includes AED attachment per "
        "training when arrest criteria are met.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "Which action is part of high-quality infant chest compressions?",
        "Pushing hard enough to depress the chest one third of its AP diameter with full recoil",
        [
            "Leaning on the chest between compressions to save energy",
            "Compressing only once every 10 seconds",
            "Using the fingertips on the infant's face for leverage",
        ],
        "Adequate depth with full recoil defines effective compressions. Leaning between pushes blocks "
        "cardiac filling. Facial leverage does not provide sternal compression.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "After EMS activation, an infant has no pulse and is not breathing normally. What should CPR "
        "cycles include for a lone trained rescuer?",
        "30 compressions followed by 2 ventilations repeated",
        [
            "15 compressions followed by 2 ventilations only",
            "Two ventilations every five minutes without compressions",
            "Five compressions followed by one ventilation only",
        ],
        "Lone rescuer infant CPR follows 30:2 cycles. Fifteen to two is for two rescuers. Ventilation "
        "without compressions does not treat pulseless arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "Why are ventilations especially important in many infant cardiac arrests?",
        "Infants often arrest because of respiratory failure and hypoxia",
        [
            "Infants never need chest compressions under any circumstance",
            "Ventilations are required only after hospital admission",
            "Compression-only CPR is preferred for all infants at home",
        ],
        "Respiratory problems commonly precede infant arrest, so oxygenation matters. Compressions "
        "remain essential when pulse is absent. Compression-only CPR is not the preferred approach "
        "when breaths can be given.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "How long should each rescue breath last during infant CPR if chest rise is the goal?",
        "About one second per breath",
        [
            "At least five seconds per breath",
            "Less than 0.1 second with maximal force",
            "Until the rescuer feels dizzy from hyperventilation",
        ],
        "Brief breaths that produce chest rise limit interruption time and gastric inflation. Five-"
        "second breaths excessively pause compressions. Extremely forceful short puffs may not "
        "ventilate effectively.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "For infant BLS, which hand technique may a single rescuer use on a firm surface?",
        "Two fingers in the center of the chest on the lower half of the sternum",
        [
            "Heel of one hand with adult compression depth on the abdomen",
            "Two-thumb encircling hands while standing at the infant's feet alone",
            "One hand compressing the head while the other squeezes the abdomen",
        ],
        "Two-finger technique is standard for one rescuer. Adult heel depth on the abdomen is "
        "incorrect placement and depth. Two-thumb encircling is primarily a two-rescuer technique "
        "from the head of the bed.",
        _REF,
        "beginner",
    ),
    # --- intermediate (18) ---
    fact(
        "cpr-infant",
        "Two rescuers are performing infant CPR after EMS has been activated. What compression-to-"
        "ventilation ratio should they use?",
        "15 compressions to 2 ventilations",
        [
            "30 compressions to 2 ventilations",
            "5 compressions to 1 ventilation",
            "Continuous compressions with no ventilations",
        ],
        "Two-rescuer infant BLS uses 15:2 to increase ventilation frequency. Thirty to two is for a "
        "lone rescuer. Continuous compressions without breaths omit needed oxygenation in many infant "
        "arrests.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Which compression technique is preferred when two rescuers perform infant CPR?",
        "Two-thumb encircling hands technique on the lower half of the sternum",
        [
            "One rescuer compresses the infant's head while the other ventilates",
            "Two-finger technique with both rescuers stacking hands on the abdomen",
            "Heel of one hand using adult depth on the upper sternum only",
        ],
        "Two-thumb encircling hands improve depth and recoil with two providers. Head compression is "
        "never appropriate. Abdominal stacking does not provide effective cardiac compression.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "When opening an infant's airway for ventilations, what error should rescuers avoid?",
        "Excessive neck extension during head tilt",
        [
            "Any head movement regardless of trauma status",
            "Using a jaw thrust in every infant even without trauma concern",
            "Keeping the neck in a neutral position with no airway maneuver",
        ],
        "Infants have a relatively large occiput; overextension can obstruct the airway. Complete "
        "avoidance of positioning prevents opening the airway. Jaw thrust is for suspected spine "
        "injury, not every routine arrest.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "A responsive infant has severe choking with ineffective cough and poor air movement. What "
        "BLS sequence is appropriate?",
        "Alternate five back slaps and five chest thrusts while supporting the head and neck",
        [
            "Abdominal thrusts identical to adult Heimlich maneuver",
            "Finger sweeps into the mouth before any back slaps",
            "Rescue breaths only while the infant remains conscious",
        ],
        "Infant choking care uses back slaps and chest thrusts, not abdominal thrusts. Blind finger "
        "sweeps can worsen obstruction. CPR breaths are for unresponsive victims, not initial conscious "
        "severe choking.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "An infant's chest does not rise with the first rescue breath during CPR. What is the best "
        "response?",
        "Reposition the head, confirm mouth-and-nose seal, and give another gentle breath",
        [
            "Increase pressure until air leaks audibly from the stomach",
            "Skip all further ventilations for the rest of the arrest",
            "Perform blind finger sweeps before every subsequent breath",
        ],
        "Inadequate rise usually reflects position or seal, not insufficient effort alone. Forceful "
        "breaths inflate the stomach. Blind sweeps are discouraged in BLS airway management.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Why might rescuers cover an infant with a dry blanket during prolonged CPR in a cool room?",
        "Infants lose heat quickly, and hypothermia can worsen resuscitation outcomes",
        [
            "Covering replaces the need for ventilations entirely",
            "Infants always overheat during CPR and need cooling with ice",
            "Temperature has no effect on infant perfusion",
        ],
        "Thermoregulation is fragile in infants. Covering supports warmth after the chest is exposed "
        "for compressions. Ice cooling is not routine BLS. Ventilations remain necessary regardless "
        "of covering.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "How should rescuers minimize pauses when attaching AED pads to an infant?",
        "Continue compressions until pads are ready, then pause only briefly for attachment and analysis",
        [
            "Stop compressions for five minutes while reading the AED manual",
            "Remove pads after each shock and do not resume CPR",
            "Defer AED use until the infant is transported to a clinic",
        ],
        "Short pauses preserve perfusion during pad placement. Extended manual reading delays care. "
        "CPR must resume immediately after shock or no-shock advice.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "During infant CPR, what is required for adequate chest recoil?",
        "Allow the chest to return fully without resting body weight on the sternum",
        [
            "Maintain constant downward pressure between compressions",
            "Compress the ribs laterally without sternal contact",
            "Use partial recoil to increase compression rate above 180",
        ],
        "Full recoil permits ventricular filling between compressions. Constant pressure mimics leaning "
        "and reduces perfusion. Lateral rib compression is not standard BLS.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "A lone rescuer without a phone has provided infant CPR for about two minutes. What should "
        "they do about EMS activation?",
        "Leave the infant briefly to call EMS and obtain an AED if possible, then return",
        [
            "Never leave the infant to activate EMS under any circumstance",
            "Stop CPR permanently at two minutes without calling",
            "Drive the infant to a pharmacy without activating EMS",
        ],
        "After about two minutes, getting help becomes critical for lone rescuers without a phone. "
        "Never activating EMS sacrifices emergency response. Stopping CPR without a plan for help is "
        "inappropriate.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "When pediatric AED pads are available for an infant, how should they be used?",
        "Attach per manufacturer diagram, often with anterior-posterior placement if pads would overlap",
        [
            "Place both pads on the infant's back only",
            "Use adult pads on the thighs without chest contact",
            "Withhold the AED until hospital arrival",
        ],
        "Pediatric systems and placement instructions prevent pad overlap on small chests. Back-only "
        "placement without anterior pad may not deliver effective current path. Withholding "
        "defibrillation delays care in shockable rhythms.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "How often should rescuers switch the compressor during two-rescuer infant CPR?",
        "About every two minutes or sooner if compression quality declines",
        [
            "Only after ROSC has occurred",
            "Never switch to avoid breaking rhythm",
            "Every 10 seconds regardless of fatigue",
        ],
        "Switching limits fatigue-related shallow compressions in prolonged infant resuscitation. "
        "Waiting for ROSC may allow poor quality for many cycles. Ten-second switches are excessively "
        "disruptive.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "During CPR on an infant with suspected foreign body obstruction, when should you look in the "
        "mouth?",
        "Before giving rescue breaths if you suspect obstruction or after compressions as trained",
        [
            "Never look in the mouth during infant CPR",
            "Perform blind finger sweeps after every compression",
            "Only after 30 minutes of compressions",
        ],
        "Visible objects may be removed if seen, but blind sweeps are not recommended. Never inspecting "
        "misses dislodged material before breaths. Delaying inspection for 30 minutes is inappropriate.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Is compression-only CPR recommended for lay rescuers who can safely give ventilations to an "
        "infant in arrest?",
        "No; include ventilations with compressions when able",
        [
            "Yes; infants never benefit from rescue breaths",
            "Yes; breaths are contraindicated under one year of age",
            "Only health care providers may give infant ventilations",
        ],
        "Hypoxic respiratory failure commonly precedes infant arrest. Compression-only CPR omits "
        "needed oxygenation when breaths are feasible. Lay rescuers trained in BLS provide ventilations.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "What pulse check duration is appropriate during infant BLS before starting or continuing CPR?",
        "No more than 10 seconds",
        [
            "At least 60 seconds to avoid false starts",
            "Exactly two minutes between every compression cycle",
            "Lay rescuers should never pause compressions to check a pulse",
        ],
        "Brief checks limit compression interruption. A 60-second pause harms perfusion. Thinking "
        "lay rescuers must never pause to check a pulse is wrong—trained BLS still uses short checks "
        "between cycles when indicated.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "After an AED shock on an infant, what should rescuers do immediately?",
        "Resume chest compressions without waiting for a manual rhythm check",
        [
            "Wait until the infant moves before compressing again",
            "Remove AED pads and store the device",
            "Perform back slaps instead of compressions",
        ],
        "Immediate post-shock CPR maintains coronary perfusion. Waiting for movement delays care. Back "
        "slaps are for conscious choking, not post-shock arrest care.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "A caregiver performs infant CPR on a firm table. Why is a hard surface important?",
        "Soft surfaces absorb compression force and reduce effective depth",
        [
            "Soft bedding increases compression depth automatically",
            "Surface firmness only matters for adult victims",
            "Infants should always be compressed while held upright in arms only",
        ],
        "Compressions on soft mattresses dissipate force. Soft bedding does not deepen compressions. "
        "While two-rescuer encircling hands may be on a lap, effective depth still requires a firm "
        "support under the infant.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "How should ventilations be coordinated during two-rescuer infant CPR at a 15:2 ratio?",
        "The ventilator gives two breaths after every 15 compressions without delaying the next compression cycle unnecessarily",
        [
            "The ventilator gives five breaths after every 15 compressions",
            "Both rescuers stop compressions for 30 seconds to ventilate",
            "Ventilations occur only after ROSC",
        ],
        "Two breaths follow each set of 15 compressions in two-rescuer care. Five breaths exceed the "
        "ratio. Thirty-second pauses harm compression fraction.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Which finding would prompt starting infant CPR after a brief pulse check?",
        "No pulse or pulse below 60 per minute with poor perfusion signs",
        [
            "Pulse of 120 per minute with normal breathing",
            "Brief crying with strong movement",
            "Pink skin with responsive behavior",
        ],
        "Bradycardia with poor perfusion in infants is treated with CPR per pediatric BLS. Normal "
        "pulse with responsiveness does not indicate arrest. Crying and movement suggest the infant "
        "is not in pulseless arrest.",
        _REF,
        "intermediate",
    ),
    # --- advanced (13) ---
    fact(
        "cpr-infant",
        "A 4-month-old infant becomes unresponsive and is not breathing normally at home. The lone "
        "caregiver has a cell phone within reach. What is the best sequence?",
        "Call 911 on speakerphone, then begin infant CPR without leaving the infant",
        [
            "Run to a neighbor's house for two minutes before calling or starting CPR",
            "Wait until the infant turns blue before giving ventilations",
            "Perform abdominal thrusts as the first step for every unresponsive infant",
        ],
        "Speakerphone activation allows EMS dispatch while CPR starts immediately. Leaving the infant "
        "delays both activation and compressions. Color change is a late sign, and abdominal thrusts "
        "are not initial care for unresponsive non-choking infants.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "When placing AED pads on an infant and pediatric pads are unavailable, what approach is "
        "acceptable per AHA BLS?",
        "Use adult pads with anterior-posterior placement per manufacturer instructions while minimizing compression pause",
        [
            "Withhold defibrillation until the infant weighs at least 40 pounds",
            "Place both pads on the abdomen because the chest is too small",
            "Remove pads after the first shock and never resume CPR",
        ],
        "Adult AEDs may be used on infants and children with appropriate pad placement when pediatric "
        "equipment is missing. Arbitrary weight limits delay shock. CPR must resume immediately after "
        "shock delivery.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "An infant with severe choking becomes unresponsive in the rescuer's arms. What is the "
        "correct action?",
        "Lay the infant on a firm surface, call for help, and begin CPR with mouth checks before breaths",
        [
            "Continue back slaps while holding the unresponsive infant upright indefinitely",
            "Give rescue breaths only without compressions",
            "Perform abdominal thrusts on the infant",
        ],
        "Unresponsive choking infants receive CPR; compressions may dislodge the object. Back slaps "
        "alone are insufficient once unresponsive. Abdominal thrusts are not used for infants.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "After ROSC, a 6-month-old infant is breathing but remains pale and lethargic. What BLS "
        "priorities apply while awaiting EMS?",
        "Maintain airway, provide oxygen if trained, keep the infant warm, and monitor breathing and pulse",
        [
            "Place the infant alone in a cold vehicle without monitoring",
            "Resume full CPR compressions because lethargy always means arrest",
            "Withhold all monitoring once color improves slightly",
        ],
        "Post-ROSC infants need close observation for recurrence and thermoregulation. Unmonitored "
        "placement risks deterioration. Automatic return to compressions without reassessment is "
        "inappropriate.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "A newborn-style infant has a pulse of 50 per minute, limp tone, and poor perfusion after "
        "a brief check. What BLS action is appropriate?",
        "Begin chest compressions coordinated with ventilations per infant BLS protocol",
        [
            "Observe only because any palpable pulse excludes CPR",
            "Give blow-by oxygen without compressions until pulse is zero",
            "Wait for parents to arrive before any intervention",
        ],
        "Bradycardia with poor perfusion in infants is treated as arrest-equivalent. Observation "
        "alone fails to support systemic perfusion. Family presence should not delay CPR when "
        "indicated.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "During two-rescuer infant CPR, the compressor using two-thumb encircling hands should be "
        "positioned how?",
        "At the infant's head with thumbs on the sternum and hands encircling the chest",
        [
            "At the infant's feet compressing the abdomen with stacked fists",
            "Standing across the room while directing breaths only",
            "Kneeling on the infant's legs to stabilize the body",
        ],
        "Two-thumb technique is performed from the head with thumbs on the lower sternum. Abdominal "
        "fist compression is incorrect. Kneeling on the infant is unsafe and not part of BLS.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "An infant is pulled unresponsive from a bathtub. After safe removal, what BLS emphasis "
        "applies before and during CPR?",
        "Open the airway and give ventilations early because hypoxia likely preceded arrest",
        [
            "Dry the infant for 10 minutes before any breaths or compressions",
            "Start with abdominal thrusts for all drowning infants",
            "Defer CPR until the infant is wrapped in heated blankets only",
        ],
        "Submersion arrests are often hypoxic; ventilations are critical after rescue. Prolonged drying "
        "without care sacrifices oxygenation. Abdominal thrusts are not the drowning response for "
        "unresponsive infants.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "If standard anterior AED pad placement would cause pads to touch on an infant's chest, what "
        "adjustment is commonly recommended?",
        "Anterior-posterior pad placement per device instructions",
        [
            "Place both pads on the right arm only",
            "Overlap pads intentionally in the center of the chest",
            "Cancel AED use for the remainder of the arrest",
        ],
        "Separating current paths prevents overlap on small chests. Arm-only placement does not "
        "traverse the heart effectively. Canceling AED use abandons defibrillation for shockable "
        "rhythms.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "An infant in arrest has CPR in progress when the compressor notes inadequate depth with two-"
        "finger technique. Two rescuers are present. What change improves quality?",
        "Switch to two-thumb encircling hands with the second rescuer managing ventilations at 15:2",
        [
            "Switch to heel-of-hand adult compressions on the sternum",
            "Stop compressions and ventilate only until depth improves",
            "Compress the infant's back while ventilating from the side without sternal compressions",
        ],
        "Two-thumb technique generally provides better depth and recoil with two providers. Adult heel "
        "technique risks excessive depth. Ventilation-only care does not treat pulseless arrest.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "EMS places an advanced airway in an infant during resuscitation. How should ventilations be "
        "given afterward?",
        "Continue compressions without pausing for breaths and deliver about one breath every six seconds",
        [
            "Pause compressions for 10 seconds before each breath",
            "Stop compressions entirely after the airway is placed",
            "Give triple breaths after every compression",
        ],
        "Continuous compressions with asynchronous ventilations maintain perfusion after advanced "
        "airway placement. Ten-second pauses for each breath reduce coronary pressure. Triple breaths "
        "are not the post-airway ventilation rate.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "A 9-month-old infant is choking; cough is silent, lips are cyanotic, and the infant is still "
        "responsive. What should you do?",
        "Support the head and neck and alternate five back slaps and five chest thrusts",
        [
            "Encourage coughing because cyanosis always means mild obstruction",
            "Begin CPR compressions while the infant remains conscious and standing",
            "Deliver abdominal thrusts identical to adult technique",
        ],
        "Silent cough and cyanosis indicate severe obstruction requiring back slaps and chest thrusts. "
        "Mild obstruction would have a stronger cough. CPR compressions begin when the infant becomes "
        "unresponsive, not while conscious. Abdominal thrusts are not used on infants.",
        _REF,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "Which strategy best preserves chest compression fraction during infant resuscitation with AED "
        "use?",
        "Prepare pads during ongoing compressions and resume compressions immediately after shock or no-shock prompt",
        [
            "Pause compressions for two minutes after every AED voice prompt to rest",
            "Limit compressions to less than one quarter of total resuscitation time",
            "Remove the AED after the first analysis and continue without it",
        ],
        "High compression fraction supports coronary perfusion during infant arrest. Routine two-minute "
        "rest periods are harmful. Discarding the AED after one analysis prevents further rhythm "
        "management.",
        _HQ,
        "advanced",
    ),
    fact(
        "cpr-infant",
        "A premature infant in the home develops unresponsiveness and apnea. Pulse is absent after a "
        "brief brachial check. What BLS care applies?",
        "Provide infant CPR with appropriate ratio for rescuer number, using gentle but effective compressions and ventilations",
        [
            "Defer all CPR because prematurity makes resuscitation futile",
            "Ventilate only without compressions regardless of pulse status",
            "Use adult 30:2 on the mother's chest instead of the infant",
        ],
        "Premature infants receive standard infant BLS when arrest criteria are met; gentleness does "
        "not mean withholding CPR. Ventilation-only care fails when pulse is absent. CPR must be "
        "performed on the infant victim directly.",
        _REF,
        "advanced",
    ),
]
