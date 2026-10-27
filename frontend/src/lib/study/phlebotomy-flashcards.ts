// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

// Phlebotomy flashcards transcribed from the course handouts (8 pages). Website URLs and
// blank underline marks from the handouts are dropped. Repeated terms are merged; the most
// complete definition is kept. t = term, d = definition, c = category index.

export const FLASHCARD_CATEGORIES = [
	'Core terms',
	'Veins and sites',
	'Equipment and supplies',
	'Tubes and additives',
	'Specimen handling',
	'Lab and clinical',
	'Abbreviations',
	'Word parts'
];

export interface Flashcard {
	t: string;
	d: string;
	c: number;
}

export const FLASHCARDS: Flashcard[] = [
	// Core terms
	{ t: 'Phlebotomy', d: 'The process of drawing blood from a patient for laboratory testing.', c: 0 },
	{ t: 'Venipuncture', d: 'Puncturing a vein to obtain a blood sample, typically using a needle and collection tube.', c: 0 },
	{ t: 'Capillary puncture', d: 'Fingerstick or heelstick used for small blood samples.', c: 0 },
	{ t: 'Syringe method', d: 'Blood draw using a syringe instead of a vacuum tube.', c: 0 },
	{ t: 'Hemostasis', d: "The body's process of stopping bleeding.", c: 0 },
	{ t: 'Hemoconcentration', d: 'Increased analyte concentration from prolonged tourniquet use.', c: 0 },
	{ t: 'Hematology', d: 'Study of blood cells.', c: 0 },
	{ t: 'Coagulation', d: 'Study of clotting processes.', c: 0 },
	{ t: 'Erythrocyte', d: 'Red blood cell.', c: 0 },
	{ t: 'Leukocyte', d: 'White blood cell; involved in immune response.', c: 0 },
	{ t: 'Thrombocyte', d: 'Platelet; involved in clotting.', c: 0 },

	// Veins and sites
	{ t: 'Vein', d: 'A blood vessel carrying deoxygenated blood back to the heart; primary target for venipuncture.', c: 1 },
	{ t: 'Artery', d: 'A blood vessel carrying oxygenated blood away from the heart; should be avoided during venipuncture.', c: 1 },
	{ t: 'Capillary', d: 'The smallest blood vessels; used for capillary puncture when small blood volumes are needed.', c: 1 },
	{ t: 'Antecubital fossa', d: 'Inner elbow area containing major veins used for venipuncture.', c: 1 },
	{ t: 'Median cubital vein', d: 'Most commonly used vein due to size and stability. Preferred vein for venipuncture.', c: 1 },
	{ t: 'Cephalic vein', d: 'Located on the thumb side (lateral side of the arm); second-choice site.', c: 1 },
	{ t: 'Basilic vein', d: 'Located on the pinky side; third-choice vein, used cautiously due to proximity to nerves and arteries.', c: 1 },

	// Equipment and supplies
	{ t: 'Tourniquet', d: 'Device applied to the upper arm to make veins more prominent. Limit to under 60 seconds.', c: 2 },
	{ t: 'Needle gauge', d: 'Size of the needle bore; higher gauge = thinner needle (e.g., 23G).', c: 2 },
	{ t: 'Bevel', d: 'Slanted tip of a needle; should face upward during venipuncture.', c: 2 },
	{ t: 'Vacutainer', d: 'Vacuum-sealed tube system for collecting blood.', c: 2 },
	{ t: 'Butterfly needle', d: 'Winged infusion set used for small or fragile veins.', c: 2 },
	{ t: 'Centrifuge', d: 'Machine that spins blood to separate its components.', c: 2 },

	// Tubes and additives
	{ t: 'Additive', d: 'Substance in collection tubes (e.g., anticoagulants, clot activators).', c: 3 },
	{ t: 'Anticoagulant', d: 'Prevents blood clotting (e.g., EDTA, citrate, heparin).', c: 3 },
	{ t: 'EDTA', d: 'Anticoagulant that binds calcium; found in lavender tubes; used for CBC.', c: 3 },
	{ t: 'Sodium citrate', d: 'Light blue tube; coagulation studies.', c: 3 },
	{ t: 'Heparin', d: 'Green tube; chemistry tests.', c: 3 },
	{ t: 'Serum separator tube (SST)', d: 'Gold or tiger-top tube; contains a gel separator. Clot activator plus gel; yields serum.', c: 3 },
	{ t: 'Plasma', d: 'Liquid portion of anticoagulated blood containing clotting factors.', c: 3 },
	{ t: 'Serum', d: 'Liquid portion after clotting; lacks clotting factors.', c: 3 },
	{ t: 'Plasma separator tube (PST)', d: 'Mint green tube; lithium heparin plus gel; yields plasma.', c: 3 },
	{ t: 'ETS (Evacuated Tube System)', d: 'Closed-system collection (e.g., BD Vacutainer).', c: 3 },
	{ t: 'SPS (Sodium Polyanethol Sulfonate)', d: 'Yellow blood culture tube additive.', c: 3 },
	{ t: 'ACD (Acid Citrate Dextrose)', d: 'Yellow top for HLA typing and DNA studies. Also an anticoagulant in the tube list.', c: 3 },
	{ t: 'NaF (Sodium Fluoride)', d: 'Gray tube; glycolytic inhibitor.', c: 3 },
	{ t: 'KOx (Potassium Oxalate)', d: 'Gray tube anticoagulant.', c: 3 },
	{ t: 'Na citrate (Sodium Citrate)', d: 'Light blue tube for coagulation; black for ESR.', c: 3 },
	{ t: 'Li Hep (Lithium Heparin)', d: 'Green tubes; anticoagulant.', c: 3 },

	// Specimen handling
	{ t: 'Order of draw', d: 'Sequence to prevent additive contamination.', c: 4 },
	{ t: 'Basal state', d: 'Resting metabolic state after a 12-hour fast; ideal for many tests and accurate labs.', c: 4 },

	// Lab and clinical
	{ t: 'CBC (Complete Blood Count)', d: 'Test evaluating RBCs, WBCs, and platelets.', c: 5 },
	{ t: 'Blood culture', d: 'Test to detect bacteria or fungi in the bloodstream.', c: 5 },
	{ t: 'Anemia', d: 'Low RBC or hemoglobin levels causing fatigue and pallor.', c: 5 },
	{ t: 'Cyanotic', d: 'Bluish skin or discoloration due to lack of oxygen.', c: 5 },
	{ t: 'Edema', d: 'Fluid accumulation causing swelling; avoid venipuncture in these areas.', c: 5 },
	{ t: 'Anaphylaxis', d: 'Severe allergic reaction; life-threatening.', c: 5 },
	{ t: 'ABO', d: 'Blood group system.', c: 5 },
	{ t: 'AIDS', d: 'Acquired Immunodeficiency Syndrome.', c: 5 },
	{ t: 'Aerobic / Anaerobic', d: 'With oxygen / without oxygen (culture conditions).', c: 5 },

	// Abbreviations
	{ t: 'TID', d: 'Three times daily.', c: 6 },
	{ t: 'QID', d: 'Four times daily.', c: 6 },
	{ t: 'Q4H / Q6H', d: 'Every 4 / 6 hours (and so on).', c: 6 },
	{ t: 'AC / PC', d: 'Before meals / after meals.', c: 6 },
	{ t: 'NPO', d: 'Nothing by mouth.', c: 6 },
	{ t: 'Pt', d: 'Patient.', c: 6 },
	{ t: 'Dx', d: 'Diagnosis.', c: 6 },
	{ t: 'Hx / PMH', d: 'History / past medical history.', c: 6 },
	{ t: 'CC', d: 'Chief complaint.', c: 6 },
	{ t: 'HPI', d: 'History of present illness.', c: 6 },
	{ t: 'BP', d: 'Blood pressure.', c: 6 },
	{ t: 'HR', d: 'Heart rate.', c: 6 },
	{ t: 'RR', d: 'Respiratory rate.', c: 6 },
	{ t: 'SpO2', d: 'Peripheral oxygen saturation.', c: 6 },
	{ t: 'BMI', d: 'Body mass index.', c: 6 },
	{ t: 'ACD', d: 'Acid-citrate-dextrose anticoagulant.', c: 6 },
	{ t: 'CBC', d: 'Complete blood count.', c: 6 },
	{ t: 'BMP', d: 'Basic metabolic panel.', c: 6 },
	{ t: 'CMP', d: 'Comprehensive metabolic panel.', c: 6 },
	{ t: 'LFT', d: 'Liver function tests.', c: 6 },
	{ t: 'PT', d: 'Prothrombin time.', c: 6 },
	{ t: 'PTT / aPTT', d: 'Partial thromboplastin time.', c: 6 },
	{ t: 'INR', d: 'International normalized ratio.', c: 6 },
	{ t: 'TSH', d: 'Thyroid-stimulating hormone.', c: 6 },
	{ t: 'HbA1c', d: 'Glycated hemoglobin A1c.', c: 6 },
	{ t: 'PSA', d: 'Prostate-specific antigen.', c: 6 },
	{ t: 'UA', d: 'Urinalysis.', c: 6 },
	{ t: 'ABG', d: 'Arterial blood gas.', c: 6 },
	{ t: 'STAT', d: 'Immediately.', c: 6 },
	{ t: 'ASAP', d: 'As soon as possible.', c: 6 },
	{ t: 'PRN', d: 'As needed.', c: 6 },
	{ t: 'QD', d: 'Daily.', c: 6 },
	{ t: 'BID', d: 'Twice daily.', c: 6 },

	// Word parts
	{ t: 'Prefix', d: 'Beginning of a word that modifies its meaning (e.g., hypo- = low).', c: 7 },
	{ t: 'Root word', d: 'Core meaning (e.g., hem- / hemat- = blood).', c: 7 },
	{ t: 'Suffix', d: 'Ending that indicates a procedure or condition (e.g., -itis = inflammation).', c: 7 },
	{ t: 'Phlebotomy (word parts)', d: 'phlebo- (vein) + -tomy (cutting) = incision into a vein.', c: 7 }
];
