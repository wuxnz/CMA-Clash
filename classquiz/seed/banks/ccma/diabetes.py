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
        'Albuminuria screening in diabetes detects?',
        'Early diabetic kidney disease',
        [
            'Acute appendicitis',
            'Otitis media',
            'Dental caries',
        ],
        'Urine albumin-to-creatinine ratio monitors nephropathy. Choosing Acute appendicitis is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'Blood pressure target for many adults with diabetes is often?',
        'Below 130/80 mmHg if achievable without undue burden',
        [
            'Above 160/100 always',
            'Ignored in diabetes care',
            'Only measured yearly if asymptomatic always',
        ],
        'Cardiovascular risk reduction includes BP control. Choosing Above 160/100 always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'Continuous glucose monitoring provides?',
        'Interstitial glucose trends with alerts in many systems',
        [
            'Direct arterial pressure only',
            'Bone density',
            'Culture results',
        ],
        'CGM supports pattern management. Choosing Direct arterial pressure only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Diabetes self-management education should?',
        'Be offered at diagnosis and as needed thereafter',
        [
            'Occur once lifetime only',
            'Be withheld if insured',
            'Replace medical follow-up entirely',
        ],
        'Ongoing education supports behavior change. Choosing Occur once lifetime only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Diabetic ketoacidosis may present with?',
        'Hyperglycemia, ketosis, and metabolic acidosis',
        [
            'Substituting V6 for limb leads only',
            'Normal glucose always',
            'Isolated rash only',
        ],
        'DKA is an acute complication needing emergency care. Choosing Substituting V6 for limb leads only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Fasting plasma glucose at or above this value meets diabetes diagnostic threshold on repeat testing?',
        '126 mg/dL',
        [
            '100 mg/dL',
            '110 mg/dL always',
            '200 mg/dL without symptoms only threshold',
        ],
        'Diagnosis requires confirmatory testing unless hyperglycemic crisis present. Choosing 100 mg/dL is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Foot exams in diabetes screen for?',
        'Neuropathy, ulcers, and vascular insufficiency',
        [
            'Hair color only',
            'Vision only',
            'Hearing acuity exclusively',
        ],
        'Foot complications drive morbidity in diabetes. Choosing Hair color only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Hemoglobin A1c at or above this percentage indicates diabetes on repeat testing?',
        '6.5%',
        [
            '5.0%',
            '5.7% on one test alone always',
            '8.0% only in pregnancy',
        ],
        'A1c reflects average glycemia over about three months. Choosing 5.0% is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Hypoglycemia in alert adults is often treated first with?',
        '15 grams of fast-acting carbohydrate',
        [
            'High-fat protein only',
            'Large pizza immediately always',
            'Skipping recheck',
        ],
        'Follow 15-15 rule and recheck glucose. Choosing High-fat protein only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Metformin is contraindicated in many cases of?',
        'Significant renal impairment or acute conditions risking lactic acidosis',
        [
            'Mild diet changes only',
            'All hypertension always',
            'Using a glucometer',
        ],
        'eGFR guides metformin safety. Choosing Mild diet changes only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Prediabetes is often defined by A1c of?',
        '5.7% to 6.4%',
        [
            'Below 5.0% always',
            'Above 8.0%',
            'Exactly 7.0% only',
        ],
        'Prediabetes signals elevated future diabetes risk. Choosing Below 5.0% always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Statins may be recommended for adults with diabetes?',
        'Based on age and additional risk factors per guidelines',
        [
            'Never in any diabetic patient',
            'Only if glucose below 70 always',
            'Instead of all glucose monitoring',
        ],
        'Lipid management lowers ASCVD risk. Choosing Never in any diabetic patient is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Type 1 diabetes is characterized by?',
        'Autoimmune destruction of pancreatic beta cells with absolute insulin deficiency',
        [
            'Primary insulin resistance only',
            'Reversible gestational hormones only',
            'Exclusively diet-induced always',
        ],
        'Type 1 requires insulin for survival. Choosing Primary insulin resistance only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Type 2 diabetes most often involves?',
        'Insulin resistance with relative insulin deficiency',
        [
            'Only autoimmune beta-cell loss',
            'Only pediatric onset always',
            'Normal glucose lifelong',
        ],
        'Lifestyle and genetics influence type 2 risk. Choosing Only autoimmune beta-cell loss is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'What does Sick-day rules for insulin-treated patients often include?',
        'Continue insulin, monitor glucose frequently, stay hydrated',
        [
            'Stop all insulin when ill',
            'Ignore ketones if vomiting',
            'Avoid fluids',
        ],
        'Illness can raise glucose and ketone risk. Choosing Stop all insulin when ill is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

