// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { BrowserContext } from '@playwright/test';
import { installLiveApiProxy } from './liveApiProxy';

export const PRODUCTION_BASE_URL =
	process.env.PLAYWRIGHT_TEST_BASE_URL ?? 'https://cmaclash.com';

export function isLocalPreviewBase(): boolean {
	try {
		const host = new URL(PRODUCTION_BASE_URL).hostname;
		return host === '127.0.0.1' || host === 'localhost';
	} catch {
		return false;
	}
}

export async function maybeInstallLiveApiProxy(context: BrowserContext): Promise<void> {
	if (isLocalPreviewBase()) {
		await installLiveApiProxy(context);
	}
}
