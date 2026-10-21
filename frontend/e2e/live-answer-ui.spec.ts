// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const artifactDir = '/opt/cursor/artifacts/screenshots';

test.describe('live answer UI', () => {
	test.use({ viewport: { width: 390, height: 844 } });

	test.beforeAll(() => {
		fs.mkdirSync(artifactDir, { recursive: true });
	});

	test('player answer screen mobile', async ({ page }) => {
		await page.goto('/e2e/arena-preview');
		await expect(page.getByTestId('player-answer-screen')).toBeVisible();
		await page.screenshot({
			path: path.join(artifactDir, 'player-answer-mobile.png'),
			fullPage: true
		});
	});

	test('host kahoot screen mobile', async ({ page }) => {
		await page.goto('/e2e/arena-preview');
		await page.getByRole('button', { name: 'Host kahoot' }).click();
		await expect(page.getByTestId('host-answer-screen')).toBeVisible();
		await page.screenshot({
			path: path.join(artifactDir, 'host-answer-mobile.png'),
			fullPage: true
		});
	});
});
