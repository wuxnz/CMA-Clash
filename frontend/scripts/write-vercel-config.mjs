// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const DEFAULT_BACKEND = 'https://cmaclash-api.onrender.com';

const scriptDir = dirname(fileURLToPath(import.meta.url));
const frontendVercelPath = join(scriptDir, '..', 'vercel.json');
const rootVercelPath = join(scriptDir, '..', '..', 'vercel.json');

const defaultPrivateHeaders = [
	{
		source: '/(.*)',
		headers: [
			{
				key: 'X-Robots-Tag',
				value: 'noindex, nofollow'
			}
		]
	}
];

function normalizeBackendUrl(raw) {
	if (!raw || typeof raw !== 'string') {
		return null;
	}
	const trimmed = raw.trim().replace(/\/$/, '');
	if (!trimmed) {
		return null;
	}
	try {
		const url = new URL(trimmed);
		if (!url.hostname) {
			return null;
		}
		if (url.protocol !== 'https:' && url.protocol !== 'http:') {
			return null;
		}
		return trimmed;
	} catch {
		return null;
	}
}

function loadExistingConfig(vercelPath) {
	if (!existsSync(vercelPath)) {
		return null;
	}
	try {
		return JSON.parse(readFileSync(vercelPath, 'utf8'));
	} catch {
		return { headers: defaultPrivateHeaders };
	}
}

function buildRewrites(backend) {
	return [
		{ source: '/api/:path*', destination: `${backend}/api/:path*` },
		{ source: '/socket.io', destination: `${backend}/socket.io` },
		{ source: '/socket.io/:path*', destination: `${backend}/socket.io/:path*` },
		{ source: '/openapi.json', destination: `${backend}/openapi.json` },
		{ source: '/rapidoc', destination: `${backend}/rapidoc` },
		{ source: '/rapidoc/:path*', destination: `${backend}/rapidoc/:path*` }
	];
}

function mergeConfig(existing, backend) {
	const base = existing ?? { headers: defaultPrivateHeaders };
	return {
		$schema: base.$schema ?? 'https://openapi.vercel.sh/vercel.json',
		...(base.framework !== undefined ? { framework: base.framework } : {}),
		...(base.installCommand ? { installCommand: base.installCommand } : {}),
		...(base.buildCommand ? { buildCommand: base.buildCommand } : {}),
		headers: base.headers?.length ? base.headers : defaultPrivateHeaders,
		rewrites: buildRewrites(backend)
	};
}

function writeVercelConfig(vercelPath, backend) {
	const existing = loadExistingConfig(vercelPath);
	if (existing === null) {
		return false;
	}
	const config = mergeConfig(existing, backend);
	writeFileSync(vercelPath, `${JSON.stringify(config, null, '\t')}\n`);
	return true;
}

const backend =
	normalizeBackendUrl(process.env.BACKEND_URL) ?? normalizeBackendUrl(DEFAULT_BACKEND);

if (!backend) {
	console.log(
		'BACKEND_URL missing or invalid — not updating vercel.json rewrites (would risk DNS_HOSTNAME_EMPTY).'
	);
	process.exit(0);
}

const wroteFrontend = writeVercelConfig(frontendVercelPath, backend);
const wroteRoot = writeVercelConfig(rootVercelPath, backend);

if (wroteFrontend) {
	console.log(`Wrote frontend/vercel.json with backend ${backend}`);
}
if (wroteRoot) {
	console.log(`Wrote root vercel.json with backend ${backend}`);
}
if (!wroteFrontend && !wroteRoot) {
	console.log('No vercel.json found to update.');
}
