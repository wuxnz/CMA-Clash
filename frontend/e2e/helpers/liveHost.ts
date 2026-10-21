// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, type Page } from '@playwright/test';

export type HostModeLabel = 'Standard' | 'On player devices';

export async function startFromNavbarHost(page: Page, mode: HostModeLabel): Promise<string> {
	await page.goto('/host', { waitUntil: 'domcontentloaded' });
	await page.getByRole('button', { name: /^Host$/ }).first().click({ timeout: 90_000 });
	await page.getByRole('radio', { name: mode }).click();
	await page.getByRole('button', { name: /^Start game$/i }).click();
	await page.waitForURL(/\/admin\?/, { timeout: 120_000 });
	const pin = new URL(page.url()).searchParams.get('pin');
	expect(pin).toMatch(/^\d{6}$/);
	return pin!;
}
