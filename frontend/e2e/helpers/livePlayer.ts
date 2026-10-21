// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, type Page } from '@playwright/test';

export async function expectPlayerOnAnswerTiles(page: Page, label: string) {
	const root = page.getByTestId('answer-tiles');
	await expect(root, label).toBeVisible({ timeout: 60_000 });
	await expect(
		root.locator('button:not([disabled])'),
		`${label}: interactive tiles`
	).not.toHaveCount(0, { timeout: 60_000 });
}

/** After both players answer, wait through reveal then the next question's enabled tiles. */
export async function expectPlayerAdvancedToNextQuestion(page: Page, label: string) {
	const root = page.getByTestId('answer-tiles');
	await expect(root, `${label}: leave prior question`).toBeHidden({ timeout: 20_000 });
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
