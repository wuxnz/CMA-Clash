# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-law-ethics)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-law-ethics-001
    fact(
        'ccma-law-ethics',
        'In healthcare ethics, what does the principle of beneficence require of the care team?',
        "Act in ways that promote the patient's welfare and best interest",
        [
            'Prioritize clinic revenue over clinical need when they conflict',
            'Withhold treatment whenever any risk exists, regardless of benefit',
            'Conceal errors from the patient to avoid distress',
        ],
        'Beneficence is an active duty to do good for the patient, not merely to avoid harm. Financial gain, blanket risk avoidance, or hiding mistakes conflict with putting the patient first.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-002
    fact(
        'ccma-law-ethics',
        'What does fidelity mean as an ethical obligation in patient care?',
        'Keeping promises and honoring professional duties to patients and employers',
        [
            'Sharing identifiable patient stories on personal social media',
            'Leaving assigned patients without notifying a qualified replacement',
            'Performing tasks beyond training without telling the supervising provider',
        ],
        'Fidelity builds trust through reliability and honesty. Abandonment, unauthorized scope expansion, and casual disclosure of PHI undermine the professional relationship.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-003
    fact(
        'ccma-law-ethics',
        'Which statement best defines nonmaleficence in clinical practice?',
        'Avoiding actions that cause unnecessary harm to the patient',
        [
            'Documenting known drug allergies but administering the allergen anyway',
            'Skipping patient teaching because it takes extra time',
            'Discussing a patient\'s diagnosis in the staff break room for entertainment',
        ],
        'Nonmaleficence is often summarized as "do no harm." Ignoring safety data, withholding education, or gossiping about patients can directly or indirectly injure the person receiving care.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-004
    fact(
        'ccma-law-ethics',
        'When applying nonmaleficence during medication administration, what is the medical assistant\'s priority?',
        'Follow the five rights and report concerns before giving a medication that may harm the patient',
        [
            'Give the dose on time even when the allergy band contradicts the order',
            'Skip reporting new side effects if the patient seems uncomfortable complaining',
            'Carry out a procedure the provider ordered if you are unsure you are trained for it',
        ],
        'Safe practice means verifying identity, drug, dose, route, and time, then stopping when something does not fit. Speed, silence about adverse effects, or working outside scope increases harm risk.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-005
    fact(
        'ccma-law-ethics',
        'What does respect for patient autonomy require when the patient is decisionally capable?',
        "Honor the patient's right to accept or refuse care after adequate information",
        [
            'Proceed with treatment because the provider knows what is best',
            'Ignore a clear refusal if family members want the procedure done',
            'Make routine care decisions for the patient without discussion',
        ],
        'Autonomy protects competent adults from unwanted intervention. Overriding refusals or deciding without the patient\'s input violates respect for persons, even when the team disagrees with the choice.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-006
    fact(
        'ccma-law-ethics',
        'A provider recommends a procedure with meaningful risks. How does beneficence guide the medical assistant\'s role in that conversation?',
        'Support honest education so the patient can weigh benefits against risks',
        [
            'Encourage the patient to sign quickly so the schedule stays full',
            'Emphasize only benefits and avoid mentioning complications',
            'Tell the patient the team will decide what is best without their input',
        ],
        'Beneficence includes helping patients pursue favorable outcomes, which requires truthful information. Rushed or one-sided consent undermines the patient\'s ability to choose what is best for them.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-007
    fact(
        'ccma-law-ethics',
        'A medical assistant copies patient handouts from a publisher\'s website without permission or citation. Why is this problematic?',
        'It is unethical and may violate copyright law',
        [
            'It is encouraged whenever it saves documentation time',
            'It is acceptable as long as the clinic logo is on the page',
            'HIPAA requires copying third-party materials without attribution',
        ],
        'Patient education materials should be properly licensed or attributed. Copyright protects authors; HIPAA governs privacy of PHI, not permission to reproduce published content.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-008
    fact(
        'ccma-law-ethics',
        'What authority does a durable power of attorney for health care grant when the patient loses decision-making capacity?',
        'A named agent may make medical decisions within the document\'s limits and state law',
        [
            'Any visitor in the waiting room may consent to surgery',
            'The agent may override every written advance directive in all situations',
            'Front-desk staff may perform invasive procedures without a license',
        ],
        'Healthcare agents step in only for medical decisions defined by the form and statute. They are not a blanket license for unqualified people to treat or to ignore valid advance directives.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-009
    fact(
        'ccma-law-ethics',
        'How is a durable power of attorney for health care different from a financial power of attorney?',
        'It appoints someone to make health care decisions, not to manage property or finances',
        [
            'It transfers real estate automatically when the patient is hospitalized',
            'It removes the need for informed consent for every future procedure',
            'It allows a medical assistant to practice medicine without supervision',
        ],
        'Advance care planning documents name trusted decision makers for treatment when the patient cannot speak. They do not replace licensure, routine consent, or financial legal instruments.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-010
    fact(
        'ccma-law-ethics',
        'Under typical state mandated-reporter rules, what must a medical assistant report?',
        'Reasonable suspicion of child abuse, elder abuse, or neglect as defined by law',
        [
            'A parent arriving late to a well-child visit',
            'A patient\'s preference for a different nurse on the care team',
            'An uncomplicated upper respiratory infection',
        ],
        'Mandated reporting protects vulnerable populations from harm. Scheduling friction, staffing preferences, and routine illness are not reportable events unless abuse or neglect is suspected.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-011
    fact(
        'ccma-law-ethics',
        'An adolescent requests confidential STI screening where state law permits minor consent. What should the medical assistant do?',
        'Follow state minor-consent statutes and the clinic\'s privacy policy for results and disclosure',
        [
            'Call the parent and disclose all visit details before checking whether confidentiality applies',
            'Refuse all laboratory testing for patients under 18 regardless of state law',
            'Post normal results on a public social media page to reduce phone calls',
        ],
        'Many states allow minors to consent to certain sensitive services; HIPAA still requires safeguarding PHI. Automatic parental notification or public disclosure may be illegal and unethical.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-012
    fact(
        'ccma-law-ethics',
        'What is the primary purpose of an advance directive in the medical record?',
        'Document the patient\'s wishes for future treatment if they become unable to decide',
        [
            'List the patient\'s preferred appointment days for the next year',
            'State fixed insurance copayment amounts for common visits',
            'Provide laboratory reference ranges for routine chemistry panels',
        ],
        'Living wills, health care agents, and similar tools guide care during incapacity. They are legal-clinical documents, not scheduling sheets, fee schedules, or lab tables.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-013
    fact(
        'ccma-law-ethics',
        'After a medication error with no immediate injury, how should the medical assistant complete an incident report?',
        'Record objective facts, times, and actions taken for quality improvement review',
        [
            'State in the report that the patient caused the mistake',
            'Alter the original medication record to match what should have been given',
            'Discard the report so the event is not tracked',
        ],
        'Incident reporting supports systems fixes, not blame. Falsifying records or omitting events hides safety problems and may create additional legal exposure.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-014
    fact(
        'ccma-law-ethics',
        'Which practice best reflects respect for autonomy during informed consent?',
        'Give the patient clear information and accept a voluntary yes or no without pressure',
        [
            'Have staff decide the plan of care and inform the patient afterward',
            'Withhold a new cancer diagnosis until family insists on telling the patient',
            'Obtain a signature by warning the patient they will be discharged otherwise',
        ],
        'Informed consent requires disclosure, comprehension, and voluntariness. Secret decisions, selective truth-telling, and threats undermine the patient\'s right to participate in care choices.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-015
    fact(
        'ccma-law-ethics',
        'Why do many organizations maintain a corporate compliance hotline?',
        'To allow confidential reporting of suspected fraud, abuse, or policy violations',
        [
            'To publish patient identifiers so employees can verify appointments',
            'To require kickbacks before approving vendor contracts',
            'To destroy records that might reveal billing errors',
        ],
        'Compliance programs depend on early, protected reporting. Hotlines are not tools for exposing PHI, concealing misconduct, or encouraging illegal payments.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-016
    fact(
        'ccma-law-ethics',
        'A late entry is needed because vital signs were charted in the wrong column. What is the ethical way to correct the record?',
        'Add a dated, signed addendum per policy without deleting or obscuring the original entry',
        [
            'Delete the entire electronic note and recreate it as if the error never occurred',
            'Change the timestamp so the entry appears to have been made on the prior day',
            'Ask a colleague to sign the note as if they had witnessed the visit',
        ],
        'Medical records must remain auditable. Silent deletion, backdating, and signature forgery are falsification and can harm patients and providers in future care or legal review.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-017
    fact(
        'ccma-law-ethics',
        'When state law recognizes a patient as an emancipated minor, what consent authority usually applies?',
        'The minor may consent to their own medical care within the limits of that statute',
        [
            'The minor may never receive outpatient care without a parent present',
            'The minor may hire and fire all clinic employees',
            'The minor may override federal and state practice acts for every facility',
        ],
        'Emancipation is a legal status, often via marriage, military service, or court order, that grants limited adult consent rights. It does not grant employer authority or licensure to practice medicine.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-018
    fact(
        'ccma-law-ethics',
        'Which action by a medical assistant best demonstrates beneficence during a routine visit?',
        'Notice the patient\'s uncontrolled blood pressure and promptly alert the licensed provider',
        [
            'Skip repeat vitals because the patient says they feel fine',
            'Tell the patient elevated readings are normal without provider input',
            'Delay reporting abnormal findings until the end of the week',
        ],
        'Beneficence means actively promoting well-being. Ignoring or minimizing abnormal data delays treatment that could prevent serious complications.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-019
    fact(
        'ccma-law-ethics',
        'A medical assistant owns stock in a laboratory that the clinic uses for send-out tests. What should happen before discussing that lab with patients?',
        'Disclose the financial interest and follow facility policy so patient welfare comes first',
        [
            'Keep the ownership private so patients are not confused',
            'Recommend that lab because personal profit is the main goal',
            'Ignore the conflict if the lab offers the highest commission',
        ],
        'Conflicts of interest must be managed transparently. Hidden financial ties can bias recommendations and erode trust in the care team\'s advice.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-020
    fact(
        'ccma-law-ethics',
        'You suspect a coworker is practicing while impaired by alcohol or drugs. What is the appropriate first step?',
        'Notify a supervisor or follow the facility\'s policy for reporting impaired practice',
        [
            'Describe the coworker\'s behavior on a public social media post',
            'Say nothing because loyalty to colleagues matters more than safety',
            'Physically confront the coworker in the patient waiting area',
        ],
        'Impaired practice endangers patients and staff. Facilities have defined reporting paths; public shaming, silence, or aggression escalate risk instead of protecting care.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-021
    fact(
        'ccma-law-ethics',
        'Before a surgical procedure, what information must the patient receive for consent to be considered informed?',
        'The nature of the procedure, material risks, expected benefits, and reasonable alternatives',
        [
            'Only the estimated patient responsibility on the billing statement',
            'A guarantee that no complication will ever occur',
            'Contact information for staff personal social media accounts',
        ],
        'Informed consent rests on meaningful disclosure, not billing alone. Outcomes cannot be guaranteed, and unrelated personal details do not substitute for clinical education.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-022
    fact(
        'ccma-law-ethics',
        'Which elements must all be present for informed consent to be valid?',
        'Adequate information, patient understanding, and voluntary agreement without coercion',
        [
            'A signature obtained before any explanation to save clinic time',
            'Agreement obtained after threats to withhold all future care',
            'A blanket waiver of the right to ask questions about any treatment',
        ],
        'Valid consent combines disclosure, comprehension, and voluntariness. Rushed signatures, pressure tactics, or giving up the right to ask questions invalidate the ethical and legal basis for treatment.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-023
    fact(
        'ccma-law-ethics',
        'In bioethics, what does the principle of justice emphasize?',
        'Fair distribution of health care benefits and burdens among patients and populations',
        [
            'Delivering premium services only to personal friends of the staff',
            'Ignoring insurance status when allocating scarce resources in every setting',
            'Denying care based on race, religion, or other protected characteristics',
        ],
        'Justice requires equitable treatment and responsible stewardship of limited resources. Favoritism, arbitrary denial, and discrimination violate ethical and often legal standards.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-024
    fact(
        'ccma-law-ethics',
        'During a vaccine shortage, how does justice guide clinic triage decisions?',
        'Allocate doses using evidence-based priority rules that treat similar patients fairly',
        [
            'Give vaccine only to patients who pay the highest cash fee',
            'Select recipients based on staff members\' personal preferences',
            'Skip triage protocols and vaccinate whoever arrives first regardless of risk',
        ],
        'Justice supports transparent criteria, such as age, risk, and occupation, during scarcity. Payment alone, bias, or chaos undermines fair access to preventive care.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-025
    fact(
        'ccma-law-ethics',
        'Which situations commonly trigger mandatory reporting duties for health care workers?',
        'Suspected physical abuse, sexual abuse, or neglect of children or dependent adults',
        [
            'A dispute over a $15 copayment at check-in',
            'A patient\'s choice of hairstyle or hair color',
            'An uncomplicated viral upper respiratory infection',
        ],
        'Mandatory reporting laws focus on protecting vulnerable people from harm. Billing disagreements, appearance choices, and routine minor illness are not abuse-reporting triggers.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Mandatory reporting of suspected abuse generally?',
        'Requires reporting to designated authorities per state law',
        [
            'Is optional if the patient is wealthy',
            'Can be delayed until next holiday',
            'Applies only in hospitals never clinics',
        ],
        'Healthcare workers must know local reporting statutes and agency contacts. Failure to report can carry legal penalties.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Minors may consent without parent involvement for certain services when?',
        'State law explicitly allows (e.g., some reproductive or mental health care)',
        [
            'Never under any law',
            'Whenever the minor prefers always',
            'Only if parent is traveling',
        ],
        'Consent rules for minors vary by state and service. Choosing Never under any law is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Negligence requires?',
        'Duty, breach, causation, and damages',
        [
            'Only patient anger',
            'Only paperwork typos without harm',
            'Intent to harm always',
        ],
        'Malpractice analysis uses these elements. Choosing Only patient anger is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Patient autonomy supports?',
        'The right to refuse treatment',
        [
            'Forced procedures without discussion',
            'Withholding all information',
            'Unlimited access to other charts',
        ],
        'Competent adults may decline care. Choosing Forced procedures without discussion is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Scope of practice for medical assistants is defined by?',
        'State law and delegating provider regulations',
        [
            'Personal preference',
            'Social media trends',
            'Patient requests alone',
        ],
        'MAs work under supervision per state rules. Choosing Personal preference is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Stark Law broadly restricts?',
        'Physician self-referral for designated health services',
        [
            'All patient education',
            'Hand hygiene',
            'Interpreter use',
        ],
        'Self-referral rules protect against financial conflicts. Choosing All patient education is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'The Anti-Kickback Statute prohibits?',
        'Remuneration to induce referrals for federal healthcare programs',
        [
            'Properly disclosed quality bonuses per safe harbors in some cases',
            'All salaries to employees',
            'All continuing education',
        ],
        'Kickbacks distort medical judgment. Choosing Properly disclosed quality bonuses per safe harbors in some cases is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'The False Claims Act addresses?',
        'Fraudulent claims for government healthcare payment',
        [
            'Patient parking fines',
            'Personal social media posts',
            'Break room theft only',
        ],
        'Submitting false claims can trigger civil penalties. Choosing Patient parking fines is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'What does A mandatory reporting situation may include?',
        'Reasonable suspicion of abuse per state law',
        [
            'Minor billing disputes',
            'Patient lateness',
            'Preference for another provider',
        ],
        'Report per legal duty and facility policy. Choosing Minor billing disputes is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'What does Boundary violations include?',
        'Inappropriate personal relationships with patients',
        [
            'Professional empathy',
            'Maintaining confidentiality',
            'Using interpreters',
        ],
        'Professional boundaries protect patients. Choosing Professional empathy is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'What does Patient self-determination include?',
        'Right to refuse treatment even if refusal risks harm',
        [
            'Forced treatment for any disagreement',
            'Waiving all privacy forever',
            'Mandatory experimental drugs',
        ],
        'Competent adults may refuse recommended care. Choosing Forced treatment for any disagreement is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'What does Professional boundary violations in healthcare include?',
        'Inappropriate personal relationships with patients',
        [
            'Using interpreters',
            'Offering education materials',
            'Scheduling follow-up',
        ],
        'Professional boundaries protect patients. Choosing Using interpreters is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'What is Battery in a healthcare context?',
        'Unwanted touching or treatment without valid consent',
        [
            'Only verbal insults',
            'Billing errors only',
            'Late appointments',
        ],
        'Unauthorized treatment can be battery even if well intended. Choosing Only verbal insults is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'What is Fraud in healthcare billing?',
        'Illegal misrepresentation for financial gain',
        [
            'A clerical typo once',
            'Normal discounting',
            'Required for Medicare',
        ],
        'Intentional deception is unlawful. Choosing A clerical typo once is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'When uncertain about legality of a requested action, the MA should?',
        'Seek guidance from supervisor, compliance, or provider before proceeding',
        [
            'Proceed to avoid delay',
            'Ask uninvolved patients',
            'Post question on social media',
        ],
        'Compliance resources clarify legal boundaries. Choosing Proceed to avoid delay is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'Workplace harassment policy should?',
        'Define reporting pathways and prohibit retaliation',
        [
            'Encourage intimidation',
            'Delete complaints automatically',
            'Require victims to stay silent',
        ],
        'Safe reporting supports respectful workplaces. Choosing Encourage intimidation is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'A HIPAA breach may require?',
        'Risk assessment and notification per federal/state rules',
        [
            'No action ever',
            'Posting details online',
            'Sharing with unauthorized staff',
        ],
        'Breaches follow defined response steps. Choosing No action ever is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'Good Samaritan laws generally?',
        'Protect certain voluntary emergency aid in good faith',
        [
            'Require MAs to practice outside license everywhere',
            'Eliminate documentation',
            'Waive all standards',
        ],
        'Laws vary by state; know local rules. Choosing Require MAs to practice outside license everywhere is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'Minors may consent to certain services without parental consent when?',
        'State law allows (e.g., some reproductive or mental health services)',
        [
            'Never under any circumstance',
            'Whenever the minor wants surgery for fun',
            'Only if parent is in waiting room',
        ],
        'Consent laws vary by state and service. Choosing Never under any circumstance is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'State Good Samaritan statutes for lay rescuers typically?',
        'Limit civil liability when emergency aid is given in good faith without gross negligence',
        [
            'Protect intentional harm',
            'Apply to billing fraud',
            'Eliminate documentation requirements in clinic',
        ],
        'Laws vary by state; intent and setting matter. Choosing Protect intentional harm is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'The False Claims Act concerns?',
        'Fraudulent billing to government programs',
        [
            'Tube draw order',
            'Hand hygiene',
            'Injection sites',
        ],
        'Submitting false claims is illegal. Choosing Tube draw order is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

