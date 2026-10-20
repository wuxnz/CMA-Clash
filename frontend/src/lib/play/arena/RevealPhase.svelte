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
		streak?: number;
		isPlayer?: boolean;
	}

	let {
		question,
		distribution,
		correct = null,
		points = 0,
		streak = 0,
		isPlayer = false
	}: Props = $props();

	let max = $derived(Math.max(1, ...distribution.map((d) => d.count)));
</script>

<div class="h-dvh min-h-dvh w-full bg-paper flex flex-col px-4 sm:px-8 py-8">
	<p class="font-sans text-lg sm:text-2xl text-ink text-center font-semibold max-w-4xl mx-auto mb-8">
		{@html normalizeQuizText(question)}
	</p>

	{#if isPlayer && correct !== null}
		<div class="text-center mb-8">
			<p class="font-display text-5xl sm:text-7xl {correct ? 'text-gold' : 'text-danger'}">
				{correct ? 'Correct' : 'Incorrect'}
			</p>
			<p class="font-display text-3xl text-gold tabular-nums mt-2">
				+<AnimatedCounter value={points} duration={0.8} />
			</p>
			{#if streak > 0}
				<p class="text-signal font-display text-xl mt-1">{streak}-streak</p>
			{/if}
		</div>
	{/if}

	<ul class="max-w-2xl mx-auto w-full space-y-4 flex-1">
		{#each distribution as row, i}
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
