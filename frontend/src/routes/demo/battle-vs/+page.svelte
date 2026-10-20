<!-- Static battle VS + countdown for marketing captures (no API). -->
<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import CountdownRing from '$lib/ui/CountdownRing.svelte';
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { fly } from 'svelte/transition';

	navbarVisible.visible = false;
	const reduced = prefersReducedMotion();
	let phase = $state<'vs' | 'countdown'>('vs');

	function startCountdown() {
		phase = 'countdown';
	}
</script>

<div
	class="min-h-screen bg-paper text-ink flex flex-col items-center justify-center px-4 relative overflow-hidden"
>
	<div
		class="absolute inset-0 bg-gradient-to-b from-primary/20 to-transparent pointer-events-none"
		aria-hidden="true"
	></div>

	{#if phase === 'countdown'}
		<CountdownRing seconds={5} label="Battle starts" />
	{:else}
		<div
			class="relative z-10 text-center max-w-lg w-full"
			in:fly={reduced ? { duration: 0 } : { y: 30 }}
		>
			<p class="text-sm uppercase tracking-[0.3em] text-gold mb-8">Arena</p>
			<div class="flex items-center justify-center gap-4 sm:gap-8">
				<div class="flex-1">
					<p class="font-display text-2xl sm:text-4xl font-bold truncate">You</p>
				</div>
				<p class="font-display text-3xl text-gold font-black">VS</p>
				<div class="flex-1">
					<p class="font-display text-2xl sm:text-4xl font-bold truncate">M. Chen</p>
				</div>
			</div>
			<button
				type="button"
				class="mt-12 ledger-btn-primary w-auto px-8 mx-auto"
				onclick={startCountdown}
			>
				Preview countdown
			</button>
		</div>
	{/if}
</div>
