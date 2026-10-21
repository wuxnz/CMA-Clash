# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored CCMA questions (topic ccma-vaccines)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ccma-vaccines-001
    fact(
        'ccma-vaccines',
        'When must a Vaccine Information Statement (VIS) be offered for a federally covered vaccine?',
        'Before each dose when a current VIS is required for that vaccine',
        [
            'Only after the patient reports a reaction',
            'Once per lifetime regardless of booster doses',
            'Only when billing commercial insurance',
        ],
        'Federal requirements tie VIS distribution to specific vaccines and doses so patients receive current benefit and risk information. Waiting until after administration or tying VIS solely to billing would not meet informed consent expectations for immunization.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-002
    fact(
        'ccma-vaccines',
        'Which site is most often used for intramuscular vaccines in healthy adults?',
        'Deltoid muscle of the upper arm',
        [
            'Ventrogluteal muscle in newborns only',
            'Plantar surface of the foot',
            'Subcutaneous tissue of the earlobe',
        ],
        'CDC administration guidance lists the deltoid as a standard adult intramuscular site when muscle mass and product labeling support it. Foot, earlobe, and age-inappropriate gluteal choices do not match routine outpatient immunization practice.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-003
    fact(
        'ccma-vaccines',
        'Rotating stock so the soonest-expiring vials are used first is called what?',
        'First-expire, first-out (FEFO) inventory',
        [
            'Last-expire, first-out rotation',
            'Random vial selection from the shelf',
            'Ignoring expiration until a dose is drawn',
        ],
        'FEFO limits wasted doses and reduces the chance of administering expired vaccine. Random selection or prioritizing the newest stock increases the risk that older vials expire on the shelf.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-004
    fact(
        'ccma-vaccines',
        'Per CDC vaccine storage guidance, what should staff record on the refrigerator temperature log at least twice daily?',
        'Minimum and maximum temperatures inside the vaccine storage unit',
        [
            'Only the outdoor weather forecast',
            'Patient copayment amounts collected that day',
            'Staff break schedules',
        ],
        'Twice-daily min/max readings help detect excursions between checks when continuous loggers are not used. Unrelated administrative data does not document cold-chain integrity.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-005
    fact(
        'ccma-vaccines',
        'Why is documenting the vaccine lot number at administration important?',
        'It links the dose to the manufacturer for safety tracking and recalls',
        [
            'It replaces the need to record route and site',
            'It is collected only for cosmetic charting',
            'It allows vials to be used after expiration',
        ],
        'Lot numbers identify production batches if safety alerts or recalls occur. Lot data supports traceability but does not replace full administration documentation or override expiration rules.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-006
    fact(
        'ccma-vaccines',
        'After giving a vaccine, which documentation best supports registry reporting and medicolegal records?',
        'Vaccine product, lot number, site, route, and VIS or education when applicable',
        [
            'Patient nickname only',
            'Billing code without clinical details',
            'No entry when the clinic is busy',
        ],
        'Complete immunization records enable state registries, continuity of care, and investigation of adverse events. Sparse or absent documentation breaks the chain needed for accurate patient histories.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-007
    fact(
        'ccma-vaccines',
        'A patient develops diffuse hives, wheezing, and hypotension within minutes of a vaccine. What is the priority intervention?',
        'Give epinephrine immediately and activate emergency response per protocol',
        [
            'Observe in the waiting room without medication',
            'Give oral antihistamine alone and send the patient home',
            'Document the reaction and schedule a follow-up next week',
        ],
        'Anaphylaxis after vaccination is a medical emergency treated with prompt epinephrine and emergency care. Antihistamines alone or delayed treatment can allow progression to airway compromise or shock.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-008
    fact(
        'ccma-vaccines',
        'Before administering an injectable vaccine, what should the medical assistant complete?',
        'Verify the six rights of medication administration and inspect the vial for defects',
        [
            'Select any open vial without reading the label',
            'Shake every vaccine vigorously regardless of instructions',
            'Skip identity checks when the patient is familiar',
        ],
        'Medication safety rules apply to immunizations, including correct patient, product, dose, route, time, and documentation. Skipping checks or mishandling vials increases wrong-patient and wrong-product risk.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-009
    fact(
        'ccma-vaccines',
        'What must staff confirm on a vaccine vial immediately before withdrawing a dose?',
        'Expiration date, lot number, and appearance per the package insert',
        [
            'That the vial was stored with employee lunches',
            'That any diluent from another manufacturer may be added',
            'That particulates disappear if the vial is shaken hard',
        ],
        'Label review catches expired, recalled, or visibly compromised product before it reaches the patient. Mixing unrelated diluents or ignoring appearance can inactivate vaccine or harm the recipient.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-010
    fact(
        'ccma-vaccines',
        'A staff member draws vaccine into a syringe for one patient. Who should give that dose when clinic policy allows?',
        'The person who prepared or opened the syringe for that patient when feasible',
        [
            'Any clinician who did not prepare the dose',
            'A second patient to save supplies',
            'No one; leave the syringe uncapped on the counter overnight',
        ],
        'One needle, one syringe, only one time aligns with injection safety and reduces cross-contamination. Sharing prepared syringes between patients or leaving them unsecured violates basic infection control.',
        [S.CDC_INJECTION_SAFETY, S.CDC_ONE_AND_ONLY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-011
    fact(
        'ccma-vaccines',
        'During inspection, a vaccine vial shows cracked glass. What is the correct action?',
        'Do not administer the vaccine; isolate the vial and report per policy',
        [
            'Filter the liquid through cotton and administer',
            'Shake the vial and proceed if the crack is small',
            'Dilute with sterile water to dissolve glass fragments',
        ],
        'Cracked vials may leak, become non-sterile, or shed glass into the dose. Damaged containers are removed from use and handled according to facility and program waste procedures.',
        [S.CDC_VACCINE_ADMIN, S.CDC_INJECTION_SAFETY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-012
    fact(
        'ccma-vaccines',
        'A vaccine vial appears cloudy, the wrong color, or contains floating particles. What should staff do?',
        'Discard or quarantine per policy and do not administer the dose',
        [
            'Administer a half dose to limit exposure',
            'Store at room temperature until particles settle',
            'Mix with diluent and use if the color lightens',
        ],
        'Visible abnormalities suggest contamination, improper storage, or the wrong product. Suspect vials are not given to patients until the manufacturer or immunization program confirms otherwise.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-013
    fact(
        'ccma-vaccines',
        'When policy requires labeling a syringe after vaccine is drawn, what information should the label include?',
        'Vaccine name, dose, date, and time of preparation',
        [
            'Only the preparer\'s initials in an unshared code',
            'The patient\'s full Social Security number on the barrel',
            'No label if the dose will be given within the hour',
        ],
        'Syringe labeling reduces wrong-drug errors when multiple injections are prepared. Identifiers belong in the chart under privacy rules, not on small labels that could be misread or lost.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-014
    fact(
        'ccma-vaccines',
        'Staff discover a frozen vaccine product thawed in the refrigerator. How should it be managed?',
        'Follow manufacturer and immunization program guidance, which often includes discarding the vials',
        [
            'Refreeze all vials to restore potency',
            'Use the vials if they still feel cool to the touch',
            'Combine thawed vaccine with new stock without labeling',
        ],
        'Freezing or uncontrolled thawing can destroy live or adjuvanted products. Program consultants help decide whether doses remain viable instead of assuming refrigeration alone saved potency.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-015
    fact(
        'ccma-vaccines',
        'A parent asks when they will receive the Vaccine Information Statement before their child\'s shots. What is the correct timing when a VIS is required?',
        'Before vaccination with the current edition for that vaccine',
        [
            'After all injections are complete',
            'Only if the parent requests a paper copy years later',
            'Replaced by informal online forums',
        ],
        'VIS materials support informed consent before immunization. Providing them only after doses are given or substituting unverified sources does not meet federal expectations for covered vaccines.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-016
    fact(
        'ccma-vaccines',
        'How should vaccine refrigerator temperatures be monitored per the CDC storage toolkit?',
        'In degrees Celsius with calibrated thermometers or continuous digital data loggers',
        [
            'By staff estimate without a thermometer',
            'In Fahrenheit only with no conversion records',
            'By checking the clinic parking lot thermometer',
        ],
        'CDC ranges and excursion thresholds are defined in Celsius for vaccine refrigerators. Calibrated probes or loggers provide auditable data; guesswork cannot prove the cold chain stayed in range.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-017
    fact(
        'ccma-vaccines',
        'How should expired or unused vaccine doses be handled in the clinic?',
        'Document the waste and dispose per facility and immunization program policy',
        [
            'Pour remaining liquid down the sink',
            'Offer doses to staff as personal supplies',
            'Pool partial doses into one syringe for the next patient',
        ],
        'Waste documentation supports inventory accountability and vaccine program reporting. Improper disposal or dose pooling risks contamination and breaks injection safety rules.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-018
    fact(
        'ccma-vaccines',
        'Which practice best protects vaccines stored in the clinic refrigerator?',
        'Continuous temperature monitoring with alarms on the storage unit',
        [
            'Storing vials next to uncovered food in a break-room fridge',
            'Keeping vaccines on an open shelf at room temperature',
            'Placing all products in a household freezer',
        ],
        'Monitored units alert staff to excursions before large batches are compromised. Food refrigerators and uncontrolled room storage lack validated temperature maps required for biologics.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-019
    fact(
        'ccma-vaccines',
        'What type of refrigerator is recommended for routine vaccine storage in outpatient settings?',
        'A dedicated, purpose-built or pharmacy-grade unit with temperature monitoring',
        [
            'Any dorm-style refrigerator shared with lunches',
            'An unplugged unit used only during business hours',
            'A vehicle glove compartment during summer',
        ],
        'Purpose-built units maintain stable temperatures away from frequent door openings that occur with food storage. Improvised locations cannot reliably keep vaccines within labeled ranges.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-020
    fact(
        'ccma-vaccines',
        'For intramuscular vaccination, how should needle length be chosen?',
        'Long enough for the patient\'s size to reach muscle at the selected site',
        [
            'Short enough to stay only in subcutaneous tissue for every product',
            'Identical length for neonates and large adults without adjustment',
            'Based solely on whichever syringe is already open',
        ],
        'Needle length and site selection follow patient age, weight, and product labeling so antigen reaches muscle. Using one length for all patients or staying superficial can reduce immunogenicity.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-021
    fact(
        'ccma-vaccines',
        'After a multidose vaccine vial is opened, what infection control practices are required?',
        'Aseptic technique and adherence to beyond-use dating on the label',
        [
            'Leave a used needle inserted in the stopper between patients',
            'Share one syringe after changing only the needle',
            'Store the open vial indefinitely without a date',
        ],
        'Repeated entry increases contamination risk, so sterile technique and manufacturer beyond-use times apply. Reusing syringes or needles between patients violates fundamental injection safety.',
        [S.CDC_INJECTION_SAFETY, S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-022
    fact(
        'ccma-vaccines',
        'A medical assistant sustains a needlestick after giving a vaccine. What is the required response?',
        'Initiate the bloodborne pathogen exposure protocol per OSHA and facility policy',
        [
            'Ignore small-bore sticks if the skin barely breaks',
            'Continue working without reporting to save time',
            'Wait until the end of the month to document',
        ],
        'OSHA requires evaluation, source-patient testing when indicated, and follow-up after sharps injuries. Delayed or omitted reporting can miss post-exposure prophylaxis windows.',
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-023
    fact(
        'ccma-vaccines',
        'Why is drawing vaccine doses at the point of administration preferred in many clinics?',
        'It shortens time out of cold storage and lowers preparation errors',
        [
            'It eliminates the need for hand hygiene',
            'It removes the requirement for informed consent',
            'It allows skipping lot number documentation',
        ],
        'Just-in-time preparation keeps vials in the refrigerator until needed and pairs drawing with immediate verification. It does not waive consent, documentation, or standard precautions.',
        [S.CDC_VACCINE_STORAGE, S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-024
    fact(
        'ccma-vaccines',
        'When reconstituting a lyophilized vaccine, which diluent is acceptable?',
        'Only the diluent supplied by the manufacturer for that vaccine',
        [
            'Any saline vial found in the treatment room',
            'Tap water from the sink',
            'Leftover intravenous fluids from another patient',
        ],
        'Incorrect diluent volume or type can inactivate antigen or change osmolarity. Manufacturers pair specific diluents with each lyophilized product in the package insert.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-025
    fact(
        'ccma-vaccines',
        'Can multiple inactivated vaccines be administered during the same visit?',
        'Yes, generally at different anatomical sites per the immunization schedule',
        [
            'No, inactivated vaccines may never be given the same day',
            'Yes, but only if mixed in one syringe',
            'No, unless doses are separated by twelve months',
        ],
        'ACIP schedules routinely allow same-day inactivated vaccines at separate sites to improve coverage. Combining unrelated products in one syringe is not standard unless explicitly labeled for combination.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-026
    fact(
        'ccma-vaccines',
        'A patient becomes pale and faints right after vaccination. What is the first management step?',
        'Lay the patient supine, protect from injury, and monitor per protocol',
        [
            'Escort the patient to drive home immediately',
            'Ignore the episode if vitals normalize quickly',
            'Withhold all future vaccines without medical review',
        ],
        'Syncope can occur with any injection; supine positioning reduces fall injury and supports perfusion. Observation after vaccination follows clinic policy and may include timing based on patient risk.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-027
    fact(
        'ccma-vaccines',
        'The anterolateral thigh is a preferred intramuscular site for which group?',
        'Infants and young children when labeling allows that site',
        [
            'Healthy adults receiving influenza vaccine only in the thigh',
            'Patients who require intradermal TB testing in the thigh',
            'Anyone regardless of age for every intramuscular product',
        ],
        'Large muscle mass in the anterolateral thigh accommodates pediatric IM vaccines per CDC site guidance. Adults more often receive deltoid injections unless product directions specify otherwise.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-028
    fact(
        'ccma-vaccines',
        'Where is the deltoid intramuscular injection site located on the upper extremity?',
        'Lateral upper arm over the deltoid muscle belly',
        [
            'Medial antecubital fossa over superficial veins',
            'Plantar arch of the foot',
            'Over the ischial tuberosity in the buttocks for every adult dose',
        ],
        'The deltoid site targets the thick lateral shoulder muscle used for many adult vaccines. Antecubital veins are for venipuncture, and gluteal sites are selected for specific products and sizes, not universal adult use.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-029
    fact(
        'ccma-vaccines',
        'Vaccines must be moved from one clinic to another for a community outreach event. What transport setup is required?',
        'Validated containers with temperature monitoring during transit',
        [
            'A plain paper bag without ice or probes',
            'A cooler shared with ice cream and sandwiches',
            'An unmonitored vehicle trunk for several days',
        ],
        'Validated transport maintains the cold chain with documented temperatures for program accountability. Food coolers and prolonged unmonitored storage invite excursions that ruin potency.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-030
    fact(
        'ccma-vaccines',
        'During inter-facility vaccine shipment, what equipment helps prove temperatures stayed in range?',
        'A digital data logger recording conditions throughout transport',
        [
            'Verbal assurance that the driver drove quickly',
            'A standard food thermometer checked once at delivery',
            'No monitoring because cold packs are present',
        ],
        'Data loggers create a continuous record for immunization programs to review after transit. Single-point or absent monitoring cannot show whether vials warmed during delays or loading.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-031
    fact(
        'ccma-vaccines',
        'What is a primary purpose of scheduled vaccine inventory audits?',
        'Reconcile doses administered, wastage, and upcoming expirations',
        [
            'Hide discrepancies from the state immunization program',
            'Eliminate lot tracking to speed documentation',
            'Stop ordering until all shelves are empty',
        ],
        'Audits align physical stock with records so clinics reorder appropriately and retire expiring vials. Concealing shrinkage undermines vaccine accountability and patient safety.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-032
    fact(
        'ccma-vaccines',
        'The vaccine refrigerator alarm indicates temperatures were out of range overnight. What should staff do first?',
        'Document the excursion and contact the immunization coordinator per CDC steps',
        [
            'Discard every vial immediately without review',
            'Assume potency is fine if the unit feels cold',
            'Turn off the alarm and take no further action',
        ],
        'CDC toolkit workflows require recording min/max or logger data and seeking guidance before administering potentially compromised doses. Blanket discard without review may waste viable vaccine; ignoring alarms risks giving ineffective product.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-033
    fact(
        'ccma-vaccines',
        'Minutes after vaccination, a patient has stridor, wheezing, and a blood pressure of 80/50 mmHg. Which treatment is essential?',
        'Intramuscular epinephrine and emergency activation per anaphylaxis protocol',
        [
            'Oral diphenhydramine alone as definitive therapy',
            'Observation without medication for twenty-four hours',
            'Discharge home if the rash is only on the arms',
        ],
        'Anaphylaxis requires rapid epinephrine and emergency care because symptoms can progress quickly. Antihistamines and passive observation do not reliably reverse airway edema or shock.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-034
    fact(
        'ccma-vaccines',
        'A vaccine carton includes a manufacturer-packaged diluent vial. How must that diluent be used?',
        'Only to reconstitute the matching vaccine named on both labels',
        [
            'With any lyophilized vaccine needing liquid',
            'After open storage for months without a beyond-use date',
            'Shared between clinics without maintaining cold chain',
        ],
        'Diluent type and volume are validated for a specific antigen presentation. Substituting diluents or mishandling open vials can reduce potency or introduce contamination.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-035
    fact(
        'ccma-vaccines',
        'A patient reports a history of egg allergy before routine immunization. What should guide the medical assistant\'s screening?',
        'Current ACIP vaccine-specific contraindications and precautions',
        [
            'Defer all vaccines permanently for any egg mention',
            'Skip allergy history because vaccines contain no protein',
            'Substitute oral home remedies for every injection',
        ],
        'Egg-related recommendations differ by product; for example, influenza guidance has evolved while other vaccines have distinct rules. Blanket deferral without product review can leave patients under-immunized.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-036
    fact(
        'ccma-vaccines',
        'Where should clinically significant post-vaccination adverse events be reported when appropriate?',
        'The Vaccine Adverse Event Reporting System (VAERS)',
        [
            'Only on personal social media accounts',
            'Nowhere because vaccine reactions are not tracked',
            'The patient\'s neighbors for informal monitoring',
        ],
        'VAERS is the national early-warning system used to detect possible safety signals. Formal reporting complements clinical documentation and does not replace medical evaluation of the patient.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-037
    fact(
        'ccma-vaccines',
        'Vials were stored at an undocumented out-of-range temperature. What must occur before any dose is given?',
        'Label and quarantine the vials and consult immunization program guidance',
        [
            'Administer doses quickly before potency might decline further',
            'Return vials to the shipping box without a temperature record',
            'Mix affected vials with unaffected stock to average temperature',
        ],
        'Quarantine prevents use of potentially compromised vaccine until viability is determined. Administering or blending vials without review risks ineffective immunization.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-038
    fact(
        'ccma-vaccines',
        'Live attenuated intranasal influenza vaccine is generally avoided in which patients?',
        'Those who are severely immunocompromised per product labeling and ACIP guidance',
        [
            'Every adult older than sixty-five years regardless of health',
            'Anyone treated for uncomplicated hypertension',
            'Anyone who wears prescription eyeglasses',
        ],
        'Live intranasal vaccines replicate in mucosa and carry contraindications in significant immunosuppression. Age or common chronic conditions alone are not automatic exclusions without reviewing current product guidance.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-039
    fact(
        'ccma-vaccines',
        'Live attenuated injectable or mucosal vaccines are usually withheld from which patients unless a specialist directs otherwise?',
        'Patients with severe immunosuppression or certain immunocompromising therapies',
        [
            'All patients older than sixty-five years',
            'Patients with well-controlled hypertension',
            'Patients who wear contact lenses',
        ],
        'Replication of live vaccines can be dangerous in profound immunocompromise. Many older or chronically ill patients still receive live vaccines when immune function is adequate per schedule guidance.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-040
    fact(
        'ccma-vaccines',
        'Staff use a new needle and syringe for each entry into a multidose vial. What additional rules still apply?',
        'Maintain aseptic technique and observe manufacturer beyond-use dating after opening',
        [
            'Pool leftover partial doses into one syringe for multiple patients',
            'Store the open vial at room temperature indefinitely',
            'Reuse the same needle on the next patient after alcohol wipe',
        ],
        'Sterile technique and dated multidose vials limit bacterial contamination even when needles are changed. Pooling doses or reusing needles between patients remains prohibited.',
        [S.CDC_INJECTION_SAFETY, S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-041
    fact(
        'ccma-vaccines',
        'After a vaccine is reconstituted, how long may it remain usable?',
        'Only within the stability period stated in the package insert',
        [
            'Indefinitely if kept at room temperature',
            'Until visible mold appears on the vial rim',
            'Until the next calendar year if refrigerated',
        ],
        'Each product has a defined use-by window once diluent is added. Exceeding labeled times or ignoring storage conditions can administer antigen that is degraded or unsafe.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-042
    fact(
        'ccma-vaccines',
        'How is recombinant zoster vaccine (Shingrix) given per current ACIP recommendations?',
        'Intramuscularly as a two-dose series at the recommended interval',
        [
            'Orally with the first meal of the day',
            'Intradermally as a single lifetime dose in infancy',
            'Subcutaneously once without a booster',
        ],
        'Shingrix is an adjuvanted recombinant product given IM in two doses for adults per immunization schedules. Oral or pediatric single-dose schemes do not match labeled administration.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-043
    fact(
        'ccma-vaccines',
        'When relocating vaccines between buildings on the same campus, what must accompany the shipment?',
        'Validated transport materials and a temperature record for the trip',
        [
            'Only a handwritten note that the cooler felt cold',
            'Ice packs without a thermometer or data logger',
            'Open transfer on a loading dock for several hours unmonitored',
        ],
        'Even short moves can warm vials if doors stay open or packs fail; documentation shows the cold chain stayed intact. Unmonitored transfers cannot support decisions about dose viability.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
]
