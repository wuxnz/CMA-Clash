# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Additional diabetes facts to expand ccma-diabetes to 112 total (four 28-question sets)."""

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    fact(
        'ccma-diabetes',
        'Latent autoimmune diabetes in adults (LADA) often presents as:',
        'Slowly progressive autoimmune diabetes in adults initially resembling type 2',
        [
            'Type 1 only in infants',
            'Reversible gestational diabetes only',
            'Pancreatic cancer always'
        ],
        'LADA may require insulin earlier than classic type 2.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Maturity-onset diabetes of the young (MODY) is:',
        'Monogenic diabetes with autosomal dominant inheritance in many forms',
        [
            'Always caused by obesity only',
            'Same as type 1 autoimmune always',
            'Diagnosed only by urine color'
        ],
        'MODY may be misclassified as type 1 or 2.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Steroid-induced hyperglycemia occurs because:',
        'Glucocorticoids increase insulin resistance and hepatic glucose output',
        [
            'Steroids always lower glucose',
            'Only in type 1 patients',
            'Only with oral steroids never IV'
        ],
        'Monitor glucose when patients receive systemic steroids.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Pancreatitis history increases risk of:',
        'Diabetes due to beta-cell injury and insulin deficiency',
        [
            'Hypoglycemia only always',
            'Lower A1C always',
            'No glucose effect'
        ],
        'Exocrine pancreatic disease affects endocrine function.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Cystic fibrosis-related diabetes (CFRD) is:',
        'A distinct form of diabetes associated with cystic fibrosis',
        [
            'Only gestational diabetes',
            'Always type 1 autoimmune',
            'Unrelated to pancreas'
        ],
        'CFRD management follows specialized guidelines.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Hemoglobin variants can affect:',
        'Accuracy of some A1C assays',
        [
            'Fingerstick glucose only always',
            'Blood pressure cuff size',
            'Urine ketones only'
        ],
        'Use alternative tests if A1C unreliable.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Anemia may cause A1C to read:',
        'Falsely low or high depending on assay and anemia type',
        [
            'Always accurate regardless',
            'Only in pregnancy never',
            'Unchanged always'
        ],
        'Interpret A1C with hematologic context.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Random plasma glucose 200 mg/dL or higher with classic symptoms:',
        'Supports diabetes diagnosis without repeat testing',
        [
            'Is always normal',
            'Requires OGTT only never',
            'Means hypoglycemia'
        ],
        'Symptomatic hyperglycemia meets criteria.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Screening adults for type 2 diabetes is recommended for:',
        'Overweight or obese adults with additional risk factors per ADA',
        [
            'All newborns only',
            'Only patients on insulin',
            'Never in primary care'
        ],
        'Risk-based screening detects undiagnosed diabetes.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'First-line pharmacotherapy for many type 2 diabetes patients without contraindication is:',
        'Metformin plus lifestyle modification',
        [
            'Sliding-scale insulin only always',
            'High-dose steroids',
            'No treatment until A1C 10%'
        ],
        'Metformin is guideline-supported unless contraindicated.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Metformin is contraindicated in:',
        'Severe renal impairment or acute conditions risking lactic acidosis per labeling',
        [
            'Mild controlled hypertension',
            'All elderly always',
            'Any patient over BMI 25'
        ],
        'eGFR thresholds guide metformin use.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'SGLT2 inhibitors may provide:',
        'Glycemic lowering and cardiovascular/renal benefits in selected patients',
        [
            'Only weight gain always',
            'Cure of type 1 diabetes',
            'No need for kidney monitoring ever'
        ],
        'Class effects include genital mycotic infections and euglycemic DKA risk rarely.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'GLP-1 receptor agonists can:',
        'Lower glucose and promote weight loss in many patients',
        [
            'Replace insulin in all type 1 patients always',
            'Cause mandatory hypoglycemia always',
            'Be given without injection technique teaching'
        ],
        'GI side effects are common initially.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Sulfonylureas primarily:',
        'Stimulate insulin secretion from pancreatic beta cells',
        [
            'Block glucose absorption in gut only',
            'Excrete glucose in urine only',
            'Replace all insulin needs in type 1'
        ],
        'Hypoglycemia risk increases especially in elderly.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Basal insulin (e.g., glargine) is typically:',
        'Given once daily to provide background insulin',
        [
            'Only with meals only always',
            'Stopped during illness always',
            'Oral tablet form'
        ],
        'Basal-bolus regimens mimic physiology.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Rapid-acting insulin (e.g., lispro) is usually:',
        'Given with meals to cover carbohydrate',
        [
            'Given once weekly',
            'Only at bedtime for all patients',
            'Oral before meals'
        ],
        'Timing matches postprandial glucose rise.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Insulin storage of unopened vials/pens generally requires:',
        'Refrigeration per manufacturer until in-use dates',
        [
            'Freezer for all insulin',
            'Hot car storage',
            'Direct sunlight on dashboard'
        ],
        'Temperature extremes inactivate insulin.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'In-use insulin vial or pen room temperature stability:',
        'Follow product labeling; many allow room temp days to weeks',
        [
            'Must stay frozen after opening',
            'Boil before each injection',
            'Share pen among family'
        ],
        'Room temp use reduces injection discomfort.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Continuous glucose monitor (CGM) trend arrows help patients:',
        'Anticipate rising or falling glucose and adjust per plan',
        [
            'Replace fingersticks entirely always without policy',
            'Ignore alarms always',
            'Skip provider follow-up'
        ],
        'CGM supports time-in-range goals.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Time in range (TIR) for many adults targets:',
        'About 70% time between 70 and 180 mg/dL when using CGM metrics',
        [
            '100% below 70 mg/dL',
            '0% ever above 100',
            'No monitoring needed'
        ],
        'TIR complements A1C.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Diabetic ketoacidosis (DKA) hallmark labs include:',
        'Hyperglycemia, ketosis, and anion gap metabolic acidosis',
        [
            'Normal glucose always',
            'Only hypernatremia',
            'Respiratory alkalosis only'
        ],
        'DKA is medical emergency.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Hyperosmolar hyperglycemic state (HHS) most often occurs in:',
        'Type 2 diabetes with extreme hyperglycemia and dehydration',
        [
            'Only children with type 1',
            'Normal glucose states',
            'Only during exercise'
        ],
        'HHS has high mortality without treatment.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Sick-day rules for insulin-requiring diabetes include:',
        'Continue insulin, monitor glucose frequently, stay hydrated, contact provider for persistent vomiting or high ketones',
        [
            'Stop all insulin when ill',
            'Skip fluids',
            'Ignore ketones in urine'
        ],
        'Illness can raise glucose and ketone risk.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Urine ketone testing is especially important when:',
        'Glucose is persistently high or patient is ill with type 1 or insulin deficiency',
        [
            'Patient is hypoglycemic only',
            'A1C is normal',
            'Patient is fasting for labs only'
        ],
        'Ketones signal possible DKA.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Glucagon emergency kit is used for:',
        'Severe hypoglycemia when patient cannot take oral carbohydrate',
        [
            'Mild hunger',
            'Hyperglycemia over 300 only',
            'Hypertension'
        ],
        'Family/caregivers need training.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Hypoglycemia unawareness means:',
        'Reduced autonomic warning symptoms at low glucose',
        [
            'Always feeling shaky at 200 mg/dL',
            'Only in type 2 never on insulin',
            'Improved with ignoring lows'
        ],
        'Increases severe hypoglycemia risk.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Carbohydrate counting for meal insulin dosing:',
        'Matches rapid insulin to planned carbohydrate intake per education',
        [
            'Eliminates need for glucose monitoring',
            'Means avoiding all carbs forever',
            'Replaces provider entirely'
        ],
        'Education improves postprandial control.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Medical nutrition therapy for diabetes emphasizes:',
        'Individualized macronutrient distribution and portion control',
        [
            'Single fad diet for all',
            'Unlimited sugar if on metformin',
            'Skipping all fat always'
        ],
        'ADA supports flexible eating patterns.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'Alcohol use in diabetes can cause:',
        'Delayed hypoglycemia especially with insulin or secretagogues',
        [
            'Permanent hyperglycemia only',
            'Improved A1C always',
            'No interaction with meds'
        ],
        'Educate about food and monitoring with alcohol.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Smoking cessation in diabetes reduces:',
        'Cardiovascular and microvascular complication risk',
        [
            'Only lung cancer risk without glucose effect',
            'Need for foot exams',
            'Kidney function always worsens'
        ],
        'Smoking worsens vascular disease.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'Annual dilated eye exam for diabetes screens for:',
        'Diabetic retinopathy',
        [
            'Glaucoma only without retina view',
            'Hearing loss',
            'Foot ulcers'
        ],
        'Early retinopathy may be asymptomatic.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Urine albumin-to-creatinine ratio monitors:',
        'Diabetic kidney disease',
        [
            'Retinopathy only',
            'Thyroid function',
            'Liver enzymes only'
        ],
        'Microalbuminuria precedes macroalbuminuria.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'ACE inhibitor or ARB may be used in diabetes when:',
        'Hypertension or albuminuria is present per guidelines',
        [
            'Only for pain',
            'To lower glucose directly always',
            'Instead of all diabetes meds always'
        ],
        'Renoprotective benefits in albuminuric disease.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Statin therapy in diabetes over age 40 often aims to:',
        'Reduce ASCVD risk per guidelines',
        [
            'Raise LDL intentionally',
            'Replace blood pressure meds always',
            'Cure neuropathy'
        ],
        'Diabetes is ASCVD risk equivalent in many adults.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Blood pressure goal for many diabetes patients is:',
        'Below 140/90 mmHg unless lower target individualized',
        [
            'Always 180/110 mmHg',
            'Only measured yearly',
            'Ignored if A1C normal'
        ],
        'Hypertension accelerates complications.',
        [
            S.ADA_STANDARDS,
        S.CDC_HBP,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Diabetic autonomic neuropathy may cause:',
        'Gastroparesis, orthostatic hypotension, or silent ischemia',
        [
            'Only foot numbness never other systems',
            'Improved heart rate variability always',
            'Hyperglycemia cure'
        ],
        'Autonomic involvement affects multiple organs.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Painful diabetic peripheral neuropathy symptoms include:',
        'Burning, tingling, or shooting pain in feet or hands',
        [
            'Only painless ulcers always',
            'Improved sensation to injury',
            'Only headache'
        ],
        'Painful neuropathy affects quality of life.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Monofilament foot exam tests for:',
        'Loss of protective sensation',
        [
            'Visual acuity',
            'Pulse oximetry',
            'Hearing'
        ],
        '10-g monofilament identifies ulcer risk.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Proper diabetes footwear education includes:',
        'Well-fitting shoes, daily foot inspection, and prompt care for breaks in skin',
        [
            'Walking barefoot always',
            'Ignoring hot surfaces',
            'Cutting own thick nails if neuropathic without podiatry'
        ],
        'Ulcer prevention reduces amputations.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'Charcot foot in diabetes is:',
        'Neuroarthropathy causing bone and joint deformity',
        [
            'Simple sprain only always',
            'Bacterial cellulitis only',
            'Normal aging'
        ],
        'Immobilization and offloading are critical.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Periodontal disease and diabetes:',
        'Have bidirectional relationship worsening glycemic control and gum disease',
        [
            'Are unrelated',
            'Only affect teeth cosmetically',
            'Cured by mouthwash alone'
        ],
        'Oral health is part of diabetes care.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Preconception counseling in diabetes emphasizes:',
        'Tight glycemic control before pregnancy to reduce malformations',
        [
            'Stopping all care until delivery',
            'A1C goals unimportant',
            'Only folic acid without glucose control'
        ],
        'Poor preconception control increases congenital risk.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Gestational diabetes screening is typically performed:',
        'At 24-28 weeks gestation with protocol-defined test',
        [
            'Only after delivery',
            'Never in overweight patients',
            'Only if prior C-section'
        ],
        'Early detection reduces complications.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Postpartum follow-up after gestational diabetes should include:',
        'Glucose testing to detect persistent diabetes or prediabetes',
        [
            'No further testing ever',
            'Only weight of baby',
            'Stopping all lifestyle advice'
        ],
        'GDM increases later type 2 risk.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Breastfeeding in mothers with diabetes:',
        'May improve maternal glucose and provides infant nutrition benefits',
        [
            'Is always contraindicated',
            'Requires stopping insulin always',
            'Worsens neonatal hypoglycemia always without monitoring'
        ],
        'Coordinate insulin needs with lactation.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'School or work diabetes accommodations may include:',
        'Breaks for glucose monitoring and snack per documented plan',
        [
            'Hiding diabetes from school nurse always',
            'No access to glucose',
            'Sharing one glucometer unsanitized among students'
        ],
        '504 plans support safe management.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Driving safety with diabetes requires:',
        'Treating hypoglycemia before driving and monitoring as directed',
        [
            'Driving during severe hypoglycemia',
            'Skipping meals before long trips without plan',
            'Ignoring CGM low alerts'
        ],
        'Hypoglycemia impairs driving ability.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'A1C goal may be relaxed in older adults with:',
        'Limited life expectancy, severe hypoglycemia history, or extensive comorbidities',
        [
            'Perfect health only',
            'All adolescents',
            'Every pregnancy first trimester only without nuance'
        ],
        'Individualization reduces harm.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Continuous subcutaneous insulin infusion (pump) users need backup:',
        'Long-acting insulin or rapid insulin and supplies if pump fails',
        [
            'No plan if pump stops',
            'Only oral meds if pump fails without transition plan',
            'Share pump among patients'
        ],
        'Pump failure risks DKA in type 1.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Sensor-augmented pump therapy can:',
        'Suspend insulin delivery for predicted hypoglycemia on some systems',
        [
            'Replace fingersticks and labs entirely always',
            'Operate without training',
            'Guarantee never high glucose'
        ],
        'Technology requires education and maintenance.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Dawn phenomenon refers to:',
        'Early morning rise in glucose from counter-regulatory hormones',
        [
            'Night hypoglycemia only always',
            'Allergic reaction to insulin',
            'Ketoacidosis only'
        ],
        'Basal insulin timing may be adjusted per team.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Somogyi effect (historical term) suggested:',
        'Rebound hyperglycemia after nocturnal hypoglycemia',
        [
            'Stable overnight glucose always',
            'Only in type 2 never',
            'No clinical relevance ever'
        ],
        'Nocturnal checks clarify morning highs.',
        [
            S.ADA_STANDARDS,
        S.CDC_DIABETES_BASICS,
        S.MEDLINEPLUS_DIABETES
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Hospital insulin orders should use:',
        'Scheduled basal plus correction and nutritional coverage per protocol',
        [
            'Sliding scale only without basal always',
            'Patient home doses without review',
            'Oral agents only in NPO patient without plan'
        ],
        'Inpatient glycemic management protocols improve safety.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Perioperative diabetes management aims to:',
        'Avoid hypoglycemia and extreme hyperglycemia around surgery',
        [
            'Stop all monitoring',
            'Target glucose 400 mg/dL',
            'Withhold all fluids'
        ],
        'Coordination among surgery, anesthesia, and medicine teams.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Contrast CT with metformin may require:',
        'Temporary hold and renal function check per facility protocol',
        [
            'Double metformin dose',
            'No kidney assessment ever',
            'Ignore eGFR'
        ],
        'Risk of lactic acidosis with renal impairment after contrast.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Flu and pneumococcal vaccines in diabetes:',
        'Recommended per immunization schedule to reduce severe infection',
        [
            'Contraindicated always',
            'Only for children',
            'Replace glucose monitoring'
        ],
        'Infections worsen glycemic control.',
        [
            S.CDC_DIABETES,
        S.CDC_VACCINE_ADMIN,
        S.ADA_STANDARDS
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Diabetes distress differs from depression by:',
        'Focusing on emotional burden of self-management rather than solely mood disorder criteria',
        [
            'Being identical to major depression always',
            'Not affecting adherence',
            'Requiring no support'
        ],
        'Screening and referral help coping.',
        [
            S.ADA_STANDARDS,
        S.CDC_DIABETES_BASICS,
        S.MEDLINEPLUS_DIABETES
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'DSMES (diabetes self-management education and support) should be:',
        'Offered at diagnosis and thereafter when needed',
        [
            'One-time only at age 65',
            'Only for type 1',
            'Replaced by internet memes'
        ],
        'Education improves outcomes and safety.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-diabetes',
        'Glucocorticoid dose increases in sick patients on steroids require:',
        'Glucose monitoring and insulin adjustment per provider',
        [
            'Stopping glucose checks',
            'Assuming steroids lower glucose',
            'No communication with team'
        ],
        'Steroids raise glucose unpredictably.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Fatty liver disease (NAFLD/MASLD) is common in type 2 diabetes and:',
        'May progress to fibrosis; lifestyle and weight management are key',
        [
            'Never occurs with diabetes',
            'Cured by skipping meals only',
            'Diagnosed only by foot exam'
        ],
        'Liver disease affects metabolic health.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Hypothyroidism in diabetes may:',
        'Worsen dyslipidemia and complicate glucose control',
        [
            'Improve insulin sensitivity always',
            'Eliminate need for thyroid screening',
            'Cause permanent hypoglycemia only'
        ],
        'Thyroid dysfunction is more common with diabetes.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Celiac disease screening in type 1 diabetes:',
        'May be considered because of increased association',
        [
            'Never indicated',
            'Only if patient eats gluten freely without symptoms always skip',
            'Replaces A1C testing'
        ],
        'Autoimmune clustering occurs.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'Travel across time zones with insulin requires:',
        'Plan for dose timing adjustments with diabetes team guidance',
        [
            'Stop insulin during flight always',
            'Store insulin in checked baggage uninsulated in heat',
            'Ignore meal timing'
        ],
        'Travel plans prevent hypo and hyperglycemia.',
        [
            S.ADA_STANDARDS,
        S.ADA_DIAGNOSIS,
        S.CDC_DIABETES,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Expired diabetes test strips should be:',
        'Discarded; results may be inaccurate',
        [
            'Used if color looks fine',
            'Shared between patients',
            'Stored in humid bathroom'
        ],
        'Strip age and storage affect accuracy.',
        [
            S.FDA_CLIA_WAIVED,
        S.ADA_STANDARDS
        ],
        'beginner',
    ),
]
