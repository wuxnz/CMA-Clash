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

export function isKahootStyleMode(gameMode: unknown): boolean {
	return gameMode === 'kahoot' || gameMode === 'battle' || gameMode == null || gameMode === '';
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
