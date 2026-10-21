# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-admin)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-admin-001
    fact(
        "ccma-admin",
        "When should a medical office collect a patient copayment?",
        "At the time of service according to the payer contract",
        [
            "After the plan's annual deductible resets in January",
            "When the patient submits a tax return",
            "During inpatient admission regardless of outpatient policy",
        ],
        "Copayments are fixed cost-sharing amounts defined in the benefit plan. Collecting at the visit matches most payer contracts and reduces accounts receivable follow-up.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-002
    fact(
        "ccma-admin",
        "Under which circumstance may a managed care plan require a referral?",
        "The member selected a primary care gatekeeper plan that mandates specialist authorization",
        [
            "The patient pays the day sheet in cash",
            "The visit includes a routine blood pressure screening",
            "The clinic schedules a flu vaccine clinic",
        ],
        "Gatekeeper models tie specialist access to PCP referral rules. Cash payment or preventive nursing measures do not by themselves trigger referral requirements.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-003
    fact(
        "ccma-admin",
        "What information does a superbill or encounter form capture for billing staff?",
        "Diagnoses, procedures performed, and charges for the visit",
        [
            "Procedure codes without linked diagnosis pointers",
            "Charges posted without units or service dates",
            "Patient demographic updates without encounter diagnoses",
        ],
        "Superbills translate the clinical encounter into codable data for claims. Supply and parking details are operational, not claim drivers.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-004
    fact(
        "ccma-admin",
        "What does the accounts receivable ledger track for a medical practice?",
        "Outstanding balances owed by patients and third-party payers",
        [
            "Par levels for exam room gloves",
            "Employee paid time off balances",
            "Laboratory specimen rejection rates",
        ],
        "Accounts receivable reflects revenue still due after service. Inventory and HR metrics belong to other operational reports.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-005
    fact(
        "ccma-admin",
        "How are ICD-10-CM codes used on an insurance claim?",
        "They report the patient's diagnoses and reasons for the encounter",
        [
            "They list surgical instrument sterilization times",
            "They document nursing shift handoffs as the primary diagnosis",
            "They report supply par levels for exam room stock",
        ],
        "Diagnosis codes establish medical necessity for billed services. Environmental logs and staffing notes are not ICD-10-CM purposes.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-006
    fact(
        "ccma-admin",
        "How should no-show appointments be handled in the electronic health record?",
        "Document the missed visit per policy so scheduling and outreach can follow up",
        [
            "Delete the patient's entire chart to free space",
            "Convert the slot into a billing code for a completed visit",
            "Leave the schedule blank without any note",
        ],
        "No-show tracking supports access management and may trigger outreach. Deleting charts or fabricating visits creates legal and revenue integrity problems.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-007
    fact(
        "ccma-admin",
        "What is the primary legal role of the medical record?",
        "It documents the care provided and supports continuity, billing, and legal review",
        [
            "It serves as a personal journal for staff opinions",
            "It may be discarded after each outpatient visit",
            "It replaces informed consent forms in every setting",
        ],
        "The record is the formal account of patient care. It is retained per law and policy, and it complements rather than replaces consent documentation.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-008
    fact(
        "ccma-admin",
        "How is a copayment defined in most commercial insurance plans?",
        "A fixed dollar amount the member pays for a covered service at the time of care",
        [
            "The full billed charge regardless of contract",
            "A payment made by the clinic to the employer",
            "A penalty assessed when the patient uses an in-network provider",
        ],
        "Copays are predetermined member responsibility for covered services. They differ from total charges and are not paid by the clinic to others.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-009
    fact(
        "ccma-admin",
        "Which insurance card details should be verified when scanning into the EHR?",
        "Member identifier, group number, and coverage effective dates",
        [
            "Card background color and font style",
            "Payer phone number without member or group identifiers",
            "Prior plan name without updating effective dates",
        ],
        "Payers route claims using member and group identifiers with effective dates. Cosmetic card features do not determine eligibility.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-010
    fact(
        "ccma-admin",
        "Why is insurance eligibility verification helpful when scheduling a new patient?",
        "It confirms active coverage before services are provided",
        [
            "It removes the need to obtain a medical history",
            "It exempts the clinic from HIPAA privacy rules",
            "It eliminates member cost sharing for every service",
        ],
        "Eligibility responses reduce surprise denials and clarify benefits. Privacy rules and clinical assessment requirements still apply.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-011
    fact(
        "ccma-admin",
        "What is the goal of a practice compliance program?",
        "Promote ethical coding, billing, and adherence to regulations",
        [
            "Maximize revenue through intentional upcoding",
            "Destroy audit logs after each business day",
            "Ignore Office of Inspector General guidance",
        ],
        "Compliance programs train staff and monitor processes to prevent fraud and abuse. Destroying audits or ignoring OIG guidance increases legal risk.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-012
    fact(
        "ccma-admin",
        "How does a superbill link clinical work to the revenue cycle?",
        "It maps services rendered to diagnosis and procedure codes for charge entry",
        [
            "It matches patient hobbies to payroll deductions",
            "It ties parking citations to laboratory orders",
            "It links nursing vital signs to payroll tax withholdings",
        ],
        "Charge capture depends on accurate code linkage from the encounter. Nonclinical data do not generate insurable claims.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-013
    fact(
        "ccma-admin",
        "What is the focus of accounts receivable follow-up work?",
        "Collecting or resolving unpaid patient and payer balances",
        [
            "Ordering exam room paper supplies",
            "Scheduling staff break rotations",
            "Archiving personal email folders",
        ],
        "Follow-up targets outstanding balances on statements and remittance advice. Supply ordering is materials management, not collections.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-014
    fact(
        "ccma-admin",
        "Why are audit trails in billing modules important?",
        "They show who changed charges, payments, or adjustments",
        [
            "They hide user activity from compliance officers",
            "They replace clinical progress notes",
            "They remove the need for unique login credentials",
        ],
        "Audit logs support internal monitoring and payer audits. They supplement, not replace, clinical documentation and authentication controls.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-015
    fact(
        "ccma-admin",
        "What do Current Procedural Terminology (CPT) codes describe?",
        "Physician and other qualified health care professional services and procedures",
        [
            "Vacutainer tube additive colors",
            "Reference ranges for vital signs",
            "Recommended injection angles for vaccines",
        ],
        "CPT codes report billable procedures and visits. Specimen handling colors and vital norms are reference data, not CPT descriptors.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-016
    fact(
        "ccma-admin",
        "When does coordination of benefits apply?",
        "A patient has more than one active health plan that may share payment responsibility",
        [
            "The patient is uninsured and pays cash",
            "The visit is limited to vision hardware fitting",
            "The clinic closes for a weather emergency",
        ],
        "Secondary and primary payers are identified when multiple policies exist. Uninsured cash visits do not trigger coordination rules.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-017
    fact(
        "ccma-admin",
        "How should front desk staff handle copayment collection?",
        "Follow written financial policy and issue receipts when required",
        [
            "Waive balances informally for acquaintances without documentation",
            "Collect a flat cash amount without checking the eligibility copay",
            "Ignore contracted copay amounts on the eligibility response",
        ],
        "Consistent policy application supports fairness and audits. Public posting of payments violates privacy expectations.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-018
    fact(
        "ccma-admin",
        "What does a daily day sheet report typically summarize?",
        "Charges posted, payments received, and adjustments for that business day",
        [
            "Patient birth dates for the calendar year",
            "Year-to-date revenue without daily payment detail",
            "Personal staff vacation requests",
        ],
        "Day sheets reconcile cash drawers and posting batches. Demographic lists and weather are unrelated to daily financial totals.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-019
    fact(
        "ccma-admin",
        "Which data may appear on an electronic eligibility response?",
        "Coverage status, plan name, and benefit highlights",
        [
            "Patient portal passwords",
            "Unrelated consumer credit scores by default",
            "Home addresses of billing staff",
        ],
        "Eligibility transactions return benefit information permitted by the transaction. Authentication secrets and employee home data are out of scope.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-020
    fact(
        "ccma-admin",
        "How does the HIPAA minimum necessary standard apply in the billing office?",
        "Staff should access the least PHI needed to perform the billing task",
        [
            "Entire charts may be emailed to any vendor upon request",
            "Diagnosis lists can be posted in the waiting room",
            "Break room televisions may display claim details",
        ],
        "Minimum necessary limits incidental disclosure during payment operations. Public display of diagnoses violates privacy expectations.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-021
    fact(
        "ccma-admin",
        "What is the purpose of ICD-10-CM diagnosis coding on a claim?",
        "Communicate why the patient was seen and justify medical necessity",
        [
            "Record the sequence of blood tube draws",
            "Document chest compression depth during CPR",
            "List EKG electrode cable colors",
        ],
        "Diagnosis codes explain the reason for service. Procedural technique details belong in clinical documentation, not ICD-10-CM selection.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-022
    fact(
        "ccma-admin",
        "Who determines how long medical records must be retained?",
        "Federal and state law, accreditation standards, and organizational policy",
        [
            "Whichever staff member prefers the shortest period",
            "The same interval used for general office supply invoices",
            "Text messages from patients without documentation",
        ],
        "Retention schedules are governed by legal and accreditation rules. Individual preference or informal polls do not set retention.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-023
    fact(
        "ccma-admin",
        "When should CPT modifiers be appended to a claim line?",
        "When payer rules require clarification of how a service was performed",
        [
            "On every line to raise payment without documentation",
            "Instead of supplying any diagnosis code",
            "To replace medical record documentation entirely",
        ],
        "Modifiers convey special circumstances such as bilateral procedures. They do not substitute for diagnoses or clinical records.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-024
    fact(
        "ccma-admin",
        "What does prior authorization indicate for a scheduled service?",
        "The payer may require approval before the procedure or test is performed",
        [
            "The member will have no cost sharing for the service",
            "HIPAA authorization is no longer required for treatment",
            "The medical assistant may perform invasive surgery independently",
        ],
        "Prior auth addresses coverage and medical necessity review. It does not change scope of practice or eliminate copays by itself.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-025
    fact(
        "ccma-admin",
        "What registration steps are important when enrolling a minor patient?",
        "Verify guardian identity and custody or consent authority when applicable",
        [
            "Accept the minor's signature as the sole legal authorization",
            "Omit guardian contact information to save time",
            "Publish the patient's home address on the clinic website",
        ],
        "Minors generally require guardian involvement for consent and billing. Public posting of addresses breaches privacy and safety expectations.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-026
    fact(
        "ccma-admin",
        "What risk can occur if providers are double-booked without a written scheduling policy?",
        "Visit length and patient access may suffer, leading to dissatisfaction",
        [
            "Clinical quality automatically improves for every patient",
            "HIPAA privacy rules are waived for that day",
            "Waiting times disappear for all appointment types",
        ],
        "Overbooking without controls can shorten contact time and delay care. It does not alter privacy law or eliminate queues by itself.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-027
    fact(
        "ccma-admin",
        "How do scheduling templates benefit an outpatient practice?",
        "They align appointment types with provider time and room resources",
        [
            "They permanently hide all open appointment slots",
            "They require unlimited double booking of physical exams",
            "They remove the need to document visit types",
        ],
        "Templates balance acute, preventive, and procedure visits. Hiding slots or skipping documentation undermines access and data quality.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-028
    fact(
        "ccma-admin",
        "Which of the following belongs in telehealth intake documentation?",
        "Patient location, consent to virtual care, and modality used",
        [
            "Chief complaint alone with no consent or location documented",
            "Insurance eligibility verified with no note of virtual versus in-person visit",
            "A scanned insurance card without patient identity or visit consent",
        ],
        "Payers and regulators expect location and consent for telehealth claims. Marketing metrics do not satisfy clinical or billing documentation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-029
    fact(
        "ccma-admin",
        "For which type of claim is the CMS-1500 form commonly used?",
        "Professional services provided in outpatient settings",
        [
            "Inpatient facility charges billed on the UB-04",
            "Retail prescription labels printed by pharmacies",
            "Internal employee payroll direct deposits",
        ],
        "CMS-1500 is the standard professional claim form in many ambulatory settings. Inpatient facilities typically use UB-04 institutional claims.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-030
    fact(
        "ccma-admin",
        "An attorney's office faxes a records request for a current patient. The cover sheet shows firm letterhead and a HIPAA authorization, but the printed patient name is one letter different from the chart while date of birth matches. What should staff do before releasing information?",
        "Hold the request and verify patient identity per policy before matching the authorization to the chart",
        [
            "Ask the attorney to resend the authorization with a corrected patient name, then release the full chart",
            "Release the minimum necessary records because the date of birth on the form matches the chart",
            "Call the patient to confirm the request and release records based on verbal approval alone",
        ],
        "Valid disclosure requires a correct authorization tied to the right individual. Similar names and partial identifiers are a common source of misdirected PHI.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-admin-031
    fact(
        "ccma-admin",
        "What does a signed release of information (ROI) form authorize?",
        "Disclosure of specified health information to named recipients",
        [
            "Disclosure of the entire chart to any caller who knows the patient name",
            "Deletion of every diagnosis from the legal record",
            "Unlimited use of data for unrelated product marketing",
        ],
        "ROI forms define who may receive which records. They do not permit marketing or destruction of legally required documentation.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-032
    fact(
        "ccma-admin",
        "Under CLIA, what characterizes a waived laboratory test?",
        "It is simple and low risk of an erroneous result per FDA waiver criteria",
        [
            "It requires the same daily quality control as high-complexity chemistry",
            "It is exempt from quality checks and training",
            "It may be run without following manufacturer instructions",
        ],
        "Waived tests still require controlled procedures, personnel competency, and manufacturer directions. Waived status is not the same as unregulated testing.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-033
    fact(
        "ccma-admin",
        "When should verification of benefits be performed for a scheduled procedure?",
        "Before or at the time of service when feasible",
        [
            "After the payer denies the first claim without a prior eligibility check",
            "After the patient has filed bankruptcy",
            "After the claim has been denied without review",
        ],
        "Timely benefit verification clarifies coverage and cost sharing before service. Delayed checks increase surprise bills and rework.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-034
    fact(
        "ccma-admin",
        "Which practices support safe clinic supply inventory control?",
        "Set par levels, monitor expiration dates, and store items securely",
        [
            "Reorder supplies when shelves are empty without par levels",
            "Ignore lot numbers on vaccines",
            "Store personal medications with clinic stock",
        ],
        "Inventory control prevents waste and safety events. Sharps and commingled personal drugs create exposure and error risk.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-035
    fact(
        "ccma-admin",
        "What is prior authorization in the revenue cycle?",
        "Payer review and approval before selected services or medications are covered",
        [
            "A vital sign measurement taken at check-in",
            "A requirement to bandage every minor abrasion",
            "An optional step that payers do not enforce",
        ],
        "Many plans mandate authorization for high-cost imaging or specialty drugs. Skipping required auth commonly results in denial.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-036
    fact(
        "ccma-admin",
        "Which demographic updates should be confirmed at registration?",
        "Legal name, address, contacts, insurance, and communication preferences",
        [
            "Nickname only without confirming legal name for the health record",
            "Mailing address copied from a prior patient with the same last name",
            "Removal of documented allergy entries without clinician review",
        ],
        "Accurate demographics keep claims and messages routed correctly. Allergy deletion requires clinical oversight, not front desk discretion alone.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-037
    fact(
        "ccma-admin",
        "What should telephone triage documentation record?",
        "Caller identity, symptoms, advice given, and follow-up instructions",
        [
            "Symptoms described without documenting advice given",
            "Callback number missing when the caller is not the patient",
            "Full credit card numbers in unencrypted progress text",
        ],
        "Triage notes create a legal record of the call. Other patients' identifiers and card data must not appear in clinical documentation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-038
    fact(
        "ccma-admin",
        "A patient requests an itemized billing statement. What is the appropriate first step?",
        "Follow office policy and route the request to billing or a supervisor",
        [
            "Refuse all financial questions categorically",
            "Provide another person's itemized charges",
            "Email the full chart unencrypted without consent",
        ],
        "Patients have rights to billing information within policy and law. Sharing another person's charges or unsecured records violates privacy.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-039
    fact(
        "ccma-admin",
        "The scanner queue shows two active charts for patients named Maria Lopez with the same date of birth but different medical record numbers. The medical assistant is indexing an outside referral PDF for the patient standing at the desk. Which step prevents a serious indexing error?",
        "Verify two patient identifiers against wristband or photo ID, then attach the scan to the matching chart",
        [
            "Match patient name and date of birth on the referral to the chart header, then attach",
            "Match the medical record number on the referral to the chart selected in the queue",
            "Ask the patient to confirm date of birth, then attach the scan to the open encounter",
        ],
        "Same-name patients are a high-risk scenario for misfiled documents. Two identifiers alone are insufficient when names and birth dates collide.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-admin-040
    fact(
        "ccma-admin",
        "Which data are required for many workers' compensation visits?",
        "Employer name, date of injury, and mechanism of injury when known",
        [
            "Employer name documented without date or mechanism of injury",
            "Verbal report without any charting",
            "Standard cosmetic procedure consent for elective surgery",
        ],
        "Occupational carriers need injury context to adjudicate claims. Incomplete injury details delay claim adjudication.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-041
    fact(
        "ccma-admin",
        "What does an electronic remittance advice (ERA) explain?",
        "How each claim line was paid, denied, or adjusted",
        [
            "Patient appointment reminders for the next week",
            "Annual staff performance rankings",
            "Vital sign flowsheet trends for the nursing unit",
        ],
        "ERAs drive payment posting and appeal decisions. Clinical flowsheet data are not claim adjudication tools.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-042
    fact(
        "ccma-admin",
        "What does days in accounts receivable measure?",
        "Average time between providing service and collecting payment",
        [
            "Number of patients seated in the waiting room",
            "Vaccine storage unit temperature",
            "Annual needlestick injury rate",
        ],
        "Days in A/R is a revenue cycle metric. Clinical safety indicators such as needlesticks are tracked separately.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-043
    fact(
        "ccma-admin",
        "A payer denies a claim for missing prior authorization. What should staff do first?",
        "Review the denial code and contract rules, then follow appeal or correction steps",
        [
            "Rebill the same claim without correcting the authorization issue",
            "Bill the patient for the entire charge without review",
            "Write off the balance without documenting the denial reason",
        ],
        "Denials require structured follow-up that may include retro authorization or appeal. Immediate full balance billing without review may violate policy.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-044
    fact(
        "ccma-admin",
        "Which action supports accurate charge capture after a visit?",
        "Select diagnosis and procedure codes that match documented services",
        [
            "Use the same code combination for every patient",
            "Choose codes based on highest payment regardless of documentation",
            "Leave diagnosis fields blank on every claim",
        ],
        "Coding must reflect the record to pass audits. Upcoding or blank diagnoses creates compliance and denial risk.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-045
    fact(
        "ccma-admin",
        "An insurance card shows a new group number after open enrollment. What should registration staff do?",
        "Update the EHR insurance profile and reverify eligibility for upcoming visits",
        [
            "Ignore the change until a claim is denied",
            "Apply the old group number to save time",
            "Store the card image without updating structured fields",
        ],
        "Stale insurance data produces rejections at clearinghouses. Structured updates plus eligibility checks catch benefit changes early.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-046
    fact(
        "ccma-admin",
        "A clinic adds a new self-pay policy for elective services. How should staff communicate costs?",
        "Provide written estimates per policy before nonurgent services when required",
        [
            "Quote random amounts verbally without documentation",
            "Refuse to discuss fees with any patient",
            "Collect the full charge at check-in without discussing the self-pay policy",
        ],
        "Transparent financial communication supports informed decisions. Public display of other balances violates privacy.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-047
    fact(
        "ccma-admin",
        "During end-of-day reconciliation, the day sheet total does not match the cash drawer. What is the best next step?",
        "Investigate discrepancies using receipts and EHR posting reports per policy",
        [
            "Adjust totals without documentation to match the drawer",
            "Discard the day sheet to avoid supervisor review",
            "Combine tomorrow's deposits without recounting",
        ],
        "Financial controls require tracing variances through documented transactions. Undocumented adjustments hide errors or theft.",
        [S.NHA_CCMA],
        "advanced",
    ),

    # ccma-admin-048
    fact(
        "ccma-admin",
        "What does a Current Procedural Terminology (CPT) code primarily describe on a claim?",
        "A procedure or service performed",
        ["A patient address",
        "A nursing diagnosis narrative",
        "A medication allergy"],
        "CPT codes report professional services and procedures. Diagnoses are coded with ICD-10-CM, which students sometimes swap on billing items.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-049
    fact(
        "ccma-admin",
        "When verifying insurance eligibility, what key detail confirms active coverage on the date of service?",
        "Payer response showing plan status and effective dates for the patient",
        ["A verbal promise from the patient",
        "The color of the insurance card",
        "Whether the patient parked in the clinic lot"],
        "Eligibility systems return structured benefit data tied to policy dates. Card appearance does not prove active enrollment.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-050
    fact(
        "ccma-admin",
        "What is a deductible in a commercial health plan?",
        "The amount the patient pays for covered services before the plan begins sharing cost",
        ["A fixed copay collected at every visit",
        "The clinic's wholesale supply budget",
        "A code describing surgical procedures"],
        "Deductibles are annual patient responsibility thresholds. Copays are per-visit amounts; CPT codes describe services, not plan design.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-051
    fact(
        "ccma-admin",
        "Why is accurate demographic data entry important at registration?",
        "It links results, bills, and correspondence to the correct individual",
        ["It allows sharing records with random callers",
        "It removes the need for patient identification later",
        "It guarantees clinical outcomes"],
        "Wrong demographics cause merged charts and misdirected PHI. Identification and clinical quality still require ongoing verification.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-052
    fact(
        "ccma-admin",
        "What does accounts receivable aging track?",
        "How long patient and payer balances have remained unpaid",
        ["Vaccine refrigerator temperature trends",
        "Employee vacation accrual",
        "Suture removal dates"],
        "AR aging supports collection workflows and cash flow analysis. Clinical device logs track different quality metrics.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-053
    fact(
        "ccma-admin",
        "A workers' compensation visit requires which registration detail?",
        "Employer name, injury date, and mechanism when known",
        ["Patient shoe size for billing",
        "Favorite television show",
        "Unrelated family member income"],
        "Occupational claims need injury context for adjusters. Personal preferences do not satisfy regulatory billing fields.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-054
    fact(
        "ccma-admin",
        "What is coordination of benefits when a patient has two insurance plans?",
        "Rules that determine which plan pays first",
        ["A method to duplicate payment for the same service",
        "A nursing diagnosis code",
        "A type of surgical consent"],
        "Primary and secondary payers follow contract order to avoid overpayment. It is not a clinical consent document.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-055
    fact(
        "ccma-admin",
        "When collecting a copayment, what receipt information helps the patient?",
        "Date, amount paid, and service location",
        ["Another patient's account number",
        "Staff home addresses",
        "Unrelated lab reference ranges"],
        "Copay receipts support personal records and secondary billing. Other patients' identifiers must not appear.",
        [S.NHA_CCMA],
        "beginner",
    ),
]
