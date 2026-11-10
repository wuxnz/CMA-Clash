// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

// Phlebotomy Test Study Guide. Generated from classquiz/seed/flashcards/phlebotomy-test-study.json,
// the same source the seed uses for the study guide, quiz, flashcards, and practice test.
// Do not edit by hand: change the JSON and regenerate.
//
// t = question, d = answer, c = category index, w = three wrong answers,
// qd and qw = quiz and practice answers (the same as d and w here),
// e = explanation, u = official reference URL, s = reference name.

import type { TestCard } from './diabetes-test-2nd-half';

export const PHLEB_TEST_CATEGORIES: string[] = [
  "Safety and compliance",
  "Patient identification and preparation",
  "Routine blood collection",
  "Order of draw and additives",
  "Special collections and processing",
  "Hemolysis and specimen quality",
  "Ethics and core knowledge"
];

export const PHLEB_TEST_CARDS: TestCard[] = [
 {
  "t": "Under OSHA's bloodborne pathogens rules, what must an employer provide to reduce needlestick risk?",
  "d": "Engineering controls such as safety-engineered needles and tube holders, which the employer must supply.",
  "c": 0,
  "w": [
   "Written warnings posted in the lab, along with a reminder to take extra care during every draw.",
   "Gloves and gowns only, with the same needles and holders that were used before the rule.",
   "A yearly training video, with no requirement to supply any new safety-engineered devices."
  ],
  "qd": "Engineering controls such as safety-engineered needles and tube holders, which the employer must supply.",
  "qw": [
   "Administrative controls such as written exposure plans and sharps-disposal schedules, which the employer must supply to staff.",
   "Work practice controls such as a ban on recapping, with safety devices left for each employee to purchase as needed.",
   "Hepatitis B vaccination offered to staff, which the employer must supply in place of safety-engineered needles."
  ],
  "e": "OSHA requires employers to evaluate and control exposure, which includes safer devices. Tube holders and safety devices are part of that control.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "What should happen to a needle right after it is removed from a patient?",
  "d": "Activate the safety device and discard it into a sharps container without recapping.",
  "c": 0,
  "w": [
   "Recap it carefully with one hand so the next patient is protected from accidental contact.",
   "Set it on the tray until the draw is finished, then activate the safety device at the desk.",
   "Place it in a biohazard bag with the used gauze and tubes for later disposal."
  ],
  "qd": "Activate the safety device and discard it into a sharps container without recapping.",
  "qw": [
   "Activate the safety device and place it in a puncture-resistant container at the end of the draw, after labeling the tubes.",
   "Recap it with the one-handed scoop technique and place it in the sharps container at the end of the draw.",
   "Leave the safety device open until the patient has been cleared, then activate it and discard it in the sharps container."
  ],
  "e": "Used needles must never be recapped. The safety device should be activated the moment the needle leaves the patient, because the window for a needlestick is open until it is concealed.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "What is the maximum fill level recommended for a sharps container?",
  "d": "No more than 75 percent full.",
  "c": 0,
  "w": [
   "Completely full, so that no space is wasted and fewer containers are used each week.",
   "Half full, so the container is light enough to lift and carry to the disposal area.",
   "Up to the top, as long as the lid closes without needing extra force from the user."
  ],
  "qd": "No more than 75 percent full.",
  "qw": [
   "No more than 90 percent full, unless the container lid can still be closed without force.",
   "No more than 50 percent full, so the container can be moved safely to the disposal area.",
   "No more than 75 percent by weight, measured on the facility's scale before each disposal."
  ],
  "e": "Many facilities and sharps-container labels use a 75 percent fill line, as the course handout states. OSHA's bloodborne pathogens standard requires containers to be closable, leak-proof, and not overfilled; it does not set a 75 percent number.",
  "u": "https://www.osha.gov/bloodborne-pathogens/standards",
  "s": "OSHA: Bloodborne Pathogens Standards"
 },
 {
  "t": "Why must a tube holder stay on the needle after the last tube is removed?",
  "d": "Removing the holder exposes the phlebotomist to the back end of a contaminated needle.",
  "c": 0,
  "w": [
   "It keeps the needle from bending while the used assembly is carried to the disposal area.",
   "It keeps the needle cool so that the blood left in the hub does not clot before disposal.",
   "It keeps the needle sterile until the next tube is ready to be filled from the same site."
  ],
  "qd": "Removing the holder exposes the phlebotomist to the back end of a contaminated needle.",
  "qw": [
   "Removing the holder lets blood drain from the back of the needle, which can contaminate the sample tubes.",
   "Removing the holder breaks the seal of the safety device, which must then be replaced before disposal.",
   "Removing the holder causes the needle to retract, which can injure the patient during the disposal step."
  ],
  "e": "OSHA requires used needles to be discarded immediately without recapping. The course handout adds that the tube holder stays on the needle so the whole assembly is disposed of as one unit.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "What is the correct way to anchor the vein during a draw?",
  "d": "Pull the skin firmly downward below the site with the thumb.",
  "c": 0,
  "w": [
   "Place the index and middle fingers in front of the needle to hold the vein in place.",
   "Spread two fingers on either side of the site to keep the vein from rolling away.",
   "Press the flat of the palm directly over the site to stop the vein from moving."
  ],
  "qd": "Pull the skin firmly downward below the site with the thumb.",
  "qw": [
   "Press firmly upward above the site with the index finger to stop the vein from rolling away.",
   "Pull the skin sideways across the site with two fingers to keep the vein from moving during entry.",
   "Press the thumb directly over the site to flatten the vein against the tissue below it."
  ],
  "e": "Anchoring from below with the thumb keeps fingers out of the path of the needle. A two-finger spread puts the worker at risk if the patient jumps or someone bumps the worker.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "What does a safety transfer device do when blood is collected by syringe?",
  "d": "It moves blood from the syringe into the tube, keeping the fingers out of the way of the needle.",
  "c": 0,
  "w": [
   "It holds the syringe plunger steady so that the pressure in the vein stays constant during the draw.",
   "It attaches the tourniquet to the syringe so the vein stays filled during the transfer step.",
   "It cools the blood sample to slow hemolysis while it moves from the syringe to the tube."
  ],
  "qd": "It moves blood from the syringe into the tube, keeping the fingers out of the way of the needle.",
  "qw": [
   "It moves blood from the syringe into the tube through a valve that keeps the vacuum constant during the fill.",
   "It moves blood from the syringe into the tube while keeping the plunger from being pulled back too far.",
   "It moves blood from the syringe into the tube and locks the needle so it cannot be withdrawn accidentally."
  ],
  "e": "A needle inside the transfer device protects the user. The tube fills from the syringe through the device, which is why OSHA requires one in place of the venipuncture needle.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "What do standard precautions require when contact with blood or body fluids is possible?",
  "d": "Hand hygiene, gloves, and other PPE matched to the task, treating all blood as potentially infectious.",
  "c": 0,
  "w": [
   "Gloves only for patients with a known infection listed on the chart before the draw begins.",
   "Hand washing only after the procedure is finished and the patient has left the room.",
   "A surgical mask only, since the main risk from blood during a draw is through the air."
  ],
  "qd": "Hand hygiene, gloves, and other PPE matched to the task, treating all blood as potentially infectious.",
  "qw": [
   "Hand hygiene and gloves, with the level of PPE chosen according to the patient's known infection status.",
   "Gloves and a gown, changed between patients, with eye protection required only for procedures with splash risk.",
   "Hand hygiene and a mask, with gloves required only when the blood is visibly on the skin of the patient."
  ],
  "e": "Standard precautions apply to every patient, because infection status is not always known. PPE and hand hygiene reduce exposure to blood and body fluids.",
  "u": "https://www.cdc.gov/infection-control/hcp/isolation-precautions/index.html",
  "s": "CDC: Isolation Precautions"
 },
 {
  "t": "When should hand hygiene be performed during a routine venipuncture?",
  "d": "Before putting on gloves, and again after removing them, following the CDC hand hygiene steps.",
  "c": 0,
  "w": [
   "Only at the end of the shift, after the last patient has been drawn and the tubes are sent out.",
   "Only if the gloves tear or become visibly soiled during the venipuncture procedure itself.",
   "Only after touching the tubes, since the patient's skin is not considered a source of germs."
  ],
  "qd": "Before putting on gloves, and again after removing them, following the CDC hand hygiene steps.",
  "qw": [
   "Before putting on gloves only, since hands are cleaned again automatically when gloves are removed at the sink.",
   "After removing gloves and before touching the tubes, but not before gloving if the hands look clean.",
   "Before each tube is filled and after the bandage is applied, following the facility's sanitizer schedule."
  ],
  "e": "CDC hand hygiene guidance calls for cleaning hands at key moments of care, including before and after glove use, to prevent spread of germs.",
  "u": "https://www.cdc.gov/infection-control/hcp/hand-hygiene/index.html",
  "s": "CDC: Hand Hygiene in Healthcare Settings"
 },
 {
  "t": "What is the first step after a needlestick or other exposure to blood?",
  "d": "Wash the area and report the exposure right away, so a post-exposure evaluation can begin as soon as possible.",
  "c": 0,
  "w": [
   "Wait until the end of the shift to report it, so that the incident can be documented with the day's other notes.",
   "Apply an antiseptic and return to work, since minor exposures rarely need a medical evaluation.",
   "Ask the patient to reveal their test history first, before any report is made to a supervisor."
  ],
  "qd": "Wash the area and report the exposure right away, so a post-exposure evaluation can begin as soon as possible.",
  "qw": [
   "Wash the area and document the exposure in the chart, so the treating physician can review it at the next visit.",
   "Wash the area and report the exposure after the shift, once the tubes have been delivered to the lab safely.",
   "Wash the area and report the exposure only if the source patient's test results are positive for a bloodborne pathogen."
  ],
  "e": "OSHA requires a documented post-exposure evaluation and follow-up. Prompt reporting allows the evaluation and any prophylaxis to be started in time.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "What does the OSHA Bloodborne Pathogens Standard require of employers for personal protective equipment?",
  "d": "Provide PPE such as gloves, gowns, and eye protection at no cost, and make sure it is used correctly.",
  "c": 0,
  "w": [
   "Require employees to buy their own gloves, with the employer posting only a reminder notice.",
   "Provide PPE only to supervisors, who then decide which employees need it for each shift.",
   "Provide PPE only for surgery, since phlebotomy is classified as a low-exposure procedure."
  ],
  "qd": "Provide PPE such as gloves, gowns, and eye protection at no cost, and make sure it is used correctly.",
  "qw": [
   "Provide PPE such as gloves and gowns, with eye protection left to the employee's discretion for routine draws.",
   "Provide PPE at no cost, but only to employees who have completed the annual training and signed the form.",
   "Provide PPE such as gloves and gowns for a fee deducted from pay, with eye protection provided at no cost."
  ],
  "e": "OSHA's bloodborne pathogens standard requires employers to provide appropriate PPE at no cost to employees and to ensure its use.",
  "u": "https://www.osha.gov/bloodborne-pathogens/standards",
  "s": "OSHA: Bloodborne Pathogens Standards"
 },
 {
  "t": "How many patient identifiers does CLSI recommend confirming before a draw?",
  "d": "At least two, such as the full name and date of birth, compared with the request form and wristband.",
  "c": 1,
  "w": [
   "One, the patient's full name, confirmed by the collector before the draw begins at the bedside.",
   "Three, including the room number, medical record number, and the ordering physician's name.",
   "Two, the room number and the name of the nurse who admitted the patient to the unit."
  ],
  "qd": "At least two, such as the full name and date of birth, compared with the request form and wristband.",
  "qw": [
   "At least two, such as the full name and medical record number, compared with the request form and wristband.",
   "At least two, such as the full name and the room number, confirmed with the ordering provider by phone.",
   "At least two, such as the date of birth and the insurance number, compared with the lab's accession list."
  ],
  "e": "CLSI asks the patient to state their full name and birth date, and the collector compares them with the request form. Room numbers can change and are not patient identifiers.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Which approach best avoids a false confirmation of a patient's identity?",
  "d": "Ask the patient to state their full name and birth date, rather than asking 'Are you John Doe?'",
  "c": 1,
  "w": [
   "Read the name aloud from the chart and ask the patient to nod if it is correct.",
   "Ask whether the patient is the person whose name is on the wristband in the room.",
   "Ask a family member standing nearby to confirm the patient's name and address aloud."
  ],
  "qd": "Ask the patient to state their full name and birth date, rather than asking 'Are you John Doe?'",
  "qw": [
   "Ask the patient to spell their last name aloud and then state the date of birth, rather than reading the name.",
   "Ask the patient to state the name on the wristband, then compare the room number with the chart.",
   "Ask the patient to confirm the name on the requisition, then state the date of birth for the record."
  ],
  "e": "A yes-or-no question invites a polite yes. Asking the patient to state their own name and birth date gives the collector information to compare.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "When can an identification bracelet be trusted to identify a patient?",
  "d": "Only when it is attached to the patient and matches what the patient states.",
  "c": 1,
  "w": [
   "Whenever it is taped to the foot of the bed, since it is still in the same room as the patient.",
   "Whenever it hangs from the bedrail and is visible to the phlebotomist from the doorway.",
   "Whenever a nurse has said the name aloud at the station that morning before the draw."
  ],
  "qd": "Only when it is attached to the patient and matches what the patient states.",
  "qw": [
   "Only when it is attached to the patient and the patient has not been moved to a different room since admission.",
   "Only when it is attached to the patient and the bedside label was printed the same day as the draw.",
   "Only when it is attached to the patient, and the patient's family has confirmed the name in writing."
  ],
  "e": "Bracelets attached to the bedrail, the bedside table, or the foot of the bed do not identify the patient. Assuming otherwise can treat the wrong person with someone else's results.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Who should provide identification for an unconscious patient who cannot communicate?",
  "d": "A family member or caregiver, with the verifier's name documented in case the patient is misidentified.",
  "c": 1,
  "w": [
   "The phlebotomist, who should use the room number and bed location to identify the patient.",
   "The nearest patient on the ward, who can confirm the name of the person in the next bed.",
   "The physician on call, who should sign the requisition as the only verifier of identity."
  ],
  "qd": "A family member or caregiver, with the verifier's name documented in case the patient is misidentified.",
  "qw": [
   "A family member or caregiver, with the verifier's signature recorded only if the patient later disputes the result.",
   "The patient's attending nurse, with the verifier's name documented on the requisition after the draw is complete.",
   "A family member or caregiver, who may verbally confirm the name without the verifier's identity being recorded."
  ],
  "e": "When a patient cannot give identifying information, a family member or caregiver must provide it. Documenting the verifier allows the error to be traced if one occurs.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What should you do if the requisition and the patient's ID band do not match?",
  "d": "Do not draw the patient until the discrepancy is resolved and corrected.",
  "c": 1,
  "w": [
   "Draw the patient and note the mismatch on the tube label so the lab can sort it out later.",
   "Draw the patient using the name on the requisition, since the requisition is the legal order.",
   "Ask the patient to choose which name is correct, then draw them under the name they choose."
  ],
  "qd": "Do not draw the patient until the discrepancy is resolved and corrected.",
  "qw": [
   "Do not draw the patient until the discrepancy is noted on the requisition and the ordering provider is informed.",
   "Draw the patient after the discrepancy is reported to the charge nurse and the shift supervisor on duty.",
   "Do not draw the patient until the discrepancy is corrected on the wristband by a clerk at the registration desk."
  ],
  "e": "CLSI requires that discrepancies be resolved before the draw. A specimen with the wrong identity is a serious error, not a labeling detail.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What is the acceptable number of mislabeled samples per person or per month?",
  "d": "Zero.",
  "c": 1,
  "w": [
   "One per month, if the error is reported in writing to the supervisor within one business day.",
   "Fewer than one percent of all samples collected at the facility in a given calendar month.",
   "Up to five per week, when the lab is very busy and the collector is working alone."
  ],
  "qd": "Zero, for each patient and for the facility as a whole in any month.",
  "qw": [
   "Zero per person, but up to two per month for the facility as a whole, if each one is documented in writing.",
   "One per person per month, if the error is reported in writing to the supervisor within one business day.",
   "Zero per month for the facility, but one per person is allowed when the collector is working alone in a unit."
  ],
  "e": "The course handout states that the acceptable number of mislabeled samples is zero, and that every error should trigger a root-cause review.",
  "u": "https://www.ahrq.gov/patient-safety/index.html",
  "s": "AHRQ: Patient Safety"
 },
 {
  "t": "Why is the question 'Are you John Doe?' discouraged when confirming a patient's name?",
  "d": "The patient may answer yes just to be polite, or may misunderstand the name.",
  "c": 1,
  "w": [
   "It takes too long, and the lab will not accept samples collected after a short conversation.",
   "It is only required for outpatients, while inpatients are identified by the wristband alone.",
   "It may upset the patient, and privacy law forbids using a patient's name in any question."
  ],
  "qd": "A patient may answer yes just to be polite, or may misunderstand the name.",
  "qw": [
   "A patient may answer yes without hearing the name clearly, but the answer is still counted as a valid identifier.",
   "A patient may answer yes because the question is leading, which means the answer is recorded as confirmed by default.",
   "A patient may answer yes if they are hard of hearing, so the question is replaced with a written form at the desk."
  ],
  "e": "Relying on a verbal yes can lead to misidentification. The patient should state their own name in response to an open request.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What information should be explained to a patient before a venipuncture?",
  "d": "The procedure to be performed, what the patient may feel, and the patient's consent to the draw.",
  "c": 1,
  "w": [
   "The price of each test and the insurance billing code, since that affects how the lab charges.",
   "The name of the technician who will process the tubes after collection in the lab.",
   "The time the results will post, since the ordering physician handles all of the explanation."
  ],
  "qd": "The procedure to be performed, what the patient may feel, and the patient's consent to the draw.",
  "qw": [
   "The procedure to be performed, how long the draw will take, and the facility's policy on billing disputes.",
   "The procedure to be performed, what the lab will test, and the patient's right to a copy of the requisition.",
   "The procedure to be performed, what the patient may feel, and the physician's consent to the draw on the patient's behalf."
  ],
  "e": "Explaining the procedure and obtaining consent is part of patient preparation. Patients should understand what will happen before the needle is inserted.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Which arm should be avoided for venipuncture?",
  "d": "The arm with a fistula or graft, or the same side as a mastectomy.",
  "c": 1,
  "w": [
   "The non-dominant arm, because its veins are usually smaller and harder to anchor during a draw.",
   "The arm with the most visible vein, because the vein may collapse once the tourniquet is applied.",
   "The arm the patient writes with, since the veins on the dominant side are often thinner."
  ],
  "qd": "The arm with a fistula or graft, or the same side as a mastectomy.",
  "qw": [
   "The arm with a fistula or graft only if it is actively in use for dialysis, or the arm with a recent IV infusion.",
   "The arm on the same side as a mastectomy only when the lymph nodes were removed, or an arm with a cast.",
   "The arm with a fistula or graft, or any arm with a bruise that is larger than a coin in size."
  ],
  "e": "Draws in a fistula, a graft, or on the mastectomy side are avoided. The arm the patient uses most is not a restriction on its own.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Where should a venipuncture not be performed?",
  "d": "Above an IV line, or in an area with edema, hematoma, scars, or burns.",
  "c": 1,
  "w": [
   "Below the wrist on the back of the hand, which holds the veins closest to the skin surface.",
   "On the hand of the dominant arm, since the veins there are usually the easiest to reach.",
   "Over a flat, firm area of the forearm, which keeps the vein stable during the draw."
  ],
  "qd": "Above an IV line, or in an area with edema, hematoma, scars, or burns.",
  "qw": [
   "Below an IV line on the same arm, or in an area with mild bruising, freckles, or a healed surgical scar.",
   "In an area with edema that is limited to the ankle, or above an IV line that is saline-locked.",
   "Above an IV line only when the IV is saline-locked, or in an area with superficial varicose veins."
  ],
  "e": "Edema, hematoma, scars, burns, and areas that feel hard or pulsate are unsafe or unreliable sites. A draw above an IV can contaminate the sample.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "How should a vein be palpated before the draw?",
  "d": "With the index finger, never the thumb, because the thumb has its own pulse.",
  "c": 1,
  "w": [
   "With the thumb, which is more sensitive to small changes in the texture of the vein wall.",
   "With the little finger, which avoids pressing too hard on the surface of the skin.",
   "With the flat palm, held on the arm for a few seconds at the proposed site before the draw."
  ],
  "qd": "With the index finger, never the thumb, because the thumb has its own pulse.",
  "qw": [
   "With the index finger and middle finger together, which gives a wider reading of the vein's depth.",
   "With the ring finger, which is more sensitive than the index finger to changes in vein texture.",
   "With the thumb after the index finger has checked the site, because the thumb reads depth more accurately."
  ],
  "e": "The thumb's own pulse can be mistaken for a vein. The index finger is the recommended palpation finger.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Which vein is the first choice for a venipuncture?",
  "d": "The median cubital vein, then the cephalic, with the basilic vein last.",
  "c": 1,
  "w": [
   "The basilic vein first, because it is the largest and lies near the brachial artery and nerve.",
   "The cephalic vein first, because it is the most visible vein on the forearm of most adults.",
   "A dorsal hand vein first, because it is the easiest vein to anchor during a draw."
  ],
  "qd": "The median cubital vein, then the cephalic, with the basilic vein last.",
  "qw": [
   "The cephalic vein, then the median cubital, with the basilic vein used only if the others are unavailable.",
   "The median basilic vein, then the cephalic, with the median cubital vein last to avoid the brachial artery.",
   "The median cubital vein, then the basilic, with the cephalic vein last because it lies closest to the skin."
  ],
  "e": "The basilic vein lies close to the brachial artery and median nerve, so it is used last. The median cubital vein is the usual first choice.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "How long can a tourniquet stay on before a draw, and what should happen if it stays longer?",
  "d": "No longer than one minute. If it stays on longer, release it and wait two minutes before reapplying.",
  "c": 2,
  "w": [
   "Up to three minutes, to let the veins fill fully before the needle goes into the skin.",
   "Until the patient has made a fist at least five times in a row without stopping for breath.",
   "Until the first tube is filled, and then it stays on until the last tube has been labeled."
  ],
  "qd": "No longer than one minute. If it stays on longer, release it and wait two minutes before reapplying.",
  "qw": [
   "No longer than two minutes. If it stays on longer, release it and wait one minute before reapplying.",
   "No longer than one minute. If it stays on longer, release it immediately and reapply after the patient has rested.",
   "No longer than one minute per arm. If it stays on longer, release it and wait five minutes before reapplying."
  ],
  "e": "A tourniquet left on too long can change test results. Releasing it and waiting two minutes lets the blood return to normal before another application.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Where should the tourniquet be placed relative to the puncture site?",
  "d": "Three to four inches (7.5 to 10 cm) above the site.",
  "c": 2,
  "w": [
   "Directly over the site, so the vein stays closed until the needle is in place for the draw.",
   "One inch (2.5 cm) below the site, pressed against the bone for a firm seal on the vein.",
   "At the wrist, far from the site, so that the hand stays warm during the entire draw."
  ],
  "qd": "Three to four inches (7.5 to 10 cm) above the site.",
  "qw": [
   "Three to four centimeters (1.5 inches) above the site, snug enough to stop arterial flow.",
   "Five to six inches (12.5 to 15 cm) above the site, to restrict venous return fully during the draw.",
   "Three to four inches (7.5 to 10 cm) below the site, so the vein is compressed before the needle enters."
  ],
  "e": "The tourniquet is placed above the site to restrict venous flow and make the vein more prominent. It is not placed directly over the puncture.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What should the patient do with the hand after the tourniquet is applied?",
  "d": "Make a fist without pumping it, since pumping can change some test results.",
  "c": 2,
  "w": [
   "Open and close the hand rapidly for fifteen seconds to bring the blood close to the surface.",
   "Hold the arm straight out with the fingers spread apart as far as they will go comfortably.",
   "Rest the hand flat on the table, palm up, with the fingers relaxed and open the whole time."
  ],
  "qd": "Make a fist without pumping it, since pumping can change some test results.",
  "qw": [
   "Make a fist and release it once every five seconds to keep the vein filled without pumping it.",
   "Make a loose fist, pumping gently only if the vein is hard to see at the start of the draw.",
   "Make a fist and hold it for the whole draw, since pumping is only needed for capillary samples."
  ],
  "e": "Fist pumping raises the potassium level and changes other results. A relaxed fist without pumping keeps the vein full without altering the sample.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What are the correct needle angle and bevel direction for a venipuncture?",
  "d": "15 to 30 degrees, bevel up.",
  "c": 2,
  "w": [
   "45 to 60 degrees, bevel down, so the needle slides into the vein without catching the wall.",
   "5 to 10 degrees, bevel down, so the needle stays flat against the vein wall during entry.",
   "90 degrees, bevel up, pushed straight into the center of the vein in one firm motion."
  ],
  "qd": "15 to 30 degrees, bevel up.",
  "qw": [
   "15 to 30 degrees, bevel down, so the needle enters the vein wall before the bevel flattens.",
   "30 to 45 degrees, bevel up, so the needle passes through the vein wall at a shallow angle.",
   "15 to 30 degrees, bevel up, with the tube holder angled at the same degree as the needle."
  ],
  "e": "A shallow angle with the bevel up enters the vein smoothly. A steep angle or a bevel down increases the risk of passing through the vein.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "When should the tourniquet be released during a venipuncture?",
  "d": "As soon as blood flow is established in the tube.",
  "c": 2,
  "w": [
   "After the last tube has been filled, so the vein stays dilated throughout the entire draw.",
   "Before the needle enters the skin, so the vein is not compressed during insertion.",
   "When the patient reports feeling dizzy, regardless of how far the draw has progressed so far."
  ],
  "qd": "As soon as blood flow is established in the tube.",
  "qw": [
   "Once the first tube is halfway filled, so the flow stays steady for the remaining tubes.",
   "After the needle is removed from the patient, so the vein stays dilated while the site is covered.",
   "Once the needle is seated in the vein, before any blood enters the first tube."
  ],
  "e": "Keeping the tourniquet on after flow starts can affect results. Releasing it as flow begins limits the time the tourniquet is in place.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Why should additive tubes be inverted right after they are filled?",
  "d": "To mix the additive with the blood immediately, which prevents clotting.",
  "c": 2,
  "w": [
   "To warm the blood so it flows more easily through the needle during the draw.",
   "To separate the serum from the cells before the sample is sent to the lab.",
   "To release air bubbles that formed in the tube during the vacuum draw."
  ],
  "qd": "To mix the additive with the blood immediately, which prevents clotting.",
  "qw": [
   "To distribute the heat of the blood evenly so the additive does not settle during the transfer.",
   "To wet the inside wall of the tube so that the additive does not stick to the stopper.",
   "To prevent the blood from separating into layers before the tube reaches the centrifuge in the lab."
  ],
  "e": "Additive tubes contain anticoagulant or clot activator that must mix with the blood as soon as it enters the tube.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "How should an additive tube be mixed after it is filled?",
  "d": "Gently inverted the number of times the tube requires, and never shaken.",
  "c": 2,
  "w": [
   "Shaken vigorously for ten seconds to mix the additive completely with the blood sample.",
   "Rolled rapidly across the table to spread the additive over the inside wall of the tube.",
   "Tapped sharply against the palm several times to remove the air bubbles from the blood."
  ],
  "qd": "Gently inverted the number of times the tube requires, and never shaken.",
  "qw": [
   "Gently inverted in the same direction each time, then rotated slowly to coat the stopper with additive.",
   "Gently inverted five to ten times, then shaken lightly to break up any small clots in the tube.",
   "Inverted once after the tube is full, then left to stand until the additive has settled to the bottom."
  ],
  "e": "Shaking can hemolyze red cells. The course handout says to invert gently and never shake.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "How many inversions does a light blue citrate tube need?",
  "d": "Three to four times, gently.",
  "c": 2,
  "w": [
   "Eight to ten times, as a lavender EDTA tube does, to mix the anticoagulant fully into the blood.",
   "Five times, as a gold serum tube does, to start the clotting process in the sample.",
   "Twenty times, rapidly, to make certain the citrate is evenly distributed through the plasma."
  ],
  "qd": "Three to four gentle inversions, so the citrate mixes without foaming.",
  "qw": [
   "Three to four gentle inversions with the tube held at the fill line, so the citrate does not overflow.",
   "Five to six gentle inversions, so the citrate mixes at the same rate as the gold serum tube.",
   "Eight to ten gentle inversions, since light blue citrate needs the same mixing as lavender EDTA."
  ],
  "e": "Light blue citrate tubes are inverted three to four times. Each tube type has its own number, so the handout's chart should be used.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What should happen after the final tube is filled, before the patient leaves?",
  "d": "Apply pressure until bleeding stops, bandage the site, and label every tube in the patient's presence.",
  "c": 2,
  "w": [
   "Leave the bandage off so the site can be checked later, then label the tubes at the lab desk.",
   "Elevate the arm above the head and send the patient to the waiting room to rest alone.",
   "Remove the gloves and wash the hands, then place the unlabeled tubes in the rack for transport."
  ],
  "qd": "Apply pressure until bleeding stops, bandage the site, and label every tube in the patient's presence.",
  "qw": [
   "Apply pressure for thirty seconds, check the site, and label the tubes after the patient has left the room.",
   "Apply pressure until bleeding stops, then leave the bandage off for 15 minutes so the site can be inspected.",
   "Apply pressure until bleeding stops, bandage the site, and label the tubes at the desk before the next patient."
  ],
  "e": "Pressure and a bandage prevent bleeding and hematoma. Labeling in front of the patient confirms identity at the point of collection.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "When is a capillary (dermal) puncture the better choice?",
  "d": "When only a small sample is needed or when venous access is difficult.",
  "c": 2,
  "w": [
   "When a large volume of blood is needed for a complete panel of chemistry and hematology tests.",
   "Whenever the patient has a fistula in the arm, since veins there cannot be used for any draw.",
   "When the patient takes anticoagulants, because capillary blood flows more slowly than venous blood."
  ],
  "qd": "When only a small sample is needed or when venous access is difficult.",
  "qw": [
   "When a single small sample is needed for a test that is stable at room temperature for several hours.",
   "When a large volume is needed, but the veins are too small for the standard winged butterfly needle.",
   "When only a small sample is needed, but only in patients who are taking anticoagulant therapy."
  ],
  "e": "A capillary puncture uses a lancet on the fingertip or the infant's heel. It is used for small volumes or when veins are hard to access.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "Where is the preferred site for a capillary puncture in an adult?",
  "d": "The side of the fingertip, rather than the center of the pad.",
  "c": 2,
  "w": [
   "The center of the palm, which has the most blood flow of any site on the hand.",
   "The big toe, which is easy to reach and rarely causes bruising or pain afterward.",
   "The inside of the wrist, over the radial artery, where the pulse is strongest."
  ],
  "qd": "The side of the fingertip, rather than the center of the pad.",
  "qw": [
   "The center of the fingertip pad, where the capillary beds are largest and most reliably perfused.",
   "The side of the ring finger, which has fewer nerves than the index or middle finger.",
   "The heel of the hand, which has the largest capillary beds and is least likely to cause pain."
  ],
  "e": "The lateral side of the finger avoids the nerve-rich pad and reduces pain. The center of the palm and the wrist are not recommended sites.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is the standard order of draw for venipuncture?",
  "d": "Blood cultures, light blue citrate, serum (gold or red), green heparin, lavender EDTA, then gray glycolytic inhibitor.",
  "c": 3,
  "w": [
   "Lavender EDTA, green heparin, light blue citrate, gold serum, blood cultures, and then gray.",
   "Gray glycolytic, lavender EDTA, green heparin, gold serum, light blue citrate, and then cultures.",
   "Light blue citrate, blood cultures, lavender EDTA, green heparin, gold serum, and then gray."
  ],
  "qd": "Blood cultures, light blue citrate, serum, green heparin, lavender EDTA, then gray.",
  "qw": [
   "Blood cultures, light blue citrate, green heparin, gold serum, lavender EDTA, then gray.",
   "Light blue citrate, blood cultures, gold serum, lavender EDTA, green heparin, then gray.",
   "Blood cultures, light blue citrate, serum, lavender EDTA, green heparin, then gray."
  ],
  "e": "The order runs from the tube least likely to contaminate the next to the most sensitive additives, so that carryover does not change results.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What does the mnemonic 'Boys Can See How Every Game' help you remember?",
  "d": "The order of draw: blood cultures, coagulation (citrate), serum, heparin, EDTA, and glycolytic inhibitor (gray).",
  "c": 3,
  "w": [
   "The names of the six tube colors in the order a phlebotomist sees them on the rack.",
   "The steps of venipuncture, from tourniquet placement to bandaging the site afterward.",
   "The sizes of needles used for adult, pediatric, and infant blood collection in the clinic."
  ],
  "qd": "The order of draw: blood cultures, coagulation (citrate), serum, heparin, EDTA, and glycolytic inhibitor (gray).",
  "qw": [
   "The order of draw: blood cultures, coagulation (citrate), serum, EDTA, heparin, and glycolytic inhibitor (gray).",
   "The order of draw: blood cultures, coagulation (citrate), heparin, serum, EDTA, and glycolytic inhibitor (gray).",
   "The order of draw: blood cultures, coagulation (citrate), serum, heparin, EDTA, and fluoride inhibitor (gray)."
  ],
  "e": "Each word in the mnemonic maps to one tube type in the standard order. The order is the same for glass and plastic tubes.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Why is a discard tube drawn first when a butterfly is used with a light blue citrate tube?",
  "d": "The tubing holds air, so a discard tube keeps the citrate tube filled to its line and maintains the 9:1 ratio.",
  "c": 3,
  "w": [
   "The discard tube warms the needle so that the light blue citrate tube does not clot inside the holder.",
   "The discard tube removes the anticoagulant from the tubing so the citrate tube fills more quickly.",
   "The discard tube collects the first blood, which contains the most white cells for later testing."
  ],
  "qd": "The tubing holds air, so a discard tube keeps the citrate tube filled to its line and maintains the 9:1 ratio.",
  "qw": [
   "The tubing holds saline from the catheter, so a discard tube keeps the citrate tube filled to its line and maintains the 9:1 ratio.",
   "The tubing holds air, so a discard tube removes clot fragments before the citrate tube is filled to its line.",
   "The tubing holds anticoagulant residue, so a discard tube keeps the citrate tube from diluting at its line."
  ],
  "e": "Citrate must be drawn to its fill line for the correct blood-to-additive ratio. The first tube after a butterfly fills with air from the tubing.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What is additive carryover?",
  "d": "Transfer of a small amount of blood and additive from one tube into the next tube filled, through the needle.",
  "c": 3,
  "w": [
   "Spilling of the additive out of an overfilled tube when the stopper is removed at the bench.",
   "Leakage through the tube seal during transport, which dries out the sample before it reaches the lab.",
   "Mixing of two patients' samples when the labels are printed in the same room at the same time."
  ],
  "qd": "Transfer of a small amount of blood and additive from one tube into the next tube filled, through the needle.",
  "qw": [
   "Transfer of a small amount of blood and additive from one tube into the next tube filled, through the holder's rubber sleeve.",
   "Transfer of a small amount of blood and additive from the tube stopper onto the outside of the needle hub.",
   "Transfer of a small amount of blood from the patient's arm into the tube before the vacuum begins to pull."
  ],
  "e": "Carryover happens when the needle that fills a tube touches the blood and additive already in it. Filling in the recommended order limits its effect.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What happens when EDTA carries over into a serum tube tested for potassium?",
  "d": "Potassium is falsely elevated, which can lead to a dangerous wrong result.",
  "c": 3,
  "w": [
   "Potassium is falsely lowered, which is the usual cause of false low sodium values on the report.",
   "Calcium is falsely raised, while potassium stays the same because EDTA binds only sodium.",
   "Glucose is falsely lowered, because EDTA stops glycolysis in the serum tube during spinning."
  ],
  "qd": "Potassium is falsely elevated, which can lead to a dangerous wrong result.",
  "qw": [
   "Potassium is falsely lowered, which can mask a true hyperkalemia and delay treatment for the patient.",
   "Potassium is falsely elevated only in the plasma, while the serum potassium stays within the normal range.",
   "Calcium is falsely elevated, which can make the serum look hemolyzed when the lab checks the sample."
  ],
  "e": "EDTA is rich in potassium. Carryover into a chemistry tube raises potassium and can lower calcium, which is why EDTA is filled after serum.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What happens when clot activator carries over into a light blue citrate tube?",
  "d": "PT and aPTT can be falsely shortened.",
  "c": 3,
  "w": [
   "PT and aPTT can be falsely lengthened, which mimics a clotting disorder in the patient.",
   "Hemoglobin is falsely lowered, which mimics anemia on the complete blood count report.",
   "Lactate is falsely raised, which mimics a lack of oxygen in the tissues of the patient."
  ],
  "qd": "PT and aPTT can be falsely shortened.",
  "qw": [
   "PT and aPTT can be falsely lengthened, which mimics a clotting disorder in the patient.",
   "PT can be falsely shortened, while aPTT stays the same because only the intrinsic pathway is affected.",
   "Fibrinogen can be falsely raised, which mimics an acute inflammatory response in the patient."
  ],
  "e": "Clot activator in a citrate tube speeds clotting and shortens coagulation times. This is why serum tubes are now filled after coagulation tubes.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Why must blood cultures be filled first when they are collected with other tests?",
  "d": "Bacteria from the non-sterile stoppers of other tubes can contaminate the culture bottles.",
  "c": 3,
  "w": [
   "Culture bottles must be warmed before other tubes, or the bacteria will not grow in the lab incubator.",
   "Culture bottles hold the most blood, so they must be filled first before other tubes can be used.",
   "The lab reads culture bottles first, so the other tubes can wait until the next shift begins."
  ],
  "qd": "Bacteria from the non-sterile stoppers of other tubes can contaminate the culture bottles.",
  "qw": [
   "Bacteria from the patient's skin can enter the other tubes first and then travel into the culture bottles.",
   "Bacteria from the tube holder's needle can be pushed into the culture bottles when the holder is removed.",
   "Bacteria from the non-sterile gloves of the collector can contaminate culture bottles only after the tubes are capped."
  ],
  "e": "Culture bottles must stay sterile. Filling them first prevents organisms from other tubes' stoppers from reaching the culture medium.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Which two tests are the classic transport-on-ice tests?",
  "d": "Ammonia and lactate.",
  "c": 3,
  "w": [
   "Glucose and bilirubin, both of which degrade within minutes at room temperature if not spun quickly.",
   "Hemoglobin A1c and type and screen, which must be kept cold before the blood bank can test them.",
   "Potassium and sodium, which break down if the sample is not spun in a centrifuge within an hour."
  ],
  "qd": "Ammonia and lactate, both of which change quickly at room temperature.",
  "qw": [
   "Ammonia and glucose, both of which change quickly at room temperature.",
   "Lactate and potassium, both of which change quickly at room temperature.",
   "Glucose and bilirubin, both of which change quickly at room temperature."
  ],
  "e": "Ammonia and lactate change quickly in the tube. Ammonia is placed on ice and spun within about 15 minutes; lactate uses a pre-chilled gray tube.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What additive does a lavender-top tube contain, and what is it used for?",
  "d": "K2EDTA, which binds calcium to prevent clotting, used for whole-blood hematology tests.",
  "c": 3,
  "w": [
   "Sodium citrate, which binds calcium to keep plasma liquid for coagulation studies in the lab.",
   "Lithium heparin, which blocks thrombin so the plasma can be spun right away after the draw.",
   "Silica clot activator, which speeds clotting so serum separates from the cells in the tube."
  ],
  "qd": "K2EDTA, which binds calcium to prevent clotting, used for whole-blood hematology tests.",
  "qw": [
   "K3EDTA, which binds calcium to prevent clotting, used for whole-blood hematology tests.",
   "Sodium citrate, which binds calcium to prevent clotting, used for whole-blood hematology tests.",
   "Potassium oxalate, which binds calcium to prevent clotting, used for whole-blood hematology tests."
  ],
  "e": "EDTA stops clotting by binding calcium. Lavender tubes are inverted 8 to 10 times and are used for CBC, hemoglobin A1c, and type and screen.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What does a green-top tube contain, and what is its main use?",
  "d": "Lithium heparin, with or without gel, for plasma used in many STAT chemistry tests.",
  "c": 3,
  "w": [
   "Sodium fluoride, which stops glycolysis so that glucose can be measured hours after the draw.",
   "Potassium oxalate, which binds calcium for coagulation tests such as PT and aPTT in the lab.",
   "Silica particles, which activate clotting so that serum separates cleanly from the blood cells."
  ],
  "qd": "Lithium heparin, with or without gel, for plasma used in many STAT chemistry tests.",
  "qw": [
   "Sodium heparin, with or without gel, for plasma used in many STAT chemistry tests.",
   "Lithium citrate, with or without gel, for plasma used in many STAT chemistry tests.",
   "Lithium heparin, with or without gel, for serum used in many STAT chemistry tests."
  ],
  "e": "Heparin is an anticoagulant that lets plasma be spun right away. Green tubes are inverted 8 to 10 times.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What does a gray-top tube contain, and what does it preserve?",
  "d": "Sodium fluoride and potassium oxalate, which preserve glucose and other analytes in the sample.",
  "c": 3,
  "w": [
   "Sodium citrate, which keeps platelets intact so that the lab can count them accurately later.",
   "EDTA, which prevents clotting so that whole blood can be tested for hemoglobin and hematocrit.",
   "Heparin, which blocks thrombin so that the plasma stays liquid during transport to the lab."
  ],
  "qd": "Sodium fluoride and potassium oxalate, which preserve glucose and other analytes in the sample.",
  "qw": [
   "Sodium fluoride and sodium citrate, which preserve glucose and other analytes in the sample.",
   "Potassium fluoride and potassium oxalate, which preserve glucose and other analytes in the sample.",
   "Sodium fluoride and potassium EDTA, which preserve glucose and other analytes in the sample."
  ],
  "e": "Fluoride stops glycolysis, which is why gray tubes are used for glucose, lactate, and blood alcohol. Gray tubes are drawn last.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "Which tube has no additive and does not need to be inverted?",
  "d": "The glass red-top plain tube, which clots naturally.",
  "c": 3,
  "w": [
   "The light blue citrate tube, which is filled to the line and then held still during transport.",
   "The gray glycolytic tube, which is inverted once after it has been filled to the top completely.",
   "The gold serum tube, which is inverted only after it has been spun in the laboratory centrifuge."
  ],
  "qd": "The glass red-top plain tube, which clots naturally.",
  "qw": [
   "The plastic red-top plain tube, which clots naturally.",
   "The glass red-top tube with a silica activator, which clots within five minutes.",
   "The glass red-top tube with a gel barrier, which clots naturally and separates on spinning."
  ],
  "e": "Plain red tubes rely on the glass surface to clot. The course handout notes that glass red tubes have no additive and need no inversions.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Why do serum tubes follow coagulation tubes in the current order of draw?",
  "d": "Clot activator carryover into a citrate tube can shorten PT and aPTT, so serum tubes were moved after coagulation tubes.",
  "c": 3,
  "w": [
   "Serum tubes hold the most blood and must be filled last so that the other tubes are not overfilled.",
   "Serum tubes are filled after the gray tube so that glucose can be measured before a clot forms.",
   "Gold tubes are always filled last because the gel must cool before the sample can be poured out."
  ],
  "qd": "Clot activator carryover into a citrate tube shortens PT and aPTT, so serum moved after coag tubes.",
  "qw": [
   "Clot activator carryover into a lavender tube shortens CBC counts, so serum moved after EDTA tubes.",
   "Heparin carryover into a gold tube lengthens PT and aPTT, so serum moved before coag tubes.",
   "Clot activator carryover into a citrate tube lengthens PT and aPTT, so serum moved before coag tubes."
  ],
  "e": "The order changed in 2003, when plastic tubes replaced glass. Plastic does not activate clotting, so serum carryover into a citrate tube became a risk.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "How much blood should an adult blood culture bottle receive?",
  "d": "About 8 to 10 mL per bottle, with the aerobic bottle filled first.",
  "c": 4,
  "w": [
   "About 2 mL per bottle, with the anaerobic bottle filled first to protect oxygen-sensitive germs.",
   "About 20 mL per bottle, split evenly so that each bottle receives half of the total volume.",
   "About 15 mL in the aerobic bottle only, with the anaerobic bottle left empty for the lab."
  ],
  "qd": "About 8 to 10 mL per bottle, with the aerobic bottle filled first.",
  "qw": [
   "About 8 to 10 mL per bottle, with the anaerobic bottle filled first to protect oxygen-sensitive organisms.",
   "About 4 to 5 mL per bottle, with the aerobic bottle filled first to maximize growth in the lab.",
   "About 8 to 10 mL per bottle, with the aerobic and anaerobic bottles filled at the same time."
  ],
  "e": "CDC describes about 10 mL per bottle for an adult set of aerobic and anaerobic bottles, and two or more sets totaling 40-60 mL. The course handout gives 8 to 10 mL per bottle and directs filling the aerobic bottle first.",
  "u": "https://www.cdc.gov/lab-quality/php/preventing-adult-blood-culture-contamination/collect.html",
  "s": "CDC: Collect Adult Blood Culture Sets"
 },
 {
  "t": "What is the pediatric blood culture volume guideline in the course handout?",
  "d": "1 mL of blood for every year of the child's life.",
  "c": 4,
  "w": [
   "1 mL of blood for every ten pounds of body weight, up to a maximum of 5 mL per bottle.",
   "5 mL for every child under age 12, regardless of the child's weight or exact age in years.",
   "0.5 mL per kilogram of body weight, with a maximum of 1 mL for any child under age six."
  ],
  "qd": "1 mL of blood for every year of the child's life.",
  "qw": [
   "1 mL of blood for every two years of the child's life, up to a maximum of 5 mL per bottle.",
   "1 mL of blood for every 10 pounds of body weight, up to a maximum of 5 mL per bottle.",
   "1 mL of blood for every year of the child's life, split equally between the aerobic and anaerobic bottles."
  ],
  "e": "The course handout gives 1 mL per year of the child's age. CDC's guidance is for adult sets (about 10 mL per bottle, two or more sets, 40-60 mL total). Confirm the pediatric volume in your facility's protocol.",
  "u": "https://www.cdc.gov/lab-quality/php/preventing-adult-blood-culture-contamination/collect.html",
  "s": "CDC: Collect Adult Blood Culture Sets"
 },
 {
  "t": "Why are underfilled blood culture bottles a risk?",
  "d": "Low-concentration organisms can go undetected or take longer to find, which delays antibiotic therapy.",
  "c": 4,
  "w": [
   "Underfilled bottles let air in, which kills all bacteria before the culture has a chance to grow.",
   "Underfilled bottles cause the lab to discard the sample without reading it at all, to be safe.",
   "Underfilled bottles build up pressure during incubation, which can burst the seal on the bottle."
  ],
  "qd": "Low-concentration organisms can go undetected or take longer to find, which delays antibiotic therapy.",
  "qw": [
   "Low-concentration organisms can be killed by the extra air in the bottle, which delays antibiotic therapy.",
   "Low-concentration organisms can grow faster in underfilled bottles, which produces false positives in the lab.",
   "Low-concentration organisms can settle to the bottom of the bottle, which delays antibiotic therapy in the lab."
  ],
  "e": "Septicemia can be present at very low concentrations. The handout notes that about 16 percent of unacceptable specimens are underfilled.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "How should blood tubes be labeled?",
  "d": "With two identifiers, the date, time, and collector's initials, in the patient's presence, immediately after collection.",
  "c": 4,
  "w": [
   "At the lab desk after the tubes are sent, using the requisition to fill in the details later.",
   "Once at the start of the shift with the patient's name, then reused for every draw that day.",
   "By the nurse before the draw, so the phlebotomist can focus on the venipuncture itself."
  ],
  "qd": "With two identifiers, the date, time, and initials, in the patient's presence, right after collection.",
  "qw": [
   "With two identifiers, the date, time, and initials, in the patient's presence, before rack-sorting.",
   "With two identifiers and the provider's initials, in the patient's presence, right after collection.",
   "With two identifiers, the date, time, and accession number, in the patient's presence, right after collection."
  ],
  "e": "The handout says to label every tube in the presence of the patient before leaving. Labels made away from the patient increase the risk of misidentification.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What is the purpose of centrifugation in specimen processing?",
  "d": "To separate serum or plasma from the cells so the sample is ready for testing.",
  "c": 4,
  "w": [
   "To mix the additive with the blood so that clotting is prevented inside the tube.",
   "To warm the sample to body temperature so that the enzymes in it work more accurately.",
   "To remove air bubbles and sterilize the sample before it is sent to the laboratory."
  ],
  "qd": "To separate serum or plasma from the cells so the sample is ready for testing.",
  "qw": [
   "To separate serum or plasma from the clot so the sample is ready for testing.",
   "To separate serum or plasma from the gel so the sample can be stored at room temperature.",
   "To separate plasma from the platelets so the sample can be sent for CBC testing."
  ],
  "e": "Centrifugation separates the liquid part of blood from the cells. Its speed and time must be right, because inadequate spinning leaves platelets in the serum.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "How should a specimen for ammonia be handled?",
  "d": "Placed on ice at once and spun within about 15 minutes.",
  "c": 4,
  "w": [
   "Kept at room temperature for up to two hours before it is spun in the laboratory centrifuge.",
   "Refrigerated overnight in the same tube that was used for the complete blood count.",
   "Warmed to body temperature, then spun in a centrifuge for a full hour before testing."
  ],
  "qd": "Placed on ice at once and spun within about 15 minutes.",
  "qw": [
   "Placed on ice within about 15 minutes and spun within an hour of collection.",
   "Kept at room temperature and spun within about 15 minutes, with no ice required.",
   "Placed on ice at once and spun within about 45 minutes, after the tube is inverted eight times."
  ],
  "e": "Ammonia rises quickly in the tube, so it is kept on ice and separated promptly.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is chain of custody used for?",
  "d": "A documented, unbroken record of handling a specimen, used for forensic, blood alcohol, and drug screen samples.",
  "c": 4,
  "w": [
   "A list of the tubes drawn from each patient, used to match the lab's inventory count at the end of the day.",
   "A schedule that shows which technician will pick up the specimens from each unit every morning.",
   "A form that records the patient's insurance and billing codes for each draw in the clinic."
  ],
  "qd": "A documented, unbroken record of handling a specimen, used for forensic, blood alcohol, and drug screen samples.",
  "qw": [
   "A documented record of handling a specimen, used for forensic and blood alcohol samples, but not for drug screens.",
   "A documented, unbroken record of handling a specimen, used only for forensic samples sent to outside labs.",
   "A documented record of the tubes drawn from each patient, used for drug screens and blood alcohol samples."
  ],
  "e": "Chain of custody documents each person who handles a specimen, so that the sample's integrity and identity can be shown in a legal or forensic setting.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "Why is a gray-top tube used for a glucose test?",
  "d": "Sodium fluoride stops glycolysis, so the glucose level stays accurate until the sample is spun.",
  "c": 4,
  "w": [
   "Heparin stops clotting, so the glucose can be read directly from whole blood in the tube.",
   "Potassium oxalate speeds clotting so that glucose separates into the serum layer quickly.",
   "Citrate binds glucose directly, so its level is preserved for a full day in storage."
  ],
  "qd": "Sodium fluoride stops glycolysis, so the glucose level stays accurate until the sample is spun.",
  "qw": [
   "Sodium fluoride slows clotting, so the glucose level stays accurate until the sample is spun.",
   "Sodium fluoride stops glycolysis, so the glucose level stays accurate until the sample is refrigerated.",
   "Sodium fluoride stops glycolysis only in whole blood, so the glucose level is checked after spinning."
  ],
  "e": "Blood cells keep using glucose after the draw. Fluoride slows that process, which is why gray tubes are used for glucose.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "Which tube is typically used for a complete blood count (CBC)?",
  "d": "A lavender EDTA tube, inverted 8 to 10 times, which prevents clotting.",
  "c": 4,
  "w": [
   "A gold serum tube, inverted five times, which allows the sample to clot before it is tested.",
   "A light blue citrate tube, filled to the line and inverted three to four times before testing.",
   "A green heparin tube, centrifuged within 15 minutes to separate the plasma from the cells."
  ],
  "qd": "A lavender EDTA tube, inverted 8 to 10 times, which prevents clotting.",
  "qw": [
   "A lavender EDTA tube, inverted 3 to 4 times, which prevents clotting.",
   "A pink EDTA tube, inverted 8 to 10 times, which prevents clotting in the blood bank.",
   "A lavender sodium citrate tube, inverted 8 to 10 times, which prevents clotting."
  ],
  "e": "CBC counts cells, so the sample must stay whole blood. EDTA keeps the cells intact for counting.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "Which tube is typically used for a type and screen?",
  "d": "A lavender (or pink) EDTA tube, labeled at the bedside for the blood bank.",
  "c": 4,
  "w": [
   "A gold serum tube, inverted five times, and sent to the lab without a bedside label.",
   "A light blue citrate tube, filled to the line so the blood bank can clot-test the sample.",
   "A gray tube, inverted eight times, and held on ice until the blood bank opens each morning."
  ],
  "qd": "A lavender (or pink) EDTA tube, labeled at the bedside for the blood bank.",
  "qw": [
   "A light blue citrate tube, labeled at the bedside for the blood bank.",
   "A lavender (or pink) EDTA tube, labeled at the lab desk for the blood bank.",
   "A gold serum tube, labeled at the bedside for the blood bank."
  ],
  "e": "The handout lists type and screen in the lavender or pink tube. Blood bank tubes are labeled at the bedside to prevent a transfusion error.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is hemolysis?",
  "d": "Rupture of red blood cells, which releases their contents into the serum or plasma.",
  "c": 5,
  "w": [
   "Clumping of white blood cells that forms clots and blocks the needle during the draw.",
   "Separation of the serum from the cells when a tube is left standing too long before spinning.",
   "Drying of the blood inside the tube, which thickens the sample and changes its color."
  ],
  "qd": "Rupture of red blood cells, which releases their contents into the serum or plasma.",
  "qw": [
   "Rupture of white blood cells, which releases their contents into the serum or plasma.",
   "Rupture of platelets, which releases their contents into the serum or plasma.",
   "Rupture of red blood cells, which releases their contents into the anticoagulant solution in the tube."
  ],
  "e": "Hemolysis releases hemoglobin and intracellular contents into the sample. It can falsely change many test results and often requires a redraw.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Which two analytes does the handout identify as most often falsely raised by hemolysis?",
  "d": "Potassium and magnesium.",
  "c": 5,
  "w": [
   "Glucose and creatinine, which are lowered when the red cells rupture in the sample.",
   "Sodium and chloride, which become more concentrated when the plasma is spun too quickly.",
   "Calcium and albumin, which bind to the free hemoglobin that is released by the cells."
  ],
  "qd": "Potassium and magnesium, which red cells contain in high concentration.",
  "qw": [
   "Calcium and chloride, which red cells contain in high concentration.",
   "Sodium and bicarbonate, which red cells contain in high concentration.",
   "Glucose and magnesium, which red cells contain in high concentration."
  ],
  "e": "Red cells contain much more potassium and magnesium than plasma. Hemolysis releases these into the sample and raises the reported values.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "Which collection practice is most likely to hemolyze a sample?",
  "d": "Drawing through a needle that is too small, or pulling too hard on a syringe plunger.",
  "c": 5,
  "w": [
   "Letting the tube sit at room temperature for thirty minutes before it is spun in the centrifuge.",
   "Inverting an additive tube the correct number of times after it has been filled completely.",
   "Keeping the tourniquet on for less than one minute during the entire draw and release."
  ],
  "qd": "Drawing through a needle that is too small, or pulling too hard on a syringe plunger.",
  "qw": [
   "Drawing through a needle that is too large for the vein, or letting the tube stand for twenty minutes before inverting.",
   "Drawing through a needle of the correct gauge, but pulling the plunger slowly to avoid any suction at all.",
   "Drawing through a 21-gauge needle in a patient with normal veins, or inverting the tube too gently for the additive."
  ],
  "e": "Excessive suction and narrow needles damage red cells. The handout lists rough handling and vigorous mixing among the causes.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Why should a line draw from an IV usually be avoided?",
  "d": "Hemolysis is more likely, and IV fluid can dilute the sample and change the results.",
  "c": 5,
  "w": [
   "IV lines are not sterile enough for culture collection, so the lab cannot use any sample taken from them.",
   "IV lines are too slow to fill a tube, so the sample starts to clot before the draw is complete.",
   "IV lines use a needle gauge that the lab cannot read from the requisition, so results are delayed."
  ],
  "qd": "Hemolysis is more likely, and IV fluid can dilute the sample and change the results.",
  "qw": [
   "Hemolysis is less likely, but IV fluid can clot the sample and change the results.",
   "Hemolysis is more likely, but IV fluid only affects results for patients taking heparin.",
   "Hemolysis is more likely, and IV fluid can raise the pH of the sample, changing the results."
  ],
  "e": "The handout notes that IV devices are notorious for hemolyzing red cells. A venipuncture is preferred unless a specific device is in use.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Why should clots not be rimmed into a tube?",
  "d": "Forcing clot into the tube removes fibrin and ruptures red cells, which hemolyzes the sample.",
  "c": 5,
  "w": [
   "Clots left in the tube are read by the lab as platelet counts, which must be recorded separately.",
   "Rimmed clots absorb the additive, so the tube has too little anticoagulant to prevent clotting.",
   "Rimmed clots raise the temperature of the tube, which changes glucose results during testing."
  ],
  "qd": "Forcing clot into the tube removes fibrin and ruptures red cells, which hemolyzes the sample.",
  "qw": [
   "Forcing clot into the tube adds fibrin, which thickens the sample and raises the reported hematocrit.",
   "Forcing clot into the tube removes platelets, which prevents the sample from being used for coagulation.",
   "Forcing clot into the tube removes fibrin, which only affects the glucose result and not the hemolysis index."
  ],
  "e": "Rimming removes fibrin and tears red cells. Clotted specimens are rejected or redrawn, so the clot should not be pushed into the tube.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "What effect does spinning tubes with stoppers off have on potassium?",
  "d": "Potassium can increase by about 135 percent.",
  "c": 5,
  "w": [
   "Potassium falls by about half, because gas escapes and reduces the volume of the sample.",
   "Potassium is unchanged, since the stopper only affects the glucose and calcium levels.",
   "Potassium rises only slightly, by about five percent, which is within the normal range."
  ],
  "qd": "Potassium can increase by about 135 percent.",
  "qw": [
   "Potassium can increase by about 35 percent.",
   "Potassium can increase by about 13.5 percent.",
   "Potassium can decrease by about 135 percent."
  ],
  "e": "CDC's NHANES electrolyte manual confirms that potassium leaks from red cells into the serum and falsely raises results when serum stays on the cells. The 135 percent figure is from the course handout, which cites Young's Effects of Preanalytical Variables on Clinical Laboratory Tests.",
  "u": "https://wwwn.cdc.gov/nchs/data/nhanes/public/2013/labmethods/urlt_h_r_met_electrolytes.pdf",
  "s": "CDC NHANES: Sodium, Potassium, Chloride Lab Manual"
 },
 {
  "t": "When is it acceptable to refrigerate a blood sample that will be tested for potassium?",
  "d": "Only after the serum or plasma has been separated from contact with the cells.",
  "c": 5,
  "w": [
   "Immediately after the draw, because cold slows all potassium movement out of the red cells.",
   "Any time before centrifugation, since chilling stops the red cells from leaking potassium.",
   "Only if the tube is kept upright, with the stopper removed to release any built-up gas pressure."
  ],
  "qd": "Only after the serum or plasma has been separated from contact with the cells.",
  "qw": [
   "Only after the sample has been spun for a full five minutes with the stopper removed.",
   "Only after the tube has been inverted and held upright at room temperature for ten minutes.",
   "Only after the cells have been discarded and the remaining serum has been transferred to a new tube."
  ],
  "e": "Refrigeration slows potassium leakage only once the cells are separated from the serum or plasma. Unseparated blood should not be chilled for potassium.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is the effect of recentrifuging a gel tube?",
  "d": "Potassium can increase by about 47 percent.",
  "c": 5,
  "w": [
   "Potassium drops, because the gel absorbs most of the potassium before the second spin begins.",
   "Glucose rises by about 47 percent, because the gel releases sugar stored inside the cells.",
   "Sodium rises by about 47 percent, but potassium is not affected by a second spin of the tube."
  ],
  "qd": "Potassium can increase by about 47 percent.",
  "qw": [
   "Potassium can increase by about 74 percent.",
   "Potassium can increase by about 4.7 percent.",
   "Potassium can decrease by about 47 percent."
  ],
  "e": "A second spin can release potassium from cells that remain in contact with the serum. This is one of the handout's six preanalytical causes of false potassium.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is the risk of delayed centrifugation?",
  "d": "Red cells keep leaking potassium into the serum, so potassium reads falsely high within two hours.",
  "c": 5,
  "w": [
   "The serum separates too well, so the sample is rejected as having too little plasma for the test.",
   "Glucose rises because the gel dissolves and releases sugar into the sample during the delay.",
   "Platelets clot in the tube, so the sample is rejected for coagulation testing by the laboratory."
  ],
  "qd": "Red cells keep leaking potassium into the serum, so potassium reads falsely high within two hours.",
  "qw": [
   "Red cells keep leaking glucose into the serum, so glucose reads falsely high within two hours.",
   "Red cells keep leaking potassium into the serum, so potassium reads falsely high only after twelve hours.",
   "Red cells keep absorbing potassium from the serum, so potassium reads falsely low within two hours."
  ],
  "e": "Potassium continues to move out of the cells while the sample stands. Prompt separation prevents this shift.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What does fist pumping during a draw do to potassium?",
  "d": "It can raise the potassium level by up to 20 percent.",
  "c": 5,
  "w": [
   "It lowers potassium by about 20 percent, since muscle activity uses up the mineral in the blood.",
   "It has no effect on potassium, but it can change the chloride level slightly in the sample.",
   "It raises potassium only in patients who are already taking potassium supplements or diuretics."
  ],
  "qd": "It can raise the potassium level by up to 20 percent.",
  "qw": [
   "It can raise the potassium level by up to 2 percent.",
   "It can lower the potassium level by up to 20 percent.",
   "It can raise the sodium level by up to 20 percent."
  ],
  "e": "Fist pumping pushes potassium out of muscle into the blood at the site of the draw. The handout cites this as a cause of false potassium elevation.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is the effect of excessive pulling pressure on a syringe?",
  "d": "It can rupture red cells, which hemolyzes the specimen.",
  "c": 5,
  "w": [
   "It makes the blood clot faster by pulling platelets in from the wall of the vein during the draw.",
   "It makes the serum look clearer, which can hide lipemia from the lab on the final report.",
   "It increases the hematocrit, which the lab corrects automatically during the testing process."
  ],
  "qd": "It can rupture red cells, which hemolyzes the specimen.",
  "qw": [
   "It can rupture platelets, which prevents the specimen from being used for coagulation.",
   "It can rupture white cells, which releases enzymes that falsely raise the lipase result.",
   "It can rupture red cells, which only affects glucose and not the hemolysis index."
  ],
  "e": "Hard pulling on a syringe creates suction that damages red cells. Gentle, steady pressure keeps the sample intact.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Why must tubes be filled fully?",
  "d": "Too much anticoagulant for the blood volume damages red cell membranes and can give erroneous results.",
  "c": 5,
  "w": [
   "Full tubes spin faster in the centrifuge, which helps platelets separate more cleanly from the plasma.",
   "Full tubes hold more air, which keeps the sample from freezing during transport to the lab.",
   "Full tubes are easier to label, since the barcode sits on the fullest part of the tube body."
  ],
  "qd": "Too much anticoagulant for the blood volume damages red cell membranes and can give erroneous results.",
  "qw": [
   "Too little anticoagulant for the blood volume allows clot formation and can give erroneous results.",
   "Too much anticoagulant for the blood volume thickens the plasma and slows the analyzer's sampling.",
   "Too much blood volume for the anticoagulant damages white cell membranes and can give erroneous results."
  ],
  "e": "The handout notes that an excessive concentration of anticoagulant in an underfilled tube is hard on fragile red cell membranes. Fill each tube to its line.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "What should you do if a patient faints during or after a draw?",
  "d": "Stop the draw, remove the needle with the safety device activated, and lower the patient to a safe position.",
  "c": 6,
  "w": [
   "Keep the needle in place and continue drawing, since the vein refills before the next tube is needed.",
   "Give the patient a glass of water and ask them to stand up to reset their circulation quickly.",
   "Call the lab and ask whether the tubes already filled can still be processed before the patient wakes."
  ],
  "qd": "Stop the draw, remove the needle with the safety device activated, and lower the patient to a safe position.",
  "qw": [
   "Stop the draw, leave the needle in place, and raise the patient's legs above the heart to restore circulation.",
   "Stop the draw, remove the needle, and have the patient sit upright with the head between the knees immediately.",
   "Stop the draw, remove the needle without activating the device, and call the lab for instructions on the tubes."
  ],
  "e": "Syncope is a vasovagal response triggered by emotional or physical stress. Immediate patient care takes priority over any tubes already drawn.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "What is the correct response to a hematoma at the puncture site?",
  "d": "Remove the needle, apply firm pressure, and do not reattempt a draw in the same vein.",
  "c": 5,
  "w": [
   "Massage the area firmly to spread the blood out, then draw from the same vein right away.",
   "Apply a warm compress and draw from the other arm, but leave the first site uncovered.",
   "Wait ten minutes for the swelling to settle, then reinsert the needle at the same site."
  ],
  "qd": "Remove the needle, apply firm pressure, and do not reattempt a draw in the same vein.",
  "qw": [
   "Remove the needle, apply a cold pack, and reattempt the draw in the same vein after ten minutes of rest.",
   "Remove the needle, apply firm pressure, and reattempt in the same vein only if the bleeding has stopped.",
   "Leave the needle in, apply firm pressure, and reattempt in the same vein after the bleeding slows."
  ],
  "e": "A hematoma is a collection of blood under the skin from a leaking vein. It requires stopping the draw and pressure, and a new site should be chosen.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "What should you do if the patient reports shooting or electric-like pain during a draw?",
  "d": "Stop immediately and remove the needle, since nerve injury can be permanent.",
  "c": 0,
  "w": [
   "Push the needle a little deeper to reach the vein, since pain usually means a vein is close by.",
   "Keep drawing quickly to finish before the pain increases in intensity during the procedure.",
   "Ask the patient to hold still while you adjust the needle angle slightly and continue the draw."
  ],
  "qd": "Stop immediately and remove the needle, since nerve injury can be permanent.",
  "qw": [
   "Stop immediately and reposition the needle slightly, since nerve contact can resolve without further treatment.",
   "Stop only if the pain continues after one minute, then remove the needle and apply a cold pack.",
   "Stop immediately and leave the needle in while the patient is evaluated, since removal can injure the nerve."
  ],
  "e": "Shooting pain suggests the needle is touching a nerve. Continuing risks complex regional pain syndrome, so the needle must be removed.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "How can you tell that a needle has entered an artery instead of a vein?",
  "d": "The blood is bright red, pulses or spurts, and flows faster than venous blood.",
  "c": 2,
  "w": [
   "The blood is dark red, flows slowly, and fills the tube evenly without any pulsing at all.",
   "The blood is pale pink with bubbles, and the tube fills only halfway before the flow stops.",
   "The blood is brown and thick, and the needle clogs as soon as the tube is attached to the holder."
  ],
  "qd": "The blood is bright red, pulses or spurts, and flows faster than venous blood.",
  "qw": [
   "The blood is bright red, but flows steadily without pulsing and fills the tube more slowly than venous blood.",
   "The blood is dark red and pulses, but flows slowly and fills the tube with visible air bubbles.",
   "The blood is bright red and pulses, but flows only when the tourniquet is released, not during the draw."
  ],
  "e": "Arterial blood is bright red and pulsates. If an artery is punctured, pressure must be applied for several minutes and the draw should be reported.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Which federal rule governs the privacy of patient information, including identification details, during collection and testing?",
  "d": "The HIPAA Privacy Rule, which limits how protected health information is used and shared.",
  "c": 6,
  "w": [
   "The Clean Air Act, which governs air exchange and filtration in patient rooms and laboratories.",
   "The Food, Drug, and Cosmetic Act, which regulates the labeling of medicines and medical devices.",
   "The Medicare Conditions of Participation, which set staffing limits for nurses and phlebotomists."
  ],
  "qd": "The HIPAA Privacy Rule, which limits how protected health information is used and shared.",
  "qw": [
   "The HIPAA Security Rule, which limits how protected health information is stored and transmitted electronically.",
   "The HIPAA Breach Notification Rule, which requires reporting of lost or stolen protected health information.",
   "The HIPAA Transactions Rule, which standardizes electronic billing and claim formats for healthcare providers."
  ],
  "e": "The HIPAA Privacy Rule protects identifiable patient information. Collectors handle this information during identification, labeling, and requisitions.",
  "u": "https://www.hhs.gov/hipaa/for-professionals/privacy/index.html",
  "s": "HHS: HIPAA Privacy"
 },
 {
  "t": "What is the most common source of preanalytical errors that the lab cannot correct?",
  "d": "Mislabeling or drawing the wrong patient, since the lab tests whatever sample it receives.",
  "c": 6,
  "w": [
   "Using a room that is too warm, which causes the sample to spoil before it reaches the laboratory.",
   "Pausing too long between tubes, which lets the first tube clot inside the holder before it fills.",
   "Using the wrong color of tourniquet, which can change how the veins look during the draw."
  ],
  "qd": "Mislabeling or drawing the wrong patient, since the lab tests whatever sample it receives.",
  "qw": [
   "Hemolysis during the draw, since the lab cannot detect a damaged sample once it is labeled correctly.",
   "Underfilling of tubes, since the lab cannot detect a low volume once the tube is labeled correctly.",
   "Delayed transport to the lab, since the lab cannot detect elapsed time once the sample is labeled correctly."
  ],
  "e": "The lab can detect some problems, but it cannot know whether a sample came from the right patient. Identification at collection prevents these errors.",
  "u": "https://www.ahrq.gov/patient-safety/index.html",
  "s": "AHRQ: Patient Safety"
 },
 {
  "t": "Which response best supports ethical practice after a phlebotomy error?",
  "d": "Report the error, document it, and cooperate with a root-cause review.",
  "c": 6,
  "w": [
   "Discard the sample quietly and redraw, so the error does not appear on any record kept by the facility.",
   "Tell the patient the error was a lab problem, so that the phlebotomist is not held responsible.",
   "Wait until the next shift and mention the error only if the patient asks about it later."
  ],
  "qd": "Report the error, document it, and cooperate with a root-cause review.",
  "qw": [
   "Report the error to the supervisor verbally, and document it only if a patient complains about the result.",
   "Report the error, correct the record, and cooperate with a review that is limited to the individual's own errors.",
   "Report the error after the patient has been discharged, and cooperate with a review limited to the lab's records."
  ],
  "e": "The handout describes root-cause analysis and facility-wide training after errors. Honest reporting protects patients and the collector.",
  "u": "https://www.ahrq.gov/patient-safety/index.html",
  "s": "AHRQ: Patient Safety"
 },
 {
  "t": "Which code of conduct does the course handout identify for ethical standards in phlebotomy?",
  "d": "The NHA code of ethics for certified phlebotomy technicians.",
  "c": 6,
  "w": [
   "The AMA code of medical ethics, which governs all physicians in outpatient and hospital settings.",
   "The hospital visitor policy, which sets the rules for family members in patient rooms.",
   "The state nursing practice act, which governs all clinical staff who draw blood on the unit."
  ],
  "qd": "The NHA code of ethics for certified phlebotomy technicians.",
  "qw": [
   "The NHA code of ethics for certified medical assistants, which covers phlebotomy as one of many duties.",
   "The NHA code of conduct for certified phlebotomy technicians, which covers only the lab's billing practices.",
   "The AMA code of ethics for certified phlebotomy technicians, which governs all healthcare employees."
  ],
  "e": "The handout lists the NHA code of ethics as the standard applicable to phlebotomy practice. The NHA certifies phlebotomy technicians.",
  "u": "https://www.nhanow.com/certifications/ccma",
  "s": "NHA: Certifications"
 },
 {
  "t": "What are the first steps of a venipuncture that the handout lists as essential?",
  "d": "Review the requisition for tests, timing, fasting, and special handling, then assemble the supplies.",
  "c": 1,
  "w": [
   "Lay out the tubes in the rack by color, then ask the patient to choose the arm for the draw.",
   "Put on gloves and apply the tourniquet, then check the requisition after the first tube is filled.",
   "Clean the site with alcohol, then check the patient's name against the wristband and the chart."
  ],
  "qd": "Review the requisition for tests, timing, fasting, and special handling, then assemble the supplies.",
  "qw": [
   "Review the requisition for the ordering physician's name, then confirm the patient's insurance before assembling the supplies.",
   "Assemble the supplies, then review the requisition for tests, timing, fasting, and special handling.",
   "Review the requisition for the test priority only, then assemble the supplies and greet the patient."
  ],
  "e": "The first step in the venipuncture checklist is reviewing the requisition and assembling supplies before the patient is approached.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "Which federal standard governs occupational exposure to bloodborne pathogens?",
  "d": "OSHA's Bloodborne Pathogens Standard, 29 CFR 1910.1030.",
  "c": 0,
  "w": [
   "OSHA's Hazard Communication Standard, 29 CFR 1910.1200, which governs chemical labels and safety data sheets.",
   "OSHA's Respiratory Protection Standard, 29 CFR 1910.134, which governs fit testing for N95 respirators.",
   "The CLIA regulations, 42 CFR Part 493, which govern laboratory test certification and quality control."
  ],
  "qd": "OSHA's Bloodborne Pathogens Standard, 29 CFR 1910.1030.",
  "qw": [
   "OSHA's Hazard Communication Standard, 29 CFR 1910.1200, which governs chemical labels and safety data sheets.",
   "OSHA's Respiratory Protection Standard, 29 CFR 1910.134, which governs fit testing for N95 respirators.",
   "The CLIA regulations, 42 CFR Part 493, which govern laboratory test certification and quality control."
  ],
  "e": "The bloodborne pathogens standard sets exposure control, PPE, engineering controls, labeling, training, and hepatitis B vaccination duties.",
  "u": "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030",
  "s": "OSHA: Bloodborne Pathogens Standard 1910.1030"
 },
 {
  "t": "What must an employer's exposure control plan include about sharps devices?",
  "d": "A review each year of safer medical devices, with the plan updated to reflect technology that reduces exposure.",
  "c": 0,
  "w": [
   "A single sharps device approved for the whole facility, reviewed only when the vendor contract ends.",
   "A list of syringes with fixed needles that staff use for every draw, to limit device changes per patient.",
   "A glove brand chosen by the infection control committee, reviewed every five years by the facility board."
  ],
  "qd": "A review each year of safer medical devices, with the plan updated to reflect technology that reduces exposure.",
  "qw": [
   "A single sharps device approved for the whole facility, reviewed only when the vendor contract ends.",
   "A list of syringes with fixed needles that staff use for every draw, to limit device changes per patient.",
   "A glove brand chosen by the infection control committee, reviewed every five years by the facility board."
  ],
  "e": "The Needlestick Safety and Prevention Act amended the standard so that employers must consider and document safer devices each year.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "Who must be offered the hepatitis B vaccine, and when?",
  "d": "Employees with occupational exposure risk, offered at no cost within 10 days of initial assignment, unless exceptions apply.",
  "c": 0,
  "w": [
   "Only employees who request it in writing, offered after one year of employment at the facility.",
   "All patients who have blood drawn at the facility, offered before their first venipuncture each year.",
   "Only supervisors and charge staff, offered at the employee's own expense before starting work."
  ],
  "qd": "Employees with occupational risk, offered at no cost within 10 days of assignment, unless exceptions apply.",
  "qw": [
   "Employees who request it in writing, offered after one year of employment at the facility.",
   "All patients who have blood drawn at the facility, offered before their first draw each year.",
   "Supervisors and charge staff only, offered at the employee's own expense before starting work."
  ],
  "e": "OSHA requires the series to be offered at no cost to exposed workers, with exceptions for prior vaccination, documented immunity, or contraindication.",
  "u": "https://www.osha.gov/bloodborne-pathogens/general",
  "s": "OSHA: Bloodborne Pathogens General Guidance"
 },
 {
  "t": "Which precaution category applies to pathogens spread by large respiratory droplets?",
  "d": "Droplet precautions, which use a surgical mask and eye protection for close contact with the patient.",
  "c": 0,
  "w": [
   "Airborne precautions, which require an N95 respirator and a negative-pressure room for every patient visit.",
   "Contact precautions, which require a gown and gloves only for patients with a rash or an open wound.",
   "Standard precautions only, since droplet spread is fully covered by hand hygiene alone in every setting."
  ],
  "qd": "Droplet precautions, which use a surgical mask and eye protection for close contact with the patient.",
  "qw": [
   "Airborne precautions, which require an N95 respirator and a negative-pressure room for every patient visit.",
   "Contact precautions, which require a gown and gloves only for patients with a rash or an open wound.",
   "Standard precautions only, since droplet spread is fully covered by hand hygiene alone in every setting."
  ],
  "e": "CDC's isolation precautions define droplet precautions for pathogens transmitted by droplets over short distances.",
  "u": "https://www.cdc.gov/infection-control/hcp/isolation-precautions/index.html",
  "s": "CDC: Isolation Precautions"
 },
 {
  "t": "What is the purpose of an eyewash station in a blood collection area?",
  "d": "Immediate flushing of the eyes after a splash of blood or chemicals, as the facility's exposure control protocol requires.",
  "c": 0,
  "w": [
   "Cleaning the phlebotomy chair and armrest after each patient to prevent cross-contamination between draws.",
   "Cooling the centrifuge after long runs so that samples are not heated during the spin cycle.",
   "Washing reusable tourniquets, which must be rinsed in running water after every single draw."
  ],
  "qd": "Immediate eye flushing after a splash of blood or chemicals, as the exposure protocol requires.",
  "qw": [
   "Cleaning the phlebotomy chair and armrest after each patient to prevent cross-contamination.",
   "Cooling the centrifuge after long runs so that samples are not heated during the spin cycle.",
   "Washing reusable tourniquets, which must be rinsed in running water after every draw."
  ],
  "e": "Eye and body wash equipment must be available near hazards so that exposed areas can be flushed right away.",
  "u": "https://www.osha.gov/bloodborne-pathogens/standards",
  "s": "OSHA: Bloodborne Pathogens Standards"
 },
 {
  "t": "Which personal protective equipment protects the eyes and face during a collection?",
  "d": "Goggles or a face shield, used with a mask when splashes are likely.",
  "c": 0,
  "w": [
   "Safety glasses with side shields only, which are sufficient for every collection in all settings.",
   "A hair net and shoe covers, which protect the collection area from contamination by staff.",
   "Ear plugs and a cap, which prevent blood from entering the ears during a difficult draw."
  ],
  "qd": "Goggles or a face shield, used with a mask when splashes are likely.",
  "qw": [
   "Safety glasses with side shields only, which are sufficient for every collection in all settings.",
   "A hair net and shoe covers, which protect the collection area from contamination by staff.",
   "Ear plugs and a cap, which prevent blood from entering the ears during a difficult draw."
  ],
  "e": "OSHA's PPE guidance requires eye and face protection where splashes of blood or other material are possible.",
  "u": "https://www.osha.gov/personal-protective-equipment",
  "s": "OSHA: Personal Protective Equipment"
 },
 {
  "t": "What is the first step when a blood spill occurs in the collection area?",
  "d": "Alert others, restrict access, and clean with an EPA-registered disinfectant while wearing gloves, following the facility's spill procedure.",
  "c": 0,
  "w": [
   "Wipe the spill with a dry paper towel and return the area to use once the floor appears dry.",
   "Cover the spill with sterile gauze and wait until the end of the shift for the cleaning crew.",
   "Dilute the spill with water and mop it up using the same cloth for every surface in the room."
  ],
  "qd": "Alert others, restrict access, and clean with an EPA-registered disinfectant while wearing gloves.",
  "qw": [
   "Wipe the spill with a dry paper towel and reuse the area once the floor looks dry.",
   "Cover the spill with sterile gauze and wait until the end of the shift for cleanup.",
   "Dilute the spill with water and mop it with the same cloth across every surface."
  ],
  "e": "Blood spills must be contained and disinfected using approved products, with protective equipment used during cleanup.",
  "u": "https://www.cdc.gov/infection-control/hcp/index.html",
  "s": "CDC: Infection Control in Healthcare Settings"
 },
 {
  "t": "How must regulated medical waste from blood collection be contained?",
  "d": "In red biohazard bags or sharps containers labeled with the biohazard symbol, disposed of by state and facility rules.",
  "c": 0,
  "w": [
   "In clear plastic bags with the patient's name written on the outside for easy tracking by staff.",
   "In the break room refrigerator until the weekly pickup by the housekeeping staff.",
   "In the regular trash after the bag is sealed with tape at the end of the shift."
  ],
  "qd": "In red biohazard bags or sharps containers labeled with the biohazard symbol.",
  "qw": [
   "In clear bags with the patient's name written on the outside for easy tracking.",
   "In the break room refrigerator until the weekly pickup by housekeeping staff.",
   "In regular trash, after the bag is sealed with tape at the end of the shift."
  ],
  "e": "The bloodborne pathogens standard requires labeling or color coding of regulated waste and containers.",
  "u": "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030",
  "s": "OSHA: Bloodborne Pathogens Standard 1910.1030"
 },
 {
  "t": "Why is a temperature log kept for a specimen refrigerator?",
  "d": "To show that storage stayed within the required range, with corrective action recorded when it did not.",
  "c": 0,
  "w": [
   "To track how often staff open the door, which is billed to the patient as a storage fee.",
   "To show the refrigerator is cleaned monthly with bleach, with no temperature record required.",
   "To record the outside weather, which affects the cooling efficiency of the refrigerator motor."
  ],
  "qd": "To show that storage stayed within the required range, with corrective action recorded when it did not.",
  "qw": [
   "To track how often staff open the door, which is billed to the patient as a storage fee.",
   "To show the refrigerator is cleaned monthly with bleach, with no temperature record required.",
   "To record the outside weather, which affects the cooling efficiency of the refrigerator motor."
  ],
  "e": "Quality control for laboratory equipment includes checking and recording storage temperatures.",
  "u": "https://www.cms.gov/files/document/cms-clia-laboratory-quick-start-guide-remediated.pdf",
  "s": "CMS: CLIA Laboratory Quick Start Guide"
 },
 {
  "t": "What is the purpose of quality control checks on a point-of-care glucose meter?",
  "d": "To confirm that the meter and test strips give accurate results before patient results are reported.",
  "c": 0,
  "w": [
   "To extend battery life by reducing how often the meter is turned on during a shift.",
   "To reduce the cost of test strips by limiting how many strips each staff member may use.",
   "To change the reference range used for the patient's glucose result printed on the report."
  ],
  "qd": "To confirm that the meter and test strips give accurate results before patient results are reported.",
  "qw": [
   "To extend battery life by reducing how often the meter is turned on during a shift.",
   "To reduce the cost of test strips by limiting how many strips each staff member may use.",
   "To change the reference range used for the patient's glucose result printed on the report."
  ],
  "e": "Point-of-care tests under CLIA require quality control to be run and documented.",
  "u": "https://www.cms.gov/files/document/cms-clia-laboratory-quick-start-guide-remediated.pdf",
  "s": "CMS: CLIA Laboratory Quick Start Guide"
 },
 {
  "t": "Which CLIA test category has the lowest complexity?",
  "d": "Waived tests, which are simple and carry a low risk of an incorrect result.",
  "c": 0,
  "w": [
   "High-complexity tests, which are performed only in hospital laboratories with a pathologist on staff.",
   "Moderate-complexity tests, which require a supervisor to review every result before reporting.",
   "Provider-performed microscopy tests, which require a pathologist to read each slide personally."
  ],
  "qd": "Waived tests, which are simple and carry a low risk of an incorrect result.",
  "qw": [
   "High-complexity tests, which are performed only in hospital laboratories with a pathologist on staff.",
   "Moderate-complexity tests, which require a supervisor to review every result before reporting.",
   "Provider-performed microscopy tests, which require a pathologist to read each slide personally."
  ],
  "e": "CLIA sorts tests into waived, moderate, and high complexity. The FDA assigns each test to a category.",
  "u": "https://www.cms.gov/files/document/cms-clia-laboratory-quick-start-guide-remediated.pdf",
  "s": "CMS: CLIA Laboratory Quick Start Guide"
 },
 {
  "t": "Which agency issues the CLIA Certificate of Waiver?",
  "d": "The Centers for Medicare and Medicaid Services (CMS).",
  "c": 0,
  "w": [
   "The Food and Drug Administration, which issues the certificate after each device is cleared.",
   "The Occupational Safety and Health Administration, which issues it after a safety inspection.",
   "The National Healthcareer Association, which issues it to certified phlebotomy technicians."
  ],
  "qd": "The Centers for Medicare and Medicaid Services (CMS).",
  "qw": [
   "The Food and Drug Administration, which issues the certificate after each device is cleared.",
   "The Occupational Safety and Health Administration, which issues it after a safety inspection.",
   "The National Healthcareer Association, which issues it to certified phlebotomy technicians."
  ],
  "e": "CMS administers CLIA. Sites that perform only waived tests need a Certificate of Waiver before testing patient samples.",
  "u": "https://www.cms.gov/files/document/cms-clia-laboratory-quick-start-guide-remediated.pdf",
  "s": "CMS: CLIA Laboratory Quick Start Guide"
 },
 {
  "t": "What does a Certificate of Waiver allow a site to do?",
  "d": "Perform only CLIA-waived tests, following the manufacturer's instructions.",
  "c": 0,
  "w": [
   "Perform any moderate-complexity test if a physician is on site at the time of testing.",
   "Perform high-complexity tests in a satellite lab located within a mile of the main hospital.",
   "Perform microbiology cultures of any kind, provided the results are reported within one day."
  ],
  "qd": "Perform only CLIA-waived tests, following the manufacturer's instructions.",
  "qw": [
   "Perform any moderate-complexity test if a physician is on site at the time of testing.",
   "Perform high-complexity tests in a satellite lab located within a mile of the main hospital.",
   "Perform microbiology cultures of any kind, provided the results are reported within one day."
  ],
  "e": "Waived testing sites have limited obligations, including fees, renewal, and following manufacturer instructions.",
  "u": "https://www.cms.gov/files/document/cms-clia-laboratory-quick-start-guide-remediated.pdf",
  "s": "CMS: CLIA Laboratory Quick Start Guide"
 },
 {
  "t": "Where is the authoritative list of CLIA-waived tests found?",
  "d": "The FDA's Currently Waived Analytes list.",
  "c": 0,
  "w": [
   "The NHA study guide appendix, which is updated each year with the latest test categories.",
   "The hospital formulary of approved drugs, which lists the tests that can be done at the bedside.",
   "The CDC list of notifiable diseases, which includes all waived tests grouped by category."
  ],
  "qd": "The FDA's Currently Waived Analytes list.",
  "qw": [
   "The NHA study guide appendix, which is updated each year with the latest test categories.",
   "The hospital formulary of approved drugs, which lists the tests that can be done at the bedside.",
   "The CDC list of notifiable diseases, which includes all waived tests grouped by category."
  ],
  "e": "The FDA list identifies waived analytes. A modified test loses its waived status and cannot be run under the certificate.",
  "u": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfclia/analyteswaived.cfm",
  "s": "FDA: Currently Waived Analytes"
 },
 {
  "t": "Which of these is an example of CLIA-waived testing?",
  "d": "Certain glucose tests, fecal occult blood tests, and some pregnancy and urine tests.",
  "c": 0,
  "w": [
   "Blood cultures, bone marrow biopsies, and the full cytogenetic panel ordered for each patient.",
   "Electrolyte panels run on the main chemistry analyzer each morning under a supervisor's review.",
   "Surgical pathology slides read by a pathologist and reported only after the case conference."
  ],
  "qd": "Certain glucose tests, fecal occult blood tests, and some pregnancy and urine tests.",
  "qw": [
   "Blood cultures, bone marrow biopsies, and the full cytogenetic panel ordered for each patient.",
   "Electrolyte panels run on the main chemistry analyzer each morning under a supervisor's review.",
   "Surgical pathology slides read by a pathologist and reported only after the case conference."
  ],
  "e": "Waived categories include some glucose, cholesterol, fecal occult blood, pregnancy, and urine tests. Check the FDA list for current analytes.",
  "u": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfclia/analyteswaived.cfm",
  "s": "FDA: Currently Waived Analytes"
 },
 {
  "t": "What should a phlebotomist do before handling an exposure incident?",
  "d": "Wash the area, report the exposure right away, and begin the post-exposure evaluation as the facility protocol requires.",
  "c": 0,
  "w": [
   "Finish the draw and report the incident at the end of the shift with the other notes.",
   "Apply an antiseptic and return to work, since minor exposures rarely need follow-up care.",
   "Ask the patient for their test history before any report is made to a supervisor."
  ],
  "qd": "Wash the area, report the exposure right away, and begin the post-exposure evaluation.",
  "qw": [
   "Finish the draw and report the exposure at the end of the shift with other notes.",
   "Apply antiseptic and return to work, since minor exposures rarely need follow-up.",
   "Ask the patient for their test history before any report is made to a supervisor."
  ],
  "e": "A documented post-exposure evaluation and follow-up is required. Prompt reporting allows prophylaxis to be started in time.",
  "u": "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
  "s": "OSHA: Evaluating and Controlling Exposure"
 },
 {
  "t": "What is the recommended timing for hepatitis B post-exposure prophylaxis?",
  "d": "As soon as possible after exposure, ideally within 24 hours.",
  "c": 0,
  "w": [
   "Within 30 days, after the source patient's test results become available to the lab.",
   "Only after symptoms appear in the weeks following the needlestick.",
   "After the end of the shift, once the incident report has been completed and signed."
  ],
  "qd": "As soon as possible after exposure, ideally within 24 hours.",
  "qw": [
   "Within 30 days, after the source patient's test results become available to the lab.",
   "Only after symptoms appear in the weeks following the needlestick.",
   "After the end of the shift, once the incident report has been completed and signed."
  ],
  "e": "CDC guidance says hepatitis B immune globulin and vaccine decisions depend on the source's HBsAg status, and that care is most effective when started promptly.",
  "u": "https://www.cdc.gov/hepatitis/hcp/populations-settings/health-care-providers.html",
  "s": "CDC: Viral Hepatitis Health Care Providers"
 },
 {
  "t": "Which sharps injury record does OSHA require employers to keep?",
  "d": "A sharps injury log that records each injury, the device involved, and the circumstances.",
  "c": 0,
  "w": [
   "A payroll log of overtime hours worked on the shift when the injury occurred.",
   "A patient log of blood types for each needlestick, so the lab can match donors.",
   "A daily count of tubes filled by each phlebotomist to compare productivity across staff."
  ],
  "qd": "A sharps injury log that records each injury, the device involved, and the circumstances.",
  "qw": [
   "A payroll log of overtime hours worked on the shift when the injury occurred.",
   "A patient log of blood types for each needlestick, so the lab can match donors.",
   "A daily count of tubes filled by each phlebotomist to compare productivity across staff."
  ],
  "e": "The standard requires a sharps injury log, which the employer uses to evaluate and select safer devices.",
  "u": "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030",
  "s": "OSHA: Bloodborne Pathogens Standard 1910.1030"
 },
 {
  "t": "What information must a requisition form include?",
  "d": "Patient demographics, physician information, diagnosis code, tests ordered, and test priority.",
  "c": 1,
  "w": [
   "The patient's occupation, marital status, and employer address, which are needed for billing the lab.",
   "The technician's name, the time of the draw, and the room temperature at the moment of collection.",
   "The patient's blood type, last meal, and preferred language, which must be entered by the phlebotomist."
  ],
  "qd": "Patient demographics, physician information, diagnosis code, tests ordered, and test priority.",
  "qw": [
   "The patient's occupation, marital status, and employer address, which are needed for billing the lab.",
   "The technician's name, the time of the draw, and the room temperature at the moment of collection.",
   "The patient's blood type, last meal, and preferred language, which must be entered by the phlebotomist."
  ],
  "e": "The NHA test plan lists these requisition fields as knowledge the candidate must have.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is the difference between a STAT order and a routine order?",
  "d": "A STAT order must be collected and processed immediately, while a routine order follows the normal collection schedule.",
  "c": 1,
  "w": [
   "A STAT order is collected after lunch, while a routine order is collected first thing each morning.",
   "A STAT order is drawn only by capillary puncture, while a routine order requires a venous draw.",
   "A STAT order is always a fasting test, while a routine order can be drawn at any time of day."
  ],
  "qd": "A STAT order is collected and processed right away; a routine order follows the normal schedule.",
  "qw": [
   "A STAT order is collected after lunch; a routine order is collected first thing each morning.",
   "A STAT order is drawn by capillary puncture only; a routine order requires a venous draw.",
   "A STAT order is always a fasting test; a routine order can be drawn at any time of day."
  ],
  "e": "The test plan lists STAT and routine draws, peaks and troughs, and time of day as timing requirements.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is a trough level draw?",
  "d": "A sample collected just before the next dose, when the drug level is at its lowest.",
  "c": 1,
  "w": [
   "A sample collected right after a dose, when the drug level is at its highest point.",
   "A sample collected in the middle of the dosing interval, when levels are stable.",
   "A sample collected at the end of a fasting period, unrelated to any medication schedule."
  ],
  "qd": "A sample collected just before the next dose, when the drug level is at its lowest.",
  "qw": [
   "A sample collected right after a dose, when the drug level is at its highest point.",
   "A sample collected in the middle of the dosing interval, when levels are stable.",
   "A sample collected at the end of a fasting period, unrelated to any medication schedule."
  ],
  "e": "Peak and trough timing is a timing requirement the test plan asks candidates to know.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is a fasting requirement for a blood test?",
  "d": "No food or drink, except water, for the number of hours the order specifies before the draw.",
  "c": 1,
  "w": [
   "No water for the stated hours, but light meals and coffee are allowed until the draw.",
   "A large meal two hours before the draw, so that blood sugar stays stable during collection.",
   "All scheduled medications, with only the morning coffee skipped before the draw."
  ],
  "qd": "No food or drink, except water, for the number of hours the order specifies before the draw.",
  "qw": [
   "No water for the stated hours, but light meals and coffee are allowed until the draw.",
   "A large meal two hours before the draw, so that blood sugar stays stable during collection.",
   "All scheduled medications, with only the morning coffee skipped before the draw."
  ],
  "e": "MedlinePlus explains that fasting for a blood test usually means no food or drink except water for a set period.",
  "u": "https://medlineplus.gov/lab-tests/fasting-for-a-blood-test/",
  "s": "MedlinePlus: Fasting for a Blood Test"
 },
 {
  "t": "What does a basal state requirement mean for a draw?",
  "d": "The patient is at rest, without recent exercise or stress, before the sample is drawn.",
  "c": 1,
  "w": [
   "The patient has just finished a large meal and is walking around the waiting room.",
   "The patient has taken a dose of their usual medication shortly before the draw.",
   "The patient has been awake for several hours and is preparing for an afternoon test."
  ],
  "qd": "The patient is at rest, without recent exercise or stress, before the sample is drawn.",
  "qw": [
   "The patient has just finished a large meal and is walking around the waiting room.",
   "The patient has taken a dose of their usual medication shortly before the draw.",
   "The patient has been awake for several hours and is preparing for an afternoon test."
  ],
  "e": "Testing requirements include fasting, medication, and basal state, which the test plan lists together.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which type of question is best for learning about a patient's special considerations?",
  "d": "An open-ended question, such as asking the patient to describe any past problems with blood draws.",
  "c": 1,
  "w": [
   "A yes-or-no question, such as asking whether the patient has ever fainted during a draw.",
   "A leading question, such as asking whether the patient is worried about needles today.",
   "A closed question, such as asking the patient to confirm their date of birth only."
  ],
  "qd": "An open-ended question, such as asking the patient to describe any past problems with blood draws.",
  "qw": [
   "A yes-or-no question, such as asking whether the patient has ever fainted during a draw.",
   "A leading question, such as asking whether the patient is worried about needles today.",
   "A closed question, such as asking the patient to confirm their date of birth only."
  ],
  "e": "The test plan lists open-ended questions and empathetic listening as patient interviewing techniques.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What are the three types of consent a phlebotomist may need to obtain?",
  "d": "Implied, informed, and expressed consent.",
  "c": 1,
  "w": [
   "Verbal, written, and witnessed consent, which are all required for every draw in every setting.",
   "Parental, legal, and emergency consent, which apply only to patients under the age of eighteen.",
   "Oral, electronic, and proxy consent, which must be recorded on the requisition before the draw."
  ],
  "qd": "Implied, informed, and expressed consent.",
  "qw": [
   "Verbal, written, and witnessed consent, which are all required for every draw in every setting.",
   "Parental, legal, and emergency consent, which apply only to patients under the age of eighteen.",
   "Oral, electronic, and proxy consent, which must be recorded on the requisition before the draw."
  ],
  "e": "The test plan lists implied, informed, and expressed consent and the components required for each.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "When must a legal guardian's permission be obtained before a draw?",
  "d": "When the patient cannot give verbal or expressed consent, such as a child or a patient with dementia or a mental disability.",
  "c": 1,
  "w": [
   "Whenever the patient is older than seventy, regardless of their mental capacity at the time.",
   "Whenever the draw is a routine test ordered during a clinic visit with a physician present.",
   "Only when the patient refuses to sign the lab's privacy notice at the front desk."
  ],
  "qd": "When the patient cannot give verbal or expressed consent, such as a child or a patient with dementia.",
  "qw": [
   "When the patient is older than seventy, regardless of their mental capacity at the time.",
   "When the draw is a routine test ordered during a clinic visit with a physician present.",
   "When the patient refuses to sign the lab's privacy notice at the front desk."
  ],
  "e": "The test plan lists obtaining permission from a legal guardian when consent cannot be obtained directly.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What should be verified about a patient's insurance before a draw?",
  "d": "That the coverage is current and covers the tests ordered, with the orders and requisitions reviewed.",
  "c": 1,
  "w": [
   "That the patient's employer pays for all tests, so no insurance card needs to be shown.",
   "That the patient has paid the copayment in full, so the lab can accept the order.",
   "That the insurance company has approved the phlebotomist, not the patient's coverage."
  ],
  "qd": "That the coverage is current and covers the tests ordered, with the orders and requisitions reviewed.",
  "qw": [
   "That the patient's employer pays for all tests, so no insurance card needs to be shown.",
   "That the patient has paid the copayment in full, so the lab can accept the order.",
   "That the insurance company has approved the phlebotomist, not the patient's coverage."
  ],
  "e": "Confirming insurance coverage and reviewing orders and requisitions is a patient preparation task in the test plan.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Why is a fistula or a physical condition noted before a draw?",
  "d": "Because it can change how the draw is done, including the site, the arm, or the equipment used.",
  "c": 1,
  "w": [
   "Because it changes the color of the tubes the lab requires, so the right colors are ordered.",
   "Because it determines which hospital department the patient will be billed through.",
   "Because it sets the number of tubes the patient may take home after the appointment."
  ],
  "qd": "Because it can change how the draw is done, including the site, the arm, or the equipment used.",
  "qw": [
   "Because it changes the color of the tubes the lab requires, so the right colors are ordered.",
   "Because it determines which hospital department the patient will be billed through.",
   "Because it sets the number of tubes the patient may take home after the appointment."
  ],
  "e": "Special considerations such as age, physical and mental condition, and the presence of fistulas affect collection.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is a patient positioning requirement for venipuncture?",
  "d": "Seated in a phlebotomy chair with an armrest, or lying down, with the arm extended downward.",
  "c": 1,
  "w": [
   "Standing upright with the arm raised above the head to fill the veins before the draw.",
   "Seated on a stool with the arm held at chest height to stop the blood from pooling.",
   "Lying flat on the back with both arms crossed over the chest during the whole procedure."
  ],
  "qd": "Seated in a phlebotomy chair with an armrest, or lying down, with the arm extended downward.",
  "qw": [
   "Standing upright with the arm raised above the head to fill the veins before the draw.",
   "Seated on a stool with the arm held at chest height to stop the blood from pooling.",
   "Lying flat on the back with both arms crossed over the chest during the whole procedure."
  ],
  "e": "Patient positioning is listed in the test plan, and the handout describes the seated or lying positions.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What can cause a patient to faint during a draw?",
  "d": "Emotional or physical stress, which triggers a vasovagal response that lowers blood pressure and heart rate.",
  "c": 1,
  "w": [
   "Eating a light snack before the draw, which lowers the blood sugar too quickly.",
   "Wearing a short-sleeved shirt, which lets the tourniquet slip during the procedure.",
   "Drinking a glass of water before the draw, which dilutes the blood in the arm."
  ],
  "qd": "Emotional or physical stress, which triggers a vasovagal response that lowers heart rate.",
  "qw": [
   "Eating a light snack before the draw, which lowers blood sugar too quickly for the patient.",
   "Wearing a short-sleeved shirt, which lets the tourniquet slip during the procedure.",
   "Drinking a glass of water before the draw, which dilutes the blood in the arm."
  ],
  "e": "Fainting, or syncope, is a vasovagal response triggered by stress. A patient with a fainting history needs a seated or lying position.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "Why are medications and allergies checked before a draw?",
  "d": "Because they can affect test results and the timing or fasting needed for the order.",
  "c": 1,
  "w": [
   "Because medication lists determine the patient's billing category and co-payment amount.",
   "Because the medication list replaces the requisition, so the physician's order is not needed.",
   "Because medication lists are required only for patients under twelve years of age."
  ],
  "qd": "Because they can affect test results and the timing or fasting needed for the order.",
  "qw": [
   "Because medication lists determine the patient's billing category and co-payment amount.",
   "Because the medication list replaces the requisition, so the physician's order is not needed.",
   "Because medication lists are required only for patients under twelve years of age."
  ],
  "e": "The test plan lists allergies, medications, recent surgeries, and history of fainting as variables that may impact collections.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What are the minimum and maximum blood volume requirements?",
  "d": "Each test has a minimum and maximum blood volume that gives an adequate sample without excess draw.",
  "c": 1,
  "w": [
   "Each test requires exactly one tube, and blood volume is not tracked for any test type.",
   "The maximum volume is always the full capacity of the largest tube in the set.",
   "The minimum volume applies only to capillary samples, while venous samples have no limits."
  ],
  "qd": "Each test has a minimum and maximum blood volume that gives an adequate sample without excess draw.",
  "qw": [
   "Each test requires exactly one tube, and blood volume is not tracked for any test type.",
   "The maximum volume is always the full capacity of the largest tube in the set.",
   "The minimum volume applies only to capillary samples, while venous samples have no limits."
  ],
  "e": "Minimum and maximum blood volume is a knowledge item in the test plan, important for patients at higher risk.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which collection instructions does the phlebotomist give a patient for a non-blood specimen?",
  "d": "Clean-catch midstream urine, collected in a sterile container and labeled as the instructions describe.",
  "c": 1,
  "w": [
   "Random urine collected from the bathroom trash, placed in a plastic bag without a container.",
   "First morning urine poured into a glass vial, with no instructions given to the patient.",
   "Urine collected from the catheter bag after it has been emptied at the nurses' station."
  ],
  "qd": "Clean-catch midstream urine, collected in a sterile container and labeled as the instructions describe.",
  "qw": [
   "Random urine collected from the bathroom trash, placed in a plastic bag without a container.",
   "First morning urine poured into a glass vial, with no instructions given to the patient.",
   "Urine collected from the catheter bag after it has been emptied at the nurses' station."
  ],
  "e": "The test plan lists non-blood specimen collection, including stool, urine, semen, and sputum, with patient instructions.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which non-blood specimens does the test plan list for patient instructions?",
  "d": "Stool, urine, semen, and sputum.",
  "c": 1,
  "w": [
   "Blood, saliva, tears, and hair follicles.",
   "Stool, bile, sweat, and nail clippings.",
   "Urine, cerebrospinal fluid, bone marrow, and synovial fluid."
  ],
  "qd": "Stool, urine, semen, and sputum.",
  "qw": [
   "Blood, saliva, tears, and hair follicles.",
   "Stool, bile, sweat, and nail clippings.",
   "Urine, cerebrospinal fluid, bone marrow, and synovial fluid."
  ],
  "e": "The test plan lists these four non-blood specimens under patient instructions for collection.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Why must the patient's identity be checked again after a patient is moved to a different bed?",
  "d": "Patients may be moved or swapped, so the wristband and bed location may no longer match the requisition.",
  "c": 1,
  "w": [
   "Because the lab computer resets its patient registry each time a bed is changed.",
   "Because bed moves require a new requisition to be printed by the front desk each time.",
   "Because bed changes cancel the order, so the phlebotomist must start over with a new one."
  ],
  "qd": "Patients may be moved or swapped, so the wristband and bed may no longer match the requisition.",
  "qw": [
   "The lab computer resets its patient registry each time a bed is changed in the unit.",
   "Bed moves require a new requisition to be printed at the front desk each time they happen.",
   "Bed changes cancel the order, so the phlebotomist must start over with a new order."
  ],
  "e": "CLSI recommends identification at the point of collection, which must match the patient's current identity.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What must be entered in the EMR or EHR after a draw?",
  "d": "All pertinent information about the collection, so the record is complete and accurate.",
  "c": 1,
  "w": [
   "Only the tube count, since the lab stores the rest of the information in its own system.",
   "Only the patient's name, since the test results are entered by the lab technologist later.",
   "Nothing, because the record is updated automatically from the printed requisition."
  ],
  "qd": "All pertinent information about the collection, so the record is complete and accurate.",
  "qw": [
   "Only the tube count, since the lab stores the rest of the information in its own system.",
   "Only the patient's name, since the test results are entered by the lab technologist later.",
   "Nothing, because the record is updated automatically from the printed requisition."
  ],
  "e": "The test plan includes entering all pertinent information into the electronic medical record or health record.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What should be checked about equipment quality before use?",
  "d": "Sterility, expiration date, and any manufacturer defects, such as cracked tubes.",
  "c": 2,
  "w": [
   "Only the color of the tube cap, which indicates whether the tube is new or previously used.",
   "Only the weight of the needle package, which must match the manufacturer's listed weight.",
   "Only the room temperature at the time the equipment is taken out of storage."
  ],
  "qd": "Sterility, expiration date, and any manufacturer defects, such as cracked tubes.",
  "qw": [
   "Only the color of the tube cap, which indicates whether the tube is new or previously used.",
   "Only the weight of the needle package, which must match the manufacturer's listed weight.",
   "Only the room temperature at the time the equipment is taken out of storage."
  ],
  "e": "The test plan lists verifying equipment quality, including sterility, expiration date, and manufacturer defects.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which equipment is needed for a basic evacuated-tube venipuncture?",
  "d": "An evacuated tube holder, needle, tubes in the correct order, tourniquet, antiseptic, gauze, and a bandage.",
  "c": 2,
  "w": [
   "A syringe, tubes, a heat pack, and a glucometer, with no tourniquet needed for the draw.",
   "A scalpel, gauze, tubes with no additives, and a blood pressure cuff for each patient.",
   "A lancet, microscope slides, a timer, and a clipboard with the patient's chart attached."
  ],
  "qd": "An evacuated tube holder, needle, tubes in order, tourniquet, antiseptic, gauze, and a bandage.",
  "qw": [
   "A syringe, tubes, a heat pack, and a glucometer, with no tourniquet needed for the draw.",
   "A scalpel, gauze, tubes with no additives, and a blood pressure cuff for each patient.",
   "A lancet, microscope slides, a timer, and a clipboard with the patient's chart attached."
  ],
  "e": "The test plan lists selecting and assembling equipment such as the evacuated tube system, needle, syringe, and winged set.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which needle gauge is commonly used for an adult venipuncture?",
  "d": "21-gauge.",
  "c": 2,
  "w": [
   "7-gauge, a large needle used to draw blood from a central line in critical care.",
   "30-gauge, a very fine needle used for insulin injections under the skin.",
   "14-gauge, a large needle used for blood donation and transfusion procedures only."
  ],
  "qd": "21-gauge.",
  "qw": [
   "7-gauge, a large needle used to draw blood from a central line in critical care.",
   "30-gauge, a very fine needle used for insulin injections under the skin.",
   "14-gauge, a large needle used for blood donation and transfusion procedures only."
  ],
  "e": "The test plan lists needle gauge sizes and lengths as knowledge for device selection. 21-gauge is a common adult size.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What should a phlebotomist do if a vein is hard to palpate?",
  "d": "Try warming the arm, lower the arm below heart level, or choose another site, following facility guidance.",
  "c": 2,
  "w": [
   "Press harder on the skin with the thumb until a vein rises, then insert the needle right away.",
   "Remove the tourniquet and try the same site immediately after the patient makes a fist.",
   "Ask the patient to stand and swing the arm to fill the veins before the draw begins."
  ],
  "qd": "Try warming the arm, lower the arm below heart level, or choose another site, following facility guidance.",
  "qw": [
   "Press harder on the skin with the thumb until a vein rises, then insert the needle right away.",
   "Remove the tourniquet and try the same site immediately after the patient makes a fist.",
   "Ask the patient to stand and swing the arm to fill the veins before the draw begins."
  ],
  "e": "Palpation techniques are a knowledge item in the test plan. Warming and lowering the arm are common techniques.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is the purpose of antiseptic preparation at the venipuncture site?",
  "d": "To reduce the risk of introducing microorganisms into the puncture site and the sample.",
  "c": 2,
  "w": [
   "To remove the patient's natural skin oils so the needle slides in more easily during the draw.",
   "To make the veins larger so that the needle stays in place during the draw.",
   "To warm the skin so that the blood flows more freely into the tube during collection."
  ],
  "qd": "To reduce the risk of introducing microorganisms into the puncture site and the sample.",
  "qw": [
   "To remove the patient's natural skin oils so the needle slides in more easily during the draw.",
   "To make the veins larger so that the needle stays in place during the draw.",
   "To warm the skin so that the blood flows more freely into the tube during collection."
  ],
  "e": "Skin preparation with an antiseptic before a needle enters the skin is standard infection prevention.",
  "u": "https://www.cdc.gov/injection-safety/hcp/clinical-safety/",
  "s": "CDC: Injection Safety, Clinical Safety"
 },
 {
  "t": "Which antiseptic is commonly used for venipuncture site preparation?",
  "d": "70 percent isopropyl alcohol, allowed to air dry completely.",
  "c": 2,
  "w": [
   "Undiluted hydrogen peroxide, applied and wiped off with a dry gauze pad immediately.",
   "Water-based hand soap, rinsed off with cool water before the tourniquet is applied.",
   "Household bleach diluted to one part in ten, wiped on and left to dry for one minute."
  ],
  "qd": "70 percent isopropyl alcohol, allowed to air dry completely.",
  "qw": [
   "Undiluted hydrogen peroxide, applied and wiped off with a dry gauze pad immediately.",
   "Water-based hand soap, rinsed off with cool water before the tourniquet is applied.",
   "Household bleach diluted to one part in ten, wiped on and left to dry for one minute."
  ],
  "e": "The course handout specifies 70 percent isopropyl alcohol with complete air drying before the needle enters.",
  "u": "https://www.cdc.gov/injection-safety/hcp/clinical-safety/",
  "s": "CDC: Injection Safety, Clinical Safety"
 },
 {
  "t": "What should a phlebotomist do when a tube does not fill?",
  "d": "Check the needle position, tourniquet, and tube vacuum, then reposition or change the needle and use a new tube.",
  "c": 2,
  "w": [
   "Leave the needle in place and wait several minutes for the vacuum to refill the tube naturally.",
   "Remove the tube and label it as an incomplete draw, then send it to the lab anyway.",
   "Shake the tube vigorously to start the flow of blood into the empty space inside it."
  ],
  "qd": "Check the needle, tourniquet, and tube vacuum, then reposition or change the needle and tube.",
  "qw": [
   "Leave the needle in place and wait for the vacuum to refill the tube naturally over time.",
   "Remove the tube and label it as incomplete, then send it to the lab anyway for testing.",
   "Shake the tube vigorously to start blood flowing into the empty space inside the tube."
  ],
  "e": "Adjusting the needle, tube, or angle to establish blood flow is listed among the test plan's knowledge items.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is the correct order of steps to remove a venipuncture device?",
  "d": "Release the tourniquet, remove the needle, activate the safety device, then apply gauze and pressure.",
  "c": 2,
  "w": [
   "Remove the tourniquet last, after the needle is discarded and the site has been bandaged.",
   "Leave the needle in place until the patient is standing, then remove it with the tourniquet on.",
   "Remove the needle first, recap it with the safety sleeve, then release the tourniquet."
  ],
  "qd": "Release the tourniquet, remove the needle, activate the safety device, then apply gauze and pressure.",
  "qw": [
   "Remove the tourniquet last, after the needle is discarded and the site has been bandaged.",
   "Leave the needle in place until the patient is standing, then remove it with the tourniquet on.",
   "Remove the needle first, recap it with the safety sleeve, then release the tourniquet."
  ],
  "e": "The test plan lists the procedural steps for removing the tourniquet, tubes, and needle.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What should a phlebotomist do after a capillary (dermal) puncture?",
  "d": "Apply gentle pressure to stop bleeding and bandage if needed, after the sample is collected.",
  "c": 2,
  "w": [
   "Squeeze the finger hard to collect more blood, then leave the site uncovered for the patient to see.",
   "Hold the finger above the heart for ten minutes, then return the patient to the waiting room.",
   "Massage the wrist firmly to restart circulation, then draw the next tube from the same finger."
  ],
  "qd": "Apply gentle pressure to stop bleeding and bandage if needed, after the sample is collected.",
  "qw": [
   "Squeeze the finger hard to collect more blood, then leave the site uncovered for the patient to see.",
   "Hold the finger above the heart for ten minutes, then return the patient to the waiting room.",
   "Massage the wrist firmly to restart circulation, then draw the next tube from the same finger."
  ],
  "e": "Post-procedural care and bandaging are listed in the test plan under dermal puncture for capillary collection.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which additive is used in a lavender or pink tube for a type and screen?",
  "d": "EDTA, a whole-blood anticoagulant that the blood bank accepts for typing when labeled at the bedside.",
  "c": 3,
  "w": [
   "Sodium citrate, a liquid anticoagulant that the blood bank uses only for coagulation studies.",
   "Lithium heparin, a plasma anticoagulant that the blood bank accepts for serum typing tests.",
   "Silica clot activator, which speeds clotting so the blood bank can read a serum sample."
  ],
  "qd": "EDTA, a whole-blood anticoagulant that the blood bank accepts for typing when labeled at the bedside.",
  "qw": [
   "Sodium citrate, a liquid anticoagulant that the blood bank uses only for coagulation studies.",
   "Lithium heparin, a plasma anticoagulant that the blood bank accepts for serum typing tests.",
   "Silica clot activator, which speeds clotting so the blood bank can read a serum sample."
  ],
  "e": "The course handout lists type and screen in the lavender or pink tube. Blood bank samples are labeled at the bedside.",
  "u": "https://medlineplus.gov/ency/article/003345.htm",
  "s": "MedlinePlus: Blood Typing"
 },
 {
  "t": "Which special collection uses a dried blood spot on filter paper?",
  "d": "Newborn screening for inborn errors of metabolism, such as PKU and galactosemia.",
  "c": 4,
  "w": [
   "Blood donation screening for hepatitis B and hepatitis C in a blood bank setting.",
   "Blood alcohol testing collected in a gray tube after a motor vehicle accident.",
   "Blood culture collection performed in the emergency department for suspected sepsis."
  ],
  "qd": "Newborn screening for inborn errors of metabolism, such as PKU and galactosemia.",
  "qw": [
   "Blood donation screening for hepatitis B and hepatitis C in a blood bank setting.",
   "Blood alcohol testing collected in a gray tube after a motor vehicle accident.",
   "Blood culture collection performed in the emergency department for suspected sepsis."
  ],
  "e": "The test plan lists collecting samples for inborn errors of metabolism and collecting blood on filter paper.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is a peripheral blood smear used for?",
  "d": "Examining blood cell shape, size, and number under a microscope.",
  "c": 4,
  "w": [
   "Measuring the clotting time of plasma after a standard dose of heparin is given to the patient.",
   "Culturing bacteria from a patient's blood to identify the infecting organism in the lab.",
   "Measuring blood sugar with a handheld meter at the bedside before the patient eats."
  ],
  "qd": "Examining blood cell shape, size, and number under a microscope.",
  "qw": [
   "Measuring the clotting time of plasma after a standard dose of heparin is given to the patient.",
   "Culturing bacteria from a patient's blood to identify the infecting organism in the lab.",
   "Measuring blood sugar with a handheld meter at the bedside before the patient eats."
  ],
  "e": "The test plan lists preparing peripheral blood smears and the equipment, such as slides and lancets, needed for them.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which glucose tests may require a 2-hour post-prandial draw?",
  "d": "Glucose tolerance tests, and lactose or 2-hour post-prandial glucose tests, timed from the start of the meal.",
  "c": 4,
  "w": [
   "A fasting lipid panel, drawn before breakfast with no timing relative to a meal.",
   "A hemoglobin A1c test, drawn at any time without regard to meals or fasting status.",
   "A type and screen test, drawn during the patient's first hour after surgery."
  ],
  "qd": "Glucose tolerance tests and lactose or 2-hour post-prandial glucose tests, timed from the meal.",
  "qw": [
   "A fasting lipid panel drawn before breakfast, with no timing relative to any meal.",
   "A hemoglobin A1c test drawn at any time, without regard to meals or fasting status.",
   "A type and screen drawn during the first hour after surgery, before any meal is served."
  ],
  "e": "The test plan lists tolerance tests such as gestational glucose, lactose, and 2-hour post-prandial glucose.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What does a hemoglobin A1c test require about fasting?",
  "d": "No fasting is required, because the test reflects average blood glucose over about three months.",
  "c": 4,
  "w": [
   "Eight hours of fasting, since the test measures glucose that is present on the day of the draw.",
   "A two-hour fast followed by a glucose drink, so the result shows the body's response to sugar.",
   "Complete avoidance of all food and drink for twelve hours before the sample is drawn."
  ],
  "qd": "No fasting is required, because the test reflects average blood glucose over about three months.",
  "qw": [
   "Eight hours of fasting, since the test measures glucose that is present on the day of the draw.",
   "A two-hour fast followed by a glucose drink, so the result shows the body's response to sugar.",
   "Complete avoidance of all food and drink for twelve hours before the sample is drawn."
  ],
  "e": "The A1c reflects average glucose over roughly the past two to three months, so timing relative to meals does not change it.",
  "u": "https://medlineplus.gov/lab-tests/fasting-for-a-blood-test/",
  "s": "MedlinePlus: Fasting for a Blood Test"
 },
 {
  "t": "What is required for a blood donation draw?",
  "d": "Screening for hemoglobin, hematocrit, weight, and a complete patient screening before collection.",
  "c": 4,
  "w": [
   "Only a finger-stick glucose check, since donors are screened by the lab after collection.",
   "A signed waiver from the family, with no screening required for healthy adult donors.",
   "A urine sample from the donor to confirm hydration before any blood is drawn."
  ],
  "qd": "Screening for hemoglobin, hematocrit, weight, and a complete patient screening before collection.",
  "qw": [
   "Only a finger-stick glucose check, since donors are screened by the lab after collection.",
   "A signed waiver from the family, with no screening required for healthy adult donors.",
   "A urine sample from the donor to confirm hydration before any blood is drawn."
  ],
  "e": "The test plan lists standards for blood donation, including hemoglobin and hematocrit levels, weight, and complete screening.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Why is a pediatric volume calculation done before a draw?",
  "d": "To keep the total blood drawn within safe limits for the patient's weight or blood volume, avoiding iatrogenic anemia.",
  "c": 4,
  "w": [
   "To match the size of the tube to the child's height, so the label fits on the tube correctly.",
   "To decide how many adults can share a single tube during a lab shift.",
   "To estimate the child's future insurance premium based on the amount of blood drawn."
  ],
  "qd": "To keep total blood drawn within safe limits for the patient's weight, avoiding iatrogenic anemia.",
  "qw": [
   "To match the tube size to the child's height, so the label fits on the tube correctly.",
   "To decide how many adults can share a single tube during a busy lab shift.",
   "To estimate the child's future insurance premium based on the amount of blood drawn."
  ],
  "e": "The test plan asks candidates to calculate volume requirements for higher-risk patients to avoid causing iatrogenic anemia.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is the purpose of a blood culture in a suspected infection?",
  "d": "To detect bacteria or fungi circulating in the bloodstream of a patient with suspected sepsis.",
  "c": 4,
  "w": [
   "To measure the oxygen carried by red blood cells in a patient with anemia.",
   "To check the patient's cholesterol level before a planned surgery is performed.",
   "To identify the blood type of a patient before a transfusion is given on the ward."
  ],
  "qd": "To detect bacteria or fungi circulating in the bloodstream of a patient with suspected sepsis.",
  "qw": [
   "To measure the oxygen carried by red blood cells in a patient with anemia.",
   "To check the patient's cholesterol level before a planned surgery is performed.",
   "To identify the blood type of a patient before a transfusion is given on the ward."
  ],
  "e": "Blood cultures are collected before antibiotics when possible, with two or more sets drawn from separate sites.",
  "u": "https://www.cdc.gov/lab-quality/php/preventing-adult-blood-culture-contamination/collect.html",
  "s": "CDC: Collect Adult Blood Culture Sets"
 },
 {
  "t": "What rule applies to chain of custody for a drug screen or blood alcohol test?",
  "d": "Chain of custody is used when required, with the specimen and its documentation tracked at every handling step.",
  "c": 4,
  "w": [
   "Any tube may be used, since drug screens are not affected by the additive or the handling.",
   "Urine is always substituted for blood, so chain of custody does not apply to blood tests.",
   "The sample is collected after the patient has been medicated, so results show the treatment level."
  ],
  "qd": "Chain of custody is used when required, with the specimen and its documentation tracked at every handling step.",
  "qw": [
   "Any tube may be used, since drug screens are not affected by the additive or the handling.",
   "Urine is always substituted for blood, so chain of custody does not apply to blood tests.",
   "The sample is collected after the patient has been medicated, so results show the treatment level."
  ],
  "e": "The test plan lists adhering to chain of custody guidelines for forensic studies, blood alcohol, and drug screens.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Which specimens are collected with swabs for culture?",
  "d": "Non-blood specimens, such as throat cultures, nasal swabs, and wound cultures.",
  "c": 4,
  "w": [
   "Blood specimens collected by venipuncture, such as serum for chemistry and CBC testing.",
   "Capillary samples from the fingertip, such as glucose and hemoglobin measurements.",
   "Clean-catch urine specimens collected in a sterile cup for routine urinalysis."
  ],
  "qd": "Non-blood specimens, such as throat cultures, nasal swabs, and wound cultures.",
  "qw": [
   "Blood specimens collected by venipuncture, such as serum for chemistry and CBC testing.",
   "Capillary samples from the fingertip, such as glucose and hemoglobin measurements.",
   "Clean-catch urine specimens collected in a sterile cup for routine urinalysis."
  ],
  "e": "The test plan lists performing or processing non-blood specimen collection, including throat cultures and wound cultures.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is aliquoting?",
  "d": "Dividing a processed specimen into smaller labeled portions for testing, storage, or transport.",
  "c": 4,
  "w": [
   "Adding a preservative to a whole blood sample so that it can be stored at room temperature.",
   "Mixing two patients' samples together to save time when the lab is busy.",
   "Removing platelets from a whole blood sample before the sample is labeled and counted."
  ],
  "qd": "Dividing a processed specimen into smaller labeled portions for testing, storage, or transport.",
  "qw": [
   "Adding a preservative to a whole blood sample so that it can be stored at room temperature.",
   "Mixing two patients' samples together to save time when the lab is busy.",
   "Removing platelets from a whole blood sample before the sample is labeled and counted."
  ],
  "e": "Aliquoting procedures and techniques are a knowledge item in the test plan for specimen processing.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "How should specimens be stored and transported when integrity depends on temperature?",
  "d": "At the temperature the test requires, protected from light when needed, and transported within the stated time limit.",
  "c": 4,
  "w": [
   "At room temperature in all cases, since refrigeration damages every type of blood specimen.",
   "On the bench until the lab opens, regardless of the temperature the specific test requires.",
   "In the patient's room until the next scheduled pickup, with the tube cap left open."
  ],
  "qd": "At the temperature the test requires, protected from light if needed, and transported on time.",
  "qw": [
   "At room temperature in all cases, since refrigeration damages every type of blood specimen.",
   "On the bench until the lab opens, regardless of the temperature the specific test requires.",
   "In the patient's room until the next pickup, with the tube cap left open for ventilation."
  ],
  "e": "The test plan lists handling, storage, transportation, and disposal requirements, including temperature and viability guidelines.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Why are specimens sealed in biohazard bags for transport?",
  "d": "To contain potentially infectious material and protect transporters and the public.",
  "c": 4,
  "w": [
   "To keep the samples cold without needing ice packs or a refrigerated cooler.",
   "To prevent the labels from getting wet, so that the barcodes stay readable in the lab.",
   "To keep the tubes upright during the courier's route so that the specimens do not spill."
  ],
  "qd": "To contain potentially infectious material and protect transporters and the public.",
  "qw": [
   "To keep the samples cold without needing ice packs or a refrigerated cooler.",
   "To prevent the labels from getting wet, so that the barcodes stay readable in the lab.",
   "To keep the tubes upright during the courier's route so that the specimens do not spill."
  ],
  "e": "Handling and transport requirements for biohazard specimens are part of the processing domain.",
  "u": "https://www.osha.gov/bloodborne-pathogens/standards",
  "s": "OSHA: Bloodborne Pathogens Standards"
 },
 {
  "t": "What are critical values?",
  "d": "Lab results so abnormal they could be life-threatening, which must be reported promptly to the ordering provider.",
  "c": 4,
  "w": [
   "Results that fall within the normal reference range and are reported as a routine confirmation.",
   "Test results from the previous week that are kept on file for auditors each month.",
   "Values that show the lab's equipment calibration, which are reported only to the manufacturer."
  ],
  "qd": "Results so abnormal they could be life-threatening, reported promptly to the ordering provider.",
  "qw": [
   "Results within the normal reference range, reported as a routine confirmation of health.",
   "Test results from the previous week, kept on file for auditors to review each month.",
   "Values showing the lab's equipment calibration, reported only to the manufacturer."
  ],
  "e": "The test plan lists recognizing and reporting critical values for point-of-care and CLIA-waived testing.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is the phlebotomist's role in distributing laboratory results?",
  "d": "Following the lab's basic protocol so results reach the ordering provider and the medical record is updated.",
  "c": 4,
  "w": [
   "Calling the patient directly with results, since the phlebotomist is the only staff member who can speak to patients.",
   "Sending results to the insurance company before the physician reviews them, to speed up payment.",
   "Keeping a personal copy of results to share with coworkers as a training example."
  ],
  "qd": "Following the lab's basic protocol so results reach the ordering provider and the medical record is updated.",
  "qw": [
   "Calling the patient directly with results, since the phlebotomist is the only staff member who can speak to patients.",
   "Sending results to the insurance company before the physician reviews them, to speed up payment.",
   "Keeping a personal copy of results to share with coworkers as a training example."
  ],
  "e": "The test plan lists basic protocols to distribute laboratory results and updating the medical record.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "When is patient recollection needed?",
  "d": "When a specimen is rejected, mislabeled, hemolyzed, or otherwise unsuitable, so the patient must be contacted for a new collection.",
  "c": 4,
  "w": [
   "Only when the patient requests a second test for personal reasons unrelated to the lab result.",
   "Only when the physician asks for the sample to be repeated after the next day's rounds.",
   "Only when the lab has run out of tubes and needs the patient to come back another day."
  ],
  "qd": "A specimen rejected as mislabeled, hemolyzed, or unsuitable, so the patient must be recollected.",
  "qw": [
   "Only when the patient requests a second test for personal reasons unrelated to the result.",
   "Only when the physician asks for a repeat sample after the next day's rounds are done.",
   "Only when the lab has run out of tubes and needs the patient to return another day."
  ],
  "e": "The test plan lists contacting the patient for re-collection as needed.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What does LIS stand for, and what does it do in processing?",
  "d": "Laboratory information system, used to enter and retrieve specimen data.",
  "c": 4,
  "w": [
   "Laboratory isolation system, used to keep infected specimens separated during transport.",
   "Legal inspection service, used to audit the lab's records once each year.",
   "Limited inventory system, used to track which tubes are in stock at each unit."
  ],
  "qd": "Laboratory information system, used to enter and retrieve specimen data.",
  "qw": [
   "Laboratory isolation system, used to keep infected specimens separated during transport.",
   "Legal inspection service, used to audit the lab's records once each year.",
   "Limited inventory system, used to track which tubes are in stock at each unit."
  ],
  "e": "The test plan lists inputting and retrieving specimen data using the available laboratory information system.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is lipemia?",
  "d": "Milky or turbid serum or plasma caused by excess lipids, which can interfere with laboratory tests.",
  "c": 5,
  "w": [
   "Yellow discoloration of serum caused by bile pigments released from damaged red cells.",
   "Clumping of white blood cells that forms visible threads in the tube after centrifugation.",
   "Clear serum produced when the sample is spun too quickly in the centrifuge."
  ],
  "qd": "Milky or turbid serum or plasma caused by excess lipids, which can interfere with laboratory tests.",
  "qw": [
   "Yellow discoloration of serum caused by bile pigments released from damaged red cells.",
   "Clumping of white blood cells that forms visible threads in the tube after centrifugation.",
   "Clear serum produced when the sample is spun too quickly in the centrifuge."
  ],
  "e": "Lipemia is a common specimen interference that the handout describes alongside hemolysis.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is icterus in a serum sample?",
  "d": "Yellow discoloration caused by high bilirubin, which can interfere with some tests.",
  "c": 5,
  "w": [
   "Red discoloration caused by free hemoglobin released from damaged red cells.",
   "Clear serum showing that the sample was drawn from an IV line with saline contamination.",
   "Dark brown color caused by urine that was placed in a blood tube by mistake."
  ],
  "qd": "Yellow discoloration caused by high bilirubin, which can interfere with some tests.",
  "qw": [
   "Red discoloration caused by free hemoglobin released from damaged red cells.",
   "Clear serum showing that the sample was drawn from an IV line with saline contamination.",
   "Dark brown color caused by urine that was placed in a blood tube by mistake."
  ],
  "e": "Icterus, lipemia, and hemolysis are common specimen interferences that the lab checks for.",
  "u": "https://medlineplus.gov/lab-tests/",
  "s": "MedlinePlus: Medical Tests"
 },
 {
  "t": "What is a clotted specimen?",
  "d": "A sample in which a clot has formed in the tube, usually from underfilling, poor mixing, or delayed inversion.",
  "c": 5,
  "w": [
   "A sample that has separated into layers because it was left upright for too long at room temperature.",
   "A sample that is perfectly liquid but darker than normal because of the anticoagulant used.",
   "A sample in which the serum has turned pink from a small amount of free hemoglobin."
  ],
  "qd": "A sample in which a clot has formed in the tube, usually from underfilling, poor mixing, or delayed inversion.",
  "qw": [
   "A sample that has separated into layers because it was left upright for too long at room temperature.",
   "A sample that is perfectly liquid but darker than normal because of the anticoagulant used.",
   "A sample in which the serum has turned pink from a small amount of free hemoglobin."
  ],
  "e": "Clotted samples are unsuitable for many tests. The handout and CLSI PRE02 describe proper mixing and filling.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What does a rejected specimen mean?",
  "d": "A specimen the lab will not test because it is mislabeled, unsuitable, or compromised, so it must be recollected.",
  "c": 5,
  "w": [
   "A specimen the lab will test but with a note that the result may be reported late.",
   "A specimen that was collected correctly but was sent to the wrong department for testing.",
   "A specimen that is held for two extra days in case the physician changes the order."
  ],
  "qd": "A specimen the lab will not test because it is mislabeled or compromised, so it must be redrawn.",
  "qw": [
   "A specimen the lab tests with a note that the result may be reported late to the provider.",
   "A specimen collected correctly but sent to the wrong department for testing by mistake.",
   "A specimen held for two extra days in case the physician changes the order."
  ],
  "e": "Rejected specimens require recollection, which is why proper identification and collection technique matter.",
  "u": "https://clsi.org/shop/standards/pre02/",
  "s": "CLSI PRE02: Venipuncture (replaces GP41)"
 },
 {
  "t": "What is the antecubital fossa?",
  "d": "The bend of the arm opposite the elbow where the median cubital, cephalic, and basilic veins lie close to the surface.",
  "c": 6,
  "w": [
   "The inner wrist, where the radial artery and the cephalic vein run side by side.",
   "The back of the hand, where the dorsal venous network lies just under the skin.",
   "The outer thigh, where the great saphenous vein runs beneath the skin of the leg."
  ],
  "qd": "The bend of the arm opposite the elbow, where the median cubital, cephalic, and basilic veins lie.",
  "qw": [
   "The inner wrist, where the radial artery and the cephalic vein run side by side.",
   "The back of the hand, where the dorsal venous network lies just under the skin.",
   "The outer thigh, where the great saphenous vein runs beneath the skin of the leg."
  ],
  "e": "The test plan lists phlebotomy-related vascular anatomy, including the antecubital fossa, hand, and foot.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What are the main blood components a phlebotomist should know?",
  "d": "Plasma, red blood cells, white blood cells, and platelets, with serum as the fluid left after clotting.",
  "c": 6,
  "w": [
   "Plasma, bile, lymph, and cerebrospinal fluid, each carried in a separate circulation loop.",
   "Red blood cells, bone, cartilage, and synovial fluid, the four tissues that make up the marrow.",
   "White blood cells, nerve tissue, muscle fibers, and fat, the four main tissue types of the body."
  ],
  "qd": "Plasma, red blood cells, white blood cells, and platelets, with serum as the fluid left after clotting.",
  "qw": [
   "Plasma, bile, lymph, and cerebrospinal fluid, each carried in a separate circulation loop.",
   "Red blood cells, bone, cartilage, and synovial fluid, the four tissues that make up the marrow.",
   "White blood cells, nerve tissue, muscle fibers, and fat, the four main tissue types of the body."
  ],
  "e": "Blood components, including serum, plasma, whole blood, red cells, white cells, and platelets, are a test plan knowledge item.",
  "u": "https://medlineplus.gov/blood.html",
  "s": "MedlinePlus: Blood"
 },
 {
  "t": "Which system classifies human blood into A, B, AB, and O types?",
  "d": "The ABO blood group system, defined by the antigens on red blood cells.",
  "c": 6,
  "w": [
   "The Rh system, defined by the proteins that appear in the plasma after centrifugation.",
   "The white cell count system, defined by the number of white cells on a CBC.",
   "The clotting scale, defined by the time a sample takes to form a clot in the tube."
  ],
  "qd": "The ABO blood group system, defined by the antigens on red blood cells.",
  "qw": [
   "The Rh system, defined by the proteins that appear in the plasma after centrifugation.",
   "The white cell count system, defined by the number of white cells on a CBC.",
   "The clotting scale, defined by the time a sample takes to form a clot in the tube."
  ],
  "e": "Blood group systems, including ABO and Rh, are a knowledge item in the test plan.",
  "u": "https://medlineplus.gov/ency/article/003345.htm",
  "s": "MedlinePlus: Blood Typing"
 },
 {
  "t": "Which blood type is the universal donor for red cell transfusion?",
  "d": "Type O red cells.",
  "c": 6,
  "w": [
   "Type AB red cells, since they contain both A and B antigens and are compatible with all.",
   "Type A red cells, since they are the most common blood type in the general population.",
   "Type B red cells, since they contain no antigens that can trigger an immune response."
  ],
  "qd": "Type O red cells.",
  "qw": [
   "Type AB red cells, since they contain both A and B antigens and are compatible with all.",
   "Type A red cells, since they are the most common blood type in the general population.",
   "Type B red cells, since they contain no antigens that can trigger an immune response."
  ],
  "e": "Type O red cells lack A and B antigens, so they can be given to most recipients. Type AB recipients can receive all types.",
  "u": "https://medlineplus.gov/ency/article/003345.htm",
  "s": "MedlinePlus: Blood Typing"
 },
 {
  "t": "What does the Rh factor refer to?",
  "d": "The D antigen on red blood cells. Blood with it is Rh-positive, and blood without it is Rh-negative.",
  "c": 6,
  "w": [
   "A white cell protein that rises during infection and is used to diagnose bacterial pneumonia.",
   "A clotting factor made in the liver that is required for normal wound healing after a draw.",
   "A plasma hormone that controls the body's response to dehydration and thirst."
  ],
  "qd": "The D antigen on red blood cells. Blood with it is Rh-positive, and blood without it is Rh-negative.",
  "qw": [
   "A white cell protein that rises during infection and is used to diagnose bacterial pneumonia.",
   "A clotting factor made in the liver that is required for normal wound healing after a draw.",
   "A plasma hormone that controls the body's response to dehydration and thirst."
  ],
  "e": "The Rh factor is a red cell antigen. Rh incompatibility matters in transfusion and pregnancy.",
  "u": "https://medlineplus.gov/ency/article/003345.htm",
  "s": "MedlinePlus: Blood Typing"
 },
 {
  "t": "What is the cephalic vein?",
  "d": "A superficial vein on the outer side of the arm, usually the second choice for venipuncture.",
  "c": 6,
  "w": [
   "A deep vein of the leg that is used only for surgical access and not for routine draws.",
   "A vein in the neck that is used for central line placement and never for routine draws.",
   "An artery at the wrist that is used for arterial blood gas sampling in the emergency room."
  ],
  "qd": "A superficial vein on the outer side of the arm, usually the second choice for venipuncture.",
  "qw": [
   "A deep vein of the leg that is used only for surgical access and not for routine draws.",
   "A vein in the neck that is used for central line placement and never for routine draws.",
   "An artery at the wrist that is used for arterial blood gas sampling in the emergency room."
  ],
  "e": "The cephalic vein is one of the vessels the test plan asks candidates to know for phlebotomy.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "Why is the basilic vein used last for venipuncture?",
  "d": "It lies near the brachial artery and median nerve, so the risk of injury is higher.",
  "c": 6,
  "w": [
   "It is the largest vein in the arm, so the tourniquet slips off it more easily during a draw.",
   "It runs along the surface of the forearm, so it is easily damaged by the tourniquet.",
   "It drains only the hand, so it is used mainly for capillary draws in infants."
  ],
  "qd": "It lies near the brachial artery and median nerve, so the risk of injury is higher.",
  "qw": [
   "It is the largest vein in the arm, so the tourniquet slips off it more easily during a draw.",
   "It runs along the surface of the forearm, so it is easily damaged by the tourniquet.",
   "It drains only the hand, so it is used mainly for capillary draws in infants."
  ],
  "e": "The basilic vein sits close to the brachial artery and median nerve, which is why it is the last choice.",
  "u": "https://medlineplus.gov/ency/article/003423.htm",
  "s": "MedlinePlus: Venipuncture"
 },
 {
  "t": "What is hemostasis?",
  "d": "The process that stops bleeding after an injury, through vessel constriction, platelet plugs, and clotting.",
  "c": 6,
  "w": [
   "The process that transports oxygen from the lungs to the body's tissues through the arteries.",
   "The process that digests food in the stomach and small intestine into absorbable nutrients.",
   "The process that filters waste from the blood in the kidneys and passes it into the bladder."
  ],
  "qd": "The process that stops bleeding after an injury, through vessel constriction, platelet plugs, and clotting.",
  "qw": [
   "The process that transports oxygen from the lungs to the body's tissues through the arteries.",
   "The process that digests food in the stomach and small intestine into absorbable nutrients.",
   "The process that filters waste from the blood in the kidneys and passes it into the bladder."
  ],
  "e": "Hemostasis describes the body's stop-bleeding response, which the handout and the lab coagulation tests reflect.",
  "u": "https://medlineplus.gov/blood.html",
  "s": "MedlinePlus: Blood"
 },
 {
  "t": "What is the coagulation cascade?",
  "d": "A sequence of clotting factor reactions that converts fibrinogen into fibrin to form a stable clot.",
  "c": 6,
  "w": [
   "A sequence of red cell reactions that releases oxygen into the tissues at the site of an injury.",
   "A sequence of white cell reactions that digests bacteria inside the blood vessel wall.",
   "A sequence of hormone reactions that raise blood pressure after a loss of blood volume."
  ],
  "qd": "A sequence of clotting factor reactions that converts fibrinogen into fibrin to form a stable clot.",
  "qw": [
   "A sequence of red cell reactions that releases oxygen into the tissues at the site of an injury.",
   "A sequence of white cell reactions that digests bacteria inside the blood vessel wall.",
   "A sequence of hormone reactions that raise blood pressure after a loss of blood volume."
  ],
  "e": "Coagulation tests such as PT and aPTT measure parts of this cascade, which is why additive carryover matters.",
  "u": "https://medlineplus.gov/blood.html",
  "s": "MedlinePlus: Blood"
 },
 {
  "t": "Which ethical principle requires that patient information be kept private?",
  "d": "Confidentiality, which protects patient information from unauthorized disclosure.",
  "c": 6,
  "w": [
   "Beneficence, which requires providers to act for the patient's benefit in every decision made.",
   "Autonomy, which requires providers to follow the patient's wishes about the time of the draw.",
   "Justice, which requires providers to distribute resources fairly across all patient groups."
  ],
  "qd": "Confidentiality, which protects patient information from unauthorized disclosure.",
  "qw": [
   "Beneficence, which requires providers to act for the patient's benefit in every decision made.",
   "Autonomy, which requires providers to follow the patient's wishes about the time of the draw.",
   "Justice, which requires providers to distribute resources fairly across all patient groups."
  ],
  "e": "The AMA ethics code describes confidentiality as a core obligation of medical practice.",
  "u": "https://www.ama-assn.org/about/ethics",
  "s": "AMA: Ethics"
 },
 {
  "t": "What does professionalism include for a phlebotomy technician?",
  "d": "Integrity, punctuality, etiquette, respect, and a professional presentation.",
  "c": 6,
  "w": [
   "Owning the most advanced equipment, paying for continuing education, and wearing a uniform in all settings.",
   "Working the fastest shift, drawing the most patients, and taking the fewest breaks each day.",
   "Speaking only to physicians, avoiding all patient questions, and keeping the lab door closed."
  ],
  "qd": "Integrity, punctuality, etiquette, respect, and a professional presentation.",
  "qw": [
   "Owning the most advanced equipment, paying for continuing education, and wearing a uniform in all settings.",
   "Working the fastest shift, drawing the most patients, and taking the fewest breaks each day.",
   "Speaking only to physicians, avoiding all patient questions, and keeping the lab door closed."
  ],
  "e": "The test plan lists professionalism, including integrity, punctuality, etiquette, respect, and professional presentation.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is culturally competent communication?",
  "d": "Showing respect for diversity, using clear language, and adjusting to the patient's cultural and language needs.",
  "c": 6,
  "w": [
   "Using medical jargon consistently with all patients, so that each conversation is precise and brief.",
   "Speaking loudly to all patients who appear to be from another country to make sure they hear you.",
   "Asking every patient to explain their religion before the draw to confirm the correct protocol."
  ],
  "qd": "Showing respect for diversity, using clear language, and adjusting to the patient's cultural and language needs.",
  "qw": [
   "Using medical jargon consistently with all patients, so that each conversation is precise and brief.",
   "Speaking loudly to all patients who appear to be from another country to make sure they hear you.",
   "Asking every patient to explain their religion before the draw to confirm the correct protocol."
  ],
  "e": "The test plan lists demonstrating respect for diversity and cultural sensitivity as a patient preparation task.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is active listening?",
  "d": "Giving full attention, confirming understanding, and responding with empathy to a patient's concerns.",
  "c": 6,
  "w": [
   "Repeating the patient's words back exactly, without asking any questions to clarify their meaning.",
   "Reading the requisition aloud to the patient so they can follow along during the draw.",
   "Interrupting the patient to explain the procedure before they finish describing the concern."
  ],
  "qd": "Giving full attention, confirming understanding, and responding with empathy to a patient's concerns.",
  "qw": [
   "Repeating the patient's words back exactly, without asking any questions to clarify their meaning.",
   "Reading the requisition aloud to the patient so they can follow along during the draw.",
   "Interrupting the patient to explain the procedure before they finish describing the concern."
  ],
  "e": "Verbal and nonverbal communication, including active listening, is a knowledge item in the test plan.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What should be documented after a patient incident during a draw?",
  "d": "What happened, the time, the interventions and their timing, the patient's response, and the completed incident report.",
  "c": 6,
  "w": [
   "Only the patient's name and the test ordered, since the incident is handled by the nurse.",
   "Nothing, if the patient recovers before the end of the shift, to protect the facility's reputation.",
   "The incident in a personal notebook kept at home, to avoid review by coworkers."
  ],
  "qd": "What happened, the time, the interventions and their timing, the patient's response, and the completed incident report.",
  "qw": [
   "Only the patient's name and the test ordered, since the incident is handled by the nurse.",
   "Nothing, if the patient recovers before the end of the shift, to protect the facility's reputation.",
   "The incident in a personal notebook kept at home, to avoid review by coworkers."
  ],
  "e": "The test plan lists documentation and reporting requirements, including patient-related incidents and charting guidelines.",
  "u": "https://www.ahrq.gov/patient-safety/index.html",
  "s": "AHRQ: Patient Safety"
 },
 {
  "t": "What is a practice management system?",
  "d": "Software used for scheduling, billing, records, and related office tasks in a medical practice.",
  "c": 6,
  "w": [
   "A set of rules for cleaning the lab bench at the end of each shift, posted on the wall.",
   "A type of centrifuge that separates blood cells by size instead of density.",
   "A patient-facing app that lets patients choose their own tubes before the draw."
  ],
  "qd": "Software used for scheduling, billing, records, and related office tasks in a medical practice.",
  "qw": [
   "A set of rules for cleaning the lab bench at the end of each shift, posted on the wall.",
   "A type of centrifuge that separates blood cells by size instead of density.",
   "A patient-facing app that lets patients choose their own tubes before the draw."
  ],
  "e": "The test plan lists practice management systems, EMR and EHR software, and paper logs as tools for the role.",
  "u": "https://info.nhanow.com/hubfs/Test%20Plans/nha-2025-cpt-test-plan.pdf",
  "s": "NHA: CPT Test Plan (2025)"
 },
 {
  "t": "What is an electronic health record?",
  "d": "A digital record of a patient's health information, including orders, results, and notes.",
  "c": 6,
  "w": [
   "A paper form that lists each lab test that the facility has discontinued this year.",
   "A list of employee schedules, kept by human resources for payroll purposes.",
   "A booklet of drug interactions, kept at the nurses' station for quick reference."
  ],
  "qd": "A digital record of a patient's health information, including orders, results, and notes.",
  "qw": [
   "A paper form that lists each lab test that the facility has discontinued this year.",
   "A list of employee schedules, kept by human resources for payroll purposes.",
   "A booklet of drug interactions, kept at the nurses' station for quick reference."
  ],
  "e": "Electronic health records hold the patient information that the HIPAA Privacy Rule protects.",
  "u": "https://www.hhs.gov/hipaa/for-professionals/privacy/index.html",
  "s": "HHS: HIPAA Privacy"
 },
 {
  "t": "What does the HIPAA right of access allow a patient to do?",
  "d": "Request copies of their health records, which the provider must provide within 30 calendar days, with one extension of up to 30 more days.",
  "c": 6,
  "w": [
   "Request that their records be destroyed within seven days of any test, with no copies provided.",
   "Request that the lab send results only to the patient's employer, who must then approve them.",
   "Request access only to records created by a physician, with no access to lab results allowed."
  ],
  "qd": "Copies of health records, which the provider must supply within 30 days, with one extension of 30 more days.",
  "qw": [
   "Destruction of records within seven days of any test, with no copies provided to the patient.",
   "Results sent only to the patient's employer, who must approve them before release.",
   "Access only to physician notes, with no access to laboratory results allowed at all."
  ],
  "e": "HHS sets a 30-day limit for access, with one extension of up to 30 days if the patient is notified in writing.",
  "u": "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access/index.html",
  "s": "HHS: Right of Access (45 CFR 164.524)"
 },
 {
  "t": "What is the purpose of a Notice of Privacy Practices?",
  "d": "To describe how a provider may use and disclose protected health information, and the patient's rights.",
  "c": 6,
  "w": [
   "To list the prices of all lab tests so the patient can compare costs before the draw.",
   "To tell the patient which staff members are allowed to see their records without consent.",
   "To provide a list of tube colors the patient may choose during the venipuncture."
  ],
  "qd": "How a provider may use and disclose protected health information, and the patient's privacy rights.",
  "qw": [
   "The prices of all lab tests, so the patient can compare costs before the draw is done.",
   "Which staff members may see records without consent, so the patient knows who has access.",
   "A list of tube colors the patient may choose from during the venipuncture procedure."
  ],
  "e": "HHS publishes a model Notice of Privacy Practices that providers use to explain patient privacy rights.",
  "u": "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/privacy-practices-health-care-provider/index.html",
  "s": "HHS: Model Notice of Privacy Practices"
 }
];
