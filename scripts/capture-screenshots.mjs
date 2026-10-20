/**
 * Capture marketing screenshots (1280x800). Requires frontend on :3000 with CSS.
 * Full dashboard/battle lists need backend + seed on :8000 behind same origin (Caddy or vite proxy).
 */
import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const OUT = process.env.SCREENSHOT_OUT ?? 'cma-clash-research/screenshots/after';

const routes = [
	['home', '/'],
	['login', '/account/login'],
	['play', '/play'],
	['leaderboard', '/leaderboard'],
	['battle', '/battle'],
	['demo-live-flow', '/demo/screens#live-question'],
	['demo-podium', '/demo/screens#podium']
];

async function shot(page, file, theme) {
	await page.evaluate((t) => {
		localStorage.setItem('theme', t);
		document.documentElement.classList.toggle('dark', t === 'dark');
	}, theme);
	await page.reload({ waitUntil: 'networkidle' });
	await page.waitForTimeout(600);
	await page.screenshot({ path: file, fullPage: false });
}

const browser = await chromium.launch();
for (const theme of ['dark', 'light']) {
	await mkdir(`${OUT}/${theme}`, { recursive: true });
	const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
	for (const [name, path] of routes) {
		await page.goto(`${BASE}${path}`, { waitUntil: 'networkidle' });
		await shot(page, `${OUT}/${theme}/${name}.png`, theme);
		console.log('wrote', theme, name);
	}
	await page.close();
}
await browser.close();
