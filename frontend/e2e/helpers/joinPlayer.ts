// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, type BrowserContext, type Page } from '@playwright/test';
import { installLiveApiProxy } from './liveApiProxy';

/** Join a live game on /play (production or preview). */
export async function joinPlayer(
	context: BrowserContext,
	pin: string,
	name: string,
	viewport = { width: 390, height: 844 }
): Promise<Page> {
	await installLiveApiProxy(context);
	if (process.env.CMA_PLAY_SOCKET_DEBUG === '1') {
		await context.addInitScript(() => {
			window.localStorage.setItem('cma_play_socket_debug', '1');
		});
	}
	await context.clearCookies();
	const page = await context.newPage();
	await page.setViewportSize(viewport);

	const pinDigits = pin.replace(/\D/g, '');
	await page.goto(`/play?pin=${encodeURIComponent(pinDigits)}`, { waitUntil: 'networkidle' });
	await page.waitForTimeout(3000);

	const lobby = page.getByText(/get ready/i);
	if (await lobby.isVisible().catch(() => false)) {
		return page;
	}

	const nickname = page.locator('input[autocomplete="nickname"]');
	await expect(nickname).toBeVisible({ timeout: 60_000 });
	await nickname.fill(name);

	const connecting = page.getByText(/connecting to game server/i);
	if (await connecting.isVisible().catch(() => false)) {
		await expect(connecting).toBeHidden({ timeout: 120_000 });
	}

	const submit = page.getByRole('button', { name: /^submit$/i });
	for (let attempt = 0; attempt < 8; attempt++) {
		await submit.click();
		if (await lobby.isVisible().catch(() => false)) {
			break;
		}
		const notConnected = page.getByRole('alert', { name: /not connected/i });
		if (await notConnected.isVisible().catch(() => false)) {
			await page.waitForTimeout(2000);
			continue;
		}
		await page.waitForTimeout(1000);
	}

	await expect(lobby).toBeVisible({ timeout: 90_000 });
	return page;
}
