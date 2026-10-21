// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

/** Socket joined_game payloads were briefly emitted as a one-tuple; unwrap for safety. */
export function normalizeGamePayload<T extends Record<string, unknown>>(data: unknown): T | undefined {
	if (data == null) return undefined;
	if (Array.isArray(data)) {
		const first = data[0];
		return first && typeof first === 'object' ? (first as T) : undefined;
	}
	return typeof data === 'object' ? (data as T) : undefined;
}

export function normalizeGameMode(gameMode: unknown): string | null {
	if (gameMode == null || gameMode === '') return null;
	if (typeof gameMode === 'string') {
		const trimmed = gameMode.trim().toLowerCase();
		return trimmed === '' ? null : trimmed;
	}
	return String(gameMode).trim().toLowerCase();
}

export function isKahootStyleMode(gameMode: unknown): boolean {
	const mode = normalizeGameMode(gameMode);
	return mode === 'kahoot' || mode === 'battle' || mode == null;
}

function questionTypeKey(type: unknown): string | null {
	if (type == null) return null;
	if (typeof type === 'string') {
		const trimmed = type.trim();
		return trimmed === '' ? null : trimmed.toUpperCase();
	}
	const asString = String(type).trim();
	return asString === '' ? null : asString.toUpperCase();
}

/** ABCD / voting questions rendered as the 2×2 tile grid on player devices. */
export function hasChoiceTileAnswers(
	question: { type?: unknown; answers?: unknown } | undefined | null
): boolean {
	if (!question?.answers || !Array.isArray(question.answers) || question.answers.length === 0) {
		return false;
	}
	const type = questionTypeKey(question.type) ?? 'ABCD';
	return type === 'ABCD' || type === 'VOTING';
}

/** Unwrap question payload from set_question_number (nested or legacy flat). */
export function questionFromSocketPayload(
	data: Record<string, unknown> | null | undefined
): { type?: unknown; answers?: unknown; question?: string } | undefined {
	if (!data) return undefined;
	if (data.question && typeof data.question === 'object') {
		return data.question as { type?: unknown; answers?: unknown; question?: string };
	}
	if (Array.isArray(data.answers) && data.answers.length > 0) {
		return data as { type?: unknown; answers?: unknown; question?: string };
	}
	return undefined;
}

export function hasActiveQuestion(
	questionIndex: number | null | undefined | string
): boolean {
	return questionIndex != null && questionIndex !== '';
}

export type LivePhase = 'intro' | 'answer' | 'reveal' | 'rankings';

export function initialLivePhaseForQuestion(
	gameMode: unknown,
	introLeftSec: number
): LivePhase {
	if (isKahootStyleMode(gameMode)) {
		return 'answer';
	}
	return introLeftSec > 0 ? 'intro' : 'answer';
}

export type StandingsRow = {
	username: string;
	score: number;
	overall_rank: number;
	points_behind_above?: number;
	player_above?: string;
	points_ahead_of_next?: number;
};

export type QuestionResultsPayload = {
	questionIndex: number | null;
	rows: Array<Record<string, unknown>>;
	revealHoldSec: number;
	scoreboardHoldSec: number;
	standingsTop: StandingsRow[];
};

const DEFAULT_REVEAL_HOLD_SEC = 4;
const DEFAULT_SCOREBOARD_HOLD_SEC = 9;

/** Legacy bare arrays and wrapped `{ question_index, results }` payloads. */
export function parseQuestionResultsPayload(data: unknown): QuestionResultsPayload {
	if (Array.isArray(data)) {
		return {
			questionIndex: null,
			rows: data as Array<Record<string, unknown>>,
			revealHoldSec: DEFAULT_REVEAL_HOLD_SEC,
			scoreboardHoldSec: DEFAULT_SCOREBOARD_HOLD_SEC,
			standingsTop: []
		};
	}
	if (data && typeof data === 'object') {
		const obj = data as Record<string, unknown>;
		const rawRows = obj.results ?? obj.answers;
		if (Array.isArray(rawRows)) {
			const qi = obj.question_index;
			const questionIndex =
				qi === null || qi === undefined || qi === ''
					? null
					: Number(qi);
			const revealHoldSec = Number(obj.reveal_hold_sec);
			const scoreboardHoldSec = Number(obj.scoreboard_hold_sec);
			const standingsTop = Array.isArray(obj.standings_top)
				? (obj.standings_top as StandingsRow[])
				: [];
			return {
				questionIndex: Number.isFinite(questionIndex) ? questionIndex : null,
				rows: rawRows as Array<Record<string, unknown>>,
				revealHoldSec: Number.isFinite(revealHoldSec) ? revealHoldSec : DEFAULT_REVEAL_HOLD_SEC,
				scoreboardHoldSec: Number.isFinite(scoreboardHoldSec)
					? scoreboardHoldSec
					: DEFAULT_SCOREBOARD_HOLD_SEC,
				standingsTop
			};
		}
	}
	return {
		questionIndex: null,
		rows: [],
		revealHoldSec: DEFAULT_REVEAL_HOLD_SEC,
		scoreboardHoldSec: DEFAULT_SCOREBOARD_HOLD_SEC,
		standingsTop: []
	};
}

export function ordinalPlace(n: number): string {
	if (n === 1) return '1st';
	if (n === 2) return '2nd';
	if (n === 3) return '3rd';
	return `${n}th`;
}

/** Drop results for a question the client has already advanced past. */
export function isStaleQuestionResults(
	activeQuestionIndex: number | null | undefined,
	resultsQuestionIndex: number | null,
	latestQuestionIndex: number
): boolean {
	const active =
		activeQuestionIndex != null && activeQuestionIndex !== ''
			? Number(activeQuestionIndex)
			: null;
	const latest = Number.isFinite(latestQuestionIndex) ? latestQuestionIndex : -1;

	if (resultsQuestionIndex != null && Number.isFinite(resultsQuestionIndex)) {
		if (latest > resultsQuestionIndex) {
			return true;
		}
		if (active != null && Number.isFinite(active) && active > resultsQuestionIndex) {
			return true;
		}
		return false;
	}

	// Legacy bare arrays have no question_index — treat as stale once the client has advanced.
	if (latest > 0) {
		return true;
	}
	if (active != null && Number.isFinite(active) && active > 0) {
		return true;
	}
	return false;
}
