// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, type Page } from '@playwright/test';

export async function expectPlayerOnAnswerTiles(page: Page, label: string) {
	const root = page.getByTestId('answer-tiles');
	await expect(root, label).toBeVisible({ timeout: 120_000 });
	await expect(
		root.locator('button:not([disabled])'),
		`${label}: interactive tiles`
	).not.toHaveCount(0, { timeout: 60_000 });
}

/** After both players answer, wait until the next question's answer UI is ready. */
export async function expectPlayerAdvancedToNextQuestion(page: Page, label: string) {
	const root = page.getByTestId('answer-tiles');
	const firstTile = root.locator('button').first();
	const priorTile = ((await firstTile.textContent().catch(() => '')) ?? '').trim();

	await expect
		.poll(
			async () => {
				if (!(await root.isVisible().catch(() => false))) return false;
				const enabled = await root.locator('button:not([disabled])').count();
				if (enabled === 0) return false;
				const now = ((await firstTile.textContent().catch(() => '')) ?? '').trim();
				return Boolean(priorTile && now && now !== priorTile);
			},
			{ message: `${label}: next question answer tiles`, timeout: 90_000 }
		)
		.toBe(true);

	await expect(root, `${label}: next question visible`).toBeVisible({ timeout: 60_000 });
	await expect(
		root.locator('button:not([disabled])'),
		`${label}: interactive tiles`
	).not.toHaveCount(0, { timeout: 60_000 });
}

/** Tap the first enabled answer tile (skips if this client already answered). */
export async function answerFirstTile(page: Page) {
	const root = page.getByTestId('answer-tiles');
	await expect(root).toBeVisible({ timeout: 90_000 });
	const tile = root.locator('button:not([disabled])').first();
	if ((await tile.count()) === 0) {
		return;
	}
	await tile.click();
}
