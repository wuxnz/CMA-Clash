// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import { routeNeedsSessionRefresh } from './protectedRoutes';

describe('routeNeedsSessionRefresh', () => {
	it('includes site-admin paths', () => {
		expect(routeNeedsSessionRefresh('/site-admin/users')).toBe(true);
		expect(routeNeedsSessionRefresh('/site-admin')).toBe(true);
	});

	it('excludes public explore', () => {
		expect(routeNeedsSessionRefresh('/explore')).toBe(false);
	});
});
