// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import { formatApiErrorDetail } from './apiErrorDetail';

describe('formatApiErrorDetail', () => {
	it('reads message from object detail', () => {
		expect(
			formatApiErrorDetail({ code: 'rate_limited', message: 'Too many requests. Try again later.' })
		).toBe('Too many requests. Try again later.');
	});

	it('reads string detail', () => {
		expect(formatApiErrorDetail('User deletion failed: boom')).toBe('User deletion failed: boom');
	});
});
