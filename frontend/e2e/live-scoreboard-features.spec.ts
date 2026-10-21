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
	process.env.PLAYWRIGHT_ARTIFACT_DIR ?? '/opt/cursor/artifacts/live-ui';
const SCOREBOARD_HOLD_MS = 9000;
const REVEAL_HOLD_MS = 4000;

test.describe('live scoreboard and reveal stats', () => {
	test.describe.configure({ timeout: 240_000 });
	test.use({ viewport: { width: 390, height: 844 } });

	test('Standard: 3 players see place, bonus copy and scoreboard hold', async ({ browser }) => {
		const hostContext = await browser.newContext({ viewport: { width: 1280, height: 800 } });
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();
		const pin = await startFromNavbarHost(hostPage, 'Standard');

		const p1 = await joinPlayer(await browser.newContext(), pin, 'SB_A');
		const p2 = await joinPlayer(await browser.newContext(), pin, 'SB_B');
		const p3 = await joinPlayer(await browser.newContext(), pin, 'SB_C');

		await hostPage.getByRole('button', { name: /^Start game$/i }).click({ timeout: 90_000 });

		await answerFirstTile(p1);
		await new Promise((r) => setTimeout(r, 400));
		await answerFirstTile(p2);
		await new Promise((r) => setTimeout(r, 400));
		await answerFirstTile(p3);

		await expect(p1.getByTestId('reveal-place-line')).toBeVisible({ timeout: 30_000 });
		await expect(p1.getByText(/place$/i)).toBeVisible();
		await expect(p1.getByTestId('reveal-speed-rank')).toBeVisible();
		await expect(p1.getByText(/speed bonus/i)).toBeVisible();

		await p1.screenshot({
			path: path.join(ARTIFACT_DIR, 'player-reveal-stats.png'),
			fullPage: true
		});

		const rankingsStart = Date.now();
		await expect(p1.getByTestId('live-scoreboard')).toBeVisible({ timeout: REVEAL_HOLD_MS + 2000 });
		await expect(hostPage.getByTestId('live-scoreboard')).toBeVisible({ timeout: REVEAL_HOLD_MS + 2000 });

		const rowCountHost = await hostPage.getByTestId('scoreboard-row').count();
		expect(rowCountHost).toBeLessThanOrEqual(5);
		expect(rowCountHost).toBeGreaterThanOrEqual(3);

		await hostPage.screenshot({
			path: path.join(ARTIFACT_DIR, 'host-scoreboard.png'),
			fullPage: true
		});

		await expect(p1.getByTestId('answer-tiles')).toBeVisible({ timeout: SCOREBOARD_HOLD_MS + 8000 });
		const rankingsMs = Date.now() - rankingsStart;
		expect(rankingsMs).toBeGreaterThanOrEqual(SCOREBOARD_HOLD_MS - 1500);

		await hostContext.close();
		await p1.context().close();
		await p2.context().close();
		await p3.context().close();
	});
});
