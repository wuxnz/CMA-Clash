# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-hipaa)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-hipaa-001
        fact('ccma-hipaa', 'Two staff members discuss a patient by name and diagnosis while riding a crowded hospital elevator. Why is this a privacy concern?', 'Others nearby may overhear individually identifiable health information', ['Elevator conversations are permitted when both employees wear facility badges', 'Whispering patient names makes the exchange a de-identified workforce update', 'Verbal diagnosis discussion between coworkers counts as TPO in public areas'], 'The HIPAA Privacy Rule limits uses and disclosures of PHI to permitted purposes and safeguards. Conversations in public areas can expose identifiers to people who are not part of the care team.', [S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-002
        fact('ccma-hipaa', 'Which information does the HIPAA Privacy Rule regulate when held or transmitted by a covered entity or business associate?', 'Individually identifiable protected health information held or transmitted', ["Public information with no connection to a patient's care", "Health data stripped of identifiers under HIPAA de-identification standards", "Handouts printed with no patient-specific health content"], 'PHI ties health data to a specific person and triggers privacy and security obligations. Data stripped of identifiers under HIPAA rules or unrelated public information falls outside that scope.', [S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-003
        fact('ccma-hipaa', 'At first visit, what written document must a covered entity offer that explains how it may use and share PHI?', 'A notice of privacy practices describing uses and patient rights', ['A blanket waiver allowing unlimited marketing texts without opt-out', 'A consent form that lets the patient receive care at the clinic', 'A financial responsibility agreement for the charges of the visit'], 'The notice of privacy practices describes routine uses, patient rights, and how to file complaints. A marketing waiver, a consent to receive care, and a financial responsibility agreement do not explain how the clinic may use and share PHI.', [S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-004
        fact('ccma-hipaa', 'Which organizations are HIPAA covered entities subject to the Privacy and Security Rules?', 'Health plans, clearinghouses, and certain health care providers', ["Employers who do not create, receive, maintain, or transmit PHI", "Patients and family members who receive treatment in the clinic", "Device manufacturers that do not create, receive, or transmit PHI"], 'HHS defines covered entities that create, receive, maintain, or transmit PHI in defined roles. Employers without covered functions and vendors without PHI access are addressed through other relationships such as business associate agreements.', [S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-005
    fact(
        'ccma-hipaa',
        'How does HIPAA define protected health information (PHI) in the outpatient setting?',
        'Individually identifiable health information held by a covered entity',
        [
            'Billing codes with all patient identifiers permanently removed',
            'Aggregate quality reports with no link to a person',
            'Paper appointment books that list first names of staff without patient data',
        ],
        'PHI includes demographic and clinical details that identify the individual or could reasonably be used to identify them. De-identified or workforce scheduling data without patient health content is not PHI.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-006
        fact('ccma-hipaa', 'A medical assistant sends a lab report by fax to another clinic. What step best reduces the risk of an unauthorized disclosure?', 'Confirm the fax number, use a cover sheet, and limit the detail', ['Redial the last stored fax number on the machine without verifying the recipient', 'Place the patient social security number on the cover sheet for quick matching', 'Send the full chart to a front-desk fax at a business with a similar name'], 'Misdirected faxes are a common breach source. Verifying the destination and labeling the transmission helps ensure PHI reaches the intended covered entity or provider.', [S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-007
    fact(
        'ccma-hipaa',
        'When should HIPAA privacy and security training occur for medical assistants and other workforce members?',
        'At hire and on a recurring schedule set by facility policy',
        [
            'After OCR opens a formal investigation into the clinic',
            'For information technology staff and not for clinical assistants',
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
            'Omit a contract when the vendor receives encrypted files',
            'Treat the vendor like an office supply order with no privacy terms',
        ],
        'Business associates must contractually agree to safeguard PHI and report breaches. Covered entities remain accountable for PHI handled on their behalf by vendors.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-009
        fact('ccma-hipaa', 'A hospital wishes to tell callers whether a patient is in the building and their room number. What must happen first under the facility directory rules?', 'Inform the patient and offer a chance to object to directory disclosure', ["Publish a medical record summary on the lobby monitor for visitors", "Release diagnosis details to a visitor who knows the last name", "Add the patient to the directory automatically at admission without notice"], 'Directory information is limited and voluntary for the patient. Name, location, and general condition may be shared only within the rules when the patient does not object.', [S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-010
    fact(
        'ccma-hipaa',
        'A patient asks for an accounting of disclosures. Which disclosures are typically listed?',
        'Disclosures for purposes other than treatment, payment, and operations',
        [
            'Every internal note another clinician read for the care of the patient',
            'Routine billing transmissions to the health plan for payment',
            'Disclosures to a pharmacy to fill refill prescriptions',
        ],
        'Treatment, payment, and operations uses are excluded from the accounting unless required by law. Patients may learn about many non-routine disclosures made in the prior six years, subject to exceptions.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-011
    fact(
        'ccma-hipaa',
        'Which HIPAA Security Rule safeguard requires electronic systems to record who accessed ePHI?',
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
            'No, because every employee may disclose the full record',
            'Yes, unless the patient told the front desk the specialist may get records',
        ],
        'Treatment, payment, and health care operations form the core permitted uses without individual authorization. Disclosures still must follow minimum necessary and facility policy.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-013
    fact(
        'ccma-hipaa',
        'A researcher wants a dataset stripped of identifiers using the HIPAA Safe Harbor method. Which action aligns with that approach?',
        'Remove specified identifiers such as names and dates',
        [
            "Rename the patient but keep the medical record number in the file",
            "Delete the patient's preferred contact method and call it de-identified",
            "Share the full chart because the research protocol was approved locally",
        ],
        'Safe Harbor requires removal of 18 categories of identifiers unless an expert certifies very low re-identification risk. Partial redaction that leaves key identifiers still counts as PHI.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-014
        fact('ccma-hipaa', 'A clinic laptop stores ePHI and may leave the building for home visits. Encrypting the drive is an example of what type of safeguard?', 'A technical safeguard under the HIPAA Security Rule', ['A patient marketing authorization under the Privacy Rule', 'An optional step that replaces the need for a documented risk analysis', 'A substitute for workforce privacy and security training requirements'], 'Technical safeguards protect ePHI through access controls, encryption, and integrity tools selected after risk analysis. Encryption reduces impact if a device is lost or stolen.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-015
    fact(
        'ccma-hipaa',
        'Before buying new software that stores ePHI, what Security Rule process should the practice complete?',
        'Conduct an accurate and thorough risk analysis of ePHI vulnerabilities',
        [
            'Install the product first and document risks after a breach occurs',
            'Rely on the vendor brochure without reviewing local workflows',
            'Delegate the decision entirely to staff who do not handle patient data',
        ],
        'Risk analysis identifies threats to confidentiality, integrity, and availability of ePHI. Safeguards such as encryption and access controls should address documented risks.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-016
        fact('ccma-hipaa', 'The practice wants to email patients about a third-party weight-loss product unrelated to their care plan. What is generally required?', 'Patient authorization for marketing communications that use PHI', ['No permission because the message promotes wellness in general terms', 'Automatic consent because the patient listed an email address at registration', "Verbal agreement from front-desk staff without documenting the patient's choice"], 'Marketing communications paid for by third parties or promoting unrelated products usually need explicit authorization. Treatment reminders and certain face-to-face communications follow different rules.', [S.NHA_CCMA], 'advanced'),

    # ccma-hipaa-017
        fact('ccma-hipaa', 'How should role-based access to the electronic health record reflect the minimum necessary standard?', 'Grant each user access to the PHI needed for that job and no more', ['Give every employee the same super-user password for workstation convenience', 'Allow volunteers to open every chart while shadowing without training', 'Share executive personnel files with clinical staff to fill idle time'], 'Minimum necessary limits both disclosures to outsiders and internal chart access. Segregating modules by role reduces curiosity browsing and accidental exposure.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-018
        fact('ccma-hipaa', "A caller says they are the patient's cousin and asks for today's test results by phone. What approach follows minimum necessary principles?", 'Verify identity and authority, then share only what policy allows', ["Read the entire chart aloud once the caller states the patient's date of birth", "Fax all results to the number provided without confirming who will receive them", "Refuse to document the call so no record of the disclosure exists"], 'Even permitted disclosures should be limited to what the recipient needs to know. Identity verification and policy on family involvement prevent casual over-sharing.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-019
        fact('ccma-hipaa', "When discussing a patient with a consulting physician by phone in a semi-private nurses' station, what practice supports the minimum necessary standard?", 'Lower your voice, move somewhere private, and share what is relevant', ['Use the hallway speakerphone so the consulting team can hear clearly', 'Project the chart on the wall monitor for staff in the unit to view', 'Email the complete record to personal accounts for faster reading'], 'Minimum necessary applies to oral disclosures as well as electronic ones. Physical privacy and limiting content reduce incidental disclosure to visitors and other patients.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-020
    fact(
        'ccma-hipaa',
        'A patient believes the clinic mishandled their PHI. Where may they file a privacy complaint?',
        'With the privacy officer and the HHS Office for Civil Rights',
        [
            'With the state medical board instead of the clinic privacy officer',
            'With the clinician who previously cared for the patient',
            'With local law enforcement and the county district attorney',
        ],
        'Covered entities must have a complaint process and may not retaliate for filing, and OCR investigates alleged violations of the Privacy and Security Rules. A medical board, the treating clinician, and law enforcement are not substitutes for that complaint route.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-021
        fact('ccma-hipaa', 'A patient asks the practice not to disclose information about their care to their spouse. How must the covered entity respond?', 'Consider the request and document agreed restrictions where allowed', ['Ignore the request because family members usually want clinical updates', 'Agree to every restriction even when payment from the spouse requires it', 'Tell the patient that restrictions cannot be honored'], 'Patients may request limits on certain disclosures, but the entity is not required to agree in every situation such as some payment arrangements. Documented restrictions must be honored when accepted.', [S.NHA_CCMA], 'advanced'),

    # ccma-hipaa-022
        fact('ccma-hipaa', 'Which right does HIPAA grant individuals regarding their designated record set?', 'Inspect and copy their PHI, and request amendment of certain errors', ["Demand that factual lab results be erased because the numbers upset them", "Access and copy other patients' records for personal comparison", "Block all sharing of information with treating clinicians during an emergency"], 'Access and amendment rights include timely copies and a process to correct inaccurate information. Providers may deny some amendment requests when records are accurate and complete.', [S.NHA_CCMA], 'advanced'),

    # ccma-hipaa-023
        fact('ccma-hipaa', 'A patient wants bills sent to a different address so a household member does not see diagnoses on statements. What should the practice do?', 'Accommodate reasonable requests for confidential communications when asked', ["Refuse because mail must go to the address on the driver's license", 'Send detailed clinical notes to the alternate address without discussing format', 'Charge a punitive fee not permitted under HIPAA for honoring the request'], 'Patients may request that communications arrive by alternative means or at alternative locations. Covered entities must accommodate reasonable requests and may not require explanation of the reason.', [S.NHA_CCMA], 'advanced'),

    # ccma-hipaa-024
        fact('ccma-hipaa', 'How quickly must a covered entity act when an individual requests copies of their medical record?', 'Within 30 days of the request, with one 30-day extension allowed', ["Within 30 days of the request, with no extension allowed", "Within 30 days of the request, with two 30-day extensions allowed", "Within 90 days of the request, with two 30-day extensions allowed"], 'The right of access requires the covered entity to act on the request within 30 days, and it may take one additional 30 days when the records cannot be produced on time. Refusing any extension, allowing two extensions, or waiting 90 days pushes production beyond the regulatory timeline.', [S.NHA_CCMA], 'advanced'),

    # ccma-hipaa-025
        fact('ccma-hipaa', "Under HIPAA, when may a personal representative access or authorize disclosure of a patient's PHI?", 'When law or patient designation gives them authority to act', ['Whenever a neighbor states they are a close friend of the family', 'When the patient signs a verbal agreement at the front desk', 'When someone finds discarded paperwork in a public trash bin'], 'Representative status must be verified through legal documentation such as guardianship or health care proxy. Curiosity or commercial interest does not create authority to receive PHI.', [S.NHA_CCMA], 'advanced'),

    # ccma-hipaa-026
    fact(
        'ccma-hipaa',
        'A medical assistant suspects a coworker is accessing celebrity charts out of curiosity. What is the appropriate first action under typical facility policy?',
        'Report the concern through the privacy officer or compliance hotline',
        [
            'Confront the coworker in the patient waiting area without reporting',
            'Delete system access logs so the coworker cannot be identified',
            'Confront the coworker publicly in the waiting room without involving leadership',
        ],
        'Workforce members are expected to escalate suspected privacy violations internally so the entity can investigate and mitigate harm. Public disclosure or tampering with evidence can worsen breaches and violate policy.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-027
    fact(
        'ccma-hipaa',
        'The practice wants to text patients their lab results using personal smartphones. What approach aligns with HIPAA security expectations?',
        'Use a compliant messaging platform with patient consent and warnings',
        [
            'Send the full chart through standard unencrypted SMS to a number on file',
            'Text a link to the patient portal without verifying the phone number on file',
            'Add patients to an unencrypted group chat that includes unrelated staff',
        ],
        'Consumer texting apps may lack required safeguards for ePHI. Covered entities should implement vendor solutions or documented patient agreements that address confidentiality and retention.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-028
        fact('ccma-hipaa', 'Which category of health information does the HIPAA Security Rule primarily protect?', 'Electronic PHI protected by administrative and technical safeguards', ['Paper records stored in locked file rooms with no electronic systems', 'Records kept on paper with no electronic system in place', 'Printed patient education handouts left in the lobby'], 'The Security Rule applies to ePHI held or transmitted by covered entities and business associates. Paper-only workflows and printed handouts may still fall under the Privacy Rule, but the Security Rule targets electronic systems and media.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-029
        fact('ccma-hipaa', 'A billing clerk needs a diagnosis code to submit a claim. How does the minimum necessary standard apply?', 'Use the PHI required for the billing task rather than the whole chart', ["Email the complete chart to every payer contact for convenience", "Post the patient diagnosis on the clinic lobby monitor for staff", "Automatically forward all future lab results to the patient's employer"], 'Minimum necessary limits internal uses and external disclosures to the amount needed for the stated purpose. Routine dumping of full records increases exposure without business justification.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-030
    fact(
        'ccma-hipaa',
        'A patient signs a form allowing records to be sent to a disability attorney. Which element must appear on a valid HIPAA authorization?',
        'A description of the information to be disclosed and the purpose',
        [
            "Blank permission to release every record with no stated reason or end date",
            "A verbal okay from an unidentified caller without the patient's signature",
            "The patient's email address typed by the caller without verification",
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
        fact('ccma-hipaa', 'Which workstation practices satisfy common HIPAA Security Rule technical safeguards for the EHR?', 'Unique user IDs, automatic logoff, and screens away from public view', ["One shared password posted on every monitor in the nurses' station", "Leaving sessions open overnight so the next shift saves login time", "Disabling automatic lock because staff memorize each other's credentials"], 'Access controls and workstation use policies reduce unauthorized viewing of ePHI. Shared accounts and always-open sessions prevent accurate audit trails and invite snooping.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-033
    fact(
        'ccma-hipaa',
        'A quality team reviews aggregate readmission rates with all patient names removed using the HIPAA Safe Harbor method. How is that dataset classified?',
        'De-identified health information that is not PHI',
        [
            'PHI because a health-related number identifies someone',
            'PHI unless the patient signs a new authorization every month',
            'Public domain information that may be sold without restrictions',
        ],
        'Proper de-identification under Safe Harbor or expert determination removes HIPAA protections. Aggregate quality metrics without identifiers support improvement without triggering PHI rules.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-034
    fact(
        'ccma-hipaa',
        'A medical assistant works at a check-in desk visible from the waiting room. Which workstation habit best protects ePHI?',
        'Lock the screen when stepping away and angle the monitor away',
        [
            "Leave the prior patient's chart open while calling the next person",
            "Store login passwords on sticky notes attached to the keyboard",
            "Connect the EHR through unsecured public Wi-Fi with no VPN",
        ],
        'Physical safeguards complement technical controls by limiting who can see screens in public areas. Visible charts and shared credentials are frequent sources of incidental disclosure.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-035
    fact(
        'ccma-hipaa',
        'After a risk analysis shows laptops may leave the clinic with ePHI, what Security Rule safeguard is commonly implemented?',
        'Encrypting portable device storage when the risk analysis warrants it',
        [
            'Prohibiting encryption because HIPAA forbids protecting laptops',
            'Ignoring the finding because encryption is not considered after analysis',
            'Emailing ePHI to a personal address instead of storing it locally',
        ],
        'Addressable specifications require covered entities to implement a safeguard or document why an equivalent measure is reasonable. Encryption mitigates loss or theft of mobile media.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-036
    fact(
        'ccma-hipaa',
        'A caller requests a copy of imaging results for a patient who is not present. What identity verification approach is appropriate?',
        'Follow facility policy with pre-established identifiers',
        [
            "Release records when the caller states a date of birth",
            "Fax results immediately if the caller knows the patient's nickname",
            "Omit verification because voice recognition apps are accurate",
        ],
        'The right of access and minimum necessary rules assume the requester is who they claim to be. Weak verification enables wrongful disclosure to strangers or domestic abusers.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-037
    fact(
        'ccma-hipaa',
        'A marketing firm offers payment if the clinic emails patient lists for a supplement promotion. When is patient authorization required?',
        'For the marketing use because it is not a permitted disclosure',
        [
            'When the patient is hospitalized, not in outpatient clinics',
            'When the clinic already has the email address of the patient on file',
            'When the promotion covers wellness items the patient already uses',
        ],
        'Financially motivated marketing to sell unrelated products generally needs explicit authorization, while core TPO and legally required public health reporting follow different pathways. An email address on file, a hospitalized status, and a wellness-themed promotion do not create authorization.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-038
    fact(
        'ccma-hipaa',
        'Unencrypted backup tapes with PHI are stolen from a courier van. What must the covered entity do first under the Breach Notification Rule?',
        'Perform a risk assessment to decide whether notification is required',
        [
            'Suspend all system access while the investigation of the loss proceeds',
            'Omit documentation because criminal theft exempts HIPAA duties',
            'Notify the courier first and document the incident afterward',
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
            'A business associate agreement with the employer of the researcher',
            'A verbal promise that the research laptop stays with the team',
            'A business associate agreement replacing institutional review board oversight',
        ],
        'Limited data sets exclude direct identifiers but may retain certain geographic and date elements. Recipients must sign data use agreements, so an agreement with the employer, a verbal promise about the laptop, and business associate terms do not qualify.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-040
        fact('ccma-hipaa', 'A patient requests an accounting of disclosures for the past three years. Which type of disclosure will usually appear on that list?', 'Disclosures outside treatment, payment, and operations', ["Every internal note another clinician read for the patient's care", "Routine claim transmissions to the health plan for payment", "Casual text messages staff sent about weekend plans without PHI"], 'Accounting focuses on non-routine sharing such as many research or legal disclosures. Everyday TPO and many treatment-related exchanges are excluded unless law requires listing them.', [S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-041
    fact(
        'ccma-hipaa',
        'A vendor offers to sell a clinic list of patients with full names and MRNs for outreach. Why does that dataset fail HIPAA de-identification?',
        'It retains direct identifiers that tie health information to people',
        [
            'It contains clinical details that the vendor will use for marketing',
            'Quality improvement projects may not use health-related numbers',
            'De-identified and PHI are legally identical terms with no difference',
        ],
        'PHI remains regulated until identifiers are removed under Safe Harbor or expert certification. The intended marketing use, a blanket limit on quality improvement work, and treating the two terms as synonyms do not describe de-identification.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-042
    fact(
        'ccma-hipaa',
        'A patient asks the clinic not to bill the spouse\'s insurance because it would reveal sensitive care. How should the practice handle a restriction request?',
        'Follow Privacy Rule procedures to consider the request and document limits',
        [
            'Ignore the patient because insurers receive every diagnosis automatically',
            'Tell the patient that the restriction cannot be honored at all by the practice',
            'Require the patient to pay the full balance before the request is reviewed',
        ],
        'Patients may request limits on certain disclosures to health plans when they pay out of pocket in full, among other situations. Entities are not required to agree in every case but must use the formal process.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-hipaa-043
        fact('ccma-hipaa', 'A behavioral health provider keeps separate psychotherapy notes from progress notes in the EHR. What disclosure rule applies to those psychotherapy notes?', 'They need patient authorization for most uses outside exceptions', ['They may be shared with a relative who asks about the care', 'They follow the same authorization rules as the rest of the chart', 'They have no HIPAA protection and may be shared with visitors'], 'Psychotherapy notes are defined narrowly and receive extra consent requirements, so sharing them with a relative or treating them like the rest of the chart does not meet that rule. General medical record entries about medications or hospitalization follow different disclosure rules.', [S.NHA_CCMA], 'advanced'),

    # ccma-hipaa-044
    fact(
        'ccma-hipaa',
        'A specialist shares operative details with the referring primary care provider to coordinate follow-up. Is individual patient authorization required for this exchange?',
        'No, when the disclosure is for treatment purposes',
        [
            'Yes, every treatment-related fax needs a new signed authorization',
            'No, because a bystander may receive the full record on request',
            'Yes, unless the patient posted a de-identified clinic photo online',
        ],
        'Treatment disclosures among providers involved in care are core permitted uses without separate authorization. Disclosures must still respect minimum necessary and facility policy.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-045
    fact(
        'ccma-hipaa',
        'Home health staff carry tablets with ePHI into patients\' homes. Which safeguard addresses loss of those portable devices?',
        'Encrypting device storage and using remote wipe after risk analysis',
        [
            'Storing tablets unlocked in vehicles because encryption is banned by HIPAA',
            'Relying on a sign-out sheet instead of a documented risk analysis',
            'Limiting encryption to desktop billing computers and excluding field tablets',
        ],
        'Portable media face theft and loss outside the clinic. Addressable encryption and device management reduce the chance that ePHI is readable if hardware disappears.',
        [S.NHA_CCMA],
        'intermediate',
    ),

    # ccma-hipaa-046
        fact('ccma-hipaa', 'What does the HIPAA minimum necessary standard require when using protected health information?', 'Limit access and disclosure to what the purpose requires', ['Share the entire chart with a vendor who requests access', 'Post visit summaries on a public bulletin board in the waiting room', 'Email full records to personal accounts for staff convenience'], 'Minimum necessary reduces privacy risk for treatment, payment, and operations. Broad sharing without role-based limits violates the Privacy Rule.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-047
        fact('ccma-hipaa', 'A patient requests a copy of their medical record. What should the office do?', 'Follow right-of-access procedures, including timelines and fees', ['Deny all requests because charts are clinic property without exception', 'Give records to a neighbor without verifying legal authority', 'Require the patient to delete their own diagnoses before copies are sent'], 'Patients generally have a right to access their PHI with defined exceptions. Neighbors lack authority unless documented; outright denial conflicts with access rules.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-048
        fact('ccma-hipaa', 'Which disclosure is generally permitted without patient authorization for treatment purposes?', 'Sharing clinical information with a provider involved in care', ['Selling the list of diagnoses to a marketing firm for outreach', 'Sharing clinical photographs with a coworker of the patient', 'Giving records to an employer who requests them out of curiosity'], 'HIPAA permits TPO disclosures among involved professionals. Marketing and employer curiosity are not treatment purposes.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-049
    fact(
        'ccma-hipaa',
        'What is required before a business associate may handle electronic protected health information for a covered entity?',
        'A business associate agreement with required safeguards',
        ['A verbal agreement without required contractual safeguards',
        'A written agreement that omits the required privacy safeguards',
        'A signed agreement covering billing and not clinical services'],
        'The Security Rule expects contractual obligations for vendors touching ePHI. An informal promise, an agreement without the safeguards list, and a billing-only contract do not replace a complete business associate agreement.',
        [S.HHS_HIPAA_SECURITY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-hipaa-050
    fact(
        'ccma-hipaa',
        'Where should patient conversations about diagnoses occur to protect privacy?',
        'In private treatment areas away from public corridors',
        [
            'In a crowded elevator with visitors and families present',
            'At the front desk with the waiting line listening',
            'In the cafeteria during the lunch hour',
        ],
        'HIPAA safeguards oral disclosures; public areas risk incidental exposure. Private rooms or lowered voices in enclosed spaces reduce breaches.',
        [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-hipaa-051
        fact('ccma-hipaa', "A workforce member accesses a celebrity's chart out of curiosity without a job reason. What risk does this create?", 'A privacy violation that may require investigation and workforce sanction', ['Improved public relations for the clinic when celebrity charts are viewed', 'Automatic HIPAA waiver for all staff after one unauthorized lookup', 'Permission to discuss the chart casually in the staff break room'], 'Minimum necessary and role-based access prohibit curiosity browsing. Sanctions and breach analysis may follow unauthorized access.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-052
        fact('ccma-hipaa', 'Which action helps secure electronic health record workstations?', 'Log off or lock sessions when leaving the desk unattended', ['Share login credentials with float staff to avoid password resets', 'Leave prior patient charts open in public view for faster access', 'Disable passwords on workstations to speed rooming workflows'], 'Automatic timeouts and unique credentials protect ePHI under the Security Rule. Shared logins break audit trails.', [S.HHS_HIPAA_SECURITY, S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-053
        fact('ccma-hipaa', 'A patient authorizes release of records to a specific attorney. What should be verified before sending?', 'The authorization is signed, dated, and lists the correct recipient', ["That the attorney is licensed in the state where the clinic sits", "That the records release fee has been paid before the records are mailed", "That the patient remains an active patient of the clinic at the time"], 'Valid authorizations specify who may receive PHI. Attorney licensure and similar names still require identity checks to avoid misdirected disclosures.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'intermediate'),

    # ccma-hipaa-054
        fact('ccma-hipaa', 'Which fax practice reduces misdirected protected health information?', 'Verify the recipient number and use a confidentiality cover sheet', ['Send to the last number dialed on the fax machine without checking', 'Include every diagnosis in the subject line read aloud in the hallway', 'Fax to the front desk printer in a public area without prompt retrieval'], 'Confirmation and cover sheets limit wrong routing. Public unattended prints expose PHI.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'beginner'),

    # ccma-hipaa-055
        fact('ccma-hipaa', "A patient requests amendment of an error in their record. What is the covered entity's obligation?", 'Review and respond per the Privacy Rule, accepting or denying', ['Ignore the request because legal medical records cannot be changed', 'Delete the entire chart instead of correcting the disputed entry', 'Charge a fee to refuse automatically without following policy'], 'Patients have rights to request amendments with defined timelines. Wholesale deletion is not the pathway for correcting a single error.', [S.HHS_HIPAA_PRIVACY, S.NHA_CCMA], 'intermediate'),

]
