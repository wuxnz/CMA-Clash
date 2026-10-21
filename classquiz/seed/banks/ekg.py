# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

FACTS: list[dict] = [
 {
 "topic": "ekg-leads",
 "stem": "For a standard 12-lead EKG, limb electrodes include:",
 "correct": "RA, LA, RL, and LL placements on arms and legs",
 "distractors": [
 "Only chest leads",
 "Electrodes on the forehead only",
 "A single chest electrode"
 ],
 "explanation": "Limb leads form the basis of the frontal plane.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-leads",
 "stem": "Chest lead V1 is typically placed:",
 "correct": "Fourth intercostal space, right sternal border",
 "distractors": [
 "Left midclavicular line only",
 "Over the umbilicus",
 "On the right shoulder"
 ],
 "explanation": "Standard precordial placement improves consistency.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-leads",
 "stem": "Chest lead V2 is placed:",
 "correct": "Fourth intercostal space, left sternal border",
 "distractors": [
 "Fifth intercostal space, midaxillary line",
 "Over the xiphoid only",
 "On the left ankle"
 ],
 "explanation": "V1 and V2 are parasternal leads.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-leads",
 "stem": "Lead II is often monitored because it:",
 "correct": "Usually shows clear P waves and QRS for rhythm checks",
 "distractors": [
 "Measures blood pressure",
 "Is always artifact-free",
 "Replaces all chest leads"
 ],
 "explanation": "Lead II is common for single-lead monitoring.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-leads",
 "stem": "Right leg (RL) electrode on EKG often serves as:",
 "correct": "An electrical ground/reference",
 "distractors": [
 "Active recording only for ventricular rhythm",
 "A substitute for V6",
 "A blood pressure sensor"
 ],
 "explanation": "RL reduces noise in many systems.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-leads",
 "stem": "Before attaching electrodes, skin should be:",
 "correct": "Clean and dry; prep if needed for oil or hair",
 "distractors": [
 "Soaked in saline",
 "Covered with lotion",
 "Left dirty"
 ],
 "explanation": "Good contact reduces artifact and baseline wander.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-leads",
 "stem": "V4 is commonly placed at the:",
 "correct": "Fifth intercostal space, left midclavicular line",
 "distractors": [
 "Second intercostal space right",
 "Right costal margin only",
 "Posterior thorax"
 ],
 "explanation": "V4 is a key precordial lead for anterior forces.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-leads",
 "stem": "V5 is typically at:",
 "correct": "Fifth intercostal space, anterior axillary line",
 "distractors": [
 "Fourth intercostal right sternal",
 "Suprasternal notch",
 "Left foot"
 ],
 "explanation": "V5 with V6 helps lateral wall assessment.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-leads",
 "stem": "V6 is placed at:",
 "correct": "Fifth intercostal space, midaxillary line",
 "distractors": [
 "Right sternal border",
 "Epigastrium",
 "Chin"
 ],
 "explanation": "V6 completes lateral precordial placement.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-leads",
 "stem": "If electrode cables are reversed between arms, the tracing may show:",
 "correct": "Axis and morphology changes suggesting limb lead reversal",
 "distractors": [
 "Normal tracing always",
 "Only faster heart rate",
 "No effect"
 ],
 "explanation": "Technician should verify lead placement.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-leads",
 "stem": "EKG paper speed standard is:",
 "correct": "25 mm per second",
 "distractors": [
 "50 mm per minute",
 "10 mm per second always",
 "Variable without labeling"
 ],
 "explanation": "Speed affects interval measurement.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-leads",
 "stem": "Standard EKG calibration mark is:",
 "correct": "1 mV deflection equals 10 mm (1 cm) at standard gain",
 "distractors": [
 "5 mm per mV always",
 "Unlabeled",
 "Depends on patient weight"
 ],
 "explanation": "Calibration checks voltage amplitude.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Normal sinus rhythm shows:",
 "correct": "Upright P before each QRS and regular rate ~60 to 100",
 "distractors": [
 "No P waves and irregularly irregular rhythm",
 "Wide QRS tachycardia only",
 "P waves unrelated to QRS"
 ],
 "explanation": "NSR originates from the SA node with 1:1 conduction.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Atrial fibrillation is characterized by:",
 "correct": "Irregularly irregular rhythm and absent distinct P waves",
 "distractors": [
 "Regular rhythm with sawtooth P waves",
 "Every P followed by QRS with constant PR",
 "Bradycardia only"
 ],
 "explanation": "AF is a common irregular supraventricular arrhythmia.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Ventricular tachycardia typically shows:",
 "correct": "Wide QRS tachycardia often >100 bpm",
 "distractors": [
 "Narrow QRS with P for every QRS",
 "Slow irregular rhythm with fibrillatory waves",
 "Flat line"
 ],
 "explanation": "VT is a life-threatening wide-complex tachycardia.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Asystole appears as:",
 "correct": "Flat or nearly flat line without organized electrical activity",
 "distractors": [
 "Chaotic irregular baseline",
 "Normal P-QRS-T cycles",
 "Only P waves"
 ],
 "explanation": "Asystole requires CPR per ACLS/BLS pathways.",
 "references": [
 "AHA BLS"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Pulseless electrical activity (PEA) is:",
 "correct": "Organized electrical activity without palpable pulse",
 "distractors": [
 "No electrical activity at all",
 "Normal sinus rhythm with pulse",
 "Only VF"
 ],
 "explanation": "PEA is a non-shockable arrest rhythm.",
 "references": [
 "AHA BLS"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "First-degree AV block shows:",
 "correct": "Prolonged PR interval with every P conducted",
 "distractors": [
 "Dropped QRS without warning",
 "No relationship between P and QRS",
 "PR shorter than normal"
 ],
 "explanation": "All atrial impulses conduct, but delayed.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Second-degree Mobitz type I (Wenckebach) shows:",
 "correct": "Progressive PR prolongation until a dropped beat",
 "distractors": [
 "Constant PR with sudden dropped QRS",
 "No P waves",
 "Wide QRS only"
 ],
 "explanation": "Type I block is often at the AV node.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Sinus bradycardia is:",
 "correct": "Sinus rhythm with rate below 60 bpm",
 "distractors": [
 "Irregular rhythm without P waves",
 "Ventricular rate 150 with narrow QRS",
 "Asystole"
 ],
 "explanation": "Bradycardia may be benign or pathologic by context.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Sinus tachycardia is:",
 "correct": "Sinus rhythm with rate above 100 bpm",
 "distractors": [
 "Irregularly irregular rhythm",
 "Complete heart block",
 "VF"
 ],
 "explanation": "Tachycardia has many causes including fever and hypovolemia.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Premature ventricular contractions (PVCs) appear as:",
 "correct": "Early wide bizarre QRS without preceding P",
 "distractors": [
 "Early narrow QRS with identical P",
 "Flat line",
 "Only ST elevation"
 ],
 "explanation": "PVCs originate in the ventricles.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Atrial flutter often shows:",
 "correct": "Sawtooth flutter waves especially in inferior leads",
 "distractors": [
 "Regular narrow QRS with no atrial activity",
 "Chaotic baseline without pattern",
 "Long QT only"
 ],
 "explanation": "Flutter involves rapid atrial activity.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-rhythm",
 "stem": "Ventricular fibrillation appears as:",
 "correct": "Chaotic irregular waveform without discernible QRS",
 "distractors": [
 "Organized bradycardia",
 "Normal sinus rhythm",
 "Uniform P waves"
 ],
 "explanation": "VF is a shockable arrest rhythm.",
 "references": [
 "AHA BLS"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-intervals",
 "stem": "The PR interval measures:",
 "correct": "Time from start of P wave to start of QRS",
 "distractors": [
 "QRS width only",
 "T wave to next P",
 "ST segment length"
 ],
 "explanation": "PR reflects atrioventricular conduction time.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-intervals",
 "stem": "Normal PR interval is commonly:",
 "correct": "0.12 to 0.20 seconds (3 to 5 small boxes at 25 mm/s)",
 "distractors": [
 "Less than 0.06 seconds",
 "Greater than 0.40 seconds always",
 "One large box only"
 ],
 "explanation": "Prolonged PR suggests AV delay.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-intervals",
 "stem": "The QRS complex represents:",
 "correct": "Ventricular depolarization",
 "distractors": [
 "Atrial repolarization only",
 "Ventricular filling",
 "Arterial pulse pressure"
 ],
 "explanation": "Wide QRS suggests ventricular origin or bundle branch block.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-intervals",
 "stem": "Normal QRS duration is typically:",
 "correct": "Less than 0.12 seconds (3 small boxes)",
 "distractors": [
 "Greater than 0.20 seconds",
 "Exactly 0.20 seconds always",
 "Unmeasurable"
 ],
 "explanation": "Prolonged QRS indicates conduction delay in ventricles.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-intervals",
 "stem": "The QT interval spans:",
 "correct": "Start of QRS to end of T wave",
 "distractors": [
 "End of P to start of QRS",
 "P wave only",
 "ST segment only"
 ],
 "explanation": "QT reflects ventricular repolarization; correct for rate.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-intervals",
 "stem": "The ST segment is:",
 "correct": "Between end of QRS and start of T wave",
 "distractors": [
 "Same as PR interval",
 "Only in lead III",
 "Always elevated normally"
 ],
 "explanation": "ST changes may indicate ischemia or injury.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-intervals",
 "stem": "Left axis deviation may be suggested when lead I is positive and aVF is:",
 "correct": "Negative",
 "distractors": [
 "Markedly positive",
 "Isoelectric only",
 "Inverted T only"
 ],
 "explanation": "Axis is estimated from limb lead QRS deflection.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-intervals",
 "stem": "Right axis deviation may be suggested when lead I is negative and aVF is:",
 "correct": "Positive",
 "distractors": [
 "Deeply negative",
 "Flat always",
 "Absent"
 ],
 "explanation": "Consider RV strain, blocks, or normal variant in context.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-intervals",
 "stem": "A prolonged QT on EKG may increase risk of:",
 "correct": "Torsades de pointes and sudden arrhythmia",
 "distractors": [
 "Bradycardia only",
 "Normal sinus always",
 "Lead reversal only"
 ],
 "explanation": "Many drugs and electrolyte issues affect QT.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-intervals",
 "stem": "R wave progression across precordial leads normally shows:",
 "correct": "Increasing R wave amplitude from V1 toward V5/V6",
 "distractors": [
 "Decreasing R always",
 "No R waves",
 "Only S waves in all chest leads"
 ],
 "explanation": "Poor R progression may suggest anterior MI or misplacement.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-intervals",
 "stem": "The J point is:",
 "correct": "Where the QRS ends and ST segment begins",
 "distractors": [
 "Start of P wave",
 "Peak of T wave",
 "Calibration mark"
 ],
 "explanation": "J-point elevation or depression is clinically significant.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-intervals",
 "stem": "Rate calculation from EKG using 300 method divides:",
 "correct": "300 by number of large boxes between R waves",
 "distractors": [
 "600 by small boxes only",
 "Patient age",
 "ST length"
 ],
 "explanation": "Quick estimate at 25 mm/s paper speed.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Muscle tremor artifact often appears as:",
 "correct": "Irregular baseline noise during patient movement",
 "distractors": [
 "Perfectly isoelectric baseline",
 "Only ST elevation",
 "Absent QRS"
 ],
 "explanation": "Ask patient to relax; ensure warm comfortable position.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Loose or dry electrodes commonly cause:",
 "correct": "Baseline wander and intermittent signal loss",
 "distractors": [
 "Fixed ST elevation",
 "Bradycardia on monitor",
 "Widened QRS always"
 ],
 "explanation": "Check snaps, replace electrodes, and re-prep skin.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Wandering baseline may be reduced by:",
 "correct": "Ensuring good skin prep and patient stillness",
 "distractors": [
 "Increasing lotion on skin",
 "Tightening tourniquet on arm",
 "Turning off monitor"
 ],
 "explanation": "Motion and poor contact cause baseline drift.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "60-cycle (mains) interference may show as:",
 "correct": "Fine regular oscillation on baseline",
 "distractors": [
 "Huge QRS widening",
 "Absent T waves",
 "Only in V1"
 ],
 "explanation": "Check cable routing, grounding, and nearby electrical equipment.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "If the tracing shows flat line, first check:",
 "correct": "Lead connection and cable to patient and machine",
 "distractors": [
 "Patient diet",
 "Blood tube order",
 "Injection site"
 ],
 "explanation": "Technical disconnects mimic asystole on monitor.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Chest lead misplacement can:",
 "correct": "Mimic ischemia or chamber enlargement patterns",
 "distractors": [
 "Never change morphology",
 "Only affect rate",
 "Eliminate P waves always"
 ],
 "explanation": "Verify precordial positions against landmarks.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Electrode reversal between LA and RA may produce:",
 "correct": "Negative P and QRS in lead I suggesting arm lead switch",
 "distractors": [
 "Normal sinus only",
 "VF pattern",
 "Long QT only"
 ],
 "explanation": "Compare limb lead appearance to prior tracings.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Sweaty skin during EKG increases:",
 "correct": "Artifact and poor adhesion",
 "distractors": [
 "QRS voltage always",
 "PR interval",
 "Paper speed"
 ],
 "explanation": "Dry and prep skin; replace electrodes if needed.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Printing speed set to 50 mm/s without noting it will:",
 "correct": "Compress time intervals appearing shorter",
 "distractors": [
 "Have no effect",
 "Widen QRS only",
 "Change voltage gain"
 ],
 "explanation": "Always label speed and calibration.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Patient coughing during recording may cause:",
 "correct": "Motion artifact obscuring ST segments",
 "distractors": [
 "True ventricular fibrillation",
 "Fixed bradycardia",
 "Lead II only loss"
 ],
 "explanation": "Pause recording until patient is still if possible.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "Broken lead wire may produce:",
 "correct": "Intermittent loss of signal in one lead",
 "distractors": [
 "Synchronized PVCs",
 "ST elevation in all leads",
 "Automatic defibrillation"
 ],
 "explanation": "Swap cables and electrodes to isolate fault.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-artifacts",
 "stem": "After troubleshooting artifact, document:",
 "correct": "Actions taken and whether tracing is diagnostic quality",
 "distractors": [
 "Patient gossip only",
 "Unrelated vitals only",
 "Staff schedules"
 ],
 "explanation": "Quality tracings support accurate interpretation.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "The sinoatrial (SA) node is located in the:",
 "correct": "Right atrium near superior vena cava entrance",
 "distractors": [
 "Left ventricle apex",
 "Aortic arch",
 "Pulmonary vein orifice"
 ],
 "explanation": "SA node is the normal pacemaker.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "The AV node delays conduction to allow:",
 "correct": "Ventricular filling before contraction",
 "distractors": [
 "Atrial hypertrophy only",
 "Blood clotting",
 "Respiratory gas exchange"
 ],
 "explanation": "AV delay coordinates atrial and ventricular systole.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "The bundle of His conducts impulses into the:",
 "correct": "Interventricular septum toward bundle branches",
 "distractors": [
 "Left atrium only",
 "Pulmonary artery",
 "Coronary sinus"
 ],
 "explanation": "His bundle is part of AV conduction system.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "The left coronary artery primarily supplies:",
 "correct": "Left ventricle and much of interventricular septum",
 "distractors": [
 "Entire right ventricle only",
 "Pulmonary tissue only",
 "SA node exclusively"
 ],
 "explanation": "Coronary anatomy explains ischemia patterns on EKG.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "Myocardial ischemia may produce:",
 "correct": "ST-segment and T-wave changes on EKG",
 "distractors": [
 "Only bradycardia",
 "Absent P waves always",
 "Long PR only"
 ],
 "explanation": "ECG changes depend on territory and severity.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "Repolarization occurs during the:",
 "correct": "T wave phase of ventricular recovery",
 "distractors": [
 "QRS only",
 "P wave only",
 "ST segment exclusively"
 ],
 "explanation": "T wave reflects ventricular repolarization.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "Cardiac output depends on:",
 "correct": "Heart rate and stroke volume",
 "distractors": [
 "Only blood type",
 "Skin temperature",
 "Respiratory rate alone"
 ],
 "explanation": "CO = HR × SV.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "The pericardium surrounds the:",
 "correct": "Heart",
 "distractors": [
 "Lungs only",
 "Liver",
 "Brain"
 ],
 "explanation": "Pericardial disease can affect EKG.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "beginner"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "Anterior wall MI often involves leads:",
 "correct": "V1, V4",
 "distractors": [
 "II, III, aVF only",
 "V5, V6 only",
 "aVR only"
 ],
 "explanation": "Lead groups correspond to myocardial territories.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "Inferior wall ischemia is often seen in leads:",
 "correct": "II, III, and aVF",
 "distractors": [
 "V1, V3 only",
 "I and aVL only",
 "V4 only"
 ],
 "explanation": "Inferior territory reflects RCA or circumflex supply.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "Afterload is:",
 "correct": "Resistance the ventricle must overcome to eject blood",
 "distractors": [
 "Blood volume in atria",
 "Lung compliance",
 "Venous tone only"
 ],
 "explanation": "Afterload relates to arterial pressure.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "advanced"
 },
 {
 "topic": "ekg-cardiac-ap",
 "stem": "Preload is:",
 "correct": "Ventricular end-diastolic volume/stretch",
 "distractors": [
 "Afterload only",
 "Heart rate only",
 "Oxygen saturation only"
 ],
 "explanation": "Preload reflects venous return and filling.",
 "references": [
 "NHA CCMA"
 ],
 "difficulty": "intermediate"
 }
]
