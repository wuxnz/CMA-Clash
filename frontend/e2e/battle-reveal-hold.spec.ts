// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect } from '@playwright/test';
import path from 'node:path';
import { installLiveApiProxy } from './helpers/liveApiProxy';

const ARTIFACT_DIR =
	process.env.PLAYWRIGHT_ARTIFACT_DIR ?? '/opt/cursor/artifacts/battle-reveal-hold';

test.describe('battle reveal hold', () => {
	test.describe.configure({ timeout: 240_000 });
	test.use({ viewport: { width: 390, height: 844 } });

	test('2-player battle keeps reveal visible at least 7 seconds', async ({ browser }) => {
		const hostContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();
		await hostPage.goto('/battle');
		await hostPage.locator('button.action-button', { hasText: 'Host' }).first().click({ timeout: 60_000 });
		await expect(hostPage).toHaveURL(/\/battle\/\d+/, { timeout: 30_000 });
		const code = new URL(hostPage.url()).pathname.split('/').pop()!;

		await hostPage.goto(`/battle/${code}`);
		await hostPage.getByPlaceholder(/nickname/i).fill('HoldHost');
		await hostPage.getByRole('button', { name: /join battle/i }).click();

		const guestContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
		await installLiveApiProxy(guestContext);
		const guestPage = await guestContext.newPage();
		await guestPage.goto(`/battle/${code}`);
		await guestPage.getByPlaceholder(/nickname/i).fill('HoldGuest');
		await guestPage.getByRole('button', { name: /join battle/i }).click();

		await hostPage.getByRole('button', { name: /start battle/i }).click();
		await hostPage.waitForURL(/\/play\?pin=/, { timeout: 120_000 });
		await guestPage.waitForURL(/\/play\?pin=/, { timeout: 120_000 });

		const answerTiles = (page: import('@playwright/test').Page) => page.getByTestId('answer-tiles');
		await expect(answerTiles(hostPage)).toBeVisible({ timeout: 120_000 });
		await answerTiles(hostPage).locator('button').first().click();
		await answerTiles(guestPage).locator('button').first().click();

		const reveal = guestPage.getByTestId('reveal-correct-answer');
		await expect(reveal).toBeVisible({ timeout: 90_000 });
		const visibleAt = Date.now();
		await expect(reveal).toBeVisible({ timeout: 8_000 });
		expect(Date.now() - visibleAt).toBeGreaterThanOrEqual(7_000);

		await guestPage.screenshot({
			path: path.join(ARTIFACT_DIR, 'battle-reveal-mobile.png'),
			fullPage: true
		});

		const rankings = guestPage.getByTestId('live-scoreboard');
		await expect(rankings).toBeVisible({ timeout: 20_000 });
		await guestPage.screenshot({
			path: path.join(ARTIFACT_DIR, 'battle-scoreboard-mobile.png'),
			fullPage: true
		});

		await hostContext.close();
		await guestContext.close();
	});
});
