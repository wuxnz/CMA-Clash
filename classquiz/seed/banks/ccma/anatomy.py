# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-anatomy)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-anatomy-001
    fact(
        'ccma-anatomy',
        'Where in the respiratory tract does oxygen from inhaled air cross into the bloodstream?',
        'Alveoli in the lungs',
        [
            'Renal tubules in the kidney',
            'Hepatic sinusoids in the liver',
            'Islets of Langerhans in the pancreas',
        ],
        'Alveoli are thin-walled air sacs surrounded by pulmonary capillaries, which is where gas exchange occurs. The kidney, liver, and pancreas perform filtration, metabolism, and endocrine functions rather than pulmonary gas transfer.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-002
    fact(
        'ccma-anatomy',
        'Which pulmonary structures are the main site of oxygen and carbon dioxide exchange?',
        'Alveoli',
        [
            'Trachea',
            'Primary bronchi',
            'Pleural space',
        ],
        'The trachea and bronchi conduct air but their walls are too thick for efficient diffusion. Gas exchange happens across the alveolar-capillary membrane, not in the pleural space between lung and chest wall.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-003
    fact(
        'ccma-anatomy',
        'What is the principal function of mature red blood cells (erythrocytes)?',
        'Carry oxygen to tissues using hemoglobin',
        [
            'Produce antibodies against pathogens',
            'Form the first line of platelet plugs',
            'Engulf bacteria by phagocytosis',
        ],
        'Hemoglobin in erythrocytes binds oxygen in the lungs and releases it where it is needed in tissues. Antibody production, clotting, and phagocytosis are roles of lymphocytes, platelets, and certain white cells.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-004
    fact(
        'ccma-anatomy',
        'In which region of the body is the femur located?',
        'Thigh (upper leg)',
        [
            'Upper arm (brachium)',
            'Lower leg below the knee',
            'Bony pelvis without the thigh',
        ],
        'The femur articulates with the hip and knee and forms the skeleton of the thigh. The humerus is the upper-arm bone, and the tibia and fibula lie in the lower leg.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-005
    fact(
        'ccma-anatomy',
        'What is the main job of the heart in the circulatory system?',
        'Pump blood through the pulmonary and systemic circuits',
        [
            'Filter toxins from blood like the kidneys',
            'Secrete digestive enzymes into the duodenum',
            'Store most of the body\'s calcium reserves',
        ],
        'Cardiac muscle contracts rhythmically to move blood to the lungs and the rest of the body. Detoxification, digestion, and bulk calcium storage are functions of other organs such as the liver, pancreas, and bone.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-006
    fact(
        'ccma-anatomy',
        'Which artery is the largest in the human body?',
        'Aorta',
        [
            'Pulmonary artery',
            'Femoral artery',
            'Common carotid artery',
        ],
        'The aorta leaves the left ventricle and branches to supply the systemic circulation. Regional arteries such as the pulmonary, femoral, and carotid vessels are smaller conduits downstream of the aorta.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-007
    fact(
        'ccma-anatomy',
        'The pharynx (throat) serves as a shared passageway for which two systems?',
        'Respiratory and digestive tracts',
        [
            'Urinary and reproductive tracts',
            'Endocrine and lymphatic systems',
            'Muscular and skeletal systems',
        ],
        'Air moves through the pharynx toward the larynx, and swallowed food passes toward the esophagus. The urinary and reproductive organs, endocrine glands, and named muscle-bone systems do not use the pharynx as a common channel.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-008
    fact(
        'ccma-anatomy',
        'Which skeletal muscle is the principal driver of quiet (resting) inspiration?',
        'Diaphragm',
        [
            'Trapezius',
            'Gastrocnemius',
            'Masseter',
        ],
        'When the diaphragm contracts, the thoracic cavity enlarges and air is drawn into the lungs. The trapezius moves the shoulder girdle, the gastrocnemius plantarflexes the ankle, and the masseter closes the jaw.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-009
    fact(
        'ccma-anatomy',
        'Which description best identifies the femur?',
        'The longest and strongest bone in the body',
        [
            'A tiny ossicle of the middle ear',
            'The clavicle (collarbone)',
            'A carpal bone of the wrist',
        ],
        'The femur bears body weight during standing and walking. Ear ossicles, the clavicle, and wrist carpals are much smaller bones with different locations and roles.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-010
    fact(
        'ccma-anatomy',
        'Which type of blood vessel typically carries blood away from the heart?',
        'Arteries',
        [
            'Veins',
            'Capillaries',
            'Lymphatic vessels',
        ],
        'Arteries convey blood from the heart toward tissues (the pulmonary artery is the notable exception carrying deoxygenated blood to the lungs). Veins return blood toward the heart, capillaries exchange nutrients and gases, and lymphatics drain excess fluid.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-011
    fact(
        'ccma-anatomy',
        'Which organ synthesizes bile that emulsifies dietary fats?',
        'Liver',
        [
            'Pancreas',
            'Gallbladder',
            'Spleen',
        ],
        'Hepatocytes in the liver produce bile, which may be stored and concentrated in the gallbladder before release into the duodenum. The pancreas secretes digestive enzymes and hormones, and the spleen filters blood and supports immune function.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-012
    fact(
        'ccma-anatomy',
        'Which tube transports urine from each kidney to the urinary bladder?',
        'Ureter',
        [
            'Urethra',
            'Renal pelvis',
            'Glomerulus',
        ],
        'Each ureter drains urine from the renal pelvis into the bladder. The urethra empties the bladder to the outside, the renal pelvis is a collecting basin in the kidney, and the glomerulus is a filtration capillary network.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-013
    fact(
        'ccma-anatomy',
        'Where is most cerebrospinal fluid (CSF) produced within the central nervous system?',
        'Choroid plexus in the brain ventricles',
        [
            'Gray matter of the spinal cord',
            'Dura mater of the meninges',
            'Cerebellar cortex',
        ],
        'The choroid plexus secretes CSF into the ventricular system, which then circulates around the brain and spinal cord. Spinal gray matter, the dura, and cerebellar tissue are not the primary CSF factories.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-014
    fact(
        'ccma-anatomy',
        'Through which vessels does systemic venous blood enter the right atrium?',
        'Superior and inferior vena cava',
        [
            'Pulmonary veins',
            'Aorta',
            'Coronary sinus',
        ],
        'The superior and inferior venae cavae return deoxygenated blood from the upper and lower body to the right atrium. Pulmonary veins bring oxygenated blood from the lungs to the left atrium, and the aorta leaves the left ventricle.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-015
    fact(
        'ccma-anatomy',
        'During a resting breath in, which muscle contraction most increases thoracic volume?',
        'Diaphragm',
        [
            'External intercostal muscles',
            'Rectus abdominis',
            'Genioglossus of the tongue',
        ],
        'Diaphragm descent is the dominant mechanism for quiet inspiration. Intercostals can assist with deeper breathing, abdominal muscles aid forced exhalation, and tongue muscles move the tongue rather than expand the chest.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-016
    fact(
        'ccma-anatomy',
        'Which pancreatic islet cells secrete insulin?',
        'Beta cells in the islets of Langerhans',
        [
            'Alpha cells in the islets of Langerhans',
            'Acinar cells of the exocrine pancreas',
            'Hepatocytes in the liver',
        ],
        'Beta cells release insulin when blood glucose rises. Alpha cells secrete glucagon, acinar cells produce digestive enzymes, and hepatocytes are liver cells with metabolic rather than endocrine pancreatic roles.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-017
    fact(
        'ccma-anatomy',
        'A patient has hyperglycemia. Which cell type is responsible for secreting the hormone that lowers blood glucose?',
        'Pancreatic beta cells',
        [
            'Pancreatic alpha cells',
            'Pancreatic acinar cells',
            'Kupffer cells in the liver',
        ],
        'Insulin from beta cells promotes glucose uptake and storage, which reduces blood sugar. Alpha cells release glucagon, which raises glucose; acinar and Kupffer cells are not insulin sources.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-018
    fact(
        'ccma-anatomy',
        'Insulin is an endocrine product of which tissue?',
        'Pancreatic islet (beta) cells',
        [
            'Hepatocytes in the liver',
            'Chromaffin cells of the adrenal medulla',
            'Thyroid follicular cells',
        ],
        'Beta cells within pancreatic islets synthesize and release insulin into the bloodstream. The liver, adrenal medulla, and thyroid produce other hormones such as albumin-related proteins, catecholamines, and thyroid hormone.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-019
    fact(
        'ccma-anatomy',
        'What do lymphatic vessels collect and move toward lymph nodes and the venous system?',
        'Lymph (fluid, proteins, and immune cells)',
        [
            'Oxygenated blood from the lungs',
            'Bile from the gallbladder',
            'Cerebrospinal fluid within the skull',
        ],
        'Lymphatics drain interstitial fluid and transport antigens and leukocytes for immune surveillance. Pulmonary blood, bile, and CSF use separate circulatory and duct systems.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-020
    fact(
        'ccma-anatomy',
        'Which vessels deliver oxygenated blood from the lungs into the left atrium?',
        'Pulmonary veins',
        [
            'Superior vena cava',
            'Pulmonary artery',
            'Coronary sinus',
        ],
        'After gas exchange in the lungs, oxygen-rich blood flows through four pulmonary veins into the left atrium. The superior vena cava and coronary sinus drain into the right atrium, and the pulmonary artery carries blood away from the right ventricle to the lungs.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-021
    fact(
        'ccma-anatomy',
        'Mature erythrocytes lack a nucleus. What is their main circulatory role?',
        'Transport oxygen bound to hemoglobin',
        [
            'Synthesize immunoglobulins',
            'Destroy bacteria by phagocytosis',
            'Secrete insulin into the portal vein',
        ],
        'Anucleate red cells are specialized for gas carriage via hemoglobin. Antibody production, bacterial engulfment, and insulin secretion belong to lymphocytes, neutrophils/macrophages, and pancreatic beta cells.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-022
    fact(
        'ccma-anatomy',
        'What process occurs chiefly in red bone marrow?',
        'Hematopoiesis (formation of blood cells)',
        [
            'Bile synthesis',
            'Cerebrospinal fluid production',
            'Pulmonary surfactant secretion',
        ],
        'Red marrow generates erythrocytes, leukocytes, and platelets throughout life in many bones. Bile is made in the liver, CSF by choroid plexus, and surfactant by type II alveolar cells.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-023
    fact(
        'ccma-anatomy',
        'Which feature defines a synovial joint such as the knee or shoulder?',
        'A joint cavity containing synovial fluid',
        [
            'Immovable fusion of adjacent bones',
            'A fibrous joint with no cavity',
            'An intervertebral disc between vertebrae',
        ],
        'Synovial joints have a lubricated cavity that allows varied movement. Fused or fibrous joints permit little or no motion, and spinal discs are cartilaginous structures rather than synovial cavities.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-024
    fact(
        'ccma-anatomy',
        'Which functions are coordinated mainly by the cerebellum?',
        'Balance, posture, and fine motor control',
        [
            'Sharp central vision',
            'Sound localization in the ear',
            'Detection of airborne odors',
        ],
        'The cerebellum compares intended movement with actual performance and adjusts muscle activity. Primary visual, auditory, and olfactory processing occur in other regions of the brain.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-025
    fact(
        'ccma-anatomy',
        'Contraction of the diaphragm is essential for which phase of breathing?',
        'Inspiration (drawing air into the lungs)',
        [
            'Emulsification of dietary fats',
            'Filtration of lymph in lymph nodes',
            'Amplification of sound in the ear',
        ],
        'Diaphragm contraction increases thoracic volume so air enters the lungs during inhalation. Fat emulsification involves bile, lymph filtration occurs in nodes, and the middle ear ossicles amplify sound.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The duodenum is the?',
        'First segment of the small intestine',
        [
            'Last part of the colon',
            'Gallbladder duct',
            'Stomach fundus',
        ],
        'Most chemical digestion begins in the duodenum. Choosing Last part of the colon is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The femur articulates with the pelvis at the?',
        'Acetabulum of the hip joint',
        [
            'Glenoid fossa',
            'Patella only',
            'Tibial plateau',
        ],
        'The hip is a ball-and-socket synovial joint. Choosing Glenoid fossa is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The functional contractile layer of the heart wall is the?',
        'Myocardium',
        [
            'Endocardium',
            'Epicardium only',
            'Pericardial fluid',
        ],
        'Myocardium generates the pumping force. Choosing Endocardium is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The functional unit of the kidney is the?',
        'Nephron',
        [
            'Alveolus',
            'Neuron',
            'Osteon',
        ],
        'Nephrons filter blood and form urine. Choosing Alveolus is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The hormone insulin is secreted by?',
        'Beta cells of pancreatic islets',
        [
            'Alpha cells only',
            'Adrenal cortex',
            'Thyroid follicles',
        ],
        'Insulin lowers blood glucose by promoting uptake. Choosing Alpha cells only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The kidneys primarily regulate?',
        'Fluid balance, electrolytes, and waste excretion',
        [
            'Blood glucose exclusively',
            'Heart rhythm',
            'Red blood cell shape only',
        ],
        'Nephrons filter blood and help maintain acid-base and volume homeostasis. Choosing Blood glucose exclusively is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The left ventricle pumps blood into the?',
        'Aorta',
        [
            'Pulmonary artery',
            'Superior vena cava',
            'Right atrium',
        ],
        'The left ventricle supplies the systemic circulation through the aorta. The pulmonary artery carries blood from the right ventricle to the lungs.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The meninges function to?',
        'Protect the brain and spinal cord',
        [
            'Produce digestive enzymes',
            'Filter glomerular filtrate',
            'Conduct cardiac impulse only',
        ],
        'Dura, arachnoid, and pia layers encase the CNS. Choosing Produce digestive enzymes is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    fact(
        'ccma-anatomy',
        'The mitral (bicuspid) valve separates the?',
        'Left atrium and left ventricle',
        [
            'Right atrium and ventricle',
            'Aorta and ventricle',
            'Pulmonary artery and ventricle',
        ],
        'Mitral valve prevents backflow into the left atrium. Choosing Right atrium and ventricle is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The mitral valve is located between the?',
        'Left atrium and left ventricle',
        [
            'Right atrium and right ventricle',
            'Aorta and left ventricle',
            'Pulmonary artery and right ventricle',
        ],
        'Mitral (bicuspid) valve is on the left side of the heart. Choosing Right atrium and right ventricle is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The nephron structure that filters blood is the?',
        "Glomerulus within Bowman's capsule",
        [
            'Loop of Henle only',
            'Collecting duct only',
            'Ureter',
        ],
        'Filtration occurs in the renal corpuscle. Choosing Loop of Henle only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The pleura surrounds the?',
        'Lungs',
        [
            'Heart only',
            'Liver',
            'Kidneys',
        ],
        'Pleural fluid reduces friction during breathing. Choosing Heart only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The portal vein carries nutrient-rich blood from the?',
        'Digestive tract to the liver',
        [
            'Lungs to the heart',
            'Kidney to bladder',
            'Brain to neck veins',
        ],
        'Hepatic processing occurs before systemic return. Choosing Lungs to the heart is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The primary pacemaker of the heart is the?',
        'Sinoatrial (SA) node',
        [
            'AV node only',
            'Bundle of His only',
            'Purkinje fibers only',
        ],
        'The SA node initiates normal sinus rhythm. Choosing AV node only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The thyroid gland is located?',
        'Anterior neck below the larynx',
        [
            'Posterior mediastinum',
            'Left upper quadrant of abdomen',
            'Retroperitoneal space',
        ],
        'Thyroid hormones regulate metabolism. Choosing Posterior mediastinum is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The tricuspid valve separates the?',
        'Right atrium and right ventricle',
        [
            'Left atrium and left ventricle',
            'Right ventricle and pulmonary artery',
            'Left ventricle and aorta',
        ],
        'The mitral (bicuspid) valve is between the left atrium and left ventricle. Choosing Left atrium and left ventricle is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'What is The autonomic nervous system division that slows heart rate?',
        'Parasympathetic',
        [
            'Sympathetic only',
            'Somatic motor',
            'Enteric only',
        ],
        'Parasympathetic activity promotes rest-and-digest responses. Choosing Sympathetic only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'Which lobe of the brain is primarily responsible for vision?',
        'Occipital lobe',
        [
            'Frontal lobe',
            'Temporal lobe',
            'Cerebellum',
        ],
        'The primary visual cortex lies in the occipital region. Choosing Frontal lobe is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'Cerebrospinal fluid circulates around the brain and spinal cord within the?',
        'Subarachnoid space and ventricles',
        [
            'Epidural space only',
            'Synovial cavities',
            'Pericardial sac',
        ],
        'CSF cushions the CNS and is produced mainly by the choroid plexus. Choosing Epidural space only is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
    fact(
        'ccma-anatomy',
        'The hormone glucagon is secreted by the pancreas to?',
        'Raise blood glucose',
        [
            'Lower blood glucose',
            'Increase urine output',
            'Slow heart rate',
        ],
        'Glucagon opposes insulin when glucose is low. Choosing Lower blood glucose is a plausible near-miss that does not match the clinical fact tested in this question.',
        [S.NHA_CCMA],
        'advanced',
    ),
]

