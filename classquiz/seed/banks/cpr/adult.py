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
 "30 compressions followed by 2 ventilations (30:2)",
 [
 "15 compressions followed by 2 ventilations for every adult arrest",
 "5 compressions followed by 1 ventilation to shorten pauses between breaths",
 "Continuous compressions with no ventilations until advanced airway placement",
 ],
 "AHA adult BLS uses 30:2 for a lone rescuer on adults. Fifteen-to-two is the two-rescuer "
 "pediatric ratio, and compression-only care is reserved for specific lay-rescuer situations, "
 "not the default ventilated adult algorithm.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "What is the recommended compression depth range for most adults during BLS CPR?",
 "At least 2 inches (5 cm) but not more than 2.4 inches (6 cm)",
 [
 "About 1 inch (2.5 cm) to limit rib and sternal injury during adult CPR",
 "At least 3 inches (7.5 cm) on the sternum for all adult victims",
 "Any visible chest movement without a specified minimum depth target",
 ],
 "AHA targets at least 2 inches (5 cm) with an upper limit near 2.4 inches (6 cm) to balance "
 "perfusion and injury risk. Shallow one-inch compressions rarely generate adequate coronary "
 "and cerebral pressure during arrest.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "Which chest compression rate should rescuers deliver during adult CPR?",
 "100 to 120 compressions per minute",
 [
 "90 to 100 compressions per minute",
 "120 to 140 compressions per minute",
 "140 to 160 compressions per minute",
 ],
 "AHA specifies 100 to 120 compressions per minute for adults. Slower rates often follow "
 "fatigue or hesitation, while very fast rates usually sacrifice depth; both patterns reduce "
 "high-quality CPR.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "Where should rescuers place their hands when performing adult chest compressions?",
 "On the lower half of the sternum in the center of the chest",
 [
 "Directly over the xiphoid process at the distal tip of the sternum",
 "On the upper abdomen just below the costal margin",
 "On the left lateral chest wall over the cardiac apex",
 ],
 "Hand placement on the lower half of the sternum directs force through the heart. "
 "Compressing the xiphoid, epigastrium, or lateral chest is a frequent placement error that "
 "reduces effectiveness and increases injury risk per AHA adult BLS guidance.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "After you activate emergency response for an unresponsive adult, how should a trained rescuer assess circulation and breathing?",
 "Check breathing and pulse together for no more than about 10 seconds",
 [
 "Measure blood glucose with a fingerstick before any chest compressions",
 "Obtain a manual blood pressure reading while the patient remains supine",
 "Assess core temperature first to exclude hypothermic arrest",
 ],
 "Trained rescuers check breathing and pulse simultaneously for no more than about 10 seconds "
 "to avoid harmful delays in starting CPR. Checking glucose, blood pressure, or temperature "
 "first wastes critical time when arrest is likely.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "What does high-quality chest recoil require during adult CPR?",
 "Allow the chest to return fully to its resting position without leaning on the sternum",
 [
 "Maintain light downward pressure on the chest between each compression",
 "Use rapid shallow pumps that do not permit full chest expansion",
 "Keep elbows locked while shifting body weight onto the sternum continuously",
 ],
 "Full recoil lets the heart refill during diastole so the next compression can perfuse the "
 "brain and myocardium. Leaning on the chest between compressions is a subtle error that AHA "
 "high-quality CPR metrics specifically discourage.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How should rescue breaths be delivered during adult CPR when ventilations are included?",
 "Give each breath over about 1 second until visible chest rise is seen",
 [
 "Deliver forceful gusts in under half a second to minimize compression pauses",
 "Give two slow breaths lasting about 5 seconds each for maximal oxygen",
 "Withhold all ventilations until EMS places an advanced airway device",
 ],
 "Each breath should produce visible chest rise over roughly one second, limiting ventilation "
 "volume and interruption time. Forceful rapid breaths risk gastric inflation and longer pauses "
 "in compressions, contrary to AHA adult BLS.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "When should rescuers apply an AED during adult cardiac arrest?",
 "As soon as the device is available while minimizing pauses in compressions",
 [
 "Only after at least five minutes of uninterrupted chest compressions",
 "Only after the patient regains a cough or gag reflex spontaneously",
 "Before confirming unresponsiveness and activating the emergency response system",
 ],
 "Early defibrillation is a core link in the Chain of Survival; attach the AED as soon as it "
 "arrives while limiting compression gaps. Waiting several minutes or delaying until reflexes "
 "return misses shockable rhythms that respond to prompt defibrillation.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "How should rescuers manage pauses in chest compressions during adult CPR?",
 "Keep interruptions as brief as possible, especially for rhythm analysis and shocks",
 [
 "Schedule at least 30 seconds off the chest each minute for rescuer recovery",
 "Extend pauses during AED use to allow a full team briefing at the bedside",
 "Avoid pausing compressions even when the AED must analyze rhythm or deliver a shock",
 ],
 "Coronary perfusion pressure drops quickly when compressions stop. AHA emphasizes limiting "
 "pauses, often under about 10 seconds when possible, even when integrating AED rhythm checks "
 "and shocks.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "What compression-to-ventilation approach should two rescuers use during adult BLS CPR?",
 "30 compressions to 2 ventilations with periodic switching of compressor roles",
 [
 "15 compressions to 2 ventilations because two rescuers always use the pediatric ratio",
 "5 compressions to 1 ventilation with one rescuer compressing between every breath",
 "Continuous compressions with no ventilations for all multi-rescuer adult responses",
 ],
 "Adult two-rescuer CPR remains 30:2; rescuers switch compressor duty about every two minutes "
 "to fight fatigue. Fifteen-to-two applies to two-rescuer child CPR, not adult BLS, a common "
 "crossover mistake on exams.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How should rescuers interpret agonal gasps in an unresponsive adult?",
 "Agonal gasps are not normal breathing and may indicate cardiac arrest",
 [
 "Agonal gasps show adequate ventilation so chest compressions are not needed",
 "Agonal gasps require supplemental oxygen only without starting compressions",
 "Agonal gasps rule out cardiac arrest unless the patient can speak clearly",
 ],
 "Agonal respirations are ineffective gasps that may occur during arrest and are not normal "
 "breathing. Treating them as reassuring delays CPR; AHA adult BLS directs CPR when breathing "
 "is absent or not normal.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "Which combination best describes high-quality adult CPR according to AHA guidance?",
 "Hard and fast compressions, full chest recoil, and minimal interruptions",
 [
 "Slow shallow compressions with frequent long pauses for pulse checks",
 "Fast compressions while leaning on the chest between compression cycles",
 "Gentle compressions with primary focus on rescue breath volume alone",
 ],
 "High-quality CPR combines adequate rate and depth, full recoil, and limited pauses. Slow "
 "shallow compressions feel easier but fail to maintain perfusion; AHA high-quality CPR "
 "standards require the harder, faster approach with full recoil.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "An adult is found unresponsive at work. After you confirm the scene is safe, what should you do next before starting compressions?",
 "Check responsiveness, shout for help, and activate the emergency response system",
 [
 "Begin two minutes of chest compressions before anyone notifies emergency services",
 "Search distant floors for an AED while leaving the patient unattended",
 "Roll the patient prone to improve drainage before assessing breathing",
 ],
 "Recognition and activation are early links in the Chain of Survival. Delaying the emergency "
 "call to compress first or leaving the patient to hunt remotely for an AED slows EMS and "
 "defibrillator response.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "An unresponsive adult is not breathing normally after emergency response is activated. "
 "What should a trained lay rescuer do first?",
 "Begin chest compressions before rescue breaths (CAB sequence)",
 [
 "Wait for EMS on scene before starting any chest compressions",
 "Give two minutes of rescue breaths before delivering any compressions",
 "Place the patient in recovery position and observe without compressions",
 ],
 "For unresponsive adults without normal breathing, AHA adult BLS starts with compressions "
 "(CAB). Waiting for EMS or providing breaths-only care delays circulatory support in likely "
 "cardiac arrest.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "A witnessed adult collapse is likely cardiac arrest. What should a trained lay rescuer do if unwilling or unable to give rescue breaths?",
 "Start high-quality chest compressions immediately and use an AED when available",
 [
 "Wait at the bedside until another person agrees to provide rescue breaths",
 "Provide rescue breaths only without compressions until EMS takes over care",
 "Begin passive oxygen by nasal cannula without chest compressions",
 ],
 "Compression-only CPR is acceptable for witnessed adult arrest when breaths cannot be given. "
 "Breath-only care without compressions does not support circulation in primary cardiac arrest; "
 "AHA emphasizes immediate hard, fast compressions plus early AED use.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "When checking for a pulse during adult BLS, how long should compressions be paused at most?",
 "No more than about 10 seconds for the pulse assessment",
 [
 "Up to 30 seconds to be certain circulation is absent before compressing",
 "Until a second rescuer independently agrees that no pulse is present",
 "Only during AED charging, with no time limit for manual pulse checks",
 ],
 "Prolonged pulse checks erode coronary perfusion pressure built by compressions. AHA adult "
 "BLS limits pulse assessment to about 10 seconds; 30-second pauses or open-ended checks are "
 "far too long.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How should rescuers position their upper body when delivering adult chest compressions?",
 "Shoulders directly over the hands with elbows extended, pushing straight down on the sternum",
 [
 "Arms bent at 90 degrees with force directed at an angle toward the patient's feet",
 "Torso angled away from the chest while compressing with minimal elbow extension",
 "Hands on the lower sternum while compressing from a kneeling position far behind the head",
 ],
 "Vertical alignment over the sternum maximizes depth and minimizes rescuer fatigue. Angled or "
 "flexed-elbow technique reduces effective depth and is inconsistent with AHA compression "
 "mechanics teaching.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "How can rescuers reduce fatigue and maintain compression quality during prolonged adult CPR?",
 "Switch compressors about every 2 minutes or sooner if quality drops",
 [
 "Have one rescuer compress continuously for at least 15 minutes without switching",
 "Reduce compression depth to about 1 inch after the first two minutes of CPR",
 "Stop compressions for two minutes of team rest every five minutes of resuscitation",
 ],
 "Compressor switching about every two minutes preserves depth and rate as fatigue sets in. "
 "Letting one person compress for many minutes or scheduling long rests both degrade "
 "compression fraction against AHA recommendations.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "During adult CPR you notice the chest does not rise with a rescue breath. What is the best next step?",
 "Reopen the airway with head tilt-chin lift and give another breath over about one second",
 [
 "Increase breath force and duration to about 5 seconds for each ventilation",
 "Skip all further ventilations and compress continuously for ten minutes",
 "Perform blind finger sweeps in the mouth before every subsequent breath",
 ],
 "Failed chest rise usually signals airway positioning or seal problems; reposition and retry "
 "with a one-second breath. Forceful long breaths or blind finger sweeps risk gastric inflation "
 "and airway trauma; AHA stresses repositioning first.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "An unresponsive adult has only agonal gasps after you shout and tap. What is the appropriate BLS action?",
 "Agonal gasps are not normal breathing; begin CPR when breathing is absent or not normal",
 [
 "Agonal gasps indicate effective respiration requiring a non-rebreather mask only",
 "Agonal gasps mean breathing is adequate so a pulse check can wait several minutes",
 "Agonal gasps require abdominal thrusts before any chest compressions are started",
 ],
 "Agonal gasps are not adequate breathing and often signal arrest. Oxygen or observation alone "
 "without compressions misses the circulation support AHA adult BLS requires when breathing is "
 "not normal.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "When an AED arrives while adult CPR is in progress, what sequence best follows AHA guidance?",
 "Apply pads to bare skin and follow prompts while limiting pauses in compressions",
 [
 "Stop all CPR until the AED completes three full rhythm analysis cycles",
 "Finish five minutes of compressions before opening the AED and attaching pads",
 "Continue compressions while AED pads remain placed over clothing and belts",
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
 "Support breathing with ventilations, perform CPR if pulseless, and give naloxone when available",
 [
 "Give naloxone and wait for spontaneous breathing before providing any ventilations",
 "Perform abdominal thrusts before rescue breaths or chest compressions",
 "Delay EMS activation until the substance involved is confirmed",
 ],
 "AHA opioid-associated emergencies still require airway support and CPR when indicated; "
 "naloxone may be given while EMS is en route but does not replace ventilations or "
 "compressions when arrest criteria are met.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "After return of spontaneous circulation (ROSC) in an adult, what is the immediate BLS priority?",
 "Monitor breathing and perfusion and support the airway while awaiting advanced care",
 [
 "Discharge the patient from the scene once a palpable pulse returns",
 "Resume chest compressions at half depth to maintain forward blood flow",
 "Place the patient upright in a chair and stop all monitoring once pulse returns",
 ],
 "ROSC begins post-arrest care: maintain airway, support breathing, and monitor perfusion. "
 "Stopping all care at the scene or restarting full CPR without re-arrest ignores AHA integrated "
 "post-cardiac arrest management.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "When should a lay rescuer stop CPR on an adult who was in cardiac arrest?",
 "When the patient shows purposeful movement and begins breathing normally",
 [
 "After exactly two minutes of CPR even when breathing and movement look normal",
 "When a single cough is heard once during ongoing compressions",
 "Only after EMS verbally orders cessation over the emergency radio",
 ],
 "Stop when there is clear evidence of circulation and normal breathing; continue otherwise "
 "until EMS takes over. A lone cough or an arbitrary two-minute limit does not equal ROSC; "
 "AHA directs reassessment for purposeful movement and adequate respirations.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "Where should AED electrode pads be placed on an adult chest during cardiac arrest?",
 "Upper-right chest below the clavicle and lower-left lateral chest below the armpit",
 [
 "Both pads stacked vertically along the midline of the anterior chest",
 "Upper-left chest and lower-right quadrant of the abdomen as a fixed pair",
 "One pad on the posterior thorax and one pad on the anterior thigh",
 ],
 "Standard anterior placement routes current through the heart from upper right to lower left. "
 "Stacked midline or non-diagram placements prevent an effective defibrillation path per "
 "AHA AED instructions for adults.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "An unresponsive adult is on a soft mattress during CPR and compressions feel ineffective. What surface adjustment best supports high-quality compressions?",
 "Move the patient to a firm flat surface before continuing compressions",
 [
 "Continue on the mattress because depth targets are unchanged on soft bedding",
 "Elevate the head of the bed to maximum height to improve blood return",
 "Compress only the lower ribs while leaving the sternum unsupported on the mattress",
 ],
 "AHA emphasizes a firm surface so compressions translate into sternal depression rather than "
 "mattress absorption. Head-up positioning or rib-only pumping does not substitute for stable "
 "hand placement on the lower sternum during adult BLS.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "During two-rescuer adult CPR, compressions measure about 1.5 inches despite full rescuer effort. What is the best immediate team response?",
 "Reposition on the lower sternum and compress to at least 2 inches (5 cm)",
 [
 "Accept 1.5 inches because any sternal movement creates some forward flow",
 "Stop chest compressions and provide ventilations only until depth improves on its own",
 "Wait to resume compressions until an AED is physically resting on the chest",
 ],
 "Adult BLS requires at least about 2 inches of depth with full recoil. Shallow compressions "
 "with good effort usually reflect placement or fatigue; coaching and compressor rotation "
 "address both without abandoning circulation support.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "Real-time feedback shows an adult victim is receiving compressions at about 1.5 inches depth during BLS. What target depth should the team aim for next?",
 "At least 2 inches (5 cm) but not more than about 2.4 inches (6 cm) for most adults",
 [
 "Exactly 1 inch (2.5 cm) for all adults to minimize rib injury risk",
 "At least 3.5 inches (9 cm) on the sternum for all adult victims",
 "Any visible chest motion without a measured depth target during arrest care",
 ],
 "One-and-a-half-inch compressions fall below the AHA minimum that generates useful coronary "
 "and cerebral perfusion. The guideline window caps depth near 2.4 inches to balance output "
 "with injury risk rather than relying on visible movement alone.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "After ROSC, an adult breathes normally and moves purposefully, and no trauma is suspected. What should BLS rescuers do while awaiting EMS?",
 "Stop compressions and monitor breathing and pulse until EMS arrives",
 [
 "Continue 30:2 cycles because post-arrest movement may still represent seizure activity",
 "Stop compressions and leave the patient flat without further monitoring or positioning",
 "Stop compressions and leave the patient unattended once movement is seen",
 ],
 "Normal breathing with purposeful movement indicates circulation has returned; ongoing "
 "compressions can injure a perfusing patient. Monitoring and recovery positioning support "
 "the airway while EMS manages post-arrest assessment and transport.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "When performing adult chest compressions, how should the rescuer position the hands on the chest?",
 "Heel of one hand on the lower half of the sternum with the second hand on top and fingers lifted off the ribs",
 [
 "Fingers interlaced over the xiphoid process to anchor compressions at the sternal tip",
 "Both palms flat on the upper abdomen to displace the diaphragm with each push",
 "One hand on the left lateral chest wall at the mid-axillary line for all body sizes",
 ],
 "The heel of the hand on the lower sternum directs force through the heart while keeping "
 "fingers off the ribs reduces injury and wasted pressure. Xiphoid, abdominal, and lateral "
 "landmarks are frequent placement errors in AHA adult BLS teaching.",
 [S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "A lay rescuer witnesses an adult collapse from apparent sudden cardiac arrest but refuses mouth-to-mouth ventilations. What care still aligns with AHA lay rescuer guidance?",
 "Deliver continuous high-quality chest compressions and apply an AED as soon as one is available",
 [
 "Delay all compressions until a bystander agrees to provide rescue breaths at the scene",
 "Provide rescue breaths every six seconds without any chest compressions until EMS arrives",
 "Place the patient on supplemental oxygen through a nasal cannula without starting compressions",
 ],
 "Witnessed adult arrest still requires immediate circulation support; compression-only CPR is "
 "acceptable when breaths are declined. Breath-only care or passive oxygen without "
 "compressions does not treat primary cardiac arrest in AHA lay rescuer algorithms.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "During 30:2 adult CPR you give a rescue breath and the chest does not rise. What is the best next action before additional ventilations?",
 "Reopen the airway and give another breath over about one second",
 [
 "Deliver each subsequent breath with maximal force for about five seconds until resistance is felt",
 "Stop all ventilations for ten minutes and compress continuously without further breath attempts",
 "Perform blind finger sweeps in the mouth before every rescue breath attempt",
 ],
 "Absent chest rise usually means the airway is not open or the seal is poor; reposition and "
 "retry with a one-second breath. Forceful prolonged breaths and blind sweeps increase gastric "
 "inflation and trauma risk without fixing positioning, which AHA lists first.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "Which description best matches a high chest compression fraction during adult resuscitation?",
 "Keep compressions going for most of the event and limit pauses to brief rhythm checks or defibrillation",
 [
 "Pause compressions for about 30 seconds each minute so the team can plan roles aloud",
 "Compress the chest only about half of the time to prioritize prolonged bag-mask ventilation",
 "Stop compressions whenever equipment is adjusted even if no rhythm check is needed",
 ],
 "Compression fraction is the proportion of time with active compressions; AHA links higher "
 "fraction to better perfusion when pauses stay short. Scheduled half-minute breaks or "
 "compressing half the time let coronary perfusion pressure collapse between cycles.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "EMS secures an advanced airway in an adult who remains in cardiac arrest. How should the resuscitation team ventilate while compressions continue?",
 "Give one breath about every 6 seconds without pausing compressions for each ventilation",
 [
 "Pause compressions for about 15 seconds every time a breath is delivered through the tube",
 "Stop all compressions and provide one breath per minute until ROSC or termination",
 "Return to 30 compressions followed by 2 ventilations despite the secured advanced airway",
 ],
 "Once an advanced airway is in place, compressions are continuous and breaths are given "
 "asynchronously about every six seconds. Long pauses or reverting to 30:2 after intubation "
 "contradicts AHA adult BLS airway management during ongoing arrest.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "During adult CPR a teammate keeps leaning on the chest between compressions so the sternum never fully rises. What problem does that create?",
 "Incomplete recoil reduces diastolic filling so later compressions generate less blood flow",
 [
 "Leaning between compressions is encouraged because it steadies hand placement on the sternum",
 "Incomplete recoil primarily lowers compression rate below 100 per minute",
 "Incomplete recoil is acceptable whenever compression depth exceeds 2.4 inches",
 ],
 "Full recoil allows the chest to refill during diastole; leaning keeps the heart and great "
 "vessels partially compressed. AHA high-quality CPR metrics treat incomplete recoil as a "
 "correctable performance error, not a technique that stabilizes hands or replaces depth.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "A CPR instructor asks which audible pacing tempo best helps rescuers stay within the adult compression rate guideline. What rate should they target?",
 "About 100 to 120 compressions per minute when using a metronome or pacing song",
 [
 "About 60 to 80 beats per minute to match a slow ballad and reduce rescuer fatigue",
 "About 140 to 160 beats per minute to match fast dance music and maximize output",
 "Any tempo that feels comfortable because rate guidelines do not apply during real arrests",
 ],
 "AHA specifies 100 to 120 compressions per minute for adults; training metronomes in that "
 "range reinforce the target window. Slower music invites subtherapeutic rate, while very "
 "fast pacing often trades away adequate depth.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "beginner",
 ),
 fact(
 "cpr-adult",
 "While integrating an AED during adult CPR, how long should a manual pulse check pause compressions at most?",
 "No more than about 10 seconds while assessing for a pulse",
 [
 "Up to 20 seconds whenever the rescuer is uncertain whether a pulse is present",
 "Until two rescuers independently agree that no pulse is palpable",
 "As long as needed when the patient has a history of heart disease or prior cardiac arrest",
 ],
 "Coronary perfusion pressure drops quickly during compression pauses. AHA adult BLS limits "
 "pulse checks to about 10 seconds; extended checks or waiting for dual confirmation prolong "
 "time off the chest beyond what high-quality CPR allows.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "Two rescuers are performing adult BLS CPR without an advanced airway. What compression-to-ventilation cycle should they use?",
 "30 chest compressions followed by 2 rescue breaths, switching compressors about every 2 minutes",
 [
 "15 chest compressions followed by 2 rescue breaths because two rescuers always use the pediatric ratio",
 "30 chest compressions followed by 1 rescue breath to shorten pauses between cycles",
 "Continuous compressions with no ventilations until EMS places an advanced airway device",
 ],
 "Adult two-rescuer CPR remains 30:2 with periodic compressor switching to limit fatigue. "
 "Fifteen-to-two applies to two-rescuer child CPR, and withholding ventilations by default "
 "is not the standard adult BLS algorithm before advanced airway placement.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "A resuscitation team has one rescuer compressing for more than four minutes and depth is falling. When should they switch the compressor role during adult CPR?",
 "About every 2 minutes or sooner if rate or depth begins to deteriorate",
 [
 "Only after return of spontaneous circulation has been confirmed and sustained",
 "About every 10 minutes so each rescuer can rest through most of the event",
 "Never switch roles once the first compressor establishes an acceptable rhythm",
 ],
 "Compressor fatigue usually appears within a few minutes and shows up as shallow or slow "
 "compressions. AHA team guidance calls for rotation near two minutes, not marathon stints "
 "that let quality drift while waiting for ROSC.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "EMS is still en route but an adult arrest victim starts breathing normally and moving purposefully during your CPR. When should a lay rescuer stop chest compressions?",
 "When there are obvious signs of life such as normal breathing and purposeful movement, while continuing to monitor until EMS arrives",
 [
 "After exactly two minutes of CPR even when breathing and movement look normal",
 "When a single cough is heard once while compressions are still in progress",
 "Only after EMS personnel verbally order CPR to stop over the radio or phone",
 ],
 "A lone cough or a fixed time limit does not prove circulation has returned. AHA directs "
 "lay rescuers to stop compressions when breathing is normal and movement is purposeful, "
 "then monitor for re-arrest until professional responders assume care.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "During prolonged adult CPR the compressor's rate has slowed to about 85 per minute even though depth still looks acceptable. What team action best restores AHA rate guidance?",
 "Switch compressors about every two minutes and use a metronome or verbal coaching to stay near 100 to 120 per minute",
 [
 "Accept 85 per minute because adequate depth matters more than compression rate alone",
 "Push rate above 140 per minute for several cycles to compensate for earlier slowing",
 "Pause all compressions for one full minute so the tired rescuer can recover completely",
 ],
 "Fatigue often slows rate below 100 before depth collapses. Rotating compressors and audible "
 "pacing preserve the 100 to 120 target without the perfusion gap created by a long "
 "compression halt or unsustainably fast bursts.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "Which compression fraction goal best reflects high-quality adult CPR in most resuscitation attempts?",
 "Greater than 80% of the event spent performing chest compressions when that target is achievable",
 [
 "About 50% on the chest so half the time can be used for equipment setup and documentation",
 "Less than 40% on the chest so rescuers can rest and debrief between compression cycles",
 "100% on the chest with zero pauses even while the AED charges and delivers a shock",
 ],
 "AHA quality metrics emphasize maximizing time on the chest while still allowing necessary "
 "pauses for rhythm analysis and safe defibrillation. Extremely low fractions or refusing "
 "any pause during shock delivery both conflict with integrated high-quality CPR.",
 [S.AHA_HQ_CPR],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "Why does AHA stress limiting pauses in chest compressions during adult cardiac arrest care?",
 "Pauses let coronary perfusion pressure fall, reducing blood flow to the heart and brain between compressions",
 [
 "Pauses mainly increase the risk of rib fractures so compressions should never stop for any reason",
 "Pauses are mainly required so each rescuer can palpate a radial pulse before every compression",
 "Long pauses help the compressor regain grip on the sternum between compression cycles",
 ],
 "Myocardial and cerebral perfusion depend on sustained compressions that rebuild pressure "
 "during diastole. Fracture concern or team comfort does not replace the physiologic reason "
 "AHA limits interruptions during adult BLS.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "An adult has a palpable carotid pulse but is not breathing or is only gasping after you assess responsiveness. What BLS care is indicated?",
 "Provide rescue breaths about every 6 seconds without starting chest compressions",
 [
 "Begin immediate 30:2 CPR cycles because gasping always indicates cardiac arrest",
 "Provide one rescue breath about every 30 seconds while rechecking the pulse once per hour",
 "Apply a non-rebreather mask only and withhold all positive-pressure ventilations",
 ],
 "Pulse with absent or abnormal respirations is respiratory arrest in the adult BLS algorithm; "
 "ventilate about every six seconds while monitoring the pulse. Full CPR despite a palpable "
 "pulse is a critical error that can harm a perfusing patient.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "A second trained rescuer joins while you are performing 30:2 CPR on an adult in cardiac arrest. How should roles be organized to maintain quality?",
 "One rescuer compresses while the other gives breaths, switching compressor about every 2 minutes",
 [
 "The new rescuer should give breaths only and should not share compression duty at any time",
 "Both rescuers should stop CPR for a full team huddle before any further compressions",
 "Switch to 15 compressions and 2 ventilations because a second rescuer is now present",
 ],
 "The additional rescuer enables coordinated 30:2 with shared compression duty and regular "
 "rotation. Adult BLS does not switch to pediatric 15:2 ratios or extended timeouts when help "
 "arrives; continuous organized compressions remain the priority.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "For which situation does AHA teach lay rescuers that compression-only CPR is appropriate for adults?",
 "Witnessed sudden cardiac arrest when the rescuer is unwilling or unable to give rescue breaths",
 [
 "Any unresponsive adult even when breathing is normal and pulse is strong",
 "A lone rescuer with a pediatric drowning victim who is pulseless and apneic",
 "Only adults with end-stage chronic lung disease who still have a palpable pulse",
 ],
 "Compression-only CPR is intended for witnessed adult arrest when mouth-to-mouth is declined. "
 "It is not a substitute for ventilations in drowning pediatric arrest or for patients who "
 "are simply unresponsive but breathing.",
 [S.AHA_ADULT_BLS, S.AHA_WHAT_IS_CPR],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "You are about to attach an AED to an adult in cardiac arrest. Where should the electrode pads be placed on the chest?",
 "One pad on the upper-right chest below the clavicle and one on the lower-left lateral chest below the armpit",
 [
 "Both pads stacked vertically along the anterior midline over the sternum",
 "One pad on the upper-left chest and one on the lower-right quadrant of the abdomen",
 "One pad on the posterior thorax and one pad on the anterior thigh as a fixed pair",
 ],
 "Anterior-lateral placement routes defibrillation current through the ventricular mass. "
 "Stacked midline, abdominal, or back-thigh placements do not match AHA AED diagrams and "
 "reduce the likelihood of effective shock delivery.",
 [S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "During a long adult resuscitation the compressor reports burning arm fatigue and rate is slipping. What is the best fatigue management strategy on the team?",
 "Switch to a fresh compressor about every 2 minutes while maintaining depth and rate targets",
 [
 "Reduce target depth to about 1 inch after the first minute to preserve stamina",
 "Assign the smallest rescuer to compress for the entire event without rotation",
 "Alternate five minutes of complete rest with five minutes of compressions for each rescuer",
 ],
 "Scheduled rotation near two minutes keeps compressions hard and fast as rescuers tire. "
 "Shallow targets, single-rescuer marathons, or long rest intervals all erode the compression "
 "fraction and depth AHA associates with better outcomes.",
 [S.AHA_HQ_CPR, S.AHA_ADULT_BLS],
 "intermediate",
 ),
 fact(
 "cpr-adult",
 "An AED attached during adult CPR finishes analyzing rhythm and advises no shock. What should rescuers do next?",
 "Immediately resume high-quality chest compressions and follow subsequent AED prompts",
 [
 "Remove the AED pads and stop all CPR because no shock means the patient is stable",
 "Wait with compressions held until EMS arrives even if the patient remains pulseless",
 "Deliver three stacked manual defibrillation shocks before restarting any compressions",
 ],
 "A non-shockable rhythm still requires circulation support; AHA directs immediate resumption "
 "of compressions after a no-shock advisory. Stopping CPR or withholding compressions until "
 "EMS arrives abandons the patient during ongoing arrest.",
 [S.AHA_ADULT_BLS],
 "advanced",
 ),
 fact(
 "cpr-adult",
 "EMS personnel arrive while you are performing chest compressions on an adult in cardiac arrest. How should care be transferred?",
 "Continue compressions until EMS is ready, then hand off with closed-loop communication",
 [
 "Stop compressions as soon as EMS enters the room before they are ready to compress",
 "End CPR when EMS opens the monitor case without a planned compression transfer",
 "Leave the scene once EMS arrives without giving a patient care report",
 ],
 "AHA team resuscitation emphasizes minimizing gaps when transitioning to advanced providers. "
 "Stopping compressions before the incoming team is set to resume creates an avoidable pause "
 "in coronary perfusion pressure.",
 [S.AHA_ADULT_BLS, S.AHA_HQ_CPR],
 "advanced",
 ),
]
