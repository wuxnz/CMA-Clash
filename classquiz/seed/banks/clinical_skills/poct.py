# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-poct)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [

    # skill-poct-001
    fact(
        "skill-poct",
        "Which requirement still applies to a site that performs CLIA-waived point-of-care testing?",
        "Run internal quality control and keep operator competency records",
        [
            "Employ a laboratory director to oversee every waived test on the menu",
            "Enroll every waived assay in a federally required proficiency program",
            "Validate each waived assay on the site's own analyzer before use",
        ],
        "Waived status does not remove quality control, recordkeeping, or competency expectations at the testing site. Employing a laboratory director and federal proficiency enrollment belong to higher complexity testing, and site validation is not required for assays the FDA has already cleared as waived.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-002
    fact(
        "skill-poct",
        "Which testing is authorized under a CLIA Certificate of Waiver?",
        "Waived complexity tests performed with the cleared instructions",
        [
            "Moderate complexity tests run by staff with the required training",
            "High complexity tests supervised by a qualified testing director",
            "Waived complexity tests run on an analyzer the clinic owns",
        ],
        "A Certificate of Waiver covers waived complexity assays performed exactly as the manufacturer cleared them, including the device and the instructions for use. Moderate and high complexity testing requires a certificate of compliance or accreditation, and the waiver does not extend to other analyzers.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-003
    fact(
        "skill-poct",
        "What does liquid control solution check during glucose meter quality control?",
        "Whether the meter and strips read near known glucose concentrations",
        [
            "Whether the patient followed the fasting instructions before the visit",
            "Whether the strip lot was stored within its labeled temperature range",
            "Whether the operator completed competency for the meter that morning",
        ],
        "Liquid control solution carries a known glucose value, so a passing control confirms the meter and strips are reading within the expected range. A patient's diet and fasting status affect the result itself, while storage temperature and competency records are verified elsewhere in the quality system.",
        [S.FDA_CLIA_WAIVED, S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-004
    fact(
        "skill-poct",
        "When is glucose meter quality control required?",
        "On each scheduled day, with each new strip lot, and after a drop",
        [
            "Before every patient result, with each new strip lot, and after a drop",
            "Once a year, with each new strip lot, and after the meter is dropped",
            "On each scheduled day, with each new strip lot, and after the meter is cleaned",
        ],
        "Manufacturer instructions call for control runs on the scheduled days, whenever a new strip lot is opened, and after the meter is dropped or otherwise damaged. Routine cleaning between patients does not change calibration, and controls are scheduled rather than repeated before every patient result or run once a year.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-005
    fact(
        "skill-poct",
        "Why should finger sites for capillary glucose testing be rotated between tests?",
        "To limit calluses, pain, and thickened skin that skew readings",
        [
            "To reduce the risk of bloodborne pathogen exposure between patients",
            "To make sure each finger is used an equal number of times",
            "To keep puncture sites away from the nail beds and cuticles",
        ],
        "Repeated puncture of one site produces calluses and thick skin, which hurts more and can alter capillary glucose values, so sites are rotated. A single-use lancet already prevents exposure between patients, equal use of each finger is not the goal, and avoiding the nail bed is a collection technique step rather than the reason for rotation.",
        [S.NHA_CCMA, S.CDC_DIABETES_BASICS],
        "beginner",
    ),
    # skill-poct-006
    fact(
        "skill-poct",
        "How should the pharynx be swabbed before a waived rapid strep antigen test?",
        "Swab the tonsillar pillars and posterior pharynx, avoiding the tongue",
        [
            "Swab the buccal mucosa and tongue surface, avoiding the tonsillar area",
            "Swab the anterior nasal passage and the roof of the mouth",
            "Swab the soft palate and uvula, avoiding the tonsillar area",
        ],
        "Group A streptococcus colonizes the tonsils and posterior pharynx, so the swab targets those surfaces and avoids the tongue and the mouth. Buccal mucosa, the tongue, nasal passages, and the soft palate are not the reservoir for this organism, and sampling them lowers the chance of a true positive.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-poct-007
    fact(
        "skill-poct",
        "What substance do urine pregnancy point-of-care immunoassays detect?",
        "Human chorionic gonadotropin in the urine specimen",
        [
            "Human chorionic gonadotropin in the blood specimen",
            "Estriol hormone in the urine specimen",
            "Progesterone hormone in the urine specimen",
        ],
        "These are qualitative immunoassays that detect human chorionic gonadotropin in urine, the hormone produced by the placenta after implantation. Estriol and progesterone are not the target analyte, and a blood specimen would need a different testing method than this urine immunoassay.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-008
    fact(
        "skill-poct",
        "Which details must be recorded for a waived test result?",
        "Patient identifiers, test, result, date and time, operator, and reagent lot",
        [
            "Patient identifiers, result, date and time, and the reagent lot on file",
            "Test name, result, date and time, operator, and the reagent lot control number",
            "Patient identifiers, test, result, date and time, and the clinic room number",
        ],
        "CLIA expects the waived test record to identify the patient, the test, the result with its date and time, the operator, and the reagent lot numbers. A record missing the operator or the patient identifiers makes it impossible to show who tested whom, and a room number is not part of the required record set.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-009
    fact(
        "skill-poct",
        "Why should a blood glucose meter be cleaned and disinfected between patients?",
        "To reduce cross-contamination from blood on device surfaces",
        [
            "To keep the meter's calibration from drifting between uses",
            "To keep previous patient results from being misread on screen",
            "To keep the strip port clear of dried blood and lint",
        ],
        "Blood from one patient can remain on a shared meter's surface, so cleaning and disinfecting between patients prevents cross-contamination and transmission. Calibration is checked with control solution, screen readability is not an infection control reason, and clearing the strip port supports device function rather than patient safety.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-010
    fact(
        "skill-poct",
        "What is the appropriate response when a waived test control is out of range?",
        "Repeat the control, find the cause, and hold patient testing until it passes",
        [
            "Report the patient results and record the control failure in the progress note",
            "Recalibrate the meter and release the results without rerunning the control",
            "Hold patient testing until the next scheduled control run that day",
        ],
        "A failed control means results from that device cannot be trusted, so the control is repeated, the cause is found, and patient testing waits until the device passes. Releasing results with the failure documented still exposes patients to unreliable values, recalibrating without a passing control proves nothing, and waiting for the next scheduled run leaves the problem in place.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-011
    fact(
        "skill-poct",
        "What do most point-of-care hemoglobin A1c analyzers require for valid testing?",
        "Whole blood specimens and control runs on the analyzer schedule",
        [
            "Serum specimens and control runs on the analyzer's stated schedule",
            "Whole blood specimens and control runs once each calendar month",
            "Serum specimens and control runs once each calendar month",
        ],
        "Most point-of-care A1c analyzers are validated for capillary or venous whole blood, and the manufacturer sets how often control material is run. Serum and plasma are not the validated matrices for these devices, and monthly control runs would leave every result between runs unverified.",
        [S.FDA_CLIA_WAIVED, S.ADA_STANDARDS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-012
    fact(
        "skill-poct",
        "What is essential for accurate bedside fingerstick INR testing?",
        "Correct sample volume and control testing on the device schedule",
        [
            "Correct sample volume and a control run at the start of each shift",
            "A finger hematoma sample and control testing on the device schedule",
            "An unvalidated serum sample and control testing on the device schedule",
        ],
        "Bedside INR devices need the exact sample volume the instructions specify and control material run on the manufacturer's schedule before results are reported. Controls run at the start of a shift leave gaps between runs, hematoma blood is not a valid sample, and serum has not been validated for these capillary devices.",
        [S.FDA_CLIA_WAIVED, S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-013
    fact(
        "skill-poct",
        "Which collection condition gives a rapid influenza antigen test the best chance of detecting virus?",
        "Early in the illness, when the patient is shedding the most virus",
        [
            "Late in the illness, when the patient is shedding the least virus",
            "After the patient has started antiviral medication for the flu",
            "After the patient has eaten or had a drink before the swab",
        ],
        "Rapid influenza antigen detection depends on how much virus is present, and shedding peaks during the first days of symptoms, so early collection with correct swab technique works best. Shedding falls later in the illness, antiviral medication reduces it further, and food or drink before a throat swab can also cut the yield.",
        [S.FDA_CLIA_WAIVED, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-poct-014
    fact(
        "skill-poct",
        "How is operator competency for a waived assay maintained over time?",
        "Documented training, observed performance checks, and periodic reassessment",
        [
            "Documented training with observed performance checks at the end of each shift",
            "Documented training with a written examination and periodic reassessment",
            "Documented training with a written examination at the end of each shift",
        ],
        "CLIA treats competency as an ongoing duty, so operators are trained and documented, observed while they run the test, and reassessed on a schedule. A written examination alone does not show that the operator still performs the test correctly, and a sign-off after a single shift cannot support ongoing competency.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-015
    fact(
        "skill-poct",
        "How should a clinic screening thermometer be prepared for the next patient?",
        "Cleaned and disinfected, with the probe cover replaced before reuse",
        [
            "Wiped with a dry paper towel, with the probe cover replaced before reuse",
            "Cleaned and disinfected, with the probe cover rinsed and put back on",
            "Wiped with a dry paper towel, with the probe cover rinsed and put back on",
        ],
        "A reusable probe carries organisms from one patient to the next, so it is cleaned and disinfected between patients and the single-use cover is replaced. A dry paper towel leaves contamination on the probe, and a rinsed cover that goes back on the device can carry organisms to the next patient.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-016
    fact(
        "skill-poct",
        "Which conditions commonly cause falsely low or unstable pulse oximetry readings?",
        "Poor perfusion, nail polish on the probe site, and patient motion",
        [
            "Strong perfusion, nail polish on the probe site, and patient motion",
            "Poor perfusion, clean nail beds on the probe site, and patient motion",
            "Poor perfusion, nail polish on the probe site, and steady breathing",
        ],
        "The oximeter depends on steady blood flow and on light passing through the finger, so vasoconstriction, nail polish, and movement all distort the reading. Strong perfusion and clean nail beds support an accurate result, and steady breathing does not change the signal reaching the probe.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-017
    fact(
        "skill-poct",
        "What is the main purpose of external quality assessment for waived testing?",
        "Blinded proficiency samples graded against peer laboratories",
        [
            "Scheduled on-site inspections of the testing area and the records",
            "Review of operator training files by the accrediting agency",
            "Repeat testing of the same patient specimen to measure repeatability",
        ],
        "External quality assessment sends samples with unknown expected values so results are graded against other laboratories, which shows the assay is accurate beyond this clinic. On-site inspections and training file reviews are survey activities, and repeating the same specimen measures repeatability rather than proficiency.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-018
    fact(
        "skill-poct",
        "What should be confirmed before a waived point-of-care lipid panel is collected?",
        "The fasting status on the order and the specimen type the device accepts",
        [
            "The fasting status on the order and the specimen type the operator prefers",
            "The fasting status on the order and the time of day the panel is run",
            "The fasting status on the order and the patient's insurance for the panel",
        ],
        "Lipid results are interpreted against fasting status, especially triglycerides, and the analyzer has to receive the specimen type it was validated for. Operator preference and time of day do not change the result, and insurance coverage has no bearing on pre-collection preparation.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-019
    fact(
        "skill-poct",
        "When does the positive predictive value of a rapid strep antigen test fall?",
        "When group A strep prevalence in the tested population is low",
        [
            "When group A strep prevalence in the tested population is high",
            "When the operator has completed training for the strep assay",
            "When control material passes before the first patient test",
        ],
        "Predictive value depends on prevalence, so when strep is uncommon a larger share of positive screens is a false positive. High prevalence raises predictive value instead, while operator training and a passing control affect the accuracy of each run rather than the predictive value of the result.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-020
    fact(
        "skill-poct",
        "What must be controlled during a capillary hematocrit centrifugation procedure?",
        "Rotor speed and spin time for a reliable packed cell volume",
        [
            "Rotor speed and spin time for a reliable platelet estimate",
            "Rotor speed and spin time for a reliable white blood cell count",
            "Rotor speed and spin time for a reliable plasma volume estimate",
        ],
        "The capillary microhematocrit method packs the red cells and reads the height of that column as the packed cell volume, so rotor speed and spin time have to be controlled. Platelet estimates, white cell counts, and plasma volume come from other methods and are not what this separation measures.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-021
    fact(
        "skill-poct",
        "How should waived test kits be stored when room temperature is required?",
        "Within the labeled range, in a closed cabinet away from light",
        [
            "Within the labeled range, in a refrigerated cabinet in the supply room",
            "Within the labeled range, in an open bin near the exam room window",
            "Within the labeled range, in a bin under the reagent sink",
        ],
        "Reagents lose performance outside the temperature range printed on the carton, and light or moisture adds to that damage. Refrigeration when the label calls for room temperature can also stress the kit, so the labeled range and a protected, dry location both matter.",
        [S.FDA_CLIA_WAIVED, S.CDC_VACCINE_STORAGE],
        "intermediate",
    ),
    # skill-poct-022
    fact(
        "skill-poct",
        "Why must urinalysis dipstick pads be read within the stated time window?",
        "Pad color continues to develop past the limit, so a late read can be wrong",
        [
            "The specimen's cells break down past the limit, so a late read can be wrong",
            "The reagent strip loses strength past the limit, so a late read can be wrong",
            "The control material expires past the limit, so a late read can be wrong",
        ],
        "Each pad carries a stated read time because the color reaction keeps going after that window, so a late read can report a value the specimen does not support. Cell breakdown belongs to urine microscopy, and reagent strength and control expiry are shelf life issues rather than read timing.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-023
    fact(
        "skill-poct",
        "Which records may a CLIA survey request at a waived testing site?",
        "Test menu, control logs, operator training, and competency records",
        [
            "Test menu, control logs, billing claims, and competency records",
            "Test menu, control logs, operator training, and facility licenses",
            "Test menu, supplier invoices, operator training, and competency records",
        ],
        "A CLIA survey at a waived site reviews the test menu, the quality control records, operator training, and competency documentation for the testing performed. Billing claims, supplier invoices, and facility licensing are handled by other offices and are outside the surveyor's review.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-024
    fact(
        "skill-poct",
        "After blood splashes on a point-of-care analyzer, what must happen before the next patient test?",
        "The device is cleaned and disinfected for the stated contact time",
        [
            "The device is cleaned with a damp cloth and left un-disinfected",
            "The device is disinfected with a quick wipe and used again right away",
            "The device is returned to service once the visible blood has dried",
        ],
        "Blood on a shared analyzer can transfer organisms to the next patient, so the device is cleaned and disinfected with the product and contact time the instructions specify. A damp cloth without disinfection leaves organisms behind, a quick wipe may not reach the required dwell time, and blood that has merely dried is still contamination.",
        [S.CDC_STANDARD_PRECAUTIONS, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-025
    fact(
        "skill-poct",
        "Which steps belong in capillary glucose collection under common clinic policy?",
        "Hand hygiene, a single-use lancet, and wiping away the first drop of blood",
        [
            "Hand hygiene, a reusable lancing device, and wiping away the first drop",
            "Hand hygiene, a single-use lancet, and milking the finger to produce the drop",
            "Hand hygiene, a reusable lancing device, and milking the finger",
        ],
        "Capillary glucose collection starts with hand hygiene and a single-use lancet, and the first drop of blood is wiped away because it carries interstitial fluid that dilutes the sample. A reusable lancing device carries blood between patients, and milking the finger mixes tissue fluid into the drop and distorts the result.",
        [S.CDC_DIABETES_BASICS, S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-026
    fact(
        "skill-poct",
        "Which elements must a waived rapid HIV screening program provide?",
        "Pre-test and post-test counseling with confirmatory testing arranged",
        [
            "Pre-test counseling and confirmatory testing arranged for reactive screens",
            "Post-test counseling and confirmatory testing arranged for reactive screens",
            "Pre-test and post-test counseling with confirmatory testing left to the patient",
        ],
        "A rapid HIV screening program includes counseling before the test, counseling once the result is known, and an arrangement for confirmatory testing when the screen is reactive. Counseling at one point alone leaves part of the required counseling out, and leaving confirmatory testing to the patient breaks the referral pathway.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-027
    fact(
        "skill-poct",
        "Why should controls be run on both the current and the new glucose strip lot?",
        "To detect a bias in the new lot before it is used for patient samples",
        [
            "To verify that the new lot was shipped at the temperature on the carton",
            "To confirm that both lots expire on the same calendar date",
            "To check the new lot for visible damage to the strip packaging",
        ],
        "Running control material on the old and new lots side by side shows whether the new reagent reads the same known value, so a lot-specific bias is caught before any patient result is reported. Shipping temperature, expiration dates, and package condition are receiving checks that are handled apart from the control comparison.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-028
    fact(
        "skill-poct",
        "In which situations are urine pregnancy point-of-care false negatives more likely?",
        "Very early pregnancy or a very dilute urine specimen",
        [
            "Very early pregnancy or a very concentrated urine specimen",
            "Late in pregnancy with a very dilute urine specimen",
            "Mid pregnancy with a very concentrated urine specimen",
        ],
        "These kits detect hCG, and its concentration is lowest just after implantation, while very dilute urine pushes the level below the detection limit of the test. Concentrated urine raises the detectable concentration, and later pregnancy carries far higher hCG levels, so neither raises the false negative rate.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-029
    fact(
        "skill-poct",
        "Which metrics best support quality improvement for point-of-care testing?",
        "Control failure rates, competency renewal dates, and labeling error counts",
        [
            "Patient visit volume, control failure rates, and supply cost per month",
            "Competency renewal dates, labeling error counts, and average waiting room times",
            "Patient visit volume, supply cost per month, and waiting room times",
        ],
        "Improvement work needs measures tied to the analytic and preanalytic steps of testing, so control failures, competency records, and labeling errors are the useful indicators. Visit volume, supply cost, and waiting room times describe clinic operations rather than testing performance, and a set built from those does not show where testing breaks down.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-030
    fact(
        "skill-poct",
        "How should waived test cartridges be handled when shipped between clinic sites?",
        "Shipped within the labeled temperature range with lot numbers documented",
        [
            "Shipped within the labeled temperature range with the cartons left unlabeled",
            "Shipped at ambient temperature with the lot numbers documented",
            "Shipped at ambient temperature with the cartons left unlabeled",
        ],
        "Transport has to protect reagent performance and keep the shipment traceable, so the labeled temperature range is maintained and lot numbers stay with the cartons. An unlabeled carton cannot be traced if a recall happens, and shipping without temperature protection risks degrading the reagent.",
        [S.FDA_CLIA_WAIVED, S.CDC_VACCINE_STORAGE],
        "intermediate",
    ),
    # skill-poct-031
    fact(
        "skill-poct",
        "How should capillary blood be applied to a waived hemoglobin cuvette or strip?",
        "Filled exactly to the fill line with no air bubble in the chamber",
        [
            "Filled past the fill line with no air bubble in the chamber",
            "Filled exactly to the fill line with a trapped air pocket in the chamber",
            "Filled past the fill line with a trapped air pocket in the chamber",
        ],
        "The cuvette or strip measures a fixed amount of blood, so the drop reaches the fill line exactly and no air bubble sits in the chamber, since underfilling and bubbles both produce an incorrect hemoglobin value. Filling past the line and leaving a bubble in the chamber each change the amount the device reads.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-032
    fact(
        "skill-poct",
        "What should a medical assistant do when a point-of-care result conflicts with the clinical picture?",
        "Notify the provider and repeat the test or send it for confirmation",
        [
            "Report the result that matches the clinical picture and discard the other",
            "Repeat the test at the end of the shift and keep the result on file",
            "Hold the result until the next scheduled quality control run",
        ],
        "A value that does not fit the exam may come from a preanalytic or analytic problem, so the provider is told and the result is repeated or confirmed by another method. Choosing the value that fits the picture hides the discrepancy, and waiting until the end of the shift or until the next control run delays the correction.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-033
    fact(
        "skill-poct",
        "Which testing requires a laboratory director under CLIA?",
        "Moderate and high complexity testing under a certificate of compliance",
        [
            "Waived complexity testing under a certificate of waiver at the testing site",
            "Moderate complexity testing under a certificate of waiver at the testing site",
            "High complexity testing under a certificate of waiver at the testing site",
        ],
        "CLIA assigns a laboratory director to moderate and high complexity testing, which runs under a certificate of compliance or accreditation. Waived complexity assays do not require a director, and moderate or high complexity testing cannot be offered under a certificate of waiver at all.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-034
    fact(
        "skill-poct",
        "When should external control materials packaged with a strep antigen kit be run?",
        "On the manufacturer's schedule and each time a new shipment is opened",
        [
            "Each time a shipment arrives and each time a lot reaches its expiration date",
            "Each time a lot expires and after each patient result is reported",
            "Once each year when the laboratory submits proficiency samples",
        ],
        "External control material checks that the shipped reagents perform as expected, so it runs on the manufacturer's schedule and whenever a new shipment or lot is opened. Waiting for a lot to expire, testing after every patient result, and tying controls to annual proficiency samples all leave gaps in verification.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-035
    fact(
        "skill-poct",
        "Which patient factors may alter fingerstick INR point-of-care results?",
        "Anemia and anticoagulant levels that change the clotting response",
        [
            "Anemia and the choice of finger used for the capillary puncture",
            "Room humidity and anticoagulant levels that change the clotting response",
            "Room humidity and the choice of finger used for the puncture",
        ],
        "Some bedside INR devices are sensitive to hematocrit and to the effect of anticoagulants on clotting, so anemia and drug levels can shift the result. Room humidity does not affect the assay, and the finger chosen for the puncture does not change the clotting measurement.",
        [S.FDA_CLIA_WAIVED, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-poct-036
    fact(
        "skill-poct",
        "Where should current waived test instructions be available to operators?",
        "At the testing station, updated when the manufacturer revises them",
        [
            "In the office policy manual, updated at the annual compliance review",
            "In the quality control binder, filed with the monthly control records",
            "In the training folder, kept after the first competency sign-off",
        ],
        "Operators need the instructions for use at the point of testing so they can work through a failed control or an unexpected flag, and the copy is replaced when the manufacturer revises it. An annual policy review, a filing in the control binder, and a copy kept from initial training each leave the bench without a current procedure.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-037
    fact(
        "skill-poct",
        "When must capillary tubes or cartridges be labeled during bedside collection?",
        "Before leaving the bedside, using two patient identifiers",
        [
            "Before leaving the bedside, using the patient's room number",
            "After the specimen reaches the laboratory, using two identifiers",
            "Before leaving the bedside, using initials for a rushed draw",
        ],
        "Labeling at the bedside with two identifiers confirms that the specimen belongs to the patient in front of you before it leaves your hands, which prevents mislabeled specimens. A room number is not a patient identifier, labeling after the specimen reaches the laboratory delays the check, and initials can match more than one patient.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-038
    fact(
        "skill-poct",
        "What trends might routine review of point-of-care incident logs reveal?",
        "Control failures, training gaps, and specimen handling errors",
        [
            "Repeated control failures, scheduling delays, and patient complaints",
            "Equipment purchases, staffing turnover, and recurring supply shortages",
            "Supply shortages, patient complaints, and purchases of new equipment",
        ],
        "Incident logs are reviewed for patterns that point to defects in the testing process, so recurring control failures, missing training, and specimen handling errors stand out. Scheduling delays, patient complaints, equipment purchases, and supply shortages are clinic operations issues rather than measures of testing quality.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-039
    fact(
        "skill-poct",
        "Why is careful finger site preparation important before capillary lead screening?",
        "Lead on the skin surface can falsely elevate the capillary result",
        [
            "Lead on the skin surface can falsely lower the capillary result",
            "Alcohol on the skin can falsely elevate the capillary result",
            "Insufficient cleaning of the site can falsely lower the capillary result",
        ],
        "Environmental lead dust on unwashed fingers contaminates the sample and raises the measured value, so the skin is washed and cleaned before the puncture. Skin contamination does not lower the value, alcohol does not add lead to the blood, and cleaning that is too little would raise the result rather than lower it.",
        [S.FDA_CLIA_WAIVED, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-poct-040
    fact(
        "skill-poct",
        "Which elements let a clinic keep point-of-care testing running during a power outage?",
        "Battery-backed meters and documented manual workflows for urgent testing",
        [
            "Spare reagent stock and a written schedule for reordering reagent supplies",
            "A written schedule for notifying patients of delayed test results",
            "A written schedule for rescheduling postponed patient appointments",
        ],
        "Continuity planning keeps essential point-of-care results coming during a long outage, which means having battery powered meters ready and written manual workflows for the priority tests. Reordering supplies, notifying patients of delayed results, and rescheduling appointments describe how the clinic handles the backlog, and none of them keeps a test running while the power is out.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-041
    fact(
        "skill-poct",
        "How should waived test results be relayed to the patient in clinic?",
        "Relay results privately after the provider reviews and charts them",
        [
            "Relay results privately before the provider reviews and charts the value",
            "Post results to the patient portal without provider sign-off",
            "Give the printed result to a family member waiting at the front desk",
        ],
        "A waived result is relayed privately once the provider has reviewed and documented it. Relaying before provider review, posting unreviewed results to the portal, and handing a printed result to someone else each break standard workflow and privacy safeguards.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-042
    fact(
        "skill-poct",
        "What should staff do before patient testing with a newly opened waived kit lot?",
        "Run the required control materials and document the pass or fail outcome",
        [
            "Run the required control materials and file the results with the inventory",
            "Check the expiration date and begin patient testing that morning",
            "Check the expiration date and document it in the supply inventory",
        ],
        "Opening a new lot means the shipment and the reagents have not been verified, so control material runs first and the pass or fail result is written down before any patient sample is tested. Checking an expiration date alone does not verify the reagents, and filing control results with the inventory keeps them out of the quality record.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
]
