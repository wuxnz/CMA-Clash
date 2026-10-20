<script lang="ts">
	import { onMount } from 'svelte';
	import { prefersReducedMotion } from './motion';
	import { scale } from 'svelte/transition';

	interface Props {
		from?: number;
		onComplete?: () => void;
	}

	let { from = 3, onComplete }: Props = $props();

	let current = $state(from);
	let reduced = prefersReducedMotion();

	onMount(() => {
		if (reduced) {
			onComplete?.();
			return;
		}
		const id = setInterval(() => {
			current -= 1;
			if (current <= 0) {
				clearInterval(id);
				onComplete?.();
			}
		}, 1000);
		return () => clearInterval(id);
	});
</script>

{#if !reduced && current > 0}
	<div
		class="fixed inset-0 z-50 flex items-center justify-center bg-ink/70 backdrop-blur-sm"
		role="status"
		aria-live="assertive"
		aria-label="Countdown"
	>
		{#key current}
			<span
				class="font-display font-bold text-8xl sm:text-9xl text-gold tabular-nums"
				in:scale={{ duration: 300 }}
				out:scale={{ duration: 150 }}
			>
				{current}
			</span>
		{/key}
	</div>
{/if}
