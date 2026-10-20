// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { describe, expect, it, vi } from 'vitest';
import { applyPaletteTabAutocomplete, paletteShortcutActive } from './commandPaletteKeys';

describe('paletteShortcutActive', () => {
	it('is inactive when the palette is closed', () => {
		expect(paletteShortcutActive(false)).toBe(false);
	});

	it('is active when the palette is open', () => {
		expect(paletteShortcutActive(true)).toBe(true);
	});
});

describe('applyPaletteTabAutocomplete', () => {
	it('does not prevent Tab when the palette is closed (forms keep default tab order)', () => {
		const preventDefault = vi.fn();
		const setInput = vi.fn();
		applyPaletteTabAutocomplete(false, { preventDefault }, 'suggestion', setInput);
		expect(preventDefault).not.toHaveBeenCalled();
		expect(setInput).not.toHaveBeenCalled();
	});

	it('autocompletes and prevents Tab when the palette is open', () => {
		const preventDefault = vi.fn();
		const setInput = vi.fn();
		applyPaletteTabAutocomplete(true, { preventDefault }, '/dash', setInput);
		expect(preventDefault).toHaveBeenCalledOnce();
		expect(setInput).toHaveBeenCalledWith('/dash');
	});
});
