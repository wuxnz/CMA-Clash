<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import type { Question } from '$lib/quiz_types';
	import { QuizQuestionType } from '$lib/quiz_types';
	import { socket } from '$lib/socket';
	import Spinner from '../Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import { kahoot_icons } from './kahoot_mode_assets/kahoot_icons';
	import CircularTimer from '$lib/play/circular_progress.svelte';
	import { flip } from 'svelte/animate';
	import BrownButton from '$lib/components/buttons/brown.svelte';
	import { get_foreground_color } from '../helpers';
	import MediaComponent from '$lib/editor/MediaComponent.svelte';
	import { LEDGER_ANSWER_COLORS, LEDGER_ANSWER_SHAPES } from '$lib/ui/tokens';
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import TimerBar from '$lib/ui/TimerBar.svelte';
	import TopicTag from '$lib/ui/TopicTag.svelte';
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';
	import type { AnswerShape } from '$lib/ui/tokens';
	import { normalizeQuizText } from '$lib/cma/text';

	const { t } = getLocalization();

	interface Props {
		question: Question;
		game_mode: any;
		question_index: string | number;
		solution: any;
		topic_tag?: string;
		/** When set, countdown follows server deadlines instead of restarting locally. */
		serverRemainingSeconds?: number;
	}

	let {
		question = $bindable(),
		game_mode = $bindable(),
		question_index,
		solution,
		topic_tag = '',
		serverRemainingSeconds
	}: Props = $props();

	if (question.type === undefined) {
		question.type = QuizQuestionType.ABCD;
	} else {
		question.type = QuizQuestionType[question.type];
	}

	let timer_res = $state(question.time);
	let selected_answer: string = $state();

	socket.on('everyone_answered', (_) => {
		timer_res = '0';
	});

	$effect(() => {
		if (serverRemainingSeconds != null) {
			timer_res = String(Math.max(0, Math.ceil(serverRemainingSeconds)));
			return;
		}
		let seconds = Number(question.time);
		timer_res = seconds.toString();
		const id = setInterval(() => {
			if (timer_res === '0') {
				clearInterval(id);
				return;
			}
			seconds -= 1;
			timer_res = seconds.toString();
		}, 1000);
		return () => clearInterval(id);
	});

	$effect(() => {
		if (solution !== undefined) {
			timer_res = '0';
		}
	});

	const selectAnswer = (answer: string) => {
		selected_answer = answer;
		socket.emit('submit_answer', {
			question_index: question_index,
			answer: answer
		});
	};

	const select_complex_answer = (data) => {
		selected_answer = 'a';
		const new_array = [];
		for (let i = 0; i < data.length; i++) {
			new_array.push({ answer: data[i].answer });
		}
		socket.emit('submit_answer', {
			question_index: question_index,
			answer: 'a',
			complex_answer: new_array
		});
	};

	let text_input = $state('');

	let slider_value = $state([0]);
	if (question.type === QuizQuestionType.RANGE) {
		slider_value[0] = (question.answers.max - question.answers.min) / 2 + question.answers.min;
	}
	const set_answer_if_not_set_range = (time) => {
		if (question.type !== QuizQuestionType.RANGE) {
			return;
		}
		if (selected_answer === undefined && time === '0') {
			selected_answer = `${slider_value[0]}`;
			selectAnswer(selected_answer);
		}
	};

	if (question.type === QuizQuestionType.ORDER) {
		for (let i = 0; i < question.answers.length; i++) {
			question.answers[i] = { ...question.answers[i], id: i };
		}
	}

	const swapArrayElements = (arr, a: number, b: number) => {
		let _arr = [...arr];
		let temp = _arr[a];
		_arr[a] = _arr[b];
		_arr[b] = temp;
		return _arr;
	};
	$effect(() => {
		set_answer_if_not_set_range(timer_res);
	});
	let circular_progress = $derived.by(() => {
		try {
			return 1 - ((100 / question.time) * parseInt(timer_res)) / 100;
		} catch {
			return 0;
		}
	});

	const get_div_height = (): string => {
		if (game_mode === 'normal') {
			if (question.image) {
				return '66.666667';
			} else {
				return '83.333333';
			}
		} else {
			return '100';
		}
	};
	const default_colors = [...LEDGER_ANSWER_COLORS];

	let totalTime = $derived(parseInt(question.time) || 30);
	let remainingTime = $derived(parseInt(timer_res) || 0);
	let topicLabel = $derived(topic_tag || `Live · Q${Number(question_index) + 1}`);
</script>

<div class="min-h-screen w-screen bg-paper flex flex-col">
	{#if game_mode === 'kahoot'}
		<LivePlayHeader />
	{/if}
	{#if game_mode === 'normal'}
		<div
			class="flex flex-col justify-start"
			class:mt-10={[QuizQuestionType.RANGE, QuizQuestionType.ORDER, QuizQuestionType.TEXT]}
			style="height: {question.image ? '33.333333' : '16.666667'}%"
		>
			<h1
				class="lg:text-2xl text-lg text-center text-ink text-ink mt-2 break-normal mb-2"
			>
				{@html normalizeQuizText(question.question)}
			</h1>
			{#if question.image !== null && game_mode !== 'kahoot'}
				<div class="max-h-full">
					<MediaComponent
						src={question.image}
						css_classes="object-cover mx-auto mb-8 max-h-[90%]"
					/>
				</div>
			{/if}
		</div>
	{/if}
	{#if timer_res !== '0'}
		{#if question.type === QuizQuestionType.ABCD || question.type === QuizQuestionType.VOTING}
			<div
				class="flex-1 flex flex-col max-w-3xl mx-auto w-full px-4 py-4 gap-4"
				style={game_mode !== 'kahoot' ? `height: ${get_div_height()}%` : ''}
			>
				{#if game_mode === 'kahoot'}
					<div class="rounded-2xl border border-ink/10 bg-surface p-4 sm:p-6 shadow-sm">
						<TopicTag label={topicLabel} />
						<h1
							class="font-display text-lg sm:text-xl text-ink mt-3 mb-4 leading-snug text-center"
						>
							{@html normalizeQuizText(question.question)}
						</h1>
						<TimerBar remainingSeconds={remainingTime} totalSeconds={totalTime} showRing={true} />
					</div>
				{:else}
					<div
						class="absolute top-0 bottom-0 left-0 right-0 m-auto rounded-full h-fit w-fit border-2 border-ink/20 shadow-lg z-40 pointer-events-none"
					>
						<CircularTimer text={timer_res} progress={circular_progress} color="#0ea5e9" />
					</div>
				{/if}

				<div
					class="grid grid-cols-2 gap-3 flex-1 min-h-[12rem] {game_mode === 'kahoot'
						? 'sm:gap-4'
						: 'grid-rows-2 grid-flow-col auto-cols-auto'}"
				>
					{#each question.answers as answer, i}
						<button
							type="button"
							class="rounded-xl flex flex-col items-center justify-center gap-2 disabled:opacity-60 p-4 sm:p-6 min-h-[5.5rem] border-2 border-white/20 shadow-md hover:brightness-105 press-scale focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-white"
							style="background-color: {answer.color ??
								default_colors[i]}; color: {get_foreground_color(
								answer.color ?? default_colors[i]
							)}"
							disabled={selected_answer !== undefined}
							onclick={() => selectAnswer(answer.answer)}
						>
							{#if game_mode === 'kahoot'}
								<AnswerShapeIcon
									shape={LEDGER_ANSWER_SHAPES[i] as AnswerShape}
									class="w-8 h-8 sm:w-10 sm:h-10"
								/>
								<span class="font-mono text-sm sm:text-base font-medium text-center"
									>{normalizeQuizText(answer.answer)}</span
								>
							{:else}
								<p class="m-auto text-center">{normalizeQuizText(answer.answer)}</p>
							{/if}
						</button>
					{/each}
				</div>
			</div>
		{:else if question.type === QuizQuestionType.RANGE}
			<span
				class="fixed top-0 bg-red-500 h-8 transition-all"
				style="width: {(100 / parseInt(question.time)) * parseInt(timer_res)}vw"
			></span>
			{#await import('svelte-range-slider-pips')}
				<Spinner />
			{:then c}
				<div class:pointer-events-none={selected_answer !== undefined} class="mt-24">
					<c.default
						bind:values={slider_value}
						bind:min={question.answers.min}
						bind:max={question.answers.max}
						id="pips-slider"
						pips
						float
						all="label"
					/>
				</div>
				<div class="flex justify-center">
					<div class="w-1/2">
						<BrownButton onclick={() => selectAnswer(slider_value[0])}
							>{$t('words.submit')}
						</BrownButton>
					</div>
				</div>
			{/await}
		{:else if question.type === QuizQuestionType.TEXT}
			<div>
				<span
					class="fixed top-0 bg-red-500 h-8 transition-all"
					style="width: {(100 / parseInt(question.time)) * parseInt(timer_res)}vw"
				></span>
				<div class="flex justify-center mt-10">
					<p class="text-ink text-ink">Enter your answer</p>
				</div>
				<div class="flex justify-center m-2">
					<input
						type="text"
						bind:value={text_input}
						disabled={selected_answer !== undefined}
						class="bg-gray-50 focus:ring text-ink rounded-lg focus:ring-blue-500 block w-full p-2 bg-elevated text-ink dark:focus:ring-blue-500 outline-hidden transition text-center disabled:opacity-50 disabled:cursor-not-allowed"
					/>
				</div>

				<div class="flex justify-center mt-2">
					<div class="w-1/3">
						<BrownButton
							type="button"
							disabled={!text_input || text_input.length === 0}
							onclick={() => {
								selectAnswer(text_input);
							}}
						>
							{$t('words.submit')}
						</BrownButton>
					</div>
				</div>
			</div>
		{:else if question.type === QuizQuestionType.ORDER}
			<!--			{#if solution === undefined}
                            <Spinner />
                        {:else}-->
			<span
				class="fixed top-0 bg-red-500 h-8 transition-all"
				style="width: {(100 / parseInt(question.time)) * parseInt(timer_res)}vw"
			></span>
			<div class="flex flex-col w-full h-full gap-4 px-4 py-6 mt-10">
				{#each question.answers as answer, i (answer.id)}
					<div
						class="w-full h-fit flex-row rounded-lg p-2 align-middle"
						animate:flip={{ duration: 100 }}
						style="background-color: {answer.color ?? '#b07156'}"
					>
						<button
							onclick={() => {
								question.answers = swapArrayElements(question.answers, i, i - 1);
							}}
							class="disabled:opacity-50 shadow-lg bg-black/30 w-full flex justify-center rounded-lg p-2 hover:bg-black/20 transition"
							type="button"
							aria-label="Move item up"
							disabled={i === 0 || Boolean(selected_answer)}
						>
							<svg
								class="w-8 h-8"
								stroke-width="2"
								viewBox="0 0 24 24"
								fill="none"
								xmlns="http://www.w3.org/2000/svg"
								color="currentColor"
							>
								<path
									d="M12 22a2 2 0 110-4 2 2 0 010 4zM12 15V2m0 0l3 3m-3-3L9 5"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
						</button>
						<p class="w-full text-center p-2 text-2xl">{answer.answer}</p>

						<button
							onclick={() => {
								question.answers = swapArrayElements(question.answers, i, i + 1);
							}}
							class="disabled:opacity-50 shadow-lg bg-black/30 w-full flex justify-center rounded-lg p-2 hover:bg-black/20 transition"
							type="button"
							aria-label="Move item down"
							disabled={i === question.answers.length - 1 || Boolean(selected_answer)}
						>
							<svg
								class="w-8 h-8"
								stroke-width="2"
								viewBox="0 0 24 24"
								fill="none"
								xmlns="http://www.w3.org/2000/svg"
								color="currentColor"
							>
								<path
									d="M12 6a2 2 0 110-4 2 2 0 010 4zM12 9v13m0 0l3-3m-3 3l-3-3"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
						</button>
					</div>
				{/each}
				<div class="w-full mt-2">
					<BrownButton
						type="button"
						disabled={Boolean(selected_answer)}
						onclick={() => {
							select_complex_answer(question.answers);
						}}>{$t('words.submit')}</BrownButton
					>
				</div>
			</div>
			<!--{/if}-->
		{:else if question.type === QuizQuestionType.CHECK}
			{#await import('./questions/check.svelte')}
				<Spinner />
			{:then c}
				<c.default
					{question}
					bind:selected_answer
					{game_mode}
					{timer_res}
					{circular_progress}
				/>
				<div class="flex justify-center h-[5%]">
					<div class="w-1/2">
						<BrownButton
							type="button"
							disabled={selected_answer === undefined}
							onclick={() => selectAnswer(selected_answer)}
							>{$t('words.submit')}
						</BrownButton>
					</div>
				</div>
			{/await}
		{/if}
	{/if}
</div>
