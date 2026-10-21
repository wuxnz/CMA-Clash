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

export function resetPlaySocketBinding(): void {
	boundPlayPin = null;
}

export function isPlaySocketBoundToExpectedPin(): boolean {
	return (
		expectedPlayPin.length >= 6 &&
		boundPlayPin !== null &&
		boundPlayPin === expectedPlayPin
	);
}

export function getExpectedPlayPin(): string {
	return expectedPlayPin;
}
