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
        "When caring for patients across the lifespan in clinic, growth charts in pediatrics help track, which action is appropriate?",
        "Height, weight, and head circumference percentiles",
        [
            "not appropriate shoe size",
            "Parent income",
            "Favorite color",
        ],
        "Percentiles identify nutritional or endocrine concerns. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-002
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, infant fontanelle assessment notes, which action is appropriate?",
        "Size, tension, and bulging or sinking",
        [
            "Hair color not appropriate",
            "Ear piercing status",
            "Number of teeth",
        ],
        "Fontanelle changes may signal dehydration or increased ICP. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-003
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, adolescent confidentiality discussions should, which action is appropriate?",
        "Explain limits such as harm to self or others",
        [
            "Promise secrecy for all topics",
            "Exclude patient from conversation",
            "Share details on social media",
        ],
        "Clear limits build trust while meeting legal duties. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-004
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, geriatric fall risk screening may include, which action is appropriate?",
        "History of falls, gait, and home hazards",
        [
            "not appropriate cholesterol level",
            "Ignoring assistive devices",
            "Skipping vision questions",
        ],
        "Multifactorial risks guide prevention. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-005
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, prenatal visits often monitor, which action is appropriate?",
        "Blood pressure, weight, and fetal heart tones per protocol",
        [
            "not appropriate dental x-rays",
            "Eliminating all exercise",
            "Withholding iron without assessment",
        ],
        "Routine surveillance detects preeclampsia and growth issues. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-006
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, newborn hearing screening is typically, which action is appropriate?",
        "Performed before discharge per state program",
        [
            "Optional forever if parents busy",
            "not appropriate at age 5",
            "Replaced by vision test alone",
        ],
        "Early detection improves language outcomes. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-007
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, menopause symptom counseling may address, which action is appropriate?",
        "Hot flashes, sleep, and bone health",
        [
            "Ignoring cardiovascular risk",
            "Stopping all preventive care",
            "Mandatory hormone therapy for all",
        ],
        "Shared decision-making guides therapy. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-008
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, toddler immunization schedules follow, which action is appropriate?",
        "ACIP recommendations documented in EHR",
        [
            "Parent social media trends not appropriate",
            "Random intervals",
            "Adult influenza schedule not appropriate",
        ],
        "Timely vaccines prevent VPDs. Clinic teams should follow facility policy and document findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-009
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, school-age vision screening in clinic, which action is appropriate?",
        "Identifies refractive errors needing referral",
        [
            "Replaces comprehensive eye exam not appropriate",
            "Uses not appropriate color blindness cards for glaucoma",
            "Is unnecessary after age 3",
        ],
        "Screening prompts formal evaluation. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-010
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, elder abuse screening questions are asked, which action is appropriate?",
        "Privately when safe per protocol",
        [
            "not appropriate with alleged abuser present",
            "not appropriate documented",
            "On loudspeaker in waiting room",
        ],
        "Safety and privacy encourage disclosure. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-011
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, developmental milestones for 12-month infant include, which action is appropriate?",
        "Babbling and possibly first steps with wide variation",
        [
            "Reading chapter books",
            "Driving toy car on highway",
            "Adult abstract reasoning",
        ],
        "Wide normal ranges exist; delays need referral. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-012
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, contraceptive counseling for adolescents emphasizes, which action is appropriate?",
        "Effectiveness, STI prevention, and confidentiality limits",
        [
            "Withholding all options",
            "not appropriate permanent sterilization",
            "No documentation",
        ],
        "Evidence-based options support reproductive health. Clinic teams should follow facility policy and document findings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-013
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, postpartum visit care includes screening for, which action is appropriate?",
        "Mood disorders and physical recovery",
        [
            "not appropriate cosmetic concerns",
            "Ignoring blood pressure",
            "Discontinuing all breastfeeding support",
        ],
        "Postpartum depression affects mother and infant. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-014
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, end-of-life planning discussions document, which action is appropriate?",
        "Advance directives and surrogate decision makers",
        [
            "not appropriate billing codes",
            "Staff opinions without patient input",
            "Social security numbers in lobby",
        ],
        "Goals-of-care align treatment with values. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-015
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, pediatric pain assessment tools may use, which action is appropriate?",
        "Faces scales or FLACC for nonverbal children",
        [
            "not appropriate numeric scale refusing child input",
            "Ignoring behavioral cues",
            "Assuming no pain in infants",
        ],
        "Age-appropriate tools improve analgesia. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-016
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, older adults may show atypical infection signs such as, which action is appropriate?",
        "Confusion or functional decline without fever",
        [
            "not appropriate high fever not appropriate",
            "Rash not appropriate on palms",
            "No change in mentation ever",
        ],
        "Atypical presentations delay diagnosis. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-life-stages-017
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, lactation support in primary care includes, which action is appropriate?",
        "Referral to lactation consultant and monitoring infant weight",
        [
            "Telling all mothers to stop breastfeeding at 2 days",
            "Withholding hydration advice",
            "Ignoring painful latch",
        ],
        "Support improves breastfeeding success. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-018
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, transition of adolescent to adult care planning, which action is appropriate?",
        "Begins early with self-management skills",
        [
            "Occurs not appropriate at age 30",
            "Excludes medical summary transfer",
            "Removes all parental contact instantly at 18 without plan",
        ],
        "Gradual transition improves adherence. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-019
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, infant length measurement for growth charts uses, which action is appropriate?",
        "A recumbent stadiometer or length board",
        [
            "Adult-not appropriate scale",
            "Blood pressure cuff",
            "Otoscope",
        ],
        "Accurate length supports pediatric growth assessment. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-020
    fact(
        "skill-life-stages",
        "When caring for patients across the lifespan in clinic, hearing screening in older adults may use, which action is appropriate?",
        "Validated questionnaires or audiometry per protocol",
        [
            "not appropriate whisper tests in noisy halls",
            "Ignoring patient concerns",
            "Skipping documentation",
        ],
        "Age-related hearing loss is common and underreported. Clinic teams should follow facility policy and document findings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-021
    fact(
        "skill-life-stages",
        "Pediatric growth charts in primary care track:",
        "Height, weight, head circumference, and BMI as age appropriate",
        [
            "Shoe size and favorite cartoon",
            "Parent employer stock price",
            "Parking spot number at the clinic",
        ],
        "Percentile trends flag nutrition and endocrine concerns. Nonclinical data do not assess growth.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-022
    fact(
        "skill-life-stages",
        "An infant anterior fontanelle assessment documents:",
        "Size, tension, and whether it is sunken or bulging",
        [
            "Hair color and earring status",
            "Number of deciduous teeth erupted",
            "Parent marital status",
        ],
        "Fontanelle changes may reflect dehydration or increased intracranial pressure. Dental and social details are separate history.",
        [S.NHA_CCMA, S.MEDLINEPLUS_HAND_HYGIENE],
        "intermediate",
    ),
    # skill-life-stages-023
    fact(
        "skill-life-stages",
        "Newborn hearing screening in the United States is typically:",
        "Performed before discharge or at early follow-up per state program requirements",
        [
            "Deferred until kindergarten entry without exception",
            "Replaced by vision testing alone in the nursery",
            "Discussed among staff without parental communication",
        ],
        "Early detection improves language development support. Vision screening complements but does not replace hearing programs.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-024
    fact(
        "skill-life-stages",
        "Toddler immunization timing should follow:",
        "Advisory Committee on Immunization Practices schedules documented in the EHR",
        [
            "Unverified social media trends",
            "Random intervals chosen by front desk staff",
            "Adult influenza dosing for every infant",
        ],
        "Evidence-based schedules protect against vaccine-preventable disease. Adult products and doses differ from pediatric formulations.",
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-025
    fact(
        "skill-life-stages",
        "School-age vision screening in clinic aims to:",
        "Identify refractive errors and refer for comprehensive eye exams when indicated",
        [
            "Diagnose glaucoma definitively without specialists",
            "Replace cycloplegic refraction in every child",
            "End at age three regardless of symptoms",
        ],
        "Screening prompts formal evaluation when children fail tests or have symptoms.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-026
    fact(
        "skill-life-stages",
        "Adolescent confidential care discussions should clarify:",
        "Limits of confidentiality such as imminent harm to self or others",
        [
            "That all topics can be kept secret from guardians in every situation",
            "That the conversation will be posted online",
            "That the patient cannot ask questions",
        ],
        "Trust grows when limits are explained honestly. Absolute secrecy is not possible when safety is at risk.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-027
    fact(
        "skill-life-stages",
        "Contraceptive counseling for adolescents emphasizes:",
        "Effectiveness, side effects, STI prevention, and confidentiality limits",
        [
            "Withholding all reversible methods",
            "Permanent sterilization as the first option for every teen",
            "No documentation in the medical record",
        ],
        "Shared decision-making supports reproductive health within legal and ethical boundaries.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-028
    fact(
        "skill-life-stages",
        "Prenatal visit vital signs commonly include:",
        "Blood pressure and weight with comparison to baseline",
        [
            "Dental bitewing x-rays at every visit",
            "Elimination of all physical activity without assessment",
            "Withholding iron supplementation universally",
        ],
        "Hypertension and excessive weight gain may signal preeclampsia or other complications. Supplements follow individual plans.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-029
    fact(
        "skill-life-stages",
        "Postpartum clinic visits screen for:",
        "Mood disorders, blood pressure, and physical recovery including perineal or incision healing",
        [
            "Cosmetic nail preferences without vitals",
            "Discontinuing all breastfeeding support automatically",
            "Ignoring headache with visual changes",
        ],
        "Postpartum depression and hypertensive disorders affect maternal and infant wellbeing.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-030
    fact(
        "skill-life-stages",
        "Geriatric fall risk assessment may include:",
        "History of falls, gait observation, medications, and home hazards",
        [
            "Cholesterol value alone without mobility questions",
            "Ignoring use of walkers or canes",
            "Skipping vision and footwear review",
        ],
        "Falls are multifactorial; medication sedatives and clutter contribute. Mobility aids must be noted.",
        [S.NHA_CCMA, S.CDC_HBP],
        "intermediate",
    ),
    # skill-life-stages-031
    fact(
        "skill-life-stages",
        "Older adults may show infection with:",
        "New confusion or functional decline even when fever is absent",
        [
            "Rash limited to palms without other signs",
            "No change in mentation during sepsis",
            "High fever in every case without exception wording",
        ],
        "Atypical presentations delay treatment in elders. Baseline cognition changes warrant evaluation.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-life-stages-032
    fact(
        "skill-life-stages",
        "Pediatric pain assessment for a nonverbal child may use:",
        "FLACC or similar behavioral scales",
        [
            "Assumption that infants do not feel pain",
            "Numeric scale without developmental adaptation",
            "Ignoring crying during procedures as meaningless",
        ],
        "Age-appropriate tools improve analgesia and comfort measures.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-033
    fact(
        "skill-life-stages",
        "Lactation support in primary care includes:",
        "Monitoring infant weight and referring to lactation specialists when latch problems persist",
        [
            "Telling all mothers to stop breastfeeding at forty-eight hours",
            "Withholding hydration counseling",
            "Ignoring painful latch or cracked nipples",
        ],
        "Early support improves breastfeeding success and infant nutrition.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-034
    fact(
        "skill-life-stages",
        "Transition planning from pediatric to adult care should:",
        "Begin in adolescence with self-management skills and medical summary transfer",
        [
            "Occur suddenly at age thirty without preparation",
            "Delete all records at the eighteenth birthday",
            "Exclude patients from understanding their diagnoses",
        ],
        "Gradual transition improves adherence and safety across settings.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-035
    fact(
        "skill-life-stages",
        "Menopause symptom counseling may address:",
        "Hot flashes, sleep disruption, mood changes, and bone health",
        [
            "Stopping all preventive screenings",
            "Mandatory hormone therapy for every patient",
            "Ignoring cardiovascular risk factors",
        ],
        "Symptoms vary; therapy decisions are individualized with shared decision-making.",
        [S.NHA_CCMA, S.MEDLINEPLUS_HAND_HYGIENE],
        "intermediate",
    ),
    # skill-life-stages-036
    fact(
        "skill-life-stages",
        "Developmental surveillance at twelve months expects skills such as:",
        "Babbling, gesturing, and possibly first steps with wide normal variation",
        [
            "Reading chapter books independently",
            "Abstract algebraic reasoning",
            "Driving a motor vehicle",
        ],
        "Milestones have ranges; persistent delays need referral.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-037
    fact(
        "skill-life-stages",
        "Elder abuse screening questions are asked:",
        "Privately when safe according to protocol",
        [
            "With the alleged abuser present to save time",
            "Over a loudspeaker in the waiting room",
            "Without documentation to protect staff",
        ],
        "Privacy encourages disclosure; mandated reporting still applies when required.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-life-stages-038
    fact(
        "skill-life-stages",
        "End-of-life planning documents in the chart include:",
        "Advance directives and identified surrogate decision makers",
        [
            "Staff opinions without patient input",
            "Social security numbers displayed in the lobby",
            "Billing codes without goals-of-care discussion",
        ],
        "Documented wishes align treatment with patient values.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-039
    fact(
        "skill-life-stages",
        "Pregnancy dating by last menstrual period assumes:",
        "Regular cycles and known LMP date confirmed with the patient",
        [
            "Irregular bleeding without clarification",
            "Conception date guessed without ultrasound when indicated",
            "Gestational age chosen from insurance ID numbers",
        ],
        "Accurate dating guides screening tests and delivery planning.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-life-stages-040
    fact(
        "skill-life-stages",
        "Fetal heart rate auscultation in prenatal visits uses:",
        "Doppler or fetoscope per protocol after the expected audible window",
        [
            "Adult stethoscope on the maternal carotid",
            "Palpation of the maternal radial pulse as fetal rate",
            "Ultrasound at every urine dip without orders",
        ],
        "Proper device and gestational age improve detection. Maternal pulses are not fetal heart tones.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-life-stages-041
    fact(
        "skill-life-stages",
        "Car seat education for newborns emphasizes:",
        "Rear-facing installation per manufacturer and state law",
        [
            "Front-facing seat for all neonates",
            "Placing pillows behind infant face in the seat",
            "Leaving straps loose for comfort",
        ],
        "Correct restraint reduces injury during crashes. Loose straps fail in collisions.",
        [S.NHA_CCMA, S.RED_CROSS_FIRST_AID],
        "advanced",
    ),
    # skill-life-stages-042
    fact(
        "skill-life-stages",
        "Geriatric polypharmacy review aims to:",
        "Identify potentially inappropriate medications and interactions",
        [
            "Add duplicate sedatives without indication",
            "Stop all chronic meds without provider input",
            "Ignore over-the-counter herbs",
        ],
        "Medication reconciliation reduces adverse drug events in elders.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
]
