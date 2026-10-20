// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const backend = process.env.BACKEND_URL?.replace(/\/$/, '');

const root = dirname(fileURLToPath(import.meta.url));
const vercelPath = join(root, '..', 'vercel.json');

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

if (!backend) {
	console.log('BACKEND_URL not set — keeping existing vercel.json (private launch headers only).');
	process.exit(0);
}

const existing = loadExistingConfig();
const config = {
	$schema: 'https://openapi.vercel.sh/vercel.json',
	framework: null,
	headers: existing.headers?.length ? existing.headers : defaultPrivateHeaders,
	rewrites: [
		{ source: '/api/:path*', destination: `${backend}/api/:path*` },
		{ source: '/socket.io', destination: `${backend}/socket.io` },
		{ source: '/socket.io/:path*', destination: `${backend}/socket.io/:path*` },
		{ source: '/openapi.json', destination: `${backend}/openapi.json` },
		{ source: '/rapidoc', destination: `${backend}/rapidoc` },
		{ source: '/rapidoc/:path*', destination: `${backend}/rapidoc/:path*` }
	]
};

writeFileSync(vercelPath, `${JSON.stringify(config, null, '\t')}\n`);
console.log(`Wrote vercel.json with backend ${backend}`);
