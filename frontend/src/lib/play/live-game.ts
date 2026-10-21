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
	if (typeof type === 'string') return type;
	return String(type);
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
