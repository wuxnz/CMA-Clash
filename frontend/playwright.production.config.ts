// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { defineConfig, devices } from '@playwright/test';

const baseURL = process.env.PLAYWRIGHT_BASE_URL ?? 'https://cmaclash.com';
const apiBase = process.env.PLAYWRIGHT_API_BASE ?? 'https://cmaclash-api.onrender.com';

export default defineConfig({
	testDir: 'e2e',
	timeout: 180_000,
	use: {
		...devices['Desktop Chrome'],
		baseURL
	},
	projects: [{ name: 'production-chrome', use: { ...devices['Desktop Chrome'] } }],
	metadata: { apiBase }
});
