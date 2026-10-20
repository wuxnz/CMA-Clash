<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->
<script lang="ts">
	import { page } from '$app/state';
	import type { QuizData } from '$lib/quiz_types';
	import Spinner from '$lib/Spinner.svelte';
	import TitleScreen from '$lib/practice/title_screen.svelte';
	import Question from '$lib/practice/question.svelte';
	import AnswerTiles from '$lib/play/arena/AnswerTiles.svelte';
	import { LEDGER_ANSWER_COLORS } from '$lib/ui/tokens';
	import { navbarVisible } from '$lib/stores.svelte';

	navbarVisible.visible = true;

	let quiz: QuizData = $state();
	let unique = $state({});
	let selected_question = $state(-1);

	const quizId = $derived(page.url.searchParams.get('quiz_id'));

	const sampleAnswers = [
		{ answer: 'Left ventricle', color: LEDGER_ANSWER_COLORS[0] },
		{ answer: 'Right atrium', color: LEDGER_ANSWER_COLORS[1] },
		{ answer: 'Left atrium', color: LEDGER_ANSWER_COLORS[2] },
		{ answer: 'Right ventricle', color: LEDGER_ANSWER_COLORS[3] }
	];

	const get_quiz = async () => {
		const res = await fetch(`/api/v1/quiz/get/public/${quizId}`);
		if (!res.ok) {
			throw res.status;
		}
		quiz = await res.json();
		return quiz;
	};
	const reload_q = () => {
		unique = {};
	};
</script>

<svelte:head>
	<title>CMA Clash: Practice</title>
</svelte:head>

{#if !quizId}
	<div class="min-h-[80vh] px-4 py-10 max-w-6xl mx-auto w-full grid lg:grid-cols-2 gap-8 items-center">
		<div>
			<h1 class="text-2xl sm:text-3xl font-semibold text-ink tracking-tight">Practice</h1>
			<p class="text-ink-muted mt-3 max-w-md leading-relaxed">
				Answer questions on a timer. Pick a set and start (no lobby).
			</p>
			<a href="/explore" class="btn btn-primary w-auto mt-8">Pick a quiz</a>
		</div>
		<div class="rounded-3xl bg-surface overflow-hidden h-[28rem]">
			<div class="h-full [&_>div]:h-full [&_>div]:min-h-0">
				<AnswerTiles
					question="Which chamber of the heart receives oxygenated blood from the pulmonary veins?"
					answers={sampleAnswers}
					remainingSeconds={18}
					totalSeconds={30}
					interactive={true}
					compact
				/>
			</div>
		</div>
	</div>
{:else}
	{#await get_quiz()}
		<Spinner />
	{:then q}
		<div class="h-full overflow-hidden">
			{#if selected_question === -1}
				<TitleScreen bind:data={quiz} />
			{:else}
				{#key unique}
					<Question bind:question={quiz.questions[selected_question]} />
				{/key}
			{/if}

			<div class="grid grid-cols-2 h-fit px-20 mt-6 absolute bottom-0 w-full">
				<button
					class="flex justify-start disabled:opacity-60 press-scale"
					disabled={selected_question <= -1}
					onclick={() => {
						selected_question -= 1;
					}}
				>
					<svg
						class="w-16 h-16"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
						xmlns="http://www.w3.org/2000/svg"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M15 19l-7-7 7-7"
						/>
					</svg>
				</button>
				<button
					class="flex justify-end disabled:opacity-60 press-scale"
					disabled={selected_question >= quiz.questions.length - 1}
					onclick={() => {
						reload_q();
						selected_question += 1;
					}}
				>
					<svg
						class="w-16 h-16"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
						xmlns="http://www.w3.org/2000/svg"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M9 5l7 7-7 7"
						/>
					</svg>
				</button>
			</div>
		</div>
	{:catch e}
		{#if e === 404 || e === 400}
			<h1 class="text-center text-xl font-semibold text-ink tracking-tight pt-20">Quiz not found</h1>
		{:else}
			<h1 class="text-center text-xl font-semibold text-ink tracking-tight pt-20">Could not load practice</h1>
		{/if}
	{/await}
{/if}
