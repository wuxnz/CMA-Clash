// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

// Diabetes flashcards drawn from the CDC diabetes pages listed on https://www.cdc.gov/diabetes/site.html.
// Facts are paraphrased from the pages named in each source comment. t = front, d = back, c = category index.

import type { Flashcard } from './phlebotomy-flashcards';

export const DIABETES_FLASHCARD_CATEGORIES = [
	'Types and causes',
	'Blood sugar and testing',
	'Complications',
	'Pregnancy and risk',
	'Treatment and care',
	'Day to day and emergencies'
];

export const DIABETES_FLASHCARDS: Flashcard[] = [
	// Types and causes (about-type-1-diabetes, about-type-2-diabetes, insulin-resistance-type-2-diabetes)
	{ t: 'What is type 1 diabetes?', d: 'A condition in which the pancreas makes little or no insulin, so people with it need insulin every day.', c: 0 },
	{ t: 'What is thought to cause type 1 diabetes?', d: 'An autoimmune reaction that destroys the insulin-producing beta cells in the pancreas.', c: 0 },
	{ t: 'What share of people with diabetes have type 1?', d: 'About 5 to 10 percent.', c: 0 },
	{ t: 'What share of people with diabetes have type 2?', d: 'About 90 to 95 percent.', c: 0 },
	{ t: 'What is type 2 diabetes?', d: 'A condition in which the body does not respond normally to insulin, so blood sugar stays too high.', c: 0 },
	{ t: 'What is insulin?', d: 'A hormone made by the pancreas that moves blood sugar from the bloodstream into cells, where it is used for energy.', c: 0 },
	{ t: 'What is insulin resistance?', d: 'Cells respond poorly to insulin, so the pancreas releases more of it to keep blood sugar in check.', c: 0 },
	{ t: 'How does insulin resistance relate to type 2 diabetes?', d: 'It sets the stage for prediabetes and type 2 diabetes. It is not caused by the body failing to make insulin.', c: 0 },
	{ t: 'Why can insulin not be taken as a pill?', d: 'Stomach acid would destroy it before it reached the bloodstream.', c: 0 },
	{ t: 'How can type 2 diabetes be prevented or delayed?', d: 'Losing weight, eating a healthy diet, and getting regular physical activity.', c: 0 },

	// Blood sugar and testing (prediabetes-a1c-test, low-blood-sugar-hypoglycemia, continuous-glucose-monitors, carb-counting)
	{ t: 'What does an A1C test measure?', d: 'Average blood sugar over roughly the past three months.', c: 1 },
	{ t: 'What A1C result is considered normal?', d: 'Below 5.7 percent.', c: 1 },
	{ t: 'What A1C range indicates prediabetes?', d: '5.7 to 6.4 percent.', c: 1 },
	{ t: 'What A1C result indicates diabetes?', d: '6.5 percent or more.', c: 1 },
	{ t: 'What blood sugar reading is considered low?', d: 'Under 70 mg/dL.', c: 1 },
	{ t: 'What reading is considered severe low blood sugar?', d: 'Under 54 mg/dL. It can cause fainting, so someone may need to help treat it.', c: 1 },
	{ t: 'What are common symptoms of low blood sugar?', d: 'A racing heartbeat, shaking, sweating, nervousness, confusion, dizziness, and hunger.', c: 1 },
	{ t: 'What is a continuous glucose monitor (CGM)?', d: 'A wearable device that tracks blood sugar in real time by measuring glucose in the fluid between cells just below the skin.', c: 1 },
	{ t: 'What do many CGMs do when blood sugar changes quickly?', d: 'They send alerts when blood sugar is rising or falling quickly.', c: 1 },
	{ t: 'What is carb counting?', d: 'Tracking the grams of carbohydrates in the foods and drinks you eat. People on mealtime insulin match their dose to the carbs they eat.', c: 1 },
	{ t: 'Which foods raise blood sugar?', d: 'Sugars and starches. Fiber does not raise blood sugar.', c: 1 },

	// Complications (diabetes-and-your-heart, diabetes-and-nerve-damage, diabetes-and-your-feet, diabetes-and-chronic-kidney-disease, diabetes-and-hearing-loss, diabetes-and-oral-health, diabetes-and-your-skin)
	{ t: 'How does diabetes affect heart disease risk?', d: 'Diabetes roughly doubles the risk of heart disease, and the risk rises the longer a person has diabetes.', c: 2 },
	{ t: 'How can blocked arteries cause a heart attack or stroke?', d: 'Plaque buildup can block blood flow to the heart, causing a heart attack, or to the brain, causing a stroke.', c: 2 },
	{ t: 'What is diabetic neuropathy?', d: 'Nerve damage caused by high blood sugar. Peripheral nerve damage, the most common type, usually starts in the feet.', c: 2 },
	{ t: 'Why is nerve damage in the feet dangerous?', d: 'Numbness can hide cuts, blisters, or sores, which can lead to infections and serious foot problems.', c: 2 },
	{ t: 'How often should you check your feet?', d: 'Every day, for skin, nail, or color changes. Use a mirror if you cannot see the bottoms of your feet.', c: 2 },
	{ t: 'What share of adults with diabetes has chronic kidney disease?', d: 'Roughly 1 in 3.', c: 2 },
	{ t: 'How can kidney disease from diabetes be found early?', d: 'Regular blood and urine tests, because it often has no symptoms early on.', c: 2 },
	{ t: 'How does hearing loss compare for people with diabetes?', d: 'It is about twice as common as in same-age people without diabetes.', c: 2 },
	{ t: 'How does diabetes affect gum health?', d: 'Gum disease can be more severe and take longer to heal in people with diabetes.', c: 2 },
	{ t: 'What do skin changes often signal?', d: 'Skin changes are one of the most common signs of diabetes.', c: 2 },

	// Pregnancy and risk (gestational-diabetes, screening-type-1-diabetes)
	{ t: 'What is gestational diabetes?', d: 'Diabetes that develops during pregnancy in a woman who did not have diabetes before.', c: 3 },
	{ t: 'When is gestational diabetes usually tested for?', d: 'Between weeks 24 and 28 of pregnancy, because it often has no symptoms.', c: 3 },
	{ t: 'What are risk factors for gestational diabetes?', d: 'A prior gestational diabetes diagnosis, a previous baby over 9 pounds, being overweight, a family history of type 2 diabetes, PCOS, and being African American, Hispanic or Latino, American Indian, Alaska Native, Native Hawaiian, or Pacific Islander.', c: 3 },
	{ t: 'What happens to women after gestational diabetes?', d: 'Roughly half later develop type 2 diabetes, so regular blood sugar checks after pregnancy are recommended.', c: 3 },
	{ t: 'Who should be offered type 1 screening?', d: 'People with a close family member who has type 1 diabetes, who are about 15 times more likely to develop it. Screening can begin at age 2.', c: 3 },

	// Treatment and care (4-ways-to-take-insulin, diabetes-doctors)
	{ t: 'What are ways to take insulin?', d: 'Syringe, insulin pen, insulin pump, and inhaled insulin used with a long-acting injectable insulin.', c: 4 },
	{ t: 'What is an insulin pump?', d: 'A device about the size of a small cell phone that delivers rapid-acting insulin through a thin tube placed under the skin.', c: 4 },
	{ t: 'Why do some people prefer an insulin pen?', d: 'It lets you dial in the dose and is often more comfortable than a syringe.', c: 4 },
	{ t: 'What does a primary care provider handle?', d: 'Routine care such as yearly checkups and prescriptions.', c: 4 },
	{ t: 'Who treats the feet and lower legs?', d: 'A podiatrist. Any sore on your foot should be seen right away.', c: 4 },
	{ t: 'When should an eye doctor check your eyes?', d: 'Soon after you are diagnosed with diabetes.', c: 4 },
	{ t: 'Why ask a pharmacist about medicines?', d: 'They can tell you which medicines, including over-the-counter ones, may affect your blood sugar.', c: 4 },

	// Day to day and emergencies (managing-sick-days, diabetic-ketoacidosis, diabetes-and-oral-health)
	{ t: 'How often should you check blood sugar when you are sick?', d: 'About every 4 hours, writing down the results. Drink plenty of fluids.', c: 5 },
	{ t: 'What should you do if urine tests positive for ketones?', d: 'Call your doctor right away.', c: 5 },
	{ t: 'When should you go to the emergency room during an illness?', d: 'If you cannot keep liquids down for more than 4 hours, or your blood sugar falls below 60 mg/dL.', c: 5 },
	{ t: 'What is diabetic ketoacidosis (DKA)?', d: 'A medical emergency that happens when the body lacks enough insulin. The liver breaks down fat for fuel and produces ketones that can build to dangerous levels.', c: 5 },
	{ t: 'What are early signs of DKA?', d: 'Being very thirsty and urinating much more than usual.', c: 5 },
	{ t: 'What are severe signs of DKA?', d: 'Fruity-smelling breath, fast deep breathing, and nausea or vomiting.', c: 5 },
	{ t: 'What causes DKA most often?', d: 'Illness, missed insulin shots, a clogged insulin pump, or the wrong insulin dose.', c: 5 },
	{ t: 'What should you do if ketones are high or blood sugar stays at 300 mg/dL or above?', d: 'Go to the emergency room or call 911 right away.', c: 5 },
	{ t: 'How should you care for your teeth and gums with diabetes?', d: 'Brush at least twice a day with fluoride toothpaste and floss daily. Smoking raises the risk of gum disease.', c: 5 }
];
