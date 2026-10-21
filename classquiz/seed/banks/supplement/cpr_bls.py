# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

FACTS: list[dict] = [{'correct': '100 to 120 compressions per minute',
  'difficulty': 'beginner',
  'distractors': ['60 to 80 per minute',
                  '150 to 180 per minute',
                  'As fast as possible without limit'],
  'explanation': 'AHA recommends 100 to 120/min for adult compressions. 60 to 80 per minute is '
                 'incorrect because it does not follow AHA BLS for this situation; 100 to 120 '
                 'compressions per minute is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Adult CPR compression rate should be?',
  'topic': 'cpr-adult'},
 {'correct': 'Greater than 80% when possible',
  'difficulty': 'intermediate',
  'distractors': ['Less than 20%', 'Exactly 50% always', 'Only during shockable rhythms'],
  'explanation': 'AHA high-quality CPR metrics include CCF >80%. Less than 20% is incorrect '
                 'because it does not follow AHA BLS for this situation; Greater than 80% when '
                 'possible is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'High-quality CPR includes chest compression fraction?',
  'topic': 'cpr-adult'},
 {'correct': 'Improve coronary perfusion pressure',
  'difficulty': 'advanced',
  'distractors': ['Allow longer breaks for talking',
                  'Stopping compressions for several minutes without switching roles',
                  'Reduce need for AED'],
  'explanation': 'AHA emphasizes high chest compression fraction. Allow longer breaks for talking '
                 'is incorrect because it does not follow AHA BLS for this situation; Improve '
                 'coronary perfusion pressure is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'During adult CPR, rescuers should minimize interruptions in chest compressions to?',
  'topic': 'cpr-adult'},
 {'correct': 'Provide rescue breaths about every 6 seconds (10 breaths/min)',
  'difficulty': 'advanced',
  'distractors': ['Start immediate compressions at 120/min',
                  'Wait indefinitely',
                  'Apply AED first always'],
  'explanation': 'Rescue breathing is indicated for respiratory arrest with pulse. Start immediate '
                 'compressions at 120/min is incorrect because it does not follow AHA BLS for this '
                 'situation; Provide rescue breaths about every 6 seconds (10 breaths/min) is the '
                 'expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'If an adult victim has a palpable pulse but is not breathing, the rescuer should?',
  'topic': 'cpr-adult'},
 {'correct': 'Switch compressor roles about every 2 minutes',
  'difficulty': 'intermediate',
  'distractors': ['Stop all compressions permanently',
                  'Continuing as sole compressor until exhausted without a switch',
                  'Remove AED pads'],
  'explanation': 'Switching reduces fatigue and maintains quality. Stop all compressions '
                 'permanently is incorrect because it does not follow AHA BLS for this situation; '
                 'Switch compressor roles about every 2 minutes is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'When a second rescuer arrives during adult CPR, they should?',
  'topic': 'cpr-adult'},
 {'correct': 'Shave pad contact areas if needed so pads adhere fully',
  'difficulty': 'intermediate',
  'distractors': ['Skip pad placement if hair is present',
                  'Place pads over wet clothing only',
                  'Use one pad on the abdomen'],
  'explanation': 'Good contact improves rhythm analysis and shock delivery. Skip pad placement if '
                 'hair is present is incorrect because it does not follow AHA BLS for this '
                 'situation; Shave pad contact areas if needed so pads adhere fully is the '
                 'expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'Before attaching AED pads to a hairy chest, the rescuer should?',
  'topic': 'cpr-aed'},
 {'correct': 'Upper right chest and lower left side of chest',
  'difficulty': 'beginner',
  'distractors': ['Both pads on the abdomen', 'Only on the back', 'On the thighs'],
  'explanation': 'Standard anterior placement allows effective defibrillation. Both pads on the '
                 'abdomen is incorrect because it does not follow AHA BLS for this situation; '
                 'Upper right chest and lower left side of chest is the expected response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'AED pads for an adult should be placed?',
  'topic': 'cpr-aed'},
 {'correct': 'Ensure no one is touching the patient',
  'difficulty': 'intermediate',
  'distractors': ['Continue compressions through analysis',
                  'Pour water on the chest',
                  'Remove oxygen tubing only'],
  'explanation': 'Motion and contact can interfere with rhythm analysis. Continue compressions '
                 'through analysis is incorrect because it does not follow AHA BLS for this '
                 'situation; Ensure no one is touching the patient is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'While the AED analyzes rhythm, rescuers should?',
  'topic': 'cpr-aed'},
 {'correct': 'Immediately resume chest compressions',
  'difficulty': 'beginner',
  'distractors': ['Wait 5 minutes before touching the patient',
                  'Remove pads before compressions',
                  'Check pulse for 2 minutes first'],
  'explanation': 'Post-shock compressions maintain perfusion until rhythm check. Wait 5 minutes '
                 'before touching the patient is incorrect because it does not follow AHA BLS for '
                 'this situation; Immediately resume chest compressions is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'After an AED shock is delivered, the rescuer should?',
  'topic': 'cpr-aed'},
 {'correct': 'Resume high-quality CPR and recheck per device prompts',
  'difficulty': 'intermediate',
  'distractors': ['Stop all resuscitation efforts',
                  'Remove pads and leave',
                  'Deliver a manual shock anyway'],
  'explanation': 'Non-shockable rhythms require continuous CPR and treatment per ACLS. Stop all '
                 'resuscitation efforts is incorrect because it does not follow AHA BLS for this '
                 'situation; Resume high-quality CPR and recheck per device prompts is the '
                 'expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'If the AED advises no shock, the team should?',
  'topic': 'cpr-aed'},
 {'correct': 'Placing pads at least 1 inch away from the device when possible',
  'difficulty': 'advanced',
  'distractors': ['Avoiding AED use entirely',
                  'Placing one pad directly over the generator',
                  'Using pediatric pads only'],
  'explanation': 'Pad placement avoids damage and improves energy delivery. Avoiding AED use '
                 'entirely is incorrect because it does not follow AHA BLS for this situation; '
                 'Placing pads at least 1 inch away from the device when possible is the expected '
                 'response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'AED use on a patient with an implanted pacemaker requires?',
  'topic': 'cpr-aed'},
 {'correct': 'Use adult pads with appropriate placement per manufacturer',
  'difficulty': 'advanced',
  'distractors': ['Withhold defibrillation until adult pads arrive next day',
                  'Use only one adult pad',
                  'Place pads on the legs only'],
  'explanation': 'AHA allows adult pads on children when pediatric pads are unavailable. Withhold '
                 'defibrillation until adult pads arrive next day is incorrect because it does not '
                 'follow AHA BLS for this situation; Use adult pads with appropriate placement per '
                 'manufacturer is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'For a child needing an AED when no pediatric pads are available?',
  'topic': 'cpr-aed'},
 {'correct': 'As soon as the device is at the patient while CPR continues',
  'difficulty': 'beginner',
  'distractors': ['Only after 15 minutes of compressions',
                  'Before checking responsiveness',
                  'After EMS transports the patient'],
  'explanation': 'Early defibrillation improves survival in shockable rhythms. Only after 15 '
                 'minutes of compressions is incorrect because it does not follow AHA BLS for this '
                 'situation; As soon as the device is at the patient while CPR continues is the '
                 'expected response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr',
                 'American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'The AED power-on step should occur?',
  'topic': 'cpr-aed'},
 {'correct': 'Recognition, CPR, defibrillation, and advanced care',
  'difficulty': 'beginner',
  'distractors': ['Billing, coding, and scheduling only',
                  'Cooling before any CPR',
                  'Medication without compressions'],
  'explanation': 'Each link must occur quickly to improve neurologically intact survival. Billing, '
                 'coding, and scheduling only is incorrect because it does not follow AHA BLS for '
                 'this situation; Recognition, CPR, defibrillation, and advanced care is the '
                 'expected response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'The out-of-hospital adult Chain of Survival includes early?',
  'topic': 'cpr-chain'},
 {'correct': 'Early high-quality CPR',
  'difficulty': 'beginner',
  'distractors': ['Post-arrest hypothermia only',
                  'Hospital discharge planning',
                  'Insurance authorization'],
  'explanation': 'Immediate compressions bridge time to defibrillation and EMS. Post-arrest '
                 'hypothermia only is incorrect because it does not follow AHA BLS for this '
                 'situation; Early high-quality CPR is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'Bystander CPR most directly strengthens which chain link?',
  'topic': 'cpr-chain'},
 {'correct': 'Early defibrillation before EMS arrival',
  'difficulty': 'intermediate',
  'distractors': ['Delayed EMS activation', 'Removal of CPR training', 'Mandatory sedation first'],
  'explanation': 'AEDs in public settings shorten time to first shock. Delayed EMS activation is '
                 'incorrect because it does not follow AHA BLS for this situation; Early '
                 'defibrillation before EMS arrival is the expected response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr',
                 'American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'Public access defibrillation programs improve survival by adding?',
  'topic': 'cpr-chain'},
 {'correct': 'Hemodynamics, ventilation, and targeted temperature management when indicated',
  'difficulty': 'advanced',
  'distractors': ['Only paperwork completion',
                  'Immediate discharge home',
                  'Withholding oxygen always'],
  'explanation': 'Hospital care optimizes recovery after ROSC. Only paperwork completion is '
                 'incorrect because it does not follow AHA BLS for this situation; Hemodynamics, '
                 'ventilation, and targeted temperature management when indicated is the expected '
                 'response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Integrated post-cardiac arrest care addresses?',
  'topic': 'cpr-chain'},
 {'correct': 'Starting compressions while EMS is en route',
  'difficulty': 'intermediate',
  'distractors': ['Avoiding any chest compressions',
                  'Waiting for a physician on scene',
                  'Using only back blows'],
  'explanation': 'Dispatcher-guided CPR increases bystander intervention rates. Avoiding any chest '
                 'compressions is incorrect because it does not follow AHA BLS for this situation; '
                 'Starting compressions while EMS is en route is the expected response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'Telephone-assisted CPR dispatch instructions help bystanders with?',
  'topic': 'cpr-chain'},
 {'correct': 'Willingness and ability to start the CPR link early',
  'difficulty': 'beginner',
  'distractors': ['Laboratory specimen labeling', 'Vaccine storage', 'Surgical sterile technique'],
  'explanation': 'Education increases confidence in emergency response. Laboratory specimen '
                 'labeling is incorrect because it does not follow AHA BLS for this situation; '
                 'Willingness and ability to start the CPR link early is the expected response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr',
                 'American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Community CPR training primarily improves?',
  'topic': 'cpr-chain'},
 {'correct': 'Failure to activate EMS and retrieve an AED promptly',
  'difficulty': 'intermediate',
  'distractors': ['Using gloves during compressions',
                  'Documenting vitals in arrest',
                  'Switching compressors every 2 minutes'],
  'explanation': 'Delays in recognition and device access reduce shock success. Using gloves '
                 'during compressions is incorrect because it does not follow AHA BLS for this '
                 'situation; Failure to activate EMS and retrieve an AED promptly is the expected '
                 'response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'A weak link in the Chain of Survival that delays defibrillation is?',
  'topic': 'cpr-chain'},
 {'correct': 'Rapid recognition, team response, and high-quality CPR',
  'difficulty': 'intermediate',
  'distractors': ['Outpatient scheduling',
                  'Skipping debriefing',
                  'Deferring compressions for imaging'],
  'explanation': 'In-hospital teams emphasize prevention of interruptions. Outpatient scheduling '
                 'is incorrect because it does not follow AHA BLS for this situation; Rapid '
                 'recognition, team response, and high-quality CPR is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'Hospital in-hospital cardiac arrest systems focus on?',
  'topic': 'cpr-chain'},
 {'correct': 'Ensuring scene safety and checking responsiveness',
  'difficulty': 'beginner',
  'distractors': ['Immediate defibrillation without assessment',
                  'Leaving the child alone',
                  'Calling parents only'],
  'explanation': 'AHA pediatric algorithm starts with safety and assessment. Immediate '
                 'defibrillation without assessment is incorrect because it does not follow AHA '
                 'BLS for this situation; Ensuring scene safety and checking responsiveness is the '
                 'expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Pediatric BLS begins with?',
  'topic': 'cpr-child'},
 {'correct': 'Activate EMS and get an AED as soon as possible',
  'difficulty': 'intermediate',
  'distractors': ['Delay help for 30 minutes',
                  'Withhold all compressions',
                  'Delaying EMS activation to search the building alone'],
  'explanation': 'Early defibrillation improves outcomes in arrest. Delay help for 30 minutes is '
                 'incorrect because it does not follow AHA BLS for this situation; Activate EMS '
                 'and get an AED as soon as possible is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'For a child with sudden collapse, the rescuer should?',
  'topic': 'cpr-child'},
 {'correct': 'Two-rescuer infant CPR',
  'difficulty': 'advanced',
  'distractors': ['Adult CPR only', 'Choking conscious adult', 'AED maintenance'],
  'explanation': 'Two-thumb technique is taught for infant two-rescuer CPR. Adult CPR only is '
                 'incorrect because it does not follow AHA BLS for this situation; Two-rescuer '
                 'infant CPR is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Two-thumb encircling hand technique for chest compressions is used for?',
  'topic': 'cpr-child'},
 {'correct': '15 compressions to 2 breaths',
  'difficulty': 'advanced',
  'distractors': ['30:2 only always', '5:1', 'Continuous breaths without compressions'],
  'explanation': 'Two-rescuer pediatric ratio differs from single rescuer. 30:2 only always is '
                 'incorrect because it does not follow AHA BLS for this situation; 15 compressions '
                 'to 2 breaths is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Compression-to-ventilation ratio for two-rescuer child CPR is?',
  'topic': 'cpr-child'},
 {'correct': 'At least one-third the depth of the chest',
  'difficulty': 'intermediate',
  'distractors': ['Only 1 cm regardless of size',
                  'Until ribs always crack',
                  'Without allowing full recoil'],
  'explanation': 'Adequate depth with full recoil is required. Only 1 cm regardless of size is '
                 'incorrect because it does not follow AHA BLS for this situation; At least '
                 'one-third the depth of the chest is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When performing CPR on a child, compress the chest?',
  'topic': 'cpr-child'},
 {'correct': 'Activate EMS if not already done and retrieve AED',
  'difficulty': 'intermediate',
  'distractors': ['Stop CPR forever', 'Document only', 'Remove clothing for photos'],
  'explanation': 'Lone rescuer sequence balances CPR and activation. Stop CPR forever is incorrect '
                 'because it does not follow AHA BLS for this situation; Activate EMS if not '
                 'already done and retrieve AED is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'If a lone rescuer finds an unresponsive child, after 2 minutes of CPR they should?',
  'topic': 'cpr-child'},
 {'correct': 'Abdominal thrusts (Heimlich) if appropriate for age/size',
  'difficulty': 'intermediate',
  'distractors': ['Blind finger sweeps in mouth',
                  'Chest compressions only initially',
                  'Back blows only for all ages'],
  'explanation': 'AHA choking algorithm uses age-appropriate maneuvers. Blind finger sweeps in '
                 'mouth is incorrect because it does not follow AHA BLS for this situation; '
                 'Abdominal thrusts (Heimlich) if appropriate for age/size is the expected '
                 'response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Foreign-body airway obstruction in a conscious child is treated first with?',
  'topic': 'cpr-child'},
 {'correct': 'Provide oxygen and monitor per advanced guidance',
  'difficulty': 'advanced',
  'distractors': ['Stop all monitoring', 'Discharge immediately', 'Withhold warmth'],
  'explanation': 'Post-ROSC care includes support and monitoring. Stop all monitoring is incorrect '
                 'because it does not follow AHA BLS for this situation; Provide oxygen and '
                 'monitor per advanced guidance is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'After ROSC in a child, the rescuer should?',
  'topic': 'cpr-child'},
 {'correct': 'Abdominal thrusts until the object is expelled or patient becomes unresponsive',
  'difficulty': 'intermediate',
  'distractors': ['Blind finger sweeps in the mouth',
                  'Immediate chest compressions while standing',
                  'No intervention until EMS arrives'],
  'explanation': 'AHA teaches abdominal thrusts for responsive adults with severe choking. Blind '
                 'finger sweeps in the mouth is incorrect because it does not follow AHA BLS for '
                 'this situation; Abdominal thrusts until the object is expelled or patient '
                 'becomes unresponsive is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'A conscious adult with severe airway obstruction should receive?',
  'topic': 'cpr-choking'},
 {'correct': 'Back blows and chest thrusts per BLS sequence',
  'difficulty': 'intermediate',
  'distractors': ['Abdominal thrusts only',
                  'Heimlich maneuver as for adults',
                  'Finger sweeps in the mouth first'],
  'explanation': 'Infant choking management differs from adult techniques. Abdominal thrusts only '
                 'is incorrect because it does not follow AHA BLS for this situation; Back blows '
                 'and chest thrusts per BLS sequence is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'For a conscious infant with airway obstruction, initial maneuvers include?',
  'topic': 'cpr-choking'},
 {'correct': 'Lower the victim safely and begin CPR starting with compressions',
  'difficulty': 'advanced',
  'distractors': ['Continue abdominal thrusts only',
                  'Leave the victim sitting upright',
                  'Wait for pulse check for 2 minutes'],
  'explanation': 'CPR compressions may dislodge the obstruction and provide circulation. Continue '
                 'abdominal thrusts only is incorrect because it does not follow AHA BLS for this '
                 'situation; Lower the victim safely and begin CPR starting with compressions is '
                 'the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'If a choking victim becomes unresponsive, the rescuer should?',
  'topic': 'cpr-choking'},
 {'correct': 'Encouraging forceful coughing while monitoring',
  'difficulty': 'beginner',
  'distractors': ['Immediate abdominal thrusts',
                  'Back blows in all ages without assessment',
                  'Slapping the back while leaning forward'],
  'explanation': 'Effective cough indicates partial airway obstruction. Immediate abdominal '
                 'thrusts is incorrect because it does not follow AHA BLS for this situation; '
                 'Encouraging forceful coughing while monitoring is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid',
                 'American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Mild choking in a responsive person is managed by?',
  'topic': 'cpr-choking'},
 {'correct': 'Look in the mouth for visible object before breaths and remove if seen',
  'difficulty': 'advanced',
  'distractors': ['Perform blind finger sweeps each cycle',
                  'Skip ventilations entirely',
                  'Use only jaw thrust without compressions'],
  'explanation': 'Visible foreign bodies may be removed; blind sweeps are not recommended. Perform '
                 'blind finger sweeps each cycle is incorrect because it does not follow AHA BLS '
                 'for this situation; Look in the mouth for visible object before breaths and '
                 'remove if seen is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'During CPR on an unresponsive choking victim, the rescuer should?',
  'topic': 'cpr-choking'},
 {'correct': 'Chest thrusts instead of abdominal thrusts when indicated',
  'difficulty': 'advanced',
  'distractors': ['No assistance until delivery',
                  'Only back blows while prone',
                  'CPR before any thrusts while conscious'],
  'explanation': 'Chest thrusts reduce risk when abdominal thrusts are difficult. No assistance '
                 'until delivery is incorrect because it does not follow AHA BLS for this '
                 'situation; Chest thrusts instead of abdominal thrusts when indicated is the '
                 'expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Pregnant or obese patients with severe choking may need?',
  'topic': 'cpr-choking'},
 {'correct': 'Silent cough, inability to speak, and clutching the throat',
  'difficulty': 'beginner',
  'distractors': ['Loud productive cough only',
                  'Slow deep breathing with whistling',
                  'Chest pain without dyspnea'],
  'explanation': 'Recognition prompts immediate airway intervention. Loud productive cough only is '
                 'incorrect because it does not follow AHA BLS for this situation; Silent cough, '
                 'inability to speak, and clutching the throat is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Universal sign of severe choking often includes?',
  'topic': 'cpr-choking'},
 {'correct': 'Be evaluated by EMS or medical personnel because complications can occur',
  'difficulty': 'intermediate',
  'distractors': ['Be discharged without assessment',
                  'Eat a large meal immediately',
                  'Avoid medical care if color returns'],
  'explanation': 'Airway edema or residual obstruction may develop later. Be discharged without '
                 'assessment is incorrect because it does not follow AHA BLS for this situation; '
                 'Be evaluated by EMS or medical personnel because complications can occur is the '
                 'expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid',
                 'American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'After successful relief of choking, the patient should?',
  'topic': 'cpr-choking'},
 {'correct': 'Just below the nipple line on the sternum',
  'difficulty': 'beginner',
  'distractors': ['On the upper abdomen', 'On the forehead', 'Over the xiphoid process'],
  'explanation': 'Correct hand placement optimizes coronary perfusion. On the upper abdomen is '
                 'incorrect because it does not follow AHA BLS for this situation; Just below the '
                 'nipple line on the sternum is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Infant CPR compressions with two fingers are placed?',
  'topic': 'cpr-infant'},
 {'correct': 'About one-third the anterior-posterior diameter of the chest',
  'difficulty': 'intermediate',
  'distractors': ['At least 3 inches always',
                  'Less than 1 cm regardless of size',
                  'As deep as possible without recoil'],
  'explanation': 'AHA specifies one-third AP chest depth for infants. At least 3 inches always is '
                 'incorrect because it does not follow AHA BLS for this situation; About one-third '
                 'the anterior-posterior diameter of the chest is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Compression depth for infant CPR should be?',
  'topic': 'cpr-infant'},
 {'correct': '30 compressions to 2 breaths',
  'difficulty': 'beginner',
  'distractors': ['15:2 only', '5:1', 'Continuous compressions without breaths'],
  'explanation': 'Single rescuer pediatric BLS uses 30:2. 15:2 only is incorrect because it does '
                 'not follow AHA BLS for this situation; 30 compressions to 2 breaths is the '
                 'expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'The lone rescuer compression-ventilation ratio for infant CPR is?',
  'topic': 'cpr-infant'},
 {'correct': 'Cover mouth and nose with the mouth to make the chest rise',
  'difficulty': 'intermediate',
  'distractors': ['Pinch the nose and seal only the mouth',
                  'Blow forcefully until the stomach distends maximally',
                  'Deliver breaths only through a nasal cannula'],
  'explanation': 'Infant ventilations require mouth-and-nose seal. Pinch the nose and seal only '
                 'the mouth is incorrect because it does not follow AHA BLS for this situation; '
                 'Cover mouth and nose with the mouth to make the chest rise is the expected '
                 'response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'When giving breaths to an infant, the rescuer should?',
  'topic': 'cpr-infant'},
 {'correct': 'Activate EMS and obtain an AED if not already done',
  'difficulty': 'intermediate',
  'distractors': ['Stop all care',
                  'Transport alone without calling',
                  'Wait for parents before help'],
  'explanation': 'EMS activation and AED access are time-critical. Stop all care is incorrect '
                 'because it does not follow AHA BLS for this situation; Activate EMS and obtain '
                 'an AED if not already done is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'If an infant is unresponsive and not breathing normally, after 2 minutes of CPR a lone '
          'rescuer should?',
  'topic': 'cpr-infant'},
 {'correct': 'Two-thumb encircling hands or two-finger technique per training',
  'difficulty': 'advanced',
  'distractors': ['Heel of one hand only as for adults',
                  'Abdominal thrusts',
                  'No compressions, breaths only'],
  'explanation': 'Two-thumb technique is preferred with two rescuers when possible. Heel of one '
                 'hand only as for adults is incorrect because it does not follow AHA BLS for this '
                 'situation; Two-thumb encircling hands or two-finger technique per training is '
                 'the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Two-rescuer infant CPR uses which compression technique?',
  'topic': 'cpr-infant'},
 {'correct': 'May use adult AED with pads placed per manufacturer instructions',
  'difficulty': 'advanced',
  'distractors': ['Is contraindicated in all infants',
                  'Requires manual internal paddles only',
                  'Should be delayed until age 8'],
  'explanation': 'AHA permits adult AED use when pediatric equipment is not available. Is '
                 'contraindicated in all infants is incorrect because it does not follow AHA BLS '
                 'for this situation; May use adult AED with pads placed per manufacturer '
                 'instructions is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support',
                 'American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr'],
  'stem': 'AED use in infants when pediatric pads are unavailable?',
  'topic': 'cpr-infant'},
 {'correct': 'Maintaining airway, oxygenation, and warmth while monitoring',
  'difficulty': 'advanced',
  'distractors': ['Immediate oral feeding',
                  'Removing all monitoring',
                  'Discharge without evaluation'],
  'explanation': 'Post-ROSC infants need ongoing assessment and treatment. Immediate oral feeding '
                 'is incorrect because it does not follow AHA BLS for this situation; Maintaining '
                 'airway, oxygenation, and warmth while monitoring is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'After ROSC in an infant, supportive care includes?',
  'topic': 'cpr-infant'},
 {'correct': 'Cleaning the wound and applying a sterile dressing',
  'difficulty': 'beginner',
  'distractors': ['Ignoring wound cleaning',
                  'Applying butter to burns',
                  'Using tourniquet for all scrapes'],
  'explanation': 'Basic wound care reduces infection risk. Ignoring wound cleaning is incorrect '
                 'because it does not follow AHA BLS for this situation; Cleaning the wound and '
                 'applying a sterile dressing is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'For a minor scrape with bleeding controlled, Red Cross first aid includes?',
  'topic': 'cpr-red-cross'},
 {'correct': 'A clean cloth or dressing over the wound',
  'difficulty': 'beginner',
  'distractors': ['Dirty rags from the floor',
                  'Ice directly in the wound bed',
                  'No pressure for 10 minutes'],
  'explanation': 'Direct pressure assists clot formation. Dirty rags from the floor is incorrect '
                 'because it does not follow AHA BLS for this situation; A clean cloth or dressing '
                 'over the wound is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'When applying direct pressure to bleeding, use?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Difficulty breathing or swelling of tongue/lips',
  'difficulty': 'intermediate',
  'distractors': ['Mild localized hive only',
                  'Slow pulse without symptoms',
                  'Dry skin without rash'],
  'explanation': 'Systemic allergic reactions are emergencies. Mild localized hive only is '
                 'incorrect because it does not follow AHA BLS for this situation; Difficulty '
                 'breathing or swelling of tongue/lips is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid',
                 'NHA: CCMA certification — https://www.nhanow.com/certifications/ccma'],
  'stem': 'Signs of anaphylaxis that warrant calling 911 include?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Rest, ice, compression, and elevation (RICE)',
  'difficulty': 'beginner',
  'distractors': ['Heat application immediately',
                  'Aggressive massage of injury',
                  'Weight-bearing exercise'],
  'explanation': 'RICE limits swelling in acute soft-tissue injury. Heat application immediately '
                 'is incorrect because it does not follow AHA BLS for this situation; Rest, ice, '
                 'compression, and elevation (RICE) is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'For a suspected sprain, initial care is often?',
  'topic': 'cpr-red-cross'},
 {'correct': 'High and tight on the limb proximal to the wound',
  'difficulty': 'advanced',
  'distractors': ['Over the wound only', 'On a joint whenever possible', 'Loosely for comfort'],
  'explanation': 'High placement occludes arterial flow when direct pressure fails. Over the wound '
                 'only is incorrect because it does not follow AHA BLS for this situation; High '
                 'and tight on the limb proximal to the wound is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'A tourniquet for life-threatening extremity bleeding should be placed?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Flush with water for at least 15 minutes while calling for help',
  'difficulty': 'intermediate',
  'distractors': ['Rub the eye vigorously',
                  'Apply ointment before flushing',
                  'Wait until next day to rinse'],
  'explanation': 'Immediate irrigation dilutes chemical injury. Rub the eye vigorously is '
                 'incorrect because it does not follow AHA BLS for this situation; Flush with '
                 'water for at least 15 minutes while calling for help is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid',
                 'OSHA: Bloodborne Pathogens Standard (29 CFR 1910.1030) — '
                 'https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030'],
  'stem': 'For chemical splash to the eye, first aid is?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Heavy sweating, weakness, and cool clammy skin',
  'difficulty': 'intermediate',
  'distractors': ['Hot dry skin with altered mental status only',
                  'No fluid loss',
                  'Bradycardia without symptoms'],
  'explanation': 'Recognition allows cooling and fluids per protocol. Hot dry skin with altered '
                 'mental status only is incorrect because it does not follow AHA BLS for this '
                 'situation; Heavy sweating, weakness, and cool clammy skin is the expected '
                 'response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Heat exhaustion may present with?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Face droop, Arm weakness, Speech difficulty, Time to call 911',
  'difficulty': 'beginner',
  'distractors': ['Fever, Anemia, Swelling, Temperature',
                  'Foot pain only',
                  'Forget allergies only'],
  'explanation': 'Early EMS activation enables rapid stroke care. Fever, Anemia, Swelling, '
                 'Temperature is incorrect because it does not follow AHA BLS for this situation; '
                 'Face droop, Arm weakness, Speech difficulty, Time to call 911 is the expected '
                 'response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'For suspected stroke, FAST assessment includes?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Emergency medical evaluation',
  'difficulty': 'intermediate',
  'distractors': ['Only aloe vera at home',
                  'Popping blisters immediately',
                  'Applying ice directly to char'],
  'explanation': 'Serious burns risk compartment syndrome and shock. Only aloe vera at home is '
                 'incorrect because it does not follow AHA BLS for this situation; Emergency '
                 'medical evaluation is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Burns with charred skin or circumferential limb burns need?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Pinch soft part of nose for 10–15 minutes',
  'difficulty': 'beginner',
  'distractors': ['Tilt head fully backward',
                  'Pack gauze deep into nasopharynx blindly',
                  'Ignore bleeding if mild'],
  'explanation': 'Forward lean prevents swallowing blood. Tilt head fully backward is incorrect '
                 'because it does not follow AHA BLS for this situation; Pinch soft part of nose '
                 'for 10–15 minutes is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Nosebleed first aid with the patient leaning slightly forward?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Gentle handling, removing wet clothing, and gradual rewarming',
  'difficulty': 'advanced',
  'distractors': ['Rapid hot tub immersion always',
                  'Rubbing frostbitten tissue vigorously',
                  'Giving alcohol to warm up'],
  'explanation': 'Gentle rewarming prevents afterdrop and arrhythmias. Rapid hot tub immersion '
                 'always is incorrect because it does not follow AHA BLS for this situation; '
                 'Gentle handling, removing wet clothing, and gradual rewarming is the expected '
                 'response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Hypothermia management in the field includes?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Remove stinger by scraping and apply cold pack',
  'difficulty': 'beginner',
  'distractors': ['Squeeze venom sac with fingers',
                  'Apply tourniquet proximal',
                  'Ignore patient if breathing is normal'],
  'explanation': 'Scraping avoids injecting more venom. Squeeze venom sac with fingers is '
                 'incorrect because it does not follow AHA BLS for this situation; Remove stinger '
                 'by scraping and apply cold pack is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'For a bee sting with localized swelling only?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Immobilize above and below the injury',
  'difficulty': 'intermediate',
  'distractors': ['Splint only the joint distal',
                  'Remove all circulation checks',
                  'Force limb into normal alignment'],
  'explanation': 'Immobilization reduces pain and further injury. Splint only the joint distal is '
                 'incorrect because it does not follow AHA BLS for this situation; Immobilize '
                 'above and below the injury is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Splinting an injured extremity aims to?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Hypoglycemia requiring fast-acting sugar if conscious and able to swallow',
  'difficulty': 'intermediate',
  'distractors': ['Hyperglycemia always treated with insulin by lay rescuers',
                  'No need for EMS',
                  'Only water restriction'],
  'explanation': 'Low blood glucose needs rapid glucose if safe to swallow. Hyperglycemia always '
                 'treated with insulin by lay rescuers is incorrect because it does not follow AHA '
                 'BLS for this situation; Hypoglycemia requiring fast-acting sugar if conscious '
                 'and able to swallow is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid',
                 'NHA: CCMA certification — https://www.nhanow.com/certifications/ccma'],
  'stem': 'Diabetic emergency with confusion and sweating may indicate?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Substance, amount, time, and patient weight/age',
  'difficulty': 'intermediate',
  'distractors': ['Patient social security number only',
                  'Favorite foods',
                  'Insurance group number only'],
  'explanation': 'Accurate information guides antidote and observation advice. Patient social '
                 'security number only is incorrect because it does not follow AHA BLS for this '
                 'situation; Substance, amount, time, and patient weight/age is the expected '
                 'response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Poisoning questions for poison control should include?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Scene safety, shutting off power if possible, and EMS activation',
  'difficulty': 'advanced',
  'distractors': ['Immediate touch while wires are live',
                  'Only bandaging entry wound',
                  'No cardiac monitoring ever'],
  'explanation': 'Electricity can cause dysrhythmias and internal injury. Immediate touch while '
                 'wires are live is incorrect because it does not follow AHA BLS for this '
                 'situation; Scene safety, shutting off power if possible, and EMS activation is '
                 'the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Electrical injury victims require?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Keep tooth moist in milk or saline and seek urgent dental care',
  'difficulty': 'intermediate',
  'distractors': ['Scrub tooth with soap and dry on paper',
                  'Discard tooth if dirty',
                  'Store in tap water only long term'],
  'explanation': 'Moist storage improves reimplantation success. Scrub tooth with soap and dry on '
                 'paper is incorrect because it does not follow AHA BLS for this situation; Keep '
                 'tooth moist in milk or saline and seek urgent dental care is the expected '
                 'response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'For a knocked-out permanent tooth, transport should?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Pale cool skin, rapid pulse, and altered mental status',
  'difficulty': 'intermediate',
  'distractors': ['Slow pulse with hypertension only',
                  'Warm flushed skin always',
                  'Improved alertness'],
  'explanation': 'Shock requires positioning, bleeding control, and EMS. Slow pulse with '
                 'hypertension only is incorrect because it does not follow AHA BLS for this '
                 'situation; Pale cool skin, rapid pulse, and altered mental status is the '
                 'expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Signs of shock after injury include?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Removing from play and medical evaluation',
  'difficulty': 'intermediate',
  'distractors': ['Returning immediately if athlete insists',
                  'Only icing the neck',
                  'Ignoring headache'],
  'explanation': 'Second impact syndrome risk mandates evaluation. Returning immediately if '
                 'athlete insists is incorrect because it does not follow AHA BLS for this '
                 'situation; Removing from play and medical evaluation is the expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'A concussion in sports should be managed by?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Rapid extrication and airway management while protecting rescuers',
  'difficulty': 'advanced',
  'distractors': ['Solo digging without EMS notification',
                  'Delayed rescue until equipment arrives hours later',
                  'Hyperventilation coaching only'],
  'explanation': 'Airway and hypothermia care are time-critical. Solo digging without EMS '
                 'notification is incorrect because it does not follow AHA BLS for this situation; '
                 'Rapid extrication and airway management while protecting rescuers is the '
                 'expected response.',
  'references': ['American Red Cross: First Aid — https://www.redcross.org/take-a-class/first-aid'],
  'stem': 'Avalanche or burial situations prioritize?',
  'topic': 'cpr-red-cross'},
 {'correct': 'Adult sudden cardiac arrest when unwilling to give breaths',
  'difficulty': 'intermediate',
  'distractors': ['All pediatric arrests',
                  'Choking with foreign body',
                  'Drowning without special training'],
  'explanation': 'AHA supports hands-only CPR for witnessed adult collapse. All pediatric arrests '
                 'is incorrect because it does not follow AHA BLS for this situation; Adult sudden '
                 'cardiac arrest when unwilling to give breaths is the expected response.',
  'references': ['American Heart Association: What is CPR — '
                 'https://cpr.heart.org/en/resources/what-is-cpr',
                 'American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'Compression-only CPR may be used by lay rescuers for?',
  'topic': 'cpr-adult'},
 {'correct': 'Upper-right chest and lower-left side',
  'difficulty': 'beginner',
  'distractors': ['Both pads on the abdomen',
                  "On the patient's back only while standing on table",
                  'Overlapping pads on sternum'],
  'explanation': 'Pad placement allows current through the heart. Both pads on the abdomen is '
                 'incorrect because it does not follow AHA BLS for this situation; Upper-right '
                 'chest and lower-left side is the expected response.',
  'references': ['American Heart Association: Adult Basic Life Support Guidelines — '
                 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support'],
  'stem': 'AED pad placement for an adult is typically?',
  'topic': 'cpr-adult'},
 {'correct': 'Switching compressors every 2 minutes',
  'difficulty': 'intermediate',
  'distractors': ['Stopping CPR for 10 minutes',
                  'Removing AED pads',
                  'Letting compressions become shallow without switching'],
  'explanation': 'Rotation maintains adequate depth and rate. Stopping CPR for 10 minutes is '
                 'incorrect because it does not follow AHA BLS for this situation; Switching '
                 'compressors every 2 minutes is the expected response.',
  'references': ['American Heart Association: High-Quality CPR — '
                 'https://cpr.heart.org/en/resuscitation-science/high-quality-cpr'],
  'stem': 'Fatigue during compressions is managed by?',
  'topic': 'cpr-adult'}]
