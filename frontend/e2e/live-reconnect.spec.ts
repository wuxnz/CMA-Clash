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

test.describe('live match reconnect', () => {
	test.describe.configure({ timeout: 240_000 });
	test.use({ viewport: { width: 390, height: 844 } });

	test('host and players return to the active question after refresh or rejoin', async ({ browser }) => {
		const hostContext = await browser.newContext();
		await installLiveApiProxy(hostContext);
		const hostPage = await hostContext.newPage();
		const pin = await test.step('create a match', () => startFromNavbarHost(hostPage, 'Standard'));

		const player1Context = await browser.newContext();
		const p1 = await joinPlayer(player1Context, pin, 'ReconnectP1');
		const p2 = await joinPlayer(await browser.newContext(), pin, 'ReconnectP2');

		await test.step('start and sync Q1', async () => {
			await hostPage.getByRole('button', { name: /^Start game$/i }).click({ timeout: 90_000 });
			await expect(p1.getByTestId('answer-tiles'), 'player 1 Q1').toBeVisible({ timeout: 15_000 });
			await expect(p2.getByTestId('answer-tiles'), 'player 2 Q1').toBeVisible({ timeout: 15_000 });
		});

		await test.step('restore host after refresh', async () => {
			await hostPage.reload();
			await expect(
			hostPage.getByText(
				/(Which answer is correct|What comes next|Final question\?|Test explanation|Second explanation|Third explanation)/
			)
			).toBeVisible({ timeout: 30_000 });
		});

		const p1Context = p1.context();
		const readJoinedPlayer = async () => {
			const value = (await p1Context.cookies()).find((c) => c.name === 'joined_game')?.value;
			return JSON.parse(decodeURIComponent(value ?? '%7B%7D'));
		};
		const joinedBefore = await readJoinedPlayer();
		expect(joinedBefore.username).toBe('ReconnectP1');
		await test.step('restore player after refresh', async () => {
			await p1.reload();
			await expect(p1.getByTestId('answer-tiles'), 'player 1 restored Q1').toBeVisible({ timeout: 15_000 });
		});
		const joinedAfterRefresh = await readJoinedPlayer();
		expect(joinedAfterRefresh.username).toBe('ReconnectP1');

		await test.step('rejoin by PIN and the same name', async () => {
			await p1.goto('/');
			await p1.goto(`/play?pin=${pin}`);
			await expect(p1.getByTestId('answer-tiles'), 'player 1 rejoined by code Q1').toBeVisible({ timeout: 15_000 });
		});
		const joinedAfterRejoin = await readJoinedPlayer();
		expect(joinedAfterRejoin.username).toBe('ReconnectP1');

		await Promise.all([answerFirstTile(p1), answerFirstTile(p2)]);
		await expect(p1.getByText(/(Test|Second|Third) explanation/)).toBeVisible({ timeout: 15_000 });
		await expect(p2.getByText(/(Test|Second|Third) explanation/)).toBeVisible({ timeout: 15_000 });
		await Promise.all([
			expectPlayerAdvancedToNextQuestion(p1, 'player 1 Q2'),
			expectPlayerAdvancedToNextQuestion(p2, 'player 2 Q2')
		]);

		await hostContext.close();
		await p1Context.close();
		await p2.context().close();
	});
});
