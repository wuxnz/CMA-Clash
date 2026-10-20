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
	const { t } = getLocalization();

	interface Props {
		data: any;
	}

	let { data }: Props = $props();
	let game_pin = $state(data.game_pin ?? '');

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
	let question_index = $state('');
	let unique = $state({});
	let answer_results: Array<PlayerAnswer> | undefined = $state();
	let gameData: any = $state();
	let solution: QuestionType = $state();
	let username = $state('');
	let scores = $state({});
	let game_mode = $state();
	let final_results: Array<null> | Array<Array<PlayerAnswer>> = $state([null]);
	let gameMeta: GameMeta = $state({
		started: false
	});
	let question: QuestionType = $state();
	let livePhase = $state<'intro' | 'answer' | 'reveal' | 'rankings'>('answer');
	let introTimer: ReturnType<typeof setTimeout> | undefined;
	let revealTimer: ReturnType<typeof setTimeout> | undefined;
	let selectedAnswer = $state<string | undefined>(undefined);
	let remainingLive = $state(30);
	let streak = $state(0);
	let prevRanks: Record<string, number> = {};

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
		question_index !== '' && gameData
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

	socket.on('time_sync', (data) => {
		socket.emit('echo_time_sync', data);
	});

	socket.on('connect', async () => {
		console.log('Connected!');
		const cookie_data = Cookies.get('joined_game');
		if (!cookie_data) {
			return;
		}
		const data = JSON.parse(cookie_data);
		socket.emit('rejoin_game', {
			old_sid: data.sid,
			username: data.username,
			game_pin: data.game_pin
		});
		const res = await fetch(`/api/v1/quiz/play/check_captcha/${game_pin}`);
		const json = await res.json();
		game_mode = json.game_mode;
	});

	// Socket-events
	socket.on('joined_game', (data) => {
		gameData = data;
		if (data.started) {
			gameMeta.started = true;
		}
		// eslint-disable-next-line no-undef
		plausible('Joined Game', { props: { game_id: gameData.game_id } });
		Cookies.set('joined_game', JSON.stringify({ sid: socket.id, username, game_pin }), {
			expires: 3600
		});
	});
	socket.on('rejoined_game', (data) => {
		gameData = data;
		if (data.started) {
			gameMeta.started = true;
		}
	});

	socket.on('game_not_found', () => {
		const cookie_data = Cookies.get('joined_game');
		if (cookie_data) {
			Cookies.remove('joined_game');
			window.location.reload();
			return;
		}
	});

	function syncRemainingFromServer(data: { question_started_at?: string; question?: { time?: unknown } }) {
		const total = parseInt(String(data.question?.time ?? 30)) || 30;
		if (data.question_started_at) {
			const elapsed = (Date.now() - new Date(data.question_started_at).getTime()) / 1000;
			const introLeft = Math.max(0, 3.5 - elapsed);
			if (introLeft > 0) {
				remainingLive = total;
				return { introLeft };
			}
			remainingLive = Math.max(0, Math.ceil(total - (elapsed - 3.5)));
			return { introLeft: 0 };
		}
		remainingLive = total;
		return { introLeft: 3.5 };
	}

	socket.on('set_question_number', (data) => {
		solution = undefined;
		restart();
		question = data.question;
		question_index = data.question_index;
		answer_results = undefined;
		selectedAnswer = undefined;
		prevRanks = Object.fromEntries(
			Object.keys(scores)
				.sort(
					(a, b) =>
						(parseFloat(String(scores[b])) || 0) - (parseFloat(String(scores[a])) || 0)
				)
				.map((name, idx) => [name, idx + 1])
		);
		clearTimeout(introTimer);
		clearTimeout(revealTimer);
		const { introLeft } = syncRemainingFromServer(data);
		livePhase = introLeft > 0 ? 'intro' : 'answer';
		if (introLeft > 0) {
			introTimer = setTimeout(() => {
				livePhase = 'answer';
			}, introLeft * 1000);
		}
		if (!gameMeta.started) {
			gameMeta.started = true;
		}
	});

	socket.on('start_game', () => {
		gameMeta.started = true;
	});

	socket.on('join_error', (payload?: { code?: string }) => {
		if (payload?.code === 'game_already_started' && game_mode !== 'battle') {
			window.alert(
				'This game already started — you can no longer join the lobby. Ask the host for a new PIN.'
			);
		}
	});

	socket.on('question_results', (data) => {
		restart();
		answer_results = data;
		if (Array.isArray(data)) {
			const next = { ...scores };
			for (const row of data) {
				const name = row?.username;
				if (!name) continue;
				next[name] = (Number(next[name]) || 0) + (Number(row.score) || 0);
			}
			scores = next;
			const mine = data.find((r) => r.username === username);
			const right =
				mine?.right === true || mine?.right === 'true' || mine?.right === 1;
			streak = right ? streak + 1 : 0;
		}
		livePhase = 'reveal';
		clearTimeout(revealTimer);
		revealTimer = setTimeout(() => {
			livePhase = 'rankings';
		}, 4500);
	});

	socket.on('username_already_exists', () => {
		window.alert('Username already exists!');
	});

	socket.on('kick', () => {
		window.alert('You got kicked');
		preventReload = false;
		game_pin = '';
		username = '';
		Cookies.set('kicked', 'value', { expires: 1 });
		window.location.reload();
	});
	socket.on('final_results', (data) => {
		final_results = data;
		Cookies.remove('joined_game');
	});

	socket.on('solutions', (data) => {
		solution = data;
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
		if (livePhase !== 'answer') return;
		const id = setInterval(() => {
			remainingLive = Math.max(0, remainingLive - 1);
		}, 1000);
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

	let remainingTime = $derived(parseInt(String((question as any)?.time ?? 30)) || 30);
</script>

<svelte:window onbeforeunload={confirmUnload} />
<svelte:head>
	<title>CMA Clash - Play</title>
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
		{:else if gameData !== undefined && question_index === ''}
			<ShowTitle
				title={gameData.title}
				description={gameData.description}
				cover_image={gameData.cover_image}
			/>
		{:else if gameMeta.started && gameData !== undefined && question_index !== '' && answer_results === undefined}
			{#if livePhase === 'intro' && question}
				<QuestionIntro question={question.question} topic={topic_tag} />
			{:else if question?.answers && (game_mode === 'kahoot' || game_mode === 'battle' || !game_mode)}
				<AnswerTiles
					question={question.question}
					answers={Array.isArray(question.answers) ? question.answers : []}
					remainingSeconds={remainingLive}
					totalSeconds={remainingTime}
					interactive={true}
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
					points={Number(playerMine?.score ?? 0)}
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
