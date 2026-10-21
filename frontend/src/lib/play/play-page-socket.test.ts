// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { beforeEach, describe, expect, it, vi } from 'vitest';

vi.mock('$app/environment', () => ({ browser: true }));
vi.mock('$lib/socket', () => ({
	socket: { on: vi.fn(), off: vi.fn() }
}));

import {
	isPlaySocketBoundToExpectedPin,
	markPlaySocketBound,
	resetPlaySocketBinding,
	setExpectedPlayPin
} from './play-socket-pin';

describe('play socket pin binding', () => {
	beforeEach(() => {
		resetPlaySocketBinding();
		setExpectedPlayPin('');
	});

	it('ignores binding when pin does not match URL', () => {
		setExpectedPlayPin('222222');
		markPlaySocketBound('111111');
		expect(isPlaySocketBoundToExpectedPin()).toBe(false);
	});

	it('accepts binding when pin matches URL', () => {
		setExpectedPlayPin('222222');
		markPlaySocketBound('222222');
		expect(isPlaySocketBoundToExpectedPin()).toBe(true);
	});

	it('reset clears binding', () => {
		setExpectedPlayPin('222222');
		markPlaySocketBound('222222');
		resetPlaySocketBinding();
		expect(isPlaySocketBoundToExpectedPin()).toBe(false);
	});
});
