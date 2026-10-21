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
	await page.getByRole('button', { name: /^Host$/ }).first().click({ timeout: 60_000 });
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

async function enterPlayFromLobby(page: Page): Promise<void> {
	const enter = page.getByRole('link', { name: /enter game/i });
	if (await enter.isVisible().catch(() => false)) {
		await enter.click();
	} else {
		await page.waitForURL(/\/play\?pin=/, { timeout: 120_000 });
	}
	await expect(page.getByTestId('answer-tiles').or(page.locator('button').first())).toBeVisible({
		timeout: 120_000
	});
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
		await guestPage.waitForURL(/\/play\?pin=/, { timeout: 120_000 }).catch(() => undefined);
		await hostPage.waitForURL(/\/play\?pin=/, { timeout: 120_000 }).catch(() => undefined);

		await enterPlayFromLobby(hostPage);
		await enterPlayFromLobby(guestPage);

		await expect(hostPage.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });
		await expect(guestPage.getByTestId('answer-tiles')).toBeVisible({ timeout: 120_000 });

		await hostContext.close();
		await guestContext.close();
	});
});
