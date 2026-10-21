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
            'Guarantee an exact rooming time you cannot control',
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
            'Pushing optional retail products during every visit',
            'Dismissing questions about wait times as unimportant',
            'Discussing one patient\'s care where others can overhear',
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
            'Ignore the patient until security staff arrive',
            'Argue that the schedule is perfect and the patient is wrong',
            'Describe other patients\' appointment times to justify the delay',
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
            'Use complex jargon without checking comprehension',
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
            'Typed progress notes in the electronic record',
            'Numeric results on a laboratory report',
            'Insurance identification stored in the chart',
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
            'Stand close above the seated patient with arms crossed',
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
            'Interrupt frequently to shorten the visit',
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
            'Speak louder to assert control over the room',
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
        'What characteristics should written take-home patient instructions include?',
        'Clear, actionable steps reviewed aloud with the patient',
        [
            'Abbreviations the patient has not been taught',
            'Omitting warning signs that need urgent attention',
            'Relying on memory because verbal teaching is enough',
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
            'As an informal verbal agreement among staff',
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
            'Change the subject without acknowledging the wait',
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
            'Confirm the receiver knows your first name',
            'Recite unrelated billing codes for practice',
            'Proceed with handoffs without verbal confirmation',
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
            'Treating stereotyped beliefs about a group as clinical facts',
            'Declining reasonable requests tied to culture or religion',
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
            'Leaving out direct quotes the patient provided',
            'Entering rumors heard in the break room as facts',
        ],
        'Neutral documentation supports continuity of care and legal review. Subjective attacks or omitted patient statements weaken the record\'s credibility.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-communication-018
    fact(
        'ccma-communication',
        'What should documentation of patient education include?',
        'Topics taught, materials provided, and how the patient responded',
        [
            'A single note that education happened with no detail',
            'Staff opinions about the patient\'s intelligence',
            'Billing codes with no mention of teaching content',
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
            'Continue arguing in front of patients in the waiting room',
            'Give each other silent treatment while patients wait for help',
            'Post details of the disagreement on personal social media',
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
            'File the complaint with no record in the chart',
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
            'Publish responses that include names and diagnoses',
            'Discard feedback because scores are subjective',
            'Let waiting-room visitors vote on other patients\' diagnoses',
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
            'Sarcastic when the caller repeats a question',
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
            'Registration',
            'Reimbursement',
            'Radiology',
        ],
        'SBAR ends with a clear recommendation so the receiver knows what action or decision is needed. The full acronym is Situation, Background, Assessment, Recommendation—not scheduling or billing terms.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'SBAR format stands for?',
        'Situation, Background, Assessment, Recommendation',
        [
            'Schedule, Billing, Accounts, Records',
            'Safety, Blood, Air, Route',
            'Single Best Answer Response',
        ],
        'SBAR structures concise clinical communication. Choosing Schedule, Billing, Accounts, Records is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'SBAR stands for?',
        'Situation, Background, Assessment, Recommendation',
        [
            'Schedule, Billing, Accounts, Records',
            'Sterile, Bandage, Asepsis, Recovery',
            'None of these',
        ],
        'SBAR standardizes handoff communication. Choosing Schedule, Billing, Accounts, Records is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'Teach-back is used to?',
        'Confirm the patient understands instructions in their own words',
        [
            'Speed up visits by skipping questions',
            'Test reading level of the clinician',
            'Replace interpreter services',
        ],
        'Teach-back checks understanding without shaming the patient. It is not a literacy test of the staff member.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'Telephone triage messages should document?',
        'Caller name, callback number, symptoms, and urgency',
        [
            'Only the time hung up',
            'Unrelated advertisements heard',
            'Staff lunch preferences',
        ],
        'Complete messages support safe callbacks. Choosing Only the time hung up is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'The HIPAA Security Rule focuses on?',
        'Safeguards for electronic PHI',
        [
            'Only paper records',
            'Only verbal conversations',
            'Public health statistics',
        ],
        'HHS Security Rule addresses administrative, physical, and technical safeguards for ePHI. Choosing Only paper records is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'What does Conflict de-escalation may include?',
        'Lowering voice, maintaining distance, and seeking help if threatened',
        [
            'Matching aggressive behavior',
            'Blocking exits',
            'Sharing PHI to shame',
        ],
        'Safety first; follow workplace violence policy. Choosing Matching aggressive behavior is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What does Cultural competence in communication include?',
        'Respecting beliefs that affect care decisions',
        [
            'Imposing staff beliefs on patients',
            'Refusing interpreters',
            'Mocking dietary practices',
        ],
        'Respect builds trust and adherence. Choosing Imposing staff beliefs on patients is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What does Customer service recovery after an error include?',
        'Correcting the issue and explaining next steps',
        [
            'Denying documented facts',
            'Refusing supervisor contact always',
            'Deleting complaints',
        ],
        'Transparent recovery rebuilds confidence. Choosing Denying documented facts is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What does Health literacy considerations include?',
        'Using plain language and teach-back',
        [
            'Assuming all patients read at college level',
            'Providing only dense text',
            'Avoiding questions',
        ],
        'Teach-back confirms understanding. Choosing Assuming all patients read at college level is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What does Health literacy techniques include?',
        'Using plain language and avoiding jargon when possible',
        [
            'Long unexplained acronyms only',
            'Refusing written materials',
            'Speaking only in whispers',
        ],
        'Plain language improves comprehension. Choosing Long unexplained acronyms only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What does Managing wait times include?',
        'Updating patients about delays when possible',
        [
            'Hiding all wait information always',
            'Blaming patients for schedules',
            'Closing registration without notice',
        ],
        'Updates reduce frustration during delays. Choosing Hiding all wait information always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What does Work practice controls under OSHA include?',
        'Prohibiting bending or recapping needles by hand',
        [
            'Reusing gloves all day',
            'Skipping hand hygiene',
            'Eating in procedure rooms',
        ],
        'OSHA specifies work practice controls to reduce blood exposure risk. Choosing Reusing gloves all day is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What is After a needlestick, the first priority?',
        'Wash needlesticks and cuts with soap and water; flush splashes to nose/mouth with water',
        [
            'Apply a tourniquet',
            'Wait until end of shift to report',
            'Squeeze the wound hard',
        ],
        'OSHA post-exposure steps include immediate cleansing and prompt reporting. Choosing Apply a tourniquet is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What is When language barriers exist, best practice?',
        'Use a qualified interpreter (not a minor child)',
        [
            'Ask another patient to translate confidential details',
            'Skip informed consent',
            'Guess the diagnosis',
        ],
        'Qualified interpretation improves safety and consent. Choosing Ask another patient to translate confidential details is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What is When language interpretation is needed, the best option?',
        'A qualified medical interpreter',
        [
            'A minor child of the patient',
            'Any passerby in the hall',
            "Guessing the patient's language",
        ],
        'Professional interpreters improve safety and consent. Choosing A minor child of the patient is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'What should Telephone triage messages for the provider include?',
        'Patient name, callback number, symptoms, and urgency',
        [
            'Gossip about other patients',
            'Full social security number shouted in waiting room',
            'No clinical details',
        ],
        'Complete messages support safe callbacks. Choosing Gossip about other patients is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'When a patient uses an assistive communication device, the MA should?',
        'Allow adequate time and address the patient directly',
        [
            'Speak only to the caregiver always',
            'Rush the encounter',
            'Take the device away',
        ],
        'Direct engagement respects autonomy. Choosing Speak only to the caregiver always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'When communicating bad news, allow?',
        'Time for questions and emotional response',
        [
            'Immediate dismissal from the room',
            'Jokes to lighten mood always',
            'Recording without consent',
        ],
        'Compassionate pacing supports coping. Choosing Immediate dismissal from the room is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'When de-escalating an upset caller, first?',
        'Remain calm and acknowledge the concern',
        [
            'Match yelling volume',
            'Hang up immediately',
            "Share other patients' stories",
        ],
        'Calm acknowledgment can reduce tension. Choosing Match yelling volume is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'When giving bad news, the MA should?',
        "Follow office protocol and support the provider's plan",
        [
            'Speculate about prognosis beyond scope',
            'Promise a cure',
            'Share unrelated stories',
        ],
        'Stay within role and scope. Choosing Speculate about prognosis beyond scope is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'When language interpretation is needed, use?',
        'Qualified medical interpreters',
        [
            'Minor children for all adult sensitive topics',
            'Random bilingual visitors',
            'Online machine translation alone for consent',
        ],
        'Qualified interpreters protect accuracy and privacy. Choosing Minor children for all adult sensitive topics is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-communication',
        'When using an interpreter, the medical assistant should?',
        'Allow the patient to speak freely and face the patient while the interpreter works',
        [
            'Ask the child to interpret confidential history',
            'Speak only to the interpreter and ignore the patient',
            'Use a family member for sensitive abuse disclosure',
        ],
        'Qualified interpreters protect accuracy and privacy. Speaking to the patient maintains rapport.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

