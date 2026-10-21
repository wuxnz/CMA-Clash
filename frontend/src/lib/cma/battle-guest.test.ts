// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, it, expect, beforeEach, vi } from 'vitest';
import {
	battleLobbyUsernameForPlayer,
	getBattlePlayUsername,
	setBattlePlayUsername
} from './battle-guest';

describe('battle play username session', () => {
	const store: Record<string, string> = {};

	beforeEach(() => {
		for (const key of Object.keys(store)) delete store[key];
		vi.stubGlobal('sessionStorage', {
			getItem: (key: string) => store[key] ?? null,
			setItem: (key: string, value: string) => {
				store[key] = value;
			},
			removeItem: (key: string) => {
				delete store[key];
			},
			clear: () => {
				for (const key of Object.keys(store)) delete store[key];
			}
		});
	});

	it('stores and reads username by game pin', () => {
		setBattlePlayUsername('183310', 'HostAlpha');
		expect(getBattlePlayUsername('183310')).toBe('HostAlpha');
		expect(getBattlePlayUsername('999999')).toBeNull();
	});

	it('resolves lobby slot for guest player id', () => {
		const lobby = {
			battle_code: '1',
			quiz_id: 'q',
			host_user_id: 'h',
			max_players: 2,
			player_slots: [{ user_id: 'g1', username: 'GuestBeta' }],
			status: 'waiting',
			game_pin: null,
			game_id: null
		};
		expect(battleLobbyUsernameForPlayer(lobby, { guestPlayerId: 'g1' })).toBe('GuestBeta');
	});
});
