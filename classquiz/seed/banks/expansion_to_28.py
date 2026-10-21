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
