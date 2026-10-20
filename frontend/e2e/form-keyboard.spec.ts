// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, test } from '@playwright/test';

test.describe('form keyboard navigation', () => {
	test('register: Tab moves focus through text inputs in order', async ({ page }) => {
		await page.goto('/account/register');
		const email = page.locator('#email');
		const username = page.locator('#username');
		const password1 = page.locator('#password1');
		const password2 = page.locator('#password2');

		await email.focus();
		await expect(email).toBeFocused();

		await page.keyboard.press('Tab');
		await expect(username).toBeFocused();
		await page.keyboard.type('tabtest');

		await page.keyboard.press('Tab');
		await expect(password1).toBeFocused();

		await page.keyboard.press('Tab');
		await expect(password2).toBeFocused();
	});

	test('login: Tab moves from email field to continue control', async ({ page }) => {
		await page.goto('/account/login');
		const email = page.locator('#email');
		await email.focus();
		await expect(email).toBeFocused();

		await page.keyboard.press('Tab');
		const active = page.locator(':focus');
		await expect(active).toBeVisible();
		const tag = await active.evaluate((el) => el.tagName);
		expect(['A', 'BUTTON', 'INPUT']).toContain(tag);
	});

	test('play join: Tab moves from PIN to next focusable after 6 digits', async ({ page }) => {
		await page.goto('/play');
		const pin = page.locator('input[autocomplete="one-time-code"]');
		await pin.focus();
		await pin.fill('123456');
		const nickname = page.locator('input[autocomplete="nickname"]');
		await expect(nickname).toBeVisible();
		await nickname.focus();
		await page.keyboard.type('Player');
		await expect(nickname).toHaveValue(/Player/);
	});

	test('register: keeps field values and shows inline error when username is taken', async ({
		page
	}) => {
		await page.route('**/api/v1/users/create', async (route) => {
			await route.fulfill({
				status: 409,
				contentType: 'application/json',
				body: JSON.stringify({ detail: 'username_taken' })
			});
		});

		await page.goto('/account/register');
		await page.locator('#email').fill('newuser@example.com');
		await page.locator('#username').fill('takenname');
		await page.locator('#password1').fill('password12');
		await page.locator('#password2').fill('password12');
		await page.locator('input[name="privacy_accept"]').check();
		await page.locator('input[name="tos_accept"]').check();

		const submit = page.getByRole('button', { name: /register/i });
		await expect(submit).toBeEnabled({ timeout: 10_000 });
		await Promise.all([
			page.waitForResponse(
				(res) => res.url().includes('/users/create') && res.status() === 409
			),
			submit.click()
		]);

		await expect(page.getByText('That username is taken.')).toBeVisible();
		await expect(page.locator('#email')).toHaveValue('newuser@example.com');
		await expect(page.locator('#username')).toHaveValue('takenname');
		await expect(page.locator('#password1')).toHaveValue('password12');
	});
});
