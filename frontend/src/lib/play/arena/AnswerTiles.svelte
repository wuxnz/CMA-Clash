<script lang="ts">
	import TimerBar from '$lib/ui/TimerBar.svelte';
	import { normalizeQuizText } from '$lib/cma/text';
	import { fitText } from '$lib/ui/fit-text';
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
		onSelect?: (_answer: string) => void;
		/** When false, use the compact timer bar above the grid (recommended on player phones). */
		showRing?: boolean;
		compact?: boolean;
		hideQuestion?: boolean;
		/** e.g. cert · topic · Q1/10 (shown above the question in battle mode). */
		questionLabel?: string;
		questionImage?: string | null;
		/** High-contrast question copy for player-only battle screens. */
		battlePlayerLayout?: boolean;
		/** Host admin shell: fill scroll region, not full viewport. */
		hostFit?: boolean;
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
		hideQuestion = false,
		questionLabel = '',
		questionImage = null,
		battlePlayerLayout = false,
		hostFit = false
	}: Props = $props();

	const embedded = $derived(hostFit || compact);
</script>

<div
	data-testid="answer-tiles"
	class="w-full bg-paper flex flex-col items-center px-4 sm:px-8 py-5 sm:py-8 {embedded
		? 'h-full min-h-0'
		: 'min-h-dvh'}"
>
	<div class="w-full max-w-[34rem] sm:max-w-2xl flex flex-col gap-5 flex-1">
		{#if !hideQuestion && question}
			<div class="flex flex-col gap-3 w-full">
				{#if questionLabel}
					<p
						class="text-xs sm:text-sm font-mono uppercase tracking-[0.18em] {battlePlayerLayout
							? 'text-white/70'
							: 'text-ink-subtle'}"
					>
						{questionLabel}
					</p>
				{/if}
				{#if questionImage}
					<div class="w-full max-h-40 sm:max-h-52 overflow-hidden border border-line">
						<img
							src={questionImage.startsWith('http') || questionImage.startsWith('/')
								? questionImage
								: `/api/v1/storage/download/${questionImage}`}
							alt=""
							class="w-full h-full object-contain bg-black/40"
						/>
					</div>
				{/if}
				<p
					data-testid="battle-question-text"
					class="font-display text-2xl sm:text-3xl leading-[1.14] tracking-[-0.03em] text-balance wrap-break-word px-0 {battlePlayerLayout
						? 'text-white'
						: 'text-ink'}"
				>
					{@html normalizeQuizText(question)}
				</p>
			</div>
		{/if}

		<div class="w-full border border-line bg-paper px-3 py-2.5">
			<TimerBar {remainingSeconds} {totalSeconds} {showRing} />
			{#if answeredCount !== undefined}
				<p class="text-center text-xs text-ink-muted font-mono tabular-nums mt-2">
					{answeredCount} answered
				</p>
			{/if}
		</div>

		<div class="grid grid-cols-2 gap-px bg-line border border-line pb-4 auto-rows-fr">
			{#each answers as ans, i (ans.answer)}
				{#if interactive}
					<button
						type="button"
						class="bg-paper flex flex-col items-start justify-between gap-3 px-4 py-4 sm:px-5 sm:py-5 h-[8rem] sm:h-[9rem] text-ink text-left press-scale border-0 transition-colors duration-200 {selected ===
						ans.answer
							? 'bg-primary-soft shadow-[inset_3px_0_0_0_var(--color-primary)]'
							: 'hover:bg-elevated'} {disabled ? 'opacity-60' : ''}"
						disabled={disabled || selected !== undefined}
						onclick={() => {
							if (typeof navigator !== 'undefined' && navigator.vibrate)
								navigator.vibrate(12);
							onSelect?.(ans.answer);
						}}
					>
						<span
							class="font-mono text-[0.7rem] tracking-[0.2em] {selected === ans.answer
								? 'text-primary'
								: 'text-ink-subtle'}"
						>
							{String.fromCharCode(65 + i)}
						</span>
						<span
							class="block text-sm sm:text-base leading-snug wrap-break-word font-medium [&_*]:!text-ink"
			use:fitText={{ min: 11, max: 18 }}
						>
							{@html normalizeQuizText(ans.answer)}
						</span>
					</button>
				{:else}
					<div
						class="bg-paper flex flex-col items-start justify-between gap-3 px-4 py-4 sm:px-5 sm:py-5 h-[8rem] sm:h-[9rem] text-ink"
					>
						<span class="font-mono text-[0.7rem] tracking-[0.2em] text-ink-subtle">
							{String.fromCharCode(65 + i)}
						</span>
						<span
							class="block text-sm sm:text-base leading-snug wrap-break-word font-medium [&_*]:!text-ink"
			use:fitText={{ min: 11, max: 18 }}
						>
							{@html normalizeQuizText(ans.answer)}
						</span>
					</div>
				{/if}
			{/each}
		</div>
	</div>
</div>
