# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Study guides with authoritative links, keyed by topic slug.

Each guide is a list of blocks. A block carries a short title, a prose
summary, optional key points (``bullets``) and the official source the
content is drawn from (``source`` + ``url``).

Sources are restricted to government agencies (CDC, OSHA, FDA, HHS, eCFR,
NIH/NLM, CMS, AHRQ, USPSTF), standards bodies (CLSI, AHA, American Red Cross,
WHO, ADA), the certifying body (NHA) and the AMA Code of Medical Ethics.
"""

from __future__ import annotations

from collections.abc import Sequence

from classquiz.seed.sources import (
    ADA_DIAGNOSIS,
    ADA_STANDARDS,
    AHA_ADULT_BLS,
    AHA_ADULT_FBAO,
    AHA_AED_PROGRAM,
    AHA_ALGORITHMS,
    AHA_CHAIN,
    AHA_CHILD_FBAO,
    AHA_EXECUTIVE_SUMMARY,
    AHA_GUIDELINES,
    AHA_HIGH_QUALITY,
    AHA_NEONATAL_ALG,
    AHA_PALS,
    AHA_TOP_THINGS,
    AHA_WHAT_IS_CPR,
    AHRQ_CARE_COORDINATION,
    AHRQ_HEALTH_LITERACY,
    AHRQ_PATIENT_SAFETY,
    AHRQ_TEAMSTEPPS,
    AMA_ETHICS,
    CDC_A1C,
    CDC_CHILD_DEV,
    CDC_CHRONIC_DISEASE,
    CDC_COVID,
    CDC_DIABETES,
    CDC_DIABETES_HEART,
    CDC_DIABETES_TESTING,
    CDC_FLU,
    CDC_GESTATIONAL,
    CDC_HAND_HYGIENE,
    CDC_HBP_MEASURE,
    CDC_HEPATITIS_B,
    CDC_HIV,
    CDC_IMZ_BEST_PRACTICES,
    CDC_IMZ_SCHEDULES,
    CDC_INFECTION_CONTROL,
    CDC_INJECTION_SAFETY,
    CDC_INSULIN_RESISTANCE,
    CDC_ISOLATION_PRECAUTIONS,
    CDC_KIDNEY_DISEASE,
    CDC_LEAD,
    CDC_MMWR_CARDIOMETABOLIC,
    CDC_NCHS_DB319,
    CDC_NIOSH_BBP,
    CDC_NIOSH_INFECTIOUS,
    CDC_NIOSH_PPE,
    CDC_NIOSH_RISK,
    CDC_PHYSICAL_ACTIVITY,
    CDC_PINKBOOK,
    CDC_PREDIABETES,
    CDC_SLEEP,
    CDC_TB,
    CDC_TB_HCP,
    CDC_TYPE_2,
    CDC_VACCINE_ADMIN,
    CDC_VACCINE_STORAGE,
    CDC_VACCINES_HCP,
    CDC_VIS,
    CDC_VISION_LOSS,
    CLSI_GP41,
    CLSI_GP41_SAMPLE,
    DIETARY_GUIDELINES,
    ECFR_CLIA,
    ECFR_HIPAA_PRIVACY,
    ECFR_HIPAA_SECURITY,
    FDA_CLIA,
    FDA_CLIA_WAIVED,
    FDA_DRUG_SAFETY,
    FDA_HUMULIN_R_LABEL,
    FDA_INSULIN_SYRINGE_510K,
    FDA_MEDICATION_SAFETY,
    FDA_MEDWATCH,
    HHS_HIPAA,
    HHS_HIPAA_COVERED,
    HHS_HIPAA_PRIVACY,
    HHS_HIPAA_SECURITY,
    MEDICAID_GOV,
    MEDICARE_GOV,
    ML_A1C,
    ML_AFIB,
    ML_AGING_VITALS,
    ML_ANAPHYLAXIS,
    ML_ARRHYTHMIAS,
    ML_BLOOD,
    ML_BP_MEASURE,
    ML_BURNS,
    ML_BURNS_TOPIC,
    ML_CAD,
    ML_CAREGIVERS,
    ML_CHILD_HEALTH,
    ML_CHOKING_ADULT,
    ML_CHOKING_INFANT,
    ML_CPR_CHILD,
    ML_CPR_INFANT,
    ML_CUTS,
    ML_DEHYDRATION,
    ML_DEMENTIA,
    ML_DIABETIC_FOOT,
    ML_ECG,
    ML_ENCYCLOPEDIA,
    ML_FIRST_AID_KIT,
    ML_HAND_HYGIENE,
    ML_HEALTH_INSURANCE,
    ML_HEALTH_TOPICS,
    ML_HEART_ATTACK,
    ML_HEART_ATTACK_FIRST_AID,
    ML_HEART_ATTACK_TOPIC,
    ML_HEAT_ILLNESS,
    ML_LAB_TESTS,
    ML_MEDICATION_ERRORS,
    ML_OGTT,
    ML_OLDER_ADULT,
    ML_PATIENT_RIGHTS,
    ML_PNEUMONIA,
    ML_SEPSIS,
    ML_TEEN_HEALTH,
    ML_VENIPUNCTURE,
    ML_VITAL_SIGNS,
    NCBI_BOOKSHELF,
    NCI_CANCER,
    NHA_CCMA,
    NHA_CCMA_EXAM,
    NHA_CET,
    NHLBI_BP,
    NHLBI_HEALTH,
    NIA_HEALTH,
    NIAMS_HEALTH,
    NIDDK_DIABETES,
    NIDDK_DIABETES_SYMPTOMS,
    NIDDK_GDM_CHAPTER,
    NIDDK_INSULIN_TREATMENTS,
    NIDDK_KIDNEY,
    NIDDK_LOW_BLOOD_GLUCOSE,
    NIDDK_SEXUAL_BLADDER,
    NIDDK_TYPE_1,
    NIDDK_TYPE_2,
    NINDS_HEALTH,
    NLM_MEDLINEPLUS,
    OSHA_BBP,
    OSHA_BBP_GENERAL,
    OSHA_BBP_HAZARDS,
    OSHA_BBP_RESOURCES,
    OSHA_BBP_STANDARDS,
    OSHA_ERGONOMICS,
    OSHA_HAZCOM,
    OSHA_HEALTHCARE,
    OSHA_NEEDLESTICK,
    OSHA_PPE,
    RED_CROSS_CPR,
    RED_CROSS_FIRST_AID,
    RED_CROSS_FIRST_AID_STEPS,
    USPSTF,
    USPSTF_TOPICS,
    WHO_HAND_HYGIENE,
    WHO_INJECTION_SAFETY,
    WHO_PHLBOTOMY,
)


def _split_cite(cite: str) -> tuple[str, str]:
    """Split a ``Name — URL`` citation into its label and URL.

    Labels may themselves contain an em dash (for example
    ``AHA: Part 7 — Adult Basic Life Support``), so the URL is located from
    the right instead of splitting on the first separator.
    """
    marker = " — https://"
    index = cite.rfind(marker)
    if index == -1:
        return cite, ""
    return cite[:index], cite[index + 3 :]


def _b(
    title: str,
    summary: str,
    cite: str,
    bullets: Sequence[str] | None = None,
) -> dict:
    """Build one study block from a source citation (``Name — URL``)."""
    name, url = _split_cite(cite)
    block: dict = {"title": title, "summary": summary, "url": url, "source": name}
    if bullets:
        block["bullets"] = list(bullets)
    return block


STUDY_BY_TOPIC: dict[str, list[dict]] = {
    # ------------------------------------------------------------------
    # NHA CCMA
    # ------------------------------------------------------------------
    "ccma-foundational": [
        _b(
            "What the CCMA exam covers",
            "The NHA publishes the CCMA content outline and exam blueprint. Expect "
            "questions across basic science, anatomy and physiology, clinical "
            "patient care, patient care coordination and education, administrative "
            "assistance, communication and customer service, and law and ethics. "
            "Preparation should follow the current outline rather than older study "
            "guides, because the weighting of each domain changes over time.",
            NHA_CCMA_EXAM,
            [
                "Read the current NHA test plan before studying — domains and percentages change.",
                "Expect application questions: scope, sequence, and what to do next.",
                "Know the certification and renewal requirements (recertification cycle, exam eligibility).",
            ],
        ),
        _b(
            "Medical terminology: word parts",
            "Medical terms are built from combining forms (roots), prefixes that "
            "modify meaning, and suffixes that define the word type. Learn to "
            "deconstruct unfamiliar terms rather than memorize whole words: "
            "hyper- (above) + glyc (sugar) + -emia (in the blood) gives hyperglycemia. "
            "The MedlinePlus medical encyclopedia is a free, government-reviewed "
            "reference for term definitions.",
            NLM_MEDLINEPLUS,
            [
                "Prefix: a- (no), an- (without), brady- (slow), tachy- (fast), hyper-/hypo- (too much/too little).",
                "Root: cardi (heart), myo (muscle), osteo (bone), gastro (stomach), nephro (kidney), hepato (liver).",
                "Suffix: -itis (inflammation), -ectomy (removal), -emia (in blood), -algia (pain), -scope (to view).",
                "Terminology also uses body-system suffixes: -ectomy, -otomy, -ostomy, -centesis, -graphy.",
            ],
        ),
        _b(
            "Anatomy and physiology study approach",
            "Physiology explains how body structures function; anatomy describes the "
            "structures themselves. For exam purposes, connect structure to function "
            "and to the clinical task: why the antecubital vein is a preferred "
            "venipuncture site, why insulin is given subcutaneously, or why an "
            "infiltrating IM injection hurts more than an obese patient's does. "
            "StatPearls on the NCBI Bookshelf provides reviewed clinical summaries "
            "for each system.",
            NCBI_BOOKSHELF,
            [
                "Organize study by system: cardiovascular, respiratory, GI, renal, musculoskeletal, nervous, "
                "endocrine, integumentary, reproductive.",
                "For each structure, be able to state its function and one clinical consequence of dysfunction.",
                "Know the divisions of the body: 10 body systems, 4 cavities, 3 planes (sagittal, coronal/frontal, "
                "transverse).",
            ],
        ),
        _b(
            "Preventive care and health screening",
            "The US Preventive Services Task Force publishes evidence-based "
            "recommendations on screening and prevention, graded from A (do it) "
            "to I (insufficient evidence). Screening decisions that come up most "
            "often include breast cancer, colorectal cancer, cervical cancer, "
            "lung cancer screening for people who smoke heavily, lipid screening, "
            "and bone density testing for women 65 and older. You will be "
            "expected to know who is due for what, and to document screening "
            "status at intake.",
            USPSTF,
            [
                "Recommendations are graded A, B, C, D, or I (insufficient evidence).",
                "Know the ages and intervals: colorectal screening begins at 45 for average-risk adults.",
                "Patient education should not overstate benefit — screening can have harms and false positives.",
            ],
        ),
        _b(
            "Screening intervals and counseling topics",
            "The USPSTF publishes the full list of recommendation topics, each "
            "with the population, the age or interval, and the strength of the "
            "evidence. Alongside screening, the Task Force also issues "
            "recommendations on counseling and preventive medication — for "
            "example, tobacco cessation in adults, and diet and physical activity "
            "counseling for patients with cardiovascular risk. In the office, this "
            "is what turns a routine visit into prevention.",
            USPSTF_TOPICS,
            [
                "Check whether the patient's last screening is due before the visit ends.",
                "Document screening status in one place so it is visible to the whole care team.",
                "Counseling on smoking, nutrition, and activity is itself a preventive recommendation.",
            ],
        ),
        _b(
            "Cancer screening and referral",
            "The National Cancer Institute explains how cancers are found and "
            "treated, what screening can and cannot do, and what to expect after "
            "an abnormal result. For the medical assistant, the practical points "
            "are the screening schedule by age and risk, the referral pathway for "
            "an abnormal result, and the emotional care involved when a patient "
            "is told to wait for a diagnostic workup.",
            NCI_CANCER,
            [
                "A screening test is not a diagnosis — an abnormal screen needs diagnostic follow-up.",
                "Document the screening result, the referral, and the follow-up plan so the loop is closed.",
                "Reassure without minimizing: many abnormalities turn out to be benign.",
            ],
        ),
        _b(
            "Nutrition, weight and healthy eating",
            "The Dietary Guidelines for Americans describe a balanced eating pattern: "
            "vegetables, fruits, grains, protein foods, dairy or fortified "
            "alternatives, and healthy fats, with limits on added sugar, sodium, "
            "and saturated fat. For exam purposes, know the components of a "
            "balanced diet, the effect of diet on blood pressure and diabetes, and "
            "how to give practical, non-judgmental nutrition counseling.",
            DIETARY_GUIDELINES,
            [
                "Sodium reduction has a measurable effect on blood pressure.",
                "For diabetes, carbohydrate quantity and distribution drive glucose excursions.",
                "Counseling should be individualized and use teach-back — see the coordination topic.",
            ],
        ),
        _b(
            "Sleep, physical activity and stress",
            "CDC recommends adults get at least seven hours of sleep per night; "
            "short sleep is linked to diabetes, obesity, hypertension, and "
            "depression. The same guidance recommends at least 150 minutes of "
            "moderate-intensity aerobic activity a week plus muscle-strengthening "
            "activity on two or more days. These are the numbers you will "
            "reinforce when counseling patients with chronic disease.",
            CDC_SLEEP,
            [
                "Sleep problems and daytime fatigue are common presenting complaints in primary care.",
                "For older adults, distinguish age-related changes from sleep disorders and medication effects.",
                "Sedentary behavior is a modifiable risk factor for heart disease, diabetes, and osteoporosis.",
            ],
        ),
        _b(
            "Physical activity and the cardiovascular patient",
            "For patients with heart disease, diabetes, or hypertension, physical "
            "activity is a treatment, not just advice. CDC frames the "
            "recommendation as a gradual build toward 150 minutes of moderate "
            "activity per week plus muscle-strengthening on two days, and "
            "describes the specific benefits for blood pressure, insulin "
            "sensitivity, mood, and sleep. Know when activity needs medical "
            "clearance first, and what to tell a patient who is inactive and "
            "embarrassed about it.",
            CDC_PHYSICAL_ACTIVITY,
            [
                "Start from the patient's current activity level; small increases count.",
                "Warn signs that require stopping: chest pain, dizziness, unusual shortness of breath, palpitations.",
                "Activity advice is more effective when written down and reviewed at the next visit.",
            ],
        ),
        _b(
            "Other certifications in the same family",
            "The National Healthcareer Association administers several credentials "
            "that share the same health-care knowledge base. The Certified "
            "Electronic Technician (CET) covers the front office, billing, and "
            "medical office procedures, and the Certified Patient Care Technician "
            "(CPT) covers personal care, comfort measures, and basic clinical "
            "support. Understanding where they overlap helps you know which "
            "content applies to which role in the office.",
            NHA_CET,
            [
                "CET focuses on administrative procedures; CPT focuses on personal care and comfort measures.",
                "All three credentials are built on the same federal and state scope-of-practice rules.",
                "Certification is not a licence — state law still decides what you may perform.",
            ],
        ),
    ],
    "ccma-anatomy": [
        _b(
            "Levels of organization and anatomical language",
            "The human body is organized from the smallest to the largest: cell, "
            "tissue, organ, organ system, organism. Tissues include epithelial, "
            "connective, muscle, and nervous tissue. Anatomical position terms "
            "(superior/inferior, medial/lateral, proximal/distal, anterior/posterior) "
            "are used constantly in charting and in physical therapy or wound "
            "documentation.",
            NCBI_BOOKSHELF,
            [
                "Directional terms: superior/inferior, anterior/posterior, medial/lateral, proximal/distal, "
                "superficial/deep.",
                "Planes: sagittal divides left/right, coronal divides front/back, transverse divides top/bottom.",
                "Body cavities: cranial, vertebral, thoracic, abdominopelvic (subdivided by the diaphragm).",
                "Use the correct term in documentation — 'left antecubital' rather than 'left elbow'.",
            ],
        ),
        _b(
            "Cardiovascular system",
            "The heart is a four-chambered muscular pump: right atrium, right "
            "ventricle, left atrium, left ventricle, separated by septa and "
            "valves that maintain one-way flow. The cardiac output is the product "
            "of heart rate and stroke volume. Because the left ventricle pumps "
            "against systemic resistance, it generates the systemic blood pressure "
            "measured at the brachial artery.",
            NHLBI_HEALTH,
            [
                "Systolic pressure reflects ventricular contraction and stroke volume; diastolic reflects elastic "
                "recoil of the arteries.",
                "Valves: tricuspid, pulmonary, mitral, aortic — learn their atrioventricular and semilunar positions.",
                "The sinoatrial node sets the heart rate at roughly 60–100 beats per minute; the AV node delays it.",
            ],
        ),
        _b(
            "Respiratory system and gas exchange",
            "Air moves through the upper airway (nose, pharynx, larynx) into the "
            "trachea, bronchi, and lungs, where alveoli exchange oxygen and carbon "
            "dioxide across a thin membrane with the pulmonary capillaries. The "
            "diaphragm and intercostal muscles generate the negative pressure that "
            "draws air in. Normal adult respiratory rate is 12–20 breaths per "
            "minute and is a key sepsis screening measure.",
            CDC_COVID,
            [
                "Respiratory rate, SpO2 and work of breathing are the fastest way to spot deterioration.",
                "An adult respiratory rate above 20 or below 12 warrants prompt escalation per facility protocol.",
                "Respiratory infection spreads by droplets; TB additionally requires airborne precautions.",
            ],
        ),
        _b(
            "The endocrine system and diabetes",
            "The endocrine system uses hormones to regulate metabolism, growth, "
            "and the stress response. The pancreas, thyroid, adrenal glands, and "
            "pituitary are the most clinically relevant for a medical assistant. "
            "The pancreas is the key organ for the CCMA: insulin lowers blood "
            "glucose and glucagon raises it, and that single relationship "
            "underpins hypoglycemia teaching, insulin dosing, and sick-day rules.",
            NIDDK_DIABETES,
            [
                "Insulin lowers blood glucose; glucagon raises it — the basis of hypoglycemia teaching.",
                "The thyroid sets metabolic rate; hyperthyroidism speeds everything up and hypothyroidism slows "
                "everything down.",
                "Adrenal cortisol and adrenaline drive the fight-or-flight response.",
            ],
        ),
        _b(
            "The kidneys and fluid balance",
            "The kidneys filter the blood, regulate water and electrolytes, "
            "control blood pressure, and activate vitamin D. They are the target "
            "of several common medications, and they are the organ most often "
            "damaged by long-standing diabetes and hypertension. Fluid balance "
            "shows up in the vital signs as edema, orthostatic hypotension, and "
            "weight change.",
            NIDDK_KIDNEY,
            [
                "Kidney disease is common in diabetes and hypertension; the two account for a large share of chronic "
                "kidney disease.",
                "Fluid status shows in the vital signs: orthostatic hypotension, edema, and weight change.",
                "NSAIDs, certain antibiotics, and contrast media can be hard on the kidneys.",
            ],
        ),
        _b(
            "The nervous system",
            "The nervous system divides into the central nervous system (brain "
            "and spinal cord) and the peripheral nervous system (nerves and "
            "sensory receptors). It receives sensory input, integrates it, and "
            "coordinates the motor response. Neurologic assessment in the "
            "office means level of consciousness, orientation, strength, sensation, "
            "and reflexes — and recognizing the red flags that need escalation.",
            NINDS_HEALTH,
            [
                "Level of consciousness and orientation are the first and most important neurologic checks.",
                "Sudden weakness, facial droop, or speech change is a stroke emergency — use FAST.",
                "Peripheral neuropathy is one of the most common diabetes complications and is screened at every "
                "visit.",
            ],
        ),
        _b(
            "The musculoskeletal system and skin",
            "Muscle contraction is driven by motor neurons at the neuromuscular "
            "junction, releasing acetylcholine; bones provide structure, store "
            "minerals, and produce blood cells in marrow. The skin is the largest "
            "organ and the primary barrier to infection — which is why hand "
            "hygiene and wound care sit at the center of infection prevention.",
            NIAMS_HEALTH,
            [
                "Osteoporosis and arthritis are common in older adults and affect mobility, fall risk, and "
                "independence.",
                "Neurologic changes with age affect balance, reaction time, and medication safety.",
                "Skin breakdown (pressure injury) begins as non-blanching redness over a bony prominence.",
            ],
        ),
        _b(
            "How aging changes the body",
            "Normal aging changes vital signs, the cardiovascular system, the "
            "immune system, and the senses — and several of these changes look like "
            "disease if you do not expect them. Higher systolic blood pressure, "
            "slightly reduced pulse and respiratory reserve, and reduced renal and "
            "hepatic clearance are the classic exam items, and they directly change "
            "how you assess an older adult's symptoms.",
            ML_AGING_VITALS,
            [
                "Systolic blood pressure rises with age; diastolic may fall.",
                "Reduced baroreceptor responsiveness increases the risk of orthostatic hypotension.",
                "Reduced renal clearance means standard drug doses may need adjustment in older adults.",
            ],
        ),
    ],
    "ccma-clinical-care": [
        _b(
            "Standard Precautions for every patient",
            "Standard Precautions apply to all patients regardless of suspected or "
            "confirmed infection: hand hygiene, personal protective equipment when "
            "exposure to blood or body fluids is anticipated, respiratory hygiene "
            "and cough etiquette, safe injection practices, and appropriate patient "
            "placement. They are the baseline; Transmission-Based Precautions are "
            "added on top when a specific route of transmission is known.",
            CDC_INFECTION_CONTROL,
            [
                "Hand hygiene is required before and after every patient contact and before aseptic tasks.",
                "Gloves do not replace hand hygiene — perform it before gloving and after removing gloves.",
                "Standard Precautions are required for blood and body fluid, not only for 'dirty' patients.",
            ],
        ),
        _b(
            "Hand hygiene technique",
            "Alcohol-based hand rub is preferred for routine use when hands are not "
            "visibly soiled; soap and water are required after caring for a patient "
            "with suspected or confirmed norovirus, and before and after handling "
            "food or caring for a patient with C. difficile. The technique is "
            "friction-based: cover all hand surfaces and rub until dry. Time alone "
            "is not the target — coverage is.",
            CDC_HAND_HYGIENE,
            [
                "Alcohol-based rub: 20–30 seconds of friction over all hand surfaces.",
                "Soap and water: at least 20 seconds, including after restroom use and before eating.",
                "Five moments for hand hygiene: before touching a patient, before a clean/aseptic procedure, after "
                "body fluid exposure risk, after touching a patient, after touching patient surroundings.",
            ],
        ),
        _b(
            "Safe injection practices",
            "CDC's core rules are simple: a new needle and a new syringe for every "
            "injection, used once and only once. Never reuse a syringe or needle "
            "on another patient even if the needle has been changed, never "
            "administer medications from one syringe to multiple patients, and "
            "always use a safety-engineered needle and discard it immediately after "
            "use into a sharps container.",
            CDC_INJECTION_SAFETY,
            [
                "One needle, one syringe, one time — for every injection, every patient.",
                "Never recap a used needle; activate the safety feature and discard at the point of use.",
                "Use a new sterile needle and syringe for each entry into a vial, even for the same patient.",
            ],
        ),
        _b(
            "Vital signs and physical assessment",
            "Accurate vital signs are the backbone of clinical documentation. Use the "
            "correct cuff size — a cuff that is too small reads falsely high and one "
            "that is too large reads falsely low — rest the patient for at least "
            "five minutes, support the arm at heart level, and do not talk during "
            "the measurement. Document position, cuff size, and any change from the "
            "previous reading.",
            CDC_HBP_MEASURE,
            [
                "Correct cuff size: the bladder should cover about 80% of the upper arm circumference.",
                "Rest 5 minutes seated; feet flat, back supported, arm at heart level; no talking.",
                "Record the position used and repeat in the other arm if the first reading is unexpectedly high.",
            ],
        ),
        _b(
            "Patient education and preparation",
            "Preparing a patient for a procedure means setting expectations, "
            "checking identification, allergies, and relevant history, and giving "
            "plain-language instructions. Use teach-back: ask the patient to "
            "describe the plan in their own words. Teach-back is a quick check for "
            "understanding, not a test of the patient.",
            AHRQ_HEALTH_LITERACY,
            [
                "Use plain language and avoid medical jargon or explain it immediately.",
                "Chunk information and cover the most important points first.",
                "Confirm understanding of return precautions and who to call with questions.",
            ],
        ),
        _b(
            "Documentation of clinical care",
            "Document what you observed and what you did, at the time it happened. "
            "Include vital signs with the time obtained, the site and size of any "
            "injection, the lot number and expiration of vaccine and medication "
            "administered, specimen collection details, patient response and "
            "education given. Entries should be factual and legible; correct errors "
            "per policy rather than altering them.",
            NHA_CCMA,
            [
                "Record observations (objective data) separately from statements of opinion.",
                "Late entries must be identified as late entries with the actual time.",
                "Never document an intervention that was ordered but not performed.",
            ],
        ),
    ],
    "ccma-coordination": [
        _b(
            "What care coordination means",
            "Care coordination is the deliberate, organized, proactive management of "
            "a patient's care across multiple providers and settings. A medical "
            "assistant often owns the practical side of it: closing the loop on "
            "referrals, results, and follow-up so that no order is left hanging and "
            "no patient falls through a gap between services.",
            AHRQ_CARE_COORDINATION,
            [
                "Identify the patient's providers, payers, and active problems to avoid duplicate or conflicting care.",
                "Track every referral and every pending result until it is closed.",
                "Escalate to the clinician when a result is abnormal, a referral is refused, or the patient cannot be "
                "reached.",
            ],
        ),
        _b(
            "Care plans for chronic disease",
            "Chronic conditions such as diabetes, hypertension, and asthma are "
            "managed with written action plans that specify daily self-management, "
            "monitoring, medication, and what to do when symptoms change. The CDC "
            "describes chronic disease as the leading cause of death and "
            "disability, and effective care depends on the patient successfully "
            "carrying out the plan at home.",
            CDC_CHRONIC_DISEASE,
            [
                "Every plan should include monitoring (what the patient checks and how often), treatment, and return "
                "precautions.",
                "Confirm the patient's understanding of the plan at every visit and update the written version.",
                "Coordinate with the pharmacy, dietitian, and behavioral health as the plan requires.",
            ],
        ),
        _b(
            "Health literacy and teach-back",
            "Health literacy is the ability to understand and use information to "
            "make health decisions. AHRQ's teach-back method asks the patient to "
            "explain the plan back in their own words; if the explanation is "
            "unclear, the provider re-teaches and asks again. This shifts "
            "responsibility for misunderstanding away from the patient.",
            AHRQ_HEALTH_LITERACY,
            [
                "Frame it as a check on your own explanation: 'I want to be sure I explained this clearly.'",
                "Use the 'Chunk and Check' method for longer instructions.",
                "Provide written material at a readable level and in the patient's preferred language.",
            ],
        ),
        _b(
            "Referrals, results, and follow-up",
            "Referral workflow is a common source of error. Confirm the patient "
            "has the correct payer information, verify that the receiving provider "
            "received the request, and document the date the appointment was made. "
            "For results, use a defined policy for what gets communicated to the "
            "clinician and what gets communicated to the patient — abnormal results "
            "should reach a clinician the same day.",
            ML_LAB_TESTS,
            [
                "Check the patient's coverage and any referral authorization requirement before scheduling.",
                "Document the closing of the loop: who was told, when, and what the plan is.",
                "Never leave an abnormal result uncommunicated; escalate per office protocol.",
            ],
        ),
        _b(
            "Supporting patients and caregivers",
            "Caregivers — family members or paid aides — are part of the care team "
            "when the patient consents. They need clear instructions on medication "
            "management, warning signs, and when to call. For patients with dementia "
            "or limited capacity, involve the legally authorized representative and "
            "document the consent discussion.",
            ML_CAREGIVERS,
            [
                "Ask who the patient wants involved, and confirm legal authority when a caregiver acts on their "
                "behalf.",
                "Give caregivers written instructions they can refer to later.",
                "Reassess caregiver burden; respite and community resources are part of the plan.",
            ],
        ),
        _b(
            "Closing the visit",
            "A coordinated visit ends with a clear summary: what was done today, "
            "what the patient should do at home, what appointments are scheduled, "
            "and what would make them call the office. Provide written after-visit "
            "instructions and repeat the follow-up plan, since the last thing "
            "said is often the only thing remembered.",
            AHRQ_TEAMSTEPPS,
            [
                "Use a handoff that names the responsible person for each next step.",
                "Confirm the patient knows when and where the next visit is, and how to reschedule.",
                "Document the education delivered and the patient's response.",
            ],
        ),
    ],
    "ccma-admin": [
        _b(
            "The medical assistant as the front-office anchor",
            "Administrative duties include scheduling, registration, records "
            "management, insurance and billing support, and supply and equipment "
            "maintenance. The administrative record is a legal document: it must be "
            "accurate, complete, timely, and protected. Accuracy of demographics "
            "and insurance data directly affects billing and patient safety.",
            NHA_CCMA,
            [
                "Verify demographics, spelling of names, date of birth, and insurance at every visit — changes are "
                "common.",
                "Protect the schedule, the chart, and the badge as if they were clinical supplies.",
                "Know the difference between a scheduling problem and a clinical problem, and escalate appropriately.",
            ],
        ),
        _b(
            "Scheduling and triage",
            "Scheduling is a clinical task, not just a calendar task. The person "
            "answering the phone often triages: distinguishing an emergency that "
            "needs 911 from a same-day visit from a routine follow-up. Protocol "
            "should define how urgent complaints are escalated to a licensed "
            "clinician, and documentation should reflect the advice given.",
            AHRQ_PATIENT_SAFETY,
            [
                "New or worsening chest pain, severe shortness of breath, stroke symptoms, and uncontrolled bleeding "
                "are emergencies — direct the patient to call 911.",
                "Protect the schedule with buffer time and do not double-book urgent visits.",
                "Document the advice given during a triage call and the disposition the patient chose.",
            ],
        ),
        _b(
            "Medical records and documentation integrity",
            "The medical record is used for continuity of care, billing, legal "
            "purposes, and quality review. Records must be complete, accurate, "
            "legible, and available to authorized people. Making a correction "
            "requires the original entry to remain visible with the correction "
            "clearly identified, dated, timed, and signed — never overwriting or "
            "erasing.",
            ML_HEALTH_TOPICS,
            [
                "Only add to the chart; never delete or alter an existing entry.",
                "Late entries are identified as late entries with the actual time of the event.",
                "Release information only to authorized people, following the office's HIPAA procedure.",
            ],
        ),
        _b(
            "Insurance, Medicare and Medicaid basics",
            "Administrative staff must understand who is paying and what the plan "
            "requires. Medicare is federal health insurance for people 65 and older "
            "and for certain disabled people and those with end-stage renal "
            "disease; Medicaid covers low-income adults, children, pregnant "
            "people, and people with disabilities, jointly funded by states and the "
            "federal government. Preventive services and some screenings are "
            "covered without cost sharing.",
            MEDICARE_GOV,
            [
                "Verify eligibility and benefits before the visit; eligibility rules differ between Medicare and "
                "Medicaid.",
                "Collect copayment, deductible, and prior-authorization information at check-in.",
                "Preventive care and screening are often covered at no cost — confirm with the plan.",
            ],
        ),
        _b(
            "Billing, coding and the revenue cycle",
            "The revenue cycle runs from scheduling to claim submission to payment. "
            "Front-office accuracy — insurance card copies, demographics, and "
            "signed forms — determines whether a claim pays. Collect copayments, "
            "record payments in the system, and give receipts. Never promise a "
            "patient a coverage outcome; refer benefit questions to the plan or a "
            "financial counselor.",
            MEDICAID_GOV,
            [
                "Claim denials are usually administrative: missing authorization, wrong member ID, or a signature on "
                "file.",
                "Keep a copy of the patient's insurance card and any required consent forms.",
                "Report billing concerns to the billing office, not to the patient as a guarantee.",
            ],
        ),
        _b(
            "Office safety and supply management",
            "Administrative areas are still workplaces under OSHA rules: keep "
            "walkways clear, manage the hazard communication program for cleaning "
            "chemicals and other hazardous products, and stock emergency supplies. "
            "Medication, vaccines, and sterile supplies must be stored and rotated "
            "according to manufacturer and CDC guidance.",
            OSHA_HAZCOM,
            [
                "Safety Data Sheets (SDSs) must be accessible to every employee who handles a hazardous product.",
                "Rotate stock using first-expire, first-out; check expiration dates on a schedule.",
                "Keep sharps containers at the point of use and replace them at the fill line, never overfilling.",
            ],
        ),
    ],
    "ccma-communication": [
        _b(
            "Therapeutic communication and active listening",
            "Effective clinical communication uses open-ended questions, reflection, "
            "and validation. Active listening means giving full attention without "
            "interrupting, reflecting back what the patient said in your own words, "
            "and checking meaning rather than assuming it. Patients disclose more "
            "when they feel heard, which is how important symptoms are caught.",
            ML_HEALTH_TOPICS,
            [
                "Use open questions: 'What brings you in today?' rather than yes/no questions.",
                "Reflect: 'It sounds like the pain is worse at night — is that right?'",
                "Validate without over-promising: 'That sounds frustrating, and it makes sense that you'd be worried.'",
            ],
        ),
        _b(
            "Cultural humility and language access",
            "Culture affects health beliefs, diet, family roles, and the meaning of "
            "an illness. Ask rather than assume: ask the patient's preferred name, "
            "pronouns, and language; ask about health beliefs that affect the plan. "
            "Limited-English-proficiency patients must be offered qualified "
            "interpreter services rather than relying on family members, especially "
            "for consent and medication instructions.",
            ML_PATIENT_RIGHTS,
            [
                "Ask: 'What language do you prefer for medical conversations?'",
                "Use a qualified medical interpreter for consent, medication teaching, and discharge instructions.",
                "Documents about patient rights include the right to be treated with dignity and to have language "
                "assistance available.",
            ],
        ),
        _b(
            "Customer service in a medical setting",
            "Front-desk interactions set the tone for the visit. Greet patients by "
            "their preferred name, protect privacy by speaking quietly in public "
            "areas and using the private area for sensitive discussions, and never "
            "leave patients waiting without acknowledgment. Set realistic "
            "expectations about wait times instead of guessing at them.",
            AHRQ_PATIENT_SAFETY,
            [
                "Move sensitive conversations (billing balances, results, complaints) out of the waiting room.",
                "Acknowledge a wait: 'The clinician is with another patient who needed extra time.'",
                "Never use the waiting room to discuss a patient's condition with family members who are not "
                "authorized.",
            ],
        ),
        _b(
            "Health literacy and plain language",
            "About one in three adults in the United States has difficulty reading "
            "health information, so plain-language communication is a clinical "
            "skill, not a courtesy. Avoid jargon, use short sentences, and give "
            "specific numbers rather than vague advice ('take two pills every day at "
            "8 a.m. and 8 p.m.'). Confirm understanding before the patient leaves.",
            AHRQ_HEALTH_LITERACY,
            [
                "Write '8 a.m.' instead of 'qAM'.",
                "Use the 'Chunk and Check' method: three key points, then confirm each.",
                "Written materials should be at a 5th–6th grade reading level.",
            ],
        ),
        _b(
            "Phone, portal and electronic communication",
            "Phone triage, patient portals, and text reminders are all part of "
            "patient communication and carry the same privacy requirements as "
            "in-person visits. Confirm the patient's identity before disclosing "
            "any protected health information, and verify portal messaging is "
            "appropriate for the topic — the portal is not the right channel for "
            "an urgent problem.",
            ML_PATIENT_RIGHTS,
            [
                "Verify two identifiers before giving any information by phone.",
                "Send urgent instructions by phone and confirm receipt, not just that a message was sent.",
                "Document the communication method, time, and content.",
            ],
        ),
        _b(
            "Conflict, complaints and boundaries",
            "Most complaints are about communication rather than clinical care: "
            "feeling unheard, waiting without explanation, or a scheduling problem "
            "that was never resolved. Listen without interruption, apologize for "
            "the experience, and escalate substance to the office manager. Maintain "
            "professional boundaries — the relationship is therapeutic and "
            "professional, never social.",
            AMA_ETHICS,
            [
                "The AMA Code of Medical Ethics is built on principles of patient welfare, patient autonomy, and "
                "confidentiality.",
                "Never accept gifts or money that could influence care; document conflicts of interest.",
                "Report unsafe or unethical conduct through the organization's channels.",
            ],
        ),
    ],
    "ccma-law-ethics": [
        _b(
            "HIPAA: the privacy rule",
            "The HIPAA Privacy Rule limits how covered entities and business "
            "associates may use and disclose protected health information. The "
            "core operating rule is the minimum necessary standard: use only the "
            "information needed for the task, and disclose only to people involved "
            "in the patient's care or payment. Patients have enforceable rights to "
            "access and amend their records.",
            HHS_HIPAA_PRIVACY,
            [
                "Permitted disclosures include treatment, payment, and healthcare operations, plus required by law.",
                "Authorization is generally required for other uses, with specific exceptions.",
                "Workforce training is required, and sanctions apply to anyone who violates the rule.",
            ],
        ),
        _b(
            "HIPAA: the security rule",
            "The Security Rule adds safeguards for electronic protected health "
            "information: administrative, physical, and technical protections. "
            "Administrative safeguards include a security management process, risk "
            "analysis, workforce security, and contingency planning. Technical "
            "safeguards cover access control, audit controls, integrity, and "
            "transmission security.",
            HHS_HIPAA_SECURITY,
            [
                "Access to records is role-based; use individual logins and never share passwords.",
                "Audit controls track who accessed what and when.",
                "Workstations in shared areas should be locked when unattended.",
            ],
        ),
        _b(
            "OSHA bloodborne pathogens standard",
            "29 CFR 1910.1030 applies to occupations with reasonable expectation of "
            "exposure to blood or other potentially infectious materials. It "
            "requires an exposure control plan, universal precautions, engineering "
            "and work practice controls, personal protective equipment, hepatitis B "
            "vaccination, post-exposure evaluation and follow-up, and annual "
            "training with recordkeeping.",
            OSHA_BBP,
            [
                "The standard is performance-based: it sets the outcome (e.g., 'contaminated sharps shall be disposed "
                "of in a manner that prevents employee exposure') rather than a specific device.",
                "Annual training is mandatory and must be documented.",
                "Post-exposure evaluation and follow-up must be offered promptly after an exposure.",
            ],
        ),
        _b(
            "Consent, capacity, and scope of practice",
            "Informed consent requires disclosure of the nature and purpose of the "
            "procedure, its material risks and benefits, alternatives including the "
            "option of doing nothing, and the patient's right to withdraw. Consent "
            "must be documented. Separately, medical assistants work within state "
            "law, licensure, and the limits of their employer's policies and any "
            "delegated order — never outside them.",
            AMA_ETHICS,
            [
                "Consent is a process, not a signed form.",
                "A patient's refusal is a valid choice that must be documented without pressure.",
                "Know which tasks require an order (injections, medications, wound care) and which do not.",
            ],
        ),
        _b(
            "Mandatory reporting and fraud awareness",
            "State law requires certain professionals to report suspected abuse or "
            "neglect of children, older adults, and vulnerable adults; the specific "
            "obligations and timelines vary by state. Billing and documentation "
            "must reflect what actually happened — altering claims or records to "
            "increase payment is fraud and exposes the individual and the practice "
            "to severe consequences.",
            ML_PATIENT_RIGHTS,
            [
                "Suspected abuse or neglect → follow the mandatory reporting pathway and document your report.",
                "Never falsify a diagnosis, a code, a record, or a time entry.",
                "Report concerns through the supervisor or compliance channel before acting outside your role.",
            ],
        ),
        _b(
            "Ethical practice and professional boundaries",
            "The AMA Code of Medical Ethics gives the framework most exam items "
            "reference: patient welfare, autonomy, confidentiality, and "
            "professionalism. In practice this means accurate documentation, honest "
            "reporting of errors, respecting confidentiality in hallways and "
            "break rooms, and refusing any task that would compromise safety.",
            AMA_ETHICS,
            [
                "Errors should be reported promptly so the patient can be assessed and the system can be fixed.",
                "Never photograph or discuss patients on personal devices or social media.",
                "Protect credentials: do not sign documents outside your scope or allow someone to use your login.",
            ],
        ),
    ],
    "ccma-vaccines": [
        _b(
            "Vaccine storage and the cold chain",
            "The CDC storage and handling toolkit is the reference for vaccine "
            "management in clinics. Most refrigerated vaccines must be kept between "
            "2 °C and 8 °C (36 °F and 46 °F); specific products have different "
            "requirements, so always follow the manufacturer package insert. The "
            "cold chain is broken by a single excursion — temperature monitoring, "
            "a written vaccine management plan, and documented action on any "
            "excursion are what protect the supply.",
            CDC_VACCINE_STORAGE,
            [
                "Use a purpose-built or pharmaceutical-grade unit, not a dorm-style mini-fridge, and keep a data "
                "logger in the unit.",
                "Record temperatures twice daily, including minimum and maximum, on a monitoring log.",
                "Quarantine vaccines that have been out of range and contact the immunization program — do not "
                "administer until viability is confirmed.",
            ],
        ),
        _b(
            "Vaccine administration: preparation and screening",
            "Before administering a vaccine, verify the correct patient, product, "
            "route, and dose; confirm the schedule and the interval since the last "
            "dose; and screen for contraindications and precautions, including "
            "current moderate or severe acute illness, prior dose reactions, "
            "allergies to components, pregnancy, and immunocompromising "
            "conditions. Give the Vaccine Information Statement (VIS) before "
            "vaccination.",
            CDC_VACCINE_ADMIN,
            [
                "Two independent checks of the correct product, lot, expiration date, and patient are required.",
                "Reconcile the immunization record before giving the dose so the patient is not over- or "
                "under-immunized.",
                "Document the vaccine type, manufacturer, lot number, expiration date, site, route, dose, and the date "
                "and time.",
            ],
        ),
        _b(
            "Needle selection, site and technique",
            "CDC best practices specify a 1 mL syringe for intramuscular injections "
            "and a 1- to 1.5-inch needle for adults and 1 inch for children, with "
            "larger needles for larger patients. The deltoid is the standard site "
            "for adults, using the landmark of three finger-breadths below the "
            "acromion process. Insert at a 90-degree angle, aspirate per policy, "
            "and inject steadily.",
            CDC_IMZ_BEST_PRACTICES,
            [
                "Deltoid site: three finger-breadths below the acromion process; avoid the axilla and the shoulder "
                "tip.",
                "Inject into the thickest part of the muscle, at 90 degrees.",
                "Z-track technique for subcutaneous injections reduces leakage and irritation.",
            ],
        ),
        _b(
            "Needle safety and sharps handling",
            "The safest sharps practice is not to have an injury. Activate the "
            "needle's safety feature immediately after use, never recap, never "
            "remove used devices from a sharps container, and never leave a "
            "sharps container where it can be knocked over or overfilled. "
            "Discard the device at the point of use.",
            OSHA_BBP_STANDARDS,
            [
                "Contaminated sharps must be placed directly in puncture-resistant sharps containers.",
                "Do not bend, break, or recap used needles.",
                "Fill line limits prevent overfilling and hand injuries — replace before the line.",
            ],
        ),
        _b(
            "Schedules, registries, and documentation",
            "The CDC publishes the child and adult immunization schedules and the "
            "Immunization Information System (IIS) guidance. The office must know "
            "the current schedule, the minimum ages and intervals (including the "
            "4-day grace rule and the 30-day minimum interval rule), and how to "
            "report doses to the state immunization information system.",
            CDC_IMZ_SCHEDULES,
            [
                "Minimum intervals and minimum ages define when a dose counts.",
                "The IIS is the source of truth for many patients; reconcile records at every visit.",
                "Report doses to the state IIS within the required timeframe.",
            ],
        ),
        _b(
            "Vaccine Information Statements and post-vaccination care",
            "The VIS is a standardized one-page document that must be provided "
            "before vaccination and reviewed with the patient. After administration, "
            "observe the patient for 15 minutes if there is any risk of "
            "anaphylaxis, then document the observation. Report adverse events "
            "through the Vaccine Adverse Event Reporting System and treat a "
            "suspected anaphylactic reaction immediately.",
            CDC_VIS,
            [
                "Provide the current VIS version; do not use an outdated form.",
                "15-minute observation is recommended for syncope risk and for allergy risk.",
                "Anaphylaxis after vaccination is rare but requires immediate epinephrine and emergency activation.",
            ],
        ),
        _b(
            "Vaccine-preventable diseases",
            "The CDC's Pink Book, Epidemiology and Prevention of "
            "Vaccine-Preventable Diseases, is the reference for the diseases that "
            "vaccination prevents and for the effectiveness of each vaccine. It "
            "explains why the recommended schedule looks the way it does — the "
            "spacing between doses exists because immunity is built over time and "
            "because maternal antibodies protect infants for the first months of "
            "life.",
            CDC_PINKBOOK,
            [
                "Spacing between doses reflects how long it takes to build protection, not an arbitrary rule.",
                "Combination vaccines protect against several diseases in fewer visits.",
                "A missed dose does not restart the series — catch up on the recommended schedule.",
            ],
        ),
    ],
    "ccma-hipaa": [
        _b(
            "What PHI is",
            "Protected health information is individually identifiable health "
            "information held or transmitted by a covered entity or business "
            "associate. It includes the obvious identifiers — name, address, phone, "
            "record number, dates of service — and any other information that could "
            "identify the patient, including the fact that a person is a patient "
            "at a particular clinic.",
            HHS_HIPAA,
            [
                "De-identified information is no longer PHI once 18 identifiers have been removed.",
                "Information shared with a business associate requires a written agreement.",
                "Discussing a patient's visit in public areas is an impermissible disclosure.",
            ],
        ),
        _b(
            "Permitted uses and disclosures",
            "Covered entities may use and disclose PHI without written "
            "authorization for treatment, payment, and healthcare operations, and in "
            "a limited set of other circumstances: public health reporting, "
            "mandated reporting, law enforcement requests, judicial and "
            "administrative proceedings, and certain research and donor "
            "situations. Everything else requires the patient's written "
            "authorization.",
            HHS_HIPAA_PRIVACY,
            [
                "Treatment can be disclosed to any provider involved in the patient's care without an authorization.",
                "A patient's family is not automatically entitled to information — ask the patient who may receive "
                "information.",
                "Substance-use disorder records have separate protections under 42 CFR Part 2.",
            ],
        ),
        _b(
            "The minimum necessary standard",
            "For most uses and disclosures, covered entities must limit the "
            "information used or disclosed to the minimum necessary to accomplish "
            "the purpose. Access to a chart should reflect the person's role, and "
            "workstations in shared clinical areas should be locked whenever "
            "unattended. Convenience is not a permitted reason to see more than "
            "you need.",
            ECFR_HIPAA_PRIVACY,
            [
                "The standard does not apply to disclosures for treatment.",
                "Role-based access: assign logins by job function and review them regularly.",
                "Never leave a chart open on an unattended workstation.",
            ],
        ),
        _b(
            "Patient rights under HIPAA",
            "Patients have the right to access their records and to request an "
            "amendment, to receive an accounting of certain disclosures, to "
            "request restrictions on uses and disclosures, and to receive a paper "
            "copy of the notice of privacy practices. Requests must be handled "
            "within the regulatory timelines, and denial of an amendment can be "
            "appealed.",
            HHS_HIPAA_COVERED,
            [
                "Access requests are generally answered within 30 days.",
                "The right to an accounting covers disclosures made by the organization, not by the patient.",
                "The notice of privacy practices must be provided at registration and whenever it changes.",
            ],
        ),
        _b(
            "The Security Rule and safeguards",
            "The Security Rule requires administrative, physical, and technical "
            "safeguards for electronic PHI. Administrative safeguards include risk "
            "analysis, workforce security, information access management, and "
            "contingency planning. Physical safeguards include facility access "
            "controls and device and media controls. Technical safeguards include "
            "unique user identification, emergency access, audit controls, "
            "integrity, and transmission security.",
            HHS_HIPAA_SECURITY,
            [
                "Risk analysis is the foundation — it drives which safeguards you actually need.",
                "Never share a login; use individual credentials and log out when leaving a workstation.",
                "Dispose of paper records with PHI in a secure, approved manner.",
            ],
        ),
        _b(
            "Breaches and the notification rule",
            "A breach is an impermissible use or disclosure of PHI that compromises "
            "the security of the information. When a breach occurs, the covered "
            "entity must document it, conduct a risk assessment, and notify "
            "affected individuals without unreasonable delay and no later than 60 "
            "calendar days after discovery. Small breaches affecting fewer than 500 "
            "individuals are reported to the Secretary annually.",
            ECFR_HIPAA_SECURITY,
            [
                "Report suspected breaches to the privacy officer immediately — do not wait to confirm.",
                "Misdirected faxes, email to the wrong recipient, and lost devices are common reportable events.",
                "Do not attempt to investigate or conceal a breach on your own.",
            ],
        ),
    ],
    "ccma-transmission": [
        _b(
            "Standard Precautions versus Transmission-Based Precautions",
            "Standard Precautions are used for every patient, all the time. "
            "Transmission-Based Precautions are added when a specific route of "
            "transmission is known: contact precautions for organisms spread by "
            "direct and indirect contact, droplet precautions for large droplets "
            "that travel short distances, and airborne precautions for organisms "
            "that remain suspended in air. Precautions are discontinued only when "
            "the clinician or infection prevention says so.",
            CDC_ISOLATION_PRECAUTIONS,
            [
                "Transmission-Based Precautions are in addition to Standard Precautions, never a replacement.",
                "Each precaution category specifies its own PPE, room type, and patient placement.",
                "Removing a patient from precautions is a clinician decision, not a scheduling convenience.",
            ],
        ),
        _b(
            "Contact precautions",
            "Contact precautions are used for organisms spread by direct or indirect "
            "contact, such as MRSA, VRE, C. difficile, scabies, and RSV in some "
            "settings. The core interventions are a gown and gloves, dedicated "
            "equipment where indicated, careful environmental cleaning, and "
            "properly handled laundry and waste.",
            CDC_NIOSH_INFECTIOUS,
            [
                "Don a gown and gloves for every room entry while the precaution is in place.",
                "Use dedicated equipment (stethoscope, blood pressure cuff) or disinfect shared equipment between "
                "patients.",
                "C. difficile spores require soap and water for hand hygiene — alcohol rub is not sufficient.",
            ],
        ),
        _b(
            "Droplet precautions",
            "Droplet precautions apply to pathogens transmitted by respiratory "
            "droplets generated by coughing, sneezing, or talking — influenza, "
            "pertussis, meningococcal disease, and diphtheria among them. The "
            "intervention is a surgical mask on the patient during transport and "
            "a mask on healthcare workers who enter the room. Place the patient in "
            "a private room if possible.",
            CDC_FLU,
            [
                "Mask the patient first — source control is the most effective measure.",
                "Use a surgical mask, not a respirator, for droplet precautions.",
                "Teach the patient to cover the cough and to wear the mask during transport.",
            ],
        ),
        _b(
            "Airborne precautions",
            "Airborne precautions are required for airborne transmissible diseases "
            "such as pulmonary tuberculosis, measles, and varicella. The room must "
            "be negative pressure with at least 12 air changes per hour, and "
            "healthcare workers must wear a fit-tested N95 or higher respirator. "
            "Suspected pulmonary TB patients should be moved to an airborne "
            "infection isolation room and evaluated promptly.",
            CDC_TB_HCP,
            [
                "Apply an N95 or higher respirator and verify the seal (user seal check) before entering.",
                "Negative-pressure rooms need monitoring and verification of correct air changes.",
                "Airborne precautions require the fastest possible escalation — notify the infection control team.",
            ],
        ),
        _b(
            "Bloodborne pathogens in healthcare",
            "HIV, hepatitis B, hepatitis C, and tuberculosis are the bloodborne "
            "and blood-borne-spore pathogens that shape healthcare precautions. "
            "Hepatitis B is the one that health-care workers can be vaccinated "
            "against, and it is transmitted through blood, body fluids, and "
            "needlesticks. Hepatitis C is bloodborne and has no vaccine. HIV is "
            "transmitted through blood and body fluids, and standard "
            "precautions are the protection.",
            CDC_HEPATITIS_B,
            [
                "Hepatitis B vaccination is offered to health-care workers with exposure risk.",
                "Hepatitis C has no vaccine — prevention depends entirely on exposure control.",
                "The 'three sharps' rule: contaminated sharps, contaminated equipment, and the sharps container "
                "itself.",
            ],
        ),
        _b(
            "HIV and other bloodborne infections",
            "HIV can be transmitted in health-care settings through needlesticks "
            "and significant exposure to infected blood. Following an exposure, "
            "post-exposure prophylaxis can be started within hours, which is why "
            "immediate reporting matters. The CDC's HIV pages describe how the "
            "virus is and is not transmitted, which is often the basis for "
            "patients' questions about exposure risk.",
            CDC_HIV,
            [
                "Post-exposure prophylaxis is time-critical — report the exposure immediately.",
                "Standard Precautions apply to every patient; there is no 'safe' patient to relax them for.",
                "Confidentiality after an exposure is protected by law.",
            ],
        ),
        _b(
            "Tuberculosis basics",
            "Tuberculosis is spread through the air when a person with active "
            "pulmonary disease coughs or speaks, which is why it requires "
            "airborne precautions rather than droplet precautions. Most "
            "exposures never lead to disease, but latent infection can reactivate "
            "later, and screening and treatment of latent TB are core public "
            "health activities that a medical assistant often supports.",
            CDC_TB,
            [
                "TB is airborne, not droplet — the isolation room and respirator are essential.",
                "Latent TB infection is not contagious but must be identified and treated.",
                "A cough lasting more than three weeks should prompt TB screening per protocol.",
            ],
        ),
        _b(
            "Bloodborne pathogen exposure in healthcare",
            "NIOSH identifies infectious agents, bloodborne diseases, and "
            "chemical hazards as the major occupational risk categories for "
            "healthcare workers. Exposure to bloodborne pathogens occurs through "
            "needlesticks, splashes to mucous membranes, and contact with damaged "
            "skin. Prevention is engineered: sharps with safety features, "
            "needleless systems, and prompt disposal.",
            CDC_NIOSH_BBP,
            [
                "Transmission routes: percutaneous injury, mucous membrane splash, and contact with non-intact skin.",
                "Most exposures are preventable with safety-engineered sharps and no recapping.",
                "Immediate post-exposure evaluation is time-critical — report at once.",
            ],
        ),
        _b(
            "Cleaning, disinfection, and environmental controls",
            "Environmental surfaces are touched constantly and are a reservoir for "
            "transmission. Clean and disinfect patient care equipment and frequently "
            "touched surfaces between patients, use an appropriate EPA-registered "
            "product with the correct contact time, and follow the manufacturer's "
            "instructions for equipment disinfection. Reprocess reusable "
            "equipment according to the Spaulding classification.",
            CDC_INFECTION_CONTROL,
            [
                "Follow the disinfectant's contact time and dilution exactly — the most common failure is wiping it "
                "off early.",
                "Clean patient rooms and shared equipment between patients.",
                "Ensure adequate staffing and supplies; understaffing is a major driver of infection transmission.",
            ],
        ),
    ],
    "ccma-diabetes": [
        # ------------------------------------------------------------------
        # Types, prediabetes, and A1C
        # ------------------------------------------------------------------
        _b(
            "Type 1 (T1DM) and type 2 (T2DM) diabetes",
            "Type 1 diabetes (T1DM) is an autoimmune disease in which the immune system destroys the insulin-producing "
            "beta cells of the pancreas, so the body makes little or no insulin and daily insulin is required. It "
            "usually appears quickly, most often in children and young adults, though it can start at any age. Type 2 "
            "diabetes (T2DM) develops over years as the body stops using insulin well and the pancreas cannot keep up. "
            "It accounts for about 90 to 95 percent of diagnosed cases and is often found on routine screening.",
            CDC_TYPE_2,
            [
                "T1DM: autoimmune loss of beta cells; insulin is required to survive.",
                "T2DM: insulin resistance plus a gradual decline in insulin production; lifestyle changes can prevent "
                "it.",
                "Gestational diabetes begins in pregnancy and usually resolves after delivery, but it raises later "
                "risk.",
            ],
        ),
        _b(
            "What is prediabetes",
            "Prediabetes means blood glucose is higher than normal but not high enough for a diabetes diagnosis. The "
            "ranges are a fasting plasma glucose of 100 to 125 mg/dL, a 2-hour oral glucose tolerance test of 140 to "
            "199 mg/dL, or an A1C of 5.7 to 6.4 percent. More than 2 in 5 U.S. adults have prediabetes, and about 8 in "
            "10 "
            "of them do not know it. It raises the risk of type 2 diabetes, heart disease, and stroke. Weight loss, "
            "healthy eating, and regular physical activity can prevent or delay type 2 diabetes.",
            CDC_PREDIABETES,
            [
                "FPG 100–125 mg/dL, 2-hour OGTT 140–199 mg/dL, A1C 5.7–6.4%.",
                "Most people with prediabetes do not know it, so screening is how it is found.",
                "Lifestyle change is the main prevention strategy named by CDC.",
            ],
        ),
        _b(
            "What is an A1C and its levels",
            "A1C measures the percentage of hemoglobin in red blood cells that has glucose attached. Red blood cells "
            "live about 3 months, so the test reflects average glucose over roughly the past 2 to 3 months, not a "
            "single "
            "reading. Normal is below 5.7 percent, prediabetes is 5.7 to 6.4 percent, and diabetes is 6.5 percent or "
            "higher. CDC's table gives the estimated average glucose: 6 percent is about 126 mg/dL, 7 percent about "
            "154, "
            "8 percent about 183, 9 percent about 212, and 10 percent about 240.",
            CDC_A1C,
            [
                "Normal below 5.7%; prediabetes 5.7–6.4%; diabetes 6.5% or higher.",
                "The estimated average glucose may miss spikes and lows, so it does not replace home glucose checks.",
                "Anemia, kidney failure, liver disease, transfusion, and pregnancy can make A1C read falsely high or "
                "low.",
            ],
        ),
        # ------------------------------------------------------------------
        # Complications
        # ------------------------------------------------------------------
        _b(
            "Diabetes complications: heart disease and stroke",
            "Over time, high blood glucose damages blood vessels throughout the body, which raises the risk of heart "
            "disease and stroke. Diabetes is one of the leading risk factors for these conditions, so blood pressure, "
            "cholesterol, and weight are managed alongside glucose. Clinics track these numbers because the "
            "cardiovascular "
            "damage develops silently for years.",
            CDC_DIABETES_HEART,
            [
                "Heart disease and stroke are among the complications CDC names for diabetes.",
                "Managing blood pressure and cholesterol lowers the cardiovascular risk of diabetes.",
            ],
        ),
        _b(
            "Diabetes complications: eyes and vision loss",
            "Diabetic retinopathy damages the blood vessels of the retina, the light-sensing nerve tissue at the back "
            "of "
            "the eye. Weakened vessels leak fluid that swells the macula and distorts central vision; this macular "
            "edema "
            "is the most common cause of blindness in people with retinopathy. In advanced disease the retina grows "
            "fragile "
            "new vessels that can bleed heavily and block vision. CDC reports that diabetes is a leading cause of "
            "adult "
            "blindness in the United States.",
            CDC_VISION_LOSS,
            [
                "Blurred or distorted central vision is a warning sign that needs an eye exam.",
                "Regular dilated eye exams find retinopathy before the patient notices vision loss.",
                "Macular edema is the most common cause of blindness in retinopathy.",
            ],
        ),
        _b(
            "Diabetes complications: kidneys",
            "Diabetes is a leading cause of kidney failure in the United States. High glucose damages the tiny "
            "filtering "
            "vessels of the kidneys, and the damage can progress to kidney failure that requires dialysis or a "
            "transplant. "
            "Kidney damage can develop without obvious symptoms, which is why routine kidney testing is part of "
            "diabetes care.",
            CDC_KIDNEY_DISEASE,
            [
                "Diabetes is one of the leading causes of kidney failure, according to CDC.",
                "Kidney failure can require dialysis or a transplant; early damage often has no symptoms.",
            ],
        ),
        _b(
            "Diabetes complications: nerves, feet, and skin",
            "Diabetic nerve damage (neuropathy) reduces feeling in the feet, so small cuts, blisters, and pressure "
            "sores go "
            "unnoticed. Poor circulation and infection then turn them into ulcers, and diabetes is a leading cause of "
            "lower-limb amputation. NIDDK lists sores that do not heal and frequent infections among the symptoms of "
            "diabetes, and both should be reported the same day.",
            ML_DIABETIC_FOOT,
            [
                "Daily foot inspection and well-fitted shoes reduce the risk of ulcers and amputation.",
                "Sores that do not heal and frequent infections are warning signs of diabetes.",
            ],
        ),
        # ------------------------------------------------------------------
        # Gestational diabetes
        # ------------------------------------------------------------------
        _b(
            "Gestational diabetes and risk factors",
            "Gestational diabetes develops during pregnancy in a woman who did not have diabetes before. About 5 to 9 "
            "percent of U.S. pregnancies are affected each year. Higher-risk women include those with a previous "
            "pregnancy "
            "with gestational diabetes, a previous baby weighing over 9 pounds, overweight, a family history of type 2 "
            "diabetes, polycystic ovary syndrome (PCOS), and African American, Hispanic or Latino, American Indian, "
            "Alaska "
            "Native, Native Hawaiian, or Pacific Islander background. It usually resolves after birth but raises the "
            "mother's lifetime risk of type 2 diabetes.",
            CDC_GESTATIONAL,
            [
                "Risk factors: prior gestational diabetes, prior baby over 9 lb, overweight, family history, PCOS.",
                "Certain racial and ethnic groups are at higher risk, as listed above.",
                "About half of women with gestational diabetes later develop type 2 diabetes, according to CDC.",
            ],
        ),
        _b(
            "The test for gestational diabetes",
            "Gestational diabetes is screened for in pregnancy, usually between 24 and 28 weeks, and earlier for "
            "people at "
            "higher risk. The ADA describes two approaches: a one-step 75-gram, 2-hour oral glucose tolerance test, or "
            "a "
            "two-step process that starts with a 50-gram glucose challenge and a 1-hour blood draw, followed by a "
            "100-gram, "
            "3-hour test if the first result is high. The clinician orders the protocol. If glucose is high early in "
            "pregnancy, the patient may have type 1 or type 2 diabetes instead.",
            ADA_STANDARDS,
            [
                "Screening window is 24 to 28 weeks, earlier when risk is high (CDC).",
                "One-step test: 75 g glucose load with a 2-hour sample.",
                "Two-step test: 50 g challenge, then a 100 g test if the first result is high; record vomiting, since "
                "it can invalidate the result.",
            ],
        ),
        _b(
            "How gestational diabetes affects the fetus",
            "Extra glucose crosses the placenta, and the baby responds by making extra insulin, which drives excess "
            "growth. "
            "Babies born large (macrosomia, 4,000 g or more) face a higher risk of shoulder dystocia, when a shoulder "
            "gets "
            "stuck during birth, and related injuries such as clavicle fracture and brachial plexus injury. Newborns "
            "can also "
            "have low blood sugar and breathing problems after birth. In two trials, treating gestational diabetes "
            "lowered "
            "macrosomia from 21 and 14 percent to 10 and 6 percent.",
            NIDDK_GDM_CHAPTER,
            [
                "Macrosomia: birth weight of 4,000 g (about 8.8 lb) or more.",
                "Shoulder dystocia is about 13% in macrosomic infants and about 1% under 4,000 g.",
                "Newborn risks include low blood sugar after birth and breathing problems.",
            ],
        ),
        _b(
            "Symptoms of gestational diabetes",
            "Gestational diabetes often has no symptoms, so it is found by screening rather than by how the patient "
            "feels. "
            "When symptoms occur they are usually mild, such as increased thirst or needing to urinate more often. "
            "Testing "
            "is the only way to confirm the diagnosis.",
            CDC_GESTATIONAL,
            [
                "Often no symptoms at all.",
                "Mild symptoms: increased thirst and more frequent urination.",
                "Do not diagnose from symptoms alone; route results to the clinician.",
            ],
        ),
        # ------------------------------------------------------------------
        # Hyper- and hypoglycemia
        # ------------------------------------------------------------------
        _b(
            "Difference between hyperglycemia and hypoglycemia",
            "Hypoglycemia is low blood glucose, generally below 70 mg/dL for people on insulin or certain diabetes "
            "medicines, "
            "and it can become an emergency. Hyperglycemia is blood glucose above the patient's target; the diagnostic "
            "thresholds are a fasting plasma glucose of 126 mg/dL or higher and an A1C of 6.5 percent or higher. "
            "Hypoglycemia "
            "can develop quickly and needs treatment now. Hyperglycemia develops gradually in type 2 and can become "
            "rapid in type 1.",
            NIDDK_LOW_BLOOD_GLUCOSE,
            [
                "Hypo: below 70 mg/dL; shakiness, hunger, sweating, confusion, irritability.",
                "Hyper: thirst, frequent urination, hunger, blurred vision, fatigue, slow-healing sores, frequent "
                "infections.",
                "The clinician sets which number counts as low for each patient.",
            ],
        ),
        _b(
            "Treatment for hypoglycemia",
            "Treat a conscious person with low blood glucose right away with 15 to 20 grams of fast-acting "
            "carbohydrate, such "
            "as four glucose tablets, one tube of glucose gel, 4 ounces of regular juice or soda, or 1 tablespoon of "
            "sugar "
            "or honey. Recheck blood glucose after 15 minutes and repeat if it is still low. Once it is corrected, eat "
            "a "
            "snack if the next meal is more than an hour away. When a person is too severely low to swallow safely, "
            "glucagon "
            "by injection or nasal spray is the treatment, and 911 should be called.",
            NIDDK_LOW_BLOOD_GLUCOSE,
            [
                "15-15 rule: 15 to 20 g of carbohydrate, recheck in 15 minutes, repeat if still low.",
                "Glucose tablets or gel work fastest for patients taking medicines that slow digestion.",
                "Never give food or drink to an unconscious person; give glucagon and call 911.",
            ],
        ),
        _b(
            "Treatment for hyperglycemia",
            "High blood glucose is treated under the clinician's orders. Typical measures include correction insulin "
            "or "
            "medication changes, fluids, and activity as prescribed, with repeat glucose checks. Medical assistants do "
            "not "
            "change insulin doses or medicines on their own. They record the reading, symptoms, food, and insulin "
            "given, and "
            "report them to the clinician the same day. Very high glucose with vomiting, abdominal pain, fruity "
            "breath, "
            "trouble breathing, confusion, or fainting is an emergency.",
            NIDDK_DIABETES_SYMPTOMS,
            [
                "Document the time, symptoms, food eaten, and insulin given before the reading.",
                "Report critical values immediately and document the callback.",
                "Vomiting, abdominal pain, trouble breathing, or fainting means urgent care or 911.",
            ],
        ),
        _b(
            "Tests used to detect high and low blood glucose",
            "High glucose is detected with an A1C, a fasting plasma glucose, a 2-hour oral glucose tolerance test, or "
            "a random "
            "plasma glucose of 200 mg/dL or higher with classic symptoms. Low glucose is detected with a blood glucose "
            "reading, "
            "usually a fingerstick on a meter or a continuous glucose monitor. A low reading is confirmed with a "
            "laboratory "
            "glucose when the result is unclear or the patient is symptomatic. Point-of-care meters need quality "
            "control "
            "with each new lot and whenever a result is unexpected.",
            CDC_DIABETES_TESTING,
            [
                "A1C 6.5% or higher, fasting glucose 126 mg/dL or higher, or 2-hour OGTT 200 mg/dL or higher, indicate "
                "diabetes.",
                "Hypoglycemia is a glucose reading below 70 mg/dL with symptoms.",
                "Run liquid controls with each new lot of strips and whenever a result is unexpected.",
            ],
        ),
        _b(
            "When hypoglycemia symptoms occur",
            "Symptoms of low blood glucose appear when glucose falls below the patient's low threshold, usually under "
            "70 mg/dL. "
            "They are most likely when insulin or a sulfonylurea is taken without enough food, when a meal is skipped "
            "or "
            "delayed, or after extra physical activity. Low glucose can also occur during sleep, with crying out, "
            "nightmares, "
            "sweating that soaks the sheets, or waking confused and tired.",
            NIDDK_LOW_BLOOD_GLUCOSE,
            [
                "Mild to moderate: shakiness, hunger, tiredness, dizziness, confusion, irritability, racing heartbeat, "
                "headache.",
                "Very low: loss of consciousness or seizure.",
                "Trouble seeing or speaking clearly is also listed as a symptom of low glucose.",
            ],
        ),
        _b(
            "When hyperglycemia symptoms occur",
            "Symptoms of high blood glucose depend on the type. Type 1 symptoms usually develop quickly, over a few "
            "days or "
            "weeks, often with unexplained weight loss. Type 2 symptoms can develop slowly over several years, and "
            "many people "
            "have no symptoms or only mild ones. Symptoms appear once glucose stays high enough to exceed the body's "
            "ability to "
            "handle it, and illness, stress, infection, or missed medication can push it higher.",
            NIDDK_DIABETES_SYMPTOMS,
            [
                "Common symptoms: increased urination, thirst, hunger even after eating, blurred vision, fatigue.",
                "Also listed: sores that do not heal and frequent infections.",
                "Infection, stress, and missed medication commonly trigger high glucose.",
            ],
        ),
        # ------------------------------------------------------------------
        # Pathophysiology
        # ------------------------------------------------------------------
        _b(
            "What is an insulin autoantibody",
            "Autoantibodies are proteins made by the immune system that attack healthy tissue by mistake. In type 1 "
            "diabetes "
            "the immune system makes autoantibodies against the insulin-producing cells, and certain autoantibodies in "
            "the "
            "blood can indicate type 1 diabetes. An insulin autoantibody is an antibody directed at insulin itself; it "
            "is one "
            "of the islet autoantibodies that screening programs measure. The NIDDK page does not name specific "
            "autoantibodies, "
            "so confirm the terminology against the program's materials.",
            NIDDK_TYPE_1,
            [
                "Autoantibodies are immune proteins that attack the body's own cells.",
                "Testing is offered to people with symptoms and to some relatives of people with type 1 diabetes.",
                "Autoantibody testing can find type 1 diabetes before symptoms appear.",
            ],
        ),
        _b(
            "Pancreatic beta cell function",
            "Beta cells are the insulin-producing cells in the pancreatic islets, clusters of cells within the "
            "pancreas. They "
            "sense blood glucose and release insulin, which signals muscle, fat, and liver cells to take up glucose "
            "from the "
            "blood. In type 1 diabetes the immune system destroys these cells, so insulin production stops. In type 2 "
            "diabetes "
            "the beta cells cannot keep up with the demand for insulin over time.",
            NIDDK_TYPE_1,
            [
                "Function: sense glucose and secrete insulin.",
                "Type 1: immune destruction of beta cells.",
                "Type 2: progressive decline in insulin output.",
            ],
        ),
        _b(
            "What is hepatic glucose overproduction",
            "The liver stores glucose as glycogen and makes new glucose when the body needs it, especially between "
            "meals and "
            "overnight. Normally insulin tells the liver to stop releasing glucose. In type 2 diabetes the liver keeps "
            "releasing "
            "glucose even when blood glucose is already high. This hepatic glucose overproduction drives fasting "
            "hyperglycemia. "
            "Metformin lowers liver glucose output and is first-line for most patients with type 2 diabetes.",
            ADA_STANDARDS,
            [
                "Insulin normally suppresses hepatic glucose output.",
                "Metformin reduces hepatic glucose production.",
                "Liver output is a major reason fasting glucose is high in type 2 diabetes.",
            ],
        ),
        _b(
            "How sugar affects the body",
            "Glucose is the body's main fuel, and insulin moves it into cells. When insulin is missing or does not "
            "work well, "
            "glucose stays in the blood and cells are short of fuel. Chronically high glucose damages small blood "
            "vessels in the "
            "eyes, kidneys, and nerves and speeds up damage to large vessels in the heart, brain, and legs. Those "
            "long-term "
            "changes are the complications of diabetes.",
            CDC_DIABETES,
            [
                "Short term: thirst and frequent urination as the body tries to clear excess glucose.",
                "Long term: damage to eyes, kidneys, nerves, and blood vessels.",
            ],
        ),
        _b(
            "How sugar affects the brain",
            "The brain depends on a steady supply of glucose and stores very little, so it is sensitive to low blood "
            "glucose. "
            "Hypoglycemia first causes shakiness, hunger, and irritability, then confusion, trouble speaking, poor "
            "coordination, "
            "seizure, or loss of consciousness. Repeated or severe lows are dangerous. Very high glucose causes "
            "fatigue, one "
            "of the symptoms NIDDK lists for diabetes.",
            NIDDK_LOW_BLOOD_GLUCOSE,
            [
                "Low glucose can cause confusion, seizure, and loss of consciousness.",
                "Severe lows need glucagon and a call to 911.",
            ],
        ),
        _b(
            "What is the disease for sugar in the body",
            "The disease in which blood glucose stays too high is diabetes mellitus. Diabetes is a group of metabolic "
            "diseases, "
            "including type 1, type 2, and gestational diabetes, in which glucose stays elevated because insulin is "
            "absent, "
            "insufficient, or ineffective. The type depends on the cause.",
            CDC_DIABETES,
            [
                "Diabetes mellitus is the name of the disease of high blood sugar.",
                "Type 1: autoimmune loss of insulin. Type 2: insulin resistance with declining secretion. Gestational: "
                "pregnancy-related.",
            ],
        ),
        _b(
            "What is the disease for insulin in the heart and blood",
            "The notes ask about the disease of insulin in the heart and blood. Two answers apply. Insulin resistance "
            "is a "
            "blood-level problem in which the body does not respond well to insulin and needs more of it to move "
            "glucose; "
            "blood insulin levels are often high. Cardiovascular disease is the heart and blood-vessel damage that "
            "diabetes "
            "causes, including heart attack and stroke. Confirm which answer your instructor expects.",
            CDC_INSULIN_RESISTANCE,
            [
                "Insulin resistance: the body does not respond well to insulin.",
                "Cardiovascular disease: heart attack and stroke risk raised by diabetes.",
            ],
        ),
        _b(
            "The organ that produces insulin",
            "The organ that produces insulin is the pancreas. Insulin is made by beta cells in the islets of "
            "Langerhans, "
            "clusters of cells within the pancreas, and is released into the blood. Damage to these islet cells is "
            "what "
            "causes type 1 diabetes.",
            NIDDK_TYPE_1,
            [
                "Organ: pancreas.",
                "Cells: beta cells within the pancreatic islets.",
            ],
        ),
        # ------------------------------------------------------------------
        # Insulin products and cure
        # ------------------------------------------------------------------
        _b(
            "Review insulin formulas and problems",
            "Insulin products differ in onset, peak, and duration. Rapid-acting analogs begin working in about 15 "
            "minutes and "
            "peak at 1 to 2 hours; regular insulin peaks around 2 to 3 hours; NPH is intermediate and cloudy until "
            "mixed; "
            "glargine and detemir provide long-acting basal coverage. Common problems include hypoglycemia from too "
            "much "
            "insulin for the food eaten, hardening of tissue from repeated injection in one spot, and loss of potency "
            "from heat, "
            "freezing, or an expired vial.",
            ADA_STANDARDS,
            [
                "Never mix insulin types in the same syringe without a specific order.",
                "Insulin is high-alert: two-person verification is commonly required by policy.",
                "Rotate injection sites; repeated injection in one spot hardens the tissue.",
            ],
        ),
        _b(
            "Is type 1 diabetes curable",
            "There is no cure for type 1 diabetes. NIDDK notes that islet and pancreas transplants can help but do not "
            "cure it. "
            "Teplizumab can delay symptoms and the need for insulin in people with two or more autoantibodies and "
            "rising blood "
            "glucose, but it is not a cure. Insulin and glucose monitoring are required for life.",
            NIDDK_TYPE_1,
            [
                "Answer on exams: type 1 diabetes is not curable; insulin is lifelong.",
                "Transplants help but do not cure type 1 diabetes.",
            ],
        ),
        _b(
            "Is type 2 diabetes curable",
            "NIDDK does not describe a cure for type 2 diabetes. It recommends losing 5 to 7 percent of body weight to "
            "prevent "
            "or delay diabetes, and healthy eating and physical activity are the core of prevention. Some people with "
            "type 2 "
            "diabetes, after weight-loss surgery, may no longer need diabetes medicines. For exam purposes, type 2 is "
            "managed and "
            "can be prevented or delayed; the NIDDK page does not describe a cure.",
            NIDDK_TYPE_2,
            [
                "Prevention target: 5–7% weight loss, according to NIDDK.",
                "Lifestyle change can prevent or delay type 2 diabetes, according to CDC.",
            ],
        ),
        _b(
            "Weight-loss surgery and type 2 diabetes",
            "Some people with type 2 diabetes may no longer need diabetes medicines after weight-loss surgery, "
            "according to NIDDK. "
            "NIDDK also notes that researchers are still studying weight-loss surgery for type 1 diabetes in people "
            "with obesity. "
            "Surgery is a medical decision made with a surgeon and the patient's care team, not a standard step for "
            "every patient.",
            NIDDK_INSULIN_TREATMENTS,
            [
                "Some people with type 2 no longer need diabetes medicines after surgery.",
                "Type 1 with obesity is still under study.",
            ],
        ),
        # ------------------------------------------------------------------
        # Who is affected
        # ------------------------------------------------------------------
        _b(
            "Race and ethnicity most affected by diabetes",
            "Diabetes burden is highest among American Indian and Alaska Native, Black, and Pacific Islander adults. "
            "CDC's "
            "analysis of Behavioral Risk Factor Surveillance System data from 2013 to 2021 found an overall prevalence "
            "of 10.9 "
            "percent, rising to about 16 to 17 percent among American Indian and Alaska Native, Black, and Pacific "
            "Islander "
            "adults, compared with 9.1 percent among White adults. Asian subgroups vary widely.",
            CDC_MMWR_CARDIOMETABOLIC,
            [
                "American Indian and Alaska Native, Black, and Pacific Islander adults: about 16–17%.",
                "White adults: 9.1%.",
                "Asian subgroups range from 6.3% (Vietnamese adults) to 15.2% (Filipino adults).",
            ],
        ),
        _b(
            "Sex most affected by diabetes",
            "In NHANES 2013 to 2016, men had a higher prevalence of total diabetes, counting diagnosed and undiagnosed "
            "cases, "
            "than women among adults age 20 and older. The sex difference varies by race and ethnicity and by survey "
            "year, so "
            "the answer depends on the data set named in the question.",
            CDC_NCHS_DB319,
            [
                "Total diabetes: men 15.9%, women 12.2% (NHANES 2013–2016).",
                "Sex-specific rates vary by race and ethnicity.",
            ],
        ),
        # ------------------------------------------------------------------
        # Insulin syringes, units, and injection
        # ------------------------------------------------------------------
        _b(
            "Insulin syringe sizes",
            "Insulin syringes come in three common volumes: 0.3 mL, which holds 30 units; 0.5 mL, which holds 50 "
            "units; and "
            "1 mL, which holds 100 units. U-100 is the standard U.S. insulin strength, and the scale on a U-100 "
            "syringe is "
            "marked in units and labeled for U-100 insulin. Markings differ by manufacturer, so read the scale on the "
            "package "
            "before drawing a dose.",
            FDA_INSULIN_SYRINGE_510K,
            [
                "0.3 mL = 30 units; 0.5 mL = 50 units; 1 mL = 100 units.",
                "Use only syringes labeled for U-100 insulin with standard U-100 insulin.",
            ],
        ),
        _b(
            "Insulin syringe increments",
            "Increments differ by syringe. A BD 510(k) clearance describes a 0.3 mL syringe with 1-unit marks, some "
            "with "
            "half-unit marks, and a 1 mL syringe with 2-unit marks. Other manufacturers' syringes use different "
            "spacing. Never "
            "estimate between marks; if the dose falls between two marks on the syringe in hand, clarify the dose with "
            "the "
            "clinician before drawing it.",
            FDA_INSULIN_SYRINGE_510K,
            [
                "0.3 mL on this clearance: 1-unit marks (some with half-unit marks).",
                "1 mL on this clearance: 2-unit marks.",
                "Confirm the scale on the box you are using before measuring.",
            ],
        ),
        _b(
            "Insulin units to mL conversion",
            "For U-100 insulin, 1 unit equals 0.01 mL, so milliliters equal units divided by 100, and units equal "
            "milliliters "
            "multiplied by 100. The common doses convert as follows: 10 units is 0.10 mL, 25 units is 0.25 mL, 50 "
            "units is 0.50 "
            "mL, and 100 units is 1.00 mL. Confirm the vial's strength on its label before any conversion.",
            FDA_HUMULIN_R_LABEL,
            [
                "mL = units ÷ 100.   units = mL × 100.",
                "10 units = 0.10 mL; 25 units = 0.25 mL; 50 units = 0.50 mL; 100 units = 1.00 mL.",
            ],
        ),
        _b(
            "Choosing the syringe by dosage size",
            "Choose the smallest syringe that holds the full dose. A smaller syringe has finer marks and fewer "
            "measuring errors. "
            "A 0.3 mL syringe fits doses up to 30 units, a 0.5 mL syringe fits up to 50 units, and a 1 mL syringe fits "
            "up to "
            "100 units. A dose that needs two syringes should be clarified with the clinician.",
            FDA_INSULIN_SYRINGE_510K,
            [
                "18 units: use a 0.3 mL syringe.",
                "42 units: use a 0.5 mL syringe.",
                "80 units: use a 1 mL syringe.",
            ],
        ),
        _b(
            "Five injection sites for insulin",
            "NIDDK lists four common injection sites: the abdomen, where insulin acts fastest; the thigh; the "
            "buttocks; and the "
            "upper arm, which may act more slowly. The fifth site taught in many programs is the hip; confirm the five "
            "sites "
            "your program uses. Rotate sites within each area, because repeated injection in one spot hardens the "
            "tissue.",
            NIDDK_INSULIN_TREATMENTS,
            [
                "Abdomen: fastest absorption, according to NIDDK.",
                "Thigh, buttocks, and upper arm: may take longer to act.",
                "Rotate sites; repeated injection in one spot hardens the tissue.",
            ],
        ),
        # ------------------------------------------------------------------
        # Symptoms in patients
        # ------------------------------------------------------------------
        _b(
            "Polyuria and polydipsia",
            "Polyuria means excessive urination and polydipsia means excessive thirst. Both are classic early signs of "
            "high blood "
            "glucose. When glucose rises above what the kidneys can reabsorb, it spills into the urine and pulls water "
            "with it, "
            "so the patient urinates more and becomes thirsty.",
            NIDDK_DIABETES_SYMPTOMS,
            [
                "Polyuria: frequent urination, including at night.",
                "Polydipsia: thirst that does not go away after drinking.",
                "Classic signs with them: hunger even after eating, and weight loss.",
            ],
        ),
        _b(
            "Symptoms of diabetes in children",
            "In children, the common early symptoms of diabetes are increased thirst, frequent urination, bedwetting "
            "in a child "
            "who was previously dry at night, unexplained weight loss, extreme hunger, and fatigue. Type 1 usually "
            "develops "
            "quickly, over days or weeks. A child with these symptoms needs same-day evaluation.",
            NIDDK_DIABETES_SYMPTOMS,
            [
                "Type 1 in children: sudden onset, often with weight loss.",
                "Any child with thirst, frequent urination, or weight loss needs same-day evaluation.",
            ],
        ),
        _b(
            "Fruity-smelling breath and ketones",
            "Fruity-smelling breath is a sign of ketones, which build up when the body lacks enough insulin and burns "
            "fat for "
            "energy. Ketones with high glucose indicate diabetic ketoacidosis (DKA), a medical emergency. So a patient "
            "with "
            "fruity breath has a build-up of ketones and needs urgent evaluation. DKA usually affects type 1 diabetes "
            "but can "
            "occur in type 2 when the body does not produce enough insulin.",
            NIDDK_DIABETES_SYMPTOMS,
            [
                "Answer: a build-up of ketones.",
                "Other DKA signs: very tired, trouble breathing, fainting from dehydration, abdominal pain, nausea, "
                "vomiting.",
            ],
        ),
        _b(
            "Erectile dysfunction (ED) and men with diabetes",
            "Erectile dysfunction is the inability to get or keep an erection firm enough for sex. High blood glucose "
            "damages the "
            "blood vessels and nerves that control erection, so men with diabetes develop ED more often, and often "
            "roughly a "
            "decade or more earlier than men without diabetes. Keeping glucose in the target range, and controlling "
            "blood "
            "pressure, cholesterol, weight, and smoking, reduces the risk.",
            NIDDK_SEXUAL_BLADDER,
            [
                "ED can start about a decade or more earlier in men with diabetes, according to NIDDK.",
                "Other risk factors: high blood pressure, high cholesterol, obesity, inactivity, smoking, heavy "
                "drinking.",
                "ED can signal vascular or nerve damage, so refer the patient to the clinician.",
            ],
        ),
        _b(
            "Blurred vision and the eye nerve affected by diabetes",
            "When blood sugar is high, vision can become blurred, and that blur is usually temporary once glucose "
            "returns to "
            "target. The tissue damaged by diabetes in the eye is the retina, the light-sensing layer at the back of "
            "the eye, "
            "and the condition is diabetic retinopathy. Retinopathy causes blindness when leaking vessels swell the "
            "macula and "
            "when fragile new vessels bleed into the eye.",
            CDC_VISION_LOSS,
            [
                "Blurred vision from high glucose is usually temporary.",
                "The affected tissue is the retina; the optic nerve is involved in other eye diseases such as "
                "glaucoma.",
                "Macular edema from leaking vessels is the most common cause of blindness in retinopathy.",
            ],
        ),
        _b(
            "How diabetes affects the skin",
            "Diabetes affects the skin mainly by slowing healing and making infection more likely. NIDDK lists sores "
            "that do not "
            "heal and frequent infections among the symptoms of diabetes. High glucose impairs circulation to the "
            "skin, which "
            "slows wound repair. Feet are the most common site of serious skin injury, so daily skin checks are part "
            "of care.",
            NIDDK_DIABETES_SYMPTOMS,
            [
                "Sores that do not heal and frequent infections are listed by NIDDK.",
                "Check skin daily, especially the feet.",
            ],
        ),
        # ------------------------------------------------------------------
        # Insulin calculation and conversion formulas
        # ------------------------------------------------------------------
        _b(
            "Insulin math: total dose and syringe volume",
            "Calculation formulas are for checking an order, not for setting a dose. The total insulin dose is the "
            "meal dose plus "
            "the correction dose, both set by the clinician. Convert the total to volume with mL = units ÷ 100. "
            "Example: 4 units "
            "for the meal plus 2 units for correction is 6 units, or 0.06 mL, which is drawn in a 0.3 mL syringe. "
            "Medical "
            "assistants verify the arithmetic against the order with a second person; they do not set the dose.",
            ADA_STANDARDS,
            [
                "Total units = meal units + correction units.",
                "mL = total units ÷ 100.",
                "Verify the order and the arithmetic with a second person before administration.",
            ],
        ),
        _b(
            "Insulin math: meal dose from the carbohydrate ratio",
            "Meal insulin is often calculated with an insulin-to-carbohydrate ratio: units = grams of carbohydrate ÷ "
            "grams covered "
            "per unit. A ratio of 1 unit per 15 grams with a 60-gram meal gives 60 ÷ 15 = 4 units. The ratio is set by "
            "the "
            "prescriber for each patient and is never chosen by the medical assistant.",
            ADA_STANDARDS,
            [
                "Example: 45 g ÷ 15 g per unit = 3 units.",
                "Example: 90 g at 1 unit per 10 g = 9 units.",
                "The ratio must come from the order, not from a chart or memory.",
            ],
        ),
        _b(
            "Insulin math: correction dose for high glucose",
            "A correction dose lowers a high reading toward the target: units = (current glucose − target glucose) ÷ "
            "correction "
            "factor. A reading of 250 mg/dL with a target of 150 mg/dL and a factor of 1 unit per 50 mg/dL gives (250 "
            "− 150) ÷ 50 "
            "= 2 units. The target and factor come from the prescriber, and the answer is rounded only as the order "
            "specifies.",
            ADA_STANDARDS,
            [
                "Example: 310 mg/dL, target 150, factor 1 unit per 40 mg/dL: (310 − 150) ÷ 40 = 4 units.",
                "Do not round a dose unless the order says how.",
            ],
        ),
        _b(
            "Glucose unit conversion: mg/dL and mmol/L",
            "Some labs report glucose in mmol/L, while U.S. clinics usually use mg/dL. Divide mg/dL by 18 to get "
            "mmol/L, or "
            "multiply mmol/L by 18 to get mg/dL. Example: 126 mg/dL ÷ 18 = 7.0 mmol/L, and 70 mg/dL ÷ 18 = 3.9 mmol/L. "
            "The "
            "factor of 18 is the standard laboratory conversion, not a figure taken from the cited page.",
            ADA_DIAGNOSIS,
            [
                "mmol/L = mg/dL ÷ 18.   mg/dL = mmol/L × 18.",
                "Example: 126 mg/dL = 7.0 mmol/L; 70 mg/dL = 3.9 mmol/L.",
            ],
        ),
        _b(
            "A1C to estimated average glucose formula",
            "Estimated average glucose (eAG) can be calculated from A1C with eAG (mg/dL) = 28.7 × A1C − 46.7. Example: "
            "an A1C "
            "of 7 percent gives 28.7 × 7 − 46.7 = 154 mg/dL, which matches CDC's table value. An A1C of 8 percent "
            "gives 183 mg/dL. "
            "CDC's table is the reference for these values, and the estimate can miss spikes and lows.",
            CDC_A1C,
            [
                "eAG (mg/dL) = 28.7 × A1C − 46.7.",
                "A1C 7%: 154 mg/dL.   A1C 8%: 183 mg/dL.",
            ],
        ),
        _b(
            "Practice questions: insulin math",
            "Work each problem on paper before checking the answers in the next section. Use the formulas above, and "
            "show the "
            "units and the mL result for every dose.",
            FDA_HUMULIN_R_LABEL,
            [
                "1. How many mL is 30 units of U-100 insulin?",
                "2. How many units are in 0.15 mL of U-100 insulin?",
                "3. Which syringe holds a 37-unit dose?",
                "4. Convert 10, 25, 50, and 100 units to mL.",
                "5. A meal of 45 g carbohydrate at 1 unit per 15 g, plus 2 units correction: total units and mL?",
                "6. Glucose 310 mg/dL, target 150, factor 1 unit per 40 mg/dL: correction units?",
                "7. A1C of 8 percent: estimated average glucose?",
                "8. Convert 70 mg/dL to mmol/L.",
                "9. A conscious patient has glucose 62 mg/dL. What is the first treatment?",
                "10. Why is a 0.3 mL syringe more precise than a 1 mL syringe for a 12-unit dose?",
            ],
        ),
        _b(
            "Answers: insulin math",
            "Check each answer against your working. The formulas and examples are in the sections above.",
            FDA_HUMULIN_R_LABEL,
            [
                "1. 0.30 mL (30 ÷ 100).",
                "2. 15 units (0.15 × 100).",
                "3. 0.5 mL, which holds 50 units. The 0.3 mL syringe holds only 30 units.",
                "4. 10 units = 0.10 mL; 25 units = 0.25 mL; 50 units = 0.50 mL; 100 units = 1.00 mL.",
                "5. Meal: 45 ÷ 15 = 3 units. Total: 3 + 2 = 5 units, which is 0.05 mL.",
                "6. (310 − 150) ÷ 40 = 4 units.",
                "7. 28.7 × 8 − 46.7 = 182.9, about 183 mg/dL.",
                "8. 70 ÷ 18 = 3.9 mmol/L.",
                "9. 15 to 20 g of fast carbohydrate, such as four glucose tablets; recheck in 15 minutes and repeat if "
                "still low.",
                "10. On the BD clearance, the 0.3 mL syringe has 1-unit marks and the 1 mL syringe has 2-unit marks, "
                "so 12 units is easier to measure exactly.",
            ],
        ),
        # ------------------------------------------------------------------
        # Scope
        # ------------------------------------------------------------------
        _b(
            "Medical assistant scope and documentation",
            "Perform point-of-care testing, vital signs, patient teaching, and injections only within state law, "
            "licensure, and "
            "delegation. Document glucose values with the time, the symptoms present, the treatment given, and the "
            "patient's "
            "response. Do not adjust insulin doses without an order or explicit delegation, and route abnormal results "
            "to the "
            "clinician the same day.",
            NHA_CCMA,
            [
                "Never independently change an insulin dose; that requires a new order.",
                "Document the patient's own words about symptoms rather than interpreting them.",
                "Know where the hypoglycemia protocol and glucagon are kept.",
            ],
        ),
    ],
    # ------------------------------------------------------------------
    # EKG technician
    # ------------------------------------------------------------------
    "ekg-leads": [
        _b(
            "The 12-lead ECG",
            "A standard 12-lead ECG records 12 electrical views of the heart: three "
            "limb leads (I, II, III), three augmented limb leads (aVR, aVL, aVF), "
            "and six precordial (chest) leads (V1–V6). Each lead looks at the "
            "heart from a different angle. Limb leads look at the vertical plane "
            "and precordial leads at the horizontal plane, and every lead also "
            "sees two of the four chambers.",
            ML_ECG,
            [
                "Lead I: left arm (+), right arm (−). Lead II: left leg (+), right arm (−). Lead III: left leg (+), "
                "left arm (−).",
                "aVR, aVL, aVF are augmented versions of leads I, II, and III at half voltage, so they are not true "
                "leads I, II, III.",
                "An ECG records electrical activity, not mechanical contraction — it does not measure pumping "
                "strength.",
            ],
        ),
        _b(
            "Limb lead placement",
            "Place the four limb electrodes on the right arm, left arm, right leg, "
            "and left leg, at the fleshy part of the limb away from joints and "
            "arterial sites. Electrodes can go on the upper arms and thighs if the "
            "patient cannot expose a limb. Correct limb placement is what makes "
            "lead II usable as a rhythm strip, and reversing right and left arm "
            "electrodes produces a false dextrocardia pattern.",
            ML_ECG,
            [
                "Right arm and right leg electrodes are both ground; they can be placed anywhere on those limbs.",
                "Never place an electrode over a pacemaker generator or over a fresh IV.",
                "If right and left arm are reversed, lead I is inverted and lead III becomes the mirror of lead II.",
            ],
        ),
        _b(
            "Precordial (chest) lead placement",
            "V1 goes to the 4th intercostal space at the right sternal border; V2 "
            "in the 4th intercostal space at the left sternal border; V3 midway "
            "between V2 and V4; V4 at the midclavicular line in the 5th "
            "intercostal space; V5 at the anterior axillary line in the same "
            "horizontal level as V4; V6 at the midaxillary line in the same level. "
            "Palpate landmarks, not visual estimation.",
            ML_ECG,
            [
                "V4 and V5 are placed in the 5th intercostal space at the midclavicular and anterior axillary lines.",
                "Mistranslated chest leads are a common cause of a falsely abnormal study.",
                "Mark the sites so repeat tracings in the same session are comparable.",
            ],
        ),
        _b(
            "Standardization and the rhythm strip",
            "The standard ECG is recorded at 25 mm per second and 10 mm per "
            "millivolt. At that speed, one small square is 0.04 seconds and one "
            "large square is 0.20 seconds; 300 large squares fit into a 60-second "
            "strip. A rhythm strip — usually lead II — recorded for at least 10 "
            "seconds is what lets you count the rate and assess rhythm regularity.",
            AHA_ALGORITHMS,
            [
                "Always check the calibration mark and confirm the paper speed before measuring anything.",
                "At 25 mm/second one small square is 0.04 s, one large square is 0.20 s, and 300 large squares fill a "
                "60-second strip.",
                "If the machine runs at 50 mm/second, one small square is 0.02 s and one large square is 0.10 s — "
                "recalculate before measuring.",
                "Report a technical problem (limb reversal, artifact, baseline wander) separately from a clinical "
                "finding.",
            ],
        ),
        _b(
            "Patient preparation and safety",
            "Explain the procedure, confirm the patient is still, and position them "
            "supine with the arms at the sides. Remove jewelry from the limbs, "
            "ensure skin is clean and dry, and avoid placing electrodes over "
            "hair, wounds, or heavy scar tissue. Confirm the patient's identity "
            "before connecting the machine and check for a pacemaker or ICD, "
            "which must be documented.",
            ML_VITAL_SIGNS,
            [
                "Ask the patient to lie still and to breathe normally during the recording.",
                "Warm the room — shivering produces artifact.",
                "Confirm and document rhythm interpretation with the supervising clinician per policy.",
            ],
        ),
    ],
    "ekg-rhythm": [
        _b(
            "Reading a rhythm strip systematically",
            "Use a consistent method: rate, rhythm regularity, P waves, PR "
            "interval, QRS width and morphology, ST segment and T wave, then QTC. "
            "Calculate the rate by counting large boxes between R waves and "
            "dividing 300 by that number, or count QRS complexes in a 6-second "
            "strip and multiply by 10. Always work through the same sequence so "
            "nothing is missed.",
            ML_ARRHYTHMIAS,
            [
                "300 ÷ number of large boxes between R waves = approximate heart rate.",
                "6-second strip method: count QRS complexes, multiply by 10.",
                "R-R intervals that vary by more than three small boxes (0.12 s) are irregular.",
            ],
        ),
        _b(
            "Normal sinus rhythm",
            "Normal sinus rhythm has a rate of 60–100 beats per minute, is "
            "regular, and has one upright P wave before every QRS in leads II, III, "
            "and aVF with a constant PR interval. Sinus bradycardia is below 60 and "
            "sinus tachycardia is above 100 with the same morphology. Athletes and "
            "well-conditioned patients commonly have resting sinus bradycardia.",
            ML_ARRHYTHMIAS,
            [
                "P wave upright in II, III, aVF; inverted in aVR.",
                "Constant PR interval of 0.12–0.20 seconds.",
                "Rate changes with breathing are respiratory (phasic) sinus arrhythmia and are benign, especially in "
                "young people.",
            ],
        ),
        _b(
            "Atrial fibrillation and flutter",
            "Atrial fibrillation has no discrete P waves; the baseline shows "
            "irregular fibrillatory waves and the ventricular response is "
            "irregularly irregular. Atrial flutter shows sawtooth flutter waves "
            "at about 250–350 per minute, usually with a regular or variably "
            "conducted ventricular rate. Both are important because of the risk of "
            "embolism, and the irregular pulse is a classic exam finding.",
            ML_AFIB,
            [
                "Atrial fibrillation: irregularly irregular rhythm with no P waves.",
                "Atrial flutter: sawtooth baseline (F waves), regular R-R when conduction is fixed.",
                "Check the pulse and compare it with the apical rate — a pulse deficit suggests AF with a very fast "
                "ventricular response.",
            ],
        ),
        _b(
            "Supraventricular and ventricular tachycardias",
            "Supraventricular tachycardia is a regular, narrow-complex tachycardia "
            "that starts and stops abruptly, typically above 150 beats per "
            "minute. Ventricular tachycardia is a wide-complex tachycardia with "
            "no preceding P wave and is treated as cardiac arrest until proven "
            "otherwise. Torsades de pointes is a polymorphic ventricular "
            "tachycardia with twisting QRS complexes.",
            ML_ARRHYTHMIAS,
            [
                "Narrow complex (QRS < 0.12 s) suggests a supraventricular origin.",
                "Wide complex tachycardia: assume ventricular tachycardia.",
                "Assess for pulse — a pulseless wide-complex tachycardia is defibrillated immediately.",
            ],
        ),
        _b(
            "Dangerous rhythms and shockable rhythms",
            "Ventricular fibrillation is chaotic with no identifiable QRS complexes "
            "and is always pulseless — it is shockable. Pulseless electrical "
            "activity and asystole are non-shockable rhythms, and the priority is "
            "high-quality CPR with epinephrine rather than defibrillation. "
            "Confirming pulselessness takes no more than ten seconds.",
            AHA_ADULT_BLS,
            [
                "Shockable: ventricular fibrillation and pulseless ventricular tachycardia.",
                "Non-shockable: asystole and pulseless electrical activity.",
                "For every shockable rhythm, defibrillation is the definitive treatment and CPR is the bridge.",
            ],
        ),
        _b(
            "Blocks, ectopy, and escape rhythms",
            "A prolonged PR interval (greater than 0.20 seconds) with every P wave "
            "conducted is first-degree AV block. A dropped QRS with progressively "
            "lengthening PR intervals is second-degree AV block (Mobitz I); fixed "
            "PR with sudden dropped beats is Mobitz II. A wide QRS without P waves "
            "at a slow, regular rate is a ventricular escape rhythm. Premature "
            "atrial and ventricular complexes are common and usually benign but "
            "must be distinguished from the dangerous rhythms above.",
            ML_ARRHYTHMIAS,
            [
                "First-degree AV block: PR > 0.20 s, every P conducted.",
                "Mobitz II and complete heart block require urgent evaluation — they can progress to asystole.",
                "Premature ventricular complexes that occur in runs of three or more, or with a wide, bizarre "
                "morphology, need prompt review.",
            ],
        ),
    ],
    "ekg-intervals": [
        _b(
            "The PR interval",
            "The PR interval measures the time from the onset of atrial "
            "depolarization to the onset of ventricular depolarization — the delay "
            "at the AV node. Normal is 0.12 to 0.20 seconds (3 to 5 small boxes). "
            "A prolonged PR indicates delayed AV conduction; a short PR suggests "
            "an accessory pathway, as in Wolff-Parkinson-White syndrome.",
            ML_ECG,
            [
                "Normal PR: 120–200 milliseconds.",
                "Measure from the start of the P wave to the start of the QRS.",
                "PR varies with heart rate — it shortens as the rate increases.",
            ],
        ),
        _b(
            "The QRS complex",
            "The QRS complex represents ventricular depolarization and therefore "
            "ventricular contraction. Normal duration is less than 0.12 seconds (3 "
            "small boxes). A wide QRS indicates ventricular origin, bundle branch "
            "block, or a pre-excitation pattern, and changes the interpretation of "
            "the whole tracing.",
            ML_ECG,
            [
                "Normal QRS: < 0.12 s (120 ms).",
                "Prolonged QRS ≥ 0.12 s means wide complex — think ventricular rhythm, bundle branch block, or "
                "pre-excitation.",
                "A pacemaker rhythm produces wide QRS complexes with pacing spikes.",
            ],
        ),
        _b(
            "The QT interval and QTc",
            "The QT interval runs from the start of the QRS to the end of the T "
            "wave and represents total ventricular depolarization and "
            "repolarization. Because QT shortens as the heart rate rises, it is "
            "corrected to the heart rate using the QTc (Bazett formula). A "
            "prolonged QTc predisposes to torsades de pointes and is caused by a "
            "long list of medications, electrolyte abnormalities, and congenital "
            "conditions.",
            ML_ECG,
            [
                "QT is measured from the start of QRS to the end of the T wave; use the longest lead, usually II or "
                "V5.",
                "QTc above about 450–500 ms is prolonged and warrants review of medications and electrolytes.",
                "Always check potassium and magnesium when QTc is prolonged.",
            ],
        ),
        _b(
            "Axis determination",
            "Electrical axis describes the mean direction of ventricular "
            "depolarization. Lead I and aVF are used as the primary axes: a "
            "positive QRS in both gives a normal axis (roughly −30° to +90°), "
            "positive in I with negative in aVF gives left axis deviation, and "
            "negative in both gives right axis deviation. Axis shifts occur with "
            "infarction, ventricular hypertrophy, and conduction blocks.",
            ML_ECG,
            [
                "Normal axis: −30° to +90°.",
                "Left axis deviation (LAD): −30° to −90°. Right axis deviation (RAD): +90° to +180°.",
                "Axis deviation is a clue, not a diagnosis — consider infarct, hypertrophy, and block together.",
            ],
        ),
        _b(
            "ST segment and T wave",
            "The ST segment is the interval between ventricular depolarization and "
            "repolarization and should be flat and isoelectric. ST elevation or "
            "depression, and T wave inversion or peaking, are the ECG findings "
            "of ischemia, injury, electrolyte disturbance, and medication effect. "
            "ST elevation of 1 mm in two contiguous leads is a STEMI criterion in "
            "the appropriate context.",
            ML_CAD,
            [
                "ST elevation ≥ 1 mm in two contiguous leads is a STEMI criterion.",
                "T wave peaking suggests hyperkalemia; flattened T waves suggest ischemia or hypokalemia.",
                "Compare with the patient's baseline and repeat the tracing if the patient has symptoms.",
            ],
        ),
        _b(
            "Reporting the tracing",
            "A technically competent ECG report states rate, rhythm, axis, "
            "intervals, ST-T findings, and any technical limitations. Identify "
            "artifacts and technical problems explicitly so the clinician can "
            "interpret correctly, and communicate critical findings — ST "
            "elevation, a new wide-complex tachycardia, or asystole — immediately "
            "rather than waiting for the formal read.",
            AHRQ_TEAMSTEPPS,
            [
                "Report the technical quality separately from the clinical interpretation.",
                "Escalate critical results immediately and document who was notified and when.",
                "Never delay urgent care for the formal interpretation.",
            ],
        ),
    ],
    "ekg-artifacts": [
        _b(
            "Recognizing artifact",
            "Artifact is any recording problem that does not come from the heart. "
            "Artifact is by far the most common reason for a false-positive "
            "abnormality, so recognizing it is a core technician skill. The "
            "distinguishing feature is that artifact usually looks identical in "
            "every lead, because it is generated outside the heart and travels "
            "equally to all leads.",
            ML_ECG,
            [
                "True cardiac abnormalities generally differ from lead to lead; artifact tends to be identical across "
                "leads.",
                "Walking through the lead in which the abnormality appears is the fastest way to separate artifact "
                "from real ectopy.",
                "Re-record with the patient still and the electrodes reattached before escalating a finding.",
            ],
        ),
        _b(
            "AC interference (60-cycle artifact)",
            "Alternating current from electrical equipment produces a regular, "
            "fine, sawtooth-like baseline artifact at 60 cycles per second in the "
            "United States. It can make the baseline look like flutter waves or "
            "fine ventricular fibrillation. Common causes include poorly grounded "
            "equipment, loose electrodes, and nearby motors or lights.",
            ML_ECG,
            [
                "Regular, uniform fuzz at a fixed frequency across all leads.",
                "Check cables, electrodes, and grounding; move away from electrical equipment.",
                "Do not report atrial flutter from a tracing with 60-cycle artifact — confirm the baseline is stable.",
            ],
        ),
        _b(
            "Somatic tremor and muscle artifact",
            "Muscle tremor from shivering, Parkinson disease, or patient anxiety "
            "produces irregular, fuzzy baseline artifact that is often most "
            "prominent in leads with the most muscle. Warming the patient, "
            "supporting the limbs, and ensuring comfort reduces it.",
            ML_ECG,
            [
                "Artifact looks like fine, irregular oscillations and can mimic atrial fibrillation.",
                "Keep the patient warm and relaxed; support the arms at the sides.",
                "Parkinson tremor artifact is often regular and mimics flutter or VT.",
            ],
        ),
        _b(
            "Baseline wander and motion artifact",
            "Baseline wander results from movement, poor skin contact, or loose "
            "electrodes, and produces slow, rolling deflections of the baseline. "
            "Motion artifact from a patient or cable movement produces abrupt, "
            "large, irregular spikes. Both can make ST segments and T waves "
            "uninterpretable.",
            ML_ECG,
            [
                "Re-seat electrodes, clean the skin, and allow a few seconds of stabilization before recording.",
                "Secure cables so they are not pulled or brushed.",
                "Ask the patient to remain still for the 10-second recording.",
            ],
        ),
        _b(
            "Electrode problems and half-lead displacement",
            "A single displaced or reversed limb electrode distorts the tracing "
            "without any real cardiac change. Reversing the right and left arm "
            "electrodes inverts lead I and swaps leads II and III, which can mimic "
            "dextrocardia or lateral myocardial infarction. A loose electrode on "
            "one limb produces an abrupt shift in all leads that share that limb.",
            ML_ECG,
            [
                "Check limb electrode placement before accepting an abnormal tracing.",
                "Verify the machine's limb lead labels (RA, LA, RL, LL) match the physical electrodes.",
                "Document the technical correction that was made, not just the repeat study.",
            ],
        ),
        _b(
            "Troubleshooting checklist and escalation",
            "When a tracing looks wrong, work the sequence: patient still and "
            "warm, skin prepared and electrodes attached firmly, cables intact and "
            "not crossed, correct lead placement confirmed, calibration and paper "
            "speed verified, and equipment grounded. Re-record after correcting "
            "the problem. If the fault persists, escalate to biomedical "
            "engineering and document both the technical correction that was made "
            "and the repeat study, because the corrected tracing is the record.",
            NHA_CCMA,
            [
                "Patient factors (movement, shivering, anxiety) → comfort, warmth, and reassurance.",
                "Preparation factors (oils, lotions, hair) → clean the skin and reposition electrodes.",
                "Equipment factors (cables, ground, battery) → check, then escalate to biomedical engineering.",
                "Never report a rhythm from a tracing you know is technically invalid.",
            ],
        ),
    ],
    "ekg-cardiac-ap": [
        _b(
            "Cardiac anatomy and the conduction system",
            "The heart sits in the mediastinum with two-thirds of its mass left of "
            "the midline. The conduction system begins in the sinoatrial node in "
            "the right atrium, spreads through the atria to the atrioventricular "
            "node in the interatrial septum, passes through the bundle of His, "
            "divides into right and left bundle branches, and ends in the Purkinje "
            "fibers that activate the ventricles from the apex upward.",
            NHLBI_HEALTH,
            [
                "SA node: the pacemaker, normally 60–100 beats per minute.",
                "AV node: the only normal electrical connection between atria and ventricles; it delays the impulse.",
                "Bundle of His → bundle branches → Purkinje fibers.",
            ],
        ),
        _b(
            "The cardiac cycle and what the ECG records",
            "During atrial systole the atria contract and fill the ventricles; "
            "ventricular systole ejects blood into the arteries; diastole allows "
            "filling. The P wave corresponds to atrial depolarization, the QRS "
            "complex to ventricular depolarization, and the T wave to ventricular "
            "repolarization. Atrial repolarization is hidden inside the QRS.",
            ML_ECG,
            [
                "P wave = atrial depolarization; QRS = ventricular depolarization; T wave = ventricular "
                "repolarization.",
                "The ECG records electrical activity, not blood flow or contractility.",
                "An ECG can be normal in significant heart disease and abnormal without symptoms — interpret in "
                "context.",
            ],
        ),
        _b(
            "Coronary circulation",
            "The right coronary artery supplies the right atrium, right ventricle, "
            "and in most people the inferior wall of the left ventricle and the "
            "SA and AV nodes. The left coronary artery divides into the left "
            "anterior descending artery, which supplies the anterior wall and the "
            "bundle branches, and the circumflex artery, which supplies the "
            "lateral wall. Occlusion patterns determine which ECG territories "
            "change.",
            ML_CAD,
            [
                "LAD occlusion produces anterior ST elevation and can cause bundle branch block.",
                "RCA occlusion produces inferior ST elevation, sometimes with right-axis deviation.",
                "Knowing the territory helps localize ischemia seen on the tracing.",
            ],
        ),
        _b(
            "Valves and hemodynamics",
            "Four valves maintain one-way flow: the tricuspid and mitral valves "
            "separate atria from ventricles, and the pulmonary and aortic valves "
            "separate ventricles from the great arteries. Stenosis narrows the "
            "opening and increases upstream pressure; regurgitation allows "
            "backflow and increases downstream volume. Murmurs are heard best "
            "at specific auscultation points.",
            ML_HEART_ATTACK_TOPIC,
            [
                "Aortic: right 2nd intercostal space at the sternal border; aortic stenosis gives a "
                "crescendo-decrescendo systolic murmur radiating to the carotids.",
                "Mitral: left 5th intercostal space at the midclavicular line (apex); mitral regurgitation gives a "
                "holosystolic murmur.",
                "Pulmonic: left 2nd intercostal space; tricuspid: left lower sternal border.",
            ],
        ),
        _b(
            "Blood pressure and hemodynamic basics",
            "Blood pressure is the product of cardiac output and systemic "
            "vascular resistance. Systolic pressure reflects the force of "
            "ventricular ejection; diastolic pressure reflects the elastic recoil "
            "of the arteries during relaxation. Persistent elevation of either is "
            "hypertension, a leading cause of stroke, heart failure, and chronic "
            "kidney disease.",
            NHLBI_BP,
            [
                "Systolic = ventricles contracting; diastolic = heart at rest.",
                "Pulse pressure = systolic minus diastolic; widening can indicate aortic regurgitation.",
                "Orthostatic hypotension is a drop of 20 mm Hg systolic or 10 mm Hg diastolic within three minutes of "
                "standing.",
            ],
        ),
        _b(
            "Connecting the anatomy to the symptoms you will see",
            "Angina is chest discomfort from inadequate myocardial oxygen supply; "
            "a myocardial infarction is necrosis from sustained ischemia, and it "
            "produces a characteristic combination of symptoms and ECG changes. "
            "Heart failure produces congestion because the heart cannot pump "
            "effectively, and dyspnea, orthopnea, and edema are its cardinal "
            "presentations.",
            ML_HEART_ATTACK,
            [
                "Classic MI presentation: chest pressure, radiation to arm or jaw, diaphoresis, nausea, shortness of "
                "breath.",
                "Women, older adults, and patients with diabetes may present with dyspnea, fatigue, or epigastric "
                "discomfort instead of classic chest pain.",
                "Compare the current ECG with prior tracings when they are available.",
            ],
        ),
    ],
    "ekg-acls-basics": [
        _b(
            "High-quality CPR metrics",
            "Survival from cardiac arrest depends on the quality of CPR. The AHA "
            "metrics are a compression rate of 100–120 per minute, a depth of at "
            "least 5 cm (2 inches) and no more than 6 cm (2.4 inches) in adults, "
            "full chest recoil, and minimal interruptions — interruptions should be "
            "under 10 seconds.",
            AHA_HIGH_QUALITY,
            [
                "Rate 100–120/min; depth 5–6 cm in adults.",
                "Full recoil with no leaning; minimize interruptions to under 10 seconds.",
                "Switch compressors about every 2 minutes to avoid fatigue-related quality decline.",
            ],
        ),
        _b(
            "Defibrillation and the AED",
            "Early defibrillation is the single intervention that most improves "
            "survival from witnessed ventricular fibrillation. Every minute "
            "without defibrillation reduces survival by 7–10 percent. An AED "
            "analyzes the rhythm, and shocks only a shockable rhythm, so using it "
            "on a non-shockable rhythm is safe. Follow the device's prompts "
            "exactly.",
            AHA_AED_PROGRAM,
            [
                "Turn the AED on and follow the voice prompts.",
                "Bare, dry chest — remove clothing, medication patches, and jewelry; shave excessive hair only if "
                "directed.",
                "Do not touch the patient during analysis or shock delivery; say 'clear' and look to be sure no one is "
                "touching.",
            ],
        ),
        _b(
            "Team roles and communication",
            "Resuscitation is a team event. The AHA guidelines emphasize clear role "
            "assignment, closed-loop communication, and continuous reassessment. "
            "TeamSTEPPS provides a structured framework: introductions and "
            "assignments, clear handoffs, feedback, and a debriefing after the "
            "event.",
            AHRQ_TEAMSTEPPS,
            [
                "Assign roles explicitly: compressor, airway, defibrillator, medication, timing, and team leader.",
                "Use closed-loop communication: 'I am giving epinephrine 1 mg now' — 'epinephrine 1 mg given'.",
                "Debrief after every resuscitation: what happened, what worked, what to improve.",
            ],
        ),
        _b(
            "ACLS pharmacology and capnography",
            "In adult cardiac arrest, epinephrine 1 mg is given every 3–5 minutes "
            "for a non-shockable rhythm and after defibrillation fails in a "
            "shockable rhythm. Amiodarone and lidocaine are used for refractory "
            "shockable rhythms, and atropine is no longer recommended for "
            "asystole or PEA. End-tidal carbon dioxide confirms tube placement "
            "and shows effective CPR.",
            AHA_GUIDELINES,
            [
                "Epinephrine 1 mg IV/IO every 3–5 minutes as indicated.",
                "End-tidal CO2 confirms tube placement and reflects CPR quality; a low and falling value means poor "
                "perfusion.",
                "Do not delay defibrillation for any medication.",
            ],
        ),
        _b(
            "Post-cardiac arrest care",
            "After a return of spontaneous circulation, care continues with airway "
            "and hemodynamic support, temperature management, and evaluation at a "
            "cardiac center. The 2025 AHA guidelines emphasize maintaining "
            "temperature control for at least 36 hours in adults who remain "
            "unresponsive to verbal commands, and recommend critical care "
            "transfer.",
            AHA_EXECUTIVE_SUMMARY,
            [
                "A single chain of survival now applies to adults and children, with a separate newborn chain of care.",
                "Continue compressions and oxygenation immediately after ROSC; do not stop care.",
                "Document the arrest time, interventions, and ROSC time for the receiving team.",
            ],
        ),
        _b(
            "Recording and reporting the event",
            "Accurate documentation of a resuscitation is both a clinical and a "
            "quality requirement. Record the time of recognition, the time of "
            "each intervention, the number and energy of shocks, medications with "
            "times and doses, the return of spontaneous circulation, and the "
            "outcome at transfer.",
            AHA_TOP_THINGS,
            [
                "Note who was present and what role each person performed.",
                "Record the time of the first shock and the time of ROSC — these drive quality review.",
                "Document barriers to care and any deviations from protocol.",
            ],
        ),
    ],
    # ------------------------------------------------------------------
    # Phlebotomy
    # ------------------------------------------------------------------
    "phleb-order-draw": [
        _b(
            "Why order of draw matters",
            "The order of draw exists because of additive carryover. Blood drawn "
            "from a tube with an additive can contaminate the next tube, "
            "producing falsely abnormal results. CLSI specifies the sequence, and "
            "it is one of the most commonly tested and most frequently violated "
            "procedures in specimen collection.",
            CLSI_GP41,
            [
                "Blood cultures and sterile tubes first, then citrate, then serum, then heparin, then EDTA, then "
                "additives with glycolytic inhibitors.",
                "Never transfer blood between tubes or fill tubes from one another.",
                "When using a winged collection set, start with the discard tube to fill the tubing dead space.",
            ],
        ),
        _b(
            "The order of draw, step by step",
            "Draw blood cultures (or the discard tube) first. Next, light blue "
            "sodium citrate tubes for coagulation studies. Then red or gold tubes "
            "for serum tests. Then green heparin tubes. Then lavender or pink EDTA "
            "tubes. Finally, gray tubes with sodium fluoride or potassium oxalate "
            "for glucose testing, which may be drawn last.",
            CLSI_GP41_SAMPLE,
            [
                "1. Blood culture / sterile (e.g., discard tube).",
                "2. Light blue (citrate).",
                "3. Red (plain), gold (SST).",
                "4. Green (heparin).",
                "5. Lavender (EDTA), pink (EDTA).",
                "6. Gray (sodium fluoride / potassium oxalate).",
            ],
        ),
        _b(
            "Exceptions and special collections",
            "Some combinations require a different order. When coagulation "
            "specimens are drawn from a saline lock, withdraw and discard twice "
            "the dead-space volume before collecting the specimen. Blood "
            "cultures drawn from a central line or peripheral line require a "
            "paired set to rule out line infection, and the order of draw for "
            "those draws follows facility protocol.",
            CLSI_GP41,
            [
                "Citrate from a saline lock: withdraw and discard twice the dead space, then collect.",
                "Blood cultures: one set from the peripheral site and one from the line, when line sepsis is a "
                "concern.",
                "When a test requires a fasting specimen, the last meal and time should be documented.",
            ],
        ),
        _b(
            "Mixing and clot activation",
            "Each tube type has a required handling step: invert gently the "
            "specified number of times immediately after collection. Serum tubes "
            "with clot activator need thorough mixing and a full clot-activation "
            "time before centrifugation; citrate tubes must be filled to the "
            "fill line and inverted slowly to avoid clotting.",
            CLSI_GP41,
            [
                "Invert, do not shake, and do not under- or over-mix.",
                "Under-filling a citrate tube causes a falsely elevated PT/INR.",
                "Allow serum tubes to clot for the full time specified by the manufacturer before spinning.",
            ],
        ),
        _b(
            "Labeling at the bedside",
            "Label every tube in the presence of the patient, before leaving the "
            "bedside, using at least two patient identifiers plus the date, time, "
            "and collector information. CLSI requires that the label be applied "
            "before the specimen leaves the patient's immediate vicinity so the "
            "identity of the collected specimen is never in doubt.",
            CLSI_GP41,
            [
                "Two identifiers: full name and date of birth or medical record number.",
                "Never pre-label empty tubes at the workstation.",
                "If a label is lost or unreadable, recollect — do not relabel by memory.",
            ],
        ),
        _b(
            "Patient identification before the draw",
            "Before every draw, positively identify the patient with two "
            "identifiers and ask the patient to state their full name and date of "
            "birth. Inpatients and patients with cognitive impairment require "
            "verification against the wristband and chart. Transfusion specimens "
            "require stricter identification and bedside labeling procedures.",
            WHO_PHLBOTOMY,
            [
                "Ask the patient to state their name and date of birth rather than confirming with a yes/no question.",
                "Any discrepancy in identification is a stop — resolve it before drawing.",
                "For blood bank specimens, follow the transfusion service's identification protocol.",
            ],
        ),
    ],
    "phleb-additives": [
        _b(
            "Additives and what they do",
            "An additive in a collection tube does one of three things: it "
            "anticoagulates the specimen, preserves it, or directs it. "
            "Understanding the additive makes the tube choice obvious: citrate for "
            "clotting studies, EDTA for cell counts, heparin for some chemistry "
            "and blood gases, and sodium fluoride for glucose.",
            ML_BLOOD,
            [
                "Anticoagulants: sodium citrate, EDTA, heparin.",
                "Preservatives: sodium fluoride (glycolysis inhibitor) and potassium oxalate.",
                "Clot activator and gel: serum tubes (red, gold).",
            ],
        ),
        _b(
            "Serum tubes (red and gold)",
            "Red tubes are plain with no additive; blood is allowed to clot, then "
            "centrifuged and the serum separated. Gold tubes (SST) contain a clot "
            "activator and a separation gel that forms a barrier after "
            "centrifugation, so the serum can be poured or aspirated without "
            "contacting the clot. Red tubes are used for serology, chemistry, and "
            "any test requiring serum.",
            ML_LAB_TESTS,
            [
                "Allow the full clot-activation time before centrifugation.",
                "Gel tubes must be centrifuged with the correct speed and time to activate the barrier.",
                "Do not transfer serum between tubes before analysis.",
            ],
        ),
        _b(
            "Citrate tubes (light blue)",
            "Light blue tubes contain sodium citrate, which binds calcium and "
            "prevents clotting for coagulation studies such as PT/INR and aPTT. "
            "The citrate-to-blood ratio is critical: the tube must be filled to "
            "the fill line. An under-filled citrate tube contains a relatively "
            "higher concentration of citrate, which falsely elevates PT/INR.",
            ML_LAB_TESTS,
            [
                "Fill to the fill line and invert slowly 3–4 times.",
                "Any tube with less than the required fill is unacceptable and must be recollected.",
                "Use a citrate tube with a 9:1 blood-to-citrate ratio for coagulation studies.",
            ],
        ),
        _b(
            "EDTA tubes (lavender and pink)",
            "EDTA chelates calcium and prevents clotting. Lavender-top tubes are "
            "used for the complete blood count, and pink-top tubes (with a "
            "smaller fill) for pediatric and capillary collections where blood "
            "volume is limited. EDTA preserves cellular morphology, which is why "
            "samples for blood cell morphology must be analyzed promptly.",
            ML_BLOOD,
            [
                "Lavender top = complete blood count; pink top = small-volume pediatric collection.",
                "Invert 8 times; do not under-mix, as clotting will cause a falsely elevated cell count.",
                "EDTA specimens for differential counts should be analyzed within a few hours.",
            ],
        ),
        _b(
            "Heparin and glucose tubes (green and gray)",
            "Green-top tubes contain heparin, an anticoagulant that works by "
            "activating antithrombin, and are used for chemistry tests that must "
            "be performed on whole blood or plasma. Gray-top tubes contain sodium "
            "fluoride, which inhibits glycolysis so that red cells do not consume "
            "glucose in the tube, and potassium oxalate, an anticoagulant.",
            CDC_DIABETES,
            [
                "Green heparin tubes are used for some chemistry assays and for blood gas specimens.",
                "Gray tubes delay glycolysis, giving more reliable glucose results than plain serum tubes.",
                "Label the tube with the exact collection time when a timed test such as a glucose tolerance test is "
                "ordered.",
            ],
        ),
        _b(
            "Choosing the right tube for the test",
            "Read the test order carefully, and take it from the laboratory's test "
            "menu rather than from memory. Multiple analytes from one draw often "
            "require several tubes, and the order of draw determines which tube "
            "receives the specimen first. When in doubt, check with the "
            "laboratory before you begin.",
            CLSI_GP41,
            [
                "Confirm tube type, volume, and order of draw from the laboratory's collection manual.",
                "Additive and volume must both be right — a correct tube at the wrong fill volume is still a wrong "
                "specimen.",
                "Special handling requirements (cold, dark, on ice, immediate delivery) are part of the order.",
            ],
        ),
    ],
    "phleb-site": [
        _b(
            "Vein selection",
            "The median cubital vein in the antecubital fossa is the preferred "
            "site for venipuncture because it is large, superficial, well anchored, "
            "and less likely to move. The basilic and cephalic veins are "
            "alternatives. Palpate rather than look: a good vein feels soft, "
            "bouncy, and fills on release, and following it reduces the number of "
            "attempts.",
            ML_VENIPUNCTURE,
            [
                "Median cubital vein is first choice; basilic is the second; cephalic is less suitable because it is "
                "more mobile.",
                "Palpate to confirm vein location and size before preparing the site.",
                "In difficult draws, warm the arm to dilate veins and use a tourniquet for less than one minute.",
            ],
        ),
        _b(
            "Sites to avoid",
            "Never draw from an arm with an intravenous line, an arteriovenous "
            "fistula, a hematoma, a scar, a burn, an infected or inflamed area, or "
            "a limb used for dialysis. Avoid drawing proximal to an IV because "
            "contaminating fluid may be aspirated, and avoid the side of a "
            "mastectomy or axillary surgery, where lymphedema is a risk.",
            ML_VENIPUNCTURE,
            [
                "Do not use the arm with a running IV; draw from the opposite side.",
                "Avoid scarred, bruised, sclerosed, or previously accessed sites.",
                "In dialysis patients, avoid the fistula arm entirely.",
            ],
        ),
        _b(
            "Patient positioning and preparation",
            "Place the patient supine or semi-recumbent with the arm extended and "
            "supported, and ask the patient to make a fist to engorge the veins. "
            "Clean the site with an antiseptic and let it dry completely — "
            "applying the needle before the antiseptic has dried causes "
            "hemolysis and contaminates the site. Avoid areas with hair, and do "
            "not apply the tourniquet too tightly.",
            ML_VENIPUNCTURE,
            [
                "Apply the tourniquet 1–2 inches above the antecubital fossa; it should be felt but not painful.",
                "Let the antiseptic dry for the manufacturer's recommended time before puncturing.",
                "Ask the patient to state their name and date of birth before you begin.",
            ],
        ),
        _b(
            "Tourniquet time and patient comfort",
            "Prolonged tourniquet time causes hemoconcentration and pseudohyperkalemia "
            "and increases discomfort. Release the tourniquet as soon as the blood "
            "is flowing. Talk the patient through each step, keep them informed, "
            "and if the draw is difficult, consider options such as warming the "
            "arm, using a smaller-gauge needle, or asking the patient to pump "
            "their fist.",
            WHO_PHLBOTOMY,
            [
                "Keep the tourniquet on for the shortest possible time.",
                "Prolonged tourniquet use causes falsely elevated potassium and falsely elevated glucose.",
                "If more than two attempts are needed, seek help rather than repeatedly puncturing.",
            ],
        ),
        _b(
            "Needle choice and angle",
            "Use the smallest gauge that will reliably deliver the specimen, "
            "typically 21–23 gauge for routine venipuncture and a smaller gauge "
            "for small or fragile veins. Insert the needle with the bevel up at a "
            "30–45 degree angle, advancing slightly once the vein is entered to "
            "avoid exiting the other wall of the vein.",
            ML_VENIPUNCTURE,
            [
                "Bevel up, 30–45 degree entry angle; lower the angle once in the vein.",
                "Smaller gauge means less trauma and less hemolysis but longer draw time.",
                "Never re-insert a needle that has been withdrawn from a failed attempt into the same vein.",
            ],
        ),
        _b(
            "Difficult draws and alternatives",
            "When venipuncture is not possible, alternatives include capillary "
            "puncture (heel stick for infants, finger stick for adults) and "
            "collection from vascular access devices. Capillary specimens have "
            "different reference ranges for some analytes and must be documented "
            "as such. Always attempt venipuncture first when it is appropriate.",
            CLSI_GP41,
            [
                "Capillary puncture: lateral fingertip or medial heel; do not use a previously punctured site.",
                "Arterial puncture is a higher-risk procedure requiring specific training.",
                "Document the collection method and any complications.",
            ],
        ),
    ],
    "phleb-handling": [
        _b(
            "Labeling and identification at the bedside",
            "Every specimen must be labeled in the patient's presence with at "
            "least two identifiers, the date and time of collection, and the "
            "collector's identification. Pre-labeled tubes must not be taken into "
            "the room. A mislabeled or unlabeled specimen cannot be used and must "
            "be recollected — a recollection costs more than a careful label.",
            CLSI_GP41,
            [
                "Label at the bedside, before leaving the patient.",
                "Use the patient's full name and date of birth or medical record number.",
                "If in doubt, recollect rather than relabel from memory.",
            ],
        ),
        _b(
            "Transport and time to the laboratory",
            "Specimens must be transported promptly and protected from light, "
            "heat, and freezing where required. Routine blood samples should "
            "reach the laboratory for processing within about two hours of "
            "collection; tests with longer stability windows are specified "
            "individually. Send unrefrigerated specimens that require immediate "
            "processing with a hand-carried courier.",
            CLSI_GP41,
            [
                "Protect specimens from extremes of temperature and from light during transport.",
                "Document the collection and receipt times.",
                "Use a biohazard transport bag and a rigid carrier for all specimens.",
            ],
        ),
        _b(
            "Hemolysis and specimen integrity",
            "Hemolysis — rupture of red blood cells — is the most common cause of "
            "rejected specimens and can falsely lower potassium, raise LDH and "
            "bilirubin, and interfere with many assays. It is caused by rough "
            "handling, small needles with excessive vacuum, drawing through a "
            "needle, or vigorous mixing. A hemolyzed specimen must be recollected.",
            ML_BLOOD,
            [
                "Use appropriate needle size and avoid excessive vacuum.",
                "Do not transfer blood through a needle or force it through a smaller needle.",
                "Allow a full clot-activation time on serum tubes before transport.",
            ],
        ),
        _b(
            "Fasting and timed specimens",
            "Some tests require fasting (typically 8–12 hours) and others are "
            "timed, such as a 2-hour oral glucose tolerance test and drug levels. "
            "Document the last food or drink intake, the exact collection time, "
            "and any medication taken. When a fasting requirement is not met, "
            "escalate rather than proceeding.",
            ML_OGTT,
            [
                "For the 2-hour OGTT: fasting 8 hours, then the glucose load at time zero, with samples at exactly 2 "
                "hours.",
                "Water is usually permitted during a fast; confirm with the laboratory.",
                "Document deviations (a missed fast, recent illness) on the requisition.",
            ],
        ),
        _b(
            "Storage, refrigeration, and stability",
            "Refrigeration slows bacterial growth in specimens that will not be "
            "processed immediately, but freezing or over-refrigeration can lyse "
            "cells and destroy analytes. Know which tests in your order set "
            "require refrigeration, which must stay at room temperature, and "
            "which must be delivered within a specific window.",
            ML_LAB_TESTS,
            [
                "Refrigerate when the test directory says to; never freeze unless directed.",
                "Do not place specimens on ice unless the order requires it.",
                "When in doubt, call the laboratory before discarding or recollecting.",
            ],
        ),
        _b(
            "Chain of custody and special handling",
            "Some specimens have legal or safety significance: blood alcohol "
            "levels, drugs of abuse, sexual assault evidence, and newborn "
            "screens. These follow strict chain-of-custody procedures with sealed "
            "tamper-evident transport containers, documented transfers, and "
            "specific handling instructions. Never leave such a specimen "
            "unattended.",
            OSHA_BBP,
            [
                "Seal and sign the tamper-evident container across the seal.",
                "Document every transfer with date, time, and signatures.",
                "Handle as potentially infectious throughout.",
            ],
        ),
    ],
    "phleb-complications": [
        _b(
            "Hematoma",
            "A hematoma is a collection of blood under the skin caused by a "
            "needle that has exited the vein or by leaking during the draw. It "
            "appears as a swelling that may be painful and discolored and can "
            "obscure a future venipuncture site. To manage it, apply gentle "
            "pressure after the draw, then elevate the arm and apply a cold pack "
            "for the first 24 hours.",
            ML_VENIPUNCTURE,
            [
                "Apply gentle pressure for 2–5 minutes after the draw; longer if the patient is on anticoagulants.",
                "Ice for the first 24 hours, then warm compresses to promote absorption.",
                "Report a rapidly expanding, painful swelling or bleeding that does not stop immediately.",
            ],
        ),
        _b(
            "Hemolysis",
            "Hemolysis can occur at the time of collection or later in transport. "
            "In vivo hemolysis is caused by fragile or diseased red cells; "
            "ex vivo hemolysis is caused by collection technique — small-bore "
            "needles, excessive vacuum, forceful transfer through a needle, or "
            "rough handling. It causes falsely low potassium and falsely high "
            "LDH, and requires recollection.",
            ML_BLOOD,
            [
                "Use the correct needle gauge and avoid excessive vacuum.",
                "Never push blood through a needle or transfer it between tubes.",
                "Let serum tubes clot fully and centrifuge gently.",
            ],
        ),
        _b(
            "Nerve injury and pain",
            "Nerve injury is uncommon but real, and it most often affects the "
            "median nerve or the lateral cutaneous nerve of the forearm during "
            "antecubital punctures. Symptoms include shooting pain, tingling, or "
            "numbness along the distribution of the affected nerve. Document the "
            "complaint, notify the supervisor, and follow the facility's incident "
            "process.",
            ML_VENIPUNCTURE,
            [
                "Nerve injury is more likely with a deep, high-angle puncture or repeated attempts.",
                "Document the exact symptoms, the site, and the time of the complaint.",
                "Reassure the patient and explain that most symptoms resolve.",
            ],
        ),
        _b(
            "Syncope and vasovagal reactions",
            "Some patients faint during or after a blood draw because of a "
            "vasovagal response to the sight of blood, fear, or prolonged "
            "standing. Warning signs include pallor, sweating, nausea, and "
            "lightheadedness. Prevent it by having the patient lie down, keep "
            "them talking, and ensure they remain lying down for several minutes "
            "after the draw.",
            ML_DEHYDRATION,
            [
                "Position the patient supine for all draws when possible.",
                "If the patient feels faint, lay them flat and elevate the legs.",
                "Ensure the patient has recovered before allowing them to stand and leave.",
            ],
        ),
        _b(
            "Accidental arterial puncture",
            "An inadvertent arterial puncture is recognized by a bright red, "
            "pulsatile blood return that fills the collection tube rapidly. Stop "
            "immediately, apply firm pressure for 10 minutes or more, and "
            "document it. Arterial specimens for blood gases have specific "
            "collection requirements and a much lower complication tolerance, so "
            "if an artery is entered during a venous draw, the specimen is "
            "usually not usable for the venous order.",
            ML_VENIPUNCTURE,
            [
                "Pulsatile flow and bright red blood suggest arterial entry.",
                "Apply firm pressure for 10+ minutes and check for expanding swelling before releasing.",
                "Notify the supervisor and document the event.",
            ],
        ),
        _b(
            "Infection, back-bleeding, and needlestick injury",
            "Infection is rare when aseptic technique is used, but back-bleeding "
            "into the tissue can produce a hematoma or bruising. Needlestick "
            "injuries are prevented by never recapping and by using safety "
            "devices; when one occurs, the injury must be washed, reported "
            "immediately, and evaluated under the post-exposure protocol, which "
            "includes consideration of hepatitis B and HIV post-exposure "
            "prophylaxis based on source and employee status.",
            OSHA_BBP_HAZARDS,
            [
                "Wash a needlestick immediately with soap and water and report it right away — timing matters for "
                "post-exposure prophylaxis.",
                "Do not squeeze or suck the wound.",
                "Sharps disposal at the point of use prevents most injuries.",
            ],
        ),
    ],
    "phleb-safety": [
        _b(
            "Standard Precautions for every draw",
            "Every blood draw is performed with Standard Precautions: hand "
            "hygiene before and after, gloves whenever blood contact is possible, "
            "a new sterile needle and syringe for each patient, and safe disposal "
            "of all sharps at the point of use. The assumption that blood is "
            "'clean' only because a patient looks healthy is exactly what OSHA's "
            "universal precautions rule was written to prevent.",
            OSHA_BBP_GENERAL,
            [
                "Treat all blood and body fluids as potentially infectious.",
                "Hand hygiene before putting on gloves and after removing them.",
                "Change gloves between patients, and between tasks if glove integrity is questionable.",
            ],
        ),
        _b(
            "Needle and syringe safety",
            "Use a safety-engineered needle with an engine-activated or "
            "user-activated feature, activate it immediately after use, and never "
            "recap, bend, break, or detach a used needle. A needle that has been "
            "used on one patient must never be used on another, and a used "
            "syringe must never be reused for a second patient even with a new "
            "needle.",
            CDC_INJECTION_SAFETY,
            [
                "One needle, one syringe, one time.",
                "Never recap; activate the safety mechanism at the point of use.",
                "Never remove a used device from a sharps container.",
            ],
        ),
        _b(
            "Personal protective equipment",
            "Gloves are required for any procedure where exposure to blood is "
            "reasonably anticipated, and they must be changed between patients. "
            "Additional protection depends on the risk: gowns and eye protection "
            "for splash risk, and a mask with eye protection for aerosol or "
            "splash-generating procedures. PPE does not replace hand hygiene or "
            "correct technique.",
            OSHA_PPE,
            [
                "Change gloves after every patient and after any tear or contamination.",
                "Remove PPE before leaving the room and wash hands immediately.",
                "Know which procedures require eye and face protection.",
            ],
        ),
        _b(
            "Sharps container management",
            "Sharps containers must be puncture-resistant, leak-proof, and "
            "labeled; they belong within arm's reach of the area where sharps "
            "are used, and they must be replaced before they are overfilled so "
            "that closing the lid never requires touching discarded needles.",
            OSHA_BBP_STANDARDS,
            [
                "Never overfill a sharps container; replace it at the fill line.",
                "Never recap or manually remove a device from a sharps container.",
                "Transport full containers for disposal according to the waste plan.",
            ],
        ),
        _b(
            "Healthcare workplace hazards beyond bloodborne pathogens",
            "NIOSH groups the occupational risks for healthcare workers into "
            "infectious agents, bloodborne diseases, chemical hazards, "
            "antineoplastic (chemotherapy) agents, and work stress. Infection "
            "control is only one part of the picture: chemicals, cleaning "
            "products, hazardous drugs, radiation, and ergonomic strain account "
            "for a large share of workplace injuries and illness in healthcare.",
            CDC_NIOSH_RISK,
            [
                "Chemical hazards: cleaning agents, disinfectants, formaldehyde, and anesthetic gases.",
                "Antineoplastic agents require dedicated handling equipment and spill kits.",
                "Work stress and burnout affect retention and patient safety as much as physical injury does.",
            ],
        ),
        _b(
            "OSHA and the healthcare workplace",
            "OSHA covers healthcare settings directly: the bloodborne pathogens "
            "standard, personal protective equipment, hazard communication for "
            "cleaning chemicals, and ergonomics. Bloodborne pathogens are the "
            "standard most often tested on the CCMA, but the others come up in "
            "practice every day — from choosing the right glove to preventing a "
            "repetitive-strain injury while doing injections all day.",
            OSHA_HEALTHCARE,
            [
                "Every covered employee needs hazard communication training and access to safety data sheets.",
                "Report injuries and near misses — reporting is what drives prevention.",
                "Employers must provide PPE at no cost to the employee.",
            ],
        ),
        _b(
            "Exposure control plan and training",
            "OSHA requires an exposure control plan that is reviewed and updated "
            "at least annually, accessible to all employees, and supported by "
            "training. It covers engineering and work practice controls, PPE, "
            "the hepatitis B vaccination program, post-exposure evaluation and "
            "follow-up, and recordkeeping.",
            OSHA_BBP_RESOURCES,
            [
                "The exposure control plan must be reviewed and updated at least annually.",
                "Annual training in bloodborne pathogens is required for all covered employees.",
                "Hepatitis B vaccination must be offered at no cost after exposure to blood or body fluids.",
            ],
        ),
        _b(
            "Responding to an exposure",
            "If a needlestick or splash occurs, wash the site immediately, report "
            "the exposure to the supervisor, and complete the post-exposure "
            "evaluation promptly. Source-patient testing and the employee's "
            "serology status determine whether hepatitis B vaccination, HBIG, "
            "or HIV post-exposure prophylaxis is indicated, and the decision is "
            "time-sensitive.",
            OSHA_NEEDLESTICK,
            [
                "Wash with soap and water; do not squeeze or suck the wound.",
                "Report the incident immediately — do not wait to see if it hurts.",
                "Complete the incident report and follow the post-exposure protocol.",
            ],
        ),
    ],
    "phleb-who": [
        _b(
            "WHO best practices in phlebotomy",
            "The WHO's best-practice guidance for drawing blood is built around "
            "the idea that most risks in phlebotomy are preventable. It covers "
            "preparation and planning, patient identification and communication, "
            "the collection procedure itself, and safe disposal — with sharps "
            "safety and the prevention of needlestick injury at the center.",
            WHO_PHLBOTOMY,
            [
                "Every risk of phlebotomy can be eliminated or reduced by following the recommended practices.",
                "The guidelines are used as the basis for national phlebotomy training programmes worldwide.",
                "They place sharps safety and patient identification as the two highest priorities.",
            ],
        ),
        _b(
            "Safe sharps handling in phlebotomy",
            "Never recap, manually remove a needle from a syringe, or bend or "
            "break a used needle. After the draw, activate the safety device, "
            "discard the device directly into a sharps container, and dispose of "
            "the whole assembly — needle and syringe together — in the same "
            "container.",
            WHO_INJECTION_SAFETY,
            [
                "Discard the entire needle-and-syringe assembly into the sharps container.",
                "Never leave a used sharps container unattended or in a public area.",
                "Report any needlestick immediately, even if the injury seems minor.",
            ],
        ),
        _b(
            "Reducing pain and distress",
            "Good technique reduces both pain and anxiety. Use the smallest "
            "suitable needle, insert with the bevel up at a shallow angle, and "
            "release the tourniquet as soon as blood flow is established. For "
            "children and anxious patients, distraction, a relaxed posture, and "
            "explaining what is about to happen all measurably reduce distress.",
            ML_CHILD_HEALTH,
            [
                "Explain each step before you do it, especially with children.",
                "Distraction and positioning reduce distress and improve vein quality.",
                "Keep the patient informed during the draw; silence increases anxiety.",
            ],
        ),
        _b(
            "Infection prevention during phlebotomy",
            "Hand hygiene, gloves, a new sterile needle and syringe for every "
            "patient, a clean and dry site, and the correct order of draw are "
            "the core infection prevention measures. The WHO emphasizes that "
            "reuse of syringes or needles between patients is a major route of "
            "bloodborne pathogen transmission and is entirely preventable.",
            WHO_HAND_HYGIENE,
            [
                "Perform hand hygiene before putting on gloves and after removing them.",
                "Clean the site and allow it to dry before puncturing.",
                "Never reuse a needle or syringe, even for the same patient.",
            ],
        ),
        _b(
            "Correct sharps disposal",
            "Discard sharps immediately into a nearby puncture-resistant "
            "container. Do not leave filled containers on work surfaces, do not "
            "overfill them, and do not transport them loosely. In settings with "
            "limited resources, WHO emphasizes a safe, accessible disposal "
            "system at every point of use so that the distance between the "
            "patient and the container is minimal.",
            CDC_INJECTION_SAFETY,
            [
                "The sharps container should be within arm's reach of the procedure.",
                "Replace containers at the fill line and seal and transport per policy.",
                "Never throw loose sharps into regular waste bags.",
            ],
        ),
        _b(
            "Quality and patient identification in resource-limited settings",
            "WHO notes that in many settings the biggest risks come from "
            "reused equipment, unlabeled specimens, and inadequate record "
            "keeping. A simple system — two identifiers, labeling at the bedside, "
            "and a log of collection time and collector — prevents the "
            "misidentification that makes results unsafe.",
            WHO_PHLBOTOMY,
            [
                "Two identifiers for every patient, every time.",
                "Label at the point of collection, never before.",
                "A simple collection log with date, time, and collector supports accountability.",
            ],
        ),
    ],
    "phleb-glucose": [
        _b(
            "Point-of-care versus laboratory glucose",
            "Point-of-care glucometers give a result in seconds and are essential "
            "for hypoglycemia treatment and for daily self-management, while "
            "laboratory methods are more accurate and are used for diagnosis. "
            "The main sources of disagreement are timing relative to the last "
            "meal, the type of specimen, and the analyzer's calibration.",
            ML_A1C,
            [
                "Point-of-care meters are usually CLIA-waived in outpatient settings.",
                "Plasma glucose and whole blood glucose read differently — meters typically report plasma-equivalent "
                "values.",
                "Document the time of the test and the time of the last meal.",
            ],
        ),
        _b(
            "Capillary collection technique",
            "For fingerstick collection, wash and dry the hands, warm the finger, "
            "clean the site with an alcohol wipe and let it dry fully, use a "
            "single-use lancet with a controlled puncture depth, and apply the "
            "blood drop to the strip as the manufacturer directs. A common "
            "error is milking the finger, which dilutes the specimen with tissue "
            "fluid and falsely lowers the result.",
            FDA_CLIA_WAIVED,
            [
                "Use a new single-use lancet for every patient and every puncture.",
                "Never squeeze or milk the finger — alternate sites and warm the hand instead.",
                "Alternate sites to avoid long-term callus formation.",
            ],
        ),
        _b(
            "Quality control for waived testing",
            "CLIA-waived testing carries responsibilities even though it does not "
            "require full laboratory certification. Follow the manufacturer's "
            "instructions, run control solution at the required intervals and "
            "whenever a result is unexpected, maintain records of all testing "
            "performed, and report critical results according to policy.",
            FDA_CLIA,
            [
                "Run liquid controls with each new lot of strips, when results are unexpected, and on the "
                "manufacturer's schedule.",
                "Keep a log of control results and corrective actions.",
                "Have a written procedure for out-of-range and critical results.",
            ],
        ),
        _b(
            "Specimen handling for laboratory glucose",
            "For a laboratory glucose, use the correct tube — sodium fluoride "
            "inhibits glycolysis so that red cells do not consume glucose after "
            "collection. Serum or plasma glucose should be separated within 30 to "
            "60 minutes of collection; delayed separation produces falsely low "
            "results because the cells consume glucose.",
            CDC_DIABETES,
            [
                "Grey-top sodium fluoride tubes are preferred for glucose in most settings.",
                "Separate and centrifuge within 30–60 minutes, or refrigerate promptly if the lab permits.",
                "Document the time of collection for any timed or therapeutic monitoring test.",
            ],
        ),
        _b(
            "Diagnostic thresholds",
            "Diabetes is diagnosed with a fasting plasma glucose of 126 mg/dL or "
            "higher, a 2-hour oral glucose tolerance test of 200 mg/dL or higher, "
            "or an A1C of 6.5% or higher. A random plasma glucose of 200 mg/dL or "
            "higher with classic hyperglycemic symptoms is diagnostic without "
            "confirmation.",
            ADA_DIAGNOSIS,
            [
                "Prediabetes: FPG 100–125 mg/dL, 2-hour OGTT 140–199 mg/dL, A1C 5.7–6.4%.",
                "Confirm abnormal screening results unless classic symptoms with hyperglycemia are present.",
                "A1C is unreliable in hemoglobinopathies, recent transfusion, pregnancy, and some hemoglobin variants.",
            ],
        ),
        _b(
            "Oral glucose tolerance testing",
            "The 2-hour OGTT requires an overnight fast of at least 8 hours, a "
            "baseline sample, ingestion of 75 grams of anhydrous glucose, and a "
            "second sample exactly 2 hours later. Nausea during the test is not "
            "uncommon; document it, because vomiting invalidates the result and "
            "the test usually needs to be repeated.",
            ML_OGTT,
            [
                "Fasting means no calories for at least 8 hours; water is usually permitted.",
                "The 2-hour sample is drawn exactly 2 hours after the glucose load.",
                "Document the start time, the load given, and any symptoms.",
            ],
        ),
    ],
    # ------------------------------------------------------------------
    # CPR / BLS
    # ------------------------------------------------------------------
    "cpr-adult": [
        _b(
            "Adult BLS: the core sequence",
            "For an unresponsive adult with no normal breathing and no pulse, "
            "activate the emergency response system and begin CPR immediately. "
            "Compressions come first: 30 compressions to 2 breaths at a rate of "
            "100–120 per minute with a depth of at least 5 cm (2 inches) and no "
            "more than 6 cm (2.4 inches). Use an AED as soon as it is available.",
            AHA_ADULT_BLS,
            [
                "Check responsiveness, call for help, and get an AED.",
                "30:2 compression-to-ventilation ratio for a single rescuer with an advanced airway, compressions "
                "continue without pausing for breaths.",
                "Minimize interruptions and switch compressors about every 2 minutes.",
            ],
        ),
        _b(
            "High-quality compression technique",
            "Quality is measurable and improvable: rate 100–120 per minute, depth "
            "5–6 cm, full chest recoil with no leaning, and interruptions under 10 "
            "seconds. Push hard and fast, but push straight down on the lower half "
            "of the sternum with the heel of the hand. Let the chest fully "
            "recoil between compressions.",
            AHA_HIGH_QUALITY,
            [
                "Heel of one hand on the lower half of the sternum, other hand on top, arms straight.",
                "Full recoil and equal compression time.",
                "Use a feedback device if available — compression depth and rate devices are now routine in clinical "
                "settings.",
            ],
        ),
        _b(
            "Airway and ventilation",
            "Open the airway with a head tilt–chin lift (or jaw thrust if a "
            "cervical spine injury is suspected), give two breaths of about one "
            "second each, and watch for visible chest rise. Deliver enough air to "
            "make the chest rise, but avoid excessive ventilation, which "
            "decreases venous return and cardiac output.",
            AHA_ADULT_BLS,
            [
                "Head tilt–chin lift; use a jaw thrust if a cervical spine injury is suspected.",
                "Each breath over about 1 second with visible chest rise.",
                "Do not hyperventilate; excessive ventilation reduces cardiac output and increases intrathoracic "
                "pressure.",
            ],
        ),
        _b(
            "Special situations",
            "Pregnancy in the third trimester: displace the uterus to the left, "
            "or move the patient to the left side, to relieve aortocaval "
            "compression. Suspected opioid overdose: give naloxone and support "
            "ventilation, because respiratory arrest is the usual cause of arrest. "
            "Trauma, drowning, and electrocution are also managed differently "
            "from a typical medical arrest.",
            AHA_TOP_THINGS,
            [
                "Left uterine displacement or left lateral positioning in late pregnancy.",
                "Naloxone for suspected opioid overdose, with a focus on ventilation.",
                "Drowning and asphyxia arrests need early ventilation, not compressions alone.",
            ],
        ),
        _b(
            "Two-rescuer CPR and teamwork",
            "Two rescuers compress at a rate of 100–120 per minute with a ratio of "
            "30:2 and rotate compressors every 2 minutes to prevent fatigue. The "
            "team leader assigns roles, watches the quality of compressions and "
            "the clock, and calls for the AED, medications, and any change in "
            "rhythm.",
            AHRQ_TEAMSTEPPS,
            [
                "Compressors rotate every 2 minutes; the change should take under 5 seconds.",
                "Change compressors at the rhythm check if quality drops.",
                "The team leader should not be doing compressions.",
            ],
        ),
        _b(
            "When to stop CPR",
            "Continue CPR until the patient shows clear signs of life (movement, "
            "breathing, or a pulse), a qualified healthcare professional takes "
            "over, the scene becomes unsafe, or you are physically unable to "
            "continue. Good Samaritan protection and an emergency medical "
            "exemption usually apply while acting in good faith within your "
            "training.",
            RED_CROSS_FIRST_AID,
            [
                "Signs of life: purposeful movement, normal breathing, or a definite pulse.",
                "Do not stop because you are tired — call for relief and continue.",
                "Handover should include time of arrest, shocks given, medications, and any ROSC.",
            ],
        ),
    ],
    "cpr-child": [
        _b(
            "Child BLS: what is different",
            "For a child from about 1 year to puberty, CPR follows the same "
            "principles as adult CPR, with two differences: compressions are about "
            "one third of the chest depth (roughly 5 cm / 2 inches) rather than a "
            "fixed adult depth, and two rescuers use a 15:2 ratio to give more "
            "ventilations. Rescue breaths are particularly important because "
            "respiratory causes are the usual reason a child arrests.",
            AHA_PALS,
            [
                "Rate stays 100–120 per minute for children.",
                "Depth about one third of the chest AP diameter, approximately 5 cm.",
                "15:2 with two rescuers; 30:2 with one rescuer.",
            ],
        ),
        _b(
            "Assessing the child",
            "Check for responsiveness and breathing for no more than 10 seconds. "
            "Look for signs of life such as movement or normal breathing rather "
            "than agonal gasps, which occur in some arrests. If the child is not "
            "breathing normally, start CPR and call for help.",
            ML_CPR_CHILD,
            [
                "Agonal gasps are not normal breathing — treat them as cardiac arrest.",
                "Check for a pulse for no more than 10 seconds if you are trained.",
                "Start CPR immediately; do not delay to find a pulse.",
            ],
        ),
        _b(
            "Brachial pulse and CPR technique",
            "In infants and children, the brachial pulse at the inner upper arm is "
            "used to assess a pulse. Compress the lower half of the sternum with "
            "one or two hands, keeping the rate at 100–120 per minute and "
            "allowing full recoil. If a second rescuer is available, one "
            "compresses while the other prepares the airway.",
            AHA_PALS,
            [
                "Brachial pulse is the pediatric pulse check point.",
                "One- or two-hand compressions are both acceptable for a child.",
                "Look for chest rise after each set of breaths to confirm effective ventilation.",
            ],
        ),
        _b(
            "Common causes of pediatric arrest",
            "Children most often arrest because of a respiratory problem — "
            "obstruction, asthma, pneumonia, or dehydration — rather than a "
            "primary cardiac cause. Because of this, effective ventilation is "
            "the priority, and airway obstruction should be looked for and "
            "relieved during the resuscitation.",
            ML_PNEUMONIA,
            [
                "Respiratory causes account for the majority of pediatric arrests.",
                "Look for and relieve airway obstruction during CPR.",
                "AEDs are used in children over 1 year if available; use pediatric pads or attenuating pads when the "
                "child is small.",
            ],
        ),
        _b(
            "Pediatric AED and pads",
            "Use an AED on a child who is unresponsive and not breathing normally. "
            "If pediatric pads are available and the child is small enough, use "
            "them; if not, use adult pads — a shock to a pediatric patient is far "
            "better than no shock. Pediatric pads must not be used on an adult, "
            "and adult pads must not be cut or resized.",
            AHA_AED_PROGRAM,
            [
                "Use pediatric attenuating pads if available; otherwise use adult pads without modification.",
                "If the child is larger than about 8 years or has reached puberty, use adult pads.",
                "Keep the chest bare and dry — medication patches must be removed and the skin wiped.",
            ],
        ),
        _b(
            "When to stop and handover",
            "Continue until the child shows signs of life, a healthcare "
            "professional takes over, the scene becomes unsafe, or you are unable "
            "to continue. In the handover, tell the team the child's estimated "
            "age and weight, the time of arrest, the duration of CPR, the number "
            "of shocks, medications given, and any signs of life observed.",
            RED_CROSS_FIRST_AID_STEPS,
            [
                "Handover should include estimated age and weight — it changes dosing.",
                "Note the time of arrest and the time of ROSC.",
                "Note anything known about the cause, including choking, allergy, or trauma.",
            ],
        ),
    ],
    "cpr-infant": [
        _b(
            "Infant BLS: what is different",
            "For an infant under 1 year, use 15 compressions to 2 breaths for "
            "two rescuers and 30:2 for a single rescuer, a rate of 100–120 per "
            "minute, and a depth of about one third of the chest, roughly 4 cm "
            "(1.5 inches). Use the brachial pulse to assess circulation.",
            AHA_NEONATAL_ALG,
            [
                "Two-rescuer ratio 15:2; single-rescuer ratio 30:2.",
                "Compression depth about 4 cm (1.5 inches) — one third of the chest.",
                "Rate 100–120 per minute.",
            ],
        ),
        _b(
            "Compression technique for infants",
            "The 2025 AHA guidelines eliminated the two-finger technique because "
            "it does not reliably achieve adequate depth. Use the two-thumb "
            "encircling-hands technique (with the hands forming a ring around the "
            "chest) or the heel of one hand for a lone rescuer, with the chest "
            "compressed just below the nipple line.",
            AHA_TOP_THINGS,
            [
                "Two-thumb encircling hands technique, or heel of one hand for a single rescuer.",
                "Compress the chest just below the nipple line, not on it.",
                "Do not use the two-finger technique.",
            ],
        ),
        _b(
            "Airway and breathing in infants",
            "Because infants have large occiputs, a neutral position is achieved "
            "by placing a folded towel under the shoulders. Keep the head in a "
            "sniffing position — tipped too far back, the airway closes. Give "
            "gentle breaths that produce visible chest rise, and check for "
            "over-ventilation.",
            ML_CPR_INFANT,
            [
                "Pad the shoulders to maintain a neutral airway position.",
                "Look for chest rise rather than auscultating for breath sounds.",
                "Avoid excessive ventilation — it causes gastric distension and reduces effectiveness.",
            ],
        ),
        _b(
            "Choking in infants",
            "The 2025 AHA guidelines changed the infant choking response: for a "
            "conscious choking infant, alternate 5 back blows with 5 chest "
            "thrusts until the object is expelled or the infant becomes "
            "unresponsive. Abdominal thrusts are not recommended for infants. If "
            "the infant becomes unresponsive, begin CPR and look for the object "
            "before giving breaths.",
            AHA_CHILD_FBAO,
            [
                "5 back blows then 5 chest thrusts, repeated.",
                "Do not use abdominal thrusts on an infant.",
                "If unresponsive: start CPR, open the airway, and remove the object if visible before giving breaths.",
            ],
        ),
        _b(
            "Neonatal resuscitation differences",
            "A newly born baby is resusitated under the neonatal algorithm, which "
            "emphasizes warmth, positioning, drying, and clearing the airway, "
            "followed by positive-pressure ventilation if the baby is apneic or "
            "has a heart rate below 100. Chest compressions are coordinated with "
            "ventilation at 3:1 and are started if the heart rate remains below "
            "60 despite effective ventilation.",
            AHA_NEONATAL_ALG,
            [
                "Steps happen within the first minute after birth.",
                "Skin-to-skin contact and warmth are the first steps for a vigorous infant.",
                "Preductal oxygen saturation targets are time-based: about 60–65% at 1 minute rising to 85–95% by 10 "
                "minutes.",
            ],
        ),
        _b(
            "Prevention and preparation",
            "Most infant emergencies are preventable. Safe sleep practices — "
            "placing the infant on their back on a firm, flat surface with no "
            "loose bedding — sharply reduce sudden infant death syndrome. "
            "Caregivers should be taught infant CPR and choking response, and "
            "families should have a plan for emergency care.",
            CDC_CHILD_DEV,
            [
                "Safe sleep: back position, firm flat surface, no pillows or loose bedding.",
                "Post-partum education should include CPR, choking response, and when to call 911.",
                "Know the child's age in months and any relevant medical history before an emergency happens.",
            ],
        ),
    ],
    "cpr-aed": [
        _b(
            "How an AED works",
            "An AED analyzes the heart rhythm and, if the rhythm is one that can "
            "be treated with a shock, prompts the user to deliver it. Because the "
            "device only shocks shockable rhythms, it cannot shock a heart that "
            "is beating normally, and a patient in a non-shockable rhythm will "
            "receive CPR instructions instead. Defibrillation is the definitive "
            "treatment for ventricular fibrillation and pulseless ventricular "
            "tachycardia.",
            AHA_AED_PROGRAM,
            [
                "Chances of survival fall 7–10% for every minute without defibrillation.",
                "The AED is safe to use on anyone in cardiac arrest — you do not need to diagnose the rhythm.",
                "Resume CPR immediately after the shock.",
            ],
        ),
        _b(
            "Step-by-step AED use",
            "Turn the device on, bare the chest, apply the pads to the upper right "
            "chest and the left side below the armpit, and follow the prompts. "
            "Stand clear during analysis and shock delivery, and make sure no one "
            "is touching the patient. Resume CPR immediately after the shock, "
            "without pausing to check a pulse.",
            AHA_AED_PROGRAM,
            [
                "Pad placement: upper right chest and left lateral chest below the armpit.",
                "Say 'clear' and visually check that nobody is in contact with the patient.",
                "Resume compressions immediately after the shock is delivered.",
            ],
        ),
        _b(
            "Special situations",
            "Remove transdermal medication patches before applying pads, and "
            "wipe the skin under them, because the patch can block the shock "
            "energy. Remove jewelry and metal objects that touch the chest, and "
            "dry the chest thoroughly — wet skin can cause arcing. A pacemaker or "
            "ICD is not a contraindication: place the pad at least an inch away "
            "from the device.",
            AHA_AED_PROGRAM,
            [
                "Remove medication patches and wipe the skin; never apply pads over a patch.",
                "Dry the chest — wet skin causes arcing and burns.",
                "For a pacemaker or ICD, place the pad at least 1 inch (2.5 cm) away from the generator.",
            ],
        ),
        _b(
            "AEDs in children and special populations",
            "Use pediatric pads or attenuating pads for a child under 8 years or "
            "anyone smaller than the pad; otherwise use adult pads, which are "
            "acceptable in a child. Pediatric pads are intended for children "
            "under 8 and must never be used on an adult. For a pregnant patient, "
            "the AED is still used normally; if a shock is delivered, move the "
            "uterus to the left or use left lateral positioning.",
            AHA_TOP_THINGS,
            [
                "Use pediatric attenuating pads if the child is under 8 years or weighs less than 25 kg.",
                "If pediatric pads are unavailable, adult pads are better than no defibrillation.",
                "In pregnancy, do not delay defibrillation for fetal monitoring.",
            ],
        ),
        _b(
            "AED readiness in the workplace",
            "AHA guidance on AED implementation covers placement, maintenance, "
            "training, and policy. Devices should be visible, accessible, checked "
            "on a documented schedule, and used by people who have been trained. "
            "The chance of survival drops with every minute of delay, so "
            "response plans should specify who fetches the AED and who calls for "
            "help.",
            AHA_AED_PROGRAM,
            [
                "Post the location of every AED in the building and check them on a documented schedule.",
                "Everyone on staff should know how to use an AED — training is minimal and broadly useful.",
                "Link the AED to the emergency response plan.",
            ],
        ),
        _b(
            "After the event",
            "After any use of an AED, the device should be retrieved, the data "
            "card or event data reviewed, the pads and battery replaced according "
            "to the manufacturer's guidance, and the event documented for "
            "quality review. The event record is also part of the patient's "
            "medical record.",
            RED_CROSS_CPR,
            [
                "Leave the device in place for EMS unless they ask you to remove it.",
                "Attach the defibrillator data card to the patient record.",
                "Report the event internally per facility policy.",
            ],
        ),
    ],
    "cpr-choking": [
        _b(
            "Recognizing a severe airway obstruction",
            "A choking person who can cough forcefully, speak, or breathe is not "
            "in severe obstruction — encourage coughing and monitor. Severe "
            "foreign-body airway obstruction is signalled by a weak or absent "
            "cough, inability to speak or make sound, change in color, altered "
            "mental status, or apnea.",
            AHA_ADULT_FBAO,
            [
                "Universal choking sign: hands clutching the throat.",
                "Partial obstruction: encourage coughing, do not intervene further.",
                "Severe obstruction: act immediately and activate the emergency response system.",
            ],
        ),
        _b(
            "Severe choking in adults and children",
            "The 2025 AHA guidelines recommend alternating 5 back blows with 5 "
            "abdominal thrusts for a conscious adult or child with severe foreign "
            "body airway obstruction, repeating until the object is expelled or "
            "the person becomes unresponsive. Chest thrusts are used instead of "
            "abdominal thrusts in late pregnancy or when the rescuer cannot "
            "encircle the abdomen.",
            AHA_ADULT_FBAO,
            [
                "Alternate 5 back blows and 5 abdominal thrusts.",
                "Use 5 chest thrusts in late pregnancy or when abdominal thrusts cannot be delivered.",
                "Do not sweep the mouth with your fingers.",
            ],
        ),
        _b(
            "Severe choking in infants",
            "For a conscious choking infant, alternate 5 back blows with 5 chest "
            "thrusts using the heel of one hand, until the object is expelled or "
            "the infant becomes unresponsive. Abdominal thrusts are not "
            "recommended for infants because of the risk of organ injury.",
            AHA_CHILD_FBAO,
            [
                "5 back blows with the heel of the hand between the shoulder blades, then 5 chest thrusts.",
                "Never use abdominal thrusts on an infant.",
                "If the infant becomes unresponsive, begin CPR.",
            ],
        ),
        _b(
            "When the person becomes unresponsive",
            "Lower the person to the floor, activate the emergency response "
            "system, and begin CPR. Before giving breaths, open the airway and "
            "remove the object only if you can see it. Do not sweep the mouth "
            "blindly, because that can push the object further in. Continue CPR "
            "and check the mouth each time the airway is opened.",
            ML_CHOKING_ADULT,
            [
                "Start CPR and look for the object in the mouth before each set of breaths.",
                "Never perform a blind finger sweep.",
                "Continue until the object is expelled and the person breathes or shows signs of life.",
            ],
        ),
        _b(
            "Choking in a conscious patient who is pregnant or obese",
            "When the abdomen cannot be encircled — late pregnancy, obesity, or "
            "the patient is unresponsive and cannot be held from behind — use "
            "chest thrusts in the same manner as for an infant, applied to the "
            "lower half of the sternum.",
            ML_CHOKING_ADULT,
            [
                "Chest thrusts are the recommended alternative when abdominal thrusts cannot be delivered.",
                "Deliver 5 chest thrusts, alternating with back blows.",
                "Continue until the obstruction clears or the patient becomes unresponsive.",
            ],
        ),
        _b(
            "After the obstruction is cleared",
            "After the object is expelled, the person should be evaluated: check "
            "for breathing, coughing, and signs of injury from the thrusts, and "
            "arrange medical evaluation, since abdominal thrusts can cause "
            "internal injury. Document the event, the maneuvers performed, and "
            "the outcome.",
            ML_CHOKING_INFANT,
            [
                "Even if the person seems well, abdominal thrusts can cause abdominal organ injury — recommend "
                "evaluation.",
                "Watch for aspiration if the person was unresponsive for any period.",
                "Document the intervention and the outcome.",
            ],
        ),
    ],
    "cpr-chain": [
        _b(
            "The six links",
            "The AHA Chain of Survival has six links: recognition of cardiac "
            "arrest and activation of the emergency response system; early CPR "
            "with an emphasis on chest compressions; rapid defibrillation; "
            "advanced resuscitation by EMS and healthcare providers; post-cardiac "
            "arrest care; and recovery. The 2025 guidelines consolidated the "
            "adult and pediatric chains into a single universal chain, with a "
            "separate newborn chain of care.",
            AHA_CHAIN,
            [
                "1. Recognition and activation of the emergency response system.",
                "2. Early CPR with an emphasis on chest compressions.",
                "3. Rapid defibrillation.",
                "4. Advanced resuscitation by EMS and healthcare providers.",
                "5. Post-cardiac arrest care.",
                "6. Recovery.",
            ],
        ),
        _b(
            "Why the chain matters",
            "Survival depends on all the links, not just the first. Each link "
            "depends on the one before it: defibrillation is useless if no one "
            "recognizes the arrest and starts CPR, and CPR alone is insufficient "
            "for a shockable rhythm. That is why public access defibrillation, "
            "bystander CPR, and rapid EMS response are all public health "
            "priorities.",
            AHA_EXECUTIVE_SUMMARY,
            [
                "Each link depends on the previous one.",
                "Bystander CPR roughly doubles to triples survival in out-of-hospital arrest.",
                "System-level measures — dispatch, data registries, quality review — determine real-world outcomes.",
            ],
        ),
        _b(
            "Recognition and activation",
            "Recognition starts with the absence of normal breathing and signs of "
            "life. Agonal gasping is not normal breathing; it is a sign of "
            "arrest. Check for a pulse for no more than 10 seconds if trained, "
            "and activate the emergency response system immediately — do not "
            "delay CPR to make the call.",
            AHA_WHAT_IS_CPR,
            [
                "Cardiac arrest is usually sudden and causes collapse, gasping, and no pulse.",
                "Activate emergency response first, then begin CPR.",
                "Send someone specific: 'You in the blue shirt, call 911 and bring the AED.'",
            ],
        ),
        _b(
            "Early CPR and rapid defibrillation",
            "Early CPR maintains coronary and cerebral perfusion, and early "
            "defibrillation is the definitive treatment for ventricular "
            "fibrillation. The public-access AED program, along with CPR in "
            "schools and workplaces, is what closes the gap between collapse and "
            "defibrillation.",
            AHA_ADULT_BLS,
            [
                "CPR maintains blood flow to the brain and heart until defibrillation arrives.",
                "Defibrillation should occur as soon as an AED is available.",
                "Every minute of delay reduces survival by 7–10%.",
            ],
        ),
        _b(
            "Advanced resuscitation and post-arrest care",
            "Advanced resuscitation by EMS and healthcare providers includes "
            "airway management, medications, defibrillation, and transport. "
            "Post-cardiac arrest care after a return of spontaneous circulation "
            "focuses on hemodynamic and respiratory support, temperature "
            "management, and transfer to a cardiac center; the 2025 guidelines "
            "recommend temperature control for at least 36 hours in adults who "
            "remain unresponsive to verbal commands.",
            AHA_EXECUTIVE_SUMMARY,
            [
                "Post-arrest care begins immediately after ROSC and continues in the intensive care unit.",
                "Temperature control is now emphasized for at least 36 hours in unresponsive adults.",
                "Transfer to a cardiac arrest center improves outcomes.",
            ],
        ),
        _b(
            "Recovery and the survivor",
            "Recovery is the newest link and the one most often neglected. "
            "Survivors and their families need rehabilitation, psychological "
            "support, and assessment for physical, cognitive, and psychosocial "
            "problems, which are common and often under-addressed.",
            AHA_TOP_THINGS,
            [
                "Psychological support for survivors and families is part of the chain, not an optional extra.",
                "Cognitive and physical deficits may be subtle and emerge over months.",
                "Rehabilitation referral and follow-up should be documented in the care plan.",
            ],
        ),
    ],
    "cpr-red-cross": [
        _b(
            "First aid basics",
            "First aid is immediate care given to an injured or ill person until "
            "professional help arrives. The priorities are always the same: "
            "ensure the scene is safe, check responsiveness, call for help, and "
            "then assess. The Red Cross teaching sequence places scene safety "
            "first because helping a patient in an unsafe environment creates a "
            "second casualty.",
            RED_CROSS_FIRST_AID,
            [
                "Scene safety, then responsiveness, then call for help — in that order.",
                "Use PPE and barrier devices when blood or body fluids are involved.",
                "Do not move a person with a suspected spinal injury unless they are in danger.",
            ],
        ),
        _b(
            "Universal first aid principles",
            "Control bleeding first — it is the most immediately life-threatening "
            "thing you can do for many patients. Then support the airway and "
            "breathing, then control any shock by laying the person down, "
            "elevating the legs if no injury prevents it, keeping them warm, and "
            "reassuring them. For most first aid, the best thing you can do is "
            "call 911 and keep the person comfortable.",
            RED_CROSS_FIRST_AID_STEPS,
            [
                "Bleeding control comes before most other interventions.",
                "Shock management: lie flat, raise the legs if safe, keep warm, and reassure.",
                "Never give food or drink to someone who may need surgery.",
            ],
        ),
        _b(
            "Bleeding and wound care",
            "For external bleeding, apply firm direct pressure with a dressing or "
            "clean cloth and hold it in place. If blood soaks through, add "
            "another layer rather than removing the first. For a life-threatening "
            "bleeding injury, a commercial tourniquet or hemostatic dressing "
            "may be appropriate if trained. Once bleeding is controlled, keep the "
            "wound clean and cover it.",
            ML_CUTS,
            [
                "Direct pressure first: firm, continuous pressure for 10 minutes or more.",
                "Add layers on top; do not remove soaked dressings.",
                "For severe limb bleeding, apply a tourniquet above the wound if trained and document the time.",
            ],
        ),
        _b(
            "First aid kit contents",
            "A well-stocked first aid kit should include gloves and other PPE, "
            "sterile gauze pads of several sizes, adhesive bandages, roller "
            "gauze, adhesive tape, scissors, tweezers, a CPR barrier mask, an "
            "instant cold pack, and any facility-specific items. MedlinePlus "
            "describes how to assemble and maintain a kit.",
            ML_FIRST_AID_KIT,
            [
                "Check expiration dates and replace used items after every use.",
                "Include a CPR barrier device and gloves — protection for the responder comes first.",
                "Keep kits accessible and check them on a documented schedule.",
            ],
        ),
        _b(
            "Heat, cold, and environmental emergencies",
            "Heat illness ranges from heat cramps and heat exhaustion to "
            "heat stroke, in which the core temperature rises above 40 °C and "
            "the person may be confused, unconscious, or seizing — that is a "
            "medical emergency requiring rapid cooling and emergency care. "
            "Hypothermia causes shivering that stops, slurred speech, and a slow "
            "pulse, and is treated with gradual, passive warming.",
            ML_HEAT_ILLNESS,
            [
                "Heat stroke: call for emergency help and begin rapid cooling immediately.",
                "Cool first, transport second — do not delay cooling while waiting for EMS.",
                "Never rub frostbitten skin or apply direct heat.",
            ],
        ),
        _b(
            "Recognizing stroke and other time-critical emergencies",
            "Use the BE-FAST or F.A.S.T. approach for stroke: Balance, Eyes, "
            "Face, Arm, Speech, Time. Sudden weakness on one side, facial "
            "droop, slurred speech, or a sudden vision loss require an "
            "immediate emergency response because treatment is time-limited. "
            "Chest pain, severe shortness of breath, and uncontrolled bleeding "
            "follow the same rule.",
            ML_HEART_ATTACK_FIRST_AID,
            [
                "FAST: Face drooping, Arm weakness, Speech difficulty, Time to call for help.",
                "Note the time symptoms started — it determines eligibility for reperfusion treatment.",
                "Do not give aspirin or food or drink unless directed by emergency services.",
            ],
        ),
    ],
    # ------------------------------------------------------------------
    # Clinical skills
    # ------------------------------------------------------------------
    "skill-injection": [
        _b(
            "Routes of administration",
            "Routes determine how fast a medication is absorbed. Intradermal is "
            "used for allergy testing and TB skin testing, producing a small "
            "raised wheal. Subcutaneous is used for insulin and some vaccines, "
            "given into the fatty tissue below the skin. Intramuscular goes into "
            "the muscle for faster absorption and larger volumes, and "
            "intravenous delivers medication directly into the circulation.",
            CDC_INJECTION_SAFETY,
            [
                "Intradermal: 15-degree angle, small volume, read at the specified time.",
                "Subcutaneous: 45–90 degree angle, into fatty tissue; use the Z-track technique.",
                "Intramuscular: 90-degree angle, into the deltoid or vastus lateralis or ventrogluteal site.",
            ],
        ),
        _b(
            "Intramuscular sites",
            "The deltoid is used for small volumes in adults; the vastus "
            "lateralis is used in infants and young children and is the "
            "preferred site for larger volumes; the ventrogluteal site is used "
            "for larger volumes in adults. Landmarks must be identified by "
            "palpation, and the needle length must be chosen for the patient's "
            "size, not by habit.",
            CDC_IMZ_BEST_PRACTICES,
            [
                "Deltoid: three finger-breadths below the acromion process.",
                "Vastus lateralis: middle third of the anterolateral thigh; the preferred site in young children.",
                "Ventrogluteal: place the heel of the hand over the greater trochanter with fingers pointing toward "
                "the hip; inject in the upper triangle.",
            ],
        ),
        _b(
            "Aseptic technique and skin preparation",
            "Hand hygiene and gloves come first, then skin antisepsis. Clean the "
            "injection site with an alcohol-based antiseptic and let it dry "
            "completely before penetrating the skin — puncturing through a wet "
            "site causes a sting and increases contamination. Use a new sterile "
            "needle and syringe for each injection and each patient.",
            CDC_HAND_HYGIENE,
            [
                "Wash or rub hands before putting on gloves; change gloves between patients.",
                "Let the antiseptic dry fully — do not fan or blot it.",
                "Use a new needle and syringe for every injection, every time.",
            ],
        ),
        _b(
            "Needle safety and disposal",
            "Activate the safety mechanism immediately after the injection, "
            "discard the device directly into a sharps container at the point of "
            "use, and never recap. If the safety device cannot be activated, "
            "follow the manufacturer's alternative disposal procedure, which "
            "still never involves recapping with your fingers.",
            OSHA_BBP_STANDARDS,
            [
                "Never recap, bend, or break a used needle.",
                "Discard at the point of use — do not leave it on a tray.",
                "Never remove a device from a sharps container.",
            ],
        ),
        _b(
            "Documentation after an injection",
            "Record the medication name, dose, route, site, date, and time, plus "
            "the lot number and expiration date for vaccines, and any patient "
            "reaction. For vaccines, record the manufacturer, lot, expiration, "
            "route, site, and the date administered in the immunization "
            "information system.",
            CDC_VACCINES_HCP,
            [
                "Document the site used — deltoid right or left — for vaccines.",
                "Record the manufacturer, lot number, and expiration date for every vaccine.",
                "Report the injection in the state immunization information system.",
            ],
        ),
        _b(
            "Adverse reactions",
            "Most injection reactions are mild, but anaphylaxis is rare and "
            "life-threatening. Watch for urticaria, wheezing, facial or throat "
            "swelling, hypotension, or collapse. If anaphylaxis occurs, activate "
            "the emergency response plan and give epinephrine immediately — "
            "antihistamines and steroids are secondary. Document the reaction, "
            "the treatment given, and the outcome.",
            ML_ANAPHYLAXIS,
            [
                "Epinephrine is the first-line treatment for anaphylaxis — do not delay it for other medications.",
                "Lie the patient flat with legs elevated unless breathing is compromised.",
                "Document the reaction and add the substance to the allergy list.",
            ],
        ),
    ],
    "skill-vitals": [
        _b(
            "Blood pressure measurement technique",
            "Accurate blood pressure measurement starts with the right cuff. The "
            "cuff bladder should cover about 80% of the upper arm circumference; "
            "a cuff that is too small falsely elevates the reading and one that "
            "is too large falsely lowers it. Have the patient rest quietly for at "
            "least five minutes, sit with back supported and feet flat, support "
            "the arm at heart level, and do not talk during the measurement.",
            CDC_HBP_MEASURE,
            [
                "Rest 5 minutes; no caffeine, exercise, or smoking for 30 minutes beforehand where practical.",
                "Use the bladder-over-artery rule: the artery marker should sit over the brachial artery.",
                "Use the bladder size written on the cuff; check it against the patient, not the machine.",
            ],
        ),
        _b(
            "Documenting and interpreting blood pressure",
            "Record the blood pressure with the position, the arm used, the cuff "
            "size, and the time. A first reading that is unexpectedly high should "
            "be repeated with the other arm. Home and ambulatory readings use "
            "different thresholds, so know the standard and ambulatory targets "
            "before counseling a patient.",
            ML_BP_MEASURE,
            [
                "Note the arm used and the position; repeat in the other arm if the first value is high.",
                "A difference of more than 10 mm Hg between arms may indicate vascular disease.",
                "Home readings are lower than office readings — use the patient's log, not the office value, for "
                "adjustments.",
            ],
        ),
        _b(
            "Pulse, respirations, and temperature",
            "The radial pulse is counted for 30 seconds and doubled when regular, "
            "or for a full minute when irregular. Normal adult respiratory rate "
            "is 12–20 per minute, and tachypnea is one of the earliest signs of "
            "deterioration. Temperature is measured orally, axillary, tympanic, "
            "or rectally depending on age and the clinical situation.",
            ML_HEALTH_TOPICS,
            [
                "Radial pulse: 60–100 bpm in adults; irregular rhythms require counting for a full minute.",
                "Respirations should be counted without telling the patient, because the rate changes when they are "
                "aware.",
                "Axillary temperature reads about 0.5 °C lower than oral; use the appropriate conversion.",
            ],
        ),
        _b(
            "Oxygen saturation and pulse oximetry",
            "Pulse oximetry estimates the percentage of oxygen-saturated "
            "hemoglobin using light absorption through a sensor placed on a "
            "perfusion-rich site. The reading can be inaccurate with poor "
            "perfusion, hypothermia, nail polish, motion, or darkly pigmented "
            "skin at the sensor site, so confirm with a co-oximetry or arterial "
            "blood gas when the reading does not fit the clinical picture.",
            ML_VITAL_SIGNS,
            [
                "Normal saturation at sea level is typically 95–100%.",
                "Nail polish, motion, and poor perfusion produce false readings.",
                "Check the perfusion index and waveform when the reading looks implausible.",
            ],
        ),
        _b(
            "Pediatric vital signs",
            "Pediatric normal ranges vary by age, so always compare with an "
            "age-specific chart. Neonates breathe faster, have a faster resting "
            "heart rate, and have a wider normal blood pressure range. Weight "
            "is essential for all calculations, so measure and document it at "
            "every visit.",
            CDC_CHILD_DEV,
            [
                "Infants: respiratory rate 30–60/min; heart rate 100–160/min.",
                "Children: respiratory rate 20–30/min; heart rate 80–130/min.",
                "Weight is needed for every weight-based medication calculation.",
            ],
        ),
        _b(
            "Older adult vital signs",
            "Normal aging changes blood pressure, pulse, respiratory rate, and "
            "temperature perception. A slight rise in systolic pressure, a "
            "slightly lower resting heart rate, and reduced respiratory reserve "
            "are expected. Fever may be blunted, so a change in mental status or "
            "function in an older adult is a more reliable sign of infection than "
            "a normal temperature.",
            ML_AGING_VITALS,
            [
                "Older adults may not feel fever — investigate a change in function.",
                "Reduced baroreceptor sensitivity increases orthostatic hypotension risk; check lying, sitting, and "
                "standing pressures.",
                "Reduced renal and hepatic clearance alters drug dosing.",
            ],
        ),
    ],
    "skill-infection": [
        _b(
            "Hand hygiene: the single most important measure",
            "The CDC hand hygiene guideline is the reference for healthcare "
            "settings and remains the core of infection prevention. Alcohol-based "
            "hand rub is preferred for routine use when hands are not visibly "
            "soiled; soap and water are required after caring for a patient with "
            "norovirus or C. difficile and before and after handling food. The "
            "technique matters: friction over all hand surfaces for the full "
            "duration.",
            CDC_HAND_HYGIENE,
            [
                "Alcohol-based rub: 20–30 seconds; soap and water: at least 20 seconds.",
                "Rub all surfaces: palms, backs of hands, between fingers, fingertips, thumbs, and under the nails.",
                "Do not wipe the antiseptic off early.",
            ],
        ),
        _b(
            "The five moments for hand hygiene",
            "The CDC guideline defines moments for hand hygiene: before touching "
            "a patient, before any clean or aseptic procedure, after body fluid "
            "exposure risk, after touching a patient, and after touching patient "
            "surroundings. Gloves do not remove the need for hand hygiene at any "
            "of these points.",
            CDC_INFECTION_CONTROL,
            [
                "Before patient contact — protects the patient from your hands.",
                "Before clean/aseptic procedures — protects the sterile field.",
                "After body fluid exposure risk — protects you and the next patient.",
            ],
        ),
        _b(
            "Personal protective equipment",
            "PPE is the last line of defense. Gloves, gowns, masks, eye "
            "protection, and respirators are selected based on the anticipated "
            "exposure: contact, droplet, or airborne. Put PPE on before "
            "approaching the patient and remove it before leaving the room, then "
            "perform hand hygiene immediately.",
            CDC_NIOSH_PPE,
            [
                "Sequence for donning: gown, mask/respirator, eye protection, gloves.",
                "Sequence for doffing: gloves, eye protection, gown, mask/respirator — then hand hygiene.",
                "Remove PPE without touching the contaminated outer surface.",
            ],
        ),
        _b(
            "Aseptic versus clean technique",
            "Clean technique is used for procedures that contact intact skin, such "
            "as routine dressing changes, while aseptic technique is used for any "
            "procedure that enters sterile tissue or the vascular system — "
            "injections, wound debridement, catheter insertion. Aseptic technique "
            "requires sterile gloves, a sterile field, and no contamination at "
            "any point.",
            CDC_INJECTION_SAFETY,
            [
                "Aseptic technique: sterile gloves, sterile field, sterile supplies, and a maintained sterile field.",
                "Keep the sterile field in view and treat anything out of view as contaminated.",
                "Clean technique still requires hand hygiene and standard precautions.",
            ],
        ),
        _b(
            "Disinfection, sterilization, and the Spaulding classification",
            "Critical items that enter sterile tissue or the vascular system must "
            "be sterilized; semi-critical items that contact mucous membranes must "
            "be disinfected at minimum; non-critical items that contact intact "
            "skin need only cleaning between patients. Reprocessing requires "
            "cleaning first, then disinfection or sterilization, using the "
            "manufacturer's instructions and verifying effectiveness with "
            "monitoring and testing.",
            CDC_INFECTION_CONTROL,
            [
                "Critical: sterile — needles, catheters, implants.",
                "Semi-critical: disinfected at minimum — endoscopes, respiratory equipment.",
                "Non-critical: cleaned — blood pressure cuffs, stethoscopes, bed rails.",
            ],
        ),
        _b(
            "Safe injection practice as infection prevention",
            "Unsafe injection practice is one of the largest preventable sources "
            "of bloodborne pathogen transmission in healthcare globally. CDC's "
            "rules are absolute: a new needle and a new syringe for every "
            "injection, one time only, and safe disposal immediately after use. "
            "Reusing syringes or needles on a single patient still transmits "
            "infection.",
            CDC_INJECTION_SAFETY,
            [
                "Never reuse a syringe or needle on the same patient for a second injection.",
                "Use a new sterile needle and syringe for each entry into a vial.",
                "Discard immediately into a sharps container.",
            ],
        ),
    ],
    "skill-terminology": [
        _b(
            "Building terms from parts",
            "Most medical terms are built from a prefix, a root, and a suffix. "
            "Decomposing a term is far more reliable than memorizing it: "
            "cyan/o (blue) + -osis (condition) gives cyanosis; hyper- (excessive) "
            "+ tens (pressure) + -ion gives hypertension. Recognizing the parts "
            "lets you interpret an unfamiliar term on an exam.",
            ML_ENCYCLOPEDIA,
            [
                "Roots: cardi (heart), myo (muscle), osteo (bone), patho (disease), gastro (stomach), entero "
                "(intestine), nephro (kidney), hemo/hema (blood), derm/o (skin), neuro (nerve).",
                "Suffixes: -itis (inflammation), -osis (abnormal condition), -emia (in the blood), -megaly "
                "(enlargement), -pathy (disease), -algia (pain), -penia (deficiency).",
                "Prefixes: a-/an- (without), dys- (painful/difficult), hyper-/hypo- (excessive/deficient), "
                "tachy-/brady- (fast/slow), bi-/uni- (two/one).",
            ],
        ),
        _b(
            "Abbreviations and symbols",
            "Medical abbreviations are used constantly on orders, charts, and "
            "lab requisitions. Learn the common ones and, more importantly, learn "
            "the dangerous ones that must never be written on an order because "
            "they can be misread — for example U for units, IU for international "
            "units, and QD or QOD for daily or every other day.",
            NHA_CCMA,
            [
                "Never abbreviate 'units' as a bare U — write 'unit'.",
                "Write 'once daily' rather than QD, and 'every other day' rather than QOD.",
                "Use only facility-approved abbreviations; check the list before charting.",
            ],
        ),
        _b(
            "Body systems and directional terminology",
            "Knowing the major body systems and the vocabulary used to describe "
            "location, position, and planes of section is the foundation for "
            "charting and for communicating about injuries and findings. Terms "
            "such as distal, proximal, superior, and inferior appear in "
            "documentation, in patient instructions, and in examination questions.",
            ML_HEALTH_TOPICS,
            [
                "Directional terms: superior/inferior, anterior/posterior, medial/lateral, proximal/distal, "
                "superficial/deep.",
                "Planes: sagittal (left/right), coronal (front/back), transverse (top/bottom).",
                "Body systems: integumentary, skeletal, muscular, nervous, endocrine, cardiovascular, lymphatic, "
                "respiratory, digestive, urinary, reproductive.",
            ],
        ),
        _b(
            "Symptoms, signs, and syndromes",
            "A symptom is something the patient reports (pain, dizziness); a "
            "sign is something the clinician observes or measures (fever, "
            "tachypnea, edema); a syndrome is a recognizable pattern of signs and "
            "symptoms. Distinguishing them matters in charting and in assessment: "
            "record what the patient says as a symptom and what you observed as a "
            "sign.",
            ML_HEALTH_TOPICS,
            [
                "Symptom: subjective — 'my chest feels tight'.",
                "Sign: objective — respiratory rate 24/min, temperature 38.9 °C.",
                "Never upgrade a patient's report into a clinical interpretation in the chart.",
            ],
        ),
        _b(
            "Medical specialties and the referral network",
            "Knowing which specialty handles which problem supports appropriate "
            "referrals and patient education. Nurse practitioners and physician "
            "assistants provide primary care, internists manage adult medical "
            "problems, pediatricians treat children, and specialists concentrate "
            "on a single organ system or condition.",
            ML_HEALTH_TOPICS,
            [
                "Primary care: family medicine, internal medicine, pediatrics, nurse practitioner and physician "
                "assistant practice.",
                "Specialties: cardiology, pulmonology, gastroenterology, nephrology, endocrinology, orthopedics, "
                "dermatology.",
                "Allied health: nursing, medical assisting, phlebotomy, laboratory science, radiography.",
            ],
        ),
        _b(
            "Using terminology accurately with patients",
            "Clinical terminology is for the chart; plain language is for the "
            "patient. Saying 'you have hypertension' means little to many "
            "patients, while 'your blood pressure is high — that puts strain on "
            "your heart and kidneys' is understandable and actionable. Avoid "
            "jargon in teaching, and check understanding with teach-back.",
            AHRQ_HEALTH_LITERACY,
            [
                "Translate the term into what the patient will notice and do.",
                "Use teach-back to confirm the patient understood the explanation.",
                "Written instructions should be at a plain-language reading level.",
            ],
        ),
    ],
    "skill-pharm-dosage": [
        _b(
            "The rights of medication administration",
            "Before administering any medication, verify the right patient, the "
            "right drug, the right dose, the right route, and the right time. "
            "Many facilities add the right documentation, the right to refuse, "
            "and the right of the patient to be informed. The check is repeated "
            "at three points: when the order is received, when the medication is "
            "prepared, and when it is administered.",
            FDA_MEDICATION_SAFETY,
            [
                "Right patient, right drug, right dose, right route, right time.",
                "Verify allergies every time — an allergy list is not static.",
                "Never administer a medication whose order is unclear; clarify it first.",
            ],
        ),
        _b(
            "Reading a medication order",
            "Prescriptions and medication orders contain specific elements: the "
            "patient, the date and time, the medication and strength, the dose, "
            "the route, the frequency, the indication, and the prescriber's "
            "signature. You must be able to read the order accurately and notice "
            "discrepancies such as an illegible dose, a missing route, or a "
            "frequency that does not match the drug.",
            FDA_DRUG_SAFETY,
            [
                "Check the order for patient, drug, strength, dose, route, frequency, and indication.",
                "Distinguish a stat dose from a scheduled dose.",
                "When an order is incomplete or ambiguous, clarify it with the prescriber and document the "
                "clarification.",
            ],
        ),
        _b(
            "Dosage calculation essentials",
            "Dosage calculations require converting units so that the numerator "
            "and denominator match before you calculate. Know the equivalences "
            "for the metric system (1 g = 1000 mg, 1 kg = 1000 g, 1 mL = 1 cc), "
            "household measurements (1 tablespoon = 3 teaspoons = 15 mL), and "
            "fractions (½ = 0.5, ⅓ = 0.33). Dimensional analysis cancels units "
            "and is the safest method.",
            NHA_CCMA,
            [
                "Set up the problem so the units cancel: (ordered dose / stock dose) × stock volume = volume to "
                "administer.",
                "Convert everything to one system before calculating.",
                "Have a second person verify pediatric and high-alert calculations.",
            ],
        ),
        _b(
            "Weight-based and pediatric dosing",
            "Pediatric and some adult medications are dosed by weight in "
            "milligrams per kilogram per day, divided into divided doses. "
            "Confirm the weight in kilograms at the time of administration "
            "rather than relying on a charted weight, and be aware that dosing "
            "recommendations are often based on ideal body weight rather than "
            "actual weight.",
            CDC_CHILD_DEV,
            [
                "Convert pounds to kilograms by dividing by 2.2.",
                "Verify the dose against the child's most recent weight, not a remembered weight.",
                "Never round a calculated dose up; round down when the maximum dose would be exceeded.",
            ],
        ),
        _b(
            "High-alert medications",
            "High-alert medications have a heightened risk of causing harm when "
            "used in error and require additional safeguards. Insulin, "
            "anticoagulants, concentrated electrolytes, opioid analgesics, "
            "chemotherapy agents, and neuromuscular blocking agents are "
            "commonly classified as high-alert. Independent double-checks, "
            "standard concentrations, and independent double-checks of the "
            "label are typical controls.",
            FDA_MEDICATION_SAFETY,
            [
                "Perform an independent double-check for high-alert medications before administration.",
                "Look-alike/sound-alike names are a common cause of error — read the full label.",
                "Never leave a high-alert medication unattended at the bedside.",
            ],
        ),
        _b(
            "Preventing medication errors",
            "Common error mechanisms include look-alike packaging, illegible "
            "orders, decimal-point mistakes, wrong-unit errors, and interruptions "
            "during calculation. Control them with a quiet, undistracted "
            "workspace, standardized storage with separation of similar "
            "products, and a culture that encourages reporting near misses "
            "without blame.",
            ML_MEDICATION_ERRORS,
            [
                "Avoid trailing zeroes and leading decimals (write 0.5 mg, not .5 mg; write 5 mg, not 5.0 mg).",
                "Interruptions during calculation are a leading cause of error — move to a quiet area.",
                "Report and document every medication error, including near misses, per policy.",
            ],
        ),
    ],
    "skill-specimen-lab": [
        _b(
            "Types of specimens",
            "Laboratory specimens include blood, urine, stool, sputum, throat "
            "swabs, wound cultures, and body fluids. Each has collection "
            "requirements that determine whether the result is valid: clean "
            "catch midstream urine, a timed urine collection, a fasting blood "
            "draw, or a throat swab taken before antibiotics. The order and the "
            "collection instructions come from the laboratory's test directory.",
            ML_LAB_TESTS,
            [
                "Follow the specific collection instructions in the laboratory manual for each test.",
                "Clean-catch midstream urine is the standard for urinalysis and culture.",
                "Document the collection time, especially for timed and therapeutic monitoring tests.",
            ],
        ),
        _b(
            "Patient preparation",
            "Preparation determines the accuracy of the result. Fasting, "
            "medication holds, recent exercise, and recent transfusion all "
            "affect results. When a preparation requirement is not met, contact "
            "the ordering clinician rather than collecting a specimen that will "
            "have to be discarded.",
            ML_OGTT,
            [
                "Fasting specimens: no calories for 8–12 hours; water is usually permitted.",
                "Some tests require withholding certain medications — clarify with the prescriber.",
                "Recent exercise, smoking, and stress can alter glucose and other values.",
            ],
        ),
        _b(
            "Labeling and chain of identification",
            "Every specimen is labeled at the bedside in the patient's presence "
            "with at least two identifiers, the collection date and time, and "
            "the collector. Pre-labeled tubes must never be carried into the "
            "patient room. An unlabeled or mislabeled specimen cannot be "
            "identified and must be recollected.",
            ML_VENIPUNCTURE,
            [
                "Two identifiers plus the date, time, and collector.",
                "Label in the patient's presence, before leaving the bedside.",
                "Never pre-label tubes at the workstation.",
            ],
        ),
        _b(
            "Handling and transport",
            "Specimens are transported promptly in a sealed biohazard bag inside "
            "a rigid carrier, protected from light, heat, and freezing. "
            "Time-to-lab is critical: many analytes change with delay, and "
            "specimens that require refrigeration or immediate delivery must be "
            "handled according to the test directory.",
            ML_LAB_TESTS,
            [
                "Deliver promptly; many tests have stability limits measured in hours.",
                "Refrigerate or protect from light only when the test directory requires it.",
                "Hand-carry specimens that must not be delayed, and document the hand-off.",
            ],
        ),
        _b(
            "Point-of-care testing and quality control",
            "Point-of-care testing performed in the office is usually CLIA-waived "
            "or moderate-complexity. Either way, the operator must follow the "
            "manufacturer's instructions, run controls on the required schedule, "
            "keep records of testing, and have a plan for reporting results, "
            "including critical values.",
            FDA_CLIA,
            [
                "Follow the manufacturer's instructions exactly — the basis of the waived status.",
                "Run controls with each new lot, when results are unexpected, and on the required schedule.",
                "Keep a log of all control results, patient results, and corrective actions.",
            ],
        ),
        _b(
            "Understanding results and critical values",
            "Knowing the reference ranges for the tests you perform helps you "
            "recognize an outlier and escalate it. Critical values — results "
            "that require immediate action — have facility-defined limits and "
            "must be reported to the ordering clinician as soon as they are "
            "identified, with the callback documented.",
            ECFR_CLIA,
            [
                "Critical values require immediate notification and documented read-back.",
                "Recheck the specimen when a result is implausible before escalating.",
                "Never report a critical value verbally without documenting the recipient and time.",
            ],
        ),
    ],
    "skill-intake": [
        _b(
            "Patient registration and demographics",
            "Registration sets the foundation for everything that follows. Verify "
            "the patient's full legal name, date of birth, address, phone, "
            "emergency contact, and insurance information, and confirm that the "
            "demographics on the chart match the patient in front of you. "
            "Corrections to demographics are common and should be made at every "
            "visit.",
            ML_HEALTH_TOPICS,
            [
                "Confirm two identifiers before any clinical interaction.",
                "Update address, phone, and insurance at every visit.",
                "Ask how the patient wishes to be addressed and record their preferred name.",
            ],
        ),
        _b(
            "The patient interview",
            "A structured interview covers the chief complaint, the history of "
            "the present illness, past medical and surgical history, "
            "medications, allergies, family history, and social history. Ask open "
            "questions, then targeted ones, and record the patient's own words "
            "for the chief complaint. Confirm allergy details specifically — "
            "including the reaction — rather than accepting a list of names.",
            ML_PATIENT_RIGHTS,
            [
                "Document the chief complaint in the patient's own words, with the date of onset.",
                "For each allergy, record the substance and what reaction occurred.",
                "Complete the medication reconciliation: prescription, over-the-counter, and supplements.",
            ],
        ),
        _b(
            "Vital signs and the physical check",
            "Record vital signs at every visit, including height, weight, and "
            "BMI where the clinic does so. Compare against the previous values "
            "and note any meaningful change. Perform the screening the clinic "
            "requires — fall risk, pain scale, depression screening, and "
            "frailty — and document the score.",
            CDC_HBP_MEASURE,
            [
                "Compare every reading with the previous visit and escalate significant change.",
                "Weight is needed for medication calculations and for monitoring fluid status.",
                "Document pain score, location, character, and what relieves it.",
            ],
        ),
        _b(
            "Consent forms and patient rights",
            "Consent documents should state what the visit involves, who will "
            "receive information, financial responsibility, and the patient's "
            "rights. Provide the notice of privacy practices, and confirm the "
            "patient has had the chance to ask questions. Signature on a form is "
            "not a substitute for an actual consent conversation.",
            HHS_HIPAA_COVERED,
            [
                "Provide the notice of privacy practices at registration.",
                "Consent for treatment, for the financial agreement, and for information sharing are separate "
                "decisions.",
                "Document the questions the patient asked and the answers given.",
            ],
        ),
        _b(
            "Insurance, identification, and financial screening",
            "Collect the insurance card, photo identification, and any referral "
            "authorization, and verify eligibility before the patient is seen. "
            "Collect the copayment and give a receipt. If the patient cannot pay, "
            "refer them to financial counseling or a social worker rather than "
            "delaying or refusing care.",
            ML_HEALTH_INSURANCE,
            [
                "Copy the insurance card and check the member identification number carefully.",
                "Confirm referral or prior-authorization requirements before the visit.",
                "Offer financial assistance resources and document the referral.",
            ],
        ),
        _b(
            "Closing the intake",
            "Before the clinician arrives, confirm the reason for the visit is "
            "correctly captured, all screening paperwork is complete, and "
            "safety needs — mobility, hearing, language, and allergies — are "
            "communicated to the care team. A brief, structured handoff prevents "
            "the most common intake errors.",
            AHRQ_TEAMSTEPPS,
            [
                "Confirm the reason for the visit and the priority of the problem.",
                "Flag safety issues and allergies at the handoff.",
                "Use a consistent structure: situation, background, assessment, recommendation.",
            ],
        ),
    ],
    "skill-osha-bbp": [
        _b(
            "Scope of the bloodborne pathogens standard",
            "29 CFR 1910.1030 applies to all occupations where there is "
            "reasonable expectation of exposure to blood or other potentially "
            "infectious materials. It covers blood, semen and vaginal secretions, "
            "saliva, and any body fluid containing visible blood, as well as "
            "potentially infectious materials such as cultures and tissue.",
            OSHA_BBP_GENERAL,
            [
                "The standard applies to employees, not to patients; it is about occupational exposure.",
                "Potentially infectious materials include cultures, tissue, and contaminated equipment.",
                "Determine applicability by documenting your reasonably anticipated exposure.",
            ],
        ),
        _b(
            "The exposure control plan",
            "Each covered employer must have a written exposure control plan "
            "reviewed and updated at least annually and whenever new tasks or "
            "procedures change occupational exposure. It identifies tasks with "
            "potential exposure, specifies controls, and documents the hepatitis "
            "B vaccination program, post-exposure evaluation, and training.",
            OSHA_BBP_RESOURCES,
            [
                "Review the plan at least annually and after every exposure incident.",
                "Make the plan accessible to all employees.",
                "Document job classifications and tasks with occupational exposure.",
            ],
        ),
        _b(
            "Engineering and work practice controls",
            "Engineering controls come first: safety-engineered needle devices, "
            "needleless systems, sharps containers, and self-sheathing needles. "
            "Work practice controls include prohibiting recapping, using "
            "appropriate handwashing facilities, and rotating employees to areas "
            "with lower risk where feasible. Personal protective equipment is "
            "the last layer.",
            OSHA_BBP_HAZARDS,
            [
                "Use the safer device whenever one is available — this is the primary control.",
                "Prohibit recapping, bending, and manual removal of needles.",
                "Prohibit eating, drinking, smoking, and applying cosmetics in areas where exposure is reasonably "
                "anticipated.",
            ],
        ),
        _b(
            "Personal protective equipment",
            "PPE is required when exposure to blood or other potentially "
            "infectious materials is anticipated: gloves, gowns, masks, and eye "
            "protection as appropriate, at no cost to the employee. Gloves must "
            "be changed between tasks and patients, and must not be worn "
            "outside the work area where contamination is likely.",
            OSHA_PPE,
            [
                "Provide PPE at no cost to the employee.",
                "Change gloves whenever contaminated or between patients.",
                "Remove PPE before leaving the work area and wash hands immediately.",
            ],
        ),
        _b(
            "Hepatitis B vaccination and post-exposure follow-up",
            "The employer must offer hepatitis B vaccination series at no cost "
            "within 10 working days of initial assignment for covered employees, "
            "or after an exposure incident if the employee has not been "
            "vaccinated. Following an exposure, the employee must receive a "
            "medical evaluation and follow-up, and the evaluation must be "
            "confidential.",
            OSHA_BBP_STANDARDS,
            [
                "Vaccination must be offered, not merely available, and at no cost.",
                "Post-exposure evaluation includes source-patient testing and employee serology.",
                "The employee's medical evaluation and follow-up are confidential.",
            ],
        ),
        _b(
            "Training and recordkeeping",
            "OSHA requires annual training in bloodborne pathogens for all "
            "covered employees, covering the standard, exposure risks, "
            "prevention, and the reporting procedure. Records of training, "
            "exposures, and medical evaluations must be kept for the duration of "
            "employment plus the required retention period.",
            OSHA_BBP_RESOURCES,
            [
                "Annual training is required, and retraining is required after an exposure incident.",
                "Training must be documented with the employee's name, date, and content covered.",
                "Sharps injury logs must be maintained and reviewed for prevention opportunities.",
            ],
        ),
    ],
    "skill-med-safety": [
        _b(
            "The rights of administration in practice",
            "Medication errors cluster around a small number of predictable "
            "failures: wrong patient, wrong drug, wrong dose, wrong route, wrong "
            "time, and missed documentation. Each of the rights is a specific "
            "check performed deliberately, not a step skipped because the "
            "medication 'looks right'.",
            FDA_MEDICATION_SAFETY,
            [
                "Right patient — verify with two identifiers, every time.",
                "Right drug, dose, route, and time — read the label, do not identify by appearance.",
                "Right documentation — record the administration in the MAR.",
            ],
        ),
        _b(
            "Three checks before administration",
            "Perform the safety check at three distinct points: when the order "
            "is received or picked up, when the medication is prepared, and at "
            "the patient's bedside immediately before administration. The final "
            "check at the bedside is the last chance to catch an error and it "
            "must always include patient identification.",
            FDA_DRUG_SAFETY,
            [
                "Check 1: at the start of the medication pass or when the order is reviewed.",
                "Check 2: when the medication is prepared and measured.",
                "Check 3: at the bedside with the patient, before administration.",
            ],
        ),
        _b(
            "High-alert medications and independent double-checks",
            "Insulin, anticoagulants, concentrated electrolytes, opioids, "
            "chemotherapy, and neuromuscular blockers carry a heightened risk of "
            "harm if used in error. Independent double-checks by a second "
            "qualified person, standardized concentrations, and storage away "
            "from look-alike products are the core controls.",
            ML_MEDICATION_ERRORS,
            [
                "Independent double-check means a second person verifies the order, the label, and the dose "
                "calculation.",
                "Store concentrated electrolytes separately from IV fluids.",
                "Separate look-alike products and apply auxiliary warning labels.",
            ],
        ),
        _b(
            "Preventing look-alike and sound-alike errors",
            "Many medication errors involve names that look or sound similar — "
            "for example, two products with similar names or strengths, or "
            "durations of action such as immediate, extended, and sustained "
            "release. Read the full label including the strength and the "
            "release type, and never identify a medication by the color of the "
            "container or the tablet.",
            FDA_MEDICATION_SAFETY,
            [
                "Read the entire label: name, strength, route, and formulation.",
                "Never identify a medication by appearance alone.",
                "Ask for the medication's complete name and indication if the order is ambiguous.",
            ],
        ),
        _b(
            "Monitoring and documentation",
            "Administration is not the end of the task. Know what effect the "
            "medication is expected to have, what adverse effects to watch for, "
            "and when to recheck a vital sign — for example, a pulse after a "
            "beta blocker or a blood pressure after an antihypertensive. "
            "Document the medication, dose, route, site, time, the patient's "
            "response, and any adverse effect.",
            FDA_MEDICATION_SAFETY,
            [
                "Document the site of administration for injections and the site of IV access.",
                "Document the patient's response, including any adverse effect.",
                "Recheck and document vital signs when the medication requires it.",
            ],
        ),
        _b(
            "Reporting errors and near misses",
            "When an error occurs, the patient is assessed first, the error is "
            "reported immediately, and the facts are documented factually. "
            "Reporting near misses is how the system is improved — the goal is "
            "prevention, not blame. Patients have the right to be told what "
            "happened and what is being done about it.",
            FDA_MEDWATCH,
            [
                "Assess and stabilize the patient first, then report.",
                "Document the facts only — what was ordered, what was given, and when.",
                "Report adverse drug reactions and product problems through MedWatch.",
            ],
        ),
    ],
    "skill-poct": [
        _b(
            "What CLIA waived means",
            "CLIA categorizes testing by complexity: waived, moderate complexity, "
            "high complexity, and moderate or high complexity plus. A waived test "
            "is one that the FDA has cleared for home use or that meets the "
            "statutory criteria for being simple and unlikely to pose a risk of "
            "harm to the patient. The test may be performed outside a certified "
            "laboratory, but the manufacturer instructions are the legal "
            "requirement.",
            FDA_CLIA,
            [
                "Waived status applies to the specific test system, not to every test from that manufacturer.",
                "Using a waived test differently from the instructions removes its waived status.",
                "42 CFR 493 lists the criteria and the waived analytes.",
            ],
        ),
        _b(
            "Quality control for waived tests",
            "For waived testing, follow the manufacturer's instructions for "
            "quality control. Most glucose meter systems require running liquid "
            "control solution with each new box of strips, when a result is "
            "unexpected, and at a defined interval. External proficiency "
            "testing may also be required by the facility or state.",
            FDA_CLIA_WAIVED,
            [
                "Run controls with each new lot of strips and on the manufacturer's schedule.",
                "Repeat the patient test with a new strip and a control if the result is unexpected.",
                "Document all control results and any corrective action.",
            ],
        ),
        _b(
            "Operator training and competency",
            "Although CLIA does not require specific training for waived tests, "
            "the operator must be trained and competent. Competency is usually "
            "demonstrated through observation of routine testing, monitoring of "
            "control results, and periodic re-evaluation including a test of "
            "knowledge and a test of competency.",
            FDA_CLIA,
            [
                "Maintain records of operator training and competency assessment.",
                "Reassess competency periodically and after any change in the test system or procedure.",
                "Include the correct interpretation of control results in training.",
            ],
        ),
        _b(
            "Performing the test and interpreting the result",
            "Follow the manufacturer's instructions exactly, including sample "
            "volume, timing, and the display of results. Many systems require a "
            "specific coding check on the test strip or the meter. Verify patient "
            "identification, and confirm that the result is plausible in the "
            "clinical context before acting on it.",
            ML_A1C,
            [
                "Check the code on the strip or meter against the display before testing.",
                "Use the correct sample type and volume — fingerstick whole blood for most meters.",
                "Repeat an implausible result before escalating or treating.",
            ],
        ),
        _b(
            "Reporting results and critical values",
            "Point-of-care results become part of the medical record, and "
            "critical values must be reported to the ordering clinician promptly, "
            "with read-back and documentation of who was notified and when. "
            "Critical limits are defined by the facility and include the "
            "extremes that require immediate clinical intervention.",
            ECFR_CLIA,
            [
                "Critical limits are set by the laboratory director and by facility policy.",
                "Report critical results immediately; do not leave them for the next shift.",
                "Document the notification, the read-back, and the response.",
            ],
        ),
        _b(
            "Troubleshooting and common errors",
            "Common point-of-care errors include expired strips, improper "
            "storage of strips, insufficient or excessive blood, failure to wash "
            "and dry hands before a fingerstick, and failure to clean the site. "
            "Each of these produces a recognizable pattern — for example, "
            "inadequate sample volume reads low, and excess sample diluted by "
            "tissue fluid reads falsely low.",
            ML_HAND_HYGIENE,
            [
                "Wash and dry hands before every fingerstick — alcohol and food residues interfere with some assays.",
                "Store strips as the manufacturer specifies; heat and humidity degrade them.",
                "Use a new single-use lancet for every patient.",
            ],
        ),
    ],
    "skill-wound-care": [
        _b(
            "Classifying a wound",
            "Wounds are described by cause, contamination, and tissue involved. "
            "Clean wounds involve the skin and subcutaneous tissue, contusions "
            "are bruising without a break in the skin, and lacerations, "
            "incisions, punctures, and abrasions have different characteristics. "
            "Staging pressure injuries uses the visible tissue layers and is "
            "assigned by the deepest affected layer, and unstageable injuries "
            "are documented as such.",
            ML_CUTS,
            [
                "Describe the wound: type, length, width, depth, location, and edges.",
                "Pressure injury stages describe the deepest affected tissue; do not downgrade a wound.",
                "Note undermining, tunneling, and exudate separately.",
            ],
        ),
        _b(
            "Cleaning and irrigation",
            "Wound cleaning means removing debris with a saline solution or tap "
            "water; antiseptics such as hydrogen peroxide and alcohol are "
            "cytotoxic and should not be used in an open wound. Irrigate with "
            "sterile saline at low pressure using a bulb syringe, or with a "
            "commercial pressurized device. The old practice of pouring peroxide "
            "or iodine into a wound damages tissue and delays healing.",
            ML_BURNS,
            [
                "Use saline or tap water for routine cleansing; avoid hydrogen peroxide in open wounds.",
                "Irrigate at low pressure to avoid damaging granulation tissue.",
                "Remove visible debris with forceps and sterile gauze.",
            ],
        ),
        _b(
            "Choosing a dressing",
            "Dressings are selected to maintain moisture, absorb exudate, "
            "provide a barrier to microorganisms, and protect the wound while it "
            "heals. Alginate dressings absorb heavily and are used for moderate "
            "to heavy exudate; foam dressings absorb moderate exudate and "
            "provide cushioning; hydrocolloids and hydrogels maintain a moist "
            "environment for lighter wounds; gauze is used when the wound needs "
            "frequent inspection or when packing is required.",
            ML_CUTS,
            [
                "Match the dressing to the amount of exudate and the depth of the wound.",
                "Moist wound healing requires a moist surface and a dry periwound — protect the surrounding skin.",
                "Change dressings at the interval specified by the order or the wound protocol.",
            ],
        ),
        _b(
            "Aseptic technique versus clean technique",
            "Clean technique uses clean gloves and clean supplies for routine "
            "wound care on a wound that is not entering sterile tissue, such as "
            "a healing surgical incision. Aseptic technique with sterile gloves, "
            "sterile instruments, and a sterile field is required for any wound "
            "with deep tissue involvement, a fresh burn, or a procedure that "
            "opens a closed system.",
            CDC_INFECTION_CONTROL,
            [
                "Aseptic for deep wounds, fresh burns, and anything entering sterile tissue.",
                "Clean technique for superficial wounds and dressing changes on closed incisions.",
                "Perform hand hygiene before either, and between patients.",
            ],
        ),
        _b(
            "Burns and thermal injuries",
            "Burn depth is described as superficial (epidermal, red and painful, "
            "heals without scarring), partial-thickness (blanching or non-blanching "
            "with blistering), or full-thickness (leathery, white, brown, or "
            "charred and insensate). Cool running water for 20 minutes is the "
            "first aid for a thermal burn; do not apply ice, butter, or creams, "
            "and do not break blisters.",
            ML_BURNS_TOPIC,
            [
                "First aid: cool the burn under cool running water for 20 minutes.",
                "Do not use ice, which can worsen tissue damage.",
                "Remove jewelry and constrictive clothing unless stuck to the burn.",
            ],
        ),
        _b(
            "Monitoring for infection and documentation",
            "Watch for the classic signs of wound infection: increasing pain, "
            "warmth, redness spreading beyond the wound edges, swelling, purulent "
            "drainage, and fever. Document each dressing change with the date, "
            "time, the type and amount of dressing used, the wound description, "
            "and the patient's response. Documentation of wound appearance over "
            "time is what demonstrates healing or deterioration.",
            ML_SEPSIS,
            [
                "Increasing pain, spreading erythema, purulent drainage, and fever suggest infection — escalate.",
                "Document wound measurements at every dressing change using the same method.",
                "Report a wound that is not improving within the expected timeframe.",
            ],
        ),
    ],
    "skill-life-stages": [
        _b(
            "Pediatric growth and development",
            "Development proceeds predictably: gross motor, fine motor, "
            "language, and social milestones are reached in a predictable "
            "sequence. Recognizing that a child is meeting, or not meeting, "
            "expected milestones supports accurate assessment and gives parents "
            "reassurance. Growth is measured with weight, length or height, head "
            "circumference, and plotted on a growth chart over time.",
            CDC_CHILD_DEV,
            [
                "Track growth on a percentile chart — the trend over time matters more than a single value.",
                "Developmental screening is recommended at 9, 18, and 30 months, and at other ages per the schedule.",
                "Immunization status should be reviewed at every visit.",
            ],
        ),
        _b(
            "Pediatric vital signs and dosing",
            "Pediatric vital signs differ from adult values and vary by age, so "
            "always use an age-specific chart. Weight is the basis for nearly "
            "all pediatric medication dosing and must be measured at each visit "
            "rather than estimated. Pediatric equipment — cuffs, needles, "
            "resuscitation equipment — must be sized correctly.",
            CDC_CHILD_DEV,
            [
                "Measure and record weight at every visit; never estimate it from appearance.",
                "Use weight in kilograms for all medication calculations.",
                "A pediatric blood pressure cuff is correctly sized when the bladder covers about 80% of the arm.",
            ],
        ),
        _b(
            "Communication with children and parents",
            "Communication with a child is age-appropriate and directed partly "
            "through the caregiver: keep explanations simple and honest, use "
            "distraction and comfort holds, and praise cooperation. With "
            "adolescents, speak directly to the adolescent as well as the "
            "parent, and respect confidentiality within legal limits, which "
            "should be explained to both parties at the start of the visit.",
            ML_TEEN_HEALTH,
            [
                "Explain honestly what will happen; surprises damage trust.",
                "Adolescents should be interviewed alone for part of the visit, with confidentiality explained.",
                "Involve the caregiver in education and consent appropriately.",
            ],
        ),
        _b(
            "Normal aging changes",
            "Normal aging involves predictable changes to vital signs, the "
            "cardiovascular system, the immune system, and the senses. "
            "Presbyopia, reduced hearing, reduced renal clearance, thinner skin, "
            "slower healing, and reduced thermoregulation are expected and "
            "change how you assess symptoms and how you dose medications.",
            NIA_HEALTH,
            [
                "Reduced renal and hepatic clearance increases medication half-life.",
                "Reduced total body water and thirst perception increase dehydration risk.",
                "Arthritis and osteoporosis affect mobility, fall risk, and independence.",
            ],
        ),
        _b(
            "Geriatric assessment and polypharmacy",
            "A geriatric assessment looks beyond disease to function: mobility, "
            "falls, cognition, nutrition, continence, sleep, mood, social "
            "support, and the ability to manage medications. Polypharmacy is the "
            "norm rather than the exception, and medication review is one of the "
            "highest-value interventions in older adults because adverse drug "
            "events are a leading cause of hospitalization.",
            ML_OLDER_ADULT,
            [
                "Ask about falls, not just about dizziness.",
                "Review the entire medication list including over-the-counter drugs and supplements at every visit.",
                "Look for the Beers criteria medications that are inappropriate in older adults.",
            ],
        ),
        _b(
            "Pediatric lead exposure screening",
            "Lead is a potent neurotoxin with no safe level for children, and "
            "children are most often exposed through old housing, dust, soil, or "
            "imported products. Because the effects are developmental and "
            "permanent, screening is the primary defense. The CDC's lead "
            "prevention resources explain the risk factors, the blood lead "
            "reference value, and the follow-up steps after an abnormal result.",
            CDC_LEAD,
            [
                "Ask about the home environment, not just the patient's history.",
                "An elevated result requires prompt notification and a documented follow-up plan.",
                "Handwashing after outdoor play and before meals reduces exposure.",
            ],
        ),
        _b(
            "Repetitive work, workstation setup and patient handling",
            "Medical assisting is physically demanding: the same motions are "
            "repeated all day, and patients are often asked to move with "
            "limited ability. OSHA's ergonomics guidance covers the two biggest "
            "injury categories in healthcare — musculoskeletal disorders from "
            "repetitive work and awkward patient handling, and the strain of "
            "working in a poorly designed station.",
            OSHA_ERGONOMICS,
            [
                "Adjust the workstation height and equipment to the task and to you, not the other way around.",
                "Use a second person or a mechanical aid for lifting and repositioning patients.",
                "Report pain and numbness early — the sooner it is reported, the easier it is to fix.",
            ],
        ),
        _b(
            "Communication and sensory changes in older adults",
            "Hearing loss, vision impairment, and cognitive change affect how "
            "information is received. Slow down, face the patient, speak at a "
            "moderate volume, use written reinforcement, and confirm "
            "understanding. If the patient seems confused compared with their "
            "baseline, that is a clinical finding — possible delirium or "
            "infection — not simply 'being old'.",
            ML_DEMENTIA,
            [
                "Reduce background noise and speak facing the patient.",
                "A sudden change in mental status is a medical emergency until proven otherwise.",
                "Involve a family member or caregiver with the patient's permission.",
            ],
        ),
    ],
    "skill-emergency-aid": [
        _b(
            "The emergency response sequence",
            "A consistent sequence prevents omissions under stress: ensure scene "
            "safety, check responsiveness, call for help, assess airway, "
            "breathing, and circulation, and begin treatment. For the medical "
            "assistant, the priorities are usually to call 911 early, send "
            "someone for the AED, and start CPR while help is on the way.",
            RED_CROSS_FIRST_AID,
            [
                "Safety first — you do not become a second casualty.",
                "Call for help early; do not delay CPR to find a phone.",
                "Assign specific tasks: 'You — call 911 and bring the AED.'",
            ],
        ),
        _b(
            "Bleeding control",
            "Life-threatening external bleeding is controlled with firm direct "
            "pressure and, when needed, a commercial tourniquet or hemostatic "
            "dressing. Apply sustained pressure for at least 10 minutes, add "
            "dressings on top rather than removing soaked ones, and do not peek "
            "to check. If a tourniquet is used, record the time it was applied "
            "and never remove it in the field.",
            ML_CUTS,
            [
                "Direct pressure first, continuously, for 10 minutes or more.",
                "For severe limb bleeding, a tourniquet applied above the wound is appropriate if trained.",
                "Never remove a tourniquet once applied — document the time.",
            ],
        ),
        _b(
            "Anaphylaxis",
            "Anaphylaxis is a rapidly progressing, life-threatening systemic "
            "allergic reaction. Look for airway swelling, breathing difficulty, "
            "widespread hives, and low blood pressure or collapse. The first-line "
            "treatment is intramuscular epinephrine in the outer mid-thigh, given "
            "immediately, with the emergency response activated and the patient "
            "laid flat with legs elevated.",
            ML_ANAPHYLAXIS,
            [
                "Give epinephrine IM immediately in the anterolateral thigh — do not delay for antihistamines.",
                "Lie the patient flat with legs elevated; if breathing is difficult, let them sit up.",
                "Repeat epinephrine every 5–15 minutes if symptoms persist while awaiting help.",
            ],
        ),
        _b(
            "Choking and airway obstruction",
            "For a conscious adult or child with severe foreign-body airway "
            "obstruction, the current AHA guidance is to alternate 5 back blows "
            "with 5 abdominal thrusts until the object is expelled or the person "
            "becomes unresponsive. For infants, alternate 5 back blows with 5 "
            "chest thrusts. If the person becomes unresponsive, start CPR and "
            "look for the object before each set of breaths.",
            ML_CHOKING_ADULT,
            [
                "Encourage coughing if the person can cough forcefully.",
                "Do not perform a blind finger sweep.",
                "Check the mouth for the object each time the airway is opened during CPR.",
            ],
        ),
        _b(
            "Stroke, heart attack, and other time-critical events",
            "Use FAST to recognize stroke: Face drooping, Arm weakness, Speech "
            "difficulty, Time to call for help. For a heart attack, chest "
            "pressure, radiation, diaphoresis, and shortness of breath need "
            "immediate emergency care, and the patient should be kept still and "
            "reassured. Note the time symptoms started — it determines "
            "treatment eligibility.",
            ML_HEART_ATTACK_FIRST_AID,
            [
                "Activate the emergency response system and note the onset time.",
                "Do not give food, drink, or aspirin unless directed by emergency services.",
                "Keep the patient calm and still while waiting.",
            ],
        ),
        _b(
            "Documentation and debrief after an emergency",
            "After any emergency, document what happened, the interventions "
            "performed with times, the patient's response, and who was notified. "
            "A structured debrief helps the team process the event and improves "
            "future performance — it is a quality activity, not blame.",
            AHRQ_PATIENT_SAFETY,
            [
                "Record the time of the event, each intervention and its time, and the outcome.",
                "Complete the incident report and replace any used emergency supplies.",
                "Offer support to staff who were involved.",
            ],
        ),
    ],
}
# The Diabetes Study Guide quiz shares this guide with the CCMA diabetes topic.
STUDY_BY_TOPIC["diabetes-study-guide"] = STUDY_BY_TOPIC["ccma-diabetes"]
