<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { socket } from './socket';
	import { QuizQuestionType } from '$lib/quiz_types';
	import Spinner from '$lib/Spinner.svelte';
	import Controls from '$lib/play/admin/controls.svelte';
	import Question from '$lib/play/admin/question.svelte';
	import { SocketGameControls } from '$lib/play/admin/socket_game_controls.ts';
	import type { IGameState } from '$lib/play/admin/game_state.ts';

	const { t } = getLocalization();
	import { LEDGER_ANSWER_COLORS } from '$lib/ui/tokens';
	import { formatQuestionTopicTag, resolveQuizContentLabels } from '$lib/cma/client';
	import QuestionIntro from '$lib/play/arena/QuestionIntro.svelte';
	import AnswerTiles from '$lib/play/arena/AnswerTiles.svelte';
	import RevealPhase from '$lib/play/arena/RevealPhase.svelte';
	import RankingsBoard from '$lib/play/arena/RankingsBoard.svelte';
	import HostProgress from '$lib/play/admin/host-progress.svelte';
	import HostTopBar from '$lib/play/admin/host-top-bar.svelte';
	import { normalizeQuizText } from '$lib/cma/text';
	import type { LedgerRow } from '$lib/ui/LedgerTable.svelte';
	import { isKahootStyleMode } from '$lib/play/live-game';
	import { applyQuestionResultScores } from '$lib/play/live-scoring';
	import {
		applyClockSync,
		parseQuestionTiming,
		remainingAnswerSeconds,
		resolveLivePhase,
		serverNowMs,
		type QuestionTiming
	} from '$lib/play/live-timing';

	const default_colors = [...LEDGER_ANSWER_COLORS];
	let cert_label = $state<string | null>(null);
	let topic_label = $state<string | null>(null);

	$effect(() => {
		const title = game_state.quiz_data?.title;
		if (!title) return;
		resolveQuizContentLabels(title).then((labels) => {
			cert_label = labels.certLabel;
			topic_label = labels.topicLabel;
		});
	});

	let final_results_clicked = $state(false);
	let timer_interval: NodeJS.Timeout;
	let livePhase = $state<'intro' | 'answer' | 'reveal' | 'rankings'>('answer');
	let revealTimer: ReturnType<typeof setTimeout> | undefined;
	let prevRanks: Record<string, number> = {};
	let lastScoreAppliedQuestionIndex: number | null = $state(null);
	let questionTiming = $state<QuestionTiming | null>(null);
	let clockOffsetMs = $state(0);

	interface Props {
		game_token: string;
		bg_color: string;
		game_state: IGameState;
	}

	let { game_token, bg_color, game_state = $bindable() }: Props = $props();

	socket.on('get_question_results', () => {
		console.log('get_question_results');
	});

	socket.on('clock_sync', (data: { server_time_ms?: number }) => {
		if (data?.server_time_ms != null) {
			clockOffsetMs = applyClockSync(Number(data.server_time_ms));
			syncHostClock();
		}
	});

	function syncHostClock() {
		if (!questionTiming) return;
		const now = serverNowMs(clockOffsetMs);
		livePhase = resolveLivePhase(questionTiming, game_state.quiz_data?.game_mode, now);
		const rem = Math.ceil(remainingAnswerSeconds(questionTiming, now));
		game_state.timer_res = String(rem);
	}

	socket.on('set_question_number', (data) => {
		game_state.timer_res = '0';
		game_state.question_results = null;
		game_state.shown_question_now = data.question_index;
		game_state.timer_res = game_state.quiz_data.questions[data.question_index].time;
		game_state.selected_question = data.question_index;
		game_state.answer_count = 0;
		const current = game_state.player_scores ?? {};
		prevRanks = Object.fromEntries(
			Object.keys(current)
				.sort(
					(a, b) =>
						(parseFloat(String(current[b])) || 0) - (parseFloat(String(current[a])) || 0)
				)
				.map((name, idx) => [name, idx + 1])
		);
		clearTimeout(revealTimer);
		const fallback = parseInt(game_state.quiz_data.questions[data.question_index].time) || 30;
		questionTiming = parseQuestionTiming(data, game_state.quiz_data?.game_mode, fallback);
		if (data?.server_time_ms != null) {
			clockOffsetMs = applyClockSync(Number(data.server_time_ms));
		}
		syncHostClock();
		clearInterval(timer_interval);
		timer_interval = setInterval(syncHostClock, 250);
	});

	socket.on('solutions', (_) => {
		game_state.timer_res = '0';
		clearInterval(timer_interval);
	});

	socket.on('final_results', (data) => {
		final_results_clicked = true;
		game_state.timer_res = '0';
		game_state.final_results = data;
	});

	socket.on('everyone_answered', (_) => {
		game_state.timer_res = '0';
	});

	socket.on('question_results', (data) => {
		game_state.question_results = data;
		game_state.timer_res = '0';
		if (Array.isArray(data)) {
			const applied = applyQuestionResultScores(
				game_state.player_scores ?? {},
				data,
				game_state.shown_question_now ?? game_state.selected_question,
				lastScoreAppliedQuestionIndex
			);
			game_state.player_scores = applied.scores;
			lastScoreAppliedQuestionIndex = applied.lastAppliedQuestionIndex;
		}
		livePhase = 'reveal';
		clearTimeout(revealTimer);
		revealTimer = setTimeout(() => {
			livePhase = 'rankings';
		}, 4500);
	});

	socket.on('player_answer', (_) => {
		game_state.answer_count += 1;
	});

	const socket_game_controls: SocketGameControls = new SocketGameControls(socket);

	let activeQ = $derived(
		game_state.selected_question >= 0
			? game_state.quiz_data?.questions?.[game_state.selected_question]
			: null
	);

	let hostDistribution = $derived.by(() => {
		const rows = game_state.question_results;
		if (!rows || !Array.isArray(rows) || !activeQ) return [];
		const counts: Record<string, number> = {};
		for (const r of rows) {
			const key = r.answer ?? '(blank)';
			counts[key] = (counts[key] ?? 0) + 1;
		}
		const answers = Array.isArray(activeQ.answers) ? activeQ.answers : [];
		return answers.map((a: { answer?: string; right?: boolean }) => ({
			answer: a.answer ?? '',
			count: counts[a.answer ?? ''] ?? 0,
			right: Boolean(a.right)
		}));
	});

	let hostKahootStyle = $derived(isKahootStyleMode(game_state.quiz_data?.game_mode));

	let rankingRows = $derived.by((): LedgerRow[] => {
		const scores = game_state.player_scores ?? {};
		return Object.keys(scores)
			.sort((a, b) => (parseFloat(String(scores[b])) || 0) - (parseFloat(String(scores[a])) || 0))
			.map((name, idx) => {
				const rank = idx + 1;
				const prev = prevRanks[name];
				return {
					rank,
					name,
					score: scores[name],
					delta: prev != null ? prev - rank : 0
				};
			});
	});
</script>

{#if game_state.control_visible}
	<Controls {bg_color} {socket_game_controls} {game_token} bind:game_state />
{/if}

<div class="w-full min-h-dvh bg-paper pb-28">
	{#if game_state.selected_question >= 0 && game_state.quiz_data}
		<HostTopBar
			current={game_state.selected_question + 1}
			total={game_state.quiz_data.questions.length}
			gamePin={game_state.quiz_data.game_pin}
		/>
	{/if}
	{#if game_state.timer_res !== undefined && !final_results_clicked && !game_state.question_results}
		{#if game_state.quiz_data.questions[game_state.selected_question].type === QuizQuestionType.SLIDE}
			{#await import('$lib/play/admin/slide.svelte')}
				<Spinner my_20={false} />
			{:then c}
				<c.default
					question={game_state.quiz_data.questions[game_state.selected_question]}
				/>
			{/await}
		{:else if hostKahootStyle && livePhase === 'intro' && activeQ}
			<QuestionIntro
				question={activeQ.question}
				topic={formatQuestionTopicTag(
					cert_label,
					topic_label,
					game_state.selected_question,
					game_state.quiz_data?.questions?.length
				)}
				onComplete={() => {
					syncHostClock();
				}}
			/>
		{:else if hostKahootStyle && activeQ}
			<AnswerTiles
				question={activeQ.question}
				answers={Array.isArray(activeQ.answers) ? activeQ.answers : []}
				remainingSeconds={parseInt(game_state.timer_res) || 0}
				totalSeconds={parseInt(activeQ.time) || 30}
				answeredCount={game_state.answer_count}
				showRing={false}
			/>
		{:else if activeQ}
			<HostProgress
				remainingSeconds={parseInt(game_state.timer_res) || 0}
				totalSeconds={parseInt(activeQ.time) || 30}
				answerCount={game_state.answer_count}
			/>
		{:else}
			<Question
				quiz_data={game_state.quiz_data}
				selected_question={game_state.selected_question}
				timer_res={game_state.timer_res}
				answer_count={game_state.answer_count}
				{default_colors}
				game_pin={game_state.quiz_data?.game_pin}
				topic_tag={formatQuestionTopicTag(
					cert_label,
					topic_label,
					game_state.selected_question,
					game_state.quiz_data?.questions?.length
				)}
			/>
		{/if}
	{/if}
	{#if game_state.timer_res === '0' && JSON.stringify(game_state.final_results) === JSON.stringify( [null] ) && game_state.quiz_data.questions[game_state.selected_question].type !== QuizQuestionType.SLIDE && game_state.question_results !== null && game_state.quiz_data.questions[game_state.selected_question]?.hide_results !== true}
		{#if game_state.question_results === undefined}
			{#if !final_results_clicked}
				<div class="w-full flex justify-center">
					<h1 class="text-3xl">{$t('admin_page.no_answers')}</h1>
				</div>
			{/if}
		{:else if game_state.quiz_data.questions[game_state.selected_question].type === QuizQuestionType.VOTING}
			{#await import('$lib/play/admin/voting_results.svelte')}
				<Spinner />
			{:then c}
				<c.default
					data={game_state.question_results}
					question={game_state.quiz_data.questions[game_state.selected_question]}
				/>
			{/await}
		{:else if livePhase === 'reveal' && activeQ}
			<RevealPhase
				question={activeQ.question}
				distribution={hostDistribution}
			/>
		{:else if livePhase === 'rankings'}
			<RankingsBoard rows={rankingRows} />
		{:else}
			{#await import('$lib/play/admin/results.svelte')}
				<Spinner />
			{:then c}
				<c.default
					bind:data={game_state.player_scores}
					question={game_state.quiz_data.questions[game_state.selected_question]}
					new_data={game_state.question_results}
				/>
			{/await}
		{/if}
	{/if}
	{#if game_state.selected_question === -1}
		<div class="flex flex-col justify-center w-screen min-h-dvh px-6">
			<p class="font-display text-gold text-sm tracking-[0.3em] text-center mb-4">Get ready</p>
			<h1 class="font-display text-6xl sm:text-7xl text-center">{@html normalizeQuizText(game_state.quiz_data.title)}</h1>
			<p class="text-xl pt-6 text-center text-ink-muted">{@html game_state.quiz_data.description}</p>
			{#if game_state.quiz_data.cover_image}
				<div class="flex justify-center align-middle items-center">
					<div class="h-[30vh] m-auto w-auto mt-12">
						<img
							class="max-h-full max-w-full block"
							src="/api/v1/storage/download/{game_state.quiz_data.cover_image}"
							alt="Not provided"
						/>
					</div>
				</div>
			{/if}
		</div>
	{/if}
</div>
