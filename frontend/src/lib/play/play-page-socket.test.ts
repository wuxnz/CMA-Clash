// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it, vi, beforeEach } from 'vitest';

/**
 * Documents the play-page socket bridge: only the bound instance should receive events.
 */
describe('play page socket binding pattern', () => {
	let active: { onSetQuestionNumber: (d: Record<string, unknown>) => void } | null = null;
	const dispatch = (data: Record<string, unknown>) => active?.onSetQuestionNumber(data);

	beforeEach(() => {
		active = null;
	});

	it('dispatches to the currently bound handler', () => {
		const a = vi.fn();
		const b = vi.fn();
		active = { onSetQuestionNumber: a };
		dispatch({ question_index: 1 });
		expect(a).toHaveBeenCalledTimes(1);
		active = { onSetQuestionNumber: b };
		dispatch({ question_index: 2 });
		expect(b).toHaveBeenCalledWith({ question_index: 2 });
		expect(a).toHaveBeenCalledTimes(1);
	});

	it('no-op when unbound', () => {
		active = null;
		expect(() => dispatch({ question_index: 0 })).not.toThrow();
	});
});
