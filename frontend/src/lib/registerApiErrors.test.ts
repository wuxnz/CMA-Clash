// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it } from 'vitest';
import {
	registerConflictFromResponse,
	registerConflictMessage
} from './registerApiErrors';

describe('registerConflictFromResponse', () => {
	it('maps username_taken', () => {
		expect(registerConflictFromResponse(409, 'username_taken')).toBe('username');
	});

	it('maps email_taken', () => {
		expect(registerConflictFromResponse(409, 'email_taken')).toBe('email');
	});
});

describe('registerConflictMessage', () => {
	it('uses plain copy for username', () => {
		expect(registerConflictMessage('username')).toBe('That username is taken.');
	});
});
