// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type BrowserContext, type Page } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { installLiveApiProxy } from './helpers/liveApiProxy';

const artifactDir = '/opt/cursor/artifacts/screenshots';

async function joinPlayer(context: BrowserContext, pin: string, name: string): Promise<Page> {
	const page = await context.newPage();
	await installLiveApiProxy(page.context());
	await page.goto('/play');
	await page.getByLabel(/game pin/i).fill(pin);
	await page.getByPlaceholder(/username/i).fill(name);
	await page.getByRole('button', { name: /submit/i }).click();
	await expect(page.getByText(pin)).toBeVisible({ timeout: 60_000 });
	return page;
}

async function startFromNavbarHost(page: Page, mode: 'Standard' | 'On player devices'): Promise<string> {
	await page.goto('/host');
	await page.getByRole('button', { name: /^Host$/ }).first().click({ timeout: 60_000 });
	await page.getByRole('radio', { name: mode }).click();
	await page.getByRole('button', { name: 'Start game' }).click();
	await page.waitForURL(/\/admin\?/, { timeout: 90_000 });
	const url = new URL(page.url());
	const pin = url.searchParams.get('pin');
	expect(pin).toBeTruthy();
	return pin!;
}

test.describe('live host navbar flow', () => {
	test.use({ viewport: { width: 390, height: 844 } });

	test.beforeAll(() => {
		fs.mkdirSync(artifactDir, { recursive: true });
	});

	test('standard mode: host and players see answer UI', async ({ browser }) => {
		const hostContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();

		const pin = await startFromNavbarHost(hostPage, 'Standard');

		const p1 = await joinPlayer(await browser.newContext(), pin, 'PlayerA1');
		const p2 = await joinPlayer(await browser.newContext(), pin, 'PlayerA2');

		await hostPage.getByTestId('lobby-start-game').click({ timeout: 90_000 });

		await expect(p1.getByTestId('answer-tiles')).toBeVisible({ timeout: 90_000 });
		await expect(p1.locator('svg circle[r="18"]')).toHaveCount(0);

		await hostPage.screenshot({
			path: path.join(artifactDir, 'live-host-standard-mobile.png'),
			fullPage: true
		});
		await p1.screenshot({
			path: path.join(artifactDir, 'live-player-standard-mobile.png'),
			fullPage: true
		});

		await p1.locator('button').first().click();
		await expect(p1.getByText(/Correct|Incorrect/i)).toBeVisible({ timeout: 60_000 });

		await hostContext.close();
		await p1.context().close();
		await p2.context().close();
	});

	test('on player devices: host progress view', async ({ browser }) => {
		const hostContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();

		const pin = await startFromNavbarHost(hostPage, 'On player devices');
		const playerPage = await joinPlayer(await browser.newContext(), pin, 'PlayerB1');

		await hostPage.getByTestId('lobby-start-game').click({ timeout: 90_000 });
		await expect(hostPage.getByText(/Players see the question/i)).toBeVisible({ timeout: 90_000 });
		await expect(playerPage.getByTestId('answer-tiles')).toBeVisible({ timeout: 90_000 });
		await expect(playerPage.getByText(/Which|Is|Do/i).first()).toBeVisible({ timeout: 90_000 });

		await hostPage.screenshot({
			path: path.join(artifactDir, 'live-host-normal-mobile.png'),
			fullPage: true
		});
		await playerPage.screenshot({
			path: path.join(artifactDir, 'live-player-normal-mobile.png'),
			fullPage: true
		});

		await hostContext.close();
		await playerPage.context().close();
	});
});
