import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after';

const mobileRoutes = [
	['join', '/play'],
	['demo-live-question', '/demo/screens#live-question'],
	['demo-podium', '/demo/screens#podium']
];

const browser = await chromium.launch();
const videoDir = `${OUT}/video`;
await mkdir(`${OUT}/mobile/dark`, { recursive: true });
await mkdir(videoDir, { recursive: true });

const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
for (const [name, path] of mobileRoutes) {
	await mobile.goto(`${BASE}${path.split('#')[0]}`, { waitUntil: 'networkidle' });
	if (path.includes('#')) {
		const id = path.split('#')[1];
		await mobile.evaluate((i) => document.getElementById(i)?.scrollIntoView(), id);
		await mobile.waitForTimeout(400);
	}
	await mobile.screenshot({ path: `${OUT}/mobile/dark/${name}.png` });
	console.log('mobile', name);
}
await mobile.close();

const recCtx = await browser.newContext({
	viewport: { width: 1280, height: 800 },
	recordVideo: { dir: videoDir, size: { width: 1280, height: 800 } }
});
await recCtx.addInitScript(() => {
	localStorage.setItem('theme', 'dark');
	document.documentElement.classList.add('dark');
});
const rec = await recCtx.newPage();
await rec.goto(`${BASE}/`, { waitUntil: 'domcontentloaded' });
await rec.evaluate(async () => {
	const h = document.body.scrollHeight;
	for (let i = 0; i <= 28; i++) {
		window.scrollTo(0, (h * i) / 28);
		await new Promise((r) => setTimeout(r, 140));
	}
});
await rec.waitForTimeout(500);
const landingVid = rec.video();
await rec.close();
await landingVid?.saveAs(`${videoDir}/landing-scroll.webm`);
await recCtx.close();

const podCtx = await browser.newContext({
	viewport: { width: 1280, height: 800 },
	recordVideo: { dir: videoDir, size: { width: 1280, height: 800 } }
});
await podCtx.addInitScript(() => {
	localStorage.setItem('theme', 'dark');
	document.documentElement.classList.add('dark');
});
const pod = await podCtx.newPage();
await pod.goto(`${BASE}/demo/screens`, { waitUntil: 'domcontentloaded' });
await pod.evaluate(() => document.getElementById('podium')?.scrollIntoView());
await pod.waitForTimeout(5000);
const podVid = pod.video();
await pod.close();
await podVid?.saveAs(`${videoDir}/podium-reveal.webm`);
await podCtx.close();
await browser.close();
console.log('done');
