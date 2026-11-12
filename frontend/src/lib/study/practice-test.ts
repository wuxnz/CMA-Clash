// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

/** The untimed diabetes practice test. */
export const PRACTICE_TEST_PATH = '/practice-test/diabetes';

/** The untimed Diabetes Test 2nd Half practice test. Its questions are shuffled on every visit. */
export const TEST_2ND_HALF_PRACTICE_PATH = '/practice-test/diabetes-test-2nd-half';

/** The untimed Diabetes Test 1st Half practice test. Its questions are shuffled on every visit. */
export const TEST_1ST_HALF_PRACTICE_PATH = '/practice-test/diabetes-test-1st-half';

/** The untimed Phlebotomy Test Study Guide practice test. Its questions are shuffled on every visit. */
export const PHLEB_TEST_STUDY_PRACTICE_PATH = '/practice-test/phlebotomy-test-study';

/** The untimed TEAS Test Study Guide practice test. Its questions are shuffled on every visit. */
export const TEAS_TEST_STUDY_PRACTICE_PATH = '/practice-test/teas-test-study';

/** Practice test path for each seed quiz that has one. */
const PRACTICE_TEST_PATHS: Record<string, string> = {
	'quiz:ccma-diabetes': PRACTICE_TEST_PATH,
	'quiz:diabetes-study-guide': PRACTICE_TEST_PATH,
	'quiz:diabetes-test-2nd-half': TEST_2ND_HALF_PRACTICE_PATH,
	'quiz:diabetes-test-1st-half': TEST_1ST_HALF_PRACTICE_PATH,
	'quiz:phlebotomy-test-study': PHLEB_TEST_STUDY_PRACTICE_PATH,
	'quiz:teas-test-study': TEAS_TEST_STUDY_PRACTICE_PATH
};

/** The practice test path for a quiz, or null when the quiz has no practice test. */
export function practiceTestPath(quiz: { seed_slug?: string | null }): string | null {
	return quiz.seed_slug ? (PRACTICE_TEST_PATHS[quiz.seed_slug] ?? null) : null;
}

export function isPracticeTestQuiz(quiz: { seed_slug?: string | null }): boolean {
	return practiceTestPath(quiz) !== null;
}

/** Practice link for a quiz: the untimed practice test where one exists, timed practice otherwise. */
export function practiceHref(quiz: { id: string; seed_slug?: string | null }): string {
	return practiceTestPath(quiz) ?? `/practice?quiz_id=${quiz.id}`;
}
