# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Batch rewrites for distractor wording and length.

Each entry maps the current option text to its replacement. Apply with
``python scripts/apply_choice_rewrites.py --apply``.
"""

REWRITES: dict[str, str] = {

    # ---------------------------------------------------------------- cpr-child
    "Only after five minutes of uninterrupted compressions":
        "After five minutes of uninterrupted compressions have run",
    "Only when the patient regains a cough or gag reflex":
        "When the patient regains a cough or gag reflex",
    "15:2 because two rescuers always use the pediatric ratio":
        "15:2 because two rescuers use the pediatric ratio",
    "Compressions only with no ventilations for all team responses":
        "Compressions with no ventilations for all team responses",
    "Require supplemental oxygen only without compressions":
        "Require supplemental oxygen without compressions",
    "Gentle compressions focused only on ventilation quality":
        "Gentle compressions focused on ventilation quality",
    "15:2 because additional rescuers always change the ratio":
        "15:2 because additional rescuers change the ratio",
    "30:1 with breaths only after each minute of compressions":
        "30:1 with breaths after each minute of compressions",
    "Only during AED charging, with no limit for manual checks":
        "During AED charging, with no limit for manual checks",
    "Wait for EMS arrival before any chest compressions":
        "Wait for EMS arrival before starting chest compressions",
    "Represent effective respiration requiring oxygen mask only":
        "Represent effective respiration requiring an oxygen mask",
    "Require abdominal thrusts before any compressions":
        "Require abdominal thrusts before starting compressions",
    "Perform abdominal thrusts before any breaths or compressions":
        "Perform abdominal thrusts before starting breaths or compressions",
    "Continue shallow compressions because any chest movement helps":
        "Continue shallow compressions because chest movement is sufficient",
    "Switch to ventilations only until depth improves spontaneously":
        "Switch to ventilations until depth improves on its own",
    "Continue 30:2 because movement may be seizure activity only":
        "Continue 30:2 because movement may be seizure activity",
    "Provide rescue breaths only without compressions until EMS arrives":
        "Provide rescue breaths without compressions until EMS arrive",
    "Compressing only half the time to allow extended ventilation":
        "Compressing half the time to allow extended ventilation",
    "Stopping compressions whenever any rescuer needs to adjust equipment":
        "Stopping compressions whenever a rescuer adjusts equipment",
    "Stop compressions entirely and ventilate once per minute only":
        "Stop compressions entirely and ventilate once per minute",
    "Only after ROSC is confirmed":
        "After return of spontaneous circulation is confirmed",
    "Never switch once the first compressor establishes a rhythm":
        "Avoid switching once the first compressor sets the rhythm",
    "When any single cough is heard during compressions":
        "When a single cough is heard during compressions",
    "Only when EMS verbally orders cessation over the radio":
        "When EMS verbally orders cessation over the radio",
    "Reduce the risk of rib fractures only":
        "Reduce the risk of rib fractures during compressions",
    "Administer only passive oxygen without ventilations":
        "Administer passive oxygen without ventilations",
    "Take over ventilations only and never compress":
        "Take over ventilations and avoid compressions",
    "Any unresponsive patient regardless of breathing status":
        "An unresponsive patient regardless of breathing status",
    "Adults with known chronic respiratory disease only":
        "Adults with known chronic respiratory disease",
    "Upper-left chest and lower-right abdomen only":
        "Upper-left chest and lower-right abdomen",
    "Left nipple line over the cardiac apex only":
        "Left nipple line over the cardiac apex",
    "Children never need chest compressions once breaths are given":
        "Children do not need compressions once breaths are given",
    "Only after 10 minutes of compressions have been completed":
        "After 10 minutes of compressions have been completed",
    "Only if the child is older than 12 years":
        "If the child is older than 12 years",
    "Wait for EMS on scene before starting any compressions":
        "Wait for EMS on scene before starting compressions",
    "Give two minutes of rescue breaths before any compressions":
        "Give two minutes of rescue breaths before compressions",
    "Apical pulse only through clothing without exposing the chest":
        "Apical pulse through clothing without exposing the chest",
    "Give supplemental oxygen only without compressions":
        "Give supplemental oxygen without compressions",
    "Continuous compressions with breaths every 30 seconds only":
        "Continuous compressions with breaths every 30 seconds",
    "Breaths only after every fifth compression cycle regardless of chest rise":
        "Breaths after the fifth compression cycle without chest rise",
    "Complete five minutes of CPR before any call for help":
        "Complete five minutes of CPR before the call for help",
    "Only once at the beginning of the arrest":
        "Once at the beginning of the arrest",
    "After ROSC has been confirmed by EMS only":
        "After ROSC has been confirmed by EMS",
    "Yes; breaths are never indicated below age 18":
        "Yes; breaths are not indicated below age 18",
    "Yes; compressions alone are always preferred for children":
        "Yes; compressions alone are preferred for children",
    "Only if two rescuers are present may breaths be considered":
        "If two rescuers are present breaths may be considered",
    "One rescuer gives breaths only while the other waits without compressing":
        "One rescuer gives breaths while the other waits without compressing",
    "Compress only the upper ribs without sternal contact":
        "Compress the upper ribs without sternal contact",
    "Only when three rescuers are present":
        "When three rescuers are present",
    "Encourage coughing only because any cough means mild obstruction":
        "Encourage coughing because a cough means mild obstruction",
    "Deliver back blows only until the child loses consciousness":
        "Deliver back blows until the child loses consciousness",
    "Only neonates under one month of age":
        "Neonates under one month of age",
    "Only children who weigh less than 10 pounds":
        "Children who weigh less than 10 pounds",
    "Only deep enough to hear a click from the ribs each time":
        "Deep enough to hear a click from the ribs each time",
    "Only after EMS takes over on arrival":
        "After EMS takes over on arrival",
    "Never switch roles to avoid confusion":
        "Keep the same roles to avoid confusion",
    "Always use infant technique for anyone under 10 years old":
        "Use infant technique for a child under 10 years old",
    "Always use adult technique for anyone who can walk":
        "Use adult technique for a child who can walk",
    "Choose technique based on the rescuer's hand size only":
        "Choose technique based on the rescuer's hand size",
    "Dry the child completely and wait for normal breathing before any breaths":
        "Dry the child and wait for normal breathing before breaths",
    "Begin compressions only after 10 minutes of rescue breaths without pulse check":
        "Begin compressions after 10 minutes of rescue breaths without a pulse check",
    "Monitor only because any palpable pulse means CPR is contraindicated":
        "Monitor because a palpable pulse means CPR is contraindicated",
    "Switch to ventilations only until depth improves on its own":
        "Switch to ventilations until depth improves on its own",
    "Continue shallow compressions because any activity is sufficient":
        "Continue shallow compressions because activity is sufficient",
    "30:2 is only used for adults and never for children":
        "30:2 is used for adults and not for children",
    "Two rescuers should never give ventilations during pediatric arrest":
        "Two rescuers do not give ventilations during pediatric arrest",
    "Give breaths only when the compressor requests a break":
        "Give breaths when the compressor requests a break",
    "Resume CPR compressions because lethargy always means recurrent arrest":
        "Resume compressions because lethargy means recurrent arrest",
    "Give ventilations only because asthma means compressions are harmful":
        "Give ventilations because asthma means compressions are harmful",
    "Use compression-only CPR because asthma is a cardiac disease":
        "Use compression-only CPR because asthma is a cardiac disease",
    "Wait for bronchodilator medication before starting any CPR":
        "Wait for bronchodilator medication before starting CPR",
    "Stop CPR every five minutes to warm hands only":
        "Stop CPR every five minutes to warm hands",
    "Naloxone only without compressions until the child wakes up":
        "Naloxone without compressions until the child wakes up",
    "Rescue breaths only because opioids never cause cardiac arrest in children":
        "Rescue breaths because opioids do not cause arrest in children",

    # ---------------------------------------------------------------- cpr-infant
    "Continuous compressions without any ventilations":
        "Continuous compressions without ventilations",
    "Pinch the nose closed and blow only into the mouth as for an adult":
        "Pinch the nose closed and blow into the mouth as for an adult",
    "Radial artery at the wrist as the only acceptable site":
        "Radial artery at the wrist as the acceptable site",
    "Apical pulse through multiple layers of clothing only":
        "Apical pulse through multiple layers of clothing",
    "As normal sleep breathing that never requires CPR":
        "As normal sleep breathing that does not require CPR",
    "As a sign to give oral fluids only":
        "As a sign to give oral fluids",
    "Only after the infant reaches 12 months of age":
        "After the infant reaches 12 months of age",
    "Never for patients under 10 kg":
        "Not for patients under 10 kg",
    "Only in the hospital after physician approval":
        "In the hospital after physician approval",
    "Compressing only once every 10 seconds":
        "Compressing once every 10 seconds",
    "15 compressions followed by 2 ventilations only":
        "15 compressions followed by 2 ventilations",
    "Five compressions followed by one ventilation only":
        "Five compressions followed by one ventilation",
    "Infants never need chest compressions under any circumstance":
        "Infants need chest compressions when the pulse is absent",
    "Ventilations are required only after hospital admission":
        "Ventilations are required before hospital admission",
    "Compression-only CPR is preferred for all infants at home":
        "Compression-only CPR is preferred for infants at home",
    "Heel of one hand using adult depth on the upper sternum only":
        "Heel of one hand using adult depth on the upper sternum",
    "Any head movement regardless of trauma status":
        "Head movement regardless of trauma status",
    "Finger sweeps into the mouth before any back slaps":
        "Finger sweeps into the mouth before back slaps",
    "Rescue breaths only while the infant remains conscious":
        "Rescue breaths while the infant remains conscious",
    "Infants always overheat during CPR and need cooling with ice":
        "Infants overheat during CPR and need cooling with ice",
    "Never leave the infant to activate EMS under any circumstance":
        "Leave the infant to activate EMS without delay",
    "Place both pads on the infant's back only":
        "Place both pads on the infant's back",
    "Only after ROSC has occurred":
        "After return of spontaneous circulation has occurred",
    "Never switch to avoid breaking rhythm":
        "Avoid switching to keep the rhythm unbroken",
    "Never look in the mouth during infant CPR":
        "Do not look in the mouth during infant CPR",
    "Only after 30 minutes of compressions":
        "After 30 minutes of compressions",
    "Yes; infants never benefit from rescue breaths":
        "Yes; infants do not benefit from rescue breaths",
    "Only health care providers may give infant ventilations":
        "Health care providers may give infant ventilations",
    "Lay rescuers should never pause compressions to check a pulse":
        "Lay rescuers pause compressions briefly to check a pulse",
    "Surface firmness only matters for adult victims":
        "Surface firmness matters for adult victims",
    "Infants should always be compressed while held upright in arms only":
        "Infants are compressed while held upright in the arms",
    "Ventilations occur only after ROSC":
        "Ventilations occur after ROSC",
    "Remove pads after the first shock and never resume CPR":
        "Remove pads after the first shock and do not resume CPR",
    "Give rescue breaths only without compressions":
        "Give rescue breaths without compressions",
    "Resume full CPR compressions because lethargy always means arrest":
        "Resume compressions because lethargy means recurrent arrest",
    "Observe only because any palpable pulse excludes CPR":
        "Observe because a palpable pulse excludes CPR",
    "Wait for parents to arrive before any intervention":
        "Wait for parents to arrive before intervening",
    "Standing across the room while directing breaths only":
        "Standing across the room while directing breaths",
    "Dry the infant for 10 minutes before any breaths or compressions":
        "Dry the infant for 10 minutes before breaths or compressions",
    "Defer CPR until the infant is wrapped in heated blankets only":
        "Defer CPR until the infant is wrapped in heated blankets",
    "Place both pads on the right arm only":
        "Place both pads on the right arm",
    "Stop compressions and ventilate only until depth improves":
        "Stop compressions and ventilate until depth improves",
    "Encourage coughing because cyanosis always means mild obstruction":
        "Encourage coughing because cyanosis means mild obstruction",
    "Ventilate only without compressions regardless of pulse status":
        "Ventilate without compressions regardless of pulse status",

    # ------------------------------------------------- ccma, ekg, phleb, skills
    "Is exempt from any quality standards":
        "Is exempt from most quality standards",
    "Any harmless skin bacterium":
        "A harmless skin bacterium",
    "Refusing any accommodation":
        "Refusing an accommodation",
    "Any passerby in the hall":
        "A passerby in the hall",
    "Random bilingual visitors":
        "Untrained bilingual visitors",
    "Random diagnosis codes":
        "Incorrect diagnosis codes",
    "Avoiding any follow-up":
        "Avoiding follow-up",
    "Stand 20 feet from any chart without protocol":
        "Stand 20 feet from the chart without a protocol",
    "Tap water from any sink without asepsis":
        "Tap water from a sink without asepsis",
    "Eliminates need for any consent ever":
        "Eliminates the need for consent",
    "Random care based on payment":
        "Care assigned by payment status",
    "Not under any state law":
        "Not under state law",
    "Forced treatment for any disagreement":
        "Forced treatment after a disagreement",
    "Not under any circumstance":
        "Not under any circumstance of consent",
    "Is encouraged at any volume":
        "Is encouraged at every volume",
    "Fax to any number without checking":
        "Fax to a number without checking it",
    "Includes full diagnosis for any caller":
        "Includes a full diagnosis for a caller",
    "Full diagnosis to any visitor without consent":
        "A full diagnosis to a visitor without consent",
    "Random online forums":
        "Unverified online forums",
    "Instead of any cleaning":
        "Instead of cleaning",
    "Continue forever after any cold":
        "Continue indefinitely after a cold",
    "Random choice":
        "An arbitrary choice",
    "Be random":
        "Be arbitrary",
    "Gloves first before any other step":
        "Gloves first before the other steps",
    "Random selection":
        "An arbitrary selection",
    "Use any vial without reading label":
        "Use a vial without reading the label",
    "Any intradermal injection":
        "An intradermal injection",
    "It allows any adult IM volume in the deltoid muscle":
        "It allows a larger adult IM volume in the deltoid muscle",
    "Use any open vial first to limit waste without chart review":
        "Use an open vial first to limit waste without chart review",
    "Up to 5 mL in the deltoid for any medication ordered that clinic day":
        "Up to 5 mL in the deltoid for a medication ordered that clinic day",
    "Needles cannot penetrate inflamed skin at any angle or depth":
        "Inflamed skin is unsuitable for injection at a shallow depth",
    "At least two hours of strict bed rest before any cuff inflation":
        "At least two hours of strict bed rest before cuff inflation",
    "Inflate the cuff to maximum pressure before any reading is taken at each clinic visit":
        "Inflate the cuff to maximum pressure before each clinic reading",
    "It indicates mandatory hospital admission before any further vitals are obtained":
        "It indicates hospital admission before further vitals are obtained",
    "Tell them that any spoon from the kitchen drawer holds exactly 5 mL":
        "Tell them that a kitchen spoon holds exactly 5 mL",
    "Provide a single random spot check of urine color at one void":
        "Provide a single spot check of urine color at one void",
    "Pause the infusion and use any visible hand vein on the same arm":
        "Pause the infusion and use a visible hand vein on the same arm",
    "The patient should fast for three days before any blood sample is taken":
        "The patient should fast for three days before a blood sample is taken",
    "Before staff ask any allergy screening questions at this clinic visit":
        "Before staff ask the allergy screening questions at this visit",
    "Complete all billing entries before any brief safety assessment at triage":
        "Complete all billing entries before a brief safety assessment at triage",
    "Select a diagnosis code at random instead of the patient's stated concern":
        "Select a diagnosis code at random instead of the stated concern",
    "Dietary preferences and caffeine intake recorded without any family disease history":
        "Dietary preferences and caffeine intake recorded without family history",
    "Any contact at all with a patient who has a confirmed bloodborne pathogen infection":
        "Contact with a patient who has a confirmed bloodborne pathogen infection",
    "Any task in a clinical setting that involves handling patient specimens or blood products":
        "A task in a clinical setting that involves handling specimens or blood products",
    "Any injury sustained in the workplace, including slips, falls, strains, and sprains":
        "An injury sustained in the workplace, such as a slip, fall, or strain",
    "After attending training, without any written documentation of the refusal":
        "After attending training, without written documentation of the refusal",
    "Waived complexity tests run on any analyzer the clinic owns":
        "Waived complexity tests run on an analyzer the clinic owns",
    "Post results to the patient portal without any provider sign-off":
        "Post results to the patient portal without provider sign-off",
    "A distraction video during the procedure without any prior explanation":
        "A distraction video during the procedure without prior explanation",
    "Food aversions to certain vegetables without any other symptoms":
        "Food aversions to certain vegetables without other symptoms",
    "Wait for EMS to arrive before attempting any airway clearance maneuvers":
        "Wait for EMS to arrive before attempting airway clearance maneuvers",
    "Wait for a triage officer from EMS before approaching any patient":
        "Wait for a triage officer from EMS before approaching a patient",
    "Any visible sternal movement, with no minimum depth":
        "Visible sternal movement, with no minimum depth",
    "Blood glucose with a fingerstick before any chest contact":
        "Blood glucose with a fingerstick before chest contact",
    "Refuse to perform any EKG on patients with amputations":
        "Refuse to perform an EKG on a patient with amputations",
    "It removes the need for any skin preparation":
        "It removes the need for skin preparation",
    "V1 recorded alone without any other chest leads":
        "V1 recorded alone without the other chest leads",
    "Muscle tissue prevents any voltage from being detected":
        "Muscle tissue prevents a voltage from being detected",
    "Diaphoresis prevents any electrical signal from being recorded":
        "Diaphoresis prevents an electrical signal from being recorded",
    "Random fine fibrillatory waves without organized P waves":
        "Fine, disorganized fibrillatory waves without organized P waves",
    "A flat baseline without any organized atrial activity":
        "A flat baseline without organized atrial activity",
    "ST segment elevation without any QRS change":
        "ST segment elevation without a QRS change",
    "A flat line without any ventricular activity":
        "A flat line without ventricular activity",
    "No R waves in any of the chest leads":
        "No R waves in the chest leads",
    "Gold serum separator (SST) before any citrate tube":
        "Gold serum separator (SST) before the citrate tube",
    "Lavender EDTA before any other tube including cultures":
        "Lavender EDTA before the other tubes including cultures",
    "Before blood cultures whenever any coagulation test is ordered":
        "Before blood cultures whenever a coagulation test is ordered",
    "First to stabilize glucose before any other additive":
        "First to stabilize glucose before the other additives",
    "Stop at any visible blood because partial fills are acceptable for all tests":
        "Stop at visible blood because partial fills work for all tests",
    "Because citrate cannot be the first tube under any circumstance":
        "Because citrate cannot be the first tube under any condition",
    "Any transfer order because syringes neutralize additives":
        "Any transfer order because syringes neutralize the additives",
    "Random order because capillary specimens are exempt from every CLSI rule":
        "An arbitrary order because capillary specimens skip CLSI rules",
    "Any test can use green tubes interchangeably with serum":
        "Green tubes can substitute for serum in most assays",
    "Any lavender tube stored at room temperature for 24 hours":
        "A lavender tube stored at room temperature for 24 hours",
    "Plain red-top serum collected without any dilution step":
        "Plain red-top serum collected without a dilution step",
    "Any green tube because heparin plasma is universal for drugs":
        "A green tube because heparin plasma suits most drugs",
    "No action because intact skin does not require any follow-up":
        "No action because intact skin does not require follow-up",
    "Random because bevel direction does not affect entry":
        "An arbitrary choice because bevel direction does not affect entry",
    "Any test ordered can be collected capillary without a manual check":
        "An ordered test can be collected capillary without a manual check",
    "Random gauge assignment to train on every size each visit":
        "An arbitrary gauge assignment to train on each size every visit",
    "Centrifuging before any inversion occurs":
        "Centrifuging before inversion occurs",
    "Verbal results without any tube label":
        "Verbal results without a tube label",
    "Any serum separator left upright for several hours":
        "A serum separator left upright for several hours",
    "Eliminate the need for any centrifuge step":
        "Eliminate the need for a centrifuge step",
    "Random numbers instead of patient identifiers":
        "Arbitrary numbers instead of patient identifiers",
    "Arterial spasm without any bruising":
        "Arterial spasm without bruising",
    "Hemolysis that occurs without any effect of stasis":
        "Hemolysis that occurs without an effect of stasis",
    "Giving stimulants without any assessment or observation":
        "Giving stimulants without assessment or observation",
    "Having no effect on any liver chemistry analyte":
        "Having no effect on a liver chemistry analyte",
    "Completing all draws before any documentation":
        "Completing all draws before documentation",
    "Use physical restraint without any provider order":
        "Use physical restraint without a provider order",
    "Hold the child without any collector instruction":
        "Hold the child without collector instruction",
    "Removal of the need for any gloves":
        "Removal of the need for gloves",
    "Random tube color selection to save time":
        "Tube color chosen by convenience to save time",
    "Identical drug regimens without any risk review":
        "Identical drug regimens without a risk review",
    "Unregulated and exempt from any quality checks":
        "Unregulated and exempt from quality checks",
    "Fail to change any laboratory analyte":
        "Fail to change a laboratory analyte",
    "Use any brand of strips in one meter without verification":
        "Use a strip brand in one meter without verification",
    "Patient identity before the test without any chemistry check":
        "Patient identity before the test without a chemistry check",
    "Before the patient drinks any glucose":
        "Before the patient drinks the glucose",
    "As proof of diabetes without any context":
        "As proof of diabetes without clinical context",
    "Any finger of a newborn without an institutional protocol":
        "A finger of a newborn without an institutional protocol",
    "Any soft drink the patient prefers":
        "A soft drink the patient prefers",
    "Having no effect on any POC device":
        "Having no effect on a POC device",
    "Any use of gloves by operators":
        "Use of gloves by operators",
    "Random numbers without units":
        "Arbitrary numbers without units",
    "Fail to alter any analyte result in the collected sample":
        "Fail to alter an analyte result in the collected sample",
    "Allow use of any manufacturer's strips":
        "Allow use of another manufacturer's strips",
    "Document a random normal value on the glucose worksheet":
        "Document an arbitrary normal value on the glucose worksheet",
    "Diabetes in pregnancy that always resolves with no later risk of type 2":
        "Diabetes in pregnancy that resolves with no later risk of type 2",
    "Patients with prediabetes who have not started any medication":
        "Patients with prediabetes who have not started medication",

    # --------------------------------------------------- final giveaway cleanups
    "Not under any circumstance of consent":
        "Not a substitute for parental consent in every case",
    "Select a diagnosis code at random instead of the stated concern":
        "Select a diagnosis code by assumption instead of the stated concern",
    "Because citrate cannot be the first tube under any condition":
        "Because citrate cannot be the first tube under every condition",
    "Any transfer order because syringes neutralize the additives":
        "A transfer order because syringes neutralize the additives",

    # ------------------------------------- key length balance for the skill bank
    "Before staff ask the allergy screening questions at this visit":
        "Before staff ask the allergy screening questions during this clinic visit",
    "Skin, eye, mucous membrane, and parenteral routes with reasonably anticipated contact":
        "Skin, eye, mucous membrane, and parenteral routes with anticipated contact",

    # ------------------------------------------------ long distractors trimmed
    "To eliminate audible Korotkoff sounds during cuff deflation at the antecubital fossa":
        "To eliminate Korotkoff sounds during cuff deflation at the antecubital fossa",
    "To raise the recorded diastolic value for chart trending during serial measurements":
        "To raise the recorded diastolic value for trending across visits",
    "Poor sublingual seal with recent cold or hot drink intake before oral measurement":
        "Poor sublingual seal with a recent cold or hot drink before the reading",
    "Temporal artery scan over sweat or hair on the forehead during infrared screening":
        "Temporal artery scan over sweat or hair on the forehead",
    "Measure both arms simultaneously without a position change between the two readings":
        "Measure both arms at once without a position change between readings",
    "Record one standing pressure without a baseline seated or supine value before standing":
        "Record a standing pressure with no baseline seated value first",
    "At the second intercostal space along the right sternal border at the base of the neck":
        "At the second intercostal space along the right sternal border",
    "Over the carotid artery at the anterior neck midline with firm palpation pressure":
        "Over the carotid artery at the anterior neck midline",
    "Respiratory rate counted while the patient completes distraction tasks during the exam":
        "Respiratory rate counted while the patient completes distraction tasks",
    "Calibration converts height measures into blood pressure values on the vital sign flowsheet":
        "Calibration converts height measures into blood pressure values",
    "Calibration replaces documenting whether the patient ate breakfast before the weight entry":
        "Calibration replaces documenting whether the patient ate breakfast",
    "Patient sits on the exam table while staff estimates height visually without a stadiometer":
        "Patient sits on the exam table while staff estimates the height visually",
    "Patient stands on tiptoes against the stadiometer backboard to maximize recorded height":
        "Patient stands on tiptoes against the stadiometer backboard",
    "Patient lies supine while a tape measure follows the mattress curve along the spine":
        "Patient lies supine while a tape measure follows the mattress curve",
    "Weight in kilograms multiplied by height in meters without squaring the height term":
        "Weight in kilograms multiplied by height in meters without squaring",
    "They cannot display systolic and diastolic numbers on the device screen during use":
        "They cannot display systolic and diastolic numbers on the screen",
    "They eliminate the need to select cuff size based on measured upper arm circumference":
        "They eliminate the need to select a cuff size from arm circumference",
    "Recording the measurement site when documenting temperature in the medical record":
        "Recording the measurement site when documenting temperature",
    "It requires immediate defibrillation in an outpatient setting without further assessment":
        "It requires immediate defibrillation in an outpatient setting",
    "When the patient prefers not to hear the numbers at the bedside during vital sign collection":
        "When the patient prefers not to hear the numbers at the bedside",
    "After all scheduled appointments finish regardless of severity, symptoms, or trending change":
        "After the scheduled appointments finish regardless of severity",
    "When the reading matches yesterday's value without new symptoms, orders, or policy triggers":
        "When the reading matches yesterday with no new symptoms or orders",
    "Eliminate terminal cleaning of exam rooms and high-touch surfaces between patients":
        "Eliminate terminal cleaning of exam rooms between patients",
    "Gloves first, then gown draped over gloved hands without securing ties at the back":
        "Gloves first, then the gown draped over the gloved hands",
    "Permission to reuse needles and syringes between patients in the same procedure bay":
        "Permission to reuse needles and syringes between patients",
    "Removal of hand hygiene requirements whenever a surgical mask is worn during patient care":
        "Removal of hand hygiene requirements whenever a surgical mask is worn",
    "Routine room cleaning without EPA-registered disinfectants on high-touch surfaces after visits":
        "Routine room cleaning without EPA-registered disinfectants",
    "Patients who completed antibiotics three weeks ago without relapse or active symptoms":
        "Patients who completed antibiotics three weeks ago without symptoms",
    "Sterilization of every countertop with autoclave packs each morning before clinic opens":
        "Sterilization of every countertop with autoclave packs each morning",
    "Complete elimination of all bacteria on patient skin without cleansing before procedures":
        "Complete elimination of all bacteria on patient skin",
    "Use of sterile surgical fields for every blood pressure measurement in the exam room":
        "Sterile surgical fields for every blood pressure measurement",
    "Turn your back to the field while reaching backward for instruments behind the drape":
        "Turn your back to the field while reaching for instruments behind it",
    "Eliminate the need for PPE during blood specimen collection from the antecubital vein":
        "Eliminate the need for PPE during antecubital blood collection",
    "Labeling as a furniture polish safe for wood grain shine without healthcare pathogen claims":
        "Labeling as a furniture polish safe for wood grain shine",
    "Labeling as a hand lotion with fragrance for staff comfort without disinfectant contact time":
        "Labeling as a hand lotion with fragrance for staff comfort",
    "Labeling as a window cleaner without tuberculocidal, virucidal, or hospital disinfectant claims":
        "Labeling as a window cleaner without a hospital disinfectant claim",
    "One multi-dose vial shared between exam rooms if the rubber diaphragm looks intact":
        "One multi-dose vial shared between exam rooms if it looks intact",
    "Allow shared patient equipment without cleaning between uses in the same clinic day":
        "Allow shared patient equipment without cleaning between uses",
    "Permit food trays from the cafeteria to sit on the bedside table unwashed overnight":
        "Permit food trays to sit on the bedside table unwashed overnight",
    "Replace hand hygiene with a single pair of gloves for the whole shift on the unit":
        "Replace hand hygiene with one pair of gloves for the whole shift",
    "Mop with plain water and leave the area open to air dry overnight without barriers":
        "Mop with plain water and leave the area to air dry overnight",
    "Seating in the general pediatric waiting area during active rash onset and coughing":
        "Seating in the general pediatric waiting area during rash onset",
    "Rooming with an immunocompromised patient in the same exam room to conserve space":
        "Rooming with an immunocompromised patient in the same exam room",
    "Discharge home by crowded public transit while vesicular lesions are still open and contagious":
        "Discharge home by public transit while the lesions remain open",
    "They improve alcohol rub penetration under stone settings and long nail extensions":
        "They improve alcohol rub penetration under stone settings",
    "They replace the need for gloves during phlebotomy and other blood exposure tasks":
        "They replace the need for gloves during phlebotomy tasks",
    "They indicate senior staff who may bypass required hand hygiene before every patient contact":
        "They indicate senior staff who may bypass required hand hygiene",
    "Store blood-soiled linen in open hampers at the nurse station for aesthetic display":
        "Store blood-soiled linen in open hampers at the nurse station",
    "Continue with one gloved hand because the other hand stayed clean during the task":
        "Continue with one gloved hand because the other stayed clean",
    "Dip the torn glove in alcohol to sterilize the defect before continuing the procedure":
        "Dip the torn glove in alcohol before continuing the procedure",
    "Enter in street clothes and don gloves after touching the bed rails and door handle":
        "Enter in street clothes and glove after touching the bed rails",
    "It is performed once per month regardless of the scheduled sterile procedure list":
        "It is performed once per month regardless of the procedure list",
    "When blood collection tubes are stored next to sandwiches in the same storage bin":
        "When blood tubes are stored next to sandwiches in the same bin",
    "When the refrigerator has no thermometer because the interior feels cold to touch":
        "When the refrigerator has no thermometer to check the temperature",
    "Group all respiratory patients together at the front desk for faster triage and registration":
        "Group all respiratory patients together at the front desk for triage",
    "Ask immunocompromised patients to remove masks briefly for photo identification at check-in":
        "Ask immunocompromised patients to remove masks for identification",
    "Close the entire clinic without notifying the provider on call or arranging patient follow-up":
        "Close the clinic without notifying the provider on call",
    "Enter without PPE to ask the patient about travel history before calling the charge nurse":
        "Enter without PPE to ask about travel history before calling the nurse",
    "Use Standard Precautions alone for every rash, cough, or draining wound while awaiting orders":
        "Use Standard Precautions alone for every rash or draining wound",
    "Wait in the hallway until the patient leaves without notifying the charge nurse or provider":
        "Wait in the hallway until the patient leaves without notifying anyone",
    "Clot formation in an EDTA tube intended for hematology cell counts on the analyzer":
        "Clot formation in an EDTA tube intended for hematology cell counts",
    "Label smearing on the tube making the patient name hard to read at the laboratory bench":
        "Label smearing that makes the patient name hard to read",
    "Have the patient pump the fist vigorously for two minutes before needle insertion":
        "Have the patient pump the fist for two minutes before the stick",
    "Nursing unit room color code without patient name or medical record number on the tube":
        "Nursing unit room color code without the patient name or MRN",
    "Ordering provider home address to route questions about pending laboratory results":
        "Ordering provider home address to route questions about results",
    "Insurance group number in place of medical record number and collection date-time":
        "Insurance group number in place of the record number and date",
    "Drawn whenever the phlebotomist returns from break without timing the ordered interval":
        "Drawn whenever the phlebotomist returns from break without timing it",
    "Combined with the fasting sample in one tube to save venipunctures on the patient":
        "Combined with the fasting sample in one tube to save a stick",
    "Left at room temperature for six hours before centrifugation and courier transport":
        "Left at room temperature for six hours before courier transport",
    "After boiling the sample to sterilize it before courier transport to the laboratory":
        "After boiling the sample before courier transport to the laboratory",
    "One large watery sample filling the entire occult blood card without separate smears":
        "One watery sample filling the whole card without separate smears",
    "Leave the used needle on the bed for environmental services staff to collect later":
        "Leave the used needle on the bed for staff to collect later",
    "Phlebotomy station phone extensions for the nursing unit assigned that collection day":
        "Phlebotomy station phone extensions for the nursing unit",
    "Patient appointment reminder scripts for front-desk scheduling staff to read aloud":
        "Patient appointment reminder scripts for front-desk staff to read",
    "Waiting room chair inventory colors for facilities maintenance department weekly tracking":
        "Waiting room chair inventory colors for the maintenance department",
    "Wipe wet alcohol forward into the intended venipuncture puncture site before insertion":
        "Wipe wet alcohol forward into the intended puncture site",
    "Potassium leaks out of tubes that are labeled with the wrong color cap on the tube":
        "Potassium leaks out of a tube labeled with the wrong color cap",
    "Lists grocery items the patient ate before a routine fasting cholesterol blood test":
        "Lists what the patient ate before a routine fasting lipid panel",
    "Replaces patient identifiers on standard chemistry tubes processed in the laboratory":
        "Replaces patient identifiers on standard chemistry tubes",
    "Whenever a chemistry panel includes liver enzymes listed on the laboratory requisition":
        "Whenever a chemistry panel includes liver enzymes on the requisition",
    "Whenever the patient drank water in the waiting room before the venipuncture draw":
        "Whenever the patient drank water before the venipuncture draw",
    "The specimen can remain at the bedside unattended until the end of the nursing shift":
        "The specimen can stay at the bedside until the end of the shift",
    "Fasting raises glucose because the body stops insulin production entirely after sleep":
        "Fasting raises glucose because the body stops producing insulin",
    "To warm the blood sample to body temperature for immediate oral patient drinking trials":
        "To warm the blood sample to body temperature for oral trials",
    "To remove hemoglobin from plasma by shaking red cells out of liquid suspension phase":
        "To remove hemoglobin by shaking red cells out of suspension",
    "To let air bubbles rise so the additive tube can be underfilled safely without redraw":
        "To let air bubbles rise so the tube can be underfilled safely",
    "Whether the patient prefers generic medications over brand-name products at the pharmacy":
        "Whether the patient prefers generic over brand-name products",
    "Whether mild heartburn after spicy meals has occurred intermittently for several years":
        "Whether mild heartburn after spicy meals has lasted for years",
    "Blood along with every other body fluid a patient produces, including sweat and tears":
        "Blood along with every body fluid a patient produces, including sweat",
    "Blood that the laboratory has confirmed as carrying a bloodborne pathogen infection":
        "Blood confirmed by the laboratory as carrying a bloodborne pathogen",
    "Urine, feces, and sputum whenever they are collected anywhere inside a clinical building":
        "Urine, feces, and sputum whenever they are collected in a clinic",
    "Charge employees the cost of the series when they work fewer than twenty hours weekly":
        "Charge employees the cost of the series when they work part time",
    "Require vaccination for every person who enters the building, including visitors and vendors":
        "Require vaccination for every person who enters the building",
    "Exposure determination, annual training dates, and a supply budget for protective equipment":
        "Exposure determination, training dates, and a budget for protective gear",
    "Engineering controls, work practice controls, and a list of employees who declined vaccination":
        "Engineering controls, work practice controls, and a list of decliners",
    "Post-exposure follow-up steps, incident reporting forms, and the annual training calendar":
        "Post-exposure follow-up steps, reporting forms, and the training calendar",
    "Reduce the hazard by adding protective equipment that shields the hands during device handling":
        "Reduce the hazard by adding equipment that shields the hands",
    "Gloves alone, because mucous membrane exposure is not addressed by PPE rules for staff":
        "Gloves alone, because mucous membrane exposure is not addressed by PPE",
    "When the employee works part time and has fewer than twenty scheduled hours weekly":
        "When the employee works part time with fewer than twenty hours",
    "When the clinic is privately owned rather than part of a hospital or larger health system":
        "When the clinic is privately owned rather than part of a hospital",
    "Squeeze the wound to stop bleeding, then return to patient care without reporting":
        "Squeeze the wound to stop bleeding, then return to patient care",
    "Devices and equipment that physically block contact with blood or other body fluids":
        "Devices and equipment that physically block contact with blood",
    "Employee baseline labs, follow-up testing schedule, and the employee's billing account number":
        "Baseline labs, a follow-up testing schedule, and the billing account number",
    "Source patient status when available, the employee's insurance plan, and the billing code used":
        "Source patient status, the employee's insurance plan, and the billing code",
    "The employee's baseline labs, the incident narrative, and the department where the stick occurred":
        "Baseline labs, the incident narrative, and the department of the stick",
    "To confirm that the employee may safely reuse the same needle between different patients":
        "To confirm the employee may safely reuse a needle between patients",
    "To document the employee's status so that gloves may be skipped on later blood draws":
        "To document the status so gloves may be skipped on later blood draws",
    "To show that annual bloodborne pathogen training is no longer required for that task":
        "To show that annual bloodborne pathogen training is no longer required",
    "Absorbing the spill, then disinfecting the area with a germicide and no protective equipment":
        "Absorbing the spill, then disinfecting the area with a germicide",
    "Cleaning the floor with a disinfectant first, then mopping up the remaining blood":
        "Cleaning the floor with a disinfectant first, then mopping up the blood",
    "When the task involves a specimen that might contain blood, even when it is sealed":
        "When the task involves a specimen that might contain blood",
    "When the employee has completed bloodborne pathogen training for the patient unit":
        "When the employee has completed training for the patient unit",
    "Evaluate the request, document the decision, and keep the current devices in service":
        "Evaluate the request, document it, and keep the current devices",
    "Wait for the annual injury count to reach a threshold before reviewing device options":
        "Wait for the annual injury count to reach a threshold first",
    "Announcing each instrument before passing it so the receiving clinician is prepared":
        "Announcing each instrument so the receiving clinician is prepared",
    "The employee's exposure details are shared with the whole unit for safety awareness":
        "The exposure details are shared with the whole unit for safety",
    "The source patient's identity is posted with the incident report in the staff break room":
        "The source patient's identity is posted in the staff break room",
    "Confidentiality ends once the employee returns to work and has been medically cleared":
        "Confidentiality ends once the employee returns to work",
    "The medical record number on the chart header, read before the medication is prepared":
        "The medical record number on the chart header read before preparation",
    "After the dose is given and the medication is entered on the administration record":
        "After the dose is given and entered on the administration record",
    "At the annual wellness visit, even when no new prescriptions are ordered that day":
        "At the annual wellness visit when no prescriptions are ordered",
    "A printed record of the product that was dispensed and the patient it was given to":
        "A printed record of the product dispensed and the patient",
    "A leading zero confirms the prescriber intends a weight-based dose for the patient":
        "A leading zero confirms the prescriber intends a weight-based dose",
    "A leading zero indicates that the drug strength was verified against a pharmacy record":
        "A leading zero indicates the strength was checked against a record",
    "Document the reason for the override and close the drawer at the end of the month":
        "Document the override reason and close the drawer at month end",
    "Reconcile the inventory after the override and leave the reason to the supervisor":
        "Reconcile the inventory later and leave the reason to the supervisor",
    "Before each patient result, with every new strip lot, and after the meter is dropped":
        "Before each patient result, with each new strip lot, and after a drop",
    "Hand hygiene, a reusable lancing device, and milking the finger to produce the drop":
        "Hand hygiene, a reusable lancing device, and milking the finger",
    "An age-appropriate explanation, permission to ask questions, and a promise of no pain":
        "An age-appropriate explanation, permission to ask questions, and no pain",
    "Room the patient privately, explain the confidentiality limits, and delay the testing":
        "Room the patient privately, explain the limits, and delay the testing",
    "Ask the guardian to sign the laboratory requisition before the specimen is collected":
        "Ask the guardian to sign the requisition before the specimen",
    "Call the guardian on the phone and arrange for the guardian to speak with the provider":
        "Call the guardian and arrange for the guardian to speak with the provider",
    "Chart the refusal and counseling, provide the information sheet, and end the visit without a return date":
        "Chart the refusal and counseling, give the information sheet, and end the visit",
    "Effectiveness, common side effects, and a guarantee that condoms prevent every STI":
        "Effectiveness, common side effects, and a guarantee condoms prevent STIs",
    "Medication review, home hazard changes, vision correction, and scheduled bed rest":
        "Medication review, home hazard changes, vision correction, and bed rest",
    "Medication review, home hazard changes, vision correction, and a low calcium diet":
        "Medication review, hazard changes, vision correction, and a calcium supplement",
    "A sucrose pacifier or breastfeeding, with the child counting aloud during the injection":
        "A sucrose pacifier or breastfeeding, with the child counting aloud",
    "Lie the patient flat, tilt the head back, and pinch the soft nose for ten to fifteen minutes":
        "Lie the patient flat, tilt the head back, and pinch the soft nose",
    "Give fifteen grams of fast-acting carbohydrate and recheck the glucose after one hour":
        "Give fifteen grams of fast-acting carbohydrate and recheck in an hour",
    "Onset time, interventions given, insurance status, and the most recent vital signs":
        "Onset time, interventions given, insurance status, and vital signs",
    "Give milk or water to dilute the chemical and then wait for the ambulance to arrive":
        "Give milk or water to dilute it and wait for the ambulance",
    "Abdominal compression displaces the diaphragm equally to direct cardiac compression":
        "Abdominal compression displaces the diaphragm to compress the heart",
    "A fixed point on the left lateral chest at the mid-axillary line for every body size":
        "A fixed point on the left lateral chest for every body size",
    "Compress the infant's back while ventilating from the side without sternal compressions":
        "Compress the infant's back while ventilating from the side",
    "Restricting AED training to hospital staff and removing devices from public areas":
        "Restricting AED training to hospital staff and removing public devices",
    "Add culture bottles to the same needle if it is still in the vein without restarting sterile technique":
        "Add culture bottles to the same needle while it is still in the vein",
    "Correct order of draw automatically prevents hemolysis regardless of tourniquet time":
        "Correct order of draw prevents hemolysis regardless of tourniquet time",
    "The wrong anticoagulant was used, since heparin raises potassium without hemolysis":
        "The wrong anticoagulant was used, since heparin raises potassium",
    "The laboratory result should be discarded because capillary samples are less accurate":
        "The laboratory result should be discarded because capillary is less accurate",
    "The two results should be averaged together before they are reported to the provider":
        "The two results should be averaged before they reach the provider",
    "Dietary change alone, with no medication needed once the glucose values normalize":
        "Dietary change alone, with no medication once the glucose normalizes",
    "Within the 100 to 125 mg/dL prediabetes range, so testing is repeated in one year":
        "Within the 100 to 125 mg/dL prediabetes range, so testing repeats yearly",
    "A body mass index under 25, a family history of diabetes, and weekly aerobic exercise":
        "A body mass index under 25, a family history, and weekly aerobic exercise",
    "A body mass index over 30, a family history of diabetes, and regular aerobic exercise":
        "A body mass index over 30, a family history, and regular aerobic exercise",
    "The drug slows the breakdown of insulin in the bloodstream, so its effect lasts longer":
        "The drug slows the breakdown of insulin so its effect lasts longer",
    "Whether the patient has eaten, the price of the drug, and the pharmacy pickup time":
        "Whether the patient has eaten, the price of the drug, and the pickup time",
    "Neuropathy reduces sensation, while poor circulation increases the pulses in the foot":
        "Neuropathy reduces sensation, while poor circulation increases pulses",
    "Neuropathy changes the color of the foot, while poor circulation changes vibration sense":
        "Neuropathy changes foot color, while poor circulation changes vibration",
    "Dose changes fall to the medical assistant whenever the glucose log shows a trend":
        "Dose changes fall to the medical assistant when the log shows a trend",
    "Dose changes are made by the medical assistant after a phone call with the patient":
        "Dose changes are made by the medical assistant after a phone call",
    "Labeling as a window cleaner without tuberculocidal, virucidal, or hospital disinfectant data":
        "Labeling as a window cleaner without a hospital disinfectant claim",
    "Add culture bottles to the same needle if it is still in the vein without restarting sterile prep":
        "Add culture bottles to the same needle while it is still in the vein",

    # ------------------------------- key and sibling length balance (skill bank)
    "Compare supine or sitting pressure with standing pressure after a position change":
        "Compare supine or sitting pressure with standing pressure after a change",
    "Inflate the cuff to maximum pressure before each clinic reading":
        "Inflate the cuff to maximum pressure before each clinic blood pressure reading",
    "Patient stands straight against a stadiometer with heels together and head level":
        "Patient stands straight against a stadiometer with heels together",
    "It may be a normal training effect if rhythm is regular and perfusion is good":
        "It may be a normal training effect if the rhythm and perfusion are good",
    "When values fall outside expected limits or match protocol-defined critical thresholds":
        "When values fall outside expected limits or critical thresholds",
    "After the scheduled appointments finish regardless of severity":
        "After all the scheduled appointments finish regardless of severity",
    "Added measures for contact, droplet, or airborne spread when known or suspected":
        "Added measures for contact, droplet, or airborne spread when suspected",
    "Removal of hand hygiene requirements whenever a surgical mask is worn":
        "Removal of the hand hygiene requirement whenever a surgical mask is worn",
    "Patients with intact skin and no draining wounds during routine clinic visits":
        "Patients with intact skin and no draining wounds during a routine clinic visit",
    "Techniques that reduce microbes and protect clean sites and supplies from contamination":
        "Techniques that reduce microbes and protect clean sites from contamination",
    "Sterilization of every countertop with autoclave packs each morning":
        "Sterilization of every countertop with autoclave packs each morning before clinic",
    "Hospital disinfectant labeling effective against relevant pathogens when used as directed":
        "Hospital disinfectant labeling effective against relevant pathogens",
    "Labeling as a window cleaner without a hospital disinfectant claim":
        "Labeling as a window cleaner without a hospital disinfectant claim listed",
    "One bag of saline used as a common flush for multiple peripheral catheters":
        "One bag of saline used as a common flush for several peripheral catheters",
    "Limit direct contact and require gown and gloves for anticipated body contact":
        "Limit direct contact and require gown and gloves for body contact",
    "Replace hand hygiene with one pair of gloves for the whole shift":
        "Replace hand hygiene with a single pair of gloves for the whole shift",
    "Immediate isolation from susceptible individuals and airborne precautions when available":
        "Isolation from susceptible individuals and airborne precautions",
    "Seating in the general pediatric waiting area during rash onset":
        "Seating in the general pediatric waiting area during rash onset and cough",
    "Rooming with an immunocompromised patient in the same exam room":
        "Rooming with an immunocompromised patient in the same exam room today",
    "Discharge home by public transit while the lesions remain open":
        "Discharge home by public transit while the lesions stay open and weeping",
    "They can harbor organisms and interfere with effective hand washing and rub coverage":
        "They harbor organisms and interfere with hand washing and rub coverage",
    "They improve alcohol rub penetration under stone settings":
        "They improve alcohol rub penetration under stone settings and long nails",
    "Shake linen in the hallway to remove solids before placing it in laundry bags":
        "Shake linen in the hallway to remove solids before placing it in the laundry bags",
    "Tape the tear with nonsterile tape and finish the procedure without regloving":
        "Tape the tear with nonsterile tape and finish the procedure without regloving it",
    "When vaccines and staff lunches share one refrigerator shelf to save space":
        "When vaccines and staff lunches share one refrigerator shelf to save clinic space",
    "Separate seating, offer a mask, and expedite rooming per respiratory hygiene policy":
        "Separate seating, offer a mask, and expedite rooming per policy",
    "Follow protocol, ask the charge nurse or provider, and wear PPE pending clarification":
        "Follow protocol, ask the charge nurse, and wear PPE pending clarification",
    "Enter without PPE to ask about travel history before calling the nurse":
        "Enter without PPE to ask about travel history before calling the charge nurse",
    "Nursing unit room color code without the patient name or MRN":
        "Nursing unit room color code without the patient name or medical record number",
    "Drawn whenever the phlebotomist returns from break without timing it":
        "Drawn whenever the phlebotomist returns from break without timing the draw",
    "After twenty-four hours at room temperature to maximize bacterial colony growth":
        "After twenty-four hours at room temperature to maximize the bacterial colony growth",
    "Activate safety device and place the intact needle in an approved sharps container":
        "Activate the safety device and place the needle in an approved sharps container",
    "Break the needle off into the regular trash can to save sharps container space":
        "Break the needle off into the regular trash can to save on container space",
    "Ordered tests, clinical information, collection time, and patient identifiers":
        "Ordered tests, clinical information, collection time, and identifiers",
    "Waiting room chair inventory colors for the maintenance department":
        "Waiting room chair inventory colors for the facilities maintenance department",
    "Intracellular potassium release falsely elevates serum or plasma potassium results":
        "Intracellular potassium release falsely elevates serum potassium results",
    "Records parking receipts for outpatient phlebotomy visits at the clinic entrance":
        "Records parking receipts for outpatient phlebotomy visits at the clinic car park",
    "When legal or workplace testing requires sealed kits and witnessed blood collection":
        "When legal or workplace testing requires sealed kits and witnessed collection",
    "Whenever gray-top fluoride tubes are unavailable for routine glucose testing":
        "Whenever gray-top fluoride tubes are unavailable for routine glucose testing work",
    "The test may be collected next week when the central laboratory is less busy":
        "The test may be collected next week when the central laboratory is less busy then",
    "To warm the blood sample to body temperature for oral trials":
        "To warm the blood sample to body temperature for oral patient drinking trials",
    "Blood and other potentially infectious materials such as semen and cerebrospinal fluid":
        "Blood and potentially infectious materials such as semen and cerebrospinal fluid",
    "Blood along with every body fluid a patient produces, including sweat":
        "Blood along with every other body fluid a patient produces, including sweat and tears",
    "Exposure determination, engineering and work practice controls, PPE, and post-exposure care":
        "Exposure determination, controls, protective equipment, and post-exposure care",
    "Exposure determination, training dates, and a budget for protective gear":
        "Exposure determination, training dates, and a supply budget for protective gear",
    "Remove or isolate the hazard with devices such as safety needles and sharps containers":
        "Remove or isolate the hazard with safety needles and sharps containers",
    "Eye protection such as goggles or a face shield in addition to other needed PPE":
        "Eye protection such as goggles or a face shield plus other needed PPE",
    "They may not require payment when vaccination is offered due to occupational exposure":
        "They may not require payment when vaccination is offered for exposure",
    "Devices and equipment that physically block contact with blood":
        "Devices and equipment that physically block contact with blood or other fluids",
    "Source patient status when available, employee baseline labs, and follow-up testing schedule":
        "Source patient status, employee baseline labs, and a follow-up testing schedule",
    "Baseline labs, a follow-up testing schedule, and the billing account number":
        "Baseline labs, a follow-up testing schedule, and the employee's billing account number",
    "To document the immune response when recommended for occupational health programs":
        "To document the immune response for occupational health programs",
    "Wearing PPE, absorbing the spill, cleaning it, then disinfecting with a germicide":
        "Wearing PPE, absorbing the spill, cleaning it, then disinfecting it",
    "When contact with blood, OPIM, mucous membranes, or nonintact skin is anticipated":
        "When contact with blood, OPIM, mucous membranes, or nonintact skin is expected",
    "When the task involves a specimen that might contain blood":
        "When the task involves a specimen that might contain blood or OPIM",
    "Refer the request to purchasing for a price and contract comparison first":
        "Refer the request to the purchasing department for a price and contract comparison",
    "Passing the instrument through the doorway to avoid crossing into the room":
        "Passing the instrument through the doorway to avoid anyone crossing the room",
    "Employer medical records stay confidential and are kept apart from the personnel file":
        "Employer medical records stay confidential and separate from personnel files",
    "The exposure details are shared with the whole unit for safety":
        "The exposure details are shared with the whole clinical unit for safety awareness",
    "The room number on the exam room sign, checked against the appointment schedule":
        "The room number on the exam room sign, checked against the day's appointment schedule",
    "When the patient requests a refill of an unrelated over-the-counter product":
        "When the patient requests a refill of an unrelated over-the-counter medication",
    "A second signature from another staff member on the administration record":
        "A second signature from another staff member on the medication administration record",
    "Room the patient privately, explain confidentiality limits, and complete the testing":
        "Room the patient privately, explain the limits, and complete the testing",
    "Room the patient privately, explain the limits, and delay the testing":
        "Room the patient privately, explain the limits, and delay the testing visit",
    "Chart the refusal and counseling, and administer the first vaccine of the series":
        "Chart the refusal and counseling, and administer the first vaccine of the series anyway",
    "Sit the patient up, lean forward, and pinch the soft nose for ten to fifteen minutes":
        "Sit the patient up, lean forward, and pinch the nose for ten to fifteen minutes",
    "Give fifteen grams of fast-acting carbohydrate and recheck glucose in fifteen minutes":
        "Give fifteen grams of fast-acting carbohydrate and recheck in fifteen minutes",
    "Induce vomiting so the chemical leaves the stomach as quickly as possible":
        "Induce vomiting so the chemical leaves the stomach as quickly as possible at home",

    # -------------------- second balance pass: keys shortened to match siblings
    "Patients with suspected or confirmed infection spread by large respiratory droplets":
        "Patients with suspected or confirmed droplet-spread infection",
    "Techniques that reduce microbes and protect clean sites from contamination":
        "Techniques that reduce microbes and protect clean sites and supplies",
    "Sterilization of every countertop with autoclave packs each morning before clinic":
        "Sterilization of every countertop with autoclave packs each morning shift",
    "One needle, one syringe, one patient for each injection and medication entry":
        "One needle, one syringe, one patient for each injection and entry",
    "Handle with gloves and place in labeled leak-resistant laundry bags without rinsing":
        "Handle with gloves and place in labeled leak-resistant laundry bags",
    "Shake linen in the hallway to remove solids before placing it in the laundry bags":
        "Shake linen in the hallway to remove solids before placing it in laundry bags",
    "When policy separates staff food from medications and specimens in labeled areas":
        "When policy separates staff food from medications and specimens",
    "When vaccines and staff lunches share one refrigerator shelf to save clinic space":
        "When vaccines and staff lunches share one refrigerator shelf to save space",
    "Patient name, identifier, collection date and time, and collector when required":
        "Patient name, identifier, collection date and time, and collector",
    "Drawn at the ordered minute mark and processed per laboratory test instructions":
        "Drawn at the ordered minute mark and processed per test instructions",
    "Within thirty minutes to two hours per laboratory policy unless additive is present":
        "Within thirty minutes to two hours per laboratory policy",
    "After twenty-four hours at room temperature to maximize the bacterial colony growth":
        "After twenty-four hours at room temperature to maximize colony growth",
    "Activate the safety device and place the needle in an approved sharps container":
        "Activate the safety device and place the needle in a sharps container",
    "Tracks each handler of a legal or forensic sample from collection through storage":
        "Tracks each handler of a legal sample from collection through storage",
    "When legal or workplace testing requires sealed kits and witnessed collection":
        "When legal or workplace testing requires sealed kits and witnessed draws",
    "Whenever gray-top fluoride tubes are unavailable for routine glucose testing work":
        "Whenever gray-top fluoride tubes are unavailable for routine glucose testing",
    "Urgent processing for patient care; prioritize specimen collection and transport":
        "Urgent processing for patient care; prioritize collection and transport",
    "The test may be collected next week when the central laboratory is less busy then":
        "The test may be collected next week when the central laboratory is less busy",
    "Blood and potentially infectious materials such as semen and cerebrospinal fluid":
        "Blood and other potentially infectious materials such as semen and CSF",
    "Blood along with every other body fluid a patient produces, including sweat and tears":
        "Blood along with every body fluid a patient produces, including sweat and tears",
    "Policies and behaviors such as no recapping and hand hygiene that reduce exposure":
        "Policies and behaviors such as no recapping and hand hygiene that reduce risk",
    "Source patient status, employee baseline labs, and a follow-up testing schedule":
        "Source patient status, baseline labs, and a follow-up testing schedule",
    "Baseline labs, a follow-up testing schedule, and the employee's billing account number":
        "Baseline labs, a follow-up testing schedule, and the billing account number",
    "Evaluate the request and implement safer devices in the exposure control plan":
        "Evaluate the request and implement safer devices in the control plan",
    "Refer the request to the purchasing department for a price and contract comparison":
        "Refer the request to purchasing for a price and contract comparison",
    "Using a neutral zone or a tray instead of hand-to-hand transfer of instruments":
        "Using a neutral zone or a tray instead of hand-to-hand transfer",
    "The exposure details are shared with the whole clinical unit for safety awareness":
        "The exposure details are shared with the whole unit for safety awareness",
    "The source patient's identity is posted in the staff break room":
        "The source patient's identity is posted with the incident report in the break room",
    "Confidentiality ends once the employee returns to work":
        "Confidentiality ends once the employee returns to work and is cleared",
    "One identifier, such as full name, confirmed with the patient before the dose":
        "A single identifier, such as the full name, confirmed with the patient before the dose",
    "Before selecting or administering any drug, including vaccines and contrast dye":
        "Before selecting or administering any drug, including vaccines and contrast",
    "An electronic match of patient, product, and order before the dose is given":
        "An electronic match of patient, product, and order before the dose",
    "A second signature from another staff member on the medication administration record":
        "A second signature from another staff member on the administration record",
    "Chart the refusal and counseling, provide the information sheet, and schedule follow-up":
        "Chart the refusal and counseling, give the information sheet, and follow up",
    "Chart the refusal and counseling, and administer the first vaccine of the series anyway":
        "Chart the refusal and counseling, and administer the first vaccine of the series",
    "Rinse the mouth with mouthwash and give the patient a soft snack to eat":
        "Rinse the mouth with mouthwash and give the patient a soft snack to eat at once",

    # ------------------------------- third balance pass on the last four items
    "Evaluate the request and implement safer devices in the control plan":
        "Evaluate the request and implement safer devices in the plan",
    "Refer the request to purchasing for a price and contract comparison":
        "Refer the request to purchasing for a price and contract comparison first",
    "The source patient's identity is posted with the incident report in the break room":
        "The source patient's identity is posted with the report in the break room",
    "Two identifiers, such as full name and date of birth, confirmed with the patient":
        "Two identifiers, such as name and date of birth, confirmed with the patient",
    "A single identifier, such as the full name, confirmed with the patient before the dose":
        "A single identifier, such as the full name, confirmed with the patient in the room",
    "The room number on the exam room sign, checked against the day's appointment schedule":
        "The room number on the exam room sign, checked against the schedule",
    "Induce vomiting so the chemical leaves the stomach as quickly as possible at home":
        "Induce vomiting so the chemical leaves the stomach quickly at home",
    "Employer medical records stay confidential and separate from personnel files":
        "Employer medical records stay confidential and apart from personnel files",
    "A single identifier, such as the full name, confirmed with the patient in the room":
        "A single identifier, such as the full name, confirmed with the patient",
    "A single identifier, such as the full name, confirmed with the patient":
        "A single identifier, such as the full name, confirmed with the patient first",
}
