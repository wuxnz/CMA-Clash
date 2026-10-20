import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const API = process.env.API_BASE ?? 'http://127.0.0.1:8000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after/dark';
const DEMO_EMAIL = process.env.DEMO_EMAIL ?? 'demo@cmaclash.local';
const DEMO_PASSWORD = process.env.DEMO_PASSWORD ?? 'CMA-Clash-Demo1!';

const VIEWPORTS = [
	{ name: '375', width: 375, height: 844, fullPage: true },
	{ name: '768', width: 768, height: 1024, fullPage: false },
	{ name: '1280', width: 1280, height: 1024, fullPage: false }
];

async function login(page) {
	await page.goto(`${BASE}/account/login`, { waitUntil: 'networkidle' });
	await page.fill('#email', DEMO_EMAIL);
	await page.locator('form button[type="submit"]:not([disabled])').click();
	await page.waitForTimeout(1000);
	const pw = page.locator('#password');
	if (!(await pw.isVisible().catch(() => false))) {
		const btn = page.getByRole('button', { name: /password/i });
		if (await btn.isVisible().catch(() => false)) await btn.click();
	}
	await pw.waitFor({ state: 'visible', timeout: 15000 });
	await pw.fill(DEMO_PASSWORD);
	await page.locator('form button[type="submit"]').click();
	await page.waitForTimeout(2500);
	if (page.url().includes('/account/login')) {
		throw new Error('demo login failed');
	}
}

function proxyApi(context) {
	return context.route(/\/api\//, async (route) => {
		const url = new URL(route.request().url());
		const api = new URL(API);
		url.protocol = api.protocol;
		url.host = api.host;
		await route.continue({ url: url.toString() });
	});
}

async function shot(page, path, file, mustInclude, { fullPage = false } = {}) {
	await page.goto(`${BASE}${path}`, { waitUntil: 'networkidle' });
	await page.waitForTimeout(1100);
	await page.getByText(mustInclude, { exact: false }).first().waitFor({ timeout: 8000 });
	if (path.includes('/dashboard')) {
		await page.getByText('Mastery', { exact: false }).first().waitFor({ timeout: 8000 });
	}
	const body = await page.locator('body').innerText();
	if (/Internal Error|UNKNOWN ERROR|Click the "Create"-button|\/api\/v1\//i.test(body)) {
		throw new Error(`${file}: bad dashboard copy or error`);
	}
	if (path.includes('/dashboard') && page.url().includes('/account/login')) {
		throw new Error(`${file}: redirected to login`);
	}
	if (fullPage) {
		await page.evaluate(() => window.scrollTo(0, 0));
	}
	await page.screenshot({ path: `${OUT}/${file}.png`, fullPage });
	console.log('ok', file);
}

const browser = await chromium.launch();
await mkdir(OUT, { recursive: true });

{
	const homeCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
	await proxyApi(homeCtx);
	const homePage = await homeCtx.newPage();
	await shot(homePage, '/', 'home-1280', 'Clash.');
	await homeCtx.close();
}

for (const vp of VIEWPORTS) {
	const context = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
	await proxyApi(context);
	const page = await context.newPage();
	await login(page);
	await shot(page, '/dashboard', `dashboard-${vp.name}`, 'Quizzes', {
		fullPage: false
	});
	await shot(page, '/dashboard?empty=1', `dashboard-empty-${vp.name}`, 'No quizzes yet', {
		fullPage: vp.name === '375'
	});
	await context.close();
}

const desktop = await browser.newContext({ viewport: { width: 1280, height: 800 } });
await proxyApi(desktop);
const page = await desktop.newPage();
await login(page);
await shot(page, '/dashboard', 'dashboard', 'Quizzes');
await desktop.close();

await browser.close();
console.log('done');
