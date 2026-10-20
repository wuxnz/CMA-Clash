# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

FACTS: list[dict] = [
    {
        "topic": "cpr-adult",
        "stem": "Adult BLS compression-to-ventilation ratio for single rescuer CPR is:",
        "correct": "30:2",
        "distractors": [
            "15:2",
            "5:1",
            "Continuous compressions with no breaths ever"
        ],
        "explanation": "AHA guidelines use 30:2 for adult BLS.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-adult",
        "stem": "Adult compression depth should be at least:",
        "correct": "2 inches (5 cm) but not more than 2.4 inches (6 cm)",
        "distractors": [
            "1 inch",
            "3.5 inches always",
            "Varies without limit"
        ],
        "explanation": "Adequate depth generates perfusion.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-adult",
        "stem": "Compression rate for adult CPR should be:",
        "correct": "100 to 120 per minute",
        "distractors": [
            "60 to 80 per minute",
            "150 to 200 per minute",
            "As slow as possible"
        ],
        "explanation": "Push hard and fast in center of chest.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-adult",
        "stem": "Hand placement for adult compressions is:",
        "correct": "Center of chest on lower half of sternum",
        "distractors": [
            "Upper abdomen",
            "Left nipple only",
            "Over xiphoid tip"
        ],
        "explanation": "Avoid compressing over xiphoid.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-adult",
        "stem": "After activating emergency response for unresponsive adult, check:",
        "correct": "Breathing and pulse simultaneously if trained (no more than 10 seconds)",
        "distractors": [
            "Blood glucose only",
            "Blood pressure cuff",
            "Temperature only"
        ],
        "explanation": "Recognize cardiac arrest and start CPR if indicated.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-adult",
        "stem": "Chest recoil during compressions requires:",
        "correct": "Allowing full chest return without leaning",
        "distractors": [
            "Keeping weight on chest",
            "Shallow pumps",
            "Arms locked leaning"
        ],
        "explanation": "Full recoil improves coronary perfusion.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-adult",
        "stem": "Rescue breaths in adult CPR should:",
        "correct": "Make chest rise over about 1 second each",
        "distractors": [
            "Be forceful rapid gusts",
            "Never be given",
            "Last 5 seconds each"
        ],
        "explanation": "Minimize interruptions to compressions.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-adult",
        "stem": "AED should be applied:",
        "correct": "As soon as available for cardiac arrest",
        "distractors": [
            "Only after 10 minutes of CPR",
            "Only if patient speaks",
            "Before checking responsiveness"
        ],
        "explanation": "Early defibrillation improves survival.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-adult",
        "stem": "CPR compression interruptions should be:",
        "correct": "Minimized, especially for rhythm analysis and shocks",
        "distractors": [
            "Maximized for rest",
            "At least 30 seconds each minute",
            "Avoided entirely even for AED"
        ],
        "explanation": "Limit pauses to less than 10 seconds when possible.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-adult",
        "stem": "Two-rescuer adult CPR compression ratio is:",
        "correct": "30:2 with rescuers switching roles",
        "distractors": [
            "15:2 only always",
            "5:1",
            "No ventilations"
        ],
        "explanation": "Switch compressors every 2 minutes to prevent fatigue.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-adult",
        "stem": "Agonal gasps in unresponsive patient:",
        "correct": "May be sign of cardiac arrest, not normal breathing",
        "distractors": [
            "Mean patient is fine",
            "Require only oxygen mask",
            "Contraindicate CPR"
        ],
        "explanation": "Treat as respiratory arrest/ arrest and follow BLS.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-adult",
        "stem": "High-quality CPR includes:",
        "correct": "Hard fast compressions, full recoil, minimal interruptions",
        "distractors": [
            "Slow shallow compressions",
            "Frequent long pauses",
            "Leaning on chest"
        ],
        "explanation": "Quality compressions are key to outcomes.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-child",
        "stem": "Pediatric BLS single rescuer compression-ventilation ratio is:",
        "correct": "30:2",
        "distractors": [
            "15:2 only for all child ages always",
            "5:1",
            "No compressions"
        ],
        "explanation": "AHA uses 30:2 for single rescuer child CPR.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-child",
        "stem": "Two-rescuer child CPR compression-ventilation ratio is:",
        "correct": "15:2",
        "distractors": [
            "30:2",
            "10:1",
            "Continuous only"
        ],
        "explanation": "Two rescuers may use 15:2 for children.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-child",
        "stem": "Child compression depth is about:",
        "correct": "One third the anteroposterior diameter of chest, about 2 inches (5 cm)",
        "distractors": [
            "1 inch maximum always",
            "4 inches minimum",
            "No depth standard"
        ],
        "explanation": "Use one or two hands depending on child size.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-child",
        "stem": "Child pulse check locations include:",
        "correct": "Carotid or femoral for infant/child per training",
        "distractors": [
            "Radial only always",
            "Apical only",
            "Pedal only"
        ],
        "explanation": "Use site appropriate to age.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-child",
        "stem": "For unresponsive child not breathing normally, after activating EMS:",
        "correct": "Start CPR beginning with compressions if lone rescuer",
        "distractors": [
            "Wait for parents only",
            "Give fluids",
            "Leave to find AED only"
        ],
        "explanation": "Follow pediatric BLS algorithm.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-child",
        "stem": "Compression rate for child CPR is:",
        "correct": "100 to 120 per minute",
        "distractors": [
            "80 per minute",
            "150 per minute",
            "60 per minute"
        ],
        "explanation": "Same rate target as adult.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-child",
        "stem": "Ventilation volume for child should:",
        "correct": "Produce visible chest rise without excessive force",
        "distractors": [
            "Hyperinflate always",
            "Be omitted entirely",
            "Use adult bag without adjustment"
        ],
        "explanation": "Avoid gastric inflation.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-child",
        "stem": "If child chokes and becomes unresponsive:",
        "correct": "Start CPR and look for object before breaths",
        "distractors": [
            "Blind finger sweeps in mouth always",
            "No CPR",
            "Only back blows"
        ],
        "explanation": "CPR may dislodge object; follow choking algorithm.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-child",
        "stem": "AED use in children:",
        "correct": "Use pediatric pads/dose attenuator if available; adult pads anterior-posterior if not",
        "distractors": [
            "Never on children",
            "Only on infants <1 year",
            "Skip AED entirely"
        ],
        "explanation": "Early defibrillation is indicated for shockable rhythms.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-child",
        "stem": "Lone rescuer should call EMS first for:",
        "correct": "Witnessed sudden collapse likely cardiac in child",
        "distractors": [
            "All choking",
            "Every minor fall",
            "Routine fever"
        ],
        "explanation": "Activate EMS and get AED quickly for arrest.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "cpr-child",
        "stem": "Hand placement for child compressions:",
        "correct": "Center of chest on lower half of sternum",
        "distractors": [
            "Abdomen only",
            "Back only",
            "One finger only"
        ],
        "explanation": "Same landmark as adult, adjust force.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-child",
        "stem": "Reassessment during pediatric CPR occurs:",
        "correct": "Every 2 minutes or when AED prompts",
        "distractors": [
            "Never",
            "Every 30 seconds only",
            "After 20 minutes only"
        ],
        "explanation": "Minimize interruption when checking rhythm.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-infant",
        "stem": "Infant compression depth is about:",
        "correct": "One third AP diameter, about 1.5 inches (4 cm)",
        "distractors": [
            "2.4 inches",
            "0.5 inch",
            "No standard"
        ],
        "explanation": "Two fingers or two-thumb encircling technique.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-infant",
        "stem": "Two-finger infant compression technique places fingers:",
        "correct": "Center of chest just below nipple line",
        "distractors": [
            "On abdomen",
            "On throat",
            "On forehead"
        ],
        "explanation": "Compress sternum, not soft upper abdomen.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-infant",
        "stem": "Infant BLS lone rescuer ratio is:",
        "correct": "30:2",
        "distractors": [
            "15:2 only",
            "5:1",
            "No ventilations"
        ],
        "explanation": "Follow infant BLS algorithm.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-infant",
        "stem": "Two-rescuer infant CPR ratio is:",
        "correct": "15:2",
        "distractors": [
            "30:2",
            "10:1",
            "3:1 always"
        ],
        "explanation": "Two rescuers use 15:2 for infants.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-infant",
        "stem": "Infant pulse check is best at:",
        "correct": "Brachial artery",
        "distractors": [
            "Carotid only",
            "Radial only",
            "Popliteal only"
        ],
        "explanation": "Brachial is reliable in infants.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-infant",
        "stem": "Head tilt-chin lift for infant airway avoids:",
        "correct": "Excessive neck extension",
        "distractors": [
            "Hyperflexion only",
            "Jaw thrust always first in all cases",
            "No airway maneuver"
        ],
        "explanation": "Neutral position supports open airway.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-infant",
        "stem": "Rescue breaths for infant cover:",
        "correct": "Mouth and nose with gentle puffs",
        "distractors": [
            "Mouth only with tight seal always",
            "Nose only",
            "Cheeks"
        ],
        "explanation": "Small tidal volume prevents gastric inflation.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-infant",
        "stem": "Infant choking responsive protocol uses:",
        "correct": "Back slaps and chest thrusts",
        "distractors": [
            "Abdominal thrusts only",
            "CPR first",
            "No intervention"
        ],
        "explanation": "Do not use abdominal thrusts on infants.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-infant",
        "stem": "AED on infant:",
        "correct": "Use pediatric system if available; place pads per manufacturer",
        "distractors": [
            "Forbidden",
            "Adult pads on limbs only always",
            "Only manual defibrillation"
        ],
        "explanation": "Follow device instructions for small patients.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "cpr-infant",
        "stem": "Compression rate for infant CPR:",
        "correct": "100 to 120 per minute",
        "distractors": [
            "60 per minute",
            "150 per minute",
            "Variable without guidance"
        ],
        "explanation": "Consistent rate improves perfusion.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-infant",
        "stem": "If infant is unresponsive and not breathing:",
        "correct": "Start CPR after activating EMS or after 2 minutes lone care per scenario training",
        "distractors": [
            "Wait for parents indefinitely",
            "Only oxygen",
            "No compressions"
        ],
        "explanation": "Follow local EMS protocol for lone rescuer.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "cpr-infant",
        "stem": "Two-thumb encircling technique is performed:",
        "correct": "From base of infant with hands encircling chest",
        "distractors": [
            "Standing at feet only",
            "One hand on head",
            "On patient's back only"
        ],
        "explanation": "Thumbs compress sternum; alternative to two-finger.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-aed",
        "stem": "When AED arrives on scene, first action is:",
        "correct": "Turn on and follow voice prompts",
        "distractors": [
            "Place pads on patient before powering on",
            "Wait for physician",
            "Remove all clothing including needed for pad placement only per modesty"
        ],
        "explanation": "Early application saves time.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-aed",
        "stem": "AED pads for adult are placed:",
        "correct": "One upper right chest, one lower left side below armpit",
        "distractors": [
            "Both on sternum",
            "On back only both",
            "On legs"
        ],
        "explanation": "Follow diagram on pads.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-aed",
        "stem": "Before shock delivery, rescuers should:",
        "correct": "Ensure no one is touching the patient",
        "distractors": [
            "Continue compressions on patient",
            "Hold patient hand",
            "Stand on wet metal"
        ],
        "explanation": "Clear the patient and shout \"stand clear.\"",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-aed",
        "stem": "AED analyzes rhythm during:",
        "correct": "Pause in compressions per device",
        "distractors": [
            "Continuous compressions always",
            "Patient walking",
            "Never"
        ],
        "explanation": "Minimize pause but allow analysis.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-aed",
        "stem": "Shockable rhythms for AED include:",
        "correct": "VF and pulseless VT",
        "distractors": [
            "Asystole and PEA",
            "Normal sinus",
            "Sinus bradycardia with pulse"
        ],
        "explanation": "AED advises shock only for shockable rhythms.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-aed",
        "stem": "After AED shock, immediately:",
        "correct": "Resume CPR for 2 minutes or per prompt",
        "distractors": [
            "Check pulse for 2 minutes",
            "Remove pads",
            "Stop all care"
        ],
        "explanation": "CPR continues unless signs of life.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-aed",
        "stem": "AED use with implanted pacemaker:",
        "correct": "Avoid placing pad directly over device",
        "distractors": [
            "Forbidden entirely",
            "Requires higher energy always",
            "Pads on pacemaker only"
        ],
        "explanation": "Adjust pad placement per training.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "cpr-aed",
        "stem": "AED on wet surface requires:",
        "correct": "Moving to dry area and drying chest if safe",
        "distractors": [
            "Shock anyway in puddle",
            "Only towel over head",
            "No modification"
        ],
        "explanation": "Water conducts electricity; ensure dry chest.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-aed",
        "stem": "Pediatric AED dose attenuation:",
        "correct": "Reduces energy for child per device",
        "distractors": [
            "Increases to maximum always",
            "Disables shock",
            "Is optional always"
        ],
        "explanation": "Use child capability when available.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-aed",
        "stem": "Hair on chest may interfere with AED pads; solution is:",
        "correct": "Press firmly or use razor if needed per protocol",
        "distractors": [
            "Skip AED",
            "Use gel only",
            "Place on hair without prep"
        ],
        "explanation": "Poor contact impedes analysis and shock.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-aed",
        "stem": "AED maintenance in facility includes:",
        "correct": "Checking battery and pads per schedule",
        "distractors": [
            "Ignoring expiration",
            "Storing unplugged always",
            "Removing from public areas"
        ],
        "explanation": "Ready devices improve chain of survival.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-aed",
        "stem": "If AED advises no shock:",
        "correct": "Resume CPR; rhythm may be non-shockable",
        "distractors": [
            "Remove pads and leave",
            "Stop all resuscitation",
            "Repeat shock anyway"
        ],
        "explanation": "Treat per BLS/ACLS for PEA/asystole pathways.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "Mild choking in responsive adult is managed with:",
        "correct": "Encouraging cough if effective",
        "distractors": [
            "Immediate CPR",
            "Blind finger sweep",
            "Abdominal thrusts always"
        ],
        "explanation": "Monitor; intervene if becomes severe.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-choking",
        "stem": "Severe choking responsive adult receives:",
        "correct": "Abdominal thrusts (Heimlich)",
        "distractors": [
            "Back blows only in US adult algorithm alone",
            "Chest compressions first",
            "No intervention"
        ],
        "explanation": "Thrusts increase airway pressure to expel object.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-choking",
        "stem": "Unresponsive choking victim requires:",
        "correct": "CPR starting with compressions; look in mouth before breaths",
        "distractors": [
            "Finger sweeps blindly",
            "Only back blows",
            "Wait for EMS without CPR"
        ],
        "explanation": "CPR may relieve obstruction.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "Pregnant or obese choking patient may receive:",
        "correct": "Chest thrusts instead of abdominal thrusts",
        "distractors": [
            "No help",
            "Only fluids",
            "Heimlich in water"
        ],
        "explanation": "Chest thrusts reduce abdominal injury risk.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "Infant choking responsive care uses:",
        "correct": "5 back slaps then 5 chest thrusts cycles",
        "distractors": [
            "Abdominal thrusts",
            "Only CPR",
            "Finger sweeps first"
        ],
        "explanation": "Support head and jaw; keep head lower than trunk.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "After relieving choking, patient should:",
        "correct": "Be evaluated medically even if seems fine",
        "distractors": [
            "Be sent home without assessment",
            "Avoid all food forever",
            "Drive self to work"
        ],
        "explanation": "Complications like swelling can occur.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-choking",
        "stem": "Difference between mild and severe airway obstruction:",
        "correct": "Effective cough vs poor air exchange and silent cough",
        "distractors": [
            "Color of skin only",
            "Age only",
            "Presence of fever"
        ],
        "explanation": "Severe obstruction needs immediate action.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "If choking victim becomes unconscious during back blows:",
        "correct": "Lower to ground and begin CPR",
        "distractors": [
            "Continue back blows only",
            "Leave on chair",
            "Shake vigorously"
        ],
        "explanation": "Start CPR per unresponsive choking algorithm.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "Conscious child severe choking may use:",
        "correct": "Abdominal thrusts appropriate to size",
        "distractors": [
            "Adult-only technique always",
            "No intervention",
            "Only oxygen"
        ],
        "explanation": "Adjust force for child body habitus.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "Do not perform blind finger sweeps because:",
        "correct": "May push object deeper",
        "distractors": [
            "Always effective",
            "Required in all choking",
            "Replaces thrusts"
        ],
        "explanation": "Visualize mouth only if object seen.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "Partial airway obstruction signs include:",
        "correct": "Stridor, wheezing, and some air movement",
        "distractors": [
            "No sound at all always",
            "Normal speech",
            "Only cyanosis without distress"
        ],
        "explanation": "Monitor closely; may worsen.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-choking",
        "stem": "EMS activation for choking is needed when:",
        "correct": "Obstruction is not relieved or victim is unresponsive",
        "distractors": [
            "Patient coughs once",
            "After water sip",
            "Never"
        ],
        "explanation": "Advanced care may be required.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-chain",
        "stem": "The first link in the adult out-of-hospital Chain of Survival is:",
        "correct": "Recognition and activation of emergency response",
        "distractors": [
            "Defibrillation",
            "Advanced airway",
            "Post-arrest care"
        ],
        "explanation": "Early recognition and calling for help start the chain.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-chain",
        "stem": "Early CPR in the chain of survival:",
        "correct": "Improves oxygen delivery until defibrillation",
        "distractors": [
            "Replaces need for EMS",
            "Is optional",
            "Only for children"
        ],
        "explanation": "Bystander CPR doubles survival potential.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-chain",
        "stem": "Rapid defibrillation is critical because:",
        "correct": "VF/pulseless VT may respond to early shock",
        "distractors": [
            "Asystole always shocks",
            "It cools the brain",
            "It replaces compressions entirely"
        ],
        "explanation": "Time to shock matters.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-chain",
        "stem": "Advanced life support link includes:",
        "correct": "Airway management, medications, and advanced monitoring",
        "distractors": [
            "Only bandaging",
            "Registration at hospital desk",
            "Patient education only"
        ],
        "explanation": "EMS/hospital teams provide ACLS.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-chain",
        "stem": "Integrated post-cardiac arrest care focuses on:",
        "correct": "Optimizing oxygenation, blood pressure, and targeted temperature management per protocol",
        "distractors": [
            "Immediate discharge",
            "No monitoring",
            "Only family notification"
        ],
        "explanation": "Post-arrest care affects neurologic outcome.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "cpr-chain",
        "stem": "Public access defibrillation programs aim to:",
        "correct": "Place AEDs where arrest is likely and train lay rescuers",
        "distractors": [
            "Remove AEDs from airports",
            "Replace CPR training",
            "Eliminate EMS"
        ],
        "explanation": "Community AEDs shorten time to shock.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-chain",
        "stem": "Bystander CPR rates are improved by:",
        "correct": "Training and dispatcher-assisted CPR instructions",
        "distractors": [
            "Hiding AEDs",
            "Discouraging lay help",
            "Removing 911 access"
        ],
        "explanation": "Education strengthens the chain.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    },
    {
        "topic": "cpr-chain",
        "stem": "Pediatric chain of survival emphasizes:",
        "correct": "Prevention of injury and illness as well as early CPR",
        "distractors": [
            "Only defibrillation",
            "No prevention link",
            "Adult-only steps"
        ],
        "explanation": "Injury prevention reduces pediatric arrest.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-chain",
        "stem": "Recovery phase after cardiac arrest may include:",
        "correct": "Rehabilitation and psychological support",
        "distractors": [
            "No follow-up",
            "Immediate return to driving always",
            "Ignoring depression"
        ],
        "explanation": "Survivors need structured recovery.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "cpr-chain",
        "stem": "Team-based resuscitation improves:",
        "correct": "Compression quality and role clarity",
        "distractors": [
            "Confusion only",
            "Delays defibrillation always",
            "Documentation errors only"
        ],
        "explanation": "Clear roles during in-hospital arrest.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "intermediate"
    },
    {
        "topic": "cpr-chain",
        "stem": "Continuous quality improvement in resuscitation uses:",
        "correct": "Data review and debriefing",
        "distractors": [
            "Ignoring outcomes",
            "No training updates",
            "Single rescuer only"
        ],
        "explanation": "Measurement improves systems.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "advanced"
    },
    {
        "topic": "cpr-chain",
        "stem": "Telephone CPR instructions help:",
        "correct": "Bystanders start compressions before EMS arrival",
        "distractors": [
            "Delay activation",
            "Replace AED",
            "Eliminate need for EMS"
        ],
        "explanation": "Dispatchers coach immediate action.",
        "references": [
            "AHA BLS"
        ],
        "difficulty": "beginner"
    }
]
