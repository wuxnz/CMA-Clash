/** Dark marketing samples with optional demo login for authed routes. */
import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after/dark';
const DEMO_EMAIL = process.env.DEMO_EMAIL ?? 'demo@cmaclash.local';
const DEMO_PASSWORD = process.env.DEMO_PASSWORD ?? 'CMA-Clash-Demo1!';

async function login(page) {
	await page.goto(`${BASE}/account/login`, { waitUntil: 'networkidle' });
	const email = page.locator('#email');
	if (!(await email.isVisible().catch(() => false))) return false;
	await email.fill(DEMO_EMAIL);
	await page.locator('form button[type="submit"]:not([disabled])').click();
	await page.waitForTimeout(1200);
	const pw = page.locator('#password');
	if (!(await pw.isVisible().catch(() => false))) {
		const usePassword = page.getByRole('button', { name: /password/i });
		if (await usePassword.isVisible().catch(() => false)) {
			await usePassword.click();
		}
	}
	await pw.waitFor({ state: 'visible', timeout: 15000 });
	await pw.fill(DEMO_PASSWORD);
	await page.locator('form button[type="submit"]').click();
	await page.waitForTimeout(3500);
	return !page.url().includes('/account/login');
}

async function assertNotError(page, label) {
	const body = await page.locator('body').innerText();
	if (body.includes('Internal Error') || body.match(/\b500\b/) && body.includes('Error')) {
		throw new Error(`${label}: page looks like an error state`);
	}
}

const API = process.env.API_BASE ?? 'http://127.0.0.1:8000';

const browser = await chromium.launch();
await mkdir(OUT, { recursive: true });
const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
await context.route(/\/api\//, async (route) => {
	const url = new URL(route.request().url());
	url.protocol = new URL(API).protocol;
	url.host = new URL(API).host;
	await route.continue({ url: url.toString() });
});
const page = await context.newPage();

const publicRoutes = [
	['join', '/play'],
	['home', '/'],
	['demo-live-question', '/demo/screens#live-question'],
	['leaderboard', '/leaderboard']
];

for (const [name, path] of publicRoutes) {
	await page.goto(`${BASE}${path.split('#')[0]}`, { waitUntil: 'networkidle' });
	if (path.includes('#')) {
		const id = path.split('#')[1];
		await page.evaluate((i) => document.getElementById(i)?.scrollIntoView(), id);
		await page.waitForTimeout(400);
	}
	await assertNotError(page, name);
	await page.screenshot({ path: `${OUT}/${name}.png` });
	console.log('ok', name);
}

const authed = await login(page);
if (!authed) {
	console.warn('demo login failed — skipping authed shots');
} else {
	for (const [name, path] of [
		['dashboard', '/dashboard'],
		['editor-create', '/create']
	]) {
		await page.goto(`${BASE}${path}`, { waitUntil: 'networkidle' });
		await assertNotError(page, name);
		if (name === 'editor-create' && page.url().includes('/account/login')) {
			throw new Error('editor-create: still on login');
		}
		await page.screenshot({ path: `${OUT}/${name}.png` });
		console.log('ok', name);
	}
}

await browser.close();
console.log('done');
