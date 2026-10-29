// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

// Diabetes flashcards checked against the full text of the CDC diabetes pages listed on
// https://www.cdc.gov/diabetes/site.html. Facts are paraphrased from the pages named in each
// source comment. t = front, d = back, c = category index.

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
	{ t: 'What is thought to cause type 1 diabetes?', d: 'An autoimmune reaction that destroys the insulin-producing beta cells in the pancreas. Diet and lifestyle do not cause it.', c: 0 },
	{ t: 'What share of people with diabetes have type 1?', d: 'About 5 to 10 percent.', c: 0 },
	{ t: 'What share of people with diabetes have type 2?', d: 'About 90 to 95 percent.', c: 0 },
	{ t: 'What is type 2 diabetes?', d: 'A condition in which cells do not respond normally to insulin, so blood sugar stays too high.', c: 0 },
	{ t: 'What is insulin?', d: 'A hormone made by the pancreas that acts like a key to let blood sugar into cells for use as energy.', c: 0 },
	{ t: 'What is insulin resistance?', d: 'Cells respond poorly to insulin, so the pancreas releases more of it to keep blood sugar in check.', c: 0 },
	{ t: 'How is insulin resistance different from type 1 diabetes?', d: 'People with insulin resistance do not respond well to insulin. People with type 1 do not make enough insulin to survive.', c: 0 },
	{ t: 'Why can insulin not be taken as a pill?', d: 'Stomach acid would destroy it before it reached the bloodstream.', c: 0 },
	{ t: 'How can type 2 diabetes be prevented or delayed?', d: 'Losing weight if you have overweight, eating a healthy diet, and getting regular physical activity.', c: 0 },
	{ t: 'Who is at higher risk for type 2 diabetes?', d: 'People with prediabetes or overweight, people 45 or older, people with a parent, brother, or sister who has type 2, and people who are active less than 3 times a week.', c: 0 },
	{ t: 'Which groups are at higher risk for type 2 diabetes?', d: 'African American, Hispanic or Latino, American Indian, and Alaska Native people. Some Pacific Islander and Asian American people are also at higher risk.', c: 0 },
	{ t: 'What is acanthosis nigricans?', d: 'Dark, velvety patches of skin in body creases such as the neck, armpits, or groin. It is a sign of insulin resistance.', c: 0 },

	// Blood sugar and testing (prediabetes-a1c-test, low-blood-sugar-hypoglycemia, continuous-glucose-monitors, carb-counting)
	{ t: 'What does an A1C test measure?', d: 'Average blood sugar over the past 3 months.', c: 1 },
	{ t: 'What A1C result is considered normal?', d: 'Below 5.7 percent.', c: 1 },
	{ t: 'What A1C range indicates prediabetes?', d: '5.7 to 6.4 percent.', c: 1 },
	{ t: 'What A1C result indicates diabetes?', d: '6.5 percent or above.', c: 1 },
	{ t: 'What blood sugar reading is considered low?', d: 'Below 70 mg/dL.', c: 1 },
	{ t: 'What reading is considered severe low blood sugar?', d: 'Below 54 mg/dL. It can make you faint, so someone may need to help treat it.', c: 1 },
	{ t: 'What are common symptoms of low blood sugar?', d: 'Fast heartbeat, shaking, sweating, nervousness or anxiety, irritability or confusion, dizziness, and hunger.', c: 1 },
	{ t: 'What can cause nighttime low blood sugar?', d: 'An active day, being active close to bedtime, taking too much insulin, or drinking alcohol at night.', c: 1 },
	{ t: 'What is hypoglycemia unawareness?', d: 'Having no symptoms when blood sugar is low. It makes severe lows more likely, and it is more likely after more than 5 to 10 years of diabetes or with frequent lows.', c: 1 },
	{ t: 'What is a continuous glucose monitor (CGM)?', d: 'A wearable device that tracks blood sugar in real time by measuring glucose in the fluid between cells just below the skin.', c: 1 },
	{ t: 'Why do you still need fingersticks with a CGM?', d: 'Glucose in the fluid between cells can differ from blood glucose, so an occasional fingerstick checks that the CGM is accurate.', c: 1 },
	{ t: 'How often are CGM sensors replaced?', d: 'Every 7 to 14 days.', c: 1 },
	{ t: 'What is carb counting?', d: 'Tracking the grams of carbohydrates in the foods and drinks you eat. People who take mealtime insulin match their dose to the carbs they eat.', c: 1 },
	{ t: 'Which foods raise blood sugar?', d: 'Sugars and starches. Fiber does not raise blood sugar.', c: 1 },

	// Complications (diabetes-and-your-heart, diabetes-and-nerve-damage, diabetes-and-your-feet, diabetes-and-chronic-kidney-disease, diabetes-and-hearing-loss, diabetes-and-oral-health, diabetes-and-your-skin)
	{ t: 'How does diabetes affect heart disease risk?', d: 'People with diabetes have twice the risk of heart disease, and the risk rises the longer they have diabetes.', c: 2 },
	{ t: 'How can plaque cause a heart attack or stroke?', d: 'Plaque buildup can block blood flow to the heart, causing a heart attack, or to the brain, causing a stroke.', c: 2 },
	{ t: 'What is diabetic neuropathy?', d: 'Nerve damage caused by high blood sugar. Peripheral nerve damage is the most common type, and it usually starts in the feet.', c: 2 },
	{ t: 'What are the four main types of nerve damage?', d: 'Peripheral, autonomic, proximal, and focal. It is possible to have more than one type.', c: 2 },
	{ t: 'Why is nerve damage in the feet dangerous?', d: 'Numbness can hide cuts, blisters, or sores, which can lead to infections and serious foot problems.', c: 2 },
	{ t: 'How often should you check your feet?', d: 'Every day, even if they feel fine. Use a mirror if you cannot see the bottoms of your feet, or ask a family member to help.', c: 2 },
	{ t: 'What share of adults with diabetes has chronic kidney disease?', d: 'About 1 in 3.', c: 2 },
	{ t: 'How can kidney disease from diabetes be found early?', d: 'With regular blood and urine tests, because it often develops slowly with few symptoms.', c: 2 },
	{ t: 'How does hearing loss compare for people with diabetes?', d: 'It is about twice as common as in people the same age who do not have diabetes.', c: 2 },
	{ t: 'How does diabetes affect gum health?', d: 'Gum disease can be more severe and take longer to heal in people with diabetes.', c: 2 },
	{ t: 'What do skin changes often signal?', d: 'Skin changes are one of the most common signs of diabetes.', c: 2 },

	// Pregnancy and risk (gestational-diabetes, screening-type-1-diabetes)
	{ t: 'What is gestational diabetes?', d: 'Diabetes that develops during pregnancy in a woman who did not already have diabetes.', c: 3 },
	{ t: 'When is gestational diabetes usually tested for?', d: 'Between weeks 24 and 28 of pregnancy, because it often has no symptoms.', c: 3 },
	{ t: 'What are risk factors for gestational diabetes?', d: 'A previous gestational diabetes diagnosis, a previous baby over 9 pounds, being overweight, a family history of type 2 diabetes, PCOS, and being African American, Hispanic or Latino, American Indian, Alaska Native, Native Hawaiian, or Pacific Islander.', c: 3 },
	{ t: 'What happens to women after gestational diabetes?', d: 'About half later develop type 2 diabetes, so regular blood sugar checks after pregnancy are recommended.', c: 3 },
	{ t: 'Who should be offered type 1 screening?', d: 'People with a family member who has type 1 diabetes, who are about 15 times more likely to develop it. Screening can begin at age 2.', c: 3 },

	// Treatment and care (4-ways-to-take-insulin, diabetes-doctors)
	{ t: 'What are four ways to take insulin?', d: 'Syringe, insulin pen, insulin pump, and insulin inhaler.', c: 4 },
	{ t: 'What is an insulin pump?', d: 'A device about the size of a small cell phone that gives short- or rapid-acting insulin through a thin tube placed under the skin.', c: 4 },
	{ t: 'Why do some people prefer an insulin pen?', d: 'You dial the dose on the pen, and many people find it more comfortable than a syringe.', c: 4 },
	{ t: 'What does a primary care provider handle?', d: 'Routine care such as yearly checkups, physical exams, lab tests, and prescriptions.', c: 4 },
	{ t: 'What does an endocrinologist treat?', d: 'Hormone problems. Diabetes affects how the body produces and uses insulin, so an endocrinologist may help manage it.', c: 4 },
	{ t: 'Who treats the feet and lower legs?', d: 'A podiatrist. If you notice sores on your feet or legs, see a foot doctor right away.', c: 4 },
	{ t: 'When should you have an eye exam after a diabetes diagnosis?', d: 'As soon as you are diagnosed, because diabetes can damage the blood vessels in the eyes.', c: 4 },
	{ t: 'When should your hearing be tested after a diabetes diagnosis?', d: 'When you first find out you have diabetes.', c: 4 },
	{ t: 'Why ask a pharmacist about your medicines?', d: 'They can tell you which medicines, including over-the-counter ones, may affect your blood sugar.', c: 4 },

	// Day to day and emergencies (managing-sick-days, diabetic-ketoacidosis, diabetes-and-oral-health)
	{ t: 'How often should you check blood sugar when you are sick?', d: 'Every 4 hours, keeping track of the results. Keep drinking fluids.', c: 5 },
	{ t: 'What should you do if urine tests positive for ketones?', d: 'Call your doctor right away. You will probably need hospital treatment.', c: 5 },
	{ t: 'When should you go to the emergency room during an illness?', d: 'Examples include being unable to keep liquids down for more than 4 hours, blood sugar below 60 mg/dL, or trouble breathing.', c: 5 },
	{ t: 'What is diabetic ketoacidosis (DKA)?', d: 'A serious, life-threatening complication that develops when the body does not have enough insulin. The liver breaks down fat for fuel and makes ketones, which can build up to dangerous levels.', c: 5 },
	{ t: 'What are early signs of DKA?', d: 'Being very thirsty and urinating much more than usual.', c: 5 },
	{ t: 'What are severe signs of DKA?', d: 'Fast, deep breathing, fruity-smelling breath, nausea and vomiting, and stomach pain, among others.', c: 5 },
	{ t: 'What most often causes DKA?', d: 'Illness, missed insulin shots, a clogged insulin pump, or the wrong insulin dose.', c: 5 },
	{ t: 'What should you do if your blood sugar stays at 300 mg/dL or above?', d: 'Go to the emergency room or call 911 right away.', c: 5 },
	{ t: 'How should you care for your teeth and gums with diabetes?', d: 'Brush your teeth at least twice a day with fluoride toothpaste, floss at least once a day, and tell your dentist you have diabetes.', c: 5 }
];
