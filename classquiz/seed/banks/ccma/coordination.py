# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-coordination)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-coordination-001
    fact(
        'ccma-coordination',
        'After reviewing discharge instructions with a patient, which step best confirms they understood the plan?',
        'Ask the patient to explain the key steps back in their own words',
        [
            'Read the handout silently while the patient waits',
            'Assume the patient can read because they signed the form',
            'Provide only a printed pamphlet without discussion',
        ],
        'Teach-back reveals misunderstandings before the patient leaves the clinic. Silent review or paperwork alone does not verify that safety-critical details were grasped.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-002
    fact(
        'ccma-coordination',
        'Which statement best describes the typical supervisory relationship for a certified clinical medical assistant?',
        'Work under licensed provider supervision within state scope and employer policy',
        [
            'Perform invasive surgery independently without oversight',
            'Prescribe schedule II controlled substances without a delegating provider',
            'Interpret and sign off on all imaging studies alone',
        ],
        'Medical assistants coordinate care and perform delegated tasks; they do not practice medicine independently. Scope limits protect patients and define what tasks may be assigned.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-003
    fact(
        'ccma-coordination',
        'When enrolling a patient in the online patient portal, which topic should education include?',
        'Secure messaging limits and when to call 911 instead of using the portal',
        [
            'Encourage sharing login credentials with family members by default',
            'Use portal messages for chest pain or other emergencies',
            'Post laboratory results on public social media for convenience',
        ],
        'Portals improve access to results and messaging but are not a substitute for emergency services. Credential sharing and public posting violate privacy expectations.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-004
    fact(
        'ccma-coordination',
        'A clinic uses a recall list for patients overdue for preventive screenings. What is the primary purpose of that system?',
        'Identify patients due for recommended preventive services and outreach',
        [
            'Order duplicate tests on every patient regardless of history',
            'Replace provider judgment about whether screening is appropriate',
            'Waive informed consent because the list is automated',
        ],
        'Recall workflows close gaps in preventive care by flagging who needs contact. They support—not override—clinical decision making and consent requirements.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-005
    fact(
        'ccma-coordination',
        'Which community resources are appropriate to discuss with a patient managing type 2 diabetes?',
        'Hospital- or clinic-linked diabetes education classes and peer support groups',
        [
            'Unverified online products marketed as guaranteed cures',
            'Retail sales seminars unrelated to medical care',
            'Coupon programs for unrelated merchandise only',
        ],
        'Evidence-based self-management programs reinforce monitoring, nutrition, and follow-up. Unvalidated cures and unrelated promotions do not meet care coordination standards.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-006
    fact(
        'ccma-coordination',
        'The provider asks you to coordinate an urgent cardiology referral. What should appear in the referral documentation?',
        'Clinical reason, urgency, and confirmation that the consultation request was sent',
        [
            'Only the patient\'s chronological age',
            'Internal staff meal preferences for the week',
            'Unrelated procedure codes with no clinical narrative',
        ],
        'Specialists need context and urgency to triage appointments. Demographics alone or billing codes without indication delay appropriate specialty care.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-007
    fact(
        'ccma-coordination',
        'When scheduling a new patient for a dermatology referral, which information belongs in the referral packet or EHR entry?',
        'Reason for consult, urgency, and pertinent clinical findings',
        [
            'The patient\'s favorite color as the sole clinical note',
            'Links to unrelated personal social media profiles',
            'Front-desk staff scheduling preferences only',
        ],
        'Complete referral data helps the specialist prepare and prioritize the visit. Nonclinical trivia does not support safe handoffs between providers.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-008
    fact(
        'ccma-coordination',
        'A patient sends a portal message asking about a flagged abnormal laboratory result. What is the appropriate medical assistant response per typical workflow?',
        'Follow facility policy and route the message to the provider when clinical action may be needed',
        [
            'State a definitive diagnosis in the reply without provider review',
            'Ignore HIPAA because the patient initiated contact',
            'Attach another patient\'s results to illustrate a comparison',
        ],
        'Secure messaging must stay within scope and privacy rules. Abnormal values often require licensed review before the patient receives clinical interpretation.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-009
    fact(
        'ccma-coordination',
        'A patient declines a recommended specialty referral after education. How should the team document the encounter?',
        'The refusal, teaching provided, and notification of the ordering provider',
        [
            'No documentation because the patient changed their mind',
            'Only the medical assistant\'s personal opinion about the decision',
            'Another patient\'s documented choice from a different chart',
        ],
        'Informed refusal creates a legal and clinical record that the patient understood risks and alternatives. Objective notes support continuity if symptoms worsen later.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-010
    fact(
        'ccma-coordination',
        'In referral tracking, when is a specialty referral considered fully closed?',
        'The consultant\'s report is received and shared with the ordering provider',
        [
            'The patient schedules a personal vacation',
            'The waiting room receives new paint',
            'The referral is filed with no documented follow-up',
        ],
        'Closing the loop ensures recommendations and results reach the primary team. Open loops are a common source of missed diagnoses and delayed treatment.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-011
    fact(
        'ccma-coordination',
        'During a transition-of-care visit, medication reconciliation should compare which sources?',
        'Every medication the patient actually takes against the clinic medication list',
        [
            'Only vitamins the patient enjoys taking',
            'Prescriptions filled on a single arbitrary day',
            'Herbal products the patient denies using',
        ],
        'Reconciliation catches omissions, duplications, and interactions at handoffs. Partial lists that ignore OTC or denied supplements leave dangerous gaps.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-012
    fact(
        'ccma-coordination',
        'Which standards apply to documentation in the care coordination record?',
        'Objective, timely entries accessible to authorized members of the care team',
        [
            'Unsubstantiated personal judgments about the patient',
            'Notes kept only on unsecured sticky notes at the desk',
            'Progress entries with no date or time stamp',
        ],
        'Shared electronic or paper records support safe transitions. Opinionated, undated, or hidden notes break continuity when other clinicians pick up the case.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-013
    fact(
        'ccma-coordination',
        'What is the central goal of care coordination in an ambulatory practice?',
        'Connect patients with appropriate services across settings and time',
        [
            'Replace physician diagnosis with front-desk triage alone',
            'Eliminate all specialty referrals to reduce paperwork',
            'Avoid telephone follow-up to save staff time',
        ],
        'Coordination improves adherence, transitions, and access to resources. It complements—not substitutes for—licensed diagnosis and necessary referrals.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-014
    fact(
        'ccma-coordination',
        'A practice tracks referrals in a closed-loop system. What does successful loop closure require?',
        'Verification that the specialist visit occurred and results returned to the primary care provider',
        [
            'Faxing the referral once with no further contact',
            'Assuming attendance without confirming appointment or report',
            'Discarding the referral form after scheduling',
        ],
        'Closed-loop tracking prevents lost consult notes and imaging recommendations. One-way sends without follow-up leave patients and PCPs unaware of specialty findings.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-015
    fact(
        'ccma-coordination',
        'The referral coordinator notes an open loop on a six-week-old consult. What action best closes the referral loop?',
        'Confirm specialty results reached the primary care team and are filed in the chart',
        [
            'Mark the consult complete because enough time has passed',
            'Delete the referral record to clear the work queue',
            'Close the loop when billing posts without reading the report',
        ],
        'Loop closure is about information flow, not elapsed time or payment. Missing consult reports can delay cancer treatment or medication changes ordered by the specialist.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-016
    fact(
        'ccma-coordination',
        'A screen identifies food insecurity and the patient agrees to a food bank referral. What must occur before sharing information?',
        'Obtain patient consent and document the referral per clinic workflow',
        [
            'Notify local media automatically about the patient\'s situation',
            'Make the referral with no plan to confirm the patient used services',
            'Post the referral details on a public community bulletin board',
        ],
        'Social needs referrals involve sensitive information. Consent and confidential documentation align with HIPAA and respect patient autonomy.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-017
    fact(
        'ccma-coordination',
        'Which approach reflects cultural competence when coordinating care for a diverse panel?',
        'Respect health beliefs while delivering safe, evidence-based recommendations',
        [
            'Dismiss preferences that differ from staff habits',
            'Apply an identical plan without assessing individual values',
            'Refuse interpreter services to shorten visit length',
        ],
        'Culturally responsive coordination builds trust and adherence. Stereotyping or language barriers increase misunderstanding and disparities in outcomes.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-018
    fact(
        'ccma-coordination',
        'A clinic offers shared medical appointments for stable chronic conditions. What is a valid benefit of the group visit model?',
        'Combine structured education with brief individual assessment in one session',
        [
            'Waive all HIPAA privacy protections for participants',
            'Eliminate individual consent for every sensitive topic',
            'Skip documentation because the visit is held in a group room',
        ],
        'Group visits can improve efficiency and peer support when facilitation, privacy, and documentation follow policy. Privacy rules and consents still apply.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-019
    fact(
        'ccma-coordination',
        'A patient with heart failure has new symptoms and changed personal goals. How should the written care plan be managed?',
        'Revise the plan to reflect current condition, targets, and follow-up intervals',
        [
            'Leave the original plan unchanged indefinitely',
            'Keep the plan hidden from the patient and caregivers',
            'Base updates on informal staff gossip rather than assessment',
        ],
        'Living care plans align the team and patient on measurable goals. Static or secret plans fail when clinical status or priorities shift.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-020
    fact(
        'ccma-coordination',
        'You are selecting take-home education for a patient with low health literacy. Which choice is most appropriate?',
        'Materials written at an appropriate reading level in the patient\'s preferred language',
        [
            'Peer-reviewed journal articles with no plain-language summary',
            'Identical handouts for every diagnosis regardless of need',
            'Handouts distributed without teach-back or questions',
        ],
        'Readable, language-concordant materials plus teach-back improve self-management. Dense text or one-size-fits-all packets often fail in real-world use.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-021
    fact(
        'ccma-coordination',
        'Under HIPAA, what does the minimum necessary standard require when disclosing protected health information?',
        'Share only the PHI reasonably needed for the specific purpose',
        [
            'Release the entire medical record whenever any request arrives',
            'Deny patients access to their own information by default',
            'Send full charts to marketing vendors for convenience',
        ],
        'Minimum necessary limits incidental over-disclosure during treatment, payment, and operations. Patients retain access rights separate from workforce disclosure rules.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-022
    fact(
        'ccma-coordination',
        'The lab orders fasting chemistry panels. Which details should a reminder call include?',
        'How long to remain NPO and whether to take usual medications',
        [
            'Eat a large breakfast before the draw to avoid dizziness',
            'Withhold all fluids including water for 72 hours in every case',
            'Tell the patient not to ask about prescription timing',
        ],
        'Fasting instructions vary by test and medication; clear guidance reduces cancelled specimens. Food or incorrect med holds can invalidate results or harm the patient.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-023
    fact(
        'ccma-coordination',
        'Population health staff call patients overdue for mammography or hemoglobin A1C testing. What is the intended outcome?',
        'Close documented preventive care gaps with scheduled screening',
        [
            'Market unrelated retail products during the call',
            'Replace annual wellness visits with phone outreach only',
            'Discuss patient names and results on public social networks',
        ],
        'Outreach targets evidence-based screenings that improve early detection and chronic disease control. It supplements—not replaces—clinical visits and must stay confidential.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-024
    fact(
        'ccma-coordination',
        'Insurance requires prior authorization before an MRI. What must typically happen before the scan?',
        'Submit clinical documentation supporting medical necessity to the payer',
        [
            'Rely on the patient\'s verbal assurance that insurance will pay',
            'Post the order on a public website for faster approval',
            'Proceed with imaging without contacting the payer',
        ],
        'Payers review diagnosis, indications, and prior treatments before approving high-cost studies. Starting without authorization commonly results in denial and patient financial liability.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-025
    fact(
        'ccma-coordination',
        'When completing a prior authorization request for physical therapy, which supporting information do payers usually need?',
        'Clinical notes that document medical necessity for the ordered service',
        [
            'A list of the patient\'s hobbies unrelated to the condition',
            'Random diagnosis codes chosen to match the fee schedule',
            'Deleted visit documentation to shorten the packet',
        ],
        'Authorization reviewers match orders to coverage criteria using visit notes, diagnoses, and functional status. Incomplete or inaccurate packets delay therapy start dates.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'Recall systems for preventive care should?',
        'Identify patients due for screenings and contact per protocol',
        [
            'Call only new patients',
            'Skip documented refusals without note',
            'Use unencrypted public posts',
        ],
        'Systematic outreach improves preventive uptake. Choosing Call only new patients is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'Social determinants of health screening may identify needs for?',
        'Food, housing, or transportation support',
        [
            'Only cosmetic services',
            'Unrelated retail discounts',
            'Deleting the EHR',
        ],
        'Addressing social needs supports outcomes. Choosing Only cosmetic services is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'Social determinants screening may identify needs for?',
        'Food, housing, or transportation support',
        [
            'Mandatory cosmetic procedures',
            'Unrelated retail discounts only',
            'Staff scheduling preferences',
        ],
        'Addressing barriers supports adherence and outcomes. Choosing Mandatory cosmetic procedures is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'Transition-of-care phone calls after discharge should verify?',
        'Patient understanding of new medications',
        [
            'Ignoring pharmacy pickup',
            'Deleting the discharge plan',
            'Skipping PCP follow-up',
        ],
        'Follow-up reduces adverse events after discharge. Choosing Ignoring pharmacy pickup is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'Transition-of-care summaries help by?',
        'Communicating medications and pending results to the next provider',
        [
            'Deleting the medication list',
            'Avoiding diagnosis lists',
            'Using only verbal handoffs without records',
        ],
        'Structured handoffs reduce errors after discharge. Choosing Deleting the medication list is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'What does Care plans for chronic disease often include?',
        'Self-management goals and follow-up intervals',
        [
            'Only billing codes',
            'No measurable targets',
            'Avoiding family involvement always',
        ],
        'Collaborative goals support adherence. Choosing Only billing codes is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'What does Cultural competence in scheduling include?',
        'Offering interpreter services when language barriers exist',
        [
            'Assuming family will translate confidential details',
            'Refusing alternate appointment times always',
            'Documenting ethnicity for gossip',
        ],
        'Qualified interpreters improve safety and trust. Choosing Assuming family will translate confidential details is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'What does Patient self-management education for diabetes include?',
        'Glucose monitoring and foot care basics',
        [
            'Stopping all insulin without provider input',
            'Avoiding any follow-up',
            'Ignoring hypoglycemia symptoms',
        ],
        'Education empowers safe self-care. Choosing Stopping all insulin without provider input is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'What should A referral tracking log include?',
        'Reason, date, specialist, and follow-up status',
        [
            'Only patient favorite color',
            'Staff lunch orders',
            'Unrelated billing codes only',
        ],
        'Tracking supports closure of the referral loop. Choosing Only patient favorite color is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'What should Care coordination after hospital discharge include?',
        'Scheduling follow-up and reviewing new medications with the patient',
        [
            'Discarding discharge instructions',
            'Assuming the hospital will call the patient',
            'Deleting the problem list',
        ],
        'Transitions of care reduce readmissions and medication errors. Choosing Discarding discharge instructions is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'What should Transition-of-care summaries include?',
        'Medications, allergies, and follow-up plan',
        [
            'Only billing codes',
            'Staff schedules',
            'Marketing flyers',
        ],
        'Accurate handoffs reduce errors after discharge. Choosing Only billing codes is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'When PHI is used for treatment?',
        'HIPAA generally permits disclosure without separate authorization',
        [
            'Always forbidden',
            'Requires court order each time',
            'Requires patient notary',
        ],
        'Treatment, payment, and operations are permitted uses under HIPAA. Choosing Always forbidden is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'When a patient misses appointments repeatedly, the team should?',
        'Assess barriers and adjust outreach per policy',
        [
            'Discharge without contact automatically',
            'Share details on public forums',
            'Ignore no-show patterns',
        ],
        'Barrier assessment supports engagement. Choosing Discharge without contact automatically is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'When coordinating home health services, the MA documents?',
        'Referral sent, services ordered, and patient consent per policy',
        [
            "Only the patient's favorite color",
            'Unrelated billing codes',
            'Staff vacation schedules',
        ],
        "Documentation supports continuity and billing accuracy. Choosing Only the patient's favorite color is a plausible near-miss that does not match the clinical fact tested in this question.",
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'When coordinating home health, verify?',
        'Orders, insurance authorization, and patient consent as required',
        [
            "Only the patient's address",
            'That equipment is decorative',
            'Nothing if family insists',
        ],
        "Authorization and orders must align with payer rules. Choosing Only the patient's address is a plausible near-miss that does not match the clinical fact tested in this question.",
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'When scheduling a diagnostic test, confirm?',
        'Preparation instructions and authorization if required',
        [
            'Social media handles',
            'Patient shoe size',
            'Unrelated vaccine lot numbers',
        ],
        'Prep errors can delay or invalidate testing. Choosing Social media handles is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-coordination',
        'Sharps injury logs must be maintained?',
        'Per OSHA requirements for covered employers',
        [
            'Only if OSHA inspects',
            'Only in hospitals',
            'Never for medical offices',
        ],
        'OSHA bloodborne pathogens standard includes recordkeeping provisions. Choosing Only if OSHA inspects is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

