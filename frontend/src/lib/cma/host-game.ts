// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

export type StartGameResponse = {
	game_id: string;
	game_pin: string;
	cqc_code: string;
};

/** Start a live kahoot-style game from a quiz (requires sign-in). */
export async function startHostGame(quizId: string): Promise<StartGameResponse | 'auth' | 'error'> {
	const params = new URLSearchParams({
		captcha_enabled: 'False',
		game_mode: 'kahoot',
		custom_field: '',
		cqcs_enabled: 'False',
		randomize_answers: 'False'
	});
	const res = await fetch(`/api/v1/quiz/start/${quizId}?${params}`, {
		method: 'POST',
		credentials: 'include'
	});
	if (res.status === 401 || res.status === 403) {
		return 'auth';
	}
	if (!res.ok) {
		return 'error';
	}
	return (await res.json()) as StartGameResponse;
}

export function adminLobbyUrl(data: StartGameResponse): string {
	return `/admin?token=${data.game_id}&pin=${data.game_pin}&connect=1&cqc_code=${data.cqc_code}`;
}
