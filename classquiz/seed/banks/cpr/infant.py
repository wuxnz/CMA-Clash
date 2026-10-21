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
        "What compression-to-ventilation ratio should a single lay rescuer use during infant BLS CPR?",
        "30 compressions followed by 2 ventilations (30:2)",
        [
            "15 compressions followed by 2 ventilations for every infant arrest",
            "5 compressions followed by 1 ventilation to shorten pauses between breaths",
            "Continuous chest compressions with no ventilations until EMS places an advanced airway",
        ],
        "AHA infant BLS uses 30:2 when only one rescuer is available. Fifteen-to-two is reserved "
        "for two-rescuer infant CPR so ventilations can be given more frequently. Compression-only "
        "care without breaths omits needed oxygenation in many hypoxic infant arrests.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "Which chest compression rate should rescuers deliver during high-quality infant CPR?",
        "100 to 120 compressions per minute",
        [
            "90 to 100 compressions per minute",
            "120 to 140 compressions per minute",
            "140 to 160 compressions per minute",
        ],
        "Infant compressions follow the same rate target as other BLS victims. Rates below 100 "
        "often fail to maintain coronary and cerebral perfusion. Very fast rates usually sacrifice "
        "depth and full recoil, reducing effectiveness.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "Where should a single rescuer place two-finger chest compressions during infant BLS CPR?",
        "On the lower half of the sternum in the center of the chest, just below the nipple line",
        [
            "On the upper abdomen over the stomach with the heel of one hand",
            "Directly on the xiphoid process with maximal downward pressure",
            "On the infant's back while the infant lies prone without sternal contact",
        ],
        "Sternal compressions on the lower half of the sternum direct force through the heart. "
        "Abdominal compression does not compress the heart effectively. Prone back compressions "
        "are not standard infant BLS on a firm surface.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "How should rescue breaths be delivered to an infant during CPR when ventilations are included?",
        "Seal the mouth and nose and give each breath over about one second until chest rise",
        [
            "Pinch the nose shut and ventilate only through the mouth as for adults",
            "Give two-second breaths until the abdomen rises with each ventilation",
            "Cover the mouth alone and leave the nose open during each breath",
        ],
        "Infants need a mouth-and-nose seal with modest tidal volume. Pinching the nose is an "
        "adult technique. Overventilation causes gastric inflation and reduces effective "
        "ventilation during infant BLS.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "During a pulse check on an unresponsive infant, where should the rescuer palpate and for "
        "how long?",
        "Feel the brachial pulse on the inside of the upper arm for no more than about 10 seconds",
        [
            "Palpate the femoral pulse in the groin for up to about 10 seconds before starting CPR",
            "Palpate the brachial pulse on the upper arm for about 15 to 20 seconds before deciding on CPR",
            "Palpate the carotid pulse in the neck for about 5 to 10 seconds before starting CPR",
        ],
        "The brachial pulse is accessible and reliable in infants during BLS assessment. Radial "
        "pulses may be difficult to feel with poor perfusion. Brief checks limit harmful delays "
        "in starting compressions when arrest is likely.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "You confirm scene safety and find an infant unresponsive in a crib. What should you do "
        "immediately after checking responsiveness?",
        "Shout for nearby help and activate emergency response or send someone to call EMS",
        [
            "Begin chest compressions immediately without ever activating emergency response",
            "Leave the infant alone to search a distant building for an AED before any assessment",
            "Wait for a caregiver to arrive before activating emergency response",
        ],
        "Early activation brings EMS and equipment while assessment continues. Compressions follow "
        "quick activation when arrest criteria are met, but ignoring help entirely delays advanced "
        "care. Oral fluids are not part of arrest assessment.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "What compression depth target is recommended for most infants during BLS CPR?",
        "About 1.5 inches (4 cm), or at least one third of the chest front-to-back depth",
        [
            "About 1 inch (2.5 cm) on the sternum for all infant CPR",
            "About 2 inches (5 cm) on the sternum for all infant CPR",
            "About one half of the chest front-to-back depth on each compression",
        ],
        "AHA infant BLS targets about one third AP diameter, near 1.5 inches (4 cm). Shallow "
        "one-inch compressions often under-perfuse; a fixed two-inch depth may be excessive for "
        "small infants.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "An unresponsive infant has only weak gasping breaths and no effective ventilation. How "
        "should rescuers treat this breathing pattern?",
        "Treat gasping as abnormal breathing and start CPR if no pulse is detected within 10 seconds",
        [
            "Consider gasping normal sleep breathing and withhold CPR until EMS confirms arrest",
            "Offer small sips of formula because gasping may reflect hunger rather than arrest",
            "Perform abdominal thrusts before any pulse check or chest compressions",
        ],
        "Agonal gasps are not effective ventilation and may occur during cardiac arrest. Treating "
        "gasps as normal breathing delays CPR. Abdominal thrusts are not used for infants and do "
        "not replace pulse assessment in primary gasping arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "When should rescuers apply an AED during suspected cardiac arrest in an infant?",
        "As soon as the device is available, using pediatric pads or equipment when possible",
        [
            "Only after the infant reaches 12 months of age even during witnessed collapse",
            "Never for patients under 10 kg even when arrest criteria are met",
            "Only in the hospital after physician approval and advanced monitoring are in place",
        ],
        "Early defibrillation improves survival in shockable rhythms. Age and size alone should not "
        "arbitrarily exclude AED use when arrest is present. Lay BLS includes AED attachment per "
        "training and manufacturer instructions when indicated.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "Which description best matches high-quality chest compressions during infant CPR?",
        "Hard, fast compressions to one third AP depth with full chest recoil and minimal pauses",
        [
            "Leaning on the chest between compressions to conserve rescuer energy",
            "Compressing only once every 10 seconds even when pulse is absent",
            "Two-finger compressions on the lateral rib cage instead of the sternum",
        ],
        "Depth, rate, recoil, and limited interruptions define high-quality CPR. Leaning on the chest "
        "blocks recoil and reduces perfusion. Lateral rib compressions do not provide effective "
        "sternal compression.",
        _HQ,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "After EMS activation, an unresponsive infant is not breathing normally and has no pulse. "
        "What should a trained lone rescuer do next?",
        "Begin CPR, starting with chest compressions per CAB in most lay infant BLS programs",
        [
            "Wait on scene for EMS arrival before starting any chest compressions",
            "Give two minutes of rescue breaths alone before any compressions are started",
            "Observe breathing in the crib without compressions until parents arrive",
        ],
        "Immediate CPR supports circulation and oxygen delivery until advanced care arrives. Waiting "
        "for EMS without compressions sacrifices perfusion. Breath-only care without compressions "
        "does not treat pulseless arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "Why does AHA recommend including rescue ventilations during infant CPR when the rescuer can "
        "deliver breaths safely?",
        "Many infant arrests begin with respiratory failure and hypoxia, so early ventilation matters",
        [
            "Chest compressions are unnecessary once two effective rescue breaths are given",
            "Rescue breaths are optional when the infant had a witnessed collapse at home",
            "Compression-only CPR is the preferred lay approach for all infants under one year",
        ],
        "Respiratory failure commonly precedes infant cardiac arrest. Compressions remain essential "
        "when pulse is absent, but ventilations address hypoxia in many cases. Compression-only CPR "
        "is not preferred when full BLS ventilations can be delivered safely.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "How should a rescuer deliver each rescue breath during infant CPR when chest rise is the goal?",
        "Give each breath over about 1 second until visible chest rise, without excessive volume",
        [
            "Deliver each breath over at least 5 seconds to maximize oxygen delivery",
            "Give very short forceful puffs in under 0.1 second without checking chest rise",
            "Deliver each breath over at least 5 seconds to maximize oxygen delivery",
        ],
        "Brief breaths that produce chest rise limit interruption time and gastric inflation. "
        "Five-second breaths excessively pause compressions. Forceful puffs without visible rise "
        "may fail to ventilate effectively.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "When opening the airway for infant CPR and significant trauma is not suspected, which "
        "maneuver should rescuers use?",
        "Head tilt-chin lift while avoiding excessive neck extension",
        [
            "Jaw thrust with deliberate maximal neck hyperextension on every infant arrest",
            "Keep the head and neck completely still even when the airway does not open",
            "Finger sweep of the oropharynx before every rescue breath even when no object is seen",
        ],
        "Head tilt-chin lift opens the airway in most medical infant arrests. Infants have a "
        "relatively large occiput, so overextension can obstruct rather than open the airway. "
        "Blind finger sweeps are discouraged because they can push objects deeper.",
        _REF,
        "beginner",
    ),
    # --- intermediate (18) ---
    fact(
        "cpr-infant",
        "Two trained rescuers are managing cardiac arrest in an infant after EMS has been activated. "
        "What compression-to-ventilation ratio should they use?",
        "15 compressions followed by 2 ventilations (15:2)",
        [
            "30 compressions followed by 2 ventilations for every two-rescuer infant arrest",
            "5 compressions followed by 1 ventilation to minimize compression interruptions",
            "Continuous compressions with rescue breaths given only every 30 seconds",
        ],
        "Two-rescuer infant BLS uses 15:2 so ventilations can be given more frequently while one "
        "rescuer focuses on compressions. The 30:2 ratio applies to single-rescuer CPR. Continuous "
        "compressions without breaths omit needed oxygenation in many infant arrests.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Which compression technique is preferred when two rescuers perform infant CPR from the head "
        "of the bed?",
        "Two-thumb encircling hands technique on the lower half of the sternum",
        [
            "Two-finger compressions on the upper sternum near the chin while ventilating",
            "Two-finger technique with both rescuers stacking hands on the upper abdomen",
            "Heel of one hand using adult compression depth on the upper sternum only",
        ],
        "Two-thumb encircling hands improve depth and recoil with two providers at the head of the "
        "bed. Upper-sternum two-finger placement and abdominal stacking do not provide effective "
        "cardiac compression during infant BLS.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "When opening an infant's airway for ventilations during CPR, which positioning error should "
        "rescuers avoid?",
        "Excessive neck extension during head tilt that can obstruct the airway",
        [
            "Avoid any head or neck movement even when the airway stays obstructed",
            "Using a jaw thrust maneuver on every infant even when spine injury is not suspected",
            "Keeping the neck completely neutral with no attempt to open the airway",
        ],
        "Infants have a relatively large occiput; overextension can obstruct the airway. Complete "
        "avoidance of positioning prevents opening the airway. Jaw thrust is for suspected spine "
        "injury, not every routine arrest without trauma concern.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "A responsive infant has severe choking with an ineffective cough and poor air movement. "
        "What BLS sequence is appropriate?",
        "Alternate five back slaps and five chest thrusts while supporting the head and neck",
        [
            "Abdominal thrusts identical to the adult Heimlich maneuver",
            "Blind finger sweeps into the mouth before any back slaps or chest thrusts",
            "Rescue breaths only while the infant remains conscious and crying weakly",
        ],
        "Infant choking care uses back slaps and chest thrusts, not abdominal thrusts. Blind finger "
        "sweeps can worsen obstruction. CPR ventilations are for unresponsive victims, not initial "
        "conscious severe choking with poor air exchange.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "During infant CPR, a rescue breath does not produce visible chest rise on the first attempt. "
        "What should the rescuer do before giving the next breath?",
        "Reposition the airway, confirm the mouth-and-nose seal, and retry a gentle breath over about 1 second",
        [
            "Increase pressure until air leaks audibly from the stomach on every subsequent breath",
            "Skip all further ventilations for the remainder of the arrest and compress only",
            "Perform blind finger sweeps of the mouth before every subsequent rescue breath",
        ],
        "Inadequate chest rise usually means the airway is not open or the seal or volume was wrong. "
        "Repositioning and a one-second breath limits gastric inflation. Forceful breaths and blind "
        "sweeps are discouraged in AHA infant BLS.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Why might rescuers cover an infant with a dry blanket during prolonged out-of-hospital CPR "
        "in a cool environment?",
        "Infants lose heat quickly, and hypothermia can worsen resuscitation outcomes",
        [
            "Covering the infant replaces the need for rescue ventilations entirely",
            "Infants always overheat during CPR and need active cooling with ice packs",
            "Body temperature has no effect on infant perfusion during resuscitation",
        ],
        "Thermoregulation is fragile in infants. Covering supports warmth after the chest is exposed "
        "for compressions. Ice cooling is not routine BLS. Ventilations remain necessary regardless "
        "of covering.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Which action best limits harmful pauses during infant CPR when an AED is integrated into care?",
        "Continue compressions until pads are ready, then pause only briefly for attachment and rhythm analysis",
        [
            "Stop compressions until the AED finishes its automatic self-test on startup",
            "Remove AED pads after each shock and do not resume CPR until EMS arrives",
            "Defer all AED use until the infant is transported to an outpatient clinic",
        ],
        "Short pauses preserve coronary perfusion during pad placement. Extended reading or rest "
        "periods delay care. CPR must resume immediately after shock delivery or when no shock is "
        "advised.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "During infant CPR, leaning on the chest between compressions prevents full recoil. What is "
        "the main consequence?",
        "Reduced ventricular filling and lower effective coronary perfusion during the next compression",
        [
            "Leaning steadies hand placement and always improves compression depth",
            "Incomplete recoil affects only ventilation rate and not blood flow",
            "Partial recoil is acceptable if compression rate exceeds 180 per minute",
        ],
        "Full recoil permits ventricular filling between compressions. Leaning mimics incomplete "
        "recoil and reduces perfusion. Lateral rib-only compression without sternal contact is not "
        "standard infant BLS.",
        _HQ,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "A lone rescuer without a cell phone has provided infant CPR for about two minutes. What "
        "should they do about EMS activation and AED retrieval?",
        "Leave the infant briefly to activate EMS and obtain an AED if possible, then return to CPR",
        [
            "Never leave the infant to activate EMS under any circumstance",
            "Stop CPR permanently at two minutes without calling for emergency help",
            "Transport the infant alone to a pharmacy without activating EMS",
        ],
        "After about two minutes, getting help becomes critical for lone rescuers without a phone. "
        "Brief activation improves access to EMS and defibrillation. Stopping CPR without a plan "
        "for help is inappropriate.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "When pediatric AED pads are available for an infant, how should rescuers attach them?",
        "Place pediatric pads per the diagram, often anterior-posterior when front-chest pads would overlap",
        [
            "Use adult pads on the anterior chest anterolateral even if the pads overlap on a small chest",
            "Delay attaching the AED until five full cycles of CPR have been completed",
            "Place one pediatric pad on the center of the chest and one on the right upper chest so the pads touch",
        ],
        "Pediatric systems and placement instructions prevent pad overlap on small chests. An "
        "effective current path usually requires appropriate anterior and posterior or lateral "
        "placement per instructions. Withholding defibrillation delays care in shockable rhythms.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "How often should rescuers switch the compressor during two-rescuer infant CPR?",
        "About every two minutes or sooner if compression quality or depth declines",
        [
            "Only after return of spontaneous circulation has been confirmed",
            "Never switch compressors to avoid breaking team rhythm",
            "Every 10 seconds even when rate and depth still meet targets",
        ],
        "Switching limits fatigue-related shallow compressions in prolonged infant resuscitation. "
        "Waiting for ROSC may allow poor quality for many cycles. Ten-second switches are excessively "
        "disruptive to compressions.",
        _HQ,
        "intermediate",
    ),
 fact(
 "cpr-infant",
 "During CPR on an infant with suspected foreign body obstruction, when should you look in the "
 "mouth?",
 "Before giving rescue breaths if you suspect obstruction or after compressions as trained",
 [
 "Skip mouth inspection until EMS arrives even when obstruction is suspected",
 "Perform blind finger sweeps after every compression",
 "Only inspect the mouth after several full 30:2 cycles without any breath attempt",
 ],
 "Visible objects may be removed if seen, but blind sweeps are not recommended. Never inspecting "
 "misses dislodged material before breaths when obstruction is suspected.",
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
 "lay rescuers must never pause to check a pulse is wrong, trained BLS still uses short checks "
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
 "Lay the infant on a firm surface, call for help, and start CPR with mouth checks before breaths",
 [
 "Continue back slaps and chest thrusts while the infant stays in your arms",
 "Give rescue breaths without chest compressions after calling for help",
 "Perform abdominal thrusts as for an adult choking victim",
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
 "Maintain airway patency, provide supplemental oxygen, keep the infant warm, and monitor breathing and pulse",
 [
 "Place the infant alone in a cold vehicle without supplemental oxygen or monitoring",
 "Resume full CPR compressions for lethargy without reassessing pulse and breathing",
 "Provide supplemental oxygen but stop monitoring once color improves slightly",
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
 "Start chest compressions with ventilations per infant BLS bradycardia care",
 [
 "Monitor at the bedside because a pulse is felt on palpation",
 "Give blow-by oxygen without compressions until the pulse is absent",
 "Delay intervention until the infant's caregivers arrive at the scene",
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
 "At the infant's feet using stacked fists on the upper abdomen",
 "One rescuer at the side compressing the abdomen while the other ventilates",
 "Both rescuers kneeling on opposite sides of the chest to stabilize the infant",
 ],
 "Two-thumb technique is performed from the head with thumbs on the lower sternum. Abdominal "
 "fist compression and side abdominal compressions are incorrect for infant BLS.",
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
 "Begin chest compressions while the infant remains conscious and upright in your arms",
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
 "Start infant CPR with gentle compressions and ventilations at the ratio for rescuer number",
 [
 "Delay CPR until EMS arrives because the infant was born prematurely",
 "Provide ventilations without compressions when pulse is absent after the check",
 "Use two-thumb compressions on the caregiver while the infant is held upright",
 ],
 "Premature infants receive standard infant BLS when arrest criteria are met; gentleness does "
 "not mean withholding CPR. Ventilation-only care fails when pulse is absent. CPR must be "
 "performed on the infant victim directly.",
 _REF,
 "advanced",
 ),
    fact(
        "cpr-infant",
        "A second rescuer joins while a lone provider is performing 30:2 infant CPR. What ratio "
        "should the team use once roles are assigned?",
        "15 compressions followed by 2 ventilations (15:2) with one rescuer compressing and one ventilating",
        [
            "Continue 30:2 with both rescuers alternating compressions on every cycle",
            "5 compressions followed by 1 ventilation to minimize pause time between breaths",
            "Continuous compressions with ventilations withheld until EMS places an advanced airway",
        ],
        "Two-rescuer infant BLS uses 15:2 so ventilations can be given more often while compressions "
        "continue with minimal interruption. Lone-rescuer 30:2 is not the two-provider ratio. "
        "Compression-only care omits ventilations needed in many hypoxic infant arrests.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "During infant CPR, an AED completes rhythm analysis and advises no shock. What should "
        "rescuers do immediately?",
        "Resume chest compressions without delay and follow subsequent AED prompts",
        [
            "Stop CPR for two minutes to let the heart recover spontaneously",
            "Remove the AED pads and discontinue defibrillation attempts for the arrest",
            "Deliver a manual shock anyway because analysis can miss treatable rhythms",
        ],
        "Non-shockable rhythms still require high-quality CPR and continued AED monitoring per "
        "prompts. Prolonged pauses or abandoning the AED reduces compression fraction and rhythm "
        "reassessment. Manual shocks against device advice are unsafe and ineffective.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "You are about to start infant BLS on a stranger's child in a public setting. What PPE "
        "practice aligns with standard precautions during ventilations?",
        "Use a barrier device or face shield when available and perform hand hygiene before and after care",
        [
            "Skip all barriers and ventilate mouth-to-mouth without hand hygiene to save time",
            "Wear only exam gloves and skip airway barriers even when a mask is on the AED kit",
            "Delay all ventilations until full hospital isolation garb can be obtained",
        ],
        "Barrier devices reduce body-fluid exposure during rescue breaths when available. Hand "
        "hygiene limits cross-contamination after care. Delaying ventilations for full isolation "
        "equipment sacrifices oxygenation in arrest.",
        _REF,
        "beginner",
    ),
    fact(
        "cpr-infant",
        "An infant has no trauma history and needs rescue breaths during CPR. How should the "
        "airway most often be opened?",
        "Head tilt-chin lift while supporting the head and neck",
        [
            "Head extension with the neck tilted back before each ventilation",
            "Neck flexion with a rolled towel under the shoulders before each breath",
            "Jaw thrust as the first-line maneuver when trauma is not suspected",
        ],
        "Head tilt-chin lift is the standard airway maneuver for infants without suspected spine "
        "injury. Excessive extension or routine jaw thrust when trauma is not suspected reflects "
        "common training errors in infant BLS airway opening.",
        _REF,
        "intermediate",
    ),
    fact(
        "cpr-infant",
        "Real-time feedback shows infant compressions are fast but shallow during two-rescuer CPR. "
        "What depth target should the team prioritize?",
        "About 1.5 inches (4 cm), or at least one third of the chest front-to-back depth",
        [
            "About 1 inch (2.5 cm) on the sternum for all infant CPR",
            "About 2 inches (5 cm) on the sternum for all infant CPR",
            "About one half of the chest front-to-back depth on each compression",
        ],
        "Adequate depth generates perfusion in infant arrest; shallow fast compressions are a "
        "common quality problem. A fixed deep target may be excessive for small infants. Rate "
        "alone does not replace depth and full recoil in high-quality infant CPR.",
        _HQ,
        "intermediate",
    ),
]
