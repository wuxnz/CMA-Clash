// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

const GUEST_PLAYER_KEY = 'cma_battle_guest_player_id';
const HOST_SECRET_PREFIX = 'cma_battle_host_secret:';

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
