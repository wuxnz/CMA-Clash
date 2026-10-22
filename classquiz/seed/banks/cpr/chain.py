# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""AHA Chain of Survival question bank."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

_AHA = [S.AHA_WHAT_IS_CPR, S.AHA_ADULT_BLS, S.AHA_HQ_CPR]

FACTS: list[dict] = [
    fact(
        "cpr-chain",
        "In the adult out-of-hospital Chain of Survival, which link comes first?",
        "Recognition and activation of emergency response",
        [
            "Immediate hospital discharge planning",
            "Cooling the patient before anyone calls for help",
            "Advanced airway placement by bystanders first",
        ],
        "The adult out-of-hospital Chain of Survival begins with recognition and activation of the emergency response system, because arrest must be identified before CPR and defibrillation can begin. Discharge planning, cooling the patient before anyone calls for help, and bystander advanced airway placement are not links in the chain.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "Why does early CPR matter in the Chain of Survival?",
        "Improves oxygen delivery until defibrillation",
        [
            "Replaces defibrillation once compressions are started",
            "Provides documentation for the arrest record",
            "Delays EMS activation until ROSC occurs",
        ],
        "Early CPR matters because chest compressions deliver oxygenated blood to the heart and brain during the minutes before a shock, which is what keeps the early CPR link working. Replacing defibrillation once compressions start, recording the event for the chart, and delaying EMS activation until ROSC each defeat the purpose of that link.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "Why is rapid defibrillation critical in cardiac arrest care?",
        "VF/pulseless VT may respond to early shock",
        [
            "Asystole converts to a perfusing rhythm after one shock",
            "Defibrillation treats stable sinus tachycardia",
            "Shocks are deferred until ten minutes of CPR have been completed",
        ],
        "Ventricular fibrillation and pulseless ventricular tachycardia are the shockable rhythms, and survival falls with every minute without a shock, so rapid defibrillation is critical. Asystole does not convert with a shock, defibrillation does not treat stable sinus tachycardia, and deferring shocks for ten minutes of CPR delays the definitive treatment.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "What does the advanced life support link of the Chain of Survival involve?",
        "Airway management, medications, and advanced monitoring",
        [
            "Preventive screening for coronary risk factors in the community",
            "Targeted temperature management in the intensive care unit",
            "Family counseling and grief support after the resuscitation",
        ],
        "The advanced life support link covers airway management, medications, and advanced "
        "monitoring delivered by EMS and hospital teams beyond lay rescuer BLS. Preventive screening, "
        "temperature management in the intensive care unit, and family counseling belong to "
        "prevention or post-arrest care rather than to advanced resuscitation.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "What does integrated post-cardiac arrest care focus on?",
        "Oxygenation, blood pressure support, and targeted temperature management",
        [
            "Discharging the patient home as soon as ROSC returns and care ends",
            "Completing paperwork and discharge forms without continued monitoring",
            "Withholding supplemental oxygen, ventilation, and pressure support after ROSC",
        ],
        "Integrated post-cardiac arrest care focuses on oxygenation, blood pressure support, and "
        "targeted temperature management after ROSC, because a return of circulation does not end the "
        "resuscitation process. Discharging the patient home at once, filling out discharge forms "
        "without monitoring, and withholding oxygen and ventilation after ROSC leave the patient "
        "without the support that limits secondary injury.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "What are public access defibrillation programs designed to achieve?",
        "Place AEDs where arrest is likely and train lay rescuers",
        [
            "Removing AEDs from public buildings",
            "Restricting AED training to hospital staff and removing public devices",
            "Replacing hands-on CPR education with online surveys",
        ],
        "Public access defibrillation programs place AEDs where cardiac arrests occur and train lay rescuers to use them, which shortens the time to first shock. Removing devices from public buildings, restricting training to hospital staff, and replacing hands-on CPR education with online surveys all move defibrillation further from the public.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "Which community strategies best increase bystander CPR and AED use?",
        "Hands-on training plus dispatcher-assisted CPR coaching for callers",
        [
            "Teaching bystanders to wait for EMS before starting compressions",
            "Delaying 911 calls until a supervisor approves the request",
            "Restricting AED use to trained healthcare workers in hospital clinics",
        ],
        "Hands-on courses build the skill to compress and to use an AED, and dispatcher assisted CPR "
        "coaching gets untrained bystanders compressing during the call for help, so both raise "
        "bystander CPR and AED use. Teaching that compressions wait for EMS, delaying 911 calls until "
        "a supervisor approves, and restricting AEDs to trained healthcare workers work against the "
        "community response.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "What does the pediatric Chain of Survival emphasize?",
        "Prevention of injury and illness as well as early CPR",
        [
            "Ignoring injury prevention in children",
            "Deferring all CPR until hospital arrival",
            "Applying the adult algorithm to every newborn and young child",
        ],
        "The pediatric Chain of Survival emphasizes prevention of injury and illness along with early CPR and defibrillation when indicated, because most pediatric arrests follow a preventable event such as drowning. Ignoring injury prevention in children, deferring CPR until hospital arrival, and applying the adult algorithm to every newborn discard the prevention and age differences that drive pediatric survival.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "What does the recovery phase after cardiac arrest involve?",
        "Rehabilitation, psychological support, and follow-up care",
        [
            "Immediate return to competitive sports without evaluation",
            "Discharge from the ICU with no follow-up plan of care",
            "Withholding mental health resources from survivors and families",
        ],
        "The recovery phase after cardiac arrest includes rehabilitation, psychological support, and "
        "follow-up care, because survivors can be left with physical limits, cognitive changes, and "
        "anxiety. Returning to competitive sports without evaluation, leaving the ICU without a "
        "follow-up plan, and withholding mental health resources all ignore the long-term needs of "
        "survivors.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "What does team-based resuscitation improve?",
        "Compression quality and role clarity",
        [
            "Eliminating role assignments during codes",
            "Allowing one person to perform all tasks without switching",
            "Dropping compression quality feedback during the event",
        ],
        "Team-based resuscitation improves compression quality and role clarity, since named roles and compressor rotation keep compressions continuous at the correct depth and rate. Eliminating role assignments, having one person perform every task alone, and dropping compression quality feedback all lengthen pauses and lower the quality of CPR.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "What does continuous quality improvement in resuscitation use?",
        "Data review, team debriefing, and system-level improvement",
        [
            "Avoiding review of resuscitation data and case outcomes",
            "Punishing the newest team member after each difficult arrest",
            "Replacing debriefs with anonymous complaint forms and surveys",
        ],
        "Continuous quality improvement in resuscitation uses data review, team debriefing, and "
        "system-level improvement, so teams can see trends in arrest response and fix system gaps. "
        "Avoiding review of resuscitation data, punishing the newest team member, and replacing "
        "debriefs with complaint forms produce nothing that can improve the next code.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "How do telephone CPR instructions help bystanders?",
        "Bystanders start compressions before EMS arrival",
        [
            "Keeping bystanders from touching the patient until EMS arrives",
            "Replacing AED programs with telephone hold music",
            "Delaying activation until two physicians reach the scene",
        ],
        "Telephone CPR instructions help bystanders start compressions before EMS arrival, because dispatch coaches untrained callers through compression-only CPR while responders are en route. Keeping bystanders from touching the patient until EMS arrives, replacing AED programs with telephone hold music, and delaying activation until two physicians reach the scene all delay lifesaving care.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "Which step opens the adult out-of-hospital Chain of Survival?",
        "Recognizing cardiac arrest and activating emergency response",
        [
            "Billing insurance before checking responsiveness",
            "Placing the patient in a recovery position without assessment",
            "Starting compressions before confirming the scene is safe",
        ],
        "The first link of the out-of-hospital adult Chain of Survival is recognizing cardiac arrest and activating emergency response, which means identifying unresponsiveness and abnormal breathing then calling for help. Billing insurance before checking responsiveness, placing the patient in a recovery position without assessment, and starting compressions before confirming scene safety all miss the recognition step.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "Why is early high-quality CPR a critical link in the Chain of Survival?",
        "Delivers oxygenated blood to the heart and brain until defibrillation",
        [
            "Delivers oxygenated blood to the heart and brain after hospital arrival",
            "Removes the need for early defibrillation once compressions start",
            "Replaces EMS activation with transport by private vehicle",
        ],
        "Early high-quality CPR is a critical link because chest compressions perfuse the heart and "
        "brain during the minutes before defibrillation and advanced care arrive. Delivering "
        "oxygenated blood after hospital admission, removing the need for early defibrillation, and "
        "replacing EMS activation with private transport each break the sequence that carries a "
        "patient from recognition to defibrillation.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "Early defibrillation is most likely to improve survival in which cardiac arrest rhythms?",
        "Shockable rhythms such as ventricular fibrillation",
        [
            "Normal sinus rhythm with a pulse and normal blood pressure",
            "Stable atrial fibrillation with good perfusion and a pulse",
            "Mild choking with an effective cough and a clear airway",
        ],
        "Early defibrillation improves survival in shockable rhythms such as ventricular fibrillation, because an AED shocks pulseless shockable rhythms and earlier shocks restore a perfusing rhythm more often. Normal sinus rhythm with a pulse, stable atrial fibrillation with good perfusion, and mild choking with an effective cough are not arrest rhythms that benefit from defibrillation.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "How does bystander CPR affect survival and neurologic outcome?",
        "Odds of survival and favorable neurologic outcome",
        [
            "Decreases survival when started promptly",
            "Changes nothing about survival or neurologic outcome",
            "Eliminates the need for EMS transport",
        ],
        "Bystander CPR started immediately raises the odds of survival and a favorable neurologic outcome, because compressions preserve perfusion until defibrillation and advanced care arrive. Decreasing survival when CPR starts promptly, changing nothing about survival or neurologic outcome, and removing the need for EMS transport all contradict the documented benefit of early CPR.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "How do public access defibrillation programs strengthen the Chain of Survival?",
        "Early defibrillation link in community chain",
        [
            "Removing the early defibrillation link",
            "Replacing hands-on CPR training with posted signage",
            "Delaying EMS to complete paperwork",
        ],
        "Public access defibrillation programs strengthen the early defibrillation link of the community chain by shortening the time to first shock. Removing the early defibrillation link, replacing hands-on CPR training with posted signage, and delaying EMS to complete paperwork all push defibrillation further from the moment of arrest.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "How does telephone-assisted CPR support bystanders?",
        "Coaching compressions until EMS arrives",
        [
            "Telling callers to wait for EMS before touching the patient",
            "Replacing compressions with back blows for arrest",
            "Discouraging speakerphone use during 911 calls",
        ],
        "Telephone-assisted CPR supports bystanders by coaching compressions until EMS arrives, which keeps circulation going through the response interval. Telling callers to wait for EMS before touching the patient, replacing compressions with back blows for arrest, and discouraging speakerphone use during 911 calls all undercut the dispatcher coaching that keeps CPR going.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "How can fear of legal liability sometimes weaken the Chain of Survival, and what often addresses that concern?",
        "Good Samaritan laws in many jurisdictions",
        [
            "Mandatory payment before starting compressions",
            "Requiring a notarized consent form on scene",
            "Declining to help so that no contact with the patient occurs",
        ],
        "Fear of legal liability can delay bystander help, and Good Samaritan laws in many jurisdictions address that concern by protecting good-faith rescue efforts. Requiring payment before starting compressions, demanding a notarized consent form on scene, and declining to help so that no contact with the patient occurs all discourage the bystander action the chain depends on.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "What does the in-hospital Chain of Survival add compared with community response?",
        "Rapid recognition of in-hospital arrest and organized code teams",
        [
            "Hospital scheduling that routinely runs before the code team is called",
            "Eliminating rapid response systems for deteriorating patients",
            "Deferring all compressions until imaging and labs are complete",
        ],
        "The in-hospital Chain of Survival adds rapid recognition of in-hospital arrest and organized response teams, so code teams and resuscitation resources reach the patient quickly. Outpatient scheduling without code teams, eliminating rapid response systems, and deferring compressions until imaging is complete remove the hospital-side links that keep arrest care moving.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "How does continuous quality improvement strengthen resuscitation systems?",
        "Debrief after resuscitation events",
        [
            "Skipping team discussion after every arrest",
            "Destroying monitor data after each event",
            "Replacing hands-on skills training with annual survey reviews",
        ],
        "Continuous quality improvement strengthens resuscitation systems because debriefing after resuscitation events identifies what worked and what must change in the next attempt. Skipping team discussion after every arrest, destroying monitor data after each event, and replacing hands-on skills training with annual survey reviews all erase the evidence improvement depends on.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "How should family presence during resuscitation be handled?",
        "An institutional policy supporting a designated support person",
        [
            "Mandatory livestreaming of the resuscitation for all families",
            "Banning support persons without a written departmental policy",
            "Allowing unrestricted interference with the resuscitation team",
        ],
        "Hospitals should handle family presence with an institutional policy that supports a designated support person, which answers family needs while the team stays focused on the arrest. Mandatory livestreaming for all families, banning support persons without a written policy, and allowing unrestricted interference with the team all work against a safe and humane resuscitation environment.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "How does community CPR training expand the Chain of Survival?",
        "Increasing number of competent bystanders",
        [
            "Reducing the number of trained bystanders",
            "Removing AEDs from public spaces",
            "Eliminating EMS from the chain",
        ],
        "Community CPR training expands the Chain of Survival by increasing the number of competent bystanders who can start CPR and retrieve an AED. Reducing the number of trained bystanders, removing AEDs from public spaces, and eliminating EMS from the chain shrink the pool of people who can act during the first minutes of an arrest.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "Which sequence best lists the links in the adult out-of-hospital Chain of Survival?",
        "Recognition, CPR, defibrillation, advanced care, and post-arrest care",
        [
            "Billing, registration, and discharge teaching, then optional CPR classes",
            "Cooling the patient before recognition in every community arrest",
            "Defibrillation before anyone activates the emergency response system on scene",
        ],
        "The AHA lists the adult out-of-hospital links as recognition and activation, immediate high-quality CPR, rapid defibrillation, advanced life support, and post-arrest care, in that order. Billing, registration, and discharge teaching, cooling before recognition, and defibrillation before anyone activates emergency response each break the accepted sequence.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "How does dispatcher-assisted CPR strengthen the Chain of Survival?",
        "It coaches untrained bystanders to start compressions while EMS travels",
        [
            "It replaces AED placement with telephone hold times on the emergency call",
            "It instructs callers to avoid patient contact during the call",
            "It delays the 911 call until a manager approves the request",
        ],
        "Dispatcher-assisted CPR strengthens the early CPR link by coaching untrained bystanders to start compressions while EMS is en route, so circulation begins before professionals arrive. Replacing AED placement with telephone hold times, instructing callers to avoid patient contact, and delaying 911 until a manager approves help each remove the link that dispatcher coaching provides.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "Why is post-cardiac arrest care considered a distinct chain link?",
        "ROSC does not guarantee survival; patients still need ongoing support",
        [
            "ROSC means the patient can be discharged home without further care",
            "Post-arrest care is limited to completing the required forms",
            "Monitoring, blood pressure support, and treating the cause are unnecessary",
        ],
        "Post-cardiac arrest care is a distinct link because ROSC does not guarantee survival, and "
        "patients still need oxygenation, blood pressure support, and treatment of the underlying "
        "cause. Discharge home right after ROSC, limiting post-arrest care to paperwork, and treating "
        "monitoring, blood pressure support, and treatment of the cause as unnecessary all leave room "
        "for rearrest and organ injury.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "A workplace installs AEDs but does not train staff. Which chain link remains weakest?",
        "Early CPR and rapid defibrillation, which need trained responders",
        [
            "Discharge planning carried out instead of bystander CPR training",
            "Post-arrest rehabilitation programs offered instead of early defibrillation",
            "Insurance authorization completed before the AED is unpacked",
        ],
        "The early CPR and rapid defibrillation links remain weakest, because AEDs and compressions need trained responders and untrained staff may fail to start CPR or use the device. Discharge planning in place of bystander CPR, post-arrest rehabilitation in place of early defibrillation, and insurance authorization before AED use each miss the links that depend on training.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "What is the purpose of debriefing after an in-hospital resuscitation attempt?",
        "Review team performance and system factors to improve the next response",
        [
            "Assigning blame to the least experienced clinician present on the code team",
            "Eliminating documentation of the arrest for the quality review",
            "Canceling future simulation training for the involved staff",
        ],
        "The purpose of debriefing is to review team performance and system factors so the next response is better, which turns each arrest into a learning opportunity. Assigning blame to the least experienced clinician, eliminating documentation of the arrest, and canceling future simulation training turn the review into something that damages the team.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "Why might fear of lawsuits reduce bystander CPR rates, and what helps address that fear?",
        "Good Samaritan laws in many areas protect good-faith rescue efforts",
        [
            "Bystanders fear legal risk and jurisdictions offer no protection",
            "Legal risk increases when Good Samaritan laws apply to the rescuer",
            "Compressions are treated as medical treatment that requires a license",
        ],
        "Bystanders may fear legal risk, and Good Samaritan laws in many areas protect good-faith rescue efforts, which is what encourages them to act. Believing that jurisdictions offer no protection for rescuers, claiming legal risk increases when Good Samaritan laws apply, and treating compressions as medical treatment that requires a license all keep bystanders from helping.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "How do community AED maps and signage support the Chain of Survival?",
        "They help bystanders locate devices for early defibrillation",
        [
            "They replace the need for CPR training for bystanders",
            "They delay EMS activation while responders search for a device",
            "They eliminate the maintenance of AED batteries and pads",
        ],
        "Community AED maps and signage support the Chain of Survival by helping bystanders locate a device quickly, so defibrillation happens earlier. They do not replace the need for CPR training, they do not delay EMS activation, and they do not remove the maintenance that keeps AED batteries and pads ready for use.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "Which outcome measure best reflects success of a community CPR training program?",
        "Increased rate of bystander CPR started before EMS arrival",
        [
            "Number of employees who completed the payroll training session",
            "Hospital cafeteria satisfaction scores from staff surveys",
            "Count of AED battery replacements across the city each year",
        ],
        "The outcome measure that best reflects success is an increased rate of bystander CPR started before EMS arrival, because that is the change in the early CPR link that saves lives. Counting employees who completed payroll training, tracking cafeteria satisfaction scores, and counting AED battery replacements across the city measure activity rather than patient benefit.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "Which action best describes the recognition link in the out-of-hospital Chain of Survival?",
        "Promptly identifying arrest and activating the response system",
        [
            "Waiting for a physician on scene before calling 911 for help",
            "Starting compressions without checking responsiveness and breathing",
            "Applying an AED before confirming that the scene is safe",
        ],
        "The recognition link is the prompt identification of cardiac arrest and activation of the emergency response system, which begins with checking responsiveness and breathing. Waiting for a physician on scene before calling 911, starting compressions without checking responsiveness, and applying an AED before ensuring scene safety all skip the assessment that recognition requires.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "Which links appear early in the out-of-hospital adult Chain of Survival?",
        "Recognition, CPR, defibrillation, and advanced care",
        [
            "Post-arrest hypothermia delivered later in the hospital",
            "Insurance preauthorization and elective scheduling",
            "Medication reconciliation performed without compressions",
        ],
        "The early links of the out-of-hospital adult Chain of Survival are recognition, CPR, defibrillation, and advanced care, since each of them begins before the patient reaches the hospital. Post-arrest hypothermia delivered in the hospital, insurance preauthorization and scheduling, and medication reconciliation without compressions belong to a different phase of care.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "Bystander CPR most directly strengthens which chain link?",
        "Early high-quality CPR for the arrest witness",
        [
            "Post-arrest rehabilitation services in the community",
            "Hospital discharge planning before EMS arrives",
            "Primary prevention of trauma around the world",
        ],
        "Bystander CPR most directly strengthens the early high-quality CPR link, because lay rescuers are usually the first people on scene and can start compressions at once. Post-arrest rehabilitation services in the community, hospital discharge planning before EMS arrives, and primary prevention of trauma around the world address different problems entirely.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "What do public access defibrillation programs add that improve survival?",
        "Early defibrillation before EMS arrival",
        [
            "Defibrillation that is delayed until hospital arrival",
            "Removal of CPR from public education",
            "Mandatory sedation of the patient before a shock",
        ],
        "Public access defibrillation programs add early defibrillation before EMS arrival, which shortens the time to first shock and improves survival in shockable rhythms. Defibrillation that is delayed until hospital arrival, removal of CPR from public education, and mandatory sedation of the patient before a shock all push back or disrupt the early shock.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "Which physiologic goals drive integrated post-cardiac arrest care?",
        "Hemodynamics, ventilation, and temperature management when indicated",
        [
            "Completing discharge paperwork before the patient leaves the hospital unit",
            "Immediate unsupervised home discharge for the recovering patient",
            "Withholding ventilation and oxygen after ROSC returns",
        ],
        "Integrated post-cardiac arrest care addresses hemodynamics, ventilation, and targeted temperature management when indicated, because these measures limit secondary brain and organ injury after ROSC. Completing discharge paperwork before the patient leaves, discharging the patient unsupervised and at once, and withholding ventilation after ROSC all skip the physiologic support that post-arrest care provides.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "What do telephone-assisted CPR dispatch instructions help bystanders with?",
        "Starting compressions while EMS is en route",
        [
            "Waiting silently on the line without instructions",
            "Telling callers to perform abdominal thrusts for arrest",
            "Delaying compressions until two rescuers arrive",
        ],
        "Telephone-assisted CPR dispatch instructions help bystanders with starting compressions while EMS is en route, so the response interval is filled with circulation instead of delay. Waiting silently on the line without instructions, telling callers to perform abdominal thrusts for arrest, and delaying compressions until two rescuers arrive each waste the time that dispatcher coaching is meant to use.",
        _AHA,
        "intermediate",
    ),
    fact(
        "cpr-chain",
        "What does community CPR training primarily improve?",
        "Willingness and ability to start the CPR link early",
        [
            "The speed of billing insurance for the responding service",
            "The reduced need for routine AED battery and pad checks",
            "The elimination of EMS from the response sequence",
        ],
        "Community CPR training primarily improves the willingness and ability of bystanders to start the CPR link early, because repeated practice builds confidence and skill. Billing insurance faster, reducing the need for AED maintenance, and eliminating EMS from the chain are administrative effects rather than the goal of the training.",
        _AHA,
        "beginner",
    ),
    fact(
        "cpr-chain",
        "Which failure in the Chain of Survival most directly delays defibrillation?",
        "Failure to activate EMS and retrieve an AED promptly",
        [
            "Taking a prolonged pulse check after every compression cycle",
            "Switching the compressor every two minutes during the arrest",
            "Documenting vital signs and reassessing after ROSC",
        ],
        "Failure to activate EMS and retrieve an AED promptly is the failure that most directly delays defibrillation, because shockable rhythms lose survival with every minute without a shock. Taking a pulse check after every compression cycle, switching compressors every two minutes, and documenting vital signs after ROSC are not the steps that postpone the shock.",
        _AHA,
        "advanced",
    ),
    fact(
        "cpr-chain",
        "What do in-hospital cardiac arrest systems focus on?",
        "Rapid recognition, team response, and high-quality CPR",
        [
            "Outpatient scheduling that runs without formal code teams",
            "Skipping the team debrief after each in-hospital arrest",
            "Deferring compressions for routine imaging before care",
        ],
        "In-hospital cardiac arrest systems focus on rapid recognition, team response, and high-quality CPR, because a code team at the bedside can start compressions and defibrillate within minutes. Outpatient scheduling without code teams, skipping debriefing after arrests, and deferring compressions for routine imaging remove the elements that make hospital arrests survivable.",
        _AHA,
        "advanced",
    ),
]
