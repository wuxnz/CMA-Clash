// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { browser } from '$app/environment';
import { fetchWithRetry } from '$lib/api/http';

export const DEFAULT_BACKEND_ORIGIN = 'https://cmaclash-api.onrender.com';

/** Same rules as `frontend/scripts/write-vercel-config.mjs`. */
export function normalizeHttpOrigin(raw: string | undefined | null): string | null {
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

export function getBackendOrigin(): string {
	return normalizeHttpOrigin(process.env.BACKEND_URL) ?? DEFAULT_BACKEND_ORIGIN;
}

/**
 * Origin used for server-side fetches to the CMA Clash API.
 *
 * - Local + Caddy: set API_URL=http://localhost:8080
 * - Vercel (rewrites): set API_URL to your public site URL (or rely on VERCEL_URL)
 * - Split without rewrites: set API_URL or BACKEND_URL to the backend origin
 */
export function getServerApiOrigin(): string {
	const apiUrl = normalizeHttpOrigin(process.env.API_URL);
	if (apiUrl) {
		return apiUrl;
	}
	if (process.env.VERCEL_URL) {
		return `https://${process.env.VERCEL_URL}`;
	}
	const backend = normalizeHttpOrigin(process.env.BACKEND_URL);
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

function backendApiUrl(path: string): string {
	const origin = getBackendOrigin();
	if (!path.startsWith('/')) {
		return `${origin}/${path}`;
	}
	return `${origin}${path}`;
}

/** SSR: call Render directly (validated origin, timeout, retry). Browser: same-origin `/api` via SvelteKit `fetch`. */
export async function kitOrBackendFetch(
	kitFetch: typeof fetch,
	path: string,
	init?: RequestInit
): Promise<Response | null> {
	if (browser) {
		try {
			return await kitFetch(path, init);
		} catch {
			return null;
		}
	}
	return fetchWithRetry(backendApiUrl(path), init ?? {}, {
		attempts: 4,
		baseDelayMs: 1500,
		timeoutMs: 25_000
	});
}
