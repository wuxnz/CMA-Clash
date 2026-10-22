// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

/** Palette-specific shortcuts must not intercept keys while the palette is closed. */
export function paletteShortcutActive(open: boolean): boolean {
	return open;
}

export function applyPaletteTabAutocomplete(
	open: boolean,
	event: Pick<KeyboardEvent, 'preventDefault'>,
	bgText: string,
	setInput: (_value: string) => void
): void {
	if (!paletteShortcutActive(open)) {
		return;
	}
	event.preventDefault();
	setInput(bgText);
}
