# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-hipaa)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-hipaa-001
    fact(
        'ccma-hipaa',
        'Two staff members discuss a patient by name and diagnosis while riding a crowded hospital elevator. Why is this a privacy concern?',
        'Others may overhear individually identifiable health information',
        [
            'Elevator conversations are exempt when both employees wear badges',
            'Whispering makes the exchange a permitted treatment disclosure',
            'Verbal updates between coworkers count as de-identified data',
        ],
        'The HIPAA Privacy Rule limits uses and disclosures of PHI to permitted purposes and safeguards. Conversations in public areas can expose identifiers to people who are not part of the care team.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-002
    fact(
        'ccma-hipaa',
        'Which information does the HIPAA Privacy Rule regulate when held or transmitted by a covered entity or business associate?',
        'Individually identifiable protected health information',
        [
            'Weather forecasts displayed in the waiting room',
            'Properly de-identified data that meets HIPAA standards',
            'Restaurant menus used for patient dietary teaching',
        ],
        'PHI ties health data to a specific person and triggers privacy and security obligations. Data stripped of identifiers under HIPAA rules or unrelated public information falls outside that scope.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-003
    fact(
        'ccma-hipaa',
        'At first visit, what written document must a covered entity offer that explains how it may use and share PHI?',
        'A notice of privacy practices',
        [
            'A blanket waiver allowing unlimited marketing texts',
            'A contract granting the public access to every chart',
            'A form that waives all future breach notifications',
        ],
        'The notice of privacy practices describes routine uses, patient rights, and how to file complaints. It supports informed expectations before treatment and billing activities begin.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-004
    fact(
        'ccma-hipaa',
        'Which organizations are HIPAA covered entities subject to the Privacy and Security Rules?',
        'Health plans, health care clearinghouses, and certain health care providers',
        [
            'Every employer in every industry regardless of health data',
            'Patients and family members who receive care',
            'Medical device makers that do not handle patient-identifiable data',
        ],
        'HHS defines covered entities that create, receive, maintain, or transmit PHI in defined roles. Employers without covered functions and vendors without PHI access are addressed through other relationships such as business associate agreements.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-005
    fact(
        'ccma-hipaa',
        'How does HIPAA define protected health information (PHI) in the outpatient setting?',
        'Individually identifiable health information held or transmitted by a covered entity',
        [
            'Billing codes with all patient identifiers permanently removed',
            'Aggregate quality reports with no link to a person',
            'Paper appointment books that list only first names of staff',
        ],
        'PHI includes demographic and clinical details that identify the individual or could reasonably be used to identify them. De-identified or workforce scheduling data without patient health content is not PHI.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-006
    fact(
        'ccma-hipaa',
        'A medical assistant sends a lab report by fax to another clinic. What step best reduces the risk of an unauthorized disclosure?',
        'Confirm the fax number, use a confidentiality cover sheet, and limit detail to what is needed',
        [
            'Dial the last number used on the machine without verifying the recipient',
            'Place the patient social security number on the cover for quick matching',
            'Send the full chart to a front-desk fax at a business with a similar name',
        ],
        'Misdirected faxes are a common breach source. Verifying the destination and labeling the transmission helps ensure PHI reaches the intended covered entity or provider.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-007
    fact(
        'ccma-hipaa',
        'When should HIPAA privacy and security training occur for medical assistants and other workforce members?',
        'At hire and on a recurring schedule defined by facility policy',
        [
            'Only after OCR opens a formal investigation',
            'Only for information technology staff, not clinical assistants',
            'One session with no refresher unless a new law passes',
        ],
        'Administrative safeguards under the Security Rule expect workforce members to understand policies before handling ePHI. Periodic retraining reinforces safe workflows as systems and threats change.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-008
    fact(
        'ccma-hipaa',
        'A cloud billing vendor will store patient names and diagnoses for the practice. What contractual step is required under HIPAA?',
        'Execute a business associate agreement before PHI is shared',
        [
            'Rely on a verbal promise because the vendor is well known',
            'Skip a contract when the vendor only receives encrypted files',
            'Treat the vendor like an office supply order with no privacy terms',
        ],
        'Business associates must contractually agree to safeguard PHI and report breaches. Covered entities remain accountable for PHI handled on their behalf by vendors.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-009
    fact(
        'ccma-hipaa',
        'A hospital wishes to tell callers whether a patient is in the building and their room number. What must happen first under the facility directory rules?',
        'Inform the patient and give a chance to agree or object to directory disclosures',
        [
            'Publish the full medical record summary on the lobby monitor',
            'Release diagnosis details to any visitor who knows the last name',
            'Add the patient to the directory automatically at admission without notice',
        ],
        'Directory information is limited and voluntary for the patient. Name, location, and general condition may be shared only within the rules when the patient does not object.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-010
    fact(
        'ccma-hipaa',
        'A patient asks for an accounting of disclosures. What will the list typically include?',
        'Certain disclosures made for purposes other than treatment, payment, and health care operations',
        [
            'Every internal note another clinician read for continuity of care',
            'Routine billing transmissions to the health plan for payment',
            'Meal orders the dietary staff placed for the patient',
        ],
        'Treatment, payment, and operations uses are excluded from the accounting unless required by law. Patients may learn about many non-routine disclosures made in the prior six years, subject to exceptions.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-011
    fact(
        'ccma-hipaa',
        'Which Security Rule safeguard requires systems that create, maintain, or transmit ePHI to log who accessed records?',
        'Audit controls that record and review ePHI access activity',
        [
            'Disabling access logs to save server storage space',
            'Assigning one shared user ID for every employee on the unit',
            'Storing passwords on sticky notes attached to workstations',
        ],
        'Audit trails support breach investigation and deter snooping. Reviewing logs is part of detecting inappropriate access to electronic charts.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-012
    fact(
        'ccma-hipaa',
        'A provider shares PHI with another specialist to coordinate the patient\'s surgery. Is patient authorization required for this disclosure?',
        'No, when the disclosure is for treatment within permitted HIPAA uses',
        [
            'Yes, written authorization is required for every treatment-related fax',
            'No, because any employee may disclose the full record to anyone',
            'Yes, unless the patient posted their diagnosis on personal social media',
        ],
        'Treatment, payment, and health care operations form the core permitted uses without individual authorization. Disclosures still must follow minimum necessary and facility policy.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-013
    fact(
        'ccma-hipaa',
        'A researcher wants a dataset stripped of identifiers using the HIPAA Safe Harbor method. Which action aligns with that approach?',
        'Remove specified identifier elements such as names and dates tied to the individual',
        [
            'Rename the patient but keep the medical record number in the file',
            'Delete only the patient favorite color field and call the file de-identified',
            'Share the full chart because the research protocol was approved locally',
        ],
        'Safe Harbor requires removal of 18 categories of identifiers unless an expert certifies very low re-identification risk. Partial redaction that leaves key identifiers still counts as PHI.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-014
    fact(
        'ccma-hipaa',
        'A clinic laptop stores ePHI and may leave the building for home visits. Encrypting the drive is an example of what type of safeguard?',
        'A technical safeguard under the HIPAA Security Rule',
        [
            'A patient marketing authorization under the Privacy Rule',
            'An optional step that replaces the need for any risk analysis',
            'A substitute for workforce privacy training',
        ],
        'Technical safeguards protect ePHI through access controls, encryption, and integrity tools selected after risk analysis. Encryption reduces impact if a device is lost or stolen.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-015
    fact(
        'ccma-hipaa',
        'Before buying new software that stores ePHI, what Security Rule process should the practice complete?',
        'Conduct an accurate and thorough risk analysis of ePHI vulnerabilities',
        [
            'Install the product first and document risks only after a breach occurs',
            'Rely on the vendor brochure without reviewing local workflows',
            'Delegate the decision entirely to staff who do not handle patient data',
        ],
        'Risk analysis identifies threats to confidentiality, integrity, and availability of ePHI. Safeguards such as encryption and access controls should address documented risks.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-016
    fact(
        'ccma-hipaa',
        'The practice wants to email patients about a third-party weight-loss product unrelated to their care plan. What is generally required?',
        'Patient authorization for marketing communications using PHI',
        [
            'No permission because the message promotes wellness in general',
            'Automatic consent because the patient listed an email at registration',
            'Verbal agreement from front-desk staff without documenting the patient choice',
        ],
        'Marketing communications paid for by third parties or promoting unrelated products usually need explicit authorization. Treatment reminders and certain face-to-face communications follow different rules.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-017
    fact(
        'ccma-hipaa',
        'How should role-based access to the electronic health record reflect the minimum necessary standard?',
        'Grant each user access to the PHI needed for that job and no more',
        [
            'Give every employee the same super-user password for convenience',
            'Allow volunteers to open any chart while shadowing without training',
            'Share executive payroll files with clinical staff to fill idle time',
        ],
        'Minimum necessary limits both disclosures to outsiders and internal chart access. Segregating modules by role reduces curiosity browsing and accidental exposure.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-018
    fact(
        'ccma-hipaa',
        "A caller says they are the patient's cousin and asks for today's test results by phone. What approach follows minimum necessary principles?",
        'Verify identity and authority, then share only the information appropriate to the request and policy',
        [
            'Read the entire chart aloud once the caller knows the patient date of birth',
            'Fax all results to the number provided without confirming who will receive them',
            'Refuse to document the call so no record of the disclosure exists',
        ],
        'Even permitted disclosures should be limited to what the recipient needs to know. Identity verification and policy on family involvement prevent casual over-sharing.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-019
    fact(
        'ccma-hipaa',
        'When discussing a patient with a consulting physician by phone in a semi-private nurses\' station, what practice supports the minimum necessary standard?',
        'Lower your voice, move to a private area, and share only clinically relevant details',
        [
            'Use the hallway speakerphone so the consulting team can hear clearly',
            'Project the chart on the wall monitor for everyone in the unit to view',
            'Email the complete record to personal accounts for faster reading',
        ],
        'Minimum necessary applies to oral disclosures as well as electronic ones. Physical privacy and limiting content reduce incidental disclosure to visitors and other patients.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-020
    fact(
        'ccma-hipaa',
        'A patient believes the clinic mishandled their PHI. Where may they file a privacy complaint?',
        'With the covered entity\'s privacy officer and with the HHS Office for Civil Rights',
        [
            'Only with the local restaurant health inspector',
            'Only on anonymous gossip boards with no contact information',
            'Nowhere, because patients waive privacy rights by seeking care',
        ],
        'Covered entities must have a complaint process and may not retaliate for filing. OCR investigates alleged violations of the Privacy and Security Rules.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-021
    fact(
        'ccma-hipaa',
        'A patient asks the practice not to disclose information about their care to their spouse. How must the covered entity respond?',
        'Consider the request; agreed restrictions must be documented except where law limits them',
        [
            'Ignore the request because family members usually want updates',
            'Agree to every restriction even when payment from the spouse requires disclosure',
            'Tell the patient restrictions are impossible for any purpose',
        ],
        'Patients may request limits on certain disclosures, but the entity is not required to agree in every situation such as some payment arrangements. Documented restrictions must be honored when accepted.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-022
    fact(
        'ccma-hipaa',
        'Which right does HIPAA grant individuals regarding their designated record set?',
        'Inspect and obtain a copy of their PHI, and request amendment of certain errors',
        [
            'Demand that factual lab results be erased because they dislike the numbers',
            'Access and copy other patients\' records for comparison',
            'Block all sharing of information with treating clinicians during an emergency',
        ],
        'Access and amendment rights include timely copies and a process to correct inaccurate information. Providers may deny some amendment requests when records are accurate and complete.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-023
    fact(
        'ccma-hipaa',
        'A patient wants bills sent to a different address so a household member does not see diagnoses on statements. What should the practice do?',
        'Accommodate reasonable requests for confidential communications when asked',
        [
            'Refuse because mail must go to the address on the driver license',
            'Send detailed clinical notes to the alternate address without discussing format',
            'Charge a punitive fee not permitted under HIPAA for honoring the request',
        ],
        'Patients may request that communications arrive by alternative means or at alternative locations. Covered entities must accommodate reasonable requests and may not require explanation of the reason.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-024
    fact(
        'ccma-hipaa',
        'How quickly must a covered entity generally act when an individual requests copies of their medical record?',
        'Within time frames set by HIPAA and applicable state law, often about 30 days with possible extension',
        [
            'Deny the request automatically if the patient owes a small copay',
            'Provide another patient\'s record if the names are similar',
            'Withhold all records until the patient agrees to unrelated marketing',
        ],
        'The right of access requires timely production of readable copies, with limited fees allowed by rule. Delays beyond regulatory timelines or conditioning access on unrelated demands violate patient rights.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-025
    fact(
        'ccma-hipaa',
        'Under HIPAA, when may a personal representative access or authorize disclosure of a patient\'s PHI?',
        'When law or documented patient designation gives them authority to act for the individual',
        [
            'Whenever a neighbor states they are a close friend of the family',
            'When a pharmaceutical sales representative requests records for coaching',
            'When someone finds discarded paperwork in a public trash bin',
        ],
        'Representative status must be verified through legal documentation such as guardianship or health care proxy. Curiosity or commercial interest does not create authority to receive PHI.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'Reporting suspected HIPAA violations internally should follow?',
        'Facility privacy and compliance policies',
        [
            'Posting on personal social media first',
            'Ignoring unless media asks',
            'Deleting audit logs',
        ],
        'Internal reporting enables investigation and mitigation. Choosing Posting on personal social media first is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'Texting PHI with patients requires?',
        'Secure platform or patient consent with warnings if allowed by policy',
        [
            'Standard SMS with full chart always',
            'Public Twitter DMs',
            'Unencrypted group chats',
        ],
        'Standard texting may not meet security requirements. Choosing Standard SMS with full chart always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'The HIPAA Security Rule primarily addresses?',
        'Electronic PHI safeguards',
        [
            'Only paper records',
            'Parking lot design',
            'Cafeteria menus',
        ],
        'Administrative, physical, and technical safeguards protect ePHI. Choosing Only paper records is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'The HIPAA minimum necessary standard means?',
        'Limit PHI used or disclosed to what is needed for the purpose',
        [
            'Share entire charts routinely',
            'Post diagnoses publicly',
            'Email all results to family by default',
        ],
        'Minimum necessary reduces privacy risk. Choosing Share entire charts routinely is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'What does A HIPAA authorization for disclosure must include?',
        'Specific description of information and purpose',
        [
            'Blanket lifetime permission without limits always',
            'Verbal OK from unknown caller',
            'Social media username only',
        ],
        'Authorizations require core elements under the Privacy Rule. Choosing Blanket lifetime permission without limits always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'What does A valid HIPAA authorization must include?',
        'Specific description of information and purpose of disclosure',
        [
            'Blanket permission for all future uses forever',
            'No expiration date required always',
            'Verbal okay only without signature when written required',
        ],
        'Authorizations have required elements. Choosing Blanket permission for all future uses forever is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'What does Access controls for EHR workstations include?',
        'Automatic logoff and unique user IDs',
        [
            'Shared passwords on all PCs',
            'Leaving sessions open overnight',
            'Posting passwords on monitors',
        ],
        'Security Rule technical safeguards protect ePHI. Choosing Shared passwords on all PCs is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'What does Protected health information (PHI) include?',
        'Individually identifiable health information held by covered entities',
        [
            'De-identified data per HIPAA rules',
            'Only billing codes without identifiers',
            'Public weather reports',
        ],
        'PHI ties health data to a person. Choosing De-identified data per HIPAA rules is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'What does Workstation security include?',
        'Screen locks and positioning away from public view',
        [
            'Leaving charts open in hallway',
            'Shared passwords on sticky notes',
            'Unencrypted public Wi-Fi for EHR without safeguards',
        ],
        'Physical and technical safeguards reduce snooping. Choosing Leaving charts open in hallway is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'What is Encryption of ePHI on laptops?',
        'A recommended addressable safeguard under the Security Rule',
        [
            'Prohibited by HIPAA',
            'Optional with no risk consideration',
            'Only for public blogs',
        ],
        'Risk analysis guides encryption decisions. Choosing Prohibited by HIPAA is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'What should Verifying identity before releasing records use when measuring?',
        'Policy-defined identifiers, not guesses',
        [
            'Birthday alone from social media',
            'Voice recognition without policy',
            'Anyone who knows patient nickname',
        ],
        'Identity verification prevents unauthorized access. Choosing Birthday alone from social media is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'A HIPAA authorization is generally required for?',
        'Uses and disclosures not otherwise permitted by the Privacy Rule',
        [
            'Treatment, payment, and health care operations',
            'Reporting to public health authorities as required by law',
            'Disclosures to the patient',
        ],
        'Marketing and many non-routine disclosures need patient authorization. Choosing Treatment, payment, and health care operations is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'A breach of unsecured PHI requires?',
        'Risk assessment and notification per HIPAA Breach Notification Rule',
        [
            'Automatic jail for all staff',
            'No documentation',
            'Public social media post only',
        ],
        'Covered entities must evaluate and report certain breaches. Choosing Automatic jail for all staff is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'A limited data set may be used for research when?',
        'A data use agreement is in place',
        [
            'PHI is posted online',
            'No safeguards exist',
            'Patients are not informed when required',
        ],
        'HHS allows limited data sets with agreements. Choosing PHI is posted online is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'An accounting of disclosures provides patients?',
        'A list of certain non-routine disclosures of PHI',
        [
            'All text messages ever sent',
            'Unlimited access to employee HR files',
            'Free medications',
        ],
        'Patients have rights to accounting in defined circumstances. Choosing All text messages ever sent is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'De-identified health information?',
        'Has identifiers removed per HIPAA methods',
        [
            'Contains full name and SSN',
            'Cannot be used for quality improvement',
            'Is identical to PHI',
        ],
        'Proper de-identification removes HIPAA protections. Choosing Contains full name and SSN is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'Patients may request restrictions on disclosures when?',
        'The request is submitted per Privacy Rule procedures',
        [
            'They demand deletion of all medical facts',
            'They refuse all treatment forever',
            'They want unlimited marketing',
        ],
        'Restrictions are limited but recognized under HIPAA. Choosing They demand deletion of all medical facts is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'Psychotherapy notes receive?',
        'Stronger protection than general medical record under HIPAA',
        [
            'No protection',
            'Automatic public posting',
            'Marketing use without consent',
        ],
        'Separate authorization rules apply to psychotherapy notes. Choosing No protection is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'Treatment, payment, and health care operations (TPO) disclosures?',
        'Are permitted without patient authorization in many cases',
        [
            'Always require written authorization',
            'Are never allowed',
            'Apply only to employers',
        ],
        'HIPAA allows TPO without separate authorization. Choosing Always require written authorization is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'What is Encryption of ePHI on portable devices?',
        'An addressable Security Rule safeguard',
        [
            'Prohibited by HIPAA',
            'Optional with no risk analysis',
            'Only for billing staff',
        ],
        'Risk analysis guides encryption implementation. Choosing Prohibited by HIPAA is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

