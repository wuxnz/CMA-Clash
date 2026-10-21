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

const { socketMock } = vi.hoisted(() => ({
	socketMock: {
		emit: vi.fn(),
		id: 'sid-1',
		on: vi.fn(),
		off: vi.fn(),
		connected: true,
		connect: vi.fn(),
		disconnect: vi.fn()
	}
}));

vi.mock('$lib/socket', () => ({
	socket: socketMock
}));

import {
	clearJoinedGameCookieIfPinMismatch,
	emitRejoinFromCookie,
	normalizePlayPin,
	preparePlaySessionForPin,
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
		cookieStore.joined_game = JSON.stringify({
			sid: 'a',
			username: 'OldHost',
			game_pin: '111111'
		});
		expect(emitRejoinFromCookie('222222')).toBe(false);
		expect(socketMock.emit).not.toHaveBeenCalled();
		expect(readJoinedGameCookie()).toBeNull();
	});

	it('preparePlaySessionForPin clears stale cookie without forcing reconnect', () => {
		cookieStore.joined_game = JSON.stringify({
			sid: 'a',
			username: 'OldHost',
			game_pin: '111111'
		});
		preparePlaySessionForPin('222222');
		expect(readJoinedGameCookie()).toBeNull();
		expect(socketMock.disconnect).not.toHaveBeenCalled();
	});
});
