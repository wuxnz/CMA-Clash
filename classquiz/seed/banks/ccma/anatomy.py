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
            'Terminal bronchioles in the conducting zone',
            'Pulmonary capillaries without alveolar contact',
            'Respiratory bronchioles before the alveolar ducts',
        ],
        'Alveoli are thin-walled air sacs surrounded by pulmonary capillaries, which is where gas exchange occurs. Bronchioles conduct air but lack the thin alveolar-capillary interface required for diffusion.',
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
            'Exchange oxygen and carbon dioxide across alveolar membranes',
            'Filter plasma and form urine in renal nephrons',
            'Return interstitial fluid through lymphatic vessels',
        ],
        'Cardiac muscle contracts rhythmically to move blood to the lungs and the rest of the body. Gas exchange occurs in the lungs, filtration in the kidneys, and lymph return uses separate vessels rather than cardiac pumping.',
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
            'Laryngeal airway and trachea as one digestive channel',
            'Nasal cavity and oral cavity for digestion of food',
            'Esophagus and stomach as the shared respiratory passage',
        ],
        'Air moves through the pharynx toward the larynx, and swallowed food passes toward the esophagus. The larynx and trachea are respiratory; the esophagus and stomach are digestive, but only the pharynx serves both routes.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-008
    fact(
        'ccma-anatomy',
        'Which skeletal muscle is the principal driver of quiet (resting) inspiration?',
        'Diaphragm',
        [
            'External intercostal muscles between the ribs',
            'Sternocleidomastoid during quiet tidal breathing',
            'Rectus abdominis during passive inhalation at rest',
        ],
        'When the diaphragm contracts, the thoracic cavity enlarges and air is drawn into the lungs. Intercostals assist forced breathing, sternocleidomastoid is an accessory muscle, and abdominal muscles mainly aid exhalation.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-009
    fact(
        'ccma-anatomy',
        'Which description best identifies the femur?',
        'The longest and strongest bone in the body',
        [
            'The humerus of the upper arm',
            'The tibia of the lower leg',
            'The fibula lateral to the tibia',
        ],
        'The femur bears body weight during standing and walking. The humerus, tibia, and fibula are other long bones but the femur is the longest and strongest in the body.',
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
            'Interstitial fluid drained from capillary beds',
            'Chyle absorbed from intestinal lacteals',
            'Plasma filtrate returning directly through venules',
        ],
        'Lymphatics drain interstitial fluid and transport antigens and leukocytes for immune surveillance. Chyle and interstitial fluid enter lymphatics, but the collected fluid moved toward nodes is lymph, not direct venous plasma return.',
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
            'Forced exhalation during cough or speech',
            'Passive recoil exhalation at end expiration',
            'Gas exchange across the alveolar-capillary membrane',
        ],
        'Diaphragm contraction increases thoracic volume so air enters the lungs during inhalation. Exhalation and alveolar gas exchange are separate phases and processes from inspiratory muscle contraction.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-026
    fact(
        'ccma-anatomy',
        'Which segment of the gastrointestinal tract is the duodenum?',
        'The first portion of the small intestine',
        [
            'The terminal segment of the large intestine',
            'The cystic duct draining the gallbladder',
            'The dome-shaped upper region of the stomach',
        ],
        'Chyme from the stomach enters the duodenum, where bile and pancreatic enzymes continue digestion. The colon stores and compacts feces, the cystic duct carries bile toward the duodenum, and the gastric fundus is part of the stomach.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-027
    fact(
        'ccma-anatomy',
        'At which pelvic structure does the head of the femur articulate?',
        'Acetabulum of the hip joint',
        [
            'Glenoid fossa of the scapula',
            'Patellar surface of the distal femur at the knee',
            'Tibial plateau of the knee',
        ],
        'The acetabulum forms the socket of the ball-and-socket hip joint. The glenoid articulates with the humerus at the shoulder, the patella slides over the femur at the knee, and the tibial plateau receives the femoral condyles.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-028
    fact(
        'ccma-anatomy',
        'Which layer of the heart wall contains the contractile cardiac muscle that generates pump force?',
        'Myocardium',
        [
            'Endocardium',
            'Epicardium (visceral pericardium)',
            'Pericardial fluid',
        ],
        'Myocardial fibers contract to eject blood. The endocardium lines the chambers, the epicardium covers the outer surface, and pericardial fluid lubricates between serous layers rather than contracting.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-029
    fact(
        'ccma-anatomy',
        'What is the functional microscopic unit of the kidney responsible for filtration and urine formation?',
        'Nephron',
        [
            'Alveolus',
            'Neuron',
            'Osteon',
        ],
        'Each nephron includes a glomerulus, tubules, and collecting structures that process blood into urine. Alveoli exchange gases in the lungs, neurons transmit signals, and osteons are structural units of compact bone.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-030
    fact(
        'ccma-anatomy',
        'Which pancreatic cells secrete insulin into the bloodstream?',
        'Beta cells in the islets of Langerhans',
        [
            'Alpha cells in the islets of Langerhans',
            'Zona glomerulosa of the adrenal cortex',
            'Thyroid follicular cells',
        ],
        'Beta cells release insulin when blood glucose rises. Alpha cells secrete glucagon, adrenal cortical zones produce mineralocorticoids and glucocorticoids, and thyroid follicles release thyroid hormone.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-031
    fact(
        'ccma-anatomy',
        'Which homeostatic roles are chiefly performed by the kidneys?',
        'Fluid balance, electrolyte regulation, and waste excretion',
        [
            'Primary regulation of blood glucose via insulin release',
            'Initiation of each heartbeat at the sinoatrial node',
            'Production of bile for emulsification of dietary fat',
        ],
        'Nephrons filter plasma, reabsorb needed solutes and water, and excrete nitrogenous wastes while helping stabilize pH. Glucose, cardiac rhythm, and bile production involve the pancreas, SA node, and liver respectively.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-032
    fact(
        'ccma-anatomy',
        'Into which great vessel does the left ventricle eject oxygenated blood?',
        'Aorta',
        [
            'Pulmonary artery',
            'Superior vena cava',
            'Right atrium',
        ],
        'The aortic valve guards the outflow from the left ventricle into the systemic circulation. The pulmonary artery leaves the right ventricle, and the superior vena cava delivers venous blood to the right atrium.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-033
    fact(
        'ccma-anatomy',
        'What is the primary purpose of the meninges around the brain and spinal cord?',
        'Protect and support the central nervous system',
        [
            'Secrete cerebrospinal fluid from choroid plexus epithelium',
            'Line the inner surface of the heart chambers (endocardium)',
            'Conduct voluntary motor signals through peripheral nerves',
        ],
        'The dura mater, arachnoid mater, and pia mater encase the CNS and contribute to CSF compartments. CSF secretion, cardiac lining, and peripheral motor conduction are related anatomic functions but not the primary role of the meninges.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-034
    fact(
        'ccma-anatomy',
        'The mitral (bicuspid) valve lies between which two heart chambers?',
        'Left atrium and left ventricle',
        [
            'Right atrium and right ventricle',
            'Left ventricle and aorta',
            'Right ventricle and pulmonary artery',
        ],
        'The mitral valve prevents backflow from the left ventricle into the left atrium during systole. The tricuspid valve guards the right AV orifice, and semilunar valves separate ventricles from the pulmonary artery and aorta.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-035
    fact(
        'ccma-anatomy',
        'Which atrioventricular valve has two cusps and is found on the left side of the heart?',
        'Mitral (bicuspid) valve between the left atrium and left ventricle',
        [
            'Tricuspid valve between the right atrium and right ventricle',
            'Aortic semilunar valve at the left ventricular outflow',
            'Pulmonary semilunar valve at the right ventricular outflow',
        ],
        'Bicuspid refers to two leaflets on the left AV valve. The tricuspid valve has three cusps on the right, and semilunar valves lack chordae tendineae because they guard arterial outlets rather than atrioventricular openings.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-036
    fact(
        'ccma-anatomy',
        'Within the nephron, where does initial filtration of blood plasma occur?',
        "Glomerulus enclosed by Bowman's capsule",
        [
            'Descending limb of the loop of Henle',
            'Collecting duct in the renal medulla',
            'Ureter transporting urine to the bladder',
        ],
        'The renal corpuscle (glomerulus plus Bowman capsule) forms filtrate under hydrostatic pressure. The loop of Henle and collecting duct reabsorb and concentrate urine, and the ureter is an extrarenal transport tube.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-037
    fact(
        'ccma-anatomy',
        'The visceral and parietal pleura envelop which organ pair?',
        'Lungs',
        [
            'Heart within the pericardium',
            'Liver in the right upper abdomen',
            'Kidneys in the retroperitoneum',
        ],
        'Pleural membranes and a thin fluid layer reduce friction during ventilation. The pericardium surrounds the heart, and the liver and kidneys lie below the diaphragm without pleural investment.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-038
    fact(
        'ccma-anatomy',
        'The hepatic portal vein delivers blood from which source to the liver?',
        'Capillary beds of the digestive tract and associated organs',
        [
            'Oxygenated pulmonary veins from the lungs',
            'Renal pelvis draining urine toward the ureter',
            'Cerebral venous sinuses of the brain',
        ],
        'Portal blood is rich in absorbed nutrients and must be processed by hepatocytes before entering systemic circulation via hepatic veins. Pulmonary veins carry oxygenated blood to the left atrium, and urine and cerebral venous drainage use separate pathways.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-039
    fact(
        'ccma-anatomy',
        'Which structure normally initiates each heartbeat and sets intrinsic sinus rhythm?',
        'Sinoatrial (SA) node',
        [
            'Atrioventricular (AV) node in isolation',
            'Bundle of His without upstream input',
            'Purkinje fibers without prior depolarization',
        ],
        'The SA node fires first and spreads depolarization through atrial muscle; the AV node delays the impulse before it reaches the bundle branches and Purkinje network. Those downstream structures conduct rather than spontaneously pace under normal conditions.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-040
    fact(
        'ccma-anatomy',
        'Where is the thyroid gland located in the neck?',
        'Anterior neck, draping the trachea below the larynx',
        [
            'Posterior to the trachea at the level of the hyoid bone',
            'Superior to the thyroid cartilage in the submandibular space',
            'Lateral to the carotid sheath in the posterior triangle',
        ],
        'The thyroid isthmus crosses the trachea anteriorly. Posterior tracheal and carotid triangle positions are common landmarks confused on neck diagrams; the submandibular space lies above the thyroid cartilage.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-041
    fact(
        'ccma-anatomy',
        'The tricuspid valve separates which two chambers on the right side of the heart?',
        'Right atrium and right ventricle',
        [
            'Left atrium and left ventricle',
            'Right ventricle and pulmonary artery',
            'Left ventricle and aorta',
        ],
        'Three cusps guard the right atrioventricular opening. The mitral valve is on the left, and pulmonary and aortic semilunar valves lie at the outlets of the right and left ventricles respectively.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-042
    fact(
        'ccma-anatomy',
        'Which division of the autonomic nervous system predominates during rest and tends to slow heart rate?',
        'Parasympathetic (craniosacral) division',
        [
            'Sympathetic (thoracolumbar) division',
            'Somatic motor neurons to skeletal muscle',
            'Enteric nervous plexus regulating gut motility',
        ],
        'Vagal parasympathetic fibers release acetylcholine at the SA node to reduce rate. Sympathetic stimulation accelerates the heart, somatic motor neurons govern voluntary movement, and the enteric plexus regulates gut motility with modulatory autonomic input.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-043
    fact(
        'ccma-anatomy',
        'Primary processing of visual information occurs in which cerebral lobe?',
        'Occipital lobe',
        [
            'Frontal lobe',
            'Temporal lobe',
            'Cerebellum',
        ],
        'The primary visual cortex lies along the calcarine sulcus in the occipital region. The frontal lobe plans movement and executive function, the temporal lobe handles audition and memory, and the cerebellum coordinates motor precision and balance.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-044
    fact(
        'ccma-anatomy',
        'In which spaces does cerebrospinal fluid (CSF) circulate after leaving the ventricular system?',
        'Subarachnoid space around the brain and spinal cord (and within ventricles)',
        [
            'Epidural space between skull and dura',
            'Synovial cavities of diarthrodial joints',
            'Pericardial sac surrounding the heart',
        ],
        'CSF flows from the choroid plexus through ventricles into the subarachnoid space before reabsorption via arachnoid granulations. The epidural space is outside the dura, synovial fluid lubricates joints, and pericardial fluid cushions the heart.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-045
    fact(
        'ccma-anatomy',
        'What effect does pancreatic glucagon have on blood glucose concentration?',
        'Raises blood glucose by promoting glycogen breakdown and gluconeogenesis',
        [
            'Lowers blood glucose by increasing cellular uptake',
            'Increases urine volume by acting on renal tubules directly',
            'Slows heart rate through direct SA node inhibition',
        ],
        'Alpha cells release glucagon when glucose is low, opposing insulin. Insulin lowers glucose; diuretics, not glucagon, are typical agents for altering urine output, and heart rate is regulated chiefly by autonomic and pacemaker mechanisms.',
        [S.NHA_CCMA],
        'intermediate',
    ),

    # ccma-anatomy-046
    fact(
        'ccma-anatomy',
        'Which chamber of the heart receives oxygenated blood from the pulmonary veins?',
        'Left atrium',
        [
            'Right atrium receiving systemic venous blood',
            'Right ventricle pumping blood to the lungs',
            'Pulmonary artery carrying blood to the lungs',
        ],
        'Oxygenated blood returns from the lungs via pulmonary veins into the left atrium. The right atrium receives venous systemic blood, which is a frequent reversal error.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-047
    fact(
        'ccma-anatomy',
        'Where does gas exchange between air and blood occur in the respiratory system?',
        'Alveoli of the lungs',
        [
            'Larynx and vocal folds in the upper airway',
            'Mainstem bronchi in the conducting airways',
            'Pleural cavity between visceral and parietal pleura',
        ],
        'Alveoli provide the thin membrane needed for oxygen and carbon dioxide diffusion. Conducting airways move air but do not perform primary gas exchange.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-048
    fact(
        'ccma-anatomy',
        'A patient with right-sided heart failure may develop dependent edema because fluid backs up in which circulation?',
        'Systemic venous circulation',
        [
            'Pulmonary arterial circulation backing up into the lungs',
            'Coronary arterial circulation reducing myocardial perfusion',
            'Lymphatic return from the lungs into thoracic ducts',
        ],
        'Right heart failure increases venous hydrostatic pressure in the systemic veins, promoting peripheral edema. Pulmonary congestion is more typical of left-sided failure.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-anatomy-049
    fact(
        'ccma-anatomy',
        'Which blood vessel carries deoxygenated blood from the right ventricle to the lungs?',
        'Pulmonary artery',
        [
            'Pulmonary vein returning oxygenated blood to the left atrium',
            'Aorta carrying oxygenated blood to the systemic circulation',
            'Coronary sinus draining venous blood into the right atrium',
        ],
        'Pulmonary arteries carry low-oxygen blood to the lungs for gas exchange. Pulmonary veins return oxygenated blood, reversing the everyday meaning of artery versus vein.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-050
    fact(
        'ccma-anatomy',
        'What is the primary function of the nephron in the kidney?',
        'Filter blood and form urine while regulating electrolytes',
        [
            'Reabsorb filtrate and concentrate urine in renal tubules',
            'Secrete erythropoietin in response to low oxygen tension',
            'Regulate blood pressure via the renin-angiotensin pathway',
        ],
        'Nephrons filter plasma and adjust water and solute excretion. Tubular reabsorption, erythropoietin release, and renin secretion are renal functions but filtration and urine formation define the nephron\'s primary role.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-051
    fact(
        'ccma-anatomy',
        'Which structure prevents food from entering the trachea during swallowing?',
        'Epiglottis',
        [
            'Cricoid cartilage forming the lower laryngeal ring',
            'Arytenoid cartilages pivoting the vocal folds',
            'Soft palate elevating during swallow initiation',
        ],
        'The epiglottis covers the glottis during swallowing. Laryngeal cartilages support the airway, and the soft palate separates the nasopharynx from the oropharynx but does not block the trachea during swallow.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-052
    fact(
        'ccma-anatomy',
        'A patient with a spinal cord injury at the cervical level may lose voluntary control of which function first?',
        'Diaphragmatic breathing and limb movement',
        [
            'Isolated bladder retention with intact respiratory effort',
            'Distal lower-extremity reflexes with preserved arm strength',
            'Upper-extremity fine motor loss with intact leg movement',
        ],
        'High cervical lesions can impair phrenic nerve function and major motor pathways. Lower-level injuries may spare respiration while affecting bladder or distal reflexes differently than high tetraplegia.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-anatomy-053
    fact(
        'ccma-anatomy',
        'Which organ produces bile that is stored in the gallbladder?',
        'Liver',
        [
            'Pancreas secreting digestive enzymes and bicarbonate',
            'Gallbladder concentrating bile between meals',
            'Stomach secreting acid and intrinsic factor',
        ],
        'Hepatocytes secrete bile; the gallbladder stores and concentrates it. The pancreas and stomach contribute to digestion but do not synthesize bile.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-054
    fact(
        'ccma-anatomy',
        'What is the main function of hemoglobin in red blood cells?',
        'Bind and transport oxygen',
        [
            'Produce antibodies against specific antigens',
            'Aggregate at injury sites to initiate clotting',
            'Engulf bacteria by phagocytosis in tissues',
        ],
        'Hemoglobin carries oxygen from lungs to tissues. Platelets and white cells perform clotting and immune roles respectively.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-055
    fact(
        'ccma-anatomy',
        'Which valve separates the left atrium and left ventricle?',
        'Mitral (bicuspid) valve',
        [
            'Tricuspid valve between the right atrium and ventricle',
            'Pulmonic semilunar valve at the right ventricular outflow',
            'Aortic semilunar valve at the left ventricular outflow',
        ],
        'The mitral valve guards the left AV opening. Tricuspid is right-sided; pulmonic and aortic are semilunar valves leaving the ventricles.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-056
    fact(
        'ccma-anatomy',
        'Why may a patient with dehydration present with tachycardia and hypotension?',
        'Lower circulating volume reduces venous return and stroke volume',
        [
            'Peripheral vasodilation from excess circulating volume',
            'Compensatory bradycardia to conserve myocardial oxygen',
            'Hypertension from fluid overload in hypovolemia',
        ],
        'Hypovolemia decreases preload, triggering compensatory tachycardia while pressure falls. Vasodilation with volume excess, bradycardia, and hypertensive overload describe different hemodynamic states.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-anatomy-057
    fact(
        'ccma-anatomy',
        'Which structure connects the pharynx to the stomach?',
        'Esophagus',
        [
            'Trachea conducting air to the bronchi',
            'Ureter transporting urine to the bladder',
            'Eustachian tube linking middle ear and nasopharynx',
        ],
        'The esophagus carries swallowed food and liquid. The trachea is an airway; ureters transport urine.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-058
    fact(
        'ccma-anatomy',
        'What is the primary role of the sinoatrial node?',
        'Initiate normal electrical impulses for heart rhythm',
        [
            'Delay conduction at the atrioventricular (AV) node',
            'Spread depolarization through the bundle of His',
            'Distribute impulses via Purkinje fibers in the ventricles',
        ],
        'The SA node is the heart\'s intrinsic pacemaker. The AV node, bundle of His, and Purkinje fibers conduct the impulse but normally do not initiate sinus rhythm.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-059
    fact(
        'ccma-anatomy',
        'What is the main function of lymph nodes?',
        'Filter lymph and support immune responses',
        [
            'Return interstitial fluid directly into systemic veins',
            'Filter bloodborne pathogens in the splenic pulp',
            'Transport chyle from intestinal lacteals to the cisterna chyli',
        ],
        'Lymph nodes trap antigens and house immune cells. Lymphatics drain interstitial fluid into nodes; the spleen filters blood, and lacteals carry chyle before nodal filtration.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-060
    fact(
        'ccma-anatomy',
        'An elderly patient with chronic obstructive pulmonary disease sits upright and leans forward to breathe. Which muscle group is working harder to expand the thoracic cavity?',
        'Accessory muscles of respiration including sternocleidomastoid and scalenes',
        [
            'Diaphragm as the recruited muscle in forward-leaning tripod posture',
            'External intercostals raising ribs with no neck muscle effort',
            'Pectoralis major protraction as the main driver of tidal volume',
        ],
        'Tripod positioning recruits neck and chest accessory muscles when diaphragm effort is insufficient. In severe COPD exacerbation, sternocleidomastoid and scalenes augment a fatiguing diaphragm.',
        [S.NHA_CCMA],
        'advanced',
    ),
    # ccma-anatomy-061
    fact(
        'ccma-anatomy',
        'Where is cerebrospinal fluid primarily produced?',
        'Choroid plexus within the ventricles',
        [
            'Ependymal lining of the ventricular walls',
            'Arachnoid granulations reabsorbing CSF into venous sinuses',
            'Dural venous sinuses draining cerebral blood',
        ],
        'Choroid plexus epithelium secretes CSF into the ventricles. Ependyma lines ventricles, arachnoid granulations reabsorb CSF, and dural sinuses drain venous blood rather than producing CSF.',
        [S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-anatomy-062
    fact(
        'ccma-anatomy',
        'Which blood cell type is primarily responsible for hemostasis through plug formation?',
        'Platelets',
        [
            'Erythrocytes carrying oxygen via hemoglobin',
            'Lymphocytes mediating adaptive immune responses',
            'Basophils releasing histamine during allergic reactions',
        ],
        'Platelets aggregate at injury sites to start clotting. Red cells carry oxygen; lymphocytes mediate adaptive immunity.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-063
    fact(
        'ccma-anatomy',
        'What do hormones such as cortisol from the adrenal cortex help regulate?',
        'Metabolism and stress response',
        [
            'Mineralocorticoid-mediated sodium retention in the nephron',
            'Parathyroid hormone regulation of serum calcium',
            'Thyroid hormone control of basal metabolic rate',
        ],
        'Cortisol influences glucose metabolism and anti-inflammatory pathways. Aldosterone, parathyroid hormone, and thyroid hormone regulate electrolytes, calcium, and metabolic rate through distinct endocrine axes.',
        [S.NHA_CCMA],
        'beginner',
    ),
    # ccma-anatomy-064
    fact(
        'ccma-anatomy',
        'A patient with left-sided weakness and slurred speech is suspected of acute stroke. Which anatomic system is primarily affected?',
        'Central nervous system',
        [
            'Peripheral nervous system with nerve root compression',
            'Neuromuscular junction failure at the motor end plate',
            'Musculoskeletal strain of the shoulder girdle',
        ],
        'Focal neuro deficits suggest brain or brainstem involvement. Peripheral nerve injury, neuromuscular junction disorders, or isolated musculoskeletal pain do not typically produce sudden unilateral weakness with dysarthria.',
        [S.NHA_CCMA],
        'advanced',
    ),
]
