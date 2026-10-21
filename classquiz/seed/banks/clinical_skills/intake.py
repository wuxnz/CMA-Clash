# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-intake)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-intake-001
    fact(
        "skill-intake",
        "Before beginning clinical intake tasks, how should the medical assistant verify patient identity?",
        "Match two identifiers per policy, such as legal name and date of birth",
        [
            "Use the exam room number on the door as the sole patient identifier",
            "Call the first name aloud in the waiting room to confirm identity",
            "Rely on a visitor's report of clothing color as sufficient verification",
        ],
        "Two-identifier matching reduces wrong-patient errors that affect orders and allergies. Room numbers change and public name calls do not uniquely identify the person receiving care.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-002
    fact(
        "skill-intake",
        "What does chief complaint documentation capture at the start of intake?",
        "The patient's stated primary reason for the visit in their own words",
        [
            "The billing diagnosis code selected at registration before the interview",
            "The insurance plan name and group number from the membership card",
            "A staff guess about the problem without asking the patient directly",
        ],
        "Chief complaint focuses the visit and guides history of present illness. Payer data and preselected codes are administrative and may not reflect the patient's concern today.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-003
    fact(
        "skill-intake",
        "How does review of systems (ROS) differ from the physical examination during intake?",
        "ROS records subjective symptoms by body system that the patient reports",
        [
            "ROS lists objective findings the clinician palpates during the exam",
            "ROS replaces medication reconciliation when the list was updated last year",
            "ROS documents prior surgical scars without asking about current symptoms",
        ],
        "ROS is a structured symptom inventory gathered from the patient. Examination findings and medication lists belong in separate parts of the record.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-004
    fact(
        "skill-intake",
        "What should allergy documentation at intake include when the patient reports a reaction?",
        "The allergen, type of reaction, and severity when known",
        [
            "A general allergy checkbox without naming the specific substance",
            "The medication class alone with no description of the reaction",
            "Allergies reported for a family member entered as the patient's own",
        ],
        "Reaction detail guides prescribing, contrast decisions, and emergency treatment. Blank or copied entries create risk of re-exposure.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-intake-005
    fact(
        "skill-intake",
        "When is it appropriate to document no known drug allergies (NKDA)?",
        "After the patient confirms no allergies or verified data support NKDA",
        [
            "Before staff ask any allergy screening questions at this clinic visit",
            "Because a chart from five years ago was not reviewed at check-in",
            "When the patient is in a hurry and skips the allergy interview",
        ],
        "NKDA is a clinical assertion that requires inquiry or reliable prior documentation. Defaulting without asking can hide true allergies from prescribers.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-006
    fact(
        "skill-intake",
        "Which elements belong in social history documentation when they affect patient care?",
        "Tobacco, alcohol or substance use, occupation, and support system",
        [
            "Portal login credentials used for online appointment self-scheduling",
            "Primary credit card numbers collected for same-day copay processing",
            "Waiting room television programs the patient watched before intake",
        ],
        "Social factors influence risk counseling, screening, and discharge planning. Payment card data belong in secure billing workflows, not the clinical social history.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-007
    fact(
        "skill-intake",
        "Why is the patient's preferred pharmacy recorded during intake?",
        "To route electronic prescriptions and answer refill access questions",
        [
            "To replace two-identifier patient verification at the start of the visit",
            "To determine ABO blood type without ordering laboratory testing",
            "To publish the pharmacy street address on the clinic's public website",
        ],
        "Pharmacy choice affects e-prescribing interfaces and patient access to medications. It does not establish identity or substitute for blood typing.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-008
    fact(
        "skill-intake",
        "What is the primary purpose of triage during intake in an urgent care setting?",
        "Prioritize by acuity and evaluate immediately when symptoms appear severe",
        [
            "Assign exam rooms strictly by arrival time without symptom screening",
            "Complete all billing entries before any brief safety assessment at triage",
            "Delay chest pain evaluation until every registration form is finished first",
        ],
        "Triage identifies emergencies such as unstable chest pain or stroke symptoms. First-come scheduling without acuity review can postpone critical care.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-009
    fact(
        "skill-intake",
        "Which triage finding should trigger immediate escalation according to typical protocols?",
        "Active chest pain with diaphoresis or shortness of breath",
        [
            "Mild seasonal rhinitis without fever or respiratory distress",
            "Stable hypertension refill for a patient without new symptoms",
            "Resolved cold symptoms needing a routine work excuse note",
        ],
        "Cardiopulmonary red flags need urgent provider awareness and monitoring. Stable chronic follow-up and minor illness are lower acuity when alarming symptoms are absent.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-010
    fact(
        "skill-intake",
        "When a patient has limited English proficiency, what is the appropriate communication approach?",
        "Use a qualified interpreter per policy instead of untrained family by default",
        [
            "Speak louder in English until the patient appears to understand questions",
            "Use a young child in the family as the default interpreter for consent",
            "Omit detailed procedure explanations to shorten the intake interview timeline",
        ],
        "Qualified interpretation supports accurate history, consent, and discharge teaching. Volume changes and ad hoc child interpreters do not meet communication standards.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-011
    fact(
        "skill-intake",
        "How should medication reconciliation be documented at intake?",
        "List Rx, OTC products, and supplements with doses and adherence when known",
        [
            "Record antibiotics taken ten years ago without noting current use",
            "Document vitamins the patient admires but denies taking regularly",
            "Leave the medication list blank for adults under thirty by local clinic habit",
        ],
        "Complete active medication data prevents interactions, duplication, and dosing errors. Age alone does not eliminate the need for a current therapy list.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-intake-012
    fact(
        "skill-intake",
        "What does history of present illness (HPI) describe compared with review of systems?",
        "Timeline and character of the chief complaint, such as onset and duration",
        [
            "Every body system whether or not the patient reports related symptoms",
            "Insurance authorization reference numbers for the scheduled visit",
            "Clinic staff break schedules and shift change times for the day on the unit",
        ],
        "HPI explores the presenting problem in depth, including modifying factors. ROS screens broadly across systems; authorization codes are billing metadata.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-013
    fact(
        "skill-intake",
        "Why should intake staff confirm the patient's phone number and mailing address?",
        "To deliver results, appointment reminders, and urgent clinical messages",
        [
            "To share contact details with unrelated vendors without patient consent",
            "To substitute contact data for documented medication allergy lists",
            "To list the home address on an unauthenticated public webpage",
        ],
        "Accurate contact information supports continuity and safety notifications. Demographics are protected health information and are not marketing lists.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-014
    fact(
        "skill-intake",
        "When should the Notice of Privacy Practices be addressed during intake?",
        "Offer the notice and document acknowledgment when required by policy",
        [
            "After staff disclose the diagnosis to a friend waiting in the lobby",
            "By displaying another patient's open chart at the front desk",
            "By waiving privacy rights verbally without providing the written notice",
        ],
        "Patients receive information about privacy rights at entry to care. Unauthorized disclosure before notice violates trust, policy, and HIPAA expectations.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-015
    fact(
        "skill-intake",
        "How should intake accommodate a patient with significant hearing loss?",
        "Offer assistive devices, written materials, or sign language interpreter help",
        [
            "Complete the interview from the hallway without face-to-face contact",
            "Assume the patient cannot participate in care and decline to room them",
            "Guess answers from appearance when the patient does not hear screening questions",
        ],
        "Reasonable accommodation supports accurate history and informed consent. Refusing interaction or guessing responses compromises care quality and dignity.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-016
    fact(
        "skill-intake",
        "What is appropriate documentation of tobacco use in social history?",
        "Type, amount, quit date or current use, and pack-years when policy requires",
        [
            "Label every patient a nonsmoker without asking any tobacco screening questions",
            "Record favorite brand names without documenting current use status",
            "Copy a relative's smoking history into the patient's social history",
        ],
        "Quantified tobacco data guides cessation counseling and cardiovascular risk assessment. Assumed nonsmoking status misrepresents exposure and missed teachable moments.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-017
    fact(
        "skill-intake",
        "Why document alcohol use in social history when it is clinically relevant?",
        "Use patterns affect medication choices, liver risk, and safety counseling",
        [
            "To rank personal character when assigning seats in the waiting room",
            "To replace measurement of vital signs at the beginning of the intake visit",
            "To defer allergy screening because alcohol use was already discussed",
        ],
        "Alcohol interacts with sedatives and contributes to liver injury and injury risk. It is a clinical risk factor, not a basis for seating or skipping allergy review.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-018
    fact(
        "skill-intake",
        "When a patient gives a long story at intake, how should chief complaint be documented?",
        "Summarize the primary concern briefly and confirm accuracy with the patient",
        [
            "Record unrelated childhood anecdotes as the sole chief complaint entry",
            "Select a random diagnosis code without asking what troubles them today",
            "Leave chief complaint blank because the patient's story exceeded a word limit",
        ],
        "Brief, confirmed summaries keep the record usable while respecting the patient's words. Empty fields or unrelated anecdotes break continuity for the evaluating clinician.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-019
    fact(
        "skill-intake",
        "A patient reports childhood penicillin allergy with hives but is uncertain. What intake documentation is best?",
        "Record penicillin, the reported reaction, and uncertainty for provider review",
        [
            "Remove the allergy from the chart because many years have passed since the event",
            "Document NKDA without asking about reactions to other medication classes",
            "Add all antibiotic classes as anaphylaxis without symptom details",
        ],
        "Uncertain history still warrants caution until the provider clarifies tolerance. Removing entries or labeling all classes as anaphylaxis without data is unsafe.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-intake-020
    fact(
        "skill-intake",
        "What should intake do when a walk-in patient has no photo identification?",
        "Follow policy for alternate verification and supervisor guidance as needed",
        [
            "Assign care to another patient in the waiting room with the same first name",
            "Create a chart using a fabricated date of birth to speed registration",
            "Refuse all clinical services without attempting policy-approved steps",
        ],
        "Policies balance access with safety through approved alternate identifiers. Fabricated demographics create permanent record errors and downstream treatment risk.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-021
    fact(
        "skill-intake",
        "When collecting family history at intake, which information is most clinically useful?",
        "Major illness in parents and siblings, such as heart disease or diabetes",
        [
            "Favorite sports teams followed by cousins on the maternal side",
            "Vaccination status of neighbors the patient knows in the community",
            "Vehicle license plate numbers for cars parked near the clinic entrance today",
        ],
        "Inherited risk patterns guide screening intervals and preventive counseling. Unrelated social or vehicle details do not change evidence-based prevention plans.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-022
    fact(
        "skill-intake",
        "How should staff handle a patient who refuses to answer social history questions?",
        "Document the refusal and complete other required intake steps per policy",
        [
            "Enter assumed tobacco and alcohol data so the form appears complete",
            "Dismiss the patient from the clinic for declining nonclinical questions",
            "Discuss the refusal on a staff group chat visible to nonclinical volunteers",
        ],
        "Refusal is clinically relevant documentation that the provider may need to interpret. Falsifying data or sharing refusals broadly violates ethics and privacy rules.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "intermediate",
    ),
    # skill-intake-023
    fact(
        "skill-intake",
        "What is a clinical purpose of asking about current occupation during social history?",
        "Identify work exposures, ergonomic strain, or need for work documentation",
        [
            "Calculate the patient's credit score before collecting the visit copayment",
            "Assign examination rooms based on employer logos on the patient's clothing",
            "Replace allergy screening because employment was documented elsewhere",
        ],
        "Job tasks influence respiratory, musculoskeletal, and return-to-work planning. Occupation does not substitute for medication allergy review or financial scoring.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-024
    fact(
        "skill-intake",
        "Which intake question helps distinguish emergent abdominal pain from lower-acuity complaints?",
        "Whether pain is severe, sudden, or paired with dizziness or vomiting blood",
        [
            "Whether the patient prefers generic medications over brand-name products",
            "Whether the vehicle is parked in the numbered space on the clinic lot",
            "Whether the patient watched television the night before without new symptoms",
        ],
        "Alarm features suggest surgical, vascular, or gastrointestinal emergencies needing rapid evaluation. Medication preferences and parking details do not assess peritoneal signs.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-025
    fact(
        "skill-intake",
        "A Spanish-speaking patient arrives while the bilingual medical assistant is busy. What is the best next step?",
        "Activate phone or video interpreter services per policy during the wait",
        [
            "Proceed with consent using improvised hand gestures for complex medical terms",
            "Ask another patient to translate private medical and social history",
            "Wait for the bilingual colleague without offering interpreter services",
        ],
        "Professional interpreters preserve confidentiality and accuracy for history and consent. Ad hoc translation by strangers or indefinite delay without services fails standards of care.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-026
    fact(
        "skill-intake",
        "How should intake document use of herbal or dietary supplements?",
        "Include product names on the medication or supplement list for the provider",
        [
            "Exclude them from the record because they are marketed as natural products",
            "List them under family history because relatives may use similar products",
            "Record them in billing comments without entering the clinical medication list",
        ],
        "Herbal products have pharmacologic effects and interaction potential. They belong with other current therapies the prescribing clinician must reconcile.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-027
    fact(
        "skill-intake",
        "Why confirm preferred language and interpreter needs at each new visit when policy requires?",
        "Language needs can change and affect consent and instruction comprehension",
        [
            "Charge an interpreter surcharge to the patient without prior written notice",
            "Use language preference instead of legal name during identity verification",
            "Display language preference on a lobby signboard visible to all visitors",
        ],
        "Reassessment prevents miscommunication during teaching, medication instructions, and discharge. Language data are part of the medical record, not public signage.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-028
    fact(
        "skill-intake",
        "What does documenting patient denies in review of systems indicate?",
        "The patient reports no symptoms in that system when asked directly",
        [
            "The staff member refuses to complete the ROS section on the form",
            "The physician performed surgery on that body system in the past year",
            "The insurance payer rejected the claim for the scheduled service",
        ],
        "Denies in ROS means a negative symptom review for that system. It is not staff refusal, procedural history, or payer claim status.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-029
    fact(
        "skill-intake",
        "When a patient lists several concerns at intake, how should documentation prioritize them?",
        "Record each concern and clarify which symptom is most bothersome today",
        [
            "Document the last complaint mentioned and discard earlier concerns",
            "Choose the complaint with the highest reimbursement diagnosis code today",
            "Tell the patient to book separate visits for each issue without triage",
        ],
        "Multiple active issues are common; prioritization guides the provider's focus and time. Billing codes alone do not set clinical urgency or safety sequencing.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-030
    fact(
        "skill-intake",
        "Which pharmacy detail at intake helps prevent prescription routing errors?",
        "Confirm pharmacy name, location, and mail-order versus retail preference",
        [
            "Record the dispensing pharmacist's personal cellphone without permission",
            "Select the pharmacy closest to the clinic regardless of patient preference",
            "Delete prior pharmacy entries from the chart without patient confirmation",
        ],
        "Matching the patient's chosen dispensing site reduces wrong-site fills and callback delays. Staff convenience or unverified contacts can misroute time-sensitive medications.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-031
    fact(
        "skill-intake",
        "The chart shows NKDA but the patient now reports lip swelling with sulfa antibiotics. What should the medical assistant do?",
        "Update allergy list with sulfa, reaction, chart flag, and provider notification",
        [
            "Add sulfa as drug intolerance pending provider review without a chart alert flag",
            "Document the reaction in HPI and leave structured allergies unchanged at NKDA",
            "Ask the patient to update allergies in the portal before the provider visit",
        ],
        "New allergy information overrides outdated NKDA entries and must appear in structured fields prescribers query. HPI-only notes, delayed portal updates, or passive intolerance entries can miss acute prescribing alerts.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-intake-032
    fact(
        "skill-intake",
        "What is the role of a brief screening tool such as PHQ-2 at intake?",
        "Detect behavioral symptoms that may need scored follow-up per protocol",
        [
            "Replace a full mental health evaluation by the licensed clinician entirely",
            "Post screening scores on a monitor in the waiting room for patient education",
            "Determine blood pressure cuff size based on the numeric screening result",
        ],
        "Screeners triage need for further assessment and tracking; they supplement clinical judgment. Scores are confidential health information, not vital sign equipment settings.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-033
    fact(
        "skill-intake",
        "How should living situation be captured in social history when it affects care planning?",
        "Note home safety, caregivers, and barriers like stairs or poor transport",
        [
            "Record landlord bank routing numbers for monthly rent payment transfers",
            "Document neighbors' names without a clinical discharge planning reason",
            "List interior wall paint colors observed during a prior home health visit",
        ],
        "Functional context affects discharge instructions, durable equipment, and referral needs. Unrelated financial or decorative details do not guide safe transitions.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-034
    fact(
        "skill-intake",
        "A patient with triaged emergent chest pain insists on finishing insurance paperwork first. What supports patient safety?",
        "Escort for immediate evaluation while registration completes insurance forms",
        [
            "Hold clinical evaluation until every insurance form is signed in full",
            "Ask the patient to return tomorrow when paperwork can be completed",
            "Direct the patient to wait in the retail pharmacy aisle until forms are done",
        ],
        "Emergent symptoms take precedence over administrative tasks that can follow stabilization. Delaying evaluation for paperwork increases risk of preventable harm.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-035
    fact(
        "skill-intake",
        "During intake, a patient asks whether their employer can read the visit note. What is an accurate response within MA scope?",
        "Explain PHI is shared under HIPAA and patient authorization rules",
        [
            "Promise the employer the full clinical note automatically after each visit",
            "State that anyone who knows the patient's name may access the chart",
            "Advise avoiding future medical care so employer-linked records cannot exist",
        ],
        "HIPAA limits disclosure without patient authorization except defined permitted uses. Employers do not receive visit notes by default, and chart access requires legal permissions.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-036
    fact(
        "skill-intake",
        "Which documentation approach supports a meaningful ROS when intake time is limited?",
        "Document pertinent ROS for the complaint and expand review as required",
        [
            "Copy ROS text from a different patient's chart with a similar age and sex",
            "Mark every body system positive to reduce screening questions during intake",
            "Leave ROS blank because the physician can infer symptoms without asking",
        ],
        "Focused ROS must remain truthful and relevant to the presenting problem. Template copying or fabricated positives create legal risk and mislead treatment decisions.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-037
    fact(
        "skill-intake",
        "A deaf patient requests a sign language interpreter and video connection will take five minutes. What should intake do meanwhile?",
        "Use written notes for urgent needs and defer full history to the interpreter",
        [
            "Complete surgical consent relying on lip reading alone in a noisy clinic",
            "Cancel the visit because a brief wait would exceed clinic efficiency targets",
            "Borrow another patient's interpreter slot without rescheduling either visit",
        ],
        "Brief waits for qualified services protect consent quality and accurate history. Lip reading alone is insufficient for complex discussions, and sharing interpreter time violates scheduling fairness.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-038
    fact(
        "skill-intake",
        "The patient admits taking a friend's opioid for back pain but has no prescription. How should intake capture this?",
        "Document opioid use in medication and social history and notify the provider",
        [
            "Omit the opioid because it was not prescribed by a licensed clinician of record",
            "List the friend as prescriber in the medication administration record",
            "Record the opioid under allergies instead of active substance use",
        ],
        "Nonprescribed opioid use affects safety, prescribing decisions, and substance use screening. Omitting active substances or miscoding them as allergies misrepresents risk.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-intake-039
    fact(
        "skill-intake",
        "Why should emergency contact information be confirmed at intake?",
        "Reach a designated person if the patient cannot participate in care decisions",
        [
            "Bill the emergency contact for all services without a financial agreement",
            "Add the contact as guarantor on the account without discussing responsibility",
            "Release the full medical record to the contact by default after each visit",
        ],
        "Emergency contacts support communication during crises when the patient is incapacitated. They are not automatic payers or recipients of protected health information.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-040
    fact(
        "skill-intake",
        "A returning patient has a new legal last name after marriage with matching photo ID and date of birth. What is essential?",
        "Verify identity with ID, update legal name, and link prior records per policy",
        [
            "Create a duplicate chart with a new medical record number for the new name",
            "Refuse service until the patient uses the previous legal name on all paperwork",
            "Merge charts with another patient sharing the new surname in the system",
        ],
        "Proper identity verification and record linkage preserve allergy, medication, and problem list continuity. Duplicate or incorrect merges cause treatment and billing errors.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "advanced",
    ),
    # skill-intake-041
    fact(
        "skill-intake",
        "What element should be included when closing the intake interview with the patient?",
        "Confirm next steps, follow-up timing, and whom to call if symptoms worsen",
        [
            "End abruptly while the patient is asking a question about prescribed medications",
            "Provide another patient's recent test results for comparison with their symptoms",
            "Discourage questions about the care plan to shorten room turnover time",
        ],
        "Clear closing instructions reduce callbacks and harm from delayed care when symptoms change. Other patients' results are confidential and must not be disclosed.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-042
    fact(
        "skill-intake",
        "An MA is told to room a patient with fever, rash, and recent international travel. What documentation priority applies?",
        "Document travel, exposure, and onset in HPI and flag isolation per protocol",
        [
            "Record footwear brand in demographics before documenting fever and rash",
            "Defer clinical documentation until the patient completes checkout at discharge",
            "Place travel history in billing comments without a clinical intake entry",
        ],
        "Travel and symptom timing guide communicable disease precautions and public health reporting. Infectious risk data belong in the clinical narrative the care team reads during the visit.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
]
