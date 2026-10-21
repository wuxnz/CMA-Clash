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
            "Acute urinary tract infection with pyuria as the primary marker of diabetic kidney disease",
            "Elevated serum creatinine as the earliest sign before urinary protein changes",
            "Isolated hematuria on dipstick without measuring urinary albumin excretion",
        ],
        "Persistent albuminuria signals glomerular damage and guides ACE inhibitor or ARB therapy and nephrology referral per ADA kidney care standards.",
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
        "Hypertension and diabetes both raise atherosclerotic cardiovascular disease risk; tighter BP control is individualized but often aims near 130/80 mmHg.",
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
            "Urinary glucose on dipstick from the prior void without continuous interstitial readings",
        ],
        "CGM shows direction and rate of glucose change, helping patients and clinicians adjust therapy between laboratory A1C checks.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-004
    fact(
        "ccma-diabetes",
        "How should diabetes self-management education and support (DSMES) be offered across the care continuum?",
        "At diagnosis and whenever treatment, comorbidities, or life circumstances change",
        [
            "One group class at diagnosis with no follow-up education",
            "After insurance authorization is obtained, with no further sessions when therapy changes",
            "As a substitute for scheduled medical visits and laboratory monitoring",
        ],
        "DSMES teaches meal planning, glucose monitoring, and sick-day planning; revisiting skills improves adherence when regimens or goals shift.",
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
        "DKA reflects insulin deficiency with lipolysis and ketone production; it is a medical emergency requiring IV fluids, insulin, and electrolyte monitoring.",
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
            "200 mg/dL on a random sample without symptoms or confirmatory testing",
        ],
        "Unless unequivocal hyperglycemia with symptoms is present, diagnosis generally requires a second abnormal result or a different qualifying test.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-007
    fact(
        "ccma-diabetes",
        "During a comprehensive foot examination in a patient with diabetes, what should the clinician assess?",
        "Peripheral neuropathy, skin ulcers, and vascular perfusion",
        [
            "Hair color, nail polish shade, and cosmetic nail changes without monofilament testing",
            "Palpable pedal pulses without monofilament testing or skin inspection",
            "Footwear inspection without monofilament testing or vascular assessment",
        ],
        "Loss of protective sensation and poor circulation predispose to nonhealing ulcers and amputation; monofilament and pulse checks are routine components.",
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
        "A1C estimates average glycemia over roughly two to three months and is one of the ADA-listed diagnostic criteria when performed in a certified laboratory.",
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
        "The 15-15 approach raises glucose quickly; recheck in about 15 minutes and repeat if levels remain below 70 mg/dL per protocol.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-010
    fact(
        "ccma-diabetes",
        "Metformin is commonly withheld or dose-limited when which patient situation is present?",
        "Significant renal impairment or an acute illness that raises lactic acidosis risk",
        [
            "Mild dietary counseling without laboratory abnormalities",
            "Well-controlled hypertension on a single antihypertensive",
            "Routine self-monitoring of blood glucose with a glucometer",
        ],
        "Estimated glomerular filtration rate guides metformin prescribing; contrast studies and dehydration may also require temporary discontinuation per provider orders.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-011
    fact(
        "ccma-diabetes",
        "According to ADA categories, which A1C range most often defines prediabetes?",
        "5.7% to 6.4%",
        [
            "Below 5.0% in adults without other risk factors",
            "8.0% or higher, meeting diabetes diagnostic threshold",
            "Exactly 7.0% when fasting glucose and OGTT are normal",
        ],
        "Prediabetes carries higher future diabetes and cardiovascular risk; lifestyle programs and periodic rescreening are recommended.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-012
    fact(
        "ccma-diabetes",
        "When might a moderate- or high-intensity statin be recommended for an adult with diabetes?",
        "Based on age, ASCVD history, and additional risk factors per guidelines",
        [
            "Lipid-lowering therapy is withheld when diabetes is the sole cardiovascular risk factor",
            "When fingerstick glucose is below 70 mg/dL with documented symptomatic hypoglycemia",
            "Instead of any glucose or blood pressure monitoring",
        ],
        "Most adults with diabetes benefit from statin therapy when cardiovascular risk warrants it, alongside glycemic and blood pressure management.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-013
    fact(
        "ccma-diabetes",
        "Which pathophysiology best describes type 1 diabetes mellitus?",
        "Autoimmune destruction of pancreatic beta cells with absolute insulin deficiency",
        [
            "Isolated insulin resistance without beta-cell loss",
            "Reversible hyperglycemia from placental hormones during an uncomplicated pregnancy",
            "Primary dietary excess with preserved beta-cell mass and no autoimmunity",
        ],
        "Type 1 usually presents in younger patients and requires exogenous insulin for survival; autoantibody testing may support diagnosis.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-014
    fact(
        "ccma-diabetes",
        "Type 2 diabetes mellitus most commonly develops through which mechanism?",
        "Progressive insulin resistance with relative insulin secretory failure",
        [
            "Sudden autoimmune loss of pancreatic beta cells presenting in infancy",
            "Absence of blood glucose despite high dietary sugar intake",
            "Gestational hormone effects that persist after delivery without return to euglycemia",
        ],
        "Genetics, adiposity, and inactivity contribute to insulin resistance; oral agents and later insulin may be needed as beta-cell function declines.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-015
    fact(
        "ccma-diabetes",
        "For an insulin-treated patient following sick-day instructions during a febrile illness, which actions are typically emphasized?",
        "Continue basal insulin, monitor glucose and ketones, and maintain hydration",
        [
            "Stop all insulin until oral intake returns and omit ketone checks",
            "Ignore moderate or large urine ketones when nausea and vomiting occur",
            "Restrict oral fluids to limit hyperglycemia despite fever and vomiting",
        ],
        "Stress hormones raise glucose during illness; withholding insulin can worsen ketosis, while frequent monitoring guides supplemental doses per provider plan.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-016
    fact(
        "ccma-diabetes",
        "A newly diagnosed adolescent has positive pancreatic autoantibodies and requires insulin immediately. Which diabetes type does this presentation most suggest?",
        "Type 1 diabetes mellitus with autoimmune beta-cell destruction",
        [
            "Type 2 diabetes driven by insulin resistance without meaningful beta-cell failure",
            "Gestational diabetes that resolves after delivery",
            "Steroid-induced hyperglycemia without ongoing insulin need",
        ],
        "Type 1 results in little or no endogenous insulin; insulin therapy is essential from diagnosis in most cases.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-017
    fact(
        "ccma-diabetes",
        "An overweight adult develops gradual hyperglycemia and responds initially to metformin. Which underlying process is most likely?",
        "Insulin resistance with relative insulin deficiency over time",
        [
            "Acute autoimmune destruction of beta cells in infancy",
            "Complete absence of circulating glucose",
            "Hyperglycemia confined to the third trimester with normal prepregnancy glucose values",
        ],
        "Type 2 is the most common form in adults and may progress from lifestyle measures to oral agents and/or insulin.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-018
    fact(
        "ccma-diabetes",
        "How is gestational diabetes mellitus (GDM) distinguished from preexisting diabetes?",
        "Hyperglycemia first detected during pregnancy that was not overt diabetes before conception",
        [
            "Glucose intolerance that first appears during postpartum lactation",
            "Diagnosis based on a random fingerstick below 70 mg/dL",
            "Hyperglycemia during pregnancy assumed resolved after delivery without postpartum testing",
        ],
        "Obstetric screening between 24 and 28 weeks (or earlier with risk factors) identifies GDM; postpartum glucose testing is recommended.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
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
        "Prediabetes on FPG overlaps with impaired fasting glucose; confirmatory categories also use A1C and oral glucose tolerance testing.",
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
        "A second abnormal test or a different qualifying criterion is usually required unless classic hyperglycemic symptoms are present.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-021
    fact(
        "ccma-diabetes",
        "A standardized A1C result of 6.5% or higher on confirmatory testing indicates which diagnosis?",
        "Diabetes mellitus",
        [
            "Normal glucose metabolism",
            "Prediabetes without progression risk",
            "Hypoglycemia without meeting diabetes A1C criteria",
        ],
        "A1C reflects average glycemia over approximately two to three months and is listed among ADA diagnostic criteria.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-022
    fact(
        "ccma-diabetes",
        "Which A1C range is classified as prediabetes under ADA diagnostic categories?",
        "5.7% to 6.4%",
        [
            "Below 4.0%, below typical laboratory reference intervals",
            "6.5% or higher, which meets diabetes criteria",
            "8.0% or higher without symptoms",
        ],
        "Intensive lifestyle intervention can delay or prevent progression to type 2 diabetes in many individuals with prediabetes.",
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
        "OGTT remains an ADA-listed criterion and may clarify diagnosis when FPG or A1C results are equivocal.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
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
        "Polyuria and polydipsia result from osmotic diuresis; weight loss may occur despite polyphagia when insulin is insufficient.",
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
        "Severe hyperglycemia with altered mental status may signal DKA or hyperosmolar crisis and requires urgent clinical evaluation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-026
    fact(
        "ccma-diabetes",
        "Which combination of factors most increases risk for developing type 2 diabetes mellitus?",
        "Overweight or obesity, family history, and physical inactivity",
        [
            "Positive islet autoantibodies typical of type 1 disease",
            "Daily use of rapid-acting insulin from childhood",
            "Age under 2 years as the sole risk factor",
        ],
        "Modifiable risks include weight, activity, and cardiometabolic control; screening follows ADA recommendations for at-risk adults.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-027
    fact(
        "ccma-diabetes",
        "Before drawing blood for a fasting glucose ordered by the provider, what should the medical assistant verify with the patient?",
        "No caloric intake for at least 8 hours unless the order allows plain water",
        [
            "A full breakfast eaten within the past hour",
            "A brief 30-minute fast with withholding of water and morning diabetes medications",
            "Doubling diabetes medications the morning of the draw",
        ],
        "Nonfasting samples can falsely lower or raise interpreted results; follow the laboratory requisition and facility protocol.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-028
    fact(
        "ccma-diabetes",
        "Per ADA guidance, at which blood glucose level is treatment for hypoglycemia generally initiated?",
        "70 mg/dL (3.9 mmol/L)",
        [
            "200 mg/dL, which is above typical postmeal targets",
            "126 mg/dL, the diabetes diagnostic FPG threshold",
            "50 mg/dL overnight rechecked at breakfast without treating during the night",
        ],
        "Alert patients receive fast-acting carbohydrate; severe or unresponsive hypoglycemia triggers emergency protocols including glucagon when available.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-029
    fact(
        "ccma-diabetes",
        "When applying the 15-15 rule for mild hypoglycemia in a patient who can swallow, what should the medical assistant do?",
        "Administer about 15 grams of carbohydrate and recheck glucose in roughly 15 minutes",
        [
            "Wait 15 minutes before giving carbohydrate so symptoms can fully develop",
            "Give 15 grams of protein alone without rechecking glucose afterward",
            "Recheck glucose in 15 minutes without administering carbohydrate first",
        ],
        "If glucose remains low, repeat carbohydrate and notify the provider per facility policy; once stable, add a snack with protein if the next meal is delayed.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-030
    fact(
        "ccma-diabetes",
        "Which signs and symptoms may indicate hypoglycemia in a patient taking insulin or sulfonylureas?",
        "Shakiness, diaphoresis, irritability, and difficulty concentrating",
        [
            "Slow, deep respirations without shakiness, diaphoresis, or other autonomic symptoms",
            "Marked polyuria without thirst or autonomic symptoms",
            "Warm dry skin with severe hypertension exclusively",
        ],
        "Autonomic warning symptoms may be blunted in long-standing diabetes or neuropathy, so glucose checks should not rely on symptoms alone.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-031
    fact(
        "ccma-diabetes",
        "A conscious patient with hypoglycemia is vomiting and cannot swallow oral carbohydrate safely. What is the appropriate medical assistant action?",
        "Summon help immediately and follow facility emergency protocol without forcing oral glucose",
        [
            "Attempt oral glucose gel while the patient is actively vomiting",
            "Leave the patient alone to retrieve glucagon from the medication room",
            "Document the low reading and defer treatment until the next scheduled visit",
        ],
        "Aspiration risk outweighs oral treatment when swallowing is unsafe; severe hypoglycemia may require intramuscular glucagon or EMS activation per scope and standing orders.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-032
    fact(
        "ccma-diabetes",
        "Which laboratory and clinical pattern is characteristic of diabetic ketoacidosis (DKA)?",
        "Hyperglycemia with ketonemia or ketonuria and metabolic acidosis",
        [
            "Normoglycemia with absent ketones and normal pH",
            "Isolated hypoglycemia without acid-base disturbance",
            "Hypertension as the sole metabolic abnormality",
        ],
        "Insulin deficiency drives lipolysis and ketone production; DKA is most common in type 1 diabetes but can occur in type 2 under stress or illness.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
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
        "HHS often develops gradually in older adults with type 2 diabetes and carries high mortality without aggressive fluids and insulin in a monitored setting.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
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
        "Both syndromes need hospital-level fluid resuscitation, insulin therapy, electrolyte correction, and continuous monitoring rather than routine office management alone.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
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
        "Waived status still obligates trained operators, control testing, and policies that align with the Clinical Laboratory Improvement Amendments and facility protocols.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-036
    fact(
        "ccma-diabetes",
        "Which steps are required before performing a fingerstick glucose test in the clinic?",
        "Confirm patient identity, perform hand hygiene, don gloves, and prepare the puncture site per protocol",
        [
            "Puncture the thumb pad without site prep because capillary flow is faster",
            "Use the same lancet for repeat checks on one patient during the same visit",
            "Confirm identity verbally but omit hand hygiene when gloves are already worn",
        ],
        "Standard precautions and two-patient identifiers reduce wrong-patient errors and bloodborne pathogen transmission during waived testing.",
        ["CDC: Infection Control in Healthcare Settings (overview) — https://www.cdc.gov/infection-control/hcp/index.html", S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-037
    fact(
        "ccma-diabetes",
        "For an adult fingerstick glucose sample, which puncture site is generally preferred?",
        "The lateral aspect of the fingertip, avoiding cold, cyanotic, or edematous digits",
        [
            "The center of the palm as the routine first choice for capillary sampling",
            "The earlobe as the preferred site for routine adult glucose monitoring",
            "The heel as the primary puncture site for ambulatory adults in clinic",
        ],
        "Rotating fingers and matching lancet depth to skin thickness improve comfort and sample quality while limiting callus formation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-038
    fact(
        "ccma-diabetes",
        "What quality control practice is expected for waived glucose meters in clinical use?",
        "Run control solution on the schedule in policy and document each result",
        [
            "Defer control solution runs when clinic patient volume is high",
            "Use expired test strips if the vial seal looks intact",
            "Adjust calibration by estimating rather than following the manual",
        ],
        "Failed controls should halt patient testing until the device is troubleshooted or serviced according to manufacturer and laboratory director guidance.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-039
    fact(
        "ccma-diabetes",
        "A fingerstick glucose reading conflicts with the patient's symptoms and appearance. What should the medical assistant do?",
        "Repeat the test, confirm strip lot and technique, and report discrepancies to the provider",
        [
            "Chart the first value without rechecking to save time",
            "Omit the result from the record when it seems inconvenient",
            "Give insulin immediately based on a single unverified reading",
        ],
        "Critical or unexpected values trigger facility notification rules; repeating the measurement helps distinguish device error from true metabolic crisis.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
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
        "Mealtime analogs are given shortly before or with food so insulin action parallels postprandial glucose rise per the prescribed regimen.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-041
    fact(
        "ccma-diabetes",
        "When is regular (short-acting) human insulin expected to reach peak activity after subcutaneous injection?",
        "About 2 to 3 hours post-injection",
        [
            "Within 15 minutes, similar to rapid-acting insulin analogs given before meals",
            "Between 4 and 12 hours, overlapping the typical peak window for NPH insulin",
            "With no discernible peak because action is flat from injection to offset",
        ],
        "Onset is roughly 30 minutes and total duration is often 5 to 8 hours, so timing relative to meals and snacks must match the provider order.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-042
    fact(
        "ccma-diabetes",
        "Intermediate-acting NPH insulin is characterized by which pharmacokinetic profile?",
        "Onset in 1 to 2 hours, peak between 4 and 12 hours, duration up to about 24 hours",
        [
            "Onset within minutes and duration under one hour, like mealtime insulin analogs",
            "Peak activity near 30 to 60 minutes, similar to regular insulin given before meals",
            "Peakless basal coverage for roughly 24 hours, similar to insulin glargine",
        ],
        "NPH suspension appears cloudy and must be rolled gently to resuspend particles before drawing the dose into the syringe.",
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
        "Basal-bolus regimens combine once- or twice-daily basal insulin with rapid insulin for carbohydrate coverage and corrections.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-044
    fact(
        "ccma-diabetes",
        "How should unopened and in-use insulin vials or pens be stored under typical manufacturer guidance?",
        "Refrigerate unopened insulin; after opening, keep at room temperature per label until in-use days expire",
        [
            "Store unopened and in-use insulin in direct sunlight to maintain potency between doses",
            "Freeze unopened vials and thaw weekly to extend potency beyond the expiration date",
            "Combine leftover insulin from several patients into one shared vial to reduce waste",
        ],
        "Heat, freezing, and prolonged room-temperature exposure degrade insulin; discard preparations that are expired, frosted, or discolored.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-045
    fact(
        "ccma-diabetes",
        "When assisting with insulin administration within scope, what must the medical assistant verify?",
        "Written order, patient identity, drug name, concentration, dose, route, site, and technique per protocol",
        [
            "An estimated dose based on prior visits when the syringe scale is difficult to read",
            "That one insulin syringe may be used for multiple patients after wiping the needle with alcohol",
            "That small air bubbles in the syringe may be injected without attempting to remove them",
        ],
        "Insulin is a high-alert medication; many facilities require an independent double-check before subcutaneous injection.",
        ["FDA: Medication Safety Program — https://www.fda.gov/drugs/medication-safety-program", S.NHA_CCMA],
        "intermediate",
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
        "Metformin remains first-line pharmacotherapy for many adults with type 2 diabetes when renal function and other contraindications are absent.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-047
    fact(
        "ccma-diabetes",
        "How do sulfonylureas such as glipizide lower blood glucose?",
        "Stimulating insulin release from functioning pancreatic beta cells",
        [
            "Blocking renal sodium-glucose cotransport in the proximal tubule",
            "Serving as the sole inpatient treatment for diabetic ketoacidosis",
            "Eliminating hypoglycemia risk when taken without food",
        ],
        "Because secretion continues even when glucose is low, patients need education on recognizing and treating hypoglycemia, especially the elderly.",
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
        "Patients should report genital mycotic infections, volume depletion, or persistent nausea, because rare euglycemic ketoacidosis can occur.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-049
    fact(
        "ccma-diabetes",
        "How do GLP-1 receptor agonists improve glycemic control?",
        "Enhancing glucose-dependent insulin secretion and delaying gastric emptying",
        [
            "Replacing oral fluids with hypertonic saline as routine outpatient diabetes therapy",
            "Suppressing appetite through prolonged unsupervised fasting with limited hydration",
            "Making fingerstick and A1C monitoring unnecessary once the injection is started",
        ],
        "Injectable GLP-1 agents may also promote modest weight loss and carry gastrointestinal side effects that often lessen over time.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-050
    fact(
        "ccma-diabetes",
        "How do DPP-4 inhibitors such as sitagliptin affect glucose regulation?",
        "Prolonging active incretin hormones that stimulate insulin in a glucose-dependent manner",
        [
            "Mimicking GLP-1 agonist effects on gastric emptying without injectable dosing",
            "Blocking SGLT2 transporters to increase urinary glucose excretion",
            "Stimulating insulin secretion independent of glucose like a sulfonylurea",
        ],
        "These oral agents are generally weight-neutral and carry lower intrinsic hypoglycemia risk when not combined with secretagogues.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-051
    fact(
        "ccma-diabetes",
        "Before administering a prescribed diabetes medication, which patient information should the medical assistant review?",
        "Documented allergies, relevant renal or hepatic notes, and whether food is required with the dose",
        [
            "Footwear size for durable medical equipment inventory without allergy or renal review",
            "Patient preference for tablets over injections regardless of the order",
            "Unverified dosing suggestions from nonclinical sources",
        ],
        "Several classes need renal dose adjustment or are contraindicated with contrast, surgery, or acute illness per provider and pharmacy guidance.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-052
    fact(
        "ccma-diabetes",
        "Why is periodic diabetic retinopathy screening emphasized in chronic diabetes care?",
        "Microvascular eye disease may progress silently until vision is threatened",
        [
            "Dilated eye exams eliminate the need for foot surveillance",
            "Retinal screening cures hyperglycemia without other therapy",
            "A single childhood eye visit replaces all future diabetic eye care",
        ],
        "ADA guidelines recommend dilated eye evaluation intervals based on type of diabetes, prior findings, and pregnancy status.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-053
    fact(
        "ccma-diabetes",
        "Diabetic peripheral neuropathy commonly causes which patient-reported symptoms?",
        "Numbness, tingling, burning, or pain in the feet or hands",
        [
            "Isolated substernal chest pressure without numbness, tingling, or foot symptoms",
            "Heightened vibration sense with improved detection of hot surfaces and trauma",
            "Assurance that neuropathy prevents plantar ulcer formation despite poor glycemic control",
        ],
        "Loss of protective sensation increases ulcer and amputation risk; monofilament testing may be incorporated into comprehensive foot exams.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-054
    fact(
        "ccma-diabetes",
        "Which tests are routinely used to monitor diabetic kidney disease?",
        "Urine albumin-to-creatinine ratio and serum creatinine with estimated GFR",
        [
            "Annual fasting fingerstick without urinalysis or serum creatinine trend review",
            "Spot urine dipstick for protein without albumin-to-creatinine ratio or eGFR calculation",
            "Deferring renal laboratory monitoring once ACE inhibitor or ARB therapy is started",
        ],
        "Persistent albuminuria and declining eGFR guide ACE inhibitor or ARB therapy and nephrology referral when indicated.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-055
    fact(
        "ccma-diabetes",
        "What should daily self foot-care education stress for patients with diabetes?",
        "Inspect skin and nails, wear appropriate footwear, and report redness, breaks, or drainage promptly",
        [
            "Soak feet in very hot water daily without drying between toes",
            "Trim toenails into the corners to prevent ingrown nails",
            "Walk barefoot on hot or uneven surfaces to toughen skin",
        ],
        "Early referral for nonhealing wounds reduces progression to deep infection and lower-extremity amputation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-056
    fact(
        "ccma-diabetes",
        "How does carbohydrate counting support insulin or meal planning education?",
        "It aligns prandial insulin doses or oral regimens with anticipated carbohydrate intake",
        [
            "It matches prandial insulin units to counted carbohydrate grams at each meal",
            "It eliminates dietary protein to reduce gluconeogenesis without dietitian input",
            "It replaces self-monitoring of blood glucose without provider or educator input",
        ],
        "Registered dietitian nutritionists help patients interpret labels and portion sizes so postmeal glucose targets are more achievable.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-057
    fact(
        "ccma-diabetes",
        "Which elements belong in complete documentation of diabetes-related care in the medical record?",
        "Glucose values, relevant symptoms, interventions provided, and patient response",
        [
            "Diet preferences and meal timing without glucose values, symptoms, or interventions recorded",
            "Copy-forward narrative text that omits current glucose readings and intervention times",
            "Numeric glucose results without accompanying symptoms, actions taken, or patient response",
        ],
        "Accurate, timely charting supports safe handoffs, billing integrity, and quality measurement across the care team.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-058
    fact(
        "ccma-diabetes",
        "How is independent adjustment of a patient's insulin doses by a medical assistant classified under typical scope rules?",
        "Outside standard scope unless explicitly delegated by law and supervising clinician protocol",
        [
            "Expected at every visit without a provider order",
            "Permitted based on informal advice from nonclinical contacts",
            "Allowed without charting when the change seems minor",
        ],
        "Medication titration remains a licensed prescriber function unless state regulations and written delegation authorize otherwise.",
        [S.NHA_CCMA, "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "intermediate",
    ),
    # ccma-diabetes-059
    fact(
        "ccma-diabetes",
        "Sick-day teaching for insulin-treated patients typically emphasizes which actions?",
        "Continue basal insulin unless directed otherwise, check glucose frequently, test ketones if ordered, and maintain hydration",
        [
            "Hold all insulin, including basal doses, until the patient has been afebrile for 24 hours",
            "Restrict oral and intravenous fluids to lower glucose when the patient is thirsty",
            "Ignore repeated vomiting or inability to tolerate fluids while waiting for follow-up",
        ],
        "Counter-regulatory hormones during illness raise glucose and ketone risk; withholding insulin can worsen ketoacidosis while dehydration impairs perfusion.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-060
    fact(
        "ccma-diabetes",
        "Why should many people with diabetes wear medical identification such as a bracelet or necklace?",
        "It informs emergency personnel of diabetes and need for glucose monitoring or treatment",
        [
            "It eliminates the need for daily glucose checks at home",
            "Decorative jewelry worn for fashion without emergency medical information engraved",
            "It guarantees euglycemia during any acute illness",
        ],
        "Combined with patient education on when to seek urgent care, medical ID supports safer management when the patient cannot speak for themselves.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-061
    fact(
        "ccma-diabetes",
        "Why is treating hypertension a priority in a patient who already has diabetes mellitus?",
        "Elevated blood pressure multiplies cardiovascular and chronic kidney disease risk beyond glycemia alone",
        [
            "Normal blood pressure removes the need for dilated eye examinations",
            "Antihypertensive therapy prevents all diabetic peripheral neuropathy",
            "Once blood pressure is controlled, A1C targets no longer apply",
        ],
        "Diabetes and hypertension share vascular injury pathways; combined control reduces stroke, heart disease, and nephropathy progression.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-062
    fact(
        "ccma-diabetes",
        "When teaching a patient with diabetes about safe physical activity, what should the medical assistant emphasize?",
        "Check glucose before and after exercise and keep a fast-acting carbohydrate available",
        [
            "Exercise vigorously whenever glucose exceeds 400 mg/dL without contacting the care team",
            "Avoid all fluids during activity to limit hyperglycemia",
            "Wear open footwear during walks to improve circulation",
        ],
        "Activity can lower glucose or unmask hypoglycemia when insulin or secretagogues are used; foot protection and hydration remain important.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-063
    fact(
        "ccma-diabetes",
        "For many nonpregnant adults with diabetes, what hemoglobin A1C goal do ADA guidelines commonly cite when achievable without problematic hypoglycemia?",
        "Below 7% for many adults when it can be reached without excessive hypoglycemia risk",
        [
            "Below 4%, which is below typical laboratory reference ranges for adults",
            "At or above 8% for every adult regardless of age, comorbidities, or hypoglycemia risk",
            "Based on fingerstick averages alone without laboratory A1C confirmation",
        ],
        "Targets are relaxed or tightened based on age, duration of disease, hypoglycemia risk, and life expectancy.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-064
    fact(
        "ccma-diabetes",
        "An adult with gradual hyperglycemia, positive islet autoantibodies, and eventual insulin requirement most likely has which condition?",
        "Latent autoimmune diabetes in adults (LADA)",
        [
            "Classic type 2 diabetes with dominant insulin resistance and absent islet autoantibodies",
            "Gestational diabetes that resolves after delivery",
            "Transient steroid-induced hyperglycemia that resolves with taper and oral agents alone",
        ],
        "LADA bridges type 1 and type 2 phenotypes; insulin is often needed earlier than in typical type 2 disease.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-065
    fact(
        "ccma-diabetes",
        "Which description best fits maturity-onset diabetes of the young (MODY)?",
        "A monogenic form of diabetes often inherited in an autosomal dominant pattern",
        [
            "Obesity-induced hyperglycemia with no genetic component",
            "Autoimmune beta-cell destruction identical to classic type 1 in every case",
            "A diagnosis made solely from urine color or odor",
        ],
        "MODY can be mislabeled as type 1 or type 2; family history and genetic testing guide correct management.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-066
    fact(
        "ccma-diabetes",
        "A patient started on prednisone for asthma reports rising fingerstick glucose. What is the most likely mechanism?",
        "Increased hepatic glucose production and insulin resistance from glucocorticoids",
        [
            "Direct beta-cell stimulation that lowers fasting glucose even without meals",
            "Hyperglycemia limited to patients with established autoimmune type 1 disease",
            "Glucose elevation confined to inhaled or topical corticosteroids without systemic dosing",
        ],
        "Systemic steroids commonly worsen glycemic control; glucose monitoring and medication adjustment follow provider orders.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-067
    fact(
        "ccma-diabetes",
        "How can a history of recurrent acute pancreatitis relate to diabetes mellitus?",
        "Injury to pancreatic islet cells can reduce insulin secretion",
        [
            "Pancreatitis that produces symptomatic hypoglycemia as the primary glucose pattern",
            "Pancreatic inflammation reliably lowers hemoglobin A1C",
            "There is no relationship between pancreas disease and glucose metabolism",
        ],
        "Both exocrine and endocrine pancreatic function may be impaired after severe or repeated pancreatitis.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-068
    fact(
        "ccma-diabetes",
        "How does cystic fibrosis-related diabetes (CFRD) differ from typical type 1 diabetes?",
        "It arises in the setting of cystic fibrosis with distinct screening and treatment considerations",
        [
            "It is identical to gestational diabetes that remits immediately after delivery",
            "It presents as acute autoimmune ketoacidosis during the first year of life",
            "It does not involve pancreatic endocrine function",
        ],
        "CFRD reflects progressive insulin deficiency in cystic fibrosis and is managed with specialized protocols.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-069
    fact(
        "ccma-diabetes",
        "Before relying on hemoglobin A1C in a patient with sickle cell trait, what should the clinical team consider?",
        "Some A1C assays are inaccurate when hemoglobin variants are present",
        [
            "Hemoglobin variants alter fingerstick capillary glucose but spare laboratory A1C assays",
            "Variants change cuff size needed for blood pressure measurement",
            "Variants interfere with urine ketone strips while leaving A1C assays unaffected",
        ],
        "When A1C may be unreliable, alternate diagnostic tests such as fasting glucose or OGTT are used per guidelines.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-070
    fact(
        "ccma-diabetes",
        "How can iron-deficiency anemia influence interpretation of a hemoglobin A1C result?",
        "It may falsely raise or lower A1C depending on the assay and red cell turnover",
        [
            "Anemia has no effect on A1C because the assay quantifies plasma glucose rather than glycated hemoglobin",
            "Anemia distorts A1C in the third trimester but spares iron-deficient nonpregnant adults",
            "Anemia yields an A1C that tracks average glycemia despite altered red cell turnover",
        ],
        "Review hematologic conditions and assay limitations when A1C disagrees with daily glucose readings.",
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
            "Diagnosis requires a 75-g OGTT even when random glucose and classic symptoms are present",
            "Isolated hypoglycemia requiring carbohydrate restriction",
        ],
        "Unequivocal hyperglycemia with classic symptoms meets diagnostic thresholds on a single qualifying value.",
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
            "Patients already established on basal-bolus insulin as the primary screening cohort",
            "Ambulatory screening is unnecessary because emergency departments detect all adult diabetes",
        ],
        "Risk-based screening in ambulatory settings helps detect undiagnosed diabetes and prediabetes early.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-073
    fact(
        "ccma-diabetes",
        "For a newly diagnosed adult with type 2 diabetes and no contraindication, what initial pharmacotherapy do guidelines most often recommend alongside lifestyle change?",
        "Metformin as first-line pharmacotherapy when renal function and other contraindications are absent",
        [
            "Scheduled sliding-scale insulin as routine monotherapy for each newly diagnosed adult",
            "Systemic glucocorticoids to blunt postmeal glucose spikes in stable outpatient care",
            "Withholding pharmacotherapy until A1C reaches 10% despite symptomatic hyperglycemia",
        ],
        "Metformin remains first-line for many patients because of efficacy, safety profile, and cardiovascular data when not contraindicated.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-074
    fact(
        "ccma-diabetes",
        "Which situation most commonly requires holding or not initiating metformin?",
        "Estimated glomerular filtration rate below guideline thresholds or acute illness with lactic acidosis risk",
        [
            "Well-controlled hypertension on a single antihypertensive agent",
            "Age older than 65 years in every patient regardless of renal function",
            "Body mass index above 25 kg/m² without other abnormalities",
        ],
        "Renal function, contrast procedures, and hemodynamic instability influence metformin safety per labeling and ADA guidance.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-075
    fact(
        "ccma-diabetes",
        "Beyond lowering glucose, why might an SGLT2 inhibitor be selected for certain patients with type 2 diabetes?",
        "Demonstrated cardiovascular and kidney protective benefits in eligible high-risk groups",
        [
            "Primary weight gain without meaningful effect on glucose or cardiovascular endpoints",
            "Replacement of insulin therapy in type 1 autoimmune diabetes without concurrent insulin",
            "Relief from monitoring renal function, volume status, or genital infection symptoms",
        ],
        "Clinicians balance glycemic effect with heart failure, ASCVD, and CKD indications while counseling on genital infections and rare euglycemic DKA.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-076
    fact(
        "ccma-diabetes",
        "What dual benefit do GLP-1 receptor agonists often provide in type 2 diabetes management?",
        "Improved glycemic control with meaningful weight reduction in many patients",
        [
            "Elimination of insulin requirements in type 1 diabetes with a single weekly injection",
            "Predictable symptomatic hypoglycemia after every dose regardless of carbohydrate intake",
            "Self-administration without teaching site rotation, injection technique, or pen disposal",
        ],
        "Nausea is common early; slow titration and patient education improve tolerability.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-077
    fact(
        "ccma-diabetes",
        "When reviewing a new prescription for glipizide, what hypoglycemia risk should the medical assistant reinforce with the patient?",
        "Insulin release continues even if the patient skips or delays a meal",
        [
            "Sulfonylureas work chiefly by blocking intestinal glucose absorption like alpha-glucosidase inhibitors",
            "They increase urinary glucose loss like SGLT2 inhibitors",
            "They supply basal insulin coverage for 24 hours",
        ],
        "Secretagogues raise hypoglycemia risk, especially in older adults and those with irregular eating patterns.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-078
    fact(
        "ccma-diabetes",
        "In a basal-bolus insulin plan, what role does once-daily glargine most often serve?",
        "Background insulin between meals and overnight",
        [
            "A once-daily injection intended to cover mealtime spikes without separate bolus insulin",
            "Automatic discontinuation during febrile illness without provider or protocol guidance",
            "Oral administration with breakfast using a nonformulary tablet preparation",
        ],
        "Basal insulin is paired with rapid insulin for meals and corrections per the individualized regimen.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-079
    fact(
        "ccma-diabetes",
        "When should rapid-acting insulin such as lispro typically be administered relative to a meal?",
        "Shortly before or with the meal to match postprandial glucose rise",
        [
            "Once weekly at bedtime for all regimens",
            "When premeal fasting glucose is below 70 mg/dL regardless of planned carbohydrate",
            "As an oral tablet taken with water instead of injection",
        ],
        "Matching insulin onset to carbohydrate absorption reduces postmeal hyperglycemia and late hypoglycemia.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-080
    fact(
        "ccma-diabetes",
        "How should unopened insulin vials or pens be stored under typical manufacturer directions?",
        "Refrigerated at 36°F to 46°F (2°C to 8°C) until the expiration date",
        [
            "Frozen at or below 0°F (-18°C) to preserve potency past the labeled expiration date",
            "Kept in a hot vehicle glove compartment between clinic and home deliveries",
            "Stored on a sunny windowsill at room temperature before first patient use",
        ],
        "Heat and freezing denature insulin; discard products that are expired, clumped, or discolored.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-081
    fact(
        "ccma-diabetes",
        "After an insulin vial or pen is opened for patient use, what storage practice is usually acceptable?",
        "Room temperature storage for the in-use period allowed on the product label",
        [
            "Return to freezer storage after each injection",
            "Heat the vial in boiling water before drawing up each dose",
            "Share one pen device among household members to reduce waste",
        ],
        "Room-temperature in-use storage can reduce injection discomfort while respecting beyond-use dating on the label.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-082
    fact(
        "ccma-diabetes",
        "On a continuous glucose monitor display, what do rate-of-change arrows help the patient do?",
        "Anticipate impending highs or lows and respond per the action plan",
        [
            "Eliminate all confirmatory fingersticks in every patient without a provider order",
            "Ignore urgent low alerts because trend arrows are informational rather than actionable",
            "Defer scheduled diabetes follow-up because continuous data replaces clinician review",
        ],
        "Trend information complements A1C and supports time-in-range goals when patients are trained on alarm responses.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-083
    fact(
        "ccma-diabetes",
        "For many adults using CGM, what time-in-range goal is commonly cited alongside A1C?",
        "At least about 70% of readings between 70 and 180 mg/dL",
        [
            "100% of readings below 70 mg/dL to maximize tight control",
            "Zero readings above 100 mg/dL at any time of day",
            "No glucose targets because CGM replaces laboratory monitoring entirely",
        ],
        "Time below range, variability, and A1C together describe glycemic control more completely than a single average.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-084
    fact(
        "ccma-diabetes",
        "Which laboratory pattern is most consistent with diabetic ketoacidosis (DKA)?",
        "Elevated glucose, positive serum or urine ketones, and metabolic acidosis",
        [
            "Normoglycemia with absent ketones and normal pH",
            "Isolated hypernatremia without glucose elevation",
            "Primary respiratory alkalosis without an anion gap",
        ],
        "DKA requires urgent inpatient management with fluids, insulin, electrolyte replacement, and monitoring for cerebral edema in children.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-085
    fact(
        "ccma-diabetes",
        "Hyperosmolar hyperglycemic state (HHS) is most often seen in which clinical context?",
        "Older adults with type 2 diabetes, extreme hyperglycemia, and profound dehydration",
        [
            "Otherwise healthy children with new-onset autoimmune type 1 diabetes",
            "Euglycemic patients without fluid losses",
            "Athletes immediately after moderate exercise with normal hydration",
        ],
        "HHS carries high mortality; slow careful rehydration and insulin therapy occur in a monitored setting.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-086
    fact(
        "ccma-diabetes",
        "Which sick-day instructions are appropriate for a patient on basal-bolus insulin who has fever and vomiting?",
        "Continue basal insulin, check glucose frequently, maintain hydration, and call the team for persistent ketones or inability to keep fluids down",
        [
            "Stop all insulin until oral intake returns to normal",
            "Restrict fluids to prevent worsening hyperglycemia",
            "Ignore moderate or large urine ketones because intercurrent illness predictably lowers glucose",
        ],
        "Counter-regulatory hormones during illness raise glucose; withholding insulin increases ketosis and dehydration risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-087
    fact(
        "ccma-diabetes",
        "When should urine ketone testing be emphasized for a patient with type 1 diabetes?",
        "During illness or when blood glucose stays elevated despite extra insulin per the plan",
        [
            "When fingerstick glucose is below 70 mg/dL in an asymptomatic patient at routine checks",
            "Whenever A1C is at goal and the patient feels well",
            "Solely while fasting overnight for a routine chemistry panel",
        ],
        "Positive ketones with hyperglycemia may signal evolving DKA and need prompt provider contact.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-088
    fact(
        "ccma-diabetes",
        "For whom is a glucagon emergency kit primarily intended?",
        "Caregivers treating severe hypoglycemia when the patient cannot safely swallow carbohydrate",
        [
            "Alert patients with glucose 55 mg/dL who can drink juice or glucose gel",
            "Patients with persistent hyperglycemia above 300 mg/dL without acute symptoms",
            "Individuals starting metformin who need education on gastrointestinal side effects",
        ],
        "Train family or coworkers on administration, storage, and when to call emergency services after glucagon use.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-089
    fact(
        "ccma-diabetes",
        "What does impaired hypoglycemia awareness imply for a long-standing patient on insulin therapy?",
        "Warning signs such as tremor and sweating may be blunted at low glucose levels",
        [
            "Autonomic symptoms reliably occur whenever glucose is above 200 mg/dL",
            "The phenomenon occurs in diet-controlled type 2 disease without prior insulin therapy",
            "Repeated untreated lows improve awareness over time without medical intervention",
        ],
        "Loss of warning symptoms raises the risk of severe hypoglycemia; more frequent monitoring and therapy adjustment may be needed.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-090
    fact(
        "ccma-diabetes",
        "Why is carbohydrate counting taught to patients using mealtime rapid insulin?",
        "Dose can be aligned with anticipated carbohydrate grams per the insulin-to-carb ratio",
        [
            "It removes the need for pre- and postmeal glucose checks entirely",
            "It requires eliminating all starch and fruit from the diet permanently",
            "It replaces medical supervision and laboratory A1C monitoring",
        ],
        "Accurate carb estimates improve postprandial control and reduce mismatch between insulin peaks and glucose absorption.",
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
        "Alcohol can cause delayed hypoglycemia, especially with insulin or insulin secretagogues",
        [
            "Alcohol permanently raises fasting glucose without later lows",
            "Alcohol has no interaction with diabetes medications or monitoring",
            "Alcohol replaces the need for bedtime glucose checks",
        ],
        "Hepatic gluconeogenesis is impaired while alcohol is metabolized, which can drop glucose hours after drinking. Patients should eat if drinking, monitor glucose, and know when to seek help.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-093
    fact(
        "ccma-diabetes",
        "Why is smoking cessation counseling emphasized for patients with diabetes mellitus?",
        "It lowers cardiovascular and microvascular complication risk beyond lung cancer alone",
        [
            "It removes the need for annual diabetic foot examinations",
            "It guarantees normalization of kidney function without other therapy",
            "It affects lung cancer risk but not glucose-related vascular disease",
        ],
        "Tobacco accelerates atherosclerosis and worsens outcomes in diabetes. Cessation support is part of comprehensive risk reduction alongside blood pressure, lipid, and glycemic management.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-094
    fact(
        "ccma-diabetes",
        "What condition is the main target of an annual dilated eye examination in a patient with diabetes?",
        "Diabetic retinopathy",
        [
            "Sensorineural hearing loss detected by audiometry",
            "Plantar foot ulceration without retinal evaluation",
            "Primary open-angle glaucoma without fundoscopic exam",
        ],
        "Retinopathy may progress before vision changes occur. Timely ophthalmology referral and glycemic control help preserve sight per ADA eye care intervals.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
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
        "Hypertension or albuminuria is present and not contraindicated",
        [
            "Mild musculoskeletal pain without blood pressure elevation",
            "As a direct substitute for all glucose-lowering agents",
            "Isolated hypoglycemia without renal or vascular disease",
        ],
        "These agents lower blood pressure and may slow progression of albuminuric kidney disease. Therapy is individualized for pregnancy status, potassium, and renal function.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-097
    fact(
        "ccma-diabetes",
        "For many adults with diabetes who are 40 years or older, why might moderate- or high-intensity statin therapy be prescribed?",
        "To reduce atherosclerotic cardiovascular disease risk per guideline-based assessment",
        [
            "To intentionally raise LDL cholesterol for energy metabolism",
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
        "Below 140/90 mmHg",
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
        "Gastroparesis, orthostatic hypotension, or silent myocardial ischemia",
        [
            "Isolated loss of foot sensation without autonomic involvement",
            "Improved heart rate variability during standing",
            "Permanent cure of hyperglycemia without medication",
        ],
        "Autonomic fibers regulate GI motility, cardiovascular reflexes, and symptom perception. Recognition prompts targeted evaluation and therapy beyond foot sensory testing alone.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
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
        "Loss of protective sensation that increases ulcer risk",
        [
            "Central visual acuity for reading a Snellen chart",
            "Peripheral oxygen saturation at the great toe",
            "Hearing thresholds in a quiet examination room",
        ],
        "Inability to feel the filament at standard sites suggests neuropathy. Combined with pulse checks and skin inspection, it guides ulcer prevention education and referrals.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-102
    fact(
        "ccma-diabetes",
        "Which teaching points belong in proper diabetes footwear and foot-care education?",
        "Well-fitting shoes, daily foot inspection, and prompt care for skin breaks",
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
        "Neuroarthropathy with bone and joint deformity in a neuropathic foot",
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
        "They worsen each other through bidirectional effects on inflammation and glycemic control",
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
        "Achieve tight glycemic control before conception to lower congenital malformation risk",
        [
            "Defer all medical visits until after delivery",
            "Focus on folic acid while ignoring pre-pregnancy A1C",
            "Stop glucose monitoring once pregnancy is confirmed",
        ],
        "Hyperglycemia during organogenesis raises teratogenic risk. Multidisciplinary planning includes medication review, A1C targets, and contraception until ready for pregnancy.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
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
        "intermediate",
    ),
    # ccma-diabetes-107
    fact(
        "ccma-diabetes",
        "After delivery, what follow-up is recommended for a woman who had gestational diabetes mellitus?",
        "Postpartum glucose testing to detect persistent diabetes or prediabetes",
        [
            "No further glucose assessment because risk ends at delivery",
            "Neonatal weight measurement without maternal metabolic testing",
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
        "Breastfeeding is encouraged with insulin or medication adjustments and glucose monitoring",
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
        "intermediate",
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
        "Limited life expectancy, recurrent severe hypoglycemia, or major comorbid illness",
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
        "advanced",
    ),
    # ccma-diabetes-113
    fact(
        "ccma-diabetes",
        "What capability can sensor-augmented insulin pump systems provide on approved devices?",
        "Temporary suspension or reduction of insulin delivery when hypoglycemia is predicted",
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
            "Hyperglycemia limited to patients who do not use any insulin",
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
        "Scheduled basal insulin plus correction and meal coverage per protocol",
        [
            "Correction-scale insulin alone without basal coverage for type 1 diabetes",
            "Home insulin doses continued without physician review on admission",
            "Oral agents alone for a patient who is NPO without an alternative plan",
        ],
        "Basal insulin prevents ketosis and wide glucose swings. Nutrition changes, steroids, and procedures require coordinated order updates.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-117
    fact(
        "ccma-diabetes",
        "What is a primary goal of perioperative diabetes management?",
        "Preventing symptomatic hypoglycemia and dangerous hyperglycemia around the procedure",
        [
            "Withholding all glucose monitoring until full oral diet resumes",
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
        "Temporary metformin hold with renal function assessment per facility protocol",
        [
            "Doubling the metformin dose the morning of the scan",
            "Proceeding without reviewing estimated glomerular filtration rate",
            "Discontinuing intravenous hydration after contrast",
        ],
        "Contrast-associated acute kidney injury raises lactic acidosis risk with metformin in vulnerable patients. Protocols define when to restart the drug safely.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-119
    fact(
        "ccma-diabetes",
        "Why are influenza and pneumococcal vaccines recommended for many patients with diabetes?",
        "They reduce risk of severe infection that can destabilize glycemic control",
        [
            "They are contraindicated because vaccines raise A1C permanently",
            "They replace the need for annual foot and eye screening",
            "They are indicated for pediatric patients but not adults with diabetes",
        ],
        "Infections provoke stress hyperglycemia and dehydration. Immunization schedules follow CDC guidance adapted to age and comorbidity.",
        [S.CDC_DIABETES, "CDC: Vaccine Administration — https://www.cdc.gov/vaccines/hcp/admin/index.html", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "intermediate",
    ),
    # ccma-diabetes-120
    fact(
        "ccma-diabetes",
        "How does diabetes distress differ from major depressive disorder?",
        "It centers on the emotional burden of living with and managing diabetes",
        [
            "It is identical to major depression and requires the same screening tools without context",
            "It has no effect on self-care behaviors or appointment attendance",
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
        "At diagnosis and again when treatment, comorbidities, or life circumstances change",
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
        "More frequent glucose monitoring with insulin adjustments per provider orders",
        [
            "Stopping capillary glucose checks because steroids are short term",
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
        "It may progress to fibrosis and cirrhosis, so weight and lifestyle management matter",
        [
            "It cannot occur in patients with elevated BMI and diabetes",
            "It is diagnosed exclusively with a monofilament foot examination",
            "It is cured by skipping breakfast without other intervention",
        ],
        "Fatty liver is common with insulin resistance. Screening and cardometabolic risk reduction address both hepatic and glycemic outcomes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
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
        "Autoimmune disorders cluster, and untreated celiac disease affects nutrition and glucose",
        [
            "Celiac disease occurs exclusively in type 2 diabetes",
            "A negative screen replaces ongoing A1C monitoring",
            "Gluten exposure has no impact on growth or glycemic variability",
        ],
        "Malabsorption can cause erratic carbohydrates and hypoglycemia. Positive serology prompts gastroenterology evaluation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-126
    fact(
        "ccma-diabetes",
        "What should an insulin-treated patient plan before international travel across time zones?",
        "Dose timing adjustments worked out with the diabetes care team before departure",
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
        "Discard them because expired strips may give inaccurate results",
        [
            "Use them if the vial color appears unchanged",
            "Transfer them to another patient's home kit to avoid waste",
            "Store future strips in a steamy bathroom for convenience",
        ],
        "Manufacturer expiration dates and dry storage protect enzyme activity. Inaccurate POC results can lead to incorrect treatment decisions.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "beginner",
    ),
    # ccma-diabetes-128
    fact(
        "ccma-diabetes",
        "Why should a patient with diabetes inspect feet daily?",
        "Neuropathy can hide injury until infection develops",
        [
            "Foot exams replace HbA1c testing",
            "Shoes are unnecessary if vision is normal",
            "Glucose monitoring becomes optional",
        ],
        "Peripheral neuropathy reduces sensation, delaying wound care. Foot checks complement, not replace, glycemic monitoring and eye care.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-129
    fact(
        "ccma-diabetes",
        "Which finding during a foot exam should be reported promptly to the provider?",
        "A new open ulcer with surrounding erythema",
        [
            "Trimmed toenails from last week",
            "Normal skin temperature symmetry",
            "Presence of socks",
        ],
        "Open lesions with inflammation suggest infection risk in diabetes. Routine grooming or symmetric warmth are not acute warning signs.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-130
    fact(
        "ccma-diabetes",
        "A patient brings a personal blood glucose log to clinic. How should the team use it?",
        "Review patterns with the patient and share relevant trends with the provider",
        [
            "Discard it without reading",
            "Post values on a public board",
            "Use it to bill without clinical review",
        ],
        "Home logs inform medication and lifestyle adjustments. Public display violates privacy; billing requires clinical relevance.",
        [S.NHA_CCMA],
        "beginner",
    ),
]
