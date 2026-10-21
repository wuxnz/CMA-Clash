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
        "Before any clinical task at intake, how should patient identity be verified?",
        "Use at least two patient identifiers per facility policy, such as name and date of birth",
        [
            "Room number posted on the door",
            "First name spoken across the waiting room",
            "Clothing color described by another visitor",
        ],
        "Two-identifier matching reduces wrong-patient errors. Room numbers and public name calls do not uniquely identify the person receiving care.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-002
    fact(
        "skill-intake",
        "What is the chief complaint in an intake interview?",
        "The patient's stated primary reason for the visit in their own words when possible",
        [
            "The billing diagnosis code selected by registration",
            "The insurance plan name on the card",
            "The medical assistant's guess without asking the patient",
        ],
        "Chief complaint focuses the visit and guides the history of present illness. Diagnosis codes and payer information are administrative, not the patient's concern.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-003
    fact(
        "skill-intake",
        "How does review of systems (ROS) differ from the physical examination?",
        "ROS records subjective symptoms by body system that the patient reports",
        [
            "ROS lists objective findings the clinician palpates",
            "ROS replaces medication reconciliation",
            "ROS documents parking and visitor preferences",
        ],
        "ROS is a structured symptom inventory. Exam findings and medication lists belong in separate sections of the record.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-004
    fact(
        "skill-intake",
        "What should allergy documentation include at intake?",
        "The allergen, type of reaction, and severity when known",
        [
            "A check mark with no substance named",
            "Drug class without any reaction description",
            "Family member allergies copied as the patient's",
        ],
        "Reaction detail guides future prescribing and emergency care. Blank or assumed entries create re-exposure risk.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-intake-005
    fact(
        "skill-intake",
        "When may \"no known drug allergies\" (NKDA) be documented?",
        "After the patient confirms no known drug allergies or the record is updated with verified information",
        [
            "Before any allergy question is asked",
            "Because the chart from five years ago was not reviewed",
            "When the patient is too busy to answer",
        ],
        "NKDA is a clinical assertion that requires inquiry or verified prior documentation. Defaulting without asking hides true allergies.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-006
    fact(
        "skill-intake",
        "Which elements belong in social history documentation when relevant to care?",
        "Tobacco, alcohol or substance use, occupation, and support system",
        [
            "Social media passwords for portal access",
            "Credit card numbers for copay collection",
            "Unrelated celebrity gossip",
        ],
        "Social factors influence risk counseling and follow-up planning. Financial card data belong in secure payment workflows, not the social history note.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-007
    fact(
        "skill-intake",
        "Why is the preferred pharmacy recorded during intake?",
        "To route electronic prescriptions and support medication access questions",
        [
            "To replace two-identifier patient verification",
            "To determine blood type without testing",
            "To publish the patient's address online",
        ],
        "Pharmacy choice affects e-prescribing and refill logistics. It does not establish identity or laboratory results.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-008
    fact(
        "skill-intake",
        "What is the primary purpose of triage during intake in an urgent care setting?",
        "To prioritize patients by acuity and direct immediate evaluation when symptoms are severe",
        [
            "To assign exam rooms by arrival time without symptom review",
            "To complete billing before any safety screening",
            "To discourage patients with chest pain from waiting",
        ],
        "Triage identifies emergencies such as unstable chest pain or stroke symptoms. Time of arrival alone can delay critical care.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-009
    fact(
        "skill-intake",
        "Which finding during intake triage should prompt immediate escalation per protocol?",
        "Active chest pain with diaphoresis or shortness of breath",
        [
            "Mild seasonal rhinitis without fever",
            "Routine prescription refill for stable hypertension",
            "Need for work excuse after resolved cold",
        ],
        "Cardiopulmonary red flags need urgent provider awareness. Stable chronic care and minor illness are lower acuity when symptoms are absent.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-010
    fact(
        "skill-intake",
        "When a patient has limited English proficiency, what is the appropriate communication step?",
        "Use a qualified interpreter per policy, not untrained family unless the patient declines offered services",
        [
            "Speak louder in English until understood",
            "Use a child family member as default interpreter for consent",
            "Omit procedure explanations to save time",
        ],
        "Qualified interpretation supports accurate history and informed consent. Raising volume or relying on minors does not meet communication standards.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-011
    fact(
        "skill-intake",
        "How should medication reconciliation at intake be documented?",
        "List prescription drugs, over-the-counter products, and supplements with doses and adherence when known",
        [
            "Record antibiotics the patient took ten years ago without context",
            "Document vitamins the patient likes but denies taking",
            "Leave the medication list blank for adults under 30",
        ],
        "Complete active medication data prevents interactions and duplication. Age alone does not eliminate the need for a current list.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-intake-012
    fact(
        "skill-intake",
        "What does history of present illness (HPI) describe compared with ROS?",
        "The timeline and character of the chief complaint, such as onset, duration, and modifying factors",
        [
            "Every body system whether or not symptoms exist",
            "Insurance authorization numbers",
            "Staff break schedules",
        ],
        "HPI explores the presenting problem in depth. ROS screens broadly; authorization codes are billing metadata.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-013
    fact(
        "skill-intake",
        "Why should intake staff confirm contact phone and address?",
        "To reach the patient with results, appointments, and urgent messages",
        [
            "To share the number with unrelated vendors without consent",
            "To replace clinical allergy documentation",
            "To post the address on a public website",
        ],
        "Accurate contact data supports continuity and safety notifications. Demographics are protected health information.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-014
    fact(
        "skill-intake",
        "When should the HIPAA Notice of Privacy Practices be addressed at intake?",
        "Per facility policy, such as offering the notice and documenting acknowledgment when required",
        [
            "After disclosing the patient's diagnosis to a friend in the lobby",
            "By posting another patient's chart at the front desk",
            "By waiving all privacy rights without discussion",
        ],
        "Patients receive information about privacy rights at entry to care. Unauthorized disclosure before notice violates trust and policy.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-015
    fact(
        "skill-intake",
        "How should a patient with hearing impairment be accommodated during intake questioning?",
        "Offer assistive devices, written materials, or sign language interpreter services per policy",
        [
            "Complete the interview from the hallway without eye contact",
            "Assume inability to understand and refuse care",
            "Rely on guessing answers from appearance",
        ],
        "Reasonable accommodation supports accurate history. Refusing interaction or guessing responses compromises care quality.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-016
    fact(
        "skill-intake",
        "What is an appropriate way to document tobacco use in social history?",
        "Type, amount, and quit date or current use with pack-year estimate when policy requires",
        [
            "Label every patient as a nonsmoker",
            "Record brand preference without use status",
            "Copy a relative's smoking history",
        ],
        "Quantified tobacco data guides cessation counseling and risk scores. Assumed nonsmoking status misrepresents exposure.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-017
    fact(
        "skill-intake",
        "Why document alcohol use in social history when clinically relevant?",
        "Patterns of use affect medication choices, liver risk, and safety counseling",
        [
            "To judge personal character for waiting room seating",
            "To replace vital sign measurement",
            "To determine shoe size for gait training",
        ],
        "Alcohol interacts with sedatives and contributes to organ injury. It is a clinical risk factor, not a social ranking tool.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-018
    fact(
        "skill-intake",
        "Which action supports accurate chief complaint documentation for a patient who gives a long narrative?",
        "Summarize the primary concern in brief terms and confirm accuracy with the patient",
        [
            "Record unrelated childhood stories as the chief complaint",
            "Select a random ICD code without patient input",
            "Leave the field empty because the story was long",
        ],
        "Brief, confirmed summaries keep the record usable while respecting the patient's words. Empty or random entries break continuity of care.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-019
    fact(
        "skill-intake",
        "A patient reports penicillin allergy with hives as a child but is unsure. What intake documentation is best?",
        "Record penicillin allergy with reported reaction and note uncertainty pending provider review",
        [
            "Delete the allergy because it was years ago",
            "Mark NKDA without asking about other drugs",
            "Add every antibiotic class as anaphylaxis without symptoms",
        ],
        "Uncertain history still warrants caution until clarified. Removing entries or blanket anaphylaxis labels without data are unsafe.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-intake-020
    fact(
        "skill-intake",
        "What should be verified when a walk-in patient states they have no identification?",
        "Follow facility policy for identity verification, such as photo ID alternatives and supervisor guidance",
        [
            "Assign care to another waiting patient with the same first name",
            "Create a chart with a fabricated date of birth",
            "Refuse all care without attempting policy-approved steps",
        ],
        "Policies balance access with safety through approved alternate identifiers. Fabricated demographics create permanent record errors.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-021
    fact(
        "skill-intake",
        "When collecting family history at intake, what information is most useful clinically?",
        "First-degree relatives' major conditions such as heart disease, diabetes, or cancer",
        [
            "Cousins' favorite sports teams",
            "Neighbors' vaccination status",
            "Parking permit numbers",
        ],
        "Inherited risk patterns guide screening intervals. Unrelated social details do not change preventive care plans.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-022
    fact(
        "skill-intake",
        "How should intake staff handle a patient who refuses to answer social history questions?",
        "Document the refusal and complete other required intake elements per policy",
        [
            "Enter false tobacco and alcohol data to finish the form",
            "Dismiss the patient from the clinic immediately",
            "Share the refusal on social media",
        ],
        "Refusal is itself clinically relevant documentation. Falsifying data or public disclosure violates ethics and privacy rules.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "intermediate",
    ),
    # skill-intake-023
    fact(
        "skill-intake",
        "What is the purpose of asking about current occupation during social history?",
        "To identify work-related exposures, ergonomic risks, or need for work documentation",
        [
            "To determine the patient's credit score",
            "To assign exam rooms by employer logo",
            "To replace allergy screening",
        ],
        "Job tasks influence respiratory, musculoskeletal, and return-to-work planning. Occupation does not substitute for medication allergy review.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-024
    fact(
        "skill-intake",
        "Which triage question helps separate emergent abdominal pain from lower-acuity complaints?",
        "Whether pain is severe, sudden, or accompanied by dizziness, vomiting blood, or rigid abdomen",
        [
            "Whether the patient prefers generic medications",
            "Whether they parked in the correct space",
            "Whether they watched television last night",
        ],
        "Alarm features suggest surgical or vascular emergencies. Parking and entertainment choices do not assess peritoneal signs.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-025
    fact(
        "skill-intake",
        "A Spanish-speaking patient arrives for intake and the bilingual MA is with another patient. What is the best next step?",
        "Activate telephone or video qualified interpreter services while the patient waits per policy",
        [
            "Proceed with complex consent using hand gestures alone",
            "Ask another waiting patient to translate private history",
            "Delay all care until the relative MA is free without offering interpreter",
        ],
        "Professional interpreters preserve confidentiality and accuracy. Ad hoc translation by strangers or prolonged delay without services fails standards.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-026
    fact(
        "skill-intake",
        "How should intake document use of herbal supplements?",
        "Include product names in the medication or supplement list because they may interact with prescribed drugs",
        [
            "Exclude them because they are natural",
            "List them under family history",
            "Record them in billing comments without the clinical record",
        ],
        "Herbal products have pharmacologic effects and interaction potential. They belong with other current therapies the provider must review.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-027
    fact(
        "skill-intake",
        "Why confirm preferred language and need for interpreter on every new visit when policy requires?",
        "Language needs can change and affect understanding of instructions and consent",
        [
            "To charge an interpreter fee to the patient without notice",
            "To replace legal name verification",
            "To publish language preference on a public board",
        ],
        "Reassessment prevents miscommunication during teaching and discharge. Language data are part of the medical record, not public signage.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-028
    fact(
        "skill-intake",
        "What does documenting \"patient denies\" in ROS indicate?",
        "The patient reports no symptoms in that system when asked",
        [
            "The staff member refuses to ask questions",
            "The physician already performed surgery there",
            "Insurance denied the claim",
        ],
        "Denies in ROS means negative symptom review. It is not staff refusal, procedural history, or payer status.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-029
    fact(
        "skill-intake",
        "When a patient lists multiple complaints, how should intake prioritize documentation?",
        "Record each concern and clarify which symptom is most bothersome today",
        [
            "Document the last complaint mentioned and discard the rest",
            "Choose the complaint with the highest reimbursement code",
            "Tell the patient to return for one symptom per visit without assessment",
        ],
        "Multiple active issues are common; prioritization guides the provider's focus. Billing codes alone do not set clinical priority.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-030
    fact(
        "skill-intake",
        "Which pharmacy detail helps prevent prescription errors at discharge?",
        "Confirming the pharmacy name, location, and whether the patient uses mail order or retail",
        [
            "Recording the pharmacist's personal phone without consent",
            "Selecting a pharmacy the staff prefers",
            "Deleting prior pharmacy entries without patient confirmation",
        ],
        "Matching the patient's chosen site reduces wrong-site dispensing. Staff preference or unverified contact data can misroute medications.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-031
    fact(
        "skill-intake",
        "An intake form shows NKDA but the patient now reports lip swelling with sulfa drugs. What should the medical assistant do?",
        "Update the allergy list with sulfa and reaction, flag the chart, and inform the provider",
        [
            "Keep NKDA because the form was signed last year",
            "Add sulfa under social history as tobacco use",
            "Tell the patient allergies are irrelevant to clinic visits",
        ],
        "New allergy information overrides outdated NKDA entries. Accurate allergy data must be visible to prescribing clinicians.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-intake-032
    fact(
        "skill-intake",
        "What is the role of screening questionnaires such as PHQ-2 at intake?",
        "To detect behavioral health symptoms that need scored follow-up per protocol",
        [
            "To replace provider mental health evaluation entirely",
            "To publish scores in the waiting room",
            "To determine blood pressure cuff size",
        ],
        "Screeners triage need for further assessment; they supplement, not replace, clinical judgment. Scores are confidential health information.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-intake-033
    fact(
        "skill-intake",
        "How should living situation be captured in social history when relevant?",
        "Note home safety, caregivers, and barriers such as stairs or lack of transportation",
        [
            "Record landlord bank account numbers",
            "Document neighbors' names without clinical reason",
            "List interior paint colors",
        ],
        "Functional context affects discharge planning and home care referrals. Unrelated financial or decorative details do not guide care.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-034
    fact(
        "skill-intake",
        "A patient with chest pain is triaged as emergent but insists on completing insurance paperwork first. What aligns with patient safety?",
        "Escort the patient for immediate clinical evaluation while registration completes forms later per policy",
        [
            "Hold clinical evaluation until every form is signed",
            "Ask the patient to return tomorrow if forms are incomplete",
            "Send the patient to the pharmacy aisle to wait",
        ],
        "Emergent symptoms take precedence over administrative tasks. Delaying evaluation for paperwork increases harm risk.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-035
    fact(
        "skill-intake",
        "During intake, a patient asks whether their employer can access the visit note. What is the accurate response within scope?",
        "Explain that health information is protected and released per HIPAA and patient authorization rules",
        [
            "Promise the employer will receive full notes automatically",
            "State that anyone with the patient's name may read the chart",
            "Advise the patient to avoid all future care to hide records",
        ],
        "HIPAA limits disclosure without authorization except defined permitted uses. Employers do not receive records by default.",
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-036
    fact(
        "skill-intake",
        "Which documentation practice supports meaningful ROS when time is limited?",
        "Document pertinent positives and negatives related to the chief complaint and complete broader ROS when required",
        [
            "Copy ROS from a different patient with similar age",
            "Mark every system positive to save questions",
            "Leave ROS blank because the physician will guess",
        ],
        "Focused ROS still must be truthful and relevant. Template copying or fabricated positives create legal and clinical risk.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-037
    fact(
        "skill-intake",
        "A deaf patient prefers a sign language interpreter and the video service connects in five minutes. What should intake do meanwhile?",
        "Offer written communication for urgent questions and wait to obtain informed history through the interpreter",
        [
            "Proceed with detailed surgical consent using lip reading alone",
            "Cancel the visit because of the short delay",
            "Use another patient's interpreter appointment slot",
        ],
        "Brief waits for qualified services protect consent quality. Lip reading alone is insufficient for complex history and consent.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-intake-038
    fact(
        "skill-intake",
        "The patient reports taking a friend's opioid for back pain but has no prescription. How should intake capture this?",
        "Document nonprescription opioid use in medication and social history and notify the provider",
        [
            "Omit the information because it was not prescribed",
            "List the friend as the prescribing physician",
            "Record the opioid under allergies",
        ],
        "Nonprescribed use affects safety, prescribing, and substance use screening. Omitting opioids misrepresents active substances.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-intake-039
    fact(
        "skill-intake",
        "Why should emergency contact information be confirmed at intake?",
        "To reach a designated person if the patient cannot participate in decisions",
        [
            "To bill the contact for all services without consent",
            "To add the contact as a guarantor without discussion",
            "To share full medical records with the contact by default",
        ],
        "Emergency contacts support communication during crises. They are not automatic payers or recipients of protected health information.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "beginner",
    ),
    # skill-intake-040
    fact(
        "skill-intake",
        "A returning patient has a new last name after marriage but the same date of birth and photo ID. What intake step is essential?",
        "Verify identity with ID and update the legal name in the record while retaining prior record linkage per policy",
        [
            "Create a duplicate chart with a random medical record number",
            "Refuse service until the old name is used",
            "Merge charts with another patient who shares the new surname",
        ],
        "Proper merges preserve continuity of allergies and medications. Duplicate or wrong merges cause treatment errors.",
        [S.NHA_CCMA, S.HHS_HIPAA_PRIVACY],
        "advanced",
    ),
    # skill-intake-041
    fact(
        "skill-intake",
        "Closing the intake interview should include which element?",
        "Confirm the patient understands next steps, follow-up timing, and whom to call with worsening symptoms",
        [
            "End the conversation while the patient is mid-question",
            "Provide other patients' test results for comparison",
            "Discourage questions to shorten room turnover",
        ],
        "Clear closing instructions reduce callbacks and harm from delayed care. Other patients' data are confidential.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-intake-042
    fact(
        "skill-intake",
        "A triage nurse asks the MA to room a patient with fever, rash, and recent international travel. What intake documentation priority applies?",
        "Capture travel, exposure, and symptom onset in HPI and flag for isolation instructions per protocol",
        [
            "Document shoe size before infectious symptoms",
            "Defer all documentation until checkout",
            "Record travel history in billing comments without the clinical record",
        ],
        "Travel and symptom timing guide communicable disease precautions. Infectious data belong in the clinical narrative for the care team.",
        [S.NHA_CCMA, S.CDC_STANDARD_PRECAUTIONS],
        "advanced",
    ),
]
