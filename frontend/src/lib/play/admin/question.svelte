<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { QuizQuestionType } from '$lib/quiz_types';
	import type { QuizData } from '$lib/quiz_types';
	import { get_foreground_color } from '$lib/helpers.js';
	import { kahoot_icons } from '$lib/play/kahoot_mode_assets/kahoot_icons.js';
	import MediaComponent from '$lib/editor/MediaComponent.svelte';
	import { getLocalization } from '$lib/i18n';
	import TimerBar from '$lib/ui/TimerBar.svelte';
	import TopicTag from '$lib/ui/TopicTag.svelte';
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import { LEDGER_ANSWER_SHAPES } from '$lib/ui/tokens';
	import type { AnswerShape } from '$lib/ui/tokens';
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';
	import { normalizeQuizText } from '$lib/cma/text';

	interface Props {
		quiz_data: QuizData;
		selected_question: number;
		timer_res: string;
		answer_count: number;
		default_colors: string[];
		topic_tag?: string;
		game_pin?: string;
	}

	let {
		quiz_data,
		selected_question,
		timer_res = $bindable(),
		answer_count,
		default_colors,
		topic_tag = '',
		game_pin
	}: Props = $props();

	const { t } = getLocalization();

	let q = $derived(quiz_data.questions[selected_question]);
	let totalTime = $derived(parseInt(q.time) || 30);
	let remainingTime = $derived(parseInt(timer_res) || 0);
	let isKahoot = $derived(quiz_data.game_mode === 'kahoot' || quiz_data.game_mode === 'battle');
</script>

<div class="min-h-screen bg-paper flex flex-col">
	<LivePlayHeader pin={game_pin} />
	<div class="flex-1 max-w-4xl mx-auto w-full px-4 py-6 flex flex-col gap-4">
		<div class="rounded-2xl border border-ink/10 bg-surface p-4 sm:p-6 shadow-sm">
			{#if topic_tag}
				<TopicTag label={topic_tag} />
			{/if}
			<h1 class="font-display text-xl sm:text-2xl text-ink mt-3 mb-4 leading-snug text-center">
				{@html normalizeQuizText(q.question)}
			</h1>
			<TimerBar remainingSeconds={remainingTime} totalSeconds={totalTime} showRing={true} />
			<p class="text-center text-sm text-ink-muted mt-3 font-mono tabular-nums">
				{$t('admin_page.answers_submitted', { answer_count })}
			</p>
		</div>

		{#if q.image !== null}
			<div class="flex w-full justify-center">
				<MediaComponent
					src={q.image}
					muted={false}
					css_classes="max-h-[22vh] object-contain rounded-lg border border-ink/10"
				/>
			</div>
		{/if}

		{#if q.type === QuizQuestionType.ABCD || q.type === QuizQuestionType.VOTING || q.type === QuizQuestionType.CHECK}
			<div class="grid grid-cols-2 gap-3 sm:gap-4">
				{#each q.answers as answer, i (i)}
					<div
						class="rounded-xl flex flex-col items-center justify-center gap-2 p-4 sm:p-6 min-h-[5rem] border-2 border-white/20 shadow-md"
						style="background-color: {answer.color ?? default_colors[i]};"
						class:opacity-50={!answer.right &&
							timer_res === '0' &&
							q.type === QuizQuestionType.ABCD}
						class:ring-4={answer.right && timer_res === '0'}
						class:ring-gold={answer.right && timer_res === '0'}
					>
						{#if isKahoot}
							<div style="color: {get_foreground_color(answer.color ?? default_colors[i])}">
								<AnswerShapeIcon
									shape={LEDGER_ANSWER_SHAPES[i] as AnswerShape}
									class="w-8 h-8"
								/>
							</div>
						{:else if quiz_data.game_mode === 'kahoot'}
							<img class="h-12" alt="" src={kahoot_icons[i]} />
						{/if}
						<p
							class="text-center font-mono text-sm sm:text-base"
							style="color: {get_foreground_color(answer.color ?? default_colors[i])}"
						>
							{normalizeQuizText(answer.answer)}
						</p>
					</div>
				{/each}
			</div>
		{/if}
	</div>
</div>
