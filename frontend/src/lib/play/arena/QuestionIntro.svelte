<script lang="ts">
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { fly } from 'svelte/transition';
	import { normalizeQuizText } from '$lib/cma/text';

	interface Props {
		question: string;
		topic?: string;
		seconds?: number;
		onComplete?: () => void;
		/** Fit inside host admin shell (no full-viewport height). */
		hostFit?: boolean;
	}

	let { question, topic = '', seconds = 4, onComplete, hostFit = false }: Props = $props();
	const reduced = prefersReducedMotion();

	let remaining = $state(seconds);
	$effect(() => {
		if (reduced) {
			onComplete?.();
			return;
		}
		remaining = seconds;
		const id = setInterval(() => {
			remaining -= 1;
			if (remaining <= 0) {
				clearInterval(id);
				onComplete?.();
			}
		}, 1000);
		return () => clearInterval(id);
	});

	let progress = $derived(seconds > 0 ? remaining / seconds : 0);
</script>

<div
	class="w-full bg-paper flex flex-col items-center justify-center px-4 sm:px-6 {hostFit
		? 'h-full min-h-0 py-6 sm:py-10'
		: 'h-dvh min-h-dvh py-10'}"
>
	{#if topic}
		<p
			class="text-cyan text-xs font-semibold uppercase tracking-[0.28em] mb-4 sm:mb-6 text-center line-clamp-2"
		>
			{topic}
		</p>
	{/if}
	<h1
		class="font-display text-ink text-center max-w-5xl leading-[0.95] normal-case {hostFit
			? 'text-2xl sm:text-4xl md:text-5xl'
			: 'text-4xl sm:text-6xl md:text-7xl'}"
		in:fly={reduced ? { duration: 0 } : { y: 12, duration: 300 }}
	>
		{@html normalizeQuizText(question)}
	</h1>
	<div
		class="mt-6 sm:mt-12 h-1.5 w-full max-w-md rounded-full bg-elevated overflow-hidden"
		role="progressbar"
		aria-valuenow={remaining}
		aria-valuemin={0}
		aria-valuemax={seconds}
		aria-label="Read timer"
	>
		<div
			class="h-full bg-gold rounded-full"
			style="width: {progress * 100}%; transition: {reduced ? 'none' : 'width 1s linear'}"
		></div>
	</div>
</div>
