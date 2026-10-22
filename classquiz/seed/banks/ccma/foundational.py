# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-foundational)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-foundational-001
    fact(
        'ccma-foundational',
        'What is the medical assistant\'s typical responsibility when contributing to the diagnostic process?',
        'Gather subjective and objective data and report findings to the provider',
        [
            'Gather data and record a working diagnosis before the provider evaluates',
            'Collect vital signs and defer history until the provider enters the room',
            'Adjust medication doses from standing orders without provider review',
        ],
        'Medical assistants collect histories, vitals, and test results to support provider decision-making. Assigning final diagnoses, independent prescribing, or unsupervised medication changes exceed typical MA scope.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-002
    fact(
        'ccma-foundational',
        'In standard anatomical position, what does the term anterior describe?',
        'The front or ventral surface of the body',
        [
            'The back or dorsal surface of the body',
            'A structure lying on the midline of the body',
            'A structure located farther from the trunk',
        ],
        'Anterior and posterior are paired directional terms used throughout documentation and procedures. The back of the body is posterior, not anterior.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-003
    fact(
        'ccma-foundational',
        'What oral temperature is widely taught as the approximate average for a healthy adult?',
        '37°C (98.6°F)',
        [
            '35°C (95°F)',
            '39°C (102.2°F)',
            '34°C (93.2°F)',
        ],
        'Individual baselines vary by time of day, age, and measurement route. A reading near 35°C suggests hypothermia risk, while 39°C is more consistent with fever.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-004
    fact(
        'ccma-foundational',
        'What does the prefix brady- mean in words such as bradycardia?',
        'Slow or decreased rate',
        [
            'Fast or increased rate',
            'Pain or painful sensation',
            'Enlarged or excessive size',
        ],
        'Brady- denotes slowness, as in a heart rate below the expected range. Tachy- is the prefix for increased rate, which is a common terminology mix-up on exams.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-005
    fact(
        'ccma-foundational',
        'What does the suffix -itis indicate in a term such as tonsillitis?',
        'Inflammation of the referenced structure',
        [
            'Surgical removal of the structure',
            'A tumor of the structure',
            'A blood condition involving the structure',
        ],
        '-itis specifically means inflammation, seen in arthritis and gastritis. Surgical removal uses -ectomy, and blood conditions often use -emia.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-006
    fact(
        'ccma-foundational',
        'Which organization certifies candidates who pass the Certified Clinical Medical Assistant (CCMA) examination?',
        'National Healthcareer Association (NHA)',
        [
            'Clinical and Laboratory Standards Institute (CLSI)',
            'World Health Organization (WHO)',
            'U.S. Food and Drug Administration (FDA)',
        ],
        'NHA administers the CCMA credential for medical assistants. CLSI focuses on laboratory standards, and the FDA regulates drugs and devices rather than MA certification.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-007
    fact(
        'ccma-foundational',
        'What name is given to a temperature reading taken in the ear canal?',
        'Tympanic temperature',
        [
            'Axillary temperature',
            'Rectal temperature',
            'Temporal artery scan',
        ],
        'Tympanic measurements reflect heat near the tympanic membrane and require proper probe placement. Axillary readings are taken in the armpit, and rectal readings use the rectal route.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-008
    fact(
        'ccma-foundational',
        'In the metric system, by what factor does the prefix kilo- multiply a base unit?',
        '1,000',
        [
            '0.001',
            '100',
            '1,000,000',
        ],
        'Kilo- means one thousand, as in kilogram. Milli- (0.001) and centi- (0.01) are smaller prefixes that are often confused with kilo- on dosage calculations.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-009
    fact(
        'ccma-foundational',
        'Why are Standard Precautions used during routine patient care?',
        'They apply to all patients because infection status is not always known',
        [
            'They apply when gross blood is visible on linens',
            'They replace the need for hand hygiene after glove removal',
            'They are reserved for patients with known positive bloodborne pathogen tests',
        ],
        'Standard Precautions treat blood, non-intact skin, and most body fluids as potentially infectious regardless of diagnosis. Limiting precautions to visible blood or specific settings leaves gaps in outpatient and ambulatory care.',
        [S.CDC_STANDARD_PRECAUTIONS],
        'advanced',
    ),
    # ccma-foundational-010
    fact(
        'ccma-foundational',
        'What primarily determines what tasks a medical assistant may legally perform?',
        'State law, employer policy, and assistant training',
        [
            'Patient preference for who performs a given procedure',
            'Unwritten clinic tradition rather than documented policy',
            'What other clinics allow their assistants to perform',
        ],
        "Scope of practice is set by state law, employer policy, and the assistant's training. Patient preference and unwritten clinic tradition cannot expand the legal limits on delegated clinical tasks.",
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-011
    fact(
        'ccma-foundational',
        'What should you do if you do not understand a provider\'s order?',
        'Contact the provider to clarify the order before proceeding',
        [
            'Follow what was done for a similar patient last week',
            'Ask another medical assistant who was not present for the order',
            'Proceed and document uncertainty after the task',
        ],
        'Ambiguous orders are a common source of medication and procedure errors. Clarification before action protects the patient; guessing from prior cases can cause wrong-site or wrong-dose mistakes.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-012
    fact(
        'ccma-foundational',
        'What does homeostasis mean in human physiology?',
        'Maintenance of stable internal conditions despite external change',
        [
            'A complete shutdown of metabolism whenever the body is stressed',
            'Permanent elimination of every microorganism that enters the body',
            'A fixed body temperature with no variation around the set point',
        ],
        'Homeostasis uses feedback to regulate variables such as temperature, glucose, and fluid balance. The body still allows small fluctuations around set points rather than halting metabolism or forbidding any temperature change.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-013
    fact(
        'ccma-foundational',
        'Which description best defines a pathogen?',
        'A microorganism that can cause disease in a susceptible host',
        [
            'Bacteria that colonize intact skin without causing symptoms',
            'A dietary vitamin that supports normal nerve function in adults',
            'An antibody the immune system makes after a vaccination',
        ],
        'Pathogens include bacteria, viruses, fungi, and parasites capable of producing infection. Commensal skin flora, nutrients, and immune proteins are not pathogens even though they appear in clinical discussions.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-014
    fact(
        'ccma-foundational',
        'In medical terminology, what does the suffix -emia indicate?',
        'A condition involving the blood',
        [
            'Surgical incision into a vessel',
            'Inflammation of a joint',
            'Abnormal hardening of tissue',
        ],
        '-emia appears in terms such as anemia and hyperglycemia to describe blood-related conditions. Inflammation uses -itis, and incision terminology uses different suffixes such as -otomy.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-015
    fact(
        'ccma-foundational',
        'How does a negative feedback loop help regulate a body variable such as core temperature?',
        'It opposes the change and moves the variable toward a set point',
        [
            'It amplifies the initial stimulus rather than opposing the change',
            'It removes regulatory hormones from circulation for good',
            'It blocks sensory input from the skin before signals arrive',
        ],
        'Negative feedback opposes deviation, as when sweating begins after a rise in temperature. Amplifying the stimulus without limit would worsen instability rather than restore balance.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-016
    fact(
        'ccma-foundational',
        'How is a solution with a pH of 7.0 classified?',
        'Neutral, midway between acidic and alkaline',
        [
            'Strongly acidic, well below 7 on the pH scale',
            'Strongly alkaline, well above 7 on the pH scale',
            'Equal to the pH of gastric acid secretions in the stomach',
        ],
        'On the pH scale, values below 7 are acidic and above 7 are alkaline. Gastric acid is far more acidic than 7.0, so it is not equivalent to a neutral solution.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-017
    fact(
        'ccma-foundational',
        'During passive diffusion across a membrane, how do molecules move relative to concentration?',
        'From higher to lower concentration without cellular energy',
        [
            'From lower to higher concentration using cellular ATP energy',
            'Against the concentration gradient using active transport',
            'In either direction with no link to concentration differences',
        ],
        'Passive diffusion follows a concentration gradient and does not require ATP. Moving uphill against a gradient requires active transport, which is a separate mechanism.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-018
    fact(
        'ccma-foundational',
        'Which three components are integrated in evidence-based practice?',
        'Best available research, clinical expertise, and patient values',
        [
            'Best available research, clinical expertise, and cost containment goals',
            'Best available research, clinical guidelines, and expert consensus opinion',
            'Clinical expertise, patient values, and payer reimbursement policy',
        ],
        'Evidence-based practice weighs published evidence with clinician judgment and what matters to the patient. Reference ranges alone or informal habits do not replace that structured approach.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-019
    fact(
        'ccma-foundational',
        'The combining form my/o in myalgia refers to which tissue?',
        'Muscle',
        [
            'Bone marrow',
            'The ear',
            'The liver',
        ],
        'My/o relates to muscle, as in myopathy. Myel/o refers to bone marrow or spinal cord, which is a frequent terminology distractor paired with my/o.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-020
    fact(
        'ccma-foundational',
        'In limb anatomy, what does proximal mean?',
        'Closer to the point of attachment or the trunk',
        [
            'Farther from the trunk toward the extremity',
            'Toward the sole of the foot rather than the ankle',
            'Away from the midline toward the lateral side',
        ],
        'On the arm, the elbow is proximal to the wrist because it lies nearer the shoulder attachment. Distal describes structures farther from the trunk, which is the opposite pairing tested on anatomy items.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-021
    fact(
        'ccma-foundational',
        'According to CDC hand hygiene guidance, when is alcohol-based hand rub an acceptable method for cleaning hands in healthcare settings?',
        'When hands are not visibly soiled with dirt or body substances',
        [
            'When hands are visibly contaminated with blood',
            'When hands feel dry after several applications of gel',
            'When soap and water are unavailable and hands are visibly soiled',
        ],
        'CDC recommends soap and water when hands are visibly dirty or contaminated with proteinaceous material. Alcohol rub is appropriate for routine decontamination when soil is not visible.',
        [S.CDC_HAND_HYGIENE],
        'intermediate',
    ),
    # ccma-foundational-022
    fact(
        'ccma-foundational',
        'Which anatomical plane divides the body into anterior and posterior sections?',
        'Frontal (coronal) plane',
        [
            'Sagittal plane',
            'Transverse (horizontal) plane',
            'Midsagittal plane through the midline',
        ],
        'A frontal plane separates front from back. A sagittal plane divides right from left, which is a common plane-of-section mix-up in foundational anatomy questions.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-023
    fact(
        'ccma-foundational',
        'What does the prefix hyper- mean in a term such as hyperglycemia?',
        'Above normal or excessive',
        [
            'Below normal or deficient',
            'Without or lacking',
            'Pain or painful',
        ],
        'Hyper- signals excess, as in elevated blood glucose. Hypo- means below normal, and different suffixes convey pain or absence of structure.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-024
    fact(
        'ccma-foundational',
        'At standard sea-level atmospheric pressure, at what temperature does pure water boil?',
        '100°C (212°F)',
        [
            '37°C (98.6°F)',
            '0°C (32°F)',
            '50°C (122°F)',
        ],
        'Boiling point at 1 atmosphere is a fixed reference used when converting metric temperature scales in science coursework. Body temperature and freezing point are different landmark values on the Celsius scale.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-025
    fact(
        'ccma-foundational',
        'How many milligrams are equivalent to one gram when converting medication weights?',
        '1,000 milligrams',
        [
            '10 milligrams',
            '100 milligrams',
            '0.001 milligrams',
        ],
        'The metric system moves by powers of ten; milli- is one thousandth of a gram. Confusing gram-to-milligram conversion with centi- or micro- prefixes leads to tenfold or thousandfold dosing errors on paper problems.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-026
    fact(
        'ccma-foundational',
        'What is the primary goal of medical asepsis during routine patient care?',
        'Reduce the number and spread of microorganisms using clean technique',
        [
            'Achieve sterility on every work surface in the clinic and on instruments',
            'Eliminate all bacterial spores from every surface in the building',
            'Replace hand hygiene and Standard Precautions in daily patient care',
        ],
        'Medical asepsis (clean technique) lowers microbial load on hands, equipment, and surfaces. Surgical asepsis targets sterility for invasive procedures; the two approaches complement rather than replace Standard Precautions.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-027
    fact(
        'ccma-foundational',
        'What is the main purpose of OSHA\'s Bloodborne Pathogens Standard in healthcare workplaces?',
        'Protect workers from bloodborne pathogen exposure',
        [
            'Establish maximum daily doses for prescription medications',
            'Assign ICD-10 diagnosis codes for insurance billing',
            'Define the legal elements of surgical informed consent',
        ],
        'The standard requires a written exposure control plan, employee training, hepatitis B vaccination offers, and engineering or work-practice controls such as sharps safety devices. It addresses occupational safety rather than clinical coding or prescribing rules.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-028
    fact(
        'ccma-foundational',
        'Why are professional boundaries important for medical assistants?',
        'They help maintain appropriate, trust-based therapeutic relationships',
        [
            'They permit accepting small gifts from every patient without policy review',
            'They allow dual relationships when the patient initiates friendship',
            'They allow discussing patient cases in the elevator with visitors present',
        ],
        'Clear boundaries protect patient privacy, prevent favoritism, and reduce ethical conflicts. Dual relationships and casual disclosure of protected health information undermine the professional role of the care team.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-029
    fact(
        'ccma-foundational',
        'What is the central aim of quality improvement (QI) activities in an outpatient clinic?',
        'Systematically improve care processes and patient outcomes',
        [
            "Focus quality meetings on individual blame without reviewing workflow causes",
            "Track satisfaction scores while deferring review of recurring medication errors",
            "Adopt each staff member's preferred habit instead of testing a change",
        ],
        'QI uses data, teamwork, and small tests of change to reduce harm and waste. Blaming individuals without examining workflows misses recurring system causes of errors.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-030
    fact(
        'ccma-foundational',
        'Under Standard Precautions, which body fluids are generally treated as potentially infectious?',
        'All blood, non-intact skin, and most body fluids',
        [
            'Blood from patients with a documented positive HIV test',
            'Blood drawn during inpatient hospitalization but not in outpatient settings',
            'Saliva during routine dental prophylaxis without blood',
        ],
        'Standard Precautions apply to every patient encounter because infection status is not always known. Sweat is not included unless it is visibly contaminated with blood or other fluids.',
        [S.CDC_STANDARD_PRECAUTIONS],
        'intermediate',
    ),
    # ccma-foundational-031
    fact(
        'ccma-foundational',
        'In the chain of infection, what is the final link that must be present for disease to occur in a person?',
        'A susceptible host who lacks protective immunity',
        [
            'The handwashing sink used as the biologic host of germs',
            'A sterile instrument pack in central supply',
            'The clinic scheduling software database',
        ],
        'The classic chain includes an infectious agent, reservoir, portal of exit, mode of transmission, portal of entry, and a susceptible host. Interventions such as vaccination or isolation break one or more links to stop spread.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-032
    fact(
        'ccma-foundational',
        'Which component of the chain of infection must exist before transmission can begin?',
        'Infectious agent (pathogen)',
        [
            'Portal of exit from the reservoir',
            'Susceptible host in the community',
            'Mode of transmission between people',
        ],
        'The pathogen is the first link; without a microorganism capable of causing disease, the remaining steps cannot produce infection. Portals and transmission routes describe how the agent leaves one host and enters another.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-033
    fact(
        'ccma-foundational',
        'Which metric unit is most commonly used to express medication mass in prescriptions?',
        'Gram (often as milligrams)',
        [
            'Liter, for volume of medication',
            'Meter, for distance measurement',
            'Mole, for amount of a substance',
        ],
        'Solid and many liquid drug strengths are written in grams or milligrams. Liters measure volume, meters measure length, and the mole is a chemistry unit not used for everyday prescription labels.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-034
    fact(
        'ccma-foundational',
        'What does the prefix tachy- indicate in a term such as tachycardia?',
        'Fast or increased rate',
        [
            'Slow or decreased rate',
            'Pain or painful sensation',
            'Below normal amount',
        ],
        'Tachy- denotes speed or rate, as in a heart rate above the expected range. Brady- is the paired prefix for slowness, which is a common terminology contrast on CCMA exams.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-035
    fact(
        'ccma-foundational',
        'What does the prefix hypo- mean in a term such as hypoglycemia?',
        'Below normal or deficient',
        [
            'Above normal or excessive',
            'Without or lacking structure',
            'Pain or painful',
        ],
        'Hypo- signals a decrease, such as low blood glucose. Hyper- means excessive, and different prefixes convey absence of structure or pain.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-036
    fact(
        'ccma-foundational',
        'What information does a Safety Data Sheet (SDS) provide for a chemical used in the clinic?',
        'Hazards, safe handling, and emergency response measures',
        [
            "Storage temperature alone, without hazard or spill response guidance",
            "The chemical's cost and supplier contact information",
            "A substitute for infection control precautions during patient care",
        ],
        'OSHA hazard communication rules require accessible SDS files for hazardous chemicals such as disinfectants and fixatives. They support safe storage and spill response but do not replace clinical infection prevention practices.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-037
    fact(
        'ccma-foundational',
        'What is the smallest functional unit of the kidney that filters blood and forms urine?',
        'Nephron',
        [
            'Neuron',
            'Alveolus',
            'Osteon',
        ],
        'Each nephron contains a glomerulus and tubule segments that regulate filtration and reabsorption. Neurons conduct impulses, alveoli exchange gases in the lungs, and osteons are structural units of compact bone.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-038
    fact(
        'ccma-foundational',
        'In medical terminology, what does the suffix -pathy indicate?',
        'Disease or disorder of the referenced structure',
        [
            'Surgical repair of the referenced structure',
            'Inflammation of the referenced structure',
            'A blood condition involving the referenced structure',
        ],
        '-pathy appears in terms such as neuropathy and cardiomyopathy to describe disease processes. Surgical repair uses -plasty or -ectomy, inflammation uses -itis, and blood conditions often end in -emia.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-039
    fact(
        'ccma-foundational',
        'For informed consent to be valid, what must the patient receive before agreeing to a procedure?',
        'Clear information for a voluntary, informed decision',
        [
            'A signature line without discussion of risks or alternatives',
            'A promise that the procedure will produce a specific outcome',
            'A waiver releasing the clinic from all future medical care',
        ],
        'Valid consent requires disclosure of the procedure, benefits, risks, and alternatives in language the patient understands. It must be voluntary and given by a competent decision-maker; a blank form or guaranteed results do not meet that standard.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-040
    fact(
        'ccma-foundational',
        'Which behavior best reflects critical thinking during patient care?',
        'Evaluating clinical data and questioning inconsistencies',
        [
            'Carrying out every request without clarifying the order',
            'Deferring all documentation until the end of the shift',
            'Relying on habit rather than comparing findings to norms',
        ],
        'Critical thinking combines observation, knowledge, and judgment to spot errors or changes in condition. Clarifying ambiguous orders and documenting contemporaneously support safer care than unchecked routine.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-041
    fact(
        'ccma-foundational',
        'In the metric system, what fractional part of a base unit does the prefix milli- represent?',
        'One thousandth (0.001)',
        [
            'One hundredth (0.01)',
            'One millionth (0.000001)',
            'One tenth (0.1)',
        ],
        'Milli- scales doses and measurements by 10⁻³, as in milligrams and milliliters. Centi- is one hundredth, micro- is one millionth, and deci- is one tenth; mixing these prefixes causes large calculation errors.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-042
    fact(
        'ccma-foundational',
        'Which oral temperature is widely used as an approximate fever threshold in many adults?',
        '100.4°F (38°C)',
        [
            '91°F (32.8°C)',
            '98.6°F (37°C)',
            '102°F (38.9°C) at rest in every adult',
        ],
        'A single elevated reading should be interpreted with symptoms, route, and baseline. Core temperature near 91°F suggests hypothermia, while 98.6°F is closer to average than to fever.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-043
    fact(
        'ccma-foundational',
        'In healthcare risk management, what is a "near miss"?',
        'An event that could have caused harm but did not reach the patient',
        [
            'A sentinel event that resulted in serious and lasting harm to the patient',
            'An expected therapeutic response to the prescribed treatment',
            'Routine biologic variation within a laboratory reference interval',
        ],
        'Near misses reveal system weaknesses before injury occurs and are valuable for proactive improvement. Sentinel events involve actual serious harm; they are reported and analyzed under a different safety category.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-044
    fact(
        'ccma-foundational',
        'On a prescription, what does the Latin abbreviation q.d. (quaque die) commonly mean?',
        'Once daily',
        [
            'Every four hours',
            'As needed for pain',
            'Twice daily',
        ],
        'Q.d. indicates one dose per day. Q4h means every four hours, p.r.n. means as needed, and b.i.d. means twice daily; many organizations now prefer plain-language directions to reduce abbreviation errors.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-045
    fact(
        'ccma-foundational',
        'Which major body cavity houses the heart and lungs?',
        'Thoracic cavity',
        [
            'Abdominal cavity',
            'Pelvic cavity',
            'Cranial cavity',
        ],
        'The thoracic cavity lies within the rib cage and is separated from the abdomen by the diaphragm. The abdominal cavity contains digestive organs, the pelvic cavity contains reproductive and urinary structures inferiorly, and the cranial cavity encloses the brain.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-046
    fact(
        'ccma-foundational',
        'Which anatomical plane divides the body into right and left portions?',
        'Sagittal plane',
        [
            'Frontal (coronal) plane',
            'Transverse (horizontal) plane',
            'Oblique plane',
        ],
        'A sagittal section runs parallel to the midline; a midsagittal cut produces equal right and left halves. The frontal plane separates anterior from posterior, and the transverse plane divides superior from inferior.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-047
    fact(
        'ccma-foundational',
        'What does the combining form derm/o refer to in terms such as dermatology?',
        'Skin',
        [
            'Liver',
            'Kidney',
            'Bone',
        ],
        'Derm/o relates to the skin and its appendages. Hepat/o refers to the liver, nephr/o to the kidney, and oste/o to bone; pairing the wrong combining form with a suffix changes the meaning of the whole term.',
        [S.NHA_CCMA],
        'beginner',
    ),

    # ccma-foundational-048
    fact(
        'ccma-foundational',
        'What does the combining form "leuko-" refer to in medical terminology?',
        'White',
        ['Red',
        'Yellow',
        'Blue'],
        'Leuko- means white, as in leukocytes (white blood cells). Erythro- refers to red, which is a common mix-up on terminology items.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-049
    fact(
        'ccma-foundational',
        'Why are Standard Precautions applied to every patient encounter?',
        'Blood and body fluids may carry infection even when a diagnosis is unknown',
        [
            'They apply when gross blood is visible on linens but not to other body fluids',
            'They replace Transmission-Based Precautions once infection status is known',
            'They focus on hand hygiene after glove removal, not safe injection',
        ],
        'CDC Standard Precautions treat every patient as potentially infectious because blood and body fluids can carry pathogens before a diagnosis is known. Limiting precautions to visible blood, or replacing Transmission-Based Precautions once results return, misses undiagnosed carriage.',
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-050
    fact(
        'ccma-foundational',
        'A clinic implements a new chemical disinfectant. What must the medical assistant review before use?',
        'The product label for contact time, dilution, and compatible surfaces',
        ['A competitor product label copied without reading dilution instructions',
        'The color of the bottle alone',
        'Whether patients prefer scented products'],
        'EPA-registered disinfectants require label-directed contact times to kill pathogens. Dilution and surface compatibility affect both safety and effectiveness.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-051
    fact(
        'ccma-foundational',
        'What plane divides the body into superior and inferior portions?',
        'Transverse (horizontal) plane',
        [
            'Sagittal plane of the body',
            'Frontal (coronal) plane of the body',
            'Median plane through the midline',
        ],
        'A transverse cut separates head from lower body regions. Sagittal planes divide right from left, which is a common plane mix-up.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-052
    fact(
        'ccma-foundational',
        'Which type of pathogen is a single-celled organism that may produce toxins?',
        'Bacterium, a single-celled organism',
        [
            'Virus, which needs a living host cell',
            'Prion, a misfolded protein',
            'Vitamin, an organic nutrient',
        ],
        'Bacteria are living cells that can multiply outside host cells. Viruses require host machinery, and prions are misfolded proteins without cells.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-053
    fact(
        'ccma-foundational',
        'A splash of blood lands on unbroken skin of a gloved hand during a procedure. What is the priority action after the event?',
        'Remove gloves, perform hand hygiene, and follow exposure protocol',
        [
            'Wipe the glove with a dry paper towel and continue working without reporting',
            'Apply hand lotion and return to the procedure room',
            'Ignore the splash because the skin was intact',
        ],
        'OSHA bloodborne pathogen rules require prompt cleansing and evaluation after exposure. Intact skin still warrants protocol because permeability and microabrasions vary.',
        [S.OSHA_BBP, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-054
    fact(
        'ccma-foundational',
        'How does medical asepsis differ from surgical asepsis in its primary goal?',
        'Reduce the number and spread of microorganisms',
        ['Eliminate every microorganism on all surfaces in the building',
        'Use scented lotion instead of hand hygiene between patients',
        'Apply surgical sterility standards to every waiting room chair'],
        'Clean technique lowers bioburden for noninvasive care. Sterility targets absence of microbes on instruments entering sterile fields.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-055
    fact(
        'ccma-foundational',
        'An employee reports a needlestick with a contaminated hollow-bore needle. What must happen immediately?',
        'Wash the area, report the exposure, and seek medical evaluation',
        [
            'Finish the clinic day before telling anyone about the needlestick',
            'Squeeze the wound until the bleeding stops and return to work',
            'Document the incident as a patient allergy instead',
        ],
        'OSHA requires prompt reporting and medical follow-up for sharps injuries. Delayed care reduces prophylaxis options for bloodborne viruses.',
        [S.OSHA_NEEDLESTICK, S.OSHA_BBP, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-056
    fact(
        'ccma-foundational',
        'Which term describes a body position lying face up?',
        'Supine',
        ['Prone',
        'Lithotomy',
        'Trendelenburg'],
        'Supine means anterior surface up. Prone is face down; lithotomy involves raised legs for pelvic exams.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-057
    fact(
        'ccma-foundational',
        'What is the reservoir in the chain of infection?',
        'The place where pathogens live and multiply',
        ['The handwashing sink as the biologic host',
        'A sterile instrument pack in central supply',
        'The clinic scheduling software database'],
        'Reservoirs include humans, animals, or the environment where microbes persist. Equipment can transmit but is not the biologic reservoir itself.',
        [S.CDC_STANDARD_PRECAUTIONS, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-058
    fact(
        'ccma-foundational',
        'A clinic switches to a new EPA-registered surface disinfectant after a norovirus outbreak in the community. What training should staff receive?',
        'Proper dilution, contact time, and PPE for the new product',
        [
            'Use the previous product contact time for the new bottle of cleaner',
            'That every cleaner works the same without reading the product labels',
            'How to store disinfectant in unlocked exam rooms between uses',
        ],
        'Label instructions define kill claims and safe use. Misuse leaves viable viruses on surfaces and risks chemical exposure.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-foundational-059
    fact(
        'ccma-foundational',
        'What does the suffix "-ectomy" indicate in a surgical term?',
        'Surgical removal',
        [
            'Inflammation of the part',
            'Enlargement of the part',
            'Pertaining to the part',
        ],
        '-ectomy means excision, as in appendectomy. -itis is inflammation; -megaly is enlargement.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-060
    fact(
        'ccma-foundational',
        'Which temperature route is considered core-adjacent for many adults when oral measurement is not possible?',
        'Rectal temperature',
        [
            'Axillary temperature',
            'Skin over the forearm',
            'Ear without a probe cover',
        ],
        'Rectal readings reflect core trends when oral is contraindicated. Axillary and uncovered probes are more variable.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-061
    fact(
        'ccma-foundational',
        'After a chemical splash to the eye in the clinic laboratory, what is the immediate priority?',
        'Flush the eye at the eyewash station with water or saline',
        [
            'Wait for irritation symptoms to appear before rinsing the eye',
            'Apply contact lens solution and rub the eye vigorously',
            'Document the exposure event the following day',
        ],
        'Prompt irrigation dilutes caustic agents and limits corneal injury. Delay worsens chemical burns.',
        [S.OSHA_BBP, S.NHA_CCMA],
        'advanced',
    ),
]
