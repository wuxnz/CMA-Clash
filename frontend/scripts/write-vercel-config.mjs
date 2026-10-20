// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const DEFAULT_BACKEND = 'https://cmaclash-api.onrender.com';

const scriptDir = dirname(fileURLToPath(import.meta.url));
/** Repo-root vercel.json (Vercel builds from repository root, not frontend/). */
const vercelPath = join(scriptDir, '..', '..', 'vercel.json');

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

function loadExistingConfig() {
	if (!existsSync(vercelPath)) {
		return { headers: defaultPrivateHeaders };
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

const backend =
	normalizeBackendUrl(process.env.BACKEND_URL) ?? normalizeBackendUrl(DEFAULT_BACKEND);

if (!backend) {
	console.log(
		'BACKEND_URL missing or invalid — not updating root vercel.json rewrites (would risk DNS_HOSTNAME_EMPTY).'
	);
	process.exit(0);
}

const existing = loadExistingConfig();
const config = {
	$schema: existing.$schema ?? 'https://openapi.vercel.sh/vercel.json',
	...(existing.installCommand ? { installCommand: existing.installCommand } : {}),
	...(existing.buildCommand ? { buildCommand: existing.buildCommand } : {}),
	headers: existing.headers?.length ? existing.headers : defaultPrivateHeaders,
	rewrites: buildRewrites(backend)
};

writeFileSync(vercelPath, `${JSON.stringify(config, null, '\t')}\n`);
console.log(`Wrote root vercel.json with backend ${backend}`);
