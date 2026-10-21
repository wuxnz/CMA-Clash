// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import { behindOrLeadLine, placeLine, speedRankLine } from './live-standings-copy';

describe('live-standings-copy', () => {
	it('formats place and behind lines', () => {
		expect(placeLine({ overall_rank: 3 })).toBe("You're in 3rd place");
		expect(
			behindOrLeadLine({
				overall_rank: 2,
				points_behind_above: 45,
				player_above: 'Sam'
			})
		).toBe('45 points behind Sam');
	});

	it('formats lead for first place', () => {
		expect(
			behindOrLeadLine({ overall_rank: 1, points_ahead_of_next: 120 })
		).toBe('120 points ahead of 2nd place');
	});

	it('formats speed rank for correct answers', () => {
		expect(speedRankLine({ right: true, speed_rank: 2 })).toBe('You answered 2nd fastest');
		expect(speedRankLine({ right: false, speed_rank: 1 })).toBeNull();
	});
});
