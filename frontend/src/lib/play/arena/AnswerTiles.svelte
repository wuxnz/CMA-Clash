<script lang="ts">
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import { LEDGER_ANSWER_COLORS, LEDGER_ANSWER_SHAPES } from '$lib/ui/tokens';
	import type { AnswerShape } from '$lib/ui/tokens';
	import { normalizeQuizText } from '$lib/cma/text';
	export type ArenaAnswer = { answer: string; color?: string; right?: boolean };

	interface Props {
		question: string;
		answers: ArenaAnswer[];
		remainingSeconds: number;
		totalSeconds: number;
		answeredCount?: number;
		interactive?: boolean;
		selected?: string;
		disabled?: boolean;
		onSelect?: (answer: string) => void;
		showRing?: boolean;
		compact?: boolean;
		hideQuestion?: boolean;
	}

	let {
		question,
		answers,
		remainingSeconds,
		totalSeconds,
		answeredCount,
		interactive = false,
		selected,
		disabled = false,
		onSelect,
		showRing = true,
		compact = false,
		hideQuestion = false
	}: Props = $props();
</script>

<div class="w-full bg-paper flex flex-col px-3 sm:px-6 py-4 sm:py-6 {compact ? 'h-full' : 'h-full min-h-dvh'}">
	{#if !hideQuestion && question}
		<p class="font-sans text-lg sm:text-2xl md:text-3xl text-ink text-center font-semibold leading-snug max-w-4xl mx-auto">
			{@html normalizeQuizText(question)}
		</p>
	{/if}

	<div class="flex items-center justify-center gap-6 my-4">
		{#if showRing}
			<div class="scale-90 sm:scale-100">
				<div class="relative w-20 h-20 sm:w-24 sm:h-24" aria-hidden="true">
					<svg class="w-full h-full -rotate-90" viewBox="0 0 120 120">
						<circle cx="60" cy="60" r="54" fill="none" stroke="currentColor" stroke-width="10" class="text-elevated" />
						<circle
							cx="60"
							cy="60"
							r="54"
							fill="none"
							stroke="currentColor"
							stroke-width="10"
							stroke-linecap="round"
							class="text-gold"
							stroke-dasharray={2 * Math.PI * 54}
							stroke-dashoffset={2 * Math.PI * 54 * (1 - Math.max(0, remainingSeconds) / Math.max(1, totalSeconds))}
							style="transition: stroke-dashoffset 1s linear"
						/>
					</svg>
					<span class="absolute inset-0 flex items-center justify-center font-display text-3xl text-gold tabular-nums">
						{Math.max(0, Math.ceil(remainingSeconds))}
					</span>
				</div>
			</div>
		{/if}
		{#if answeredCount !== undefined}
			<p class="font-display text-xl text-ink-muted tabular-nums">{answeredCount} answered</p>
		{/if}
	</div>

	<div class="flex-1 grid grid-cols-2 gap-2 sm:gap-4 min-h-0 pb-2">
		{#each answers as ans, i}
			{@const color = ans.color ?? LEDGER_ANSWER_COLORS[i]}
			{#if interactive}
				<button
					type="button"
					class="rounded-2xl flex flex-col items-center justify-center gap-2 p-4 sm:p-8 min-h-[7rem] text-white press-scale border border-transparent {selected ===
					ans.answer
						? 'ring-4 ring-gold'
						: ''}"
					style="background:{color}"
					disabled={disabled || selected !== undefined}
					onclick={() => {
						if (typeof navigator !== 'undefined' && navigator.vibrate) navigator.vibrate(12);
						onSelect?.(ans.answer);
					}}
				>
					<AnswerShapeIcon shape={LEDGER_ANSWER_SHAPES[i] as AnswerShape} class="w-10 h-10 sm:w-14 sm:h-14" />
					<span class="font-display text-xl sm:text-3xl text-center leading-none normal-case tracking-tight">
						{normalizeQuizText(ans.answer)}
					</span>
				</button>
			{:else}
				<div
					class="rounded-2xl flex flex-col items-center justify-center gap-2 p-4 sm:p-8 min-h-[7rem] text-white"
					style="background:{color}"
				>
					<AnswerShapeIcon shape={LEDGER_ANSWER_SHAPES[i] as AnswerShape} class="w-10 h-10 sm:w-14 sm:h-14" />
					<span class="font-display text-xl sm:text-3xl text-center leading-none normal-case tracking-tight">
						{normalizeQuizText(ans.answer)}
					</span>
				</div>
			{/if}
		{/each}
	</div>
</div>
