// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { beforeEach, describe, expect, it, vi } from 'vitest';

const cookieStore: Record<string, string> = {};
const sessionStore: Record<string, string> = {};

vi.mock('js-cookie', () => ({
	default: {
		get: (key: string) => cookieStore[key] ?? undefined,
		set: (key: string, value: string) => {
			cookieStore[key] = value;
		},
		remove: (key: string) => {
			delete cookieStore[key];
		}
	}
}));

vi.mock('$lib/play/play-socket-debug', () => ({
	attachPlaySocketDebug: vi.fn()
}));

vi.mock('$lib/socket', () => ({
	socket: {
		emit: vi.fn(),
		connected: true,
		connect: vi.fn(),
		disconnect: vi.fn()
	}
}));

vi.stubGlobal('sessionStorage', {
	getItem: (key: string) => sessionStore[key] ?? null,
	setItem: (key: string, value: string) => {
		sessionStore[key] = value;
	},
	removeItem: (key: string) => {
		delete sessionStore[key];
	}
});

import { prepareBattlePlayHandoff } from './battle-play-handoff';
import { getBattlePlayUsername } from './battle-guest';

describe('prepareBattlePlayHandoff', () => {
	beforeEach(() => {
		for (const key of Object.keys(cookieStore)) delete cookieStore[key];
		for (const key of Object.keys(sessionStore)) delete sessionStore[key];
	});

	it('clears joined_game and stores battle nickname for the new pin', () => {
		cookieStore.joined_game = JSON.stringify({
			sid: 'stale',
			username: 'OldLiveHost',
			game_pin: '111111'
		});
		const lobby = {
			battle_code: '99',
			quiz_id: 'q',
			status: 'started',
			game_pin: '624620',
			player_slots: [{ username: 'HostAlpha', user_id: 'u1' }]
		};
		const pin = prepareBattlePlayHandoff(lobby, { userId: 'u1' });
		expect(pin).toBe('624620');
		expect(cookieStore.joined_game).toBeUndefined();
		expect(getBattlePlayUsername('624620')).toBe('HostAlpha');
	});
});
