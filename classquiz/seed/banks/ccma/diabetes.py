# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-diabetes)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    fact(
        'ccma-diabetes',
        'What does albuminuria screening in diabetes detect?',
        'Early diabetic kidney disease',
        [
            'Cardiovascular disease risk',
            'Visual changes from retinopathy',
            'Nerve damage in the feet',
        ],
        'A urine albumin-to-creatinine ratio measures albumin in the urine, which is the earliest sign of diabetic kidney disease and appears before serum creatinine rises. Cardiovascular risk, retinal changes, and nerve damage are tracked with blood pressure, lipid, dilated eye, and foot examinations rather than with urine testing.',
        [S.NHA_CCMA],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'How often should A1C be repeated for a patient with diabetes?',
        'Every 3 months above goal and every 6 months at goal',
        [
            'Every 6 months above goal and every 3 months at goal',
            'Every 12 months for every patient regardless of the result',
            'Every 24 months for every patient regardless of the result',
        ],
        'The ADA recommends A1C at diagnosis, every three months while the patient is above the glycemic goal, and every six months once the goal is met. Reversing those two intervals delays needed treatment changes, and testing once a year or once every two years leaves glycemic control unreviewed for too long.',
        [S.NHA_CCMA],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'What does continuous glucose monitoring give a patient with diabetes?',
        'Interstitial glucose trends with alarms for patterns',
        [
            'Continuous blood pressure readings with trend alarms',
            'Insulin pump reservoir levels with low supply alarms',
            'Venous glucose values drawn at the same time each day',
        ],
        'A continuous glucose monitor measures interstitial glucose every few minutes and shows the direction and rate of change, with alarms set by the person using it. Blood pressure readings, pump reservoir levels, and timed venous draws are separate measurements that a continuous glucose monitor does not provide.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'How often should the urine albumin-to-creatinine ratio be checked in type 1 diabetes?',
        'At least annually to screen for kidney disease',
        [
            'Every five years after the first year of diagnosis',
            'Whenever the patient reports changes in vision or urine',
            'Every three months along with each routine A1C draw',
        ],
        'People with type 1 diabetes should have a urine albumin-to-creatinine ratio checked at least once a year to screen for diabetic kidney disease. Testing every five years, tying the check to vision or urine changes, or repeating it with each A1C draw would miss albuminuria that appears early in nephropathy.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'What are the three defining features of diabetic ketoacidosis?',
        'Hyperglycemia, ketosis, and metabolic acidosis',
        [
            'Hyperglycemia, dehydration, and minimal ketosis',
            'Hypoglycemia, ketosis, and respiratory alkalosis',
            'Hyperglycemia, acidosis, and vascular occlusion',
        ],
        'Diabetic ketoacidosis is defined by high blood glucose, ketone production, and a metabolic acidosis caused by the ketones, and it is a medical emergency. Dehydration with minimal ketosis describes hyperosmolar hyperglycemic state, hypoglycemia with respiratory alkalosis does not fit, and vascular occlusion is not part of the definition.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'What fasting plasma glucose value confirms diabetes when repeated on a second test?',
        '126 mg/dL or higher',
        [
            '100 mg/dL or higher',
            '110 mg/dL or higher',
            '140 mg/dL or higher',
        ],
        'A fasting plasma glucose of 126 mg/dL or higher on two separate tests meets the ADA criterion for a diagnosis of diabetes. Values from 100 to 125 mg/dL fall in the prediabetes range, and 140 mg/dL is the impaired two hour oral glucose tolerance value rather than a fasting threshold.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Which findings does a comprehensive annual foot exam for a patient with diabetes assess?',
        'Skin, pedal pulses, and protective sensation',
        [
            'Blood pressure, pulse rate, and body temperature',
            'Glucose trends, insulin doses, and carbohydrate intake',
            'Retinal changes, visual fields, and eye pressures',
        ],
        'A comprehensive foot exam inspects the skin for breaks and calluses, palpates the pedal pulses, and checks protective sensation with a monofilament at each visit. Blood pressure, pulse rate, temperature, glucose trends, insulin doses, and retinal findings are gathered elsewhere in the visit rather than from the foot exam itself.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'What is the lowest A1C value that confirms diabetes on repeat testing?',
        '6.5% or higher',
        [
            '7.0% or higher',
            '6.0% or higher',
            '5.7% or higher',
        ],
        'The ADA confirms diabetes with an A1C of 6.5% or higher on two separate tests, and the A1C reflects average glycemia over roughly three months. A cutoff of 7.0% or 6.0% is not the diagnostic value, and 5.7% marks the start of the prediabetes range rather than diabetes.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'How should a conscious adult with a blood glucose of 62 mg/dL be treated first?',
        '15 g of fast-acting carbohydrate, then a recheck in 15 minutes',
        [
            '15 g of fast-acting carbohydrate, then a recheck in 60 minutes',
            '15 g of protein and fat, then a recheck in 15 minutes',
            'A full meal of complex carbohydrates, then a recheck in 15 minutes',
        ],
        'The 15-15 rule is to give 15 g of fast-acting carbohydrate and recheck the blood glucose in 15 minutes, repeating the treatment if the value stays low. Waiting an hour to recheck delays treatment, protein and fat raise glucose too slowly for a rescue, and a full meal is larger and slower than the rescue dose.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'In which situation is metformin contraindicated?',
        'Severe kidney disease with a risk of lactic acidosis',
        [
            'Mild hypertension controlled with a single medication',
            'A body mass index of 27 in a newly diagnosed adult',
            'Recent onset of type 2 diabetes in a 45 year old adult',
        ],
        'Metformin is withheld in significant renal impairment and in acute conditions that raise the risk of lactic acidosis, so the eGFR guides whether it can be started or continued. Controlled hypertension, a body mass index of 27, and a recent diagnosis are common reasons to start metformin rather than reasons to withhold it.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Which A1C range indicates prediabetes?',
        '5.7% to 6.4%',
        [
            '6.5% to 7.4%',
            '4.0% to 5.6%',
            '7.5% to 9.0%',
        ],
        'An A1C of 5.7% to 6.4% falls in the prediabetes range, which signals a high chance of progressing to type 2 diabetes and calls for lifestyle change and periodic re-testing. Values from 6.5% upward meet the diabetes criterion, an A1C of 4.0% to 5.6% is in the normal range, and 7.5% to 9.0% is diabetes that sits well above target.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Why is a statin often recommended for an adult with diabetes and no known heart disease?',
        'Diabetes is itself a risk factor for heart disease',
        [
            'Diabetes causes low HDL that statins can raise',
            'Diabetes causes high blood pressure that statins can lower',
            'Diabetes causes high triglycerides that statins can lower',
        ],
        'Diabetes is treated as an independent risk factor for atherosclerotic cardiovascular disease, so a statin is often started in an adult with diabetes even without a prior event. Statins do not raise HDL, lower blood pressure, or lower triglycerides, so those changes are not the reason for the recommendation.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Which mechanism best explains type 1 diabetes mellitus?',
        'Autoimmune destruction of pancreatic beta cells',
        [
            'Insulin resistance with progressive beta-cell failure',
            'Glucocorticoid-driven glucose production from the liver',
            'Autoimmune destruction of insulin receptors in muscle',
        ],
        'Type 1 diabetes results from autoimmune destruction of the pancreatic beta cells, which leaves the body with little or no endogenous insulin, so insulin replacement is required for survival. Insulin resistance with beta-cell failure describes type 2 diabetes, steroid-driven hepatic glucose output describes steroid-induced hyperglycemia, and destroying insulin receptors is not the mechanism of any common form of diabetes.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Which mechanism best explains type 2 diabetes mellitus?',
        'Insulin resistance with relative insulin deficiency',
        [
            'Autoimmune destruction of the pancreatic beta cells',
            'A complete absence of insulin from the pancreas',
            'Excess glucagon secretion from the pancreatic alpha cells',
        ],
        'Type 2 diabetes begins with insulin resistance, and the beta cells gradually fail to keep up, so insulin production becomes relatively deficient. Autoimmune beta-cell destruction describes type 1 diabetes, a complete absence of pancreatic insulin is not the pattern in type 2 diabetes, and excess glucagon by itself does not explain the hyperglycemia.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'What should a patient with insulin-treated diabetes do when illness causes vomiting and poor fluid intake?',
        'Continue basal insulin, check glucose and ketones',
        [
            'Hold basal insulin until the vomiting and fever resolve',
            'Continue basal insulin but check glucose once a day',
            'Double the basal insulin dose and delay ketone checks',
        ],
        'Sick-day rules keep the basal insulin dose going, add more frequent glucose checks, and include ketone testing when the glucose stays high, along with sipping fluids and calling the care team for persistent vomiting. Stopping insulin raises the risk of ketoacidosis, checking glucose once a day misses dangerous swings, and doubling the dose without ketone monitoring risks another emergency.',
        [S.NHA_CCMA],
        'advanced',
    ),
]
