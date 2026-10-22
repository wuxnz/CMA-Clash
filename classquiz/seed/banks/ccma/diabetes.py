# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-diabetes)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-diabetes-001
    fact(
        "ccma-diabetes",
        "When screening a patient with diabetes for kidney disease, what does a urine albumin-to-creatinine ratio primarily detect?",
        "Early diabetic nephropathy before serum creatinine rises",
        [
            "Acute urinary tract infection with pyuria as the marker",
            "Elevated serum creatinine as the earliest sign before urinary protein changes",
            "Isolated hematuria on dipstick without measuring urinary albumin excretion",
        ],
        "Persistent albuminuria signals glomerular damage and guides ACE inhibitor or ARB therapy and nephrology referral per ADA kidney care standards. Serum creatinine alone, pyuria, and dipstick hematuria do not detect early diabetic kidney disease.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-002
    fact(
        "ccma-diabetes",
        "For many nonpregnant adults with diabetes, what blood pressure goal do current guidelines commonly target when treatment is needed?",
        "Below 130/80 mmHg when it can be reached without excessive side effects",
        [
            "Above 160/100 mmHg to preserve renal perfusion in every patient",
            "No routine measurement because hypertension is unrelated to diabetes",
            "Exactly 140/90 mmHg at annual wellness visits regardless of cardiovascular risk",
        ],
        "Hypertension and diabetes both raise atherosclerotic cardiovascular disease risk, so tighter BP control is individualized but often aims near 130/80 mmHg. Targets of 160/100 mmHg, skipping measurement, or a fixed 140/90 mmHg value do not reflect guideline practice.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-003
    fact(
        "ccma-diabetes",
        "What clinical information does continuous glucose monitoring (CGM) most often provide compared with intermittent fingersticks?",
        "Trends in interstitial glucose with optional high and low alerts",
        [
            "A single fasting capillary glucose at clinic arrival without trend data",
            "Hemoglobin A1C reflecting average glycemia over months without real-time alerts",
            "Urinary glucose on dipstick from the prior void",
        ],
        "CGM shows direction and rate of glucose change, helping patients and clinicians adjust therapy between laboratory A1C checks. A single fasting value, an A1C, or a urine dipstick cannot show real-time trends or alert patients to lows.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-004
    fact(
        "ccma-diabetes",
        "How should diabetes self-management education and support (DSMES) be offered across the care continuum?",
        "At diagnosis and when treatment or life circumstances change",
        [
            "One group class at diagnosis with no follow-up education sessions",
            "After insurance authorization, with no follow-up sessions",
            "As a substitute for scheduled medical visits and lab monitoring",
        ],
        "DSMES teaches meal planning, glucose monitoring, and sick-day planning, and revisiting skills improves adherence when regimens or goals shift. A single class or education deferred until authorization does not support ongoing self-management.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-005
    fact(
        "ccma-diabetes",
        "Which cluster of findings is characteristic of diabetic ketoacidosis (DKA)?",
        "Hyperglycemia, ketonemia or ketonuria, and metabolic acidosis",
        [
            "Normoglycemia with isolated peripheral edema",
            "Marked hyperglycemia with metabolic alkalosis and absent ketones",
            "A single maculopapular rash without ketosis, acidosis, or marked hyperglycemia",
        ],
        "DKA reflects insulin deficiency with lipolysis and ketone production, making it a medical emergency requiring IV fluids, insulin, and electrolyte monitoring. Normoglycemia, metabolic alkalosis, or an isolated rash does not fit the DKA pattern.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-006
    fact(
        "ccma-diabetes",
        "On repeat testing, fasting plasma glucose at or above which value meets the ADA threshold for diabetes mellitus?",
        "126 mg/dL (7.0 mmol/L) on confirmatory fasting plasma glucose",
        [
            "100 mg/dL (5.6 mmol/L), which defines prediabetes on FPG",
            "110 mg/dL on one sample without symptoms or repeat confirmation",
            "200 mg/dL on a single sample without symptoms or confirmatory testing",
        ],
        "Unless unequivocal hyperglycemia with symptoms is present, diagnosis generally requires a second abnormal result or a different qualifying test. A single abnormal value without confirmation, or a 200 mg/dL sample with no symptoms, does not establish diabetes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-007
    fact(
        "ccma-diabetes",
        "During a comprehensive foot examination in a patient with diabetes, what should the clinician assess?",
        "Peripheral neuropathy, skin ulcers, and vascular perfusion",
        [
            "Hair color and nail polish without monofilament testing",
            "Palpable pedal pulses without monofilament testing or skin inspection",
            "Footwear inspection without monofilament testing or vascular assessment",
        ],
        "Loss of protective sensation and poor circulation predispose to nonhealing ulcers and amputation, and monofilament and pulse checks are routine components. Cosmetic findings, pulses alone, or footwear inspection alone miss neuropathy and perfusion problems.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-008
    fact(
        "ccma-diabetes",
        "Using a standardized assay on repeat testing, hemoglobin A1C at or above which level indicates diabetes mellitus?",
        "6.5% on repeat standardized laboratory testing",
        [
            "5.0%, which is within typical normal range",
            "5.7% from a single test without confirmation",
            "8.0% from one pregnancy draw without repeat confirmatory testing",
        ],
        "A1C estimates average glycemia over roughly two to three months and is one of the ADA-listed diagnostic criteria when performed in a certified laboratory. A single unconfirmed result, a normal value, or a pregnancy draw does not establish the diagnosis.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-009
    fact(
        "ccma-diabetes",
        "For a conscious, alert adult with symptomatic hypoglycemia who can swallow, what is the usual first treatment step?",
        "Approximately 15 grams of fast-acting carbohydrate",
        [
            "About 30 grams of fast-acting carbohydrate because symptoms are noticeable",
            "A high-protein snack without carbohydrate to prevent rebound hyperglycemia",
            "Oral fluids without carbohydrate while rechecking glucose in one hour",
        ],
        "The 15-15 approach raises glucose quickly, and glucose is rechecked in about 15 minutes and repeated if levels remain below 70 mg/dL per protocol. Giving 30 grams, protein alone, or fluids without carbohydrate does not match that standard.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-010
    fact(
        "ccma-diabetes",
        "Metformin is commonly withheld or dose-limited when which patient situation is present?",
        "Renal impairment or acute illness that raises lactic acidosis risk",
        [
            "Mild dietary counseling without laboratory abnormalities",
            "Well-controlled hypertension on a single antihypertensive medication",
            "Routine self-monitoring of blood glucose with a glucometer daily",
        ],
        "Estimated glomerular filtration rate guides metformin prescribing, and contrast studies and dehydration may also require temporary discontinuation per provider orders. Dietary counseling, hypertension control, and routine glucose checks do not limit metformin.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-011
    fact(
        "ccma-diabetes",
        "According to ADA categories, which A1C range most often defines prediabetes?",
        "5.7% to 6.4% on a standardized assay",
        [
            "Below 5.0% in adults without other risk factors",
            "8.0% or higher, meeting diabetes diagnostic threshold",
            "Exactly 7.0% when fasting glucose and OGTT are normal",
        ],
        "Prediabetes carries higher future diabetes and cardiovascular risk, so lifestyle programs and periodic rescreening are recommended. An A1C of 7.0% with normal glucose testing, or values above 8.0%, indicate diabetes rather than prediabetes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-012
    fact(
        "ccma-diabetes",
        "When might a moderate- or high-intensity statin be recommended for an adult with diabetes?",
        "Based on age, ASCVD history, and additional risk factors per guidelines",
        [
            "Lipid-lowering therapy withheld when diabetes is the sole risk factor",
            "When fingerstick glucose is below 70 mg/dL with symptomatic hypoglycemia",
            "In place of glucose or blood pressure monitoring",
        ],
        "Most adults with diabetes benefit from statin therapy when cardiovascular risk warrants it, alongside glycemic and blood pressure management. Withholding statins for diabetes alone, or treating hypoglycemia, does not match guideline risk assessment.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-013
    fact(
        "ccma-diabetes",
        "Which pathophysiology best describes type 1 diabetes mellitus?",
        "Autoimmune beta-cell destruction with absolute insulin deficiency",
        [
            "Isolated insulin resistance without beta-cell loss",
            "Reversible hyperglycemia from placental hormones in pregnancy",
            "Primary dietary excess with preserved beta-cell mass and no autoimmunity",
        ],
        "Type 1 usually presents in younger patients and requires exogenous insulin for survival, and autoantibody testing may support the diagnosis. Insulin resistance without beta-cell loss, gestational hyperglycemia, and dietary excess describe other mechanisms.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-014
    fact(
        "ccma-diabetes",
        "Type 2 diabetes mellitus most commonly develops through which mechanism?",
        "Progressive insulin resistance with relative secretory failure",
        [
            "Sudden autoimmune loss of pancreatic beta cells presenting in infancy",
            "Absence of blood glucose despite high dietary sugar intake",
            "Gestational hormone effects that persist after delivery",
        ],
        "Genetics, adiposity, and inactivity contribute to insulin resistance, and oral agents and later insulin may be needed as beta-cell function declines. Autoimmune loss in infancy, absent glucose, and persistent gestational effects describe other mechanisms.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-015
    fact(
        "ccma-diabetes",
        "For an insulin-treated patient following sick-day instructions during a febrile illness, which actions are typically emphasized?",
        "Continue basal insulin, monitor glucose and ketones, hydrate",
        [
            "Stop all insulin until oral intake returns and omit the ketone checks",
            "Ignore moderate or large urine ketones when nausea and vomiting occur",
            "Restrict oral fluids to limit the hyperglycemia despite fever and vomiting",
        ],
        "Stress hormones raise glucose during illness, and withholding insulin can worsen ketosis while frequent monitoring guides supplemental doses per provider plan. Stopping insulin, ignoring urine ketones, or limiting fluids is not safe sick-day teaching.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-016
    fact(
        "ccma-diabetes",
        "A newly diagnosed adolescent has positive pancreatic autoantibodies and requires insulin immediately. Which diabetes type does this presentation most suggest?",
        "Type 1 diabetes mellitus with autoimmune beta-cell destruction",
        [
            "Type 2 diabetes driven by insulin resistance alone",
            "Gestational diabetes that resolves after delivery of the infant",
            "Steroid-induced hyperglycemia without ongoing insulin need",
        ],
        "Type 1 results in little or no endogenous insulin, and insulin therapy is essential from diagnosis in most cases. Positive autoantibodies with an immediate insulin requirement point away from type 2 and gestational diabetes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-017
    fact(
        "ccma-diabetes",
        "An overweight adult develops gradual hyperglycemia and responds initially to metformin. Which underlying process is most likely?",
        "Insulin resistance with relative insulin deficiency over time",
        [
            "Acute autoimmune destruction of beta cells during early infancy",
            "Complete absence of circulating glucose in the blood",
            "Hyperglycemia confined to the third trimester of pregnancy",
        ],
        "Type 2 is the most common form in adults and may progress from lifestyle measures to oral agents and insulin. Autoimmune beta-cell loss in infancy, absent circulating glucose, and third-trimester hyperglycemia describe other processes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-018
    fact(
        "ccma-diabetes",
        "How is gestational diabetes mellitus (GDM) distinguished from preexisting diabetes?",
        "Hyperglycemia first detected in pregnancy that was not overt diabetes",
        [
            "Glucose intolerance that first appears during the postpartum lactation period",
            "Diagnosis based on a fingerstick below 70 mg/dL",
            "Hyperglycemia in pregnancy assumed resolved after delivery",
        ],
        "Obstetric screening between 24 and 28 weeks, or earlier with risk factors, identifies GDM, and postpartum glucose testing is recommended. Lactation-onset intolerance, low fingersticks, or assuming resolution at delivery do not distinguish GDM.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-019
    fact(
        "ccma-diabetes",
        "Which fasting plasma glucose (FPG) range meets ADA criteria for prediabetes?",
        "100 to 125 mg/dL (5.6 to 6.9 mmol/L)",
        [
            "Below 70 mg/dL, consistent with hypoglycemia",
            "126 mg/dL or higher, which meets diabetes on FPG",
            "200 mg/dL or higher without further testing",
        ],
        "Prediabetes on FPG overlaps with impaired fasting glucose, and confirmatory categories also use A1C and oral glucose tolerance testing. Values below 70 mg/dL or at 126 mg/dL and above fall outside that range.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-020
    fact(
        "ccma-diabetes",
        "On appropriate laboratory testing, which fasting plasma glucose level meets criteria for diabetes mellitus?",
        "126 mg/dL (7.0 mmol/L)",
        [
            "100 mg/dL, which defines prediabetes",
            "90 mg/dL in an asymptomatic adult",
            "110 mg/dL without repeat confirmation",
        ],
        "A second abnormal test or a different qualifying criterion is usually required unless classic hyperglycemic symptoms are present. A 100 mg/dL or 110 mg/dL result in an asymptomatic adult does not meet the threshold.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-021
    fact(
        "ccma-diabetes",
        "A standardized A1C result of 6.5% or higher on confirmatory testing indicates which diagnosis?",
        "Diabetes mellitus on confirmatory testing",
        [
            "Normal glucose metabolism",
            "Prediabetes without progression risk",
            "Hypoglycemia without meeting diabetes A1C criteria",
        ],
        "A1C reflects average glycemia over approximately two to three months and is listed among ADA diagnostic criteria. Normal glucose metabolism, prediabetes range, or hypoglycemia does not fit a confirmed A1C of 6.5% or higher.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-022
    fact(
        "ccma-diabetes",
        "Which A1C range is classified as prediabetes under ADA diagnostic categories?",
        "5.7% to 6.4% on a standardized assay",
        [
            "Below 4.0%, below typical laboratory reference intervals",
            "6.5% or higher, which meets diabetes criteria",
            "8.0% or higher without symptoms",
        ],
        "Intensive lifestyle intervention can delay or prevent progression to type 2 diabetes in many individuals with prediabetes. Values of 6.5% or higher meet diabetes criteria, and 8.0% or higher is well above that range.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-023
    fact(
        "ccma-diabetes",
        "After a 75-g oral glucose tolerance test (OGTT), which 2-hour plasma glucose meets diabetes diagnostic criteria?",
        "200 mg/dL (11.1 mmol/L) or higher",
        [
            "140 mg/dL, which may reflect impaired glucose tolerance",
            "100 mg/dL, within the prediabetes FPG range",
            "70 mg/dL or lower, consistent with hypoglycemia",
        ],
        "OGTT remains an ADA-listed criterion and may clarify the diagnosis when FPG or A1C results are equivocal. A 2-hour value of 140 mg/dL suggests impaired glucose tolerance, and 100 mg/dL or 70 mg/dL is below the diabetic range.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-024
    fact(
        "ccma-diabetes",
        "Which symptom cluster is classically associated with untreated hyperglycemia?",
        "Increased urination, increased thirst, and unexplained weight loss",
        [
            "Blurred vision and headache without polyuria, polydipsia, or weight change",
            "Fatigue and mild nausea without polyuria, polydipsia, or weight loss",
            "Isolated foot numbness without polyuria or polydipsia",
        ],
        "Polyuria and polydipsia result from osmotic diuresis, and weight loss may occur despite polyphagia when insulin is insufficient. Blurred vision alone, fatigue alone, or isolated foot numbness does not fit the classic triad.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-025
    fact(
        "ccma-diabetes",
        "Which office finding should the medical assistant escalate to the provider immediately?",
        "Random glucose 400 mg/dL with vomiting and confusion",
        [
            "Fasting glucose 118 mg/dL on routine screening with no acute symptoms",
            "Random glucose 280 mg/dL, thirsty and alert, without vomiting",
            "Capillary glucose 65 mg/dL, alert and oriented, eating crackers at the desk",
        ],
        "Severe hyperglycemia with altered mental status may signal DKA or hyperosmolar crisis and requires urgent clinical evaluation. A fasting value near 118 mg/dL, a random 280 mg/dL in an alert patient, and a low reading treated with crackers each need a different response.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-026
    fact(
        "ccma-diabetes",
        "Which combination of factors most increases risk for developing type 2 diabetes mellitus?",
        "Overweight or obesity, family history, and inactivity",
        [
            "Positive islet autoantibodies typical of type 1 disease",
            "Daily use of rapid-acting insulin from childhood",
            "Age under 2 years as the sole risk factor.",
        ],
        "Modifiable risks include weight, activity, and cardiometabolic control, and screening follows ADA recommendations for at-risk adults. Autoantibodies, insulin use from childhood, and very young age point to type 1 rather than type 2 risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-027
    fact(
        "ccma-diabetes",
        "Before drawing blood for a fasting glucose ordered by the provider, what should the medical assistant verify with the patient?",
        "No caloric intake for at least 8 hours unless plain water is allowed",
        [
            "A full breakfast eaten within the hour before the blood draw",
            "A brief 30-minute fast with no water and no morning medications taken",
            "Doubling diabetes medications the morning of the scheduled draw",
        ],
        "Nonfasting samples can falsely lower or raise interpreted results, so follow the laboratory requisition and facility protocol. A full breakfast, a brief fast without water, or doubling medications produces unusable results.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-028
    fact(
        "ccma-diabetes",
        "Per ADA guidance, at which blood glucose level is treatment for hypoglycemia generally initiated?",
        "A glucose of 70 mg/dL (3.9 mmol/L) or lower",
        [
            "200 mg/dL, which is above typical postmeal targets",
            "126 mg/dL, the diabetes diagnostic FPG threshold",
            "50 mg/dL overnight rechecked at breakfast without treating during the night",
        ],
        "Alert patients receive fast-acting carbohydrate, while severe or unresponsive hypoglycemia triggers emergency protocols including glucagon when available. Levels of 200 mg/dL or 126 mg/dL call for different actions.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-029
    fact(
        "ccma-diabetes",
        "When applying the 15-15 rule for mild hypoglycemia in a patient who can swallow, what should the medical assistant do?",
        "Give about 15 grams of carbohydrate and recheck in 15 minutes",
        [
            "Wait 15 minutes before giving carbohydrate so symptoms can fully develop",
            "Give 15 grams of protein alone without rechecking glucose afterward",
            "Recheck glucose in 15 minutes without administering carbohydrate first",
        ],
        "If glucose remains low, repeat the carbohydrate and notify the provider per facility policy, and once stable, add a snack with protein if the next meal is delayed. Waiting, giving protein alone, or rechecking without carbohydrate does not treat the event.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-030
    fact(
        "ccma-diabetes",
        "Which signs and symptoms may indicate hypoglycemia in a patient taking insulin or sulfonylureas?",
        "Shakiness, diaphoresis, irritability, and difficulty concentrating",
        [
            "Slow, deep respirations without autonomic warning symptoms",
            "Marked polyuria without thirst or other autonomic warning symptoms",
            "Warm dry skin with severe hypertension and no tremor",
        ],
        "Autonomic warning symptoms may be blunted in long-standing diabetes or neuropathy, so glucose checks should not rely on symptoms alone. Deep respirations, polyuria, and warm dry skin point to hyperglycemia rather than hypoglycemia.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-031
    fact(
        "ccma-diabetes",
        "A conscious patient with hypoglycemia is vomiting and cannot swallow oral carbohydrate safely. What is the appropriate medical assistant action?",
        "Summon help and follow emergency protocol without forcing oral glucose",
        [
            "Attempt oral glucose gel while the patient is actively vomiting",
            "Leave the patient alone to retrieve glucagon from the medication room",
            "Document the low reading and defer treatment until the next scheduled visit",
        ],
        "Aspiration risk outweighs oral treatment when swallowing is unsafe, and severe hypoglycemia may require intramuscular glucagon or EMS activation per scope and standing orders. Attempting oral gel during vomiting or delaying care endangers the patient.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-032
    fact(
        "ccma-diabetes",
        "Which laboratory and clinical pattern is characteristic of diabetic ketoacidosis (DKA)?",
        "Hyperglycemia with ketones and metabolic acidosis",
        [
            "Normoglycemia with absent ketones and normal pH",
            "Isolated hypoglycemia without acid-base disturbance",
            "Hypertension as the sole metabolic abnormality",
        ],
        "Insulin deficiency drives lipolysis and ketone production, and DKA is most common in type 1 diabetes but can occur in type 2 under stress or illness. Normoglycemia, isolated hypoglycemia, and hypertension alone do not fit the syndrome.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-033
    fact(
        "ccma-diabetes",
        "Hyperosmolar hyperglycemic state (HHS) is distinguished from DKA mainly by which features?",
        "Marked hyperglycemia and dehydration with little or no ketosis",
        [
            "Profound ketonemia with normal or near-normal glucose levels",
            "Blood glucose consistently below 100 mg/dL with severe dehydration",
            "Primary hypothermia without osmotic diuresis or hyperglycemia",
        ],
        "HHS often develops gradually in older adults with type 2 diabetes and carries high mortality without aggressive fluids and insulin in a monitored setting. Profound ketosis, low glucose, and hypothermia describe other presentations.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-034
    fact(
        "ccma-diabetes",
        "When DKA or HHS is suspected in the outpatient setting, what should the medical assistant do first?",
        "Notify the provider or emergency team promptly and monitor vital signs",
        [
            "Give oral carbohydrate and observe in the waiting room for one hour",
            "Start subcutaneous insulin at home doses and schedule follow-up next week",
            "Obtain a urine sample and discharge if ketones are trace on the dipstick",
        ],
        "Both syndromes need hospital-level fluid resuscitation, insulin therapy, electrolyte correction, and continuous monitoring rather than routine office management alone. Oral carbohydrate, home insulin, and discharge with trace ketones are not safe responses.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-035
    fact(
        "ccma-diabetes",
        "Under CLIA, how are most point-of-care blood glucose meters classified when used according to manufacturer instructions?",
        "Waived tests with defined personnel and quality requirements",
        [
            "Moderate-complexity laboratory procedures",
            "Provider-performed microscopy in the point-of-care setting",
            "High-complexity testing whenever the patient is critically ill in the clinic",
        ],
        "Waived status still obligates trained operators, control testing, and policies that align with the Clinical Laboratory Improvement Amendments and facility protocols. Moderate complexity, provider microscopy, and high complexity describe other test categories.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-036
    fact(
        "ccma-diabetes",
        "Which steps are required before performing a fingerstick glucose test in the clinic?",
        "Confirm identity, perform hand hygiene, don gloves, prepare the site",
        [
            "Puncture the thumb pad without site prep because capillary flow is faster",
            "Use the same lancet for repeat checks on one patient during the same visit",
            "Confirm identity verbally but omit hand hygiene when gloves are already worn",
        ],
        "Standard precautions and two-patient identifiers reduce wrong-patient errors and bloodborne pathogen transmission during waived testing. Puncturing without preparation, reusing a lancet, or skipping hand hygiene breaks that protection.",
        ["CDC: Infection Control in Healthcare Settings (overview) — https://www.cdc.gov/infection-control/hcp/index.html", S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-037
    fact(
        "ccma-diabetes",
        "For an adult fingerstick glucose sample, which puncture site is generally preferred?",
        "The lateral fingertip, avoiding cold, cyanotic, or edematous digits",
        [
            "The center of the palm as the routine first choice for capillary sampling",
            "The earlobe as the preferred site for routine adult glucose monitoring",
            "The heel as the primary puncture site for ambulatory adults in clinic",
        ],
        "Rotating fingers and matching lancet depth to skin thickness improve comfort and sample quality while limiting callus formation. The palm, earlobe, and heel are not routine adult capillary sites.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-038
    fact(
        "ccma-diabetes",
        "What quality control practice is expected for waived glucose meters in clinical use?",
        "Run control solution on schedule and document each result",
        [
            "Defer control solution runs when clinic patient volume is high",
            "Use expired test strips if the vial seal looks intact",
            "Adjust calibration by estimating rather than following the manual",
        ],
        "Failed controls should halt patient testing until the device is troubleshooted or serviced according to manufacturer and laboratory director guidance. Skipping controls, expired strips, and estimated calibration undermine result reliability.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-039
    fact(
        "ccma-diabetes",
        "A fingerstick glucose reading conflicts with the patient's symptoms and appearance. What should the medical assistant do?",
        "Repeat the test, check lot and technique, report the discrepancy",
        [
            "Chart the first value without rechecking to save time",
            "Omit the result from the record when it seems inconvenient to staff",
            "Give insulin immediately based on a single unverified reading",
        ],
        "Critical or unexpected values trigger facility notification rules, and repeating the measurement helps distinguish device error from true metabolic crisis. Charting without rechecking, omitting a result, or dosing from one reading risks harm.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-040
    fact(
        "ccma-diabetes",
        "Rapid-acting insulin analogs such as lispro or aspart typically begin lowering glucose in about how long?",
        "Approximately 15 minutes, peaking around 1 to 2 hours after injection",
        [
            "Onset at 30 to 60 minutes with peak near 4 to 6 hours like regular insulin",
            "Onset at 2 to 4 hours with minimal peak like intermediate NPH insulin",
            "Onset within minutes with flat action over 24 hours like glargine basal insulin",
        ],
        "Mealtime analogs are given shortly before or with food so insulin action parallels the postprandial glucose rise per the prescribed regimen. Regular insulin, NPH, and glargine have different onset and peak profiles.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-041
    fact(
        "ccma-diabetes",
        "When is regular (short-acting) human insulin expected to reach peak activity after subcutaneous injection?",
        "Regular insulin peaks at about 2 to 3 hours after injection",
        [
            "Within 15 minutes, similar to rapid-acting insulin analogs given before meals",
            "Between 4 and 12 hours, overlapping the typical peak window for NPH insulin",
            "With no discernible peak because action is flat from injection to offset",
        ],
        "Onset is roughly 30 minutes and total duration is often 5 to 8 hours, so timing relative to meals and snacks must match the provider order. Rapid analogs and NPH have different onset and peak windows.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-042
    fact(
        "ccma-diabetes",
        "Intermediate-acting NPH insulin is characterized by which pharmacokinetic profile?",
        "Onset in 1 to 2 hours, peak at 4 to 12 hours, duration up to 24 hours",
        [
            "Onset within minutes and duration under one hour, like mealtime insulin analogs",
            "Peak activity near 30 to 60 minutes, like regular insulin",
            "Peakless basal coverage for roughly 24 hours, similar to insulin glargine",
        ],
        "NPH suspension appears cloudy and must be rolled gently to resuspend particles before drawing the dose into the syringe. Mealtime analogs and peakless basal insulin have very different profiles.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-043
    fact(
        "ccma-diabetes",
        "What is the primary role of long-acting basal insulin such as insulin glargine?",
        "Provide relatively steady background insulin over approximately 24 hours",
        [
            "Cover each mealtime glucose rise without separate bolus or correction doses",
            "Treat alert hypoglycemia as the first-line oral or injectable therapy",
            "Stop all basal insulin during febrile illness without contacting the prescriber",
        ],
        "Basal-bolus regimens combine once- or twice-daily basal insulin with rapid insulin for carbohydrate coverage and corrections. Covering mealtimes alone, treating hypoglycemia, or stopping basal insulin during illness is not the basal role.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-044
    fact(
        "ccma-diabetes",
        "How should unopened and in-use insulin vials or pens be stored under typical manufacturer guidance?",
        "Refrigerate unopened insulin; keep in-use insulin at room temperature",
        [
            "Store unopened and in-use insulin in direct sunlight on a warm windowsill",
            "Freeze unopened vials and thaw them weekly",
            "Combine leftover insulin from several patients in one shared vial",
        ],
        "Heat, freezing, and prolonged room-temperature exposure degrade insulin, and preparations that are expired, frosted, or discolored are discarded. Direct sunlight, freezing to extend dating, and sharing vials are unsafe practices.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-045
    fact(
        "ccma-diabetes",
        "When assisting with insulin administration within scope, what must the medical assistant verify?",
        "Written order, identity, drug, concentration, dose, route, and site",
        [
            "An estimated dose from prior visits when the scale is hard to read",
            "One insulin syringe reused for several patients after wiping with alcohol",
            "Small air bubbles in the syringe injected without being removed",
        ],
        "Insulin is a high-alert medication, and many facilities require an independent double check before subcutaneous injection. Estimated doses, shared syringes, and injected air bubbles introduce serious dosing errors.",
        ["FDA: Medication Safety Program — https://www.fda.gov/drugs/medication-safety-program", S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-046
    fact(
        "ccma-diabetes",
        "What is the principal mechanism of metformin in type 2 diabetes management?",
        "Reducing hepatic glucose output and improving peripheral insulin sensitivity",
        [
            "Stimulating insulin release from beta cells independent of current glucose level",
            "Blocking renal sodium-glucose cotransport to increase urinary glucose loss",
            "Replacing injected insulin as primary therapy in autoimmune type 1 diabetes",
        ],
        "Metformin remains first-line pharmacotherapy for many adults with type 2 diabetes when renal function and other contraindications are absent. Secretagogues, SGLT2 inhibitors, and insulin replacement have different mechanisms.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-047
    fact(
        "ccma-diabetes",
        "How do sulfonylureas such as glipizide lower blood glucose?",
        "Stimulating insulin release from functioning beta cells",
        [
            "Blocking renal sodium-glucose cotransport in the proximal tubule",
            "Serving as the sole inpatient treatment for diabetic ketoacidosis",
            "Eliminating hypoglycemia risk when taken without food.",
        ],
        "Because secretion continues even when glucose is low, patients need education on recognizing and treating hypoglycemia, especially the elderly. Blocking renal glucose, treating DKA, or removing hypoglycemia risk does not describe this class.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-048
    fact(
        "ccma-diabetes",
        "SGLT2 inhibitors reduce hyperglycemia through which mechanism?",
        "Increasing urinary excretion of filtered glucose",
        [
            "Decreasing hepatic glucose output while improving peripheral insulin sensitivity",
            "Stimulating continuous insulin secretion from beta cells like a sulfonylurea",
            "Delaying gastric emptying and enhancing incretin signaling like a GLP-1 agonist",
        ],
        "Patients should report genital mycotic infections, volume depletion, or persistent nausea, because rare euglycemic ketoacidosis can occur. Reduced hepatic output, insulin secretion, and delayed gastric emptying describe other drug classes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-049
    fact(
        "ccma-diabetes",
        "How do GLP-1 receptor agonists improve glycemic control?",
        "Enhancing glucose-dependent insulin secretion and delaying gastric emptying",
        [
            "Replacing oral fluids with hypertonic saline in routine therapy",
            "Suppressing appetite through prolonged unsupervised fasting",
            "Making fingerstick and A1C monitoring unnecessary once the injection is started",
        ],
        "Injectable GLP-1 agents may also promote modest weight loss and carry gastrointestinal side effects that often lessen over time. Hypertonic saline, unsupervised fasting, and dropping monitoring do not describe this therapy.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-050
    fact(
        "ccma-diabetes",
        "How do DPP-4 inhibitors such as sitagliptin affect glucose regulation?",
        "Prolonging incretin hormones that stimulate insulin with glucose",
        [
            "Mimicking GLP-1 effects on gastric emptying without injectable dosing",
            "Blocking SGLT2 transporters to increase urinary glucose loss",
            "Stimulating insulin secretion independent of glucose like a sulfonylurea",
        ],
        "These oral agents are generally weight-neutral and carry lower intrinsic hypoglycemia risk when not combined with secretagogues. Gastric emptying effects, SGLT2 blockade, and glucose-independent secretion describe other classes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-051
    fact(
        "ccma-diabetes",
        "Before administering a prescribed diabetes medication, which patient information should the medical assistant review?",
        "Documented allergies, renal or hepatic notes, and food requirements",
        [
            "Footwear size for equipment inventory without allergy review",
            "Patient preference for tablets over injections regardless of the order",
            "Unverified dosing suggestions from nonclinical sources",
        ],
        "Several classes need renal dose adjustment or are contraindicated with contrast, surgery, or acute illness per provider and pharmacy guidance. Equipment inventory, patient preference, and unverified dosing suggestions are not medication checks.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-052
    fact(
        "ccma-diabetes",
        "Why is periodic diabetic retinopathy screening emphasized in chronic diabetes care?",
        "Eye disease may progress silently until vision is threatened",
        [
            "Dilated eye exams eliminate the need for foot surveillance.",
            "Retinal screening cures hyperglycemia without other therapy",
            "A single childhood eye visit replaces all future diabetic eye care",
        ],
        "ADA guidelines recommend dilated eye evaluation intervals based on type of diabetes, prior findings, and pregnancy status. Eye exams do not replace foot surveillance, and one childhood visit does not end eye care.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-053
    fact(
        "ccma-diabetes",
        "Diabetic peripheral neuropathy commonly causes which patient-reported symptoms?",
        "Numbness, tingling, burning, or pain in the feet or hands",
        [
            "Isolated substernal chest pressure without foot symptoms",
            "Heightened vibration sense with improved detection of hot surfaces and trauma",
            "Assurance that neuropathy prevents plantar ulcer formation",
        ],
        "Loss of protective sensation increases ulcer and amputation risk, and monofilament testing may be incorporated into comprehensive foot exams. Chest pressure, heightened vibration sense, and reassurance about ulcers do not fit neuropathy.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-054
    fact(
        "ccma-diabetes",
        "Which tests are routinely used to monitor diabetic kidney disease?",
        "Urine albumin-to-creatinine ratio with serum creatinine and eGFR",
        [
            "Annual fasting fingerstick without urinalysis or serum creatinine trend review",
            "Spot urine dipstick for protein without the albumin ratio",
            "Deferring renal monitoring once ACE inhibitor or ARB therapy starts",
        ],
        "Persistent albuminuria and declining eGFR guide ACE inhibitor or ARB therapy and nephrology referral when indicated. A fingerstick alone, a dipstick for protein, or stopping renal monitoring once therapy starts misses progression.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-055
    fact(
        "ccma-diabetes",
        "What should daily self foot-care education stress for patients with diabetes?",
        "Inspect skin and nails, wear proper footwear, report breaks promptly",
        [
            "Soak the feet in very hot water daily without drying between the toes",
            "Trim toenails into the corners to prevent ingrown nails",
            "Walk barefoot on hot or uneven surfaces to toughen the skin",
        ],
        "Early referral for nonhealing wounds reduces progression to deep infection and lower-extremity amputation. Hot water soaks, corner nail trimming, and barefoot walking on hot surfaces cause injury instead.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-056
    fact(
        "ccma-diabetes",
        "How does carbohydrate counting support insulin or meal planning education?",
        "It aligns prandial insulin doses with carbohydrate intake",
        [
            "It matches prandial insulin units to counted carbohydrate grams at each meal",
            "It eliminates dietary protein to reduce gluconeogenesis without dietitian input",
            "It replaces self-monitoring of blood glucose without provider or educator input",
        ],
        "Registered dietitian nutritionists help patients interpret labels and portion sizes so postmeal glucose targets are more achievable. Eliminating protein, dropping monitoring, or skipping the dietitian does not describe carbohydrate counting.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-057
    fact(
        "ccma-diabetes",
        "Which elements belong in complete documentation of diabetes-related care in the medical record?",
        "Glucose values, symptoms, interventions, and patient response",
        [
            "Diet preferences and meal timing without values or interventions",
            "Copy-forward text that omits current readings and intervention times",
            "Numeric results without symptoms, actions, or patient response",
        ],
        "Accurate, timely charting supports safe handoffs, billing integrity, and quality measurement across the care team. Diet notes, copy-forward text, and bare numbers leave the record without clinical meaning.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-058
    fact(
        "ccma-diabetes",
        "How is independent adjustment of a patient's insulin doses by a medical assistant classified under typical scope rules?",
        "Outside scope unless delegated by law and clinician protocol",
        [
            "Expected at every visit without a provider order",
            "Permitted based on informal advice from nonclinical contacts",
            "Allowed without charting when the change seems minor",
        ],
        "Medication titration remains a licensed prescriber function unless state regulations and written delegation authorize otherwise. Adjusting doses at every visit, informal advice, and uncharted changes are not in scope.",
        [S.NHA_CCMA, "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "advanced",
    ),
    # ccma-diabetes-059
    fact(
        "ccma-diabetes",
        "Sick-day teaching for insulin-treated patients typically emphasizes which actions?",
        "Continue basal insulin, check glucose often, test ketones, hydrate",
        [
            "Hold all insulin, including basal doses, until the patient is afebrile",
            "Restrict oral and intravenous fluids to lower the glucose",
            "Ignore repeated vomiting or inability to tolerate fluids",
        ],
        "Counter-regulatory hormones during illness raise glucose and ketone risk, and withholding insulin can worsen ketoacidosis while dehydration impairs perfusion. Stopping basal insulin, limiting fluids, and ignoring vomiting are not safe advice.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-060
    fact(
        "ccma-diabetes",
        "Why should many people with diabetes wear medical identification such as a bracelet or necklace?",
        "It tells emergency personnel about diabetes and glucose needs",
        [
            "It eliminates the need for daily glucose checks at home",
            "Decorative jewelry with no emergency medical information engraved",
            "It guarantees euglycemia during an acute illness",
        ],
        "Combined with patient education on when to seek urgent care, medical ID supports safer management when the patient cannot speak for themselves. Skipping glucose checks, decorative jewelry, and guaranteed control do not fit that purpose.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-061
    fact(
        "ccma-diabetes",
        "Why is treating hypertension a priority in a patient who already has diabetes mellitus?",
        "Elevated blood pressure multiplies cardiovascular and kidney risk",
        [
            "Normal blood pressure removes the need for dilated eye examinations",
            "Antihypertensive therapy prevents all diabetic peripheral neuropathy",
            "Once blood pressure is controlled, A1C targets no longer apply",
        ],
        "Diabetes and hypertension share vascular injury pathways, and combined control reduces stroke, heart disease, and nephropathy progression. Normal pressure, glycemic control, or eye exams do not replace blood pressure management.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-062
    fact(
        "ccma-diabetes",
        "When teaching a patient with diabetes about safe physical activity, what should the medical assistant emphasize?",
        "Check glucose before and after exercise and carry fast-acting carbs",
        [
            "Exercise vigorously when glucose exceeds 400 mg/dL without calling the team",
            "Avoid all fluids during activity to limit hyperglycemia",
            "Wear open footwear during walks to improve circulation",
        ],
        "Activity can lower glucose or unmask hypoglycemia when insulin or secretagogues are used, and foot protection and hydration remain important. Vigorous exercise above 400 mg/dL, skipped fluids, and open footwear create risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-063
    fact(
        "ccma-diabetes",
        "For many nonpregnant adults with diabetes, what hemoglobin A1C goal do ADA guidelines commonly cite when achievable without problematic hypoglycemia?",
        "Below 7% for many adults when reached without hypoglycemia risk",
        [
            "Below 4%, which is below typical laboratory reference ranges for adults",
            "At or above 8% for every adult regardless of comorbidities",
            "Based on fingerstick averages alone without laboratory A1C confirmation",
        ],
        "Targets are relaxed or tightened based on age, duration of disease, hypoglycemia risk, and life expectancy. A universal 8% target or fingerstick averages alone do not follow ADA guidance.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-064
    fact(
        "ccma-diabetes",
        "An adult with gradual hyperglycemia, positive islet autoantibodies, and eventual insulin requirement most likely has which condition?",
        "Latent autoimmune diabetes in adults, or LADA",
        [
            "Classic type 2 diabetes with insulin resistance and no autoantibodies",
            "Gestational diabetes that resolves after delivery",
            "Transient steroid hyperglycemia that resolves with the taper",
        ],
        "LADA bridges type 1 and type 2 phenotypes, and insulin is often needed earlier than in typical type 2 disease. Classic type 2, gestational diabetes, and steroid-induced hyperglycemia describe other presentations.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-065
    fact(
        "ccma-diabetes",
        "Which description best fits maturity-onset diabetes of the young (MODY)?",
        "A monogenic form of diabetes inherited in an autosomal dominant pattern",
        [
            "Obesity-induced hyperglycemia with no genetic component",
            "Autoimmune beta-cell destruction identical to classic type 1 in every case",
            "A diagnosis made solely from urine color or odor",
        ],
        "MODY can be mislabeled as type 1 or type 2, and family history and genetic testing guide correct management. Obesity-related hyperglycemia, autoimmune beta-cell loss, and urine color are not diagnostic features.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-066
    fact(
        "ccma-diabetes",
        "A patient started on prednisone for asthma reports rising fingerstick glucose. What is the most likely mechanism?",
        "Hepatic glucose production and insulin resistance from glucocorticoids",
        [
            "Direct beta-cell stimulation that lowers fasting glucose even without meals",
            "Hyperglycemia limited to patients with established autoimmune type 1 disease",
            "Glucose elevation confined to inhaled or topical steroids",
        ],
        "Systemic steroids commonly worsen glycemic control, and glucose monitoring and medication adjustment follow provider orders. Inhaled or topical steroids rarely cause this pattern, and beta-cell stimulation would lower glucose.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-067
    fact(
        "ccma-diabetes",
        "How can a history of recurrent acute pancreatitis relate to diabetes mellitus?",
        "Injury to pancreatic islet cells can reduce insulin secretion",
        [
            "Pancreatitis that produces hypoglycemia as the main pattern",
            "Pancreatic inflammation reliably lowers hemoglobin A1C",
            "There is no relationship between pancreas disease and glucose metabolism",
        ],
        "Both exocrine and endocrine pancreatic function may be impaired after severe or repeated pancreatitis. Hypoglycemia, lower A1C, and no link between the pancreas and glucose do not describe that injury.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-068
    fact(
        "ccma-diabetes",
        "How does cystic fibrosis-related diabetes (CFRD) differ from typical type 1 diabetes?",
        "It arises with cystic fibrosis and needs its own screening and care",
        [
            "It is identical to gestational diabetes that remits immediately after delivery",
            "It presents as acute autoimmune ketoacidosis during the first year of life",
            "It does not involve pancreatic endocrine function",
        ],
        "CFRD reflects progressive insulin deficiency in cystic fibrosis and is managed with specialized protocols. Gestational diabetes, infancy ketoacidosis, and normal endocrine function do not describe CFRD.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-069
    fact(
        "ccma-diabetes",
        "Before relying on hemoglobin A1C in a patient with sickle cell trait, what should the clinical team consider?",
        "Some A1C assays are inaccurate when hemoglobin variants are present",
        [
            "Hemoglobin variants alter fingerstick glucose but spare A1C assays",
            "Variants change cuff size needed for blood pressure measurement",
            "Variants interfere with urine ketone strips while leaving A1C assays unaffected",
        ],
        "When A1C may be unreliable, alternate diagnostic tests such as fasting glucose or OGTT are used per guidelines. Variants do not change cuff size, urine ketone strips, or fingerstick calibration.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-070
    fact(
        "ccma-diabetes",
        "How can iron-deficiency anemia influence interpretation of a hemoglobin A1C result?",
        "It may falsely raise or lower A1C with red cell turnover",
        [
            "Anemia has no effect on A1C because the assay measures plasma glucose",
            "Anemia distorts A1C in pregnancy but spares other adults",
            "Anemia yields an A1C that still tracks average glycemia",
        ],
        "Review hematologic conditions and assay limitations when A1C disagrees with daily glucose readings. Anemia that leaves A1C untouched, distorts only in pregnancy, or still tracks glycemia does not reflect the assay.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-071
    fact(
        "ccma-diabetes",
        "A patient has polyuria, polydipsia, and a random plasma glucose of 320 mg/dL. Under ADA criteria, what does this support?",
        "Diabetes mellitus without requiring a second confirmatory test",
        [
            "A normal glucose tolerance state requiring no follow-up",
            "Diagnosis requires a 75-g OGTT even with classic symptoms present",
            "Isolated hypoglycemia requiring carbohydrate restriction",
        ],
        "Unequivocal hyperglycemia with classic symptoms meets diagnostic thresholds on a single qualifying value. Normal tolerance, a required OGTT, or carbohydrate restriction for hypoglycemia does not apply here.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-072
    fact(
        "ccma-diabetes",
        "Per ADA guidance, which adults should be screened for type 2 diabetes even when asymptomatic?",
        "Those who are overweight or obese and have additional risk factors",
        [
            "All newborns before hospital discharge as the sole universal screen",
            "Patients already on basal-bolus insulin as the screening cohort",
            "Ambulatory screening is unnecessary because emergency rooms find it all",
        ],
        "Risk-based screening in ambulatory settings helps detect undiagnosed diabetes and prediabetes early. Universal newborn screening, established insulin users, and relying on emergency departments do not meet the recommendation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-073
    fact(
        "ccma-diabetes",
        "For a newly diagnosed adult with type 2 diabetes and no contraindication, what initial pharmacotherapy do guidelines most often recommend alongside lifestyle change?",
        "Metformin first line when renal function and other contraindications allow",
        [
            "Sliding-scale insulin as routine monotherapy for every new adult",
            "Systemic glucocorticoids to blunt postmeal glucose spikes",
            "Withholding therapy until A1C reaches 10% despite symptomatic hyperglycemia",
        ],
        "Metformin remains first-line for many patients because of efficacy, safety profile, and cardiovascular data when it is not contraindicated. Sliding-scale insulin, glucocorticoids, and delayed therapy are not first-line choices.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-074
    fact(
        "ccma-diabetes",
        "Which situation most commonly requires holding or not initiating metformin?",
        "Low eGFR below thresholds or acute illness with acidosis risk",
        [
            "Well-controlled hypertension on a single antihypertensive agent",
            "Age above 65 years in every patient regardless of kidney function",
            "Body mass index above 25 kg/m2 without other abnormalities",
        ],
        "Renal function, contrast procedures, and hemodynamic instability influence metformin safety per labeling and ADA guidance. Controlled hypertension, age alone, and body mass index do not require holding metformin.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-075
    fact(
        "ccma-diabetes",
        "Beyond lowering glucose, why might an SGLT2 inhibitor be selected for certain patients with type 2 diabetes?",
        "Cardiovascular and kidney protective benefits in eligible groups",
        [
            "Primary weight gain without an effect on glucose or cardiac endpoints",
            "Replacement of insulin therapy in type 1 autoimmune diabetes",
            "Relief from monitoring renal function or genital infection symptoms",
        ],
        "Clinicians balance glycemic effect with heart failure, ASCVD, and CKD indications while counseling on genital infections and rare euglycemic DKA. Weight gain, replacing insulin in type 1, and dropping monitoring do not apply.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-076
    fact(
        "ccma-diabetes",
        "What dual benefit do GLP-1 receptor agonists often provide in type 2 diabetes management?",
        "Improved glycemic control with weight reduction in many patients",
        [
            "Elimination of insulin needs in type 1 with one weekly injection",
            "Predictable hypoglycemia after every dose without regard to food",
            "Self-administration without teaching rotation or injection technique",
        ],
        "Nausea is common early, and slow titration with patient education improves tolerability. Replacing insulin in type 1, predictable hypoglycemia, and skipping technique teaching do not describe the benefits.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-077
    fact(
        "ccma-diabetes",
        "When reviewing a new prescription for glipizide, what hypoglycemia risk should the medical assistant reinforce with the patient?",
        "Insulin release continues even if the patient skips or delays a meal",
        [
            "Sulfonylureas block intestinal glucose absorption like alpha-glucosidase drugs",
            "They increase urinary glucose loss like SGLT2 inhibitors do",
            "They supply basal insulin coverage for a full 24 hours",
        ],
        "Secretagogues raise hypoglycemia risk, especially in older adults and those with irregular eating patterns. Blocking intestinal absorption, increasing urinary glucose loss, and providing basal insulin describe other drug classes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-078
    fact(
        "ccma-diabetes",
        "In a basal-bolus insulin plan, what role does once-daily glargine most often serve?",
        "Background insulin coverage between meals and overnight",
        [
            "A once-daily injection intended to cover mealtime spikes",
            "Automatic discontinuation during febrile illness without guidance",
            "Oral administration with breakfast using a nonformulary tablet preparation",
        ],
        "Basal insulin is paired with rapid insulin for meals and corrections per the individualized regimen. Covering mealtimes alone, stopping basal during illness, or oral administration is not the basal role.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-079
    fact(
        "ccma-diabetes",
        "When should rapid-acting insulin such as lispro typically be administered relative to a meal?",
        "Shortly before or with the meal to match the glucose rise",
        [
            "Once weekly at bedtime for every insulin regimen",
            "When the premeal glucose is below 70 mg/dL before carbohydrate",
            "As an oral tablet taken with water instead of an injection",
        ],
        "Matching insulin onset to carbohydrate absorption reduces postmeal hyperglycemia and late hypoglycemia. Weekly dosing, giving insulin when glucose is low, and oral tablets do not match mealtime practice.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-080
    fact(
        "ccma-diabetes",
        "How should unopened insulin vials or pens be stored under typical manufacturer directions?",
        "Refrigerated at 36°F to 46°F (2°C to 8°C) until the expiration date",
        [
            "Frozen at or below 0 degrees to preserve potency past the expiration date",
            "Kept in a hot vehicle glove compartment between clinic and home",
            "Stored on a sunny windowsill at room temperature before first patient use",
        ],
        "Heat and freezing denature insulin, and products that are expired, clumped, or discolored are discarded. Freezing, a hot glove compartment, and a sunny windowsill are unsafe storage conditions.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-081
    fact(
        "ccma-diabetes",
        "After an insulin vial or pen is opened for patient use, what storage practice is usually acceptable?",
        "Room temperature storage during the in-use period",
        [
            "Return the vial to freezer storage after each injection",
            "Heat the vial in boiling water before drawing each dose",
            "Share one pen device among household members to reduce waste",
        ],
        "Room-temperature in-use storage can reduce injection discomfort while respecting beyond-use dating on the label. Freezing, heating the vial, and sharing one pen between family members are not acceptable practice.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-082
    fact(
        "ccma-diabetes",
        "On a continuous glucose monitor display, what do rate-of-change arrows help the patient do?",
        "Anticipate highs or lows and respond per the action plan",
        [
            "Eliminate confirmatory fingersticks in every patient",
            "Ignore urgent low alerts because trend arrows are informational",
            "Defer diabetes follow-up because continuous data replaces review",
        ],
        "Trend information complements A1C and supports time-in-range goals when patients are trained on alarm responses. Dropping confirmatory checks, ignoring low alerts, and deferring follow-up are not appropriate uses of CGM.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-083
    fact(
        "ccma-diabetes",
        "For many adults using CGM, what time-in-range goal is commonly cited alongside A1C?",
        "At least about 70% of readings between 70 and 180 mg/dL",
        [
            "100% of readings below 70 mg/dL to maximize tight control",
            "Zero readings above 100 mg/dL during the daytime hours",
            "No glucose targets because CGM replaces laboratory monitoring entirely",
        ],
        "Time below range, variability, and A1C together describe glycemic control more completely than a single average. Readings kept entirely below 70 mg/dL or above 100 mg/dL at all times are not realistic targets.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-084
    fact(
        "ccma-diabetes",
        "Which laboratory pattern is most consistent with diabetic ketoacidosis (DKA)?",
        "Elevated glucose, positive ketones, and metabolic acidosis",
        [
            "Normoglycemia with absent ketones and a normal blood pH",
            "Isolated hypernatremia without raised glucose",
            "Primary respiratory alkalosis without an anion gap present",
        ],
        "DKA requires urgent inpatient management with fluids, insulin, electrolyte replacement, and monitoring for cerebral edema in children. Normoglycemia, hypernatremia alone, and respiratory alkalosis alone do not fit DKA.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-085
    fact(
        "ccma-diabetes",
        "Hyperosmolar hyperglycemic state (HHS) is most often seen in which clinical context?",
        "Older adults with type 2 diabetes, hyperglycemia, and dehydration",
        [
            "Otherwise healthy children with new-onset autoimmune type 1 diabetes",
            "Euglycemic patients without fluid losses",
            "Athletes immediately after moderate exercise with normal hydration",
        ],
        "HHS carries high mortality, and slow careful rehydration with insulin therapy occur in a monitored setting. Healthy children with new type 1, euglycemic patients, and athletes after exercise do not fit HHS.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-086
    fact(
        "ccma-diabetes",
        "Which sick-day instructions are appropriate for a patient on basal-bolus insulin who has fever and vomiting?",
        "Continue basal insulin, monitor glucose, and stay hydrated",
        [
            "Stop all insulin, including the basal dose, until intake returns",
            "Restrict fluids to prevent the worsening hyperglycemia",
            "Ignore moderate or large urine ketones during a febrile illness",
        ],
        "Counter-regulatory hormones during illness raise glucose, and withholding insulin increases ketosis and dehydration risk. Stopping insulin, restricting fluids, and ignoring urine ketones is not safe sick-day teaching.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-087
    fact(
        "ccma-diabetes",
        "When should urine ketone testing be emphasized for a patient with type 1 diabetes?",
        "During illness or when glucose stays high despite extra insulin",
        [
            "When the fingerstick glucose is below 70 mg/dL at a routine visit",
            "Whenever A1C is at goal and the patient reports feeling well",
            "Solely while fasting overnight for a routine chemistry panel",
        ],
        "Positive ketones with hyperglycemia may signal evolving DKA and need prompt provider contact. Routine low readings, an A1C at goal, and overnight fasting do not call for ketone testing.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-088
    fact(
        "ccma-diabetes",
        "For whom is a glucagon emergency kit primarily intended?",
        "Caregivers treating severe hypoglycemia when swallowing is unsafe",
        [
            "Alert patients with glucose 55 mg/dL who can drink juice or glucose gel",
            "Patients with persistent hyperglycemia above 300 mg/dL without acute symptoms",
            "Individuals starting metformin who need advice on side effects",
        ],
        "Train family or coworkers on administration, storage, and when to call emergency services after glucagon use. Juice or gel for alert patients, high glucose, and metformin counseling describe other situations.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-089
    fact(
        "ccma-diabetes",
        "What does impaired hypoglycemia awareness imply for a long-standing patient on insulin therapy?",
        "Warning signs such as tremor and sweating may be blunted at low glucose",
        [
            "Autonomic symptoms reliably occur whenever glucose is above 200 mg/dL",
            "The phenomenon occurs in diet-controlled type 2 disease",
            "Repeated untreated lows improve awareness over time without medical intervention",
        ],
        "Loss of warning symptoms raises the risk of severe hypoglycemia, and more frequent monitoring with therapy adjustment may be needed. Reliable symptoms above 200 mg/dL, diet-controlled type 2 disease, and improving awareness over time do not fit.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-090
    fact(
        "ccma-diabetes",
        "Why is carbohydrate counting taught to patients using mealtime rapid insulin?",
        "Dose aligns with carbohydrate grams per the insulin-to-carb ratio",
        [
            "It removes the need for pre- and postmeal glucose checks entirely",
            "It requires eliminating all starch and fruit from the diet permanently",
            "It replaces medical supervision and laboratory A1C monitoring",
        ],
        "Accurate carb estimates improve postprandial control and reduce mismatch between insulin peaks and glucose absorption. Removing glucose checks, banning starch and fruit, or dropping supervision does not describe carb counting.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-091
    fact(
        "ccma-diabetes",
        "What is the primary goal of medical nutrition therapy for a patient with diabetes?",
        "Individualized meal planning with portion control and balanced macronutrients",
        [
            "Applying one fad diet to every patient regardless of culture or comorbidities",
            "Allowing unlimited added sugar because metformin prevents hyperglycemia",
            "Eliminating all dietary fat without regard to cardiovascular risk",
        ],
        "The ADA supports flexible eating patterns tailored to preferences, culture, and glycemic targets. Registered dietitian referral helps align carbohydrate, protein, and fat with medications and activity.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-092
    fact(
        "ccma-diabetes",
        "A patient on insulin asks whether evening alcohol increases hypoglycemia risk. What should the medical assistant explain?",
        "Alcohol can cause delayed hypoglycemia with insulin therapy",
        [
            "Alcohol permanently raises the fasting glucose without later lows",
            "Alcohol has no interaction with diabetes medication or glucose monitoring",
            "Alcohol replaces the need for bedtime glucose checks",
        ],
        "Hepatic gluconeogenesis is impaired while alcohol is metabolized, which can drop glucose hours after drinking. Patients should eat if drinking, monitor glucose, and know when to seek help.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-093
    fact(
        "ccma-diabetes",
        "Why is smoking cessation counseling emphasized for patients with diabetes mellitus?",
        "It lowers cardiovascular and microvascular risk beyond lung cancer",
        [
            "It removes the need for annual diabetic foot examinations every year",
            "It guarantees normalization of kidney function without other treatments",
            "It affects lung cancer risk but not glucose-related vascular disease",
        ],
        "Tobacco accelerates atherosclerosis and worsens outcomes in diabetes, and cessation support is part of comprehensive risk reduction alongside blood pressure, lipid, and glycemic management. Dropping foot exams or curing kidney damage is not the benefit.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-094
    fact(
        "ccma-diabetes",
        "What condition is the main target of an annual dilated eye examination in a patient with diabetes?",
        "Diabetic retinopathy of the retina",
        [
            "Sensorineural hearing loss detected by audiometry",
            "Plantar foot ulceration without retinal evaluation",
            "Primary open-angle glaucoma without fundoscopic exam",
        ],
        "Retinopathy may progress before vision changes occur. Timely ophthalmology referral and glycemic control help preserve sight per ADA eye care intervals.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-095
    fact(
        "ccma-diabetes",
        "A urine albumin-to-creatinine ratio ordered for diabetes monitoring primarily assesses which complication?",
        "Early diabetic kidney disease",
        [
            "Thyroid hormone excess or deficiency",
            "Hepatic steatosis without renal involvement",
            "Diabetic retinopathy severity on fundoscopy",
        ],
        "Persistent albuminuria signals glomerular injury before serum creatinine rises sharply. Results guide ACE inhibitor or ARB therapy and nephrology referral when indicated.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-096
    fact(
        "ccma-diabetes",
        "Under current guidelines, when is an ACE inhibitor or angiotensin receptor blocker commonly indicated for a patient with diabetes?",
        "Hypertension or albuminuria without contraindications",
        [
            "Mild musculoskeletal pain without raised blood pressure",
            "As a direct substitute for the glucose-lowering agents",
            "Isolated hypoglycemia without renal or vascular damage",
        ],
        "These agents lower blood pressure and may slow progression of albuminuric kidney disease. Therapy is individualized for pregnancy status, potassium, and renal function.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-097
    fact(
        "ccma-diabetes",
        "For many adults with diabetes who are 40 years or older, why might moderate- or high-intensity statin therapy be prescribed?",
        "To reduce cardiovascular disease risk per guideline assessment",
        [
            "To intentionally raise LDL cholesterol to support energy metabolism",
            "To replace antihypertensive therapy when A1C is at goal",
            "To reverse established painful peripheral neuropathy",
        ],
        "Diabetes confers substantial ASCVD risk; statins are added when age, LDL, and comorbidities warrant. They complement, rather than replace, glycemic and blood pressure control.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-098
    fact(
        "ccma-diabetes",
        "For many adults with diabetes and hypertension, what blood pressure target is commonly used unless a lower goal is individualized?",
        "A blood pressure goal below 140/90 mmHg",
        [
            "Above 180/110 mmHg to maintain renal perfusion in every patient",
            "No routine measurement when the A1C is within goal",
            "Exactly 160/100 mmHg without regard to comorbidities",
        ],
        "Tighter targets such as below 130/80 mmHg may be appropriate when tolerated. Uncontrolled hypertension accelerates retinopathy, nephropathy, and macrovascular events.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "CDC: Measuring Blood Pressure — https://www.cdc.gov/high-blood-pressure/measure/index.html", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-099
    fact(
        "ccma-diabetes",
        "Which problems may result from diabetic autonomic neuropathy?",
        "Gastroparesis, orthostatic hypotension, or silent ischemia",
        [
            "Isolated loss of foot sensation without autonomic involvement",
            "Improved heart rate variability during standing",
            "Permanent cure of hyperglycemia without medication",
        ],
        "Autonomic fibers regulate GI motility, cardiovascular reflexes, and symptom perception. Recognition prompts targeted evaluation and therapy beyond foot sensory testing alone.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-100
    fact(
        "ccma-diabetes",
        "A patient reports burning and shooting pain in the feet with intact pulses. Which complication does this presentation suggest?",
        "Painful diabetic peripheral neuropathy",
        [
            "Acute compartment syndrome of the lower leg",
            "Improved protective sensation to thermal injury",
            "Tension-type headache unrelated to glucose control",
        ],
        "Painful neuropathy can coexist with numb areas and significantly affects sleep and function. Glycemic optimization and clinician-directed analgesic plans are typical management steps.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-101
    fact(
        "ccma-diabetes",
        "During a diabetic foot exam, what does testing with a 10-g monofilament primarily detect?",
        "Loss of protective sensation that raises ulcer risk",
        [
            "Central visual acuity for reading from a Snellen chart",
            "Peripheral oxygen saturation at the great toe",
            "Hearing thresholds in a quiet examination room",
        ],
        "Inability to feel the filament at standard sites suggests neuropathy. Combined with pulse checks and skin inspection, it guides ulcer prevention education and referrals.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-102
    fact(
        "ccma-diabetes",
        "Which teaching points belong in proper diabetes footwear and foot-care education?",
        "Well-fitting shoes, daily foot checks, and prompt care for breaks",
        [
            "Walking barefoot on hot pavement to toughen the soles",
            "Ignoring redness between toes until drainage appears",
            "Aggressive self-trimming of thickened nails when sensation is reduced",
        ],
        "Neuropathy and poor perfusion make minor trauma serious. Patients should report nonhealing lesions early to reduce amputation risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-103
    fact(
        "ccma-diabetes",
        "What is Charcot foot in the context of diabetes mellitus?",
        "Neuroarthropathy with bone and joint deformity in the foot",
        [
            "An uncomplicated ankle sprain without structural change",
            "Superficial cellulitis treated with topical antibiotic alone",
            "Normal age-related joint stiffness without neuropathy",
        ],
        "Repeated microtrauma in an insensate foot can collapse arch structure. Early immobilization, offloading, and specialist care help prevent severe deformity.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-104
    fact(
        "ccma-diabetes",
        "How are periodontal disease and diabetes related in outpatient care?",
        "They worsen each other through inflammation and glycemic control",
        [
            "They are unrelated conditions managed in separate silos",
            "Periodontal disease affects tooth appearance without metabolic impact",
            "Mouthwash alone reverses both gingivitis and insulin resistance",
        ],
        "Poor glycemic control increases infection risk in gums, and severe periodontitis can raise glucose. Dental referral and oral hygiene are part of comprehensive diabetes care.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-105
    fact(
        "ccma-diabetes",
        "What is a key message of preconception counseling for a woman with preexisting diabetes?",
        "Glycemic control before conception lowers birth defects",
        [
            "Defer all medical visits until after the delivery",
            "Focus on folic acid while ignoring the pre-pregnancy A1C",
            "Stop glucose monitoring once the pregnancy is confirmed",
        ],
        "Hyperglycemia during organogenesis raises teratogenic risk. Multidisciplinary planning includes medication review, A1C targets, and contraception until ready for pregnancy.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-106
    fact(
        "ccma-diabetes",
        "When is routine gestational diabetes screening typically performed in an uncomplicated pregnancy?",
        "Between 24 and 28 weeks gestation using a protocol-defined test",
        [
            "Immediately after hospital discharge following delivery",
            "In the first trimester for every patient without risk stratification",
            "When a prior cesarean birth is documented regardless of glucose history",
        ],
        "Earlier screening may be ordered when risk factors are present. Timely diagnosis allows nutrition, activity, and pharmacologic plans to reduce maternal and neonatal complications.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-107
    fact(
        "ccma-diabetes",
        "After delivery, what follow-up is recommended for a woman who had gestational diabetes mellitus?",
        "Postpartum testing for persistent diabetes or prediabetes",
        [
            "No further glucose assessment because the risk ends at delivery",
            "Newborn weight measurement without maternal metabolic testing",
            "Discontinuation of all nutrition and activity counseling",
        ],
        "GDM predicts later type 2 diabetes. Early lifestyle intervention and periodic screening support long-term health.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-108
    fact(
        "ccma-diabetes",
        "For a mother with diabetes who wishes to breastfeed, what guidance is appropriate?",
        "Breastfeeding is encouraged with medication adjustments",
        [
            "Breastfeeding is contraindicated for every insulin-treated mother",
            "Insulin must be discontinued for the entire lactation period",
            "Lactation eliminates the need to monitor for maternal hypoglycemia",
        ],
        "Lactation increases caloric needs and can lower glucose. Coordinating with the obstetric and diabetes teams helps balance infant nutrition and maternal safety.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-109
    fact(
        "ccma-diabetes",
        "Which accommodation may appear in a school or workplace diabetes management plan?",
        "Scheduled breaks for blood glucose monitoring and hypoglycemia treatment",
        [
            "Withholding access to glucose or glucagon during class or shifts",
            "Sharing one blood glucose meter among multiple students without cleaning",
            "Concealing the diagnosis from the school nurse or occupational health team",
        ],
        "Documented plans such as Section 504 or similar policies define who may assist with insulin, snacks, and emergency actions. Clear communication reduces safety gaps.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-110
    fact(
        "ccma-diabetes",
        "What driving safety advice should be reinforced for a patient treated with insulin or sulfonylureas?",
        "Stop driving, treat hypoglycemia, and recheck glucose before resuming",
        [
            "Check glucose when symptoms start and continue driving if values are borderline",
            "Eat a high-protein snack instead of fast-acting carbohydrate for lows",
            "Resume driving once symptoms ease without rechecking fingerstick glucose",
        ],
        "Even mild neuroglycopenia slows reaction time. Fast carbohydrate treats acute lows; protein does not raise glucose quickly, and symptom relief alone is not a safe cue to drive.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-111
    fact(
        "ccma-diabetes",
        "In which situation might an older adult with diabetes have a less stringent A1C goal than below 7%?",
        "Limited life expectancy, recurrent severe lows, or major illness",
        [
            "Newly diagnosed type 1 disease in a healthy adolescent athlete",
            "Pregnancy complicated by preexisting diabetes requiring tight control",
            "Asymptomatic prediabetes identified on routine screening",
        ],
        "Individualization balances microvascular benefit against fall and hypoglycemia harm. Shared decision-making documents the chosen target.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-112
    fact(
        "ccma-diabetes",
        "What backup plan should a patient using an insulin pump maintain?",
        "Injectable insulin and supplies to use if the pump malfunctions or is removed",
        [
            "No alternative therapy because pump failure is harmless overnight",
            "Relying on oral agents alone during pump interruption without a transition plan",
            "Borrowing another patient's pump cartridge without prescription review",
        ],
        "Interrupted insulin delivery in type 1 diabetes can lead to rapid hyperglycemia and ketosis. Patients should know when to switch to injections and whom to contact.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-113
    fact(
        "ccma-diabetes",
        "What capability can sensor-augmented insulin pump systems provide on approved devices?",
        "Temporary reduction of insulin delivery when a low is predicted",
        [
            "Elimination of all capillary glucose monitoring without clinician oversight",
            "Operation without user training or site rotation",
            "A guarantee that postmeal glucose will remain below 70 mg/dL",
        ],
        "Automated features supplement, not replace, self-management skills. Patients still need infusion set care, alarm responses, and periodic A1C review.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-114
    fact(
        "ccma-diabetes",
        "A patient on basal insulin has 3 a.m. readings of 95 to 110 mg/dL and fasting values of 185 to 205 mg/dL without documented overnight lows. What is the most likely cause of the morning hyperglycemia?",
        "Dawn phenomenon from early-morning counter-regulatory hormones",
        [
            "Somogyi rebound after unrecognized nocturnal hypoglycemia",
            "A missed evening dose of rapid-acting insulin at dinner",
            "Waning of bedtime intermediate insulin before the morning peak",
        ],
        "Stable overnight glucose with a morning rise fits physiologic dawn effect. Somogyi pattern would be preceded by lows; missed prandial insulin affects postmeal more than isolated fasting elevation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-115
    fact(
        "ccma-diabetes",
        "The historical Somogyi effect described which pattern?",
        "Rebound hyperglycemia after unrecognized nocturnal hypoglycemia",
        [
            "Stable overnight glucose without morning elevation",
            "Hyperglycemia limited to patients who do not use insulin",
            "A pattern with no relevance to current insulin dosing decisions",
        ],
        "Morning hyperglycemia has several causes, including insufficient basal insulin and the dawn phenomenon. Overnight glucose data help distinguish mechanisms.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, "MedlinePlus: Diabetes — https://medlineplus.gov/diabetes.html"],
        "advanced",
    ),
    # ccma-diabetes-116
    fact(
        "ccma-diabetes",
        "Which inpatient insulin strategy aligns with current hospital glycemic management recommendations?",
        "Scheduled basal insulin plus correction and meal coverage",
        [
            "Correction-scale insulin alone without basal coverage for type 1 diabetes",
            "Home insulin doses continued without physician review on admission",
            "Oral agents alone for a patient who is NPO without an alternative plan",
        ],
        "Basal insulin prevents ketosis and wide glucose swings. Nutrition changes, steroids, and procedures require coordinated order updates.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-117
    fact(
        "ccma-diabetes",
        "What is a primary goal of perioperative diabetes management?",
        "Preventing hypoglycemia and dangerous hyperglycemia around surgery",
        [
            "Withholding all glucose monitoring until the full oral diet resumes",
            "Maintaining glucose near 400 mg/dL to ensure adequate calories",
            "Restricting intravenous fluids to treat hyperglycemia",
        ],
        "Surgery, fasting, and stress hormones alter insulin needs. Anesthesia, surgery, and medicine teams coordinate timing of medications, fluids, and glucose checks.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-118
    fact(
        "ccma-diabetes",
        "A patient taking metformin is scheduled for iodinated contrast CT. What precaution is commonly required?",
        "Temporary metformin hold with renal function assessment",
        [
            "Doubling the metformin dose the morning of the scan",
            "Proceeding without reviewing estimated glomerular filtration rate",
            "Discontinuing intravenous hydration after contrast",
        ],
        "Contrast-associated acute kidney injury raises lactic acidosis risk with metformin in vulnerable patients. Protocols define when to restart the drug safely.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-119
    fact(
        "ccma-diabetes",
        "Why are influenza and pneumococcal vaccines recommended for many patients with diabetes?",
        "They reduce severe infection that destabilizes glycemic control",
        [
            "They are contraindicated because vaccines raise A1C permanently",
            "They replace the need for annual foot and eye screening",
            "They are indicated for pediatric patients but not adults with diabetes",
        ],
        "Infections provoke stress hyperglycemia and dehydration. Immunization schedules follow CDC guidance adapted to age and comorbidity.",
        [S.CDC_DIABETES, "CDC: Vaccine Administration — https://www.cdc.gov/vaccines/hcp/admin/index.html", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "beginner",
    ),
    # ccma-diabetes-120
    fact(
        "ccma-diabetes",
        "How does diabetes distress differ from major depressive disorder?",
        "It centers on the emotional burden of living with diabetes",
        [
            "It is identical to major depression and needs the same screening tools",
            "It has no effect on self-care behaviors or on appointment attendance",
            "It resolves without support once a glucometer is purchased",
        ],
        "Distress about regimens, costs, and fear of complications is common and distinct from mood disorder criteria alone. Brief screening and referral to behavioral health or DSMES can help.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, "MedlinePlus: Diabetes — https://medlineplus.gov/diabetes.html"],
        "intermediate",
    ),
    # ccma-diabetes-121
    fact(
        "ccma-diabetes",
        "When should diabetes self-management education and support (DSMES) be offered?",
        "At diagnosis and again when treatment or life circumstances change",
        [
            "Once at age 65 without follow-up when insulin is started",
            "For type 1 diabetes but not for type 2 diabetes",
            "After the patient reads informal online forums instead of structured teaching",
        ],
        "DSMES covers monitoring, medications, sick days, and prevention of complications. Revisiting skills improves safety when therapy intensifies.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-122
    fact(
        "ccma-diabetes",
        "A hospitalized patient on chronic prednisone receives a higher steroid dose for acute illness. What glucose-related action is needed?",
        "More frequent glucose monitoring with insulin adjustment by orders",
        [
            "Stopping capillary glucose checks because the steroids are short term",
            "Assuming glucocorticoids will lower blood glucose",
            "Documenting the dose change without notifying the diabetes team",
        ],
        "Glucocorticoids increase hepatic glucose output and insulin resistance. Hyperglycemia may persist until the taper ends.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-123
    fact(
        "ccma-diabetes",
        "Why is metabolic dysfunction-associated steatotic liver disease (MASLD) clinically important in type 2 diabetes?",
        "It may progress to fibrosis and cirrhosis, so weight matters",
        [
            "It cannot occur in patients with an elevated BMI and diabetes",
            "It is diagnosed exclusively with a monofilament foot examination",
            "It is cured by skipping breakfast without other interventions",
        ],
        "Fatty liver is common with insulin resistance. Screening and cardometabolic risk reduction address both hepatic and glycemic outcomes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-124
    fact(
        "ccma-diabetes",
        "How can hypothyroidism complicate diabetes care?",
        "It may worsen dyslipidemia and make glycemic control more difficult",
        [
            "It reliably improves insulin sensitivity without medication adjustment",
            "It removes the indication for periodic thyroid function tests",
            "It causes fixed hypoglycemia unaffected by thyroid replacement",
        ],
        "Autoimmune thyroid disease is more common with type 1 diabetes. Treating hypothyroidism supports lipid and glucose goals.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-125
    fact(
        "ccma-diabetes",
        "Why might celiac disease screening be considered in a patient with type 1 diabetes mellitus?",
        "Autoimmune disorders cluster, so celiac disease is considered",
        [
            "Celiac disease occurs exclusively in type 2 diabetes",
            "A negative screen replaces the ongoing A1C monitoring",
            "Gluten exposure has no impact on growth or glycemic variability",
        ],
        "Malabsorption can cause erratic carbohydrates and hypoglycemia. Positive serology prompts gastroenterology evaluation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-126
    fact(
        "ccma-diabetes",
        "What should an insulin-treated patient plan before international travel across time zones?",
        "Dose timing worked out with the care team before departure",
        [
            "Stopping basal insulin for the flight duration to prevent lows",
            "Storing all insulin in checked luggage exposed to cargo heat",
            "Ignoring meal timing because jet lag has no metabolic effect",
        ],
        "Eastward and westward travel shifts circadian insulin needs. Patients should carry supplies in hand luggage and know sick-day rules abroad.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-127
    fact(
        "ccma-diabetes",
        "The medical assistant finds expired blood glucose test strips in a clinic drawer. What is the appropriate action?",
        "Discard them because expired strips give inaccurate results",
        [
            "Use them if the vial color appears unchanged",
            "Transfer them to another patient's home kit to prevent waste",
            "Store future strips in a steamy bathroom for convenience",
        ],
        "Manufacturer expiration dates and dry storage protect enzyme activity, and inaccurate POC results can lead to incorrect treatment decisions. Using discolored strips or storing them in a humid room is not acceptable practice.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "beginner",
    ),
    # ccma-diabetes-128
    fact(
        "ccma-diabetes",
        "Why should a patient with diabetes inspect feet daily?",
        "Neuropathy can hide an injury until infection develops",
        [
            "Foot exams replace the HbA1c testing",
            "Shoes are unnecessary when the patient's vision is normal",
            "Glucose monitoring becomes optional after the first year",
        ],
        "Peripheral neuropathy reduces sensation, delaying wound care. Foot checks complement, not replace, glycemic monitoring and eye care.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-129
    fact(
        "ccma-diabetes",
        "Which finding during a foot exam should be reported promptly to the provider?",
        "A new open ulcer with surrounding redness and swelling",
        [
            "Toenails trimmed by the patient during the last week",
            "Normal skin temperature with symmetric warmth in both feet",
            "Presence of clean socks on the patient",
        ],
        "Open lesions with inflammation suggest infection risk in diabetes. Routine grooming or symmetric warmth are not acute warning signs.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-130
    fact(
        "ccma-diabetes",
        "A patient brings a personal blood glucose log to clinic. How should the team use it?",
        "Review patterns with the patient and share trends with the provider",
        [
            "Discard it without reading it in the usual outpatient clinic setting",
            "Post values on a public board",
            "Use it to bill without clinical review",
        ],
        "Home logs inform medication and lifestyle adjustments, and public display violates privacy while billing requires clinical relevance. Discarding the log without reading it does not help the patient.",
        [S.NHA_CCMA],
        "beginner",
    ),
]
