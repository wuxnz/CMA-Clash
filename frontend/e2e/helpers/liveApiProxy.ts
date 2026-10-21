// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { BrowserContext } from '@playwright/test';

const API_BASE = process.env.PLAYWRIGHT_API_BASE ?? 'https://cmaclash-api.onrender.com';

/** Proxy browser `/api/*` calls to the live CMA Clash API during e2e. */
export async function installLiveApiProxy(context: BrowserContext): Promise<void> {
	await context.route('**/api/**', async (route) => {
		const reqUrl = new URL(route.request().url());
		if (!reqUrl.pathname.startsWith('/api/')) {
			await route.continue();
			return;
		}
		const target = `${API_BASE}${reqUrl.pathname}${reqUrl.search}`;
		const response = await route.fetch({ url: target });
		await route.fulfill({ response });
	});
}
