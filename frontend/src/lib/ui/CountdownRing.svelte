<script lang="ts">
	import { onMount } from 'svelte';
	import { prefersReducedMotion } from './motion';

	interface Props {
		seconds?: number;
		onComplete?: () => void;
		label?: string;
	}

	let { seconds = 5, onComplete, label = 'Starting' }: Props = $props();

	let remaining = $state(seconds);
	let reduced = prefersReducedMotion();
	const circumference = 2 * Math.PI * 54;

	onMount(() => {
		if (reduced) {
			onComplete?.();
			return;
		}
		const id = setInterval(() => {
			remaining -= 1;
			if (remaining <= 0) {
				clearInterval(id);
				onComplete?.();
			}
		}, 1000);
		return () => clearInterval(id);
	});

	let progress = $derived(remaining / seconds);
</script>

<div class="flex flex-col items-center gap-3" role="status" aria-live="polite">
	<p class="text-sm font-medium text-ink-muted uppercase tracking-wider">{label}</p>
	<div class="relative w-32 h-32">
		<svg class="w-full h-full -rotate-90" viewBox="0 0 120 120" aria-hidden="true">
			<circle cx="60" cy="60" r="54" fill="none" stroke="currentColor" stroke-width="8" class="text-paper-muted" />
			<circle
				cx="60"
				cy="60"
				r="54"
				fill="none"
				stroke="currentColor"
				stroke-width="8"
				stroke-linecap="round"
				class="text-primary transition-all duration-1000 motion-reduce:transition-none"
				stroke-dasharray={circumference}
				stroke-dashoffset={circumference * (1 - progress)}
			/>
		</svg>
		<span
			class="absolute inset-0 flex items-center justify-center font-display text-4xl font-bold text-ink tabular-nums"
		>
			{Math.max(0, remaining)}
		</span>
	</div>
</div>
