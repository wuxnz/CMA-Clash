// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { BattleLobby } from '$lib/cma/client';

const GUEST_PLAYER_KEY = 'cma_battle_guest_player_id';
const HOST_SECRET_PREFIX = 'cma_battle_host_secret:';
const PLAY_SESSION_PREFIX = 'cma_battle_play_username:';

export function getBattleGuestPlayerId(): string | null {
	if (typeof sessionStorage === 'undefined') return null;
	return sessionStorage.getItem(GUEST_PLAYER_KEY);
}

export function setBattleGuestPlayerId(id: string): void {
	sessionStorage.setItem(GUEST_PLAYER_KEY, id);
}

export function getBattleHostSecret(code: string): string | null {
	if (typeof sessionStorage === 'undefined') return null;
	return sessionStorage.getItem(`${HOST_SECRET_PREFIX}${code}`);
}

export function setBattleHostSecret(code: string, secret: string): void {
	sessionStorage.setItem(`${HOST_SECRET_PREFIX}${code}`, secret);
}

/** Lobby nickname to reuse on /play so battle players are not prompted again. */
export function setBattlePlayUsername(gamePin: string, username: string): void {
	if (typeof sessionStorage === 'undefined') return;
	const pin = gamePin.replace(/\D/g, '');
	const name = username.trim();
	if (pin.length < 6 || name.length < 2) return;
	sessionStorage.setItem(`${PLAY_SESSION_PREFIX}${pin}`, name);
}

export function getBattlePlayUsername(gamePin: string): string | null {
	if (typeof sessionStorage === 'undefined') return null;
	const pin = gamePin.replace(/\D/g, '');
	if (pin.length < 6) return null;
	return sessionStorage.getItem(`${PLAY_SESSION_PREFIX}${pin}`);
}

export function clearBattlePlayUsername(gamePin: string): void {
	if (typeof sessionStorage === 'undefined') return;
	const pin = gamePin.replace(/\D/g, '');
	sessionStorage.removeItem(`${PLAY_SESSION_PREFIX}${pin}`);
}

export function battleLobbyUsernameForPlayer(
	lobby: BattleLobby,
	opts: { userId?: string | null; guestPlayerId?: string | null }
): string | null {
	const guestId = opts.guestPlayerId ?? getBattleGuestPlayerId();
	for (const slot of lobby.player_slots ?? []) {
		if (!slot.username) continue;
		if (opts.userId != null && slot.user_id === opts.userId) return slot.username;
		if (guestId != null && slot.user_id === guestId) return slot.username;
	}
	return null;
}
