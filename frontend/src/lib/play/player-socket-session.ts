// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import Cookies from 'js-cookie';
import { socket } from '$lib/socket';
import { attachPlaySocketDebug } from '$lib/play/play-socket-debug';

export interface JoinedGameCookie {
	sid: string;
	username: string;
	game_pin: string;
}

export function readJoinedGameCookie(): JoinedGameCookie | null {
	const raw = Cookies.get('joined_game');
	if (!raw) return null;
	try {
		return JSON.parse(raw) as JoinedGameCookie;
	} catch {
		return null;
	}
}

export function persistJoinedGameCookie(username: string, game_pin: string): void {
	Cookies.set(
		'joined_game',
		JSON.stringify({ sid: socket.id, username, game_pin }),
		{ expires: 3600 }
	);
}

/** Re-attach socket to game_pin room after transport reconnect (new sid). */
export function emitRejoinFromCookie(gamePinFallback?: string): boolean {
	const payload = readJoinedGameCookie();
	if (!payload) return false;
	socket.emit('rejoin_game', {
		old_sid: payload.sid,
		username: payload.username,
		game_pin: payload.game_pin || gamePinFallback || ''
	});
	return true;
}

let sessionInstalled = false;

/**
 * Register reconnect + debug hooks exactly once for the /play route.
 * Must run before JoinGame can unmount so connect handlers are not the only copy on join UI.
 */
export function ensurePlaySocketSession(options?: {
	gamePinFallback?: string;
	onReconnected?: () => void | Promise<void>;
}): void {
	if (sessionInstalled) return;
	sessionInstalled = true;

	attachPlaySocketDebug(socket);

	const onConnect = () => {
		const hadSession = Boolean(readJoinedGameCookie());
		if (!hadSession) return;
		emitRejoinFromCookie(options?.gamePinFallback);
		void options?.onReconnected?.();
	};

	socket.on('connect', onConnect);
}
