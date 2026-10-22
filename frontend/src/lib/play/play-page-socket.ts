// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { browser } from '$app/environment';
import { socket } from '$lib/socket';
import { isPlaySocketBoundToExpectedPin } from '$lib/play/play-socket-pin';

export type PlayPageSocketHandlers = {
	onTimeSync: (_data: unknown) => void;
	onClockSync: (_data: { server_time_ms?: number }) => void;
	onJoinedGame: (_data: unknown) => void;
	onRejoinedGame: (_data: unknown) => void;
	onGameNotFound: () => void;
	onQuestionTimesUp: () => void;
	onSetQuestionNumber: (_data: Record<string, unknown>) => void;
	onStartGame: () => void;
	onJoinError: (_payload?: { code?: string }) => void;
	onQuestionResults: (_data: unknown) => void;
	onUsernameAlreadyExists: () => void;
	onKick: () => void;
	onFinalResults: (_data: unknown) => void;
	onSolutions: (_data: unknown) => void;
};

let activeHandlers: PlayPageSocketHandlers | null = null;
let installed = false;

function guard<T extends (..._args: never[]) => void>(fn: T): T {
	return ((...args: Parameters<T>) => {
		if (!isPlaySocketBoundToExpectedPin()) return;
		fn(...args);
	}) as T;
}

const onTimeSync = (data: unknown) => activeHandlers?.onTimeSync(data);
const onClockSync = (data: { server_time_ms?: number }) => activeHandlers?.onClockSync(data);
const onJoinedGame = (data: unknown) => activeHandlers?.onJoinedGame(data);
const onRejoinedGame = (data: unknown) => activeHandlers?.onRejoinedGame(data);
const onGameNotFound = () => activeHandlers?.onGameNotFound();
const onQuestionTimesUp = guard(() => activeHandlers?.onQuestionTimesUp());
const onSetQuestionNumber = guard((data: Record<string, unknown>) =>
	activeHandlers?.onSetQuestionNumber(data)
);
const onStartGame = guard(() => activeHandlers?.onStartGame());
const onJoinError = (payload?: { code?: string }) => activeHandlers?.onJoinError(payload);
const onQuestionResults = guard((data: unknown) => activeHandlers?.onQuestionResults(data));
const onUsernameAlreadyExists = () => activeHandlers?.onUsernameAlreadyExists();
const onKick = () => activeHandlers?.onKick();
const onFinalResults = (data: unknown) => activeHandlers?.onFinalResults(data);
const onSolutions = guard((data: unknown) => activeHandlers?.onSolutions(data));

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
