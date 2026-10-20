<script lang="ts">
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { fly } from 'svelte/transition';
	import { normalizeQuizText } from '$lib/cma/text';

	interface Props {
		question: string;
		topic?: string;
		seconds?: number;
		onComplete?: () => void;
	}

	let { question, topic = '', seconds = 4, onComplete }: Props = $props();
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

<div class="h-dvh min-h-dvh w-full bg-paper flex flex-col items-center justify-center px-6 py-10">
	{#if topic}
		<p class="text-cyan text-xs font-semibold uppercase tracking-[0.28em] mb-6">{topic}</p>
	{/if}
	<h1
		class="font-display text-4xl sm:text-6xl md:text-7xl text-ink text-center max-w-5xl leading-[0.95] normal-case"
		in:fly={reduced ? { duration: 0 } : { y: 12, duration: 300 }}
	>
		{@html normalizeQuizText(question)}
	</h1>
	<div
		class="mt-12 h-1.5 w-full max-w-md rounded-full bg-elevated overflow-hidden"
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
