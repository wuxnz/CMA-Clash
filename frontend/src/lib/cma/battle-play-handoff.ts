// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { BattleLobby } from '$lib/cma/client';
import {
	battleLobbyUsernameForPlayer,
	setBattlePlayUsername
} from '$lib/cma/battle-guest';
import {
	clearJoinedGameCookie,
	preparePlaySessionForPin
} from '$lib/play/player-socket-session';

/** Clear stale live-game state and stash the lobby nickname for /play auto-join. */
export function prepareBattlePlayHandoff(
	lobby: BattleLobby,
	opts: { userId?: string | null; guestPlayerId?: string | null }
): string | null {
	const pin = lobby.game_pin?.replace(/\D/g, '') ?? '';
	if (pin.length < 6) return null;
	clearJoinedGameCookie();
	preparePlaySessionForPin(pin);
	const name = battleLobbyUsernameForPlayer(lobby, opts);
	if (name) setBattlePlayUsername(pin, name);
	return pin;
}
