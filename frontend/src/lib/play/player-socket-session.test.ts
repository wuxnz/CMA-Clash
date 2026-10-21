// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { beforeEach, describe, expect, it, vi } from 'vitest';

const cookieStore: Record<string, string> = {};

vi.mock('$lib/play/play-socket-debug', () => ({
	attachPlaySocketDebug: vi.fn()
}));

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

vi.mock('$lib/socket', () => ({
	socket: { emit: vi.fn(), id: 'sid-1', on: vi.fn(), off: vi.fn() }
}));

import {
	clearJoinedGameCookieIfPinMismatch,
	emitRejoinFromCookie,
	normalizePlayPin,
	readJoinedGameCookie
} from './player-socket-session';

describe('player socket session cookies', () => {
	beforeEach(() => {
		for (const key of Object.keys(cookieStore)) delete cookieStore[key];
	});

	it('normalizes pins to digits', () => {
		expect(normalizePlayPin('183-310')).toBe('183310');
	});

	it('clears cookie when URL pin differs from stored live game', () => {
		cookieStore.joined_game = JSON.stringify({
			sid: 'a',
			username: 'OldHost',
			game_pin: '111111'
		});
		expect(clearJoinedGameCookieIfPinMismatch('222222')).toBe(true);
		expect(readJoinedGameCookie()).toBeNull();
	});

	it('does not rejoin when fallback pin mismatches cookie', async () => {
		const { socket } = await import('$lib/socket');
		cookieStore.joined_game = JSON.stringify({
			sid: 'a',
			username: 'OldHost',
			game_pin: '111111'
		});
		expect(emitRejoinFromCookie('222222')).toBe(false);
		expect(socket.emit).not.toHaveBeenCalled();
	});
});
