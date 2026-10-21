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

async function expectRevealStats(page: import('@playwright/test').Page, revealTimeoutMs = 45_000) {
	await expect(page.getByTestId('reveal-place-line')).toBeVisible({ timeout: revealTimeoutMs });
	await expect(page.getByTestId('reveal-speed-rank')).toBeVisible();
	await expect(page.getByText(/speed bonus/i)).toBeVisible();
	const behind = page.getByTestId('reveal-behind-line');
	if (await behind.isVisible().catch(() => false)) {
		await expect(behind).toContainText(/behind|ahead of/i);
	}
	const bonusLine = await page.getByText(/\d+ base.*\d+ speed bonus/i).textContent();
	const match = bonusLine?.match(/(\d+) base.*?(\d+) speed bonus/);
	expect(match).toBeTruthy();
	const base = Number(match![1]);
	const bonus = Number(match![2]);
	const expectedTotal = base + bonus;
	await expect
		.poll(
			async () => {
				const nodes = page.locator('.text-gold.tabular-nums');
				const count = await nodes.count();
				for (let i = 0; i < count; i++) {
					const text = await nodes.nth(i).textContent();
					const n = Number((text ?? '').replace(/\D/g, ''));
					if (n === expectedTotal) return n;
				}
				return 0;
			},
			{ timeout: 5000 }
		)
		.toBe(expectedTotal);
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
			await expectRevealStats(p1, gameMode === 'normal' ? 90_000 : 45_000);
			await p1.screenshot({
				path: path.join(ARTIFACT_DIR, `${slug}-player-reveal-q1.png`),
				fullPage: true
			});

			const rankingsStart = Date.now();
			await expect(p1.getByTestId('live-scoreboard')).toBeVisible({ timeout: 12_000 });
			expect(await p1.getByTestId('scoreboard-row').count()).toBeLessThanOrEqual(5);
			await p1.screenshot({
				path: path.join(ARTIFACT_DIR, `${slug}-host-scoreboard.png`),
				fullPage: true
			});

			await new Promise((r) => setTimeout(r, 14_000));
			expect(Date.now() - rankingsStart).toBeGreaterThanOrEqual(8000);

			await expectPlayerAdvancedToNextQuestion(p1, 'P1 Q2');
			await expectPlayerAdvancedToNextQuestion(p2, 'P2 Q2');

			await answerFirstTile(p1);
			await answerFirstTile(p2);
			await answerFirstTile(p3);
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
