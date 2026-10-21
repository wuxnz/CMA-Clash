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

const { socketMock } = vi.hoisted(() => {
	const listeners: Record<string, Array<() => void>> = {};
	return {
		socketMock: {
			emit: vi.fn(),
			id: 'sid-1',
			connected: false,
			connect: vi.fn(() => {
				socketMock.connected = true;
				for (const fn of listeners.connect ?? []) fn();
			}),
			disconnect: vi.fn(),
			on: vi.fn((event: string, fn: () => void) => {
				(listeners[event] ??= []).push(fn);
			}),
			off: vi.fn((event: string, fn: () => void) => {
				listeners[event] = (listeners[event] ?? []).filter((h) => h !== fn);
			}),
			_simulateConnect() {
				socketMock.connected = true;
				for (const fn of listeners.connect ?? []) fn();
			}
		},
		listeners
	};
});

vi.mock('$lib/socket', () => ({
	socket: socketMock
}));

import {
	clearJoinedGameCookieIfPinMismatch,
	emitRejoinFromCookie,
	normalizePlayPin,
	preparePlaySessionForPin,
	readJoinedGameCookie,
	waitForPlaySocketConnected
} from './player-socket-session';

describe('player socket session cookies', () => {
	beforeEach(() => {
		for (const key of Object.keys(cookieStore)) delete cookieStore[key];
		socketMock.connected = true;
		vi.clearAllMocks();
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

	it('waitForPlaySocketConnected resolves after connect event', async () => {
		socketMock.connected = false;
		const pending = waitForPlaySocketConnected(1000);
		socketMock._simulateConnect();
		await expect(pending).resolves.toBeUndefined();
		expect(socketMock.connect).toHaveBeenCalled();
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
		socketMock.connected = false;
		preparePlaySessionForPin('333333');
		expect(socketMock.connect).toHaveBeenCalled();
	});
});
