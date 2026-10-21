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
            'Avoid harming the patient even when beneficial treatment carries known risks',
            'Honor the patient\'s right to refuse recommended care after adequate disclosure',
            'Distribute clinic resources fairly when not every patient can be seen the same day',
        ],
        'Beneficence is an active duty to promote the patient\'s welfare. Avoiding harm describes nonmaleficence; honoring refusal reflects autonomy; fair allocation reflects justice.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-002
    fact(
        'ccma-law-ethics',
        'What does fidelity mean as an ethical obligation in patient care?',
        'Keeping promises and honoring professional duties to patients and employers',
        [
            'Promoting patient welfare through truthful education about treatment options',
            'Avoiding unnecessary risk when a procedure has known complications',
            'Allocating limited appointment slots fairly among patients with similar acuity',
        ],
        'Fidelity is faithfulness to duties and commitments. Beneficence focuses on promoting welfare; nonmaleficence on avoiding harm; justice on fair distribution.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-003
    fact(
        'ccma-law-ethics',
        'Which statement best defines nonmaleficence in clinical practice?',
        'Avoiding actions that cause unnecessary harm to the patient',
        [
            'Actively promoting the patient\'s welfare through beneficial interventions',
            'Honoring informed refusal after the patient understands the risks of declining care',
            'Distributing scarce vaccines using published priority tiers during a shortage',
        ],
        'Nonmaleficence means avoiding unnecessary harm. Beneficence emphasizes doing good; autonomy respects choice; justice addresses fair allocation of resources.',
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
            'Obtain family consent when the patient is decisionally capable but undecided',
            'Proceed with urgent care after explaining benefits when the patient remains silent',
            'Document the recommended plan and treat unless the patient objects in writing',
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
            'Document only the corrected dose in the chart without noting the original error',
            'Complete the report but omit the patient notification step that occurred',
            'File the report with the risk manager after discussing fault with the patient in the room',
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
            'Provide a summary handout and treat consent as implied if the patient nods agreement',
            'Ask the family to sign when the patient is capable but prefers not to read the form',
            'Obtain signature during check-in before the provider explains risks and alternatives',
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
            'To route routine scheduling complaints to the billing department anonymously',
            'To document minor workflow frustrations without a compliance review pathway',
            'To report coworker interpersonal conflicts that do not involve policy or fraud concerns',
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
            'Mention the lab only if the patient asks how send-out testing is chosen',
            'List every send-out option equally while omitting the ownership interest',
            'Defer to the front desk to select the default lab without provider discussion',
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
            'A signed form after a brief verbal summary when the patient declines questions',
            'Agreement documented when the patient signs to avoid delaying the surgical schedule',
            'Witnessed signature with risks listed on the form but not discussed aloud',
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
            'Honoring informed refusal after the patient understands the risks of declining care',
            'Avoiding unnecessary harm when a beneficial treatment has known side effects',
            'Keeping promises to follow through on commitments made to patients during the visit',
        ],
        'Justice focuses on fairness in distributing care and burdens. Autonomy, nonmaleficence, and fidelity describe other core ethical principles.',
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
            'Transfuse when the hemoglobin is critically low despite a documented refusal',
            'Ask the spouse to overrule the patient\'s written refusal after counseling',
            'Continue the infusion while the patient is sedated for an unrelated procedure',
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
        'Which physician action most likely violates the federal physician self-referral law (Stark)?',
        'Referring a Medicare patient for MRI at an imaging center in which the physician has an ownership interest without a regulatory exception',
        [
            'Referring a patient to an unaffiliated laboratory where the physician has no financial relationship',
            'Accepting fair market value rent from a hospital under a lease that meets a regulatory safe harbor',
            'Paying bona fide employee wages for documented clinical work that is not tied to referral volume',
        ],
        'Stark restricts physician self-referral for designated health services when a financial relationship exists unless an exception applies. Unrelated referrals, compliant leases, and ordinary wages are not the prohibited arrangement described here.',
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
        'Beginning a romantic or sexual relationship with a patient who is still under the care team\'s active treatment',
        [
            'Using a qualified medical interpreter when language barriers affect consent and discharge teaching',
            'Providing written after-visit instructions at an appropriate literacy level with teach-back',
            'Declining a patient\'s gift that exceeds the amount allowed in the facility\'s written gift policy',
        ],
        'Romantic or sexual relationships with current patients exploit the therapeutic relationship and are boundary violations. Interpreters, literacy-appropriate teaching, and following gift policy are appropriate professional behaviors, not violations.',
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
            'A single anonymous mailbox with no defined investigation timeline or roles',
            'Training that defines harassment but omits how employees may report concerns',
            'A policy that encourages reports but allows supervisors to reassign complainants without review',
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
            'Extend the same immunity to paid clinical duties performed during a scheduled shift',
            'Remove the duty to act when a trained responder is already on scene',
            'Protect routine clinic care when no emergency is present',
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
        'Disclosure of material risks and benefits, patient comprehension, voluntary agreement, and decision-making capacity',
        [
            'A witnessed signature after a family member explains the procedure instead of the licensed provider',
            'A signed form after risks are listed on paper but not discussed when the patient declines questions',
            'Documented agreement obtained during registration before the clinical indication is reviewed with the patient',
        ],
        'Valid consent is more than a signature: the patient needs adequate disclosure, understanding, freedom from coercion, and capacity. Forms signed without discussion or before clinical review do not meet those elements.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-048
    fact(
        'ccma-law-ethics',
        'A coworker asks you to document care you did not observe. What is the ethical response?',
        'Refuse and report per facility policy because falsification is fraudulent',
        [
            'Sign after the coworker promises to complete the task before the end of the shift',
            'Document care in general terms without stating you did not observe the intervention',
            'Enter the vitals the coworker reports verbally without verifying at the bedside',
        ],
        'Accurate documentation is a legal record. Signing for unobserved care is falsification and exposes patients and staff to harm.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-049
    fact(
        'ccma-law-ethics',
        'What is the role of a medical assistant regarding scope of practice?',
        'Perform delegated tasks allowed by state law and supervising provider policy',
        [
            'Triage walk-in patients and document a working diagnosis before provider review',
            'Renew schedule II prescriptions when the patient reports running out over the weekend',
            'Interpret chest imaging and initiate treatment when the radiology report is delayed',
        ],
        'MA scope is limited and supervised. Independent diagnosis and prescribing exceed typical MA authority in most states.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-050
    fact(
        'ccma-law-ethics',
        'A patient who is alert and oriented refuses a recommended blood draw. What should be documented?',
        'The patient\'s refusal, education provided about the draw, and notification of the licensed provider',
        [
            'That the patient agreed after family persuaded them without documenting the conversation in the chart',
            'Only the laboratory order cancellation without noting the patient\'s stated reason for declining',
            'A generic refusal checkbox without recording teaching offered or provider notification steps taken',
        ],
        'Competent adults may refuse a blood draw; the chart should show what was explained, that refusal was voluntary, and that the provider was informed. Silent cancellation or incomplete checkboxes leave legal and clinical gaps.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-051
    fact(
        'ccma-law-ethics',
        'What is fidelity in health care ethics?',
        'Keeping promises and being faithful to professional duties to patients and employers',
        [
            'Promoting beneficial outcomes through honest patient education about treatment plans',
            'Avoiding treatment risks even when potential benefit outweighs known complications',
            'Treating patients with similar needs equitably when clinic resources are limited',
        ],
        'Fidelity is reliability and honoring commitments. Beneficence, nonmaleficence, and justice describe different core ethical duties.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-052
    fact(
        'ccma-law-ethics',
        'Which situation may trigger mandatory reporting obligations?',
        'Reasonable suspicion of child abuse based on exam findings',
        [
            'A caregiver insisting on staying in the exam room during a routine well visit',
            'A teenager requesting confidential STI screening where minor consent applies',
            'An adult refusing dietitian referral while otherwise engaged in care',
        ],
        'State laws require reporting suspected abuse of vulnerable populations. Scheduling and supply preferences are not reportable events.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-053
    fact(
        'ccma-law-ethics',
        'What does justice mean in health care ethics?',
        'Fair distribution of benefits and burdens of care among patients and populations',
        [
            'Keeping commitments to patients by following through on promised callbacks',
            'Avoiding unnecessary harm when a treatment carries known complication risks',
            'Promoting welfare by recommending interventions that offer net benefit to the patient',
        ],
        'Justice addresses equitable distribution of care and resources. Fidelity, nonmaleficence, and beneficence name different foundational ethical duties.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-law-ethics-054
    fact(
        'ccma-law-ethics',
        'A patient signs an advance directive refusing mechanical ventilation. The family demands intubation anyway. What guides the team?',
        'The patient\'s documented wishes if valid under state law',
        [
            'The unanimous preference of adult children when the patient lacks capacity',
            'The attending physician\'s routine practice when no directive is on file',
            'The hospital\'s default full-code policy when family disagrees but the patient is incapacitated',
        ],
        'Valid advance directives express patient autonomy. Family wishes matter for surrogate decisions when the patient lacks capacity, but documented refusals control when applicable.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-law-ethics-055
    fact(
        'ccma-law-ethics',
        'What is the purpose of an incident report after a patient fall?',
        'Support quality improvement by documenting objective fall facts for trend review and systems fixes',
        [
            'Document only subjective opinions about staff fault inside the legal medical record narrative',
            'Complete the incident report instead of charting the fall assessment and interventions provided',
            'File the incident report only if the patient requests compensation or threatens litigation',
        ],
        'Incident reports feed safety analysis separate from blaming individuals in the chart. They supplement, rather than replace, documentation of assessment and care after a fall.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-law-ethics-056
    fact(
        'ccma-law-ethics',
        'Accepting a large cash gift from a patient seeking preferential scheduling raises concerns about what ethical issue?',
        'Professional boundaries and undue influence on impartial care decisions',
        [
            'Beneficence when the gift is used to fund patient transportation vouchers',
            'Nonmaleficence when staff worry about offending the donor by declining the gift',
            'Justice when the patient also refers friends to the practice without requesting favors',
        ],
        'Large gifts tied to scheduling favors can blur boundaries and unduly influence care decisions. Beneficence, nonmaleficence, and routine referrals do not capture the boundary and influence problem created by cash for preferential access.',
        [S.NHA_CCMA],
        'advanced',
    ),
]
