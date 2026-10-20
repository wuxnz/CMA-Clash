/** Dark-only marketing samples (1280x800). */
import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after/dark';

const routes = [
	['home', '/'],
	['join', '/play'],
	['demo-live-question', '/demo/screens#live-question'],
	['leaderboard', '/leaderboard'],
	['editor-create', '/create']
];

const browser = await chromium.launch();
await mkdir(OUT, { recursive: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
for (const [name, path] of routes) {
	await page.goto(`${BASE}${path.split('#')[0]}`, { waitUntil: 'networkidle' });
	if (path.includes('#')) {
		const id = path.split('#')[1];
		await page.evaluate((i) => document.getElementById(i)?.scrollIntoView(), id);
		await page.waitForTimeout(400);
	}
	await page.screenshot({ path: `${OUT}/${name}.png` });
	console.log('wrote', name);
}
await browser.close();
