// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type BrowserContext, type Page } from '@playwright/test';
import { installLiveApiProxy } from './helpers/liveApiProxy';

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
	const pin = new URL(page.url()).searchParams.get('pin');
	expect(pin).toBeTruthy();
	return pin!;
}

async function answerFirstTile(page: Page) {
	const tile = page.getByTestId('answer-tiles').locator('button').first();
	await expect(tile).toBeVisible({ timeout: 90_000 });
	await tile.click();
}

async function expectPlayerOnAnswerTiles(page: Page) {
	await expect(page.getByTestId('answer-tiles')).toBeVisible({ timeout: 25_000 });
}

test.describe('live multi-question sync', () => {
	test.describe.configure({ timeout: 180_000 });
	test.use({ viewport: { width: 390, height: 844 } });

	for (const mode of ['Standard', 'On player devices'] as const) {
		test(`${mode}: players advance through Q2 and Q3 after all answer`, async ({ browser }) => {
			const hostContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
			await installLiveApiProxy(hostContext);
			const hostPage = await hostContext.newPage();
			const pin = await startFromNavbarHost(hostPage, mode);

			const p1 = await joinPlayer(await browser.newContext(), pin, `MQ1_${mode.slice(0, 3)}`);
			const p2 = await joinPlayer(await browser.newContext(), pin, `MQ2_${mode.slice(0, 3)}`);

			await hostPage.getByTestId('lobby-start-game').click({ timeout: 90_000 });
			await expectPlayerOnAnswerTiles(p1);
			await expectPlayerOnAnswerTiles(p2);

			for (let round = 0; round < 3; round++) {
				await answerFirstTile(p1);
				await answerFirstTile(p2);
				if (round < 2) {
					await expectPlayerOnAnswerTiles(p1);
					await expectPlayerOnAnswerTiles(p2);
				}
			}

			await hostContext.close();
			await p1.context().close();
			await p2.context().close();
		});
	}

	test('Standard: one player idle still advances both after timeout', async ({ browser }) => {
		const hostContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();
		const pin = await startFromNavbarHost(hostPage, 'Standard');

		const p1 = await joinPlayer(await browser.newContext(), pin, 'TimeoutP1');
		const p2 = await joinPlayer(await browser.newContext(), pin, 'TimeoutP2');

		await hostPage.getByTestId('lobby-start-game').click({ timeout: 90_000 });
		await expectPlayerOnAnswerTiles(p1);
		await answerFirstTile(p1);
		// p2 does not answer — server should close Q0 and auto-advance after reveal
		await expectPlayerOnAnswerTiles(p1);
		await expectPlayerOnAnswerTiles(p2);

		await hostContext.close();
		await p1.context().close();
		await p2.context().close();
	});
});
