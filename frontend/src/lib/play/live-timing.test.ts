// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import {
	applyClockSync,
	parseQuestionTiming,
	remainingAnswerSeconds,
	remainingIntroSeconds,
	resolveLivePhase,
	serverNowMs,
	totalAnswerSeconds
} from './live-timing';

const timing = {
	question_index: 0,
	question_start_ms: 1_000_000,
	intro_deadline_ms: 1_003_500,
	answer_phase_start_ms: 1_003_500,
	answer_deadline_ms: 1_013_500,
	server_time_ms: 1_000_000
};

describe('clock sync', () => {
	it('computes offset from server time', () => {
		expect(applyClockSync(10_500, 10_000)).toBe(500);
		expect(serverNowMs(500, 10_000)).toBe(10_500);
	});
});

describe('parseQuestionTiming', () => {
	it('reads deadline fields from socket payload', () => {
		const parsed = parseQuestionTiming(
			{
				question_index: 0,
				question_start_ms: 100,
				intro_deadline_ms: 100,
				answer_phase_start_ms: 100,
				answer_deadline_ms: 31_100,
				server_time_ms: 100,
				question: { time: '31' }
			},
			'kahoot',
			30
		);
		expect(parsed?.answer_deadline_ms).toBe(31_100);
	});

	it('resumes phase after intro for normal mode', () => {
		const parsed = parseQuestionTiming(
			{
				question_index: 1,
				question_start_ms: 0,
				intro_deadline_ms: 3500,
				answer_phase_start_ms: 3500,
				answer_deadline_ms: 13_500,
				question: { time: '10' }
			},
			'normal',
			10
		)!;
		expect(resolveLivePhase(parsed, 'normal', 2000)).toBe('intro');
		expect(resolveLivePhase(parsed, 'normal', 4000)).toBe('answer');
		expect(remainingAnswerSeconds(parsed, 8000)).toBe(5.5);
	});
});

describe('resolveLivePhase', () => {
	it('skips intro for kahoot', () => {
		const kahootTiming = { ...timing, intro_deadline_ms: timing.question_start_ms };
		expect(resolveLivePhase(kahootTiming, 'kahoot', timing.question_start_ms)).toBe('answer');
	});

	it('counts intro remaining', () => {
		expect(remainingIntroSeconds(timing, 1_002_000)).toBe(1.5);
		expect(totalAnswerSeconds(timing)).toBe(10);
	});
});
