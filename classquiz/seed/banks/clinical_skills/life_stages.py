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
        "What do pediatric growth charts in primary care help clinicians monitor?",
        "Height, weight, head circumference, and BMI trends by age",
        [
            "Footwear brand preference at each birthday visit without provider assessment or documented orders",
            "Parent employer name on intake forms",
            "Parking assignment at the clinic garage",
        ],
        "Percentile shifts flag nutrition, genetic, or endocrine concerns. Nonclinical administrative data do not assess growth.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-002
    fact(
        "skill-life-stages",
        "When assessing an infant anterior fontanelle, what should be documented?",
        "Size, tension, and whether it appears sunken or bulging",
        [
            "Hair color and earring placement",
            "Number of erupted primary teeth without provider assessment or documented orders",
            "Parent marital status on the registration card",
        ],
        "Fontanelle changes may reflect dehydration or increased intracranial pressure. Dental and social fields are separate history elements.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-003
    fact(
        "skill-life-stages",
        "How should confidential care be introduced to an adolescent at the start of a visit?",
        "Explain that some topics are private but safety concerns may require disclosure",
        [
            "Promise that every topic will be kept secret from guardians",
            "Conduct the interview without the patient in the room",
            "Discuss sensitive results loudly in the waiting area without provider assessment or documented orders",
        ],
        "Clear limits build trust while meeting legal duties to report imminent harm. Absolute secrecy is not possible when safety is at risk.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-004
    fact(
        "skill-life-stages",
        "Which elements belong in a geriatric fall risk screen during intake?",
        "History of recent falls, gait observation, medications, and home hazards",
        [
            "Serum cholesterol value without mobility questions",
            "Assistive device use left off the chart without provider assessment or documented orders",
            "Vision and footwear review deferred to save time",
        ],
        "Falls are multifactorial; sedating drugs and clutter contribute. Lipid values alone do not capture mobility risk.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-life-stages-005
    fact(
        "skill-life-stages",
        "What vital signs and measures are routinely tracked at prenatal visits?",
        "Blood pressure, weight, and fetal heart tones per protocol",
        [
            "Routine dental bitewing radiographs at every visit",
            "Complete elimination of physical activity without assessment",
            "Universal withholding of iron supplements",
        ],
        "Hypertension and excessive weight gain may signal preeclampsia or growth problems. Activity and supplements follow individualized plans.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-006
    fact(
        "skill-life-stages",
        "Why is developmental surveillance documented at well-child visits?",
        "To compare milestones to age expectations and refer delays early",
        [
            "To rank children against classmates for sports teams",
            "To determine cafeteria lunch menus without provider assessment or documented orders",
            "To replace vision and hearing screening entirely",
        ],
        "Early identification of developmental delay enables therapy referral. Milestone tracking complements sensory screening rather than replacing it.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-007
    fact(
        "skill-life-stages",
        "How should a medical assistant obtain height and weight on a toddler who cannot stand still on the scale?",
        "Use calibrated infant or chair scale technique per policy with caregiver help",
        [
            "Estimate weight by visual appearance without measurement",
            "Ask the parent to guess weight for the chart without provider assessment or documented orders",
            "Use adult floor scale while the child runs across it",
        ],
        "Accurate anthropometrics guide dosing and growth assessment. Guesses and unstable measurements produce unreliable trends.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-008
    fact(
        "skill-life-stages",
        "What immunization schedule should clinic staff follow for pediatric patients?",
        "Advisory Committee on Immunization Practices recommendations in the EHR",
        [
            "Unverified online forum suggestions without provider assessment or documented orders",
            "Intervals chosen by front desk staff preference",
            "Adult influenza dosing for every infant visit",
        ],
        "Evidence-based schedules prevent vaccine-preventable disease. Pediatric formulations and intervals differ from adult products.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-009
    fact(
        "skill-life-stages",
        "When rooming a school-age child, how can the MA reduce anxiety before procedures?",
        "Use age-appropriate language, explain steps, and offer distraction when allowed",
        [
            "Threaten painful consequences for crying without provider assessment or documented orders",
            "Perform procedures without any explanation to save time",
            "Restrain without telling the child what will happen",
        ],
        "Preparation lowers fear and improves cooperation. Surprise and threats increase distress and movement.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-010
    fact(
        "skill-life-stages",
        "Which topic is appropriate during adolescent reproductive health counseling within scope?",
        "Confidential discussion of contraception options and STI prevention with stated limits",
        [
            "Permanent sterilization as the default first recommendation",
            "Withholding reversible methods from every teen without provider assessment or documented orders",
            "Refusing to document any reproductive health topics",
        ],
        "Shared decision-making supports safety within legal and ethical boundaries. Documentation is required for continuity of care.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-011
    fact(
        "skill-life-stages",
        "How should hearing concerns in older adults be addressed in primary care intake?",
        "Use validated questionnaires or refer for audiometry per protocol",
        [
            "Dismiss self-reported difficulty unless the patient shouts",
            "Whisper testing in a noisy hallway as the sole assessment",
            "Document complaints without follow-up planning without provider assessment or documented orders",
        ],
        "Age-related hearing loss is common and affects adherence. Structured screening prompts referral when indicated.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-012
    fact(
        "skill-life-stages",
        "What safety topic should be reviewed with parents of a newborn before discharge from a visit?",
        "Rear-facing car seat installation per manufacturer and state law",
        [
            "Forward-facing seat use for all neonates without provider assessment or documented orders",
            "Loose harness straps for comfort in the seat",
            "Pillows placed behind the infant face in the seat",
        ],
        "Proper restraint reduces injury risk during crashes. Loose straps and soft bedding increase suffocation and ejection risk.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-life-stages-013
    fact(
        "skill-life-stages",
        "How is capillary refill time assessed in an infant during a sick visit?",
        "Press blanchable skin on sternum or extremity and count seconds to pink return",
        [
            "Measure refill by timing how long the child cries",
            "Assess by color of the diaper after voiding without provider assessment or documented orders",
            "Use capillary refill on nail beds after cold exposure without warming",
        ],
        "Delayed refill can suggest poor perfusion. Crying duration and diaper color do not measure peripheral circulation.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-014
    fact(
        "skill-life-stages",
        "What does plotting head circumference on a growth chart help detect in infancy?",
        "Abnormal brain growth or fluid accumulation trends",
        [
            "Future adult hat size for retail ordering",
            "Hair growth rate per month without provider assessment or documented orders",
            "Parent height without comparing to prior visits",
        ],
        "Serial head size trends raise concern for hydrocephalus or microcephaly. Single unrelated measurements lack context.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-015
    fact(
        "skill-life-stages",
        "Which newborn screening discussion belongs in early pediatric visits?",
        "State metabolic and hearing programs completed or scheduled",
        [
            "Deferring all screening until kindergarten entry",
            "Replacing hearing checks with vision cards alone",
            "Telling parents screening is optional gossip without provider assessment or documented orders",
        ],
        "Early detection of metabolic and hearing disorders improves outcomes. Vision programs complement but do not replace hearing protocols.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-016
    fact(
        "skill-life-stages",
        "How should menopause-related symptoms be approached during intake questioning?",
        "Ask about hot flashes, sleep, mood changes, and bone health concerns",
        [
            "Assume no symptoms exist after age forty without provider assessment or documented orders",
            "Mandate hormone therapy for every patient reporting flashes",
            "Stop all cancer screening questions at menopause",
        ],
        "Symptom clusters guide therapy discussions. Preventive care continues across the lifespan.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-017
    fact(
        "skill-life-stages",
        "A 28-year-old at 10 weeks gestation reports mild nausea but no bleeding. Which prenatal red flag would require immediate provider notification?",
        "Heavy vaginal bleeding with severe abdominal pain or shoulder pain",
        [
            "Mild morning nausea without vomiting dehydration",
            "Food aversions to certain vegetables",
            "Fatigue that improves with rest without provider assessment or documented orders",
        ],
        "Pain with bleeding may signal ectopic pregnancy or miscarriage. Common first-trimester nausea differs from acute hemorrhage.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-018
    fact(
        "skill-life-stages",
        "During a postpartum visit at two weeks, the patient reports tearful mood, poor sleep, and thoughts of harming the baby. What is the priority action?",
        "Stay with the patient, notify the provider immediately, and follow suicide or harm protocol",
        [
            "Schedule a routine visit in six months without escalation",
            "Tell her to get more sunshine and leave the room",
            "Document symptoms without telling the clinician without provider assessment or documented orders",
        ],
        "Postpartum mood disorders and intrusive thoughts are emergencies when harm risk exists. Immediate assessment protects mother and infant.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-019
    fact(
        "skill-life-stages",
        "A 16-year-old requests STI testing without parental notification where law allows. What should the MA do?",
        "Room the patient privately, explain confidentiality limits, and facilitate ordered testing",
        [
            "Refuse care until a parent signs every form without provider assessment or documented orders",
            "Broadcast the request at the front desk without provider assessment or documented orders",
            "Decline testing because the patient is a minor",
        ],
        "Confidential adolescent services are legal in many jurisdictions within safety limits. Privacy encourages honest history.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-020
    fact(
        "skill-life-stages",
        "An 85-year-old with mild dementia lives alone and missed two appointments. What intake finding should trigger a safety conversation with the provider?",
        "New confusion, weight loss, and unpaid bills suggesting self-neglect",
        [
            "Stable mood with independent bathing and meal preparation",
            "Family visits every weekend without change in cognition",
            "Well-controlled hypertension on current medications without provider assessment or documented orders",
        ],
        "Functional decline and self-neglect may indicate abuse or need for support services. Stable independence is less urgent.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-021
    fact(
        "skill-life-stages",
        "How do pediatric growth charts support clinical decision-making?",
        "They compare current height, weight, and head size to age-based percentiles",
        [
            "They list favorite toys for each developmental stage",
            "They replace physical examination of the child",
            "They document parent employment history without provider assessment or documented orders",
        ],
        "Percentile trends detect failure to thrive or obesity risk. Toys and employment data are not growth parameters.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-022
    fact(
        "skill-life-stages",
        "What should be assessed when palpating an infant fontanelle?",
        "Contour, tension, and whether it is flat, sunken, or bulging",
        [
            "Number of hair whorls on the scalp",
            "Ear piercing status at the mall kiosk",
            "Deciduous tooth eruption count without provider assessment or documented orders",
        ],
        "Bulging or sunken fontanelles may reflect fluid or pressure changes. Cosmetic piercing status is unrelated.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-023
    fact(
        "skill-life-stages",
        "When is newborn hearing screening typically performed in the United States?",
        "Before hospital discharge or at early follow-up per state program rules",
        [
            "Routinely delayed until high school entry",
            "Replaced entirely by newborn vision photos",
            "Performed without informing parents without provider assessment or documented orders",
        ],
        "Early hearing loss detection supports language intervention. Vision screening is a separate program.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-024
    fact(
        "skill-life-stages",
        "A parent refuses routine vaccines for a 2-month-old citing online articles. After provider counseling, what is the MA role?",
        "Document discussion, schedule follow-up, and support ordered vaccines per plan",
        [
            "Administer adult vaccine doses to save inventory",
            "Withhold vaccine information sheets from the parent without provider assessment or documented orders",
            "Enter vaccines as given when they were declined",
        ],
        "Shared decision-making requires accurate records. Wrong product, dose, or false documentation creates legal and safety risk.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-025
    fact(
        "skill-life-stages",
        "What is the goal of school-age vision screening in the medical home?",
        "Identify refractive errors and refer for comprehensive eye exams when indicated",
        [
            "Diagnose glaucoma definitively without specialists without provider assessment or documented orders",
            "Replace cycloplegic refraction in every child at school",
            "End vision checks after age three regardless of symptoms",
        ],
        "Screening prompts formal evaluation when children fail tests or report symptoms. Specialist diagnosis exceeds MA scope.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-026
    fact(
        "skill-life-stages",
        "How should confidentiality limits be explained during adolescent contraceptive counseling?",
        "State that privacy applies unless there is risk of harm to self or others",
        [
            "Tell the teen that guardians will hear every detail",
            "Record the conversation on a public clinic speaker",
            "Refuse to answer questions about side effects without provider assessment or documented orders",
        ],
        "Honest limits preserve trust while meeting mandatory reporting duties. Side effects must be discussed for informed consent.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-027
    fact(
        "skill-life-stages",
        "Which contraceptive counseling points are within typical MA education scope?",
        "Effectiveness, common side effects, and dual protection against STIs",
        [
            "Selecting permanent sterilization without provider involvement",
            "Withholding emergency contraception information when asked",
            "Promising that hormones treat all mood disorders without provider assessment or documented orders",
        ],
        "Patient education supports shared decisions under provider oversight. Permanent procedures require physician counseling.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-028
    fact(
        "skill-life-stages",
        "A pregnant patient at 34 weeks has blood pressure 158/96 mmHg and headache. What action aligns with prenatal urgency?",
        "Notify the provider immediately and prepare for repeat vitals per protocol",
        [
            "Document values and continue routine checkout",
            "Advise strenuous exercise to lower pressure without provider assessment or documented orders",
            "Dismiss headache as normal without reassessment",
        ],
        "Elevated pressure with symptoms may indicate preeclampsia needing urgent evaluation. Exercise advice without assessment is unsafe.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-029
    fact(
        "skill-life-stages",
        "At a six-week postpartum visit, blood pressure is elevated and the patient reports seeing spots. What is the appropriate response?",
        "Escalate to the provider for hypertensive postpartum evaluation",
        [
            "Attribute symptoms to sleep loss and end the visit",
            "Remove blood pressure cuff to reduce anxiety",
            "Delay follow-up for one year without provider assessment or documented orders",
        ],
        "Postpartum preeclampsia can occur after delivery. Visual changes with hypertension need prompt assessment.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-030
    fact(
        "skill-life-stages",
        "Which factors are commonly included in geriatric fall prevention planning?",
        "Medication review, home hazards, vision, and gait stability",
        [
            "Cholesterol value without mobility assessment",
            "Removal of walkers to force strengthening",
            "Deferring footwear review to save time without provider assessment or documented orders",
        ],
        "Sedatives and poor lighting increase fall risk. Assistive devices should be optimized, not discarded without therapy.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-life-stages-031
    fact(
        "skill-life-stages",
        "How might infection present differently in an older adult compared with a younger patient?",
        "New confusion or functional decline even when fever is absent",
        [
            "Mandatory high fever in every case of sepsis without provider assessment or documented orders",
            "Rash limited to palms without systemic signs",
            "No change in mental status during urinary infection",
        ],
        "Atypical presentations delay treatment in elders. Baseline cognition changes warrant infection workup.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-life-stages-032
    fact(
        "skill-life-stages",
        "For a six-month-old undergoing immunization, which pain reduction strategy is evidence based?",
        "Breastfeeding or sucrose pacifier per protocol plus distraction",
        [
            "Assuming infants do not perceive injection pain without provider assessment or documented orders",
            "Withholding comfort measures to avoid spoiling the child",
            "Using adult intramuscular ventrogluteal landmarks",
        ],
        "Sweet taste and sucking reduce pain responses in infants. Denying pain increases distress and movement.",
        [S.NHA_CCMA, S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-life-stages-033
    fact(
        "skill-life-stages",
        "What lactation support can the MA provide during a newborn weight check?",
        "Plot weight trend and refer to lactation services when latch problems persist",
        [
            "Advise stopping breastfeeding at forty-eight hours universally",
            "Withhold hydration counseling for the mother without provider assessment or documented orders",
            "Dismiss cracked nipples as normal without referral",
        ],
        "Early specialist support improves feeding success and infant growth.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-034
    fact(
        "skill-life-stages",
        "A 17-year-old with cystic fibrosis is transferring to adult pulmonology. What transition step should begin in adolescence?",
        "Teach self-management skills and ensure medical summary transfer before transfer date",
        [
            "Wait until age thirty to discuss adult clinics without provider assessment or documented orders",
            "Delete medical records on the eighteenth birthday",
            "Exclude the patient from understanding the diagnosis",
        ],
        "Gradual transition improves adherence and safety across care teams.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-035
    fact(
        "skill-life-stages",
        "Which symptoms are commonly addressed in menopause counseling visits?",
        "Hot flashes, sleep disruption, mood changes, and bone health",
        [
            "Discontinuing all preventive cancer screening",
            "Mandatory hormone therapy for every visitor",
            "Dismissing cardiovascular risk discussion without provider assessment or documented orders",
        ],
        "Therapy choices are individualized. Preventive care continues during midlife.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-036
    fact(
        "skill-life-stages",
        "At a twelve-month well visit, which developmental skills are within broad normal variation?",
        "Babbling, gesturing, and possibly first steps with wide ranges",
        [
            "Reading chapter books independently",
            "Solving multi-step algebra problems",
            "Operating a motor vehicle legally without provider assessment or documented orders",
        ],
        "Milestones have ranges; persistent delays need referral. Advanced literacy and driving are not expected at one year.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-037
    fact(
        "skill-life-stages",
        "How should elder abuse screening questions be asked when protocol allows?",
        "Privately when it is safe to speak without the alleged abuser present",
        [
            "With the alleged abuser in the room to save time",
            "Over a loudspeaker in the waiting room without provider assessment or documented orders",
            "Without documentation to protect the clinic",
        ],
        "Privacy encourages disclosure while mandated reporting still applies when required.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-038
    fact(
        "skill-life-stages",
        "What documents support end-of-life planning in the medical record?",
        "Advance directives and identified surrogate decision makers",
        [
            "Staff opinions without patient input without provider assessment or documented orders",
            "Displaying social security numbers in the lobby",
            "Billing codes without goals-of-care discussion",
        ],
        "Recorded wishes align treatment with patient values during incapacity.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-039
    fact(
        "skill-life-stages",
        "When dating a pregnancy by last menstrual period, what assumption must be confirmed with the patient?",
        "Regular cycles and a reliable recall of the LMP date",
        [
            "Irregular bleeding without clarification",
            "Gestational age chosen from insurance member ID",
            "Conception date guessed without ultrasound when indicated",
        ],
        "Accurate dating guides screening tests and delivery planning. Irregular cycles may require ultrasound confirmation.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-040
    fact(
        "skill-life-stages",
        "How is fetal heart rate auscultated during routine prenatal care?",
        "With Doppler or fetoscope per protocol after the expected audible gestational age",
        [
            "By counting the maternal radial pulse at the wrist without provider assessment or documented orders",
            "Using an adult stethoscope on the maternal carotid artery",
            "Ordering ultrasound at every urine dip without indication",
        ],
        "Fetal tones differ from maternal pulses and require appropriate devices and gestational timing.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-041
    fact(
        "skill-life-stages",
        "A family brings a newborn for the first outpatient visit. Which car seat teaching point is highest priority?",
        "Install rear-facing seat with snug harness per manufacturer instructions",
        [
            "Turn the seat forward facing for better leg room",
            "Place thick blankets behind the infant face in the seat",
            "Leave chest clip at the abdomen for comfort without provider assessment or documented orders",
        ],
        "Rear-facing restraint protects the neonatal spine in crashes. Loose clips and bulky bedding increase injury risk.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-life-stages-042
    fact(
        "skill-life-stages",
        "Why is medication reconciliation emphasized for older adults on multiple prescriptions?",
        "To identify potentially inappropriate drugs and interaction risks",
        [
            "To add duplicate sedatives without indication",
            "To stop chronic medications without provider input",
            "To omit over-the-counter herbs from the list without provider assessment or documented orders",
        ],
        "Polypharmacy raises adverse drug events in elders. Complete lists include supplements and OTC products.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
]
