// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { StandingsRow } from '$lib/play/live-game';

export type QuestionResultRow = {
	username?: string;
	score?: number;
	base_score?: number;
	speed_bonus?: number;
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
	if (!mine) return 0;
	// The server's score already includes the streak multiplier, and it is what the scoreboard adds.
	// Using base + speed here would drop the streak points from the reveal.
	if (mine.score != null) {
		return Number(mine.score) || 0;
	}
	return Number(mine.base_score ?? 0) + Number(mine.speed_bonus ?? 0);
}

export type LiveScoresState = {
	scores: Record<string, number>;
	lastAppliedQuestionIndex: number | null;
	standingsTop: StandingsRow[];
};

/** Merge question_results into client totals; prefer server standings_top over summed rows. */
export function integrateLiveQuestionResults(
	state: LiveScoresState,
	payload: {
		questionIndex: number | null;
		rows: QuestionResultRow[];
		standingsTop: StandingsRow[];
	}
): LiveScoresState {
	const qIndex =
		payload.questionIndex != null && Number.isFinite(payload.questionIndex)
			? Number(payload.questionIndex)
			: null;
	const incomingTop = payload.standingsTop ?? [];
	let standingsTop = state.standingsTop;
	if (incomingTop.length > 0) {
		standingsTop = incomingTop;
	}

	let scores = { ...state.scores };
	let lastAppliedQuestionIndex = state.lastAppliedQuestionIndex;

	if (incomingTop.length > 0) {
		for (const row of incomingTop) {
			const name = row.username;
			if (!name) continue;
			scores[name] = Number(row.score) || 0;
		}
		if (qIndex != null) {
			lastAppliedQuestionIndex = qIndex;
		}
	} else if (qIndex != null && lastAppliedQuestionIndex !== qIndex) {
		const applied = applyQuestionResultScores(
			scores,
			payload.rows,
			qIndex,
			lastAppliedQuestionIndex
		);
		scores = applied.scores;
		lastAppliedQuestionIndex = applied.lastAppliedQuestionIndex;
	}

	return { scores, lastAppliedQuestionIndex, standingsTop };
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
