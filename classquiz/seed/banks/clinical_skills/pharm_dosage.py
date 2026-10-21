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
        "Household spoons vary in size and can cause inaccurate volumes",
        [
            "Spoons are required by law for every liquid antibiotic",
            "Milliliter syringes are less accurate than unmarked cups",
            "Teaspoons are calibrated identically in every home when staff rely on memory from a prior patient with a similar name",
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
        "Patient match, drug name, dose, route, and expiration when visible",
        [
            "Cap color matched to the order without reading the name",
            "Pharmacy address when the drug name is familiar",
            "Lot number alone when the strength is assumed without recording the dose on the medication administration record",
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
        "Insulin units at the U-100 concentration, not milligrams of drug",
        [
            "Milligrams of oral metformin",
            "Milliequivalents of electrolyte",
            "Milliliters of saline flush when the clinic is behind schedule and checks are abbreviated",
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
        "1 and one-half tablets if the tablet is scored and the order permits splitting",
        [
            "3 tablets because halves are forbidden",
            "Quarter tablet without prescriber clarification",
            "0 tablets until the next visit without reading the expiration date on the product label",
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
        "Tall-man lettering on labels and an independent double-check before administration",
        [
            "Storing all vials in one unlabeled bin when barcode equipment is turned off to reduce alert noise",
            "Relying on cap color as the sole identifier",
            "Verifying the first letter of the drug name without the full name",
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
            "2.5 mL",
            "4 mL without notifying the prescriber about a refused or missed dose",
            "10 mL",
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
            "Placing a transdermal patch on clean dry skin as ordered",
            "Administering an oral tablet with a sip of water when partial doses are saved for a different patient later",
            "Instilling ordered eye drops into the conjunctival sac",
        ],
        "Route changes absorption rate and toxicity. Intramuscular products given intravenously can cause rapid harm, whereas correct oral, topical, and ophthalmic routes follow the order.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-024
    fact(
        "skill-pharm-dosage",
        "You discover a multi-dose vial past its expiration date while preparing a routine injection. What is the appropriate action?",
        "Do not use the product; obtain a current supply and follow wastage documentation",
        [
            "Administer it if the dose is small without comparing the drug name and strength to the prescriber order",
            "Double the dose to compensate for lost potency",
            "Transfer the contents into an unlabeled cup for later",
        ],
        "Expired medications may lack potency or stability. FDA medication safety practice expects staff to withhold expired products and involve pharmacy replacement rather than improvising doses.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-pharm-dosage-025
    fact(
        "skill-pharm-dosage",
        "A parent asks to measure children's acetaminophen with a dining spoon. What teaching aligns with safe outpatient dosing?",
        "Provide or recommend an oral syringe marked in milliliters and show how to read the meniscus",
        [
            "Tell them any spoon from the drawer is exactly 5 mL",
            "Convert milliliters to tablespoons without a measuring device",
            "Estimate volume by how full the bottle feels when the package resembles another medication on the shelf",
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
        "Independent double-check of order, calculation, and prepared dose by second qualified staff",
        [
            "Single staff verification when the clinic is behind schedule and patient volumes are high",
            "Documentation after administration without reading the product label on the vial",
            "Skipping dose calculation when the vial strength matches a familiar prior order",
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
        "Tuberculin syringes are graduated in milliliters, not insulin units, which invites unit-to-volume confusion",
        [
            "Insulin must be drawn with a 10 mL venipuncture syringe",
            "U-100 insulin has no defined relationship to volume when staff rely on memory from a prior patient with a similar name",
            "Tuberculin syringes are approved for all injectable hormones",
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
        "20 mg as 2 tablets",
        [
            "23 mg as 2.3 tablets",
            "30 mg as 3 tablets without prescriber contact",
            "0 mg until a liquid formulation arrives next month",
        ],
        "Rounding down to two whole tablets delivers 20 mg instead of the calculated 23 mg. Protocol usually requires notifying the prescriber when rounding changes the therapeutic amount.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-034
    fact(
        "skill-pharm-dosage",
        "Heparin for subcutaneous injection is ordered in units, while many oral drugs are ordered in milligrams. What is the key safety step when switching between these products?",
        "Read the label unit of measure and match the syringe or device to that unit before calculating volume",
        [
            "Assume every injectable uses milligrams per milliliter without recording the dose on the medication administration record",
            "Convert units to milligrams with one fixed factor for all drugs",
            "Use the same syringe graduations for insulin and heparin interchangeably",
        ],
        "Heparin and insulin use unit-based labeling distinct from milligram concentrations. Verifying the unit on the vial and order prevents applying the wrong formula.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-pharm-dosage-035
    fact(
        "skill-pharm-dosage",
        "A pediatric liquid calculates to 1.74 mL. Policy rounds oral volumes to the nearest 0.1 mL. What should be drawn on the oral syringe?",
        "1.7 mL",
        [
            "1.74 mL on a device without tenths",
            "2.0 mL because all liquids round up",
            "1.0 mL to simplify charting",
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
        "Use the syringe and patient education matched to U-500 because concentration differs from U-100",
        [
            "U-500 may be drawn in a tuberculin syringe using the same unit marks as U-100",
            "U-500 has 5 units per mL like normal saline when the clinic is behind schedule and checks are abbreviated",
            "Unit markings are identical on every insulin product without reading the label",
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
        "4.4 mL rounded per policy",
        [
            "8 mL using pounds as kilograms",
            "0.8 mL without weight conversion",
            "48 mL matching the pound value",
        ],
        "Forty-eight pounds is about 21.8 kg, times 8 mg per kg equals roughly 174 mg. One hundred seventy-four divided by 40 mg per mL is about 4.35 mL, often rounded per local oral liquid policy.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-pharm-dosage-040
    fact(
        "skill-pharm-dosage",
        "Your calculation exceeds the clinic's published maximum single dose for an oral antibiotic in children. What is the appropriate next step?",
        "Stop and clarify the order with the prescriber before preparing the dose",
        [
            "Give the calculated amount because math overrides policy",
            "Split the dose across two unrelated patients without reading the expiration date on the product label",
            "Halve the dose silently without documentation",
        ],
        "Maximum dose tables and prescriber limits protect against transcription and weight entry errors. Clarification is required when math conflicts with policy or reference maxima.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-pharm-dosage-041
    fact(
        "skill-pharm-dosage",
        "The medication administration record shows 10 units of insulin but the order reads 8 units at lunch. What action fits medication safety practice?",
        "Hold the dose, recheck the order and blood glucose log, and contact the prescriber per protocol",
        [
            "Give 10 units because the MAR is usually wrong when barcode equipment is turned off to reduce alert noise",
            "Give 8 units and erase the MAR entry without note",
            "Average the two numbers without telling anyone",
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
