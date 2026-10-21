// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import {
	hasActiveQuestion,
	hasChoiceTileAnswers,
	initialLivePhaseForQuestion,
	isKahootStyleMode,
	normalizeGamePayload,
	questionFromSocketPayload
} from './live-game';

describe('normalizeGamePayload', () => {
	it('unwraps tuple-shaped joined_game data', () => {
		const inner = { game_pin: '123456', game_mode: 'kahoot' };
		expect(normalizeGamePayload([inner])).toEqual(inner);
	});

	it('passes through plain objects', () => {
		const obj = { game_mode: 'normal' };
		expect(normalizeGamePayload(obj)).toEqual(obj);
	});
});

describe('isKahootStyleMode', () => {
	it('treats kahoot and battle as tile mode', () => {
		expect(isKahootStyleMode('kahoot')).toBe(true);
		expect(isKahootStyleMode('battle')).toBe(true);
	});

	it('treats normal as full-question-on-device mode', () => {
		expect(isKahootStyleMode('normal')).toBe(false);
	});
});

describe('hasActiveQuestion', () => {
	it('accepts question index zero', () => {
		expect(hasActiveQuestion(0)).toBe(true);
	});

	it('rejects empty waiting state', () => {
		expect(hasActiveQuestion(null)).toBe(false);
		expect(hasActiveQuestion('')).toBe(false);
	});
});

describe('hasChoiceTileAnswers', () => {
	it('accepts ABCD and voting arrays', () => {
		expect(
			hasChoiceTileAnswers({
				type: 'ABCD',
				question: 'Q?',
				answers: [{ answer: 'A', right: true }],
				time: '30'
			})
		).toBe(true);
		expect(
			hasChoiceTileAnswers({
				type: 'VOTING',
				question: 'Q?',
				answers: [{ answer: 'A' }],
				time: '30'
			})
		).toBe(true);
	});

	it('rejects range and empty answers', () => {
		expect(
			hasChoiceTileAnswers({
				type: 'RANGE',
				question: 'Q?',
				answers: { min: 0, max: 10 },
				time: '30'
			})
		).toBe(false);
		expect(hasChoiceTileAnswers({ type: 'ABCD', question: 'Q?', answers: [], time: '30' })).toBe(
			false
		);
	});
});

describe('questionFromSocketPayload', () => {
	it('reads nested question', () => {
		const q = { question: 'Hi', answers: [{ answer: 'a' }], type: 'ABCD', time: '30' };
		expect(questionFromSocketPayload({ question_index: 0, question: q })?.question).toBe('Hi');
	});
});

describe('initialLivePhaseForQuestion', () => {
	it('skips intro for kahoot so players see answer tiles immediately', () => {
		expect(initialLivePhaseForQuestion('kahoot', 3.5)).toBe('answer');
	});

	it('uses intro for normal mode when time remains', () => {
		expect(initialLivePhaseForQuestion('normal', 2)).toBe('intro');
		expect(initialLivePhaseForQuestion('normal', 0)).toBe('answer');
	});
});
