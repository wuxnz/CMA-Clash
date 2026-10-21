import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://localhost:3000';
const API = process.env.API_BASE ?? 'https://cmaclash-api.onrender.com';
const OUT = process.env.SCREENSHOT_OUT ?? 'docs/screenshots/table-alignment/after';

const VIEWPORTS = [
	{ name: '1280', width: 1280, height: 900 },
	{ name: '390', width: 390, height: 844 }
];

function proxyApi(context) {
	return context.route('**/api/**', async (route) => {
		const reqUrl = new URL(route.request().url());
		if (!reqUrl.pathname.startsWith('/api/')) {
			await route.continue();
			return;
		}
		const api = new URL(API);
		const target = `${api.origin}${reqUrl.pathname}${reqUrl.search}`;
		const response = await route.fetch({ url: target });
		await route.fulfill({ response });
	});
}

async function shot(page, path, file) {
	await page.goto(`${BASE}${path}`, { waitUntil: 'domcontentloaded' });
	await page.locator('[data-browse-list]').getByRole('button', { name: 'Host' }).first().waitFor({
		timeout: 45_000,
		state: 'visible'
	});
	await page.waitForLoadState('networkidle', { timeout: 15_000 }).catch(() => {});
	await page.waitForTimeout(300);
	await page.screenshot({ path: `${OUT}/${file}.png` });
	console.log('ok', file);
}

await mkdir(OUT, { recursive: true });
const browser = await chromium.launch();

for (const vp of VIEWPORTS) {
	for (const path of ['/explore', '/search']) {
		const context = await browser.newContext({
			viewport: { width: vp.width, height: vp.height },
			colorScheme: 'dark'
		});
		await proxyApi(context);
		const page = await context.newPage();
		const name = `${path.slice(1)}-${vp.name}`;
		await shot(page, path, name);
		await page.waitForTimeout(200);
		await page.unrouteAll({ behavior: 'ignoreErrors' });
		await context.close();
	}
}

await browser.close();
console.log('done', OUT);
