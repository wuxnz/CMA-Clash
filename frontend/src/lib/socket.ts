// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { io } from 'socket.io-client';
import { env } from '$env/dynamic/public';
import { browser } from '$app/environment';

// Vercel rewrites cannot proxy websockets, so in production the socket must
// connect straight to the API host. Local dev (localhost / LAN) keeps using the
// same-origin Vite proxy.
const DEFAULT_PRODUCTION_SOCKET_URL = 'https://cmaclash-api.onrender.com';

function isLocalHost(hostname: string): boolean {
	return (
		hostname === 'localhost' ||
		hostname === '127.0.0.1' ||
		hostname === '[::1]' ||
		hostname.endsWith('.local') ||
		/^(10|192\.168|172\.(1[6-9]|2\d|3[01]))\./.test(hostname)
	);
}

export function resolveSocketUrl(): string | undefined {
	const configured = env.PUBLIC_SOCKET_URL?.trim().replace(/\/$/, '');
	if (configured) return configured;
	if (browser && !isLocalHost(window.location.hostname)) {
		return DEFAULT_PRODUCTION_SOCKET_URL;
	}
	return undefined;
}

function resolveSocketTransports(): ('websocket' | 'polling')[] {
	const configured = env.PUBLIC_SOCKET_URL?.trim();
	// Local preview/dev hitting a remote API: websocket often fails (CORS/mixed context); polling works.
	if (browser && isLocalHost(window.location.hostname) && configured) {
		return ['polling', 'websocket'];
	}
	// Production site → Render API: prefer polling first (headless e2e + some networks block WS upgrade).
	if (browser && !isLocalHost(window.location.hostname)) {
		return ['polling', 'websocket'];
	}
	return ['websocket', 'polling'];
}

export const socket = io(resolveSocketUrl(), {
	withCredentials: true,
	transports: resolveSocketTransports()
});
