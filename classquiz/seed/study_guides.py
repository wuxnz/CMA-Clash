# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Short study summaries with authoritative links, keyed by topic slug."""

from classquiz.seed.sources import (
    AHA_ADULT_BLS,
    AHA_WHAT_IS_CPR,
    CDC_HAND_HYGIENE,
    CDC_INJECTION_SAFETY,
    CDC_ISOLATION_2007,
    CDC_STANDARD_PRECAUTIONS,
    CDC_VACCINE_ADMIN,
    CDC_VACCINE_STORAGE,
    CDC_HBP,
    CLSI_GP41,
    FDA_MEDICATION_SAFETY,
    HHS_HIPAA_PRIVACY,
    HHS_HIPAA_SECURITY,
    MEDLINEPLUS_HAND_HYGIENE,
    NHA_CCMA,
    OSHA_BBP,
    RED_CROSS_FIRST_AID,
    WHO_INJECTION_SAFETY,
    ADA_STANDARDS,
    ADA_DIAGNOSIS,
    CDC_DIABETES,
    CDC_DIABETES_BASICS,
    FDA_CLIA_WAIVED,
    MEDLINEPLUS_DIABETES,
)

# Each entry: title, summary, url (parsed from cite strings' URL portion)
def _blocks(*cites: str, summary: str) -> list[dict]:
    out = []
    for cite in cites:
        name, url = cite.split(" — ", 1)
        out.append({"title": name, "summary": summary, "url": url})
    return out


STUDY_BY_TOPIC: dict[str, list[dict]] = {
    "skill-infection": _blocks(
        CDC_STANDARD_PRECAUTIONS,
        CDC_HAND_HYGIENE,
        CDC_INJECTION_SAFETY,
        summary="Use Standard Precautions for all patients; perform hand hygiene before and after patient contact and before aseptic tasks. Follow safe injection practices: one needle, one syringe, only one time.",
    ),
    "ccma-clinical-care": _blocks(
        CDC_INJECTION_SAFETY,
        CDC_VACCINE_ADMIN,
        NHA_CCMA,
        summary="Clinical medical assistants support hands-on patient care within scope—vital signs, preparations, and injections—using CDC infection prevention and facility protocols.",
    ),
    "ccma-law-ethics": _blocks(
        HHS_HIPAA_PRIVACY,
        HHS_HIPAA_SECURITY,
        OSHA_BBP,
        summary="Protect patient privacy and PHI under HIPAA; follow OSHA requirements when exposure to blood or body fluids is reasonably anticipated.",
    ),
    "ccma-vaccines": _blocks(
        CDC_VACCINE_STORAGE,
        CDC_VACCINE_ADMIN,
        summary="Maintain vaccine cold chain per CDC toolkit; screen patients, use correct needle/site, and document lot and route per immunization program rules.",
    ),
    "ccma-hipaa": _blocks(
        HHS_HIPAA_PRIVACY,
        summary="The Privacy Rule limits uses and disclosures of PHI, requires safeguards, and grants patients rights to access and amend their records.",
    ),
    "ccma-transmission": _blocks(
        CDC_ISOLATION_2007,
        CDC_STANDARD_PRECAUTIONS,
        summary="Add Transmission-Based Precautions (contact, droplet, airborne) when Standard Precautions are not enough for a suspected or confirmed infection.",
    ),
    "skill-osha-bbp": _blocks(
        OSHA_BBP,
        summary="Covered employers need an Exposure Control Plan, engineering/work practice controls, HBV vaccination offer, training, and post-exposure follow-up.",
    ),
    "skill-vitals": _blocks(
        CDC_HBP,
        NHA_CCMA,
        summary="Use the correct cuff size, support the arm at heart level, have the patient rest, and document findings consistently.",
    ),
    "cpr-adult": _blocks(
        AHA_WHAT_IS_CPR,
        AHA_ADULT_BLS,
        summary="Adult BLS: push hard and fast (100–120/min), depth at least 2 inches (5 cm) without excessive depth, minimize pauses, and use 30:2 if no advanced airway.",
    ),
    "phleb-order-draw": _blocks(
        CLSI_GP41,
        WHO_INJECTION_SAFETY,
        summary="Follow CLSI order of draw to avoid additive cross-contamination; use aseptic technique and safe sharps handling.",
    ),
    "phleb-safety": _blocks(
        CDC_INJECTION_SAFETY,
        WHO_INJECTION_SAFETY,
        CLSI_GP41,
        summary="Treat all blood and sharps as potentially infectious; never reuse devices; select appropriate venipuncture sites.",
    ),
    "skill-med-safety": _blocks(
        FDA_MEDICATION_SAFETY,
        NHA_CCMA,
        summary="Verify the rights of medication administration, follow high-alert protocols, and report errors per facility policy.",
    ),
    "skill-emergency-aid": _blocks(
        AHA_WHAT_IS_CPR,
        RED_CROSS_FIRST_AID,
        summary="Recognize emergencies, call for help, provide BLS when indicated, and use first aid for bleeding and other immediate threats while awaiting EMS.",
    ),
    "skill-wound-care": _blocks(
        CDC_STANDARD_PRECAUTIONS,
        MEDLINEPLUS_HAND_HYGIENE,
        summary="Use clean or sterile technique per wound type; protect yourself with appropriate PPE and hand hygiene.",
    ),
    "ccma-diabetes": [
        {
            "title": "Types of diabetes",
            "summary": "Type 1 is autoimmune beta-cell destruction with insulin deficiency. Type 2 combines insulin resistance with declining insulin secretion. Gestational diabetes is first recognized in pregnancy. Prediabetes is a warning range on A1C, fasting glucose, or OGTT before diabetes thresholds are met.",
            "url": CDC_DIABETES_BASICS.split(" — ", 1)[1],
        },
        {
            "title": "Signs, symptoms, and pathophysiology",
            "summary": "Hyperglycemia may cause polyuria, polydipsia, fatigue, and blurred vision. Insulin deficiency or resistance raises blood glucose; without treatment, chronic elevation damages microvascular and macrovascular tissues.",
            "url": MEDLINEPLUS_DIABETES.split(" — ", 1)[1],
        },
        {
            "title": "Hypoglycemia and hyperglycemia emergencies",
            "summary": "Treat hypoglycemia below about 70 mg/dL with 15 grams of fast carbohydrate and recheck in about 15 minutes. DKA features hyperglycemia, ketosis, and acidosis. HHS features extreme hyperglycemia and dehydration with minimal ketosis. Both need urgent medical care.",
            "url": ADA_STANDARDS.split(" — ", 1)[1],
        },
        {
            "title": "Laboratory diagnosis (FPG, OGTT, A1C)",
            "summary": "Diabetes: FPG 126 mg/dL or higher; 2-hour OGTT 200 mg/dL or higher; A1C 6.5% or higher on a standardized assay. Prediabetes: FPG 100 to 125 mg/dL; 2-hour OGTT 140 to 199 mg/dL; A1C 5.7% to 6.4%. Confirm abnormal results per ADA unless classic symptoms and hyperglycemia are present.",
            "url": ADA_DIAGNOSIS.split(" — ", 1)[1],
        },
        {
            "title": "Point-of-care glucose testing",
            "summary": "Use hand hygiene, gloves, site prep, and patient identification. Many clinic meters are CLIA-waived when staff follow manufacturer instructions, run control solution on schedule, and document results. Report critical values per policy.",
            "url": FDA_CLIA_WAIVED.split(" — ", 1)[1],
        },
        {
            "title": "Insulin types and safe handling",
            "summary": "Rapid analogs act within about 15 minutes; regular insulin peaks around 2 to 3 hours; NPH is intermediate; glargine and similar agents provide basal coverage. Store unopened insulin refrigerated when required; in-use pens or vials per label. Never use cloudy or expired insulin.",
            "url": ADA_STANDARDS.split(" — ", 1)[1],
        },
        {
            "title": "Oral and injectable non-insulin agents",
            "summary": "Metformin lowers hepatic glucose output. Sulfonylureas stimulate insulin release and can cause hypoglycemia. SGLT2 inhibitors increase urinary glucose loss. DPP-4 inhibitors prolong incretin activity. GLP-1 agonists slow gastric emptying and enhance glucose-dependent insulin secretion.",
            "url": ADA_STANDARDS.split(" — ", 1)[1],
        },
        {
            "title": "Complications, foot care, and patient education",
            "summary": "Screen for retinopathy, neuropathy, and nephropathy per plan. Teach daily foot checks, proper footwear, and prompt reporting of wounds. Review carbohydrate awareness, sick-day rules, medical ID, and when to call the clinic or EMS.",
            "url": CDC_DIABETES.split(" — ", 1)[1],
        },
        {
            "title": "Medical assistant scope and documentation",
            "summary": "Perform POC testing, vitals, patient teaching, and injections only within state law and delegation. Document glucose values, symptoms, treatments, and patient response. Do not change insulin doses without an order unless explicitly delegated.",
            "url": NHA_CCMA.split(" — ", 1)[1],
        },
    ],
    "phleb-glucose": _blocks(
        CLSI_GP41,
        FDA_CLIA_WAIVED,
        CDC_DIABETES,
        summary="Collect glucose specimens with correct tubes, order of draw, and timing for OGTT. Run waived meter controls, use single-use lancets, and transport samples to limit glycolysis.",
    ),
}
