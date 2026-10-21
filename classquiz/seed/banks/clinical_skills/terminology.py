# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-terminology)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # skill-terminology-001
    fact(
        "skill-terminology",
        "What does the prefix hyper- mean in a medical term such as hypertension?",
        "Above normal or excessive",
        [
            "Below normal or deficient",
            "Painful, difficult, or abnormal",
            "Within or inside",
        ],
        "Hyper- signals increase, as in high blood pressure. Hypo- means low, dys- means abnormal, and intra- means inside.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-002
    fact(
        "skill-terminology",
        "What does the prefix hypo- mean in a term such as hypoglycemia?",
        "Below normal or deficient",
        [
            "Fast or rapid",
            "Many or much",
            "Above normal or excessive",
        ],
        "Hypo- indicates decrease, such as low blood glucose. Hyper- is the opposite direction, while tachy- and poly- describe rate and number.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-003
    fact(
        "skill-terminology",
        "What does the prefix brady- indicate in bradycardia?",
        "Slow or decreased rate",
        [
            "Fast or rapid rate",
            "Painful or difficult",
            "Enlarged or excessive size",
        ],
        "Brady- refers to slowness of the heart rate. Tachy- means fast, dys- can mean painful or abnormal, and -megaly describes enlargement rather than speed.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-004
    fact(
        "skill-terminology",
        "What does the prefix tachy- mean in tachypnea?",
        "Fast or rapid",
        [
            "Slow or decreased rate",
            "Without or absent",
            "Half or partial division",
        ],
        "Tachy- describes increased rate of breathing or pulse. Brady- is slow, a- can mean without, and hemi- means half.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-005
    fact(
        "skill-terminology",
        "What does the prefix dys- mean in dyspnea?",
        "Painful, difficult, or abnormal",
        [
            "Good or normal physiologic function",
            "Many or much increased in amount",
            "Above normal or excessive in degree",
        ],
        "Dyspnea is difficult breathing. Eu- can mean good or normal, poly- means many, and hyper- means above normal.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-006
    fact(
        "skill-terminology",
        "What does the prefix poly- mean in polyuria?",
        "Many or much",
        [
            "One or single",
            "Without or absent",
            "Below normal or deficient",
        ],
        "Polyuria is excessive urination volume or frequency. Mono- relates to one, a- can mean without, and hypo- means below.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-007
    fact(
        "skill-terminology",
        "What does the prefix intra- mean in intramuscular?",
        "Within or inside",
        [
            "Between two structures",
            "Around a structure",
            "Outside the body or organ",
        ],
        "Intramuscular injections go inside muscle tissue. Inter- means between structures, peri- means around, and extra- means outside.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-008
    fact(
        "skill-terminology",
        "What does the prefix sub- mean in subcutaneous?",
        "Under or below",
        [
            "Above or over",
            "Within or inside",
            "Across or through",
        ],
        "Subcutaneous tissue lies under the skin. Supra- means above, intra- means within, and trans- means across or through.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-009
    fact(
        "skill-terminology",
        "What does the prefix peri- mean in pericardium?",
        "Around or surrounding",
        [
            "Within or inside a cavity",
            "Under or below a structure",
            "Across or through a wall",
        ],
        "The pericardium surrounds the heart. Intra- is within, sub- is under, and trans- crosses through a structure.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-010
    fact(
        "skill-terminology",
        "What does the suffix -itis mean in dermatitis?",
        "Inflammation of tissue",
        [
            "Surgical removal of tissue",
            "Enlargement of tissue",
            "Study of tissue or a field",
        ],
        "Dermatitis is inflamed skin. -ectomy means removal, -megaly means enlargement, and -ology means study of a subject.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-011
    fact(
        "skill-terminology",
        "What does the suffix -ectomy indicate in appendectomy?",
        "Surgical removal",
        [
            "Inflammation of tissue",
            "Tumor or new growth",
            "Blood or blood condition",
        ],
        "Appendectomy removes the appendix. -itis is inflammation, -oma often indicates tumor, and -emia relates to blood.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-012
    fact(
        "skill-terminology",
        "What does the suffix -ology mean in cardiology?",
        "Study of a body system or field",
        [
            "Surgical repair of a body structure",
            "Pain related to a nerve or tissue",
            "Incision into a hollow organ",
        ],
        "Cardiology is the study and medical care of the heart. -plasty means surgical repair, -algia means pain, and -otomy means cutting into.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-013
    fact(
        "skill-terminology",
        "What does the suffix -megaly mean in hepatomegaly?",
        "Enlargement",
        [
            "Reduction or small size",
            "Inflammation of tissue",
            "Surgical fixation",
        ],
        "Hepatomegaly is an enlarged liver. Micro- or -cyte relate to small cells, -itis is inflammation, and -pexy means surgical fixation.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-014
    fact(
        "skill-terminology",
        "What body structure does the combining form cardi/o refer to?",
        "Heart",
        [
            "Liver",
            "Kidney",
            "Skin",
        ],
        "Cardi/o appears in terms such as electrocardiogram. Hepat/o is liver, ren/o or nephr/o is kidney, and dermat/o is skin.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-015
    fact(
        "skill-terminology",
        "What does the combining form dermat/o refer to?",
        "Skin",
        [
            "Bone",
            "Muscle",
            "Nerve",
        ],
        "Dermatology focuses on skin conditions. Oste/o is bone, my/o is muscle, and neur/o is nerve.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-016
    fact(
        "skill-terminology",
        "What structure does oste/o describe in osteoporosis?",
        "Bone",
        [
            "Blood vessel",
            "Lung",
            "Gland",
        ],
        "Osteoporosis involves porous bone. Angi/o relates to vessels, pulmon/o to lungs, and aden/o to glands.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-017
    fact(
        "skill-terminology",
        "What does the combining form gastr/o refer to?",
        "Stomach",
        [
            "Intestine",
            "Gallbladder",
            "Pancreas",
        ],
        "Gastritis affects the stomach lining. Enter/o is intestine, cholecyst/o is gallbladder, and pancreat/o is pancreas.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-018
    fact(
        "skill-terminology",
        "What does the abbreviation NPO mean on a preprocedure order?",
        "Nothing by mouth",
        [
            "Normal pressure oxygen therapy",
            "Night postoperative observation rounds",
            "New patient orientation visit",
        ],
        "NPO restricts oral intake before sedation or surgery. The other phrases sound clinical but do not match the Latin nil per os meaning.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-019
    fact(
        "skill-terminology",
        "What does PRN on a medication order indicate?",
        "As needed for symptoms or indication",
        [
            "Every morning at a fixed time",
            "Before each meal on a standard schedule",
            "At bedtime once each night",
        ],
        "PRN dosing depends on symptoms or indication. QAM is morning, AC is before meals, and HS is at bedtime in many facilities.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-terminology-020
    fact(
        "skill-terminology",
        "What does BID mean for a prescribed medication schedule?",
        "Twice daily",
        [
            "Once daily",
            "Four times daily",
            "Every hour around the clock",
        ],
        "BID comes from bis in die. QD is once daily, QID is four times daily, and q1h means every hour.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-terminology-021
    fact(
        "skill-terminology",
        "What does TID indicate for medication timing?",
        "Three times daily",
        [
            "Twice daily on a fixed schedule",
            "Once at bedtime each night",
            "As needed without a fixed schedule",
        ],
        "TID is ter in die, meaning three times daily. BID is twice daily, HS is at bedtime, and PRN is as needed.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-022
    fact(
        "skill-terminology",
        "What does the abbreviation HS commonly mean on a medication order?",
        "At bedtime",
        [
            "Before meals on a standard schedule",
            "At half the ordered drug concentration",
            "With a hot saline soak treatment",
        ],
        "HS often signals hour of sleep dosing. AC is before meals, half strength would be written explicitly, and soak orders use different wording.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-023
    fact(
        "skill-terminology",
        "What does STAT mean when a provider orders a lab or medication?",
        "Immediately",
        [
            "At the next routine clinic visit",
            "When the patient verbally requests it",
            "After three prior routine scheduled doses",
        ],
        "STAT signals urgent action. Delayed or conditional timing would be written with different frequency terms.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-024
    fact(
        "skill-terminology",
        "In documentation, what does SOB usually stand for?",
        "Shortness of breath",
        [
            "Systolic output balance measurement",
            "Soft outer bandage application",
            "Standing on both feet positioning",
        ],
        "SOB is a common symptom abbreviation in charts. The other expansions are not standard clinical shorthand for breathing difficulty.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-025
    fact(
        "skill-terminology",
        "What directional term describes a structure closer to the head than another structure?",
        "Superior (toward the head)",
        [
            "Inferior (toward the feet)",
            "Posterior (toward the back)",
            "Distal (farther from the trunk on a limb)",
        ],
        "Superior means toward the head. Inferior is below, posterior is toward the back, and distal is farther from the trunk on a limb.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-026
    fact(
        "skill-terminology",
        "What directional term means toward the front of the body?",
        "Anterior (toward the front)",
        [
            "Posterior (toward the back)",
            "Medial (toward the midline)",
            "Proximal (closer to the trunk on a limb)",
        ],
        "Anterior is front-facing anatomy. Posterior is back, medial is toward midline, and proximal is closer to the trunk on a limb.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-027
    fact(
        "skill-terminology",
        "On the forearm, which term describes the wrist compared with the elbow?",
        "Distal to the elbow on the same limb",
        [
            "Proximal to the elbow on the same limb",
            "Superior to the shoulder on the torso",
            "Medial to the spinal midline",
        ],
        "Distal means farther from the point of attachment on a limb. The wrist is distal to the elbow, not proximal.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-028
    fact(
        "skill-terminology",
        "What does medial describe in relation to the midline of the body?",
        "Closer to the midline",
        [
            "Farther from the midline on the same plane",
            "Toward the caudal tailbone end",
            "Lateral on the outer body surface",
        ],
        "Medial structures lie nearer the center, such as the big toe side of the foot relative to the little toe. Lateral is away from midline.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-029
    fact(
        "skill-terminology",
        "What does the suffix -algia mean in neuralgia?",
        "Pain related to the root structure",
        [
            "Inflammation of the root structure",
            "Enlargement of the root structure",
            "Record or image of the root structure",
        ],
        "Neuralgia is nerve pain. -itis is inflammation, -megaly is enlargement, and -gram refers to a recording or image.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # skill-terminology-030
    fact(
        "skill-terminology",
        "What does the suffix -emia indicate in a term such as anemia?",
        "Blood condition related to the root word",
        [
            "Urine condition related to the root word",
            "Surgical incision into the root structure",
            "Pregnancy count related to the root word",
        ],
        "Anemia and leukocytosis involve blood cells. -uria relates to urine, -otomy is cutting, and -gravida relates to pregnancy count.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # skill-terminology-031
    fact(
        "skill-terminology",
        "A chart lists cholelithiasis. Which plain-language description best matches the term?",
        "Gallstones in the gallbladder",
        [
            "Inflammation of the stomach lining",
            "Enlarged spleen from chronic infection",
            "Slow heart rate from beta-blocker therapy",
        ],
        "Chole- refers to bile or gallbladder and -lithiasis means stone condition. Gastritis, splenomegaly, and bradycardia use different roots.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-032
    fact(
        "skill-terminology",
        "A provider orders a CBC. What is the medical assistant preparing the patient to provide?",
        "Venous or capillary blood for a complete blood count",
        [
            "Clean-catch midstream urine specimen for urine culture",
            "Stool sample for occult blood testing in the laboratory",
            "Sputum specimen for acid-fast bacillus stain testing",
        ],
        "CBC analyzes blood cells and indices. Urine, stool, and sputum tests use different containers and patient instructions.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-033
    fact(
        "skill-terminology",
        "An order reads BMP. Which analyte group is typically included in this panel?",
        "Sodium, potassium, glucose, and creatinine chemistries",
        [
            "HDL, LDL, triglycerides, and fasting lipid panel fractions",
            "TSH, free T4, and thyroid hormone panel measurements",
            "Troponin, CK-MB, and acute cardiac enzyme panel markers",
        ],
        "BMP is a common electrolyte and renal function screen. Lipid, thyroid, and troponin studies are separate ordered panels.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-034
    fact(
        "skill-terminology",
        "A patient asks what hypertension means after seeing it on the intake form. What is the clearest explanation?",
        "Persistently elevated blood pressure",
        [
            "Persistently low blood pressure from volume loss",
            "Abnormally rapid breathing at rest",
            "Progressive bone density loss from calcium deficit",
        ],
        "Hyper- plus tension (pressure) describes high blood pressure. Hypoglycemia, tachypnea, and osteoporosis involve different roots and organs.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-035
    fact(
        "skill-terminology",
        "Documentation states the injection was given in the left deltoid. Which anatomical description is correct?",
        "Left deltoid on the upper arm shoulder",
        [
            "Left gluteal on the posterior hip",
            "Left vastus lateralis on the anterior thigh",
            "Left rectus on the anterior abdomen",
        ],
        "Deltoid is the shoulder muscle used for many vaccines. Gluteal, thigh, and abdominal sites are different landmarks.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-036
    fact(
        "skill-terminology",
        "A surgical schedule lists laparoscopic cholecystectomy. What procedure is planned?",
        "Minimally invasive removal of the gallbladder",
        [
            "Minimally invasive repair of an inguinal hernia",
            "Minimally invasive removal of the appendix",
            "Open replacement of a diseased hip joint",
        ],
        "Laparoscopic describes abdominal scope surgery, cholecyst/o is gallbladder, and -ectomy is removal. Hernia repair, appendectomy, and arthroplasty are different operations.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-037
    fact(
        "skill-terminology",
        "A lab result comment says hematuria. What finding does the term describe?",
        "Blood in the urine",
        [
            "Low red blood cell count on a CBC",
            "Elevated white blood cell count on a CBC",
            "Protein in the urine without red cells",
        ],
        "Hematuria combines hem/o (blood) and -uria (urine condition). Anemia and leukocytosis are blood count issues, and proteinuria is a separate urine finding.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-038
    fact(
        "skill-terminology",
        "A prescription shows acetaminophen 650 mg PO q6h PRN pain. How should the medical assistant explain the route and timing to the patient?",
        "By mouth every six hours as needed for pain",
        [
            "By injection every six hours regardless of symptoms",
            "By mouth once each morning before breakfast",
            "Applied to the skin at bedtime every night",
        ],
        "PO is per os (by mouth), q6h is every six hours, and PRN limits doses to when pain occurs. IM, QAM, and topical bedtime schedules misread parts of the sig.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-terminology-039
    fact(
        "skill-terminology",
        "An EHR problem list includes GERD. Which condition does the abbreviation represent?",
        "Gastroesophageal reflux disease",
        [
            "Gastric erosive reflux disorder",
            "Gallbladder ejection reflux disorder",
            "Glucose elevation renal disorder",
        ],
        "GERD is chronic acid reflux. The near-miss expansions reuse gastro, gallbladder, and renal wording but do not match the accepted abbreviation.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-040
    fact(
        "skill-terminology",
        "A radiology report mentions a fracture of the distal radius. Where is the injury located?",
        "Forearm bone near the wrist on the thumb side",
        [
            "Upper arm bone near the shoulder joint",
            "Hip socket on the lateral pelvis",
            "Shin bone near the knee on the anteromedial leg",
        ],
        "The radius is the lateral forearm bone, and distal refers to the wrist end. Humerus, acetabulum, and tibia are different anatomic sites.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-041
    fact(
        "skill-terminology",
        "A patient has bilateral otitis media on the chart. What does bilateral indicate about the infection?",
        "Both ears are affected",
        [
            "Both lungs are affected",
            "Both kidneys are affected",
            "Both knees are affected",
        ],
        "Bilateral means both sides of a paired structure. Otitis media is middle ear infection, so both ears are involved rather than lungs, kidneys, or knees.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # skill-terminology-042
    fact(
        "skill-terminology",
        "A note documents cyanosis of the lips. Which clinical finding best matches the term?",
        "Bluish color from low blood oxygen",
        [
            "Yellow color from high blood bilirubin",
            "Pale color from sudden blood loss",
            "Red color from allergic skin contact",
        ],
        "Cyan/o refers to blue color often seen with hypoxia. Jaundice is yellow, pallor is pale, and erythema is red inflammation.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
