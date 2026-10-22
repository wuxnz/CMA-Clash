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
        'Before each dose when a current VIS is required',
        [
            'After the patient reports a reaction at the visit',
            'Once in a lifetime regardless of how many booster doses follow',
            'When billing commercial insurance for the dose',
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
            'Ventrogluteal muscle in newborns',
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
            'First-in, first-out rotation without checking expiration dates',
            'Newest-stock-first rotation so recently received vials are used first',
            'Shelf order by manufacturer name without reviewing vial expiration',
        ],
        'FEFO limits wasted doses and reduces the chance of administering expired vaccine. Random selection or prioritizing the newest stock increases the risk that older vials expire on the shelf.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-004
    fact(
        'ccma-vaccines',
        'Per CDC vaccine storage guidance, what should staff record on the refrigerator temperature log at least twice daily?',
        'Minimum and maximum temperatures in the storage unit',
        [
            'The outdoor weather forecast at the clinic',
            'Patient copayment amounts collected in the clinic that day',
            'Staff break schedules for the week',
        ],
        'Twice-daily min/max readings help detect excursions between checks when continuous loggers are not used. A display reading or unrelated administrative data does not document cold-chain integrity.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-005
    fact(
        'ccma-vaccines',
        'Why is documenting the vaccine lot number at administration important?',
        'It links the dose to the maker for safety tracking',
        [
            'It replaces the need to record the route and injection site',
            'It is collected for cosmetic charting purposes',
            'It allows vials to be used after the expiration date',
        ],
        'Lot numbers identify production batches if safety alerts or recalls occur. Lot data supports traceability but does not replace full administration documentation or override expiration rules.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-006
    fact(
        'ccma-vaccines',
        'After giving a vaccine, which documentation best supports registry reporting and medicolegal charting?',
        'Vaccine product, lot number, site, route, and VIS when applicable',
        [
            'Date and route documented, without vaccine product or lot number',
            'CPT code and charge capture without clinical administration details',
            'Verbal confirmation to the patient without a chart entry',
        ],
        'Complete immunization records enable state registries, continuity of care, and investigation of adverse events. Sparse or absent documentation breaks the chain needed for accurate patient histories.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-007
    fact(
        'ccma-vaccines',
        'A patient develops diffuse hives, wheezing, and hypotension within minutes of a vaccine. What is the priority intervention?',
        'Give epinephrine at once and activate emergency response',
        [
            'Observe in the waiting room for thirty minutes without medication',
            'Give oral diphenhydramine and discharge when hives begin to fade',
            'Document the reaction and schedule a clinic follow-up in one week',
        ],
        'Anaphylaxis after vaccination is a medical emergency treated with prompt epinephrine and emergency care. Antihistamines alone or delayed treatment can allow progression to airway compromise or shock.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-008
    fact(
        'ccma-vaccines',
        'Before administering an injectable vaccine, what should the medical assistant complete?',
        'Verify the six rights of administration and inspect the vial',
        [
            'Select an open vial without reading the label',
            'Shake every vaccine vigorously regardless of the product instructions',
            'Omit identity checks when the patient is familiar to staff',
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
            'That expiration may be extended one month when the vial stays refrigerated',
            'That diluent from a different manufacturer lot may be substituted',
            'That visible particulates are acceptable if the vial was shaken',
        ],
        'Label review catches expired, recalled, or visibly compromised product before it reaches the patient. Mixing unrelated diluents or ignoring appearance can inactivate vaccine or harm the recipient.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-010
    fact(
        'ccma-vaccines',
        'A staff member draws vaccine into a syringe for one patient. Who should give that dose when clinic policy allows?',
        'The person who prepared or opened the syringe for that patient',
        [
            'A credentialed colleague who did not draw the dose but checks the label',
            'The front-desk staff member who escorted the patient to the exam room',
            'Whoever finds an unlabeled syringe and matches it to the chart',
        ],
        'One needle, one syringe, only one time aligns with injection safety and reduces cross-contamination. Sharing prepared syringes between patients or leaving them unsecured violates basic infection control.',
        [S.CDC_INJECTION_SAFETY, S.CDC_ONE_AND_ONLY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-011
    fact(
        'ccma-vaccines',
        'During inspection, a vaccine vial shows cracked glass. What is the correct action?',
        'Do not administer the vaccine; isolate the vial and report',
        [
            'Draw the dose through a filter needle and administer immediately',
            'Transfer the vaccine into a sterile syringe and proceed with the injection',
            'Wipe the cracked area with alcohol and use the vial if no leak is visible',
        ],
        'Cracked vials may leak, become non-sterile, or shed glass into the dose. Damaged containers are removed from use and handled according to facility and program waste procedures.',
        [S.CDC_VACCINE_ADMIN, S.CDC_INJECTION_SAFETY, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-012
    fact(
        'ccma-vaccines',
        'A vaccine vial appears cloudy, the wrong color, or contains floating particles. What should staff do?',
        'Discard or quarantine the vial and do not administer the dose',
        [
            'Administer a reduced dose to limit exposure to the abnormal product',
            'Refrigerate overnight and recheck appearance before administering',
            'Add diluent and administer if turbidity clears after mixing',
        ],
        'Visible abnormalities suggest contamination, improper storage, or the wrong product. Suspect vials are not given to patients until the manufacturer or immunization program confirms otherwise.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-013
    fact(
        'ccma-vaccines',
        'When policy requires labeling a syringe after vaccine is drawn, which information should appear on the label?',
        'Vaccine name, dose, date, and time of preparation',
        [
            'The preparer\'s initials in an unshared code',
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
        'Follow manufacturer guidance, which often includes discarding the vials',
        [
            'Refreeze the vials once the internal temperature reads below 36 degrees',
            'Administer thawed doses if the liquid still feels cool when touched',
            'Blend thawed vials with unthawed stock without separate labeling',
        ],
        'Freezing or uncontrolled thawing can destroy live or adjuvanted products. Program consultants help decide whether doses remain viable instead of assuming refrigeration alone saved potency.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-015
    fact(
        'ccma-vaccines',
        'A parent asks when they will receive the Vaccine Information Statement before their child\'s shots. What is the correct timing when a VIS is required?',
        'Before vaccination with the current VIS edition',
        [
            'After all of the injections are complete',
            'If the parent requests a paper copy of the VIS years later',
            'Replaced by informal online forums and blogs',
        ],
        'VIS materials support informed consent before immunization. Providing them only after doses are given or substituting unverified sources does not meet federal expectations for covered vaccines.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-016
    fact(
        'ccma-vaccines',
        'How should vaccine refrigerator temperatures be monitored per the CDC storage toolkit?',
        'In degrees Celsius with calibrated probes or loggers',
        [
            'By staff estimate without using a thermometer',
            'In Fahrenheit with no conversion records kept',
            'Using the wall thermostat reading taken in the front office',
        ],
        'CDC ranges and excursion thresholds are defined in Celsius for vaccine refrigerators. Calibrated probes or loggers provide auditable data; guesswork cannot prove the cold chain stayed in range.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-017
    fact(
        'ccma-vaccines',
        'How should expired or unused vaccine doses be handled in the clinic?',
        'Document the waste and dispose per facility policy',
        [
            'Return partial vials to the refrigerator for the next patient',
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
            'Twice-daily manual checks without continuous monitoring or alarms',
            'Storage in a dorm-style refrigerator shared with staff beverages',
            'Placement on open shelving when the vaccine unit is full',
        ],
        'Monitored units alert staff to excursions before large batches are compromised. Food refrigerators and uncontrolled room storage lack validated temperature maps required for biologics.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-019
    fact(
        'ccma-vaccines',
        'What type of refrigerator is recommended for routine vaccine storage in outpatient settings?',
        'A dedicated, purpose-built unit with monitoring',
        [
            'A dorm-style refrigerator shared with lunches',
            'An unplugged unit kept running during business hours',
            'A vehicle glove compartment during summer months',
        ],
        'Purpose-built units maintain stable temperatures away from frequent door openings that occur with food storage. Improvised locations cannot reliably keep vaccines within labeled ranges.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-020
    fact(
        'ccma-vaccines',
        'For intramuscular vaccination, how should needle length be chosen?',
        "Long enough for the patient's size to reach muscle at the site",
        [
            'Short enough to stay in subcutaneous tissue for every product',
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
        'Aseptic technique and beyond-use dating on the label',
        [
            'Leave a used needle inserted in the stopper between patients',
            'Share one syringe after changing the needle',
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
        'Initiate the bloodborne pathogen exposure protocol per OSHA',
        [
            "Wash the puncture site and continue vaccinating without reporting the injury",
            "Apply a bandage and document at end of shift if symptoms develop",
            "Schedule source-patient blood testing at the patient's next routine visit",
        ],
        'OSHA requires evaluation, source-patient testing when indicated, and follow-up after sharps injuries. Delayed or omitted reporting can miss post-exposure prophylaxis windows.',
        [S.OSHA_BBP, S.OSHA_NEEDLESTICK, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-023
    fact(
        'ccma-vaccines',
        'Why is drawing vaccine doses at the point of administration preferred in many clinics?',
        'It shortens time out of cold storage and lowers preparation errors',
        [
            'It removes the need for hand hygiene between consecutive injections',
            'It waives informed consent when the immunization schedule is busy',
            'It defers lot number documentation until the end of the clinic session',
        ],
        'Just-in-time preparation keeps vials in the refrigerator until needed and pairs drawing with immediate verification. It does not waive consent, documentation, or standard precautions.',
        [S.CDC_VACCINE_STORAGE, S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-024
    fact(
        'ccma-vaccines',
        'When reconstituting a lyophilized vaccine, which diluent is acceptable?',
        'The diluent supplied by the manufacturer for that vaccine',
        [
            "A 0.9% sodium chloride vial opened in the treatment room",
            "Sterile water for injection from a different vaccine kit",
            "Bacteriostatic saline drawn from another patient's IV bag",
        ],
        'Incorrect diluent volume or type can inactivate antigen or change osmolarity. Manufacturers pair specific diluents with each lyophilized product in the package insert.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-025
    fact(
        'ccma-vaccines',
        'Can multiple inactivated vaccines be administered during the same visit?',
        'Yes, generally at different sites per the immunization schedule',
        [
            'No, inactivated vaccines may not be given on the same clinic day',
            'Yes, but if mixed in one syringe',
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
        'Lay the patient supine, protect from injury, and monitor closely',
        [
            'Have the patient sit upright and drive home once skin color returns',
            'Document the episode and resume vaccines without physician review',
            'Obtain standing orders to defer all future injections permanently',
        ],
        'Syncope can occur with any injection; supine positioning reduces fall injury and supports perfusion. Observation after vaccination follows clinic policy and may include timing based on patient risk.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-027
    fact(
        'ccma-vaccines',
        'The anterolateral thigh is a preferred intramuscular site for which group?',
        'Infants and young children when labeling allows the thigh',
        [
            'Healthy adults receiving the influenza vaccine in the thigh',
            'Patients who require intradermal TB testing in the thigh',
            'Anyone regardless of age for every intramuscular product',
        ],
        'Large muscle mass in the anterolateral thigh accommodates pediatric IM vaccines per CDC site guidance. Adults more often receive deltoid injections unless product directions specify otherwise.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-028
    fact(
        'ccma-vaccines',
        'Where is the deltoid intramuscular injection site located on the upper extremity?',
        'Lateral upper arm over the deltoid muscle belly',
        [
            'Volar forearm at the antecubital crease for adult influenza doses',
            'Posterior upper arm over the triceps insertion for routine vaccines',
            'Ventrogluteal muscle in the buttock for every adult intramuscular dose',
        ],
        'The deltoid site targets the thick lateral shoulder muscle used for many adult vaccines. Antecubital veins are for venipuncture, and gluteal sites are selected for specific products and sizes, not universal adult use.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-029
    fact(
        'ccma-vaccines',
        'Vaccines must be moved from one clinic to another for a community outreach event. What transport setup is required?',
        'Validated containers with temperature monitoring during transit',
        [
            'Insulated transport without calibrated temperature monitoring during the drive',
            'Household cooler with ice packs but no probe or data logger',
            'Clinic refrigerator unplugged and carried in a passenger seat',
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
            'Driver oral report that transit took less than thirty minutes',
            'Single food-service probe reading taken when the shipment arrives',
            'Cold-pack presence alone without temperature documentation',
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
            'Match records to state registry reports without counting physical vials',
            'Track expiration dates while omitting lot numbers from the inventory log',
            'Order replacement stock before reconciling on-hand doses with wastage',
        ],
        'Audits align physical stock with records so clinics reorder appropriately and retire expiring vials. Concealing shrinkage undermines vaccine accountability and patient safety.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-032
    fact(
        'ccma-vaccines',
        'The vaccine refrigerator alarm indicates temperatures were out of range overnight. What should staff do first?',
        'Document the excursion and contact the immunization coordinator',
        [
            'Discard every vial in the unit immediately without reviewing logger data',
            'Resume use if the refrigerator door feels cold when opened in the morning',
            'Reset the alarm and continue dosing without contacting the coordinator',
        ],
        'CDC toolkit workflows require recording min/max or logger data and seeking guidance before administering potentially compromised doses. Blanket discard without review may waste viable vaccine; ignoring alarms risks giving ineffective product.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-033
    fact(
        'ccma-vaccines',
        'Minutes after vaccination, a patient has stridor, wheezing, and a blood pressure of 80/50 mmHg. Which treatment is essential?',
        'Intramuscular epinephrine and emergency activation at once',
        [
            'Oral diphenhydramine alone as the definitive therapy',
            'Observation without medication for a full twenty-four hours',
            'Discharge home if the rash is limited to the arms',
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
            'To dilute a lyophilized vaccine from a different manufacturer',
            'After the open diluent vial has been at room temperature for several weeks',
            'Shared between clinic sites without cold-chain documentation during transfer',
        ],
        'Diluent type and volume are validated for a specific antigen presentation. Substituting diluents or mishandling open vials can reduce potency or introduce contamination.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-035
    fact(
        'ccma-vaccines',
        'A patient reports a history of egg allergy before routine immunization. What should guide the medical assistant\'s screening?',
        'Current ACIP guidance for that specific product',
        [
            'Defer all vaccines permanently for an egg mention',
            'Omit allergy history because the vaccine contains no protein',
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
            'In the patient chart without reporting to the immunization safety system',
            'Nowhere because vaccine reactions are not tracked',
            'To the vaccine manufacturer sales representative who visited last month',
        ],
        'VAERS is the national early-warning system used to detect possible safety signals. Formal reporting complements clinical documentation and does not replace medical evaluation of the patient.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-037
    fact(
        'ccma-vaccines',
        'Vials were stored at an undocumented out-of-range temperature. What must occur before any dose is given?',
        'Label and quarantine the vials, then consult program guidance',
        [
            'Administer doses quickly before potency might decline further',
            'Return vials to the shipping carton without recording excursion data',
            'Mix affected vials with unaffected stock to average storage temperature',
        ],
        'Quarantine prevents use of potentially compromised vaccine until viability is determined. Administering or blending vials without review risks ineffective immunization.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-038
    fact(
        'ccma-vaccines',
        'Live attenuated intranasal influenza vaccine is generally avoided in which patients?',
        'Those who are severely immunocompromised per ACIP guidance',
        [
            'Healthy adults aged fifty to sixty-four with no chronic conditions',
            'Patients with mild seasonal allergic rhinitis not on immunosuppression',
            'Persons receiving inactivated injectable influenza vaccine the same day',
        ],
        'Live intranasal vaccines replicate in mucosa and carry contraindications in significant immunosuppression. Age or common chronic conditions alone are not automatic exclusions without reviewing current product guidance.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-039
    fact(
        'ccma-vaccines',
        'Live attenuated injectable or mucosal vaccines are usually withheld from which patients unless a specialist directs otherwise?',
        'Patients with severe immunosuppression or immunocompromising therapies',
        [
            'All adults sixty-five or older regardless of immune status',
            'Patients with controlled type 2 diabetes without immunosuppressing therapy',
            'Patients receiving inactivated injectable vaccines during the same visit',
        ],
        'Replication of live vaccines can be dangerous in profound immunocompromise. Many older or chronically ill patients still receive live vaccines when immune function is adequate per schedule guidance.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-040
    fact(
        'ccma-vaccines',
        'Staff use a new needle and syringe for each entry into a multidose vial. What additional rules still apply?',
        'Maintain aseptic technique and observe beyond-use dating after opening',
        [
            'Pool leftover partial doses into one syringe for the next scheduled patient',
            'Store the open vial at room temperature until the multidose lot expires',
            'Reuse the same needle on the next patient after wiping with alcohol',
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
            'For twenty-four hours after reconstitution if the vial stays refrigerated',
            'For seven days if the vial cap is replaced between patient draws',
            'Until the manufacturer lot expiration date if the vial remains refrigerated',
        ],
        'Each product has a defined use-by window once diluent is added. Exceeding labeled times or ignoring storage conditions can administer antigen that is degraded or unsafe.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-042
    fact(
        'ccma-vaccines',
        'How is recombinant zoster vaccine (Shingrix) given per current ACIP recommendations?',
        'Intramuscularly as a two-dose series at the interval',
        [
            'Subcutaneously as a single dose in adults per standing orders',
            'Intramuscularly as one lifetime dose without a second injection',
            'Intradermally in the forearm like a tuberculin skin test',
        ],
        'Shingrix is an adjuvanted recombinant product given IM in two doses for adults per immunization schedules. Oral or pediatric single-dose schemes do not match labeled administration.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-043
    fact(
        'ccma-vaccines',
        'When relocating vaccines between buildings on the same campus, what must accompany the shipment?',
        'Validated transport materials and a temperature record for the trip',
        [
            'A handwritten note that the cooler felt cold',
            'Ice packs without a thermometer or data logger',
            'Open transfer on a loading dock for several hours with no monitoring',
        ],
        'Even short moves can warm vials if doors stay open or packs fail; documentation shows the cold chain stayed intact. Unmonitored transfers cannot support decisions about dose viability.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),

    # ccma-vaccines-044
    fact(
        'ccma-vaccines',
        'Where should most refrigerated vaccines be stored in the clinic?',
        'In a dedicated medical refrigerator with continuous monitoring',
        [
            'In a break-room refrigerator if a probe is placed inside once daily',
            'On a medication cart near a sunny window between patient rooms',
            'In the freezer compartment to extend shelf life beyond product labeling',
        ],
        'CDC storage guidance requires monitored, dedicated units to maintain the cold chain. Food refrigerators and freezing inappropriate products ruin potency.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-045
    fact(
        'ccma-vaccines',
        'Before giving an injectable vaccine, which patient check matches two identifiers to the order?',
        'Match the legal name and date of birth stated by the patient',
        [
            'Match legal name and assigned room number to the order',
            'Match legal name and date of birth printed on the vial label to the order',
            'Match medical record number and vaccine lot number to the order',
        ],
        'Active patient confirmation of name and date of birth catches wrong-chart and wrong-patient errors. Room numbers, vial labels, and lot numbers do not verify the person receiving the dose.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-046
    fact(
        'ccma-vaccines',
        'A vaccine refrigerator alarm shows a temperature of 46°F (8°C) overnight. What is the first step?',
        'Document the event, relocate vaccines, and contact the coordinator',
        [
            'Administer all vials in the unit immediately to avoid wasting doses',
            'Silence the alarm and resume clinic without reviewing temperature data',
            'Move vaccines to the freezer compartment to cool them faster',
        ],
        'Excursions require assessment before use; administering potentially compromised vaccine risks ineffective immunity. Freezing can destroy many products.',
        [S.CDC_VACCINE_STORAGE, S.NHA_CCMA],
        'advanced',
    ),
    # ccma-vaccines-047
    fact(
        'ccma-vaccines',
        'Which documentation is required after administering a vaccine?',
        'Vaccine name, lot number, site, route, and administrator per policy',
        [
            'Vaccine name and date without the lot number or administration site',
            'Insurance authorization number and billing code for the visit',
            'Chief complaint and last visit date copied from the problem list',
        ],
        'Immunization records support recall and adverse event investigation. Nonclinical trivia does not meet registry or legal documentation needs.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'beginner',
    ),
    # ccma-vaccines-048
    fact(
        'ccma-vaccines',
        'What should be done with a multidose vial after the beyond-use date on the label?',
        'Discard the vial even if some liquid remains',
        [
            'Return to the refrigerator if the liquid still appears clear',
            'Pool remaining volume into one syringe for the next scheduled patient',
            'Relabel with a new beyond-use date set by clinic staff',
        ],
        'Opened vials have limited stability to prevent bacterial growth and potency loss. Pooling doses between patients violates injection safety.',
        [S.CDC_INJECTION_SAFETY, S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
    # ccma-vaccines-049
    fact(
        'ccma-vaccines',
        'Why is aspiration generally not recommended during routine vaccine injections?',
        'Vaccines are given intramuscularly away from blood vessels',
        [
            'Aspiration is recommended before every deltoid intramuscular injection',
            'Aspiration increases antigen uptake at the injection site',
            'Aspiration replaces rotating injection sites between doses',
        ],
        'Current CDC administration guidance does not recommend aspiration for standard IM vaccines. Aspiration does not address site rotation or potency.',
        [S.CDC_VACCINE_ADMIN, S.NHA_CCMA],
        'intermediate',
    ),
]
