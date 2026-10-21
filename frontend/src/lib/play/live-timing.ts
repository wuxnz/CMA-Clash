// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

export type LivePhase = 'intro' | 'answer' | 'reveal' | 'rankings';

function isKahootStyleMode(gameMode: unknown): boolean {
	return gameMode === 'kahoot' || gameMode === 'battle' || gameMode == null || gameMode === '';
}

export type QuestionTiming = {
	question_index: number;
	question_start_ms: number;
	intro_deadline_ms: number;
	answer_phase_start_ms: number;
	answer_deadline_ms: number;
	server_time_ms?: number;
};

export function applyClockSync(serverTimeMs: number, receivedAtMs: number = Date.now()): number {
	return serverTimeMs - receivedAtMs;
}

export function serverNowMs(clockOffsetMs: number, localNowMs: number = Date.now()): number {
	return localNowMs + clockOffsetMs;
}

export function parseQuestionTiming(
	data: Record<string, unknown> | null | undefined,
	gameMode: unknown,
	fallbackQuestionSeconds: number
): QuestionTiming | null {
	if (!data || data.question_index == null) return null;
	const idx = Number(data.question_index);
	const qObj = data['question'] as { time?: unknown } | undefined;
	const totalMs = Math.max(
		1000,
		(parseInt(String(qObj?.time ?? fallbackQuestionSeconds)) || 30) * 1000
	);

	const start = num(data.question_start_ms) ?? num(data.server_time_ms);
	const introEnd = num(data.intro_deadline_ms);
	const answerStart = num(data.answer_phase_start_ms);
	const answerEnd = num(data.answer_deadline_ms);

	if (start != null && introEnd != null && answerStart != null && answerEnd != null) {
		return {
			question_index: idx,
			question_start_ms: start,
			intro_deadline_ms: introEnd,
			answer_phase_start_ms: answerStart,
			answer_deadline_ms: answerEnd,
			server_time_ms: num(data.server_time_ms)
		};
	}

	// Legacy ISO fallback (older servers)
	const iso = typeof data.question_started_at === 'string' ? data.question_started_at : null;
	if (!iso) return null;
	const startMs = Date.parse(iso);
	if (Number.isNaN(startMs)) return null;
	const introMs = isKahootStyleMode(gameMode) ? 0 : 3500;
	const introDeadline = startMs + introMs;
	return {
		question_index: idx,
		question_start_ms: startMs,
		intro_deadline_ms: introDeadline,
		answer_phase_start_ms: introDeadline,
		answer_deadline_ms: introDeadline + totalMs,
		server_time_ms: num(data.server_time_ms)
	};
}

function num(v: unknown): number | null {
	if (v == null) return null;
	const n = Number(v);
	return Number.isFinite(n) ? n : null;
}

export function resolveLivePhase(
	timing: QuestionTiming,
	gameMode: unknown,
	nowMs: number
): LivePhase {
	if (!isKahootStyleMode(gameMode) && nowMs < timing.intro_deadline_ms) {
		return 'intro';
	}
	return 'answer';
}

export function remainingIntroSeconds(timing: QuestionTiming, nowMs: number): number {
	return Math.max(0, (timing.intro_deadline_ms - nowMs) / 1000);
}

export function remainingAnswerSeconds(timing: QuestionTiming, nowMs: number): number {
	return Math.max(0, (timing.answer_deadline_ms - nowMs) / 1000);
}

export function totalAnswerSeconds(timing: QuestionTiming): number {
	return Math.max(1, (timing.answer_deadline_ms - timing.answer_phase_start_ms) / 1000);
}
