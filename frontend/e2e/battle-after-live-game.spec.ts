// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type Page } from '@playwright/test';
import { installLiveApiProxy } from './helpers/liveApiProxy';
import fs from 'node:fs';
import path from 'node:path';
const artifactDir = '/opt/cursor/artifacts/screenshots';

const STALE_LIVE_PIN = '111111';

async function seedStaleLiveGameCookie(context: import('@playwright/test').BrowserContext) {
	await context.addCookies([
		{
			name: 'joined_game',
			value: JSON.stringify({
				sid: 'stale-sid',
				username: 'OldLiveHost',
				game_pin: STALE_LIVE_PIN
			}),
			domain: '127.0.0.1',
			path: '/'
		}
	]);
}

async function hostBattle(page: Page): Promise<string> {
	await page.goto('/battle');
	await page.locator('button.action-button', { hasText: 'Host' }).first().click({ timeout: 60_000 });
	await expect(page).toHaveURL(/\/battle\/\d+/, { timeout: 30_000 });
	const segments = new URL(page.url()).pathname.split('/');
	return segments[segments.length - 1]!;
}

async function joinBattleLobby(page: Page, code: string, nickname: string): Promise<void> {
	await page.goto(`/battle/${code}`);
	await page.getByPlaceholder(/nickname/i).fill(nickname);
	await page.getByRole('button', { name: /join battle/i }).click();
	await expect(page.getByTestId('battle-lobby-players').getByText(nickname)).toBeVisible({
		timeout: 30_000
	});
}

async function waitForBattleQuestions(page: Page): Promise<void> {
	await page.waitForURL(/\/play\?pin=/, { timeout: 120_000 });
	const submit = page.getByRole('button', { name: /submit/i });
	for (let i = 0; i < 30; i++) {
		if (await page.getByTestId('answer-tiles').isVisible().catch(() => false)) break;
		if (await submit.isEnabled().catch(() => false)) {
			await submit.click();
		}
		await page.waitForTimeout(2000);
	}
	await expect(page.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });
}

async function answerFirstTile(page: Page): Promise<void> {
	const tiles = page.getByTestId('answer-tiles');
	await expect(tiles).toBeVisible({ timeout: 120_000 });
	await tiles.locator('button').first().click();
}

test.describe('battle after live game in same browser', () => {
	test.beforeAll(() => {
		fs.mkdirSync(artifactDir, { recursive: true });
	});

	test('no stale live pin; host starts battle; both see Q1 and Q2', async ({ browser }) => {
		const hostContext = await browser.newContext();
		await installLiveApiProxy(hostContext);
		await seedStaleLiveGameCookie(hostContext);
		const hostPage = await hostContext.newPage();
		await hostPage.goto(`/play?pin=${STALE_LIVE_PIN}`);
		await expect(hostPage.getByText(STALE_LIVE_PIN)).toBeVisible({ timeout: 30_000 });

		const code = await hostBattle(hostPage);
		await joinBattleLobby(hostPage, code, 'HostAlpha');

		const guestContext = await browser.newContext();
		await installLiveApiProxy(guestContext);
		const guestPage = await guestContext.newPage();
		await joinBattleLobby(guestPage, code, 'GuestBeta');

		await hostPage.getByRole('button', { name: /start battle/i }).click();

		await waitForBattleQuestions(hostPage);
		await waitForBattleQuestions(guestPage);

		const hostUrlPin = new URL(hostPage.url()).searchParams.get('pin');
		const guestUrlPin = new URL(guestPage.url()).searchParams.get('pin');
		expect(hostUrlPin).toBeTruthy();
		expect(hostUrlPin).toBe(guestUrlPin);
		await expect(hostPage.getByText(STALE_LIVE_PIN)).toHaveCount(0);

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q1-host.png'),
			fullPage: true
		});
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q1-guest.png'),
			fullPage: true
		});

		await answerFirstTile(hostPage);
		await answerFirstTile(guestPage);

		await expect(hostPage.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });
		await expect(guestPage.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q2-host.png'),
			fullPage: true
		});
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q2-guest.png'),
			fullPage: true
		});

		await hostContext.close();
		await guestContext.close();
	});
});
