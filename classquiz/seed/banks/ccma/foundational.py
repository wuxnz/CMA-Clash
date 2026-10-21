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
        'Collect accurate data and report findings to the supervising provider',
        [
            'Assign the final diagnosis without provider review',
            'Select prescription medications for the patient',
            'Order advanced imaging without a provider order',
        ],
        'Medical assistants gather vitals, histories, and test results to support provider decision-making. Final diagnosis and prescribing remain within the licensed provider\'s scope, not the MA role.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-foundational-002
    fact(
        'ccma-foundational',
        'In standard anatomical position, what does the term anterior describe?',
        'The front or ventral surface of the body',
        [
            'The back or dorsal surface of the body',
            'A structure lying on the midline',
            'A structure farther from the trunk',
        ],
        'Anterior and posterior are paired directional terms used throughout documentation and procedures. The back of the body is posterior, not anterior.',
        [S.NHA_CCMA],
        'beginner',
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
        'beginner',
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
        'beginner',
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
            'They are reserved for inpatient hospital units',
        ],
        'Standard Precautions treat blood, non-intact skin, and most body fluids as potentially infectious regardless of diagnosis. Limiting precautions to visible blood or specific settings leaves gaps in outpatient and ambulatory care.',
        [S.CDC_STANDARD_PRECAUTIONS],
        'intermediate',
    ),
    # ccma-foundational-010
    fact(
        'ccma-foundational',
        'What primarily determines what tasks a medical assistant may legally perform?',
        'State law, employer policy, and the assistant\'s training',
        [
            'The patient\'s stated preference for who performs care',
            'Advertising claims from medical supply vendors',
            'Informal clinic tradition without written policy',
        ],
        'Scope of practice is set by regulation and delegated duties under supervision. Patient preference does not override legal limits on who may perform invasive or clinical acts.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-011
    fact(
        'ccma-foundational',
        'What should you do if you do not understand a provider\'s order?',
        'Contact the provider to clarify the order before proceeding',
        [
            'Follow what was done for a similar patient last week',
            'Ask an uninvolved patient in the waiting room',
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
        'Maintenance of relatively stable internal conditions despite external change',
        [
            'Complete shutdown of metabolism during stress',
            'Permanent elimination of all microorganisms in the body',
            'Fixed body temperature with no measurable variation',
        ],
        'Homeostasis uses feedback to regulate variables such as temperature, glucose, and fluid balance. The body still allows small fluctuations around set points rather than halting metabolism or forbidding any temperature change.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-013
    fact(
        'ccma-foundational',
        'Which description best defines a pathogen?',
        'A microorganism that can cause disease in a susceptible host',
        [
            'Any bacterium living on intact skin without symptoms',
            'A dietary vitamin required for nerve function',
            'An antibody produced after vaccination',
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
        'It counteracts the initial change to move the variable back toward a set point',
        [
            'It amplifies the initial stimulus without limit',
            'It removes hormones from circulation permanently',
            'It blocks all sensory input from the skin',
        ],
        'Negative feedback opposes deviation, as when sweating begins after a rise in temperature. Amplifying the stimulus without limit would worsen instability rather than restore balance.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-016
    fact(
        'ccma-foundational',
        'How is a solution with a pH of 7.0 classified?',
        'Neutral',
        [
            'Strongly acidic',
            'Strongly alkaline (basic)',
            'Equal to the pH of gastric acid',
        ],
        'On the pH scale, values below 7 are acidic and above 7 are alkaline. Gastric acid is far more acidic than 7.0, so it is not equivalent to a neutral solution.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-foundational-017
    fact(
        'ccma-foundational',
        'During passive diffusion across a membrane, how do molecules move relative to concentration?',
        'From higher concentration to lower concentration without cellular energy',
        [
            'From lower concentration to higher concentration using ATP',
            'Against a concentration gradient with active transport',
            'Randomly with no relationship to concentration',
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
            'Tradition, anecdote, and personal habit',
            'Billing codes, marketing data, and social media trends',
            'Laboratory reference ranges without clinical context',
        ],
        'Evidence-based practice weighs published evidence with clinician judgment and what matters to the patient. Reference ranges alone or informal habits do not replace that structured approach.',
        [S.NHA_CCMA],
        'intermediate',
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
        'advanced',
    ),
    # ccma-foundational-020
    fact(
        'ccma-foundational',
        'In limb anatomy, what does proximal mean?',
        'Closer to the point of attachment or the trunk',
        [
            'Farther from the trunk toward the extremity',
            'Toward the sole of the foot',
            'Away from the midline of the body',
        ],
        'On the arm, the elbow is proximal to the wrist because it lies nearer the shoulder attachment. Distal describes structures farther from the trunk, which is the opposite pairing tested on anatomy items.',
        [S.NHA_CCMA],
        'advanced',
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
        'advanced',
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
        'advanced',
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
        'advanced',
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
        'advanced',
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
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'Medical asepsis aims to?',
        'Reduce the number of microorganisms',
        [
            'Sterilize all surfaces always',
            'Eliminate every spore in the room',
            'Replace Standard Precautions',
        ],
        'Medical asepsis is clean technique; surgical asepsis is sterile technique. Choosing Sterilize all surfaces always is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'Medical asepsis is best defined as?',
        'Practices that reduce the number and spread of microorganisms',
        [
            'Complete absence of all microorganisms on instruments',
            'Use of sterile gowns in every exam room',
            'Destruction of only bacterial spores',
        ],
        'Medical asepsis (clean technique) lowers microbial load; surgical asepsis aims for sterility. Choosing Complete absence of all microorganisms on instruments is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        "OSHA's Bloodborne Pathogens Standard primarily aims to?",
        'Protect workers from exposure to bloodborne pathogens',
        [
            'Regulate medication dosing',
            'Set hospital billing codes',
            'Define surgical consent forms',
        ],
        'The standard requires exposure control plans, training, and engineering/work practice controls. Choosing Regulate medication dosing is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'Professional boundaries help staff?',
        'Maintain appropriate therapeutic relationships',
        [
            'Share personal social media passwords',
            'Accept large gifts from vendors routinely',
            'Discuss all patients in public areas',
        ],
        'Boundaries protect privacy and trust. Choosing Share personal social media passwords is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'Quality improvement (QI) in a clinic aims to?',
        'Systematically improve care processes and patient outcomes',
        [
            'Punish staff without system review',
            'Hide errors from leadership',
            'Replace guidelines with personal opinion',
        ],
        'QI uses measurement and teamwork to reduce harm. Choosing Punish staff without system review is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'Standard Precautions treat which body fluids as potentially infectious?',
        'All blood and body fluids except sweat unless visibly contaminated',
        [
            'Only fluids from patients with known HIV',
            'Only inpatient blood',
            'Saliva in every dental visit without exception',
        ],
        'Standard Precautions apply to all patient encounters in healthcare. Risk is not limited to known diagnoses.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'The chain of infection includes a reservoir, portal of exit, mode of transmission, portal of entry, and?',
        'Susceptible host',
        [
            'Insurance authorization',
            'Medical diagnosis',
            'Vital sign trend',
        ],
        'Breaking any link in the chain helps prevent infection spread. Choosing Insurance authorization is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'The first link in the chain of infection is the?',
        'Infectious agent (pathogen)',
        [
            'Portal of exit',
            'Susceptible host',
            'Mode of transmission',
        ],
        'Breaking any link can interrupt transmission. Choosing Portal of exit is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'The metric unit for mass commonly used in medicine is the?',
        'Gram',
        [
            'Liter',
            'Meter',
            'Mole only in nursing',
        ],
        'Drug doses often use grams or milligrams. Choosing Liter is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-foundational',
        'The prefix "brady-" means?',
        'Slow',
        [
            'Fast',
            'Pain',
            'Above normal',
        ],
        'Brady- indicates a slower rate, such as bradycardia. Tachy- indicates a faster rate. Choosing Fast is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'The prefix "hyper-" in hyperglycemia indicates?',
        'Above normal or excessive',
        [
            'Below normal',
            'Without',
            'Painful',
        ],
        'Hyper- means excessive or above a reference range. Choosing Below normal is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'The purpose of a Safety Data Sheet (SDS) in the clinic is to?',
        'Describe chemical hazards and safe handling',
        [
            'Bill insurance for supplies',
            'Store patient passwords',
            'Replace Standard Precautions',
        ],
        'Hazard communication supports safe chemical use. Choosing Bill insurance for supplies is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'The smallest functional unit of the kidney is the?',
        'Nephron',
        [
            'Neuron',
            'Alveolus',
            'Osteon',
        ],
        'Nephrons filter blood and form urine. Choosing Neuron is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'The suffix "-pathy" refers to?',
        'Disease of',
        [
            'Surgical repair',
            'Inflammation only',
            'Blood condition',
        ],
        '-pathy denotes disease or disorder of a body part. Choosing Surgical repair is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'Valid informed consent depends on the patient receiving?',
        'Clear information to make a voluntary choice',
        [
            'Only a signature without explanation',
            'Guaranteed outcomes',
            'Waivers of all future care',
        ],
        'Consent must be informed, voluntary, and competent. Choosing Only a signature without explanation is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'What does Critical thinking in patient care include?',
        'Evaluating data and questioning inconsistencies',
        [
            'Accepting all requests without review',
            'Avoiding documentation',
            'Using only intuition',
        ],
        'Clinical reasoning supports safe care decisions. Choosing Accepting all requests without review is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'What does The prefix "milli-" represent on the CCMA?',
        'One thousandth',
        [
            'One hundred',
            'One million',
            'Ten',
        ],
        'Milli- is 0.001 of the base unit. Choosing One hundred is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'What is A normal oral body temperature approximately?',
        '98.6°F (37°C)',
        [
            '91°F',
            '102°F at rest always',
            '100.4°F in all adults',
        ],
        'Fever is often defined above 100.4°F orally in adults. Choosing 91°F is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'What is In risk management, a healthcare "near miss"?',
        'An event that could have caused harm but did not',
        [
            'A confirmed sentinel event',
            'Expected treatment effect',
            'Routine lab variation',
        ],
        'Near-miss reporting improves safety systems. Choosing A confirmed sentinel event is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'When reading a prescription labeled "q.d.," it generally means?',
        'Once daily',
        [
            'Every four hours',
            'As needed',
            'Twice daily',
        ],
        'Latin abbreviations are being replaced by plain language in many settings. Choosing Every four hours is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'Which body cavity contains the heart and lungs?',
        'Thoracic cavity',
        [
            'Abdominal cavity',
            'Pelvic cavity',
            'Cranial cavity',
        ],
        'The thoracic cavity is protected by the rib cage. Choosing Abdominal cavity is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-foundational',
        'Which plane divides the body into right and left halves?',
        'Sagittal plane',
        [
            'Frontal (coronal) plane',
            'Transverse plane',
            'Oblique plane',
        ],
        'A midsagittal plane passes through the midline; parasagittal planes are offset. Choosing Frontal (coronal) plane is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]
