// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { expect, test } from '@playwright/test';

const quizId = '11111111-1111-4111-8111-111111111111';

const quiz = {
	title: 'Infection Control: Set 1',
	questions: [
		{
			time: '30',
			type: 'ABCD',
			question:
				'Which hand hygiene method is required after caring for a patient with C. difficile?',
			answers: [
				{ right: false, answer: 'Alcohol-based hand rub only' },
				{ right: true, answer: 'Soap and water' },
				{ right: false, answer: 'No hand hygiene if gloves were worn' },
				{ right: false, answer: 'Glove sanitizer before bed contact' }
			],
			explanation: 'Soap and water is required because soap removes the C. difficile spores.'
		}
	]
};

test.describe('homepage hero sample question', () => {
	test.beforeEach(async ({ context }) => {
		await context.route('**/api/v1/clash/quizzes?*', async (route) => {
			await route.fulfill({
				status: 200,
				contentType: 'application/json',
				body: JSON.stringify([
					{
						id: quizId,
						title: quiz.title,
						description: null,
						difficulty: 'intermediate',
						topic_id: null,
						certification_id: null,
						question_count: 1,
						plays: 0
					}
				])
			});
		});
		await context.route(`**/api/v1/quiz/get/public/${quizId}`, async (route) => {
			await route.fulfill({
				status: 200,
				contentType: 'application/json',
				body: JSON.stringify(quiz)
			});
		});
	});

	test('replaces the loading placeholder with a fetched question', async ({ page }) => {
		await page.goto('/');

		const card = page.getByTestId('home-preview-question');
		await expect(card).toBeVisible();

		const question = card.locator('p.font-display').first();
		await expect(question).not.toContainText('Loading a sample question', { timeout: 20_000 });
		await expect(question).toContainText('Which hand hygiene method is required');

		await expect(card.locator('p.eyebrow').first()).toContainText('Infection Control');
	});

	test('answering reveals the explanation and the next question advances', async ({ page }) => {
		await page.goto('/');

		const card = page.getByTestId('home-preview-question');
		const question = card.locator('p.font-display').first();
		await expect(question).not.toContainText('Loading a sample question', { timeout: 20_000 });

		const counter = card.locator('span.tabular-nums').first();
		await expect(counter).toHaveText(/^1\s*\/\s*12$/);

		await card.getByRole('button', { name: /Soap and water/ }).click();
		await expect(card.getByText('Correct.')).toBeVisible();
		await expect(card.getByRole('button', { name: 'Next question' })).toBeVisible();

		await card.getByRole('button', { name: 'Next question' }).click();
		await expect(counter).toHaveText(/^2\s*\/\s*12$/);
		await expect(question).not.toContainText('Loading a sample question', { timeout: 20_000 });
	});
});
