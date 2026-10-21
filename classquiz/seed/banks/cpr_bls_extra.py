# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Additional hand-authored CPR/BLS questions to meet certification coverage targets."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [{'correct': 'Shout for help and activate the emergency response system (call 911 or send someone '
             'to call)',
  'difficulty': 'intermediate',
  'distractors': ['Begin compressions for two full minutes before anyone calls for help',
                  'Search the building for an AED before checking breathing',
                  'Place the person in a recovery position and leave to find a supervisor'],
  'explanation': 'AHA adult BLS begins with recognition, activation, and early CPR. Calling for '
                 'help ensures EMS and an AED are coming while compressions start. Starting two '
                 'minutes of CPR before activation would delay defibrillation and advanced care.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'A coworker collapses at a desk. After you confirm the scene is safe and the person is '
          'unresponsive, what is your next priority before starting compressions?',
  'topic': 'cpr-adult'},
 {'correct': 'Pause briefly to coach hand placement and depth, then resume 30:2 cycles with a '
             'compressor switch if needed',
  'difficulty': 'advanced',
  'distractors': ['Stop CPR until an AED arrives even if that takes many minutes',
                  'Switch to rescue breaths only until compressions improve on their own',
                  'Continue shallow compressions because any movement is better than pausing'],
  'explanation': 'High-quality compressions require at least 2 inches (5 cm) depth in most adults '
                 'with full recoil. Coaching and switching compressors every two minutes prevents '
                 'fatigue-related shallow compressions. Breath-only CPR would not support '
                 'circulation during arrest.',
  'references': ['American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr',
                 'American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'During two-rescuer adult CPR, one rescuer is giving poor-quality compressions that are '
          'too shallow. What is the best team action?',
  'topic': 'cpr-adult'},
 {'correct': 'At least 2 inches (5 cm) but not more than 2.4 inches (6 cm)',
  'difficulty': 'beginner',
  'distractors': ['Exactly 1 inch (2.5 cm) for all body sizes',
                  'At least 3.5 inches (9 cm) for every adult',
                  'Depth is optional as long as the rate is fast'],
  'explanation': 'AHA specifies a minimum depth to generate coronary perfusion while limiting '
                 'injury from excessive depth. One inch is too shallow for adults, and maximal '
                 'depth without an upper limit is not recommended. Rate and depth both define '
                 'high-quality CPR.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Which compression depth target is correct for most adult victims during BLS CPR?',
  'topic': 'cpr-adult'},
 {'correct': 'Stop CPR, monitor breathing and pulse, and place the person in a recovery position '
             'if no trauma is suspected',
  'difficulty': 'intermediate',
  'distractors': ['Continue 30:2 cycles because movement can be misleading',
                  'Remove all clothing and stop monitoring once color improves',
                  'Discharge the person home without EMS evaluation'],
  'explanation': 'Return of spontaneous circulation requires reassessment rather than ongoing '
                 'compressions. The recovery position supports the airway while awaiting EMS. '
                 'Continuing CPR on a breathing patient could cause injury and is not indicated.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'You are performing adult CPR and the victim begins to move and breathe normally. What '
          'should you do immediately?',
  'topic': 'cpr-adult'},
 {'correct': 'That location optimizes blood flow through the heart with the least risk of injury '
             'to underlying structures',
  'difficulty': 'beginner',
  'distractors': ['The xiphoid process is the strongest point for compression',
                  'Compressions over the upper abdomen compress the heart equally well',
                  'The left nipple alone marks the ideal compression point for all adults'],
  'explanation': 'Compressions over the lower sternum generate forward blood flow. Direct pressure '
                 'on the xiphoid can cause injury, and abdominal compressions do not provide '
                 'effective cardiac compression. Nipple line varies with body habitus and is not '
                 'the sole landmark.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why does AHA recommend pushing in the center of the chest on the lower half of the '
          'sternum?',
  'topic': 'cpr-adult'},
 {'correct': 'Start high-quality chest compressions immediately and use an AED as soon as it is '
             'available',
  'difficulty': 'intermediate',
  'distractors': ['Wait for EMS to begin any compressions',
                  'Give two rescue breaths every 30 seconds without compressions',
                  'Perform abdominal thrusts before checking responsiveness'],
  'explanation': 'Hands-only CPR is recommended for witnessed adult arrest when breaths are not '
                 'provided. Ventilation is still important in many arrests, but compressions and '
                 'early defibrillation are the priority in sudden collapse. Abdominal thrusts are '
                 'for choking, not primary cardiac arrest care.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr',
                 'American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A witnessed adult collapse is likely cardiac arrest. What is the preferred approach for '
          'a trained lay rescuer who is unwilling or unable to give rescue breaths?',
  'topic': 'cpr-adult'},
 {'correct': 'Reopen the airway with head tilt-chin lift (or jaw thrust if trauma is suspected) '
             'and reattempt a breath over about one second',
  'difficulty': 'advanced',
  'distractors': ['Increase breath force until the stomach is fully distended',
                  'Stop ventilations and continue compressions only for the rest of the arrest',
                  'Perform blind finger sweeps in the mouth between every compression'],
  'explanation': 'Inadequate chest rise usually indicates poor airway position or seal, not '
                 'necessarily a need for harder breaths. Gastric inflation from forceful breaths '
                 'reduces effective ventilation. Blind finger sweeps are not recommended and can '
                 'push objects deeper.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'During adult CPR you notice the chest does not rise with rescue breaths. What is the '
          'best next step before giving more breaths?',
  'topic': 'cpr-adult'},
 {'correct': 'Compressing the chest for most of the resuscitation period with pauses limited to '
             'under about 10 seconds for rhythm checks or defibrillation',
  'difficulty': 'advanced',
  'distractors': ['Pausing compressions for two minutes after every shock',
                  'Compressing only while the AED is analyzing rhythm',
                  'Alternating five minutes of compressions with five minutes of rest'],
  'explanation': 'Perfusion pressure drops quickly when compressions stop. Brief pauses for pulse '
                 'checks, pad placement, and shock delivery are necessary, but prolonged '
                 'interruptions reduce survival. Compressions during AED analysis are not '
                 'performed because everyone must clear the patient.',
  'references': ['American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'Which action best describes high-quality chest compression fraction during adult '
          'resuscitation?',
  'topic': 'cpr-adult'},
 {'correct': 'Continue compressions without pausing for breaths and deliver one breath every 6 '
             'seconds (10 breaths per minute)',
  'difficulty': 'advanced',
  'distractors': ['Stop compressions for two minutes after each breath',
                  'Return to 30:2 compressions-to-ventilations ratio with the advanced airway',
                  'Deliver breaths only when the AED prompts a shock'],
  'explanation': 'With an advanced airway, compressions are continuous and asynchronous '
                 'ventilations are given at 10 per minute in adult BLS/ACLS practice. Pausing '
                 'compressions for each breath would reduce perfusion. The 30:2 ratio applies '
                 'before an advanced airway is secured.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'An adult in cardiac arrest has an advanced airway placed by EMS. How should '
          'ventilations be provided once the advanced airway is in place?',
  'topic': 'cpr-adult'},
 {'correct': 'To let the heart refill with blood during diastole so the next compression can '
             'generate perfusion',
  'difficulty': 'beginner',
  'distractors': ['To give rescuers time to document vital signs on a chart',
                  'To reduce compression rate below 60 per minute',
                  'To keep partial weight on the chest between compressions'],
  'explanation': 'Incomplete recoil increases intrathoracic pressure and reduces coronary '
                 'perfusion. Rescuers should not lean on the chest between compressions. '
                 'Documentation and very slow rates are not goals of high-quality CPR.',
  'references': ['American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'What is the primary purpose of allowing full chest recoil between compressions?',
  'topic': 'cpr-adult'},
 {'correct': 'Activate EMS, provide rescue breaths if not breathing, and start CPR with 30:2 if no '
             'pulse after a brief check',
  'difficulty': 'advanced',
  'distractors': ['Wait for the child to vomit water before providing any breaths',
                  'Perform abdominal thrusts as the first step for every drowning victim',
                  'Begin compressions only after the child is completely dry and warmed'],
  'explanation': 'Pediatric drowning arrests are often respiratory in origin; ventilations are '
                 'especially important. EMS activation and early CPR improve outcome. Abdominal '
                 'thrusts are not the initial treatment for drowning, and drying the child is not '
                 'a prerequisite for starting BLS.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A 7-year-old child is pulled unresponsive from a swimming pool. After rescue from the '
          'water, what BLS sequence is most appropriate?',
  'topic': 'cpr-child'},
 {'correct': 'When the child has reached adult size, such as after puberty or when the child is '
             'too large for one-hand compressions',
  'difficulty': 'intermediate',
  'distractors': ['For every child older than 1 year regardless of size',
                  'Only when two rescuers are present',
                  'Whenever an AED is attached, regardless of patient size'],
  'explanation': 'AHA guidance is based on victim size rather than age alone. Adolescents who are '
                 'adult-sized receive adult compression depth. One year of age alone does not '
                 'mandate adult depth, and AED use does not change depth targets.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When should a rescuer use adult BLS compression depth instead of child depth for a '
          'pediatric patient?',
  'topic': 'cpr-child'},
 {'correct': 'Begin chest compressions and provide ventilations per pediatric BLS protocol',
  'difficulty': 'advanced',
  'distractors': ['Monitor only because any pulse means CPR is contraindicated',
                  'Give oxygen by mask but withhold compressions until pulse is absent',
                  'Perform vagal maneuvers before assessing breathing'],
  'explanation': 'Bradycardia with poor perfusion in children is treated as arrest-equivalent with '
                 'CPR. A weak pulse with poor perfusion still requires compressions. Oxygen alone '
                 'without compressions does not support systemic perfusion in this scenario.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A child has a pulse below 60 per minute with signs of poor perfusion. What is the '
          'appropriate BLS action?',
  'topic': 'cpr-child'},
 {'correct': 'Carotid or femoral pulse for no more than 10 seconds',
  'difficulty': 'intermediate',
  'distractors': ['Radial pulse at the wrist for a full two-minute pause',
                  'Apical pulse through clothing without exposing the chest',
                  'No pulse check is ever performed in pediatric BLS'],
  'explanation': 'Central pulses are easier to feel in children during arrest. Checks must be '
                 'brief to limit interruption of compressions. Radial pulses may be absent in low '
                 'perfusion states, and prolonged pauses harm outcomes.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Which pulse site is preferred for a pulse check in an unresponsive child during BLS?',
  'topic': 'cpr-child'},
 {'correct': 'Children often arrest because of respiratory problems, so oxygenation and '
             'ventilation are critical early interventions',
  'difficulty': 'beginner',
  'distractors': ['Children never benefit from chest compressions',
                  'Ventilations are required only after ROSC',
                  'Compression-only CPR is preferred for all pediatric ages'],
  'explanation': 'Respiratory failure is a common pathway to pediatric arrest. Compressions remain '
                 'essential, but breaths address the underlying hypoxia. Compression-only CPR is '
                 'not the preferred approach when rescuers can ventilate.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why does AHA recommend ventilations for many pediatric arrests when lay rescuers are '
          'able to provide breaths?',
  'topic': 'cpr-child'},
 {'correct': 'One rescuer compresses while the other gives ventilations at a 15:2 ratio',
  'difficulty': 'intermediate',
  'distractors': ['Both rescuers compress simultaneously on opposite sides of the chest at 30:2',
                  'One rescuer performs only jaw thrust while the other compresses at 30:2',
                  'Rescuers alternate giving breaths without compressions until EMS arrives'],
  'explanation': 'Two-rescuer pediatric BLS uses 15:2 to provide more frequent ventilations with a '
                 'dedicated compressor. Dual simultaneous compressions are not standard, and '
                 'breaths without compressions do not support circulation in arrest.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'During two-rescuer child CPR, which ratio and role division is correct?',
  'topic': 'cpr-child'},
 {'correct': 'Encourage continued coughing and stay with the child while preparing to activate EMS '
             'if obstruction worsens',
  'difficulty': 'beginner',
  'distractors': ['Begin abdominal thrusts immediately',
                  'Start CPR compressions in case perfusion is low',
                  'Perform back blows until the child becomes unresponsive'],
  'explanation': 'Effective cough indicates partial obstruction; interventions could worsen the '
                 'blockage. Abdominal thrusts and CPR are for severe obstruction or '
                 'unresponsiveness. Monitoring is appropriate while the cough remains strong.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A conscious child is choking on food but can cough forcefully. What should you do?',
  'topic': 'cpr-child'},
 {'correct': 'Jaw thrust without head tilt if spinal injury cannot be ruled out',
  'difficulty': 'advanced',
  'distractors': ['Hyperextension of the neck with maximum head tilt always',
                  'Finger sweep of the oropharynx before any breaths every cycle',
                  'Placement of a pillow under the shoulders to flex the neck'],
  'explanation': 'Suspected cervical spine injury requires minimizing neck movement while opening '
                 'the airway. Routine hyperextension may worsen spinal injury. Blind finger sweeps '
                 'are not recommended.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When opening the airway for child CPR after a diving injury is suspected, what maneuver '
          'is preferred?',
  'topic': 'cpr-child'},
 {'correct': 'Call 911 on speakerphone, then begin infant CPR starting with compressions (or '
             'breaths per local training) without leaving the infant',
  'difficulty': 'advanced',
  'distractors': ["Run to a neighbor's house for two minutes before calling or starting CPR",
                  'Wait for the infant to turn blue before providing ventilations',
                  'Perform abdominal thrusts as the first step for every infant'],
  'explanation': 'A phone enables activation of EMS while CPR begins. Delaying care to find help '
                 'wastes critical time. Color change is a late sign, and abdominal thrusts are not '
                 'the initial step for unresponsive infants who are not choking.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A 4-month-old infant becomes unresponsive and is not breathing normally at home. The '
          'lone caregiver has a cell phone. What is the best sequence?',
  'topic': 'cpr-infant'},
 {'correct': 'Two-thumb encircling hands technique on the lower half of the sternum',
  'difficulty': 'intermediate',
  'distractors': ['Heel of one hand with adult compression depth',
                  'Two-finger technique on the upper abdomen',
                  'One rescuer compresses the head while the other ventilates'],
  'explanation': 'Two-thumb encircling hands provide better depth and recoil with two rescuers. '
                 'Adult hand technique can exceed safe infant depth. Abdominal compressions do not '
                 'substitute for sternal compressions.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Which compression technique is preferred when two rescuers are performing infant CPR?',
  'topic': 'cpr-infant'},
 {'correct': 'Create a seal over the mouth and nose and give a breath over about one second '
             'watching for chest rise',
  'difficulty': 'beginner',
  'distractors': ['Pinch the nose closed and blow only into the mouth as for an adult',
                  'Deliver large breaths until the abdomen is markedly distended',
                  'Ventilate through a nasal cannula without a seal'],
  'explanation': 'Infant ventilations require mouth-and-nose seal with gentle volume. Pinching the '
                 'nose is an adult technique. Overventilation causes gastric inflation and reduces '
                 'effective ventilation.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'How should you deliver ventilations to an infant during CPR?',
  'topic': 'cpr-infant'},
 {'correct': 'Reposition the head, ensure mouth-and-nose seal, and attempt another gentle breath '
             'before resuming compressions',
  'difficulty': 'intermediate',
  'distractors': ['Increase pressure until you hear air leak audibly from the stomach',
                  'Skip all further ventilations for the remainder of the arrest',
                  'Perform blind finger sweeps before every breath'],
  'explanation': 'Poor chest rise is often due to positioning or seal, not lack of effort. '
                 'Forceful breaths inflate the stomach. Blind sweeps are not recommended in BLS '
                 'airway management.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': "An infant's chest does not rise with the first rescue breath during CPR. What is the "
          'best response?',
  'topic': 'cpr-infant'},
 {'correct': 'Infants lose body heat quickly, which can worsen perfusion and complicate '
             'resuscitation',
  'difficulty': 'intermediate',
  'distractors': ['Infants overheat during CPR and must be cooled with ice packs immediately',
                  'Covering the infant replaces the need for ventilations',
                  'Temperature is irrelevant during infant arrest'],
  'explanation': 'Hypothermia increases morbidity in small patients. Covering with a dry blanket '
                 'after drying the chest supports thermoregulation. Cooling with ice is not '
                 'routine BLS care, and ventilations remain necessary.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why is heat loss a concern when providing prolonged CPR to an infant?',
  'topic': 'cpr-infant'},
 {'correct': 'Use adult pads with anterior-posterior placement per manufacturer instructions while '
             'minimizing pause in compressions',
  'difficulty': 'advanced',
  'distractors': ['Withhold defibrillation until the child reaches 8 years of age',
                  'Place both pads on the abdomen because the chest is too small',
                  'Remove pads after every shock and do not resume CPR'],
  'explanation': 'AHA permits adult AED use on infants and children when pediatric equipment is '
                 'unavailable, with appropriate pad placement. Defibrillation should not be '
                 'delayed arbitrarily, and CPR must resume immediately after shock delivery.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When placing AED pads on an infant, what is an acceptable approach if pediatric pads '
          'are not available?',
  'topic': 'cpr-infant'},
 {'correct': '30 compressions followed by 2 breaths',
  'difficulty': 'beginner',
  'distractors': ['15 compressions followed by 2 breaths',
                  'Continuous compressions without any ventilations',
                  '5 compressions followed by 1 breath'],
  'explanation': 'Lone rescuer infant BLS uses 30:2. The 15:2 ratio is for two rescuers. '
                 'Continuous compressions without breaths omit needed oxygenation in many infant '
                 'arrests.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'What compression-to-ventilation ratio should a single rescuer use for infant CPR?',
  'topic': 'cpr-infant'},
 {'correct': 'Maintain airway, provide oxygen if needed, keep the infant warm, and monitor '
             'breathing and pulse closely',
  'difficulty': 'advanced',
  'distractors': ['Offer formula immediately to prevent hunger',
                  'Place prone unmonitored to improve drainage',
                  'Discharge if color looks pink regardless of breathing effort'],
  'explanation': 'Post-ROSC infants need close monitoring for recurrent arrest and respiratory '
                 'failure. Feeding and prone unmonitored positioning are unsafe. Color alone does '
                 'not confirm stable ventilation.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'After ROSC in an infant, what is the priority nursing action in the BLS setting?',
  'topic': 'cpr-infant'},
 {'correct': 'Ensure no one is touching the patient or conductive surfaces and loudly state that '
             'everyone is clear',
  'difficulty': 'beginner',
  'distractors': ['Continue chest compressions through the shock to save time',
                  'Remove the pads and dry the chest again after the shock is delivered',
                  'Wait for a physician to arrive before allowing the shock'],
  'explanation': 'Safety requires a clear patient during shock delivery. Compressions during shock '
                 'risk injury to rescuers and may interfere with energy delivery. Pads remain in '
                 'place for subsequent analysis, and BLS does not require physician presence to '
                 'shock.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'An AED is attached to an adult in arrest and announces that a shock is advised. What '
          'must happen immediately before shock delivery?',
  'topic': 'cpr-aed'},
 {'correct': 'Turned on and prepared nearby so pads can be applied with minimal interruption in '
             'compressions',
  'difficulty': 'intermediate',
  'distractors': ['Left in the carrying case until compressions have continued for 15 minutes',
                  "Held against the patient's leg during every compression",
                  'Connected to wall power only after EMS arrival'],
  'explanation': 'Early defibrillation is time-critical. The device should be activated and pads '
                 'applied as soon as available with brief pauses. Holding the AED during '
                 'compressions is unsafe and interferes with technique.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'While CPR is in progress, where should the AED be placed until pads are attached?',
  'topic': 'cpr-aed'},
 {'correct': 'Dry the chest quickly and place pads on bare dry skin',
  'difficulty': 'intermediate',
  'distractors': ['Attach pads directly over the wet shirt without drying',
                  'Pour additional water on the chest to improve conduction',
                  'Delay AED use until clothing is sent to laundry'],
  'explanation': 'Moisture and poor contact increase transthoracic impedance and may reduce shock '
                 'effectiveness. Pads require bare dry skin per manufacturer diagrams. Adding '
                 'water or waiting unnecessarily delays defibrillation.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': "A patient's chest is wet from sweat after exertion. What should you do before attaching "
          'AED pads?',
  'topic': 'cpr-aed'},
 {'correct': 'An unresponsive patient without normal breathing or with only gasping respirations',
  'difficulty': 'beginner',
  'distractors': ['A conscious patient complaining of mild chestburn after eating',
                  'A sleeping patient who is breathing normally',
                  'A patient with a sprained ankle and normal vital signs'],
  'explanation': 'AEDs are used with CPR for cardiac arrest, not for minor complaints or normal '
                 'sleep. Gasping is not adequate breathing. Conscious patients with normal '
                 'breathing do not meet arrest criteria for AED use.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Which patient should receive AED pad placement and rhythm analysis during suspected '
          'cardiac arrest?',
  'topic': 'cpr-aed'},
 {'correct': 'Avoid placing a pad directly over the device; adjust placement at least about 1 inch '
             '(2.5 cm) away when possible',
  'difficulty': 'advanced',
  'distractors': ['Place both pads directly on top of the generator for best contact',
                  'Withhold all defibrillation because pacemakers always contraindicate AEDs',
                  'Place pads only on the lower extremities'],
  'explanation': 'Pads can be adjusted to avoid the generator while still allowing effective '
                 'current through the heart. AEDs are used in arrest despite pacemakers. Leg-only '
                 'placement would not defibrillate the heart effectively.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'An implanted pacemaker is palpable under the skin on the upper left chest. How should '
          'AED pads be placed?',
  'topic': 'cpr-aed'},
 {'correct': 'Stay clear of the patient and be prepared to resume compressions immediately if '
             'another shock is not advised',
  'difficulty': 'advanced',
  'distractors': ['Palpate a carotid pulse for two minutes before touching the patient',
                  'Remove pads to let the chest rest',
                  "Administer oral medications through the patient's mouth"],
  'explanation': 'Everyone must clear during analysis. If no shock is advised, CPR resumes without '
                 'delay. Prolonged pulse checks and pad removal waste perfusion time. Medications '
                 'are not given by lay rescuers during BLS.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'After an AED shock, the device may prompt another rhythm check. What should rescuers do '
          'while the AED analyzes?',
  'topic': 'cpr-aed'},
 {'correct': 'To remove hair that prevents pad adhesive from contacting skin',
  'difficulty': 'intermediate',
  'distractors': ['To mark incision sites for surgery after ROSC',
                  'To cool the skin before shock delivery',
                  'To test blade sharpness before opening the airway'],
  'explanation': 'Poor adhesion increases impedance and may cause artifact. Razors are for hair '
                 'removal at pad sites, not for cooling or surgical marking. Airway opening does '
                 'not require shaving.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why might rescuers use a razor from the AED kit before pad placement?',
  'topic': 'cpr-aed'},
 {'correct': 'Verify battery charge and pad expiration so the device is ready when needed',
  'difficulty': 'beginner',
  'distractors': ['Disable alarms so bystanders ignore the cabinet',
                  'Remove pads to extend shelf life outside the device',
                  'Change device language settings monthly without testing power'],
  'explanation': 'Readiness checks ensure the AED will operate during arrest. Alarms alert others '
                 'to potential use. Removing pads or skipping power checks would leave the device '
                 'unusable.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Public-access AED cabinets often beep when opened. What is the primary purpose of '
          'routine AED maintenance checks?',
  'topic': 'cpr-aed'},
 {'correct': 'Alternate 5 back blows and 5 abdominal thrusts until the object is expelled or the '
             'victim becomes unresponsive',
  'difficulty': 'intermediate',
  'distractors': ['Encourage sips of water to wash the food down',
                  'Begin CPR compressions immediately while the victim is standing',
                  'Perform blind finger sweeps in the mouth first'],
  'explanation': 'Severe choking in a responsive adult is treated with back blows and abdominal '
                 'thrusts per AHA BLS. Water may worsen obstruction. CPR begins if the victim '
                 'becomes unresponsive. Blind sweeps are not recommended.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'An adult dining in a restaurant clutches the throat and cannot speak but is conscious. '
          'What is the first BLS intervention?',
  'topic': 'cpr-choking'},
 {'correct': 'Use chest thrusts instead of abdominal thrusts',
  'difficulty': 'advanced',
  'distractors': ['Withhold all assistance until delivery',
                  'Perform only back blows while she lies flat on her back',
                  'Start CPR compressions before any thrusts while she is awake'],
  'explanation': 'Chest thrusts reduce risk to the fetus and diaphragm when abdominal thrusts are '
                 'difficult. Assistance should not be delayed. CPR is for unresponsive arrest, not '
                 'initial conscious choking.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A pregnant woman in the third trimester has severe airway obstruction and is still '
          'conscious. What modification is appropriate?',
  'topic': 'cpr-choking'},
 {'correct': 'Before giving rescue breaths if you see signs of obstruction or after compressions '
             'as part of the cycle',
  'difficulty': 'advanced',
  'distractors': ['Only after ROSC has occurred',
                  'Every 30 seconds using blind finger sweeps',
                  'Never; airway inspection is contraindicated'],
  'explanation': 'Visible objects may be removed, but blind sweeps are avoided. Airway checks '
                 'integrate with CPR cycles. Waiting until ROSC misses opportunities to relieve '
                 'obstruction during arrest.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'During CPR on an unresponsive choking victim, when should you look in the mouth for a '
          'foreign body?',
  'topic': 'cpr-choking'},
 {'correct': 'Mild obstruction allows a strong cough and some air movement; severe obstruction '
             'includes silent cough or inability to speak',
  'difficulty': 'beginner',
  'distractors': ['Mild obstruction always causes immediate unresponsiveness',
                  'Severe obstruction always allows clear speech',
                  'Cough strength does not change management'],
  'explanation': 'Cough effectiveness guides whether to encourage coughing or begin thrusts. '
                 'Immediate unresponsiveness is not mild obstruction. Inability to speak suggests '
                 'severe obstruction requiring intervention.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Which finding best distinguishes mild versus severe choking in a responsive adult?',
  'topic': 'cpr-choking'},
 {'correct': 'Lay the infant on a firm surface, call for help, and begin CPR with checks for a '
             'visible object in the mouth before breaths',
  'difficulty': 'advanced',
  'distractors': ['Hold the infant upright and perform only back slaps indefinitely',
                  'Shake the infant to dislodge the object before calling for help',
                  'Wait for cyanosis before starting any compressions'],
  'explanation': 'Unresponsive choking infants receive CPR on a firm surface with integrated '
                 'airway checks. Back slaps alone are insufficient when the infant is '
                 'unresponsive. Shaking risks injury and delays effective care.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'An infant with severe choking becomes unresponsive in your arms. What is the correct '
          'action?',
  'topic': 'cpr-choking'},
 {'correct': 'Airway swelling, aspiration, or cardiac stress can cause delayed complications after '
             'obstruction',
  'difficulty': 'intermediate',
  'distractors': ['Insurance requires hospital admission for every cough',
                  'Abdominal thrusts always fracture ribs that must be imaged',
                  'No complications occur once the object is expelled'],
  'explanation': 'Complications such as aspiration pneumonia or edema may develop after severe '
                 'choking. Not every patient needs admission, but evaluation is prudent. Rib '
                 'fracture is not universal and does not explain all post-event risk.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'After you relieve choking in an older adult who had a prolonged episode, why is EMS '
          'evaluation recommended?',
  'topic': 'cpr-choking'},
 {'correct': 'Stay with the child, encourage coughing, and be ready to activate EMS if breathing '
             'worsens',
  'difficulty': 'beginner',
  'distractors': ['Begin alternating back blows and abdominal thrusts immediately',
                  'Lay the child down and start CPR compressions',
                  'Give small pieces of food to push the object down'],
  'explanation': 'Effective cough and speech indicate partial obstruction; aggressive thrusts may '
                 'convert it to complete obstruction. CPR is for unresponsive arrest. Food may '
                 'worsen blockage.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A child with mild choking can speak in full sentences and is coughing effectively. What '
          'is appropriate care?',
  'topic': 'cpr-choking'},
 {'correct': 'Recognition and activation, immediate high-quality CPR, rapid defibrillation, '
             'advanced life support, and post-arrest care',
  'difficulty': 'beginner',
  'distractors': ['Hospital registration, medication reconciliation, discharge teaching, and '
                  'billing',
                  'Cooling the patient before any bystander CPR',
                  'Defibrillation before anyone calls for help in every setting'],
  'explanation': 'AHA emphasizes early recognition, CPR, and defibrillation before advanced care. '
                 'Administrative tasks are not chain links. Cooling is part of post-arrest care, '
                 'not a substitute for CPR. Activation and CPR generally precede defibrillation in '
                 'community response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr',
                 'American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Which sequence best lists the links in the adult out-of-hospital Chain of Survival?',
  'topic': 'cpr-chain'},
 {'correct': 'It coaches untrained bystanders to start compressions while EMS is en route',
  'difficulty': 'intermediate',
  'distractors': ['It replaces the need for AED programs in public buildings',
                  'It discourages bystanders from touching the patient',
                  'It delays 911 activation until a supervisor approves help'],
  'explanation': 'Telephone CPR increases the likelihood that compressions begin early. AED '
                 'programs remain important. Dispatchers encourage action rather than delay or '
                 'forbid compressions.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'How does dispatcher-assisted CPR strengthen the Chain of Survival?',
  'topic': 'cpr-chain'},
 {'correct': 'ROSC does not guarantee survival; patients need oxygenation, blood pressure support, '
             'and treatment of the underlying cause',
  'difficulty': 'advanced',
  'distractors': ['ROSC means the patient can always go home the same day',
                  'Post-arrest care consists only of completing paperwork',
                  'Cooling and monitoring are never used after arrest'],
  'explanation': 'Many patients rearrest or develop organ injury after ROSC. Structured '
                 'post-arrest care improves outcomes. Paperwork alone is insufficient, and '
                 'targeted temperature management may be indicated in hospital care.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why is post-cardiac arrest care considered a distinct chain link?',
  'topic': 'cpr-chain'},
 {'correct': 'Early high-quality CPR and rapid defibrillation because devices require trained '
             'responders to use them effectively',
  'difficulty': 'intermediate',
  'distractors': ['Prevention of all cardiac disease in employees',
                  'Post-arrest rehabilitation in the hospital only',
                  'Insurance authorization for ambulance transport'],
  'explanation': 'AEDs help only when paired with recognition, CPR, and trained users. Primary '
                 'prevention is important but is a separate public health goal. Hospital '
                 'rehabilitation occurs after EMS care, not instead of bystander response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'A workplace installs AEDs but does not train staff. Which chain link remains weakest?',
  'topic': 'cpr-chain'},
 {'correct': 'Review team performance and system factors to improve the next response',
  'difficulty': 'intermediate',
  'distractors': ['Assign blame to the newest team member',
                  'Eliminate documentation of the event',
                  'Replace future CPR training with online surveys only'],
  'explanation': 'Quality improvement debriefs focus on learning, not punishment. Documentation '
                 'remains required for care continuity. Debriefing complements ongoing skills '
                 'training.',
  'references': ['American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'What is the purpose of debriefing after an in-hospital resuscitation attempt?',
  'topic': 'cpr-chain'},
 {'correct': 'Elevate the injured extremity above the level of the heart while maintaining direct '
             'pressure',
  'difficulty': 'intermediate',
  'distractors': ['Remove the dressing every 30 seconds to inspect clot formation',
                  'Apply a tourniquet proximal to every finger cut',
                  'Immerse the wound in hot water to vasoconstrict vessels'],
  'explanation': 'Elevation can assist venous return when fractures are not suspected. Frequent '
                 'dressing removal disrupts clotting. Tourniquets are for life-threatening limb '
                 'bleeding, not minor cuts. Heat increases bleeding.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'While waiting for EMS after applying pressure to a bleeding laceration, what additional '
          'step is appropriate if no fracture is suspected?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Heat stroke; activate EMS and begin rapid cooling while monitoring airway and '
             'breathing',
  'difficulty': 'advanced',
  'distractors': ['Heat exhaustion only; encourage heavy exercise to finish the trail',
                  'Hypothermia; wrap in blankets without calling for help',
                  'Mild dehydration; withhold all fluids even if awake'],
  'explanation': 'Altered mental status with hot dry skin suggests heat stroke, a medical '
                 'emergency. Cooling and EMS activation are priorities. Heat exhaustion is milder; '
                 'hypothermia presents with cold exposure findings.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'A hiker shows confusion, hot dry skin, and a very high temperature after exertion in '
          'heat. What is the most likely problem and first aid priority?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Protect the head, move nearby hazards, and time the seizure duration',
  'difficulty': 'beginner',
  'distractors': ['Place a spoon in the mouth to prevent tongue biting',
                  'Hold the person down firmly to stop movements',
                  'Give water immediately while jerking continues'],
  'explanation': 'Protecting the head and clearing hazards prevents injury. Objects in the mouth '
                 'and restraint can cause harm. Fluids are unsafe during active convulsions.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'During a seizure, which action is appropriate for a trained first aid provider?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Give 15 grams of fast-acting carbohydrate and recheck glucose in about 15 minutes '
             'per protocol',
  'difficulty': 'advanced',
  'distractors': ['Administer injectable insulin immediately',
                  'Withhold all sugar because confusion means hyperglycemia',
                  'Tell the patient to sleep it off without monitoring'],
  'explanation': 'These findings suggest hypoglycemia treated with fast sugar when swallowing is '
                 'safe. Insulin would worsen low glucose. Sleep without treatment risks '
                 'progression to seizures or unresponsiveness.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid',
                 'CDC: About Diabetes — https://www.cdc.gov/diabetes/about/index.html'],
  'stem': 'A patient with diabetes is conscious, confused, and diaphoretic with a glucose meter '
          'reading of 54 mg/dL. What first aid is appropriate if they can swallow safely?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Look for hazards such as traffic, fire, or downed power lines before approaching the '
             'patient',
  'difficulty': 'beginner',
  'distractors': ['Enter any unstable structure immediately without protective equipment',
                  'Assume all scenes are safe once someone is calling for help',
                  'Ignore electrical hazards if the patient is a family member'],
  'explanation': 'Rescuer safety prevents additional victims. Hazards must be controlled or '
                 'avoided before care. Family relationship does not eliminate electrical or '
                 'structural danger.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid',
                 'American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'What is the safest approach to scene size-up taught in both Red Cross first aid and AHA '
          'CPR courses?',
  'topic': 'cpr-red-cross'},
 {'correct': '100 to 120 compressions per minute',
  'difficulty': 'beginner',
  'distractors': ['60 compressions per minute',
                  '150 to 180 compressions per minute',
                  '40 compressions per minute with long pauses between each'],
  'explanation': 'AHA targets 100 to 120 compressions per minute for all ages. Slower rates do not '
                 'support perfusion, and faster rates may not allow adequate depth and recoil.',
  'references': ['American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'Which metronome or song tempo best matches the adult CPR compression rate target?',
  'topic': 'cpr-adult'},
 {'correct': 'Continue high-quality CPR and use EMS defibrillation when it arrives',
  'difficulty': 'advanced',
  'distractors': ['Stop all resuscitation because AED failure means the patient cannot survive',
                  'Remove the patient from the scene to find another AED before compressions',
                  'Wait without compressions until a new battery is installed'],
  'explanation': 'CPR remains the bridge to defibrillation even when a public AED fails. Stopping '
                 'care or delaying compressions for equipment wastes critical time. EMS carries '
                 'defibrillators.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'If an AED malfunctions and will not power on during arrest, what should rescuers do?',
  'topic': 'cpr-aed'},
 {'correct': 'When the child is large enough that one-hand compressions are appropriate or after '
             'puberty per local protocol',
  'difficulty': 'intermediate',
  'distractors': ['At exactly 8 years of age for every student',
                  'Only when an AED is not available',
                  'Never; child depth is used for all patients under 18'],
  'explanation': 'Size and pubertal development guide transition to adult technique more than a '
                 'single age number. AED availability does not determine compression depth. Older '
                 'adolescents may require adult depth.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A school nurse begins CPR on an unresponsive child. When should the nurse switch to '
          'adult compression depth?',
  'topic': 'cpr-child'},
 {'correct': '15 compressions to 2 breaths',
  'difficulty': 'intermediate',
  'distractors': ['30 compressions to 2 breaths',
                  '5 compressions to 1 breath',
                  'Continuous compressions without ventilations'],
  'explanation': 'Two rescuers provide more frequent ventilations at 15:2 for infants. Lone '
                 'rescuers use 30:2. Continuous compressions omit needed breaths for many infant '
                 'arrests.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'During two-rescuer infant CPR, what compression-to-ventilation ratio should the team '
          'use?',
  'topic': 'cpr-infant'},
 {'correct': 'Bystanders worry about legal risk; Good Samaritan laws in many areas protect '
             'good-faith rescue efforts',
  'difficulty': 'beginner',
  'distractors': ['Fear is unfounded because resuscitation never has complications',
                  'Laws require payment before starting compressions',
                  'Only healthcare providers are allowed to call 911'],
  'explanation': 'Good Samaritan protections encourage action, though laws vary by jurisdiction. '
                 'Complications can occur, but withholding help increases mortality. Payment is '
                 'not required to activate EMS.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr',
                 'American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Why might fear of lawsuits reduce bystander CPR rates, and what helps address that '
          'fear?',
  'topic': 'cpr-chain'},
 {'correct': 'Chest thrusts with the same 5 and 5 alternation pattern as other choking sequences',
  'difficulty': 'advanced',
  'distractors': ['No intervention until the patient loses consciousness',
                  'Only finger sweeps in the mouth while the patient stands',
                  'CPR compressions while the patient is still speaking'],
  'explanation': 'Chest thrusts are the alternative when abdominal thrusts are ineffective or '
                 'contraindicated. Delaying help risks complete obstruction. CPR is for '
                 'unresponsive victims, not conscious speakers.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'An obese adult with severe choking cannot receive effective abdominal thrusts. What '
          'alternative should you try?',
  'topic': 'cpr-choking'},
 {'correct': 'No more than 10 seconds',
  'difficulty': 'intermediate',
  'distractors': ['At least 60 seconds to feel a faint pulse',
                  'No more than 2 minutes',
                  'Pulse checks are never performed once CPR begins'],
  'explanation': 'Brief pulse checks limit perfusion interruption. Prolonged pauses reduce '
                 'survival. Pulse checks are still performed at appropriate times but must be '
                 'quick.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'You must stop compressions briefly to attach AED pads. What is the maximum recommended '
          'pause for a pulse check during adult BLS?',
  'topic': 'cpr-adult'},
 {'correct': 'Clean the area, apply dressing, and seek medical evaluation for tetanus and '
             'infection risk',
  'difficulty': 'intermediate',
  'distractors': ['Seal the wound airtight without washing to keep bacteria inside',
                  'Remove the nail if embedded only when alone without EMS',
                  'Ignore punctures that are not actively spurting blood'],
  'explanation': 'Puncture wounds carry infection and tetanus risk even with minor external '
                 'bleeding. Wounds should be cleaned and evaluated. Embedded objects should be '
                 'stabilized and managed by clinicians.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'A patient has a deep puncture wound from a nail. After bleeding control, what first aid '
          'documentation and care is important?',
  'topic': 'cpr-red-cross'},
 {'correct': 'The patch may interfere with pad adhesion and medication delivery during '
             'defibrillation',
  'difficulty': 'advanced',
  'distractors': ['Nitroglycerin patches explode when exposed to AED batteries',
                  'Patches must remain in place to improve shock success',
                  'Removal is only needed for pediatric patients'],
  'explanation': 'Patches can block skin contact and may be damaged during shock. They do not '
                 'explode, but adhesion and burn risk matter. The same principle applies '
                 'regardless of age.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why should rescuers remove a nitroglycerin patch before placing an AED pad over the '
          'same area?',
  'topic': 'cpr-aed'},
 {'correct': 'About one third the anterior-posterior chest diameter or at least 2 inches (5 cm)',
  'difficulty': 'beginner',
  'distractors': ['Exactly 1 cm for all children',
                  'As deep as possible without regard to recoil',
                  'Adult depth of 2.4 inches minimum for every toddler'],
  'explanation': 'Pediatric depth scales with body size at roughly one third AP diameter. '
                 'Extremely shallow compressions are ineffective. Uncontrolled maximal depth '
                 'ignores recoil and injury risk, and fixed adult minimums may be excessive for '
                 'small children.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'During child CPR, how deep should compressions be for most pediatric victims?',
  'topic': 'cpr-child'},
 {'correct': 'Lower half of the sternum, just below the nipple line',
  'difficulty': 'beginner',
  'distractors': ['Directly on the xiphoid process',
                  'Upper abdomen over the liver',
                  'Center of the forehead'],
  'explanation': 'Infant compressions target the sternum, avoiding the xiphoid. Abdominal '
                 'compressions do not perfuse the heart. The forehead is not a compression site.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Where should two-finger compressions be placed during single-rescuer infant CPR?',
  'topic': 'cpr-infant'},
 {'correct': 'They help bystanders locate devices quickly for early defibrillation',
  'difficulty': 'beginner',
  'distractors': ['They replace the need to perform chest compressions',
                  'They eliminate the need to activate EMS',
                  'They are only for hospital staff and not the public'],
  'explanation': 'Rapid AED retrieval shortens time to shock. Compressions and EMS activation '
                 'remain essential. Public access programs are designed for lay rescuers.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'How do community AED maps and signage support the Chain of Survival?',
  'topic': 'cpr-chain'},
 {'correct': 'Are you choking? while observing whether the cough is strong and air is moving',
  'difficulty': 'intermediate',
  'distractors': ['Are you having a heart attack? and begin CPR immediately',
                  'Can you drink water to push the food down?',
                  'Do you want an ambulance before you try to cough?'],
  'explanation': 'Direct questioning clarifies severity. Heart attack assessment differs from '
                 'choking. Water may worsen obstruction, and delaying cough effort is unnecessary '
                 'when obstruction is mild.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'What should you ask a conscious adult who appears to be choking but can still cough?',
  'topic': 'cpr-choking'},
 {'correct': '30 compressions to 2 ventilations',
  'difficulty': 'beginner',
  'distractors': ['15 compressions to 2 ventilations',
                  '5 compressions to 1 ventilation',
                  'Continuous ventilations without compressions'],
  'explanation': 'Adult BLS uses 30:2 for single and two lay rescuers. Fifteen to two is the '
                 'two-rescuer ratio for infants and children, not adults. Breath-only support does '
                 'not provide circulation in arrest.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'What is the recommended adult BLS compression-to-ventilation ratio for both single- and '
          'two-rescuer CPR?',
  'topic': 'cpr-adult'},
 {'correct': 'Keep the victim calm with the bitten limb at heart level and seek emergency care',
  'difficulty': 'advanced',
  'distractors': ['Cut the bite site and suck out venom',
                  'Apply ice directly to the bite for 30 minutes',
                  'Give alcohol to reduce pain before transport'],
  'explanation': 'Cutting and suction are ineffective and harmful. Ice and alcohol do not treat '
                 'envenomation and may worsen injury. Calm transport and EMS care are recommended.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Which statement about snakebite first aid is consistent with current Red Cross '
          'guidance?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Use a pediatric dose-attenuating system or pediatric pads per manufacturer '
             'instructions',
  'difficulty': 'intermediate',
  'distractors': ['Manually reduce battery voltage without manufacturer guidance',
                  'Use only one pad regardless of patient size',
                  'Withhold shocks until the patient weighs more than 200 lb'],
  'explanation': 'Pediatric systems attenuate energy appropriately. Unauthorized voltage changes '
                 'are unsafe. Weight cutoffs follow device labeling, not arbitrary limits.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When using pediatric AED pads on a child, what is the typical energy delivery approach?',
  'topic': 'cpr-aed'},
 {'correct': '30 compressions to 2 breaths',
  'difficulty': 'beginner',
  'distractors': ['15 compressions to 2 breaths',
                  'Continuous compressions only',
                  '10 compressions to 1 breath'],
  'explanation': 'Single rescuer pediatric BLS uses 30:2. Fifteen to two is for two rescuers. '
                 'Continuous compressions omit ventilations needed in many pediatric arrests.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'A lone rescuer performing child CPR should use which compression-to-ventilation ratio?',
  'topic': 'cpr-child'},
 {'correct': 'Support the head and neck and alternate 5 back slaps and 5 chest thrusts',
  'difficulty': 'advanced',
  'distractors': ['Perform abdominal thrusts identical to adult technique',
                  'Finger sweep the mouth before any back slaps',
                  'Lay the infant prone on your lap unsupported and shake'],
  'explanation': 'Infants receive back slaps and chest thrusts, not abdominal Heimlich maneuvers. '
                 'Blind sweeps are avoided. Unsupported shaking risks head injury.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'An infant is choking with ineffective cough and begins to look cyanotic while still '
          'responsive. What should you do?',
  'topic': 'cpr-infant'},
 {'correct': 'Increased rate of bystander CPR started before EMS arrival',
  'difficulty': 'intermediate',
  'distractors': ['Replacing hands-on CPR classes with posters only',
                  'Decreased placement of AEDs in public buildings',
                  'Reduced 911 call volume for all medical problems'],
  'explanation': 'Training is successful when more arrests receive early compressions. Social '
                 'media activity does not measure skill. AED placement should increase, not '
                 'decrease, and 911 calls for non-arrest issues are unrelated.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'Which outcome measure best reflects success of a community CPR training program?',
  'topic': 'cpr-chain'},
 {'correct': 'About every 2 minutes or sooner if compression quality falls',
  'difficulty': 'intermediate',
  'distractors': ['Only after ROSC',
                  'Every 15 seconds to maximize rest',
                  'Never; one person should compress the entire event'],
  'explanation': 'Rotation prevents fatigue that reduces depth and rate. Switching every 15 '
                 'seconds would cause excessive interruption. Single rescuer fatigue is a known '
                 'problem without rotation.',
  'references': ['American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'During team resuscitation, when should compressors switch roles during adult CPR?',
  'topic': 'cpr-adult'},
 {'correct': 'They can push an object deeper and injure the airway',
  'difficulty': 'beginner',
  'distractors': ['They always remove objects faster than back blows',
                  'They are required every cycle during CPR',
                  'They are only discouraged in infants, not adults'],
  'explanation': 'Blind sweeps risk worsening obstruction and tissue injury. They are not faster '
                 'or required routinely. The caution applies to all ages.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why are blind finger sweeps discouraged in BLS airway management?',
  'topic': 'cpr-choking'},
 {'correct': 'Forward lean prevents swallowing blood, which can cause nausea and airway irritation',
  'difficulty': 'beginner',
  'distractors': ['Backward tilt increases pressure on anterior nasal vessels to stop bleeding '
                  'faster',
                  'Position does not affect bleeding or swallowing',
                  'Forward lean is only for children, not adults'],
  'explanation': 'Swallowed blood irritates the stomach and may cause vomiting. Head-back position '
                 'does not reliably stop anterior bleeds and increases swallowing. Position '
                 'matters for adults and children.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'For a nosebleed, why is leaning slightly forward preferred over head-back positioning?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Stop compressions immediately, ensure everyone is clear, and deliver the shock',
  'difficulty': 'intermediate',
  'distractors': ['Continue compressions through the shock to save seconds',
                  'Remove pads before shocking to protect equipment',
                  'Ignore the shock advice and keep compressing for five more minutes'],
  'explanation': 'Everyone must clear before shock delivery. Compressions during shock are unsafe. '
                 'Pads remain in place for defibrillation, and ignoring shock advice delays '
                 'treatment for shockable rhythms.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'What should rescuers do if the AED advises a shock while a rescuer is still performing '
          'compressions?',
  'topic': 'cpr-aed'},
 {'correct': 'More frequent ventilations address common pediatric respiratory causes of arrest '
             'while one rescuer focuses on compressions',
  'difficulty': 'advanced',
  'distractors': ['Children do not need compressions during arrest',
                  'Ventilations are eliminated to speed defibrillation',
                  'Thirty to two is only for infants, never children'],
  'explanation': 'Pediatric arrests often begin with respiratory failure; additional breaths may '
                 'improve oxygenation. Compressions remain essential. Thirty to two is for single '
                 'rescuers, not exclusive to infants.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When two trained rescuers manage pediatric cardiac arrest, why is 15:2 preferred over '
          '30:2?',
  'topic': 'cpr-child'},
 {'correct': 'When the patient shows obvious signs of life such as purposeful movement and normal '
             'breathing',
  'difficulty': 'intermediate',
  'distractors': ['After exactly 10 minutes regardless of response',
                  'When the AED battery icon flashes',
                  'When bystanders ask you to stop even if the patient is unresponsive'],
  'explanation': 'AHA BLS continues CPR until signs of life, EMS takes over, or the rescuer is '
                 'exhausted. A fixed time limit is not used. AED prompts guide rhythm checks but '
                 'do not replace assessment of breathing and responsiveness.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When should a lay rescuer stop CPR on an adult who was in cardiac arrest?',
  'topic': 'cpr-adult'},
 {'correct': 'About one third the anterior-posterior diameter of the chest',
  'difficulty': 'beginner',
  'distractors': ['At least 2 inches in every newborn',
                  'Less than 1 cm for all infants',
                  'Maximal depth without allowing recoil'],
  'explanation': 'Infant depth is size-based at roughly one third AP chest diameter. Two inches is '
                 'an adult target. Shallow compressions do not perfuse the coronary arteries.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'How deep should infant compressions be during BLS CPR?',
  'topic': 'cpr-infant'},
 {'correct': 'To prevent rescuer injury and allow effective energy delivery through the chest',
  'difficulty': 'beginner',
  'distractors': ['Because the AED cannot shock if anyone is in the room',
                  'So the device can recharge the battery faster',
                  'Because compressions must continue through the shock'],
  'explanation': 'Electricity can injure anyone in contact with the patient. Clearing also ensures '
                 'pads maintain contact. Compressions must pause during shock delivery.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Why must rescuers clear the patient before an AED delivers a shock?',
  'topic': 'cpr-aed'},
 {'correct': 'Alternate 5 back blows and 5 abdominal thrusts until the object is expelled or the '
             'victim becomes unresponsive',
  'difficulty': 'intermediate',
  'distractors': ['10 abdominal thrusts only without back blows',
                  'Continuous back blows for five minutes',
                  'One abdominal thrust then immediate CPR while standing'],
  'explanation': 'AHA teaches cycles of 5 back blows and 5 abdominal thrusts. Abdominal thrusts '
                 'alone omit back blows. CPR begins only if the victim becomes unresponsive.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'What is the correct ratio of back blows to abdominal thrusts when treating severe '
          'choking in a responsive adult per AHA BLS?',
  'topic': 'cpr-choking'},
 {'correct': 'Promptly identifying cardiac arrest and activating the emergency response system',
  'difficulty': 'beginner',
  'distractors': ['Completing hospital discharge paperwork',
                  'Scheduling a follow-up clinic visit next week',
                  'Waiting to see if the patient wakes spontaneously before calling for help'],
  'explanation': 'Early recognition and 911 activation bring EMS and an AED. Delayed activation '
                 'weakens every downstream link. Administrative tasks are not substitutes for '
                 'emergency activation.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'Which action best describes the recognition link in the out-of-hospital Chain of '
          'Survival?',
  'topic': 'cpr-chain'}]
