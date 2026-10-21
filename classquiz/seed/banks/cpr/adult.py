# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hand-authored adult BLS CPR questions (topic cpr-adult)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
 fact(
 "cpr-adult",
 "What compression-to-ventilation ratio should a single rescuer use during adult BLS CPR?",
 "30:2",
 [
 "15:2, because pediatric two-rescuer ratios apply to all ages",
 "5:1, alternating heavy compressions with single breaths",
 "Continuous compressions with no ventilations in every arrest",
 ],
 "AHA adult BLS uses 30 compressions followed by 2 ventilations for a lone rescuer. "
 "15:2 is tempting because learners memorize it for two-rescuer child CPR, but adult "
 "BLS stays 30:2 regardless of rescuer number.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "What is the minimum recommended compression depth for adult BLS CPR?",
 "2 inches (5 cm) but not more than 2.4 inches (6 cm)",
 [
 "About 1 inch (2.5 cm) to avoid rib injury",
 "At least 3 inches (7.5 cm) for every adult regardless of size",
 "Visible sternal movement, with no minimum depth",
 ],
 "AHA targets at least 2 inches (5 cm) with an upper limit near 2.4 inches (6 cm) to "
 "balance perfusion and injury risk. One inch is a common underestimate that fails to "
 "generate adequate coronary pressure during arrest.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "What chest compression rate should rescuers use during adult CPR?",
 "100 to 120 per minute",
 [
 "60 to 80 per minute for easier fatigue management",
 "140 to 160 per minute to maximize output",
 "Match the patient's resting pulse if known",
 ],
 "AHA specifies 100 to 120 compressions per minute for adults. Slower rates often follow "
 "from fatigue or hesitation, while very fast rates usually sacrifice depth, both reduce "
 "high-quality CPR.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "Where should rescuers place their hands for adult chest compressions?",
 "Center of chest on lower half of sternum",
 [
 "Directly over the xiphoid process at the tip of the sternum",
 "Upper abdomen just below the rib cage",
 "Left side of the chest over the cardiac apex",
 ],
 "Hand placement on the lower half of the sternum directs force through the heart. "
 "Compressing the xiphoid or upper abdomen is a frequent placement error that reduces "
 "effectiveness and increases injury risk per AHA adult BLS guidance.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "After activating emergency response for an unresponsive adult, what should you assess before starting CPR?",
 "Breathing and pulse simultaneously if trained (no more than 10 seconds)",
 [
 "Blood glucose with a fingerstick before chest contact",
 "Blood pressure with a cuff while the patient lies flat",
 "Core temperature to rule out hypothermic arrest",
 ],
 "Trained rescuers check breathing and pulse together for no more than about 10 seconds "
 "to avoid harmful delays. Checking glucose or blood pressure first wastes critical time; "
 "AHA adult BLS prioritizes rapid arrest recognition.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "What is required for proper chest recoil during adult CPR?",
 "Allowing full chest return without leaning",
 [
 "Maintaining partial pressure on the chest between compressions",
 "Using shallow rapid pumps without full expansion",
 "Locking elbows and leaning body weight on the sternum continuously",
 ],
 "Full recoil lets the heart refill during diastole so the next compression can perfuse "
 "the brain and myocardium. Leaning on the chest between compressions is a subtle error "
 "that AHA high-quality CPR metrics specifically discourage.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How should rescue breaths be delivered during adult CPR?",
 "Make chest rise over about 1 second each",
 [
 "Deliver forceful gusts under half a second each",
 "Give two quick breaths lasting about 5 seconds each",
 "Skip ventilations until EMS places an advanced airway",
 ],
 "Each breath should produce visible chest rise over roughly one second, limiting "
 "ventilation volume and interruption time. Forceful rapid breaths risk gastric inflation "
 "and longer pauses in compressions, contrary to AHA adult BLS.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "When should rescuers apply an AED during adult cardiac arrest?",
 "As soon as available for cardiac arrest",
 [
 "After five minutes of uninterrupted compressions have run",
 "When the patient regains a cough or gag reflex",
 "Before confirming unresponsiveness and activating EMS",
 ],
 "Early defibrillation is a core link in the Chain of Survival; attach the AED as soon as "
 "it arrives while minimizing compression pauses. Waiting several minutes or delaying until "
 "the patient speaks misses shockable rhythms that respond to prompt AED use.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "How should rescuers manage interruptions in chest compressions during adult CPR?",
 "Minimized, especially for rhythm analysis and shocks",
 [
 "Scheduled for at least 30 seconds each minute for rescuer rest",
 "Extended during AED use to allow complete team discussion",
 "Avoided entirely even when the AED must analyze rhythm",
 ],
 "Coronary perfusion pressure drops quickly when compressions stop. AHA emphasizes "
 "limiting pauses, often under about 10 seconds when possible, even when integrating AED "
 "rhythm checks and shocks.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "What compression-to-ventilation approach should two rescuers use during adult BLS CPR?",
 "30:2 with rescuers switching roles",
 [
 "15:2 because two rescuers use the pediatric ratio",
 "5:1 with one rescuer compressing between every breath",
 "Compressions with no ventilations for all team responses",
 ],
 "Adult two-rescuer CPR remains 30:2; rescuers switch compressor duty about every two "
 "minutes to fight fatigue. 15:2 applies to two-rescuer child CPR, not adult BLS, a common "
 "crossover mistake on exams.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How should rescuers interpret agonal gasps in an unresponsive adult?",
 "May be sign of cardiac arrest, not normal breathing",
 [
 "Indicate adequate ventilation so CPR is not needed",
 "Require supplemental oxygen without compressions",
 "Rule out cardiac arrest unless the patient can speak",
 ],
 "Agonal respirations are ineffective gasps that may occur during arrest and are not "
 "normal breathing. Treating them as reassuring delays CPR; AHA adult BLS directs CPR "
 "when breathing is absent or not normal.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "Which elements best describe high-quality adult CPR?",
 "Hard fast compressions, full recoil, minimal interruptions",
 [
 "Slow shallow compressions with frequent long pauses",
 "Fast compressions while leaning on the chest between cycles",
 "Gentle compressions focused on ventilation quality",
 ],
 "High-quality CPR combines adequate rate and depth, full recoil, and limited pauses. "
 "Slow shallow compressions feel easier but fail to maintain perfusion, AHA high-quality "
 "CPR standards require the harder, faster approach.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "During adult BLS, which chest compression rate should rescuers deliver?",
 "100 to 120 compressions per minute",
 [
 "80 to 90 compressions per minute for deeper strokes",
 "130 to 150 compressions per minute without regard to depth",
 "40 to 60 compressions per minute when two rescuers are present",
 ],
 "The adult rate window is 100 to 120 per minute whether one or two rescuers are present. "
 "Choosing 80 to 90 confuses a desired depth goal with rate; AHA keeps rate and depth "
 "targets separate but equally important.",
 [S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "What compression-to-ventilation ratio should a single rescuer use for adult CPR?",
 "30:2",
 [
 "15:2 for all patients when an AED is en route",
 "10:1 to emphasize ventilation in adult arrest",
 "50:2 to minimize interruption of compressions",
 ],
 "Single-rescuer adult CPR is consistently 30:2 in AHA guidelines. 15:2 is reserved for "
 "two-rescuer pediatric BLS, not lone adult rescuers.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "What compression-to-ventilation ratio should two rescuers use during adult BLS CPR?",
 "30:2",
 [
 "15:2 because additional rescuers change the ratio",
 "30:1 with breaths after each minute of compressions",
 "Continuous compressions with asynchronous ventilations every 30 seconds",
 ],
 "Adding a second rescuer does not change the adult 30:2 ratio; it enables role switching "
 "and better ventilation technique. Assuming 15:2 whenever two people are present mixes "
 "pediatric and adult algorithms.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "When checking for a pulse during adult CPR, how long should compressions be paused at most?",
 "As short as possible, under about 10 seconds for pulse checks",
 [
 "Up to 30 seconds to confirm absence of circulation",
 "Until a second rescuer agrees pulse is absent",
 "During AED charging, with no limit for manual checks",
 ],
 "Prolonged pulse checks erode coronary perfusion pressure built by compressions. AHA "
 "adult BLS limits pulse assessment to about 10 seconds; 30-second pauses are far too long.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "An unresponsive adult is not breathing normally after you activate emergency response. What should you do first if you are trained in BLS?",
 "Start CPR beginning with compressions for trained lay rescuers in many programs",
 [
 "Wait for EMS arrival before starting chest compressions",
 "Begin two minutes of rescue breaths before compressions",
 "Place the patient in a recovery position and observe",
 ],
 "For unresponsive adults without normal breathing, trained lay rescuers in many AHA "
 "courses start with compressions (CAB). Waiting for EMS or breaths-only care delays "
 "circulatory support in likely cardiac arrest.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "Where should the heel of the hand be placed for adult chest compressions?",
 "Heel of hand on lower half of sternum",
 [
 "Heel of hand centered over the upper sternum near the clavicles",
 "Heel of hand on the epigastric region below the ribs",
 "Heel of hand on the left lateral chest wall",
 ],
 "The heel of one hand (plus the second hand interlocked) presses on the lower sternum. "
 "Upper sternum or epigastric placement is a near-miss error that reduces stroke volume "
 "during compressions.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "What does full chest recoil mean during high-quality CPR?",
 "Allow chest to return fully without leaning on chest",
 [
 "Keep hands in contact while applying downward pressure between compressions",
 "Release hands completely off the chest for two seconds each cycle",
 "Pause compressions for five seconds after every tenth compression",
 ],
 "Recoil means the sternum returns to its resting position without residual load from the "
 "rescuer. Maintaining pressure between compressions mimics leaning and is specifically "
 "discouraged in AHA high-quality CPR guidance.",
 [S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How long should each rescue breath last during adult CPR?",
 "1 second each making visible chest rise",
 [
 "About 3 seconds each to maximize oxygen delivery",
 "Until the rescuer feels resistance from the airway",
 "Half a second with maximum force to reduce pause time",
 ],
 "AHA specifies roughly one second per breath with visible chest rise. Three-second breaths "
 "extend interruption time; ultra-short forceful breaths risk insufflation injury and poor "
 "ventilation coordination.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How can rescuers reduce fatigue and maintain compression quality during prolonged CPR?",
 "Switch compressors every 2 minutes or sooner if quality drops",
 [
 "Have one rescuer compress continuously for at least 15 minutes",
 "Reduce depth to 1 inch after the first two minutes",
 "Stop compressions for two minutes of team rest every five minutes",
 ],
 "Compressor switching about every two minutes preserves depth and rate as fatigue sets in. "
 "Letting one person compress for many minutes or scheduled long rests both degrade "
 "compression fraction against AHA recommendations.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "An unresponsive adult has only agonal gasps. How should you interpret this breathing pattern?",
 "Are not normal breathing; start CPR if no normal breathing",
 [
 "Represent effective respiration requiring an oxygen mask",
 "Mean the patient is breathing adequately so pulse check can wait several minutes",
 "Require abdominal thrusts before starting compressions",
 ],
 "Agonal gasps are not adequate breathing and often signal arrest. Oxygen alone without "
 "compressions misses the circulation support AHA adult BLS requires when breathing is "
 "not normal.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "When an AED arrives while you are performing adult CPR, what is the best sequence of actions?",
 "Apply pads and follow prompts with minimal compression pause",
 [
 "Stop all CPR until the AED finishes three full analysis cycles",
 "Finish five minutes of compressions before opening the AED case",
 "Have one rescuer continue compressions while pads are placed on clothing",
 ],
 "Integrate the AED promptly: power on, attach pads to bare skin, and follow voice prompts "
 "while limiting compression gaps. Continuing on clothing or delaying application several "
 "minutes postpones possible defibrillation.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "If you suspect opioid overdose in an unresponsive adult, what BLS actions are appropriate while EMS is activated?",
 "Provide ventilation support and naloxone per protocol while activating EMS",
 [
 "Withhold all ventilations until naloxone fully awakens the patient",
 "Perform abdominal thrusts before starting breaths or compressions",
 "Delay EMS activation until family confirms substance use",
 ],
 "AHA opioid-associated emergencies still require airway support and CPR when indicated; "
 "naloxone may be given per local protocol while EMS is en route. Withholding ventilations "
 "until the patient wakes leaves them apneic without support.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "After return of spontaneous circulation (ROSC) in an adult, what is the immediate priority?",
 "Monitored with airway and blood pressure support per post-arrest care",
 [
 "Discharge from the scene once a pulse returns",
 "Resume compressions at half depth to maintain circulation",
 "Place upright in a chair and offer oral fluids immediately",
 ],
 "ROSC begins post-arrest care: maintain airway, support breathing, and monitor perfusion. "
 "Stopping all care at the scene or restarting full CPR without re-arrest ignores AHA "
 "integrated post-cardiac arrest management.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "A coworker collapses at a desk. After you confirm the scene is safe and the person is unresponsive, what is your next priority before starting compressions?",
 "Shout for help and activate the emergency response system (call 911 or send someone to call)",
 [
 "Begin two minutes of compressions before anyone notifies EMS",
 "Search distant floors for an AED while leaving the patient unattended",
 "Roll the coworker prone to improve drainage before checking breathing",
 ],
 "Recognition and activation are the first links in the Chain of Survival. Delaying the "
 "911 call to compress first or hunt remotely for an AED slows EMS and defibrillator "
 "response, AHA adult BLS pairs early activation with prompt CPR.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "During two-rescuer adult CPR, one rescuer is giving poor-quality compressions that are too shallow. What is the best team action?",
 "Pause briefly to coach hand placement and depth, then resume 30:2 cycles with a compressor switch if needed",
 [
 "Continue shallow compressions because chest movement is sufficient",
 "Switch to ventilations until depth improves on its own",
 "Stop CPR completely until an AED is physically on the chest",
 ],
 "Depth at least 2 inches (5 cm) with full recoil defines effective compressions. Coaching "
 "and switching compressors addresses fatigue-related shallow compressions; ventilations-only "
 "or accepting shallow depth fails AHA high-quality CPR standards.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "Which compression depth target is correct for most adult victims during BLS CPR?",
 "At least 2 inches (5 cm) but not more than 2.4 inches (6 cm)",
 [
 "Exactly 1 inch (2.5 cm) for all body habitus",
 "At least 3.5 inches (9 cm) for larger adults",
 "Depth is optional if compression rate stays above 120",
 ],
 "AHA adult depth targets balance perfusion and injury. One inch is too shallow for typical "
 "adults, while uncapped deep compression is not recommended, rate alone cannot replace "
 "adequate depth.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "You are performing adult CPR and the victim begins to move and breathe normally. What should you do immediately?",
 "Stop CPR, monitor breathing and pulse, and place the person in a recovery position if no trauma is suspected",
 [
 "Continue 30:2 because movement may be seizure activity",
 "Stop compressions but leave the patient supine without monitoring",
 "End resuscitation and send the patient home without EMS contact",
 ],
 "Purposeful movement with normal breathing signals ROSC or spontaneous recovery; stop "
 "compressions and monitor. Continuing CPR on a breathing patient can cause harm, while "
 "abandoning monitoring misses re-arrest.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "Why does AHA recommend pushing in the center of the chest on the lower half of the sternum?",
 "That location optimizes blood flow through the heart with the least risk of injury to underlying structures",
 [
 "The xiphoid is the strongest point to transmit force to the ventricles",
 "Abdominal compression displaces the diaphragm to compress the heart",
 "A fixed point on the left lateral chest for every body size",
 ],
 "Lower sternal compression maximizes forward flow with less risk to the xiphoid and "
 "abdomen. Xiphoid-focused or lateral-chest landmarks are common misconceptions that do not "
 "match AHA hand-placement teaching.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "A witnessed adult collapse is likely cardiac arrest. What is the preferred approach for a trained lay rescuer who is unwilling or unable to give rescue breaths?",
 "Start high-quality chest compressions immediately and use an AED as soon as it is available",
 [
 "Wait at the bedside until a family member agrees to give breaths",
 "Provide rescue breaths without compressions until EMS arrive",
 "Begin passive oxygen by nasal cannula without chest compressions",
 ],
 "Compression-only CPR is acceptable for witnessed adult arrest when breaths cannot be "
 "given. Breath-only care without compressions does not support circulation in primary "
 "cardiac arrest, AHA emphasizes immediate hard, fast compressions plus early AED.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "During adult CPR you notice the chest does not rise with rescue breaths. What is the best next step before giving more breaths?",
 "Reopen the airway with head tilt-chin lift (or jaw thrust if trauma is suspected) and reattempt a breath over about one second",
 [
 "Increase breath force and duration to five seconds each",
 "Skip all further ventilations and compress for ten minutes straight",
 "Perform blind finger sweeps in the mouth before every breath",
 ],
 "Failed chest rise usually signals airway positioning or seal problems; reposition and "
 "retry with a one-second breath. Forceful long breaths or blind finger sweeps risk gastric "
 "inflation and airway trauma, AHA stresses repositioning first.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "Which action best describes high-quality chest compression fraction during adult resuscitation?",
 "Compressing the chest for most of the resuscitation period with pauses limited to under about 10 seconds for rhythm checks or defibrillation",
 [
 "Pausing compressions for 30 seconds every minute for team planning",
 "Compressing half the time to allow extended ventilation",
 "Stopping compressions whenever a rescuer adjusts equipment",
 ],
 "Compression fraction reflects time on the chest; AHA targets high fraction with brief "
 "pauses for pulse checks and AED use. Scheduled 30-second breaks or 50% compression time "
 "undermine coronary perfusion pressure.",
 [S.AHA_HQ_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "An adult in cardiac arrest has an advanced airway placed by EMS. How should ventilations be provided once the advanced airway is in place?",
 "Continue compressions without pausing for breaths and deliver one breath every 6 seconds (10 breaths per minute)",
 [
 "Pause compressions for 15 seconds to deliver each ventilation",
 "Stop compressions entirely and ventilate once per minute",
 "Resume 30:2 cycles despite the advanced airway in place",
 ],
 "With an advanced airway, compressions are continuous and asynchronous breaths are given "
 "about every six seconds. Returning to 30:2 or long compression pauses for breaths is "
 "incorrect once the airway is secured per AHA adult BLS.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "What is the primary purpose of allowing full chest recoil between compressions?",
 "To let the heart refill with blood during diastole so the next compression can generate perfusion",
 [
 "To give rescuers time to check a pulse between every compression",
 "To reduce compression depth requirements to one inch",
 "To allow the AED to charge without clearing the patient",
 ],
 "Recoil creates diastolic filling time in the chest; without it, subsequent compressions "
 "move less blood. Checking pulse between every compression or shallow depth substitutes "
 "misunderstand recoil's physiologic role in AHA high-quality CPR.",
 [S.AHA_HQ_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "Which metronome or song tempo best matches the adult CPR compression rate target?",
 "100 to 120 compressions per minute",
 [
 "60 to 80 beats per minute like a slow ballad",
 "140 to 160 beats per minute like a fast dance track",
 "Match whatever rate feels least tiring regardless of guidelines",
 ],
 "Training songs near 100 to 120 BPM reinforce the AHA rate window. Slower tempos invite "
 "inadequate rate; arbitrarily fast music often sacrifices depth.",
 [S.AHA_HQ_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "You must stop compressions briefly to attach AED pads. What is the maximum recommended pause for a pulse check during adult BLS?",
 "No more than 10 seconds",
 [
 "Up to 20 seconds if the rescuer is unsure about the pulse",
 "Until two rescuers independently agree pulse is absent",
 "No limit if the patient has a history of cardiac disease",
 ],
 "Pulse checks longer than about 10 seconds significantly reduce perfusion. Waiting for dual "
 "confirmation or extending to 20 seconds conflicts with AHA emphasis on minimizing "
 "interruption time.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "What is the recommended adult BLS compression-to-ventilation ratio for both single- and two-rescuer CPR?",
 "30 compressions to 2 ventilations",
 [
 "15 compressions to 2 ventilations for all adult team responses",
 "30 compressions to 1 ventilation to reduce pause time",
 "50 compressions to 2 ventilations when an AED is present",
 ],
 "Adult BLS uses 30:2 for one or two rescuers. Fifteen to two is the two-rescuer child "
 "ratio, choosing it for adults is a frequent guideline mix-up.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "During team resuscitation, when should compressors switch roles during adult CPR?",
 "About every 2 minutes or sooner if compression quality falls",
 [
 "After return of spontaneous circulation is confirmed",
 "Every 10 minutes to limit hand fatigue",
 "Avoid switching once the first compressor sets the rhythm",
 ],
 "Role switching near two minutes maintains depth and rate as fatigue appears. Ten-minute "
 "stints or never switching invites deteriorating compression quality against AHA team "
 "resuscitation guidance.",
 [S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "When should a lay rescuer stop CPR on an adult who was in cardiac arrest?",
 "When the patient shows obvious signs of life such as purposeful movement and normal breathing",
 [
 "After exactly two minutes regardless of patient response",
 "When a single cough is heard during compressions",
 "When EMS verbally orders cessation over the radio",
 ],
 "Stop when there is clear evidence of circulation and normal breathing; continue otherwise "
 "until EMS takes over. A lone cough or arbitrary two-minute limit does not equal ROSC, AHA "
 "directs reassessment for purposeful movement and adequate respirations.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "During prolonged adult CPR the compressor's rate drifts to about 85 per minute despite "
 "feeling exhausted. What is the best team response while maintaining AHA rate guidance?",
 "Switch compressors about every two minutes and use a metronome or coach to stay near "
 "100 to 120 per minute",
 [
 "Accept the slower rate because deeper compressions matter more than speed alone",
 "Increase rate above 140 per minute to compensate for earlier fatigue",
 "Pause compressions for one minute so the tired rescuer can recover fully",
 ],
 "Fatigue commonly slows rate below 100 even when depth still feels adequate. Switching "
 "compressors and audible pacing keeps rate in the 100 to 120 band without sacrificing "
 "uninterrupted perfusion for a full-minute break.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "What chest compression fraction target reflects high-quality adult CPR?",
 "Greater than 80% when possible",
 [
 "About 50% to balance compressions and prolonged equipment setup",
 "Less than 40% so rescuers can document the event",
 "100% with no pauses even during AED shock delivery",
 ],
 "AHA quality metrics aim for compression fraction above 80% when feasible. Fifty percent "
 "on chest time is far too low; refusing any pause during shock delivery ignores necessary "
 "AED safety clearance.",
 [S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "Why should rescuers minimize interruptions in chest compressions during adult CPR?",
 "Improve coronary perfusion pressure",
 [
 "Reduce the risk of rib fractures during compressions",
 "Allow more time for family discussions at the bedside",
 "Decrease rescuer perspiration during long events",
 ],
 "Interruptions let coronary perfusion pressure fall, starving the myocardium between "
 "compressions. Fracture risk or comfort is secondary, AHA science links minimal pauses to "
 "better arrest outcomes.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "If an adult has a palpable pulse but is not breathing, what should the BLS rescuer provide?",
 "Provide rescue breaths about every 6 seconds (10 breaths/min)",
 [
 "Start immediate chest compressions at 30:2",
 "Give one breath every 30 seconds while checking pulse hourly",
 "Administer passive oxygen without ventilations",
 ],
 "Pulse with poor or absent respirations is respiratory arrest; provide breaths about every "
 "six seconds without compressions. Starting full CPR despite a pulse is a critical "
 "algorithm error in AHA adult BLS.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "When a second rescuer arrives during adult CPR, what should the team do to maintain high-quality compressions?",
 "Switch compressor roles about every 2 minutes",
 [
 "Take over ventilations and avoid compressions",
 "Immediately stop CPR for a full team timeout",
 "Alternate 15:2 cycles because two rescuers are present",
 ],
 "The second rescuer enables rotation and coordinated 30:2 care with switches about every "
 "two minutes. Switching to 15:2 or stopping for extended timeouts misapplies adult BLS "
 "when additional help arrives.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "When may lay rescuers use compression-only CPR for adults?",
 "Adult sudden cardiac arrest when unwilling to give breaths",
 [
 "An unresponsive patient regardless of breathing status",
 "Pediatric drowning victims when alone",
 "Adults with known chronic respiratory disease",
 ],
 "Compression-only CPR is taught for witnessed adult arrest when mouth-to-mouth is declined. "
 "Using it for children or clearly breathing patients does not follow AHA lay rescuer "
 "algorithms.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "Where are AED pads typically placed on an adult chest?",
 "Upper-right chest and lower-left side",
 [
 "Both pads on the anterior midline stacked vertically",
 "Upper-left chest and lower-right abdomen",
 "One pad on the back and one on the thigh",
 ],
 "Standard anterior placement is upper right chest and lower left lateral chest. Stacking "
 "pads midline or using non-diagram placements prevents effective current path through the "
 "heart.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "How should a resuscitation team manage compressor fatigue during adult CPR?",
 "Switching compressors every 2 minutes",
 [
 "Reducing depth to one inch after the first minute",
 "Having the smallest team member compress for the entire event",
 "Alternating five minutes of rest with five minutes of compressions",
 ],
 "Scheduled compressor changes about every two minutes sustain depth and rate. Shrinking "
 "depth or long rest cycles trade away the high-quality compression standard AHA promotes.",
 [S.AHA_HQ_CPR],
 "intermediate",
 ),
]
