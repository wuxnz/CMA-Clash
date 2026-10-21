// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type Page } from '@playwright/test';
import path from 'node:path';
import { installLiveApiProxy } from './helpers/liveApiProxy';

async function joinBattleLobby(page: Page, code: string, nickname: string): Promise<void> {
	await page.goto(`/battle/${code}`);
	await page.getByPlaceholder(/nickname/i).fill(nickname);
	await page.getByRole('button', { name: /join battle/i }).click();
	await expect(page.getByTestId('battle-lobby-players').getByText(nickname)).toBeVisible({
		timeout: 30_000
	});
}

async function waitForBattleQuestions(page: Page, label: string): Promise<void> {
	await page.waitForURL(/\/play\?pin=/, { timeout: 120_000 });
	await expect(
		page.getByText(/not connected to the game server/i),
		`${label}: no socket error`
	).toHaveCount(0);
	const connecting = page.getByText(/connecting to game server/i);
	if (await connecting.isVisible().catch(() => false)) {
		await expect(connecting).toBeHidden({ timeout: 120_000 });
	}
	const submit = page.getByRole('button', { name: /submit/i });
	for (let i = 0; i < 45; i++) {
		if (await page.getByTestId('answer-tiles').isVisible().catch(() => false)) break;
		if (await submit.isEnabled().catch(() => false)) {
			await submit.click();
		}
		await page.waitForTimeout(1500);
	}
	await expect(page.getByTestId('answer-tiles'), label).toBeVisible({ timeout: 120_000 });
}

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

		await joinBattleLobby(hostPage, code, 'HoldHost');

		const guestContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
		await installLiveApiProxy(guestContext);
		const guestPage = await guestContext.newPage();
		await joinBattleLobby(guestPage, code, 'HoldGuest');

		await hostPage.getByRole('button', { name: /start battle/i }).click();
		await waitForBattleQuestions(hostPage, 'host Q1');
		await waitForBattleQuestions(guestPage, 'guest Q1');

		const answerTiles = (page: Page) => page.getByTestId('answer-tiles');
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
