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
            "Acute urinary tract infection requiring antibiotics only",
            "Gallbladder inflammation on abdominal imaging",
            "Iron-deficiency anemia from chronic blood loss",
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
            "Exactly 140/90 mmHg only during annual wellness visits",
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
            "Direct measurement of arterial oxygen saturation",
            "Bone mineral density at the sensor insertion site",
            "Bacterial culture results from subcutaneous fluid",
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
            "Only when the patient lacks health insurance coverage",
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
            "Bradycardia and pinpoint pupils without acidosis",
            "A single maculopapular rash as the only abnormality",
        ],
        "DKA reflects insulin deficiency with lipolysis and ketone production; it is a medical emergency requiring IV fluids, insulin, and electrolyte monitoring.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-006
    fact(
        "ccma-diabetes",
        "On repeat testing, fasting plasma glucose at or above which value meets the ADA threshold for diabetes mellitus?",
        "126 mg/dL (7.0 mmol/L)",
        [
            "100 mg/dL (5.6 mmol/L), which defines prediabetes on FPG",
            "110 mg/dL regardless of symptoms or confirmatory testing",
            "200 mg/dL only when the patient is asymptomatic",
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
            "Hair color and nail polish shade only",
            "Visual acuity without inspecting the feet",
            "Hearing thresholds without monofilament testing",
        ],
        "Loss of protective sensation and poor circulation predispose to nonhealing ulcers and amputation; monofilament and pulse checks are routine components.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-008
    fact(
        "ccma-diabetes",
        "Using a standardized assay on repeat testing, hemoglobin A1C at or above which level indicates diabetes mellitus?",
        "6.5%",
        [
            "5.0%, which is within typical normal range",
            "5.7% from a single test without confirmation",
            "8.0% only when measured during pregnancy",
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
            "A high-fat cheese serving without carbohydrate",
            "A large mixed meal that delays glucose absorption",
            "No treatment until the next scheduled meal",
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
            "Below 5.0% in all adults",
            "8.0% or higher, which meets diabetes criteria",
            "Exactly 7.0% regardless of other test results",
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
            "Never, because diabetes alone excludes lipid-lowering therapy",
            "Only when fingerstick glucose is below 70 mg/dL",
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
            "Reversible hyperglycemia caused only by pregnancy hormones",
            "Primary dietary excess without any immune component",
        ],
        "Type 1 usually presents in younger patients and requires exogenous insulin for survival; autoantibody testing may support diagnosis.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-014
    fact(
        "ccma-diabetes",
        "Type 2 diabetes mellitus most commonly develops through which mechanism?",
        "Progressive insulin resistance with relative insulin secretory failure",
        [
            "Sudden autoimmune loss of all beta cells in infancy only",
            "Absence of blood glucose despite high dietary sugar intake",
            "Exclusive gestational hormone effects after delivery only",
        ],
        "Genetics, adiposity, and inactivity contribute to insulin resistance; oral agents and later insulin may be needed as beta-cell function declines.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-015
    fact(
        "ccma-diabetes",
        "For an insulin-treated patient following sick-day instructions during a febrile illness, which actions are typically emphasized?",
        "Continue basal insulin, check glucose and ketones often, and maintain hydration",
        [
            "Stop all insulin until appetite returns to normal",
            "Ignore urine ketones when nausea and vomiting occur",
            "Restrict oral fluids to prevent hyperglycemia",
        ],
        "Stress hormones raise glucose during illness; withholding insulin can worsen ketosis, while frequent monitoring guides supplemental doses per provider plan.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-016
    fact(
        "ccma-diabetes",
        "A newly diagnosed adolescent has positive pancreatic autoantibodies and requires insulin immediately. Which diabetes type does this presentation most suggest?",
        "Type 1 diabetes mellitus with autoimmune beta-cell destruction",
        [
            "Type 2 diabetes driven only by insulin resistance",
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
            "Hyperglycemia limited to the third trimester of pregnancy only",
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
            "Glucose intolerance that appears only after delivery",
            "Diagnosis based on a random fingerstick below 70 mg/dL",
            "A condition that guarantees normal glucose forever after birth",
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
        "On appropriate laboratory testing, diabetes mellitus is diagnosed when fasting plasma glucose is at least:",
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
            "Hypoglycemia requiring only fluid restriction",
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
        "After a 75-g oral glucose tolerance test (OGTT), diabetes is diagnosed when the 2-hour plasma glucose is:",
        "200 mg/dL (11.1 mmol/L) or higher",
        [
            "140 mg/dL, which may reflect impaired glucose tolerance",
            "100 mg/dL, within the prediabetes FPG range",
            "70 mg/dL or lower, consistent with hypoglycemia",
        ],
        "OGTT remains an ADA-listed criterion and may clarify diagnosis when FPG or A1C results are equivocal.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-024
    fact(
        "ccma-diabetes",
        "Which symptom cluster is classically associated with untreated hyperglycemia?",
        "Increased urination, increased thirst, and unexplained weight loss",
        [
            "Bradycardia with pinpoint pupils",
            "Sudden unresponsiveness in every hyperglycemic patient",
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
            "Patient requests a printed meal-plan handout",
            "Routine diabetic foot exam scheduled in two weeks",
            "A1C recheck due next month per care plan",
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
            "Only a 30-minute fast with all fluids withheld",
            "Doubling diabetes medications the morning of the draw",
        ],
        "Nonfasting samples can falsely lower or raise interpreted results; follow the laboratory requisition and facility protocol.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-028
    fact(
        "ccma-diabetes",
        "Per ADA guidance, treatment for hypoglycemia is generally initiated when blood glucose falls below:",
        "70 mg/dL (3.9 mmol/L)",
        [
            "200 mg/dL, which is above typical postmeal targets",
            "126 mg/dL, the diabetes diagnostic FPG threshold",
            "50 mg/dL only while the patient is asleep",
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
            "Withhold all food for 15 hours to reset insulin sensitivity",
            "Give 15 units of rapid-acting insulin subcutaneously",
            "Restrict oral fluids for 15 minutes after treatment",
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
            "Slow, deep respirations as the only symptom",
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
            "Pour juice into the mouth despite active gagging",
            "Leave the patient unattended until the next scheduled visit",
            "Administer rapid-acting insulin to raise counter-regulatory hormones",
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
        "advanced",
    ),
    # ccma-diabetes-033
    fact(
        "ccma-diabetes",
        "Hyperosmolar hyperglycemic state (HHS) is distinguished from DKA mainly by which features?",
        "Marked hyperglycemia and dehydration with little or no ketosis",
        [
            "Rapid onset limited to healthy school-age children",
            "Blood glucose consistently below 100 mg/dL",
            "Primary hypothermia without osmotic symptoms",
        ],
        "HHS often develops gradually in older adults with type 2 diabetes and carries high mortality without aggressive fluids and insulin in a monitored setting.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-034
    fact(
        "ccma-diabetes",
        "When DKA or HHS is suspected in the outpatient setting, what should the medical assistant do first?",
        "Notify the provider or emergency team promptly and monitor vital signs",
        [
            "Encourage a large meal to raise blood pressure",
            "Withhold all oral and intravenous fluids indefinitely",
            "Discharge the patient without further assessment",
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
            "High-complexity tests requiring a pathologist on site for every fingerstick",
            "Exempt from infection control and documentation standards",
            "Laboratory-developed tests with no FDA oversight",
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
            "Puncture the thumb without cleaning because capillary flow is faster",
            "Reuse the same lancet device on multiple patients to save supplies",
            "Proceed without verifying the patient name when the room is busy",
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
            "The center of the palm as the routine first choice",
            "The earlobe for every ambulatory adult without exception",
            "The heel, which is standard for all walking patients",
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
            "Skip control runs when patient volume is high",
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
            "6 to 8 hours after injection with no earlier effect",
            "24 hours later with no discernible peak",
            "Instantaneously with no peak or duration",
        ],
        "Mealtime analogs are given shortly before or with food so insulin action parallels postprandial glucose rise per the prescribed regimen.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-041
    fact(
        "ccma-diabetes",
        "When is regular (short-acting) human insulin expected to reach peak activity after subcutaneous injection?",
        "About 2 to 3 hours post-injection",
        [
            "Within 30 seconds of administration",
            "At 12 hours with no earlier onset",
            "Never; regular insulin has no peak effect",
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
            "Immediate onset with no measurable duration",
            "Intravenous push as the only approved route",
            "Mixing with oral metformin in one syringe without a provider order",
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
            "Replace all oral intake at meals",
            "Treat acute hypoglycemia as first-line therapy",
            "Resolve diabetic ketoacidosis without hospital care",
        ],
        "Basal-bolus regimens combine once- or twice-daily basal insulin with rapid insulin for carbohydrate coverage and corrections.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-044
    fact(
        "ccma-diabetes",
        "How should unopened and in-use insulin vials or pens be stored under typical manufacturer guidance?",
        "Refrigerate unopened product; after opening, store at controlled room temperature per label and discard after in-use days expire",
        [
            "Keep all insulin in direct sunlight to maintain potency",
            "Freeze vials and pens to extend beyond expiration",
            "Pool leftover insulin from multiple patients into one vial",
        ],
        "Heat, freezing, and prolonged room-temperature exposure degrade insulin; discard preparations that are expired, frosted, or discolored.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-045
    fact(
        "ccma-diabetes",
        "When assisting with insulin administration within scope, what must the medical assistant verify?",
        "The written order, patient identity, drug name, concentration, dose, route, site, and injection technique per protocol",
        [
            "An estimated dose when the syringe scale is hard to read",
            "That the same syringe may be used for multiple patients after wiping",
            "That air bubbles need not be removed before injection",
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
            "Stimulating unchecked insulin secretion regardless of glucose level",
            "Blocking all intestinal carbohydrate absorption",
            "Replacing endogenous insulin in type 1 autoimmune diabetes",
        ],
        "Metformin remains first-line pharmacotherapy for many adults with type 2 diabetes when renal function and other contraindications are absent.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-047
    fact(
        "ccma-diabetes",
        "Sulfonylureas such as glipizide lower blood glucose primarily by:",
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
            "Destroying pancreatic beta cells to stop insulin production",
            "Forcing exclusive fat metabolism without renal effects",
            "Raising glucagon while blocking all renal filtration",
        ],
        "Patients should report genital mycotic infections, volume depletion, or persistent nausea, because rare euglycemic ketoacidosis can occur.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-049
    fact(
        "ccma-diabetes",
        "GLP-1 receptor agonists improve glycemic control mainly by:",
        "Enhancing glucose-dependent insulin secretion and delaying gastric emptying",
        [
            "Replacing oral hydration with hypertonic saline only",
            "Mandating permanent fasting without medical supervision",
            "Removing the need for glucose monitoring entirely",
        ],
        "Injectable GLP-1 agents may also promote modest weight loss and carry gastrointestinal side effects that often lessen over time.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-050
    fact(
        "ccma-diabetes",
        "DPP-4 inhibitors such as sitagliptin act on glucose regulation by:",
        "Prolonging active incretin hormones that stimulate insulin in a glucose-dependent manner",
        [
            "Directly oxidizing adipose tissue without hormonal effects",
            "Blocking all insulin receptor signaling permanently",
            "Inducing ketoacidosis as an intended therapeutic effect",
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
            "Only footwear size for inventory purposes",
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
            "Isolated substernal chest pressure without extremity findings",
            "Heightened vibration sense and improved injury detection",
            "Guaranteed protection from foot ulcer formation",
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
            "A single random fingerstick without urinalysis",
            "Scalp hair mineral analysis as the primary screen",
            "No laboratory monitoring once diabetes is diagnosed",
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
            "It requires eliminating all dietary protein sources",
            "It mandates avoidance of nonstarchy vegetables entirely",
            "It replaces self-monitoring of blood glucose without provider input",
        ],
        "Registered dietitian nutritionists help patients interpret labels and portion sizes so postmeal glucose targets are more achievable.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-057
    fact(
        "ccma-diabetes",
        "Complete documentation of diabetes-related care in the medical record should include:",
        "Glucose values, relevant symptoms, interventions provided, and patient response",
        [
            "Only subjective food preferences without objective data",
            "Identifying details about unrelated patients in the same note",
            "Narrative entries that omit numeric results and times",
        ],
        "Accurate, timely charting supports safe handoffs, billing integrity, and quality measurement across the care team.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-058
    fact(
        "ccma-diabetes",
        "Independent adjustment of a patient's insulin doses by a medical assistant is:",
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
            "Stop all insulin until fever resolves completely",
            "Restrict fluids to force glucose downward",
            "Ignore vomiting or inability to keep fluids down",
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
            "It serves only as jewelry without clinical purpose",
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
        "Below 7%",
        [
            "Below 4%, which is below typical laboratory reference ranges",
            "At or above 8% for every adult regardless of comorbidities",
            "No A1C testing because fingersticks alone define control",
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
            "Classic type 2 diabetes with insulin resistance only and no immune markers",
            "Gestational diabetes that resolves after delivery",
            "Steroid-induced hyperglycemia that never needs insulin",
        ],
        "LADA bridges type 1 and type 2 phenotypes; insulin is often needed earlier than in typical type 2 disease.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-065
    fact(
        "ccma-diabetes",
        "Maturity-onset diabetes of the young (MODY) is best described as:",
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
            "Direct beta-cell stimulation that always lowers glucose",
            "Hyperglycemia limited to patients with type 1 diabetes only",
            "Glucose elevation only with topical steroids, never systemic therapy",
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
            "Pancreatitis always causes symptomatic hypoglycemia without hyperglycemia",
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
        "Cystic fibrosis-related diabetes (CFRD) differs from typical type 1 diabetes because:",
        "It arises in the setting of cystic fibrosis with distinct screening and treatment considerations",
        [
            "It is identical to gestational diabetes diagnosed only after delivery",
            "It always presents with acute autoimmune ketoacidosis in infancy only",
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
            "Hemoglobin variants affect only point-of-care fingerstick meters, never laboratory A1C",
            "Variants change cuff size needed for blood pressure measurement",
            "Variants make urine ketone strips read falsely low only",
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
            "Anemia never alters A1C because the test measures only plasma glucose",
            "Anemia affects A1C only during pregnancy and never in other adults",
            "Anemia always produces a true A1C that matches average glycemia",
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
            "Diagnosis only if a 75-g OGTT is performed and never with random glucose",
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
            "Only patients already using basal-bolus insulin therapy",
            "No adults in primary care because screening is emergency-department only",
        ],
        "Risk-based screening in ambulatory settings helps detect undiagnosed diabetes and prediabetes early.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-073
    fact(
        "ccma-diabetes",
        "For a newly diagnosed adult with type 2 diabetes and no contraindication, what initial pharmacotherapy do guidelines most often recommend alongside lifestyle change?",
        "Metformin",
        [
            "Scheduled sliding-scale insulin as the only agent for every new patient",
            "Systemic glucocorticoids to blunt postmeal glucose spikes",
            "Deferring all medication until A1C reaches 10% or higher",
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
            "Guaranteed weight gain that improves insulin sensitivity",
            "Curative replacement of insulin in type 1 diabetes",
            "Elimination of all need to monitor renal function or volume status",
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
            "Complete insulin independence for all patients with type 1 diabetes",
            "Mandatory symptomatic hypoglycemia at every dose",
            "Administration without teaching injection technique or site rotation",
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
            "Sulfonylureas block intestinal glucose absorption as their only action",
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
            "Coverage of mealtime carbohydrate spikes as the only injection",
            "Automatic discontinuation during febrile illness without provider input",
            "Oral administration with breakfast",
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
            "Only when fasting glucose is below 70 mg/dL",
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
            "Frozen solid to extend shelf life beyond the labeled date",
            "In a hot vehicle glove box during summer travel",
            "In direct sunlight on a windowsill at room temperature",
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
            "Ignore urgent low alerts because trends are decorative only",
            "Skip scheduled diabetes follow-up because data self-adjust therapy",
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
            "Otherwise healthy children with new-onset type 1 disease only",
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
            "Ignore moderate or large urine ketones because illness always lowers glucose",
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
            "Only when fingerstick glucose is below 70 mg/dL without symptoms",
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
            "Patients with mild hunger before lunch",
            "Anyone with a single reading above 300 mg/dL without symptoms",
            "Hypertensive emergencies in the clinic waiting room",
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
            "The phenomenon occurs only in diet-controlled type 2 diabetes never treated with insulin",
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
        "Medical nutrition therapy for diabetes emphasizes:",
        "Individualized macronutrient distribution and portion control",
        [
            "Single fad diet for all",
            "Unlimited sugar if on metformin",
            "Skipping all fat always",
        ],
        "ADA supports flexible eating patterns.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-092
    fact(
        "ccma-diabetes",
        "Alcohol use in diabetes can cause:",
        "Delayed hypoglycemia especially with insulin or secretagogues",
        [
            "Permanent hyperglycemia only",
            "Improved A1C always",
            "No interaction with meds",
        ],
        "Educate about food and monitoring with alcohol.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-093
    fact(
        "ccma-diabetes",
        "Smoking cessation in diabetes reduces:",
        "Cardiovascular and microvascular complication risk",
        [
            "Only lung cancer risk without glucose effect",
            "Need for foot exams",
            "Kidney function always worsens",
        ],
        "Smoking worsens vascular disease.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-094
    fact(
        "ccma-diabetes",
        "Annual dilated eye exam for diabetes screens for:",
        "Diabetic retinopathy",
        [
            "Glaucoma only without retina view",
            "Hearing loss",
            "Foot ulcers",
        ],
        "Early retinopathy may be asymptomatic.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-095
    fact(
        "ccma-diabetes",
        "Urine albumin-to-creatinine ratio monitors:",
        "Diabetic kidney disease",
        [
            "Retinopathy only",
            "Thyroid function",
            "Liver enzymes only",
        ],
        "Microalbuminuria precedes macroalbuminuria.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-096
    fact(
        "ccma-diabetes",
        "ACE inhibitor or ARB may be used in diabetes when:",
        "Hypertension or albuminuria is present per guidelines",
        [
            "Only for pain",
            "To lower glucose directly always",
            "Instead of all diabetes meds always",
        ],
        "Renoprotective benefits in albuminuric disease.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-097
    fact(
        "ccma-diabetes",
        "Statin therapy in diabetes over age 40 often aims to:",
        "Reduce ASCVD risk per guidelines",
        [
            "Raise LDL intentionally",
            "Replace blood pressure meds always",
            "Cure neuropathy",
        ],
        "Diabetes is ASCVD risk equivalent in many adults.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-098
    fact(
        "ccma-diabetes",
        "Blood pressure goal for many diabetes patients is:",
        "Below 140/90 mmHg unless lower target individualized",
        [
            "Always 180/110 mmHg",
            "Only measured yearly",
            "Ignored if A1C normal",
        ],
        "Hypertension accelerates complications.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "CDC: Measuring Blood Pressure — https://www.cdc.gov/high-blood-pressure/measure/index.html", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-099
    fact(
        "ccma-diabetes",
        "Diabetic autonomic neuropathy may cause:",
        "Gastroparesis, orthostatic hypotension, or silent ischemia",
        [
            "Only foot numbness never other systems",
            "Improved heart rate variability always",
            "Hyperglycemia cure",
        ],
        "Autonomic involvement affects multiple organs.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-100
    fact(
        "ccma-diabetes",
        "Painful diabetic peripheral neuropathy symptoms include:",
        "Burning, tingling, or shooting pain in feet or hands",
        [
            "Only painless ulcers always",
            "Improved sensation to injury",
            "Only headache",
        ],
        "Painful neuropathy affects quality of life.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-101
    fact(
        "ccma-diabetes",
        "Monofilament foot exam tests for:",
        "Loss of protective sensation",
        [
            "Visual acuity",
            "Pulse oximetry",
            "Hearing",
        ],
        "10-g monofilament identifies ulcer risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-102
    fact(
        "ccma-diabetes",
        "Proper diabetes footwear education includes:",
        "Well-fitting shoes, daily foot inspection, and prompt care for breaks in skin",
        [
            "Walking barefoot always",
            "Ignoring hot surfaces",
            "Cutting own thick nails if neuropathic without podiatry",
        ],
        "Ulcer prevention reduces amputations.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-103
    fact(
        "ccma-diabetes",
        "Charcot foot in diabetes is:",
        "Neuroarthropathy causing bone and joint deformity",
        [
            "Simple sprain only always",
            "Bacterial cellulitis only",
            "Normal aging",
        ],
        "Immobilization and offloading are critical.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-104
    fact(
        "ccma-diabetes",
        "Periodontal disease and diabetes:",
        "Have bidirectional relationship worsening glycemic control and gum disease",
        [
            "Are unrelated",
            "Only affect teeth cosmetically",
            "Cured by mouthwash alone",
        ],
        "Oral health is part of diabetes care.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-105
    fact(
        "ccma-diabetes",
        "Preconception counseling in diabetes emphasizes:",
        "Tight glycemic control before pregnancy to reduce malformations",
        [
            "Stopping all care until delivery",
            "A1C goals unimportant",
            "Only folic acid without glucose control",
        ],
        "Poor preconception control increases congenital risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-106
    fact(
        "ccma-diabetes",
        "Gestational diabetes screening is typically performed:",
        "At 24-28 weeks gestation with protocol-defined test",
        [
            "Only after delivery",
            "Never in overweight patients",
            "Only if prior C-section",
        ],
        "Early detection reduces complications.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-107
    fact(
        "ccma-diabetes",
        "Postpartum follow-up after gestational diabetes should include:",
        "Glucose testing to detect persistent diabetes or prediabetes",
        [
            "No further testing ever",
            "Only weight of baby",
            "Stopping all lifestyle advice",
        ],
        "GDM increases later type 2 risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-108
    fact(
        "ccma-diabetes",
        "Breastfeeding in mothers with diabetes:",
        "May improve maternal glucose and provides infant nutrition benefits",
        [
            "Is always contraindicated",
            "Requires stopping insulin always",
            "Worsens neonatal hypoglycemia always without monitoring",
        ],
        "Coordinate insulin needs with lactation.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-109
    fact(
        "ccma-diabetes",
        "School or work diabetes accommodations may include:",
        "Breaks for glucose monitoring and snack per documented plan",
        [
            "Hiding diabetes from school nurse always",
            "No access to glucose",
            "Sharing one glucometer unsanitized among students",
        ],
        "504 plans support safe management.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-110
    fact(
        "ccma-diabetes",
        "Driving safety with diabetes requires:",
        "Treating hypoglycemia before driving and monitoring as directed",
        [
            "Driving during severe hypoglycemia",
            "Skipping meals before long trips without plan",
            "Ignoring CGM low alerts",
        ],
        "Hypoglycemia impairs driving ability.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-111
    fact(
        "ccma-diabetes",
        "A1C goal may be relaxed in older adults with:",
        "Limited life expectancy, severe hypoglycemia history, or extensive comorbidities",
        [
            "Perfect health only",
            "All adolescents",
            "Every pregnancy first trimester only without nuance",
        ],
        "Individualization reduces harm.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-112
    fact(
        "ccma-diabetes",
        "Continuous subcutaneous insulin infusion (pump) users need backup:",
        "Long-acting insulin or rapid insulin and supplies if pump fails",
        [
            "No plan if pump stops",
            "Only oral meds if pump fails without transition plan",
            "Share pump among patients",
        ],
        "Pump failure risks DKA in type 1.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-113
    fact(
        "ccma-diabetes",
        "Sensor-augmented pump therapy can:",
        "Suspend insulin delivery for predicted hypoglycemia on some systems",
        [
            "Replace fingersticks and labs entirely always",
            "Operate without training",
            "Guarantee never high glucose",
        ],
        "Technology requires education and maintenance.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-114
    fact(
        "ccma-diabetes",
        "Dawn phenomenon refers to:",
        "Early morning rise in glucose from counter-regulatory hormones",
        [
            "Night hypoglycemia only always",
            "Allergic reaction to insulin",
            "Ketoacidosis only",
        ],
        "Basal insulin timing may be adjusted per team.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-115
    fact(
        "ccma-diabetes",
        "Somogyi effect (historical term) suggested:",
        "Rebound hyperglycemia after nocturnal hypoglycemia",
        [
            "Stable overnight glucose always",
            "Only in type 2 never",
            "No clinical relevance ever",
        ],
        "Nocturnal checks clarify morning highs.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, "MedlinePlus: Diabetes — https://medlineplus.gov/diabetes.html"],
        "advanced",
    ),
    # ccma-diabetes-116
    fact(
        "ccma-diabetes",
        "Hospital insulin orders should use:",
        "Scheduled basal plus correction and nutritional coverage per protocol",
        [
            "Sliding scale only without basal always",
            "Patient home doses without review",
            "Oral agents only in NPO patient without plan",
        ],
        "Inpatient glycemic management protocols improve safety.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-117
    fact(
        "ccma-diabetes",
        "Perioperative diabetes management aims to:",
        "Avoid hypoglycemia and extreme hyperglycemia around surgery",
        [
            "Stop all monitoring",
            "Target glucose 400 mg/dL",
            "Withhold all fluids",
        ],
        "Coordination among surgery, anesthesia, and medicine teams.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-118
    fact(
        "ccma-diabetes",
        "Contrast CT with metformin may require:",
        "Temporary hold and renal function check per facility protocol",
        [
            "Double metformin dose",
            "No kidney assessment ever",
            "Ignore eGFR",
        ],
        "Risk of lactic acidosis with renal impairment after contrast.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-119
    fact(
        "ccma-diabetes",
        "Flu and pneumococcal vaccines in diabetes:",
        "Recommended per immunization schedule to reduce severe infection",
        [
            "Contraindicated always",
            "Only for children",
            "Replace glucose monitoring",
        ],
        "Infections worsen glycemic control.",
        [S.CDC_DIABETES, "CDC: Vaccine Administration — https://www.cdc.gov/vaccines/hcp/admin/index.html", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "intermediate",
    ),
    # ccma-diabetes-120
    fact(
        "ccma-diabetes",
        "Diabetes distress differs from depression by:",
        "Focusing on emotional burden of self-management rather than solely mood disorder criteria",
        [
            "Being identical to major depression always",
            "Not affecting adherence",
            "Requiring no support",
        ],
        "Screening and referral help coping.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.CDC_DIABETES, "MedlinePlus: Diabetes — https://medlineplus.gov/diabetes.html"],
        "intermediate",
    ),
    # ccma-diabetes-121
    fact(
        "ccma-diabetes",
        "DSMES (diabetes self-management education and support) should be:",
        "Offered at diagnosis and thereafter when needed",
        [
            "One-time only at age 65",
            "Only for type 1",
            "Replaced by internet memes",
        ],
        "Education improves outcomes and safety.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-122
    fact(
        "ccma-diabetes",
        "Glucocorticoid dose increases in sick patients on steroids require:",
        "Glucose monitoring and insulin adjustment per provider",
        [
            "Stopping glucose checks",
            "Assuming steroids lower glucose",
            "No communication with team",
        ],
        "Steroids raise glucose unpredictably.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-123
    fact(
        "ccma-diabetes",
        "Fatty liver disease (NAFLD/MASLD) is common in type 2 diabetes and:",
        "May progress to fibrosis; lifestyle and weight management are key",
        [
            "Never occurs with diabetes",
            "Cured by skipping meals only",
            "Diagnosed only by foot exam",
        ],
        "Liver disease affects metabolic health.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-124
    fact(
        "ccma-diabetes",
        "Hypothyroidism in diabetes may:",
        "Worsen dyslipidemia and complicate glucose control",
        [
            "Improve insulin sensitivity always",
            "Eliminate need for thyroid screening",
            "Cause permanent hypoglycemia only",
        ],
        "Thyroid dysfunction is more common with diabetes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-125
    fact(
        "ccma-diabetes",
        "Celiac disease screening in type 1 diabetes:",
        "May be considered because of increased association",
        [
            "Never indicated",
            "Only if patient eats gluten freely without symptoms always skip",
            "Replaces A1C testing",
        ],
        "Autoimmune clustering occurs.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-126
    fact(
        "ccma-diabetes",
        "Travel across time zones with insulin requires:",
        "Plan for dose timing adjustments with diabetes team guidance",
        [
            "Stop insulin during flight always",
            "Store insulin in checked baggage uninsulated in heat",
            "Ignore meal timing",
        ],
        "Travel plans prevent hypo and hyperglycemia.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-127
    fact(
        "ccma-diabetes",
        "Expired diabetes test strips should be:",
        "Discarded; results may be inaccurate",
        [
            "Used if color looks fine",
            "Shared between patients",
            "Stored in humid bathroom",
        ],
        "Strip age and storage affect accuracy.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "beginner",
    ),
]
