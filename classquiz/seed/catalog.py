# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.seed.study_guides import STUDY_BY_TOPIC

CERTIFICATIONS = [
    {
        "slug": "ccma",
        "name": "NHA CCMA",
        "description": "Certified Clinical Medical Assistant (NHA CCMA) exam preparation aligned to the current test plan.",
        "sort_order": 1,
        "topics": [
            ("ccma-foundational", "Foundational Knowledge & Basic Science", 1),
            ("ccma-anatomy", "Anatomy & Physiology", 2),
            ("ccma-clinical-care", "Clinical Patient Care", 3),
            ("ccma-coordination", "Patient Care Coordination & Education", 4),
            ("ccma-admin", "Administrative Assistance", 5),
            ("ccma-communication", "Communication & Customer Service", 6),
            ("ccma-law-ethics", "Medical Law & Ethics", 7),
            ("ccma-vaccines", "Vaccine Administration & Storage", 8),
            ("ccma-hipaa", "HIPAA & Patient Privacy", 9),
            ("ccma-transmission", "Transmission-Based Precautions", 10),
            ("ccma-diabetes", "Diabetes", 11),  # 112 facts → four 28-question quiz sets
            ("diabetes-study-guide", "Diabetes Study Guide", 12),
        ],
    },
    {
        "slug": "ekg",
        "name": "EKG Technician",
        "description": "Electrocardiography: lead placement, rhythm interpretation, intervals, artifacts, and cardiac anatomy.",
        "sort_order": 2,
        "topics": [
            ("ekg-leads", "Lead Placement & Basics", 1),
            ("ekg-rhythm", "Rhythm Recognition", 2),
            ("ekg-intervals", "Intervals & Axis", 3),
            ("ekg-artifacts", "Artifacts & Troubleshooting", 4),
            ("ekg-cardiac-ap", "Cardiac Anatomy & Physiology", 5),
            ("ekg-acls-basics", "ACLS-Related CPR Metrics", 6),
        ],
    },
    {
        "slug": "phlebotomy",
        "name": "Phlebotomy",
        "description": "Venipuncture and specimen collection per CLSI and safety standards.",
        "sort_order": 3,
        "topics": [
            ("phleb-order-draw", "Order of Draw", 1),
            ("phleb-additives", "Tube Additives & Tests", 2),
            ("phleb-site", "Site Selection & Technique", 3),
            ("phleb-handling", "Specimen Handling & Processing", 4),
            ("phleb-complications", "Complications", 5),
            ("phleb-safety", "Safety & Infection Control", 6),
            ("phleb-who", "WHO Phlebotomy Safety", 7),
            ("phleb-glucose", "Blood Glucose & POC Testing", 8),
        ],
    },
    {
        "slug": "cpr-bls",
        "name": "CPR / BLS",
        "description": "Basic life support per current AHA guidelines.",
        "sort_order": 4,
        "topics": [
            ("cpr-adult", "Adult BLS", 1),
            ("cpr-child", "Child BLS", 2),
            ("cpr-infant", "Infant BLS", 3),
            ("cpr-aed", "AED Use", 4),
            ("cpr-choking", "Choking Emergencies", 5),
            ("cpr-chain", "Chain of Survival", 6),
            ("cpr-red-cross", "First Aid & CPR Resources", 7),
        ],
    },
    {
        "slug": "clinical-skills",
        "name": "Clinical Skills",
        "description": "Cross-cutting medical assisting competencies.",
        "sort_order": 5,
        "topics": [
            ("skill-injection", "Injection Therapy", 1),
            ("skill-vitals", "Vital Signs & Blood Pressure", 2),
            ("skill-infection", "Infection Control & Asepsis", 3),
            ("skill-terminology", "Medical Terminology", 4),
            ("skill-pharm-dosage", "Pharmacology & Dosage Calculation", 5),
            ("skill-specimen-lab", "Specimen Collection & Lab Procedures", 6),
            ("skill-intake", "Patient Intake & Documentation", 7),
            ("skill-osha-bbp", "OSHA Bloodborne Pathogens", 8),
            ("skill-med-safety", "Medication Safety", 9),
            ("skill-poct", "Point-of-Care Testing", 10),
            ("skill-wound-care", "Wound Care & Dressings", 11),
            ("skill-life-stages", "Pediatric & Geriatric Considerations", 12),
            ("skill-emergency-aid", "Emergency & First Aid Basics", 13),
        ],
    },
]

# Questions per public quiz for topics that need more than the default chunk size.
TOPIC_QUESTIONS_PER_QUIZ: dict[str, int] = {
    "ccma-diabetes": 28,
}


def study_content_for_topic(slug: str) -> list[dict] | None:
    return STUDY_BY_TOPIC.get(slug)
