// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect, type Page } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const artifactDir = '/opt/cursor/artifacts/screenshots';
const viewport = { width: 390, height: 844 };

async function assertPrimaryInViewport(page: Page, label: string) {
	const btn = page.getByTestId('host-primary-action').first();
	await expect(btn, `${label}: primary host action visible`).toBeVisible({ timeout: 30_000 });
	const box = await btn.boundingBox();
	expect(box, `${label}: bounding box`).not.toBeNull();
	const vp = page.viewportSize()!;
	expect(box!.y + box!.height).toBeLessThanOrEqual(vp.height + 1);
	expect(box!.y).toBeGreaterThanOrEqual(-1);
}

async function shot(page: Page, name: string) {
	await page.screenshot({
		path: path.join(artifactDir, name),
		fullPage: false
	});
}

const hostPhases: { phase: string; file: string; label: string }[] = [
	{ phase: 'get-ready', file: 'host-phase-get-ready-390.png', label: 'get-ready' },
	{ phase: 'intro', file: 'host-phase-intro-390.png', label: 'intro' },
	{ phase: 'answer', file: 'host-phase-answer-390.png', label: 'answer' },
	{ phase: 'stop-time', file: 'host-phase-stop-time-390.png', label: 'stop-time' },
	{ phase: 'show-results', file: 'host-phase-show-results-390.png', label: 'show-results' },
	{ phase: 'reveal', file: 'host-phase-reveal-390.png', label: 'reveal' },
	{ phase: 'rankings', file: 'host-phase-rankings-390.png', label: 'rankings' },
	{ phase: 'on-devices', file: 'host-phase-on-devices-390.png', label: 'on-devices' }
];

test.describe('host mobile layout (390×844)', () => {
	test.use({ viewport });

	test.beforeAll(() => {
		fs.mkdirSync(artifactDir, { recursive: true });
	});

	for (const { phase, file, label } of hostPhases) {
		test(`demo host phase ${phase}: primary action in viewport`, async ({ page }) => {
			await page.goto(`/demo/host-phases?phase=${phase}`);
			await assertPrimaryInViewport(page, label);
			await shot(page, file);
		});
	}

	test('final podium: export actions in viewport', async ({ page }) => {
		await page.goto('/demo/screens?phase=host-podium');
		const footer = page.locator('[data-testid="host-final-podium"] button, [data-testid="host-final-podium"] a').first();
		await expect(footer).toBeVisible({ timeout: 30_000 });
		const box = await footer.boundingBox();
		expect(box).not.toBeNull();
		const vp = page.viewportSize()!;
		expect(box!.y + box!.height).toBeLessThanOrEqual(vp.height + 1);
		await shot(page, 'host-phase-podium-390.png');
	});
});
