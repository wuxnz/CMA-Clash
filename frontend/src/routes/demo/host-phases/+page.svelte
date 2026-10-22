<!-- Host live-flow phases with the same shell + controls as /admin (for mobile layout e2e). -->
<script lang="ts">
	import { page } from '$app/state';
	import { navbarVisible } from '$lib/stores.svelte';
	import HostLiveShell from '$lib/play/admin/host-live-shell.svelte';
	import Controls from '$lib/play/admin/controls.svelte';
	import QuestionIntro from '$lib/play/arena/QuestionIntro.svelte';
	import AnswerTiles from '$lib/play/arena/AnswerTiles.svelte';
	import RevealPhase from '$lib/play/arena/RevealPhase.svelte';
	import RankingsBoard from '$lib/play/arena/RankingsBoard.svelte';
	import HostProgress from '$lib/play/admin/host-progress.svelte';
	import { LEDGER_ANSWER_COLORS } from '$lib/ui/tokens';
	import { SocketGameControls } from '$lib/play/admin/socket_game_controls';
	import { QuizQuestionType } from '$lib/quiz_types';
	import { normalizeQuizText } from '$lib/cma/text';

	navbarVisible.visible = false;

	const phase = $derived(page.url.searchParams.get('phase') ?? 'get-ready');

	const q = 'Which chamber receives oxygenated blood from the pulmonary veins?';
	const answers = [
		{ answer: 'Left ventricle', color: LEDGER_ANSWER_COLORS[0] },
		{ answer: 'Right atrium', color: LEDGER_ANSWER_COLORS[1] },
		{ answer: 'Left atrium', color: LEDGER_ANSWER_COLORS[2], right: true },
		{ answer: 'Right ventricle', color: LEDGER_ANSWER_COLORS[3] }
	];
	const dist = [
		{ answer: 'Left ventricle', count: 8 },
		{ answer: 'Right atrium', count: 4 },
		{ answer: 'Left atrium', count: 14, right: true },
		{ answer: 'Right ventricle', count: 2 }
	];
	const ranks = [
		{ rank: 1, name: 'A. Okafor', score: 9420 },
		{ rank: 2, name: 'M. Chen', score: 9105, delta: 1 },
		{ rank: 3, name: 'Jordan Lee', score: 8870, delta: -1 }
	];

	const quizStub = {
		title: 'CCMA Anatomy Clash',
		description: 'Warm up before question one — players should stay on the join screen.',
		game_pin: '482913',
		game_mode: 'kahoot',
		questions: [
			{
				question: q,
				answers,
				time: '30',
				type: QuizQuestionType.ABCD
			},
			{
				question: 'Backup question',
				answers,
				time: '30',
				type: QuizQuestionType.ABCD
			}
		]
	};

	type DemoState = {
		selected_question: number;
		timer_res: string;
		question_results: typeof dist | null;
		answer_count: number;
		shown_question_now: number;
		final_results: [null];
		quiz_data: typeof quizStub;
		control_visible: boolean;
		player_scores: Record<string, number>;
	};

	function stateFor(phaseId: string): DemoState {
		const base: DemoState = {
			selected_question: 0,
			timer_res: '18',
			question_results: null,
			answer_count: 12,
			shown_question_now: 0,
			final_results: [null],
			quiz_data: quizStub,
			control_visible: true,
			player_scores: { 'A. Okafor': 9420, 'M. Chen': 9105, 'Jordan Lee': 8870 }
		};
		switch (phaseId) {
			case 'get-ready':
				return { ...base, selected_question: -1, timer_res: '0', answer_count: 0 };
			case 'intro':
				return { ...base, timer_res: '30' };
			case 'answer':
				return { ...base, timer_res: '18' };
			case 'stop-time':
				return { ...base, timer_res: '22' };
			case 'show-results':
				return { ...base, timer_res: '0', question_results: null };
			case 'reveal':
				return { ...base, timer_res: '0', question_results: dist };
			case 'rankings':
				return { ...base, timer_res: '0', question_results: dist };
			case 'on-devices':
				return { ...base, timer_res: '18', quiz_data: { ...quizStub, game_mode: 'normal' } };
			default:
				return base;
		}
	}

	let game_state = $derived(stateFor(phase));

	const noopSocket = { emit: () => {} } as import('socket.io-client').Socket;
	const socket_game_controls = new SocketGameControls(noopSocket);

	const shellCurrent = $derived(
		game_state.selected_question < 0 ? 0 : game_state.selected_question + 1
	);
</script>

<Controls bg_color="" {socket_game_controls} game_token="demo" bind:game_state />

<HostLiveShell
	current={shellCurrent}
	total={game_state.quiz_data.questions.length}
	gamePin={game_state.quiz_data.game_pin}
>
	{#if phase === 'get-ready'}
		<div
			class="flex flex-col items-center justify-center h-full min-h-0 px-4 py-6 text-center"
			data-testid="host-get-ready"
		>
			<p class="font-display text-gold text-xs tracking-[0.3em] mb-2">Get ready</p>
			<h1 class="font-display text-3xl text-ink line-clamp-4">
				{@html normalizeQuizText(game_state.quiz_data.title)}
			</h1>
			<p class="text-sm pt-3 text-ink-muted line-clamp-3">
				{@html game_state.quiz_data.description}
			</p>
		</div>
	{:else if phase === 'intro'}
		<QuestionIntro hostFit question={q} topic="CCMA · Anatomy · Q1/2" seconds={99} />
	{:else if phase === 'on-devices'}
		<HostProgress remainingSeconds={18} totalSeconds={30} answerCount={12} />
	{:else if phase === 'answer'}
		<AnswerTiles
			hostFit
			question={q}
			{answers}
			remainingSeconds={18}
			totalSeconds={30}
			answeredCount={12}
			showRing={false}
		/>
	{:else if phase === 'reveal'}
		<RevealPhase hostFit question={q} distribution={dist} />
	{:else if phase === 'rankings'}
		<RankingsBoard hostFit rows={ranks} />
	{:else if phase === 'stop-time' || phase === 'show-results'}
		<AnswerTiles
			hostFit
			question={q}
			{answers}
			remainingSeconds={phase === 'show-results' ? 0 : 22}
			totalSeconds={30}
			answeredCount={12}
			showRing={false}
		/>
	{/if}
</HostLiveShell>
