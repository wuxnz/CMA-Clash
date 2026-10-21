// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect } from '@playwright/test';
import path from 'node:path';
import { joinPlayer } from './helpers/joinPlayer';
import { hostLiveGame } from './helpers/hostViaSocket';
import type { HostModeLabel } from './helpers/liveHost';
import {
	answerFirstTile,
	expectPlayerAdvancedToNextQuestion,
	expectPlayerOnAnswerTiles
} from './helpers/livePlayer';

const ARTIFACT_DIR =
	process.env.PLAYWRIGHT_ARTIFACT_DIR ?? '/opt/cursor/artifacts/live-ui';

async function readRevealPoints(page: import('@playwright/test').Page): Promise<number> {
	const byTestId = page.getByTestId('reveal-points-total');
	if (await byTestId.count()) {
		return Number((await byTestId.innerText()).replace(/[^\d]/g, ''));
	}
	const block = page.getByText('Correct', { exact: true }).locator('xpath=..');
	const breakdown = block.getByText(/\d+ base/);
	if (await breakdown.count()) {
		const text = await breakdown.innerText();
		const m = text.match(/(\d+)\s+base(?:,\s*(\d+)\s+speed bonus)?/);
		if (m) {
			return Number(m[1]) + Number(m[2] ?? 0);
		}
	}
	return Number((await block.locator('p.font-display.text-3xl').innerText()).replace(/[^\d]/g, ''));
}

async function waitForRevealPoints(page: import('@playwright/test').Page, min = 500): Promise<number> {
	let last = 0;
	await expect
		.poll(async () => {
			last = await readRevealPoints(page);
			return last;
		}, { timeout: 20_000 })
		.toBeGreaterThan(min);
	return last;
}

async function expectRevealStats(
	page: import('@playwright/test').Page,
	revealTimeoutMs = 45_000
): Promise<number> {
	await expect(page.getByTestId('reveal-place-line')).toBeVisible({ timeout: revealTimeoutMs });
	await expect(page.getByTestId('reveal-speed-rank')).toBeVisible();
	await expect(page.getByText(/speed bonus/i)).toBeVisible();
	const behind = page.getByTestId('reveal-behind-line');
	if (await behind.isVisible().catch(() => false)) {
		await expect(behind).toContainText(/behind|ahead of/i);
	}
	return waitForRevealPoints(page);
}

test.describe('production live multi-question UI', () => {
	test.describe.configure({ timeout: 360_000, mode: 'serial' });

	for (const mode of ['Standard', 'On player devices'] as HostModeLabel[]) {
		test(`${mode}: players show Q2 and Q3 answer tiles on cmaclash.com`, async ({ browser }) => {
			const gameMode = mode === 'Standard' ? 'kahoot' : 'normal';
			const slug = mode === 'Standard' ? 'std' : 'dev';
			const lobby = await hostLiveGame(gameMode);
			const pin = lobby.pin;
			const suffix = String(Date.now()).slice(-6);

			const p1Ctx = await browser.newContext();
			const p2Ctx = await browser.newContext();
			const p3Ctx = await browser.newContext();
			const p1 = await joinPlayer(p1Ctx, pin, `P1${suffix}`);
			const p2 = await joinPlayer(p2Ctx, pin, `P2${suffix}`);
			const p3 = await joinPlayer(p3Ctx, pin, `P3${suffix}`);

			await expect(p1.getByText(/get ready/i)).toBeVisible();
			await expect(p2.getByText(/get ready/i)).toBeVisible();
			await expect(p3.getByText(/get ready/i)).toBeVisible();

			lobby.startGame();
			await new Promise((r) => setTimeout(r, gameMode === 'normal' ? 12_000 : 2500));

			await expectPlayerOnAnswerTiles(p1, 'P1 Q1');
			await expectPlayerOnAnswerTiles(p2, 'P2 Q1');
			await expectPlayerOnAnswerTiles(p3, 'P3 Q1');

			await answerFirstTile(p1);
			await new Promise((r) => setTimeout(r, 300));
			await answerFirstTile(p2);
			await new Promise((r) => setTimeout(r, 300));
			await answerFirstTile(p3);

			await expect(p1.getByText(/Correct|Incorrect|Time's up/i)).toBeVisible({
				timeout: gameMode === 'normal' ? 120_000 : 60_000
			});
			const q1RevealDelta = await expectRevealStats(
				p1,
				gameMode === 'normal' ? 90_000 : 45_000
			);

			await p1.screenshot({
				path: path.join(ARTIFACT_DIR, `${slug}-pin${pin}-player-reveal-q1.png`),
				fullPage: true
			});

			const rankingsStart = Date.now();
			await expect(p1.getByTestId('live-scoreboard')).toBeVisible({ timeout: 12_000 });
			const q1BoardTotal = Number(
				(await p1.getByTestId('scoreboard-row').first().locator('td').last().innerText()).replace(
					/[^\d]/g,
					''
				)
			);
			expect(q1BoardTotal).toBe(q1RevealDelta);
			expect(await p1.getByTestId('scoreboard-row').count()).toBeLessThanOrEqual(5);
			await p1.screenshot({
				path: path.join(ARTIFACT_DIR, `${slug}-pin${pin}-player-scoreboard-q1.png`),
				fullPage: true
			});

			await new Promise((r) => setTimeout(r, 14_000));
			expect(Date.now() - rankingsStart).toBeGreaterThanOrEqual(8000);

			await expectPlayerAdvancedToNextQuestion(p1, 'P1 Q2');
			await expectPlayerAdvancedToNextQuestion(p2, 'P2 Q2');

			await answerFirstTile(p1);
			await answerFirstTile(p2);
			await answerFirstTile(p3);

			await expect(p1.getByTestId('reveal-place-line')).toBeVisible({ timeout: 45_000 });
			const q2RevealDelta = await waitForRevealPoints(p1);
			await expect(p1.getByTestId('live-scoreboard')).toBeVisible({ timeout: 10_000 });
			const q2BoardTotal = Number(
				(await p1.getByTestId('scoreboard-row').first().locator('td').last().innerText()).replace(
					/[^\d]/g,
					''
				)
			);
			expect(q2BoardTotal).toBe(q1BoardTotal + q2RevealDelta);

			await new Promise((r) => setTimeout(r, 14_000));

			await expectPlayerAdvancedToNextQuestion(p1, 'P1 Q3');
			await expectPlayerAdvancedToNextQuestion(p2, 'P2 Q3');

			lobby.close();
			await p1Ctx.close();
			await p2Ctx.close();
			await p3Ctx.close();
		});
	}
});
