# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-med-safety)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [

    # skill-med-safety-001
    fact(
        "skill-med-safety",
        "Which set of checks makes up the classic six rights of medication administration?",
        "Right patient, drug, dose, route, time, and documentation",
        [
            "Right patient, drug, dose, route, time, and pharmacy schedule",
            "Right patient, drug, dose, route, time, and insurance coverage",
            "Right patient, drug, dose, route, time, and room assignment",
        ],
        "The six rights confirm the patient, drug, dose, route, time, and the recording of the dose before and after it is given. Pharmacy scheduling, insurance coverage, and room assignment are administrative details that do not verify the medication itself.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-002
    fact(
        "skill-med-safety",
        "How should patient identity be confirmed before giving a medication in clinic?",
        "Two identifiers, such as name and date of birth, confirmed with the patient",
        [
            "A single identifier, such as the full name, confirmed with the patient first",
            "The room number on the exam room sign, checked against the schedule",
            "The medical record number on the chart header read before preparation",
        ],
        "Two identifiers are required for every medication administration, and the patient is asked to state them so both match the chart. A single name or a medical record number alone is not enough, and a room number identifies a place rather than a person.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-003
    fact(
        "skill-med-safety",
        "Which label elements are compared with the prescriber's order before a medication is administered?",
        "Drug name, strength, dose, and route",
        [
            "Drug name, strength, and manufacturer",
            "Expiration date, lot number, and storage notes",
            "Tablet color, imprint code, and package size",
        ],
        "The order names the drug, strength, dose, and route, so those are the label details that must match before administration. Manufacturer, expiration date, lot number, storage notes, and tablet appearance support inventory and identification but do not confirm that the ordered product is in hand.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-004
    fact(
        "skill-med-safety",
        "When in the workflow should documented medication allergies be reviewed?",
        "Before selecting or administering any drug, including vaccines and contrast",
        [
            "After the dose is given and entered on the administration record",
            "At the annual wellness visit when no prescriptions are ordered",
            "When the patient requests a refill of an unrelated over-the-counter medication",
        ],
        "Allergy status is reviewed before a drug is selected or given, because a reaction follows exposure and cannot be undone. Reviewing after the dose, tying it to the annual wellness visit, or limiting it to refill requests leaves allergy information out of the decision.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-005
    fact(
        "skill-med-safety",
        "A provider order reads metformin 500 mg by mouth twice daily. Which verification step is most critical?",
        "Match the written drug name and dose to the label on the dispensed container",
        [
            "Compare the drug name on the label with the medication list in the chart",
            "Verify the drug name on the label against the pharmacy inventory record",
            "Confirm that the prescriber's signature and date appear on the printed order",
        ],
        "The label on the dispensed container is the last checkpoint before the drug reaches the patient, so the written name and dose must match it. Comparing the label with the chart or the inventory record confirms identity without confirming the ordered dose, and a signature check says nothing about the product in hand.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-006
    fact(
        "skill-med-safety",
        "Which strategies help manage look-alike sound-alike medication pairs?",
        "Tall-man lettering, separate storage, and independent double checks",
        [
            "Tall-man lettering, shared storage, and independent double checks",
            "Tall-man lettering, separate storage, and a single-operator check",
            "Cap color coding, shared storage, and observation of the first check",
        ],
        "Look-alike sound-alike names are managed by making the written name distinct, storing the products apart, and having a second person check the selection independently. Shared storage invites picking the wrong carton, a single-operator check removes the second set of eyes, and cap color does not reliably tell two similar products apart.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-007
    fact(
        "skill-med-safety",
        "What qualifies insulin and anticoagulants as high-alert medications in ambulatory settings?",
        "The potential for significant patient harm if the drug is used in error",
        [
            "The number of steps required to prepare the drug before administration",
            "The frequency with which the drug is prescribed in ambulatory practices",
            "The requirement to store the drug at a controlled room temperature",
        ],
        "High-alert status reflects the injury a medication can cause when it is used incorrectly, and insulin and anticoagulants can produce severe hypoglycemia or serious bleeding from small errors. Preparation steps, prescribing frequency, and storage requirements do not define the high-alert classification.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-008
    fact(
        "skill-med-safety",
        "What does medication reconciliation at an office visit compare?",
        "The patient's home medication list with current orders to find discrepancies",
        [
            "The clinic's formulary list with the medications stocked in the exam rooms",
            "The patient's insurance benefits with the pharmacy's generic drug price list",
            "The provider's order set with the medications kept in the supply room",
        ],
        "Reconciliation compares what the patient actually takes at home with the orders written today so omissions, duplications, and dose changes are caught. Formulary lists, insurance benefits, price lists, and supply room stock describe what is available rather than what the patient is taking.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-009
    fact(
        "skill-med-safety",
        "What does barcode medication administration add to the medication safety process?",
        "An electronic match of patient, product, and order before the dose",
        [
            "An electronic match of patient, product, and order after the dose is given",
            "A printed record of the product dispensed and the patient",
            "A second signature from another staff member on the administration record",
        ],
        "Barcode administration adds an electronic check that the patient, the product, and the order match at the moment the dose is given. Matching after the dose, printing a paper record, and adding a co-signature are separate steps that do not substitute for the point-of-administration match.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-010
    fact(
        "skill-med-safety",
        "How should a near-miss medication error caught before reaching the patient be handled?",
        "Reported through the facility incident system so the cause can be corrected",
        [
            "Recorded in the patient chart as a note about the medication order",
            "Discussed with the staff who were working the clinic when it happened",
            "Handed to the pharmacy so the prescription can be checked before dispensing",
        ],
        "Near misses reveal where a system can fail before a patient is harmed, so they go into the facility incident system where the cause can be corrected. A chart note, a verbal discussion with the staff on duty, and a call to the pharmacy record the event but do not feed the safety review.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-011
    fact(
        "skill-med-safety",
        "How does unit-dose packaging in clinic help reduce medication errors?",
        "It provides a single premeasured amount that requires less manipulation",
        [
            "It provides the full supply of a drug that staff portion out at each visit",
            "It provides a labeled bottle that stays with the patient for self-administration",
            "It provides a premeasured amount that can be split for several doses",
        ],
        "Unit-dose packaging delivers one premeasured amount in a labeled package, so staff neither measure nor manipulate the product before administration. Bulk bottles, bedside stock, and dividing a unit across doses all put back the measurement steps that cause errors.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-012
    fact(
        "skill-med-safety",
        "Why does a topical medication order specify the application site?",
        "Site affects absorption and rotation limits local irritation",
        [
            "Site determines which brand of product the pharmacy dispenses",
            "Site records the room and bed where treatment occurred",
            "Site confirms the expiration date printed on the tube",
        ],
        "Where a topical drug is placed changes how much the body absorbs, and rotating sites reduces local irritation and cumulative toxicity, so the order names the site. Brand selection, treatment location, and expiration dating come from the prescription and the product itself.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-013
    fact(
        "skill-med-safety",
        "What is required when controlled substances are counted in clinic?",
        "Two staff members witness the count and both sign the log",
        [
            "One staff member counts and records the amount in the log",
            "Two staff members record the count but the log carries one signature",
            "A supervisor reviews the count after the end of the month",
        ],
        "Controlled substance counts rely on dual verification, so two staff members witness the same count and both sign the record. Counting alone, signing without a second witness, and reviewing totals after the fact leave gaps in the chain of custody.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-014
    fact(
        "skill-med-safety",
        "What basis should be used when calculating a pediatric liquid medication dose?",
        "Milligrams per kilogram from a verified reference with double-checked math",
        [
            "The standard adult dose scaled down by the child's age in years and weight",
            "The volume of liquid left in the bottle after the previous dose was given",
            "A household tablespoon measure converted into a metric volume for the child",
        ],
        "Pediatric liquid doses are calculated from the child's weight in milligrams per kilogram using a verified reference, and the arithmetic is checked by a second person. Scaling adult doses by age, reusing the volume left from the last dose, and measuring with household spoons all produce doses that can be far above or below the intended amount.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-015
    fact(
        "skill-med-safety",
        "Why must insulin syringes match the concentration printed on the vial?",
        "U-100 and U-500 insulin put a different number of units in each milliliter",
        [
            "U-100 and U-500 insulin are drawn with syringes of different barrel sizes",
            "U-100 and U-500 insulin carry different expiration dates on the vial",
            "U-100 and U-500 insulin have different storage times once the vial is opened",
        ],
        "Insulin syringes are calibrated in units for a specific concentration, and U-100 and U-500 put a different number of units in every milliliter, so the wrong syringe draws the wrong unit count. Barrel size, expiration dates, and storage times do not explain why the match matters.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-016
    fact(
        "skill-med-safety",
        "Why should medication orders write 0.5 mg instead of .5 mg?",
        "A leading zero prevents a missed decimal and a tenfold overdose",
        [
            "A leading zero confirms the prescriber intends a weight-based dose",
            "A leading zero indicates the strength was checked against a record",
            "A leading zero marks the order as a controlled substance needing a signature log",
        ],
        "A missing leading zero lets the decimal point be overlooked, so .5 mg can be read as 5 mg and produce a tenfold overdose. Confirming a weight-based intent, verifying the strength against a pharmacy record, and marking a controlled substance are separate documentation steps that do not prevent the misread.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-017
    fact(
        "skill-med-safety",
        "What should the medical assistant do when a medication order contains an unclear abbreviation?",
        "Contact the prescriber or pharmacist for clarification before preparation",
        [
            "Use the meaning that appears most often on the clinic's order set",
            "Ask a coworker which medication the abbreviation usually stands for",
            "Document the ambiguity in the chart and continue with the order as written",
        ],
        "Ambiguous abbreviations such as qd, IU, and MS have contributed to sentinel events, so the order is clarified with the prescriber or pharmacist before the drug is prepared. Guessing from the order set or from what coworkers say repeats the error, and charting the ambiguity while giving the drug does not make the dose safe.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-018
    fact(
        "skill-med-safety",
        "What can happen if an enteric-coated tablet is crushed without authorization?",
        "The coating is destroyed so the drug irritates the stomach and acts faster",
        [
            "The coating stays intact so the drug still passes into the intestine intact",
            "The tablet becomes a timed release so the ordered dose is spread across the day",
            "The drug is absorbed more slowly because the coating delays the release",
        ],
        "Crushing an enteric-coated tablet removes the coating that keeps the drug away from stomach acid, so the drug irritates the lining and is released faster than intended. A coating that stays intact describes a tablet that was not crushed, a timed release describes a different formulation, and slower absorption is the opposite of what happens.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-019
    fact(
        "skill-med-safety",
        "What should each staff member verify during an independent double check of a high-alert drug?",
        "The order, product label, dose, route, and patient separately",
        [
            "The order and dose, while watching the other person prepare the product",
            "The product label and patient, while the first person signs the log",
            "The log entry after the dose has already been given",
        ],
        "An independent double check means each person reviews the order, the product, the dose, the route, and the patient separately instead of accepting the other person's conclusion. Watching the preparation, checking part of the order, and reviewing the record after the dose has gone in do not add a second set of eyes.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-020
    fact(
        "skill-med-safety",
        "How should medication samples in clinic be handled?",
        "Stored securely, logged, and dispensed with counseling documented",
        [
            "Left in an unlocked drawer for patients to take as they need them",
            "Dispensed from the sample closet without an entry in the log",
            "Kept in the staff break room and logged after the clinic session",
        ],
        "Samples are medications, so they are stored securely, entered in the sample log, and handed over with counseling about use and expiration. Leaving them for patients to take as they wish, dispensing them without a log entry, and keeping them in a break room each remove the traceability that sample handling requires.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-021
    fact(
        "skill-med-safety",
        "What should a medical assistant do when a patient brings herbal supplements to a medication reconciliation visit?",
        "Record the product names and doses in the medication list for provider review",
        [
            "Record the product names in the social history section of the patient's chart",
            "Record the supplement names on the allergy list so interactions are flagged",
            "Wait for the provider to ask about supplements before recording them",
        ],
        "Supplements interact with prescribed drugs and affect perioperative plans, so their names and doses belong in the medication list where the provider reviews them. Social history, the allergy list, and waiting for the provider to ask each put the information where it cannot inform medication decisions.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-022
    fact(
        "skill-med-safety",
        "What should be done with expired medications found in an exam room?",
        "Removed from patient areas and disposed of as pharmaceutical waste",
        [
            "Moved to the back of the shelf so the oldest stock is dispensed first",
            "Combined with the current stock so that the bottle count stays accurate",
            "Returned to the supplier with a note about the quantity that was found",
        ],
        "Expired products may have lost potency or stability, so they are pulled from patient care areas and disposed of through pharmaceutical waste procedures. Rotating them to the back shelf, mixing them with current stock, and returning them undocumented all leave unusable drugs where they could reach a patient.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-023
    fact(
        "skill-med-safety",
        "What safety practice is illustrated by a verbal read-back of the drug name and dose during a double check?",
        "A closed-loop communication check that catches drug selection errors",
        [
            "A method for confirming the patient's identity with a single identifier",
            "A way to confirm allergy status with the patient before administration",
            "A way to document the medication that was given in the chart",
        ],
        "Reading the drug name and dose back aloud forces an exact, shared confirmation between the person checking and the person preparing, which catches selection errors before the dose is given. Identity checks, allergy questions, and charting the medication are separate steps that the read-back supports but does not replace.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-024
    fact(
        "skill-med-safety",
        "What error risk increases when potassium chloride vials are stored next to saline flush bags?",
        "The wrong solution is selected when the flush is prepared",
        [
            "The potassium dose is diluted to an incorrect volume",
            "The flush is hung at a higher rate than the order states",
            "The expiration date on the vial is misread at the medication cart",
        ],
        "Concentrated potassium chloride can be mistaken for the flush volume when the two sit side by side, so separating them reduces the chance of grabbing the wrong vial. Dilution errors, flow rate errors, and misread expiration dates are separate hazards that storage placement does not address.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-med-safety-025
    fact(
        "skill-med-safety",
        "What documentation is needed when a patient refuses an ordered medication?",
        "The offer made, the patient's response, and provider notification",
        [
            "The drug name, the ordered dose, and the scheduled administration time",
            "The pharmacy label, the prescription number, and the dispensing date",
            "The insurance copay, the visit type, and the billing code",
        ],
        "A refused dose is charted with the fact that it was offered, the patient's response, and notification of the provider so the plan of care can be adjusted. Drug and schedule details, pharmacy labeling, and billing information are recorded elsewhere and do not document the refusal.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-026
    fact(
        "skill-med-safety",
        "What response is required when a medication error is discovered after administration?",
        "Immediate assessment, provider notification, and ongoing monitoring",
        [
            "Correction of the chart entry with the patient told at the next visit",
            "Provider notification at the end of the shift with monitoring at the visit",
            "Monitoring of the patient at the next visit with the chart corrected",
        ],
        "Once an error reaches the patient the response has to be immediate, because antidotes, labs, and monitoring may change the outcome. Correcting the chart quietly, notifying the provider at the end of the shift, and waiting for the next visit all delay care that may be time sensitive.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-027
    fact(
        "skill-med-safety",
        "What does tall-man lettering emphasize when comparing hydralazine and hydroxyzine?",
        "Dissimilar letter segments inside two look-alike drug names",
        [
            "The number of syllables in each of the two drug names",
            "The alphabetical position of each name in the formulary",
            "The strength of each drug available in single and unit doses",
        ],
        "Tall-man lettering highlights the differing letters inside names that look alike, so the eye and the ear catch the distinction during selection and verbal orders. Syllable counts, formulary placement, and available strengths do not help separate one name from the other.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-028
    fact(
        "skill-med-safety",
        "What should staff do when a barcode scanning mismatch alert appears?",
        "Stop, investigate the discrepancy, and resolve it before proceeding",
        [
            "Override the alert and document that the dose was given anyway",
            "Give the medication while another staff member investigates the alert",
            "Note the alert in the chart and continue with the ordered dose",
        ],
        "A barcode mismatch means the scan found a discrepancy in the patient, product, or dose, so the dose stops until the discrepancy is understood and corrected. Overriding the alert, giving the drug while someone else investigates, and charting the warning all move the medication past the check that exists to catch it.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-029
    fact(
        "skill-med-safety",
        "When should medication reconciliation occur after a hospital discharge?",
        "At the first follow-up visit and again whenever the orders change",
        [
            "At the first follow-up visit and then not again until the annual visit",
            "After the patient has been home for a full month without contact",
            "When the patient returns for an annual wellness examination",
        ],
        "A discharge summary and any new prescriptions create gaps and duplications, so reconciliation belongs at the first post-discharge visit and again whenever the orders change. Waiting for the annual physical, waiting a month with no contact, or waiting for an annual visit leaves the list unreliable while the patient is taking the most medicines.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-030
    fact(
        "skill-med-safety",
        "What should a suspiciously large opioid prescription for a new patient trigger?",
        "Verification with the prescriber and a check for diversion risk",
        [
            "Dispensing the prescription as written because it is signed by the provider",
            "Dispensing a smaller quantity than the prescription requests",
            "Delivering the medication to the patient with a shorter refill interval",
        ],
        "An unusual opioid quantity for a new patient is a signal to confirm the intent, the dose, and the prescriber's plan before dispensing, and to consider diversion risk. A signed order, a reduced quantity given without prescriber agreement, and a shorter refill interval each react to the concern without verifying it.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-031
    fact(
        "skill-med-safety",
        "What risks arise from pouring liquid medication from a stock bottle into an unlabeled cup?",
        "Wrong dose and wrong patient administration",
        [
            "Extra documentation work and longer visits for the patient",
            "Higher supply cost and more frequent stock room deliveries",
            "Longer wait times and less time for the provider visit",
        ],
        "Liquid poured into an unmarked cup loses both its measured volume and its identity, so the dose can be wrong or go to the wrong patient. Documentation workload, supply cost, and appointment length are affected by clinic operations rather than by the dosing error the practice creates.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-032
    fact(
        "skill-med-safety",
        "What do time-critical medications such as certain antibiotics require regarding administration timing?",
        "Administration within the prescribed windows documented on the MAR",
        [
            "Administration at the first convenient time during the clinic session",
            "Administration batched at the end of the session to save staff time",
            "Administration deferred when the stock runs low during the day",
        ],
        "Time-critical drugs are ordered for specific intervals, so doses are given inside those windows and the time is charted on the administration record. Giving a dose at a convenient time, batching doses at the end of the session, and deferring a dose for stock reasons all change drug levels unpredictably.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-033
    fact(
        "skill-med-safety",
        "What technique should the medical assistant follow when preparing medications from multidose vials?",
        "Use a new sterile needle and syringe for each entry and date the vial",
        [
            "Keep the needle in the vial between patients and cover the hub with a cap",
            "Rinse the vial with saline between patients and keep it refrigerated",
            "Label the vial with the date and return it to stock once the contents are gone",
        ],
        "Each entry into a multidose vial is a new access that can introduce contaminants, so a fresh sterile needle and syringe are used and the opened vial is dated for its beyond-use time. Leaving a needle in the hub, rinsing the vial between patients, and returning an emptied vial to stock all keep contamination and cross-use risks in place.",
        [S.CDC_INJECTION_SAFETY, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-034
    fact(
        "skill-med-safety",
        "What does patient teach-back after new medication counseling help confirm?",
        "Understanding of dose, route, timing, and side effects to report",
        [
            "That the patient has signed the informed consent for the drug",
            "That the patient has read the printed handout from the pharmacy",
            "That the patient can state the name of the pharmacy that filled it",
        ],
        "Teach-back asks the patient to describe the dose, route, timing, and what to report in their own words, which shows whether the counseling landed. Signed consent, reading a handout, and naming the dispensing pharmacy are other kinds of confirmation that do not test understanding.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-035
    fact(
        "skill-med-safety",
        "What is required when wasting partial doses of controlled substances?",
        "Witnessed disposal with the waste documented in the controlled substance log",
        [
            "Disposal into the sink with the amount recorded at the end of the shift",
            "Saving the remainder of the vial for the next patient with the same diagnosis",
            "Disposal in the regular trash with a note listing the amount that was wasted",
        ],
        "Controlled substance waste is destroyed with a witness present and recorded in the controlled substance log, which keeps the chain of custody intact. Pouring it away unobserved, saving the remainder for another patient, and discarding it in the regular trash with a note all break the documentation the DEA expects.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-036
    fact(
        "skill-med-safety",
        "How should staff resolve a pharmacy label that differs from the electronic order?",
        "Contact the pharmacist or prescriber before administration",
        [
            "Give the lower strength and note the difference in the chart",
            "Give both strengths so the patient reaches the ordered dose",
            "Remove the label and give the product as it was dispensed",
        ],
        "A label that disagrees with the electronic order is an unresolved discrepancy, so the pharmacist or prescriber settles the intended drug and strength before the dose is given. Choosing the lower strength, giving both strengths, and removing the label to avoid confusion all pick a dose without resolving what was ordered.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-037
    fact(
        "skill-med-safety",
        "How are high-alert medications stored to reduce selection errors in clinic?",
        "Locked away, separated from other products, and clearly marked",
        [
            "Locked away, kept with the routine oral medications on the shelf",
            "Left on open shelves, separated from other products and clearly marked",
            "Left on open shelves, kept with the routine oral medications",
        ],
        "High-alert products are locked, physically separated from other medications, and marked so staff recognize them at the shelf. Keeping them among routine medications or leaving them on open shelves removes the barriers that keep a distracted selection from becoming a wrong pick.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-038
    fact(
        "skill-med-safety",
        "What does the medication administration record need to document?",
        "Drug, dose, route, time, site if relevant, and patient response",
        [
            "Time of the entry, initials of the staff member, and the room number",
            "The prescription copy, the pharmacy label, and the refill date",
            "The patient's questions, the education given, and the follow-up plan",
        ],
        "The medication administration record documents what was given, so it carries the drug, dose, route, time, site when it matters, and the response when it was observed. Initials, room numbers, prescription copies, and education notes support other parts of the chart and do not show what was administered.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-039
    fact(
        "skill-med-safety",
        "What must staff do when using an automated dispensing cabinet override for emergencies?",
        "Document the reason for the override and reconcile the inventory afterward",
        [
            "Document the override reason and close the drawer at month end",
            "Reconcile the inventory later and leave the reason to the supervisor",
            "Document the reason for the override and dispense from the personal supply",
        ],
        "Overrides exist for genuine emergencies, so each use is documented with a reason and the cabinet inventory is reconciled so the audit trail matches what was removed. Closing the drawer monthly, leaving the reason for a supervisor, and dispensing from personal supply all defeat the accountability the override record is meant to provide.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-040
    fact(
        "skill-med-safety",
        "Under what conditions should tablets be split for administration?",
        "When a reliable reference confirms the product is scored and splittable",
        [
            "When the tablet shows a score line regardless of the product's release type",
            "When the medication is not controlled and the tablet appears scored",
            "When the patient requests a half dose and the tablet can be broken",
        ],
        "A tablet is split only after a reliable reference confirms that the specific product is scored and safe to split, because products that look alike can differ in their formulation. A score line alone, a non-controlled status, and a patient request do not establish that splitting the product is safe.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-041
    fact(
        "skill-med-safety",
        "Which topics belong in a medication safety huddle at the start of the clinic day?",
        "High-risk patients, look-alike products, and staffing for double checks",
        [
            "Routine patients, look-alike products, and staffing for double checks",
            "High-risk patients, common products, and staffing for double checks",
            "High-risk patients, look-alike products, and staffing coverage for new staff",
        ],
        "A short huddle at the start of the day aligns the team on the patients at highest risk, the products that look alike on the shelves, and who is available to perform double checks. Discussing routine patients, common products, and new staff does not focus attention on the day's error risks.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-042
    fact(
        "skill-med-safety",
        "What problems can returning unopened patient-specific medications to stock without approval cause?",
        "Wrong-patient labeling and loss of the original storage record",
        [
            "Duplicate billing for the medication and an inflated refill count",
            "A shorter shelf life claim and a denied manufacturer rebate",
            "An increased cost of the medication and a slower refill cycle",
        ],
        "A medication released to a patient has left clinic control, so returning it to stock means accepting unknown storage history and a label that may no longer match its contents. Billing, rebate, and cost issues are financial consequences and do not describe the safety risk of reusing a dispensed product.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
]
