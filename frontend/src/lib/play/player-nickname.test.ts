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
		id: 'sid-1',
		connected: true,
		connect: vi.fn(),
		disconnect: vi.fn(),
		on: vi.fn(),
		off: vi.fn()
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

import { persistJoinedGameCookie } from './player-socket-session';

describe('persistJoinedGameCookie nickname', () => {
	beforeEach(() => {
		for (const key of Object.keys(cookieStore)) delete cookieStore[key];
		for (const key of Object.keys(sessionStore)) delete sessionStore[key];
	});

	it('remembers the nickname for the PIN in a match, not only in battles', () => {
		persistJoinedGameCookie('Ada', '123456');

		expect(JSON.parse(cookieStore.joined_game).username).toBe('Ada');
		expect(sessionStore['cma_battle_play_username:123456']).toBe('Ada');
	});
});
