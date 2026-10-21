// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import {
	hasActiveQuestion,
	initialLivePhaseForQuestion,
	isKahootStyleMode,
	normalizeGamePayload
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

describe('initialLivePhaseForQuestion', () => {
	it('skips intro for kahoot so players see answer tiles immediately', () => {
		expect(initialLivePhaseForQuestion('kahoot', 3.5)).toBe('answer');
	});

	it('uses intro for normal mode when time remains', () => {
		expect(initialLivePhaseForQuestion('normal', 2)).toBe('intro');
		expect(initialLivePhaseForQuestion('normal', 0)).toBe('answer');
	});
});
