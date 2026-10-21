// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, test } from '@playwright/test';

test.describe('navbar active state', () => {
	test('explore link has aria-current on /explore', async ({ page }) => {
		await page.goto('/explore');
		const explore = page.locator('nav[aria-label="Main navigation"] a[href="/explore"]');
		await expect(explore).toHaveAttribute('aria-current', 'page');
	});

	test('home link has aria-current on /', async ({ page }) => {
		await page.goto('/');
		const home = page.locator('nav[aria-label="Main navigation"] a[href="/"]').first();
		await expect(home).toHaveAttribute('aria-current', 'page');
	});
});
