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

/** Sum per-question `score` fields from the live `final_results` socket payload. */
export function aggregateScoresFromFinalResults(
	finalResults: unknown
): Record<string, number> {
	if (finalResults == null || typeof finalResults !== 'object' || Array.isArray(finalResults)) {
		return {};
	}
	const scores: Record<string, number> = {};
	for (const answers of Object.values(finalResults as Record<string, unknown>)) {
		if (!Array.isArray(answers)) continue;
		for (const row of answers) {
			if (row == null || typeof row !== 'object') continue;
			const name = (row as QuestionResultRow).username;
			if (!name) continue;
			scores[name] = (Number(scores[name]) || 0) + (Number((row as QuestionResultRow).score) || 0);
		}
	}
	return scores;
}
