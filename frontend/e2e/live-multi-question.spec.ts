// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect } from '@playwright/test';
import { installLiveApiProxy } from './helpers/liveApiProxy';
import { joinPlayer } from './helpers/joinPlayer';
import { startFromNavbarHost } from './helpers/liveHost';
import {
	answerFirstTile,
	expectPlayerAdvancedToNextQuestion,
	expectPlayerOnAnswerTiles
} from './helpers/livePlayer';

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

			await hostPage.getByRole('button', { name: /^Start game$/i }).click({ timeout: 90_000 });
			await expectPlayerOnAnswerTiles(p1, 'P1 Q1');
			await expectPlayerOnAnswerTiles(p2, 'P2 Q1');

			for (let round = 0; round < 3; round++) {
				await answerFirstTile(p1);
				await answerFirstTile(p2);
				if (round < 2) {
					await expectPlayerAdvancedToNextQuestion(p1, `P1 Q${round + 2}`);
					await expectPlayerAdvancedToNextQuestion(p2, `P2 Q${round + 2}`);
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

		await hostPage.getByRole('button', { name: /^Start game$/i }).click({ timeout: 90_000 });
		await expectPlayerOnAnswerTiles(p1, 'P1 Q1');
		await answerFirstTile(p1);
		// p2 does not answer — server should close Q0 and auto-advance after reveal
		await expectPlayerAdvancedToNextQuestion(p1, 'P1 Q2');
		await expectPlayerAdvancedToNextQuestion(p2, 'P2 Q2');

		await hostContext.close();
		await p1.context().close();
		await p2.context().close();
	});
});
