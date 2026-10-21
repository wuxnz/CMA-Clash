// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type BrowserContext, type Page } from '@playwright/test';
import { installLiveApiProxy } from './helpers/liveApiProxy';
import {
	answerFirstTile,
	expectPlayerAdvancedToNextQuestion,
	expectPlayerOnAnswerTiles
} from './helpers/livePlayer';
import fs from 'node:fs';
import path from 'node:path';

const artifactDir = '/opt/cursor/artifacts/screenshots';
const baseURL = process.env.PLAYWRIGHT_TEST_BASE_URL ?? 'https://cmaclash.com';

const STALE_LIVE_PIN = '111111';

function baseHostname(): string {
	return new URL(baseURL).hostname;
}

function isLocalPreview(): boolean {
	const host = baseHostname();
	return host === '127.0.0.1' || host === 'localhost';
}

async function maybeInstallApiProxy(context: BrowserContext): Promise<void> {
	if (isLocalPreview()) {
		await installLiveApiProxy(context);
	}
}

async function seedStaleLiveGameCookie(context: BrowserContext) {
	await context.addCookies([
		{
			name: 'joined_game',
			value: JSON.stringify({
				sid: 'stale-sid',
				username: 'OldLiveHost',
				game_pin: STALE_LIVE_PIN
			}),
			domain: baseHostname(),
			path: '/'
		}
	]);
}

async function hostBattle(page: Page): Promise<{ code: string; quizTitle: string }> {
	await page.goto('/battle');
	const quizTitle = (await page.locator('li .font-medium').first().textContent())?.trim() ?? '';
	await page.locator('button.action-button', { hasText: 'Host' }).first().click({ timeout: 60_000 });
	await expect(page).toHaveURL(/\/battle\/\d+/, { timeout: 30_000 });
	const segments = new URL(page.url()).pathname.split('/');
	return { code: segments[segments.length - 1]!, quizTitle };
}

async function joinBattleLobby(page: Page, code: string, nickname: string): Promise<void> {
	await page.goto(`/battle/${code}`);
	await page.getByPlaceholder(/nickname/i).fill(nickname);
	await page.getByRole('button', { name: /join battle/i }).click();
	await expect(page.getByTestId('battle-lobby-players').getByText(nickname)).toBeVisible({
		timeout: 30_000
	});
}

async function waitForBattleQuestions(page: Page, label: string): Promise<void> {
	await page.waitForURL(/\/play\?pin=/, { timeout: 120_000 });
	const connecting = page.getByText(/connecting to game server/i);
	if (await connecting.isVisible().catch(() => false)) {
		await expect(connecting).toBeHidden({ timeout: 120_000 });
	}
	const submit = page.getByRole('button', { name: /submit/i });
	for (let i = 0; i < 45; i++) {
		if (await page.getByTestId('answer-tiles').isVisible().catch(() => false)) break;
		if (await submit.isEnabled().catch(() => false)) {
			await submit.click();
		}
		await page.waitForTimeout(1500);
	}
	await expectPlayerOnAnswerTiles(page, label);
}

async function playBattleUntilFinalPodium(hostPage: Page, guestPage: Page): Promise<void> {
	const podium = (page: Page) => page.getByTestId('host-final-podium');
	for (let round = 0; round < 25; round++) {
		if (await podium(hostPage).isVisible().catch(() => false)) break;
		if (!(await hostPage.getByTestId('answer-tiles').isVisible().catch(() => false))) {
			await hostPage.waitForTimeout(800);
			continue;
		}
		await answerFirstTile(hostPage);
		await answerFirstTile(guestPage);
		await hostPage.waitForTimeout(400);
	}
	await expect(podium(hostPage), 'host final podium').toBeVisible({ timeout: 120_000 });
	await expect(podium(guestPage), 'guest final podium').toBeVisible({ timeout: 120_000 });
}

async function expectBattleFinalScores(
	page: Page,
	names: string[],
	label: string
): Promise<void> {
	const podium = page.getByTestId('host-final-podium');
	for (const name of names) {
		await expect(podium.getByText(name, { exact: false }), `${label}: ${name}`).toBeVisible({
			timeout: 30_000
		});
	}
	const scoreTexts = await podium.locator('.tabular-nums').allTextContents();
	const numeric = scoreTexts
		.map((t) => parseFloat(t.replace(/,/g, '')))
		.filter((n) => Number.isFinite(n) && n > 0);
	expect(numeric.length, `${label}: nonzero scores on podium`).toBeGreaterThanOrEqual(2);
}

async function expectBattleQuestionText(page: Page, label: string): Promise<string> {
	const q = page.getByTestId('battle-question-text');
	await expect(q, label).toBeVisible({ timeout: 60_000 });
	const text = (await q.textContent())?.replace(/\s+/g, ' ').trim() ?? '';
	expect(text.length, `${label} question text`).toBeGreaterThan(8);
	return text;
}

test.describe('battle after live game in same browser', () => {
	test.beforeAll(() => {
		fs.mkdirSync(artifactDir, { recursive: true });
	});

	test('no stale live pin; host starts battle; both see Q1 and Q2', async ({ browser }) => {
		const hostContext = await browser.newContext();
		await maybeInstallApiProxy(hostContext);
		await seedStaleLiveGameCookie(hostContext);
		const hostPage = await hostContext.newPage();
		await hostPage.goto(`/play?pin=${STALE_LIVE_PIN}`);
		await expect(hostPage.getByText(STALE_LIVE_PIN)).toBeVisible({ timeout: 30_000 });

		const { code, quizTitle: battleQuizTitle } = await hostBattle(hostPage);
		expect(battleQuizTitle.length).toBeGreaterThan(0);
		await joinBattleLobby(hostPage, code, 'HostAlpha');

		const guestContext = await browser.newContext();
		await maybeInstallApiProxy(guestContext);
		const guestPage = await guestContext.newPage();
		await joinBattleLobby(guestPage, code, 'GuestBeta');

		await hostPage.getByRole('button', { name: /start battle/i }).click();

		await waitForBattleQuestions(hostPage, 'host Q1');
		await waitForBattleQuestions(guestPage, 'guest Q1');

		const hostUrlPin = new URL(hostPage.url()).searchParams.get('pin');
		const guestUrlPin = new URL(guestPage.url()).searchParams.get('pin');
		expect(hostUrlPin).toBeTruthy();
		expect(hostUrlPin).toBe(guestUrlPin);
		await expect(hostPage.getByText(STALE_LIVE_PIN)).toHaveCount(0);

		const hostQ1 = await expectBattleQuestionText(hostPage, 'host Q1 text');
		const guestQ1 = await expectBattleQuestionText(guestPage, 'guest Q1 text');
		expect(hostQ1).toBe(guestQ1);

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q1-host.png'),
			fullPage: true
		});
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q1-guest.png'),
			fullPage: true
		});
		await hostPage.setViewportSize({ width: 1280, height: 800 });
		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-question-desktop.png'),
			fullPage: true
		});
		await guestPage.setViewportSize({ width: 390, height: 844 });
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-question-mobile.png'),
			fullPage: true
		});

		await answerFirstTile(hostPage);
		await answerFirstTile(guestPage);

		await expectPlayerAdvancedToNextQuestion(hostPage, 'host Q2');
		await expectPlayerAdvancedToNextQuestion(guestPage, 'guest Q2');

		const hostQ2 = await expectBattleQuestionText(hostPage, 'host Q2 text');
		const guestQ2 = await expectBattleQuestionText(guestPage, 'guest Q2 text');
		expect(hostQ2).toBe(guestQ2);
		expect(hostQ2).not.toBe(hostQ1);

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q2-host.png'),
			fullPage: true
		});
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-after-live-q2-guest.png'),
			fullPage: true
		});

		await answerFirstTile(hostPage);
		await answerFirstTile(guestPage);

		await playBattleUntilFinalPodium(hostPage, guestPage);
		await expectBattleFinalScores(hostPage, ['HostAlpha', 'GuestBeta'], 'host final');
		await expectBattleFinalScores(guestPage, ['HostAlpha', 'You'], 'guest final');
		await expect(hostPage.getByTestId('battle-final-outcome')).toBeVisible();
		await expect(guestPage.getByTestId('battle-final-outcome')).toBeVisible();

		await hostPage.screenshot({
			path: path.join(artifactDir, 'battle-final-host.png'),
			fullPage: true
		});
		await guestPage.screenshot({
			path: path.join(artifactDir, 'battle-final-guest.png'),
			fullPage: true
		});

		await hostContext.close();
		await guestContext.close();
	});
});
