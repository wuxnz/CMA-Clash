// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import { applyQuestionResultScores, scoreDeltaForUser } from './live-scoring';

describe('applyQuestionResultScores', () => {
	it('adds each player score once per question index', () => {
		const rows = [{ username: 'Ada', score: 420 }, { username: 'Bob', score: 0 }];
		const first = applyQuestionResultScores({}, rows, 0, null);
		expect(first.scores).toEqual({ Ada: 420, Bob: 0 });
		expect(first.lastAppliedQuestionIndex).toBe(0);

		const dup = applyQuestionResultScores(first.scores, rows, 0, first.lastAppliedQuestionIndex);
		expect(dup.scores).toEqual({ Ada: 420, Bob: 0 });
	});

	it('accumulates across questions', () => {
		let scores: Record<string, number> = {};
		let last: number | null = null;
		({ scores, lastAppliedQuestionIndex: last } = applyQuestionResultScores(
			scores,
			[{ username: 'Ada', score: 100 }],
			0,
			last
		));
		({ scores, lastAppliedQuestionIndex: last } = applyQuestionResultScores(
			scores,
			[{ username: 'Ada', score: 250 }],
			1,
			last
		));
		expect(scores.Ada).toBe(350);
	});
});

describe('scoreDeltaForUser', () => {
	it('returns the row score shown in reveal UI', () => {
		const rows = [{ username: 'Ada', score: 512 }];
		expect(scoreDeltaForUser(rows, 'Ada')).toBe(512);
	});
});
