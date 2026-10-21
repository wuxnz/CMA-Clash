// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it, vi } from 'vitest';

/** Minimal socket.io-style emitter (off w/o fn clears all listeners for that event). */
function miniSocketEmitter() {
	const map = new Map<string, Set<(...args: unknown[]) => void>>();
	return {
		on(event: string, fn: (...args: unknown[]) => void) {
			if (!map.has(event)) map.set(event, new Set());
			map.get(event)!.add(fn);
		},
		off(event: string, fn?: (...args: unknown[]) => void) {
			if (!fn) {
				map.delete(event);
				return;
			}
			map.get(event)?.delete(fn);
		},
		emit(event: string) {
			for (const fn of map.get(event) ?? []) fn();
		}
	};
}

/**
 * Documents socket.io-client behavior: off(event) without a listener removes ALL handlers.
 * join.svelte must always pass the same function reference to off().
 */
describe('socket.io off() semantics', () => {
	it('off(event) without listener removes every handler for that event', () => {
		const emitter = miniSocketEmitter();
		const pageHandler = vi.fn();
		const joinHandler = vi.fn();
		emitter.on('connect', pageHandler);
		emitter.on('connect', joinHandler);
		emitter.off('connect');
		emitter.emit('connect');
		expect(pageHandler).not.toHaveBeenCalled();
		expect(joinHandler).not.toHaveBeenCalled();
	});

	it('off(event, fn) removes only that handler', () => {
		const emitter = miniSocketEmitter();
		const pageHandler = vi.fn();
		const joinHandler = vi.fn();
		emitter.on('connect', pageHandler);
		emitter.on('connect', joinHandler);
		emitter.off('connect', joinHandler);
		emitter.emit('connect');
		expect(pageHandler).toHaveBeenCalledTimes(1);
		expect(joinHandler).not.toHaveBeenCalled();
	});
});
