# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Authoritative source URLs used in seed references and study guides.

Every URL in this module was checked against the live site (status + page
title) while the study-guide library was expanded. Sources are limited to
government agencies (CDC, OSHA, FDA, HHS, eCFR, NIH/NLM, CMS, AHRQ, USPSTF),
standards bodies (CLSI, AHA, American Red Cross, WHO, ADA) and the certifying
body (NHA).
"""

from __future__ import annotations


def cite(name: str, url: str) -> str:
    return f"{name} — {url}"


# ---------------------------------------------------------------------------
# CDC — infection prevention and healthcare worker safety
# ---------------------------------------------------------------------------
CDC_INFECTION_CONTROL = cite(
    "CDC: Infection Control for Healthcare Providers",
    "https://www.cdc.gov/infection-control/hcp/index.html",
)
CDC_HAND_HYGIENE = cite(
    "CDC: Guideline for Hand Hygiene in Healthcare Settings",
    "https://www.cdc.gov/infection-control/hcp/hand-hygiene/index.html",
)
CDC_ISOLATION_PRECAUTIONS = cite(
    "CDC/HICPAC: Isolation Precautions Guideline",
    "https://www.cdc.gov/infection-control/hcp/isolation-precautions/index.html",
)
CDC_INJECTION_SAFETY = cite(
    "CDC: Preventing Unsafe Injection Practices",
    "https://www.cdc.gov/injection-safety/hcp/clinical-safety/",
)
CDC_NIOSH_BBP = cite(
    "CDC/NIOSH: Bloodborne Infectious Diseases in Healthcare",
    "https://www.cdc.gov/niosh/healthcare/risk-factors/bloodborne-infectious-diseases.html",
)
CDC_NIOSH_INFECTIOUS = cite(
    "CDC/NIOSH: Infectious Agents — Occupational Risk Factors",
    "https://www.cdc.gov/niosh/healthcare/risk-factors/infectious-agents.html",
)
CDC_NIOSH_RISK = cite(
    "CDC/NIOSH: Risk Factors for Healthcare Workers",
    "https://www.cdc.gov/niosh/healthcare/risk-factors/index.html",
)
CDC_NIOSH_PPE = cite(
    "CDC/NIOSH: Personal Protective Equipment for Healthcare Workers",
    "https://www.cdc.gov/niosh/healthcare/protective-clothing/index.html",
)

# ---------------------------------------------------------------------------
# CDC — immunization
# ---------------------------------------------------------------------------
CDC_VACCINES_HCP = cite(
    "CDC: Vaccines & Immunizations for Health Care Providers",
    "https://www.cdc.gov/vaccines/hcp/index.html",
)
CDC_VACCINE_ADMIN = cite(
    "CDC: Vaccine Administration",
    "https://www.cdc.gov/vaccines/hcp/administration/index.html",
)
CDC_VACCINE_STORAGE = cite(
    "CDC: Vaccine Storage and Handling Toolkit",
    "https://www.cdc.gov/vaccines/hcp/storage-handling/index.html",
)
CDC_IMZ_BEST_PRACTICES = cite(
    "CDC: Immunization Best Practices (IMZ)",
    "https://www.cdc.gov/vaccines/hcp/imz-best-practices/index.html",
)
CDC_IMZ_SCHEDULES = cite(
    "CDC: Immunization Schedules for Health Care Providers",
    "https://www.cdc.gov/vaccines/hcp/imz-schedules/index.html",
)
CDC_VIS = cite(
    "CDC: Vaccine Information Statements (VIS)",
    "https://www.cdc.gov/vaccines/hcp/about-vis/index.html",
)
CDC_PINKBOOK = cite(
    "CDC: Epidemiology and Prevention of Vaccine-Preventable Diseases (Pink Book)",
    "https://www.cdc.gov/pinkbook/",
)

# ---------------------------------------------------------------------------
# CDC — diseases and public health topics
# ---------------------------------------------------------------------------
CDC_TB = cite(
    "CDC: Tuberculosis (TB)",
    "https://www.cdc.gov/tb/index.html",
)
CDC_TB_HCP = cite(
    "CDC: Tuberculosis for Health Care Providers",
    "https://www.cdc.gov/tb/hcp/index.html",
)
CDC_HEPATITIS = cite(
    "CDC: Viral Hepatitis",
    "https://www.cdc.gov/hepatitis/index.html",
)
CDC_HEPATITIS_B = cite(
    "CDC: Hepatitis B",
    "https://www.cdc.gov/hepatitis-b/about/index.html",
)
CDC_HEPATITIS_C = cite(
    "CDC: Hepatitis C",
    "https://www.cdc.gov/hepatitis-c/index.html",
)
CDC_HIV = cite(
    "CDC: HIV",
    "https://www.cdc.gov/hiv/",
)
CDC_DIABETES = cite(
    "CDC: Diabetes Basics",
    "https://www.cdc.gov/diabetes/about/index.html",
)
CDC_DIABETES_EATING = cite(
    "CDC: Diabetes and Healthy Eating",
    "https://www.cdc.gov/diabetes/healthy-eating/index.html",
)
CDC_HBP_MEASURE = cite(
    "CDC: Measuring Your Blood Pressure",
    "https://www.cdc.gov/high-blood-pressure/measure/index.html",
)
CDC_HEART_DISEASE = cite(
    "CDC: About Heart Disease",
    "https://www.cdc.gov/heart-disease/about/index.html",
)
CDC_PHYSICAL_ACTIVITY = cite(
    "CDC: Physical Activity Recommendations",
    "https://www.cdc.gov/physical-activity-basics/guidelines/index.html",
)
CDC_SLEEP = cite(
    "CDC: About Sleep",
    "https://www.cdc.gov/sleep/about/index.html",
)
CDC_NUTRITION = cite(
    "CDC: Nutrition",
    "https://www.cdc.gov/nutrition/",
)
CDC_CANCER = cite(
    "CDC: Cancer",
    "https://www.cdc.gov/cancer/",
)
CDC_AGING = cite(
    "CDC: Older Adults",
    "https://www.cdc.gov/aging/",
)
CDC_CHILD_DEV = cite(
    "CDC: Child Development",
    "https://www.cdc.gov/child-development/",
)
CDC_ORAL_HEALTH = cite(
    "CDC: Oral Health",
    "https://www.cdc.gov/oral-health/",
)
CDC_LEAD = cite(
    "CDC: Lead Prevention",
    "https://www.cdc.gov/lead-prevention/",
)
CDC_FLU = cite(
    "CDC: Influenza (Flu)",
    "https://www.cdc.gov/flu/",
)
CDC_COVID = cite(
    "CDC: COVID-19",
    "https://www.cdc.gov/covid/",
)
CDC_CHRONIC_DISEASE = cite(
    "CDC: About Chronic Disease",
    "https://www.cdc.gov/chronic-disease/about/index.html",
)
CDC_MOLD = cite(
    "CDC: Mold and Health",
    "https://www.cdc.gov/mold-health/about/index.html",
)
CDC_HEAT = cite(
    "CDC: Heat and Health Tracker",
    "https://www.cdc.gov/heat-health/about/index.html",
)
CDC_OVERDOSE = cite(
    "CDC: Overdose Prevention",
    "https://www.cdc.gov/overdose-prevention/",
)
CDC_FOOD_SAFETY = cite(
    "CDC: Food Safety",
    "https://www.cdc.gov/food-safety/",
)

CDC_ONE_AND_ONLY = cite(
    "CDC NPIN: One & Only Campaign",
    "https://npin.cdc.gov/campaign/one-only-campaign",
)

# ---------------------------------------------------------------------------
# Legacy aliases
#
# Older question banks reference these names. They are kept so existing
# references keep resolving; new code should use the names above.
# ---------------------------------------------------------------------------
CDC_STANDARD_PRECAUTIONS = CDC_INFECTION_CONTROL
CDC_ISOLATION_2007 = CDC_ISOLATION_PRECAUTIONS
CDC_HBP = CDC_HBP_MEASURE
CDC_DIABETES_BASICS = CDC_DIABETES

OSHA_BBP = cite(
    "OSHA: Bloodborne Pathogens Standard (29 CFR 1910.1030)",
    "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030",
)
OSHA_BBP_GENERAL = cite(
    "OSHA: Bloodborne Pathogens — General",
    "https://www.osha.gov/bloodborne-pathogens/general",
)
OSHA_BBP_HAZARDS = cite(
    "OSHA: Bloodborne Pathogens — Hazards",
    "https://www.osha.gov/bloodborne-pathogens/hazards",
)
OSHA_BBP_STANDARDS = cite(
    "OSHA: Bloodborne Pathogens — Standards",
    "https://www.osha.gov/bloodborne-pathogens/standards",
)
OSHA_BBP_RESOURCES = cite(
    "OSHA: Bloodborne Pathogens — Resources and Training",
    "https://www.osha.gov/bloodborne-pathogens/resources",
)
OSHA_NEEDLESTICK = cite(
    "OSHA: Bloodborne Pathogens — Evaluating and Controlling Exposure",
    "https://www.osha.gov/bloodborne-pathogens/evaluating-controlling-exposure",
)
OSHA_HEALTHCARE = cite(
    "OSHA: Healthcare",
    "https://www.osha.gov/healthcare",
)
OSHA_PPE = cite(
    "OSHA: Personal Protective Equipment",
    "https://www.osha.gov/personal-protective-equipment",
)
OSHA_HAZCOM = cite(
    "OSHA: Hazard Communication Standard",
    "https://www.osha.gov/hazcom",
)
OSHA_ERGONOMICS = cite(
    "OSHA: Ergonomics",
    "https://www.osha.gov/ergonomics",
)

# ---------------------------------------------------------------------------
# FDA
# ---------------------------------------------------------------------------
FDA_DRUG_SAFETY = cite(
    "FDA: Drug Safety and Availability",
    "https://www.fda.gov/drugs/drug-safety-and-availability",
)
FDA_MEDICATION_SAFETY = cite(
    "FDA: Medication Errors Related to CDER-Regulated Drug Products",
    "https://www.fda.gov/drugs/drug-safety-and-availability/medication-errors-related-cder-regulated-drug-products",
)
FDA_DRUG_RECALLS = cite(
    "FDA: Drug Recalls",
    "https://www.fda.gov/drugs/drug-safety-and-availability/drug-recalls",
)
FDA_MEDWATCH = cite(
    "FDA: MedWatch Safety Information and Adverse Event Reporting",
    "https://www.fda.gov/safety/medwatch-fda-safety-information-and-adverse-event-reporting-program",
)
FDA_CLIA = cite(
    "FDA: Clinical Laboratory Improvement Amendments (CLIA)",
    "https://www.fda.gov/medical-devices/ivd-regulatory-assistance/clinical-laboratory-improvement-amendments-clia",
)
FDA_CLIA_WAIVED = cite(
    "FDA: CLIA — Tests Waived by FDA",
    "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/testswaived.cfm",
)

# ---------------------------------------------------------------------------
# Federal regulations (eCFR) and HHS guidance
# ---------------------------------------------------------------------------
ECFR_HIPAA_PRIVACY = cite(
    "eCFR: HIPAA Privacy Rule (45 CFR 164 Subpart E)",
    "https://www.ecfr.gov/current/title-45/part-164/subpart-E",
)
ECFR_HIPAA_SECURITY = cite(
    "eCFR: HIPAA Security Rule (45 CFR 164 Subpart C)",
    "https://www.ecfr.gov/current/title-45/part-164/subpart-C",
)
ECFR_BBP = cite(
    "eCFR: Bloodborne Pathogens (29 CFR 1910.1030)",
    "https://www.ecfr.gov/current/title-29/part-1910/section-1910.1030",
)
ECFR_CLIA = cite(
    "eCFR: Laboratory Requirements (42 CFR 493)",
    "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-493",
)
HHS_HIPAA = cite(
    "HHS: HIPAA",
    "https://www.hhs.gov/hipaa/index.html",
)
HHS_HIPAA_PRIVACY = cite(
    "HHS: HIPAA Privacy Rule",
    "https://www.hhs.gov/hipaa/for-professionals/privacy/index.html",
)
HHS_HIPAA_SECURITY = cite(
    "HHS: HIPAA Security Rule",
    "https://www.hhs.gov/hipaa/for-professionals/security/index.html",
)
HHS_HIPAA_COVERED = cite(
    "HHS: Covered Entities and Business Associates",
    "https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html",
)

# ---------------------------------------------------------------------------
# Care coordination, patient safety and preventive care
# ---------------------------------------------------------------------------
AHRQ_CARE_COORDINATION = cite(
    "AHRQ: Care Coordination in Primary Care",
    "https://www.ahrq.gov/ncepcr/care/coordination.html",
)
AHRQ_HEALTH_LITERACY = cite(
    "AHRQ: Use the Teach-Back Method (Health Literacy Toolkit)",
    "https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html",
)
AHRQ_PATIENT_SAFETY = cite(
    "AHRQ: Patient Safety",
    "https://www.ahrq.gov/patient-safety/index.html",
)
AHRQ_TEAMSTEPPS = cite(
    "AHRQ: TeamSTEPPS",
    "https://www.ahrq.gov/teamstepps-program/index.html",
)
USPSTF = cite(
    "US Preventive Services Task Force: Recommendations",
    "https://www.uspreventiveservicestaskforce.org/uspstf/",
)
USPSTF_TOPICS = cite(
    "US Preventive Services Task Force: Recommendation Topics",
    "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics",
)
CMS_MEDICARE = cite(
    "CMS: Medicare",
    "https://www.cms.gov/",
)
MEDICARE_GOV = cite(
    "Medicare.gov: Coverage, Benefits and Enrollment",
    "https://www.medicare.gov/",
)
MEDICAID_GOV = cite(
    "Medicaid.gov: State Medicaid Programs",
    "https://www.medicaid.gov/",
)
DIETARY_GUIDELINES = cite(
    "Dietary Guidelines for Americans",
    "https://www.dietaryguidelines.gov/",
)

# ---------------------------------------------------------------------------
# NIH institutes and National Library of Medicine
# ---------------------------------------------------------------------------
NHLBI_HEALTH = cite(
    "NHLBI: Heart, Lung, Blood and Sleep Diseases",
    "https://www.nhlbi.nih.gov/health",
)
NHLBI_BP = cite(
    "NHLBI: High Blood Pressure",
    "https://www.nhlbi.nih.gov/health/high-blood-pressure",
)
NIDDK_DIABETES = cite(
    "NIDDK: Diabetes",
    "https://www.niddk.nih.gov/health-information/diabetes",
)
NIDDK_KIDNEY = cite(
    "NIDDK: Kidney Disease",
    "https://www.niddk.nih.gov/health-information/kidney-disease",
)
NIA_HEALTH = cite(
    "NIA: Health Information for Older Adults",
    "https://www.nia.nih.gov/health",
)
NCI_CANCER = cite(
    "NCI: About Cancer",
    "https://www.cancer.gov/about-cancer",
)
NINDS_HEALTH = cite(
    "NINDS: Health Information",
    "https://www.ninds.nih.gov/health-information",
)
NIAMS_HEALTH = cite(
    "NIAMS: Health Topics",
    "https://www.niams.nih.gov/health-topics",
)
NIDCD_HEALTH = cite(
    "NIDCD: Health Information",
    "https://www.nidcd.nih.gov/health",
)
NLM_MEDLINEPLUS = cite(
    "NLM: MedlinePlus",
    "https://www.nlm.nih.gov/medlineplus",
)
NCBI_BOOKSHELF = cite(
    "NCBI Bookshelf: StatPearls and Clinical References",
    "https://www.ncbi.nlm.nih.gov/books/",
)

# ---------------------------------------------------------------------------
# MedlinePlus (NIH / National Library of Medicine)
# ---------------------------------------------------------------------------
ML_HOME = cite(
    "MedlinePlus: Health Information from the National Library of Medicine",
    "https://medlineplus.gov/",
)
ML_HEALTH_TOPICS = cite(
    "MedlinePlus: Health Topics",
    "https://medlineplus.gov/healthtopics.html",
)
ML_ENCYCLOPEDIA = cite(
    "MedlinePlus: Medical Encyclopedia",
    "https://medlineplus.gov/encyclopedia.html",
)
ML_LAB_TESTS = cite(
    "MedlinePlus: Medical Tests",
    "https://medlineplus.gov/lab-tests/",
)
ML_VENIPUNCTURE = cite(
    "MedlinePlus: Venipuncture",
    "https://medlineplus.gov/ency/article/003423.htm",
)
ML_ECG = cite(
    "MedlinePlus: Electrocardiogram (ECG/EKG)",
    "https://medlineplus.gov/ency/article/003868.htm",
)
ML_ARRHYTHMIAS = cite(
    "MedlinePlus: Arrhythmias",
    "https://medlineplus.gov/ency/article/001101.htm",
)
ML_AFIB = cite(
    "MedlinePlus: Atrial Fibrillation and Atrial Flutter",
    "https://medlineplus.gov/ency/article/000184.htm",
)
ML_CAD = cite(
    "MedlinePlus: Coronary Heart Disease",
    "https://medlineplus.gov/ency/article/007115.htm",
)
ML_CPR = cite(
    "MedlinePlus: CPR",
    "https://medlineplus.gov/ency/article/000010.htm",
)
ML_CPR_ADULT = cite(
    "MedlinePlus: CPR — Adult and Child After Onset of Puberty",
    "https://medlineplus.gov/ency/article/000013.htm",
)
ML_CPR_INFANT = cite(
    "MedlinePlus: CPR — Infant",
    "https://medlineplus.gov/ency/article/000011.htm",
)
ML_CPR_CHILD = cite(
    "MedlinePlus: CPR — Young Child",
    "https://medlineplus.gov/ency/article/000012.htm",
)
ML_CHOKING_ADULT = cite(
    "MedlinePlus: Choking — Adult or Child Over 1 Year",
    "https://medlineplus.gov/ency/article/000049.htm",
)
ML_CHOKING_INFANT = cite(
    "MedlinePlus: Choking — Infant Under 1 Year",
    "https://medlineplus.gov/ency/article/000048.htm",
)
ML_ANAPHYLAXIS = cite(
    "MedlinePlus: Anaphylaxis",
    "https://medlineplus.gov/ency/article/000844.htm",
)
ML_BURNS = cite(
    "MedlinePlus: Burns",
    "https://medlineplus.gov/ency/article/000030.htm",
)
ML_CUTS = cite(
    "MedlinePlus: Cuts and Puncture Wounds",
    "https://medlineplus.gov/ency/article/000043.htm",
)
ML_BP_MEASURE = cite(
    "MedlinePlus: Blood Pressure Measurement",
    "https://medlineplus.gov/ency/article/007490.htm",
)
ML_HYPERTENSION = cite(
    "MedlinePlus: High Blood Pressure in Adults",
    "https://medlineplus.gov/ency/article/000468.htm",
)
ML_A1C = cite(
    "MedlinePlus: A1C Test",
    "https://medlineplus.gov/ency/article/003640.htm",
)
ML_DIABETES = cite(
    "MedlinePlus: Diabetes",
    "https://medlineplus.gov/ency/article/001214.htm",
)
ML_OGTT = cite(
    "MedlinePlus: Glucose Tolerance Test",
    "https://medlineplus.gov/ency/article/003466.htm",
)
ML_VACCINES = cite(
    "MedlinePlus: Vaccines — Immunizations",
    "https://medlineplus.gov/ency/article/002024.htm",
)
ML_AGING_VITALS = cite(
    "MedlinePlus: Aging Changes in Vital Signs",
    "https://medlineplus.gov/ency/article/004019.htm",
)
ML_AGING_HEART = cite(
    "MedlinePlus: Aging Changes in the Heart and Blood Vessels",
    "https://medlineplus.gov/ency/article/004006.htm",
)
ML_FIRST_AID_KIT = cite(
    "MedlinePlus: First Aid Kit",
    "https://medlineplus.gov/ency/article/001958.htm",
)
ML_ASTHMA = cite(
    "MedlinePlus: Asthma",
    "https://medlineplus.gov/ency/article/000141.htm",
)
ML_DEHYDRATION = cite(
    "MedlinePlus: Dehydration",
    "https://medlineplus.gov/ency/article/000982.htm",
)
ML_DVT = cite(
    "MedlinePlus: Deep Vein Thrombosis",
    "https://medlineplus.gov/ency/article/000156.htm",
)
ML_ANGINA = cite(
    "MedlinePlus: Angina",
    "https://medlineplus.gov/ency/article/001107.htm",
)
ML_HEART_ATTACK = cite(
    "MedlinePlus: Heart Attack",
    "https://medlineplus.gov/ency/article/000195.htm",
)
ML_HEART_ATTACK_FIRST_AID = cite(
    "MedlinePlus: Heart Attack First Aid",
    "https://medlineplus.gov/ency/article/000063.htm",
)
ML_DEMENTIA = cite(
    "MedlinePlus: Dementia",
    "https://medlineplus.gov/ency/article/000739.htm",
)
ML_INFANT_DEVELOPMENT = cite(
    "MedlinePlus: Infant — Newborn Development",
    "https://medlineplus.gov/ency/article/002004.htm",
)
ML_DIABETES_TOPIC = cite(
    "MedlinePlus: Diabetes",
    "https://medlineplus.gov/diabetes.html",
)
ML_HBP_TOPIC = cite(
    "MedlinePlus: High Blood Pressure",
    "https://medlineplus.gov/highbloodpressure.html",
)
ML_IMMUNIZATION = cite(
    "MedlinePlus: Vaccines and Immunization",
    "https://medlineplus.gov/immunization.html",
)
ML_TB = cite(
    "MedlinePlus: Tuberculosis",
    "https://medlineplus.gov/tuberculosis.html",
)
ML_HEPATITIS_B = cite(
    "MedlinePlus: Hepatitis B",
    "https://medlineplus.gov/hepatitisb.html",
)
ML_CHILD_HEALTH = cite(
    "MedlinePlus: Children's Health",
    "https://medlineplus.gov/childrenshealth.html",
)
ML_OLDER_ADULT = cite(
    "MedlinePlus: Older Adult Health",
    "https://medlineplus.gov/olderadulthealth.html",
)
ML_PREGNANCY = cite(
    "MedlinePlus: Pregnancy",
    "https://medlineplus.gov/pregnancy.html",
)
ML_ANAPHYLAXIS_TOPIC = cite(
    "MedlinePlus: Anaphylaxis",
    "https://medlineplus.gov/anaphylaxis.html",
)
ML_NUTRITION = cite(
    "MedlinePlus: Nutrition",
    "https://medlineplus.gov/nutrition.html",
)
ML_HAND_HYGIENE = cite(
    "MedlinePlus: Hand-washing",
    "https://medlineplus.gov/ency/article/007425.htm",
)
ML_BLOOD = cite(
    "MedlinePlus: Blood and Blood Diseases",
    "https://medlineplus.gov/blood.html",
)
ML_HEART_ATTACK_TOPIC = cite(
    "MedlinePlus: Heart Attack",
    "https://medlineplus.gov/heartattack.html",
)
ML_OSTEOPOROSIS = cite(
    "MedlinePlus: Osteoporosis",
    "https://medlineplus.gov/osteoporosis.html",
)
ML_ARTHRITIS = cite(
    "MedlinePlus: Arthritis",
    "https://medlineplus.gov/arthritis.html",
)
ML_DIABETIC_FOOT = cite(
    "MedlinePlus: Diabetic Foot",
    "https://medlineplus.gov/diabeticfoot.html",
)
ML_KIDNEY_FAILURE = cite(
    "MedlinePlus: Kidney Failure",
    "https://medlineplus.gov/kidneyfailure.html",
)
ML_SEPSIS = cite(
    "MedlinePlus: Sepsis",
    "https://medlineplus.gov/sepsis.html",
)
ML_SHINGLES = cite(
    "MedlinePlus: Shingles",
    "https://medlineplus.gov/shingles.html",
)
ML_FEVER = cite(
    "MedlinePlus: Fever",
    "https://medlineplus.gov/fever.html",
)
ML_PNEUMONIA = cite(
    "MedlinePlus: Pneumonia",
    "https://medlineplus.gov/pneumonia.html",
)
ML_BRONCHITIS = cite(
    "MedlinePlus: Bronchitis",
    "https://medlineplus.gov/bronchitis.html",
)
ML_ASTHMA_TOPIC = cite(
    "MedlinePlus: Asthma",
    "https://medlineplus.gov/asthma.html",
)
ML_COPD = cite(
    "MedlinePlus: Chronic Obstructive Pulmonary Disease (COPD)",
    "https://medlineplus.gov/copd.html",
)
ML_POISONING = cite(
    "MedlinePlus: Poisoning",
    "https://medlineplus.gov/poisoning.html",
)
ML_BURNS_TOPIC = cite(
    "MedlinePlus: Burns",
    "https://medlineplus.gov/burns.html",
)
ML_DEHYDRATION_TOPIC = cite(
    "MedlinePlus: Dehydration",
    "https://medlineplus.gov/dehydration.html",
)
ML_HEAT_ILLNESS = cite(
    "MedlinePlus: Heat Illness",
    "https://medlineplus.gov/heatillness.html",
)
ML_DRUG_SAFETY = cite(
    "MedlinePlus: Medication Safety and Drug Interactions",
    "https://medlineplus.gov/drugsafety.html",
)
ML_HEALTH_INSURANCE = cite(
    "MedlinePlus: Health Insurance",
    "https://medlineplus.gov/healthinsurance.html",
)
ML_MEDICARE = cite(
    "MedlinePlus: Medicare",
    "https://medlineplus.gov/medicare.html",
)
ML_MEDICAID = cite(
    "MedlinePlus: Medicaid",
    "https://medlineplus.gov/medicaid.html",
)
ML_PATIENT_RIGHTS = cite(
    "MedlinePlus: Patient Rights",
    "https://medlineplus.gov/patientrights.html",
)
ML_CAREGIVERS = cite(
    "MedlinePlus: Caregivers",
    "https://medlineplus.gov/caregivers.html",
)
ML_TEEN_HEALTH = cite(
    "MedlinePlus: Teen Health",
    "https://medlineplus.gov/teenhealth.html",
)
ML_HEALTHY_LIVING = cite(
    "MedlinePlus: Healthy Living",
    "https://medlineplus.gov/healthyliving.html",
)
ML_VITAL_SIGNS = cite(
    "MedlinePlus: Vital Signs",
    "https://medlineplus.gov/ency/article/002341.htm",
)
ML_PULSE = cite(
    "MedlinePlus: Pulse",
    "https://medlineplus.gov/ency/article/003399.htm",
)
ML_MEDICATION_ERRORS = cite(
    "MedlinePlus: Medication Errors",
    "https://medlineplus.gov/medicationerrors.html",
)

# ---------------------------------------------------------------------------
# American Heart Association and American Red Cross
# ---------------------------------------------------------------------------
AHA_WHAT_IS_CPR = cite(
    "American Heart Association: What is CPR",
    "https://cpr.heart.org/en/resources/what-is-cpr",
)
AHA_ADULT_BLS = cite(
    "American Heart Association: Part 7 — Adult Basic Life Support",
    "https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support",
)
AHA_PALS = cite(
    "American Heart Association: Pediatric Basic Life Support",
    "https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/pediatric-basic-life-support",
)
AHA_GUIDELINES = cite(
    "American Heart Association: CPR and ECC Guidelines",
    "https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines",
)
AHA_ALGORITHMS = cite(
    "American Heart Association: CPR and ECC Algorithms",
    "https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/algorithms",
)
AHA_EXECUTIVE_SUMMARY = cite(
    "American Heart Association: Guidelines Executive Summary",
    "https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/executive-summary",
)
AHA_TOP_THINGS = cite(
    "American Heart Association: 2025 Guidelines — Top Things to Know",
    "https://professional.heart.org/en/science-news/2025-aha-guidelines-for-cpr-and-ecc/top-things-to-know",
)
AHA_CHAIN = cite(
    "American Heart Association: Chain of Survival",
    "https://cpr.heart.org/en/resources/cpr-facts-and-stats/chain-of-survival",
)
AHA_HIGH_QUALITY = cite(
    "American Heart Association: High-Quality CPR",
    "https://cpr.heart.org/en/resuscitation-science/high-quality-cpr",
)
AHA_ADULT_FBAO = cite(
    "American Heart Association: Adult Foreign-Body Airway Obstruction Algorithm",
    "https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Algorithms/Algorithm-BLS-Adult-FBAO-250630.pdf",
)
AHA_CHILD_FBAO = cite(
    "American Heart Association: Child Foreign-Body Airway Obstruction Algorithm",
    "https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Algorithms/Algorithm-BLS-Child-FBAO.pdf",
)
AHA_NEONATAL_ALG = cite(
    "American Heart Association: Neonatal Resuscitation Algorithm (2025)",
    "https://cpr.heart.org/-/media/CPR-Files/CPR-Guidelines-Files/2025-Algorithms/1-2-Algorithm-Neonatal-Resuscitation-250129.pdf",  # noqa: E501
)
AHA_AED_PROGRAM = cite(
    "American Heart Association: AED Implementation",
    "https://cpr.heart.org/en/training-programs/aed-implementation",
)
RED_CROSS_FIRST_AID = cite(
    "American Red Cross: First Aid",
    "https://www.redcross.org/take-a-class/first-aid",
)
RED_CROSS_CPR = cite(
    "American Red Cross: CPR Courses",
    "https://www.redcross.org/take-a-class/cpr",
)
RED_CROSS_FIRST_AID_STEPS = cite(
    "American Red Cross: First Aid Steps",
    "https://www.redcross.org/take-a-class/first-aid/performing-first-aid/first-aid-steps",
)

# ---------------------------------------------------------------------------
# WHO and CLSI
# ---------------------------------------------------------------------------
WHO_INJECTION_SAFETY = cite(
    "WHO: Injection safety",
    "https://www.who.int/teams/integrated-health-services/infection-prevention-control/injection-safety",
)
WHO_HAND_HYGIENE = cite(
    "WHO: Hand hygiene",
    "https://www.who.int/teams/integrated-health-services/infection-prevention-control/hand-hygiene",
)
WHO_PHLBOTOMY = cite(
    "WHO: Guidelines on drawing blood: Best practices in phlebotomy",
    "https://iris.who.int/handle/10665/44379",
)
CLSI_GP41 = cite(
    "CLSI: Collection of Diagnostic Venous Blood Specimens (PRE02/GP41)",
    "https://clsi.org/shop/standards/pre02/",
)
CLSI_GP41_SAMPLE = cite(
    "CLSI: GP41 Collection of Diagnostic Venous Blood Specimens (sample pages)",
    "https://clsi.org/media/1372/gp41ed7_sample.pdf",
)

# ---------------------------------------------------------------------------
# NHA (test plans), ADA and AMA
# ---------------------------------------------------------------------------
NHA_CCMA = cite(
    "NHA: CCMA certification",
    "https://www.nhanow.com/certifications/ccma",
)
NHA_CCMA_EXAM = cite(
    "NHA: CCMA certification exam",
    "https://www.nhanow.com/certifications/ccma/exam",
)
NHA_CET = cite(
    "NHA: CET certification",
    "https://www.nhanow.com/certifications/cet",
)
NHA_CPT = cite(
    "NHA: CPT certification",
    "https://www.nhanow.com/certifications/cpt",
)
ADA_STANDARDS = cite(
    "American Diabetes Association: Standards of Care in Diabetes",
    "https://diabetesjournals.org/care/issue/48/Supplement_1",
)
ADA_DIAGNOSIS = cite(
    "American Diabetes Association: Classification and Diagnosis of Diabetes",
    "https://diabetesjournals.org/care/article/48/Supplement_1/S27/157553",
)
ADA_NUTRITION = cite(
    "American Diabetes Association: Food and Nutrition",
    "https://diabetes.org/food-nutrition",
)

# Diabetes study guide (ccma-diabetes) — pages verified against the live site.
CDC_TYPE_1 = cite(
    "CDC: About Type 1 Diabetes",
    "https://www.cdc.gov/diabetes/about/about-type-1-diabetes.html",
)
CDC_TYPE_2 = cite(
    "CDC: About Type 2 Diabetes",
    "https://www.cdc.gov/diabetes/about/about-type-2-diabetes.html",
)
CDC_PREDIABETES = cite(
    "CDC: Prediabetes — Prevent Type 2 Diabetes",
    "https://www.cdc.gov/diabetes/prevention-type-2/prediabetes-prevent-type-2.html",
)
CDC_A1C = cite(
    "CDC: A1C Test for Prediabetes and Diabetes",
    "https://www.cdc.gov/diabetes/diabetes-testing/prediabetes-a1c-test.html",
)
CDC_DIABETES_TESTING = cite(
    "CDC: Diabetes Testing",
    "https://www.cdc.gov/diabetes/diabetes-testing/index.html",
)
CDC_GESTATIONAL = cite(
    "CDC: Gestational Diabetes",
    "https://www.cdc.gov/diabetes/about/gestational-diabetes.html",
)
CDC_INSULIN_RESISTANCE = cite(
    "CDC: Insulin Resistance and Type 2 Diabetes",
    "https://www.cdc.gov/diabetes/about/insulin-resistance-type-2-diabetes.html",
)
CDC_DIABETES_HEART = cite(
    "CDC: Diabetes and Your Heart",
    "https://www.cdc.gov/diabetes/diabetes-complications/diabetes-and-your-heart.html",
)
CDC_VISION_LOSS = cite(
    "CDC: Vision Loss and Diabetes",
    "https://www.cdc.gov/diabetes/diabetes-complications/diabetes-and-vision-loss.html",
)
CDC_KIDNEY_DISEASE = cite(
    "CDC: Diabetes and Chronic Kidney Disease",
    "https://www.cdc.gov/diabetes/diabetes-complications/diabetes-and-chronic-kidney-disease.html",
)
CDC_NCHS_DB319 = cite(
    "CDC NCHS: Data Brief 319, Diabetes Prevalence (NHANES 2013–2016)",
    "https://www.cdc.gov/nchs/data/databriefs/db319.pdf",
)
CDC_MMWR_CARDIOMETABOLIC = cite(
    "CDC MMWR: Cardiometabolic Diseases Among Racial and Ethnic Subgroups (BRFSS 2013–2021)",
    "https://www.cdc.gov/mmwr/volumes/73/wr/mm7303a1.htm",
)
NIDDK_LOW_BLOOD_GLUCOSE = cite(
    "NIDDK: Low Blood Glucose (Hypoglycemia)",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/low-blood-glucose-hypoglycemia",
)
NIDDK_DIABETES_SYMPTOMS = cite(
    "NIDDK: Symptoms & Causes of Diabetes",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/symptoms-causes",
)
NIDDK_INSULIN_TREATMENTS = cite(
    "NIDDK: Insulin, Medicines, & Other Diabetes Treatments",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/insulin-medicines-treatments",
)
NIDDK_TYPE_1 = cite(
    "NIDDK: Type 1 Diabetes",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes/type-1-diabetes",
)
NIDDK_TYPE_2 = cite(
    "NIDDK: Type 2 Diabetes",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes/type-2-diabetes",
)
NIDDK_SEXUAL_BLADDER = cite(
    "NIDDK: Diabetes, Sexual, & Bladder Problems",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/sexual-bladder-problems",
)
NIDDK_GDM_CHAPTER = cite(
    "NIDDK: Diabetes in America, Chapter 4 — Gestational Diabetes",
    "https://www.niddk.nih.gov/-/media/Files/Strategic-Plans/Diabetes-in-America-3rd-Edition/DIA_Ch04.ashx"
    "?la=en&hash=BCF055C3BF22718550FB0706FC3A6EED",
)
FDA_HUMULIN_R_LABEL = cite(
    "FDA: Humulin R U-100 Prescribing Information",
    "https://www.accessdata.fda.gov/drugsatfda_docs/label/2015/018780s150lbl.pdf",
)
FDA_INSULIN_SYRINGE_510K = cite(
    "FDA 510(k) K212499: BD Insulin Syringe Clearance",
    "https://www.accessdata.fda.gov/cdrh_docs/pdf21/K212499.pdf",
)
AMA_ETHICS = cite(
    "American Medical Association: Code of Medical Ethics",
    "https://www.ama-assn.org/about/ethics",
)

# ---------------------------------------------------------------------------
# Domains allowed in study guides. Keep in sync with the test that enforces
# that every study-guide link points at an official health-care source.
# ---------------------------------------------------------------------------
OFFICIAL_SOURCE_DOMAINS: frozenset[str] = frozenset(
    {
        "cdc.gov",
        "clsi.org",
        "cpr.heart.org",
        "diabetes.org",
        "diabetesjournals.org",
        "ecfr.gov",
        "fda.gov",
        "accessdata.fda.gov",
        "hhs.gov",
        "ahrq.gov",
        "ama-assn.org",
        "medlineplus.gov",
        "nhanow.com",
        "ncbi.nlm.nih.gov",
        "nhlbi.nih.gov",
        "niddk.nih.gov",
        "nidcd.nih.gov",
        "ninds.nih.gov",
        "nia.nih.gov",
        "niams.nih.gov",
        "nlm.nih.gov",
        "cms.gov",
        "medicaid.gov",
        "medicare.gov",
        "osha.gov",
        "redcross.org",
        "uspreventiveservicestaskforce.org",
        "who.int",
        "iris.who.int",
        "dietaryguidelines.gov",
        "professional.heart.org",
        "cancer.gov",
        "accessdata.fda.gov",
    }
)


# ---------------------------------------------------------------------------
# Legacy aliases
#
# Older question banks reference these names. They are kept so existing
# references keep resolving; new code should use the names above.
# ---------------------------------------------------------------------------
AHA_HQ_CPR = AHA_HIGH_QUALITY
MEDLINEPLUS_HAND_HYGIENE = ML_HAND_HYGIENE
MEDLINEPLUS_DIABETES = ML_DIABETES
