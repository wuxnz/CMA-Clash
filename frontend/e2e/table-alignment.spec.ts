// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, test, type Locator, type Page } from '@playwright/test';
import { installLiveApiProxy } from './helpers/liveApiProxy';

const LEFT_COLS = ['title', 'cert', 'difficulty'] as const;

async function waitForBrowseTable(page: Page) {
	await page.locator('[data-browse-list] [data-quiz-col="cert"]').first().waitFor({
		state: 'visible',
		timeout: 45_000
	});
}

async function assertDesktopColumnAlignment(table: Locator) {
	const list = table.locator('[data-browse-list]');
	for (const col of LEFT_COLS) {
		const header = table.locator(`[data-quiz-header] [data-quiz-col="${col}"]`);
		const cell = list.locator(`[data-quiz-col="${col}"]`).first();
		const hBox = await header.boundingBox();
		const cBox = await cell.boundingBox();
		expect(hBox, `${col} header box`).not.toBeNull();
		expect(cBox, `${col} cell box`).not.toBeNull();
		expect(Math.abs(hBox!.x - cBox!.x), `${col} left edge`).toBeLessThanOrEqual(1);
	}

	const hQs = await table.locator('[data-quiz-header] [data-quiz-col="qs"]').boundingBox();
	const cQs = await list.locator('[data-quiz-col="qs"]').first().boundingBox();
	expect(hQs, 'qs header').not.toBeNull();
	expect(cQs, 'qs cell').not.toBeNull();
	const headerRight = hQs!.x + hQs!.width;
	const cellRight = cQs!.x + cQs!.width;
	expect(Math.abs(headerRight - cellRight), 'qs right edge').toBeLessThanOrEqual(1);
}

test.beforeEach(async ({ context }) => {
	await installLiveApiProxy(context);
});

for (const path of ['/explore', '/search']) {
	test.describe(path, () => {
		test('header and row columns share grid tracks at 1280px', async ({ page }) => {
			await page.setViewportSize({ width: 1280, height: 900 });
			await page.goto(path);
			await waitForBrowseTable(page);

			const tables = page.locator('[data-quiz-table]');
			const tableCount = await tables.count();
			expect(tableCount).toBeGreaterThan(0);
			for (let i = 0; i < tableCount; i++) {
				await assertDesktopColumnAlignment(tables.nth(i));
			}
		});

		test('desktop column headers are hidden at 390px', async ({ page }) => {
			await page.setViewportSize({ width: 390, height: 844 });
			await page.goto(path);
			await page.locator('[data-browse-list] [data-quiz-card]').first().waitFor({
				timeout: 45_000
			});

			const headers = page.locator('[data-quiz-header]');
			const count = await headers.count();
			expect(count).toBeGreaterThan(0);
			for (let i = 0; i < count; i++) {
				await expect(headers.nth(i)).toBeHidden();
			}
			await expect(page.locator('[data-browse-list] [data-quiz-col="cert"]').first()).toBeHidden();
		});
	});
}
