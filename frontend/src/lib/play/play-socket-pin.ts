// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

function normalizePlayPin(pin: string | undefined | null): string {
	return (pin ?? '').replace(/\D/g, '');
}

/** URL pin the /play page is showing; socket events apply only after a matching join. */
let expectedPlayPin = '';
let boundPlayPin: string | null = null;

export function setExpectedPlayPin(pin: string | undefined | null): void {
	expectedPlayPin = normalizePlayPin(pin);
	boundPlayPin = null;
}

export function markPlaySocketBound(pin: string | undefined | null): void {
	const normalized = normalizePlayPin(pin);
	if (normalized.length < 6 || normalized !== expectedPlayPin) {
		return;
	}
	boundPlayPin = normalized;
}

/**
 * Join flow: the player typed the PIN on /play (no ?pin= in the URL), so the page
 * never set an expected pin. Adopt the joined pin and bind the socket to it, otherwise
 * every set_question_number / question_results event is dropped by the guard.
 */
export function bindPlaySocketForJoin(pin: string | undefined | null): void {
	const normalized = normalizePlayPin(pin);
	if (normalized.length < 6) return;
	expectedPlayPin = normalized;
	boundPlayPin = normalized;
}

export function resetPlaySocketBinding(): void {
	boundPlayPin = null;
}

export function isPlaySocketBoundToExpectedPin(): boolean {
	return expectedPlayPin.length >= 6 && boundPlayPin !== null && boundPlayPin === expectedPlayPin;
}

export function getExpectedPlayPin(): string {
	return expectedPlayPin;
}
