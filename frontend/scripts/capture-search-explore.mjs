import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const BASE = process.env.SCREENSHOT_BASE ?? 'http://127.0.0.1:3000';
const API = process.env.API_BASE ?? 'http://127.0.0.1:8000';
const OUT = process.env.SCREENSHOT_OUT ?? '../cma-clash-research/screenshots/after/dark';

const VIEWPORTS = [
	{ name: '375', width: 375, height: 844, fullPage: true },
	{ name: '768', width: 768, height: 1024, fullPage: false },
	{ name: '1280', width: 1280, height: 1024, fullPage: false }
];

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
	if (mustInclude === 'Host') {
		await page.locator('[data-browse-list]').getByRole('button', { name: 'Host' }).first().waitFor({
			timeout: 12000
		});
	} else {
		await page.getByText(mustInclude, { exact: false }).first().waitFor({ timeout: 12000 });
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

for (const vp of VIEWPORTS) {
	const context = await browser.newContext({
		viewport: { width: vp.width, height: vp.height },
		colorScheme: 'dark'
	});
	await proxyApi(context);
	const page = await context.newPage();
	await shot(page, '/search', `search-${vp.name}`, 'Host', { fullPage: vp.fullPage });
	await shot(page, '/explore', `explore-${vp.name}`, 'Host', { fullPage: vp.fullPage });
	await context.close();
}

{
	const context = await browser.newContext({
		viewport: { width: 1280, height: 1024 },
		colorScheme: 'dark'
	});
	await proxyApi(context);
	const page = await context.newPage();
	await shot(page, '/search?q=zzzznope', 'search-empty-1280', 'No results', { fullPage: false });
	await context.close();
}

await browser.close();
console.log('done');
