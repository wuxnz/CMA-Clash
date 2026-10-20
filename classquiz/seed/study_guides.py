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
}
