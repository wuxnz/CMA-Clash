// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

/**
 * Origin used for server-side fetches to the ClassQuiz API.
 *
 * - Local + Caddy: set API_URL=http://localhost:8080
 * - Vercel (rewrites): set API_URL to your public site URL (or rely on VERCEL_URL)
 * - Split without rewrites: set API_URL to the backend origin
 */
export function getServerApiOrigin(): string {
	if (process.env.API_URL) {
		return process.env.API_URL.replace(/\/$/, '');
	}
	if (process.env.VERCEL_URL) {
		return `https://${process.env.VERCEL_URL}`;
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
