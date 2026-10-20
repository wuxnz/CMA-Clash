import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after/dark';
const DEMO_EMAIL = process.env.DEMO_EMAIL ?? 'demo@cmaclash.local';
const DEMO_PASSWORD = process.env.DEMO_PASSWORD ?? 'CMA-Clash-Demo1!';

const VIEWPORTS = [
	{ name: '375', width: 375, height: 844, fullPage: true },
	{ name: '1280', width: 1280, height: 1024, fullPage: false }
];

async function login(page) {
	await page.goto(`${BASE}/account/login`, { waitUntil: 'networkidle' });
	await page.fill('#email', DEMO_EMAIL);
	await page.locator('#email').press('Enter');
	const pw = page.locator('#password');
	if (!(await pw.isVisible().catch(() => false))) {
		const btn = page.getByRole('button', { name: /password/i });
		if (await btn.isVisible().catch(() => false)) await btn.click();
	}
	await pw.waitFor({ state: 'visible', timeout: 15000 });
	await pw.fill(DEMO_PASSWORD);
	await pw.press('Enter');
	await page.waitForURL((url) => !url.pathname.includes('/account/login'), { timeout: 15000 });
}

async function shot(page, path, file, mustInclude, { fullPage = false } = {}) {
	await page.goto(`${BASE}${path}`, { waitUntil: 'networkidle' });
	await page.waitForTimeout(900);
	if (mustInclude) {
		if (mustInclude === 'Host') {
			await page
				.locator('[data-browse-list], body')
				.getByRole('button', { name: 'Host' })
				.first()
				.waitFor({ timeout: 12000 });
		} else {
			const heading = page.getByRole('heading', { name: mustInclude, exact: false });
			if ((await heading.count()) > 0) {
				await heading.first().waitFor({ timeout: 12000 });
			} else {
				await page.getByText(mustInclude, { exact: false }).first().waitFor({ timeout: 12000 });
			}
		}
	}
	const body = await page.locator('body').innerText();
	if (/Internal Error|UNKNOWN ERROR/i.test(body)) {
		throw new Error(`${file}: page error`);
	}
	if (fullPage) {
		await page.evaluate(() => window.scrollTo(0, 0));
	}
	await page.screenshot({ path: `${OUT}/${file}.png`, fullPage });
	console.log('ok', file);
}

const browser = await chromium.launch();
await mkdir(OUT, { recursive: true });

const publicPages = [
	['/account/login', 'login', 'Sign in'],
	['/account/register', 'register', 'Create account'],
	['/account/reset-password', 'reset-password', 'Reset password'],
	['/account/check-email', 'check-email', 'Check your inbox'],
	['/account/oauth-error', 'oauth-error', 'Could not sign in'],
	['/host', 'host', 'Host'],
	['/explore', 'explore', 'Host'],
	['/search', 'search', 'Host'],
	['/leaderboard', 'leaderboard', 'Leaderboard']
];

for (const vp of VIEWPORTS) {
	const context = await browser.newContext({
		viewport: { width: vp.width, height: vp.height },
		colorScheme: 'dark'
	});
	const page = await context.newPage();

	for (const [path, name, text] of publicPages) {
		await shot(page, path, `${name}-${vp.name}`, text, { fullPage: vp.fullPage });
	}

	await page.goto(`${BASE}/explore`, { waitUntil: 'networkidle' });
	await page.waitForTimeout(800);
	const viewHref = await page.locator('[data-quiz-card] a[href^="/view/"]').first().getAttribute('href');
	if (!viewHref) throw new Error('no view link on explore');
	await shot(page, viewHref, `view-${vp.name}`, 'Host', { fullPage: vp.fullPage });

	const userHref = await page.locator('a[href^="/user/"]').first().getAttribute('href');
	if (userHref) {
		await shot(page, userHref, `user-${vp.name}`, null, { fullPage: vp.fullPage });
	}

	await page.goto(`${BASE}/host`, { waitUntil: 'networkidle' });
	await page.locator('[data-browse-list]').getByRole('button', { name: 'Host' }).first().waitFor({
		timeout: 12000
	});
	await page.locator('[data-browse-list]').getByRole('button', { name: 'Host' }).first().click();
	await page.locator('[data-host-modal]').waitFor({ timeout: 8000 });
	await page.waitForTimeout(400);
	await page.screenshot({
		path: `${OUT}/host-modal-${vp.name}.png`,
		fullPage: false
	});
	console.log('ok', `host-modal-${vp.name}`);

	if (vp.name === '1280') {
		const start = page.getByRole('button', { name: 'Start game' });
		await start.click();
		await page.waitForTimeout(2500);
		if (!page.url().includes('/admin')) {
			throw new Error(`start-game did not reach admin lobby: ${page.url()}`);
		}
		console.log('ok start-game e2e', page.url());
	} else {
		await page.keyboard.press('Escape');
	}

	await context.close();
}

for (const vp of VIEWPORTS) {
	const context = await browser.newContext({
		viewport: { width: vp.width, height: vp.height },
		colorScheme: 'dark'
	});
	const page = await context.newPage();
	await login(page);
	await shot(page, '/account/settings', `settings-${vp.name}`, 'Settings', { fullPage: vp.fullPage });
	await shot(page, '/account/settings/security', `security-${vp.name}`, 'Security', {
		fullPage: vp.fullPage
	});
	await shot(page, '/account/controllers', `controllers-${vp.name}`, 'Quiz controllers', {
		fullPage: vp.fullPage
	});
	await shot(page, '/results', `results-${vp.name}`, 'Results', { fullPage: vp.fullPage });
	await shot(page, '/import', `import-${vp.name}`, 'Import', { fullPage: vp.fullPage });
	await context.close();
}

await browser.close();
console.log('done');
