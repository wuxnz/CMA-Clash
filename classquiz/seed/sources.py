# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Authoritative source URLs used in seed references (verified for this content expansion)."""

from __future__ import annotations


def cite(name: str, url: str) -> str:
    return f"{name} — {url}"


# CDC infection control & injection safety
CDC_HAND_HYGIENE = cite(
    "CDC: Guideline for Hand Hygiene in Health Care Settings",
    "https://www.cdc.gov/infection-control/hcp/hand-hygiene/index.html",
)
CDC_STANDARD_PRECAUTIONS = cite(
    "CDC: Infection Control in Healthcare Settings (overview)",
    "https://www.cdc.gov/infection-control/hcp/index.html",
)
CDC_ISOLATION_2007 = cite(
    "CDC/HICPAC: Guideline for Isolation Precautions (2007)",
    "https://www.cdc.gov/infection-control/hcp/isolation-precautions/index.html",
)
CDC_INJECTION_SAFETY = cite(
    "CDC: Preventing Unsafe Injection Practices",
    "https://www.cdc.gov/injection-safety/hcp/clinical-safety/",
)
CDC_ONE_AND_ONLY = cite(
    "CDC NPIN: One & Only Campaign",
    "https://npin.cdc.gov/campaign/one-only-campaign",
)
CDC_VACCINE_STORAGE = cite(
    "CDC: Vaccine Storage and Handling Toolkit",
    "https://www.cdc.gov/vaccines/hcp/admin/storage/toolkit/index.html",
)
CDC_VACCINE_ADMIN = cite(
    "CDC: Vaccine Administration",
    "https://www.cdc.gov/vaccines/hcp/admin/index.html",
)

# OSHA
OSHA_BBP = cite(
    "OSHA: Bloodborne Pathogens Standard (29 CFR 1910.1030)",
    "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030",
)
OSHA_NEEDLESTICK = cite(
    "OSHA: Safety and Health Topics — Needlestick Injuries",
    "https://www.osha.gov/needlestick",
)

# AHA CPR / ECC
AHA_WHAT_IS_CPR = cite(
    "American Heart Association: What is CPR",
    "https://cpr.heart.org/en/resources/what-is-cpr",
)
AHA_ADULT_BLS = cite(
    "American Heart Association: Adult Basic Life Support Guidelines",
    "https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support",
)
AHA_HQ_CPR = cite(
    "American Heart Association: High-Quality CPR",
    "https://cpr.heart.org/en/resuscitation-science/high-quality-cpr",
)

# HHS / HIPAA
HHS_HIPAA_PRIVACY = cite(
    "HHS: HIPAA Privacy Rule",
    "https://www.hhs.gov/hipaa/for-professionals/privacy/index.html",
)
HHS_HIPAA_SECURITY = cite(
    "HHS: HIPAA Security Rule",
    "https://www.hhs.gov/hipaa/for-professionals/security/index.html",
)

# NIH / MedlinePlus
MEDLINEPLUS_HAND_HYGIENE = cite(
    "MedlinePlus: Hand-washing",
    "https://medlineplus.gov/ency/article/007425.htm",
)

# FDA
FDA_MEDICATION_SAFETY = cite(
    "FDA: Medication Safety Program",
    "https://www.fda.gov/drugs/medication-safety-program",
)

# WHO
WHO_INJECTION_SAFETY = cite(
    "WHO: Injection safety",
    "https://www.who.int/teams/integrated-health-services/infection-prevention-control/injection-safety",
)

# NHA (test plans — public certification pages)
NHA_CCMA = cite(
    "NHA: CCMA certification",
    "https://www.nhanow.com/certifications/ccma",
)
NHA_CET = cite(
    "NHA: CET certification",
    "https://www.nhanow.com/certifications/cet",
)
NHA_CPT = cite(
    "NHA: CPT certification",
    "https://www.nhanow.com/certifications/cpt",
)

# CLSI / phlebotomy (public CLSI shop page for GP41)
CLSI_GP41 = cite(
    "CLSI: GP41 Collection of Diagnostic Venous Blood Specimens",
    "https://clsi.org/standards/products/general-laboratory-and-infection-control/documents/gp41/",
)

# Red Cross (first aid reference)
RED_CROSS_FIRST_AID = cite(
    "American Red Cross: First Aid",
    "https://www.redcross.org/take-a-class/first-aid",
)

# AHA/ACC blood pressure (public health guidance)
CDC_HBP = cite(
    "CDC: Measuring Blood Pressure",
    "https://www.cdc.gov/high-blood-pressure/measure/index.html",
)
