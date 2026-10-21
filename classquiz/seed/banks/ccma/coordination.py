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
            'Provide a printed pamphlet without discussion or teach-back',
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
        'When enrolling a patient in the online patient portal, which topic is most important to cover in education?',
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
        'Recall workflows close gaps in preventive care by flagging who needs contact. They support, not override, clinical decision making and consent requirements.',
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
            'Coupon programs for unrelated retail merchandise',
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
            'The patient\'s chronological age without clinical indication',
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
            'Front-desk staff scheduling preferences as the sole referral content',
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
            'The medical assistant\'s personal opinion about the decision without refusal details',
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
            'Vitamins the patient enjoys taking without prescription medications',
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
            'Notes kept on unsecured sticky notes at the desk',
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
        'Coordination improves adherence, transitions, and access to resources. It complements rather than substitutes for licensed diagnosis and necessary referrals.',
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
            'Defer documentation because the visit is held in a group room',
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
        'The lab orders fasting chemistry panels. Which instructions should the reminder call convey?',
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
            'Replace annual wellness visits with phone outreach alone',
            'Discuss patient names and results on public social networks',
        ],
        'Outreach targets evidence-based screenings that improve early detection and chronic disease control. It supplements clinical visits rather than replacing them and must stay confidential.',
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
    # ccma-coordination-026
    fact(
        'ccma-coordination',
        'When running preventive-care recall outreach, which practice best supports ethical and effective contact?',
        'Follow the clinic protocol for patients due for screening, including documented refusals',
        [
            'Contact brand-new patients while omitting established panel members',
            'Remove patients from the list after refusal without charting the discussion',
            'Post patient names and due dates on an unencrypted public website',
        ],
        'Recall workflows depend on consistent outreach and accurate lists. Undocumented refusals and privacy breaches undermine gap closure and violate confidentiality expectations.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-027
    fact(
        'ccma-coordination',
        'A validated social determinants of health screen flags unstable housing. Which need category does that finding represent?',
        'A nonclinical barrier that can interfere with treatment adherence and follow-up',
        [
            'A request for elective cosmetic surgery unrelated to housing insecurity',
            'A retail loyalty program enrollment opportunity',
            'A reason to delete the electronic health record',
        ],
        'Housing insecurity affects appointment attendance, medication storage, and safety. Coordinators connect patients to appropriate resources rather than treating SDOH as billing trivia.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-028
    fact(
        'ccma-coordination',
        'After a positive SDOH screen, what is the medical assistant\'s typical coordination role?',
        'Warm handoff or referral to social work, case management, or community partners per policy',
        [
            'Prescribe housing or food directly without provider involvement',
            'Document the screen but take no further action when the patient agrees to help',
            'Share the screen results on a public community bulletin board',
        ],
        'Screening without linkage leaves needs unaddressed. MAs facilitate referrals and documentation within scope while licensed staff manage clinical orders.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-029
    fact(
        'ccma-coordination',
        'During a post-discharge transition-of-care phone call, what should be verified first?',
        'Whether the patient understands new medications and has a plan to obtain them',
        [
            'That the patient will ignore pharmacy pickup until the next visit',
            'That discharge paperwork was discarded to reduce clutter',
            'That primary care follow-up is unnecessary if symptoms improve',
        ],
        'Medication errors drive many readmissions after hospitalization. Calls that confirm understanding and access catch problems before they become emergencies.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-030
    fact(
        'ccma-coordination',
        'Which elements belong in a transition-of-care summary sent to the primary care provider?',
        'Active medications, allergies, principal diagnoses, and pending test results',
        [
            'An empty medication list to protect privacy',
            'Front-desk staff vacation schedules',
            'Marketing flyers for unrelated retail products',
        ],
        'Structured summaries give the receiving clinician a usable snapshot at handoff. Missing meds or results recreate the information gaps that transitions are meant to close.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-031
    fact(
        'ccma-coordination',
        'A collaborative chronic disease care plan should routinely include which components?',
        'Measurable self-management goals and scheduled follow-up intervals',
        [
            'Procedure codes with no patient-facing targets',
            'A static plan that remains unchanged when status worsens',
            'A blanket rule to exclude caregivers from all discussions',
        ],
        'Shared goals align the patient and team on monitoring, lifestyle changes, and when to seek help. Plans without targets or updates fail when disease activity shifts.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-032
    fact(
        'ccma-coordination',
        'When scheduling for a patient with limited English proficiency, which action reflects culturally competent coordination?',
        'Offer qualified interpreter services for the appointment per facility policy',
        [
            'Rely on young children in the family to interpret confidential medical details',
            'Refuse all alternate appointment times without assessing need',
            'Record ethnicity in the chart solely for informal staff discussion',
        ],
        'Professional interpreters reduce errors in consent, instructions, and scheduling. Family members may omit sensitive topics; qualified services protect accuracy and privacy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-033
    fact(
        'ccma-coordination',
        'Which topics belong in diabetes self-management education coordinated by the ambulatory team?',
        'Blood glucose monitoring, hypoglycemia recognition, and daily foot inspection',
        [
            'Stopping prescribed insulin whenever glucose readings are high',
            'Avoiding all follow-up visits after the first class',
            'Ignoring shakiness and sweating as unrelated to glucose',
        ],
        'Self-management education reinforces safe monitoring and early complication detection. Unauthorized insulin changes and missed follow-up increase acute and long-term harm.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-034
    fact(
        'ccma-coordination',
        'What minimum data should a referral tracking log capture for each specialty consult?',
        'Clinical reason, referral date, specialist, and current follow-up status',
        [
            'The patient\'s favorite color for filing purposes',
            'Catering orders from the last staff meeting',
            'Unrelated diagnosis codes with no narrative indication',
        ],
        'Complete logs let coordinators chase open loops and confirm reports returned. Trivial or nonclinical fields do not support safe closure of the referral cycle.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-035
    fact(
        'ccma-coordination',
        'After a patient is discharged from the hospital, which tasks fit the medical assistant\'s care coordination role?',
        'Schedule timely primary care follow-up and review new medications with the patient',
        [
            'Discard hospital discharge instructions to simplify the chart',
            'Assume the inpatient team will call the patient about all changes',
            'Remove active problems from the problem list without provider review',
        ],
        'Ambulatory follow-up bridges inpatient recommendations to daily self-care. Discarding instructions or deferring all contact invites readmission and medication mistakes.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-036
    fact(
        'ccma-coordination',
        'For a patient discharged after heart failure exacerbation, when should outpatient follow-up typically be arranged?',
        'Within the timeframe recommended by transition-of-care guidelines and the discharging team',
        [
            'Defer follow-up until the patient develops new symptoms months later',
            'Whenever front desk has an opening with no clinical urgency review',
            'Decline scheduling because hospital care is considered complete at discharge',
        ],
        'Early post-discharge visits catch fluid overload, medication errors, and misunderstanding of diet or activity limits. Delayed access is linked to higher readmission rates.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-037
    fact(
        'ccma-coordination',
        'When sharing protected health information with another provider for active patient treatment, HIPAA generally requires what?',
        'No separate patient authorization when disclosure is for treatment purposes',
        [
            'A complete ban on any PHI exchange between clinicians',
            'A court order for every routine consult note',
            'Notarized patient consent for each fax to a specialist',
        ],
        'Treatment is a permitted use under HIPAA when minimum necessary and policy are followed. Routine care coordination does not require a new authorization for each treating clinician.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-038
    fact(
        'ccma-coordination',
        'A patient has missed three consecutive appointments. What is the most appropriate care coordination response?',
        'Assess barriers such as transport or work schedule and adjust outreach per policy',
        [
            'Automatically discharge the patient from the practice without contact',
            'Discuss the patient\'s attendance on a public social media page',
            'Ignore the pattern because reminders were sent once',
        ],
        'No-shows often reflect access, literacy, or social barriers rather than disinterest. Structured outreach and documentation support engagement and medicolegal clarity.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-039
    fact(
        'ccma-coordination',
        'When arranging home health services, what should the medical assistant document in the chart?',
        'That the referral was sent, ordered services are listed, and consent followed policy',
        [
            'Nonclinical trivia unrelated to the visit',
            'Unrelated procedure codes with no home health context',
            'Staff personal schedules instead of patient-specific actions',
        ],
        'Clear documentation supports continuity for nurses, therapists, and billing reviewers. Vague or nonclinical notes do not prove the handoff occurred.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-040
    fact(
        'ccma-coordination',
        'Before home health begins visits, which items must the coordinator typically confirm?',
        'Signed orders, payer authorization when required, and patient agreement to services',
        [
            'Confirmation that the mailing address on the ID is current',
            'That durable medical equipment is decorative rather than functional',
            'Nothing further if a family member verbally insists on care',
        ],
        'Home health agencies cannot bill or treat without valid orders and coverage. Address alone does not establish medical necessity or consent.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-041
    fact(
        'ccma-coordination',
        'When booking a colonoscopy or other diagnostic procedure, what should the scheduler verify with the patient?',
        'Preparation instructions and prior authorization when the payer requires it',
        [
            'Social media account names for appointment reminders without prep instructions',
            'Footwear size for unrelated orthopedic billing',
            'Vaccine lot numbers with no connection to the ordered test',
        ],
        'Incorrect prep or missing authorization commonly leads to cancelled procedures and delayed diagnosis. Schedulers reinforce instructions that protect specimen quality and coverage.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-042
    fact(
        'ccma-coordination',
        'After a needlestick in the clinic, why must sharps injury logs be maintained per OSHA?',
        'To document exposure incidents and support required follow-up and program evaluation',
        [
            'When a federal inspector is already on site',
            'In inpatient hospitals but not in ambulatory outpatient offices',
            'Withhold logs because medical offices are exempt from bloodborne pathogen rules',
        ],
        'The bloodborne pathogens standard applies to many ambulatory settings and requires a sharps injury log for needlestick tracking. Records guide post-exposure care and device safety reviews.',
        [S.NHA_CCMA],
        'advanced',
    ),

    # ccma-coordination-043
    fact(
        'ccma-coordination',
        'When scheduling a follow-up visit, what information helps the care team prioritize timing?',
        'Clinical urgency, provider instructions, and patient availability',
        ['The color of the patient\'s clothing',
        'Whether the front desk prefers morning breaks',
        'Unrelated social media posts'],
        'Scheduling should reflect medical need and ordered follow-up intervals. Cosmetic or staff convenience factors do not determine safe return intervals.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-044
    fact(
        'ccma-coordination',
        'Why is closing the referral loop important after a specialist visit?',
        'It ensures consultation findings reach the primary team for ongoing care',
        ['It eliminates the need for future appointments',
        'It replaces the specialist\'s medical license',
        'It guarantees insurance payment without documentation'],
        'Loop closure prevents lost results and medication changes from falling through. It does not remove follow-up needs or legal documentation requirements.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-045
    fact(
        'ccma-coordination',
        'A patient with limited English proficiency needs education about a new inhaler. What resource should be used?',
        'A qualified medical interpreter and translated materials when available',
        ['A bilingual receptionist unrelated to clinical care',
        'Hand gestures without involving the provider',
        'Written instructions in a language the patient does not read'],
        'Qualified interpretation supports informed use of devices. Untrained staff or mismatched language materials increase error risk.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-coordination-046
    fact(
        'ccma-coordination',
        'What should a transition-of-care document include for safe handoffs?',
        'Medication list, allergies, pending tests, and follow-up plan',
        ['Staff lunch orders',
        'Unrelated marketing flyers',
        'Social security numbers of visitors'],
        'Accurate med and allergy data prevent errors after discharge. Nonclinical identifiers do not support continuity.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-047
    fact(
        'ccma-coordination',
        'A recall notice identifies patients overdue for mammography screening. What is the goal of outreach?',
        'Prompt preventive care within guideline intervals',
        ['Increase duplicate testing without indication',
        'Replace shared decision making',
        'Bill for services that were not provided'],
        'Recall systems close gaps in prevention. They should follow evidence-based intervals, not drive unnecessary duplicate imaging.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-048
    fact(
        'ccma-coordination',
        'What is the benefit of using a patient portal for routine refill requests?',
        'Secure messaging that documents requests for the care team',
        ['Public posting of medication lists',
        'Automatic approval without provider review',
        'Sharing passwords among family members'],
        'Portals create auditable threads within HIPAA controls. Refills still require clinical review; shared passwords undermine security.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-049
    fact(
        'ccma-coordination',
        'When coordinating home health services, which document must align with payer rules?',
        'Signed orders describing skilled needs and frequency',
        ['A handwritten grocery list',
        'Unrelated school transcripts',
        'Social media screenshots'],
        'Payers require authorized plans of care. Nonclinical documents do not establish medical necessity for home visits.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-coordination-050
    fact(
        'ccma-coordination',
        'Why should patient education materials match literacy level?',
        'Plain language improves comprehension and adherence',
        ['Complex journal articles impress every patient',
        'Reading level is irrelevant to outcomes',
        'Pictures replace all verbal teaching'],
        'Materials at appropriate literacy support self-care. Dense text without teach-back leaves gaps.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-coordination-051
    fact(
        'ccma-coordination',
        'A care plan for heart failure includes daily weight monitoring. What instruction supports the goal?',
        'Weigh at the same time each day on the same scale',
        ['Weigh once a year before holidays',
        'Switch scales randomly for variety',
        'Ignore two-pound changes'],
        'Consistent technique detects fluid retention early. Infrequent or inconsistent weighing misses gradual gain.',
        [S.NHA_CCMA],
        'intermediate',
    ),
]
