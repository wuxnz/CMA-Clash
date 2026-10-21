# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Eight additional ABCD facts per topic to reach 28 questions per quiz set."""

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    fact(
        'ccma-foundational',
        'The suffix "-emia" in a term such as hyperglycemia refers to:',
        'A blood condition',
        [
            'A surgical incision',
            'A bone fracture',
            'A skin rash only'
        ],
        'The suffix -emia denotes a blood-related condition.',
        [
            S.NHA_CCMA,
        S.MEDLINEPLUS_HAND_HYGIENE
        ],
        'beginner',
    ),
    fact(
        'ccma-foundational',
        'Homeostasis in the human body means:',
        'Maintaining a stable internal environment despite external changes',
        [
            'Stopping all metabolic activity',
            'Eliminating the need for hormones',
            'Keeping body temperature fixed with no physiologic variation'
        ],
        'Set points for temperature, glucose, and pH are regulated by feedback.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'The metric prefix "kilo-" denotes a factor of:',
        '1,000',
        [
            '0.001',
            '100',
            '1,000,000'
        ],
        'Kilo- multiplies the base unit by one thousand.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-foundational',
        'Evidence-based practice in ambulatory care combines:',
        'Best research evidence, clinical expertise, and patient values',
        [
            'Tradition only',
            'Social media trends',
            'Billing codes alone'
        ],
        'EBP integrates science with patient preferences and clinician judgment.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        "A medical assistant's role in diagnosis is generally to:",
        'Collect data and report findings to the supervising provider',
        [
            'Independently establish all final diagnoses',
            'Prescribe controlled substances without oversight',
            'Order MRI without provider direction'
        ],
        'Scope is defined by state law, certification, and employer policy.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-foundational',
        'At standard atmospheric pressure, water boils at:',
        '100°C (212°F)',
        [
            '0°C (32°F)',
            '37°C (98.6°F)',
            '50°C (122°F)'
        ],
        'Metric temperature scales are used in many clinical settings.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-foundational',
        'The combining form "my/o" relates to:',
        'Muscle',
        [
            'Bone marrow only',
            'Ear',
            'Liver'
        ],
        'My/o appears in terms such as myopathy and myalgia.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-foundational',
        'Quality improvement (QI) in a clinic aims to:',
        'Systematically improve care processes and patient outcomes',
        [
            'Punish staff without system review',
            'Hide errors from leadership',
            'Replace guidelines with personal opinion'
        ],
        'QI uses measurement and teamwork to reduce harm.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The tricuspid valve lies between the:',
        'Right atrium and right ventricle',
        [
            'Left atrium and left ventricle',
            'Aorta and left ventricle',
            'Pulmonary vein and left atrium'
        ],
        'Right-sided AV valve prevents backflow into the atrium.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'Insulin is produced primarily by:',
        'Pancreatic beta cells in the islets of Langerhans',
        [
            'Hepatocytes',
            'Adrenal medulla',
            'Thyroid follicular cells'
        ],
        'Beta cells lower blood glucose by secreting insulin.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The primary muscle of inspiration is the:',
        'Diaphragm',
        [
            'Trapezius',
            'Gastrocnemius',
            'Masseter'
        ],
        'Diaphragm contraction increases thoracic volume.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-anatomy',
        'Red bone marrow is chiefly responsible for:',
        'Hematopoiesis (blood cell formation)',
        [
            'Bile production',
            'Filtration of cerebrospinal fluid',
            'Production of surfactant'
        ],
        'Marrow produces erythrocytes, leukocytes, and platelets.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The cerebellum primarily coordinates:',
        'Balance and fine motor control',
        [
            'Vision only',
            'Hearing only',
            'Olfaction'
        ],
        'Cerebellar injury causes ataxia and coordination deficits.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The femur is:',
        'The longest and strongest bone in the body',
        [
            'A bone of the inner ear',
            'The collarbone',
            'A wrist carpal bone'
        ],
        'The thigh bone supports weight and enables locomotion.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-anatomy',
        'The hepatic portal vein carries blood from the:',
        'Gastrointestinal tract to the liver',
        [
            'Lungs to the left atrium',
            'Kidneys to the bladder',
            'Brain to the heart directly'
        ],
        'Portal circulation delivers absorbed nutrients to the liver.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'Alveoli in the lungs are the site of:',
        'Gas exchange between air and blood',
        [
            'Urine formation',
            'Insulin secretion',
            'Erythropoietin production only'
        ],
        'Thin alveolar-capillary membranes allow O2 and CO2 diffusion.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-clinical-care',
        'When applying elastic bandage compression, the MA should:',
        'Check distal circulation, sensation, and warmth after application',
        [
            'Wrap as tightly as possible without assessment',
            'Leave toes or fingers uncovered without checking color',
            'Reuse soiled bandages on another patient'
        ],
        'Circulation checks help prevent neurovascular compromise.',
        [
            S.NHA_CCMA,
        S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Assisting with suture removal typically requires:',
        'Sterile or clean technique per provider order and policy',
        [
            'Pulling sutures without hand hygiene',
            'Using non-sterile scissors on infected wounds without plan',
            'Removing all sutures if one area looks red without notifying provider'
        ],
        'Technique and observation reduce infection risk.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'A patient scheduled for a fasting lab draw should be instructed:',
        'Not to eat or drink anything except water if allowed for the ordered test',
        [
            'To drink juice before the draw',
            'To skip water for 24 hours unless told otherwise',
            'To take double diabetes medication before the test'
        ],
        'Fasting instructions follow the specific lab order.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-clinical-care',
        'When performing a visual acuity screening, the patient should:',
        'Use corrective lenses if normally worn unless instructed otherwise',
        [
            'Squint through a pinhole only',
            'Close one eye permanently',
            'Stand 20 feet from any chart without protocol'
        ],
        'Testing conditions should mimic usual vision correction.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-clinical-care',
        'Applying heat therapy in clinic is generally avoided over:',
        'Acute inflammation, open wounds, or areas with impaired sensation',
        [
            'Chronic muscle spasm when ordered',
            'Healed scars when ordered',
            'Stiff joints when ordered'
        ],
        'Heat can worsen acute inflammation or burn insensate skin.',
        [
            S.NHA_CCMA,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'When collecting a clean-catch urine specimen, the patient should:',
        'Clean the urinary meatus and discard the first portion before collecting midstream urine',
        [
            'Collect the first stream only without cleaning',
            'Use the same container for multiple patients',
            'Add tap water if volume is low'
        ],
        'Midstream clean-catch reduces contamination.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'Orthostatic vital sign measurement compares:',
        'Blood pressure and heart rate lying, sitting, and standing',
        [
            'Temperature only in each position',
            'Respiratory rate after exercise only',
            'Pain score without position change'
        ],
        'Orthostatic changes may indicate hypovolemia or autonomic dysfunction.',
        [
            S.NHA_CCMA,
        S.CDC_HBP
        ],
        'intermediate',
    ),
    fact(
        'ccma-clinical-care',
        'When a patient faints during a procedure, the MA should:',
        'Lower the patient safely, assess responsiveness and breathing, and summon help',
        [
            'Hold the patient upright by the hair',
            'Give food by mouth while unconscious',
            'Leave the room to finish paperwork'
        ],
        'Syncope requires ABC assessment and escalation.',
        [
            S.NHA_CCMA,
        S.RED_CROSS_FIRST_AID
        ],
        'beginner',
    ),
    fact(
        'ccma-coordination',
        'Care coordination after hospital discharge should include:',
        'Scheduling follow-up and reviewing new medications with the patient',
        [
            'Discarding discharge instructions',
            'Assuming the hospital will call the patient',
            'Deleting the problem list'
        ],
        'Transitions of care reduce readmissions and medication errors.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'A teach-back method helps confirm patient understanding by:',
        'Asking the patient to explain instructions in their own words',
        [
            'Reading the handout silently to yourself',
            'Assuming literacy without checking',
            'Giving only written material in English'
        ],
        'Teach-back uncovers gaps in comprehension.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-coordination',
        'When coordinating home health services, the MA documents:',
        'Referral sent, services ordered, and patient consent per policy',
        [
            "Only the patient's favorite color",
            'Unrelated billing codes',
            'Staff vacation schedules'
        ],
        'Documentation supports continuity and billing accuracy.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'Population health outreach calls for overdue screenings aim to:',
        'Close care gaps such as mammography or A1C testing',
        [
            'Sell unrelated products',
            'Replace provider visits',
            'Share PHI on social media'
        ],
        'Outreach improves preventive care adherence.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'At transitions of care, medication reconciliation compares:',
        'All medications the patient takes with the current clinic list',
        [
            'Only vitamins the patient likes',
            'Medications from one day only',
            'Herbal products the patient denies'
        ],
        'Accurate lists prevent omissions and interactions.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'Patient portal enrollment education should cover:',
        'Secure messaging limits and when to call 911',
        [
            'Sharing passwords with family by default',
            'Using portal for emergencies instead of 911',
            'Posting results publicly'
        ],
        'Portals supplement but do not replace urgent care.',
        [
            S.HHS_HIPAA_PRIVACY,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-coordination',
        'Community resource referrals (food bank, transport) require:',
        'Patient consent and documentation per clinic workflow',
        [
            'Automatic disclosure to media',
            'No follow-up',
            'Mandatory public posting'
        ],
        'Social needs affect adherence and outcomes.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-coordination',
        'Closed-loop referral tracking means:',
        'Confirming the specialist appointment occurred and results return to the PCP',
        [
            'Sending referral and never following up',
            'Assuming patient went without contact',
            'Filing referral in trash'
        ],
        'Loop closure prevents lost test results.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-admin',
        'ICD-10-CM codes primarily describe:',
        'Diagnoses and reasons for encounter',
        [
            'Surgical instruments',
            'Staff schedules',
            'Room temperature logs'
        ],
        'Diagnosis coding supports claims and quality reporting.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-admin',
        'A superbill or encounter form links:',
        'Services provided with diagnosis and procedure codes',
        [
            'Patient hobbies with payroll',
            'Parking tickets with labs',
            'Social security numbers with marketing'
        ],
        'Charge capture requires accurate coding.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-admin',
        'Prior authorization for a procedure means:',
        'Payer approval may be required before the service is performed',
        [
            'The patient never pays copay',
            'HIPAA is waived',
            'The MA may perform surgery'
        ],
        'Auth prevents denials for non-covered services.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-admin',
        'Days in accounts receivable (A/R) measure:',
        'How quickly the practice collects payment after service',
        [
            'Number of patients in waiting room',
            'Vaccine refrigerator temperature',
            'Needlestick rate'
        ],
        'Lower A/R days improve cash flow.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-admin',
        'When scanning insurance cards, the MA should verify:',
        'Member ID, group number, and effective dates are legible in the EHR',
        [
            'Only the card color',
            'Employer picnic date',
            'Patient shoe size'
        ],
        'Accurate demographics reduce claim rejections.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-admin',
        'Coordination of benefits applies when a patient has:',
        'More than one active insurance plan',
        [
            'No insurance',
            'Only cash pay always',
            'Only vision insurance for surgery'
        ],
        'Primary and secondary payers must be identified.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-admin',
        'A remittance advice (ERA) explains:',
        'How a claim was paid or denied',
        [
            'Cafeteria menu',
            'Staff performance reviews',
            'Parking assignments'
        ],
        'ERAs guide posting payments and appeals.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-admin',
        'Registering a minor patient typically requires:',
        'Guardian identification and custody documentation when applicable',
        [
            "Only the child's signature",
            'No guardian information',
            'Public internet posting of address'
        ],
        'Legal guardianship affects consent and billing.',
        [
            S.HHS_HIPAA_PRIVACY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'Health literacy–appropriate education uses:',
        'Plain language and avoids unexplained jargon',
        [
            'Only Latin abbreviations',
            'Complex journal articles without summary',
            'Assuming all patients read at college level'
        ],
        'Plain language improves comprehension and safety.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-communication',
        'When obtaining a chief complaint, open-ended questions:',
        'Let the patient describe concerns in their own words',
        [
            'Force yes/no answers only',
            'Interrupt every 5 seconds',
            'Assume complaint from chart only'
        ],
        'Open questions reveal patient priorities.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-communication',
        'Cultural competence in communication includes:',
        'Respecting beliefs that affect care decisions',
        [
            'Imposing staff beliefs on patients',
            'Refusing interpreters',
            'Mocking dietary practices'
        ],
        'Respect builds trust and adherence.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'Telephone triage messages for the provider should include:',
        'Patient name, callback number, symptoms, and urgency',
        [
            'Gossip about other patients',
            'Full social security number shouted in waiting room',
            'No clinical details'
        ],
        'Complete messages support safe callbacks.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'Nonverbal communication that supports rapport includes:',
        'Appropriate eye contact and open posture at eye level when possible',
        [
            'Turning back while patient talks',
            'Standing over patient with arms crossed',
            'Reading phone during disclosure'
        ],
        'Body language affects patient comfort.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-communication',
        'Apologizing for a clinic delay while maintaining professionalism means:',
        'Acknowledging inconvenience and giving a realistic update',
        [
            'Blaming the patient',
            'Promising exact times you cannot guarantee',
            'Ignoring complaints'
        ],
        'Empathy reduces escalation.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-communication',
        'Documenting patient education should reflect:',
        'Topics covered, materials given, and patient response',
        [
            'Only that education occurred without content',
            'Staff opinions about patient',
            'Unrelated billing notes only'
        ],
        'Specific notes support continuity and liability defense.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-communication',
        'When a patient uses an assistive communication device, the MA should:',
        'Allow adequate time and address the patient directly',
        [
            'Speak only to the caregiver always',
            'Rush the encounter',
            'Take the device away'
        ],
        'Direct engagement respects autonomy.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Justice as a bioethical principle refers to:',
        'Fair distribution of benefits and burdens of care',
        [
            'Providing luxury services only to friends',
            'Ignoring insurance status always',
            'Withholding care based on bias'
        ],
        'Justice opposes discriminatory allocation.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Fidelity in healthcare means:',
        'Keeping promises and being faithful to professional duties',
        [
            'Sharing patient secrets online',
            'Abandoning patients without coverage',
            'Practicing outside training without disclosure'
        ],
        'Trust depends on reliability and honesty.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-law-ethics',
        'A durable power of attorney for healthcare:',
        'Names an agent to make medical decisions if the patient is incapacitated',
        [
            'Transfers property only',
            'Eliminates need for any consent ever',
            'Allows MA to practice medicine independently'
        ],
        'Advance directives guide care when patients cannot decide.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'State Good Samaritan statutes for lay rescuers typically:',
        'Limit civil liability when emergency aid is given in good faith without gross negligence',
        [
            'Protect intentional harm',
            'Apply to billing fraud',
            'Eliminate documentation requirements in clinic'
        ],
        'Laws vary by state; intent and setting matter.',
        [
            S.NHA_CCMA,
        S.RED_CROSS_FIRST_AID
        ],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'Conflict of interest in healthcare should be:',
        'Disclosed and managed to prioritize patient welfare',
        [
            'Hidden from patients',
            'Used to select poorer treatments for profit',
            'Ignored if profitable'
        ],
        'Transparency maintains trust.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-law-ethics',
        'Minors may consent to certain services without parental consent when:',
        'State law allows (e.g., some reproductive or mental health services)',
        [
            'Never under any circumstance',
            'Whenever the minor wants surgery for fun',
            'Only if parent is in waiting room'
        ],
        'Consent laws vary by state and service.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'ccma-law-ethics',
        'Plagiarism in patient education materials is:',
        'Unethical and may violate copyright law',
        [
            'Encouraged to save time',
            'Acceptable without attribution',
            'Required by HIPAA'
        ],
        'Credit sources and use licensed materials.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'ccma-law-ethics',
        'When uncertain about legality of a requested action, the MA should:',
        'Seek guidance from supervisor, compliance, or provider before proceeding',
        [
            'Proceed to avoid delay',
            'Ask uninvolved patients',
            'Post question on social media'
        ],
        'Compliance resources clarify legal boundaries.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'ccma-vaccines',
        'Diluent packaged with a vaccine must be:',
        'Used only with the specific vaccine manufacturer pairing indicated on the label',
        [
            'Mixed with any other vaccine vial',
            'Stored indefinitely after opening without dating',
            'Shared between clinics without cold chain'
        ],
        'Wrong diluent pairing inactivates or harms potency.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN
        ],
        'advanced',
    ),
    fact(
        'ccma-vaccines',
        'Vaccine refrigerator temperature should be monitored in:',
        'Degrees Celsius with calibrated thermometers or digital loggers',
        [
            'Staff guesswork only',
            'Fahrenheit without conversion ever',
            'Outdoor weather reports'
        ],
        'CDC storage toolkit specifies Celsius ranges for units.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN
        ],
        'intermediate',
    ),
    fact(
        'ccma-vaccines',
        'A vaccine with cracked glass or particulates should be:',
        'Not administered and reported per policy',
        [
            'Shaken and used anyway',
            'Filtered through cotton',
            'Mixed with diluent to dissolve particles'
        ],
        'Inspect vials before administration.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN,
        S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'ccma-vaccines',
        'Intranasal live attenuated influenza vaccine (when used) is contraindicated in:',
        'Severely immunocompromised persons per product labeling',
        [
            'All adults over 65 automatically always',
            'Anyone with hypertension',
            'Anyone wearing glasses'
        ],
        'Live intranasal vaccines have specific contraindications.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN
        ],
        'advanced',
    ),
    fact(
        'ccma-vaccines',
        'Anaphylaxis after vaccination is managed with:',
        'Epinephrine and emergency response per protocol',
        [
            'Observation only without treatment',
            'Oral antihistamine alone as sole therapy for anaphylaxis',
            'Sending patient home immediately'
        ],
        'Anaphylaxis is a medical emergency.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN,
        S.RED_CROSS_FIRST_AID
        ],
        'advanced',
    ),
    fact(
        'ccma-vaccines',
        'Vaccine lot number documentation is important for:',
        'Safety tracking and recall management',
        [
            'Decorating the chart',
            'Billing only without clinical use',
            'Deleting inventory'
        ],
        'Lot numbers link to manufacturer recalls.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN
        ],
        'beginner',
    ),
    fact(
        'ccma-vaccines',
        'Shingrix (recombinant zoster vaccine) is typically given:',
        'Intramuscularly in two doses separated per ACIP schedule',
        [
            'Orally with first meal',
            'Intradermally only always',
            'Once lifetime in infancy only'
        ],
        'Follow current ACIP product-specific schedules.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN
        ],
        'advanced',
    ),
    fact(
        'ccma-vaccines',
        'Vaccine waste should be:',
        'Documented and disposed per facility and program policy',
        [
            'Poured down sink',
            'Given to staff as bonuses',
            'Mixed into next vial'
        ],
        'Accountability supports inventory and safety.',
        [
            S.CDC_VACCINE_STORAGE,
        S.CDC_VACCINE_ADMIN
        ],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'The HIPAA Privacy Rule applies to:',
        'Individually identifiable protected health information held or transmitted by covered entities and their business associates',
        [
            'De-identified data prepared per HIPAA methods',
            'Public weather data',
            'Restaurant menus'
        ],
        'PHI requires safeguards and permitted uses.',
        [
            S.HHS_HIPAA_PRIVACY
        ],
        'beginner',
    ),
    fact(
        'ccma-hipaa',
        'Patients may request a copy of their medical record and:',
        'Receive it within time frames established by HIPAA and state law',
        [
            'Be denied all access automatically',
            'Receive only if they pay a penalty fee not allowed by law',
            "Get another patient's record"
        ],
        'Right of access is a core HIPAA provision.',
        [
            S.HHS_HIPAA_PRIVACY
        ],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'A facility directory may disclose limited information (e.g., location in facility) if:',
        'The patient has been informed and has opportunity to agree or object',
        [
            'Always includes full diagnosis to any caller',
            'Includes SSN to marketers',
            'Is posted on the internet'
        ],
        'Directory disclosures are limited and optional for patients.',
        [
            S.HHS_HIPAA_PRIVACY
        ],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'Encryption of laptops containing ePHI is an example of:',
        'A technical safeguard under the Security Rule',
        [
            'A marketing technique',
            'Optional with no risk analysis ever',
            'Prohibited by OSHA'
        ],
        'Risk analysis guides safeguard selection.',
        [
            S.HHS_HIPAA_SECURITY
        ],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'Reporting suspected HIPAA violations internally should follow:',
        'Facility privacy and compliance policies',
        [
            'Posting on personal social media first',
            'Ignoring unless media asks',
            'Deleting audit logs'
        ],
        'Internal reporting enables investigation and mitigation.',
        [
            S.HHS_HIPAA_PRIVACY,
        S.HHS_HIPAA_SECURITY
        ],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'Psychotherapy notes receive:',
        'Stronger protection than general medical record under HIPAA',
        [
            'No protection',
            'Automatic public posting',
            'Marketing use without consent'
        ],
        'Separate authorization rules apply to psychotherapy notes.',
        [
            S.HHS_HIPAA_PRIVACY
        ],
        'advanced',
    ),
    fact(
        'ccma-hipaa',
        'Minimum necessary in workforce access means:',
        'Staff receive access to only the PHI needed for their job',
        [
            'All staff access all charts',
            'Interns access payroll of celebrities',
            'Volunteers access research database without training'
        ],
        'Role-based access reduces breach risk.',
        [
            S.HHS_HIPAA_SECURITY
        ],
        'intermediate',
    ),
    fact(
        'ccma-hipaa',
        'A valid HIPAA authorization must include:',
        'Specific description of information and purpose of disclosure',
        [
            'Blanket permission for all future uses forever',
            'No expiration date required always',
            'Verbal okay only without signature when written required'
        ],
        'Authorizations have required elements.',
        [
            S.HHS_HIPAA_PRIVACY
        ],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Varicella (chickenpox) in a hospitalized patient typically requires:',
        'Airborne and Contact Precautions per CDC',
        [
            'Droplet Precautions only',
            'No precautions',
            'Standard Precautions without isolation'
        ],
        'Varicella virus spreads via airborne and contact routes.',
        [
            S.CDC_ISOLATION_2007
        ],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Measles requires:',
        'Airborne Precautions and respiratory protection when entering room',
        [
            'Contact Precautions only',
            'No mask for staff',
            'Negative pressure is optional always'
        ],
        'Measles is highly contagious via airborne spread.',
        [
            S.CDC_ISOLATION_2007
        ],
        'advanced',
    ),
    fact(
        'ccma-transmission',
        'Scabies infestation generally requires:',
        'Contact Precautions until treatment completed per policy',
        [
            'Airborne isolation only',
            'No linen handling precautions',
            'Sharing patient clothing'
        ],
        'Mites spread by prolonged skin contact.',
        [
            S.CDC_ISOLATION_2007
        ],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Enteric pathogens such as norovirus emphasize:',
        'Contact Precautions and rigorous environmental cleaning',
        [
            'Droplet mask alone',
            'No hand hygiene after glove removal',
            'Reusing commodes without disinfection'
        ],
        'Norovirus resists some disinfectants; cleaning protocols matter.',
        [
            S.CDC_ISOLATION_2007,
        S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Sharps containers in isolation rooms should be:',
        'Emptied and handled using same PPE and precautions as patient care',
        [
            'Overfilled without replacement',
            'Carried open through hallway',
            'Reused after rinsing'
        ],
        'OSHA and CDC address sharps safety in isolation.',
        [
            S.CDC_ISOLATION_2007,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'A patient with draining MRSA wound should be on:',
        'Contact Precautions plus Standard Precautions',
        [
            'Airborne Precautions only',
            'No precautions if on antibiotics',
            'Protective environment only'
        ],
        'Contact Precautions reduce spread of resistant organisms.',
        [
            S.CDC_ISOLATION_2007
        ],
        'intermediate',
    ),
    fact(
        'ccma-transmission',
        'Lice (pediculosis) management includes:',
        'Contact Precautions and treatment of infested persons',
        [
            'Airborne isolation',
            'No treatment of close contacts',
            'Sharing combs between patients'
        ],
        'Contact precautions limit spread until treated.',
        [
            S.CDC_ISOLATION_2007
        ],
        'beginner',
    ),
    fact(
        'ccma-transmission',
        'When aerosol-generating procedures are performed on airborne isolation patients, staff should use:',
        'Fit-tested N95 or higher respirator per policy',
        [
            'Surgical mask only always',
            'No eye protection',
            'Street clothing'
        ],
        'AGPs increase airborne exposure risk.',
        [
            S.CDC_ISOLATION_2007
        ],
        'advanced',
    ),
    fact(
        'ekg-leads',
        'Electrode site preparation before ECG should include:',
        'Cleaning skin and removing oils or lotions when hair is not shaved',
        [
            'Applying petroleum jelly under electrodes',
            'Leaving wet alcohol without drying indefinitely',
            'Placing electrodes over wet gauze'
        ],
        'Dry, clean skin improves electrode adhesion.',
        [
            S.NHA_CET
        ],
        'beginner',
    ),
    fact(
        'ekg-leads',
        'Chest lead V4 is typically placed at the:',
        'Fifth intercostal space, midclavicular line',
        [
            'Second intercostal space at the sternal angle',
            'Xiphoid process only',
            'Right shoulder'
        ],
        'Standard precordial landmarks improve consistency.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-leads',
        'Chest lead V5 is commonly placed:',
        'Fifth intercostal space, anterior axillary line',
        [
            'Fourth intercostal space, right sternal border',
            'Over the umbilicus',
            'On the scapula'
        ],
        'V5 and V6 complete lateral precordial views.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-leads',
        'Chest lead V6 is commonly placed:',
        'Fifth intercostal space, midaxillary line',
        [
            'First intercostal space at the clavicle',
            'On the right costal margin only',
            'Over the manubrium'
        ],
        'V6 lies lateral to V5.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-leads',
        'Right leg (RL) electrode on a 12-lead ECG serves as:',
        'An electrical ground/reference rather than an active recording lead',
        [
            'The only lead that records QRS',
            'A chest precordial lead',
            'An optional electrode that may be omitted always'
        ],
        'RL helps stabilize the signal.',
        [
            S.NHA_CET
        ],
        'beginner',
    ),
    fact(
        'ekg-leads',
        'When breasts obscure landmark placement for precordial leads, the technician should:',
        'Place electrodes under breast tissue at correct anatomical landmarks',
        [
            'Place leads on top of clothing',
            'Skip V leads entirely',
            'Use only limb leads forever'
        ],
        'Landmarks remain on the chest wall.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-leads',
        'Pediatric 12-lead ECG may use:',
        'Smaller electrodes and age-appropriate lead placement per protocol',
        [
            'Adult V1 on the abdomen only',
            'No skin prep ever',
            'Only one chest lead'
        ],
        'Size and anatomy guide pediatric acquisition.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-leads',
        'Documenting ECG acquisition should include:',
        'Patient identifiers, date/time, symptoms if any, and lead type',
        [
            'Only technician initials in secret code',
            'No indication for test',
            "Another patient's name"
        ],
        'Complete metadata supports interpretation.',
        [
            S.NHA_CET
        ],
        'beginner',
    ),
    fact(
        'ekg-rhythm',
        'Sinus tachycardia is characterized by:',
        'Normal P waves before each QRS with rate greater than 100 bpm in adults',
        [
            'Irregularly irregular rhythm without P waves',
            'Chaotic fibrillatory waves only',
            'Flat line'
        ],
        'Rate criterion defines sinus tachycardia.',
        [
            S.NHA_CET
        ],
        'beginner',
    ),
    fact(
        'ekg-rhythm',
        'Atrial flutter classically shows:',
        'Sawtooth flutter waves especially in inferior leads',
        [
            'Uniform P waves with constant PR and rate 60',
            'Wide bizarre QRS at 30',
            'Asystole'
        ],
        'Flutter often has regular atrial activity around 300 bpm.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-rhythm',
        'Junctional rhythm may show:',
        'Inverted P waves before, during, or after QRS or absent P waves with narrow QRS',
        [
            'Delta waves with short PR always',
            'Ventricular rate 300 with fibrillation',
            'Tall peaked T waves only'
        ],
        'AV junction acts as pacemaker.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-rhythm',
        'Premature ventricular complexes (PVCs) appear as:',
        'Early wide QRS complexes without preceding P waves',
        [
            'Narrow QRS with preceding P always',
            'Flat baseline only',
            'Regular sawtooth waves'
        ],
        'PVCs originate in ventricles.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-rhythm',
        'Second-degree AV block Mobitz type II may:',
        'Have sudden dropped QRS beats and often wide QRS',
        [
            'Always have progressive PR prolongation before drop',
            'Never require pacemaker evaluation',
            'Show only sinus arrhythmia'
        ],
        'Mobitz II carries risk of complete heart block.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-rhythm',
        'Third-degree (complete) heart block shows:',
        'P waves and QRS complexes with no consistent relationship',
        [
            'Each P followed by QRS with constant PR',
            'Only atrial flutter waves',
            'Normal sinus rhythm only'
        ],
        'AV dissociation defines complete block.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-rhythm',
        'Monomorphic ventricular tachycardia displays:',
        'Wide QRS complexes of uniform morphology at rapid rate',
        [
            'Narrow QRS at 60 bpm',
            'Irregularly irregular narrow complexes',
            'No QRS at all'
        ],
        'VT is a potentially unstable arrhythmia.',
        [
            S.NHA_CET,
        S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-rhythm',
        'Idioventricular rhythm is often seen:',
        'Transiently after reperfusion in acute MI with slow wide QRS',
        [
            'Only in healthy athletes at rest always',
            'As normal sinus rhythm',
            'Only in children with narrow QRS at 200'
        ],
        'Accelerated idioventricular rhythm can be benign post-MI.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-intervals',
        'QRS duration greater than 0.12 seconds suggests:',
        'Ventricular conduction delay or ventricular origin of rhythm',
        [
            'Normal conduction always',
            'Short QT syndrome',
            'Sinus bradycardia only'
        ],
        'Wide QRS indicates slowed ventricular depolarization.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-intervals',
        'ST depression in multiple leads may suggest:',
        'Myocardial ischemia or strain depending on clinical context',
        [
            'Normal variant always',
            'Lead reversal only always',
            'Hyperkalemia only'
        ],
        'ST changes require clinical correlation.',
        [
            S.NHA_CET,
        S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-intervals',
        'Tall peaked T waves may be an early sign of:',
        'Hyperkalemia',
        [
            'Hypokalemia only',
            'Normal pregnancy only',
            'Lead artifact only always'
        ],
        'Serum potassium affects repolarization.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-intervals',
        'U waves may be prominent in:',
        'Hypokalemia and some bradycardias',
        [
            'Hyperkalemia always',
            'Normal sinus only never',
            'Asystole'
        ],
        'Electrolyte disorders alter repolarization.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-intervals',
        'Left axis deviation on ECG may be associated with:',
        'Left anterior fascicular block or LV hypertrophy patterns',
        [
            'Right arm lead reversal only always',
            'Normal finding in every adult',
            'Asystole'
        ],
        'Axis is calculated from limb leads.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-intervals',
        'Right bundle branch block shows:',
        'Wide QRS with RSR prime pattern in V1 and slurred S in lateral leads',
        [
            'Narrow QRS with short PR only',
            'Sawtooth flutter waves',
            'No QRS complexes'
        ],
        'RBBB widens terminal ventricular forces.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-intervals',
        'Long QT increases risk of:',
        'Torsades de pointes and sudden arrhythmia',
        [
            'Bradycardia only always',
            'Improved exercise capacity',
            'Shorter PR always'
        ],
        'QT prolongation can be congenital or acquired.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-intervals',
        'Low voltage QRS in limb leads may suggest:',
        'Pericardial effusion, obesity, or COPD among other causes',
        [
            'Always hyperkalemia',
            'Always normal variant only',
            'Lead reversal only'
        ],
        'Voltage criteria aid differential diagnosis.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-artifacts',
        'Loose electrode contact often causes:',
        'Baseline wander and intermittent signal loss',
        [
            'Sharp ST elevation in all leads always',
            'Perfectly stable tracing',
            'Fixed bradycardia on monitor'
        ],
        'Secure electrodes reduce wander.',
        [
            S.NHA_CET
        ],
        'beginner',
    ),
    fact(
        'ekg-artifacts',
        'Patient movement during ECG acquisition can mimic:',
        'Arrhythmia or ischemia on the tracing',
        [
            'Only normal sinus rhythm',
            'Only asystole',
            'Only paced rhythm'
        ],
        'Repeat tracing after patient rests.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-artifacts',
        'Electrical interference from nearby equipment may be reduced by:',
        'Proper grounding, cable routing, and filtering per device manual',
        [
            'Increasing patient muscle tension',
            'Removing ground electrode',
            'Wetting electrodes with saline pools'
        ],
        'Shielding and technique reduce noise.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-artifacts',
        'Swapping RA and LA electrodes primarily affects:',
        'Limb lead polarity and calculated axis',
        [
            'Only chest leads',
            'Only paper speed',
            'Only printer ink'
        ],
        'Reversal changes QRS direction in affected leads.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-artifacts',
        'Paced rhythm artifact spikes should be:',
        'Noted on the report so they are not mistaken for QRS',
        [
            'Erased from medical record',
            'Interpreted as VF automatically',
            'Ignored when rate is normal'
        ],
        'Spikes precede or follow paced beats.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-artifacts',
        'Sweat during stress ECG increases risk of:',
        'Sliding electrodes and motion artifact',
        [
            'Perfect adhesion',
            'Automatic diagnosis of STEMI',
            'No need for skin prep'
        ],
        'Dry secure leads improve quality.',
        [
            S.NHA_CET
        ],
        'beginner',
    ),
    fact(
        'ekg-artifacts',
        'If ECG shows unexpected extreme tachycardia with unchanged patient status, first consider:',
        'Technical artifact or lead misplacement',
        [
            'Immediate discharge',
            'Ignoring tracing',
            'Assuming VT without pulse check'
        ],
        'Clinical assessment confirms rhythm.',
        [
            S.NHA_CET,
        S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'intermediate',
    ),
    fact(
        'ekg-artifacts',
        'Filtering settings on monitor (diagnostic vs monitor mode) can:',
        'Change apparent ST segment appearance',
        [
            'Eliminate need for 12-lead',
            'Replace provider interpretation',
            'Guarantee normal QT always'
        ],
        'Use diagnostic mode for ST analysis when indicated.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-cardiac-ap',
        'The bundle of His conducts impulses to:',
        'Right and left bundle branches',
        [
            'SA node only',
            'Pulmonary veins',
            'Coronary sinus only'
        ],
        'His bundle links AV node to ventricular conduction system.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-cardiac-ap',
        'Coronary artery supplying most of the left ventricle in right-dominant circulation often is:',
        'Left anterior descending and circumflex branches of left coronary artery',
        [
            'Posterior descending only from right always in everyone',
            'Pulmonary artery',
            'Superior vena cava'
        ],
        'Dominance affects which artery supplies PDA.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-cardiac-ap',
        'Repolarization abnormalities on ECG reflect:',
        'Ventricular recovery phase on the T wave and ST segment',
        [
            'Atrial depolarization only',
            'SA node automaticity only',
            'Pericardial friction rub sound'
        ],
        'ST-T changes map to repolarization.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-cardiac-ap',
        'Increased automaticity of a ventricular focus may produce:',
        'Accelerated idioventricular or escape rhythms',
        [
            'Normal sinus rhythm only',
            'Atrial flutter only',
            'No QRS complexes'
        ],
        'Ectopic pacemakers can take over.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-cardiac-ap',
        'The PR segment represents:',
        'Slow conduction through the AV node',
        [
            'Ventricular repolarization',
            'Atrial repolarization usually hidden',
            'QRS duration'
        ],
        'AV nodal delay creates PR interval.',
        [
            S.NHA_CET
        ],
        'intermediate',
    ),
    fact(
        'ekg-cardiac-ap',
        'Ischemia in the inferior wall may show changes in leads:',
        'II, III, and aVF',
        [
            'V1 and V2 only',
            'I and aVL only',
            'V7 through V9 only'
        ],
        'Lead groups reflect myocardial territories.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-cardiac-ap',
        'Pericarditis may cause:',
        'Diffuse ST elevation and PR depression in multiple leads',
        [
            'ST elevation in one territory only always',
            'Asystole always',
            'Only U waves'
        ],
        'Inflammation affects widespread repolarization.',
        [
            S.NHA_CET
        ],
        'advanced',
    ),
    fact(
        'ekg-cardiac-ap',
        'Hyperacute T waves in acute coronary syndrome:',
        'May precede ST elevation on ECG',
        [
            'Only occur in electrolyte disorders',
            'Mean normal variant always',
            'Exclude MI diagnosis'
        ],
        'Early ischemia can alter T wave morphology.',
        [
            S.NHA_CET,
        S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-acls-basics',
        'For adult cardiac arrest with shockable rhythm, defibrillation should be:',
        'Performed as soon as device and pads are ready with minimal pause in compressions',
        [
            'Delayed until 10 minutes of CPR only',
            'Never repeated if first shock fails',
            'Replaced by pulse checks every 30 seconds without CPR'
        ],
        'Early shock improves survival in VF/pVT.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'intermediate',
    ),
    fact(
        'ekg-acls-basics',
        'Amiodarone 300 mg IV/IO first dose in VF/pVT refractory to shock is given:',
        'Once as first antiarrhythmic dose per ACLS algorithm',
        [
            'Every 30 seconds indefinitely',
            'Only for asystole',
            'Orally during arrest'
        ],
        'Antiarrhythmics follow CPR and defibrillation.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-acls-basics',
        'Lidocaine may be considered in ACLS as:',
        'Alternative antiarrhythmic for refractory VF/pVT when amiodarone unavailable',
        [
            'First-line for sinus bradycardia',
            'Replacement for CPR',
            'Treatment for stable narrow complex SVT always'
        ],
        'Medication choice follows local protocol.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-acls-basics',
        'Atropine is no longer recommended for:',
        'Routine use in pulseless electrical activity or asystole in ACLS',
        [
            'All bradycardia with pulses',
            'Sinus tachycardia',
            'VF/pVT first line'
        ],
        'ACLS removed routine atropine for PEA/asystole.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-acls-basics',
        'Sodium bicarbonate during CPR may be considered for:',
        'Known hyperkalemia or preexisting metabolic acidosis per ACLS',
        [
            'All arrests regardless of cause',
            'Routine first medication',
            'Hypokalemia only'
        ],
        'Bicarbonate is not routine for all arrests.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-acls-basics',
        'Calcium chloride in arrest is indicated for:',
        'Hyperkalemia, hypocalcemia, or calcium channel blocker overdose per ACLS',
        [
            'All VF arrests first line',
            'Routine use every 3 minutes',
            'Asystole without electrolyte issue'
        ],
        'Calcium is not routine for all rhythms.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-acls-basics',
        'Tension pneumothorax as a reversible cause of arrest may be treated with:',
        'Needle decompression or chest tube per training and protocol',
        [
            'Defibrillation first always',
            'Only epinephrine',
            'Observation without CPR'
        ],
        'T is among reversible causes (Hs and Ts).',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'ekg-acls-basics',
        'Post-ROSC blood pressure support targets:',
        'Mean arterial pressure sufficient for organ perfusion per protocol',
        [
            'Hypotension indefinitely',
            'No monitoring',
            'Only diastolic below 20 always'
        ],
        'Hemodynamic support follows ROSC.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'phleb-order-draw',
        'When both blood culture and coagulation tubes are ordered, blood culture bottles are generally filled:',
        'Before tubes with additives that could contaminate cultures if drawn first into culture',
        [
            'After lavender EDTA tube always without exception',
            'Last after all additive tubes',
            'Only from IV catheter without policy'
        ],
        'Order of draw prevents additive carryover; follow CLSI and lab policy.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-order-draw',
        'If only a light-blue citrate tube is ordered, some policies allow:',
        'Drawing a discard tube first when using a butterfly to fill coagulation tube properly',
        [
            'Skipping patient identification',
            'Drawing without tourniquet always',
            'Pooling tubes from two patients'
        ],
        'Discard tube clears air/dead space in tubing.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-order-draw',
        'Royal blue trace-element tubes are used when:',
        'Testing requires minimal contamination from additives or metals',
        [
            'Routine CBC only',
            'Every STAT chemistry',
            'Urine pregnancy only'
        ],
        'Special metal-free tubes protect trace assays.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-order-draw',
        'Yellow-top ACD tubes may be used for:',
        'Blood bank cellular therapy or HLA testing per lab manual',
        [
            'Routine PT/INR',
            'Serum glucose',
            'Stool ova'
        ],
        'Tube color indicates specialized additive.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-order-draw',
        'When drawing ordered tubes from a syringe transfer device:',
        'Follow manufacturer and CLSI guidance to prevent hemolysis and clotting',
        [
            'Shake violently for 2 minutes',
            'Leave needle uncapped on counter',
            'Mix patients samples to save time'
        ],
        'Transfer technique affects sample quality.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-order-draw',
        'Capillary collection order when multiple tests ordered should:',
        'Follow laboratory-defined sequence for additive cards or tubes',
        [
            'Ignore test requirements',
            'Use same lancet for two patients',
            'Skip labeling until next day'
        ],
        'Order prevents erroneous results on small volumes.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-order-draw',
        'If a tube is underfilled for coagulation testing:',
        'Recollect per lab rejection policy because results may be invalid',
        [
            'Report PT anyway without note',
            'Add saline to fill line',
            'Heat tube to clot faster'
        ],
        'Citrate ratio depends on proper fill.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-order-draw',
        'Pediatric microcollection containers require:',
        'Minimum fill volumes documented on container for each test',
        [
            'Overfilling until spillage',
            'No mixing of additives',
            'Sharing lancet between siblings'
        ],
        'Volume requirements differ from adult tubes.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-additives',
        'SPS (sodium polyanetholesulfonate) in yellow-black blood culture bottles:',
        'Anticoagulates and may inhibit complement to aid organism recovery',
        [
            'Clots sample for chemistry',
            'Is the same as EDTA',
            'Replaces fluoride for glucose'
        ],
        'Culture media additives support microbiology.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-additives',
        'Lithium heparin compared to sodium heparin:',
        'May be used in plasma separator tubes depending on manufacturer',
        [
            'Is identical to citrate for PT',
            'Is used for blood bank crossmatch only',
            'Replaces EDTA in lavender'
        ],
        'Heparin type varies by tube brand.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-additives',
        'Gel separator in serum tubes:',
        'Forms barrier between cells and serum during centrifugation',
        [
            'Anticoagulates for CBC',
            'Is the same as oxalate',
            'Prevents all clotting before spin'
        ],
        'Gel aids chemistry on serum.',
        [
            S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-additives',
        'Citrate tubes for coagulation must be filled to:',
        'The manufacturer fill line to maintain 9:1 blood to anticoagulant ratio',
        [
            'One quarter full always',
            'Any volume',
            'Overflowing past stopper'
        ],
        'Incorrect ratio invalidates PT/aPTT.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-additives',
        'EDTA is inappropriate for:',
        'Potassium and calcium measurements that require serum or heparin plasma',
        [
            'CBC and differential',
            'Hemoglobin on some analyzers',
            'Reticulocyte count'
        ],
        'EDTA chelates calcium and affects some analytes.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-additives',
        'Fluoride in gray-top tubes inhibits:',
        'Enolase to slow glycolysis in glucose specimens',
        [
            'All bacterial growth in cultures',
            'Clotting in blue tops',
            'Hemolysis always'
        ],
        'Fluoride preserves glucose for lab measurement.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-additives',
        'Thrombin additive red-top rapid clot tubes are used to:',
        'Accelerate clotting for rapid serum separation when indicated',
        [
            'Run blood gases',
            'Perform crossmatch',
            'Collect EDTA plasma'
        ],
        'Clot activators speed serum formation.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-additives',
        'Plasma preparation tube (PPT) may contain:',
        'Heparin and gel for plasma chemistry after centrifugation',
        [
            'Citrate for PT only',
            'No anticoagulant',
            'Culture medium'
        ],
        'PPT yields plasma similar to green-top protocols.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-site',
        'The basilic vein is often:',
        'Larger but closer to artery and nerve, requiring careful anchoring',
        [
            'Located on the dorsum of foot only',
            'Always contraindicated',
            'The same as radial artery'
        ],
        'Basilic access needs skilled technique.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-site',
        'Hand veins for venipuncture are used when:',
        'Antecubital veins are unavailable and policy allows distal draws',
        [
            'Always preferred over antecubital',
            'Patient is mastectomy with lymphedema on that side',
            'IV fluids run in same arm without restriction'
        ],
        'Distal sites may be more painful and have higher complication rates.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-site',
        'Applying a warm compress proximal to the venipuncture site may:',
        'Dilate veins for difficult access when ordered',
        [
            'Replace skin antisepsis',
            'Eliminate need for tourniquet always',
            'Cause arterial puncture intentionally'
        ],
        'Heat can aid venodilation.',
        [
            S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-site',
        'Palpating the vein before antisepsis helps:',
        'Confirm location and direction without contaminating prep site afterward',
        [
            'Skip tourniquet always',
            'Use same gloved hand on floor then vein',
            'Ignore patient pain'
        ],
        'Assessment precedes skin antisepsis.',
        [
            S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-site',
        'Drawing from an arm with fistula or graft:',
        'Is contraindicated on that vascular access arm',
        [
            'Is preferred site',
            'Requires only alcohol wipe',
            'Replaces dialysis session'
        ],
        'Protect vascular access for dialysis.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-site',
        'Butterfly needle gauge selection balances:',
        'Vein size and required sample volume with minimizing hemolysis',
        [
            'Always largest gauge possible',
            'Smallest gauge that cannot yield volume',
            'Random choice'
        ],
        'Gauge affects flow and trauma.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-site',
        'Two-attempt policy in many labs means:',
        'After two unsuccessful attempts, seek alternative collector per policy',
        [
            'Unlimited attempts in same vein',
            'Never call for help',
            'Switch patients to practice'
        ],
        'Limits patient trauma and complications.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-site',
        'Patient arm position during venipuncture should:',
        'Extend arm downward when possible to engorge veins',
        [
            'Be hyperflexed tightly',
            'Be above head always',
            'Include tight fist pump for entire draw without release'
        ],
        'Proper position aids venous filling.',
        [
            S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-handling',
        'Specimens for ammonia testing often require:',
        'Immediate chilling and rapid transport on ice per lab manual',
        [
            'Room temperature storage overnight',
            'Freezing without protocol',
            'Exposure to sunlight'
        ],
        'Ammonia is unstable at room temperature.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-handling',
        'Lactate specimens require:',
        'Proper collection tube and prompt processing per lab requirements',
        [
            'Heparinized syringe left on counter hours',
            'Serum separator left unspun days',
            'No labeling'
        ],
        'Delays falsely lower lactate.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-handling',
        'Arterial blood gas samples need:',
        'Immediate mixing, ice if required, and analysis within lab stability limits',
        [
            'Gentle rolling of clotted serum tube',
            'Storage in vaccine refrigerator',
            'Exposure to air without capping'
        ],
        'ABG handling preserves pO2 and pCO2.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-handling',
        'Chain of custody specimens require:',
        'Documented transfer of custody with sealed containers',
        [
            'Open transport in backpack',
            'Shared labels between patients',
            'Delayed logging'
        ],
        'Forensic or legal samples need traceability.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-handling',
        'If a tube breaks in the centrifuge, the collector should:',
        'Stop machine, use PPE, and follow biohazard spill protocol',
        [
            'Reach in while spinning',
            'Wipe with bare hands',
            'Ignore shards'
        ],
        'Broken glass and aerosols are hazardous.',
        [
            S.OSHA_BBP,
        S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-handling',
        'Pneumatic tube system transport of specimens requires:',
        'Padding, upright containers, and lab approval for fragile tests',
        [
            'Uncapped tubes in carrier',
            'Mixing hematology with food',
            'No leak-proof bags'
        ],
        'Transport systems can hemolyze samples.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-handling',
        'Labeling tubes at bedside immediately after draw:',
        'Reduces misidentification risk',
        [
            'Can wait until end of shift',
            'Is optional for STAT',
            'Should use pre-labeled tubes for wrong patient'
        ],
        'Bedside labeling is best practice.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-handling',
        'Room temperature hold time for serum potassium before spin should:',
        'Follow lab manual because delays and cellular leakage affect results',
        [
            'Be unlimited',
            'Include vigorous fist pumping only',
            'Require freezing all CBC tubes'
        ],
        'Processing time affects electrolytes.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-complications',
        'Extravasation of vesicant IV medication during blood draw from IV site requires:',
        'Stopping procedure and notifying nurse/provider immediately',
        [
            'Continuing draw faster',
            'Applying heat only',
            'Ignoring swelling'
        ],
        'Vesicants can cause tissue necrosis.',
        [
            S.NHA_CPT,
        S.CLSI_GP41,
        S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-complications',
        'Petechiae above tourniquet may indicate:',
        'Prolonged or excessive tourniquet pressure',
        [
            'Successful draw only',
            'Hyperglycemia',
            'Normal finding always'
        ],
        'Capillary rupture causes petechiae.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-complications',
        'A sclerosed or thrombosed vein on palpation is:',
        'Hard, cord-like, and non-compressible',
        [
            'Bouncy and full always',
            'Pulsatile like artery always',
            'Absent on both arms always'
        ],
        'Do not use thrombosed veins.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-complications',
        'Bilirubin falsely elevated may result from:',
        'Hemolysis during difficult draw',
        [
            'Perfect gentle technique',
            'Proper fill of EDTA',
            'Timely transport on ice'
        ],
        'Hemolysis releases intracellular contents.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-complications',
        'Infection at venipuncture site presents with:',
        'Erythema, warmth, pain, or purulent drainage',
        [
            'No symptoms ever',
            'Improved vein always',
            'Lower glucose only'
        ],
        'Cellulitis requires medical evaluation.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-complications',
        'Delayed faint after leaving draw chair is managed by:',
        'Assisting patient supine, monitoring vitals, and documenting event',
        [
            'Letting patient drive immediately',
            'Ignoring if patient insists',
            'Giving stimulant without assessment'
        ],
        'Late vasovagal reactions occur.',
        [
            S.NHA_CPT,
        S.CLSI_GP41,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'phleb-complications',
        'Repeated venipuncture at same site increases risk of:',
        'Sclerosis and patient discomfort',
        [
            'Stronger veins always',
            'Lower potassium always',
            'No complications'
        ],
        'Rotate sites when possible.',
        [
            S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-complications',
        'Prolonged pressure after arterial nick may require:',
        'Extended holding and provider evaluation',
        [
            'No pressure',
            'Ice only without pressure',
            'Immediate strenuous exercise'
        ],
        'Arterial bleeding needs control.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-safety',
        'Safety-engineered phlebotomy devices must be:',
        'Activated immediately after use per OSHA and facility policy',
        [
            'Left unactivated for reuse',
            'Recapped by hand when safety fails',
            'Passed to another patient'
        ],
        'Engineered sharps injury protection is required when feasible.',
        [
            S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'phleb-safety',
        'Hand hygiene after glove removal is needed because:',
        'Gloves may have microtears and hands may be contaminated',
        [
            'Gloves sterilize hands',
            'Only before gloves never after',
            'Alcohol gel is banned'
        ],
        'Hand hygiene is final step.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.OSHA_BBP
        ],
        'beginner',
    ),
    fact(
        'phleb-safety',
        'Transporting sharps containers requires:',
        'Closed, upright, and not overfilled containers',
        [
            'Open tops in cart',
            'Shaking to compact waste',
            'Placing in passenger seat unsecured'
        ],
        'Overfilled containers increase stick risk.',
        [
            S.OSHA_BBP
        ],
        'beginner',
    ),
    fact(
        'phleb-safety',
        'Patient-owned anticoagulant use increases risk of:',
        'Bleeding and bruising at venipuncture site',
        [
            'No bleeding ever',
            'Automatic hemolysis',
            'Higher sodium'
        ],
        'Anticoagulants prolong hemostasis.',
        [
            S.CLSI_GP41,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-safety',
        'Drawing blood in isolation room requires:',
        'Following isolation PPE and room exit procedures',
        [
            'Skipping PPE if busy',
            'Leaving used tubes in hallway',
            'Removing PPE in patient room incorrectly'
        ],
        'Isolation protects staff and others.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'phleb-safety',
        'Needlestick with source patient unknown HIV status should prompt:',
        'Immediate wound care and occupational health evaluation per protocol',
        [
            'Ignoring if needle looked clean',
            'Waiting one week',
            'No documentation'
        ],
        'PEP may be time-sensitive.',
        [
            S.OSHA_NEEDLESTICK,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'phleb-safety',
        'Chemical disinfection of tourniquets between patients:',
        'Follow facility policy; many use disposable or cleanable barriers',
        [
            'Never clean shared tourniquet',
            'Share without cleaning always',
            'Soak in bleach while on patient arm'
        ],
        'Tourniquets can harbor organisms.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'intermediate',
    ),
    fact(
        'phleb-safety',
        'Unattended patient in draw chair should:',
        'Never occur; patient remains observed during and immediately after draw',
        [
            'Be left alone if eyes closed',
            'Be sent to parking lot alone if dizzy',
            'Be restrained without order'
        ],
        'Observation prevents injury from syncope.',
        [
            S.NHA_CPT,
        S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-who',
        'WHO injection safety emphasizes:',
        'One sterile syringe and needle per procedure per patient',
        [
            'Reusing syringe if needle changed',
            'Sharing multi-dose vials without policy',
            'No hand hygiene'
        ],
        'Reuse transmits bloodborne pathogens.',
        [
            S.WHO_INJECTION_SAFETY
        ],
        'beginner',
    ),
    fact(
        'phleb-who',
        'WHO global health workforce safety includes:',
        'Hepatitis B vaccination for at-risk workers',
        [
            'Discouraging vaccination',
            'Hiding needlestick data',
            'Reusing gloves all week'
        ],
        'Vaccination prevents occupationally acquired HBV.',
        [
            S.WHO_INJECTION_SAFETY,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'phleb-who',
        'WHO clean care focus in phlebotomy aligns with:',
        'Hand hygiene before patient contact and aseptic skin preparation',
        [
            'Blowing on skin to dry',
            'Skipping antisepsis',
            'Drawing through clothing'
        ],
        'Skin antisepsis reduces contamination.',
        [
            S.WHO_INJECTION_SAFETY,
        S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'beginner',
    ),
    fact(
        'phleb-who',
        'WHO patient safety curriculum teaches:',
        'Open disclosure and learning from errors',
        [
            'Blame culture only',
            'Hiding near misses',
            'No reporting systems'
        ],
        'Learning systems reduce harm.',
        [
            S.WHO_INJECTION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'phleb-who',
        'WHO standards for health facilities include:',
        'Safe waste management for sharps and blood-contaminated materials',
        [
            'Discarding sharps in regular trash',
            'Open bins in waiting room',
            'Burning plastic in patient room'
        ],
        'Segregated waste prevents community exposure.',
        [
            S.WHO_INJECTION_SAFETY,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'phleb-who',
        'WHO recommends competency verification for phlebotomists:',
        'Before independent practice and periodically thereafter',
        [
            'Never after hire',
            'Only self-attestation without observation',
            'Only for physicians'
        ],
        'Competency assessment ensures skill.',
        [
            S.WHO_INJECTION_SAFETY,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'phleb-who',
        'WHO advocacy for single-use devices supports:',
        'Eliminating needle reuse in low-resource settings',
        [
            'Boiling needles between patients',
            'Sharing lancets in clinic',
            'No sterilizer needed ever'
        ],
        'Single-use prevents outbreaks.',
        [
            S.WHO_INJECTION_SAFETY
        ],
        'advanced',
    ),
    fact(
        'phleb-who',
        'WHO surgical site infection prevention parallels phlebotomy by stressing:',
        'Alcohol-based hand rub when hands not visibly soiled',
        [
            'Skipping hand hygiene if gloves worn',
            'Using water only without soap ever',
            'Shared towels unwashed'
        ],
        'Hand hygiene is foundational.',
        [
            S.WHO_INJECTION_SAFETY,
        S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'beginner',
    ),
    fact(
        'phleb-glucose',
        'Capillary glucose testing site rotation prevents:',
        'Callus formation and inaccurate readings',
        [
            'Need for hand hygiene',
            'Calibration checks',
            'Quality control'
        ],
        'Rotate fingertip sites per manufacturer.',
        [
            S.FDA_CLIA_WAIVED,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'beginner',
    ),
    fact(
        'phleb-glucose',
        'Control solution for glucometer checks:',
        'Verifies meter and strip function when used as directed',
        [
            'Replaces patient blood always',
            'Is optional forever',
            'Is same as alcohol pad'
        ],
        'QC logs document control results.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'intermediate',
    ),
    fact(
        'phleb-glucose',
        'Hypoglycemia on POC meter reading below 70 mg/dL should prompt:',
        '15 g fast-acting carbohydrate and recheck per protocol if symptomatic or per ADA',
        [
            'Nothing if patient feels fine always',
            'High-fat meal only',
            'Exercise immediately'
        ],
        'Rule of 15 guides treatment.',
        [
            S.ADA_STANDARDS,
        S.CDC_DIABETES,
        S.FDA_CLIA_WAIVED
        ],
        'intermediate',
    ),
    fact(
        'phleb-glucose',
        'Hematocrit extremes can affect:',
        'Accuracy of some glucose meters',
        [
            'Only urine dipsticks',
            'Blood pressure cuff size only',
            'Thermometer calibration'
        ],
        'Anemia or polycythemia may skew POC glucose.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'advanced',
    ),
    fact(
        'phleb-glucose',
        'Glucose meter strips must be stored:',
        'In original container with lid closed away from moisture and heat',
        [
            'Open on windowsill',
            'Mixed with used strips',
            'In freezer always'
        ],
        'Environmental damage invalidates strips.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'beginner',
    ),
    fact(
        'phleb-glucose',
        'Fingerstick before dinner for diabetic patient on insulin should:',
        'Guide mealtime dose only per provider orders and institutional policy',
        [
            'Replace provider entirely',
            'Be ignored if patient busy',
            'Use expired strips without check'
        ],
        'POC glucose informs insulin timing per plan.',
        [
            S.ADA_STANDARDS,
        S.NHA_CCMA,
        S.FDA_CLIA_WAIVED
        ],
        'intermediate',
    ),
    fact(
        'phleb-glucose',
        'Venous plasma glucose generally runs:',
        'Slightly higher than simultaneous capillary glucose in hyperglycemic states',
        [
            'Always identical to capillary',
            'Always 100 mg/dL lower',
            'Unrelated to sample type'
        ],
        'Sample type and perfusion affect comparison.',
        [
            S.CDC_DIABETES,
        S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'phleb-glucose',
        'When POC glucose does not match lab, first steps include:',
        'Repeat test with new strip, verify hematocrit limits, and compare timing',
        [
            'Discard meter without investigation',
            'Change patient diagnosis alone',
            'Ignore discrepancy'
        ],
        'Troubleshooting follows manufacturer and lab policy.',
        [
            S.FDA_CLIA_WAIVED,
        S.NHA_CPT,
        S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'cpr-adult',
        'Adult chest compression depth should be at least:',
        '2 inches (5 cm) without exceeding 2.4 inches (6 cm)',
        [
            '1 inch (2 cm) only',
            '4 inches (10 cm) always',
            'Shallow compressions of 0.5 inch'
        ],
        'AHA recommends adequate depth for perfusion.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'intermediate',
    ),
    fact(
        'cpr-adult',
        'Adult compression rate should be:',
        '100 to 120 compressions per minute',
        [
            '60 per minute',
            '200 per minute',
            '30 per minute'
        ],
        'Rate window optimizes cardiac output.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'beginner',
    ),
    fact(
        'cpr-adult',
        'When giving breaths during adult BLS without advanced airway, each breath should:',
        'Produce visible chest rise over about 1 second',
        [
            'Be forceful enough to hear stomach gurgle only',
            'Last 5 seconds each',
            'Never pause compressions more than 10 seconds for all breaths'
        ],
        'Minimize interruption while ventilating.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'intermediate',
    ),
    fact(
        'cpr-adult',
        'If an adult chokes and becomes unresponsive during abdominal thrusts, the rescuer should:',
        'Lower patient safely and begin CPR starting with compressions',
        [
            'Continue abdominal thrusts only forever',
            'Leave patient standing',
            'Wait for pulse only without CPR'
        ],
        'Unresponsive choking victim needs CPR and look for object.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-adult',
        'Pulse check in adult BLS should take no more than:',
        '10 seconds before starting or resuming compressions if no definite pulse',
        [
            '60 seconds',
            '2 minutes',
            '30 seconds routinely between every compression'
        ],
        'Delays reduce survival.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'intermediate',
    ),
    fact(
        'cpr-adult',
        'CPR on a pregnant woman in late pregnancy may require:',
        'Manual left uterine displacement during compressions when possible',
        [
            'No modifications ever',
            'Supine flat without relief always',
            'Delay CPR until delivery'
        ],
        'Displacement improves venous return.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'cpr-adult',
        'Opioid-associated unresponsive patient with no breathing may need:',
        'CPR and naloxone per local protocol while activating emergency response',
        [
            'Only naloxone without CPR if pulseless',
            'Waiting for urine test',
            'No 911 call'
        ],
        'Treat life-threatening respiratory arrest.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR,
        S.RED_CROSS_FIRST_AID
        ],
        'advanced',
    ),
    fact(
        'cpr-adult',
        'Team CPR with feedback device uses:',
        'Real-time compression depth and rate monitoring when available',
        [
            'Slower compressions intentionally',
            'No role rotation',
            'Ignoring device prompts always'
        ],
        'Feedback improves compression quality.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'intermediate',
    ),
    fact(
        'cpr-child',
        'A child for BLS is generally defined as:',
        'Puberty not yet reached per AHA (about 1 year until puberty signs)',
        [
            'Newborn only',
            'Anyone over 65',
            'Only teenagers'
        ],
        'Age definitions guide compression technique.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-child',
        'Single rescuer child CPR compression-to-ventilation ratio is:',
        '30:2',
        [
            '15:2 always for one rescuer',
            '5:1',
            'Continuous breaths without compressions'
        ],
        'AHA uses 30:2 for single rescuer child.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-child',
        'Two-rescuer child CPR compression-to-ventilation ratio is:',
        '15:2',
        [
            '30:2',
            '5:1',
            'No ventilations'
        ],
        'Two rescuers may use 15:2 for children.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-child',
        'Child chest compressions may be given with:',
        'One or two hands depending on child size and rescuer strength',
        [
            'Two fingers only always',
            'Foot pressure',
            'No compressions if child small'
        ],
        'Hand placement ensures adequate depth.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-child',
        'AED with pediatric attenuator pads on a child should:',
        'Follow manufacturer age and weight instructions for energy dosing',
        [
            'Use adult dose always without pads',
            'Never be used under 18',
            'Replace CPR entirely'
        ],
        'Pediatric pads reduce delivered energy.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-child',
        'Foreign body airway obstruction in responsive child includes:',
        'Back blows and chest thrusts for infant or abdominal thrusts for child per algorithm',
        [
            'Blind finger sweeps in mouth always first',
            'Ignoring cough',
            'Only Heimlich on infant under 1 year'
        ],
        'Algorithm differs by age.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-child',
        'Bradycardia with poor perfusion in a child may require:',
        'CPR if heart rate remains below 60 with poor perfusion despite oxygenation',
        [
            'Only atropine without assessment',
            'Waiting until asystole',
            'No intervention'
        ],
        'Poor perfusion bradycardia is treated aggressively.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'advanced',
    ),
    fact(
        'cpr-child',
        'Rescue breathing for child with pulse but inadequate breathing rate is:',
        '1 breath every 2 to 3 seconds (20 to 30/min)',
        [
            '1 breath every 10 seconds only',
            'No breaths ever',
            'Only compressions'
        ],
        'Rescue breathing supports respiratory arrest with pulse.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'advanced',
    ),
    fact(
        'cpr-infant',
        'Infant BLS compressions are performed with:',
        'Two fingers or two thumbs encircling hands on lower half of sternum',
        [
            'Heel of one hand only always',
            'Two hands overlapping adult style only',
            'No sternum contact'
        ],
        'Infant technique differs from adult.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-infant',
        'Recommended infant chest compression depth during BLS is approximately:',
        '1.5 inches (4 cm)',
        [
            '0.5 inch always',
            '3 inches (8 cm)',
            'Until ribs crack audibly'
        ],
        'One third anterior-posterior diameter of chest.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-infant',
        'Infant choking relief for responsive infant includes:',
        '5 back blows and 5 chest thrusts alternating',
        [
            'Abdominal thrusts only',
            'Finger sweep blindly always first',
            'Ignoring mild cough'
        ],
        'Back blows and chest thrusts clear airway in infants.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-infant',
        'Infant CPR ventilation should:',
        'Cover mouth and nose with rescuer mouth or use bag-mask without excessive volume',
        [
            'Force large adult tidal volumes',
            'Ventilate only through nose pinching mouth shut hard',
            'Skip ventilations always'
        ],
        'Gentle breaths prevent gastric inflation.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-infant',
        'Two-thumb encircling technique for infant CPR is useful when:',
        'Two rescuers are present and provider prefers two hands around chest',
        [
            'Never appropriate',
            'Only for adults',
            'Only during choking'
        ],
        'Thumbs compress sternum with hands encircling chest.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'advanced',
    ),
    fact(
        'cpr-infant',
        'Infant pulse check location is:',
        'Brachial or femoral artery',
        [
            'Carotid only always',
            'Radial preferred over brachial always in infant',
            'Apical without touch'
        ],
        'Brachial pulse is accessible in infants.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-infant',
        'If infant is unresponsive and not breathing normally, rescuer should:',
        'Shout for help, begin CPR after brief pulse check, and get AED if available',
        [
            'Wait for parents only',
            'Shake vigorously as sole treatment',
            'Give water orally'
        ],
        'Early CPR and defibrillation when shockable rhythm.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-infant',
        'After successful foreign body removal in infant, if still unresponsive:',
        'Begin CPR if no normal breathing',
        [
            'Assume recovery without assessment',
            'Leave infant alone',
            'Only back blows continue'
        ],
        'Assess breathing and pulse after obstruction relieved.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-aed',
        'AED pads on a hairy chest may require:',
        'Shaving or pressing pads firmly per device instructions',
        [
            'Placing on clothing always',
            'Using only one pad',
            'Skipping AED'
        ],
        'Poor contact prevents analysis.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-aed',
        'AED should not be placed over:',
        'Medication patches; remove patch and wipe area when possible',
        [
            'Dry skin',
            'Sternum when directed by diagram',
            'Clean chest'
        ],
        'Patches may interfere with shock or burn.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-aed',
        'If AED advises shock, rescuers should:',
        'Clear others from patient before delivering shock',
        [
            'Touch patient during shock',
            'Continue compressions during shock analysis always',
            'Remove pads immediately'
        ],
        'Safety requires clear contact.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-aed',
        'AED prompts no shock advised means:',
        'Resume CPR immediately per device instructions',
        [
            'Stop all care',
            'Remove pads and leave',
            'Wait 10 minutes without CPR'
        ],
        'Non-shockable rhythms need CPR.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-aed',
        'Water on chest during AED use should be:',
        'Dried quickly before pad placement when possible',
        [
            'Ignored with powered AED in puddle without caution',
            'Used to improve conduction',
            'Sprayed on pads'
        ],
        'Moisture affects adhesion and safety.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-aed',
        'Monophasic versus biphasic AEDs differ in:',
        'Waveform and energy delivery per manufacturer',
        [
            'Need for CPR never',
            'Pad color only',
            'Patient age definition'
        ],
        'Follow device-specific instructions.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'advanced',
    ),
    fact(
        'cpr-aed',
        'AED use in rain outdoors should:',
        'Minimize rescuer and patient contact with standing water while using AED',
        [
            'Never use AED outdoors',
            'Place AED in puddle',
            'Remove all clothing and abandon CPR'
        ],
        'Balance shock safety with continued CPR.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-aed',
        'After AED shock delivery, rescuers should:',
        'Immediately resume CPR for 2 minutes or per device prompt before next rhythm check',
        [
            'Check pulse for 2 minutes without compressions',
            'Remove AED',
            'Give food by mouth'
        ],
        'Post-shock myocardium needs perfusion.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-choking',
        'Mild choking in responsive adult is managed by:',
        'Encouraging forceful cough while monitoring',
        [
            'Abdominal thrusts immediately',
            'Blind finger sweep',
            'CPR starting with compressions'
        ],
        'Effective cough may clear partial obstruction.',
        [
            S.RED_CROSS_FIRST_AID,
        S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-choking',
        'Severe choking sign in conscious adult is:',
        'Silent cough, inability to speak, or cyanosis',
        [
            'Strong audible cough only',
            'Able to drink water easily',
            'Normal voice'
        ],
        'Silent obstruction is emergency.',
        [
            S.RED_CROSS_FIRST_AID,
        S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-choking',
        'Pregnant or obese choking victim may receive:',
        'Chest thrusts instead of abdominal thrusts',
        [
            'No assistance',
            'Only back blows to abdomen',
            'Heimlich with fist above umbilicus always'
        ],
        'Chest thrusts reduce uterus injury risk.',
        [
            S.RED_CROSS_FIRST_AID,
        S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-choking',
        'Unconscious choking victim after thrusts requires:',
        'CPR and look in mouth for visible object before breaths',
        [
            'Finger sweep blindly always',
            'No CPR until object removed surgically in field',
            'Only back blows'
        ],
        'CPR may dislodge object; remove only if seen.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-choking',
        'Choking infant with ineffective cough gets:',
        'Alternating back blows and chest thrusts while supporting head',
        [
            'Abdominal thrusts',
            'Slapping face',
            'Ignoring until cyanotic'
        ],
        'Infant algorithm differs from adult.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-choking',
        'Once an obstructed airway is cleared, the patient should:',
        'Be evaluated medically because complications may occur',
        [
            'Drive home without assessment',
            'Eat large meal immediately',
            'Skip documentation'
        ],
        'Airway edema or injury may develop.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-choking',
        'Finger sweep in mouth of conscious choking victim is:',
        'Not recommended unless object is visible',
        [
            'Always first step',
            'Performed blindly deep in throat',
            'Replaces thrusts always'
        ],
        'Blind sweeps can push object deeper.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS,
        S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-choking',
        'Choking while alone may be managed by:',
        'Calling 911 and performing self-abdominal thrusts or leaning over chair back',
        [
            'Waiting silently',
            'Drinking large amount of water only',
            'Driving to hospital while choking'
        ],
        'Self-help maneuvers and EMS activation save lives.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-chain',
        'The opening link in the adult out-of-hospital chain of survival is:',
        'Recognition of cardiac arrest and activation of emergency response',
        [
            'Immediate surgery',
            'Long-term rehab only',
            'Cooling only'
        ],
        'Early recognition and 911 call start the chain.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-chain',
        'Early high-quality CPR is a chain link because it:',
        'Maintains blood flow to heart and brain until defibrillation or ROSC',
        [
            'Replaces all advanced care',
            'Eliminates need for AED',
            'Is optional if AED present'
        ],
        'CPR bridges time to definitive care.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-chain',
        'Rapid defibrillation improves survival primarily in:',
        'Shockable rhythms such as VF and pulseless VT',
        [
            'Asystole always',
            'Normal sinus rhythm',
            'Stable angina'
        ],
        'Defibrillation terminates VF/pVT.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-chain',
        'The advanced cardiovascular life support link in the chain of survival includes:',
        'Airway management, IV medications, and reversible cause treatment',
        [
            'Only paperwork',
            'Family notification only',
            'Discharge planning'
        ],
        'ALS builds on BLS.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-chain',
        'Integrated post-cardiac arrest care includes:',
        'Treating cause, supporting perfusion, and targeted temperature management when indicated',
        [
            'Immediate discharge',
            'No monitoring',
            'Withholding oxygen always'
        ],
        'Post-arrest care affects neurologic outcome.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'cpr-chain',
        'Community CPR training strengthens the chain by:',
        'Increasing bystander willingness and skill to start CPR',
        [
            'Reducing 911 calls',
            'Eliminating AEDs',
            'Discouraging compressions'
        ],
        'Bystander CPR doubles survival potential.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'beginner',
    ),
    fact(
        'cpr-chain',
        'Public access defibrillation programs place AEDs to:',
        'Reduce time to first shock in public settings',
        [
            'Replace EMS entirely',
            'Store office supplies',
            'Charge phones only'
        ],
        'AED availability shortens time to defibrillation.',
        [
            S.AHA_WHAT_IS_CPR,
        S.AHA_ADULT_BLS
        ],
        'intermediate',
    ),
    fact(
        'cpr-chain',
        'Recovery phase after cardiac arrest addresses:',
        'Physical, cognitive, and emotional needs of survivors and families',
        [
            'Only billing',
            'Ignoring depression',
            'No follow-up appointments'
        ],
        'Survivorship is part of modern chains.',
        [
            S.AHA_ADULT_BLS,
        S.AHA_HQ_CPR
        ],
        'advanced',
    ),
    fact(
        'cpr-red-cross',
        'Red Cross first aid for severe bleeding emphasizes:',
        'Direct pressure and elevation when possible plus tourniquet for life-threatening extremity bleeding when trained',
        [
            'Removing embedded objects always',
            'Waiting for clot without pressure',
            'Using dirty rags without gloves'
        ],
        'Control bleeding is priority.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-red-cross',
        'For suspected spine injury, movement should be:',
        'Minimized unless immediate danger requires relocation',
        [
            'Rapidly pulled to standing',
            'Twisted to test pain',
            'Ignored if patient talks'
        ],
        'Spinal motion may worsen cord injury.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-red-cross',
        'Heat exhaustion signs include:',
        'Heavy sweating, weakness, and cool clammy skin',
        [
            'Hot dry skin with altered mental status only always',
            'Bradycardia only always',
            'Pinpoint pupils only'
        ],
        'Heat exhaustion differs from heat stroke.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-red-cross',
        'Hypothermia rewarming in field may include:',
        'Removing wet clothing and insulating patient while monitoring breathing',
        [
            'Rubbing snow on skin vigorously',
            'Giving alcohol',
            'Delaying EMS'
        ],
        'Gentle rewarming and ABCs are key.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-red-cross',
        'Anaphylaxis may be treated with epinephrine auto-injector when:',
        'Prescribed and symptoms involve breathing or circulation',
        [
            'Mild rash only without other symptoms always',
            'Patient requests cosmetic effect',
            'Replacing CPR in arrest'
        ],
        'Epinephrine is first-line for anaphylaxis.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'advanced',
    ),
    fact(
        'cpr-red-cross',
        'Stroke recognition uses FAST: Face droop, Arm weakness, Speech difficulty, and:',
        'Time to call emergency services',
        [
            'Temperature',
            'Food intake',
            'Foot pain'
        ],
        'Time-sensitive treatment benefits stroke patients.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'beginner',
    ),
    fact(
        'cpr-red-cross',
        'During an active seizure, bystander first aid includes:',
        'Protecting head, clearing area, and timing the event',
        [
            'Putting objects in mouth',
            'Restraining violently',
            'Giving water during seizure'
        ],
        'Do not restrain; support after seizure ends.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'cpr-red-cross',
        'Poisoning call to Poison Control or 911 should include:',
        'Substance, amount, time, and patient weight or age',
        [
            'Only patient favorite food',
            'No details to save time',
            'Assuming water fixes all ingestions'
        ],
        'Accurate information guides treatment.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'skill-injection',
        'Intramuscular injection angle is typically:',
        '90 degrees to skin',
        [
            '15 degrees always',
            '45 degrees for all IM sites',
            'Parallel under skin only'
        ],
        'IM injections enter muscle belly.',
        [
            S.NHA_CCMA,
        S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'beginner',
    ),
    fact(
        'skill-injection',
        'Subcutaneous injection angle is commonly:',
        '45 to 90 degrees depending on tissue and needle length',
        [
            '180 degrees',
            'Into bone only',
            'Through hair without prep'
        ],
        'SC deposits into adipose tissue.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-injection',
        'Aspiration before IM injection is:',
        'Not recommended for vaccines per CDC; follow policy for other drugs',
        [
            'Required for all vaccines always',
            'Never discussed',
            'Replaces site rotation'
        ],
        'CDC vaccine administration guidance omits aspiration.',
        [
            S.CDC_VACCINE_ADMIN,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-injection',
        'Z-track technique for IM injection helps:',
        'Prevent medication tracking into subcutaneous tissue and leaking',
        [
            'Increase pain only',
            'Skip needle safety',
            'Inject into vein always'
        ],
        'Z-track seals depot in muscle.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'skill-injection',
        'Needlestick after injection requires:',
        'Do not recap; activate safety device and follow exposure protocol',
        [
            'Recap needle by hand',
            'Reuse syringe on next patient',
            'Hide incident'
        ],
        'OSHA prohibits unsafe recapping.',
        [
            S.OSHA_NEEDLESTICK,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-injection',
        'Rotating IM sites prevents:',
        'Lipohypertrophy and inconsistent absorption especially with insulin',
        [
            'Need for hand hygiene',
            'Vaccine storage',
            'Patient identification'
        ],
        'Scar tissue alters drug uptake.',
        [
            S.NHA_CCMA,
        S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-injection',
        'Drawing medication from ampule requires:',
        'Filtering needle change and correct break technique away from body',
        [
            'Squeezing ampule in palm toward face',
            'Sharing ampule among patients',
            'Leaving open ampule overnight'
        ],
        'Ampule glass risk and contamination prevention.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-injection',
        'Prefilled pen injector teaching includes:',
        'Do not share pens between patients even if needle changed',
        [
            'Share pen if family member',
            'Store in freezer always',
            'Skip demonstration'
        ],
        'Pens may backflow blood into cartridge.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-vitals',
        'Korotkoff phase V (disappearance of sounds) is used for:',
        'Diastolic blood pressure in most adults',
        [
            'Systolic only always',
            'Temperature measurement',
            'Respiratory rate'
        ],
        'Fifth phase marks diastolic in most patients.',
        [
            S.CDC_HBP,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-vitals',
        'Cuff bladder width should be about:',
        '40% of arm circumference',
        [
            '10% of arm',
            'Equal to entire arm length',
            'Same for all patients without sizing'
        ],
        'Proper cuff size prevents false readings.',
        [
            S.CDC_HBP,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-vitals',
        'Pulse oximetry reading may be unreliable with:',
        'Cold extremities, nail polish, or poor perfusion',
        [
            'Normal warm fingers always',
            'Room air only',
            'Patient talking'
        ],
        'Sensor contact and perfusion affect SpO2.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-vitals',
        'Apical pulse is counted for:',
        'One full minute especially in irregular rhythms or children',
        [
            '5 seconds multiplied always without note',
            'Only during exercise',
            'Never in clinic'
        ],
        'Full minute improves accuracy in arrhythmia.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-vitals',
        'For an accurate respiratory rate, the MA should count breaths:',
        'Without patient knowing when possible to avoid voluntary alteration',
        [
            'After telling patient to breathe fast',
            'Only during sleep always in clinic',
            'By guessing from color'
        ],
        'Unaware counting reflects true rate.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-vitals',
        'Tympanic temperature requires:',
        'Proper seal in ear canal per device instructions',
        [
            'Probe in mouth',
            'Shared probe without cover between patients',
            'Reading before equilibration if device requires'
        ],
        'Technique affects accuracy.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-vitals',
        'Automated BP devices need:',
        'Periodic validation against manual technique per policy',
        [
            'Never maintenance',
            'Only pediatric use',
            'Cuff on leg always'
        ],
        'Calibration drift causes errors.',
        [
            S.CDC_HBP,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-vitals',
        'Pain assessment scales should be:',
        'Appropriate to patient age and cognition (e.g., numeric, FACES)',
        [
            'Ignored in vital sign flowsheet',
            'Only 0 or 10 without questions',
            'Asked only once per lifetime'
        ],
        'Pain is fifth vital sign in many settings.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-infection',
        'Alcohol-based hand rub is preferred when:',
        'Hands are not visibly soiled',
        [
            'Hands covered in blood without washing after',
            'After C. difficile exposure without soap',
            'Instead of cleaning spill'
        ],
        'CDC prioritizes ABHR unless soiling.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'beginner',
    ),
    fact(
        'skill-infection',
        'After caring for patient with C. difficile, hands should be washed with:',
        'Soap and water because spores are not fully removed by alcohol alone',
        [
            'Alcohol rub only always',
            'No hand hygiene',
            'Perfume only'
        ],
        'Spores require mechanical removal.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'intermediate',
    ),
    fact(
        'skill-infection',
        'Sterile gloves are indicated when:',
        'Touching sterile fields or performing sterile procedures',
        [
            'Taking blood pressure on intact skin',
            'Answering phone',
            'Filing charts'
        ],
        'Sterility matches procedure risk.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-infection',
        'Cleaning high-touch surfaces in exam rooms between patients:',
        'Reduces environmental transmission',
        [
            'Is optional always',
            'Replaces hand hygiene',
            'Uses only air freshener'
        ],
        'Environment contributes to cross-transmission.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE
        ],
        'beginner',
    ),
    fact(
        'skill-infection',
        'Single-use disposable items should be:',
        'Discarded after one patient use',
        [
            'Sterilized at home',
            'Shared if looks clean',
            'Stored in pocket'
        ],
        'Disposables prevent cross-contamination.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.OSHA_BBP
        ],
        'beginner',
    ),
    fact(
        'skill-infection',
        'Respirator fit testing is required for:',
        'Employees using N95 or higher respirators per OSHA respiratory protection',
        [
            'All staff wearing surgical masks',
            'Patients only',
            'Never in outpatient'
        ],
        'Fit testing ensures seal.',
        [
            S.OSHA_BBP
        ],
        'advanced',
    ),
    fact(
        'skill-infection',
        'Biohazard waste includes:',
        'Items saturated with blood or OPIM',
        [
            'Plain office paper',
            'Empty water bottles unexposed',
            'Clean packaging'
        ],
        'Regulated medical waste rules apply.',
        [
            S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-infection',
        'Injection safety includes:',
        'Never entering a medication vial with a used syringe or needle',
        [
            'Sharing saline flush syringe',
            'Pooling leftover vaccine doses',
            'Reusing insulin pen needle on second patient without changing pen'
        ],
        'One & Only Campaign principles.',
        [
            S.CDC_INJECTION_SAFETY,
        S.WHO_INJECTION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-terminology',
        'In medical terminology, the prefix "hyper-" means:',
        'Excessive or above normal',
        [
            'Below normal',
            'Slow',
            'Pain'
        ],
        'Hyperglycemia is high blood glucose.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-terminology',
        'The suffix "-itis" in a disease name means:',
        'Inflammation',
        [
            'Tumor',
            'Surgical removal',
            'Study of'
        ],
        'Arthritis is joint inflammation.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-terminology',
        'The prefix "tachy-" means:',
        'Fast',
        [
            'Slow',
            'Large',
            'Small'
        ],
        'Tachycardia is rapid heart rate.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-terminology',
        'The combining form "cardi/o" relates to:',
        'Heart',
        [
            'Kidney',
            'Skin',
            'Bone'
        ],
        'Cardiology is study of heart.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-terminology',
        'A medical term ending in "-ectomy" means:',
        'Surgical removal',
        [
            'Inflammation',
            'Enlargement',
            'Pain'
        ],
        'Appendectomy removes appendix.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-terminology',
        'The prefix "hypo-" means:',
        'Deficient or below normal',
        [
            'Above normal',
            'Painful',
            'Enlarged'
        ],
        'Hypotension is low blood pressure.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-terminology',
        'The suffix "-ology" means:',
        'Study of',
        [
            'Surgical cut',
            'Blood condition',
            'Resembling'
        ],
        'Dermatology studies skin.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-terminology',
        'The prefix "poly-" means:',
        'Many',
        [
            'One',
            'None',
            'Half'
        ],
        'Polyuria is excessive urination.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-pharm-dosage',
        'A medication order for 500 mg PO BID means:',
        '500 milligrams by mouth twice daily',
        [
            '500 mg every bedtime only',
            '500 mg IV once',
            '5 mg twice daily'
        ],
        'Latin abbreviations are being replaced; verify unclear orders.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-pharm-dosage',
        'Converting 2.5 g to milligrams gives:',
        '2500 mg',
        [
            '25 mg',
            '250 mg',
            '0.25 mg'
        ],
        'Move decimal three places when converting g to mg.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-pharm-dosage',
        'Safe pediatric medication dosing requires:',
        'Accurate weight in kilograms and double-checking calculations',
        [
            'Guessing weight by appearance',
            'Using adult dose always',
            'Skipping allergy check'
        ],
        'Errors harm children disproportionately.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-pharm-dosage',
        'Units marked on an insulin syringe correspond to:',
        'U-100 insulin concentration unless otherwise labeled',
        [
            'Any insulin vial regardless of concentration',
            'Oral tablets',
            'IV fluids'
        ],
        'Concentration mismatch causes overdose.',
        [
            S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-pharm-dosage',
        'Dropping trailing zeros in dosage (e.g., 1.0 vs 1) helps:',
        'Prevent decimal errors',
        [
            'Speed billing only',
            'Eliminate need for pharmacist',
            'Hide allergies'
        ],
        'FDA advocates leading zeros and no trailing zeros.',
        [
            S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-pharm-dosage',
        'A suspension medication before dispensing should be:',
        'Shaken to distribute particles evenly when label instructs',
        [
            'Heated to boiling',
            'Diluted with water without order',
            'Split in half for two patients'
        ],
        'Uniform concentration ensures correct dose.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-pharm-dosage',
        'Topical medication strength 1% means:',
        '1 gram of drug per 100 grams of preparation',
        [
            '1 mg per liter only',
            '1% of bottle is water only',
            'No active drug'
        ],
        'Percent strength describes drug mass in total.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'skill-pharm-dosage',
        'Look-alike sound-alike (LASA) drug pairs require:',
        'Tall-man lettering and extra verification steps',
        [
            'Casual selection from shelf',
            'Assuming any blue pill is same drug',
            'Skipping label read'
        ],
        'LASA errors are high risk.',
        [
            S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-specimen-lab',
        'Collecting midstream clean-catch urine reduces:',
        'Contamination with periurethral flora',
        [
            'Need for label',
            'Patient privacy',
            'Hand hygiene'
        ],
        'Cleaning meatus and discarding first stream improves culture.',
        [
            S.CLSI_GP41,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-specimen-lab',
        'Stool occult blood testing cards require:',
        'Diet and medication restrictions per kit instructions',
        [
            'Eating rare red meat immediately before if forbidden',
            'Mixing samples from two patients',
            'Storing open card in sun'
        ],
        'Restrictions reduce false positives.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-specimen-lab',
        'Sputum induction specimen is collected when:',
        'Patient cannot produce adequate cough sample and order specifies',
        [
            'Routine venipuncture',
            'Any throat swab',
            'Urine dipstick'
        ],
        'Induction obtains lower airway sample.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'skill-specimen-lab',
        '24-hour urine collection starts:',
        'After discarding first morning void and timing begins with next void',
        [
            'Mid-collection without discard',
            'With first void included without protocol',
            'Without patient instructions'
        ],
        'Timing errors invalidate results.',
        [
            S.CLSI_GP41
        ],
        'intermediate',
    ),
    fact(
        'skill-specimen-lab',
        'When collecting a throat swab for group A strep, the collector should avoid:',
        'Touching tongue, teeth, or cheeks excessively',
        [
            'Posterior pharynx and tonsils',
            'Labeling tube',
            'Hand hygiene'
        ],
        'Technique maximizes pathogen recovery.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-specimen-lab',
        'Semen analysis specimen collection instructions include:',
        'Abstinence interval and transport temperature per lab',
        [
            'Hot tub before sample',
            'Sharing container',
            'Delayed delivery days later'
        ],
        'Lab manual defines abstinence period.',
        [
            S.CLSI_GP41
        ],
        'advanced',
    ),
    fact(
        'skill-specimen-lab',
        'Forensic urine drug testing with chain of custody requires:',
        'Witnessed collection when ordered and sealed containers',
        [
            'Patient leaving bathroom with open cup',
            'Adding water to dilute',
            'Unlabeled specimen'
        ],
        'Forensic standards apply.',
        [
            S.CLSI_GP41,
        S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'skill-specimen-lab',
        'Pregnancy test on urine is best read:',
        'Within manufacturer time window',
        [
            'Hours after expiration',
            'Before adding sample',
            'After washing strip'
        ],
        'Evaporation lines cause false interpretation.',
        [
            S.FDA_CLIA_WAIVED,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-intake',
        'Review of systems (ROS) documents:',
        'Patient-reported symptoms by body system',
        [
            'Only vital signs',
            'Staff schedule',
            'Insurance premium'
        ],
        'ROS supplements history of present illness.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-intake',
        'Medication allergy documentation should include:',
        'Drug name, reaction type, and severity',
        [
            'Only that patient has allergies without detail',
            'Food likes',
            'Parking spot'
        ],
        'Specific reactions guide prescribing.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-intake',
        'Social history may capture:',
        'Tobacco, alcohol, substance use, and occupation',
        [
            'Patient zodiac sign only',
            'Staff opinions',
            'Unrelated celebrity news'
        ],
        'Social factors affect health risks.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-intake',
        'The past medical history section of intake documents:',
        'Prior diagnoses, surgeries, and hospitalizations',
        [
            "Only today's lunch",
            'Neighbor diagnoses',
            'Future wishes only'
        ],
        'PMH informs care planning.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-intake',
        'Family history is important because:',
        'Many conditions have genetic or familial risk patterns',
        [
            'It replaces physical exam',
            'It is never relevant',
            'It is only for pediatrics'
        ],
        'Family history guides screening.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-intake',
        'Chief complaint should be recorded:',
        "In patient's own words when possible briefly",
        [
            'Only ICD code without words',
            'Provider guess without asking',
            'In Latin only'
        ],
        'CC drives visit focus.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-intake',
        'Height and weight at intake support:',
        'BMI calculation and medication dosing',
        [
            'Decorating chart only',
            'Skipping growth charts in children',
            'Ignoring trends'
        ],
        'Anthropometrics track health status.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-intake',
        'Screening questionnaires (PHQ-9, fall risk) at intake:',
        'Identify problems requiring follow-up per protocol',
        [
            'Replace provider exam',
            'Are never scored',
            'Posted publicly'
        ],
        'Validated tools standardize screening.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-osha-bbp',
        'Engineering controls in OSHA BBP standard include:',
        'Sharps disposal containers and safer medical devices',
        [
            'Verbal reminders only',
            'Optional gloves',
            'No controls needed'
        ],
        'Hierarchy places engineering first.',
        [
            S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-osha-bbp',
        'Hepatitis B vaccine series for at-risk employees must be offered:',
        'Free and at reasonable times unless employee declines documented',
        [
            'Only after seroconversion',
            'At employee expense only',
            'Never in medical offices'
        ],
        'OSHA requires offer to covered employees.',
        [
            S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-osha-bbp',
        'Post-exposure evaluation must be:',
        'Available promptly after exposure incident',
        [
            'Delayed 30 days routinely',
            'Only if patient known HIV positive',
            'Denied to per diem staff'
        ],
        'Timely eval enables PEP.',
        [
            S.OSHA_NEEDLESTICK,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-osha-bbp',
        'Work practice control examples include:',
        'No bending or recapping needles by hand',
        [
            'Reusing gloves all day',
            'Eating in lab bench',
            'Storing food in specimen fridge'
        ],
        'Behaviors reduce exposure risk.',
        [
            S.OSHA_BBP
        ],
        'beginner',
    ),
    fact(
        'skill-osha-bbp',
        'Personal protective equipment must be provided:',
        'At no cost to employee when occupational exposure exists',
        [
            'Purchased by employee only',
            'Optional always',
            'Only during inspections'
        ],
        'Employer provides PPE.',
        [
            S.OSHA_BBP
        ],
        'beginner',
    ),
    fact(
        'skill-osha-bbp',
        'Biohazard label symbol communicates:',
        'Presence of blood or other potentially infectious material',
        [
            'Radioactive waste only',
            'General trash',
            'Food quality'
        ],
        'Labels warn handlers.',
        [
            S.OSHA_BBP
        ],
        'beginner',
    ),
    fact(
        'skill-osha-bbp',
        'Annual review of Exposure Control Plan ensures:',
        'Plan reflects current tasks and technology',
        [
            'Plan never changes',
            'Employees not trained',
            'Sharps injuries ignored'
        ],
        'OSHA requires annual review.',
        [
            S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-osha-bbp',
        'Contaminated laundry should be:',
        'Bagged or containerized at location where used without sorting in patient area',
        [
            'Rinsed in sink splashing',
            'Taken home to wash',
            'Left on floor'
        ],
        'Handling limits aerosol and contact.',
        [
            S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-med-safety',
        'High-alert medications such as insulin require:',
        'Independent double-check per policy when indicated',
        [
            'Casual guessing',
            'Shared pens between patients',
            'Skipping allergy band'
        ],
        'High-alert drugs cause harm if misused.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-med-safety',
        'Five rights of medication administration include right:',
        'Patient, drug, dose, route, and time',
        [
            'Room color, shoe size, and hairstyle',
            'Copay only',
            'Parking spot'
        ],
        'Rights framework reduces errors.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-med-safety',
        'Discontinued medications on home med list should be:',
        'Marked inactive in EHR to prevent accidental continuation',
        [
            'Left active forever',
            'Given anyway if patient likes',
            'Deleted without audit trail per policy'
        ],
        'Accurate lists prevent duplication.',
        [
            S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-med-safety',
        'Crushing medications not labeled crushable can:',
        'Alter absorption or cause toxicity',
        [
            'Always be done for convenience',
            'Replace liquid formulation without pharmacist',
            'Be shared between patients'
        ],
        'Some formulations must stay intact.',
        [
            S.FDA_MEDICATION_SAFETY
        ],
        'intermediate',
    ),
    fact(
        'skill-med-safety',
        'Barcode medication administration when used:',
        'Matches patient, drug, dose, and time at bedside',
        [
            'Replaces patient identification',
            'Is optional for all high-risk drugs always',
            'Allows wrong patient scan'
        ],
        'BCMA adds verification layer.',
        [
            S.FDA_MEDICATION_SAFETY
        ],
        'advanced',
    ),
    fact(
        'skill-med-safety',
        'Outdated clinic stock medications should be:',
        'Removed from use and disposed per policy',
        [
            'Given to staff as samples',
            'Sold online',
            'Mixed with new stock'
        ],
        'Expired drugs may be ineffective or harmful.',
        [
            S.FDA_MEDICATION_SAFETY
        ],
        'beginner',
    ),
    fact(
        'skill-med-safety',
        'Patient teach-back for new inhaler includes:',
        'Return demonstration of technique',
        [
            'Handing device without instruction',
            'Assuming prior knowledge',
            'Skipping spacer education'
        ],
        'Technique affects drug delivery.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-med-safety',
        'Reporting medication errors internally supports:',
        'Root cause analysis and system fixes',
        [
            'Blaming patient only',
            'Hiding events',
            'Deleting EHR entries illegally'
        ],
        'Just culture improves safety.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-poct',
        'CLIA-waived tests may be performed:',
        'In sites with CLIA certificate and following manufacturer instructions',
        [
            'Anywhere without training',
            'Without quality control ever',
            'By patients without oversight in clinic'
        ],
        'Waived status still requires compliance.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'intermediate',
    ),
    fact(
        'skill-poct',
        'Quality control for waived glucometer means:',
        'Running control solution per schedule and documenting results',
        [
            'Only when meter fails visibly',
            'Using tap water on strip',
            'Skipping when busy'
        ],
        'QC detects drift and strip problems.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'intermediate',
    ),
    fact(
        'skill-poct',
        'Waived rapid strep positive result:',
        'Guides provider treatment decisions; follow positive protocol',
        [
            'Ignores without confirmation policy',
            'Automatically means viral infection',
            'Deletes without charting'
        ],
        'Follow institutional algorithm for confirmatory testing.',
        [
            S.FDA_CLIA_WAIVED,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-poct',
        'Influenza rapid antigen test sensitivity:',
        'False negatives occur; clinical judgment matters',
        [
            '100% sensitive always',
            'Never false positive',
            'Replaces all PCR always'
        ],
        'Understand test limitations.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'advanced',
    ),
    fact(
        'skill-poct',
        'Urine hCG point-of-care test false positive may result from:',
        'Certain medications or evaporation line if read late',
        [
            'Always true pregnancy only',
            'Drinking water only',
            'Using expired strip never'
        ],
        'Read within window and follow up abnormal results.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'advanced',
    ),
    fact(
        'skill-poct',
        'Personnel performing POC testing must:',
        'Complete competency training and maintenance per policy',
        [
            'Learn only from mistakes without training',
            'Perform any lab test without certificate',
            'Skip documentation'
        ],
        'Competency ensures valid results.',
        [
            S.FDA_CLIA_WAIVED,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-poct',
        'Hematocrit by spun microhematocrit is:',
        'Not waived in typical POL settings; know site CLIA status',
        [
            'Always waived in any room',
            'Same as glucometer waiver',
            'Unregulated always'
        ],
        'Test complexity determines requirements.',
        [
            S.FDA_CLIA_WAIVED
        ],
        'advanced',
    ),
    fact(
        'skill-poct',
        'POC result critical values should be:',
        'Reported immediately to provider per protocol',
        [
            'Filed without notification',
            'Given only to patient to interpret alone',
            'Posted on social media'
        ],
        'Critical values need urgent action.',
        [
            S.FDA_CLIA_WAIVED,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-wound-care',
        'Clinical signs of wound infection include:',
        'Increasing pain, erythema, warmth, purulent drainage, or fever',
        [
            'Decreased pain only always',
            'Clean healing granulation only',
            'No odor change ever'
        ],
        'Infection requires provider evaluation.',
        [
            S.CDC_STANDARD_PRECAUTIONS,
        S.CDC_HAND_HYGIENE,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-wound-care',
        'Pressure injury staging Stage 2 shows:',
        'Partial-thickness skin loss with exposed dermis',
        [
            'Full thickness to bone',
            'Intact skin non-blanchable erythema only',
            'No skin involvement'
        ],
        'Staging guides treatment.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'skill-wound-care',
        'Wound irrigation with normal saline aims to:',
        'Remove debris and bacteria gently',
        [
            'Cause pain without purpose',
            'Use high pressure always in all wounds',
            'Replace provider assessment'
        ],
        'Gentle irrigation cleanses wound bed.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-wound-care',
        'Transparent film dressing is appropriate for:',
        'Minimal drainage superficial wounds per order',
        [
            'Heavy draining wounds alone',
            'Third-degree burns without orders',
            'Untreated infection'
        ],
        'Dressing choice matches exudate.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-wound-care',
        'Alginate dressing absorbs:',
        'Moderate to heavy exudate',
        [
            'Dry wounds only',
            'Hair only',
            'Intact skin without wound'
        ],
        'Alginates form gel on contact with drainage.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'skill-wound-care',
        'Removing dressing toward wound in hairy areas:',
        'May reduce pain by pulling toward wound not away from skin',
        [
            'Always rip quickly away from wound',
            'Never secure',
            'Skip analgesia when painful'
        ],
        'Technique minimizes trauma.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-wound-care',
        'Documentation of wound care includes:',
        'Size, drainage, odor, periwound skin, and treatment applied',
        [
            'Only bandage color',
            'No measurement ever',
            "Another patient's data"
        ],
        'Trends guide healing progress.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-wound-care',
        'Unexplained foul odor from chronic wound suggests:',
        'Infection or necrotic tissue needing provider review',
        [
            'Always normal healing',
            'Need for perfume',
            'Ignore until next year'
        ],
        'Odor change warrants assessment.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-life-stages',
        'When assessing an infant fontanelle, documentation should note:',
        'Soft spots that normally close over time; bulging may indicate illness',
        [
            'Always sunken means health',
            'Hard as bone always abnormal immediately',
            'Ignore if crying'
        ],
        'Fontanelle changes can signal dehydration or increased ICP.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-life-stages',
        'Toddler injury prevention education includes:',
        'Gates on stairs and cabinet locks for chemicals',
        [
            'Unsupervised pool access',
            'Small toy parts for mouthing',
            'Car seat optional'
        ],
        'Developmental curiosity increases risk.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-life-stages',
        'Adolescent confidentiality may apply to:',
        'Certain reproductive and mental health services per state law',
        [
            'All information shared with friends by staff',
            'Never any privacy from parents always',
            'Billing data only'
        ],
        'Laws balance safety and privacy.',
        [
            S.NHA_CCMA
        ],
        'advanced',
    ),
    fact(
        'skill-life-stages',
        'Older adults may have atypical presentation of illness such as:',
        'Confusion or falls instead of classic fever',
        [
            'Always high fever first',
            'Never delirium',
            'Same as young adults always'
        ],
        'Atypical signs delay diagnosis.',
        [
            S.NHA_CCMA,
        S.MEDLINEPLUS_HAND_HYGIENE
        ],
        'intermediate',
    ),
    fact(
        'skill-life-stages',
        'Pediatric growth chart plotting requires:',
        'Accurate weight, length/height, and head circumference in infants',
        [
            'Guess percentiles',
            'Adult BMI chart for newborn',
            'Skip measurements'
        ],
        'Growth velocity detects problems.',
        [
            S.NHA_CCMA
        ],
        'beginner',
    ),
    fact(
        'skill-life-stages',
        'Geriatric polypharmacy increases risk of:',
        'Adverse drug events and interactions',
        [
            'Improved memory always',
            'Lower fall risk',
            'No side effects'
        ],
        'Medication review is essential.',
        [
            S.FDA_MEDICATION_SAFETY,
        S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-life-stages',
        'Neonatal jaundice visible in first week requires:',
        'Provider evaluation and bilirubin testing per protocol',
        [
            'Sunlamp at home only without follow-up',
            'Ignoring if feeding well always',
            'Stopping breastfeeding always'
        ],
        'Kernicterus is preventable with monitoring.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-life-stages',
        'End-of-life care planning discussions should:',
        'Occur when appropriate with compassion and documented preferences',
        [
            'Be avoided always',
            'Occur only in last minutes without prior talk',
            'Ignore advance directives'
        ],
        'Goals of care align treatment with values.',
        [
            S.NHA_CCMA
        ],
        'intermediate',
    ),
    fact(
        'skill-emergency-aid',
        'For chemical splash to eye, first aid is:',
        'Flush with water or saline for prolonged period per protocol and seek care',
        [
            'Rub eyes vigorously',
            'Wait until tomorrow',
            'Use neutralizing acid-base mix without guidance'
        ],
        'Immediate irrigation limits damage.',
        [
            S.RED_CROSS_FIRST_AID,
        S.OSHA_BBP
        ],
        'intermediate',
    ),
    fact(
        'skill-emergency-aid',
        'Nosebleed first aid includes:',
        'Leaning slightly forward and pinching soft part of nose for 10-15 minutes',
        [
            'Head tilted back swallowing blood',
            'Packing with unclean objects',
            'Ignoring anticoagulant use'
        ],
        'Forward lean prevents swallowing blood.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'beginner',
    ),
    fact(
        'skill-emergency-aid',
        'Sprain management initial care is:',
        'Rest, ice, compression, elevation (RICE) when appropriate',
        [
            'Heat immediately always',
            'Continue sport activity',
            'Massage fracture site'
        ],
        'RICE limits swelling.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'beginner',
    ),
    fact(
        'skill-emergency-aid',
        'Diabetic patient found confused and diaphoretic should receive:',
        'Fast-acting glucose if awake and able to swallow; call EMS if severe',
        [
            'Insulin dose immediately',
            'Only water if hypoglycemic',
            'Exercise'
        ],
        'Treat hypoglycemia promptly.',
        [
            S.RED_CROSS_FIRST_AID,
        S.CDC_DIABETES
        ],
        'intermediate',
    ),
    fact(
        'skill-emergency-aid',
        'Signs of shock include:',
        'Pale cool clammy skin, tachycardia, hypotension, altered mental status',
        [
            'Bradycardia only always',
            'Hypertension always',
            'Normal mental status only'
        ],
        'Shock is circulatory failure.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'skill-emergency-aid',
        'Burn with charred white skin (full thickness) needs:',
        'Emergency evaluation; do not apply home remedies alone',
        [
            'Butter application',
            'Popping blisters at home always',
            'Ignoring pain because nerves destroyed'
        ],
        'Full thickness burns need specialist care.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'intermediate',
    ),
    fact(
        'skill-emergency-aid',
        'Suspected opioid overdose with slow breathing may need:',
        'Naloxone and emergency activation when available and trained',
        [
            'Only coffee',
            'Sleep it off',
            'Cold shower alone'
        ],
        'Naloxone reverses opioid respiratory depression.',
        [
            S.RED_CROSS_FIRST_AID
        ],
        'advanced',
    ),
    fact(
        'skill-emergency-aid',
        'Emergency action plan in clinic should list:',
        'Roles, AED location, emergency numbers, and evacuation routes',
        [
            'Only lunch menu',
            'Staff birthdays',
            'Social media passwords'
        ],
        'Prepared teams respond faster.',
        [
            S.RED_CROSS_FIRST_AID,
        S.NHA_CCMA
        ],
        'beginner',
    ),
]
