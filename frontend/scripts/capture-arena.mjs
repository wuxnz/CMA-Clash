import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after/dark';
const API = process.env.API_BASE ?? 'http://127.0.0.1:8000';
const DEMO_EMAIL = process.env.DEMO_EMAIL ?? 'demo@cmaclash.local';
const DEMO_PASSWORD = process.env.DEMO_PASSWORD ?? 'CMA-Clash-Demo1!';

async function assertOk(page, label, { allowLogin = false } = {}) {
	const t = await page.locator('body').innerText();
	if (/Internal Error|Internal Server Error|UNKNOWN ERROR/i.test(t) || (/\b500\b/.test(t) && /Error/.test(t))) {
		throw new Error(`${label}: error page — ${t.slice(0, 180)}`);
	}
	if (!allowLogin && page.url().includes('/account/login') && !label.includes('login')) {
		throw new Error(`${label}: redirected to login`);
	}
}

async function shot(page, name, path, { waitMs = 500, mustInclude } = {}) {
	await page.goto(`${BASE}${path}`, { waitUntil: 'networkidle' });
	if (waitMs) await page.waitForTimeout(waitMs);
	if (mustInclude) {
		await page.getByText(mustInclude, { exact: false }).first().waitFor({ timeout: 8000 });
	}
	await assertOk(page, name);
	await page.screenshot({ path: `${OUT}/${name}.png` });
	console.log('ok', name);
}

const browser = await chromium.launch();
await mkdir(OUT, { recursive: true });
await mkdir(`${OUT}/../mobile/dark`, { recursive: true });

const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
await context.route(/\/api\//, async (route) => {
	const url = new URL(route.request().url());
	const api = new URL(API);
	url.protocol = api.protocol;
	url.host = api.host;
	await route.continue({ url: url.toString() });
});
const page = await context.newPage();

await shot(page, 'home', '/', { mustInclude: 'Clash' });
await shot(page, 'join', '/play', { mustInclude: 'Join' });
await shot(page, 'leaderboard', '/leaderboard', { mustInclude: 'Leaderboard' });
await shot(page, 'battle-vs', '/demo/battle-vs', { mustInclude: 'VS' });
await shot(page, 'practice', '/practice', { mustInclude: 'Practice' });
await shot(page, 'host-intro', '/demo/screens?phase=host-intro', {
	mustInclude: 'pulmonary veins'
});
await shot(page, 'host-answer', '/demo/screens?phase=host-answer', {
	mustInclude: 'Left ventricle'
});
await shot(page, 'host-reveal', '/demo/screens?phase=host-reveal', {
	mustInclude: 'Left atrium'
});
await shot(page, 'host-rankings', '/demo/screens?phase=host-rankings', {
	mustInclude: 'Rankings'
});
await shot(page, 'host-podium', '/demo/screens?phase=host-podium', {
	waitMs: 4300,
	mustInclude: 'A. Okafor'
});

await page.goto(`${BASE}/account/login`, { waitUntil: 'networkidle' });
await page.fill('#email', DEMO_EMAIL);
await page.locator('form button[type="submit"]:not([disabled])').click();
await page.waitForTimeout(1000);
const pw = page.locator('#password');
if (!(await pw.isVisible().catch(() => false))) {
	const btn = page.getByRole('button', { name: /password/i });
	if (await btn.isVisible().catch(() => false)) await btn.click();
}
let dashboardAuthed = false;
try {
	await pw.waitFor({ state: 'visible', timeout: 15000 });
	await pw.fill(DEMO_PASSWORD);
	await page.locator('form button[type="submit"]').click();
	await page.waitForTimeout(3000);
	await page.goto(`${BASE}/dashboard`, { waitUntil: 'networkidle' });
	await page.waitForTimeout(1500);
	const body = await page.locator('body').innerText();
	dashboardAuthed =
		!/Internal Error|UNKNOWN ERROR/i.test(body) &&
		!page.url().includes('/account/login') &&
		!/^\s*$/.test(body) &&
		!body.includes('Loading');
	if (
		dashboardAuthed &&
		(body.includes('Battle queue') ||
			body.includes('Division') ||
			body.includes('Log out') ||
			body.includes('Section mastery'))
	) {
		await page.screenshot({ path: `${OUT}/dashboard.png` });
		console.log('ok dashboard');
	} else {
		dashboardAuthed = false;
	}
} catch (err) {
	console.warn('dashboard login path failed', err?.message ?? err);
}

if (!dashboardAuthed) {
	await page.goto(`${BASE}/demo/screens?phase=dashboard`, { waitUntil: 'networkidle' });
	await page.waitForTimeout(400);
	await assertOk(page, 'dashboard-demo');
	await page.screenshot({ path: `${OUT}/dashboard.png` });
	console.log('ok dashboard (demo composition)');
}

const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
await mobile.route(/\/api\//, async (route) => {
	const url = new URL(route.request().url());
	const api = new URL(API);
	url.protocol = api.protocol;
	url.host = api.host;
	await route.continue({ url: url.toString() });
});
const mOut = `${OUT}/../mobile/dark`;

const mobileShots = [
	['join', '/play', 'Join'],
	['player-answer', '/demo/screens?phase=player-answer', 'Left ventricle'],
	['player-correct', '/demo/screens?phase=player-correct', 'Correct'],
	['player-incorrect', '/demo/screens?phase=player-incorrect', 'Incorrect']
];

for (const [name, path, mustInclude] of mobileShots) {
	await mobile.goto(`${BASE}${path}`, { waitUntil: 'networkidle' });
	await mobile.waitForTimeout(500);
	await mobile.getByText(mustInclude, { exact: false }).first().waitFor({ timeout: 8000 });
	await assertOk(mobile, `mobile ${name}`);
	await mobile.screenshot({ path: `${mOut}/${name}.png` });
	console.log('ok mobile', name);
}

await browser.close();
console.log('done');
