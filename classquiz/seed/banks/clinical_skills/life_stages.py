# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-life-stages)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-life-stages-001
    fact(
        "skill-life-stages",
        "Which measurements are plotted on a pediatric growth chart at a well-child visit?",
        "Height, weight, head circumference, and BMI plotted by age",
        [
            "Height, weight, and blood pressure plotted against the child's age",
            "Head circumference, arm circumference, and daily intake plotted by age",
            "Weight, length, and milestone timing plotted against the child's age",
        ],
        "A growth chart displays height or length, weight, head circumference, and BMI for age so trends can be followed from visit to visit. Blood pressure percentiles use a separate reference chart, and arm circumference, intake, and milestone timing belong in the visit note.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-002
    fact(
        "skill-life-stages",
        "Which findings should be recorded when examining an infant's anterior fontanelle?",
        "Size, contour, and whether it feels flat, sunken, or bulging",
        [
            "Color, warmth, and the rate of pulsation over the spot",
            "Size, contour, and the number of teeth that have erupted",
            "Shape, tenderness, and the appearance of the scalp behind the ears",
        ],
        "The anterior fontanelle is assessed for size, contour, and tension, which reflect hydration and intracranial pressure. Scalp warmth and pulsation, tooth counts, and ear findings describe other parts of the infant exam and do not document the fontanelle.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-003
    fact(
        "skill-life-stages",
        "How should confidentiality be explained to an adolescent at the start of a visit?",
        "Most topics stay private, but safety risks may require disclosure",
        [
            "All topics stay private unless the adolescent agrees to share them",
            "Guardians receive a summary of each topic discussed during the visit",
            "Confidentiality covers reproductive health questions in place of other topics",
        ],
        "Adolescents are told early which discussions stay private and that safety concerns can trigger limited disclosure. A blanket promise of secrecy ignores mandatory reporting, notifying guardians defeats the confidential visit, and limiting privacy to reproductive health misstates its scope.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-004
    fact(
        "skill-life-stages",
        "Which elements belong in a geriatric fall-risk assessment at intake?",
        "Prior falls, gait and balance, sedating medications, and home hazards",
        [
            "Prior falls, gait and balance, lipid panel results, and home hazards",
            "Prior falls, gait and balance, sedating medications, and tobacco history",
            "Prior falls, gait and balance, sedating medications, and insurance coverage",
        ],
        "Fall risk is multifactorial, so the screen captures prior falls, gait and balance, sedating medications, and home hazards. Lipid results, tobacco history, and insurance coverage are recorded elsewhere in the chart and do not screen for falls.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-life-stages-005
    fact(
        "skill-life-stages",
        "Which assessments are repeated at routine prenatal visits?",
        "Blood pressure, maternal weight, and fetal heart rate",
        [
            "Blood pressure, maternal weight, and glucose screening",
            "Blood pressure, fetal heart rate, and urine culture",
            "Maternal weight, fetal heart rate, and blood type testing",
        ],
        "Blood pressure and weight are checked at each prenatal visit to watch for hypertension and excessive gain, and fetal tones are heard once the pregnancy is far enough along. Glucose screening, urine culture, and blood typing are one-time or interval tests rather than part of every routine visit.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-006
    fact(
        "skill-life-stages",
        "Why is developmental surveillance documented at pediatric well visits?",
        "To compare milestones with age norms and refer delays early",
        [
            "To confirm that hearing and vision screening results are normal",
            "To determine the school placement that matches the child's abilities",
            "To document the immunization schedule the child has completed",
        ],
        "Surveillance compares the child's milestones with what is expected at that age and supports early referral for delay. Confirming sensory screening results, choosing school placement, and recording immunizations serve other purposes and are not the reason milestones are documented.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-007
    fact(
        "skill-life-stages",
        "How should length and weight be measured for a toddler who cannot stand without support?",
        "Use an infant or chair scale with caregiver assistance",
        [
            "Record the weight the caregiver estimated at home",
            "Measure length on the exam table and weight on the adult scale",
            "Record the measurements at the next visit when the child cooperates",
        ],
        "A toddler who cannot stand needs a scale that supports the child, and caregiver assistance keeps the child still and safe. Home estimates, exam table lengths paired with an adult scale, and deferring the measurement all produce numbers that cannot be compared reliably over time.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-008
    fact(
        "skill-life-stages",
        "Which source should clinic staff use to build a pediatric immunization schedule?",
        "The Advisory Committee on Immunization Practices schedule",
        [
            "The clinic's stock level and which vaccine lot expires first",
            "The adult immunization schedule used for patients over 19",
            "The school district's collection calendar for health forms",
        ],
        "The Advisory Committee on Immunization Practices publishes the recommended intervals and products used for pediatric scheduling. Vaccine stock levels, adult schedules, and school form calendars do not determine when a child should be immunized.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-009
    fact(
        "skill-life-stages",
        "What approach reduces anxiety before a procedure in a school-age child?",
        "Age-appropriate explanation, permission to ask questions, and distraction",
        [
            "An age-appropriate explanation, permission to ask questions, and no pain",
            "A distraction video during the procedure without prior explanation",
            "A countdown from the provider with no warning and the child held still by staff",
        ],
        "Preparation and distraction reduce fear and improve cooperation during procedures in school-age children. Promising there will be no pain sets up distrust, a video without an explanation leaves the child unprepared, and a countdown without warning adds surprise instead of preparation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-010
    fact(
        "skill-life-stages",
        "Which task belongs within MA patient education during adolescent reproductive counseling?",
        "Reviewing contraception options, STI prevention, and confidentiality limits",
        [
            "Recommending a specific contraceptive method and explaining STI prevention",
            "Explaining permanent contraception and completing the consent paperwork",
            "Deciding which method the adolescent will use and documenting STI prevention",
        ],
        "The MA educates the adolescent about contraceptive options, STI prevention, and how confidentiality works, then supports the provider's plan. Recommending a specific method, explaining permanent contraception, and deciding for the patient all exceed the assistant's scope.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-011
    fact(
        "skill-life-stages",
        "How should self-reported hearing difficulty in an older adult be handled at intake?",
        "Complete a validated hearing screen or refer for audiometry",
        [
            "Test hearing with a whisper in the busy hallway near reception",
            "Rely on the family's impression that the patient hears normally at home",
            "Defer hearing evaluation to the provider's annual review of the care plan",
        ],
        "A validated screen or audiometry referral documents the degree of hearing loss, which affects medication teaching and safety. A whisper test in a noisy hallway cannot be scored reliably, the family's impression is not a measurement, and waiting for annual review leaves the loss unaddressed.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-012
    fact(
        "skill-life-stages",
        "Which car seat setup is correct for a newborn leaving the hospital?",
        "Rear-facing car seat with a snug harness and the chest clip at armpit level",
        [
            "Forward-facing car seat with a snug harness and the chest clip at armpit height",
            "Rear-facing car seat with a loose harness and the chest clip at armpit height",
            "Rear-facing car seat with a snug harness and the chest clip at the waist",
        ],
        "Newborns travel rear-facing in a seat with a snug harness and the chest clip at armpit level, which keeps the infant positioned safely in a crash. A forward-facing seat, a loose harness, and a chest clip placed at the waist each reduce the protection the seat provides.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-life-stages-013
    fact(
        "skill-life-stages",
        "How is capillary refill time assessed in an infant during a sick visit?",
        "Press the skin until it blanches and count the seconds until color returns",
        [
            "Press the skin until it blanches and count the seconds until the limb moves",
            "Watch the color of the diaper during the visit and record the findings",
            "Press the skin until it blanches and count the seconds until the limb warms",
        ],
        "Capillary refill is judged by blanching the skin and timing the return of color, usually over the sternum or an extremity. Limb movement, diaper color, and skin temperature are separate observations and do not measure perfusion.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-014
    fact(
        "skill-life-stages",
        "Why is head circumference measured and plotted during infancy?",
        "To spot trends that suggest abnormal brain growth or fluid buildup",
        [
            "To spot trends that suggest poor weight gain or excess weight gain",
            "To spot trends that suggest an unsteady gait or delayed motor skills",
            "To spot trends that suggest anemia or poor iron intake",
        ],
        "Head circumference plotted over time shows whether brain growth is on track, and rising or falling percentiles can point to hydrocephalus or microcephaly. Weight trends, motor milestones, and anemia are judged with other measurements.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-015
    fact(
        "skill-life-stages",
        "Which newborn screening item belongs in early pediatric visits?",
        "The status of state newborn metabolic and hearing screening",
        [
            "The status of the child's school-based vision and hearing screening",
            "The status of the child's adolescent immunization record",
            "The status of the child's sports physical clearance form",
        ],
        "Early visits confirm that state newborn metabolic and hearing screening was completed or scheduled, since early detection changes long-term outcomes. School vision screening, adolescent immunization records, and sports clearance forms describe later stages of care and are not newborn screening.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-016
    fact(
        "skill-life-stages",
        "Which assessment belongs in an intake review for a patient in menopause?",
        "Symptom frequency and how the symptoms affect sleep and daily activities",
        [
            "A treatment plan for hormone replacement therapy to begin at this visit",
            "Confirmation that routine cancer screening can stop once menopause begins",
            "A summary of the patient's childhood immunization and screening records",
        ],
        "Menopause intake captures how often symptoms occur and how they disrupt sleep and daily function, which guides the provider's treatment plan. Starting hormone therapy, ending cancer screening, and reviewing childhood immunizations are not parts of this assessment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-017
    fact(
        "skill-life-stages",
        "A 28-year-old at 10 weeks gestation reports mild nausea but no bleeding. Which finding requires immediate provider notification?",
        "Heavy vaginal bleeding with severe abdominal or shoulder pain",
        [
            "Fatigue that improves with rest and a good night's sleep each day",
            "Food aversions to certain vegetables without other symptoms",
            "Mild nausea with occasional heartburn after larger evening meals",
        ],
        "Bleeding with severe abdominal or shoulder pain in early pregnancy can signal ectopic pregnancy or miscarriage and needs immediate assessment. Fatigue that improves with rest, food aversions, and mild nausea with heartburn are common and expected in the first trimester.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-018
    fact(
        "skill-life-stages",
        "At a two-week postpartum visit, a patient is tearful, sleeps poorly, and reports thoughts of harming the infant. What is the priority action?",
        "Stay with the patient, notify the provider, and follow the harm risk protocol",
        [
            "Leave the patient with a follow-up appointment and a written reassurance plan",
            "Document the symptoms and add them to the postpartum education handout given",
            "Ask the patient to return the next day for a repeat symptom and mood check",
        ],
        "Postpartum thoughts of harming the infant signal a psychiatric emergency that needs continuous supervision and immediate provider assessment. A routine follow-up, documentation alone, and a next day recheck all leave an immediate safety risk unaddressed.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-019
    fact(
        "skill-life-stages",
        "A 16-year-old requests confidential STI testing where state law allows it. What should the medical assistant do?",
        "Room the patient privately, explain the limits, and complete the testing",
        [
            "Room the patient privately, explain the limits, and delay the testing visit",
            "Ask the guardian to sign the requisition before the specimen",
            "Call the guardian and arrange for the guardian to speak with the provider",
        ],
        "Adolescents who may consent under state law receive private care with clear limits on confidentiality, and the ordered testing proceeds without a guardian signature. Delaying the test, requiring a guardian signature, and calling the guardian each compromise the confidential service the law permits.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-020
    fact(
        "skill-life-stages",
        "An 85-year-old with mild dementia lives alone and has missed two appointments. Which new finding should prompt a safety discussion with the provider?",
        "Weight loss, worsening confusion, and unpaid bills that suggest self-neglect",
        [
            "Stable mood with independent bathing, dressing, and meal preparation each day",
            "Weekly family visits with no change in cognition, mood, or daily function",
            "Blood pressure that has remained controlled on the current medication list",
        ],
        "Weight loss, new confusion, and unpaid bills together point to self-neglect, which needs an immediate safety discussion and possible support services. Independent daily function, regular family visits, and controlled blood pressure describe a stable situation rather than a new decline.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-021
    fact(
        "skill-life-stages",
        "What does plotting a child's measurements on age- and sex-specific percentiles show?",
        "Whether the child's growth is tracking or crossing percentiles over time",
        [
            "Whether the child's milestones fall within the expected range for the age",
            "Whether the child's nutrition intake covers the daily requirement",
            "Whether the child's temperature stays within the normal daily range",
        ],
        "Percentile curves show whether a child's height, weight, and head circumference are tracking the previous curve or crossing percentiles, which can signal a growth problem. Milestone screening, intake records, and temperature trends are assessed with other tools.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-022
    fact(
        "skill-life-stages",
        "What does a bulging or sunken anterior fontanelle in an infant suggest?",
        "A change in intracranial pressure or the infant's hydration status",
        [
            "The normal change that occurs as the cranial sutures begin to fuse",
            "A size difference that is common among healthy growing infants",
            "The effect of teething on the skull during the second year of life",
        ],
        "A bulging or sunken fontanelle points to raised intracranial pressure or dehydration and needs provider assessment. Suture fusion, natural differences in size between infants, and teething produce a closed or unchanged fontanelle rather than a tense or sunken one.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-023
    fact(
        "skill-life-stages",
        "When is newborn hearing screening usually completed in the United States?",
        "Before hospital discharge, or at the first follow-up visit",
        [
            "At the child's first vision screening, usually around age three",
            "At the school screening that accompanies the kindergarten forms",
            "At the child's annual well visit after the age of three",
        ],
        "Newborn hearing screening is done before discharge or at the first follow-up so hearing loss is found early enough to support language development. Vision screenings, school screenings, and well visits after age three happen long after the newborn window has closed.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-024
    fact(
        "skill-life-stages",
        "A parent refuses routine vaccines for a two-month-old after counseling. What is the appropriate action?",
        "Chart the refusal and counseling, give the information sheet, and follow up",
        [
            "Chart the refusal and counseling, and record the vaccines as given in the chart",
            "Chart the refusal and counseling, and administer the first vaccine of the series",
            "Chart the refusal and counseling, give the information sheet, and end the visit",
        ],
        "After counseling, the MA charts the discussion and the refusal, gives the parent the vaccine information sheet, and arranges a return visit so the conversation can continue. Recording vaccines as given misstates the chart, giving a vaccine against the parent's decision breaks consent, and ending the visit with no return date leaves the decision unaddressed.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-025
    fact(
        "skill-life-stages",
        "What is the purpose of vision screening in school-age children?",
        "To identify children who need a comprehensive eye examination",
        [
            "To confirm a diagnosis of glaucoma in a child with blurred vision",
            "To measure the child's visual acuity in place of a full eye examination",
            "To identify children who need a hearing evaluation as well",
        ],
        "School vision screening flags children who should receive a full eye examination, and it is quick and easy to deliver. Screening does not diagnose glaucoma, does not replace a comprehensive exam, and does not assess hearing.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-026
    fact(
        "skill-life-stages",
        "Which statement about confidentiality is accurate to give an adolescent during contraceptive counseling?",
        "The visit is private, and the adolescent is told when limits apply",
        [
            "The visit is private, and the adolescent is told a guardian receives a copy",
            "The visit is shared with a guardian, and the adolescent is told in advance",
            "The visit is private, and the adolescent is told everything stays confidential",
        ],
        "Adolescents are told that the visit is private and that limits apply when safety is at stake, which keeps trust while meeting reporting duties. Telling them a guardian receives a copy, sharing the visit with a guardian, and promising that everything stays confidential each misstate the arrangement.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-027
    fact(
        "skill-life-stages",
        "Which teaching points belong in contraceptive counseling for an adolescent?",
        "Effectiveness, common side effects, and STI protection for adolescents",
        [
            "Effectiveness, common side effects, and a guarantee that pregnancy cannot occur",
            "Effectiveness, common side effects, and the need for a pelvic examination",
            "Effectiveness, common side effects, and a guarantee condoms prevent STIs",
        ],
        "Counseling covers how well each method works, the side effects to expect, and that condoms reduce STI risk. No method guarantees that pregnancy cannot occur, a pelvic exam is not required to start contraception, and condoms reduce rather than eliminate the risk of STI.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-028
    fact(
        "skill-life-stages",
        "A pregnant patient at 34 weeks has a blood pressure of 158/96 mmHg and a headache. What is the appropriate action?",
        "Notify the provider immediately and repeat the blood pressure",
        [
            "Document the readings and finish the routine checkout for the visit",
            "Recheck the blood pressure after the patient rests and report it later",
            "Advise rest and fluids, then recheck the blood pressure at the next visit",
        ],
        "A blood pressure of 158/96 mmHg with a headache at 34 weeks can signal preeclampsia, so the provider is notified right away and the reading is repeated to confirm it. Finishing checkout, rechecking after rest and reporting later, and advising rest and fluids delay the assessment these findings require.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-029
    fact(
        "skill-life-stages",
        "At a six-week postpartum visit, the patient has an elevated blood pressure and reports visual spots. What is the appropriate response?",
        "Notify the provider immediately for hypertensive postpartum evaluation",
        [
            "Attribute the symptoms to sleep loss and complete the routine visit",
            "Repeat the blood pressure later in the day and note both readings",
            "Schedule a follow-up visit in three months to recheck the blood pressure",
        ],
        "Elevated blood pressure with visual changes after delivery can signal postpartum preeclampsia, so the provider is notified for immediate evaluation. Attributing it to sleep loss, rechecking later in the day without escalating, and scheduling a three-month follow-up all postpone care these findings need now.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-030
    fact(
        "skill-life-stages",
        "Which combination of measures is most appropriate in a geriatric fall-prevention plan?",
        "Medication review, home hazard changes, vision correction, and balance exercise",
        [
            "Medication review, home hazard changes, vision correction, and bed rest",
            "Medication review, home hazard changes, vision correction, and a daily sedative",
            "Medication review, hazard changes, vision correction, and a calcium supplement",
        ],
        "A fall-prevention plan combines medication review, home hazard changes, vision correction, and balance exercise because each targets a known risk. Scheduled bed rest, a daily sedative, and a low calcium diet add deconditioning, sedation, and bone loss instead of reducing falls.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-life-stages-031
    fact(
        "skill-life-stages",
        "Which finding in an older adult should prompt evaluation for a serious infection?",
        "New confusion with a decline in the patient's usual daily function",
        [
            "A gradual reduction in appetite and fluid intake over the past year",
            "A single night of poor sleep after a long afternoon nap at home",
            "A brief dizzy spell after standing up quickly in the morning",
        ],
        "A sudden change in cognition or daily function in an older adult can be the only sign of a serious infection, since fever is often absent. A year-long appetite change, one poor night of sleep, and a brief postural dizziness do not point to an acute infection.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-life-stages-032
    fact(
        "skill-life-stages",
        "A six-month-old is due for immunizations and becomes distressed during the visit. Which pain-reduction strategy is supported by evidence?",
        "A sucrose pacifier or breastfeeding, with distraction during the injection",
        [
            "A warm compress or breastfeeding, with distraction during the injection",
            "A sucrose pacifier or breastfeeding, with a brief delay while the child settles",
            "A sucrose pacifier or breastfeeding, with the child counting aloud",
        ],
        "Oral sucrose and sucking, whether from a pacifier or breastfeeding, reduce the pain response in infants, and distraction keeps them settled during the injection. A warm compress does not give the same effect for injection pain, delaying the shot does not treat distress, and counting is not a usable distraction for a six-month-old.",
        [S.NHA_CCMA, S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-life-stages-033
    fact(
        "skill-life-stages",
        "What lactation support can a medical assistant provide when a newborn weight check raises concern about feeding?",
        "Plot the weight trend and refer for lactation help when latch problems persist",
        [
            "Plot the weight trend and advise the family to stop breastfeeding at two weeks",
            "Record the weight and advise the mother to drink more fluids each day",
            "Weigh the infant in clothing and note the amount of feeding time spent",
        ],
        "Weight plotted over time shows whether feeding is working, and persistent latch problems need a lactation referral so feeding can be corrected early. Stopping breastfeeding, giving hydration advice, and weighing the infant in clothing do not address the latch problem or the growth trend.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-034
    fact(
        "skill-life-stages",
        "A 17-year-old with cystic fibrosis is preparing to move to adult pulmonology. Which step should begin during adolescence?",
        "Teach self-management skills and arrange the transfer of the medical summary",
        [
            "Teach self-management skills and ask the patient to request records later",
            "Withhold the diagnosis details until the patient reaches the adult clinic age",
            "Delay all transition planning until the patient turns 18 years old",
        ],
        "Transition planning starts in adolescence so the patient learns to manage their own care and the adult team receives a complete summary. Letting the patient chase records later, withholding the diagnosis, and waiting until 18 all raise the risk of gaps in care at handoff.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-035
    fact(
        "skill-life-stages",
        "Which menopause counseling task belongs to the medical assistant?",
        "Gathering symptoms, functional impact, and the patient's questions",
        [
            "Diagnosing menopause and documenting the diagnosis in the patient's chart",
            "Selecting hormone therapy and writing the prescription for the patient to fill",
            "Interpreting bone density results and counseling the patient on what they mean",
        ],
        "The medical assistant gathers the symptom history, functional impact, and questions so the provider can make treatment decisions. Diagnosing menopause, selecting hormone therapy, and interpreting bone density results fall outside the assistant's scope.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-036
    fact(
        "skill-life-stages",
        "At a twelve-month well visit, which skills fall within normal developmental variation?",
        "Babbling, gesturing, and taking first steps at some point in the year",
        [
            "Speaking in full sentences, reading simple words, and taking first steps",
            "Solving simple puzzles, dressing alone, and taking first steps",
            "Recognizing colors, counting to ten, and taking first steps",
        ],
        "At twelve months babbling, gesturing, and first steps all fall within a wide normal range, and persistent delay prompts referral. Full sentences, puzzle solving, dressing alone, color recognition, and counting to ten are skills that appear later.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-037
    fact(
        "skill-life-stages",
        "How should elder abuse screening questions be asked when protocol allows?",
        "Privately, with the suspected abuser out of the room",
        [
            "With the suspected abuser present in the room during the questions",
            "At the front desk, where other patients are waiting",
            "By phone, with a family member answering for the patient",
        ],
        "Screening questions asked privately give the older adult the chance to answer honestly, and mandatory reporting still applies when abuse is disclosed. Asking with the suspected abuser present, at a front desk, or by phone through a relative each limits what the patient will say.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-038
    fact(
        "skill-life-stages",
        "Which combination of records should be confirmed in the chart for a patient planning for serious illness?",
        "An advance directive and a documented surrogate decision maker",
        [
            "A code status note and the patient's current insurance benefits",
            "A code status note and the patient's current medication list",
            "A referral note and the patient's next appointment schedule on file",
        ],
        "Advance directives and a documented surrogate capture the patient's own wishes for care if capacity is lost. A code status note written without the patient's input, billing and medication records, and scheduling paperwork do not record treatment preferences.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-039
    fact(
        "skill-life-stages",
        "A patient's cycles have been irregular for the past year and she is unsure of her last menstrual period. How should the pregnancy be dated?",
        "By ultrasound dating rather than by the last menstrual period",
        [
            "By the last menstrual period because dating ultrasound is not needed",
            "By the gestational age of her previous pregnancy plus time since delivery",
            "By the first day of the most recent episode of spotting she noticed",
        ],
        "Dating by the last menstrual period assumes regular cycles and a date the patient can recall, so irregular cycles and uncertain dates call for ultrasound dating. Using an unreliable last menstrual period, a previous pregnancy's gestational age, or a spotting episode produces an estimate that can be wrong by weeks.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-040
    fact(
        "skill-life-stages",
        "How is fetal heart rate auscultated during routine prenatal care?",
        "With Doppler or fetoscope after the gestational age when tones are audible",
        [
            "With Doppler or fetoscope at every visit from the first prenatal appointment",
            "By counting the maternal radial pulse and recording it as the fetal rate",
            "By ultrasound imaging at every prenatal visit in the third trimester",
        ],
        "Fetal tones are heard with Doppler or a fetoscope once the pregnancy is far enough along to detect them, and the rate is counted for a full minute. Tones are not detectable at the earliest visits, the maternal pulse is a different sound, and routine ultrasound at each visit is not auscultation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-041
    fact(
        "skill-life-stages",
        "What should the medical assistant check when a newborn's car seat is reviewed at the first visit?",
        "The seat is rear-facing and the harness fits snugly against the infant",
        [
            "The seat is rear-facing and the harness fits loosely around the infant",
            "The seat is forward-facing and the harness fits snugly against the infant",
            "The seat is rear-facing and the harness fits snugly over a thick blanket",
        ],
        "A newborn travels rear-facing in a seat with the harness snug against the body, which positions the infant safely in a crash. A loose harness, a forward-facing seat, and a blanket under the harness all reduce the protection the seat provides.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-life-stages-042
    fact(
        "skill-life-stages",
        "Why is medication reconciliation emphasized for older adults taking several prescriptions?",
        "To identify duplicate or inappropriate drugs and the risks of interaction",
        [
            "To confirm that each prescription has been filled at the pharmacy",
            "To update the patient's insurance card and preferred pharmacy information",
            "To review the patient's diet and activity plan alongside the medication list",
        ],
        "Reconciling the medication list in older adults exposes duplicate therapy, drugs that increase falls or confusion, and interactions that can cause harm. Checking pharmacy fills, insurance details, and non-medication plans does not identify the drug problems reconciliation is meant to catch.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
]
