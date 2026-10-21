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
			const p1 = await joinPlayer(p1Ctx, pin, `P1${suffix}`);
			const p2 = await joinPlayer(p2Ctx, pin, `P2${suffix}`);

			lobby.startGame();
			await new Promise((r) => setTimeout(r, 1500));

			await expectPlayerOnAnswerTiles(p1, 'P1 Q1');
			await expectPlayerOnAnswerTiles(p2, 'P2 Q1');

			// Q1 — answer early
			await answerFirstTile(p1);
			await answerFirstTile(p2);

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

			// Q3
			await expectPlayerAdvancedToNextQuestion(p1, 'P1 Q3');
			await expectPlayerAdvancedToNextQuestion(p2, 'P2 Q3');

			lobby.close();
			await p1Ctx.close();
			await p2Ctx.close();
		});
	}
});
