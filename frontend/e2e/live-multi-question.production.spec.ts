// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type BrowserContext } from '@playwright/test';
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

test.describe('production live multi-question UI', () => {
	test.describe.configure({ timeout: 300_000, mode: 'serial' });

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

			lobby.startGame();
			await new Promise((r) => setTimeout(r, gameMode === 'normal' ? 5500 : 2000));

			await expectPlayerOnAnswerTiles(p1, 'P1 Q1');
			await expectPlayerOnAnswerTiles(p2, 'P2 Q1');
			await expectPlayerOnAnswerTiles(p3, 'P3 Q1');

			// Q1 — staggered answers for speed ranks
			await answerFirstTile(p1);
			await new Promise((r) => setTimeout(r, 300));
			await answerFirstTile(p2);
			await new Promise((r) => setTimeout(r, 300));
			await answerFirstTile(p3);

			await expect(p1.getByTestId('reveal-place-line')).toBeVisible({ timeout: 45_000 });
			await expect(p1.getByTestId('reveal-speed-rank')).toBeVisible();
			await p1.screenshot({
				path: path.join(ARTIFACT_DIR, `${slug}-player-reveal-q1.png`),
				fullPage: true
			});

			const rankingsStart = Date.now();
			await expect(p1.getByTestId('live-scoreboard')).toBeVisible({ timeout: 10_000 });
			expect(await p1.getByTestId('scoreboard-row').count()).toBeLessThanOrEqual(5);
			await new Promise((r) => setTimeout(r, 14_000));
			expect(Date.now() - rankingsStart).toBeGreaterThanOrEqual(8000);

			// Q2 — after server reveal + auto-advance
			await expectPlayerAdvancedToNextQuestion(p1, 'P1 Q2');
			await expectPlayerAdvancedToNextQuestion(p2, 'P2 Q2');

			await p1.screenshot({
				path: path.join(ARTIFACT_DIR, `${slug}-player1-q2.png`),
				fullPage: true
			});
			await p2.screenshot({
				path: path.join(ARTIFACT_DIR, `${slug}-player2-q2.png`),
				fullPage: true
			});

			await answerFirstTile(p1);
			await answerFirstTile(p2);
			await answerFirstTile(p3);
			await new Promise((r) => setTimeout(r, 14_000));

			// Q3
			await expectPlayerAdvancedToNextQuestion(p1, 'P1 Q3');
			await expectPlayerAdvancedToNextQuestion(p2, 'P2 Q3');

			lobby.close();
			await p1Ctx.close();
			await p2Ctx.close();
			await p3Ctx.close();
		});
	}
});
