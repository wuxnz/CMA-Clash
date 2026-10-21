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
            'Breaking confidentiality when a patient shares sensitive information in trust',
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
            'Omitting patient teaching because it takes extra time',
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
            'Defer reporting new side effects if the patient seems uncomfortable complaining',
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
            'Emphasize benefits while omitting discussion of complications',
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
            'Clinic letterhead on the handout satisfies copyright when no patient names appear',
            'Fair use permits copying publisher content used solely inside the practice',
            'HIPAA privacy rules eliminate the need for publisher permission on handouts',
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
            'The spouse automatically gains decision authority even when another agent is named',
            'The agent may override a valid living will in every circumstance nationwide',
            'Clinical staff may waive informed consent whenever an agent is listed in the chart',
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
            'It authorizes the agent to pay medical bills from the patient\'s retirement accounts',
            'It remains valid solely for inpatient stays and ends at routine discharge',
            'It allows the agent to sign employment contracts for clinical staff at the facility',
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
            'A parent declining one vaccine after counseling when the child appears well cared for',
            'An older adult refusing home health aides despite family disagreement',
            'A school-age child with fever and cough consistent with a viral upper respiratory infection',
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
            'Leave results on the patient portal without confirming confidential minor consent rules',
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
            'Capture preferred appointment times to streamline front-desk scheduling',
            'List current insurance copay amounts for common office visit codes',
            'Record laboratory reference intervals for routine chemistry panels used in clinic',
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
            'Delete the entire electronic note and recreate it as if the error had not occurred',
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
            'The minor may not receive outpatient care without a parent present',
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
            'Omit repeat vitals because the patient says they feel fine',
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
            'Ask other staff to monitor the coworker without notifying leadership',
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
            'The estimated patient financial responsibility detailed on the billing statement alone',
            'A written assurance that the procedure will produce a specific cosmetic outcome',
            'Printed names of each surgical team member who may enter the operating room that day',
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
            'Delivering premium services to personal friends of the staff',
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
            'Reserve vaccine for patients who pay the highest cash fee',
            'Select recipients based on staff members\' personal preferences',
            'Bypass triage protocols and vaccinate whoever arrives first regardless of risk',
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
            'Parents arguing in the waiting room about who will drive the child home after the visit',
            'A competent adult refusing dietitian referral while otherwise engaged in care',
            'A viral upper respiratory illness with cough and congestion but no safety concern',
        ],
        'Mandatory reporting laws focus on protecting vulnerable people from harm. Billing disagreements, appearance choices, and routine minor illness are not abuse-reporting triggers.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-026
    fact(
        'ccma-law-ethics',
        'After forming reasonable suspicion of abuse, what does mandatory reporting law typically require?',
        'Promptly notify the state-designated child or adult protective services agency per statute',
        [
            'Wait until the alleged abuser agrees to a family meeting',
            'Report when the patient pays outstanding balances in full',
            'Limit reports to inpatient hospitals and exclude outpatient clinics',
        ],
        'Mandated reporters must follow written facility policy and state timelines for agency contact. Delaying for convenience, billing disputes, or care setting alone can violate the law and leave vulnerable people at risk.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-027
    fact(
        'ccma-law-ethics',
        'A 16-year-old requests confidential pregnancy testing where state minor-consent law applies. Who may legally authorize that care?',
        'The minor, within the services and limits defined by state statute',
        [
            'Any friend of the family who drove the patient to the clinic',
            'No one, because all minors need a parent signature for every test',
            'Front-desk staff acting without provider involvement',
        ],
        'Many states permit minors to consent to specific sensitive services. Parental presence is not always required, but the scope is statutory rather than open-ended and is not delegable to unqualified staff.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-028
    fact(
        'ccma-law-ethics',
        'In a civil negligence claim against a clinic, which four elements must generally be proven?',
        'Duty, breach of duty, causation, and compensable damages',
        [
            'Patient dissatisfaction alone without injury',
            'A charting typo that caused no harm to the patient',
            'Proof that the defendant intended to injure the patient',
        ],
        'Professional negligence focuses on whether care fell below the standard and caused injury. Anger, harmless errors, and deliberate intent describe other legal theories, not the usual malpractice framework.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-029
    fact(
        'ccma-law-ethics',
        'A decisionally capable adult refuses a blood transfusion recommended for anemia. How should the team respond?',
        'Respect the refusal after ensuring informed discussion and documenting the decision',
        [
            'Proceed with the transfusion because the provider ordered it',
            'Withhold all future care until the patient changes their mind',
            'Tell the patient they lose all privacy rights if they refuse',
        ],
        'Autonomy allows competent patients to decline even life-sustaining treatment. Overriding a clear refusal or punishing the patient undermines ethical care and may constitute battery.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-030
    fact(
        'ccma-law-ethics',
        'A patient asks the medical assistant to adjust a medication dose without provider approval. What governs whether the MA may perform that task?',
        'State scope-of-practice rules and the supervising provider\'s delegation policy',
        [
            'Whatever the patient prefers if they sign a waiver',
            'Verbal instructions from a family member who works in another clinic',
            'The MA\'s personal comfort level with medications',
        ],
        'Medical assistants work under licensed supervision with tasks defined by law and employer policy. Patient requests and informal tips do not expand legal authority to practice medicine.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-031
    fact(
        'ccma-law-ethics',
        'Under the federal physician self-referral law known as Stark, what arrangement is broadly prohibited?',
        'Physician self-referral of Medicare or Medicaid patients to entities with a financial relationship for designated health services',
        [
            'Routing federally insured patients to an imaging center the physician partly owns without a regulatory exception',
            'Ordering designated health services from a laboratory in which the referring physician holds a financial interest',
            'Directing Medicare beneficiaries to a compounding pharmacy partly owned by the ordering physician for related DHS',
        ],
        'Stark targets financial conflicts in self-referral for DHS such as imaging or lab services. Routine clinical care and safety practices are not the focus of the statute.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-032
    fact(
        'ccma-law-ethics',
        'What does the federal Anti-Kickback Statute make unlawful?',
        'Offering or receiving remuneration to induce referrals or purchases paid by federal health care programs',
        [
            'Accepting fair market value rent under a lease that meets a regulatory safe harbor',
            'Paying bona fide employees their regular hourly wages for documented clinical work',
            'Receiving accredited continuing medical education with no required referral volume',
        ],
        'The Anti-Kickback Statute bars remuneration meant to steer federal-program referrals or purchases. Safe-harbor leases, ordinary wages, and compliant education are commonly lawful; inducements tied to referral volume are not.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-033
    fact(
        'ccma-law-ethics',
        'Billing Medicare for services that were never performed primarily implicates which federal law?',
        'The False Claims Act and related program integrity rules',
        [
            'The federal Anti-Kickback Statute governing inducements tied to program referrals and purchases',
            'The physician self-referral restrictions commonly known as the Stark Law for designated health services',
            'The Civil Monetary Penalties Law addressing beneficiary inducements in federal health programs',
        ],
        'Knowingly submitting false claims for government payment can trigger civil penalties and exclusion. Kickback, Stark, and beneficiary-inducement laws address different fraud and conflict issues than billing for services never rendered.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-034
    fact(
        'ccma-law-ethics',
        'Which situation most clearly meets the threshold for a mandated abuse report?',
        'Pattern of unexplained bruises in a dependent adult with a credible disclosure of hitting',
        [
            'A caregiver insisting on staying in the exam room during a routine well visit without other concerns',
            'A teenager requesting a same-gender provider for modesty during a sports physical',
            'An adult with a documented viral illness, congestion, and low-grade fever without injury',
        ],
        'Mandatory reporting turns on reasonable suspicion of abuse or neglect, not billing friction or routine illness. Document objective findings and follow agency reporting procedures immediately.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-035
    fact(
        'ccma-law-ethics',
        'Which behavior is an example of a professional boundary violation?',
        'Starting a romantic relationship with a patient currently under the team\'s care',
        [
            'Using a qualified medical interpreter for a non-English-speaking patient',
            'Offering written discharge instructions at an appropriate literacy level',
            'Showing calm empathy when a patient receives difficult news',
        ],
        'Boundaries keep the clinical relationship focused on the patient\'s needs. Appropriate communication tools, education, and compassion support care without exploiting trust.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-036
    fact(
        'ccma-law-ethics',
        'What does the ethical principle of patient self-determination protect?',
        'The competent patient\'s right to accept or refuse treatment, even when refusal may worsen health outcomes',
        [
            'Requiring participation in an available research protocol before routine care continues',
            'Conditioning future treatment on a blanket waiver of all privacy protections',
            'Allowing unrestricted review of other patients\' charts for personal curiosity',
        ],
        'Self-determination respects informed choice. Coerced research, blanket privacy waivers, and snooping in unrelated charts violate autonomy and often violate law.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-037
    fact(
        'ccma-law-ethics',
        'A long-term patient offers expensive gifts to a medical assistant every visit. What is the most appropriate response?',
        'Decline or follow facility policy on gifts and keep the relationship professional',
        [
            'Accept all gifts because refusal might hurt the patient\'s feelings',
            'Accept frequent home-cooked meals during every office visit',
            'Agree to provide care when gifts are received',
        ],
        'Accepting substantial gifts or blurring personal lines can create undue influence and boundary problems. Policies help staff respond consistently without abandoning courteous care.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-038
    fact(
        'ccma-law-ethics',
        'In health care law, battery most often refers to which action?',
        'Performing a procedure or touching a patient without valid consent or legal authority',
        [
            'Raising your voice to match the patient without seeking assistance',
            'Submitting an incorrect insurance code with no patient contact',
            'Running fifteen minutes behind schedule on a busy clinic day',
        ],
        'Battery is unauthorized physical contact or treatment. Verbal insults alone, billing mistakes without touching, and scheduling delays are not battery, though they may raise other concerns.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-039
    fact(
        'ccma-law-ethics',
        'Which billing practice best illustrates health care fraud rather than an innocent mistake?',
        'Knowingly upcoding visit levels to increase reimbursement without supporting documentation',
        [
            'Correcting a single typographical error before claim submission',
            'Applying a contracted discount shown in the payer fee schedule',
            'Charging a statutory copayment amount listed in the patient\'s plan',
        ],
        'Fraud involves intentional deception for gain. Good-faith corrections, contracted rates, and required patient cost sharing differ from deliberate misrepresentation.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-040
    fact(
        'ccma-law-ethics',
        'A supervisor asks the medical assistant to perform a task that may exceed scope of practice. What is the best first step?',
        'Pause, clarify duties with the supervisor or compliance officer, and follow written policy',
        [
            'Complete the task immediately to avoid slowing the schedule',
            'Poll waiting-room patients about whether the task seems legal',
            'Ask the patient waiting next in line whether the task seems appropriate',
        ],
        'When legality or scope is unclear, use internal escalation paths. Rushing, informal crowdsourcing, or public posts can increase patient risk and personal liability.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-041
    fact(
        'ccma-law-ethics',
        'An effective workplace anti-harassment policy should include which feature?',
        'Clear reporting channels and protection against retaliation for good-faith complaints',
        [
            'Automatic deletion of all harassment complaints after twenty-four hours',
            'A requirement that victims confront harassers alone with no support',
            'Permission for managers to punish employees who report concerns',
        ],
        'Policies should encourage early reporting and fair investigation. Destroying complaints, isolating victims, or retaliating undermines safety and may violate employment law.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-042
    fact(
        'ccma-law-ethics',
        'After discovering unsecured PHI was emailed to the wrong patient, which step belongs in the privacy officer\'s response process?',
        'Conduct a risk assessment and follow breach notification rules if required',
        [
            'Ignore the event if the recipient promises not to look',
            'Publish the patient\'s diagnosis on the clinic website to warn others',
            'Forward the misdirected message to all staff for discussion',
        ],
        'HIPAA breach response is structured: contain harm, evaluate risk, document, and notify individuals or regulators when thresholds are met. Secrecy, public disclosure, and internal gossip worsen the violation.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-043
    fact(
        'ccma-law-ethics',
        'While off duty, a medical assistant stops at a crash scene and provides basic first aid in good faith. Good Samaritan laws generally aim to do what?',
        'Offer limited civil liability protection for voluntary emergency assistance that is not grossly negligent',
        [
            'Authorize unlicensed persons to practice full medicine in any setting',
            'Eliminate the need to call emergency services or document events',
            'Waive all professional standards during routine clinic visits',
        ],
        'Good Samaritan statutes vary by state and usually apply to emergent, voluntary aid outside normal employment. They do not replace licensure in the workplace or excuse reckless care.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-044
    fact(
        'ccma-law-ethics',
        'When state law allows a minor to consent to mental health counseling, what must the clinic still maintain?',
        'Confidentiality of visit information within legal limits and the facility privacy policy',
        [
            'Automatic disclosure of all session content to parents without reviewing statute',
            'Refusal of any mental health referral for patients under eighteen',
            'Posting appointment times on a public bulletin board',
        ],
        'Minor-consent statutes define who may authorize care and what may be shared. Blanket parental notification or public exposure of visits can breach law and destroy trust.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-045
    fact(
        'ccma-law-ethics',
        'How do most state Good Samaritan statutes treat a lay rescuer who intentionally causes harm while pretending to help?',
        'They do not shield deliberate or grossly negligent conduct',
        [
            'They immunize any action regardless of intent or recklessness',
            'They apply to fraudulent Medicare billing disputes',
            'They remove all medical record documentation requirements in clinics',
        ],
        'Protections target good-faith emergency aid, not malice or reckless behavior. Billing fraud and routine documentation rules fall outside Good Samaritan purpose.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-046
    fact(
        'ccma-law-ethics',
        'Under the False Claims Act, what may happen when someone knowingly submits false bills to a federal health care program?',
        'Civil penalties, treble damages in some cases, and potential exclusion from programs',
        [
            'Automatic immunity whenever any billing typo appears on a claim',
            'Regulation of hand hygiene technique during routine vital signs',
            'Mandatory discipline for incorrect specimen tube order of draw',
        ],
        'Program integrity laws target intentional false claims, not benign lab technique debates. Penalties can be severe and include repayment multiples and loss of billing privileges.',
        [S.NHA_CCMA],
        'advanced',
    ),

    # ccma-law-ethics-047
    fact(
        'ccma-law-ethics',
        'What are the core elements of valid informed consent for a procedure?',
        'Disclosure, comprehension, voluntariness, and capacity to decide',
        ['A signature obtained while the patient is sedated without prior discussion',
        'Payment in full before any explanation',
        'Staff preference for morning appointments'],
        'Consent is a process, not just a form. Sedation without prior discussion undermines comprehension and voluntariness.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-048
    fact(
        'ccma-law-ethics',
        'A coworker asks you to document care you did not observe. What is the ethical response?',
        'Refuse and report per facility policy because falsification is fraudulent',
        ['Sign to avoid conflict and fix it later',
        'Add vague wording so no one can verify',
        'Chart for them because they are busy'],
        'Accurate documentation is a legal record. Signing for unobserved care is falsification and exposes patients and staff to harm.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-049
    fact(
        'ccma-law-ethics',
        'What is the role of a medical assistant regarding scope of practice?',
        'Perform delegated tasks allowed by state law and supervising provider policy',
        ['Diagnose complex disease independently',
        'Prescribe schedule II opioids without oversight',
        'Interpret imaging studies for treatment plans'],
        'MA scope is limited and supervised. Independent diagnosis and prescribing exceed typical MA authority in most states.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-050
    fact(
        'ccma-law-ethics',
        'A patient who is alert and oriented refuses a recommended blood draw. What should be documented?',
        'The refusal, education provided, and notification of the provider',
        ['That the patient was forced for their own good',
        'Nothing because refusal ends the visit',
        'Another patient\'s decision template'],
        'Competent adults may refuse care; documentation supports continuity and legal clarity. Forced draws without due process violate autonomy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-051
    fact(
        'ccma-law-ethics',
        'What is fidelity in health care ethics?',
        'Keeping promises and being faithful to professional duties',
        ['Maximizing revenue regardless of need',
        'Sharing confidential information for entertainment',
        'Performing tasks outside training without telling anyone'],
        'Fidelity supports reliability and trust in the patient relationship. Revenue focus or unauthorized practice violates ethical duties.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-052
    fact(
        'ccma-law-ethics',
        'Which situation may trigger mandatory reporting obligations?',
        'Reasonable suspicion of child abuse based on exam findings',
        ['A patient arriving late to an appointment',
        'Disagreement about copay amount',
        'Request for a different brand of bandage'],
        'State laws require reporting suspected abuse of vulnerable populations. Scheduling and supply preferences are not reportable events.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-053
    fact(
        'ccma-law-ethics',
        'What does justice mean in health care ethics?',
        'Fair distribution of benefits and burdens of care',
        ['Treating friends before other patients regardless of need',
        'Hiding errors to protect the clinic image',
        'Charging random fees without policy'],
        'Justice supports equitable access and triage by need. Favoritism and concealment violate ethical principles.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-054
    fact(
        'ccma-law-ethics',
        'A patient signs an advance directive refusing mechanical ventilation. The family demands intubation anyway. What guides the team?',
        'The patient\'s documented wishes if valid under state law',
        ['The loudest family member\'s preference',
        'Staff convenience',
        'Billing potential'],
        'Valid advance directives express patient autonomy. Family wishes matter for surrogate decisions when the patient lacks capacity, but documented refusals control when applicable.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-055
    fact(
        'ccma-law-ethics',
        'What is the purpose of an incident report after a patient fall?',
        'Support quality improvement and track safety trends',
        ['Assign blame in the medical record',
        'Replace required medical documentation',
        'Hide events from risk management'],
        'Incident reports analyze systems; they do not substitute for charting care provided. Concealment violates policy and ethics.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-056
    fact(
        'ccma-law-ethics',
        'Accepting a large cash gift from a patient seeking preferential scheduling raises concerns about what ethical issue?',
        'Professional boundaries and undue influence',
        ['Improved infection control',
        'Better EKG electrode adhesion',
        'Accurate blood typing'],
        'Gifts can compromise impartial care and violate policy. Clinical tests are unrelated to scheduling favors.',
        [S.NHA_CCMA],
        'advanced',
    ),
]
