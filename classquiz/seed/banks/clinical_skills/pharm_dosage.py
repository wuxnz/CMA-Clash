# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-pharm-dosage)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-pharm-dosage-001
    fact(
        "skill-pharm-dosage",
        "How many micrograms are in 2.5 milligrams?",
        "2500 mcg",
        [
            "25 mcg",
            "250 mcg",
            "0.25 mcg",
        ],
        "Milligrams convert to micrograms by multiplying by 1000. Moving the decimal three places to the right on 2.5 mg yields 2500 mcg.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-002
    fact(
        "skill-pharm-dosage",
        "How many milligrams are in 0.5 grams?",
        "500 mg",
        [
            "50 mg",
            "5000 mg",
            "5 mg",
        ],
        "One gram equals 1000 milligrams. Multiplying 0.5 by 1000 gives 500 mg for label comparisons and tablet strength checks.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-003
    fact(
        "skill-pharm-dosage",
        "A provider orders 500 mg by mouth and the pharmacy supplies 250 mg tablets. How many whole tablets should be prepared for one dose?",
        "2 tablets",
        [
            "Half of one tablet",
            "4 tablets",
            "10 tablets",
        ],
        "Divide the ordered dose by the tablet strength: 500 divided by 250 equals 2. Giving fewer or more tablets would underdose or overdose the patient.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-pharm-dosage-004
    fact(
        "skill-pharm-dosage",
        "A vial is labeled 10 mg per mL. How many milliliters are needed to deliver 5 mg?",
        "0.5 mL",
        [
            "5 mL",
            "50 mL",
            "0.05 mL",
        ],
        "Desired dose divided by concentration gives volume: 5 mg divided by 10 mg per mL equals 0.5 mL. Confusing dose amount with volume is a common liquid medication error.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-005
    fact(
        "skill-pharm-dosage",
        "U-100 insulin contains how many units in each milliliter?",
        "100 units per mL",
        [
            "10 units per mL",
            "1000 units per mL",
            "1 unit per mL",
        ],
        "The U-100 designation means 100 insulin units occupy 1 mL of solution. Syringes marked in units are matched to this standard concentration for outpatient teaching.",
        [S.NHA_CCMA, S.CDC_DIABETES],
        "beginner",
    ),
    # skill-pharm-dosage-006
    fact(
        "skill-pharm-dosage",
        "Why do pediatric medication labels recommend oral syringes marked in milliliters instead of kitchen spoons?",
        "Household spoons vary in size and cause inconsistent liquid volumes",
        [
            "Household spoons are legally required for all pediatric antibiotics",
            "Unmarked kitchen cups measure liquids more precisely than syringes",
            "Standard teaspoon sizes are identical in every home kitchen",
        ],
        "FDA medication safety messaging discourages teaspoon dosing because families use different utensils. A syringe with milliliter marks gives a reproducible volume for each administration.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-007
    fact(
        "skill-pharm-dosage",
        "A medication label reads 250 mg per 5 mL. How many milliliters provide 100 mg?",
        "2 mL",
        [
            "20 mL",
            "0.2 mL",
            "5 mL",
        ],
        "First find mg per mL: 250 divided by 5 equals 50 mg per mL. Then 100 mg divided by 50 mg per mL equals 2 mL for the ordered amount.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-008
    fact(
        "skill-pharm-dosage",
        "On a stock bottle, a ratio strength of 1:1000 for a liquid usually means what?",
        "1 gram of drug in 1000 mL of solution",
        [
            "1 milligram in 1000 liters",
            "1000 grams in 1 milliliter",
            "1 part drug in 1 part solvent without volume units",
        ],
        "Ratio strengths express drug mass per total solution volume. Recognizing the 1:1000 pattern helps compare labels before measuring a dose.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-009
    fact(
        "skill-pharm-dosage",
        "Before pouring or drawing any medication, which label elements must be verified?",
        "Patient identity, drug name, dose, route, and expiration when shown",
        [
            "Cap color matched to the order without reading the drug name",
            "Pharmacy street address when the medication looks familiar",
            "Lot number alone when tablet strength is assumed without dose check",
        ],
        "The rights of medication administration start with reading the complete label against the order. Partial checks do not confirm identity or dose.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-010
    fact(
        "skill-pharm-dosage",
        "How many milligrams equal 1500 micrograms?",
        "1.5 mg",
        [
            "15 mg",
            "0.15 mg",
            "150 mg",
        ],
        "Divide micrograms by 1000 to convert to milligrams. One thousand five hundred micrograms becomes 1.5 milligrams on a pediatric liquid label.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-011
    fact(
        "skill-pharm-dosage",
        "A child weighs 22 pounds and the clinic scale displays kilograms. Which value is closest to the weight in kilograms for dosing charts?",
        "10 kg",
        [
            "22 kg",
            "5 kg",
            "50 kg",
        ],
        "Dividing pounds by about 2.2 converts to kilograms: 22 divided by 2.2 is approximately 10 kg. Pediatric mg per kg orders require weight in kilograms.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-012
    fact(
        "skill-pharm-dosage",
        "On an insulin syringe barrel marked in units, what do those unit marks represent for U-100 insulin?",
        "U-100 insulin units, not milligrams of drug",
        [
            "Milligrams of oral hypoglycemic tablets",
            "Milliequivalents of intravenous electrolyte solution",
            "Milliliters of normal saline flush volume",
        ],
        "Insulin syringes are calibrated for insulin units when paired with U-100 product. Confusing units with milligrams or milliliters from other syringes causes large dosing mistakes.",
        [S.CDC_DIABETES, S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-013
    fact(
        "skill-pharm-dosage",
        "A provider orders 1 gram by mouth once daily and tablets are 500 mg each. How many tablets make one dose?",
        "2 tablets",
        [
            "1 tablet",
            "4 tablets",
            "Half tablet",
        ],
        "Convert grams to milligrams: 1 gram equals 1000 mg. One thousand divided by 500 mg per tablet equals 2 tablets for the daily dose.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-pharm-dosage-014
    fact(
        "skill-pharm-dosage",
        "A child weighs 20 kg and the order reads 5 mg per kg by mouth once. What total milligram dose is indicated?",
        "100 mg",
        [
            "25 mg",
            "5 mg",
            "200 mg",
        ],
        "Multiply weight by the mg per kg factor: 20 times 5 equals 100 mg. Using the child's weight in pounds without converting would underdose a kilogram-based order.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-015
    fact(
        "skill-pharm-dosage",
        "A topical solution is labeled ratio strength 1:10. How many grams of drug are present in 10 mL of that solution?",
        "1 gram",
        [
            "10 grams",
            "0.1 gram",
            "100 grams",
        ],
        "A 1:10 ratio means 1 part drug in 10 parts total solution by the label convention used on many stock bottles. Ten milliliters of this product therefore contains about 1 gram of active drug.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-016
    fact(
        "skill-pharm-dosage",
        "Facility policy states oral tablets may be rounded to the nearest whole tablet when the scored tablet allows safe splitting. The calculation yields 1.5 tablets. What is the usual preparation?",
        "1.5 scored tablets when splitting is allowed",
        [
            "3 whole tablets when half tablets are not permitted",
            "0.25 tablet without prescriber clarification",
            "0 tablets withheld until the next scheduled visit",
        ],
        "When half tablets are within policy and the product is scored, 1.5 tablets matches the math. Rounding up to 3 tablets or omitting the dose would deviate from the order without prescriber input.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-017
    fact(
        "skill-pharm-dosage",
        "A liquid order calculates to 2.64 mL and policy requires rounding oral liquids to the nearest 0.1 mL on an oral syringe. What volume should be measured?",
        "2.6 mL",
        [
            "2.0 mL",
            "3.0 mL",
            "2.64 mL without a calibrated device",
        ],
        "Rounding 2.64 to one decimal place gives 2.6 mL on a syringe that can read tenths. Guessing unmarked graduations or rounding to whole milliliters without policy guidance adds error.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-018
    fact(
        "skill-pharm-dosage",
        "A cream is labeled 2% w/v. How many grams of drug are in 100 mL of that cream?",
        "2 grams",
        [
            "20 grams",
            "0.2 grams",
            "200 grams",
        ],
        "Percent weight in volume for solids in liquid means grams per 100 mL. Two percent w/v equals 2 grams per 100 mL, which helps compare strengths between products.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-019
    fact(
        "skill-pharm-dosage",
        "Look-alike sound-alike medication pairs in the clinic require which safety practice?",
        "Tall-man lettering with independent double-check",
        [
            "Store look-alike vials together in one unlabeled supply bin",
            "Identify drugs by cap color without reading the full drug name",
            "Verify the first letter of the drug name on the product label",
        ],
        "FDA medication safety resources highlight tall-man lettering and independent verification to reduce swaps between similar names. Cap color alone does not distinguish drug identity.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-020
    fact(
        "skill-pharm-dosage",
        "A pediatric order states 15 mg per kg per day divided into three doses. The child weighs 12 kg. What is each single dose if the total daily dose is split evenly?",
        "60 mg per dose",
        [
            "15 mg per dose",
            "180 mg per dose",
            "45 mg per dose",
        ],
        "Total daily amount is 15 times 12, which equals 180 mg. Dividing by three doses gives 60 mg per administration. Forgetting to split the daily total leads to triple dosing.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-021
    fact(
        "skill-pharm-dosage",
        "The order is for 0.25 mg and the pharmacy supplies 0.5 mg scored tablets. How many tablets should be prepared if splitting is allowed?",
        "One-half tablet",
        [
            "Two tablets",
            "One whole tablet",
            "Four tablets",
        ],
        "Half of a 0.5 mg tablet delivers 0.25 mg. A whole 0.5 mg tablet would double the ordered amount unless the prescriber changes the order.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-022
    fact(
        "skill-pharm-dosage",
        "A vial reads 40 mg per mL. The order is for 10 mg intramuscular. What volume should be drawn?",
        "0.25 mL",
        [
            "2.50 mL",
            "4.00 mL",
            "10.0 mL",
        ],
        "Ten milligrams divided by 40 milligrams per milliliter equals 0.25 milliliter. Drawing the ordered milligram number as milliliters would be a tenfold overdose.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-023
    fact(
        "skill-pharm-dosage",
        "Which scenario describes a wrong-route medication error?",
        "Giving an intramuscular antibiotic as an intravenous push",
        [
            "Placing a transdermal patch on clean dry intact skin as ordered",
            "Swallowing an oral tablet with water per the medication order",
            "Instilling ordered ophthalmic drops into the conjunctival sac",
        ],
        "Route changes absorption rate and toxicity. Intramuscular products given intravenously can cause rapid harm, whereas correct topical, oral, and ophthalmic routes follow the order.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-024
    fact(
        "skill-pharm-dosage",
        "You discover a multi-dose vial past its expiration date while preparing a routine injection. What is the appropriate action?",
        "Replace the expired vial and document wasted product",
        [
            "Administer the dose if the volume needed is small",
            "Double the ordered dose to offset lost drug potency",
            "Pour the remainder into an unlabeled container for later use",
        ],
        "Expired medications may lack potency or stability. FDA medication safety practice expects staff to withhold expired products and involve pharmacy replacement rather than improvising doses.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-025
    fact(
        "skill-pharm-dosage",
        "A parent asks to measure children's acetaminophen with a dining spoon. What teaching aligns with safe outpatient dosing?",
        "Provide an oral syringe marked in milliliters and show how to read it",
        [
            "Tell them that a kitchen spoon holds exactly 5 mL",
            "Convert milliliters to tablespoons without using a measuring device",
            "Estimate the volume by how full the bottle looks when it is on the shelf",
        ],
        "Metric oral syringes improve accuracy for pediatric liquids. Household utensils are not standardized, so volume should be demonstrated on a labeled syringe.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-026
    fact(
        "skill-pharm-dosage",
        "An order reads 7.5 mg by mouth and tablets are 2.5 mg each. How many tablets should be given?",
        "3 tablets",
        [
            "2 tablets",
            "1 tablet",
            "7 tablets",
        ],
        "Seven point five divided by two point five equals three tablets. Miscounting by one tablet changes the dose by one-third of the order.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-027
    fact(
        "skill-pharm-dosage",
        "A solution concentration is 4 mg per mL. How many milligrams are in 2.5 mL?",
        "10 mg",
        [
            "1 mg",
            "6.5 mg",
            "40 mg",
        ],
        "Multiply concentration by volume: 4 mg per mL times 2.5 mL equals 10 mg. Adding concentrations and volumes without multiplying yields incorrect totals.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-028
    fact(
        "skill-pharm-dosage",
        "High-alert medications in the clinic often require which extra step before administration?",
        "Second-staff double-check of order, calculation, and dose",
        [
            "Single staff sign-off when patient volume delays the schedule",
            "Chart the dose after giving it without reading the vial label",
            "Give the dose without recalculation when strength matches prior order",
        ],
        "Independent verification catches calculation and selection errors before they reach the patient. High-alert drugs have narrow safety margins described in medication safety literature.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-029
    fact(
        "skill-pharm-dosage",
        "A child weighs 33 pounds. What weight in kilograms should be used for a 10 mg per kg order?",
        "15 kg",
        [
            "33 kg",
            "7 kg",
            "66 kg",
        ],
        "Thirty-three pounds divided by 2.2 is approximately 15 kilograms. Using pounds directly in a mg per kg formula would greatly overdose the child.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-pharm-dosage-030
    fact(
        "skill-pharm-dosage",
        "Why should insulin not be measured with a tuberculin syringe marked in milliliters when teaching U-100 insulin?",
        "Tuberculin syringes use milliliters, not insulin units",
        [
            "Insulin must be drawn with a 10 mL venipuncture syringe",
            "U-100 insulin has no fixed units-to-volume relationship",
            "Tuberculin syringes are labeled in insulin units for injectables",
        ],
        "U-100 insulin dosing is expressed in units on insulin syringes. A tuberculin syringe lacks unit graduations matched to insulin labeling, increasing the risk of tenfold errors.",
        [S.CDC_DIABETES, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-031
    fact(
        "skill-pharm-dosage",
        "A neonate weighs 3.5 kg. The order reads 2 mg per kg every 8 hours. What is each dose in milligrams?",
        "7 mg",
        [
            "3.5 mg",
            "14 mg",
            "2 mg",
        ],
        "Multiply 3.5 kg by 2 mg per kg to get 7 mg per dose. The every-8-hours interval defines frequency but does not change the per-dose milligram amount.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-pharm-dosage-032
    fact(
        "skill-pharm-dosage",
        "You must prepare 0.2 mg from a 1:1000 stock solution labeled as 1 gram per 1000 mL. How many milliliters contain 0.2 mg of drug?",
        "0.2 mL",
        [
            "2 mL",
            "20 mL",
            "0.02 mL",
        ],
        "One gram per 1000 mL equals 1 mg per mL. Zero point two milligrams therefore requires 0.2 mL of stock. Treating ratio labels as milligrams per drop causes large errors.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-033
    fact(
        "skill-pharm-dosage",
        "Policy allows whole tablets when the calculated dose is 2.3 tablets and the drug cannot be split. The tablets are 10 mg. What dose is given if rounding down per protocol?",
        "20 mg as two whole tablets",
        [
            "23 mg as two and one-third tablets",
            "30 mg as three whole tablets",
            "0 mg until a liquid is available",
        ],
        "Rounding down to two whole tablets delivers 20 mg instead of the calculated 23 mg. Protocol usually requires notifying the prescriber when rounding changes the therapeutic amount.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-034
    fact(
        "skill-pharm-dosage",
        "Heparin for subcutaneous injection is ordered in units, while many oral drugs are ordered in milligrams. What is the key safety step when switching between these products?",
        "Match vial units to the syringe scale before calculating volume",
        [
            "Convert all unit-based injectables to milligrams with one fixed factor",
            "Measure heparin units with a U-100 insulin syringe on the usual scale",
            "Record milligrams on the MAR for every unit-labeled injectable product",
        ],
        "Heparin and insulin use unit-based labeling distinct from milligram concentrations. Verifying the unit on the vial and order prevents applying the wrong formula.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-pharm-dosage-035
    fact(
        "skill-pharm-dosage",
        "A pediatric liquid calculates to 1.74 mL. Policy rounds oral volumes to the nearest 0.1 mL. What should be drawn on the oral syringe?",
        "1.7 mL of the oral liquid",
        [
            "1.74 mL without tenths",
            "2.0 mL because liquids round up",
            "1.0 mL for simpler charting",
        ],
        "One point seven four rounds to one point seven at the tenths place. Rounding up to 2 mL without policy would exceed the calculated dose for a narrow therapeutic drug.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-036
    fact(
        "skill-pharm-dosage",
        "Dimensional analysis: how many milliliters of a 50 mg per 5 mL suspension are needed for a 30 mg dose?",
        "3 mL",
        [
            "6 mL",
            "1.5 mL",
            "0.3 mL",
        ],
        "Concentration is 10 mg per mL after dividing 50 by 5. Thirty milligrams divided by 10 mg per mL equals 3 mL. Inverting the ratio during setup is a frequent student error.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-037
    fact(
        "skill-pharm-dosage",
        "A patient brings U-500 insulin from home. What teaching priority differs from standard U-100 syringes?",
        "Use a U-500 syringe and teach that concentration differs from U-100",
        [
            "Draw U-500 in a U-100 insulin syringe on the same unit scale as usual",
            "Treat U-500 as 5 units per mL like dilute intravenous fluids",
            "Assume all insulin vials share identical units-per-mL labeling",
        ],
        "U-500 insulin is five times more concentrated than U-100. Matching device and training to the labeled concentration prevents catastrophic under- or overdosing.",
        [S.CDC_DIABETES, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-pharm-dosage-038
    fact(
        "skill-pharm-dosage",
        "A 1% w/v solution is prepared for patient use. How many milligrams of drug are in 5 mL of a true 1% w/v aqueous solution?",
        "50 mg",
        [
            "5 mg",
            "500 mg",
            "1 mg",
        ],
        "One percent w/v equals 1 gram per 100 mL, or 10 mg per mL. Five milliliters therefore contain 50 mg. Percent labels must be converted before comparing to milligram orders.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-039
    fact(
        "skill-pharm-dosage",
        "A child weighs 48 pounds and the order is 8 mg per kg once daily. The liquid is 40 mg per mL. What volume should be prepared after converting weight?",
        "4.4 mL after kg conversion and tenths rounding",
        [
            "8 mL from mg per kg math using pounds as kilograms",
            "0.8 mL from mg per kg math using pounds as kilograms",
            "48 mL from mg per kg math using pounds as kilograms",
        ],
        "Forty-eight pounds is about 21.8 kg, times 8 mg per kg equals roughly 174 mg. One hundred seventy-four divided by 40 mg per mL is about 4.35 mL, often rounded per local oral liquid policy.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-pharm-dosage-040
    fact(
        "skill-pharm-dosage",
        "Your calculation exceeds the clinic's published maximum single dose for an oral antibiotic in children. What is the appropriate next step?",
        "Contact the prescriber to clarify before preparing the dose",
        [
            "Administer the calculated dose because math overrides clinic maximums",
            "Give half the calculated dose and omit documentation of the change",
            "Prepare the dose and defer prescriber contact until the next clinic day",
        ],
        "Maximum dose tables and prescriber limits protect against transcription and weight entry errors. Clarification is required when math conflicts with policy or reference maxima.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-041
    fact(
        "skill-pharm-dosage",
        "The medication administration record shows 10 units of insulin but the order reads 8 units at lunch. What action fits medication safety practice?",
        "Hold the dose, reconcile MAR with order, and call the prescriber",
        [
            "Give 10 units because the MAR entry overrides the written order",
            "Give 8 units and erase the MAR discrepancy without documentation",
            "Average 9 units from the MAR and order without notifying the team",
        ],
        "Discrepancies between the order and MAR require resolution before injection. Administering the higher undocumented amount risks hypoglycemia without prescriber awareness.",
        [S.FDA_MEDICATION_SAFETY, S.CDC_DIABETES],
        "advanced",
    ),
    # skill-pharm-dosage-042
    fact(
        "skill-pharm-dosage",
        "A ratio of 1:100 on a local anesthetic label is interpreted as 1 gram per 100 mL. How many milligrams are in 2 mL?",
        "20 mg",
        [
            "200 mg",
            "2 mg",
            "0.2 mg",
        ],
        "One gram per 100 mL equals 10 mg per mL. Two milliliters then contain 20 mg. Misreading 1:100 as milligrams per milliliter directly leads to tenfold mistakes.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
