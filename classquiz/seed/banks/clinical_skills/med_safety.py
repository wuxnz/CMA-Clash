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
            "Right room number, bed color, and parking space",
            "Right pharmacy revenue code and staff uniform",
            "Right social media profile and email domain",
        ],
        "The rights framework targets preventable administration errors before they reach the patient. Cap color and room décor do not verify drug identity or patient matching.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-002
    fact(
        "skill-med-safety",
        "Before giving any medication in clinic, the medical assistant should confirm patient identity using:",
        "At least two identifiers per facility policy, such as name and date of birth",
        [
            "First name spoken across the waiting room",
            "Room number printed on the door alone",
            "A photo on the staff badge of the MA",
        ],
        "Two-identifier verification reduces wrong-patient errors. A single identifier or public name call is insufficient for high-risk processes.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-003
    fact(
        "skill-med-safety",
        "When reading a medication label, which information must be verified against the order?",
        "Drug name, strength, route, and expiration date",
        [
            "Vial cap color matched to the patient's shirt",
            "The manufacturer's stock price",
            "Ambient hallway temperature",
        ],
        "Label checks catch look-alike products and expired stock. Cosmetic features are not reliable identifiers.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-004
    fact(
        "skill-med-safety",
        "Where should documented medication allergies be reviewed in the workflow?",
        "Before selecting or administering any drug, including vaccines and contrast when applicable",
        [
            "After the injection is completed and documented",
            "During annual staff meetings without the patient present",
            "When the patient requests a refill of an unrelated herb",
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
            "Select tablets based on pill shape preference",
            "Give a double dose if the patient missed yesterday",
            "Crush extended-release tablets for easier swallowing without asking",
        ],
        "Name and dose errors are common with oral hypoglycemics. Altering formulation without guidance changes absorption and safety.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-006
    fact(
        "skill-med-safety",
        "Look-alike sound-alike (LASA) medication pairs are managed in part by:",
        "Tall-man lettering, separate storage, and independent double checks when policy requires",
        [
            "Storing all vials in one unlabeled bin",
            "Relying on uniform color for drug class",
            "Removing pharmacy bar codes to speed workflow",
        ],
        "LASA strategies emphasize visual differentiation and deliberate verification. Unlabeled bulk storage increases selection errors.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-007
    fact(
        "skill-med-safety",
        "High-alert medications in ambulatory settings may include insulin and anticoagulants because they:",
        "Carry heightened risk of significant harm when used in error",
        [
            "Are inexpensive and widely available",
            "Require no documentation in the record",
            "May be given without prescriber orders",
        ],
        "High-alert lists focus on harm potential, not cost. Orders and documentation remain mandatory.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-008
    fact(
        "skill-med-safety",
        "Medication reconciliation at an office visit compares:",
        "The patient's home medication list with current orders to find discrepancies",
        [
            "Staff lunch preferences with the formulary",
            "Parking assignments with pharmacy hours",
            "Vital sign trends with supply invoices",
        ],
        "Reconciliation catches omissions, duplications, and dose mismatches across care transitions. Unrelated administrative data do not address drug safety.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-009
    fact(
        "skill-med-safety",
        "When barcode medication administration technology is available, scanning should occur:",
        "For the patient identifier and the specific product before administration when workflow allows",
        [
            "After the dose is injected and discarded",
            "In place of allergy assessment",
            "For cosmetic products in the same cabinet",
        ],
        "Barcode systems add an electronic match step to the rights framework. They supplement rather than replace clinical judgment and allergy review.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-010
    fact(
        "skill-med-safety",
        "A near-miss medication error (caught before reaching the patient) should be:",
        "Reported through the facility incident system to support prevention",
        [
            "Ignored because no harm occurred",
            "Hidden to protect individual staff from review",
            "Posted on public social media for discussion",
        ],
        "Near-miss reporting reveals system weaknesses before patient injury. Transparency supports quality improvement.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-011
    fact(
        "skill-med-safety",
        "Unit-dose packaging in clinic helps reduce errors by:",
        "Providing a single premeasured amount with less manipulation",
        [
            "Eliminating the need for patient identification",
            "Replacing expiration date monitoring",
            "Allowing sharing of partial doses between unrelated patients",
        ],
        "Prepackaged units limit compounding mistakes and contamination. Identity checks and dating remain required.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-012
    fact(
        "skill-med-safety",
        "Topical medication orders should document application site because:",
        "Rotation and absorption depend on accurate placement records",
        [
            "Site choice is irrelevant to effect",
            "Documentation replaces hand hygiene",
            "All topicals may be applied inside the eye without orders",
        ],
        "Site documentation supports efficacy and prevents overlapping toxic doses. Mucosal application requires specific orders.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-013
    fact(
        "skill-med-safety",
        "Controlled substance counts in clinic typically require:",
        "Two staff members per policy when opening, closing, or transferring inventory",
        [
            "A single staff member without witness",
            "Monthly counts without logs",
            "Patient volunteers to hold the logbook",
        ],
        "Dual verification deters diversion and documents chain of custody. Informal handling violates regulatory expectations.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-014
    fact(
        "skill-med-safety",
        "Pediatric liquid dosing should be calculated using:",
        "Milligrams per kilogram from a verified reference and double-checked math",
        [
            "Adult tablet strength for every age",
            "Household tablespoons without conversion",
            "Doubling the dose when the child cries",
        ],
        "Weight-based math prevents tenfold pediatric errors. Volume must be converted using metric devices.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-015
    fact(
        "skill-med-safety",
        "Insulin syringes must match vial concentration because:",
        "U-100 and other concentrations change units per volume",
        [
            "Any syringe mark equals one unit for all products",
            "Concentration is a marketing label without clinical effect",
            "Oral syringes are interchangeable with insulin syringes without training",
        ],
        "Concentration mismatch causes severe hypo- or hyperglycemia. Dedicated insulin syringes are calibrated to labeled strength.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-016
    fact(
        "skill-med-safety",
        "Leading zeros in dosage documentation (for example 0.5 mg) are used to:",
        "Prevent misreading decimal placement on orders and labels",
        [
            "Hide the true dose from pharmacists",
            "Replace metric units with grains",
            "Indicate the medication is cosmetic",
        ],
        "Decimal errors are a frequent source of tenfold mistakes. Standardized writing rules improve clarity.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-017
    fact(
        "skill-med-safety",
        "An unclear abbreviation on a medication order should prompt the MA to:",
        "Contact the prescriber or pharmacist for clarification before preparation",
        [
            "Guess the intended drug based on prior patients",
            "Administer the most common drug in that class",
            "Leave the order blank on the MAR",
        ],
        "Ambiguous abbreviations contributed to historical sentinel events. Clarification is safer than assumption.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-018
    fact(
        "skill-med-safety",
        "Crushing an enteric-coated tablet without authorization can:",
        "Destroy intended release and irritate the stomach or alter dose",
        [
            "Improve controlled release predictably",
            "Remove the need for allergy checks",
            "Convert the drug into a vaccine",
        ],
        "Coatings serve pharmacokinetic and protective roles. Altering formulation requires prescriber or pharmacist guidance.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-019
    fact(
        "skill-med-safety",
        "When two staff perform an independent double-check on a high-alert drug, each person should:",
        "Verify order, product label, dose, route, and patient independently",
        [
            "Watch the other person work without looking at the label",
            "Sign the log before the product is selected",
            "Use the same syringe to save supplies",
        ],
        "Independent checks mean separate cognitive review. Shared observation defeats the purpose.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-020
    fact(
        "skill-med-safety",
        "Medication samples in clinic should be:",
        "Stored, logged, and dispensed per policy with patient education documented",
        [
            "Left in unlocked drawers for self-service",
            "Shared between patients to reduce waste",
            "Given without labeling or expiration review",
        ],
        "Samples are still medications with traceability and counseling requirements. Loose storage invites errors and diversion.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-021
    fact(
        "skill-med-safety",
        "A patient brings herbal supplements to reconciliation. The MA should:",
        "Record product names and doses in the medication list for provider review",
        [
            "Discard the bottles without documentation",
            "Tell the patient herbs are not relevant to care",
            "Add them to the allergy list automatically",
        ],
        "Supplements interact with prescribed drugs and affect perioperative plans. Accurate lists support clinical decisions.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-022
    fact(
        "skill-med-safety",
        "Expired medications found in the exam room should be:",
        "Removed from patient care areas and disposed per pharmaceutical waste policy",
        [
            "Given quickly before the expiration date passes",
            "Mixed into one bottle for inventory simplicity",
            "Sold to staff at discount",
        ],
        "Expired products may lack potency or stability. Proper disposal prevents accidental administration.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-023
    fact(
        "skill-med-safety",
        "Verbal read-back of drug name and dose during a double-check is an example of:",
        "A communication strategy to catch selection errors",
        [
            "A replacement for patient identification",
            "A HIPAA violation in every setting",
            "An optional social conversation",
        ],
        "Read-backs close loops on high-risk tasks. They complement rather than replace identity verification.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-024
    fact(
        "skill-med-safety",
        "Storing potassium chloride vials next to saline flush bags increases risk of:",
        "Wrong solution selection during preparation",
        [
            "Improved refrigeration efficiency",
            "Lower infection rates automatically",
            "Reduced need for labeling",
        ],
        "Physical separation and look-alike labeling strategies reduce swap errors. Storage layout is an active safety control.",
        [S.FDA_MEDICATION_SAFETY],
        "advanced",
    ),
    # skill-med-safety-025
    fact(
        "skill-med-safety",
        "When a patient refuses an ordered medication, documentation should include:",
        "The offer, patient response, and notification of the provider",
        [
            "A fabricated administration time",
            "No note because refusal is unimportant",
            "Another patient's refusal copied forward",
        ],
        "Refusal affects the plan of care and legal record accuracy. Providers need timely notification.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-026
    fact(
        "skill-med-safety",
        "Medication errors discovered after administration require:",
        "Immediate assessment, provider notification, and monitoring per protocol",
        [
            "Waiting until the next scheduled visit",
            "Altering the MAR without telling the team",
            "Discharging without telling the patient",
        ],
        "Post-administration errors may need antidotes or labs. Rapid response limits harm.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-027
    fact(
        "skill-med-safety",
        "Tall-man lettering for hydrALAZINE versus hydrOXYzine highlights:",
        "Dissimilar letter segments within look-alike names",
        [
            "Identical spelling for both drugs",
            "Dose conversion between classes",
            "Insurance billing codes",
        ],
        "Emphasizing unique syllables helps distinguish sound-alike agents during verbal orders and picking.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-028
    fact(
        "skill-med-safety",
        "Barcode scanning mismatch alerts should prompt staff to:",
        "Stop, investigate the discrepancy, and resolve before proceeding",
        [
            "Override without reason to save time",
            "Disable the scanner for the rest of the day",
            "Give the product anyway if the patient is waiting",
        ],
        "Alerts often indicate wrong patient, drug, or expired product. Bypassing without resolution perpetuates risk.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-029
    fact(
        "skill-med-safety",
        "Medication reconciliation after hospital discharge should occur:",
        "At the first follow-up visit and whenever orders change",
        [
            "Once per decade regardless of care changes",
            "When the patient brings no bottles and asks no questions",
            "By deleting home meds from the chart",
        ],
        "Transitions are high risk for omissions and duplications. Repeated reconciliation keeps the list current.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-030
    fact(
        "skill-med-safety",
        "A suspiciously large opioid prescription for a new patient should trigger:",
        "Verification with the prescriber and diversion prevention steps per policy",
        [
            "Automatic dispensing without questions",
            "Sharing tablets among other patients in the clinic",
            "Discarding half the tablets in regular trash",
        ],
        "Diversion and misuse harm patients and communities. Policy-driven verification protects everyone.",
        [S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-031
    fact(
        "skill-med-safety",
        "Pouring liquid medication from a stock bottle into an unlabeled cup risks:",
        "Wrong dose and wrong patient administration",
        [
            "Improved sterility over oral syringes",
            "Elimination of metric measurement",
            "Automatic insurance approval",
        ],
        "Oral syringes and labeled cups support accurate individual doses. Unlabeled containers invite mix-ups.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "beginner",
    ),
    # skill-med-safety-032
    fact(
        "skill-med-safety",
        "Time-critical medications such as certain antibiotics may require:",
        "Administration within prescribed windows documented on the MAR",
        [
            "Random timing without regard to orders",
            "Batching all doses at clinic closing",
            "Withholding doses to extend inventory",
        ],
        "Delayed antimicrobials can worsen outcomes. Scheduled times reflect pharmacodynamic goals.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-033
    fact(
        "skill-med-safety",
        "When preparing medications from multidose vials, the MA should:",
        "Use a new sterile needle and syringe for each entry and follow beyond-use dating",
        [
            "Leave needles embedded in the vial rubber between patients",
            "Store open vials in a personal bag",
            "Share remaining volume with visitors in the waiting room",
        ],
        "Multidose vials require aseptic technique and dating to limit contamination. Embedded needles breach sterility.",
        [S.CDC_INJECTION_SAFETY, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-034
    fact(
        "skill-med-safety",
        "Patient teach-back after new medication counseling helps confirm:",
        "Understanding of dose, route, timing, and side effects to report",
        [
            "The patient's favorite television show",
            "Staff scheduling preferences",
            "Parking validation codes",
        ],
        "Teach-back reveals misunderstandings before the patient leaves. It is a structured safety communication tool.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-035
    fact(
        "skill-med-safety",
        "Wasting partial doses of controlled substances requires:",
        "Witnessed disposal documented per DEA and facility rules",
        [
            "Pouring into the sink without a witness",
            "Taking remnants home for personal use",
            "Combining with another patient's dose",
        ],
        "Witnessed waste maintains chain of custody and prevents diversion. Informal disposal is noncompliant.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-036
    fact(
        "skill-med-safety",
        "A pharmacy label that differs from the electronic order should be resolved by:",
        "Contacting the pharmacist or prescriber before administration",
        [
            "Choosing whichever dose is lower without asking",
            "Giving both strengths sequentially",
            "Removing the label to reduce confusion",
        ],
        "Discrepancies may reflect therapeutic changes or errors. Administration waits on clarification.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-037
    fact(
        "skill-med-safety",
        "High-alert medication storage in clinic often includes:",
        "Locked cabinets, separate bins, and alert stickers per policy",
        [
            "Open shelves in the waiting area",
            "Mixing with office supplies",
            "Removing lot numbers for privacy",
        ],
        "Physical controls add barriers to wrong selection. Lot tracking supports recalls.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
    # skill-med-safety-038
    fact(
        "skill-med-safety",
        "Documenting medication administration should record:",
        "Drug, dose, route, time, site if relevant, and patient response when observed",
        [
            "Staff lunch orders",
            "Unrelated social security numbers in the lobby",
            "A smiley face without drug name",
        ],
        "Complete MAR entries support continuity and error investigation. Vague icons lack clinical detail.",
        [S.NHA_CCMA, S.FDA_MEDICATION_SAFETY],
        "intermediate",
    ),
    # skill-med-safety-039
    fact(
        "skill-med-safety",
        "When using an automated dispensing cabinet override for emergencies, staff must:",
        "Document reason and reconcile inventory afterward per policy",
        [
            "Leave drawers open overnight",
            "Remove tracking labels permanently",
            "Dispense for unauthorized personal use",
        ],
        "Overrides are audited to detect patterns of unsafe bypass. Documentation maintains accountability.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-040
    fact(
        "skill-med-safety",
        "Splitting tablets should occur:",
        "With a pill splitter when the prescriber or reference confirms the product is scored and splittable",
        [
            "Using a kitchen knife on any coated tablet",
            "Crushing enteric products for convenience",
            "Splitting without updating the documented dose",
        ],
        "Uneven halves and destroyed coatings alter exposure. Confirmation prevents sub- or toxic doses.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "intermediate",
    ),
    # skill-med-safety-041
    fact(
        "skill-med-safety",
        "Medication safety huddles at the start of clinic may review:",
        "High-risk patients, look-alike products, and staffing coverage for double checks",
        [
            "Celebrity news without patient relevance",
            "Deleting allergy lists to save time",
            "Disabling barcode scanners to reduce noise",
        ],
        "Brief team reviews align attention on daily risks. Disabling technology removes safeguards.",
        [S.FDA_MEDICATION_SAFETY, S.NHA_CCMA],
        "advanced",
    ),
    # skill-med-safety-042
    fact(
        "skill-med-safety",
        "Returning unopened patient-specific medications to stock without policy approval can cause:",
        "Cross-patient contamination and labeling errors",
        [
            "Guaranteed sterility improvements",
            "Automatic insurance reimbursement",
            "Elimination of reconciliation needs",
        ],
        "Once issued to a patient, products may not meet storage and identity standards for reuse. Policy governs returns.",
        [S.FDA_MEDICATION_SAFETY],
        "beginner",
    ),
]
