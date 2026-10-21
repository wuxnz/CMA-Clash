# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Hand-authored EKG questions (topic ekg-rhythm)."""

from __future__ import annotations

from classquiz.seed import sources as S
from classquiz.seed.banks._builder import fact

FACTS: list[dict] = [
    # ekg-rhythm-001
    fact(
        "ekg-rhythm",
        "Which findings on a 12-lead EKG best support normal sinus rhythm in an adult at rest?",
        "Upright P before each QRS, stable PR, rate about 60 to 100 beats per minute",
        [
            "Absent P waves with an irregularly irregular ventricular rhythm",
            "Wide QRS complexes without preceding P waves at a rate of 150",
            "Sawtooth flutter waves between QRS complexes without variation in PR interval",
        ],
        "Normal sinus rhythm shows a sinus-origin P before every QRS with a steady PR. Irregularly irregular rhythm without P waves fits atrial fibrillation, not sinus rhythm.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-rhythm-002
    fact(
        "ekg-rhythm",
        "Which description best matches sinus bradycardia on the EKG?",
        "Normal P-QRS-T morphology with a ventricular rate below 60 beats per minute",
        [
            "Irregularly irregular rhythm without distinct P waves",
            "Narrow complex tachycardia at 150 beats per minute with hidden P waves",
            "Chaotic fibrillatory baseline without organized QRS complexes",
        ],
        "Sinus bradycardia keeps sinus P waves and 1:1 conduction but slows the rate. Irregularly irregular rhythm without P waves indicates atrial fibrillation, not sinus bradycardia.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-rhythm-003
    fact(
        "ekg-rhythm",
        "Which description best matches sinus tachycardia on the EKG?",
        "Upright P waves before each QRS with a ventricular rate above 100 beats per minute",
        [
            "Regular narrow QRS at 180 beats per minute without visible P waves",
            "Irregularly irregular rhythm with fibrillatory baseline",
            "Flat line in all leads with occasional P waves",
        ],
        "Sinus tachycardia retains sinus P waves and conduction while the rate rises. A very fast narrow complex rhythm without P waves suggests supraventricular tachycardia rather than sinus tachycardia.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-rhythm-004
    fact(
        "ekg-rhythm",
        "Which EKG pattern is most characteristic of atrial fibrillation?",
        "Irregular R-R intervals without a repeating P wave before each QRS",
        [
            "Regular sawtooth atrial activity with patterned ventricular conduction throughout the strip",
            "Upright P before every QRS with PR interval stable from beat to beat",
            "Regular wide QRS complexes at about 40 beats per minute with 1:1 P to QRS",
        ],
        "Atrial fibrillation produces chaotic atrial activity and variable ventricular response. Sawtooth flutter waves with regular conduction suggest atrial flutter instead.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-rhythm-005
    fact(
        "ekg-rhythm",
        "Which EKG finding is most suggestive of atrial flutter?",
        "Sawtooth flutter waves in inferior leads with regular or patterned ventricular response",
        [
            "Fine undulating baseline without organized atrial activity and irregular R-R intervals",
            "Progressive PR prolongation until a QRS is dropped",
            "Narrow QRS tachycardia with retrograde P waves buried in the ST segment",
        ],
        "Flutter has organized atrial activity around 250 to 350 per minute with a sawtooth appearance. Fine irregular baseline without P waves fits atrial fibrillation, and progressive PR changes fit Mobitz I block.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-rhythm-006
    fact(
        "ekg-rhythm",
        "How does first-degree atrioventricular block appear on the EKG?",
        "PR interval longer than 0.20 second with every P wave followed by a QRS complex",
        [
            "PR interval that lengthens until a QRS is dropped",
            "P waves and QRS complexes that are completely unrelated",
            "PR interval shorter than 0.12 second with delta waves",
        ],
        "First-degree block delays AV conduction but conducts every beat. Lengthening PR with dropped beats is second-degree block, and AV dissociation is third-degree block.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-rhythm-007
    fact(
        "ekg-rhythm",
        "Which pattern defines Mobitz type I (Wenckebach) second-degree AV block?",
        "Progressive PR prolongation until a P wave is not followed by a QRS, then the cycle repeats",
        [
            "Fixed PR interval with sudden dropped QRS complexes without prior PR lengthening",
            "Complete AV dissociation with more P waves than QRS complexes",
            "PR interval below 0.12 second with slurred upstroke of the QRS",
        ],
        "Mobitz I shows grouped beating as PR stretches until a beat drops. Fixed PR with sudden drops suggests Mobitz II, and independent P and QRS rates suggest complete heart block.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-008
    fact(
        "ekg-rhythm",
        "Which pattern defines Mobitz type II second-degree AV block?",
        "Constant PR interval with intermittent non-conducted P waves and dropped QRS complexes",
        [
            "Progressive PR lengthening before each dropped QRS",
            "Irregularly irregular rhythm without P waves",
            "Wide QRS escape rhythm at 30 beats per minute with no P waves",
        ],
        "Mobitz II keeps a steady PR until a beat fails to conduct, which can progress to complete block. Progressive PR changes point to Mobitz I, not type II.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-009
    fact(
        "ekg-rhythm",
        "What defines third-degree (complete) atrioventricular block on the EKG?",
        "P waves and QRS complexes occur at independent rates with no consistent PR relationship",
        [
            "PR interval greater than 0.20 second with 1:1 conduction",
            "Dropped QRS after progressively longer PR intervals",
            "Narrow QRS tachycardia with P waves inverted in lead II",
        ],
        "Complete block separates atrial and ventricular activity so PR varies without pattern. Prolonged PR with every beat conducted is first-degree block, not third-degree.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-010
    fact(
        "ekg-rhythm",
        "How does a premature atrial contraction usually appear on the EKG?",
        "An early narrow QRS preceded by a P wave with a morphology or PR interval that differs slightly from the sinus beats",
        [
            "An early wide QRS without any preceding P wave and a full compensatory pause",
            "A late wide QRS escape beat after a long pause",
            "Chaotic baseline without QRS organization",
        ],
        "PACs arise in the atria so the QRS is usually narrow with a visible P wave. Early wide beats without P waves suggest premature ventricular complexes.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-011
    fact(
        "ekg-rhythm",
        "How does a premature ventricular complex typically appear on the EKG?",
        "An early wide QRS without a preceding P wave, often followed by a compensatory pause",
        [
            "An early narrow QRS with an identical preceding P wave",
            "A regular sawtooth pattern between narrow QRS complexes",
            "Uniform P waves with a progressively lengthening PR interval",
        ],
        "PVCs start in the ventricle, producing a wide QRS and disrupting sinus timing. Early narrow beats with P waves fit PACs, not PVCs.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-012
    fact(
        "ekg-rhythm",
        "Which EKG description best fits monomorphic ventricular tachycardia?",
        "Regular wide QRS tachycardia at a rate usually above 100 beats per minute with uniform QRS shape",
        [
            "Irregularly irregular narrow QRS rhythm without P waves",
            "Regular narrow QRS tachycardia at 180 beats per minute with visible retrograde P waves",
            "Chaotic deflections without identifiable QRS complexes",
        ],
        "Monomorphic VT shows consistent wide beats at a rapid regular rate. Irregular narrow rhythm without P waves fits atrial fibrillation, and chaotic deflections fit ventricular fibrillation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-013
    fact(
        "ekg-rhythm",
        "Which tracing description best fits ventricular fibrillation?",
        "Chaotic, irregular deflections without identifiable P waves or organized QRS complexes",
        [
            "Regular wide QRS complexes at 160 beats per minute",
            "Flat line in a single lead with normal complexes in other leads",
            "Regular narrow QRS at 90 beats per minute with upright P waves",
        ],
        "VF is disorganized electrical activity without coherent QRS. A regular wide complex rhythm suggests ventricular tachycardia, and flat line in one lead may be a disconnected electrode.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-014
    fact(
        "ekg-rhythm",
        "Before labeling asystole on a monitor, what should be confirmed?",
        "The patient has no pulse and the flat line is present in multiple leads with cables attached",
        [
            "A single limb lead shows a flat line while the patient is talking",
            "The printer is out of paper",
            "The heart rate numeric reads zero with a normal QRS on the screen",
        ],
        "True asystole is a non-shockable arrest rhythm with no pulse and minimal electrical activity in multiple leads. Artifact or loose leads can mimic flat line while perfusing rhythms remain on other channels.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-015
    fact(
        "ekg-rhythm",
        "On the EKG during pulseless electrical activity, what is seen while the patient has no palpable pulse?",
        "Organized electrical complexes on the monitor without effective mechanical contraction",
        [
            "Chaotic fibrillatory waves without QRS formation",
            "Normal sinus rhythm with a strong carotid pulse",
            "Complete absence of electrical activity in every lead",
        ],
        "PEA shows organized activity such as narrow QRS complexes despite no pulse. Chaotic waves fit VF, and strong pulse with sinus rhythm is perfusing rhythm, not PEA.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-016
    fact(
        "ekg-rhythm",
        "Which finding suggests a junctional rhythm on the EKG?",
        "Narrow QRS complexes with P waves absent, inverted, or buried immediately before or after the QRS",
        [
            "Upright P before every QRS with a constant PR of 0.16 second",
            "Wide QRS at 40 beats per minute with AV dissociation and more P waves than QRS",
            "Irregularly irregular rhythm without P waves at 120 beats per minute",
        ],
        "Junctional rhythms arise near the AV node so P waves may be hidden or inverted near the QRS. Upright P with stable PR fits sinus rhythm, and irregular rhythm without P fits atrial fibrillation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-017
    fact(
        "ekg-rhythm",
        "Which pattern suggests multifocal atrial tachycardia on the EKG?",
        "At least three distinct P-wave morphologies with an irregularly irregular rhythm and rate above 100 beats per minute",
        [
            "Identical P waves before each QRS with a rate of 110 beats per minute",
            "Regular sawtooth waves with 2:1 ventricular conduction",
            "Uniform wide QRS complexes without P waves at 180 beats per minute",
        ],
        "MAT shows multiple atrial foci with varying P shapes and irregular R-R intervals at tachycardic rates. Identical P waves at 110 suggest sinus tachycardia, and sawtooth waves suggest flutter.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-018
    fact(
        "ekg-rhythm",
        "Which EKG pattern best fits paroxysmal supraventricular tachycardia in a stable adult?",
        "Sudden-onset regular narrow QRS tachycardia, often 150 to 250 beats per minute, with P waves often hidden in the QRS or ST segment",
        [
            "Irregularly irregular narrow QRS rhythm at 95 beats per minute",
            "Regular wide QRS tachycardia with AV dissociation and fusion beats",
            "Sinus rhythm at 88 beats per minute with respiratory variation in R-R interval",
        ],
        "PSVT is a rapid regular narrow complex rhythm with abrupt start and stop. Irregular rhythm at normal rates fits sinus arrhythmia or AF, and wide regular rhythm suggests ventricular tachycardia.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-019
    fact(
        "ekg-rhythm",
        "How does sinus arrhythmia with respiration typically appear on the EKG?",
        "The R-R interval shortens during inspiration and lengthens during expiration with normal P-wave morphology",
        [
            "Completely irregular R-R intervals without any P waves",
            "Progressive PR prolongation until a beat is dropped",
            "Regular wide QRS at 30 beats per minute without P waves",
        ],
        "Respiratory sinus arrhythmia is a phasic change in sinus rate with normal P waves. Totally irregular rhythm without P waves fits atrial fibrillation, and grouped PR changes fit Wenckebach.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-020
    fact(
        "ekg-rhythm",
        "What EKG pattern is called ventricular bigeminy?",
        "Every other beat is a wide premature ventricular complex following a sinus beat",
        [
            "Two narrow beats followed by a pause in repeating cycles",
            "Alternating narrow and wide beats with inverted P waves before each narrow beat",
            "Grouped beating with progressive PR lengthening",
        ],
        "Bigeminy pairs a sinus complex with a PVC in a repeating pattern. Grouped PR changes suggest Wenckebach, and alternating narrow-wide with inverted P suggests a different atrial mechanism.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-021
    fact(
        "ekg-rhythm",
        "Which description fits an idioventricular escape rhythm?",
        "Slow wide QRS rhythm, often 20 to 40 beats per minute, appearing when higher pacemaker sites fail",
        [
            "Rapid regular narrow QRS at 180 beats per minute with sudden onset",
            "Chaotic fibrillatory waves without QRS complexes",
            "Narrow QRS at 70 beats per minute with upright P before each beat",
        ],
        "Ventricular escape takes over at slow rates with wide QRS when sinus or junctional tissue fails. Rapid narrow tachycardia suggests PSVT, and chaotic waves fit VF.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-022
    fact(
        "ekg-rhythm",
        "Which EKG finding is characteristic of torsades de pointes?",
        "Polymorphic ventricular tachycardia with QRS amplitude twisting around the baseline, often with prolonged QT on the preceding tracing",
        [
            "Monomorphic wide QRS at a steady rate of 160 beats per minute",
            "Regular narrow QRS tachycardia with visible retrograde P waves",
            "Irregularly irregular rhythm with fine fibrillatory waves",
        ],
        "Torsades shows twisting polymorphic VT, often in the setting of QT prolongation. Monomorphic wide regular rhythm is typical VT without twisting, and fine irregular baseline fits AF.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-023
    fact(
        "ekg-rhythm",
        "A narrow QRS tachycardia at 200 beats per minute shows no visible P waves. Which rhythm is most likely?",
        "Paroxysmal supraventricular tachycardia",
        [
            "Ventricular tachycardia",
            "Atrial fibrillation with rapid ventricular response",
            "Sinus tachycardia at 200 beats per minute with clear P waves",
        ],
        "A regular narrow complex tachycardia near 200 with hidden P waves fits PSVT. VT would usually widen the QRS, and AF would be irregularly irregular.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-024
    fact(
        "ekg-rhythm",
        "A monitor shows a regular wide QRS tachycardia at 170 beats per minute. The patient is diaphoretic but has a blood pressure of 88/60 mmHg. Which interpretation is most appropriate?",
        "Manage as ventricular tachycardia using unstable wide-complex tachycardia protocol",
        [
            "Document sinus tachycardia, withhold treatment, and recheck blood pressure in one hour",
            "Remove all limb electrodes to eliminate artifact without obtaining another tracing",
            "Start long-term anticoagulation for atrial fibrillation before reviewing the rhythm strip",
        ],
        "Wide regular tachycardia with hypotension is VT until proven otherwise and needs urgent ACLS care. Sinus tachycardia would be narrow at this rate, and AF would be irregular.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-025
    fact(
        "ekg-rhythm",
        "An irregularly irregular rhythm at 130 beats per minute has no distinct P waves and variable QRS width is narrow. Which diagnosis is most likely?",
        "Atrial fibrillation with rapid ventricular response",
        [
            "Atrial flutter with fixed 2:1 block",
            "Mobitz type II second-degree AV block",
            "Monomorphic ventricular tachycardia",
        ],
        "Irregularly irregular narrow rhythm without P waves fits AF with RVR. Flutter with 2:1 block is usually regular, Mobitz II shows dropped beats with visible P waves, and VT is wide.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-026
    fact(
        "ekg-rhythm",
        "A flutter study shows sawtooth waves at 300 per minute with QRS every two flutter waves. What is the ventricular rate?",
        "About 150 beats per minute",
        [
            "About 75 beats per minute",
            "About 300 beats per minute",
            "About 30 beats per minute",
        ],
        "With 2:1 AV conduction, every second flutter wave conducts, halving the atrial rate to the ventricular rate. 3:1 conduction would yield about 100 beats per minute.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-027
    fact(
        "ekg-rhythm",
        "After a long pause, a single wide QRS appears without a preceding P wave. What is this beat most likely called?",
        "A ventricular escape beat",
        [
            "A premature atrial contraction",
            "A junctional premature beat with inverted P",
            "A normal sinus beat after sinus arrhythmia",
        ],
        "Escape beats follow a pause and arise from lower pacemakers, producing a wide QRS without a preceding P. PACs are early, not late, and usually narrow with a P wave.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-028
    fact(
        "ekg-rhythm",
        "A narrow QRS rhythm at 110 beats per minute shows inverted P waves immediately before each QRS with a short PR interval. What is the most likely rhythm?",
        "Accelerated junctional rhythm",
        [
            "Normal sinus rhythm with marked first-degree block",
            "Ventricular tachycardia",
            "Atrial flutter with 2:1 block",
        ],
        "Inverted P just before a narrow QRS at a modest rate suggests junctional tissue has accelerated. Sinus rhythm has upright P in lead II, VT widens the QRS, and flutter shows sawtooth waves.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-029
    fact(
        "ekg-rhythm",
        "During telemetry review, every P wave is followed by a QRS, but the PR interval is 0.24 second and unchanged beat to beat. How should this be classified?",
        "First-degree atrioventricular block",
        [
            "Mobitz type II second-degree block",
            "Complete heart block",
            "Normal sinus rhythm with short PR interval",
        ],
        "Fixed prolonged PR with 1:1 conduction is first-degree block. Mobitz II drops beats without progressive PR change, and complete block shows AV dissociation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-030
    fact(
        "ekg-rhythm",
        "A rhythm strip shows grouped beating: PR lengthens across three beats, then a P wave without a QRS, then the pattern repeats. What is the diagnosis?",
        "Mobitz type I second-degree AV block",
        [
            "Sinus arrhythmia with respiration",
            "Atrial fibrillation",
            "Ventricular bigeminy",
        ],
        "Grouped Wenckebach cycles with progressive PR then a dropped beat define Mobitz I. Respiratory sinus arrhythmia varies R-R with normal conduction, and bigeminy pairs wide PVCs with sinus beats.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-031
    fact(
        "ekg-rhythm",
        "A patient has palpitations. The EKG shows a regular narrow complex rhythm at 160 beats per minute with no visible P waves. Carotid sinus massage briefly slows or terminates the rhythm. What does this suggest?",
        "A reentrant supraventricular tachycardia such as AV nodal reentrant tachycardia",
        [
            "Ventricular fibrillation",
            "Complete heart block with ventricular escape",
            "Sinus bradycardia",
        ],
        "Carotid massage increases AV nodal block and can terminate AV nodal reentrant PSVT. VF is chaotic and non-perfusing, escape rhythms are slow and wide or junctional, and sinus bradycardia is slow.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-032
    fact(
        "ekg-rhythm",
        "Fine oscillations ride on the QRS at 60 Hz during a tracing on a plugged-in monitor. The patient is still and the rhythm underneath is regular. What is the most likely cause?",
        "Electrical interference from alternating current or grounding issues",
        [
            "Ventricular fibrillation requiring immediate defibrillation",
            "Acute ST-elevation myocardial infarction in all leads",
            "Hyperkalemia with peaked T waves in every lead",
        ],
        "60 Hz artifact from power lines or poor ground mimics fine vibration on the baseline while underlying rhythm may remain organized. VF is coarse chaotic without regular QRS, and STEMI or hyperkalemia show morphologic ST-T changes, not uniform 60 Hz oscillation.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-033
    fact(
        "ekg-rhythm",
        "A rhythm is irregularly irregular at 95 beats per minute with narrow QRS and no P waves. The patient is asymptomatic. Which management focus is most appropriate per typical outpatient guidance?",
        "Assess stroke risk and consider rate or rhythm control based on symptoms and guidelines",
        [
            "Immediate synchronized cardioversion in all asymptomatic patients",
            "Ignore the rhythm because the rate is under 100 beats per minute",
            "Start therapeutic anticoagulation without further evaluation in every case",
        ],
        "New or known AF needs stroke risk stratification and symptom-directed rate or rhythm control. Cardioversion is for unstable patients, and anticoagulation decisions require risk assessment, not automatic treatment for every asymptomatic case.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-034
    fact(
        "ekg-rhythm",
        "Two consecutive wide QRS complexes have identical shape and occur earlier than expected, each without a preceding P wave. What term describes this pattern?",
        "A pair of premature ventricular complexes (couplet)",
        [
            "A run of atrial flutter with 1:1 conduction",
            "First-degree AV block",
            "Sinus arrhythmia",
        ],
        "Back-to-back PVCs with the same morphology form a couplet. Flutter shows sawtooth waves, first-degree block prolongs PR without early wide beats, and sinus arrhythmia varies sinus rate with narrow QRS.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-035
    fact(
        "ekg-rhythm",
        "Which EKG finding distinguishes atrial flutter with 2:1 conduction from paroxysmal supraventricular tachycardia at the same ventricular rate?",
        "Visible sawtooth flutter waves, often in leads II, III, and aVF, with a regular ventricular rhythm",
        [
            "Irregularly irregular R-R intervals with fibrillatory baseline",
            "Progressive PR lengthening before a dropped beat",
            "Wide QRS complexes with AV dissociation",
        ],
        "Flutter exposes atrial sawteeth at a regular atrial rate with patterned conduction. Irregular R-R without P waves fits AF, Wenckebach shows progressive PR, and wide QRS with dissociation fits VT.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-036
    fact(
        "ekg-rhythm",
        "A patient has syncope. The EKG shows a ventricular rate of 35 beats per minute with wide QRS and P waves marching through at a faster rate unrelated to QRS. What is the diagnosis?",
        "Third-degree AV block with ventricular escape rhythm",
        [
            "Sinus bradycardia at 35 beats per minute with narrow QRS",
            "Atrial fibrillation with slow ventricular response",
            "Normal sinus rhythm with first-degree block",
        ],
        "AV dissociation with faster P waves and a slow wide escape rhythm indicates complete heart block. Sinus bradycardia keeps 1:1 P and QRS with narrow QRS, and AF lacks discrete marching P waves.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-037
    fact(
        "ekg-rhythm",
        "On a rhythm strip, each QRS is narrow and preceded by an upright P, but the PR interval is 0.18 second in beat 1, 0.22 in beat 2, and 0.26 in beat 3 before a P without QRS. What rhythm abnormality is present?",
        "Mobitz type I second-degree AV block",
        [
            "First-degree AV block only",
            "Sinus tachycardia",
            "Ventricular trigeminy",
        ],
        "Progressive PR lengthening ending in a non-conducted P defines Wenckebach. First-degree block has constant prolonged PR with every beat conducted, and trigeminy is a PVC pattern, not PR changes.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-038
    fact(
        "ekg-rhythm",
        "A hospitalized patient on telemetry has brief runs of three to five wide beats at 130 beats per minute that start and end suddenly. Blood pressure remains stable. How should these runs most likely be classified?",
        "Nonsustained ventricular tachycardia",
        [
            "Sustained ventricular fibrillation",
            "Normal sinus arrhythmia",
            "First-degree AV block",
        ],
        "Short self-terminating wide runs at tachycardic rates are nonsustained VT. VF is chaotic and non-perfusing, sinus arrhythmia is narrow with respiratory variation, and first-degree block affects PR not wide bursts.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-039
    fact(
        "ekg-rhythm",
        "An EKG shows narrow QRS at 75 beats per minute with inverted P waves immediately after each QRS. What is the most likely pacemaker site?",
        "Junctional (AV junction) rhythm",
        [
            "Normal sinus node rhythm",
            "Ventricular escape rhythm",
            "Atrial fibrillation",
        ],
        "Inverted P waves right after the QRS suggest retrograde atrial activation from the junction. Sinus rhythm has upright P before QRS, ventricular escape is wide and slow, and AF lacks discrete P waves.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-040
    fact(
        "ekg-rhythm",
        "A patient has chest pain. The rhythm is sinus at 90 beats per minute, but every third beat is a wide QRS without a P wave. How many premature ventricular complexes occur per 10-beat segment?",
        "Three PVCs in each 10-beat cycle (trigeminy pattern)",
        [
            "One PVC every 10 beats (bigeminy pattern)",
            "Five PACs in each 10-beat cycle",
            "No ectopic beats; the pattern is Wenckebach",
        ],
        "A PVC every third beat is ventricular trigeminy. Bigeminy is every other beat, PACs would be narrow with P waves, and Wenckebach changes PR and drops beats without fixed wide ectopy.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-041
    fact(
        "ekg-rhythm",
        "While brushing teeth, a patient feels palpitations. Telemetry captured onset of a regular narrow tachycardia at 180 beats per minute that ended suddenly after vagal maneuver. Which mechanism is most likely?",
        "Reentrant supraventricular tachycardia involving the AV node or accessory pathway",
        [
            "Gradual sinus tachycardia from fever over 30 minutes",
            "Progressive development of complete heart block",
            "Slow idioventricular escape at 40 beats per minute",
        ],
        "Abrupt start and stop with vagal response fits reentrant PSVT. Sinus tach from fever ramps gradually, complete block slows the rate with dissociation, and escape rhythms are slow wide or junctional, not 180 narrow.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
