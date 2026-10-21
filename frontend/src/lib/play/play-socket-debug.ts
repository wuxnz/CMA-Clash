// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { Socket } from 'socket.io-client';

const DEBUG_KEY = 'cma_play_socket_debug';

export function isPlaySocketDebugEnabled(): boolean {
	if (typeof window === 'undefined') return false;
	try {
		if (window.localStorage.getItem(DEBUG_KEY) === '1') return true;
	} catch {
		/* private mode */
	}
	return Boolean((window as unknown as { __CMA_PLAY_SOCKET_DEBUG?: boolean }).__CMA_PLAY_SOCKET_DEBUG);
}

function ts(): string {
	return new Date().toISOString();
}

function logLine(socket: Socket, kind: string, detail?: unknown) {
	const sid = socket.id ?? '(no sid)';
	const payload =
		detail === undefined ? '' : ` ${typeof detail === 'string' ? detail : JSON.stringify(detail)}`;
	console.info(`[cma-play-socket] ${ts()} sid=${sid} ${kind}${payload}`);
}

/** Attach once per page load; logs transport lifecycle and every inbound event when debug is on. */
export function attachPlaySocketDebug(socket: Socket): void {
	if (!isPlaySocketDebugEnabled()) return;
	if ((socket as unknown as { __cmaPlayDebugAttached?: boolean }).__cmaPlayDebugAttached) {
		return;
	}
	(socket as unknown as { __cmaPlayDebugAttached?: boolean }).__cmaPlayDebugAttached = true;

	logLine(socket, 'debug_enabled', { transport: socket.io.engine?.transport?.name });

	socket.on('connect', () => {
		logLine(socket, 'connect', { recovered: (socket as unknown as { recovered?: boolean }).recovered });
	});
	socket.on('disconnect', (reason) => {
		logLine(socket, 'disconnect', { reason });
	});
	socket.io.on('reconnect', (attempt) => {
		logLine(socket, 'reconnect', { attempt });
	});
	socket.io.on('reconnect_attempt', (attempt) => {
		logLine(socket, 'reconnect_attempt', { attempt });
	});
	socket.io.on('reconnect_error', (err: Error) => {
		logLine(socket, 'reconnect_error', { message: err?.message });
	});
	socket.io.on('upgrade', () => {
		logLine(socket, 'upgrade', { transport: socket.io.engine?.transport?.name });
	});

	socket.onAny((event, ...args) => {
		if (event === 'connect' || event === 'disconnect') return;
		const sample = args.length === 1 ? args[0] : args;
		logLine(socket, `event:${event}`, sample);
	});
}
