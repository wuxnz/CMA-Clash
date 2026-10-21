// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
	testDir: 'e2e',
	fullyParallel: false,
	timeout: 240_000,
	use: {
		...devices['Desktop Chrome'],
		baseURL: process.env.PLAYWRIGHT_TEST_BASE_URL ?? 'https://cmaclash.com'
	}
});
