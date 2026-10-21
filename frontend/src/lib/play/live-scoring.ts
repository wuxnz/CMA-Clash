// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

export type QuestionResultRow = {
	username?: string;
	score?: number;
};

/** Apply per-question scores at most once per question index (duplicate question_results safe). */
export function applyQuestionResultScores(
	scores: Record<string, number>,
	rows: QuestionResultRow[] | null | undefined,
	questionIndex: number | string | null | undefined,
	lastAppliedQuestionIndex: number | null
): { scores: Record<string, number>; lastAppliedQuestionIndex: number | null } {
	if (!Array.isArray(rows) || rows.length === 0) {
		return { scores, lastAppliedQuestionIndex };
	}
	if (questionIndex == null || questionIndex === '') {
		return { scores, lastAppliedQuestionIndex };
	}
	const qIndex = Number(questionIndex);
	if (!Number.isFinite(qIndex) || lastAppliedQuestionIndex === qIndex) {
		return { scores, lastAppliedQuestionIndex };
	}

	const next = { ...scores };
	for (const row of rows) {
		const name = row?.username;
		if (!name) continue;
		next[name] = (Number(next[name]) || 0) + (Number(row.score) || 0);
	}
	return { scores: next, lastAppliedQuestionIndex: qIndex };
}

export function scoreDeltaForUser(
	rows: QuestionResultRow[] | null | undefined,
	username: string
): number {
	if (!Array.isArray(rows) || !username) return 0;
	const mine = rows.find((r) => r.username === username);
	return Number(mine?.score ?? 0);
}
