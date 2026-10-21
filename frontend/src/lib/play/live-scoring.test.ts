// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import {
	aggregateScoresFromFinalResults,
	applyQuestionResultScores,
	scoreDeltaForUser
} from './live-scoring';

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

describe('aggregateScoresFromFinalResults', () => {
	it('sums scores per username across question buckets', () => {
		const payload = {
			'0': [{ username: 'HostAlpha', score: 400 }, { username: 'GuestBeta', score: 200 }],
			'1': [{ username: 'HostAlpha', score: 100 }, { username: 'GuestBeta', score: 350 }]
		};
		expect(aggregateScoresFromFinalResults(payload)).toEqual({
			HostAlpha: 500,
			GuestBeta: 550
		});
	});
});

describe('scoreDeltaForUser', () => {
	it('returns the row score shown in reveal UI', () => {
		const rows = [{ username: 'Ada', score: 512 }];
		expect(scoreDeltaForUser(rows, 'Ada')).toBe(512);
	});
});
