// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import {
	aggregateScoresFromFinalResults,
	applyQuestionResultScores,
	integrateLiveQuestionResults,
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

	it('includes the streak multiplier in the server score', () => {
		const rows = [{ username: 'Ada', score: 1100, base_score: 500, speed_bonus: 383 }];
		expect(scoreDeltaForUser(rows, 'Ada')).toBe(1100);
	});

	it('is zero for a wrong answer even when base and speed are recorded', () => {
		const rows = [{ username: 'Ada', score: 0, base_score: 500, speed_bonus: 383 }];
		expect(scoreDeltaForUser(rows, 'Ada')).toBe(0);
	});

	it('falls back to base + speed when the row has no score', () => {
		const rows = [{ username: 'Ada', base_score: 500, speed_bonus: 383 }];
		expect(scoreDeltaForUser(rows, 'Ada')).toBe(883);
	});
});

describe('integrateLiveQuestionResults', () => {
	it('syncs totals from standings_top and survives duplicate re-emits without standings', () => {
		const top = [
			{ username: 'P1', score: 883, overall_rank: 1, points_ahead_of_next: 5 },
			{ username: 'P2', score: 878, overall_rank: 2, points_behind_above: 5 }
		];
		const rows = [
			{ username: 'P1', score: 883, base_score: 500, speed_bonus: 383 },
			{ username: 'P2', score: 878, base_score: 500, speed_bonus: 378 }
		];
		let state = integrateLiveQuestionResults(
			{ scores: {}, lastAppliedQuestionIndex: null, standingsTop: [] },
			{ questionIndex: 0, rows, standingsTop: top }
		);
		expect(state.scores).toEqual({ P1: 883, P2: 878 });
		expect(state.standingsTop).toEqual(top);

		// Stale per-row-only re-emit (no standings_top) must not wipe authoritative totals.
		state = integrateLiveQuestionResults(state, {
			questionIndex: 0,
			rows: [{ username: 'P1', score: 425 }],
			standingsTop: []
		});
		expect(state.scores).toEqual({ P1: 883, P2: 878 });
		expect(state.standingsTop).toEqual(top);
	});

	it('replaces wrong summed totals when a full payload arrives after a legacy row sum', () => {
		const legacy = integrateLiveQuestionResults(
			{ scores: {}, lastAppliedQuestionIndex: null, standingsTop: [] },
			{
				questionIndex: 0,
				rows: [{ username: 'P1', score: 425 }],
				standingsTop: []
			}
		);
		expect(legacy.scores.P1).toBe(425);

		const fixed = integrateLiveQuestionResults(legacy, {
			questionIndex: 0,
			rows: [{ username: 'P1', score: 883, base_score: 500, speed_bonus: 383 }],
			standingsTop: [{ username: 'P1', score: 883, overall_rank: 1 }]
		});
		expect(fixed.scores.P1).toBe(883);
	});
});
