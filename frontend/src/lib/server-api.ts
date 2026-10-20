// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

const DEFAULT_BACKEND_ORIGIN = 'https://cmaclash-api.onrender.com';

/**
 * Origin used for server-side fetches to the CMA Clash API.
 *
 * - Local + Caddy: set API_URL=http://localhost:8080
 * - Vercel (rewrites): set API_URL to your public site URL (or rely on VERCEL_URL)
 * - Split without rewrites: set API_URL or BACKEND_URL to the backend origin
 */
export function getServerApiOrigin(): string {
	if (process.env.API_URL) {
		return process.env.API_URL.replace(/\/$/, '');
	}
	if (process.env.VERCEL_URL) {
		return `https://${process.env.VERCEL_URL}`;
	}
	const backend = process.env.BACKEND_URL?.replace(/\/$/, '');
	if (backend) {
		return backend;
	}
	if (process.env.VERCEL === '1') {
		return DEFAULT_BACKEND_ORIGIN;
	}
	return 'http://localhost:8080';
}

export function serverApiUrl(path: string): string {
	const origin = getServerApiOrigin();
	if (!path.startsWith('/')) {
		return `${origin}/${path}`;
	}
	return `${origin}${path}`;
}
