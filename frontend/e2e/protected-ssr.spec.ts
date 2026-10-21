// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, test } from '@playwright/test';
import { installLiveApiProxy } from './helpers/liveApiProxy';

const API_BASE = process.env.PLAYWRIGHT_API_BASE ?? 'https://cmaclash-api.onrender.com';

async function loginAndGetCookies(
	email: string,
	password: string
): Promise<{ name: string; value: string; domain: string; path: string }[]> {
	const body = new URLSearchParams({ username: email, password });
	const res = await fetch(`${API_BASE}/api/v1/users/token/cookie`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
		body
	});
	if (!res.ok) {
		throw new Error(`Login failed: ${res.status}`);
	}
	const raw = res.headers.get('set-cookie');
	if (!raw) {
		throw new Error('Login response missing Set-Cookie');
	}
	const cookies: { name: string; value: string; domain: string; path: string }[] = [];
	for (const part of raw.split(/,(?=[^;]+?=)/)) {
		const [pair] = part.split(';');
		const eq = pair.indexOf('=');
		if (eq < 1) continue;
		const name = pair.slice(0, eq).trim();
		const value = pair.slice(eq + 1).trim();
		if (name === 'access_token' || name === 'rememberme_token' || name === 'expiry') {
			cookies.push({ name, value, domain: '127.0.0.1', path: '/' });
		}
	}
	return cookies;
}

test.describe('protected routes SSR', () => {
	test.beforeEach(async ({ context }) => {
		await installLiveApiProxy(context);
	});

	test('logged-out site-admin users redirects to login (not 500)', async ({ page }) => {
		const res = await page.goto('/site-admin/users');
		expect(res?.status()).toBeLessThan(500);
		await expect(page).toHaveURL(/\/account\/login/);
	});

	test('logged-out dashboard redirects to login (not 500)', async ({ page }) => {
		const res = await page.goto('/dashboard');
		expect(res?.status()).toBeLessThan(500);
		await expect(page).toHaveURL(/\/account\/login/);
	});

	test('logged-in admin: full document load for site-admin and dashboard', async ({ page, context }) => {
		const email = process.env.E2E_ADMIN_EMAIL;
		const password = process.env.E2E_ADMIN_PASSWORD;
		test.skip(!email || !password, 'Set E2E_ADMIN_EMAIL and E2E_ADMIN_PASSWORD for admin SSR test');

		const cookies = await loginAndGetCookies(email!, password!);
		await context.addCookies(cookies);

		const adminRes = await page.goto('/site-admin/users', { waitUntil: 'load' });
		expect(adminRes?.status()).toBe(200);
		await expect(page.getByRole('heading', { name: 'Site admin' })).toBeVisible();

		const dashRes = await page.goto('/dashboard', { waitUntil: 'load' });
		expect(dashRes?.status()).toBe(200);
		await expect(page.getByRole('heading', { name: /Hi,/ })).toBeVisible();
	});
});
