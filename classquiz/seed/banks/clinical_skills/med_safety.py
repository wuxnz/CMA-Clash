# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored Clinical Skills questions (topic skill-med-safety)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [

    # skill-med-safety-001
    fact(
        "skill-med-safety",
        "Which components are included in the classic six rights of medication administration?",
        "Right patient, drug, dose, route, time, and documentation",
        [
            "Right room, bed assignment, and insurance tier",
            "Right prescriber signature style and pharmacy fax number",
            "Right patient age group and clinic zip code without comparing the drug name and strength to the prescriber order",
        ],
        "The rights framework targets preventable administration errors before they reach the patient. Room and billing data do not verify drug identity or patient matching.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-002
    fact(
        "skill-med-safety",
        "How should patient identity be confirmed before giving any medication in clinic?",
        "At least two identifiers per facility policy, such as name and date of birth",
        [
            "First name alone in a quiet waiting room without a second identifier or chart match",
            "Room number printed on the door without speaking to the patient",
            "A single medical record number read from a hallway monitor",
        ],
        "Two-identifier verification reduces wrong-patient errors. A single identifier or indirect lookup is insufficient for high-risk processes.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-003
    fact(
        "skill-med-safety",
        "When reading a medication label before administration, which elements must match the order?",
        "Drug name, strength, route, and expiration date",
        [
            "Manufacturer logo and tablet color without the drug name",
            "National drug code without the drug name",
            "Lot number alone when the name is abbreviated",
        ],
        "Label checks catch look-alike products and expired stock. Visual branding and partial codes do not confirm the ordered therapy.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-004
    fact(
        "skill-med-safety",
        "When in the workflow should documented medication allergies be reviewed?",
        "Before selecting or administering any drug, including vaccines and contrast when applicable",
        [
            "After the injection is completed and documented without reviewing documented allergies before preparation",
            "At the annual wellness visit without regard to new prescriptions",
            "When the patient requests a refill of an unrelated product",
        ],
        "Allergy review belongs in the preparation phase. Late review may follow irreversible exposure.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-005
    fact(
        "skill-med-safety",
        "A provider order reads metFORMIN 500 mg by mouth twice daily. Which verification step is most critical?",
        "Match the written drug name and dose to the dispensed product label",
        [
            "Select tablets by physical size as a proxy for strength",
            "Give a double dose if the patient missed yesterday without calling the prescriber",
            "Crush extended-release tablets for easier swallowing without authorization",
        ],
        "Name and dose errors are common with oral hypoglycemics. Altering formulation without guidance changes absorption and safety.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-006
    fact(
        "skill-med-safety",
        "Which strategies help manage look-alike sound-alike (LASA) medication pairs?",
        "Tall-man lettering, separate storage, and independent double checks when policy requires",
        [
            "Storing all vials together in one unlabeled bin",
            "Relying on cap color as the sole identifier when staff rely on memory from a prior patient with a similar name",
            "Using a single identifier when the drug name sounds familiar",
        ],
        "LASA strategies emphasize visual differentiation and deliberate verification. Bulk storage and single identifiers increase selection errors.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-007
    fact(
        "skill-med-safety",
        "Why are insulin and anticoagulants often classified as high-alert medications in ambulatory settings?",
        "They carry heightened risk of significant harm when used in error",
        [
            "They do not require a prescriber order in clinic",
            "They are exempt from documentation on the MAR without recording the dose on the medication administration record",
            "They may be shared between patients to reduce waste",
        ],
        "High-alert lists focus on harm potential, not convenience. Orders and documentation remain mandatory.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-008
    fact(
        "skill-med-safety",
        "What does medication reconciliation at an office visit compare?",
        "The patient's home medication list with current orders to find discrepancies",
        [
            "Staff vaccination records with the formulary",
            "Supply invoices with staff scheduling grids when the clinic is behind schedule and checks are abbreviated",
            "Vital sign trends with pharmacy delivery schedules",
        ],
        "Reconciliation catches omissions, duplications, and dose mismatches across care transitions. Unrelated administrative data do not address drug safety.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-009
    fact(
        "skill-med-safety",
        "When should barcode scanning occur if barcode medication administration technology is available?",
        "For the patient identifier and the specific product before administration when workflow allows",
        [
            "After the dose is injected and the vial is discarded",
            "In place of allergy and indication assessment without reading the expiration date on the product label",
            "On the first dose of a multi-day course but not on later doses",
        ],
        "Barcode systems add an electronic match step to the rights framework. They supplement rather than replace clinical judgment and allergy review.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-010
    fact(
        "skill-med-safety",
        "How should a near-miss medication error caught before reaching the patient be handled?",
        "Reported through the facility incident system to support prevention",
        [
            "Omitted from reporting because no harm occurred when barcode equipment is turned off to reduce alert noise",
            "Documented in a personal notebook without the incident system",
            "Discussed with the patient but not entered in the safety system",
        ],
        "Near-miss reporting reveals system weaknesses before patient injury. Formal reporting supports quality improvement.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-011
    fact(
        "skill-med-safety",
        "How does unit-dose packaging in clinic help reduce medication errors?",
        "Providing a single premeasured amount with less manipulation",
        [
            "Eliminating the need for patient identification",
            "Replacing expiration date monitoring without notifying the prescriber about a refused or missed dose",
            "Allowing partial doses to be saved for the next patient",
        ],
        "Prepackaged units limit compounding mistakes and contamination. Identity checks and dating remain required.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-012
    fact(
        "skill-med-safety",
        "Why should topical medication orders document application site?",
        "Rotation and absorption depend on accurate placement records",
        [
            "Site choice has no effect on drug action",
            "Documentation replaces hand hygiene before application",
            "All topicals may be applied to mucous membranes without a specific order",
        ],
        "Site documentation supports efficacy and prevents overlapping toxic doses. Mucosal application requires explicit orders.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-013
    fact(
        "skill-med-safety",
        "What do controlled substance counts in clinic typically require?",
        "Two staff members per policy when opening, closing, or transferring inventory",
        [
            "A single staff member without a witness",
            "Monthly counts without a written log when partial doses are saved for a different patient later",
            "Patient co-signature on the perpetual inventory",
        ],
        "Dual verification deters diversion and documents chain of custody. Informal handling violates regulatory expectations.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-014
    fact(
        "skill-med-safety",
        "What basis should be used when calculating pediatric liquid doses?",
        "Milligrams per kilogram from a verified reference and double-checked math",
        [
            "Adult tablet strength regardless of weight",
            "Household tablespoons without metric conversion",
            "Doubling the dose when the child is fussy without comparing the drug name and strength to the prescriber order",
        ],
        "Weight-based math prevents tenfold pediatric errors. Volume must be measured with metric devices.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-015
    fact(
        "skill-med-safety",
        "Why must insulin syringes match the concentration printed on the vial?",
        "U-100 and other concentrations change how many units occupy each milliliter",
        [
            "Any syringe graduation equals one unit for every insulin product",
            "Concentration is a billing code without clinical effect when the package resembles another medication on the shelf",
            "Oral syringes are interchangeable with insulin syringes without training",
        ],
        "Concentration mismatch causes severe hypo- or hyperglycemia. Dedicated insulin syringes are calibrated to labeled strength.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-016
    fact(
        "skill-med-safety",
        "Why should medication orders use a leading zero before a decimal (for example 0.5 mg) instead of writing .5 mg?",
        "To prevent misreading the decimal and giving a tenfold overdose",
        [
            "To indicate the drug is a controlled substance",
            "To convert milligrams automatically to grains without reviewing documented allergies before preparation",
            "To signal that trailing zeros are required on all strengths",
        ],
        "Decimal placement errors are a frequent source of tenfold mistakes. Leading zeros clarify doses less than one unit.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-017
    fact(
        "skill-med-safety",
        "What should the medical assistant do when a medication order contains an unclear abbreviation?",
        "Contact the prescriber or pharmacist for clarification before preparation",
        [
            "Guess the intended drug based on the last patient with a similar name",
            "Administer the most common drug in that therapeutic class",
            "Leave the order off the MAR until the next visit when staff rely on memory from a prior patient with a similar name",
        ],
        "Ambiguous abbreviations contributed to historical sentinel events. Clarification is safer than assumption.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-018
    fact(
        "skill-med-safety",
        "What can happen if an enteric-coated tablet is crushed without authorization?",
        "The intended release is destroyed and gastric irritation or toxicity may increase",
        [
            "Controlled release becomes more predictable and safer",
            "Allergy assessment is no longer required without recording the dose on the medication administration record",
            "The drug is converted to a parenteral formulation",
        ],
        "Coatings serve pharmacokinetic and protective roles. Altering formulation requires prescriber or pharmacist guidance.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-019
    fact(
        "skill-med-safety",
        "What should each staff member verify during an independent double-check of a high-alert drug?",
        "Verify order, product label, dose, route, and patient without relying on the other's conclusion",
        [
            "Watch the other person work and sign the log afterward",
            "Sign the log before the product is selected from storage",
            "Use the same prepared syringe to save supplies when the clinic is behind schedule and checks are abbreviated",
        ],
        "Independent checks mean separate cognitive review. Shared observation defeats the purpose.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-020
    fact(
        "skill-med-safety",
        "How should medication samples in clinic be handled?",
        "Stored, logged, and dispensed per policy with patient education documented",
        [
            "Left in unlocked drawers for patient self-selection",
            "Transferred between patients when unopened without reading the expiration date on the product label",
            "Given without reviewing expiration or lot information",
        ],
        "Samples are still medications with traceability and counseling requirements. Loose storage invites errors and diversion.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-021
    fact(
        "skill-med-safety",
        "What should the medical assistant do when a patient brings herbal supplements to medication reconciliation?",
        "Record product names and doses in the medication list for provider review",
        [
            "Exclude them because they are not prescription drugs",
            "List them in social history without dose detail when barcode equipment is turned off to reduce alert noise",
            "Add every supplement to the allergy list automatically",
        ],
        "Supplements interact with prescribed drugs and affect perioperative plans. Accurate lists support clinical decisions.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-022
    fact(
        "skill-med-safety",
        "What should be done with expired medications found in the exam room?",
        "Removed from patient care areas and disposed per pharmaceutical waste policy",
        [
            "Administered quickly before the expiration date changes",
            "Combined into one bottle to simplify inventory without notifying the prescriber about a refused or missed dose",
            "Returned to the manufacturer without documentation",
        ],
        "Expired products may lack potency or stability. Proper disposal prevents accidental administration.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-023
    fact(
        "skill-med-safety",
        "What safety practice is illustrated by a verbal read-back of drug name and dose during a double-check?",
        "A communication strategy to catch selection errors",
        [
            "A replacement for two-identifier patient verification",
            "A prohibited disclosure under HIPAA in all settings",
            "An optional courtesy that may be skipped when busy",
        ],
        "Read-backs close loops on high-risk tasks. They complement rather than replace identity verification.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-024
    fact(
        "skill-med-safety",
        "What error risk increases when potassium chloride vials are stored next to saline flush bags?",
        "Wrong solution selection during preparation",
        [
            "Improved cold-chain efficiency in the refrigerator",
            "Lower central line infection rates automatically",
            "Reduced need for independent double checks",
        ],
        "Physical separation and look-alike labeling strategies reduce swap errors. Storage layout is an active safety control.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-med-safety-025
    fact(
        "skill-med-safety",
        "What should documentation include when a patient refuses an ordered medication?",
        "The offer, patient response, and notification of the provider",
        [
            "A fabricated administration time to close the MAR",
            "No note because refusal is assumed to be temporary",
            "Another patient's refusal copied forward when partial doses are saved for a different patient later",
        ],
        "Refusal affects the plan of care and legal record accuracy. Providers need timely notification.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-026
    fact(
        "skill-med-safety",
        "What response is required when a medication error is discovered after administration?",
        "Immediate assessment, provider notification, and monitoring per protocol",
        [
            "Waiting until the next scheduled visit to mention it without comparing the drug name and strength to the prescriber order",
            "Correcting the MAR silently without telling the team",
            "Discharging the patient without disclosure when asymptomatic",
        ],
        "Post-administration errors may need antidotes or labs. Rapid response limits harm.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-027
    fact(
        "skill-med-safety",
        "What does tall-man lettering emphasize when comparing hydrALAZINE and hydrOXYzine?",
        "Dissimilar letter segments within look-alike names",
        [
            "Identical spelling for both drugs to reduce confusion",
            "Automatic dose conversion between the two agents",
            "Insurance billing codes for antihistamines",
        ],
        "Emphasizing unique syllables helps distinguish sound-alike agents during verbal orders and picking.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-028
    fact(
        "skill-med-safety",
        "What should staff do when a barcode scanning mismatch alert appears?",
        "Stop, investigate the discrepancy, and resolve before proceeding",
        [
            "Override without reason to keep clinic on schedule",
            "Disable the scanner for the rest of the day when the package resembles another medication on the shelf",
            "Administer the product if the patient has been waiting",
        ],
        "Alerts often indicate wrong patient, drug, or expired product. Bypassing without resolution perpetuates risk.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-029
    fact(
        "skill-med-safety",
        "When should medication reconciliation occur after hospital discharge?",
        "At the first follow-up visit and whenever orders change",
        [
            "Once per lifetime regardless of new prescriptions",
            "When the patient brings no medication bottles and orders are unchanged",
            "By removing home medications from the chart without review",
        ],
        "Transitions are high risk for omissions and duplications. Repeated reconciliation keeps the list current.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-030
    fact(
        "skill-med-safety",
        "What should a suspiciously large opioid prescription for a new patient trigger?",
        "Verification with the prescriber and diversion prevention steps per policy",
        [
            "Automatic dispensing without questions without reviewing documented allergies before preparation",
            "Splitting tablets among other patients in the clinic",
            "Discarding partial tablets in regular office trash",
        ],
        "Diversion and misuse harm patients and communities. Policy-driven verification protects everyone.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-031
    fact(
        "skill-med-safety",
        "What risks arise from pouring liquid medication from a stock bottle into an unlabeled cup?",
        "Wrong dose and wrong patient administration",
        [
            "Improved sterility compared with oral syringes",
            "Elimination of metric measurement requirements",
            "Automatic therapeutic drug monitoring",
        ],
        "Oral syringes and labeled cups support accurate individual doses. Unlabeled containers invite mix-ups.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-032
    fact(
        "skill-med-safety",
        "What may time-critical medications such as certain antibiotics require regarding administration timing?",
        "Administration within prescribed windows documented on the MAR",
        [
            "Random timing without regard to the order",
            "Batching all doses at clinic closing when staff rely on memory from a prior patient with a similar name",
            "Withholding doses to extend inventory",
        ],
        "Delayed antimicrobials can worsen outcomes. Scheduled times reflect pharmacodynamic goals.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-033
    fact(
        "skill-med-safety",
        "What technique should the medical assistant follow when preparing medications from multidose vials?",
        "Use a new sterile needle and syringe for each entry and follow beyond-use dating",
        [
            "Leave needles embedded in the vial rubber between patients",
            "Store open vials in a personal locker without dating without recording the dose on the medication administration record",
            "Share remaining volume with visitors in the waiting area",
        ],
        "Multidose vials require aseptic technique and dating to limit contamination. Embedded needles breach sterility.",
        [S.CDC_INJECTION_SAFETY, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-034
    fact(
        "skill-med-safety",
        "What does patient teach-back after new medication counseling help confirm?",
        "Understanding of dose, route, timing, and side effects to report",
        [
            "That the patient prefers generic over brand names",
            "Staff break schedules for the week when the clinic is behind schedule and checks are abbreviated",
            "Parking validation for the next visit",
        ],
        "Teach-back reveals misunderstandings before the patient leaves. It is a structured safety communication tool.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-035
    fact(
        "skill-med-safety",
        "What is required when wasting partial doses of controlled substances?",
        "Witnessed disposal documented per DEA and facility rules",
        [
            "Pouring into the sink without a witness",
            "Saving remnants for the next patient with the same diagnosis",
            "Combining waste from two patients in one syringe",
        ],
        "Witnessed waste maintains chain of custody and prevents diversion. Informal disposal is noncompliant.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-036
    fact(
        "skill-med-safety",
        "How should staff resolve a pharmacy label that differs from the electronic order?",
        "Contacting the pharmacist or prescriber before administration",
        [
            "Giving whichever strength is lower without asking",
            "Administering both strengths sequentially",
            "Removing the label to reduce confusion without reading the expiration date on the product label",
        ],
        "Discrepancies may reflect therapeutic changes or errors. Administration waits on clarification.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-037
    fact(
        "skill-med-safety",
        "What storage measures are often used for high-alert medications in clinic?",
        "Locked cabinets, separate bins, and alert stickers per policy",
        [
            "Open shelves in the waiting area for quick access",
            "Mixing with office supplies in a shared drawer when barcode equipment is turned off to reduce alert noise",
            "Removing lot numbers to protect patient privacy",
        ],
        "Physical controls add barriers to wrong selection. Lot tracking supports recalls.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-038
    fact(
        "skill-med-safety",
        "What should documentation of medication administration record?",
        "Drug, dose, route, time, site if relevant, and patient response when observed",
        [
            "The time of day without the drug name",
            "Staff initials without dose or route",
            "A check mark with no product detail without notifying the prescriber about a refused or missed dose",
        ],
        "Complete MAR entries support continuity and error investigation. Vague marks lack clinical detail.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-039
    fact(
        "skill-med-safety",
        "What must staff do when using an automated dispensing cabinet override for emergencies?",
        "Document reason and reconcile inventory afterward per policy",
        [
            "Leave drawers open overnight without logging",
            "Remove tracking labels permanently when partial doses are saved for a different patient later",
            "Dispense for unauthorized personal use",
        ],
        "Overrides are audited to detect patterns of unsafe bypass. Documentation maintains accountability.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-040
    fact(
        "skill-med-safety",
        "Under what conditions should tablets be split for administration?",
        "With a pill splitter when the prescriber or reference confirms the product is scored and splittable",
        [
            "Using any knife on enteric-coated tablets",
            "Crushing coated products for convenience without comparing the drug name and strength to the prescriber order",
            "Splitting without updating the documented dose",
        ],
        "Uneven halves and destroyed coatings alter exposure. Confirmation prevents sub- or toxic doses.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-041
    fact(
        "skill-med-safety",
        "What topics may medication safety huddles at the start of clinic review?",
        "High-risk patients, look-alike products, and staffing coverage for double checks",
        [
            "Deleting allergy lists to shorten the huddle when the package resembles another medication on the shelf",
            "Disabling barcode scanners to reduce alert noise",
            "Skipping high-alert drugs when short-staffed",
        ],
        "Brief team reviews align attention on daily risks. Disabling technology or omitting allergies removes safeguards.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-042
    fact(
        "skill-med-safety",
        "What problems can returning unopened patient-specific medications to stock without policy approval cause?",
        "Cross-patient contamination and labeling errors",
        [
            "Guaranteed sterility of multidose vials",
            "Automatic insurance reimbursement without reviewing documented allergies before preparation",
            "Elimination of reconciliation at follow-up",
        ],
        "Once issued to a patient, products may not meet storage and identity standards for reuse. Policy governs returns.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
]
