// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { defineConfig, devices } from '@playwright/test';

const port = 3000;
const baseURL = `http://127.0.0.1:${port}`;
const apiBase = process.env.PLAYWRIGHT_API_BASE ?? 'https://cmaclash-api.onrender.com';

export default defineConfig({
	testDir: 'e2e',
	fullyParallel: true,
	forbidOnly: !!process.env.CI,
	retries: process.env.CI ? 1 : 0,
	timeout: 60_000,
	use: {
		...devices['Desktop Chrome'],
		baseURL
	},
	webServer: {
		command: `node scripts/playwright-webserver.mjs ${apiBase} ${port}`,
		url: baseURL,
		reuseExistingServer: !process.env.CI,
		timeout: 120_000
	}
});
