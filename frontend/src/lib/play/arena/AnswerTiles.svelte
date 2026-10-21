<script lang="ts">
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import TimerBar from '$lib/ui/TimerBar.svelte';
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
		/** When false, use the compact timer bar above the grid (recommended on player phones). */
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
		showRing = false,
		compact = false,
		hideQuestion = false
	}: Props = $props();
</script>

<div
	data-testid="answer-tiles"
	class="w-full min-h-dvh bg-paper flex flex-col items-center px-4 sm:px-6 py-4 sm:py-6 {compact
		? 'h-full'
		: ''}"
>
	<div class="w-full max-w-[28rem] sm:max-w-xl flex flex-col gap-4 flex-1">
		{#if !hideQuestion && question}
			<p
				class="font-sans text-lg sm:text-xl text-ink text-center font-semibold leading-snug text-balance"
			>
				{@html normalizeQuizText(question)}
			</p>
		{/if}

		<div class="w-full rounded-xl border border-white/10 bg-surface/80 px-3 py-2.5 shadow-sm">
			<TimerBar {remainingSeconds} {totalSeconds} showRing={showRing} />
			{#if answeredCount !== undefined}
				<p class="text-center text-xs text-ink-muted font-mono tabular-nums mt-2">
					{answeredCount} answered
				</p>
			{/if}
		</div>

		<div class="grid grid-cols-2 gap-2.5 sm:gap-3 pb-4 auto-rows-fr">
			{#each answers as ans, i}
				{@const color = ans.color ?? LEDGER_ANSWER_COLORS[i]}
				{#if interactive}
					<button
						type="button"
						class="rounded-2xl flex flex-col items-center justify-center gap-2 px-3 py-4 min-h-[5.5rem] max-h-[9.5rem] text-white font-bold press-scale border border-white/15 shadow-md {selected ===
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
						<AnswerShapeIcon
							shape={LEDGER_ANSWER_SHAPES[i] as AnswerShape}
							class="w-8 h-8 sm:w-10 sm:h-10 shrink-0 text-white drop-shadow"
						/>
						<span
							class="text-sm sm:text-base text-center leading-snug line-clamp-4 text-white font-bold [text-shadow:0_1px_3px_rgba(0,0,0,0.55)] [&_*]:!text-white"
						>
							{@html normalizeQuizText(ans.answer)}
						</span>
					</button>
				{:else}
					<div
						class="rounded-2xl flex flex-col items-center justify-center gap-2 px-3 py-4 min-h-[5.5rem] max-h-[9.5rem] text-white font-bold border border-white/15 shadow-md"
						style="background:{color}"
					>
						<AnswerShapeIcon
							shape={LEDGER_ANSWER_SHAPES[i] as AnswerShape}
							class="w-8 h-8 sm:w-10 sm:h-10 shrink-0 text-white drop-shadow"
						/>
						<span
							class="text-sm sm:text-base text-center leading-snug line-clamp-4 text-white font-bold [text-shadow:0_1px_3px_rgba(0,0,0,0.55)] [&_*]:!text-white"
						>
							{@html normalizeQuizText(ans.answer)}
						</span>
					</div>
				{/if}
			{/each}
		</div>
	</div>
</div>
