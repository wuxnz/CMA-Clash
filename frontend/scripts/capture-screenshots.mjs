/**
 * Capture UI screenshots + short recordings.
 * Set SCREENSHOT_BASE (default http://127.0.0.1:3000). API on :8000 via vite proxy or Caddy.
 */
import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after';
const DEMO_EMAIL = process.env.DEMO_EMAIL ?? 'demo@cmaclash.local';
const DEMO_PASSWORD = process.env.DEMO_PASSWORD ?? 'CMA-Clash-Demo1!';

const desktopRoutes = [
	['home', '/'],
	['login', '/account/login'],
	['join', '/play'],
	['leaderboard', '/leaderboard'],
	['battle', '/battle'],
	['practice', '/practice'],
	['dashboard', '/dashboard'],
	['demo-host-lobby', '/demo/screens#host-lobby'],
	['demo-live-question', '/demo/screens#live-question'],
	['demo-results', '/demo/screens#results'],
	['demo-podium', '/demo/screens#podium'],
	['battle-vs', '/demo/battle-vs'],
	['battle-countdown', '/demo/battle-vs?countdown=1']
];

const mobileRoutes = [
	['join', '/play'],
	['demo-live-question', '/demo/screens#live-question'],
	['demo-podium', '/demo/screens#podium']
];

async function shot(page, file, opts = {}) {
	if (!opts.skipReload) {
		await page.reload({ waitUntil: 'networkidle' });
	}
	await page.waitForTimeout(800);
	if (opts.beforeCapture) await opts.beforeCapture(page);
	if (file.includes('#')) {
		const hash = file.split('#').pop();
		await page.evaluate((id) => {
			const el = document.getElementById(id);
			el?.scrollIntoView({ block: 'start' });
		}, hash);
		await page.waitForTimeout(400);
	}
	const pathOnly = file.replace(/#.*$/, '');
	await page.screenshot({ path: pathOnly, fullPage: false });
}

async function tryLogin(page) {
	await page.goto(`${BASE}/account/login`, { waitUntil: 'networkidle' });
	const email = page.locator('#email');
	if (!(await email.isVisible().catch(() => false))) return;
	await email.fill(DEMO_EMAIL);
	await page.locator('form button[type="submit"]:not([disabled])').click();
	await page.waitForSelector('#password', { timeout: 15000 }).catch(() => {});
	const pw = page.locator('#password');
	if (await pw.isVisible().catch(() => false)) {
		await pw.fill(DEMO_PASSWORD);
		await page.locator('form button[type="submit"]').click();
		await page.waitForTimeout(2500);
	}
}

async function main() {
	const browser = await chromium.launch();
	const missing = [];

	const themeDir = `${OUT}/dark`;
	await mkdir(themeDir, { recursive: true });
	const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
	await tryLogin(page);
	for (const [name, path] of desktopRoutes) {
		try {
			const opts =
				name === 'battle-countdown'
					? {
							beforeCapture: async (p) => {
								await p.click('button:has-text("Preview countdown")').catch(() => {});
								await p.waitForTimeout(700);
							}
						}
					: {};
			await page.goto(`${BASE}${path.split('#')[0]}`, { waitUntil: 'networkidle', timeout: 60000 });
			await shot(page, `${themeDir}/${name}.png`, opts);
			console.log('wrote dark', name);
		} catch (e) {
			missing.push(`dark/${name}: ${e.message}`);
			console.warn('skip', name, e.message);
		}
	}
	await page.close();

	await mkdir(`${OUT}/mobile/dark`, { recursive: true });
	const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
	for (const [name, path] of mobileRoutes) {
		try {
			await mobile.goto(`${BASE}${path.split('#')[0]}`, { waitUntil: 'networkidle' });
			await shot(mobile, `${OUT}/mobile/dark/${name}.png`, { skipReload: true });
			console.log('wrote mobile dark', name);
		} catch (e) {
			missing.push(`mobile/dark/${name}: ${e.message}`);
		}
	}
	await mobile.close();

	const videoDir = `${OUT}/video`;
	await mkdir(videoDir, { recursive: true });
	const recCtx = await browser.newContext({
		viewport: { width: 1280, height: 800 },
		recordVideo: { dir: videoDir, size: { width: 1280, height: 800 } }
	});
	const rec = await recCtx.newPage();
	await rec.goto(`${BASE}/`, { waitUntil: 'networkidle' });
	await rec.evaluate(() => window.scrollTo(0, 0));
	await rec.waitForTimeout(400);
	await rec.evaluate(async () => {
		const h = document.body.scrollHeight;
		const steps = 28;
		for (let i = 0; i <= steps; i++) {
			window.scrollTo(0, (h * i) / steps);
			await new Promise((r) => setTimeout(r, 140));
		}
	});
	await rec.waitForTimeout(600);
	const landingPath = await rec.video()?.path();
	await rec.close();
	await recCtx.close();
	if (landingPath) {
		const { rename } = await import('node:fs/promises');
		await rename(landingPath, `${videoDir}/landing-scroll.webm`).catch(() => {});
		console.log('wrote video landing-scroll.webm');
	}

	const podCtx = await browser.newContext({
		viewport: { width: 1280, height: 800 },
		recordVideo: { dir: videoDir, size: { width: 1280, height: 800 } }
	});
	const pod = await podCtx.newPage();
	await pod.goto(`${BASE}/demo/screens`, { waitUntil: 'networkidle' });
	await pod.evaluate(() => document.getElementById('podium')?.scrollIntoView());
	await pod.waitForTimeout(5000);
	const podPath = await pod.video()?.path();
	await pod.close();
	await podCtx.close();
	if (podPath) {
		const { rename } = await import('node:fs/promises');
		await rename(podPath, `${videoDir}/podium-reveal.webm`).catch(() => {});
		console.log('wrote video podium-reveal.webm');
	}
	await browser.close();

	if (missing.length) {
		console.log('MISSING:', JSON.stringify(missing, null, 2));
	}
}

main().catch((e) => {
	console.error(e);
	process.exit(1);
});
