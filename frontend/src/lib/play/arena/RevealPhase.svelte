<script lang="ts">
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import { LEDGER_ANSWER_COLORS, LEDGER_ANSWER_SHAPES } from '$lib/ui/tokens';
	import type { AnswerShape } from '$lib/ui/tokens';
	import { normalizeQuizText } from '$lib/cma/text';
	import AnimatedCounter from '$lib/ui/AnimatedCounter.svelte';

	export type DistRow = { answer: string; count: number; right?: boolean };

	interface Props {
		question: string;
		distribution: DistRow[];
		correct?: boolean | null;
		points?: number;
		baseScore?: number;
		speedBonus?: number;
		placeText?: string | null;
		behindText?: string | null;
		speedRankText?: string | null;
		streak?: number;
		isPlayer?: boolean;
		hostFit?: boolean;
		correctAnswer?: string | null;
		explanation?: string | null;
	}

	let {
		question,
		distribution,
		correct = null,
		points = 0,
		baseScore = 0,
		speedBonus = 0,
		placeText = null,
		behindText = null,
		speedRankText = null,
		streak = 0,
		isPlayer = false,
		hostFit = false,
		correctAnswer = null,
		explanation = null
	}: Props = $props();

	let max = $derived(Math.max(1, ...distribution.map((d) => d.count)));
	let showAnswerBlock = $derived(Boolean(correctAnswer && correctAnswer.trim().length > 0));
	let showExplanation = $derived(Boolean(explanation && explanation.trim().length > 0));
</script>

<div
	class="w-full bg-paper flex flex-col px-4 sm:px-8 {hostFit
		? 'h-full min-h-0 py-4 sm:py-6'
		: 'h-dvh min-h-dvh py-8'}"
>
	<p
		class="font-sans text-ink text-center font-semibold max-w-4xl mx-auto shrink-0 {hostFit
			? 'text-base sm:text-lg mb-4 line-clamp-3'
			: 'text-lg sm:text-2xl mb-8'}"
	>
		{@html normalizeQuizText(question)}
	</p>

	{#if isPlayer && correct !== null}
		<div class="text-center mb-6">
			{#if !correct && (points ?? 0) === 0}
				<p class="text-sm font-semibold uppercase tracking-wide text-ink-muted mb-2">Time's up</p>
			{/if}
			<p class="font-display text-5xl sm:text-7xl {correct ? 'text-gold' : 'text-danger'}">
				{correct ? 'Correct' : 'Incorrect'}
			</p>
			<p class="font-display text-3xl text-gold tabular-nums mt-2" data-testid="reveal-points-total">
				+<AnimatedCounter value={points} duration={0.8} />
			</p>
			{#if correct && (baseScore > 0 || speedBonus > 0)}
				<p class="text-sm text-ink-muted mt-2 tabular-nums">
					{baseScore} base{#if speedBonus > 0}, {speedBonus} speed bonus{/if}
				</p>
			{/if}
			{#if placeText}
				<p class="text-base text-ink font-semibold mt-3" data-testid="reveal-place-line">{placeText}</p>
			{/if}
			{#if behindText}
				<p class="text-sm text-ink-muted" data-testid="reveal-behind-line">{behindText}</p>
			{/if}
			{#if speedRankText}
				<p class="text-sm text-ink-muted mt-1" data-testid="reveal-speed-rank">{speedRankText}</p>
			{/if}
			{#if streak > 0}
				<p class="text-signal font-display text-xl mt-1">{streak}-streak</p>
			{/if}
		</div>
	{/if}

	{#if showAnswerBlock || showExplanation}
		<div
			class="max-w-2xl mx-auto w-full mb-6 rounded-xl border border-ink/10 bg-surface px-4 py-4 text-left shrink-0"
			data-testid="reveal-explanation-panel"
		>
			{#if showAnswerBlock}
				<p class="text-base text-ink font-semibold mb-2" data-testid="reveal-correct-answer">
					Correct answer: {normalizeQuizText(correctAnswer ?? '')}
				</p>
			{/if}
			{#if showExplanation}
				<p class="text-base text-ink leading-relaxed" data-testid="reveal-explanation">
					{normalizeQuizText(explanation ?? '')}
				</p>
			{/if}
		</div>
	{/if}

	<ul class="max-w-2xl mx-auto w-full space-y-2.5 sm:space-y-4 flex-1 min-h-0 overflow-y-auto">
		{#each distribution as row, i (row.answer)}
			<li>
				<div class="flex items-center gap-3 mb-1">
					<span
						class="inline-flex items-center justify-center w-8 h-8 rounded-md text-white shrink-0"
						style="background:{LEDGER_ANSWER_COLORS[i % LEDGER_ANSWER_COLORS.length]}"
					>
						<AnswerShapeIcon shape={LEDGER_ANSWER_SHAPES[i] as AnswerShape} class="w-4 h-4" />
					</span>
					<span class="font-sans text-sm sm:text-base truncate flex-1 {row.right ? 'text-gold font-semibold' : 'text-ink'}">
						{normalizeQuizText(row.answer)}
					</span>
					<span class="font-display tabular-nums text-ink-muted">{row.count}</span>
				</div>
				<div class="h-3 rounded-full bg-elevated overflow-hidden">
					<div
						class="h-full rounded-full {row.right ? 'bg-gold' : 'bg-primary'}"
						style="width: {(row.count / max) * 100}%; transition: width 300ms ease-out"
					></div>
				</div>
			</li>
		{/each}
	</ul>
</div>
