// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

export type StartGameResponse = {
	game_id: string;
	game_pin: string;
	cqc_code: string;
};

export type StartGameOptions = {
	captcha_enabled?: boolean;
	game_mode?: string;
	custom_field?: string;
	cqcs_enabled?: boolean;
	randomize_answers?: boolean;
};

/** Start a live game from a public quiz (guest or signed-in). */
export async function startHostGame(
	quizId: string,
	options: StartGameOptions = {}
): Promise<StartGameResponse | 'auth' | 'error'> {
	const params = new URLSearchParams({
		captcha_enabled: options.captcha_enabled ? 'True' : 'False',
		game_mode: options.game_mode ?? 'kahoot',
		custom_field: options.custom_field ?? '',
		cqcs_enabled: options.cqcs_enabled ? 'True' : 'False',
		randomize_answers: options.randomize_answers ? 'True' : 'False'
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
