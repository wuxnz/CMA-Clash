# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-osha-bbp)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [

    # skill-osha-bbp-001
    fact(
        "skill-osha-bbp",
        "Which body fluids are covered by OSHA's Bloodborne Pathogens Standard in typical healthcare exposure?",
        "Blood and other potentially infectious materials such as semen and CSF",
        [
            "Blood along with every body fluid a patient produces, including sweat and tears",
            "Blood confirmed by the laboratory as carrying a bloodborne pathogen",
            "Urine, feces, and sputum whenever they are collected in a clinic",
        ],
        "The standard covers blood and specified other potentially infectious materials such as semen and cerebrospinal fluid. Sweat, tears, and ordinary urine or feces fall outside the standard unless blood or other infectious material is present.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-002
    fact(
        "skill-osha-bbp",
        "What is an employer's duty regarding hepatitis B vaccination under the Bloodborne Pathogens Standard?",
        "Offer the vaccine at no cost to employees with occupational exposure risk",
        [
            "Charge employees the cost of the series when they work part time",
            "Provide the vaccine after a needlestick injury has been documented and evaluated",
            "Require vaccination for every person who enters the building",
        ],
        "Employees with occupational exposure risk must be offered hepatitis B vaccination free of charge. Charging employees, limiting the offer to post-exposure events, or extending it to visitors does not meet the standard.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-003
    fact(
        "skill-osha-bbp",
        "What must be included in an exposure control plan for bloodborne pathogens?",
        "Exposure determination, controls, protective equipment, and post-exposure care",
        [
            "Exposure determination, training dates, and a supply budget for protective gear",
            "Engineering controls, work practice controls, and a list of decliners",
            "Post-exposure follow-up steps, reporting forms, and the training calendar",
        ],
        "OSHA expects a written plan that ties each identified hazard to controls, protective equipment, and post-exposure follow-up. Training dates, declination lists, and reporting forms cover only pieces of the required plan.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-004
    fact(
        "skill-osha-bbp",
        "When should employees receive bloodborne pathogen training?",
        "At hire, annually thereafter, and when tasks or procedures change",
        [
            "At hire and annually, with no refresher when job duties or devices change",
            "Once at hire, with annual updates handled by the employee reading policy changes",
            "Annually, with the initial session deferred until the first exposure incident",
        ],
        "OSHA requires initial training, annual retraining, and added sessions when tasks or procedures change. Deferring the first session, relying on self-review, or skipping duty-based refreshers leaves staff unprepared.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-005
    fact(
        "skill-osha-bbp",
        "What is the purpose of engineering controls for sharps injury prevention?",
        "Remove or isolate the hazard with safety needles and sharps containers",
        [
            "Reduce the hazard by changing the work sequence so sharps are handled less often",
            "Reduce the hazard by adding equipment that shields the hands",
            "Reduce the hazard by training staff to recognize injuries soon after they happen",
        ],
        "Engineering controls physically remove or isolate the hazard, for example safety needles and puncture-resistant containers. Changing the work sequence is a work practice control, and gloves are personal protective equipment.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-006
    fact(
        "skill-osha-bbp",
        "How should contaminated sharps be discarded under OSHA rules?",
        "Immediately in closable, puncture-resistant, labeled containers",
        [
            "In a lined exam room trash can once the needle has been recapped",
            "On a procedure tray until the room is cleaned at the end of the shift",
            "In a rigid container kept in the supply room until it is full",
        ],
        "Sharps go into approved puncture-resistant containers right after use, which limits handling and prevents needlesticks. Recapping, delaying disposal, and storing sharps in a supply room each shift the risk onto staff.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-007
    fact(
        "skill-osha-bbp",
        "What PPE is required when blood splash to the eyes is reasonably anticipated?",
        "Eye protection such as goggles or a face shield plus other needed PPE",
        [
            "A surgical mask and gloves because splash exposure is limited to droplets",
            "Eye protection alone, since nothing else blocks blood from reaching the eye",
            "Gloves alone, because mucous membrane exposure is not addressed by PPE",
        ],
        "Blood splash to the eyes requires eye protection, and mucous membrane exposure is covered by the standard. Gloves protect hands rather than eyes, and protective equipment is matched to the task instead of used alone.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-008
    fact(
        "skill-osha-bbp",
        "When may employers require employees to pay for their own hepatitis B vaccination series?",
        "They may not require payment when vaccination is offered for exposure",
        [
            "When the employee declines the vaccine in writing after the offer is made",
            "When the employee works part time with fewer than twenty hours",
            "When the clinic is privately owned rather than part of a hospital",
        ],
        "The standard prohibits charging employees for an employer-offered hepatitis B series. A written declination documents refusal, but the offer itself must remain free of charge in every case.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-osha-bbp-009
    fact(
        "skill-osha-bbp",
        "What should an employee do immediately after a needlestick with a used patient needle?",
        "Wash the area, report the exposure promptly, and seek medical evaluation",
        [
            "Wash the area, finish the draw, and report the stick before the end of the shift",
            "Apply an antiseptic wipe and record the injury in the employee health record",
            "Squeeze the wound to stop bleeding, then return to patient care",
        ],
        "Immediate washing, prompt reporting, and medical evaluation start the post-exposure timeline and may open the prophylaxis window. Waiting until end of shift, charting it outside the exposure process, or staying silent delays evaluation.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-010
    fact(
        "skill-osha-bbp",
        "What information belongs in the OSHA sharps injury log?",
        "The type and brand of the sharps involved and the work area where it happened",
        [
            "The patient's diagnosis, insurance status, and the length of the clinic visit",
            "The employee's salary, shift schedule, and most recent performance review",
            "The laboratory results of the source patient after the testing is completed",
        ],
        "The sharps injury log records device type, device brand, and the department where the incident occurred so employers can evaluate safer devices. Patient billing, employee performance data, and source lab results do not belong in that log.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-011
    fact(
        "skill-osha-bbp",
        "What does work practice control mean in the Bloodborne Pathogens Standard?",
        "Policies and behaviors such as no recapping and hand hygiene that reduce risk",
        [
            "Devices and equipment that physically block contact with blood or other fluids",
            "Orientation sessions and training that teach staff about bloodborne pathogens",
            "Protective equipment worn on the hands and body during most patient procedures",
        ],
        "Work practice controls are the behaviors and procedures that reduce exposure, such as not recapping and performing hand hygiene. Devices that block contact are engineering controls, gloves or gowns are personal protective equipment, and orientation sessions are administrative controls.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-012
    fact(
        "skill-osha-bbp",
        "Under OSHA rules, when is manual recapping of a used needle acceptable?",
        "When a one-handed scoop technique or an approved recapping device is used",
        [
            "When two hands are used and the procedure is finished within the same minute",
            "When the needle is smaller than 20 gauge and the procedure is nearly over",
            "When the sharps container is full and the needle has already been removed",
        ],
        "Recapping by hand is acceptable only with a one-handed scoop technique or a mechanical recapping device. Speed, needle size, and a full container do not create exceptions, and two-handed recapping is a leading cause of needlesticks.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-013
    fact(
        "skill-osha-bbp",
        "How should biohazard-labeled laundry be handled before leaving the facility?",
        "Bagged without rinsing or sorting in a leak-resistant container for laundering",
        [
            "Bagged after sorting by color so soiled and clean linen items are separated",
            "Handled in a leak-resistant container and laundered on site later that evening",
            "Placed in a standard hamper after the blood has been blotted with paper towels",
        ],
        "Contaminated linen is bagged without rinsing or sorting and handed to an approved laundry service. Sorting soiled items, laundering on site, or blotting blood before bagging creates splash and handling exposure.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-osha-bbp-014
    fact(
        "skill-osha-bbp",
        "What information should post-exposure evaluation include after a blood splash to nonintact skin?",
        "Source patient status, baseline labs, and a follow-up testing schedule",
        [
            "Baseline labs, a follow-up testing schedule, and the billing account number",
            "Source patient status, the employee's insurance plan, and the billing code",
            "Baseline labs, the incident narrative, and the department of the stick",
        ],
        "Post-exposure evaluation documents the exposure route, the source patient status if known, baseline labs, and the follow-up schedule. Billing details and workplace details support recordkeeping but do not guide prophylaxis decisions.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-osha-bbp-015
    fact(
        "skill-osha-bbp",
        "Which pathogens are commonly emphasized in bloodborne pathogen training?",
        "HIV, hepatitis B, and hepatitis C",
        [
            "HIV, hepatitis B, and influenza",
            "Hepatitis A, hepatitis C, and HIV",
            "Hepatitis B, tuberculosis, and HIV",
        ],
        "Training centers on the viruses that are reliably transmitted by blood exposure in healthcare: HIV, hepatitis B, and hepatitis C. Influenza, hepatitis A, and tuberculosis follow different routes and are not the focus of bloodborne pathogen training.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-016
    fact(
        "skill-osha-bbp",
        "What does universal precautions mean in OSHA bloodborne pathogen context?",
        "Treat all blood and certain body fluids as potentially infectious",
        [
            "Treat body fluids confirmed by laboratory testing as potentially infectious",
            "Treat all body fluids a patient produces as potentially infectious",
            "Treat blood as infectious when the source patient has a known diagnosis",
        ],
        "Universal precautions treat all blood and specified potentially infectious materials as infectious without waiting for a diagnosis. Confirmed fluids, every body fluid, and diagnosis-based decisions each narrow or shift the scope of the standard.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-osha-bbp-017
    fact(
        "skill-osha-bbp",
        "When must personal protective equipment be provided to employees?",
        "At no cost whenever it is needed for occupational exposure to blood or OPIM",
        [
            "At no cost for tasks that the employee has already performed for one year",
            "At the employee's cost when the task involves blood from a known positive source",
            "When the employee has completed bloodborne pathogen training for the task",
        ],
        "Employers must supply appropriate protective equipment at no cost whenever it is needed for covered tasks. A service period, employee payment, or completion of training does not change the employer's duty to provide it.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-018
    fact(
        "skill-osha-bbp",
        "How should regulated waste be labeled for transport within the facility?",
        "With a biohazard symbol on red bags or containers where required",
        [
            "With a biohazard symbol on a clear bag so the contents stay visible",
            "With a written label listing the patient name and the room number",
            "With the department name on the outside of the red bag",
        ],
        "Regulated waste containers and bags carry the biohazard symbol where required so handlers recognize the hazard. Clear bags, patient identifiers, and department names do not meet labeling requirements.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-019
    fact(
        "skill-osha-bbp",
        "What is the role of hepatitis B surface antibody testing after vaccination?",
        "To document the immune response for occupational health programs",
        [
            "To confirm the employee may safely reuse a needle between patients",
            "To document the status so gloves may be skipped on later blood draws",
            "To show that annual bloodborne pathogen training is no longer required",
        ],
        "Surface antibody testing documents immune response after vaccination when occupational health recommends it. It does not authorize needle reuse, waive glove use, or remove the ongoing training requirement.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-osha-bbp-020
    fact(
        "skill-osha-bbp",
        "Why should employees avoid bending or shearing needles before disposal?",
        "Breaking needles increases splash and stick risk without a safety benefit",
        [
            "Bending needles makes them easier to fit into smaller sharps containers",
            "Shearing a needle removes the blood that would otherwise contaminate the cap",
            "Bent needles are easier to identify when the container is overfilled",
        ],
        "Manipulating used needles causes unpredictable fractures, splashes, and aerosols. Container fit, perceived contamination, and visual identification are not reasons to bend or shear a needle.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "intermediate",
    ),
    # skill-osha-bbp-021
    fact(
        "skill-osha-bbp",
        "What should happen to a sharps container when it is three-quarters full?",
        "It should be closed and replaced before sharps start protruding",
        [
            "It should be replaced once it is completely full and sealed",
            "It should be sealed with tape so no additional sharps can be added",
            "It should be emptied into a larger waste bin on the same unit",
        ],
        "Containers are replaced before they are overfilled because protruding sharps cause needlesticks during disposal. Waiting for a full container, taping it shut, and emptying it into a waste bin all leave the risk in place.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-022
    fact(
        "skill-osha-bbp",
        "How should sealed sharps containers be moved through the facility?",
        "In a closed cart or carrier so leaks stay contained in transit",
        [
            "In an open basket on a cart so handlers can see the container",
            "On a treatment cart where the container sits beside the supplies",
            "In a laundry hamper with the soiled linen for the unit",
        ],
        "Sealed sharps containers travel in a closed cart or carrier so a cracked tube cannot leak into public areas. Open baskets, treatment carts, and linen hampers let containers tip, leak, or be handled as ordinary waste.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-023
    fact(
        "skill-osha-bbp",
        "Which routes of contact with blood or OPIM count as occupational exposure?",
        "Skin, eye, mucous membrane, and parenteral routes with anticipated contact",
        [
            "Contact with a patient who has a confirmed bloodborne pathogen infection",
            "A task in a clinical setting that involves handling specimens or blood products",
            "An injury sustained in the workplace, such as a slip, fall, or strain",
        ],
        "Occupational exposure covers reasonably anticipated skin, eye, mucous membrane, or parenteral contact with blood or other potentially infectious materials. It is not limited to patients with known infections, to every specimen task, or to workplace injuries of any kind.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-024
    fact(
        "skill-osha-bbp",
        "When may an employee decline hepatitis B vaccination offered by the employer?",
        "After receiving mandated training and signing a declination form",
        [
            "After attending training, without written documentation of the refusal",
            "After the employee's supervisor confirms the refusal in the shift schedule",
            "After the employee tells the employer the series is not medically appropriate",
        ],
        "An employee may decline after mandated training, and the refusal must be documented in writing. Verbal refusals, supervisor notes, and medical judgments do not substitute for the signed declination form.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-025
    fact(
        "skill-osha-bbp",
        "How should blood on intact clinic flooring be cleaned?",
        "Wearing PPE, absorbing the spill, cleaning it, then disinfecting it",
        [
            "Absorbing the spill, then disinfecting the area with a germicide",
            "Cleaning the floor with a disinfectant first, then mopping up the blood",
            "Placing a wet floor sign over the spill until the nightly cleaning rounds",
        ],
        "OSHA expects prompt cleanup with protective equipment, absorbent material, cleaning, and an EPA-registered disinfectant. Skipping protective equipment, cleaning before absorbing, and leaving the spill under a sign all leave blood on the floor for longer.",
        [S.OSHA_BBP, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-osha-bbp-026
    fact(
        "skill-osha-bbp",
        "What is the purpose of evaluating safer medical devices in a facility?",
        "To select and implement needles and sharps with engineered injury protection",
        [
            "To document that device-related injuries have reached an acceptable level",
            "To compare the purchase cost of each device before it enters the supply room",
            "To reduce the number of safety-engineered devices carried in the exam rooms",
        ],
        "Employers evaluate and implement devices with engineered sharps injury protection, and frontline staff contribute to the selection. Injury tallies, purchase price, and smaller inventories do not replace the safety evaluation.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-osha-bbp-027
    fact(
        "skill-osha-bbp",
        "Which action violates work practice controls during phlebotomy?",
        "Placing used needles on the bedspread while changing tubes",
        [
            "Using a safety needle with audible activation after the draw",
            "Discarding the holder and needle as a unit at the point of use",
            "Performing hand hygiene after removing gloves at the end of the draw",
        ],
        "Work practice controls govern how tasks are performed, and leaving used needles on soft surfaces is a documented violation. Safety devices, immediate disposal as a unit, and hand hygiene after glove removal are all expected practice.",
        [S.OSHA_BBP, S.CLSI_GP41],
        "intermediate",
    ),
    # skill-osha-bbp-028
    fact(
        "skill-osha-bbp",
        "How long must employers retain documentation of bloodborne pathogen training?",
        "At least three years from the date the training was provided",
        [
            "Until the employee's next scheduled annual performance review",
            "For one year after the employee leaves the organization or clinic",
            "For the calendar year in which the training session was completed",
        ],
        "OSHA requires training records to be kept at least three years from the date of training. One year after separation, a single calendar year, and the length of the position do not meet the retention minimum.",
        [S.OSHA_BBP],
        "advanced",
    ),
    # skill-osha-bbp-029
    fact(
        "skill-osha-bbp",
        "What should be done with PPE that is torn during a bloody procedure?",
        "Removing it, performing hand hygiene, and donning intact PPE before continuing",
        [
            "Taping the tear, then completing the task before changing into intact PPE",
            "Swapping the torn item for clean scrubs and completing the procedure in them",
            "Finishing the procedure in the torn gown and changing after the patient leaves",
        ],
        "Compromised barriers are removed and replaced with intact protective equipment, with hand hygiene between. Scrubs, tape, and finishing a procedure in a torn gown leave the staff exposed.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-030
    fact(
        "skill-osha-bbp",
        "Why are eating and drinking restricted in areas where blood specimens are processed?",
        "To prevent ingestion of pathogens from contaminated surfaces or aerosols",
        [
            "To keep refrigerator temperatures stable for stored staff meals and drinks",
            "To reduce spills that could damage equipment sitting near the centrifuge",
            "To keep work surfaces clear for sorting, labeling, and packing specimens",
        ],
        "Food and drink in specimen areas can be contaminated by splashes, aerosols, or unwashed hands, and ingesting pathogens is the risk. Refrigeration, equipment protection, and workspace organization are not the reason for the restriction.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-osha-bbp-031
    fact(
        "skill-osha-bbp",
        "What does parenteral exposure mean in needlestick context?",
        "Entry through piercing of the skin, including a needle puncture",
        [
            "Inhalation of airborne particles while working in a specimen processing area",
            "Splash of blood onto the mucous membranes of the mouth or nose",
            "Contact of blood with nonintact skin such as an open abrasion",
        ],
        "Parenteral exposure means the percutaneous route, where a sharp or needle pierces skin and reaches tissue or blood directly. Airborne entry, mucous membrane splash, and contact with broken skin are separate exposure routes with different evaluation.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-032
    fact(
        "skill-osha-bbp",
        "When should gloves be worn under the Bloodborne Pathogens Standard?",
        "When contact with blood, OPIM, mucous membranes, or nonintact skin is expected",
        [
            "When the patient has a known bloodborne pathogen infection or an unknown status",
            "When the task involves a specimen that might contain blood or OPIM",
            "When the employee has completed training for the patient unit",
        ],
        "Gloves are used when contact with blood, other potentially infectious materials, mucous membranes, or nonintact skin is reasonably anticipated. Known infection status, sealed specimens, and completed training do not define when gloves are required.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-033
    fact(
        "skill-osha-bbp",
        "How should employers respond when an employee requests safer sharps devices?",
        "Evaluate the request and implement safer devices in the plan",
        [
            "Evaluate the request, document it, and keep the current devices",
            "Wait for the annual injury count to reach a threshold first",
            "Refer the request to purchasing for a price and contract comparison first",
        ],
        "OSHA requires employers to evaluate requests for safer sharps and to implement appropriate devices as part of the exposure control plan. Documenting a decision without change, waiting for injury counts, and shopping on price do not satisfy the requirement.",
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK],
        "advanced",
    ),
    # skill-osha-bbp-034
    fact(
        "skill-osha-bbp",
        "What must the hepatitis B vaccine declination form document?",
        "That the employee understands the risks and was offered the vaccination series",
        [
            "That the employee's supervisor approved the refusal before the form was signed",
            "That the employee will receive the series at the next annual physical",
            "That the employee's personal physician advised against vaccination",
        ],
        "The declination form documents that the employee understands the risks and had the vaccination offered, which is what makes the refusal informed. Supervisor approval, a promise to vaccinate later, and physician advice are not what the form records.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-035
    fact(
        "skill-osha-bbp",
        "Which practice reduces risk when passing sharps between team members?",
        "Using a neutral zone or a tray instead of hand-to-hand transfer",
        [
            "Announcing each instrument so the receiving clinician is prepared",
            "Passing the instrument through the doorway to avoid anyone crossing the room",
            "Wiping the instrument between staff members before it is handed over",
        ],
        "Neutral zones and tray placement keep both hands visible and away from sharp tips. Announcing instruments, passing through a doorway, and wiping between staff still require a hand-to-hand transfer of the sharp.",
        [S.OSHA_BBP, S.CDC_INJECTION_SAFETY],
        "intermediate",
    ),
    # skill-osha-bbp-036
    fact(
        "skill-osha-bbp",
        "What is required when housekeeping staff handle regulated waste?",
        "Training on the hazards and PPE that match their exposure risk",
        [
            "Training on the hazards and PPE provided at the employee's request",
            "Training on the hazards with PPE selected by the employee's own preference",
            "Training on the hazards and PPE supplied after the first exposure event",
        ],
        "Every worker whose tasks carry exposure risk, including environmental services, needs hazard training and appropriate protective equipment. Requesting it, choosing it personally, or waiting for an exposure event does not meet the training requirement.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-037
    fact(
        "skill-osha-bbp",
        "Why must exposure incidents be documented even when the source patient is unknown?",
        "Follow-up care and OSHA recordkeeping depend on timely incident reports",
        [
            "Medical evaluation is needed when the source patient is known and identified",
            "Incident reports determine which employees are disciplined after a stick",
            "Unknown-source incidents are reported after the employee leaves the clinic",
        ],
        "Wound care, baseline labs, and recordkeeping all move forward on a reported incident even when the source cannot be identified. Evaluation does not wait for source certainty, and reports are not used for discipline or delayed until separation.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "advanced",
    ),
    # skill-osha-bbp-038
    fact(
        "skill-osha-bbp",
        "What color coding is commonly used for biohazard warning labels?",
        "A fluorescent orange or orange-red background with the biohazard symbol",
        [
            "A white background with red lettering reading caution or warning",
            "A red background with black lettering naming the regulated waste stream",
            "A yellow background with the biohazard symbol printed in black",
        ],
        "OSHA specifies fluorescent orange or orange-red labels with a biohazard symbol for regulated waste containers. White, red, and yellow backgrounds are used for other hazard signs and do not carry the required biohazard marking.",
        [S.OSHA_BBP],
        "beginner",
    ),
    # skill-osha-bbp-039
    fact(
        "skill-osha-bbp",
        "How should employers make the exposure control plan available to employees?",
        "Accessible at the worksite during work hours without unnecessary delay",
        [
            "Available in the supervisor's office and released to staff on written request",
            "Available in the employee handbook as a summary with no complete written plan",
            "Available on the clinic's public website for staff to review it from home",
        ],
        "Employees must be able to review the written exposure control plan where they work, without having to request it or wait. Summaries, office-only copies, and public web postings do not meet the requirement.",
        [S.OSHA_BBP],
        "intermediate",
    ),
    # skill-osha-bbp-040
    fact(
        "skill-osha-bbp",
        "What additional step applies when blood splashes into the mouth during a procedure?",
        "Rinsing the mouth, reporting the exposure, and seeking medical evaluation",
        [
            "Rinsing the mouth, reporting the exposure, and continuing the procedure",
            "Reporting the exposure, rinsing the mouth, and waiting for the next clinic",
            "Rinsing the mouth with an antiseptic wash before leaving the procedure room",
        ],
        "A mucous membrane exposure warrants the same urgent reporting and evaluation as a needlestick. Continuing the procedure, waiting for the next clinic, and using an antiseptic rinse instead of evaluation all delay post-exposure care.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-osha-bbp-041
    fact(
        "skill-osha-bbp",
        "Which employee task typically requires inclusion in the exposure determination list?",
        "Phlebotomy and handling of specimens with visible blood",
        [
            "Scheduling appointments and confirming insurance coverage",
            "Cleaning exam rooms between patients without contact with specimens",
            "Billing insurance claims for laboratory services already completed",
        ],
        "Exposure determination lists job tasks with reasonable anticipation of blood or other infectious material contact, such as phlebotomy and handling visibly bloody specimens. Scheduling, room cleaning, and billing work do not create that contact potential.",
        [S.OSHA_BBP, S.NHA_CCMA],
        "beginner",
    ),
    # skill-osha-bbp-042
    fact(
        "skill-osha-bbp",
        "What should a medical assistant know about confidentiality after reporting a needlestick?",
        "Employer medical records stay confidential and apart from personnel files",
        [
            "The exposure details are shared with the whole unit for safety awareness",
            "The source patient's identity is posted with the report in the break room",
            "Confidentiality ends once the employee returns to work and is cleared",
        ],
        "Occupational health keeps the exposure record confidential and separate from the personnel file. Unit-wide disclosure, posting source details, and ending confidentiality at return to work each breach privacy expectations.",
        [S.OSHA_BBP, S.HHS_HIPAA_PRIVACY],
        "advanced",
    ),
]
