// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, test } from '@playwright/test';

const mockEntries = [
	{ rank: 1, user_id: '00000000-0000-4000-8000-000000000001', username: 'LedgerAce', xp: 4200, level: 5 },
	{ rank: 2, user_id: '00000000-0000-4000-8000-000000000002', username: 'StudyPro', xp: 3100, level: 4 }
];

test.describe('leaderboard page', () => {
	test.beforeEach(async ({ context }) => {
		await context.route('**/api/v1/clash/leaderboards?*', async (route) => {
			const url = new URL(route.request().url());
			const period = url.searchParams.get('period');
			const payload = period === 'weekly' ? [mockEntries[0]] : mockEntries;
			await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(payload) });
		});
		await context.route('**/api/v1/clash/me/gamification', async (route) => {
			await route.fulfill({
				status: 401,
				contentType: 'application/json',
				body: JSON.stringify({ detail: 'Not authenticated' })
			});
		});
	});

	test('renders users with XP in the standings table', async ({ page }) => {
		await page.goto('/leaderboard');
		await expect(page.getByRole('heading', { name: 'Leaderboard' })).toBeVisible();
		await expect(page.getByRole('table', { name: 'League standings' })).toBeVisible({ timeout: 15_000 });
		await expect(page.getByRole('cell', { name: 'LedgerAce (Lv 5)' })).toBeVisible();
		await expect(page.getByRole('cell', { name: '4,200' })).toBeVisible();
		await expect(page.getByTestId('podium-root')).toBeVisible();
	});
});
