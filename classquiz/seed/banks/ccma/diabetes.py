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
        "If a conscious patient with hypoglycemia cannot swallow safely, the MA should:",
        "Call for help and follow emergency protocol; do not force oral glucose",
        [
            "Pour juice into the airway",
            "Leave the patient alone",
            "Administer insulin",
        ],
        "Severe hypoglycemia may require glucagon or EMS per scope and orders.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-032
    fact(
        "ccma-diabetes",
        "Diabetic ketoacidosis (DKA) typically presents with:",
        "Hyperglycemia, ketosis, and metabolic acidosis",
        [
            "Normal glucose with no ketones",
            "Hypoglycemia only",
            "Isolated hypertension without glucose changes",
        ],
        "DKA is more common in type 1 but can occur in type 2.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-033
    fact(
        "ccma-diabetes",
        "Hyperosmolar hyperglycemic state (HHS) often features:",
        "Very high glucose, dehydration, and minimal ketosis",
        [
            "Rapid onset in healthy children only",
            "Blood glucose always below 100 mg/dL",
            "Immediate hypothermia",
        ],
        "HHS is an emergency more often seen in type 2 diabetes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-034
    fact(
        "ccma-diabetes",
        "For a patient with suspected DKA or HHS, the MA should first:",
        "Notify the provider or emergency team and monitor vital signs",
        [
            "Give a large meal",
            "Hold all fluids indefinitely",
            "Discharge without assessment",
        ],
        "These conditions require inpatient-level treatment and fluid/insulin management.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-035
    fact(
        "ccma-diabetes",
        "Point-of-care blood glucose meters are often:",
        "CLIA-waived tests when used per manufacturer instructions",
        [
            "Exempt from all quality checks",
            "Used without hand hygiene",
            "Shared needles between patients",
        ],
        "Follow facility policy for waived testing and documentation.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-036
    fact(
        "ccma-diabetes",
        "Before a fingerstick glucose test, the MA should:",
        "Wash hands, use gloves, and clean the site per protocol",
        [
            "Use the thumb without cleaning",
            "Reuse lancets on multiple patients",
            "Skip patient identification",
        ],
        "Infection prevention and patient ID are required for POC testing.",
        ["CDC: Infection Control in Healthcare Settings (overview) — https://www.cdc.gov/infection-control/hcp/index.html", S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-037
    fact(
        "ccma-diabetes",
        "A common fingerstick site for adults is:",
        "Lateral aspect of the fingertip, avoiding very cold or edematous sites",
        [
            "Center of the palm only",
            "Earlobe as first choice in every adult",
            "Heel in all ambulatory adults",
        ],
        "Rotate sites and use appropriate lancet depth.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-038
    fact(
        "ccma-diabetes",
        "Quality control for waived glucose meters includes:",
        "Running control solution per schedule and documenting results",
        [
            "Skipping controls when busy",
            "Using expired strips without note",
            "Calibrating by guessing",
        ],
        "QC failures require troubleshooting before patient testing.",
        ["FDA: CLIA Waived Tests — https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clia-waived-tests", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-039
    fact(
        "ccma-diabetes",
        "When a glucose meter result does not match clinical picture, the MA should:",
        "Repeat the test, verify strips and technique, and notify the provider",
        [
            "Document without recheck",
            "Hide the result",
            "Give insulin based on a single questionable value",
        ],
        "Critical values follow facility reporting rules.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-040
    fact(
        "ccma-diabetes",
        "Rapid-acting insulin analogs (for example lispro or aspart) begin working in about:",
        "15 minutes, with peak activity in about 1 to 2 hours",
        [
            "6 to 8 hours only",
            "24 hours with no onset",
            "Immediately with no peak ever",
        ],
        "Timing supports mealtime dosing and correction per orders.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-041
    fact(
        "ccma-diabetes",
        "Regular (short-acting) human insulin typically peaks at:",
        "2 to 3 hours after injection",
        [
            "30 seconds",
            "12 hours only",
            "No peak at any time",
        ],
        "Onset is about 30 minutes; duration is roughly 5 to 8 hours.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-042
    fact(
        "ccma-diabetes",
        "Intermediate-acting NPH insulin often:",
        "Peaks between 4 and 12 hours and lasts up to about 24 hours",
        [
            "Has no duration",
            "Is only given IV push",
            "Is mixed with oral metformin in one syringe without order",
        ],
        "NPH appears cloudy; roll gently to suspend before drawing.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-043
    fact(
        "ccma-diabetes",
        "Long-acting basal insulin such as glargine is used to:",
        "Provide relatively steady background insulin over about 24 hours",
        [
            "Replace meals entirely",
            "Treat hypoglycemia first line",
            "Reverse DKA alone at home",
        ],
        "Basal-bolus regimens pair long-acting with mealtime insulin.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-044
    fact(
        "ccma-diabetes",
        "Unopened insulin vials or pens in use should be stored:",
        "Per manufacturer and facility policy, often refrigerated until opened then room temperature",
        [
            "In direct sunlight on the windowsill",
            "In the freezer always",
            "Mixed with other patients' insulin",
        ],
        "Never use insulin that is discolored, clumped, or expired.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-045
    fact(
        "ccma-diabetes",
        "When assisting with insulin injection, the MA within scope should:",
        "Verify the order, identity, dose, site, and technique per protocol",
        [
            "Guess the dose if the label is unclear",
            "Reuse syringes between patients",
            "Inject air without checking units",
        ],
        "Insulin is a high-alert medication requiring independent double-checks where required.",
        ["FDA: Medication Safety Program — https://www.fda.gov/drugs/medication-safety-program", S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-046
    fact(
        "ccma-diabetes",
        "Metformin works primarily by:",
        "Decreasing hepatic glucose production and improving insulin sensitivity",
        [
            "Stimulating insulin secretion from beta cells as sole effect",
            "Blocking all carbohydrate absorption",
            "Replacing insulin in type 1 diabetes",
        ],
        "Metformin is a first-line agent for many patients with type 2 diabetes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-047
    fact(
        "ccma-diabetes",
        "Sulfonylureas (for example glipizide) mainly:",
        "Stimulate pancreatic insulin release",
        [
            "Block all renal glucose reabsorption",
            "Are used instead of insulin in DKA",
            "Have no risk of hypoglycemia",
        ],
        "Hypoglycemia risk increases; teach patients to recognize symptoms.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-048
    fact(
        "ccma-diabetes",
        "SGLT2 inhibitors lower glucose by:",
        "Increasing urinary glucose excretion",
        [
            "Destroying beta cells",
            "Forcing only fat metabolism",
            "Raising glucagon without excretion",
        ],
        "Patients should report genital infections, dehydration, or unusual symptoms.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-049
    fact(
        "ccma-diabetes",
        "GLP-1 receptor agonists help glucose control by:",
        "Enhancing glucose-dependent insulin secretion and slowing gastric emptying",
        [
            "Replacing all oral fluids with saline",
            "Stopping all food intake permanently",
            "Eliminating need for monitoring",
        ],
        "These agents may support weight loss in some patients.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-050
    fact(
        "ccma-diabetes",
        "DPP-4 inhibitors (for example sitagliptin) act by:",
        "Prolonging incretin hormones that increase insulin release in a glucose-dependent way",
        [
            "Directly burning adipose tissue",
            "Blocking all insulin receptors",
            "Inducing ketoacidosis",
        ],
        "They are generally weight-neutral with lower hypoglycemia risk alone.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-051
    fact(
        "ccma-diabetes",
        "Before giving any diabetes medication, the MA should check:",
        "Allergies, renal function notes, and whether the patient has eaten if required",
        [
            "Only shoe size",
            "Whether the patient prefers pills only",
            "Random internet advice",
        ],
        "Contraindications and renal dosing matter for several agents.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-052
    fact(
        "ccma-diabetes",
        "Diabetic retinopathy screening is important because:",
        "Early eye disease may be asymptomatic until vision loss occurs",
        [
            "It replaces foot exams",
            "It cures diabetes",
            "It is needed only once at age 10",
        ],
        "Refer patients per ADA eye exam intervals.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-053
    fact(
        "ccma-diabetes",
        "Peripheral neuropathy in diabetes may present as:",
        "Numbness, tingling, or burning in the feet",
        [
            "Only chest pain",
            "Improved vibration sense",
            "Guaranteed absence of foot ulcers",
        ],
        "Monofilament testing may be part of foot exams per protocol.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-054
    fact(
        "ccma-diabetes",
        "Diabetic nephropathy is monitored with:",
        "Urine albumin and serum creatinine/eGFR per orders",
        [
            "Only a single fingerstick",
            "Hair analysis",
            "No labs ever",
        ],
        "ACE inhibitors or ARBs may be used for kidney protection when indicated.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-055
    fact(
        "ccma-diabetes",
        "Daily foot inspection teaching for patients includes:",
        "Check skin, nails, and shoes; report redness, breaks, or drainage",
        [
            "Soak feet in hot water daily without drying",
            "Trim nails into the corners aggressively",
            "Walk barefoot on hot pavement",
        ],
        "Refer non-healing ulcers promptly.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-056
    fact(
        "ccma-diabetes",
        "Carbohydrate counting helps patients:",
        "Match mealtime insulin or oral plans to anticipated carbohydrate intake",
        [
            "Avoid all protein",
            "Eliminate vegetables",
            "Stop blood glucose monitoring",
        ],
        "Dietitian referral supports individualized meal planning.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-057
    fact(
        "ccma-diabetes",
        "When documenting diabetes care, the MA should record:",
        "Glucose values, symptoms, treatments given, and patient response",
        [
            "Only the patient's favorite food",
            "Gossip about other patients",
            "Vague notes without numbers",
        ],
        "Accurate logs support billing, safety, and continuity of care.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-058
    fact(
        "ccma-diabetes",
        "Adjusting insulin doses independently is:",
        "Outside typical MA scope unless specifically delegated by provider and law",
        [
            "Required at every visit without orders",
            "Done based on neighbor's advice",
            "Allowed without documentation",
        ],
        "Follow state scope and supervising clinician protocols.",
        [S.NHA_CCMA, "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "intermediate",
    ),
    # ccma-diabetes-059
    fact(
        "ccma-diabetes",
        "Sick-day rules for patients on insulin often include:",
        "Continue basal insulin, monitor glucose and ketones if ordered, stay hydrated",
        [
            "Stop all insulin when ill",
            "Skip fluids to lower glucose",
            "Ignore vomiting",
        ],
        "Illness can raise glucose and ketone risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-060
    fact(
        "ccma-diabetes",
        "A patient with diabetes should wear medical identification because:",
        "It alerts responders to diabetes during emergencies",
        [
            "It replaces glucose monitoring",
            "It is only for cosmetic use",
            "It guarantees normal glucose",
        ],
        "Education includes when to seek urgent care.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-061
    fact(
        "ccma-diabetes",
        "Blood pressure control in diabetes matters because:",
        "Hypertension adds cardiovascular and kidney risk",
        [
            "It eliminates need for eye exams",
            "It prevents all neuropathy",
            "It means glucose goals are optional",
        ],
        "Many patients have targets below 140/90 mmHg unless individualized.",
        ["CDC: Measuring Blood Pressure — https://www.cdc.gov/high-blood-pressure/measure/index.html", "American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1"],
        "intermediate",
    ),
    # ccma-diabetes-062
    fact(
        "ccma-diabetes",
        "Exercise education for diabetes includes:",
        "Check glucose before and after activity and carry fast carbohydrate",
        [
            "Exercise only when glucose is above 400 mg/dL without advice",
            "Never drink water",
            "Skip foot protection",
        ],
        "Activity can lower glucose; adjust plan with the care team.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-063
    fact(
        "ccma-diabetes",
        "For many nonpregnant adults with diabetes, a common ADA A1C target is:",
        "Less than 7% when it can be reached without significant hypoglycemia",
        [
            "Always below 4%",
            "Always 8% or higher",
            "Never measure A1C",
        ],
        "Goals are individualized for age, hypoglycemia risk, comorbidities, and pregnancy status.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-064
    fact(
        "ccma-diabetes",
        "Latent autoimmune diabetes in adults (LADA) often presents as:",
        "Slowly progressive autoimmune diabetes in adults initially resembling type 2",
        [
            "Type 1 only in infants",
            "Reversible gestational diabetes only",
            "Pancreatic cancer always",
        ],
        "LADA may require insulin earlier than classic type 2.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-065
    fact(
        "ccma-diabetes",
        "Maturity-onset diabetes of the young (MODY) is:",
        "Monogenic diabetes with autosomal dominant inheritance in many forms",
        [
            "Always caused by obesity only",
            "Same as type 1 autoimmune always",
            "Diagnosed only by urine color",
        ],
        "MODY may be misclassified as type 1 or 2.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-066
    fact(
        "ccma-diabetes",
        "Steroid-induced hyperglycemia occurs because:",
        "Glucocorticoids increase insulin resistance and hepatic glucose output",
        [
            "Steroids always lower glucose",
            "Only in type 1 patients",
            "Only with oral steroids never IV",
        ],
        "Monitor glucose when patients receive systemic steroids.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-067
    fact(
        "ccma-diabetes",
        "Pancreatitis history increases risk of:",
        "Diabetes due to beta-cell injury and insulin deficiency",
        [
            "Hypoglycemia only always",
            "Lower A1C always",
            "No glucose effect",
        ],
        "Exocrine pancreatic disease affects endocrine function.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-068
    fact(
        "ccma-diabetes",
        "Cystic fibrosis-related diabetes (CFRD) is:",
        "A distinct form of diabetes associated with cystic fibrosis",
        [
            "Only gestational diabetes",
            "Always type 1 autoimmune",
            "Unrelated to pancreas",
        ],
        "CFRD management follows specialized guidelines.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-069
    fact(
        "ccma-diabetes",
        "Hemoglobin variants can affect:",
        "Accuracy of some A1C assays",
        [
            "Fingerstick glucose only always",
            "Blood pressure cuff size",
            "Urine ketones only",
        ],
        "Use alternative tests if A1C unreliable.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-070
    fact(
        "ccma-diabetes",
        "Anemia may cause A1C to read:",
        "Falsely low or high depending on assay and anemia type",
        [
            "Always accurate regardless",
            "Only in pregnancy never",
            "Unchanged always",
        ],
        "Interpret A1C with hematologic context.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-071
    fact(
        "ccma-diabetes",
        "Random plasma glucose 200 mg/dL or higher with classic symptoms:",
        "Supports diabetes diagnosis without repeat testing",
        [
            "Is always normal",
            "Requires OGTT only never",
            "Means hypoglycemia",
        ],
        "Symptomatic hyperglycemia meets criteria.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-072
    fact(
        "ccma-diabetes",
        "Screening adults for type 2 diabetes is recommended for:",
        "Overweight or obese adults with additional risk factors per ADA",
        [
            "All newborns only",
            "Only patients on insulin",
            "Never in primary care",
        ],
        "Risk-based screening detects undiagnosed diabetes.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-073
    fact(
        "ccma-diabetes",
        "First-line pharmacotherapy for many type 2 diabetes patients without contraindication is:",
        "Metformin plus lifestyle modification",
        [
            "Sliding-scale insulin only always",
            "High-dose steroids",
            "No treatment until A1C 10%",
        ],
        "Metformin is guideline-supported unless contraindicated.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-074
    fact(
        "ccma-diabetes",
        "Metformin is contraindicated in:",
        "Severe renal impairment or acute conditions risking lactic acidosis per labeling",
        [
            "Mild controlled hypertension",
            "All elderly always",
            "Any patient over BMI 25",
        ],
        "eGFR thresholds guide metformin use.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-075
    fact(
        "ccma-diabetes",
        "SGLT2 inhibitors may provide:",
        "Glycemic lowering and cardiovascular/renal benefits in selected patients",
        [
            "Only weight gain always",
            "Cure of type 1 diabetes",
            "No need for kidney monitoring ever",
        ],
        "Class effects include genital mycotic infections and euglycemic DKA risk rarely.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-076
    fact(
        "ccma-diabetes",
        "GLP-1 receptor agonists can:",
        "Lower glucose and promote weight loss in many patients",
        [
            "Replace insulin in all type 1 patients always",
            "Cause mandatory hypoglycemia always",
            "Be given without injection technique teaching",
        ],
        "GI side effects are common initially.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-077
    fact(
        "ccma-diabetes",
        "Sulfonylureas primarily:",
        "Stimulate insulin secretion from pancreatic beta cells",
        [
            "Block glucose absorption in gut only",
            "Excrete glucose in urine only",
            "Replace all insulin needs in type 1",
        ],
        "Hypoglycemia risk increases especially in elderly.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-078
    fact(
        "ccma-diabetes",
        "Basal insulin (e.g., glargine) is typically:",
        "Given once daily to provide background insulin",
        [
            "Only with meals only always",
            "Stopped during illness always",
            "Oral tablet form",
        ],
        "Basal-bolus regimens mimic physiology.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-079
    fact(
        "ccma-diabetes",
        "Rapid-acting insulin (e.g., lispro) is usually:",
        "Given with meals to cover carbohydrate",
        [
            "Given once weekly",
            "Only at bedtime for all patients",
            "Oral before meals",
        ],
        "Timing matches postprandial glucose rise.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-080
    fact(
        "ccma-diabetes",
        "Insulin storage of unopened vials/pens generally requires:",
        "Refrigeration per manufacturer until in-use dates",
        [
            "Freezer for all insulin",
            "Hot car storage",
            "Direct sunlight on dashboard",
        ],
        "Temperature extremes inactivate insulin.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # ccma-diabetes-081
    fact(
        "ccma-diabetes",
        "In-use insulin vial or pen room temperature stability:",
        "Follow product labeling; many allow room temp days to weeks",
        [
            "Must stay frozen after opening",
            "Boil before each injection",
            "Share pen among family",
        ],
        "Room temp use reduces injection discomfort.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-082
    fact(
        "ccma-diabetes",
        "Continuous glucose monitor (CGM) trend arrows help patients:",
        "Anticipate rising or falling glucose and adjust per plan",
        [
            "Replace fingersticks entirely always without policy",
            "Ignore alarms always",
            "Skip provider follow-up",
        ],
        "CGM supports time-in-range goals.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-083
    fact(
        "ccma-diabetes",
        "Time in range (TIR) for many adults targets:",
        "About 70% time between 70 and 180 mg/dL when using CGM metrics",
        [
            "100% below 70 mg/dL",
            "0% ever above 100",
            "No monitoring needed",
        ],
        "TIR complements A1C.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-084
    fact(
        "ccma-diabetes",
        "Diabetic ketoacidosis (DKA) hallmark labs include:",
        "Hyperglycemia, ketosis, and anion gap metabolic acidosis",
        [
            "Normal glucose always",
            "Only hypernatremia",
            "Respiratory alkalosis only",
        ],
        "DKA is medical emergency.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-085
    fact(
        "ccma-diabetes",
        "Hyperosmolar hyperglycemic state (HHS) most often occurs in:",
        "Type 2 diabetes with extreme hyperglycemia and dehydration",
        [
            "Only children with type 1",
            "Normal glucose states",
            "Only during exercise",
        ],
        "HHS has high mortality without treatment.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-086
    fact(
        "ccma-diabetes",
        "Sick-day rules for insulin-requiring diabetes include:",
        "Continue insulin, monitor glucose frequently, stay hydrated, contact provider for persistent vomiting or high ketones",
        [
            "Stop all insulin when ill",
            "Skip fluids",
            "Ignore ketones in urine",
        ],
        "Illness can raise glucose and ketone risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-087
    fact(
        "ccma-diabetes",
        "Urine ketone testing is especially important when:",
        "Glucose is persistently high or patient is ill with type 1 or insulin deficiency",
        [
            "Patient is hypoglycemic only",
            "A1C is normal",
            "Patient is fasting for labs only",
        ],
        "Ketones signal possible DKA.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-088
    fact(
        "ccma-diabetes",
        "Glucagon emergency kit is used for:",
        "Severe hypoglycemia when patient cannot take oral carbohydrate",
        [
            "Mild hunger",
            "Hyperglycemia over 300 only",
            "Hypertension",
        ],
        "Family/caregivers need training.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-diabetes-089
    fact(
        "ccma-diabetes",
        "Hypoglycemia unawareness means:",
        "Reduced autonomic warning symptoms at low glucose",
        [
            "Always feeling shaky at 200 mg/dL",
            "Only in type 2 never on insulin",
            "Improved with ignoring lows",
        ],
        "Increases severe hypoglycemia risk.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-diabetes-090
    fact(
        "ccma-diabetes",
        "Carbohydrate counting for meal insulin dosing:",
        "Matches rapid insulin to planned carbohydrate intake per education",
        [
            "Eliminates need for glucose monitoring",
            "Means avoiding all carbs forever",
            "Replaces provider entirely",
        ],
        "Education improves postprandial control.",
        ["American Diabetes Association: Standards of Care in Diabetes — https://diabetesjournals.org/care/issue/48/Supplement_1", "American Diabetes Association: Classification and Diagnosis of Diabetes — https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553", S.CDC_DIABETES, S.NHA_CCMA],
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
