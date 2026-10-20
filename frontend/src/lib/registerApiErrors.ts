// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

export type RegisterConflictField = 'email' | 'username';

export function registerConflictFromResponse(status: number, detail: unknown): RegisterConflictField | null {
	if (status !== 409) {
		return null;
	}
	if (detail === 'email_taken') {
		return 'email';
	}
	if (detail === 'username_taken') {
		return 'username';
	}
	return null;
}

export function registerConflictMessage(field: RegisterConflictField): string {
	if (field === 'username') {
		return 'That username is taken.';
	}
	return 'An account with that email already exists.';
}
