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
        "What must a site still do when performing CLIA-waived point-of-care tests?",
        "Follow manufacturer IFU and the facility quality control schedule",
        [
            "Run any waived assay without documented operator training on file",
            "Omit control materials when the clinic day schedule is inconvenient",
            "Reuse the same lancet on unrelated patients during the same clinic session",
        ],
        "Waived status does not remove QC or competency rules. Reusing lancets risks bloodborne pathogen transmission, and busy days do not excuse skipped controls.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-002
    fact(
        "skill-poct",
        "Under a CLIA Certificate of Waiver, which tests may be performed when staff follow cleared instructions?",
        "Tests classified as waived complexity for that certificate",
        [
            "Moderate-complexity cultures without a laboratory director",
            "Any laboratory method the clinic adds to the menu",
            "High-complexity molecular assays without validation",
        ],
        "The certificate type limits which assays are allowed. Moderate and high complexity require different CLIA certificates and personnel, not a waiver alone.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-003
    fact(
        "skill-poct",
        "What does liquid control solution check during glucose meter quality control?",
        "Whether the meter and strips read near known glucose concentrations",
        [
            "Whether the patient followed a fasting order that morning at home",
            "Whether insurance will cover the current office visit for the encounter",
            "Whether the lancet gauge matches the facility supply list for that room",
        ],
        "Control solution validates the analytic system, not billing or diet history. A passing control shows the strip lot and meter are performing within expected ranges.",
        [S.FDA_CLIA_WAIVED, S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-004
    fact(
        "skill-poct",
        "When do manufacturer instructions typically require glucose meter quality control?",
        "On scheduled days, with each new strip lot, and after the meter is dropped",
        [
            "Once at initial device setup and then not again unless the screen prompts",
            "After every patient sample without using liquid control fluid on the meter",
            "When the low-battery icon first appears on the display during patient testing",
        ],
        "Event-based QC catches trauma to the device, and lot changes catch reagent shifts. Patient testing alone does not verify that the meter still reads accurately.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-005
    fact(
        "skill-poct",
        "Why should finger sites for capillary glucose be rotated over time?",
        "To limit calluses, pain, and thickened skin that skew readings",
        [
            "To remove hand hygiene requirements before lancing the skin at the bedside",
            "To avoid charting glucose results in the medical record after each test",
            "To replace meter calibration checks with finger site changes alone",
        ],
        "Thickened fingertips can hurt patients and alter capillary glucose values. Rotation preserves skin integrity; it does not replace hygiene, documentation, or QC.",
        [S.NHA_CCMA, S.CDC_DIABETES_BASICS],
        "beginner",
    ),
    # skill-poct-006
    fact(
        "skill-poct",
        "How should the pharynx be swabbed before a waived rapid strep antigen test?",
        "Swab tonsillar pillars and posterior pharynx, avoiding tongue and teeth",
        [
            "On buccal mucosa inside the cheek without contacting tonsillar tissue",
            "Right after eating when food debris still coats the throat and tonsils",
            "With one swab used for two patients in the same room to conserve supplies",
        ],
        "Adequate tonsillar and posterior pharynx sampling reduces false negatives. Cheek swabs miss the usual reservoir, and shared swabs break infection control.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-poct-007
    fact(
        "skill-poct",
        "What substance do urine pregnancy point-of-care immunoassays detect?",
        "Human chorionic gonadotropin in urine within the kit read window",
        [
            "ABO antigens on red blood cell membranes in a typing assay",
            "Serum potassium on a chemistry analyzer channel in the core lab",
            "Bacterial colonies after overnight culture incubation on agar plates",
        ],
        "These kits are qualitative hCG screens in urine, not blood typing or culture. Wrong specimen type or read time produces invalid or misleading lines.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-008
    fact(
        "skill-poct",
        "Which details should be recorded when documenting a waived test result?",
        "Patient ID, test name, result, time, operator, and lot numbers when required",
        [
            "A result label with no patient name attached to the specimen container",
            "The operator's computer login password documented in the medical chart",
            "A normal waived test result with collection time left blank in the progress note",
        ],
        "Complete records support care and inspection. Anonymous labels invite wrong-chart entries, and blank times make trending and callbacks unreliable.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-009
    fact(
        "skill-poct",
        "Why should a blood glucose meter be cleaned between patients?",
        "To reduce cross-contamination from blood on device surfaces",
        [
            "To reset the internal calibration clock on the meter after each patient",
            "To update insurance copay amounts for the visit at the front desk",
            "To extend strip expiration beyond the printed date on the vial box",
        ],
        "Blood contact on shared surfaces can spread pathogens. Calibration and billing are separate from disinfecting the meter per the instructions for use.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-010
    fact(
        "skill-poct",
        "What is the appropriate response when a waived test control is out of range?",
        "Repeat QC, troubleshoot per IFU, and hold patient tests until resolved",
        [
            "Report patient results now and note the QC issue in the chart later",
            "Change control solution brands mid-shift without logging the lot change",
            "Delete the failed QC entry so daily logs show all passes for the shift",
        ],
        "Failed controls mean patient results may be unreliable. Reporting anyway risks clinical harm; altering logs hides the problem instead of fixing the device.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-011
    fact(
        "skill-poct",
        "What do most point-of-care hemoglobin A1c analyzers require for valid testing?",
        "Whole blood specimens and QC runs listed in the instructions",
        [
            "Saliva collected from the buccal mucosa as the primary sample type",
            "Cerebrospinal fluid obtained by lumbar puncture for each bedside test",
            "Waived operation with no training records on file for point-of-care staff",
        ],
        "Devices are validated for specific matrices, usually capillary or venous whole blood. Saliva and CSF are wrong specimen types, and waived status still requires trained staff.",
        [S.FDA_CLIA_WAIVED, S.ADA_STANDARDS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-012
    fact(
        "skill-poct",
        "What is essential for accurate bedside fingerstick INR testing?",
        "Correct sample volume and control testing on the IFU schedule",
        [
            "Serum from a gold-top tube run on the device without validation",
            "A shared lancing device wiped lightly between unrelated patients",
            "Blood pooled in a finger hematoma used as the primary sample source",
        ],
        "INR devices expect a defined capillary volume and periodic controls. Unvalidated serum, reused lancets, and hematoma blood all threaten accuracy and safety.",
        [S.FDA_CLIA_WAIVED, S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-013
    fact(
        "skill-poct",
        "When is influenza rapid antigen testing most likely to detect virus?",
        "When specimens are collected early in illness with proper swab technique",
        [
            "When patients are tested weeks after respiratory symptoms have resolved",
            "When swabs are stored in a hot vehicle for several days before testing",
            "When labels are applied after results are called to patients without IDs",
        ],
        "Viral shedding drops as illness progresses, lowering sensitivity. Heat-degraded swabs and missing identifiers add separate preanalytic risks.",
        [S.FDA_CLIA_WAIVED, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-poct-014
    fact(
        "skill-poct",
        "How should operator competency for point-of-care testing be maintained?",
        "Documented after training, observed checks, and periodic reassessment",
        [
            "Assumed from hire date without watching actual test performance at the bench",
            "Completed once per waived test menu item and not reviewed again that year",
            "Accepted from a coworker's verbal report without written competency records",
        ],
        "CLIA quality systems expect evidence that staff can run tests correctly. Hire date and casual sign-off do not prove current skill on each waived assay.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-015
    fact(
        "skill-poct",
        "How should thermometers used for clinic screening be handled between patients?",
        "Checked or calibrated per policy and cleaned between uses",
        [
            "Used orally without probe covers when covers run out",
            "Aimed at the forearm to estimate core temperature",
            "Stored in a personal bag between shifts without disinfecting",
        ],
        "Probe covers and disinfecting reduce cross-infection. Forearm skin temperature is not a reliable substitute for the site's validated measurement method.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-016
    fact(
        "skill-poct",
        "Which conditions commonly cause falsely low or unstable pulse oximetry readings?",
        "Poor perfusion, nail polish on the probe site, and patient motion",
        [
            "Mild anemia with a well-seated probe on warm skin at the fingertip",
            "Room humidity within typical indoor clinic ranges during winter heating",
            "Using the index finger instead of the middle finger on the same hand",
        ],
        "The plethysmograph needs steady perfusion and light transmission. Finger choice matters less than cold, vasoconstricted, or moving digits and opaque polish.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-017
    fact(
        "skill-poct",
        "What is the main purpose of external quality assessment for waived testing?",
        "Blinded proficiency samples graded against peer laboratories",
        [
            "A full substitute for daily internal QC runs on each waived device in clinic",
            "Removal of operator training requirements after one passing survey year",
            "Reagents purchased without lot traceability labels or shipment documentation",
        ],
        "Proficiency testing benchmarks performance on unknown samples. It complements, not replaces, routine controls and documented training.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-018
    fact(
        "skill-poct",
        "What pre-collection requirement may apply to a waived point-of-care lipid panel?",
        "Fasting status per order and a specimen type validated for the device",
        [
            "A high-fat meal immediately before capillary collection at the bedside",
            "Routine heel sticks on every adult patient regardless of site policy",
            "Unlabeled collection tubes to shorten time at the patient collection area",
        ],
        "Postprandial triglycerides can rise and alter panel interpretation. Heel sticks and unlabeled specimens are wrong for typical adult capillary or venous protocols.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-019
    fact(
        "skill-poct",
        "When does the positive predictive value of a rapid strep antigen test fall?",
        "When group A strep prevalence in the tested population is low",
        [
            "When prevalence rises during a local outbreak season in the community",
            "When swab collection follows the kit instructions on every patient",
            "When daily internal controls show expected line intensity before testing",
        ],
        "In low prevalence settings, more positive screens are false positives even with good technique. High prevalence and passing controls do not create that Bayesian problem.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-020
    fact(
        "skill-poct",
        "What must be controlled during a capillary hematocrit centrifugation procedure?",
        "Rotor speed and spin time per the written laboratory protocol",
        [
            "An open centrifuge lid to watch cells separate during the run",
            "Cracked capillary tubes if the blood column looks full enough",
            "Hemolyzed samples at the site without repeating collection",
        ],
        "Speed and time determine packed cell volume accuracy. Open lids, damaged tubes, and hemolysis introduce safety and analytic error.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-021
    fact(
        "skill-poct",
        "How should waived test kits be stored when room temperature is required?",
        "Within the temperature range on the carton and in the IFU",
        [
            "In a household freezer to lengthen cartridge shelf life between clinics",
            "In direct sunlight on a vehicle dashboard between outreach sites",
            "Mixed warm and cold reagent lots in one bin without lot labels attached",
        ],
        "Reagents degrade outside labeled ranges. Freezing, heat, and unlabeled commingling risk silent performance loss.",
        [S.FDA_CLIA_WAIVED, S.CDC_VACCINE_STORAGE],
        "intermediate",
    ),
    # skill-poct-022
    fact(
        "skill-poct",
        "Why must urinalysis dipstick pads be read within the stated time window?",
        "Color reactions follow fixed timers; late reads misclassify results",
        [
            "Pads stay accurate if read many hours after dipping in the specimen",
            "Pad color is unrelated to the chemistry being measured on the strip",
            "Patient name on the cup is optional for waived urinalysis in clinic",
        ],
        "Each pad has a defined read time; delays cause false positives or negatives. Proper labeling is still required; timing does not replace identifiers.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-023
    fact(
        "skill-poct",
        "Which records may a CLIA survey request at a waived testing site?",
        "Test menu, QC logs, operator training, and proficiency files",
        [
            "Front-desk copay collection logs without any laboratory test menu data",
            "General restroom cleaning checklists for the building maintenance team",
            "Annual fire drill sign-in sheets for all departments in the facility",
        ],
        "Inspectors focus on documents that affect testing quality. Administrative logs unrelated to the lab menu do not satisfy survey scope for POCT.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-024
    fact(
        "skill-poct",
        "After blood splashes on a point-of-care analyzer, what must happen before the next patient test?",
        "Clean and disinfect the device per IFU contact times",
        [
            "Wipe wet areas with dry paper towel and continue testing",
            "Rinse the housing in a sink without approved disinfectant",
            "Cover the stain with tape and run the next specimen",
        ],
        "Blood on surfaces requires IFU-approved disinfectants and dwell times. Dry wiping or tape leaves viable contamination for the next user.",
        [S.CDC_STANDARD_PRECAUTIONS, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-025
    fact(
        "skill-poct",
        "Which steps belong in capillary glucose collection under common clinic policy?",
        "Hand hygiene, single-use lancet, and first-drop wipe when policy requires",
        [
            "A multi-use lancing device shared among unrelated clinic patients each day",
            "Vigorous finger milking that causes visible hemolysis at the puncture site",
            "Sampling through a gloved fingertip without skin preparation at the bedside",
        ],
        "Technique affects glucose accuracy and infection prevention. Shared lancets and hemolysis distort results; gloves do not replace skin preparation.",
        [S.CDC_DIABETES_BASICS, S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-026
    fact(
        "skill-poct",
        "What must waived rapid HIV screening in outreach settings include?",
        "Pre- and post-test counseling and confirmatory follow-up per protocol",
        [
            "Posting reactive screening results on a public clinic bulletin board",
            "Testing without informed consent when the outreach screening line is long",
            "Discarding the screening encounter record right after the rapid test",
        ],
        "Screening programs require confidentiality and linkage to confirmatory testing. Public posting and discarded records violate ethics and regulatory expectations.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-027
    fact(
        "skill-poct",
        "Why run parallel checks when changing to a new glucose strip lot?",
        "To detect bias if the new lot reads differently on control material",
        [
            "To open the new strip lot without documenting expiration dates in the log",
            "To run patient samples first and add QC at the end of the clinic shift",
            "To avoid running controls when yesterday's QC already passed on the meter",
        ],
        "Lot change testing catches reagent shifts before patients are affected. Delaying QC or relying on yesterday's pass does not validate the new strips.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-028
    fact(
        "skill-poct",
        "In which situations are urine pregnancy point-of-care false negatives more likely?",
        "Very early pregnancy or overly dilute urine specimens",
        [
            "Reading within the window on a valid midstream sample",
            "Following kit directions for collection and timing",
            "Labeling the cup with two identifiers at the bedside",
        ],
        "Low hCG concentration reduces sensitivity at the start of pregnancy or with dilute urine. Good technique helps but cannot guarantee detection at very low levels.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-029
    fact(
        "skill-poct",
        "Which metrics best support quality improvement for point-of-care testing?",
        "QC failure rates, competency renewal dates, and labeling error counts",
        [
            "Total clinic visit volume tracked without QC failure or competency data",
            "Bandage supply orders tracked without any tie to test performance metrics",
            "Staff overtime hours logged with no connection to point-of-care processes",
        ],
        "Improvement work needs measures linked to analytic and preanalytic steps. Visit volume or supply orders alone do not show where testing breaks down.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-030
    fact(
        "skill-poct",
        "How should waived test cartridges be handled when shipped between clinic sites?",
        "Keep required temperatures and document chain of custody per policy",
        [
            "Leave test kits in a closed vehicle over a hot holiday weekend",
            "Remove expiration dates from cartons to simplify shared inventory counts",
            "Combine chemistry and hematology kits together in unmarked storage bins",
        ],
        "Heat exposure degrades reagents, and traceability supports recalls. Erasing dates or unmarked bins invite use of compromised or untraceable materials.",
        [S.FDA_CLIA_WAIVED, S.CDC_VACCINE_STORAGE],
        "intermediate",
    ),
    # skill-poct-031
    fact(
        "skill-poct",
        "How should capillary blood be applied to a waived hemoglobin cuvette or strip?",
        "Fill to the marked volume without air bubbles in the chamber",
        [
            "Dilute the capillary drop with tap water to reach the marked fill line",
            "Use arterial blood gas syringe samples in the cuvette without validation",
            "Proceed without verifying patient identification to save bedside time",
        ],
        "Underfill, bubbles, and wrong specimen types trigger errors or wrong values. Identity checks remain mandatory regardless of test speed.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-032
    fact(
        "skill-poct",
        "What should a medical assistant do when a point-of-care result conflicts with the clinical picture?",
        "Notify the provider and repeat or send confirmatory testing per protocol",
        [
            "Remove the unexpected value from the workstation screen before saving",
            "Change the reported result to match the expected diagnosis in the chart",
            "Discharge the patient without informing the care team about the conflict",
        ],
        "Discordant values may reflect preanalytic or analytic error. Editing or deleting results hides data the provider needs to reconcile with the exam.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-033
    fact(
        "skill-poct",
        "For which test complexity does CLIA require a laboratory director?",
        "Moderate- and high-complexity testing, not typical waived menus run per IFU",
        [
            "Every wound dressing change performed in the outpatient clinic setting",
            "All waived tests at every site regardless of CLIA certificate type held",
            "Patient registration and scheduling work at the front desk computer station",
        ],
        "Certificate type matches analytic complexity. Waived sites still need QC and responsible personnel, but a full laboratory director role applies to higher tiers.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-034
    fact(
        "skill-poct",
        "When should external control materials packaged with a strep antigen kit be run?",
        "On the IFU schedule and when opening a new kit shipment lot",
        [
            "When patient test lines are faint and staff want to conserve control vials",
            "Using sterile saline instead of the control fluid supplied in the kit box",
            "One time when the clinic first adopts that rapid strep test system",
        ],
        "External controls verify reagent integrity across shipments. Substituting saline or skipping scheduled runs defeats the purpose of the provided material.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-035
    fact(
        "skill-poct",
        "Which patient factors may alter fingerstick INR point-of-care results?",
        "Anemia and changing anticoagulant levels that affect clotting",
        [
            "Room humidity within typical seasonal indoor ranges in the clinic",
            "Collection from the middle finger instead of the index on the same hand",
            "A control run that passed earlier the same morning on that device",
        ],
        "Some devices are sensitive to hematocrit and drug effect on coagulation. Passing morning QC and finger choice do not remove physiologic influence on INR.",
        [S.FDA_CLIA_WAIVED, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-poct-036
    fact(
        "skill-poct",
        "Where should current waived test instructions be available to operators?",
        "At the testing station, updated when the manufacturer revises the IFU",
        [
            "In locked off-site storage that staff cannot reach during patient care",
            "Discarded after initial training sessions to reduce drawer clutter at the bench",
            "Replaced by informal handwritten notes that omit troubleshooting steps from IFU",
        ],
        "Immediate IFU access supports correct troubleshooting during failed QC or unclear flags. Off-site or stripped-down notes may miss critical steps.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-037
    fact(
        "skill-poct",
        "When must capillary tubes or cartridges be labeled during bedside collection?",
        "Before leaving the patient, using two patient identifiers",
        [
            "After the specimen arrives in a lab in another building",
            "With patient initials alone when the full name is delayed",
            "Using labels printed earlier for a different patient",
        ],
        "Mislabeling is a leading cause of wrong-result reporting. Delayed or partial labels raise risk of swapped identity at the bedside.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-038
    fact(
        "skill-poct",
        "What trends might routine review of POCT incident logs reveal?",
        "Repeated QC failures, training gaps, and specimen handling errors",
        [
            "One-time label printer jams in the office without recurring QC failure patterns",
            "Front desk phone queue times tracked without any specimen labeling error data",
            "Elevator maintenance tickets filed without connection to POCT testing workflows",
        ],
        "Log review targets recurring testing problems. Isolated office equipment issues or unrelated facilities work do not show operator or QC trends.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-039
    fact(
        "skill-poct",
        "Why is careful finger site preparation important before capillary lead screening?",
        "Surface lead on skin can falsely elevate capillary lead results",
        [
            "Alcohol alone without first removing dust and dirt on the child's finger",
            "Shared lancets between siblings in the room when parents request reuse",
            "Proceeding without hand hygiene at the collection site to shorten the visit",
        ],
        "Environmental lead on unwashed skin can inflate capillary values. Alcohol without cleaning and shared lancets add contamination and infection risks.",
        [S.FDA_CLIA_WAIVED, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-poct-040
    fact(
        "skill-poct",
        "What should a POCT emergency plan cover during an extended power outage?",
        "Battery-backed meters and documented manual workflows",
        [
            "Clinician estimates when devices cannot be powered on",
            "Mass discharge without assessing unstable patients",
            "Suspending all QC until utility power returns for good",
        ],
        "Continuity plans keep essential testing on validated backup devices. Guessing values or halting QC abandons the standard of care during the outage.",
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
            "Post results to the patient portal without any provider sign-off",
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
        "Run required control materials and document pass or fail outcomes",
        [
            "Begin patient testing first that morning to reduce waiting room times",
            "Pour old and new reagent cartridges into one shared storage container",
            "Discard the IFU booklet from the prior lot to free drawer space at the bench",
        ],
        "Lot verification catches shipping or manufacturing problems before patients are tested. Patient-first testing or commingled reagents bypass that safety check.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
]
