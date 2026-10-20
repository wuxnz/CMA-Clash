// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { Handle } from '@sveltejs/kit';
import * as jose from 'jose';
import { fetchWithRetry } from '$lib/api/http';
import { getBackendOrigin, ssrBackendFetch } from '$lib/server-api';

const PRIVATE_ROBOTS = 'noindex, nofollow';

function shouldProxyApi(pathname: string): boolean {
	return (
		pathname.startsWith('/api/') ||
		pathname === '/api' ||
		pathname === '/openapi.json' ||
		pathname === '/rapidoc' ||
		pathname.startsWith('/rapidoc/')
	);
}

/** Vercel edge rewrites skip many trailing-slash `/api/*` URLs; normalize before proxying. */
function normalizeApiPathname(pathname: string): string {
	if (!pathname.startsWith('/api')) {
		return pathname;
	}
	if (pathname.length > 1 && pathname.endsWith('/')) {
		return pathname.replace(/\/+$/, '');
	}
	return pathname;
}

function sanitizeProxyResponse(res: Response): Response {
	const headers = new Headers(res.headers);
	headers.delete('content-encoding');
	headers.delete('transfer-encoding');
	headers.delete('content-length');
	headers.set('X-Robots-Tag', PRIVATE_ROBOTS);
	return new Response(res.body, {
		status: res.status,
		statusText: res.statusText,
		headers
	});
}

async function proxyToBackend(request: Request): Promise<Response> {
	const url = new URL(request.url);
	const pathname = normalizeApiPathname(url.pathname);
	const target = `${getBackendOrigin()}${pathname}${url.search}`;
	const headers = new Headers(request.headers);
	headers.delete('host');
	headers.delete('connection');

	let body: ArrayBuffer | undefined;
	if (request.method !== 'GET' && request.method !== 'HEAD') {
		body = await request.arrayBuffer();
		headers.delete('content-length');
		if (body.byteLength > 0) {
			headers.set('content-length', String(body.byteLength));
		}
	}

	const fetchOpts: RequestInit = {
		method: request.method,
		headers,
		redirect: 'manual',
		body
	};

	const retryOpts = { attempts: 3, baseDelayMs: 1500, timeoutMs: 25_000 };

	let res = await fetchWithRetry(target, fetchOpts, retryOpts);

	if (
		res &&
		(res.status === 301 || res.status === 302 || res.status === 307 || res.status === 308)
	) {
		const location = res.headers.get('location');
		if (location) {
			const redirectUrl = new URL(location, target);
			const redirectPath = normalizeApiPathname(redirectUrl.pathname);
			const redirectTarget = `${getBackendOrigin()}${redirectPath}${redirectUrl.search}`;
			res = await fetchWithRetry(
				redirectTarget,
				{
					method: request.method,
					headers,
					redirect: 'manual',
					body: request.method === 'GET' || request.method === 'HEAD' ? undefined : body
				},
				retryOpts
			);
		}
	}

	if (!res) {
		return new Response(JSON.stringify({ detail: 'Upstream API unavailable' }), {
			status: 502,
			headers: { 'Content-Type': 'application/json', 'X-Robots-Tag': PRIVATE_ROBOTS }
		});
	}
	return sanitizeProxyResponse(res);
}

function withRobotsTag(response: Response): Response {
	const headers = new Headers(response.headers);
	headers.set('X-Robots-Tag', PRIVATE_ROBOTS);
	return new Response(response.body, {
		status: response.status,
		statusText: response.statusText,
		headers
	});
}

/** @type {import('@sveltejs/kit').Handle} */
export const handle: Handle = async ({ event, resolve }) => {
	if (shouldProxyApi(event.url.pathname)) {
		return withRobotsTag(await proxyToBackend(event.request));
	}

	const access_token = event.cookies.get('access_token');
	if (!access_token) {
		event.locals.email = null;
		return withRobotsTag(await resolve(event));
	}
	const jwt = jose.decodeJwt(access_token.replace('Bearer ', ''));
	if (!jwt) {
		event.locals.email = null;
		return withRobotsTag(await resolve(event));
	}
	// if token expires, do a request to get a new one and set the response-cookies on the response
	if (Date.now() >= jwt.exp * 1000) {
		const res = await ssrBackendFetch('/api/v1/users/check', {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Cookie: event.request.headers.get('cookie') || ''
			}
		});
		if (res?.ok) {
			event.locals.email = await res.text();
			const resp = await resolve(event);
			try {
				resp.headers.set('Set-Cookie', res.headers.get('set-cookie'));
			} catch {
				/* empty */
			}
			return withRobotsTag(resp);
		}
	}
	event.locals.email = jwt.sub;
	return withRobotsTag(await resolve(event));
};
