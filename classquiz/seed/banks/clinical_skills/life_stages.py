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
        "What do pediatric growth charts help clinicians track during well-child visits?",
        "Height, weight, head circumference, and BMI plotted against age",
        [
            "A single weight value without prior measurements for comparison",
            "Parent education level recorded on the intake form",
            "Dental eruption count without length or weight data",
        ],
        "Serial percentiles reveal failure to thrive, obesity risk, or head growth problems. One isolated number cannot show a trend, and non-growth fields do not substitute for anthropometrics.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-002
    fact(
        "skill-life-stages",
        "When examining an infant anterior fontanelle, which findings should be documented?",
        "Size, contour, and whether it is flat, sunken, or bulging",
        [
            "Scalp hair texture without palpation of the soft spot",
            "Earlobe shape as a proxy for intracranial pressure",
            "Number of primary teeth visible without palpating the anterior fontanelle",
        ],
        "Fontanelle tension reflects hydration and intracranial pressure. Hair and dental findings do not assess the open suture the way direct palpation does.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-003
    fact(
        "skill-life-stages",
        "How should confidentiality be explained to an adolescent at the start of a visit?",
        "Some topics stay private, but safety risks may require limited disclosure",
        [
            "Guardians will hear every confidential detail discussed in the examination room",
            "The teen has no right to ask questions without a parent present",
            "Sensitive results may be discussed in a public waiting area",
        ],
        "Honest limits build trust while meeting duty to report imminent harm. Absolute secrecy promises are misleading, and public disclosure violates privacy expectations.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-004
    fact(
        "skill-life-stages",
        "Which elements belong in a geriatric fall-risk screen at intake?",
        "Recent falls, gait observation, sedating medications, and home hazards",
        [
            "Fasting lipid panel results without mobility questions",
            "Vision screening deferred because the patient walks independently",
            "Assistive device use omitted from intake when the patient denies prior falls",
        ],
        "Falls are multifactorial; drugs and clutter matter even when cholesterol is normal. Denying falls does not remove the need to note walkers or canes.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-life-stages-005
    fact(
        "skill-life-stages",
        "Which assessments are routinely repeated at scheduled prenatal visits?",
        "Blood pressure, weight gain, and fetal heart activity per protocol",
        [
            "Routine dental radiographs at every prenatal encounter",
            "Complete bed rest ordered for every pregnant patient regardless of individual risk",
            "Universal discontinuation of prescribed iron supplements",
        ],
        "Hypertension and excessive weight gain may signal preeclampsia or growth concerns. Activity and supplements follow individualized plans rather than blanket rules.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-006
    fact(
        "skill-life-stages",
        "Why is developmental surveillance documented at pediatric well visits?",
        "To compare milestones to age norms and refer delays early",
        [
            "To rank children for competitive sports placement",
            "To replace hearing and vision screening entirely",
            "To determine school cafeteria menu choices instead of comparing developmental milestones",
        ],
        "Early referral improves outcomes for speech, motor, and social delays. Milestone tracking complements sensory screening rather than replacing it.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-007
    fact(
        "skill-life-stages",
        "How should height and weight be obtained on a toddler who cannot stand still on a floor scale?",
        "Use an infant or chair scale with caregiver assistance per policy",
        [
            "Record a parental guess without placing the child on a scale",
            "Estimate weight from clothing size on the chart without placing the child on a scale",
            "Weigh the child while running across an adult platform scale",
        ],
        "Accurate measurements guide dosing and growth interpretation. Guesses and unstable readings produce unreliable trends that can delay intervention.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-008
    fact(
        "skill-life-stages",
        "Which immunization reference should clinic staff use for pediatric scheduling?",
        "Advisory Committee on Immunization Practices schedule in the EHR",
        [
            "Intervals chosen by whichever vaccine lot expires first",
            "Adult influenza formulation for every infant visit",
            "Personal blog posts about vaccines instead of the facility immunization policy",
        ],
        "Evidence-based intervals and products prevent vaccine-preventable disease. Pediatric formulations and timing differ from adult vaccines.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-009
    fact(
        "skill-life-stages",
        "What approach can reduce anxiety before procedures in a school-age child?",
        "Age-appropriate explanations, permission steps, and distraction when allowed",
        [
            "Performing the procedure without any prior warning or child-friendly explanation to save time",
            "Physical restraint applied before describing what will happen",
            "Threatening punishment if the child cries or resists during the procedure",
        ],
        "Preparation improves cooperation and reduces sudden movement. Surprise and coercion increase fear, which can make procedures less safe.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-010
    fact(
        "skill-life-stages",
        "Which topic is within typical MA education scope during adolescent reproductive counseling?",
        "Contraception options, STI prevention, and stated confidentiality limits",
        [
            "Recommending permanent sterilization as the default first step",
            "Refusing to document any reproductive health discussion in the medical record",
            "Withholding information about reversible methods when asked",
        ],
        "Patient education supports shared decisions under provider oversight. Permanent procedures and undocumented care fall outside safe MA practice.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-011
    fact(
        "skill-life-stages",
        "How should self-reported hearing difficulty in an older adult be handled at intake?",
        "Use a validated screen or refer for audiometry per protocol",
        [
            "Dismiss complaints unless the patient shouts during conversation",
            "Rely on whisper tests performed in a noisy hallway",
            "Document concerns without planning follow-up or referral",
        ],
        "Age-related loss is common and affects medication teaching and safety. Informal tests in noise miss many cases that formal screening catches.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-012
    fact(
        "skill-life-stages",
        "Which newborn vehicle safety teaching is highest priority before leaving a visit?",
        "Rear-facing car seat with snug harness per manufacturer instructions",
        [
            "Forward-facing installation to give the infant more leg room",
            "Loose harness straps left deliberately slack for infant comfort in the car seat",
            "Soft pillows placed behind the infant face in the seat",
        ],
        "Rear-facing restraint protects the neonatal spine in a crash. Loose straps and bulky bedding increase ejection and suffocation risk.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "beginner",
    ),
    # skill-life-stages-013
    fact(
        "skill-life-stages",
        "How is capillary refill time assessed in an infant during a sick visit?",
        "Blanch sternum or extremity skin and count seconds until pink returns",
        [
            "Time how long the infant cries after a heel stick",
            "Judge perfusion by diaper wetness color alone without performing capillary refill",
            "Press cold nail beds without warming the limb first",
        ],
        "Delayed refill suggests poor peripheral perfusion. Crying duration and urine color do not measure capillary filling after blanching.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-014
    fact(
        "skill-life-stages",
        "Why is head circumference plotted on a growth chart in infancy?",
        "To detect trends suggesting abnormal brain growth or fluid accumulation",
        [
            "To predict adult hat retail inventory needs rather than monitoring infant head growth",
            "To replace comparison with prior visit measurements",
            "To document maternal height without infant data",
        ],
        "Rising or falling percentiles may signal hydrocephalus or microcephaly. A single unrelated adult measurement does not assess the infant head.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-015
    fact(
        "skill-life-stages",
        "Which newborn screening topic belongs in early pediatric visits?",
        "Status of state metabolic and hearing programs completed or scheduled",
        [
            "Deferring all screening until kindergarten entry",
            "Using vision cards as a substitute for hearing protocols",
            "Telling parents newborn screening is unimportant gossip without offering education",
        ],
        "Early detection of metabolic and hearing disorders improves long-term outcomes. Vision programs complement but do not replace hearing screening.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-016
    fact(
        "skill-life-stages",
        "How should menopause-related symptoms be explored during intake?",
        "Ask about hot flashes, sleep, mood changes, and bone health concerns",
        [
            "Assume no symptoms exist after age forty without asking",
            "Mandate hormone therapy for every patient reporting flashes",
            "Stop cancer prevention discussions at menopause without updating screening plans",
        ],
        "Symptom clusters guide therapy conversations while preventive care continues across midlife. Blanket hormone orders exceed MA scope.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-017
    fact(
        "skill-life-stages",
        "A 28-year-old at 10 weeks gestation reports mild nausea but no bleeding. Which finding would require immediate provider notification?",
        "Heavy vaginal bleeding with severe abdominal or shoulder pain",
        [
            "Mild morning nausea without signs of dehydration",
            "Food aversions to certain vegetables during an otherwise uncomplicated first trimester",
            "Fatigue that improves with rest and adequate sleep",
        ],
        "Pain with bleeding may signal ectopic pregnancy or miscarriage. Common first-trimester nausea and fatigue differ from acute hemorrhage with pain.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-018
    fact(
        "skill-life-stages",
        "At a two-week postpartum visit, the patient is tearful, sleeps poorly, and reports thoughts of harming the infant. What is the priority action?",
        "Stay with the patient, notify the provider, and follow harm-risk protocol",
        [
            "Schedule a routine follow-up in six months without escalation",
            "Advise more sunshine alone and leave the room unattended without notifying the provider",
            "Chart symptoms without informing the clinician on duty",
        ],
        "Postpartum mood disorders with harm ideation are emergencies requiring immediate assessment. Delayed care risks injury to mother and baby.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-019
    fact(
        "skill-life-stages",
        "A 16-year-old requests confidential STI testing where state law allows. What should the MA do?",
        "Room the patient privately, explain confidentiality limits, and facilitate ordered testing",
        [
            "Refuse confidential STI testing until a parent signs every laboratory requisition form",
            "Discuss the adolescent STI request loudly at the front desk window within earshot of others",
            "Decline testing because the patient is a minor even when state law allows confidential care",
        ],
        "Confidential adolescent services encourage honest history within safety limits. Public disclosure or blanket refusal may violate law and deter care.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-020
    fact(
        "skill-life-stages",
        "An 85-year-old with mild dementia lives alone and missed two appointments. Which new finding should prompt a safety discussion with the provider?",
        "Weight loss, worsening confusion, and unpaid bills suggesting self-neglect",
        [
            "Stable mood with independent bathing and meal preparation",
            "Weekly family visits reported without any change in cognition or daily function",
            "Well-controlled hypertension on the current medication list",
        ],
        "Functional decline and self-neglect may indicate abuse, depression, or need for support services. Stable independence is less urgent than acute decline.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-021
    fact(
        "skill-life-stages",
        "How do growth percentiles support clinical decisions in pediatrics?",
        "They compare current measurements to age- and sex-appropriate reference curves",
        [
            "They list developmental toys appropriate for each age band",
            "They replace hands-on physical examination of the child",
            "They document parental employment and insurance data without plotting growth measurements",
        ],
        "Crossing percentiles may signal endocrine, nutritional, or genetic concerns. Charts do not substitute for examination or unrelated social fields.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-022
    fact(
        "skill-life-stages",
        "What should be assessed when palpating an infant fontanelle during examination?",
        "Contour, tension, and whether it appears sunken or bulging",
        [
            "Number of scalp hair whorls counted without palpation",
            "Ear piercing site healing at a mall kiosk",
            "Count of erupted deciduous teeth without assessing the soft spot",
        ],
        "Bulging or sunken fontanelles may reflect dehydration or increased intracranial pressure. Piercing and dental counts do not evaluate the anterior fontanelle.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-023
    fact(
        "skill-life-stages",
        "When is newborn hearing screening typically performed in the United States?",
        "Before hospital discharge or at early follow-up per state program rules",
        [
            "Routinely delayed until high school entry without newborn follow-up hearing tests",
            "Replaced entirely by newborn vision photography",
            "Performed without informing parents of the process",
        ],
        "Early hearing loss detection supports language intervention. Vision programs are separate and do not replace auditory screening.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-024
    fact(
        "skill-life-stages",
        "A parent refuses routine vaccines for a two-month-old after counseling. What is the appropriate MA action?",
        "Document the discussion, schedule follow-up, and support the provider plan",
        [
            "Administer adult vaccine product to use open inventory",
            "Enter vaccines as documented given in the chart when the family actually declined them",
            "Withhold vaccine information sheets from the parent",
        ],
        "Accurate records and education support shared decision-making. Wrong product, false documentation, or missing handouts create legal and safety risk.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-025
    fact(
        "skill-life-stages",
        "What is the purpose of school-age vision screening in the medical home?",
        "Identify possible refractive error and refer for comprehensive exams when indicated",
        [
            "Diagnose glaucoma definitively during school screening without specialist examination or confirmatory testing",
            "Replace cycloplegic refraction for every child at school",
            "End vision checks after age three regardless of symptoms",
        ],
        "Screening prompts formal evaluation when children fail tests or report symptoms. Definitive diagnosis exceeds MA and school screen scope.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-026
    fact(
        "skill-life-stages",
        "How should confidentiality limits be stated during adolescent contraceptive counseling?",
        "Privacy applies unless there is risk of harm to self or others",
        [
            "Guardians will automatically receive a full transcript of every confidential adolescent visit",
            "The conversation may be broadcast on a clinic intercom",
            "Side-effect questions may be refused when the teen asks",
        ],
        "Clear limits preserve trust while meeting mandatory reporting duties. Side effects must be discussed for informed consent.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-027
    fact(
        "skill-life-stages",
        "Which contraceptive teaching points are appropriate for MA patient education?",
        "Effectiveness, common side effects, and dual protection against STIs",
        [
            "Selecting permanent sterilization without provider involvement",
            "Withholding emergency contraception information when requested",
            "Promising hormonal contraception will treat all adolescent mood disorders without follow-up",
        ],
        "Education supports shared decisions under provider oversight. Permanent procedures and withheld options undermine informed choice.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-028
    fact(
        "skill-life-stages",
        "A pregnant patient at 34 weeks has blood pressure 158/96 mmHg and a headache. What action matches prenatal urgency?",
        "Notify the provider immediately and repeat vitals per protocol",
        [
            "Document values and continue routine checkout",
            "Advise strenuous exercise to lower pressure without reassessment",
            "Dismiss the headache as normal pregnancy discomfort",
        ],
        "Elevated pressure with symptoms may indicate preeclampsia needing urgent evaluation. Exercise advice without assessment can worsen hypertension.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-029
    fact(
        "skill-life-stages",
        "At a six-week postpartum visit, blood pressure is elevated and the patient reports visual spots. What is the appropriate response?",
        "Escalate to the provider for hypertensive postpartum evaluation",
        [
            "Attribute symptoms to sleep loss and end the visit",
            "Remove the blood pressure cuff to reduce anxiety",
            "Delay any postpartum blood pressure follow-up for twelve months without provider contact",
        ],
        "Postpartum preeclampsia can occur after delivery. Visual changes with hypertension need prompt medical assessment.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-030
    fact(
        "skill-life-stages",
        "Which factors are commonly addressed in geriatric fall-prevention planning?",
        "Medication review, home hazards, vision, and gait stability",
        [
            "Lipid values without mobility or balance assessment",
            "Removal of walkers at home to force muscle strengthening without a safety assessment",
            "Deferring home safety questions to the next annual visit",
        ],
        "Sedatives and poor lighting increase fall risk. Assistive devices should be optimized with therapy, not discarded without assessment.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-life-stages-031
    fact(
        "skill-life-stages",
        "How might serious infection present differently in an older adult than in a younger patient?",
        "New confusion or functional decline even when fever is absent",
        [
            "High fever required in every case before treating infection",
            "Rash limited to palms without fever, confusion, or other systemic infection signs",
            "Unchanged mental status during urinary tract infection",
        ],
        "Atypical presentations delay treatment in elders. Baseline cognition changes warrant infection workup even without classic fever.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-life-stages-032
    fact(
        "skill-life-stages",
        "A six-month-old is due for immunizations and becomes distressed. Which pain-reduction strategy is evidence based?",
        "Sucrose pacifier or breastfeeding plus distraction per protocol",
        [
            "Assuming infants do not perceive injection pain during routine immunization visits",
            "Withholding comfort measures to discourage crying",
            "Using adult ventrogluteal landmarks for all infant doses",
        ],
        "Sweet taste and sucking reduce pain responses in infants. Denying comfort increases movement, which raises injury risk during injection.",
        [S.NHA_CCMA, S.CDC_VACCINE_ADMIN],
        "advanced",
    ),
    # skill-life-stages-033
    fact(
        "skill-life-stages",
        "What lactation support can an MA provide during a newborn weight check?",
        "Plot weight trends and refer to lactation services when latch problems persist",
        [
            "Advise stopping breastfeeding at forty-eight hours for all families",
            "Withhold maternal hydration counseling during the visit",
            "Dismiss cracked nipples as normal lactation changes without lactation referral or teaching",
        ],
        "Early specialist support improves feeding success and infant growth. Universal weaning advice and untreated nipple trauma worsen outcomes.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-034
    fact(
        "skill-life-stages",
        "A 17-year-old with cystic fibrosis is preparing to transfer to adult pulmonology. Which step should begin in adolescence?",
        "Teach self-management and ensure medical summary transfer before the handoff date",
        [
            "Wait until age thirty to mention adult clinic options",
            "Delete the entire medical record automatically on the patient eighteenth birthday",
            "Exclude the patient from understanding the diagnosis",
        ],
        "Gradual transition improves adherence and safety across care teams. Sudden handoffs without records or skills teaching increase hospitalizations.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-035
    fact(
        "skill-life-stages",
        "Which symptom clusters are commonly addressed in menopause counseling visits?",
        "Hot flashes, sleep disruption, mood changes, and bone health",
        [
            "Discontinuing all preventive cancer screening at midlife",
            "Mandating hormone replacement therapy for every patient at the menopause counseling visit",
            "Dismissing cardiovascular risk discussion",
        ],
        "Therapy choices are individualized while preventive care continues. Blanket treatment orders exceed MA scope.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-036
    fact(
        "skill-life-stages",
        "At a twelve-month well visit, which skills fall within broad normal developmental variation?",
        "Babbling, gesturing, and possibly first steps with wide ranges",
        [
            "Reading full chapter books independently at the twelve-month well-child visit",
            "Solving multi-step algebra problems during routine twelve-month developmental screening",
            "Operating a motor vehicle legally on public roads",
        ],
        "Milestones have ranges; persistent delays need referral. Advanced literacy, algebra, and driving are not expected at one year of age.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-037
    fact(
        "skill-life-stages",
        "How should elder abuse screening questions be asked when protocol allows?",
        "Privately when it is safe to speak without the alleged abuser present",
        [
            "With the alleged abuser remaining in the examination room to save documentation time",
            "At the front desk while other patients wait nearby",
            "Without documentation to protect the clinic from reports",
        ],
        "Privacy encourages disclosure while mandated reporting still applies when required. Abuser presence and public settings suppress honest answers.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-038
    fact(
        "skill-life-stages",
        "Which documents support end-of-life planning in the medical record?",
        "Advance directives and identified surrogate decision makers",
        [
            "Staff opinions about code status recorded without any patient input or advance directive",
            "Social security numbers posted in the lobby",
            "Billing codes without goals-of-care discussion",
        ],
        "Recorded wishes align treatment with patient values during incapacity. Administrative codes alone do not capture care preferences.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-039
    fact(
        "skill-life-stages",
        "When dating a pregnancy by last menstrual period, what must be confirmed with the patient?",
        "Regular cycles and reliable recall of the LMP date",
        [
            "Irregular bleeding accepted without clarification",
            "Gestational age taken from insurance member identification",
            "Conception date guessed when ultrasound is indicated",
        ],
        "Accurate dating guides screening timing and delivery planning. Irregular cycles often require ultrasound confirmation rather than assumed dates.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-040
    fact(
        "skill-life-stages",
        "How is fetal heart rate auscultated during routine prenatal care?",
        "With Doppler or fetoscope per protocol after the expected audible gestational age",
        [
            "By counting the maternal radial pulse at the wrist and documenting it as fetal heart rate",
            "With an adult stethoscope on the maternal carotid artery",
            "By ordering ultrasound at every urine dip without indication",
        ],
        "Fetal tones differ from maternal pulses and require appropriate devices and timing. Maternal pulse counts do not document fetal activity.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-041
    fact(
        "skill-life-stages",
        "A family brings a newborn for the first outpatient visit. Which car seat teaching point is highest priority?",
        "Rear-facing seat with chest clip at armpit level and snug straps",
        [
            "Forward-facing infant car seat installed for better parent visibility during the first ride",
            "Thick blankets behind the infant face inside the harness",
            "Chest clip positioned on the abdomen for comfort",
        ],
        "Rear-facing restraint protects the neonatal spine in crashes. Bulky bedding and low clips increase injury and ejection risk.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-life-stages-042
    fact(
        "skill-life-stages",
        "Why is medication reconciliation emphasized for older adults on multiple prescriptions?",
        "To identify potentially inappropriate drugs and interaction risks",
        [
            "To add duplicate sedatives without clinical indication",
            "To stop chronic maintenance medications without provider input during reconciliation visits",
            "To omit over-the-counter herbs from the medication list",
        ],
        "Polypharmacy raises adverse drug events in elders. Complete lists include supplements and OTC products the patient actually takes.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
]
