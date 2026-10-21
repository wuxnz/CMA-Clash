// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { browser } from '$app/environment';
import { socket } from '$lib/socket';

export type PlayPageSocketHandlers = {
	onTimeSync: (data: unknown) => void;
	onClockSync: (data: { server_time_ms?: number }) => void;
	onJoinedGame: (data: unknown) => void;
	onRejoinedGame: (data: unknown) => void;
	onGameNotFound: () => void;
	onQuestionTimesUp: () => void;
	onSetQuestionNumber: (data: Record<string, unknown>) => void;
	onStartGame: () => void;
	onJoinError: (payload?: { code?: string }) => void;
	onQuestionResults: (data: unknown) => void;
	onUsernameAlreadyExists: () => void;
	onKick: () => void;
	onFinalResults: (data: unknown) => void;
	onSolutions: (data: unknown) => void;
};

let activeHandlers: PlayPageSocketHandlers | null = null;
let installed = false;

const onTimeSync = (data: unknown) => activeHandlers?.onTimeSync(data);
const onClockSync = (data: { server_time_ms?: number }) => activeHandlers?.onClockSync(data);
const onJoinedGame = (data: unknown) => activeHandlers?.onJoinedGame(data);
const onRejoinedGame = (data: unknown) => activeHandlers?.onRejoinedGame(data);
const onGameNotFound = () => activeHandlers?.onGameNotFound();
const onQuestionTimesUp = () => activeHandlers?.onQuestionTimesUp();
const onSetQuestionNumber = (data: Record<string, unknown>) =>
	activeHandlers?.onSetQuestionNumber(data);
const onStartGame = () => activeHandlers?.onStartGame();
const onJoinError = (payload?: { code?: string }) => activeHandlers?.onJoinError(payload);
const onQuestionResults = (data: unknown) => activeHandlers?.onQuestionResults(data);
const onUsernameAlreadyExists = () => activeHandlers?.onUsernameAlreadyExists();
const onKick = () => activeHandlers?.onKick();
const onFinalResults = (data: unknown) => activeHandlers?.onFinalResults(data);
const onSolutions = (data: unknown) => activeHandlers?.onSolutions(data);

function installOnce(): void {
	if (!browser || installed) return;
	installed = true;
	socket.on('time_sync', onTimeSync);
	socket.on('clock_sync', onClockSync);
	socket.on('joined_game', onJoinedGame);
	socket.on('rejoined_game', onRejoinedGame);
	socket.on('game_not_found', onGameNotFound);
	socket.on('question_times_up', onQuestionTimesUp);
	socket.on('set_question_number', onSetQuestionNumber);
	socket.on('start_game', onStartGame);
	socket.on('join_error', onJoinError);
	socket.on('question_results', onQuestionResults);
	socket.on('username_already_exists', onUsernameAlreadyExists);
	socket.on('kick', onKick);
	socket.on('final_results', onFinalResults);
	socket.on('solutions', onSolutions);
}

/** Bind the visible /play page instance; socket listeners are registered once in the browser. */
export function bindPlayPageSocketHandlers(handlers: PlayPageSocketHandlers): void {
	installOnce();
	activeHandlers = handlers;
}

export function unbindPlayPageSocketHandlers(): void {
	if (activeHandlers === null) return;
	activeHandlers = null;
}
