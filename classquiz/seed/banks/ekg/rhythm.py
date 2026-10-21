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
        "Normal P-QRS-T morphology with ventricular rate below 60 beats per minute",
        [
            "Irregularly irregular rhythm without distinct P waves or organized atrial activity",
            "Narrow complex tachycardia at 150 beats per minute with hidden or buried P waves",
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
        "Upright P before each QRS with ventricular rate above 100 beats per minute",
        [
            "Regular narrow QRS at 180 beats per minute without visible or identifiable P waves",
            "Irregularly irregular rhythm with fibrillatory baseline and no discrete P waves",
            "Flat isoelectric line in all leads with occasional isolated P waves",
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
            "Fine fibrillatory baseline with variably irregular R-R intervals and no organized flutter waves",
            "Grouped beats with progressive PR prolongation until a QRS is dropped on the strip",
            "Regular narrow QRS tachycardia with retrograde P waves buried in the ST segment",
        ],
        "Flutter has organized atrial activity around 250 to 350 per minute with a sawtooth appearance. Fine irregular baseline without P waves fits atrial fibrillation, and progressive PR changes fit Mobitz I block.",
        [S.NHA_CCMA],
        "beginner",
    ),
    # ekg-rhythm-006
    fact(
        "ekg-rhythm",
        "How does first-degree atrioventricular block appear on the EKG?",
        "PR longer than 0.20 second with every P wave followed by a QRS complex",
        [
            "PR interval that progressively lengthens until a QRS complex is dropped",
            "P waves and QRS complexes that are completely unrelated to each other",
            "PR interval shorter than 0.12 second with delta waves and slurred QRS upstroke",
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
            "Fixed PR interval with sudden dropped QRS complexes and no prior PR lengthening on the strip",
            "Complete AV dissociation with more P waves than QRS complexes and variable PR intervals",
            "PR interval below 0.12 second with slurred upstroke of the QRS and delta waves",
        ],
        "Mobitz I shows grouped beating as PR stretches until a beat drops. Fixed PR with sudden drops suggests Mobitz II, and independent P and QRS rates suggest complete heart block.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-008
    fact(
        "ekg-rhythm",
        "Which pattern defines Mobitz type II second-degree AV block?",
        "Constant PR with intermittent non-conducted P waves and dropped QRS complexes",
        [
            "Progressive PR interval lengthening before each dropped QRS beat in grouped Wenckebach cycles",
            "Irregularly irregular narrow rhythm without discernible P waves or organized atrial activity",
            "Wide QRS escape rhythm at 30 beats per minute without preceding P waves or upright sinus P morphology",
        ],
        "Mobitz II keeps a steady PR until a beat fails to conduct, which can progress to complete block. Progressive PR changes point to Mobitz I, not type II.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-009
    fact(
        "ekg-rhythm",
        "What defines third-degree (complete) atrioventricular block on the EKG?",
        "P waves and QRS at independent rates with no consistent PR relationship",
        [
            "PR interval greater than 0.20 second with consistent 1:1 AV conduction throughout every beat",
            "Dropped QRS beat after progressively longer PR intervals in grouped Wenckebach cycles",
            "Narrow QRS tachycardia with P waves inverted in lead II and short PR interval before each QRS",
        ],
        "Complete block separates atrial and ventricular activity so PR varies without pattern. Prolonged PR with every beat conducted is first-degree block, not third-degree.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-010
    fact(
        "ekg-rhythm",
        "How does a premature atrial contraction usually appear on the EKG?",
        "Early narrow QRS with a P wave whose morphology or PR differs slightly from sinus beats",
        [
            "An early wide QRS without any preceding P wave and a full compensatory pause after the beat",
            "A late wide QRS escape beat after a long pause without a preceding P wave or sinus activity",
            "Chaotic fibrillatory baseline without organized QRS complexes or identifiable atrial activity",
        ],
        "PACs arise in the atria so the QRS is usually narrow with a visible P wave. Early wide beats without P waves suggest premature ventricular complexes.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-011
    fact(
        "ekg-rhythm",
        "How does a premature ventricular complex typically appear on the EKG?",
        "Early wide QRS without a preceding P wave, often with a compensatory pause",
        [
            "An early narrow QRS with an identical preceding P wave and narrow QRS morphology",
            "A regular sawtooth flutter pattern between narrow QRS complexes at fixed rate",
            "Uniform P waves with a progressively lengthening PR interval until a beat drops",
        ],
        "PVCs start in the ventricle, producing a wide QRS and disrupting sinus timing. Early narrow beats with P waves fit PACs, not PVCs.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-012
    fact(
        "ekg-rhythm",
        "Which EKG description best fits monomorphic ventricular tachycardia?",
        "Regular wide QRS tachycardia above 100 beats per minute with uniform QRS morphology",
        [
            "Irregularly irregular narrow QRS rhythm without P waves at a rapid ventricular rate",
            "Regular narrow QRS tachycardia at 180 beats per minute with retrograde P waves in ST segments",
            "Chaotic deflections without identifiable QRS complexes or organized ventricular activity",
        ],
        "Monomorphic VT shows consistent wide beats at a rapid regular rate. Irregular narrow rhythm without P waves fits atrial fibrillation, and chaotic deflections fit ventricular fibrillation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-013
    fact(
        "ekg-rhythm",
        "Which tracing description best fits ventricular fibrillation?",
        "Chaotic irregular deflections without identifiable P waves or organized QRS complexes",
        [
            "Regular monomorphic wide QRS complexes at 160 beats per minute without P waves or organized atrial activity",
            "Flat line in a single lead with normal sinus complexes visible in other leads while the patient has a pulse",
            "Regular narrow QRS at 90 beats per minute with upright P waves before each QRS and stable PR interval",
        ],
        "VF is disorganized electrical activity without coherent QRS. A regular wide complex rhythm suggests ventricular tachycardia, and flat line in one lead may be a disconnected electrode.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-014
    fact(
        "ekg-rhythm",
        "Before labeling asystole on a monitor, what should be confirmed?",
        "No pulse with flat line in multiple leads and all electrode cables properly attached",
        [
            "A single limb lead shows a flat line while the patient is talking and has a pulse",
            "The EKG printer is out of paper so the rhythm strip appears blank on paper only",
            "The heart rate numeric reads zero with a normal QRS complex still visible on the screen",
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
            "Chaotic fibrillatory waves on the monitor without organized QRS formation",
            "Normal sinus rhythm on the monitor with upright P waves and narrow QRS in every lead",
            "Complete absence of electrical activity in every monitored EKG lead with no QRS complexes",
        ],
        "PEA shows organized activity such as narrow QRS complexes despite no pulse. Chaotic waves fit VF, and strong pulse with sinus rhythm is perfusing rhythm, not PEA.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-016
    fact(
        "ekg-rhythm",
        "Which finding suggests a junctional rhythm on the EKG?",
        "Narrow QRS with P waves absent, inverted, or buried just before or after each QRS",
        [
            "Upright P before every QRS with a constant PR interval of 0.16 second throughout the strip",
            "Wide QRS at 40 beats per minute with AV dissociation and more P waves than QRS complexes",
            "Irregularly irregular narrow rhythm without P waves at 120 beats per minute with fibrillatory baseline",
        ],
        "Junctional rhythms arise near the AV node so P waves may be hidden or inverted near the QRS. Upright P with stable PR fits sinus rhythm, and irregular rhythm without P fits atrial fibrillation.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-017
    fact(
        "ekg-rhythm",
        "Which pattern suggests multifocal atrial tachycardia on the EKG?",
        "Three or more distinct P-wave morphologies with irregular rhythm above 100 bpm",
        [
            "Identical P waves before each QRS with a ventricular rate of 110 beats per minute throughout",
            "Regular sawtooth flutter waves with fixed 2:1 ventricular conduction throughout the tracing",
            "Uniform wide QRS tachycardia without P waves at 180 beats per minute with regular R-R intervals",
        ],
        "MAT shows multiple atrial foci with varying P shapes and irregular R-R intervals at tachycardic rates. Identical P waves at 110 suggest sinus tachycardia, and sawtooth waves suggest flutter.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-018
    fact(
        "ekg-rhythm",
        "Which EKG pattern best fits paroxysmal supraventricular tachycardia in a stable adult?",
        "Sudden regular narrow QRS tachycardia, often 150 to 250 bpm, with hidden retrograde P waves",
        [
            "Irregularly irregular narrow QRS at 95 bpm without discrete P waves or organized atrial activity",
            "Regular wide QRS tachycardia with AV dissociation, fusion beats, and uniform QRS width",
            "Sinus rhythm at 88 bpm with respiratory R-R variation and upright P waves in lead II",
        ],
        "PSVT is a rapid regular narrow complex rhythm with abrupt start and stop. Irregular rhythm at normal rates fits sinus arrhythmia or AF, and wide regular rhythm suggests ventricular tachycardia.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-019
    fact(
        "ekg-rhythm",
        "How does sinus arrhythmia with respiration typically appear on the EKG?",
        "R-R shortens on inspiration and lengthens on expiration with normal sinus P-wave morphology",
        [
            "Completely irregular R-R intervals without any visible P waves or organized atrial activity",
            "Progressive PR prolongation until a beat is dropped in repeating Wenckebach cycles",
            "Regular wide QRS escape rhythm at 30 beats per minute without preceding P waves",
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
            "Two narrow sinus beats followed by a compensatory pause in repeating cycles",
            "Alternating narrow and wide beats with inverted P waves before each narrow beat",
            "Grouped beating with progressive PR lengthening until a QRS complex is dropped",
        ],
        "Bigeminy pairs a sinus complex with a PVC in a repeating pattern. Grouped PR changes suggest Wenckebach, and alternating narrow-wide with inverted P suggests a different atrial mechanism.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-021
    fact(
        "ekg-rhythm",
        "Which description fits an idioventricular escape rhythm?",
        "Slow wide QRS escape rhythm, often 20 to 40 bpm, when higher pacemaker sites fail",
        [
            "Rapid regular narrow QRS tachycardia at 180 beats per minute with abrupt sudden onset",
            "Chaotic fibrillatory waves without organized QRS complexes or identifiable P waves",
            "Narrow QRS at 70 beats per minute with upright P waves before each conducted beat",
        ],
        "Ventricular escape takes over at slow rates with wide QRS when sinus or junctional tissue fails. Rapid narrow tachycardia suggests PSVT, and chaotic waves fit VF.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-022
    fact(
        "ekg-rhythm",
        "Which EKG finding is characteristic of torsades de pointes?",
        "Polymorphic ventricular tachycardia with QRS twisting around the baseline after prolonged QT",
        [
            "Monomorphic wide QRS tachycardia at about 160 beats per minute with uniform beat morphology",
            "Regular narrow QRS tachycardia with retrograde P waves buried in the ST segment and abrupt onset",
            "Irregularly irregular narrow rhythm with fibrillatory baseline and no discrete P waves visible",
        ],
        "Torsades shows twisting polymorphic VT, often in the setting of QT prolongation. Monomorphic wide regular rhythm is typical VT without twisting, and fine irregular baseline fits AF.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-023
    fact(
        "ekg-rhythm",
        "A narrow QRS tachycardia at 200 beats per minute shows no visible P waves. Which rhythm is most likely?",
        "Paroxysmal supraventricular tachycardia with regular narrow QRS and no visible P waves",
        [
            "Sinus tachycardia with visible upright P waves before each narrow QRS at 200 bpm",
            "Atrial fibrillation with irregularly irregular narrow QRS and absent discrete P waves",
            "Atrial flutter with sawtooth waves and patterned ventricular conduction at about 200 bpm",
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
        "Atrial fibrillation with rapid ventricular response and irregularly irregular narrow QRS",
        [
            "Atrial flutter with variable AV block and sawtooth waves without discrete sinus P waves",
            "Mobitz type II second-degree AV block with constant PR and sudden non-conducted P waves",
            "Sinus tachycardia with upright P waves and fixed PR interval at about 130 beats per minute",
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
        "Accelerated junctional rhythm with inverted P waves and narrow QRS complexes",
        [
            "Normal sinus rhythm with upright P waves and marked first-degree AV block",
            "Atrial fibrillation with irregularly irregular narrow QRS and fibrillatory baseline",
            "Atrial flutter with sawtooth waves and 2:1 AV conduction at a steady ventricular rate",
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
        "Mobitz type I block with grouped beats, progressive PR lengthening, then a dropped QRS",
        [
            "Respiratory sinus arrhythmia with phasic R-R variation and normal PR on every beat",
            "Atrial fibrillation with irregularly irregular ventricular response and no grouped PR pattern",
            "Ventricular bigeminy with alternating sinus beats and wide premature ventricular complexes",
        ],
        "Grouped Wenckebach cycles with progressive PR then a dropped beat define Mobitz I. Respiratory sinus arrhythmia varies R-R with normal conduction, and bigeminy pairs wide PVCs with sinus beats.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-031
    fact(
        "ekg-rhythm",
        "A patient has palpitations. The EKG shows a regular narrow complex rhythm at 160 beats per minute with no visible P waves. Carotid sinus massage briefly slows or terminates the rhythm. What does this suggest?",
        "Reentrant supraventricular tachycardia such as AV nodal reentrant tachycardia",
        [
            "Ventricular fibrillation with chaotic coarse undulating rhythm without pulse",
            "Complete heart block with slow wide ventricular escape rhythm and AV dissociation",
            "Sinus bradycardia with upright P waves before each narrow QRS complex",
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
            "Ventricular fibrillation requiring immediate defibrillation and CPR",
            "Acute ST-elevation myocardial infarction with regional ST elevation in multiple leads",
            "Hyperkalemia with peaked T waves and widened QRS complexes in multiple leads",
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
            "Immediate synchronized cardioversion for all asymptomatic patients regardless of symptoms",
            "Ignore the rhythm because the ventricular rate is under 100 beats per minute",
            "Start full therapeutic anticoagulation in every patient without stroke-risk stratification",
        ],
        "New or known AF needs stroke risk stratification and symptom-directed rate or rhythm control. Cardioversion is for unstable patients, and anticoagulation decisions require risk assessment, not automatic treatment for every asymptomatic case.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-034
    fact(
        "ekg-rhythm",
        "Two consecutive wide QRS complexes have identical shape and occur earlier than expected, each without a preceding P wave. What term describes this pattern?",
        "Two consecutive wide premature ventricular complexes (a PVC couplet) without preceding P waves",
        [
            "A sustained run of atrial flutter with 1:1 AV conduction and sawtooth flutter waves on the strip",
            "First-degree AV block with fixed prolonged PR interval and 1:1 conduction of every beat on the strip",
            "Respiratory sinus arrhythmia with phasic R-R variation and upright sinus P waves before each QRS",
        ],
        "Back-to-back PVCs with the same morphology form a couplet. Flutter shows sawtooth waves, first-degree block prolongs PR without early wide beats, and sinus arrhythmia varies sinus rate with narrow QRS.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-035
    fact(
        "ekg-rhythm",
        "Which EKG finding distinguishes atrial flutter with 2:1 conduction from paroxysmal supraventricular tachycardia at the same ventricular rate?",
        "Sawtooth flutter waves in II, III, and aVF with regular ventricular rhythm at the same rate",
        [
            "Irregularly irregular R-R intervals with fibrillatory baseline and no sawtooth flutter waves",
            "Grouped Wenckebach beats with progressive PR lengthening before a dropped QRS and upright P waves",
            "Wide QRS tachycardia with AV dissociation, fusion beats, and more P waves than QRS complexes",
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
            "Sinus bradycardia at 35 beats per minute with 1:1 upright P before each QRS",
            "Atrial fibrillation with slow ventricular response and fibrillatory baseline",
            "Normal sinus rhythm with first-degree AV block and 1:1 AV conduction",
        ],
        "AV dissociation with faster P waves and a slow wide escape rhythm indicates complete heart block. Sinus bradycardia keeps 1:1 P and QRS with narrow QRS, and AF lacks discrete marching P waves.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-037
    fact(
        "ekg-rhythm",
        "On a rhythm strip, each QRS is narrow and preceded by an upright P, but the PR interval is 0.18 second in beat 1, 0.22 in beat 2, and 0.26 in beat 3 before a P without QRS. What rhythm abnormality is present?",
        "Mobitz type I block with progressive PR lengthening ending in a non-conducted P wave",
        [
            "First-degree AV block with fixed prolonged PR interval and every P wave conducted",
            "Sinus tachycardia with upright P waves before each QRS and rate above 100 beats per minute",
            "Ventricular trigeminy with a wide PVC every third sinus beat and stable sinus P waves",
        ],
        "Progressive PR lengthening ending in a non-conducted P defines Wenckebach. First-degree block has constant prolonged PR with every beat conducted, and trigeminy is a PVC pattern, not PR changes.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-038
    fact(
        "ekg-rhythm",
        "A hospitalized patient on telemetry has brief runs of three to five wide beats at 130 beats per minute that start and end suddenly. Blood pressure remains stable. How should these runs most likely be classified?",
        "Brief nonsustained ventricular tachycardia: three to five wide beats that start and end suddenly",
        [
            "Accelerated idioventricular rhythm with gradual rate warm-up and narrow escape morphology",
            "Supraventricular tachycardia with aberrancy and intermittently narrow captured sinus beats",
            "Sustained monomorphic ventricular tachycardia lasting more than thirty seconds without termination",
        ],
        "Brief self-terminating wide runs at tachycardic rates are nonsustained VT. AIVR warms up more slowly, SVT with aberrancy often has narrow captured beats, and sustained VT persists beyond thirty seconds.",
        [S.NHA_CCMA],
        "advanced",
    ),
    # ekg-rhythm-039
    fact(
        "ekg-rhythm",
        "An EKG shows narrow QRS at 75 beats per minute with inverted P waves immediately after each QRS. What is the most likely pacemaker site?",
        "Junctional rhythm with retrograde P waves after each narrow QRS",
        [
            "Sinus rhythm with upright P waves before each narrow QRS complex",
            "Ectopic atrial rhythm with upright P before QRS at a different atrial rate",
            "Atrial flutter with sawtooth waves and regular ventricular response near 75 bpm",
        ],
        "Inverted P waves right after the QRS suggest retrograde atrial activation from the junction. Sinus and ectopic atrial rhythms show P before QRS; AIVR is wide without retrograde P.",
        [S.NHA_CCMA],
        "intermediate",
    ),
    # ekg-rhythm-040
    fact(
        "ekg-rhythm",
        "A patient has chest pain. The rhythm is sinus at 90 beats per minute, but every third beat is a wide QRS without a P wave. How many premature ventricular complexes occur per 10-beat segment?",
        "Three wide PVCs in each 10-beat cycle consistent with ventricular trigeminy",
        [
            "One wide PVC every other beat in each cycle consistent with bigeminy",
            "Two wide PVCs per 10-beat cycle in a repeating bigeminy pattern with pauses",
            "Grouped PR lengthening with dropped beats representing Wenckebach AV block",
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
            "Gradual sinus tachycardia from fever developing over 30 minutes with upright P waves",
            "Progressive gradual development of complete third-degree AV heart block",
            "Slow idioventricular escape rhythm at about 40 beats per minute with wide QRS",
        ],
        "Abrupt start and stop with vagal response fits reentrant PSVT. Sinus tach from fever ramps gradually, complete block slows the rate with dissociation, and escape rhythms are slow wide or junctional, not 180 narrow.",
        [S.NHA_CCMA],
        "advanced",
    ),
]
