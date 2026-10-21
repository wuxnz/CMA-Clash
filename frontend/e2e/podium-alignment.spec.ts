// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { test, expect } from '@playwright/test';

type Box = { x: number; y: number; width: number; height: number };

function bottomY(box: Box): number {
	return box.y + box.height;
}

async function assertPedestalGeometry(page: import('@playwright/test').Page) {
	await page.waitForSelector('[data-testid="podium-pedestal-1"]', { timeout: 30_000 });
	const places = ['2', '1', '3'] as const;
	const boxes: Box[] = [];
	for (const place of places) {
		const box = await page.getByTestId(`podium-pedestal-${place}`).boundingBox();
		expect(box, `pedestal ${place} should be visible`).not.toBeNull();
		boxes.push(box!);
	}

	const widths = boxes.map((b) => b.width);
	const bottoms = boxes.map(bottomY);
	const maxWidthDelta = Math.max(...widths) - Math.min(...widths);
	const maxBottomDelta = Math.max(...bottoms) - Math.min(...bottoms);

	expect(maxWidthDelta).toBeLessThanOrEqual(1);
	expect(maxBottomDelta).toBeLessThanOrEqual(1);

	// Stepped heights: 1st > 2nd > 3rd
	const byPlace = Object.fromEntries(places.map((p, i) => [p, boxes[i]])) as Record<
		'1' | '2' | '3',
		Box
	>;
	expect(byPlace['1'].height).toBeGreaterThan(byPlace['2'].height);
	expect(byPlace['2'].height).toBeGreaterThan(byPlace['3'].height);
}

test.describe('podium pedestal alignment', () => {
	test('desktop: equal widths and shared baseline', async ({ page }) => {
		await page.setViewportSize({ width: 1280, height: 800 });
		await page.goto('/demo/screens?phase=host-podium-desktop');
		await assertPedestalGeometry(page);
	});

	test('mobile host: equal widths and shared baseline', async ({ page }) => {
		await page.setViewportSize({ width: 390, height: 844 });
		await page.goto('/demo/screens?phase=host-podium');
		await assertPedestalGeometry(page);
	});
});
