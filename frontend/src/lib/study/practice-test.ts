// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

/** The untimed diabetes practice test. */
export const PRACTICE_TEST_PATH = '/practice-test/diabetes';

/** Seed slugs of the diabetes quizzes that practice should open the practice test for. */
const PRACTICE_TEST_QUIZ_SLUGS = new Set(['quiz:ccma-diabetes', 'quiz:diabetes-study-guide']);

export function isPracticeTestQuiz(quiz: { seed_slug?: string | null }): boolean {
	return !!quiz.seed_slug && PRACTICE_TEST_QUIZ_SLUGS.has(quiz.seed_slug);
}

/** Practice link for a quiz: the untimed practice test for diabetes quizzes, timed practice otherwise. */
export function practiceHref(quiz: { id: string; seed_slug?: string | null }): string {
	return isPracticeTestQuiz(quiz) ? PRACTICE_TEST_PATH : `/practice?quiz_id=${quiz.id}`;
}
