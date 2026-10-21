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
        "CLIA-waived point-of-care tests in physician offices must:",
        "Follow the manufacturer's instructions for use and quality control schedule",
        [
            "Ignore control materials when the clinic is busy",
            "Use expired cartridges to reduce waste",
            "Share lancets between unrelated patients",
        ],
        "Waived status does not remove QC or competency requirements. Shared lancets transmit bloodborne pathogens.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-002
    fact(
        "skill-poct",
        "A Certificate of Waiver under CLIA allows a site to perform:",
        "Tests classified as waived when conducted per FDA-cleared instructions",
        [
            "Any laboratory assay without training",
            "Moderate complexity cultures without a director",
            "Genomic sequencing without documentation",
        ],
        "Waived tests have defined complexity limits. Higher complexity requires additional CLIA certificates.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-003
    fact(
        "skill-poct",
        "Glucose meter quality control with liquid control solution validates:",
        "That the meter and strips read within expected ranges for known concentrations",
        [
            "Patient identity without a second identifier",
            "Insurance eligibility for the visit",
            "Room lighting preferences",
        ],
        "Control solution checks catch strip lot problems and meter drift. Administrative tasks are separate steps.",
        [S.FDA_CLIA_WAIVED, S.CDC_DIABETES_BASICS, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-004
    fact(
        "skill-poct",
        "When should glucose meter QC run per typical manufacturer guidance?",
        "Each new lot of strips, after meter drops, and on scheduled days defined in policy",
        [
            "Once per decade regardless of use",
            "After every patient without using control material",
            "When results are discarded without logging",
        ],
        "Event-based and routine QC schedules detect device problems early. Patient testing alone does not replace controls.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-005
    fact(
        "skill-poct",
        "Capillary blood glucose sampling sites should be rotated to:",
        "Reduce pain, callus formation, and unreliable readings from thickened skin",
        [
            "Eliminate hand hygiene requirements",
            "Replace documentation of results",
            "Remove the need for calibration checks",
        ],
        "Thickened fingertips skew results and hurt patients. Rotation preserves skin integrity.",
        [S.NHA_CCMA, S.CDC_DIABETES_BASICS],
        "beginner",
    ),
    # skill-poct-006
    fact(
        "skill-poct",
        "Before performing a waived rapid strep test, the pharynx should be swabbed:",
        "On the tonsillar pillars and posterior pharynx without touching tongue or teeth first",
        [
            "On the buccal mucosa alone",
            "After eating greasy food without rinsing when possible",
            "With the same swab on two patients to save supplies",
        ],
        "Adequate collection reduces false negatives. Contamination and reuse compromise accuracy and safety.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "intermediate",
    ),
    # skill-poct-007
    fact(
        "skill-poct",
        "Urine pregnancy point-of-care tests detect:",
        "Human chorionic gonadotropin in urine when used within the kit read window",
        [
            "Blood type antigens on red cells",
            "Serum potassium concentration",
            "Bacterial culture growth overnight",
        ],
        "hCG immunoassays are qualitative screening tools. Misapplied specimen types yield invalid results.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-008
    fact(
        "skill-poct",
        "Documentation for waived test results should include:",
        "Patient identifier, test name, result, time, operator, and lot numbers when required",
        [
            "A sticker with no patient name",
            "The operator's personal password",
            "Zodiac sign instead of time",
        ],
        "Complete records support clinical decisions and regulatory inspection. Anonymous stickers risk wrong-chart entries.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-009
    fact(
        "skill-poct",
        "Cleaning a blood glucose meter between patients prevents:",
        "Cross-contamination with bloodborne pathogens on device surfaces",
        [
            "Battery replacement needs",
            "Insurance copay changes",
            "Calibration law expiration",
        ],
        "Blood contact requires disinfecting per instructions for use. Financial and power issues are unrelated.",
        [S.CDC_STANDARD_PRECAUTIONS, S.OSHA_BBP, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-010
    fact(
        "skill-poct",
        "If a waived test control result is out of range, the next step is:",
        "Repeat QC, troubleshoot per IFU, and withhold patient testing until resolved",
        [
            "Report patient results anyway without comment",
            "Change control solution brand mid-run without logging",
            "Disable the incident log for the day",
        ],
        "Failed controls indicate unreliable patient results. Troubleshooting restores safe testing.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-011
    fact(
        "skill-poct",
        "Hemoglobin A1c point-of-care devices typically require:",
        "Whole blood specimen type and periodic control checks listed in the IFU",
        [
            "Saliva swabs from the cheek",
            "Cerebrospinal fluid samples",
            "No operator training records",
        ],
        "Specimen matrices are validated per device. Training and QC remain mandatory for waived analyzers.",
        [S.FDA_CLIA_WAIVED, S.ADA_STANDARDS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-012
    fact(
        "skill-poct",
        "INR point-of-care testing with a fingerstick device needs:",
        "Proper sample volume and scheduled control testing per manufacturer",
        [
            "Serum from a chemistry tube without validation",
            "Shared lancing devices between patients",
            "Ignoring hematoma at the puncture site",
        ],
        "Anticoagulation monitoring depends on accurate sampling technique. Shared lancets are unsafe.",
        [S.FDA_CLIA_WAIVED, S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-013
    fact(
        "skill-poct",
        "Influenza rapid antigen testing sensitivity improves when:",
        "Specimens are collected within the recommended days of symptom onset using proper technique",
        [
            "Patients are tested years after illness",
            "Swabs are stored hot in a car trunk for days",
            "Labels are applied after results are called without IDs",
        ],
        "Viral shedding wanes over time, lowering sensitivity. Storage and labeling errors add separate risks.",
        [S.FDA_CLIA_WAIVED, S.CDC_STANDARD_PRECAUTIONS],
        "beginner",
    ),
    # skill-poct-014
    fact(
        "skill-poct",
        "Operator competency for POCT should be:",
        "Documented after training, demonstration, and periodic reassessment",
        [
            "Assumed from job title without observation",
            "Optional after the first patient",
            "Based on social media tutorials alone",
        ],
        "CLIA quality systems require evidence of competent testing personnel. Informal learning lacks verification.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-015
    fact(
        "skill-poct",
        "Thermometers used for clinic screening should be:",
        "Calibrated or checked per policy and cleaned between patients",
        [
            "Shared oral probes without covers",
            "Aimed at footwear for core temperature",
            "Stored uncleaned in a personal purse",
        ],
        "Device hygiene and calibration affect fever detection. Nonstandard sites produce unreliable readings.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-016
    fact(
        "skill-poct",
        "Pulse oximetry as a bedside test is affected by:",
        "Poor perfusion, nail polish, and patient motion",
        [
            "Shoe size alone",
            "Wall paint color in the hallway",
            "Stethoscope tubing length",
        ],
        "Optical sensors need steady perfusion at the probe site. Environmental décor does not change SpO2 physics.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-017
    fact(
        "skill-poct",
        "External quality assessment for waived testing may involve:",
        "Proficiency samples sent to a program that grades blinded results",
        [
            "Replacing all internal QC forever",
            "Eliminating operator training",
            "Using unlabeled reagents from unknown vendors",
        ],
        "Proficiency testing complements routine QC by benchmarking performance. It does not remove daily controls.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-018
    fact(
        "skill-poct",
        "A waived lipid panel point-of-care test may require:",
        "Fasting status per order and proper capillary or venous collection",
        [
            "A milkshake immediately before sampling",
            "Heel sticks on every adult routinely",
            "Discarding labels to speed workflow",
        ],
        "Triglycerides rise postprandially, affecting interpretation. Specimen type must match device validation.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-019
    fact(
        "skill-poct",
        "Positive predictive value of a rapid strep test falls when:",
        "Community prevalence of group A strep is low",
        [
            "Prevalence is high during outbreak",
            "Collection follows IFU",
            "Controls pass each day",
        ],
        "Bayesian context means more false positives in low-prevalence settings. Good technique cannot override base rates.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-020
    fact(
        "skill-poct",
        "Hematocrit spin procedures, when used, require:",
        "Calibrated centrifuge speed and timing per protocol",
        [
            "Running with the lid open",
            "Using cracked capillary tubes",
            "Ignoring hemolysis at the site",
        ],
        "Mechanical parameters affect separation accuracy. Damaged tubes and hemolysis skew results.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-021
    fact(
        "skill-poct",
        "Room temperature storage of waived test kits should follow:",
        "Manufacturer ranges listed on boxes and IFU",
        [
            "Freezing all cartridges for longevity",
            "Leaving kits in direct sunlight on the dashboard",
            "Mixing warm and cold lots without logging",
        ],
        "Reagent stability depends on controlled storage. Heat and freeze-thaw cycles degrade performance.",
        [S.FDA_CLIA_WAIVED, S.CDC_VACCINE_STORAGE],
        "intermediate",
    ),
    # skill-poct-022
    fact(
        "skill-poct",
        "When performing waived urinalysis dipsticks, timing of reading is important because:",
        "Pads change color on fixed schedules; late reads misclassify results",
        [
            "Dipsticks are valid after twenty-four hours on the strip",
            "Color is unrelated to chemistry",
            "Patient name is optional on the cup",
        ],
        "Each pad has a read window. Delayed interpretation causes false positives or negatives.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-023
    fact(
        "skill-poct",
        "CLIA-waived site surveys may review:",
        "Test menus, QC logs, operator training, and proficiency records",
        [
            "Cafeteria recipes without lab relevance",
            "Patient movie preferences",
            "Parking lot paint colors",
        ],
        "Inspectors focus on conditions that affect test quality. Non-laboratory trivia is out of scope.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-024
    fact(
        "skill-poct",
        "If a patient blood sample splashes on a POCT analyzer, the device should be:",
        "Cleaned and disinfected per IFU before the next patient use",
        [
            "Wiped with a dry tissue and used immediately",
            "Rinsed in the breakroom sink without disinfectant",
            "Covered with tape and ignored",
        ],
        "Blood contact requires approved disinfectants and contact times. Incomplete cleaning risks cross-contamination.",
        [S.CDC_STANDARD_PRECAUTIONS, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-025
    fact(
        "skill-poct",
        "Capillary collection for glucose should include:",
        "Hand hygiene, single-use lancet, and wipe away first drop when policy requires",
        [
            "Reusing lancet devices between family members in clinic",
            "Milking the finger vigorously causing hemolysis",
            "Testing through gloved finger without site prep",
        ],
        "Technique influences glucose accuracy and infection prevention. Hemolysis and reuse are unsafe practices.",
        [S.CDC_DIABETES_BASICS, S.OSHA_BBP, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-026
    fact(
        "skill-poct",
        "Waived rapid HIV screening in outreach must include:",
        "Pre- and post-test counseling per protocol and confirmatory workflow",
        [
            "Posting results on a public bulletin board",
            "Testing without informed consent processes",
            "Discarding documentation to save paper",
        ],
        "Screening programs have confidentiality and linkage requirements. Public disclosure violates ethics and law.",
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-027
    fact(
        "skill-poct",
        "Lot-to-lot strip comparisons for glucose meters help detect:",
        "Systematic bias when a new strip lot reads differently from controls",
        [
            "Patient shoe preferences",
            "Insurance deductible amounts",
            "Staff vacation schedules",
        ],
        "Parallel testing during lot changes catches reagent shifts. Administrative data do not validate chemistry.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-028
    fact(
        "skill-poct",
        "Point-of-care pregnancy test false negatives may occur with:",
        "Very early pregnancy or dilute urine specimens",
        [
            "Reading within the stated window on a valid sample",
            "Using midstream urine per kit directions",
            "Labeling the cup with two identifiers",
        ],
        "Low hCG concentration reduces sensitivity early on. Proper technique does not guarantee detection at very low levels.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-029
    fact(
        "skill-poct",
        "Quality improvement for POCT may track:",
        "QC failure rates, operator competency expirations, and specimen labeling errors",
        [
            "Number of coffee cups used per day",
            "Patient favorite music genres",
            "Parking ticket counts",
        ],
        "Metrics tied to testing steps drive corrective action. Unrelated counts do not measure lab quality.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-030
    fact(
        "skill-poct",
        "When shipping waived test cartridges between clinic sites, staff should:",
        "Maintain temperature ranges and document chain of custody per policy",
        [
            "Leave kits in a hot vehicle for weekends",
            "Remove expiration dates to simplify inventory",
            "Mix chemistry and hematology kits without labels",
        ],
        "Heat exposure degrades reagents. Traceability supports recalls and troubleshooting.",
        [S.FDA_CLIA_WAIVED, S.CDC_VACCINE_STORAGE],
        "intermediate",
    ),
    # skill-poct-031
    fact(
        "skill-poct",
        "A waived hemoglobin device using capillary blood requires:",
        "Filling the cuvette or strip to the marked volume without air bubbles",
        [
            "Diluting with tap water to double volume",
            "Using venous gas samples",
            "Ignoring patient identification to save time",
        ],
        "Volume errors cause analytic failure flags or wrong values. Specimen type must match validation.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-032
    fact(
        "skill-poct",
        "If a POCT result conflicts with clinical presentation, the MA should:",
        "Notify the provider and repeat or send confirmatory testing per protocol",
        [
            "Hide the unexpected value",
            "Change the result to match assumptions",
            "Discharge without telling the care team",
        ],
        "Discordant results may indicate preanalytic or analytic error. Providers integrate data with exam findings.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "advanced",
    ),
    # skill-poct-033
    fact(
        "skill-poct",
        "CLIA requires a laboratory director for:",
        "Moderate and high complexity testing, not typical waived test menus performed per IFU",
        [
            "Every bandage application in clinic",
            "All waived tests without exception",
            "Patient registration at the front desk",
        ],
        "Certificate type matches test complexity. Waived sites still need responsible personnel and QC programs.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-034
    fact(
        "skill-poct",
        "Strep antigen kit external controls, when provided, should be run:",
        "According to schedule in the IFU and when opening new kit lots",
        [
            "When patient tests are negative without controls",
            "Using tap water instead of provided material",
            "Once per lifetime of the clinic",
        ],
        "External controls verify reagent integrity across shipments. Substituting water invalidates the check.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-035
    fact(
        "skill-poct",
        "Fingerstick INR devices may be affected by:",
        "Anemia and certain anticoagulant levels that alter clotting dynamics",
        [
            "Patient hair color",
            "Clinic wallpaper patterns",
            "Parking validation stickers",
        ],
        "Physiologic variables influence coagulation testing. Cosmetic factors are irrelevant.",
        [S.FDA_CLIA_WAIVED, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-poct-036
    fact(
        "skill-poct",
        "Waived test operator manuals should be:",
        "Accessible at the testing station and updated when manufacturers revise IFU",
        [
            "Stored off-site without staff access",
            "Destroyed after initial training",
            "Replaced with unofficial summaries",
        ],
        "Immediate access to IFU supports correct troubleshooting. Unofficial summaries may omit critical steps.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-037
    fact(
        "skill-poct",
        "Labeling capillary tubes or cartridges at bedside requires:",
        "Two patient identifiers applied before leaving the patient",
        [
            "Labeling after centrifugation in another building",
            "Using initials without name",
            "Placing stickers from a prior patient",
        ],
        "Mislabeling is a leading cause of wrong-result reporting. Identifiers must be verified at collection.",
        [S.CLSI_GP41, S.NHA_CCMA],
        "beginner",
    ),
    # skill-poct-038
    fact(
        "skill-poct",
        "Routine review of POCT incident logs helps identify:",
        "Repeated QC failures, operator training gaps, and specimen handling issues",
        [
            "Preferred pizza toppings among staff",
            "Unrelated social media trends",
            "Weather forecasts for next month",
        ],
        "Trend analysis targets process fixes. Nonclinical trivia does not improve testing.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-poct-039
    fact(
        "skill-poct",
        "When performing waived lead screening capillary tests, site cleaning should:",
        "Reduce surface lead contamination that falsely elevates results",
        [
            "Use alcohol alone without removing dust on fingers",
            "Reuse lancets between siblings without policy",
            "Ignore handwashing to save time",
        ],
        "Environmental lead on skin can skew capillary results. Aseptic technique still applies.",
        [S.FDA_CLIA_WAIVED, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
    # skill-poct-040
    fact(
        "skill-poct",
        "Backup plans for POCT during power outage may include:",
        "Battery-powered meters and documented manual workflows per emergency plan",
        [
            "Guessing results without devices",
            "Discharging all patients without assessment",
            "Disabling all QC forever",
        ],
        "Continuity plans maintain essential testing with validated alternatives. Guessing abandons standard of care.",
        [S.NHA_CCMA, S.FDA_CLIA_WAIVED],
        "intermediate",
    ),
    # skill-poct-041
    fact(
        "skill-poct",
        "Waived test result reporting to patients should follow:",
        "Provider or protocol-driven communication with documentation in the record",
        [
            "Shouting results in a crowded waiting room",
            "Texting unencrypted messages to wrong numbers",
            "Withholding abnormal values without provider review",
        ],
        "Privacy and clinical context matter when sharing results. Public disclosure violates HIPAA expectations.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-poct-042
    fact(
        "skill-poct",
        "Before opening a new waived test kit lot, staff should:",
        "Run required control materials and document outcomes",
        [
            "Begin patient testing to save minutes",
            "Mix old and new lots in one container",
            "Discard IFU to reduce clutter",
        ],
        "Lot verification catches shipping or manufacturing issues. Discarding IFU removes essential instructions.",
        [S.FDA_CLIA_WAIVED, S.NHA_CCMA],
        "beginner",
    ),
]
