// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type BrowserContext, type Page } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { installLiveApiProxy } from './helpers/liveApiProxy';

const artifactDir = '/opt/cursor/artifacts/screenshots';

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
	await expect(page.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });
}

async function answerFirstTile(page: Page): Promise<void> {
	const tiles = page.getByTestId('answer-tiles');
	await expect(tiles).toBeVisible({ timeout: 120_000 });
	await tiles.locator('button').first().click();
}

test.describe('battle host without create nickname', () => {
	test.beforeAll(() => {
		fs.mkdirSync(artifactDir, { recursive: true });
	});

	test('guest host creates lobby, two players battle', async ({ browser }) => {
		const hostContext = await browser.newContext();
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();

		const code = await hostBattle(hostPage);
		await joinBattleLobby(hostPage, code, 'HostAlpha');

		const guestContext = await browser.newContext();
		await installLiveApiProxy(guestContext);
		const guestPage = await guestContext.newPage();
		await joinBattleLobby(guestPage, code, 'GuestBeta');

		await expect(hostPage.getByTestId('battle-lobby-players').locator('> *')).toHaveCount(2);
		await expect(hostPage.getByTestId('battle-lobby-players')).toContainText('HostAlpha');
		await expect(hostPage.getByTestId('battle-lobby-players')).toContainText('GuestBeta');

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-lobby-two-players.png'),
			fullPage: true
		});

		await hostPage.getByRole('button', { name: /start battle/i }).click();

		await waitForBattleQuestions(hostPage);
		await waitForBattleQuestions(guestPage);

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-production-q1-host.png'),
			fullPage: true
		});
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-production-q1-guest.png'),
			fullPage: true
		});

		await answerFirstTile(hostPage);
		await answerFirstTile(guestPage);

		await expect(hostPage.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });
		await expect(guestPage.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-production-q2-host.png'),
			fullPage: true
		});
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-production-q2-guest.png'),
			fullPage: true
		});

		await hostContext.close();
		await guestContext.close();
	});
});
