# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-communication)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-communication-001
    fact(
        'ccma-communication',
        'How should a medical assistant answer a call at the front desk to meet professional standards?',
        'State the facility name and your role, then offer assistance',
        [
            'Share protected health information before verifying the caller\'s identity',
            'Open the call with personal opinions about clinic policy',
            'Refuse to identify the practice when asked who is calling',
        ],
        'Clear identification shows callers they reached the correct office and sets a respectful tone. Offering help invites the caller to state their need while you follow privacy rules for any clinical details.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-002
    fact(
        'ccma-communication',
        'A patient has waited past the scheduled appointment time. What is the best way to apologize while staying professional?',
        'Acknowledge the inconvenience and give a realistic update on timing',
        [
            'Tell the patient the delay is their fault for arriving early',
            'Guarantee an exact rooming time you cannot control when documented per facility policy.',
            'Avoid mentioning the wait until the patient complains loudly',
        ],
        'Validating frustration shows respect without making promises the team cannot keep. Blaming the patient or staying silent usually increases conflict in the waiting area.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-003
    fact(
        'ccma-communication',
        'Which approach best reflects customer service expectations in an outpatient medical setting?',
        'Courtesy, respect, and timely follow-through on requests',
        [
            'Keeping every interaction brief even when patients need clarification',
            'Routing all complaints to voicemail without acknowledgment',
            'Prioritizing throughput over privacy when rooms are full',
        ],
        'Positive interactions support trust and adherence to the plan of care. Sales pressure and confidentiality breaches undermine the therapeutic relationship patients expect in healthcare.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-004
    fact(
        'ccma-communication',
        'When teaching a patient with limited health literacy, how should you present new information?',
        'Use plain language and define necessary medical terms',
        [
            'Rely on Latin prescription abbreviations without explanation',
            'Hand the patient a journal article with no summary',
            'Speak as if every adult reads at a college level',
        ],
        'Clear wording and teach-back improve understanding and reduce errors at home. Unexplained jargon and assumptions about reading level leave gaps in safety-critical instructions.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-005
    fact(
        'ccma-communication',
        'A patient in the waiting room is angry about a long delay. What should the medical assistant do first?',
        'Acknowledge the patient\'s feelings and provide periodic updates',
        [
            'Seat the patient last because they arrived before their slot time',
            'Promise an exact rooming time you cannot guarantee',
            'Ask the patient not to speak to other waiting patients about the delay',
        ],
        'De-escalation begins with empathy and transparent communication about what the team is doing. Arguing or sharing other patients\' information violates privacy and worsens the situation.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-006
    fact(
        'ccma-communication',
        'Which behaviors demonstrate active listening during a patient interview?',
        'Attend fully, ask clarifying questions, and reflect key points without interrupting',
        [
            'Rehearse your next reply while the patient is speaking',
            'Use complex jargon without checking comprehension when documented per facility policy.',
            'Turn away from the patient to finish computer entries',
        ],
        'Active listening confirms the patient\'s story and builds rapport. Divided attention or interrupting sends a message that the patient\'s concerns are not important.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-007
    fact(
        'ccma-communication',
        'Which examples belong to nonverbal communication in a clinical encounter?',
        'Eye contact, posture, and facial expression',
        [
            'Tone and pace of voice during the interview',
            'Written after-visit summaries given at checkout',
            'Printed consent forms the patient signs',
        ],
        'Nonverbal cues shape how patients interpret warmth and competence. Written documentation and laboratory data are clinically important but are not examples of nonverbal communication.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-008
    fact(
        'ccma-communication',
        'Which nonverbal behaviors help build rapport with a patient during an office visit?',
        'Appropriate eye contact and open posture at the patient\'s eye level when possible',
        [
            'Turn your back while the patient is describing symptoms',
            'Stand close above the seated patient with arms crossed when documented per facility policy.',
            'Read text messages while the patient discloses sensitive information',
        ],
        'Open, attentive body language signals that you are present for the conversation. Dismissive posture or divided attention can make patients withhold important details.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-009
    fact(
        'ccma-communication',
        'During a therapeutic conversation, what does active listening require from the medical assistant?',
        "Reflect and clarify the patient's message before responding with instructions",
        [
            'Interrupt frequently to shorten the visit in a typical outpatient clinic setting.',
            'Form your answer while the patient is still talking',
            'Face the computer screen instead of the patient',
        ],
        'Reflection checks that you understood concerns and priorities before giving directions. Rushing or planning a reply in advance misses cues that affect education and follow-up.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-010
    fact(
        'ccma-communication',
        'When you first approach a visibly anxious patient, what communication step is most appropriate?',
        'Acknowledge the patient\'s feelings and speak in a calm, steady tone',
        [
            'Label the patient\'s worries as unreasonable and move on',
            'Speak louder to assert control over the room when documented per facility policy.',
            'Leave the room without telling the patient what will happen next',
        ],
        'Calm validation reduces physiologic arousal and improves cooperation with procedures. Dismissal or abrupt exits increase fear and may trigger escalation.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-011
    fact(
        'ccma-communication',
        'Why should you use open-ended questions when beginning a history of present illness?',
        'They let the patient describe concerns in their own words',
        [
            'They restrict answers to yes or no for speed',
            'They require interrupting every few seconds to stay on time',
            'They replace the need to ask any follow-up questions',
        ],
        'Open questions surface symptoms and context the chart may not show. Overusing closed questions can miss the patient\'s main worry or timeline.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-012
    fact(
        'ccma-communication',
        'Which of the following best describes effective written take-home patient instructions?',
        'Short action steps in plain language, reviewed with the patient',
        [
            'Dense paragraphs copied from a specialty textbook',
            'A medication list using Latin sig codes without translation',
            'The clinic address and hours without care steps for the condition',
        ],
        'Written materials reinforce verbal teaching and support safe self-care at home. Leaving out red-flag symptoms or untaught abbreviations creates confusion during an emergency.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-013
    fact(
        'ccma-communication',
        'Under OSHA bloodborne pathogen standards, how must an Exposure Control Plan be maintained?',
        'In writing, reviewed at least annually and when job duties change',
        [
            'As an informal verbal agreement among staff in a typical outpatient clinic setting.',
            'Waived for small practices with few employees',
            'Written after the first needlestick event occurs',
        ],
        'A written plan documents engineering controls, work practices, and training for covered employees. Employers must update it when procedures or risks change, not react solely after an exposure.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-014
    fact(
        'ccma-communication',
        'When explaining a delay in lab results or scheduling, how should you phrase an apology?',
        'Express sincerity and empathy without admitting fault beyond organizational policy',
        [
            'Attribute the problem entirely to the patient\'s behavior',
            'Promise compensation or discounts you are not authorized to give',
            'Change the subject without acknowledging the wait for routine ambulatory patient care.',
        ],
        'Empathetic language preserves trust when processes break down. Overpromising or deflecting blame can create legal and service expectations the clinic cannot meet.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-015
    fact(
        'ccma-communication',
        'What is the purpose of closed-loop communication when relaying orders or critical details?',
        'Repeat key information back to confirm it was heard accurately',
        [
            'Document the conversation in the chart after the task is finished',
            'Send the order as a text message without verbal discussion',
            'Assume silence means the receiver understood correctly',
        ],
        'Read-back and teach-back catch transposed numbers, doses, and times before harm occurs. Skipping confirmation is a common root cause of handoff errors in busy settings.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-016
    fact(
        'ccma-communication',
        'Which statement best describes cultural humility in patient care?',
        "Recognizing that your own cultural lens may limit your understanding of the patient's experience",
        [
            'Treating stereotyped beliefs about a group as clinical facts in a typical outpatient clinic setting.',
            'Declining reasonable requests tied to culture or religion when documented per facility policy.',
            'Joking about a patient\'s food or dress preferences with coworkers',
        ],
        'Humility invites questions and partnership rather than assumptions about beliefs or practices. Stereotyping or ridicule erodes trust and can lead to missed needs.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-017
    fact(
        'ccma-communication',
        'How should patient communication be reflected in the medical record?',
        'Objectively, using factual wording without biased or insulting language',
        [
            'Recording personal insults when the patient was upset',
            'Leaving out direct quotes the patient provided when documented per facility policy.',
            'Entering rumors heard in the break room as facts',
        ],
        'Neutral documentation supports continuity of care and legal review. Subjective attacks or omitted patient statements weaken the record\'s credibility.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-018
    fact(
        'ccma-communication',
        'Which of the following should appear in a patient education note in the chart?',
        'Topics covered, handouts given, and patient response or teach-back',
        [
            'A checkbox marked education without listing what was taught',
            'The educator\'s personal opinion of the patient\'s motivation',
            'Procedure codes billed that day without teaching content for routine ambulatory patient care.',
        ],
        'Specific notes show what the patient was told and whether they understood. Vague entries cannot support adherence counseling or discharge planning if questions arise later.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-019
    fact(
        'ccma-communication',
        'When sending appointment reminders by email, what practice aligns with HIPAA and office policy?',
        'Use approved secure messaging systems configured for healthcare',
        [
            'Place the full Social Security number in the subject line',
            'Send routine messages from a personal unsecured email account',
            'Include vendors who are not part of the care team on patient threads',
        ],
        'Approved channels apply encryption and access controls appropriate for PHI. Personal email and unnecessary recipients increase breach risk and may violate policy.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-020
    fact(
        'ccma-communication',
        'Two team members disagree loudly about workflow in a patient care area. What is the appropriate response?',
        'Address the issue privately with respectful discussion and involve a supervisor if needed',
        [
            'Continue arguing in front of patients in the waiting room in a typical outpatient clinic setting.',
            'Give each other silent treatment while patients wait for help',
            'Ask the practice manager to settle the dispute during peak patient check-in',
        ],
        'Patients expect a calm, coordinated environment. Resolving conflict away from public view protects dignity and prevents care delays.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-021
    fact(
        'ccma-communication',
        'When a patient files a complaint about care or service, what should the medical assistant do?',
        'Document the concern objectively and route it according to facility policy',
        [
            'File the complaint with no record in the chart in a typical outpatient clinic setting.',
            'Respond by raising your voice to defend the clinic',
            'Share the complaint narrative on a public review site from work',
        ],
        'Structured complaint processes ensure leadership can investigate and improve. Retaliation or ignoring concerns can violate policy and patient rights regulations.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-022
    fact(
        'ccma-communication',
        'How should results from patient satisfaction surveys be used in a medical practice?',
        'Identify trends to improve processes while de-identifying individual responses',
        [
            'Post individual comments with patient initials on the staff board',
            'Ignore repeated themes because one score looks acceptable when documented per facility policy.',
            'Use survey data to choose which patients receive longer visits',
        ],
        'Aggregate data guides quality improvement without exposing PHI. Misusing survey content or ignoring patterns wastes a tool meant to strengthen service.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-023
    fact(
        'ccma-communication',
        'During telephone triage, how should the medical assistant\'s tone of voice sound to the caller?',
        'Clear, respectful, and steady even when the caller is upset',
        [
            'Rushed and dismissive to finish calls quickly',
            'Whispered or muffled so words are hard to understand',
            'Sarcastic when the caller repeats a question for routine ambulatory patient care.',
        ],
        'Callers often cannot see nonverbal cues, so vocal tone carries empathy and authority. Harsh or unclear speech leads to missed instructions and repeat calls.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-024
    fact(
        'ccma-communication',
        'What impression should front-desk nonverbal communication create for arriving patients?',
        'Approachability and respect for each person in line',
        [
            'Closed posture and deliberate avoidance of eye contact',
            'Checking a mobile device during every greeting',
            'Turning away from the patient while giving directions',
        ],
        'Reception is the first clinical touchpoint many patients remember. Welcoming posture encourages questions about paperwork, directions, and concerns.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-025
    fact(
        'ccma-communication',
        'In the SBAR handoff model, what does the final letter stand for?',
        'Recommendation',
        [
            'Resuscitation',
            'Regulation',
            'Referral for routine ambulatory patient care.',
        ],
        'SBAR ends with a clear recommendation so the receiver knows what action or decision is needed. The full acronym is Situation, Background, Assessment, Recommendation, not scheduling or billing terms.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-026
    fact(
        'ccma-communication',
        'What do the four letters in SBAR represent when structuring a clinical handoff?',
        'Situation, Background, Assessment, Recommendation',
        [
            'Summary, Baseline vitals, Action plan, Referral order',
            'Schedule, Billing, Accounts, and Records',
            'Symptoms, Behavior, Allergy, and Rx changes',
        ],
        'SBAR gives receivers a predictable order for urgent updates. Partial clinical or administrative mnemonics sound familiar but do not match the handoff framework taught for team communication.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-027
    fact(
        'ccma-communication',
        'In the SBAR model, which section should state the current clinical concern and level of urgency?',
        'Situation',
        [
            'Background',
            'Assessment',
            'Recommendation',
        ],
        'Situation opens with what is happening right now so the listener can triage the call or visit. Background and Assessment supply context and interpretation; Recommendation states the action requested.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-028
    fact(
        'ccma-communication',
        'Why is teach-back used after patient education?',
        'To confirm the patient can restate instructions in their own words',
        [
            'To document in the chart that teaching occurred',
            'To verify the patient agrees without repeating steps aloud',
            'To screen at future visits whether a professional interpreter will be needed',
        ],
        'Teach-back surfaces misunderstandings before the patient leaves without blaming literacy. It is a comprehension check, not chart checkbox compliance or a substitute for qualified interpretation.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-029
    fact(
        'ccma-communication',
        'Which of the following should appear in a telephone triage message left for the provider?',
        'Patient identity, callback number, symptoms, and urgency',
        [
            'Callback number and note that someone called with no symptoms',
            'Insurance ID and a billing question without clinical details',
            'Appointment date requested for a routine follow-up visit',
        ],
        'Complete messages let clinicians prioritize callbacks and document medicolegal decisions. Administrative or empty notes cannot guide treatment when symptoms and urgency are omitted.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-030
    fact(
        'ccma-communication',
        'What is the primary focus of the HIPAA Security Rule?',
        'Administrative, physical, and technical safeguards for electronic PHI',
        [
            'Minimum necessary limits on using and disclosing PHI in any format',
            'Patient rights to access, amend, and receive an accounting of disclosures',
            'Providing the written notice of privacy practices at first service',
        ],
        'The Security Rule protects ePHI on workstations, networks, and portable devices. Minimum necessary use, access rights, and privacy notices are Privacy Rule expectations, not Security Rule safeguards.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-031
    fact(
        'ccma-communication',
        'A visitor in the lobby begins shouting and moving toward the front desk. What de-escalation step aligns with workplace violence policies?',
        'Lower your voice, keep distance, and summon help if you feel threatened',
        [
            'Step close in front of them while raising your voice to redirect attention',
            'Physically block the exit yourself before security or a supervisor arrives',
            'Escort the visitor alone to a back office without calling for help first',
        ],
        'Calm tone and space reduce the chance of injury while you alert security or a supervisor. Confrontation, solo escorts, or trapping someone increases legal and safety risk.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-032
    fact(
        'ccma-communication',
        'Which behavior reflects cultural competence during patient communication?',
        'Asking how beliefs or practices might affect the plan of care',
        [
            'Relying on one cultural stereotype to predict patient preferences',
            'Offering the standard diet order without asking about restrictions',
            'Speaking louder in English when the patient seems hesitant',
        ],
        'Curiosity and respect help tailor education and scheduling without assuming values. Stereotypes, ignored dietary needs, or volume changes erode trust and can hide adherence barriers.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-033
    fact(
        'ccma-communication',
        'A patient receives the wrong appointment time because of a scheduling error. What service recovery approach is most appropriate?',
        'Apologize, correct the schedule, and explain the next steps clearly',
        [
            'Insist the printed schedule is correct and decline to offer another slot',
            'Offer the next open slot weeks away without acknowledging the error',
            'Direct the patient to self-schedule online without staff assistance',
        ],
        'Owning the error and fixing logistics rebuilds confidence in the practice. Denial or hands-off rebooking prolongs frustration and may violate service standards.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-034
    fact(
        'ccma-communication',
        'When discharging a patient with limited health literacy, which communication pair is most effective?',
        'Plain-language teaching with teach-back on medications, follow-up, and warning signs',
        [
            'Written handouts at a high reading level with abbreviations and no understanding check',
            'Teach-back on medication names while follow-up and lifestyle steps are taught with jargon',
            'Spoken-language interpreter during the visit without a written home summary in plain text',
        ],
        'Limited literacy calls for simple wording plus teach-back on the steps that keep the patient safe at home. Dense handouts without verification, partial teach-back, or interpreter-only visits leave home-care gaps.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-035
    fact(
        'ccma-communication',
        'The provider is running more than thirty minutes behind. How should staff communicate with waiting patients?',
        'Give honest delay updates and revised timing estimates when available',
        [
            'Post a sign that the provider is busy without giving estimated wait times',
            'Tell patients the delay is because they arrived before the physician was ready',
            'Ask patients to reschedule every delayed appointment without offering updates',
        ],
        'Transparent updates reduce anxiety and help patients reschedule errands or childcare. Silence or blame shifts frustration onto individuals who cannot control clinic flow.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-036
    fact(
        'ccma-communication',
        'Which example is an OSHA work practice control for bloodborne pathogen exposure?',
        'Prohibiting bending or recapping used needles by hand',
        [
            'Wearing the same pair of gloves between every patient',
            'Relying on gloves alone without hand hygiene between contacts',
            'Using puncture-resistant sharps containers as the sole exposure control',
        ],
        'Work practice controls change how tasks are performed to reduce splash and stick risk. Reusing gloves or relying on engineering controls alone undermines the Exposure Control Plan.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-037
    fact(
        'ccma-communication',
        'You sustain a needlestick while drawing blood. What should you do immediately before completing the exposure report?',
        'Wash the puncture with soap and water; flush mucous membranes with water if splashed',
        [
            'Apply antiseptic to the wound without washing with soap and water first',
            'Finish remaining patient care tasks before notifying your supervisor',
            'Delay the exposure report until the source patient is identified for routine ambulatory patient care.',
        ],
        'Prompt cleansing lowers viral load on the skin and documents the event while details are fresh. Delayed reporting or incomplete first aid can worsen outcomes and violate OSHA requirements.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-038
    fact(
        'ccma-communication',
        'A patient speaks limited English and no bilingual staff are available. What is the best communication solution?',
        'Arrange a qualified medical interpreter through approved services',
        [
            'Use a bilingual staff member\'s casual skills for full informed consent',
            'Proceed in English while speaking slowly and using gestures alone',
            'Ask the patient\'s adult companion to interpret in the waiting area',
        ],
        'Professional interpreters protect accuracy, privacy, and informed consent. Untrained bilingual staff, gestures alone, or companions may omit details needed for clinical and legal concepts.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-039
    fact(
        'ccma-communication',
        'A family member volunteers to interpret during a discussion of domestic violence screening. What should the medical assistant do?',
        'Request a qualified interpreter per policy and explain why neutrality matters',
        [
            'Accept the relative as interpreter to keep the visit on schedule',
            'Postpone the domestic violence screening until a relative can translate later',
            'Chart the encounter in English without explaining the interpreter policy',
        ],
        'Abuse disclosures require privacy and unbiased language access. Family interpreters may filter information or pressure the patient, creating safety and legal concerns.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-040
    fact(
        'ccma-communication',
        'You take an after-hours call about chest pressure and shortness of breath. What must you relay in the provider message?',
        'Caller name, callback number, symptom description, and perceived urgency',
        [
            'Callback number with a note that the caller was upset but gave no symptoms',
            'Insurance member ID and copay question without a symptom summary',
            'Time of call and request for a routine appointment next week',
        ],
        'Structured triage messages let on-call clinicians judge response time and document advice given. Administrative or incomplete notes cannot support safe callbacks for acute complaints.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-041
    fact(
        'ccma-communication',
        'A patient communicates using a speech-generating device. How should the medical assistant conduct the interview?',
        'Allow extra time, maintain eye contact, and speak directly to the patient',
        [
            'Direct every question to the accompanying caregiver instead of the patient',
            'Interrupt and rush answers before the device finishes composing text',
            'Remove the speech device temporarily to speed up vital sign collection',
        ],
        'Patients with assistive technology retain decision-making capacity and deserve direct engagement. Taking the device or ignoring the user undermines autonomy and accurate history.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-042
    fact(
        'ccma-communication',
        'After a provider shares serious test results, what communication support should remain available to the patient?',
        'Quiet time for questions and emotional processing',
        [
            'Scheduling the next visit before the patient can ask questions',
            'Handing printed handouts and leaving as soon as the provider exits',
            'Staying silent while rushing to prepare the next room',
        ],
        'Patients need space to absorb news and ask clarifying questions. Rushed handoffs or abandoning the room violate dignity when emotions are high.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-043
    fact(
        'ccma-communication',
        'An angry caller yells about a billing mistake. What is the most effective first response?',
        'Stay calm, listen, and acknowledge the concern before gathering facts',
        [
            'Transfer to billing immediately without hearing the concern in a typical outpatient clinic setting.',
            'State that refunds are against policy before gathering facts',
            'Place the caller on extended hold without explaining the next step',
        ],
        'Acknowledgment without admitting unauthorized concessions can lower tension enough to solve the problem. Abrupt transfers or policy lectures before listening worsen the complaint.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-044
    fact(
        'ccma-communication',
        'The physician is about to discuss a new cancer diagnosis. What is the appropriate role for the medical assistant?',
        'Stay within scope and offer practical support per office protocol',
        [
            'Quote long-term survival statistics beyond your training and certification',
            'Promise the patient that treatment will cure the disease',
            'Share unrelated personal stories to fill silence while the provider talks',
        ],
        'Scope-appropriate support helps the visit run smoothly while the licensed provider delivers clinical information. Speculation or false reassurance can harm trust and create liability.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-045
    fact(
        'ccma-communication',
        'Telehealth consent must be obtained for a patient who prefers Spanish. Which resource best meets regulatory expectations?',
        'A qualified interpreter connected through the facility\'s approved platform',
        [
            'Free machine translation of the consent form without human review',
            'A bilingual visitor pulled from the waiting area to read the consent form',
            'The patient\'s elementary-school child reading the English consent form aloud',
        ],
        'Qualified interpreters ensure both parties understand rights and risks in the patient\'s language. Automated tools and untrained helpers miss nuance required for valid consent.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-046
    fact(
        'ccma-communication',
        'During an in-person visit with a professional interpreter, how should you position yourself?',
        'Face the patient, speak to the patient, and pause for interpretation',
        [
            'Face the interpreter, speak toward them, and ignore the patient\'s nonverbal cues',
            'Ask a minor relative to replace the interpreter for sensitive topics',
            'Speak in long monologues without pausing for the patient to respond',
        ],
        'The therapeutic relationship stays between clinician and patient; the interpreter converts language. Ignoring the patient or blocking dialogue reduces accuracy and rapport.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-047
    fact(
        'ccma-communication',
        'Which written material best supports patients with low health literacy at discharge?',
        'Short action steps with common words and defined abbreviations',
        [
            'Peer-reviewed articles copied from a medical library',
            'Medication sig lines with unexplained Latin abbreviations',
            'Verbal teaching alone because the patient nodded that they understood',
        ],
        'Take-home sheets reinforce teaching when they use familiar language and defined terms. Academic papers, cryptic sig lines, or verbal-only teaching confuse patients managing doses at home.',
        [S.NHA_CCMA],
        'advanced',
    ),

    # ccma-communication-048
    fact(
        'ccma-communication',
        'How should a medical assistant respond when a patient says they do not understand a medication instruction?',
        'Use plain language, chunk steps, and ask the patient to repeat them back',
        [
            'Hand the patient the package insert and end the teaching session there',
            'Repeat the same medical terms more slowly without checking understanding',
            'Tell the patient the pharmacist will explain it when they pick up the drug',
        ],
        'Health literacy strategies improve adherence and safety. Volume alone does not simplify concepts; unresolved confusion should involve the care team.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-049
    fact(
        'ccma-communication',
        'Which action best supports professional telephone communication in a medical office?',
        'State the clinic name, your name or role, and offer to help',
        [
            'Ask for date of birth and account number before saying hello',
            'Transfer the caller to voicemail without identifying the practice',
            'Give your first name without stating the clinic or department',
        ],
        'Clear identification sets expectations and reduces callbacks. Requesting identifiers follows greeting and purpose; sharing other patients\' data violates privacy rules.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-050
    fact(
        'ccma-communication',
        'Which information belongs in the Situation section of an SBAR handoff?',
        'A brief statement of the acute problem and the patient\'s location',
        [
            'Background details: chronic diagnoses and medication list for context',
            'Assessment content: your working impression of the most likely cause',
            'Recommendation content: the order or decision you want the receiver to make',
        ],
        'Situation opens with what is happening now so the listener can triage. Medication history belongs in Background, clinical interpretation in Assessment, and requested action in Recommendation.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-051
    fact(
        'ccma-communication',
        'A visibly upset patient speaks loudly in the waiting room. What is an appropriate first response?',
        'Move to a private area, lower your tone, and listen for the concern',
        [
            'Address them loudly at the front desk while matching their volume',
            'Continue routine check-in tasks without acknowledging their distress',
            'Offer to discuss the issue at the front desk where others can overhear',
        ],
        'Privacy and calm communication support de-escalation. Public confrontation or comparisons escalate tension and may breach confidentiality.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-052
    fact(
        'ccma-communication',
        'Which of the following should be documented in the chart note for a patient telephone call?',
        'Caller identity, symptoms discussed, advice given, and follow-up plan',
        [
            'Staff scheduling complaints documented without any clinical content',
            'Caller phone number recorded with no symptoms or advice documented',
            'Insurance precertification status noted without triage or follow-up details',
        ],
        'Objective triage notes support liability and continuity. Administrative snippets without symptoms, advice, or follow-up fail the documentation standard for phone encounters.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-053
    fact(
        'ccma-communication',
        'How can a medical assistant show respect for cultural differences during intake?',
        'Ask about preferences that affect care while maintaining safety standards',
        [
            'Proceed in English without offering language assistance when available',
            'Use the same standard intake script for every patient regardless of context',
            'Record ethnicity in the chart but not preferences that affect care planning',
        ],
        'Cultural humility improves trust without abandoning evidence-based safety. Ignoring language access or relevant preferences erodes engagement.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-communication-054
    fact(
        'ccma-communication',
        'What is an appropriate way to clarify a provider order that seems unclear?',
        'Repeat the order back and ask for clarification before acting',
        [
            'Carry out the task using your best guess about the provider\'s intent',
            'Document the completed action first and confirm with the provider later',
            'Ask a coworker who did not hear the order what they think you should do',
        ],
        'Closed-loop communication prevents wrong-site or wrong-dose errors. Guessing or delayed confirmation bypasses the delegating provider\'s intent.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-055
    fact(
        'ccma-communication',
        'When serving patients with hearing loss, which strategy improves understanding?',
        'Face the patient and reduce background noise when possible',
        [
            'Turn away from the patient while speaking quickly toward the computer',
            'Cover your mouth with a mask or hand while giving instructions',
            'Shout medical jargon from the doorway across a noisy waiting area',
        ],
        'Visual cues and quiet environments aid lip reading and comprehension. Shouting from a distance adds noise without clarity.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-056
    fact(
        'ccma-communication',
        'Which behavior demonstrates empathy during intake?',
        'Acknowledging the patient\'s concern before moving to the next question',
        [
            'Interrupting the patient to finish the intake script within the time limit',
            'Staring at the computer screen without making eye contact during questions',
            'Telling the patient their worry is minor compared with other cases today',
        ],
        'Brief empathetic statements build rapport and may reveal safety issues. Scripted rushing reduces disclosure.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-communication-057
    fact(
        'ccma-communication',
        'During handoff to the provider, which Background detail is clinically useful for a patient with diabetes?',
        'Recent glucose readings and medication adherence',
        [
            'Chief complaint today and whether the patient arrived on time',
            'Allergies to housekeeping products used in the clinic',
            'Names of family members waiting in the reception area',
        ],
        'Background supplies context for decision making. Arrival logistics, environmental allergies, or visitor names do not replace glycemic history.',
        [S.NHA_CCMA],
        'intermediate',
    ),
]
