<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<!--suppress ALL -->
<script lang="ts">
	import { socket } from '$lib/socket';
	import JoinGame from '$lib/play/join.svelte';
	import type { Question as QuestionType } from '$lib/quiz_types';
	import ShowTitle from '$lib/play/title.svelte';
	import Question from '$lib/play/question.svelte';
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import ShowEndScreen from '$lib/play/admin/final_results.svelte';
	import KahootResults from '$lib/play/results_kahoot.svelte';
	import { getLocalization } from '$lib/i18n';
	import Cookies from 'js-cookie';
	import { formatQuestionTopicTag, resolveQuizContentLabels } from '$lib/cma/client';
	import QuestionIntro from '$lib/play/arena/QuestionIntro.svelte';
	import AnswerTiles from '$lib/play/arena/AnswerTiles.svelte';
	import RevealPhase from '$lib/play/arena/RevealPhase.svelte';
	import RankingsBoard from '$lib/play/arena/RankingsBoard.svelte';
	import type { LedgerRow } from '$lib/ui/LedgerTable.svelte';
	import { joinErrorMessage } from '$lib/play/join-errors';
	import {
		hasActiveQuestion,
		hasChoiceTileAnswers,
		initialLivePhaseForQuestion,
		isKahootStyleMode,
		normalizeGameMode,
		normalizeGamePayload,
		parseQuestionResultsPayload,
		isStaleQuestionResults,
		questionFromSocketPayload
	} from '$lib/play/live-game';
	import { applyQuestionResultScores, scoreDeltaForUser } from '$lib/play/live-scoring';
	import {
		applyClockSync,
		parseQuestionTiming,
		remainingAnswerSeconds,
		remainingIntroSeconds,
		resolveLivePhase,
		serverNowMs,
		totalAnswerSeconds,
		type QuestionTiming
	} from '$lib/play/live-timing';
	import {
		clearJoinedGameCookieIfPinMismatch,
		ensurePlaySocketSession,
		emitRejoinFromCookie,
		normalizePlayPin,
		persistJoinedGameCookie
	} from '$lib/play/player-socket-session';
	import { getBattlePlayUsername } from '$lib/cma/battle-guest';
	import {
		bindPlayPageSocketHandlers,
		unbindPlayPageSocketHandlers
	} from '$lib/play/play-page-socket';
	import { browser } from '$app/environment';
	import { onDestroy, onMount } from 'svelte';
	const { t } = getLocalization();

	interface Props {
		data: any;
	}

	let { data }: Props = $props();
	let game_pin = $state(data.game_pin ?? '');
	let playSessionPin = $state('');

	function resetPlayStateForPin(pin: string) {
		game_pin = pin;
		playSessionPin = pin;
		gameData = undefined;
		gameMeta.started = false;
		question_index = null;
		answer_results = undefined;
		question = undefined;
		solution = undefined;
		scores = {};
		final_results = [null];
		username = getBattlePlayUsername(pin) ?? '';
		lastScoreAppliedQuestionIndex = null;
		latestQuestionIndex = -1;
	}

	$effect(() => {
		if (!browser) return;
		const urlPin = normalizePlayPin(data.game_pin);
		if (urlPin.length < 6) return;
		clearJoinedGameCookieIfPinMismatch(urlPin);
		if (urlPin !== normalizePlayPin(playSessionPin)) {
			resetPlayStateForPin(urlPin);
		}
	});

	interface GameMeta {
		started: boolean;
	}

	interface PlayerAnswer {
		username: string;
		answer: string;
		right: boolean | string;
		score?: number;
		time_taken?: number;
	}

	// State (declare before $derived that references these — SSR TDZ)
	let question_index: number | null = $state(null);
	let unique = $state({});
	let answer_results: Array<PlayerAnswer> | undefined = $state();
	let gameData: any = $state();
	let solution: QuestionType = $state();
	let username = $state('');
	let scores = $state({});
	let game_mode = $state();
	ensurePlaySocketSession({
		getGamePin: () => game_pin,
		onReconnected: async () => {
			if (!game_pin) return;
			const res = await fetch(`/api/v1/quiz/play/check_captcha/${game_pin}`);
			const json = await res.json();
			game_mode = normalizeGameMode(json.game_mode) ?? json.game_mode;
		}
	});
	let final_results: Array<null> | Array<Array<PlayerAnswer>> = $state([null]);
	let gameMeta: GameMeta = $state({
		started: false
	});
	let question: QuestionType = $state();
	let livePhase = $state<'intro' | 'answer' | 'reveal' | 'rankings'>('answer');
	let revealTimer: ReturnType<typeof setTimeout> | undefined;
	let advanceSyncTimer: ReturnType<typeof setTimeout> | undefined;
	const ADVANCE_RESYNC_MS = 7500;

	function clearAdvanceResyncTimer() {
		if (advanceSyncTimer !== undefined) {
			clearTimeout(advanceSyncTimer);
			advanceSyncTimer = undefined;
		}
	}

	function scheduleAdvanceResync(closedQuestionIndex: number | null) {
		clearAdvanceResyncTimer();
		if (closedQuestionIndex == null || !Number.isFinite(closedQuestionIndex)) {
			return;
		}
		advanceSyncTimer = setTimeout(() => {
			if (answer_results === undefined) {
				return;
			}
			if (latestQuestionIndex > closedQuestionIndex) {
				return;
			}
			const cookie_data = Cookies.get('joined_game');
			if (!cookie_data || !socket.connected) {
				return;
			}
			emitRejoinFromCookie(game_pin);
		}, ADVANCE_RESYNC_MS);
	}
	let selectedAnswer = $state<string | undefined>(undefined);
	let remainingLive = $state(30);
	let questionTiming = $state<QuestionTiming | null>(null);
	let clockOffsetMs = $state(0);
	let streak = $state(0);
	let prevRanks: Record<string, number> = {};
	let lastScoreAppliedQuestionIndex: number | null = $state(null);
	let latestQuestionIndex = $state(-1);
	let pointsThisRound = $state(0);

	let cert_label = $state<string | null>(null);
	let topic_label = $state<string | null>(null);

	navbarVisible.visible = false;

	$effect(() => {
		const title = gameData?.title;
		if (!title) return;
		resolveQuizContentLabels(title).then((labels) => {
			cert_label = labels.certLabel;
			topic_label = labels.topicLabel;
		});
	});

	let topic_tag = $derived(
		hasActiveQuestion(question_index) && gameData
			? formatQuestionTopicTag(
					cert_label,
					topic_label,
					Number(question_index),
					gameData.question_count
				)
			: ''
	);

	let preventReload = true;

	// Functions
	function restart() {
		unique = {};
	}

	const confirmUnload = (event: Event) => {
		if (preventReload) {
			event.preventDefault();
			// eslint-disable-next-line @typescript-eslint/ban-ts-comment
			// @ts-ignore
			event.returnValue = '';
		}
	};

	function syncPlayerClock() {
		if (!questionTiming || answer_results !== undefined) return;
		const now = serverNowMs(clockOffsetMs);
		livePhase = resolveLivePhase(questionTiming, game_mode, now);
		remainingLive = Math.ceil(remainingAnswerSeconds(questionTiming, now));
	}

	function applyQuestionSocketData(data: Record<string, unknown>) {
		const fallbackSec = parseInt(String((data.question as { time?: string })?.time ?? 30)) || 30;
		questionTiming = parseQuestionTiming(data, game_mode, fallbackSec);
		if (data.server_time_ms != null) {
			clockOffsetMs = applyClockSync(Number(data.server_time_ms));
		}
		syncPlayerClock();
	}

	function handleSetQuestionNumber(data: Record<string, unknown>) {
		const nextIndex = Number(data.question_index);
		if (Number.isFinite(nextIndex) && latestQuestionIndex > nextIndex) {
			return;
		}
		if (Number.isFinite(nextIndex)) {
			latestQuestionIndex = nextIndex;
		}
		solution = undefined;
		restart();
		question = questionFromSocketPayload(data);
		question_index = Number.isFinite(nextIndex) ? nextIndex : data.question_index;
		answer_results = undefined;
		selectedAnswer = undefined;
		pointsThisRound = 0;
		clearTimeout(revealTimer);
		clearAdvanceResyncTimer();
		prevRanks = Object.fromEntries(
			Object.keys(scores)
				.sort(
					(a, b) =>
						(parseFloat(String(scores[b])) || 0) - (parseFloat(String(scores[a])) || 0)
				)
				.map((name, idx) => [name, idx + 1])
		);
		applyQuestionSocketData(data);
		syncPlayerClock();
		const introLeft =
			questionTiming != null
				? Math.ceil(remainingIntroSeconds(questionTiming, serverNowMs(clockOffsetMs)))
				: 0;
		livePhase = initialLivePhaseForQuestion(game_mode, introLeft);
		if (!gameMeta.started) {
			gameMeta.started = true;
		}
	}

	function handleQuestionResults(data: unknown) {
		const { questionIndex: resultsIndex, rows } = parseQuestionResultsPayload(data);
		if (
			isStaleQuestionResults(question_index, resultsIndex, latestQuestionIndex) ||
			rows.length === 0
		) {
			return;
		}
		restart();
		answer_results = rows as PlayerAnswer[];
		pointsThisRound = scoreDeltaForUser(rows, username);
		const scoreIndex = resultsIndex ?? question_index;
		const applied = applyQuestionResultScores(
			scores,
			rows,
			scoreIndex,
			lastScoreAppliedQuestionIndex
		);
		scores = applied.scores;
		lastScoreAppliedQuestionIndex = applied.lastAppliedQuestionIndex;
		const mine = rows.find((r) => r.username === username);
		const right =
			mine?.right === true || mine?.right === 'true' || mine?.right === 1;
		streak = right ? streak + 1 : 0;
		livePhase = 'reveal';
		clearTimeout(revealTimer);
		revealTimer = setTimeout(() => {
			livePhase = 'rankings';
		}, 4500);
		scheduleAdvanceResync(resultsIndex ?? (typeof question_index === 'number' ? question_index : null));
	}

	onMount(() => {
		bindPlayPageSocketHandlers({
			onTimeSync: (data) => {
				socket.emit('echo_time_sync', data);
			},
			onClockSync: (data) => {
				if (data?.server_time_ms != null) {
					clockOffsetMs = applyClockSync(Number(data.server_time_ms));
					syncPlayerClock();
				}
			},
			onJoinedGame: (data) => {
				gameData = normalizeGamePayload(data);
				if (gameData?.started) {
					gameMeta.started = true;
				}
				if (gameData?.game_mode != null) {
					game_mode = normalizeGameMode(gameData.game_mode) ?? gameData.game_mode;
				}
				// eslint-disable-next-line no-undef
				plausible('Joined Game', { props: { game_id: gameData?.game_id } });
				persistJoinedGameCookie(username, game_pin);
			},
			onRejoinedGame: (data) => {
				gameData = normalizeGamePayload(data);
				if (gameData?.started) {
					gameMeta.started = true;
				}
				if (gameData?.game_mode != null) {
					game_mode = normalizeGameMode(gameData.game_mode) ?? gameData.game_mode;
				}
				if (username && game_pin) {
					persistJoinedGameCookie(username, game_pin);
				}
			},
			onGameNotFound: () => {
				const cookie_data = Cookies.get('joined_game');
				if (cookie_data) {
					Cookies.remove('joined_game');
					window.location.reload();
				}
			},
			onQuestionTimesUp: () => {
				remainingLive = 0;
			},
			onSetQuestionNumber: handleSetQuestionNumber,
			onStartGame: () => {
				gameMeta.started = true;
			},
			onJoinError: (payload) => {
				if (payload?.code === 'game_already_started' && game_mode !== 'battle') {
					window.alert(joinErrorMessage(payload.code));
				}
			},
			onQuestionResults: handleQuestionResults,
			onUsernameAlreadyExists: () => {
				window.alert('Username already exists!');
			},
			onKick: () => {
				window.alert('You got kicked');
				preventReload = false;
				game_pin = '';
				username = '';
				Cookies.set('kicked', 'value', { expires: 1 });
				window.location.reload();
			},
			onFinalResults: (data) => {
				final_results = data;
				Cookies.remove('joined_game');
			},
			onSolutions: (data) => {
				solution = data;
			}
		});
	});

	onDestroy(() => {
		unbindPlayPageSocketHandlers();
	});

	let bg_color = $derived(gameData ? gameData.background_color : undefined);

	let playerMine = $derived(
		Array.isArray(answer_results)
			? answer_results.find((r) => r.username === username)
			: undefined
	);

	let playerDistribution = $derived.by(() => {
		if (!question?.answers || !Array.isArray(answer_results)) return [];
		const counts: Record<string, number> = {};
		for (const r of answer_results) {
			const key = r.answer ?? '(blank)';
			counts[key] = (counts[key] ?? 0) + 1;
		}
		const answers = Array.isArray(question.answers) ? question.answers : [];
		return answers.map((a: { answer?: string; right?: boolean }) => ({
			answer: a.answer ?? '',
			count: counts[a.answer ?? ''] ?? 0,
			right: Boolean(a.right)
		}));
	});

	let rankingRows = $derived.by((): LedgerRow[] => {
		const names = Object.keys(scores).sort(
			(a, b) => (parseFloat(String(scores[b])) || 0) - (parseFloat(String(scores[a])) || 0)
		);
		return names.map((name, idx) => {
			const rank = idx + 1;
			const prev = prevRanks[name];
			return {
				rank,
				name: name === username ? 'You' : name,
				score: scores[name],
				isYou: name === username,
				delta: prev != null ? prev - rank : 0
			};
		});
	});

	$effect(() => {
		if (!questionTiming) return;
		const id = setInterval(() => syncPlayerClock(), 250);
		return () => clearInterval(id);
	});

	function pickAnswer(answer: string) {
		selectedAnswer = answer;
		if (typeof navigator !== 'undefined' && navigator.vibrate) {
			navigator.vibrate(12);
		}
		socket.emit('submit_answer', {
			question_index: question_index,
			answer
		});
	}

	function isRightFlag(value: unknown): boolean | null {
		if (value == null) return null;
		if (value === true || value === 1 || value === 'true' || value === '1') return true;
		if (value === false || value === 0 || value === 'false' || value === '0') return false;
		return Boolean(value);
	}

	let remainingTime = $derived(
		questionTiming
			? Math.ceil(totalAnswerSeconds(questionTiming))
			: parseInt(String((question as any)?.time ?? 30)) || 30
	);
</script>

<svelte:window onbeforeunload={confirmUnload} />
<svelte:head>
	<title>CMA Clash: Play</title>
</svelte:head>
<div
	class="min-h-screen min-w-full bg-paper"
	style={bg_color ? `background: ${bg_color}` : undefined}
	class:text-ink={bg_color}
>
	<div>
		{#if !gameMeta.started && gameData === undefined}
			<JoinGame bind:game_pin bind:game_mode bind:username />
		{:else if JSON.stringify(final_results) !== JSON.stringify([null])}
			<ShowEndScreen bind:data={scores} show_final_results={true} {username} />
		{:else if gameData !== undefined && !hasActiveQuestion(question_index)}
			<ShowTitle
				title={gameData.title}
				description={gameData.description}
				cover_image={gameData.cover_image}
			/>
		{:else if gameMeta.started && gameData !== undefined && hasActiveQuestion(question_index) && answer_results === undefined}
			{#if livePhase === 'intro' && question && !isKahootStyleMode(game_mode)}
				<QuestionIntro
					question={question.question}
					topic={topic_tag}
					onComplete={() => {
						syncPlayerClock();
					}}
				/>
			{:else if hasChoiceTileAnswers(question)}
				<AnswerTiles
					question={question.question}
					answers={Array.isArray(question.answers) ? question.answers : []}
					remainingSeconds={remainingLive}
					totalSeconds={remainingTime}
					interactive={true}
					showRing={false}
					hideQuestion={isKahootStyleMode(game_mode)}
					selected={selectedAnswer}
					onSelect={pickAnswer}
				/>
			{:else}
				{#key unique}
					<div class="text-ink">
						<Question
							bind:game_mode
							bind:question
							{question_index}
							{solution}
							{topic_tag}
							serverRemainingSeconds={remainingLive}
						/>
					</div>
				{/key}
			{/if}
		{:else if gameMeta.started && answer_results !== undefined}
			{#if answer_results === null}
				<div class="w-full flex justify-center">
					<h1 class="text-3xl">{$t('admin_page.no_answers')}</h1>
				</div>
			{:else if livePhase === 'reveal' && question}
				<RevealPhase
					question={question.question}
					distribution={playerDistribution}
					isPlayer={true}
					correct={isRightFlag(playerMine?.right)}
					points={pointsThisRound}
					{streak}
				/>
			{:else if livePhase === 'rankings'}
				<RankingsBoard rows={rankingRows} />
			{:else}
				{#key unique}
					<KahootResults
						{username}
						question_results={answer_results}
						bind:scores
						{question}
					/>
				{/key}
			{/if}
		{/if}
	</div>
</div>
