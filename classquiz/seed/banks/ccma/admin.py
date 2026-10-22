# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-admin)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-admin-001
        fact('ccma-admin', 'When should a medical office collect a patient copayment?', 'Collect the contracted copayment at the time of service', ['Bill the copayment after the annual deductible is met', 'Collect the copayment after the payer posts the remittance', 'Collect the copayment on the statement after the visit'], 'Copayments are fixed cost-sharing amounts defined in the benefit plan, and collecting at the visit matches most payer contracts. Billing after the deductible is met, collecting after the remittance posts, and deferring the amount to the statement all move the collection past the point of service.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-002
        fact('ccma-admin', 'Under which circumstance may a managed care plan require a referral?', 'The plan requires PCP approval before the specialist visit', ['The member pays cash for a self-pay preventive visit', 'The visit is a routine blood pressure recheck', 'The clinic operates in a service area outside the plan network'], 'Managed care referral rules come from the plan design, so a member whose plan requires primary care approval must have a referral before a specialist visit. Cash payment, a routine screening, and the location of the clinic do not create a referral requirement.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-003
    fact(
        "ccma-admin",
        "What information does a superbill or encounter form capture for billing staff?",
        "Diagnoses, procedures performed, and charges for the visit",
        [
            "Patient history, allergies, and the medication list",
            "Appointment times, room assignments, and daily provider hours",
            "Insurance plan limits, copay amounts, and deductibles",
        ],
        "A superbill converts the visit into codable charge data: diagnoses, procedures, and charges. History and medications, appointment logistics, and plan benefit amounts are recorded elsewhere in the chart and the payer record.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-004
        fact('ccma-admin', 'What does the accounts receivable ledger track for a medical practice?', 'Outstanding balances owed by patients and third-party payers', ['Cash collected at the front desk on the day of service', 'Revenue recorded in the general ledger at the end of each month', 'Supplies purchased and vendor invoices still unpaid'], 'Accounts receivable reflects revenue that is still due after a service has been billed, whether from the patient or from the payer. Cash at the front desk, general ledger revenue, and unpaid vendor invoices are different measures.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-005
    fact(
        "ccma-admin",
        "How are ICD-10-CM codes used on an insurance claim?",
        "They report the patient's diagnoses and reasons for the encounter",
        [
            "They report the procedures and services that the provider performed",
            "They list the supply items used during the visit",
            "They identify the member insurance plan for the claim",
        ],
        "Diagnosis codes establish why the patient needed the care, so they report the diagnoses and the reason for the encounter. Procedures, supply items, and plan identifiers belong in other fields and other code sets.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-006
        fact('ccma-admin', 'How should no-show appointments be handled in the electronic health record?', 'Document the missed visit so scheduling and outreach can follow up', ['Enter the visit as a completed encounter for billing', 'Remove the appointment from the schedule entirely', 'Ask the provider to write a progress note for the legal medical record'], 'A no-show is recorded in the scheduling record so access managers can see missed visits and reach out to the patient. Billing the visit as completed, deleting the appointment, and asking the provider for a progress note all fail to capture the missed visit in the schedule.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-007
        fact('ccma-admin', 'What is the primary legal role of the medical record?', 'It documents the care provided and supports continuity and review', ['It supplies the billing detail for every claim the practice submits to payers', 'It provides the schedule for follow-up visits', 'It tracks staff competency and annual training completion'], 'The medical record is the formal legal account of the care a patient received and supports continuity, review, and legal defense. Billing detail, follow-up scheduling, and staff competency records live in separate systems, and consent forms remain a separate legal document.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-008
        fact('ccma-admin', 'How is a copayment defined in most commercial insurance plans?', 'A fixed dollar amount the member pays for a covered service', ["The full billed charge before contractual adjustments are applied", "The amount the member owes before the plan shares the cost", "A quarterly premium the member pays to keep the plan active"], 'Copays are predetermined member responsibility for covered services. They differ from the total billed charge, they are not the deductible amount the member owes before benefits apply, and they are not the premium paid to hold coverage.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-009
    fact(
        "ccma-admin",
        "Which insurance card details should be verified when scanning into the EHR?",
        "Member identifier, group number, and coverage effective dates",
        [
            "Member identifier, group number, and the plan name shown on the card",
            "Member identifier, group number, and the policy year",
            "Member identifier, group number, and the copay amount",
        ],
        "Payers route claims using the member identifier and group number with the dates coverage takes effect. The plan name, the policy year, and the copay amount do not confirm that the member's coverage is currently active.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-010
        fact('ccma-admin', 'Why is insurance eligibility verification helpful when scheduling a new patient?', 'It confirms active coverage before services are provided', ['It tells the front desk which visit types the plan covers', 'It shortens the check-in interview for every patient', 'It gives the front desk the mailing address for claims'], 'Eligibility verification confirms that the member is covered and that benefits are active before the clinic renders and bills the service. Visit-type rules, a shorter check-in, and a mailing address are not what the payer eligibility transaction returns.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-011
        fact('ccma-admin', 'What is the goal of a practice compliance program?', 'Promote ethical coding, billing, and adherence to regulations', ['Maximize payer reimbursement for every service billed', 'Reduce the number of payer audits the practice receives each year', 'Lower the administrative cost of the billing cycle'], 'Compliance programs train staff and monitor coding and billing processes so the practice follows federal and state requirements. Higher reimbursement, fewer payer audits, and lower administrative cost are business outcomes that depend on compliant practice rather than the purpose of the program.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-012
    fact(
        "ccma-admin",
        "How does a superbill link clinical work to the revenue cycle?",
        "It maps services to diagnosis and procedure codes",
        [
            "It records the time each patient spent in the exam room",
            "It totals the day charges for the front desk drawer",
            "It tracks staff hours against daily patient volume",
        ],
        "Charge capture depends on accurate code linkage from the encounter, so the superbill maps each service to its diagnosis and procedure codes. Room time, daily charge totals, and staff hours are operational data that do not produce an insurable claim.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ccma-admin-013
        fact('ccma-admin', 'What is the focus of accounts receivable follow-up work?', 'Collecting or resolving unpaid patient and payer balances', ['Reviewing payer contract terms, fee schedules, and edits', 'Maintaining the patient demographic master record and audit log', 'Scheduling staff coverage at the front desk window'], 'Follow-up targets outstanding balances on statements and remittance advice so the practice collects the money it is owed. Contract terms, demographic records, and front desk staffing support the practice generally rather than collections work.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-014
        fact('ccma-admin', 'What do audit trails in billing modules record?', 'Who changed charges, payments, or adjustments, and when', ['The diagnosis and procedure codes selected for each visit', 'The number of days in accounts receivable each month', 'The clinical narrative written during the visit'], 'An audit log records each user action on a charge, payment, or adjustment so the billing history can be reviewed later. Selected diagnosis and procedure codes, receivable aging, and clinical notes live in other parts of the record.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-015
        fact('ccma-admin', 'What do Current Procedural Terminology (CPT) codes describe?', 'Health care professional services and procedures', ['Diagnoses and conditions treated during the encounter', 'Reference ranges for the vital signs recorded at triage', 'The laboratory equipment used to process the specimen'], 'CPT codes report the professional procedures and visits that were performed for billing and data. Diagnoses use ICD-10-CM, vital sign reference ranges are clinical norms, and laboratory equipment is not a billable code.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-016
        fact('ccma-admin', 'When does coordination of benefits apply?', 'More than one active health plan covers the patient', ['The patient has no insurance and pays cash at the time of service', 'The visit is limited to a routine vision hardware fitting', 'The patient has a single active plan that covers the visit'], 'Secondary and primary payers are identified when multiple policies exist, so each plan pays in contract order. Uninsured cash visits, vision-only fittings, and single-plan patients never create a coordination sequence.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-017
    fact(
        "ccma-admin",
        "How should front desk staff handle copayment collection?",
        "Collect the copayment and give the patient a receipt",
        [
            "Bill the copayment to the card on file after the visit",
            "Collect the copayment at the end of the visit instead",
            "Record the copayment as a patient balance to bill later",
        ],
        "Copayment collection follows the payer contract, and the patient receives a receipt for what was paid at check-in. Charging the card on file after the visit, collecting at the end of the visit, and billing the copayment later each move the collection away from point-of-service receipting.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-018
        fact('ccma-admin', 'What does a daily day sheet report typically summarize?', 'Charges posted, payments received, and adjustments', ['Appointments kept, missed, and rescheduled that day', 'Claims submitted, denied, and appealed that day', 'Inventory counts and purchase orders for the week'], 'Day sheets reconcile cash drawers and posting batches by summarizing the charges, payments, and adjustments posted that day. Appointment counts, claim status, and inventory counts come from the scheduling, billing, and supply reports.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-019
        fact('ccma-admin', 'Which data may appear on an electronic eligibility response?', 'Coverage status, plan name, and benefit highlights', ['Member cost sharing and benefit limits for the plan', 'The claim status for services billed last month', 'The diagnosis codes that will be billed for the visit'], 'Eligibility transactions return the benefit information permitted by the transaction, which includes coverage status, plan details, and cost sharing for the member on the date of the check. Claim status for prior services and the diagnosis codes for an upcoming visit come from other systems.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-020
        fact('ccma-admin', 'How does the HIPAA minimum necessary standard apply in the billing office?', 'Staff should access the least PHI needed for the billing task', ['Every field of the chart may be sent to the clearinghouse', 'Staff may open the full chart whenever a patient calls the office', 'Notes may be shared with a vendor that requests them'], 'Minimum necessary limits staff to the protected health information the billing task actually requires. Sending whole charts, opening a full chart for a phone call, and sharing notes with any requesting vendor all exceed the standard.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'advanced'),

    # ccma-admin-021
        fact('ccma-admin', 'What is the purpose of ICD-10-CM diagnosis coding on a claim?', 'Communicate why the patient was seen and justify medical necessity', ['Report the procedure performed with the appropriate CPT code', 'Document the sequence of the specimen draws for the laboratory work', 'Record the EKG electrode placement that was used during the visit'], 'Diagnosis codes tell the payer why the patient needed the service and support medical necessity. Procedure coding uses CPT, specimen sequence belongs in laboratory documentation, and EKG electrode placement is a procedural detail in the clinical record.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-022
    fact(
        "ccma-admin",
        "Who determines how long medical records must be retained?",
        "Federal and state law, accreditation standards, and policy",
        [
            "The clinical team leader for each service line in the practice",
            "The vendor that stores the records off site",
            "The payer, based on its own contract terms",
        ],
        "Retention schedules are governed by legal and accreditation rules plus organizational policy. Department leaders, storage vendors, and payers do not set how long the practice keeps a record.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-admin-023
        fact('ccma-admin', 'When should CPT modifiers be appended to a claim line?', 'When payer rules require clarification of how a service was performed', ['When the claim needs a different code for the same service performed', 'When the diagnosis code does not match the procedure code that was billed', 'When the payer requires a modifier on every submitted line'], 'A modifier adds the detail a payer needs about how a procedure was performed, such as a bilateral service. Changing the code, changing the diagnosis, and adding a modifier to every line misstate the claim rather than clarify it.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-024
        fact('ccma-admin', 'What does prior authorization indicate for a scheduled service?', 'Payer approval must be obtained before the procedure or test', ['The service is guaranteed coverage with no patient cost sharing', 'The payer has already paid the clinic for the planned service', 'A referral to a specialist is required instead of payer approval'], 'Prior authorization is the payer requirement that approval be obtained before a covered procedure or test is performed, so the claim is not denied. Guaranteed coverage, payment already made, and a specialist referral are separate situations.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-025
        fact('ccma-admin', 'What registration steps are important when enrolling a minor patient?', 'Verify guardian identity and consent or custody authority', ['The minor age and the reason for the visit', 'The parent insurance card and the amount of the copay due', 'A signed authorization letter from the school nurse'], 'A minor is registered with the parent or legal guardian, and staff confirm who may consent and who is responsible for the bill. The minor age and visit reason, the insurance card and copay, and a school authorization do not establish consent or custody authority.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-026
        fact('ccma-admin', 'What risk can occur if providers are double-booked without a written scheduling policy?', 'Visit time and patient access suffer, leading to dissatisfaction', ['Staff overtime costs rise for the provider and the front desk team', 'Charting is pushed into the next day for the late encounters', 'The provider works past the end of the clinic day'], 'Overbooking without controls shortens the contact time available for each patient and reduces access, which shows up as dissatisfaction and longer waits. Staff overtime, next-day charting, and a provider working past the end of the clinic day are side effects of the same problem.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-027
        fact('ccma-admin', 'How do scheduling templates benefit an outpatient practice?', 'They align appointment types with provider time and room resources', ['They set the charges that will be billed for each visit type', 'They document the clinical findings for each scheduled patient', 'They track staff certification and credential renewal dates each year'], 'Templates balance acute, preventive, and procedure visits by assigning each appointment type a length and a slot that fits provider and room capacity. Charge amounts, clinical findings, and credential dates are handled in billing, the chart, and human resources.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-028
    fact(
        "ccma-admin",
        "What must telehealth intake documentation include?",
        "Patient location, consent to virtual care, and modality used",
        [
            "Chief complaint and the insurance eligibility for the visit",
            "The reason the visit was scheduled as virtual care instead of in person",
            "The number of minutes the patient waited to connect",
        ],
        "Payers and regulators expect the patient location, consent to virtual care, and the modality used for a telehealth encounter. The chief complaint with eligibility, the reason the visit was virtual, and the connection wait time do not replace those elements.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-029
        fact('ccma-admin', 'For which type of claim is the CMS-1500 form commonly used?', 'Professional services provided in outpatient settings', ['Inpatient facility charges billed on the UB-04 institutional claim', 'Outpatient hospital facility claims submitted on the UB-04 form', 'Charges billed to a patient directly with no payer claim'], 'CMS-1500 is the standard professional claim form in many ambulatory settings, while the UB-04 carries institutional facility charges for inpatient and outpatient hospital services. Amounts billed straight to a patient with no payer claim are self-pay transactions, not a claim form.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-030
    fact(
        "ccma-admin",
        "An attorney's office faxes a records request for a current patient. The cover sheet shows firm letterhead and a HIPAA authorization, but the printed patient name is one letter different from the chart while date of birth matches. What should staff do before releasing information?",
        "Hold the request and verify patient identity before releasing records",
        [
            "Ask the attorney to resend the authorization with a corrected patient name",
            "Release the records because the date of birth matches the chart",
            "Call the patient to confirm the request and release records on verbal approval",
        ],
        "Valid disclosure requires a correct authorization tied to the right individual. Similar names and partial identifiers are a common source of misdirected PHI.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # ccma-admin-031
        fact('ccma-admin', 'What does a signed release of information (ROI) form authorize?', 'Disclosure of specified health information to named recipients', ['Disclosure of the entire chart to a caller who knows the patient name', 'Use of the record for unrelated marketing purposes', 'Transfer of the record to an agency that requests it'], 'ROI forms define who may receive which records and for what purpose. Releasing the whole chart to a caller, using the data for marketing, and transferring the record to any requesting agency all go beyond what the patient authorized.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'intermediate'),

    # ccma-admin-032
        fact(
        "ccma-admin",
        "Under CLIA, what characterizes a waived laboratory test?",
        "It is simple and carries a low risk of an erroneous result",
        [
            "It needs the same daily quality control as high-complexity chemistry",
            "It requires certification by a clinical pathologist",
            "It carries no reporting requirement to the state health department",
        ],
        "FDA classifies a test as waived when it is simple and carries a low risk of an erroneous result, but CLIA still requires controlled procedures, personnel competency, and manufacturer directions. Full high-complexity quality control, pathologist-only certification, and no state reporting requirement describe other laboratory categories.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-admin-033
    fact(
        "ccma-admin",
        "When should verification of benefits be performed for a scheduled procedure?",
        "Before the service or at the time of service",
        [
            "After the payer denies the claim and the patient is billed",
            "During the annual enrollment period in the fall",
            "At the close of the monthly billing cycle",
        ],
        "Timely benefit verification clarifies coverage and cost sharing before the service is rendered, so surprises can be discussed with the patient. Verifying after a denial, during open enrollment, and at the end of the billing cycle all happen too late to help.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-034
        fact('ccma-admin', 'Which practices support safe clinic supply inventory control?', 'Set par levels, monitor expiration dates, and store items securely', ['Set par levels and reorder points for each stocked item', 'Monitor expiration dates and record the lot numbers', 'Track the storage temperature of refrigerated vaccines and biologics'], 'Inventory control prevents waste and safety events. Reorder points without expiration checks, lot tracking on its own, and cold chain monitoring each cover only part of the control.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-035
        fact('ccma-admin', 'What is prior authorization in the revenue cycle?', 'Payer review and approval before selected services are covered', ['A benefits check that confirms the patient is covered for the date', 'A referral from the primary care provider to a specialist', 'A patient financial agreement for monthly balances'], 'Many plans mandate authorization for high-cost imaging or specialty drugs, so the practice obtains payer approval before the service is rendered. A benefits check, a specialist referral, and a payment agreement are separate revenue cycle steps and do not substitute for authorization.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-036
        fact('ccma-admin', 'Which demographic updates should be confirmed at registration?', 'Legal name, address, contacts, insurance, and preferences', ['Legal name, address, and contact details confirmed with the patient', 'Insurance coverage and the preferred communication method', 'The reason for the visit and the referring provider'], 'Registration confirms the legal name, address, contact details, insurance, and communication preferences so claims and messages reach the right person. Each of those elements is verified on its own, and the reason for the visit and the referring provider belong in the encounter note.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-037
        fact('ccma-admin', 'What should telephone triage documentation record?', 'Caller identity, symptoms, advice, and follow-up instructions', ['The caller name, the chief complaint, and the visit that was booked', 'The billing code that will be used for the patient encounter', 'The insurance plan and the copay collected for the visit'], 'Triage notes create a legal record of the call, so they capture who called, the symptoms described, the advice given, and the follow-up plan. The visit that was booked, the billing code, and the insurance details belong in the scheduling and billing records.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-038
    fact(
        "ccma-admin",
        "A patient requests an itemized billing statement. What is the appropriate first step?",
        "Follow office policy and route the request to billing",
        [
            "Give the patient the balance and the payment options",
            "Send the itemized statement with the next billing cycle",
            "Deny the request because it is not a medical question",
        ],
        "Patients have rights to billing information within policy and law, so the first step is to follow office policy and route the request to billing. Sharing the balance directly, sending the statement later, and denying the request all fall outside the documented process.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-039
    fact(
        "ccma-admin",
        "The scanner queue shows two active charts for patients named Maria Lopez with the same date of birth but different medical record numbers. The medical assistant is indexing an outside referral PDF for the patient standing at the desk. Which step prevents a serious indexing error?",
        "Verify two identifiers against wristband or photo ID, then attach",
        [
            "Match patient name and date of birth on the referral to the chart header",
            "Match the medical record number on the referral to the chart in the queue",
            "Ask the patient to confirm date of birth, then attach to the open encounter",
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
            "The claim number and the adjuster contact at the carrier",
            "The name of the employer and the date of the injury",
            "The employee job title and the department where the injury occurred",
        ],
        "Occupational carriers need injury context to adjudicate claims. The claim and adjuster details route the claim, the employer and injury date alone leave out the mechanism, and the job title and department describe the workplace rather than the injury.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-admin-041
    fact(
        "ccma-admin",
        "What does an electronic remittance advice (ERA) explain?",
        "How each claim line was paid, denied, or adjusted",
        [
            "How much the practice collected that day from patients",
            "Which patients are due for a preventive visit next month",
            "Which appointment slots remain open in the schedule",
        ],
        "ERAs drive payment posting and appeal decisions by showing how the payer adjudicated each claim line. Cash collected at the front desk, preventive visit lists, and open appointment slots come from other systems.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ccma-admin-042
        fact('ccma-admin', 'What does days in accounts receivable measure?', 'Average time between service and collecting payment', ['The average number of claims posted each business day', 'The average balance left on unpaid patient statements', 'The percentage of charges collected within thirty days'], 'Days in accounts receivable is a revenue cycle metric that tracks the average time between providing a service and collecting the payment. Claims posted per day, the average unpaid balance, and collection rate within thirty days are related but different measurements.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-043
        fact('ccma-admin', 'A payer denies a claim for missing prior authorization. What should staff do first?', 'Review the denial code and contract rules, then appeal', ['Request retrospective authorization and then file the appeal', 'Call the payer for the appeal timeframe and required documents', 'Send the patient a statement for the full amount of the charge'], 'Denials require structured follow-up, so the first step is to read the denial code against the payer contract and then use the appeal steps. Requesting retroactive authorization, calling for the appeal timeframe, and billing the patient first all skip the review that determines the correct path.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-044
        fact('ccma-admin', 'Which action supports accurate charge capture after a visit?', 'Select diagnosis and procedure codes that match documented services', ['Review the encounter note before selecting the diagnosis and codes', 'Submit the claim with the diagnosis field left blank', 'Add the modifier that produces the highest payment on the claim line'], 'Coding must reflect the record to pass audits. Reviewing the encounter note before selecting codes and choosing codes that match the documented services both support accurate capture, while a blank diagnosis field or the modifier that pays most misstates the claim.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-045
    fact(
        "ccma-admin",
        "An insurance card shows a new group number after open enrollment. What should registration staff do?",
        "Update the EHR insurance profile and reverify eligibility",
        [
            "Verify the new group number against the eligibility response",
            "Keep the old group number until the payer rejects a claim",
            "Send the new card image to the billing office by email",
        ],
        "Stale insurance data produces rejections at clearinghouses, so staff should update the structured insurance fields and reverify eligibility. Keeping the old group number until a claim fails or emailing the card image to billing leaves the record wrong for every claim in between.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ccma-admin-046
        fact('ccma-admin', 'A clinic adds a new self-pay policy for elective services. How should staff communicate costs?', 'Provide written estimates before nonurgent services', ['Discuss the fee schedule with the patient before the service', 'Collect the full amount at check-in without an estimate', 'Wait until the bill arrives for the patient to review'], 'Transparent financial communication supports informed decisions, so staff give the patient a written estimate before a nonurgent service. A verbal discussion, taking the full amount at check-in, and waiting for the bill all leave the patient without the cost information beforehand.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-047
        fact('ccma-admin', 'During end-of-day reconciliation, the day sheet total does not match the cash drawer. What is the best next step?', 'Investigate discrepancies using receipts and posting reports', ['Recount the drawer and compare it with the deposit slip and receipts', 'Post the difference to the next business day deposit', 'Ask the staff at the register what they think happened'], 'Financial controls require tracing variances through documented transactions, so staff recount the drawer and compare it with receipts and posting reports. Adjusting the total, moving the difference to the next deposit, and asking staff what happened all bypass the documentation.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-048
        fact('ccma-admin', 'On an insurance claim, what does a Current Procedural Terminology (CPT) code describe?', 'A procedure or service performed during the encounter', ['The diagnosis that explains why the patient was seen', 'The insurance plan that covers the patient on that date', 'The supplies and medications given during the visit'], 'CPT codes report the professional procedures and services performed for the encounter. Diagnoses are coded with ICD-10-CM, and plan identifiers, supplies, and medications are not procedure codes.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-049
        fact('ccma-admin', 'When verifying insurance eligibility before a visit, which response element best confirms active coverage?', 'Payer data showing plan status and effective dates for the member', ['The plan name and the member identifier printed on the insurance card', 'The plan year printed on the card at the top of the panel', 'A verbal assurance from the patient that coverage is current'], 'Eligibility systems return structured benefit data tied to policy dates, and that payer response is what confirms active enrollment. The plan name, the plan year, and a verbal assurance from the patient do not prove the coverage is currently active.', [S.NHA_CCMA], 'advanced'),

    # ccma-admin-050
        fact('ccma-admin', 'What is a deductible in a commercial health plan?', 'The amount the patient pays before the plan shares cost', ["A fixed copay collected at every visit regardless of benefit design", "A yearly premium the member pays to keep the plan active", "The member share of a covered claim after the deductible is met"], 'Deductibles are annual patient responsibility thresholds that must be met before the plan shares cost. Copays are per-visit amounts, premiums keep coverage active, and the member share after the deductible is the portion the plan does not pay.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-051
        fact('ccma-admin', 'Why is accurate demographic data entry important at registration?', 'It links results, bills, and correspondence to the correct person', ['It reduces claim rejections caused by mismatched plan details', 'It keeps two patients with similar names from merging into one chart', 'It satisfies the payer requirement for member identification'], 'Accurate demographics at registration keep results, bills, and correspondence attached to the correct person, which prevents merged charts and misdirected health information. Meeting payer identification requirements follows from that accuracy, but patient safety is the reason to enter it carefully.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-052
        fact('ccma-admin', 'What does accounts receivable aging track?', 'How long patient and payer balances stayed unpaid', ['Which payers have the slowest reimbursement turnaround', 'The dollar value of each balance still outstanding', 'The number of claims submitted to each payer last month'], 'AR aging supports collection workflows and cash flow analysis by showing how long each balance has been outstanding. Payer reimbursement turnaround, the dollar value of balances, and monthly claim volume are different operational metrics.', [S.NHA_CCMA], 'beginner'),

    # ccma-admin-053
        fact('ccma-admin', "A workers' compensation visit requires which registration detail?", 'Employer name, injury date, and mechanism when known', ['The claim number and the adjuster contact at the carrier', 'The member insurance card and the copay for the visit', 'The name of the supervisor who witnessed the incident'], 'Occupational claims need injury context for adjusters, so registration records the employer, the injury date, and the mechanism when it is known. The adjuster contact, the member copay, and the name of a witness support processing but are not the required injury detail.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-054
        fact('ccma-admin', 'What is coordination of benefits when a patient has two insurance plans?', 'Rules that determine which plan pays first', ['The agreement that lets both plans pay the full claim', 'The process for collecting the balance from the patient', 'The review that confirms medical necessity for the service'], 'Primary and secondary payers follow contract order to avoid overpayment, so coordination of benefits sets which plan pays first. Paying both plans in full, collecting a patient balance, and confirming medical necessity are separate processes.', [S.NHA_CCMA], 'intermediate'),

    # ccma-admin-055
        fact('ccma-admin', 'When collecting a copayment, what receipt information helps the patient?', 'Date, amount paid, and service location', ['The amount paid and the balance still due', 'The member name and the insurance plan identifier', 'The copay amount and the next scheduled appointment'], "Copay receipts support personal records and secondary billing, so they show the date, the amount paid, and the service location. The remaining balance, the member and plan identifiers, and the next appointment are not receipt details.", [S.NHA_CCMA], 'beginner'),

]
