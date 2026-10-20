// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const backend = process.env.BACKEND_URL?.replace(/\/$/, '');

if (!backend) {
	console.log('BACKEND_URL not set — skipping vercel.json generation (use vercel.json.example as a template).');
	process.exit(0);
}

const root = dirname(fileURLToPath(import.meta.url));
const config = {
	$schema: 'https://openapi.vercel.sh/vercel.json',
	framework: null,
	rewrites: [
		{ source: '/api/:path*', destination: `${backend}/api/:path*` },
		{ source: '/socket.io', destination: `${backend}/socket.io` },
		{ source: '/socket.io/:path*', destination: `${backend}/socket.io/:path*` },
		{ source: '/openapi.json', destination: `${backend}/openapi.json` },
		{ source: '/rapidoc', destination: `${backend}/rapidoc` },
		{ source: '/rapidoc/:path*', destination: `${backend}/rapidoc/:path*` }
	]
};

writeFileSync(join(root, '..', 'vercel.json'), `${JSON.stringify(config, null, 2)}\n`);
console.log(`Wrote vercel.json with backend ${backend}`);
