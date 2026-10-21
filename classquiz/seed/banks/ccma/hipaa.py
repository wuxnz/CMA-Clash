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
    # ccma-hipaa-026
    fact(
        'ccma-hipaa',
        'A medical assistant suspects a coworker is accessing celebrity charts out of curiosity. What is the appropriate first action under typical facility policy?',
        'Report the concern through the privacy officer or compliance hotline per written procedures',
        [
            'Post screenshots of audit logs on a personal social media account',
            'Delete system access logs so the coworker cannot be identified',
            'Confront the coworker publicly in the waiting room without involving leadership',
        ],
        'Workforce members are expected to escalate suspected privacy violations internally so the entity can investigate and mitigate harm. Public disclosure or tampering with evidence can worsen breaches and violate policy.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-027
    fact(
        'ccma-hipaa',
        'The practice wants to text patients their lab results using personal smartphones. What approach aligns with HIPAA security expectations?',
        'Use a HIPAA-compliant messaging platform or follow policy that includes patient consent and security warnings',
        [
            'Send the full chart through standard unencrypted SMS to any number on file',
            'Post results in a public social media direct message thread',
            'Add patients to an unencrypted group chat that includes unrelated staff',
        ],
        'Consumer texting apps may lack required safeguards for ePHI. Covered entities should implement vendor solutions or documented patient agreements that address confidentiality and retention.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-028
    fact(
        'ccma-hipaa',
        'Which category of health information does the HIPAA Security Rule primarily protect?',
        'Electronic protected health information through administrative, physical, and technical safeguards',
        [
            'Paper records stored in locked file rooms with no electronic systems',
            'Parking lot traffic patterns unrelated to patient care',
            'Cafeteria daily menus displayed for visitors',
        ],
        'The Security Rule applies to ePHI held or transmitted by covered entities and business associates. Paper-only workflows may still fall under the Privacy Rule, but the Security Rule targets electronic systems and media.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-029
    fact(
        'ccma-hipaa',
        'A billing clerk needs a diagnosis code to submit a claim. How does the minimum necessary standard apply?',
        'Use only the PHI required to complete the billing task, not the entire medical record',
        [
            'Email the complete chart to every payer contact for convenience',
            'Post the patient diagnosis on the clinic lobby monitor',
            'Automatically forward all future lab results to the patient\'s employer',
        ],
        'Minimum necessary limits internal uses and external disclosures to the amount needed for the stated purpose. Routine dumping of full records increases exposure without business justification.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-030
    fact(
        'ccma-hipaa',
        'A patient signs a form allowing records to be sent to a disability attorney. Which element must appear on a valid HIPAA authorization?',
        'A specific description of the information to be disclosed and the purpose of the disclosure',
        [
            'Blank permission to release every record for any reason with no end date',
            'A verbal okay from an unidentified caller without the patient\'s signature',
            'Only the patient\'s social media username as the sole identifier',
        ],
        'Privacy Rule authorizations must state what will be shared, who may receive it, an expiration, and the patient\'s right to revoke. Vague or open-ended forms are not valid for non-permitted disclosures.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-031
    fact(
        'ccma-hipaa',
        'Before releasing psychotherapy notes to a family member, what does HIPAA generally require compared with the rest of the medical record?',
        'A separate patient authorization specific to psychotherapy notes',
        [
            'No extra steps because psychotherapy notes are treated like vital signs',
            'Automatic disclosure whenever the family member knows the patient\'s address',
            'Verbal permission from front-desk staff without reviewing the record type',
        ],
        'Psychotherapy notes held separately from the general chart receive heightened protection. Most treatment, payment, and operations uses still need explicit authorization for these notes.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-032
    fact(
        'ccma-hipaa',
        'Which workstation practices satisfy common HIPAA Security Rule technical safeguards for the EHR?',
        'Unique user IDs, automatic logoff, and screens positioned away from public view',
        [
            'One shared password posted on every monitor in the nurses\' station',
            'Leaving sessions open overnight so the next shift saves time',
            'Disabling automatic lock because staff memorize each other\'s credentials',
        ],
        'Access controls and workstation use policies reduce unauthorized viewing of ePHI. Shared accounts and always-open sessions prevent accurate audit trails and invite snooping.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-033
    fact(
        'ccma-hipaa',
        'A quality team reviews aggregate readmission rates with all patient names removed using the HIPAA Safe Harbor method. How is that dataset classified?',
        'De-identified health information that is not PHI when the standard is met',
        [
            'PHI because any health-related number always identifies someone',
            'PHI unless the patient signs a new authorization every month',
            'Public domain information that may be sold without any restrictions',
        ],
        'Proper de-identification under Safe Harbor or expert determination removes HIPAA protections. Aggregate quality metrics without identifiers support improvement without triggering PHI rules.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-034
    fact(
        'ccma-hipaa',
        'A medical assistant works at a check-in desk visible from the waiting room. Which workstation habit best protects ePHI?',
        'Lock the screen when stepping away and angle the monitor away from visitors',
        [
            'Leave the prior patient\'s chart open while calling the next person forward',
            'Store login passwords on sticky notes attached to the keyboard',
            'Connect the EHR only through unsecured public Wi-Fi with no VPN',
        ],
        'Physical safeguards complement technical controls by limiting who can see screens in public areas. Visible charts and shared credentials are frequent sources of incidental disclosure.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-035
    fact(
        'ccma-hipaa',
        'After a risk analysis shows laptops may leave the clinic with ePHI, what Security Rule safeguard is commonly implemented?',
        'Encrypting portable device storage as an addressable safeguard when risk warrants it',
        [
            'Prohibiting encryption because HIPAA forbids protecting laptops',
            'Ignoring the finding because encryption is never considered after analysis',
            'Posting ePHI on public blogs instead of storing it locally',
        ],
        'Addressable specifications require covered entities to implement a safeguard or document why an equivalent measure is reasonable. Encryption mitigates loss or theft of mobile media.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-036
    fact(
        'ccma-hipaa',
        'A caller requests a copy of imaging results for a patient who is not present. What identity verification approach is appropriate?',
        'Follow facility policy using pre-established identifiers, not casual guesses from social media',
        [
            'Release records when the caller states the patient birthday found online',
            'Fax results immediately if the caller knows the patient\'s nickname',
            'Skip verification because voice recognition apps are always accurate',
        ],
        'The right of access and minimum necessary rules assume the requester is who they claim to be. Weak verification enables wrongful disclosure to strangers or domestic abusers.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-037
    fact(
        'ccma-hipaa',
        'A marketing firm offers payment if the clinic emails patient lists for a supplement promotion. When is patient authorization required?',
        'For the marketing use because it is not a permitted treatment, payment, or operations disclosure',
        [
            'Never, because any employee may disclose PHI for commercial gain',
            'Only when the patient is hospitalized, not in outpatient clinics',
            'Never, because treatment, payment, and operations always cover third-party ads',
        ],
        'Financially motivated marketing to sell unrelated products generally needs explicit authorization. Core TPO and legally required public health reporting follow different pathways.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-038
    fact(
        'ccma-hipaa',
        'Unencrypted backup tapes with PHI are stolen from a courier van. What must the covered entity do first under the Breach Notification Rule?',
        'Perform a risk assessment to determine whether notification to individuals, HHS, or media is required',
        [
            'Assume no breach occurred if the thief promises to return the tapes',
            'Skip documentation because criminal theft automatically exempts all HIPAA duties',
            'Announce every patient diagnosis on the clinic website before investigating',
        ],
        'Not every impermissible use is a reportable breach; risk analysis examines probability that PHI was compromised. Timely assessment drives individual and regulatory notice when thresholds are met.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-039
    fact(
        'ccma-hipaa',
        'A university researcher requests dates of service and zip codes tied to diagnoses for an approved study. What agreement is required for a HIPAA limited data set?',
        'A data use agreement between the covered entity and the researcher',
        [
            'No contract because limited data sets may be posted on open internet forums',
            'Only a verbal promise that the laptop will stay in the cafeteria',
            'A business associate agreement that replaces all institutional review board oversight',
        ],
        'Limited data sets exclude direct identifiers but may retain certain geographic and date elements. Recipients must sign data use agreements promising safeguards and permitted uses.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-040
    fact(
        'ccma-hipaa',
        'A patient requests an accounting of disclosures for the past three years. Which type of disclosure will usually appear on that list?',
        'Disclosures for purposes other than treatment, payment, and health care operations, subject to exceptions',
        [
            'Every internal note another clinician read for continuity of care',
            'Routine claim transmissions to the health plan for payment',
            'All casual text messages staff sent about weekend plans',
        ],
        'Accounting focuses on non-routine sharing such as many research or legal disclosures. Everyday TPO and many treatment-related exchanges are excluded unless law requires listing them.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-041
    fact(
        'ccma-hipaa',
        'A vendor offers to sell a clinic list of patients with full names and MRNs for outreach. Why does that dataset fail HIPAA de-identification?',
        'It retains direct identifiers that tie health information to specific individuals',
        [
            'De-identified data must always include social security numbers',
            'Quality improvement projects may never use any health-related numbers',
            'De-identified and PHI are legally identical terms with no difference',
        ],
        'PHI remains regulated until identifiers are removed under Safe Harbor or expert certification. Selling identifiable lists for marketing violates privacy rules and usually needs authorization.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-042
    fact(
        'ccma-hipaa',
        'A patient asks the clinic not to bill the spouse\'s insurance because it would reveal sensitive care. How should the practice handle a restriction request?',
        'Follow Privacy Rule procedures to consider the request and document any agreed limits',
        [
            'Ignore the patient because insurers always receive every diagnosis automatically',
            'Agree to delete all factual entries from the medical record permanently',
            'Require the patient to accept unlimited marketing emails as a condition of care',
        ],
        'Patients may request limits on certain disclosures to health plans when they pay out of pocket in full, among other situations. Entities are not required to agree in every case but must use the formal process.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-043
    fact(
        'ccma-hipaa',
        'A behavioral health provider keeps separate psychotherapy notes from progress notes in the EHR. What disclosure rule applies to those psychotherapy notes?',
        'They require patient authorization for most uses outside narrow exceptions',
        [
            'They may be freely marketed to pharmaceutical representatives',
            'They must be posted on the facility directory at admission',
            'They have no HIPAA protection and may be shared with any visitor',
        ],
        'Psychotherapy notes are defined narrowly and receive extra consent requirements. General medical record entries about medications or hospitalization follow different disclosure rules.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-044
    fact(
        'ccma-hipaa',
        'A specialist shares operative details with the referring primary care provider to coordinate follow-up. Is individual patient authorization required for this exchange?',
        'No, when the disclosure is for treatment within permitted HIPAA uses',
        [
            'Yes, every treatment-related fax needs a new signed authorization',
            'No, because any bystander may receive the full record on request',
            'Yes, unless the patient posted surgery photos on personal social media',
        ],
        'Treatment disclosures among providers involved in care are core permitted uses without separate authorization. Disclosures must still respect minimum necessary and facility policy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-045
    fact(
        'ccma-hipaa',
        'Home health staff carry tablets with ePHI into patients\' homes. Which safeguard addresses loss of those portable devices?',
        'Encrypting device storage and using remote wipe after documented risk analysis',
        [
            'Storing tablets unlocked in vehicles because encryption is banned by HIPAA',
            'Relying on hope that devices are never lost without reviewing threats',
            'Limiting encryption to desktop billing computers only, never field tablets',
        ],
        'Portable media face theft and loss outside the clinic. Addressable encryption and device management reduce the chance that ePHI is readable if hardware disappears.',
        [S.NHA_CCMA],
        'advanced',
    ),

    # ccma-hipaa-046
    fact(
        'ccma-hipaa',
        'What does the HIPAA minimum necessary standard require when using protected health information?',
        'Limit access and disclosure to the amount needed for the current purpose',
        ['Share the entire chart with any vendor who requests it',
        'Post visit summaries on a public bulletin board',
        'Email full records to personal accounts for convenience'],
        'Minimum necessary reduces privacy risk for treatment, payment, and operations. Broad sharing without role-based limits violates the Privacy Rule.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-047
    fact(
        'ccma-hipaa',
        'A patient requests a copy of their medical record. What should the office do?',
        'Follow HIPAA right-of-access procedures, including reasonable timelines and fees per policy',
        ['Deny all requests because charts are clinic property',
        'Give records to a neighbor without verifying authority',
        'Require the patient to delete their own diagnoses first'],
        'Patients generally have a right to access their PHI with defined exceptions. Neighbors lack authority unless documented; outright denial conflicts with access rules.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-048
    fact(
        'ccma-hipaa',
        'Which disclosure is generally permitted without patient authorization for treatment purposes?',
        'Sharing relevant clinical information with another health care provider involved in care',
        ['Selling the diagnosis list to a marketing firm',
        'Posting photos of wounds on a personal blog',
        'Giving records to an employer for curiosity'],
        'HIPAA permits TPO disclosures among involved professionals. Marketing and employer curiosity are not treatment purposes.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-049
    fact(
        'ccma-hipaa',
        'What is required before a business associate may handle electronic protected health information for a covered entity?',
        'A business associate agreement with required safeguards',
        ['A handshake in the parking lot',
        'Public posting of patient lists',
        'Shared employee social media passwords'],
        'The Security Rule expects contractual obligations for vendors touching ePHI. Informal agreements do not replace BAAs.',
        [S.HHS_HIPAA_SECURITY, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-050
    fact(
        'ccma-hipaa',
        'Where should patient conversations about diagnoses occur to protect privacy?',
        'In private treatment areas away from public corridors',
        ['In a crowded elevator with visitors present',
        'At the front desk microphone',
        'In the cafeteria during lunch rush'],
        'HIPAA safeguards oral disclosures; public areas risk incidental exposure. Private rooms or lowered voices in enclosed spaces reduce breaches.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-051
    fact(
        'ccma-hipaa',
        'A workforce member accesses a celebrity\'s chart out of curiosity without a job reason. What risk does this create?',
        'A privacy violation that may require investigation and sanction',
        ['Improved public relations for the clinic',
        'Automatic HIPAA waiver for all staff',
        'Permission to share records on social media'],
        'Minimum necessary and role-based access prohibit curiosity browsing. Sanctions and breach analysis may follow unauthorized access.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-052
    fact(
        'ccma-hipaa',
        'Which action helps secure electronic health record workstations?',
        'Log off or lock sessions when leaving the desk',
        ['Share login credentials with float staff',
        'Leave charts open in public view',
        'Disable passwords for speed'],
        'Automatic timeouts and unique credentials protect ePHI under the Security Rule. Shared logins break audit trails.',
        [S.HHS_HIPAA_SECURITY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-053
    fact(
        'ccma-hipaa',
        'A patient authorizes release of records to a specific attorney. What should be verified before sending?',
        'The authorization is signed, dated, and lists the correct recipient',
        ['The attorney\'s favorite sport',
        'Whether the mailroom is busy',
        'Other patients with similar names'],
        'Valid authorizations specify who may receive PHI. Similar names require identity checks to avoid misdirected disclosures.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-054
    fact(
        'ccma-hipaa',
        'Which fax practice reduces misdirected protected health information?',
        'Verify the recipient number and use a confidentiality cover sheet',
        ['Send to the last number dialed without checking',
        'Include every diagnosis in the subject line shouted aloud',
        'Fax to the front desk printer in a public area without retrieval'],
        'Confirmation and cover sheets limit wrong routing. Public unattended prints expose PHI.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-055
    fact(
        'ccma-hipaa',
        'A patient requests amendment of an error in their record. What is the covered entity\'s obligation?',
        'Review and respond per the Privacy Rule, accepting or denying with explanation',
        ['Ignore the request because charts are permanent',
        'Delete the entire chart',
        'Charge a fee to refuse automatically'],
        'Patients have rights to request amendments with defined timelines. Wholesale deletion is not the pathway for correcting a single error.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'advanced',
    ),
]
