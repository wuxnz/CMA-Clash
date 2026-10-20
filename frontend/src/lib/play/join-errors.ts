// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

export function joinErrorMessage(code: string | undefined): string {
	switch (code) {
		case 'captcha_failed':
			return 'Captcha verification failed. Refresh and try again.';
		case 'game_already_started':
			return 'This game already started. You can no longer join the lobby.';
		case 'username_taken':
			return 'That nickname is already taken. Pick another.';
		case 'invalid_payload':
			return 'Could not join. Check your nickname and try again.';
		case 'not_connected':
			return 'Not connected to the game server yet. Wait a moment and retry.';
		default:
			return 'Could not join the game. Check your connection and try again.';
	}
}
