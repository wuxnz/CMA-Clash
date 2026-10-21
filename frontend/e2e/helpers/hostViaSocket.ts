// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { io, type Socket } from 'socket.io-client';

const API_BASE = process.env.PLAYWRIGHT_API_BASE ?? 'https://cmaclash-api.onrender.com';

export type HostedLobby = {
	pin: string;
	gameId: string;
	socket: Socket;
	startGame: () => void;
	close: () => void;
};

export async function hostLiveGame(gameMode: 'kahoot' | 'normal'): Promise<HostedLobby> {
	const quizzes = await fetch(`${API_BASE}/api/v1/clash/quizzes?page_size=5`).then((r) => r.json());
	if (!Array.isArray(quizzes) || quizzes.length === 0) {
		throw new Error('no public quizzes');
	}
	const quizId = quizzes[0].id;
	const params = new URLSearchParams({
		captcha_enabled: 'False',
		game_mode: gameMode,
		custom_field: '',
		cqcs_enabled: 'False',
		randomize_answers: 'False'
	});
	const start = await fetch(`${API_BASE}/api/v1/quiz/start/${quizId}?${params}`, {
		method: 'POST'
	}).then((r) => r.json());
	const pin: string = start.game_pin;
	const gameId: string = start.game_id;

	const socket = io(API_BASE, { transports: ['websocket', 'polling'] });
	await new Promise<void>((resolve, reject) => {
		const timer = setTimeout(() => reject(new Error('admin socket connect timeout')), 45_000);
		socket.once('connect', () => {
			clearTimeout(timer);
			resolve();
		});
		socket.once('connect_error', (err) => {
			clearTimeout(timer);
			reject(err);
		});
	});

	await new Promise<void>((resolve, reject) => {
		const timer = setTimeout(() => reject(new Error('register_as_admin timeout')), 30_000);
		socket.once('registered_as_admin', () => {
			clearTimeout(timer);
			resolve();
		});
		socket.emit('register_as_admin', { game_pin: pin, game_id: gameId });
	});

	return {
		pin,
		gameId,
		socket,
		startGame: () => {
			socket.emit('start_game', {});
			// "On player devices" (normal) does not auto-push Q1; host must show it.
			if (gameMode === 'normal') {
				const showQ1 = () => socket.emit('set_question_number', '0');
				showQ1();
				setTimeout(showQ1, 1500);
			}
		},
		close: () => socket.disconnect()
	};
}
