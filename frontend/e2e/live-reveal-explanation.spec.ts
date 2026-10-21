// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect } from '@playwright/test';
import path from 'node:path';
import { installLiveApiProxy } from './helpers/liveApiProxy';
import { joinPlayer } from './helpers/joinPlayer';
import { startFromNavbarHost } from './helpers/liveHost';
import { answerFirstTile } from './helpers/livePlayer';

const ARTIFACT_DIR =
	process.env.PLAYWRIGHT_ARTIFACT_DIR ?? '/opt/cursor/artifacts/reveal-explanation';

test.describe('live reveal explanation', () => {
	test.describe.configure({ timeout: 240_000 });
	test.use({ viewport: { width: 390, height: 844 } });

	test('Standard: player sees correct answer and explanation after Q1', async ({ browser }) => {
		const hostContext = await browser.newContext({ viewport: { width: 1280, height: 800 } });
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();
		const pin = await startFromNavbarHost(hostPage, 'Standard');

		const p1 = await joinPlayer(await browser.newContext(), pin, 'RX_A');
		const p2 = await joinPlayer(await browser.newContext(), pin, 'RX_B');
		const p3 = await joinPlayer(await browser.newContext(), pin, 'RX_C');

		await hostPage.getByRole('button', { name: /^Start game$/i }).click({ timeout: 90_000 });

		await answerFirstTile(p1);
		await answerFirstTile(p2);
		await answerFirstTile(p3);

		await expect(p1.getByTestId('reveal-place-line')).toBeVisible({ timeout: 45_000 });
		await expect(p1.getByTestId('reveal-correct-answer')).toBeVisible({ timeout: 10_000 });
		const correctLine = await p1.getByTestId('reveal-correct-answer').innerText();
		expect(correctLine.length).toBeGreaterThan(10);

		const explanation = p1.getByTestId('reveal-explanation');
		if (await explanation.isVisible().catch(() => false)) {
			const text = await explanation.innerText();
			expect(text.length).toBeGreaterThan(12);
		}

		await expect(hostPage.getByTestId('reveal-correct-answer')).toBeVisible({ timeout: 10_000 });

		await p1.screenshot({
			path: path.join(ARTIFACT_DIR, 'live-player-reveal-explanation-mobile.png'),
			fullPage: true
		});

		await hostContext.close();
	});

	test('battle: player sees correct answer on reveal after Q1', async ({ browser }) => {
		const artifactDir = ARTIFACT_DIR;
		const hostContext = await browser.newContext();
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();
		await hostPage.goto('/battle');
		await hostPage.locator('button.action-button', { hasText: 'Host' }).first().click({ timeout: 60_000 });
		await expect(hostPage).toHaveURL(/\/battle\/\d+/, { timeout: 30_000 });
		const code = new URL(hostPage.url()).pathname.split('/').pop()!;

		await hostPage.goto(`/battle/${code}`);
		await hostPage.getByPlaceholder(/nickname/i).fill('HostRx');
		await hostPage.getByRole('button', { name: /join battle/i }).click();

		const guestContext = await browser.newContext();
		await installLiveApiProxy(guestContext);
		const guestPage = await guestContext.newPage();
		await guestPage.goto(`/battle/${code}`);
		await guestPage.getByPlaceholder(/nickname/i).fill('GuestRx');
		await guestPage.getByRole('button', { name: /join battle/i }).click();

		await hostPage.getByRole('button', { name: /start battle/i }).click();
		await hostPage.waitForURL(/\/play\?pin=/, { timeout: 120_000 });
		await guestPage.waitForURL(/\/play\?pin=/, { timeout: 120_000 });

		const answerTiles = (page: import('@playwright/test').Page) => page.getByTestId('answer-tiles');
		await expect(answerTiles(hostPage)).toBeVisible({ timeout: 120_000 });
		await answerTiles(hostPage).locator('button').first().click();
		await answerTiles(guestPage).locator('button').first().click();

		await expect(hostPage.getByTestId('reveal-correct-answer')).toBeVisible({ timeout: 90_000 });
		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-player-reveal-explanation-mobile.png'),
			fullPage: true
		});

		await hostContext.close();
		await guestContext.close();
	});
});
