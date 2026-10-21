# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Additional diabetes facts to expand ccma-diabetes to 112 total (four 28-question sets)."""

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    fact(
        'ccma-diabetes',
        'What is latent autoimmune diabetes in adults?',
        'Slowly progressive autoimmune diabetes in adults',
        [
            'Autoimmune diabetes that begins in infancy',
            'Diabetes limited to the three months after delivery',
            'Diabetes caused by a tumor in the head of the pancreas',
        ],
        'Latent autoimmune diabetes in adults is a slowly progressive autoimmune form that often looks like type 2 diabetes at first, with beta-cell antibodies and a growing need for insulin. Diabetes beginning in infancy is type 1, the three months after delivery describes gestational diabetes, and a pancreatic tumor produces a different form of diabetes.',
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
        'What causes most forms of maturity-onset diabetes of the young?',
        'A single gene defect with autosomal dominant inheritance',
        [
            'Autoimmune destruction of the pancreatic beta cells in the islets',
            'Insulin resistance driven by obesity and physical inactivity',
            'A complication of chronic pancreatitis in later adulthood',
        ],
        'Maturity-onset diabetes of the young results from a single gene defect, and most forms are inherited in an autosomal dominant pattern, so it is often misclassified as type 1 or type 2. Autoimmune beta-cell loss is type 1 diabetes, insulin resistance with obesity is the usual type 2 pattern, and chronic pancreatitis causes a different pancreatic form of diabetes.',
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
        'Why does a systemic glucocorticoid course raise blood glucose?',
        'Increased insulin resistance and hepatic glucose output',
        [
            'Destruction of the pancreatic beta cells by the steroid',
            'Increased renal excretion of glucose through the urine',
            'Reduced absorption of insulin from the injection site',
        ],
        'Glucocorticoids raise glucose by increasing hepatic glucose output and by making muscle and liver tissue less sensitive to insulin. They do not destroy beta cells, they do not excrete glucose in the urine, and reduced absorption from the injection site does not explain the pattern seen.',
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
        'Which form of diabetes can follow chronic pancreatitis?',
        'Diabetes from loss of both endocrine and exocrine function',
        [
            'Diabetes from autoimmune destruction of the pancreatic beta cells',
            'Diabetes from insulin resistance related to body weight and diet',
            'Diabetes from gestational hormone changes during pregnancy',
        ],
        'Chronic pancreatitis damages the pancreas, so loss of islet cells causes diabetes along with malabsorption from reduced exocrine enzymes. Autoimmune beta-cell destruction is type 1 diabetes, weight-related insulin resistance is type 2 diabetes, and gestational hormone changes describe diabetes that appears in pregnancy.',
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
        'What is cystic fibrosis-related diabetes?',
        'Diabetes that develops as cystic fibrosis progresses',
        [
            'Type 1 diabetes that appears in the first year of life',
            'Gestational diabetes caused by pancreatic enzyme therapy',
            'Type 2 diabetes caused by a high fat diet in childhood',
        ],
        'Cystic fibrosis-related diabetes is a separate form of diabetes that develops in people with cystic fibrosis, with insulin deficiency that becomes common as the lung disease progresses. Diabetes in the first year of life is type 1, enzyme therapy does not cause gestational diabetes, and diet alone does not produce type 2 diabetes in childhood.',
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
        'How can a hemoglobin variant affect an A1C result?',
        'It can make the A1C value falsely high or low',
        [
            'It can make a point of care glucose reading falsely high',
            'It can make a urine albumin screen result falsely high',
            'It can make the fasting insulin level result falsely high',
        ],
        'Hemoglobin variants change the red cell structure that the A1C assay measures, so the reported A1C can be falsely high or falsely low and an alternative test is used when the value does not fit the clinical picture. A variant does not shift a point of care glucose reading, a urine albumin screen, or a fasting insulin level.',
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
        'How does anemia affect the reliability of an A1C result?',
        'It can distort the A1C value in either direction',
        [
            'It can shorten the three month window that A1C reflects',
            'It can raise the fasting glucose drawn from the vein',
            'It can lower the urine albumin to creatinine ratio',
        ],
        'Anemia changes how quickly red cells turn over, so an A1C can read falsely high or falsely low depending on the type and severity, and the result is read in that context. Red cell turnover does not change the three month window the A1C covers, anemia does not move the fasting glucose value, and albumin excretion is not affected.',
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
        'A patient has a random plasma glucose of 200 mg/dL with polyuria, polydipsia, and weight loss. What is the diagnostic implication?',
        'Diabetes is confirmed without repeat confirmatory testing',
        [
            'Prediabetes is confirmed and needs repeat testing in a year',
            'The result is inconclusive and needs an oral glucose tolerance test',
            'A second confirmatory test is still required for the diagnosis',
        ],
        'A random plasma glucose of 200 mg/dL or higher together with classic hyperglycemia symptoms meets the ADA criterion for diabetes, so the diagnosis stands without a repeat test. Symptomatic hyperglycemia at this level is not prediabetes, an oral glucose tolerance test adds nothing when criteria are already met, and a second confirmatory test is not required in this situation.',
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
        'Which adults should be screened for type 2 diabetes?',
        'Overweight adults with one or more additional risk factors',
        [
            'Every adult who is overweight regardless of other risk factors',
            'Adults who have a family history of diabetes in a parent',
            'Adults who already show classic symptoms of hyperglycemia',
        ],
        'The ADA recommends testing adults who are overweight or obese and also carry a risk factor such as family history, hypertension, low physical activity, or a history of gestational diabetes. Screening every overweight adult regardless of other factors, screening on family history alone, and waiting for symptoms each miss the purpose of risk based screening.',
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
        'What is first-line pharmacotherapy for many adults with type 2 diabetes and no contraindications?',
        'Metformin along with lifestyle change',
        [
            'Insulin sliding scale along with lifestyle change',
            'A high dose steroid course along with lifestyle change',
            'No medication until the A1C reaches 10 percent',
        ],
        'Metformin with lifestyle modification is the usual starting therapy for type 2 diabetes when kidney function and other contraindications allow it. Sliding scale insulin is not a starting regimen, steroids raise glucose rather than treat it, and delaying medication until an A1C of 10 percent leaves the patient hyperglycemic for months.',
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
        'Which finding makes metformin unsafe to start?',
        'Severe kidney disease with a risk of lactic acidosis',
        [
            'Mild hypertension controlled with a single medication',
            'A body mass index of 27 in a newly diagnosed adult',
            'A family history of type 2 diabetes in a sibling',
        ],
        'Metformin is withheld in severe kidney disease and in acute conditions such as hypoxia or sepsis because of the risk of lactic acidosis, so the eGFR guides dosing and continuation. Controlled hypertension, a body mass index of 27, and a family history of diabetes are common reasons to use metformin rather than reasons to avoid it.',
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
        'What additional benefit can an SGLT2 inhibitor provide beyond lowering glucose?',
        'Heart and kidney protection in selected patients',
        [
            'Weight gain and an increased appetite in some patients',
            'A rapid cure of type 1 diabetes without insulin',
            'Protection that removes the need for kidney monitoring',
        ],
        'SGLT2 inhibitors block glucose reabsorption in the proximal tubule, and the resulting urinary glucose loss lowers the A1C while this class also reduces heart failure and kidney outcomes in selected patients. Weight gain, a cure for type 1 diabetes, and a reason to stop kidney monitoring are not effects of these drugs.',
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
        'What effect can a GLP-1 receptor agonist have in a patient with type 2 diabetes?',
        'Lower glucose with reduced appetite and weight loss',
        [
            'Lower glucose with weight gain in most patients',
            'Unchanged glucose with weight loss in most patients',
            'Lower glucose with no effect on body weight',
        ],
        'GLP-1 receptor agonists increase glucose-dependent insulin release and slow gastric emptying, so they lower glucose and often reduce appetite and body weight. Weight gain, no change in glucose, and no effect on weight each contradict the expected effect, and teaching about side effects is part of starting the drug.',
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
        'How do sulfonylureas such as glipizide lower blood glucose?',
        'By stimulating pancreatic beta cells to release insulin',
        [
            'By blocking glucose reabsorption in the kidney tubule',
            'By slowing carbohydrate absorption in the small intestine',
            'By increasing insulin sensitivity in muscle and liver',
        ],
        'Sulfonylureas close ATP-sensitive potassium channels in the beta cell, which triggers insulin release and lowers the glucose. Blocking renal reabsorption describes an SGLT2 inhibitor, slowing intestinal absorption describes an alpha-glucosidase inhibitor, and improving insulin sensitivity describes metformin.',
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
        'What does long-acting basal insulin such as glargine provide in a regimen?',
        'A steady background insulin level over 24 hours',
        [
            'A rapid insulin peak used to cover a single meal',
            'An intermediate insulin level lasting 4 to 12 hours',
            'A short acting insulin level lasting 5 to 8 hours',
        ],
        'Glargine is a long-acting analog with a flat and relatively steady action of about 24 hours that covers fasting and background needs between meals. Rapid peaks describe mealtime insulin analogs, a 4 to 12 hour profile describes NPH, and a 5 to 8 hour profile describes regular human insulin.',
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
        'When is rapid-acting insulin such as lispro usually given?',
        'At meals to cover the carbohydrate that follows',
        [
            'At bedtime to supply the basal insulin for the night',
            'Once each morning to supply the basal insulin for the day',
            'Every four hours to keep a constant blood glucose level',
        ],
        'Rapid-acting analogs such as lispro and aspart begin working in about 15 minutes and are given at meals to cover the post-meal glucose rise. Bedtime and morning basal doses describe long-acting insulin, and dosing every four hours is neither a mealtime nor a basal pattern.',
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
        'How are unopened insulin vials and pens stored?',
        'In the refrigerator until the expiration date',
        [
            'In the freezer for the entire labeled shelf life',
            'On a warm windowsill away from direct sunlight',
            'In a closed container at room temperature for a year',
        ],
        'Unopened insulin is stored in the refrigerator at the temperature on the label until it expires, and an opened vial or pen may be kept at room temperature for the number of days the product allows. Freezing damages insulin, a warm windowsill loses its potency, and a year at room temperature is far longer than any labeled in-use period.',
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
        'Which practice is correct for an insulin pen that has been opened and kept at room temperature?',
        'Use it within about 28 days of opening the pen',
        [
            'Use it for six months if the solution stays clear',
            'Use it for one year if the cap stays sealed',
            'Return it to the freezer after each daily dose',
        ],
        'An opened insulin pen is used within the in-use period the label allows, commonly 28 days, and temperature extremes are avoided because they damage the insulin. Six months and a year go well beyond that in-use window, and freezing insulin inactivates it.',
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
        'What do the trend arrows on a continuous glucose monitor tell the patient?',
        'The direction and the speed of the glucose change',
        [
            'The accuracy of the sensor compared with a lab value',
            'The number of carbohydrates the last meal contained',
            'The amount of insulin left in the pump reservoir',
        ],
        'Trend arrows show the direction and rate of glucose movement, which lets the patient anticipate a rise or a fall and act on the plan. Sensor accuracy is checked against a laboratory value, meal content comes from the meal log, and reservoir volume comes from the pump display.',
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
        'What time in range does the ADA set for many adults using a continuous glucose monitor?',
        'More than 70 percent of the day between 70 and 180 mg/dL',
        [
            'More than 50 percent of the day between 70 and 180 mg/dL',
            'More than 70 percent of the day between 54 and 70 mg/dL',
            'More than 90 percent of the day between 180 and 250 mg/dL',
        ],
        'The ADA target for many adults is more than 70 percent of the day, roughly 17 hours, within the 70 to 180 mg/dL range, along with less than 4 percent of time below range. A target of 50 percent sits below the goal, 54 to 70 mg/dL is the hypoglycemia range, and 180 to 250 mg/dL is above the target range.',
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
        'Which laboratory pattern is typical of diabetic ketoacidosis?',
        'High glucose, ketones, and an anion gap metabolic acidosis',
        [
            'High glucose, ketones, and a normal anion gap acidosis',
            'Normal glucose, ketones, and an anion gap metabolic acidosis',
            'High glucose, normal ketones, and an anion gap acidosis',
        ],
        'Diabetic ketoacidosis shows hyperglycemia with ketone production and a high anion gap metabolic acidosis, which makes it a medical emergency. A normal anion gap and a normal glucose do not fit the condition, and DKA involves ketone production rather than a normal ketone level.',
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
        'In which group does hyperosmolar hyperglycemic state most often occur?',
        'Older adults with type 2 diabetes and dehydration',
        [
            'Children with type 1 diabetes during an infection',
            'Adults with type 2 diabetes during a routine physical',
            'Newborns with transient neonatal hyperglycemia',
        ],
        'Hyperosmolar hyperglycemic state occurs most often in older adults with type 2 diabetes, where extreme hyperglycemia and profound dehydration develop over days. Children with type 1 diabetes more often present with ketoacidosis, a routine physical does not trigger it, and transient newborn hyperglycemia is a different condition.',
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
        'Which action belongs in the sick-day plan for a patient who takes insulin?',
        'Checking glucose more often and testing urine ketones',
        [
            'Stopping insulin until the illness resolves completely',
            'Restricting fluids to keep the blood sugar down',
            'Missing meals so the pancreas can rest',
        ],
        'Sick-day rules keep basal insulin going, add more frequent glucose checks, and include ketone testing when the glucose stays high, along with drinking fluids and calling the care team for persistent vomiting. Stopping insulin raises the risk of ketoacidosis, restricting fluids worsens dehydration, and missing meals does not protect the pancreas.',
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
        'When is urine ketone testing most useful for a patient with diabetes?',
        'When glucose stays high during an acute illness',
        [
            'When the patient is hypoglycemic and needs a snack',
            'When the A1C result comes back in the normal range',
            'When the patient is fasting before a routine blood draw',
        ],
        'Urine ketones are checked when glucose remains high and the patient is sick, because insulin deficiency combined with illness can tip a person with type 1 diabetes into ketoacidosis. Ketones are not checked for a low glucose, they do not replace A1C testing, and fasting for a routine draw does not raise ketone levels.',
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
        'When is a glucagon emergency kit used?',
        'For severe hypoglycemia when oral carbohydrate fails',
        [
            'For severe hyperglycemia when the patient cannot drink fluids',
            'For a mild episode of shakiness after a meal',
            'For suspected ketoacidosis before the ambulance arrives',
        ],
        'Glucagon is given when a person with diabetes has severe hypoglycemia and cannot safely swallow glucose, so a family member or caregiver gives it and calls emergency services. It does not lower high glucose, it is not needed for a mild episode that responds to a snack, and it does not treat ketoacidosis.',
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
        'What does hypoglycemia unawareness mean?',
        'Loss of the warning symptoms that usually signal a low',
        [
            'Feeling shaky whenever the glucose rises above 200 mg/dL',
            'Missing low readings because the meter battery is low',
            'Refusing to check glucose more than once a day',
        ],
        'Hypoglycemia unawareness is the loss of the autonomic warning signs such as shakiness and sweating that would normally prompt a person to treat a low, and it raises the risk of severe episodes. Shaking at a high glucose is not hypoglycemia, a low battery explains a missed reading, and refusing to check is a different problem.',
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
        'What does carbohydrate counting let a patient with diabetes do?',
        'Match the insulin dose to the meal being eaten',
        [
            'Match the insulin dose to the amount of protein eaten',
            'Match the insulin dose to the amount of fat eaten',
            'Match the insulin dose to the calories burned that day',
        ],
        'Carbohydrate counting matches the mealtime insulin dose to the grams of carbohydrate in a meal, since carbohydrate drives the post-meal glucose rise. Protein and fat affect glucose more slowly and in smaller amounts, and calories burned during the day do not set the meal dose.',
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
        'What does medical nutrition therapy for diabetes emphasize?',
        'An individualized eating plan built with a dietitian',
        [
            'The same strict diet for every person with diabetes',
            'A carbohydrate-free eating plan for all patients',
            'A single fad diet that most people follow for a month',
        ],
        'Medical nutrition therapy is an individualized plan built with a registered dietitian, covering carbohydrate quality, portion control, and the preferences and budget of the person. A single diet for everyone ignores the differences between patients, a carbohydrate-free plan removes the nutrient that affects glucose most, and a fad diet does not support lasting control.',
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
        'How does alcohol use affect glucose in a person with diabetes?',
        'It can cause delayed hypoglycemia with insulin or sulfonylureas',
        [
            'It can cause immediate hyperglycemia with insulin or sulfonylureas',
            'It can cause delayed hyperglycemia with insulin or sulfonylureas',
            'It can lower the A1C in a person who drinks every day',
        ],
        'Alcohol blocks gluconeogenesis, so a person who drinks while taking insulin or a sulfonylurea can drop low hours later, often overnight, and monitoring with food intake is part of the plan. Immediate hyperglycemia is not the classic effect, delayed hyperglycemia does not match the mechanism, and alcohol does not lower the A1C.',
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
        'What does smoking cessation improve for a person with diabetes?',
        'Cardiovascular and microvascular complication risk',
        [
            'Blood glucose control with no medication changes needed',
            'Insulin needs within the first month after quitting',
            'The recovery of feeling in the damaged nerves of the feet',
        ],
        'Smoking accelerates atherosclerosis and harms the small vessels that supply the eyes, nerves, and kidneys, so quitting lowers the risk of heart attack, stroke, and microvascular complications. Quitting does not change glucose control on its own, it does not change insulin needs in the first month, and damaged nerves do not regenerate faster because of it.',
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
        'What does the annual dilated eye exam for diabetes screen for?',
        'Diabetic retinopathy from retinal vessel damage',
        [
            'Glaucoma from a rise in pressure inside the eye',
            'Cataract changes that blur the lens inside the eye',
            'Macular degeneration from aging of the macula',
        ],
        'The annual dilated exam screens for diabetic retinopathy, which can be present without symptoms until vision changes occur, so the exam is scheduled on a fixed interval. Glaucoma, cataract, and macular degeneration are separate eye conditions, and the visit that looks for them is not the visit that tracks the diabetes related retinal changes.',
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
        'What does the urine albumin-to-creatinine ratio monitor in diabetes?',
        'Diabetic kidney disease in its early albuminuric stage',
        [
            'Diabetic retinopathy at its earliest microvascular stage',
            'Peripheral neuropathy before symptoms of numbness begin',
            'Cardiovascular disease before plaque builds up',
        ],
        'The urine albumin-to-creatinine ratio detects small amounts of albumin in the urine, which marks early diabetic kidney disease before the serum creatinine changes. Retinopathy is found on the dilated eye exam, neuropathy is found on foot and monofilament testing, and cardiovascular risk is assessed with blood pressure and lipid values.',
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
        'When is an ACE inhibitor or ARB commonly used in a patient with diabetes?',
        'When hypertension or albuminuria is present',
        [
            'When the patient reports episodes of mild hypoglycemia',
            'When the A1C result stays above 9 percent despite insulin',
            'When the patient has painful neuropathy in both feet',
        ],
        'ACE inhibitors and ARBs are used when a patient with diabetes also has hypertension or albuminuria, because they lower blood pressure and reduce albuminuria to protect the kidneys. They do not treat low glucose, they do not replace insulin for severe hyperglycemia, and they do not relieve neuropathic pain.',
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
        'What does statin therapy aim to achieve in an adult with diabetes over age 40?',
        'Lower LDL cholesterol and reduce cardiovascular events',
        [
            'Lower HDL cholesterol and reduce cardiovascular events',
            'Raise LDL cholesterol and reduce cardiovascular events',
            'Lower blood pressure and reduce cardiovascular events',
        ],
        'Statins lower LDL cholesterol and reduce the risk of heart attack and stroke, which matters because diabetes carries its own cardiovascular risk. Statins do not lower HDL, raise LDL, or lower blood pressure, so those changes do not explain the benefit that is being sought.',
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
        'What blood pressure goal does the ADA set for most adults with diabetes?',
        'Below 130/80 mmHg',
        [
            'Below 140/90 mmHg',
            'Below 150/95 mmHg',
            'Below 160/100 mmHg',
        ],
        'The ADA recommends a blood pressure goal below 130/80 mmHg for most adults with diabetes, and the reading is taken with a cuff sized for the arm and repeated when it is elevated. Goals of 140/90, 150/95, and 160/100 mmHg leave the cardiovascular and kidney risk of diabetes higher than current guidance accepts.',
        [
            S.ADA_STANDARDS,
        S.CDC_HBP,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'Which problem is caused by diabetic autonomic neuropathy?',
        'Gastroparesis with nausea and early satiety',
        [
            'Numbness of the fingertips with reduced sensation',
            'Visual loss from damage to the retinal vessels',
            'Protein in the urine from damage to the kidney filters',
        ],
        'Autonomic neuropathy affects the nerves that control automatic body functions, so gastroparesis with nausea and early satiety, orthostatic hypotension, and bladder or heart rhythm changes can occur. Numbness of the fingertips is peripheral neuropathy, retinal vessel damage causes diabetic retinopathy, and glomerular damage causes albuminuria.',
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
        'Which symptom pattern suggests painful diabetic peripheral neuropathy?',
        'Burning or shooting pain in the feet at night',
        [
            'Painless calluses and thick skin on the soles of the feet',
            'Cool pale feet with thin hair and absent pulses',
            'Red painful feet that worsen when the legs are lowered',
        ],
        'Painful diabetic neuropathy typically causes burning, tingling, or shooting pain in the feet or hands that is often worse at night. Thick callused skin reflects loss of protective sensation without pain, cool pale feet with hair loss suggest poor circulation, and dependent red pain points to ischemia rather than neuropathy.',
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
        'What does the 10-g monofilament foot test detect?',
        'Loss of protective sensation in the feet',
        [
            'Blood flow to the small arteries of the foot',
            'The ability to feel a vibration in the toes',
            'The presence of a foot ulcer under the callus',
        ],
        'The 10-g monofilament applies light pressure at several points on the foot, and a person who cannot feel it has lost protective sensation and is at high risk for ulcers. Vibration is tested separately with a tuning fork, an ulcer is found by looking at the skin, and ankle motion is checked during the foot exam instead.',
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
        'What footwear advice belongs in diabetes education?',
        'Well fitting shoes with the feet checked every day',
        [
            'Open sandals and thin flip flops for daily walking',
            'Thick insulated boots worn without a daily foot check',
            'The same tight pair of shoes worn until they wear out',
        ],
        'Footwear advice in diabetes centers on well fitting shoes, checking the feet daily, and getting care for any break in the skin, because neuropathy means injuries go unnoticed. Open sandals and thin flip flops invite injury, thick boots hide the changes that then get missed, and wearing a tight pair until it fails raises the risk of pressure damage.',
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
        'What is Charcot foot in a person with diabetes?',
        'Neuroarthropathy that fractures and deforms the foot',
        [
            'A simple sprain that settles with rest and ice',
            'A bacterial infection of the skin and the soft tissue',
            'A callus that forms where a shoe presses on the toe',
        ],
        'Charcot foot is neuroarthropathy in which trauma goes unnoticed because of neuropathy, and repeated injury destroys bone and joint structure, so offloading and immobilization are urgent. A simple sprain does not destroy bone, a skin and soft tissue infection is cellulitis, and a pressure callus is a separate finding.',
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
        'How is periodontal disease linked to diabetes?',
        'Both gum disease and glucose control affect each other',
        [
            'Gum disease changes the color of teeth but not the gums',
            'Gum disease worsens while the glucose control improves',
            'The two conditions share no common risk factors at all',
        ],
        'Periodontal disease and diabetes move together, because inflammation worsens insulin resistance and hyperglycemia makes gum infection harder to clear, so dental care belongs in diabetes care. Tooth color is unrelated to periodontal disease, the link runs in both directions rather than one, and the two conditions share risk factors such as smoking and poor glycemic control.',
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
        'Why is preconception counseling important for a woman with diabetes?',
        'High glucose at conception raises the risk of fetal defects',
        [
            'Insulin resistance that peaks in the first trimester',
            'Folic acid alone removes the risk of fetal defects',
            'The risk of fetal defects is highest after the baby is born',
        ],
        'Preconception counseling aims for glucose control before conception, because high glucose during the first weeks of pregnancy raises the risk of fetal defects and miscarriage. Insulin resistance does not peak in the first trimester, folic acid works alongside glucose control rather than replacing it, and the highest risk window falls before and early in pregnancy rather than after birth.',
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
        'When is gestational diabetes screening usually done?',
        'Between 24 and 28 weeks of pregnancy',
        [
            'Between 8 and 12 weeks of pregnancy',
            'Between 34 and 36 weeks of pregnancy',
            'Between 6 and 12 months after delivery',
        ],
        'Gestational diabetes screening is done between 24 and 28 weeks of pregnancy, when the insulin resistance of the second trimester is at its peak. Screening in the first trimester, late in the third trimester, and after delivery each miss the window that catches undiagnosed gestational diabetes.',
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
        'Which test is part of postpartum follow-up after gestational diabetes?',
        'A glucose test to look for persistent diabetes',
        [
            'A glucose test to look for persistent hypoglycemia',
            'A lipid panel to look for cholesterol problems in the infant',
            'A vitamin D test to look for bone loss in the mother',
        ],
        'Women with gestational diabetes are tested after delivery, again at the postpartum visit, and later with routine screening, because gestational diabetes signals a high risk of developing type 2 diabetes. Testing for persistent hypoglycemia, for infant cholesterol, and for maternal bone loss does not answer whether diabetes persists in the mother.',
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
        'What effect does breastfeeding have for a mother with diabetes?',
        'It often lowers maternal glucose during feeds',
        [
            'It stops the mother from needing insulin after delivery',
            'It causes neonatal hypoglycemia without monitoring',
            'It requires the mother to stop all glucose monitoring',
        ],
        'Breastfeeding often improves maternal glucose handling, and insulin needs may fall while the mother is lactating, so doses are adjusted with monitoring of both mother and infant. Breastfeeding does not remove the need for insulin, it does not cause neonatal hypoglycemia, and glucose monitoring continues throughout this period.',
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
        'Which accommodation is common in a diabetes plan for school or work?',
        'Permission to check glucose and eat a snack as needed',
        [
            'A private area that keeps the diabetes plan from others',
            'A daily insulin injection given by a school nurse',
            'A scheduled glucose check at the end of each workday',
        ],
        'A diabetes plan for school or work usually includes permission to check glucose and treat a low wherever the person is, along with access to supplies and a snack. Keeping the plan private removes the support that makes self management safe, injections are given by the person unless a written plan says otherwise, and checking glucose only at the end of the day misses problems during the day.',
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
        'What should a person with diabetes do before driving?',
        'Treat any low glucose and check the level before starting',
        [
            'Check the glucose level after reaching the destination',
            'Leaving the glucose check out on a short drive',
            'Drive on a long trip without carrying fast acting carbohydrate',
        ],
        'A person with diabetes checks glucose before driving, treats a low before starting, and carries fast acting carbohydrate in case a low happens on the road, because hypoglycemia impairs driving. Checking only after arrival, leaving out the check on a short drive, and driving without a carbohydrate supply each leave a real risk untreated.',
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
        'When is a less strict A1C goal accepted for an older adult?',
        'When health is limited and hypoglycemia risk is high',
        [
            'When the patient is younger than 65 and in good health',
            'When the patient is pregnant in the first trimester',
            'When the patient is newly diagnosed and still learning',
        ],
        'A less strict A1C goal is accepted for older adults with limited life expectancy, multiple comorbidities, or a history of severe hypoglycemia, because tight control adds risk without a clear benefit. Being under 65 with good health is the opposite situation, pregnancy calls for tighter control, and a new diagnosis is not a reason to relax the goal.',
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
        'What backup plan does a person on an insulin pump need?',
        'Rapid acting insulin and supplies if the pump stops',
        [
            'Oral tablets and a carbohydrate drink if the pump stops',
            'A second pump kept at home for the weekend',
            'A call to the clinic once a week to check the readings',
        ],
        'If a pump fails, the person needs rapid acting insulin, syringes, and supplies to return to injections, because without any insulin a person with type 1 diabetes can develop ketoacidosis within a day. Oral tablets do not replace insulin, a second pump does not cover a failed pump or a lost infusion site, and weekly calls do not protect against an interruption.',
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
        'What can sensor-augmented pump therapy do?',
        'Pause insulin when a low is predicted',
        [
            'Deliver a correction bolus with no patient input',
            'Measure glucose from an arterial line',
            'Predict the next meal and set the basal rate',
        ],
        'Some sensor-augmented pumps use the sensor trend to suspend or reduce basal insulin when a low is predicted, which helps prevent hypoglycemia, and a closed loop system can also deliver correction doses from sensor data. The pump still needs calibration and patient input, a continuous monitor measures interstitial glucose rather than arterial samples, and meal prediction does not set the basal rate.',
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
        'What is the dawn phenomenon in diabetes?',
        'An early morning glucose rise from growth hormone',
        [
            'An early morning glucose fall after a night time low',
            'A rapid glucose rise after a high carbohydrate meal',
            'A glucose rise that follows the morning insulin injection',
        ],
        'The dawn phenomenon is an early morning rise in glucose caused by growth hormone, cortisol, and catecholamines that oppose insulin before waking. A night time low with rebound describes the Somogyi effect, a post-meal rise describes ordinary postprandial hyperglycemia, and a rise after the morning dose points to a dose or timing problem instead.',
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
        'What does the Somogyi effect describe?',
        'Rebound hyperglycemia after a night time low',
        [
            'A stable overnight glucose that does not change',
            'A low glucose that follows the morning insulin dose',
            'A high glucose that follows a high carbohydrate dinner',
        ],
        'The Somogyi effect describes rebound hyperglycemia in the early morning after a nocturnal low, in which counter regulatory hormones raise the glucose after the dip. A stable overnight glucose, a low after the morning dose, and a post dinner rise describe other patterns that are not the Somogyi effect.',
        [
            S.ADA_STANDARDS,
        S.CDC_DIABETES_BASICS,
        S.MEDLINEPLUS_DIABETES
        ],
        'advanced',
    ),
    fact(
        'ccma-diabetes',
        'What is the usual structure of an inpatient insulin order?',
        'Scheduled basal insulin with correction and meal coverage',
        [
            'A correction scale with no scheduled basal insulin at all',
            'The home dose carried over with no provider review at all',
            'Oral agents with no insulin during the hospital admission',
        ],
        'Inpatient insulin orders are built around scheduled basal insulin with a correction scale and nutritional coverage, because a correction scale on its own leaves the patient without basal insulin. Carrying a home dose over without review ignores the needs of the admission, and oral agents do not cover a sick patient who is not eating.',
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
        'What is the main goal of diabetes management around surgery?',
        'Avoiding low and dangerously high glucose values',
        [
            'Keeping the glucose exactly normal for the whole day',
            'Stopping all glucose checks on the day of surgery',
            'Giving the usual home insulin dose without changes',
        ],
        'Perioperative diabetes care aims to keep glucose in a safe range, avoiding hypoglycemia from reduced intake and extreme hyperglycemia from surgical stress, with frequent checks and an insulin plan set by the team. Holding the value exactly normal is not realistic, stopping checks removes the safety net, and the home dose ignores fasting and stress changes.',
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
        'What is needed before metformin is given around a contrast CT?',
        'A kidney function check and a plan for holding it',
        [
            'A doubled metformin dose given to protect the kidneys',
            'A glucose tolerance test completed before the scan',
            'A urine ketone check completed before the scan',
        ],
        'Iodinated contrast can reduce kidney function, and metformin is often held around the scan when kidney function is low because of the risk of lactic acidosis, so an eGFR is checked and the decision documented. Doubling the dose worsens the risk, and glucose tolerance and urine ketone tests do not address kidney safety.',
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
        'What is the vaccine guidance for an adult with diabetes?',
        'Follow the schedule for flu and pneumococcal vaccines',
        [
            'Defer both vaccines until the A1C is below 7 percent',
            'Give the flu vaccine but not the pneumococcal vaccine',
            'Avoid both vaccines because diabetes raises fever risk',
        ],
        'Adults with diabetes are advised to receive the annual influenza vaccine and the pneumococcal vaccine on the recommended schedule, because an infection can destabilize glucose and cause serious illness. Deferring for an A1C target, giving one vaccine without the other, and avoiding both are not supported guidance.',
        [
            S.CDC_DIABETES,
        S.CDC_VACCINE_ADMIN,
        S.ADA_STANDARDS
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'How does diabetes distress differ from depression?',
        'It centers on the burden of daily self management',
        [
            'It centers on a loss of interest in daily activities',
            'It centers on a chemical imbalance in the brain',
            'It centers on the fear of needles and injections',
        ],
        'Diabetes distress is the emotional burden of managing diabetes day to day, such as guilt, frustration, and fear of complications, and it is not the same as a mood disorder. Loss of interest in activities describes depression, a chemical imbalance is not the working model for distress, and fear of injections is one narrow symptom rather than the whole condition.',
        [
            S.ADA_STANDARDS,
        S.CDC_DIABETES_BASICS,
        S.MEDLINEPLUS_DIABETES
        ],
        'intermediate',
    ),
    fact(
        'ccma-diabetes',
        'When should diabetes self-management education and support be offered?',
        'At diagnosis and again when needs change',
        [
            'Once when the patient enters the practice',
            'After a year of daily glucose logs are collected',
            'When the provider starts insulin therapy',
        ],
        'Diabetes self-management education and support should be offered at the time of diagnosis and again whenever the plan needs to change, such as with a new medication, a new complication, or a change in life circumstances. A single early session, waiting for a year of logs, and starting only with insulin each miss the point at which people need support.',
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
        'What is needed when a steroid dose is increased during an illness?',
        'More frequent glucose checks and a plan for insulin',
        [
            'A lower glucose target because steroids raise the A1C',
            'No change since steroids do not affect blood glucose',
            'A single glucose check at the end of the steroid course',
        ],
        'Steroids raise glucose in a dose related and unpredictable way, so glucose is checked more often and insulin is adjusted with the prescriber when the dose goes up. Lowering the target would risk hypoglycemia, steroids clearly do affect glucose, and one check at the end of the course misses the peak of the effect.',
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
        'What is important to know about fatty liver disease in type 2 diabetes?',
        'It is common and can progress to fibrosis over time',
        [
            'It is rare and has no connection to metabolic health',
            'It is cured by removing all carbohydrate from the diet',
            'It is found by a foot examination during a clinic visit',
        ],
        'Fatty liver disease is common in type 2 diabetes because insulin resistance drives fat into the liver, and it can progress to fibrosis, so weight management, metabolic control, and liver enzymes are followed over time. It is not rare, removing all carbohydrate is not a cure, and it is found with liver tests and imaging rather than with a foot exam.',
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
        'How does hypothyroidism affect diabetes care?',
        'It can worsen lipids and complicate glucose control',
        [
            'It can improve insulin sensitivity and lower the A1C',
            'It can raise blood glucose by destroying the beta cells',
            'It can replace the need for insulin in type 1 diabetes',
        ],
        'Hypothyroidism slows metabolism and tends to raise cholesterol and triglycerides, and it makes glucose control harder, so thyroid function is checked when symptoms appear or the diabetes course changes. Improved insulin sensitivity, destruction of the beta cells, and a replacement for insulin are not effects of low thyroid hormone.',
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
        'Why is celiac disease screening considered in type 1 diabetes?',
        'Autoimmune conditions cluster in the same patient',
        [
            'Celiac disease reduces the need for A1C testing',
            'Celiac disease is caused by the same insulin antibodies',
            'Celiac disease appears mostly in patients over 60',
        ],
        'Type 1 diabetes and celiac disease are both autoimmune conditions, so they cluster, and a person with unexplained diarrhea, weight loss, or poor control may need celiac testing. Celiac disease does not change the A1C testing schedule, it is not caused by insulin antibodies, and it appears in younger as well as older adults.',
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
        'What does a person with diabetes need for travel across time zones?',
        'A plan for insulin timing and meals with the team',
        [
            'A plan to keep every dose on the home clock time',
            'Extra insulin stored in checked baggage for the flight',
            'A plan to leave insulin out during the long flight hours',
        ],
        'Time zone changes shift the timing of meals and doses, so the person builds an adjustment plan with the diabetes team, keeps supplies in carry on luggage, and checks glucose more often during the change. Staying on the home clock puts doses at the wrong times, checked baggage can be lost or exposed to temperature extremes, and leaving insulin out risks ketoacidosis.',
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
        'What should be done with an expired box of glucose test strips?',
        'Discard them, because results may be inaccurate',
        [
            'Use them if the color of the strip looks normal',
            'Store them in a humid closet for later use',
            'Share them with another patient who has no strips',
        ],
        'Expired strips can give unreliable readings because the enzyme on the strip loses activity, so they are removed from service and replaced with in date strips. A normal looking strip can still read wrong, humidity speeds the loss of accuracy, and sharing strips between patients is not safe.',
        [
            S.FDA_CLIA_WAIVED,
        S.ADA_STANDARDS
        ],
        'beginner',
    ),
]
