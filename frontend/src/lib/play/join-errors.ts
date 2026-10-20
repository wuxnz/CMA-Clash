// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

export function joinErrorMessage(code: string | undefined): string {
	switch (code) {
		case 'captcha_failed':
			return 'Captcha verification failed. Refresh and try again.';
		case 'game_already_started':
			return 'This live quiz already started — late join is not allowed. Ask the host for a new game PIN.';
		case 'username_taken':
			return 'That nickname is already taken. Pick another.';
		case 'invalid_payload':
			return 'Could not join — check your nickname and try again.';
		case 'not_connected':
			return 'Not connected to the game server yet. Wait a moment and retry.';
		default:
			return 'Could not join the game. Check your connection and try again.';
	}
}
