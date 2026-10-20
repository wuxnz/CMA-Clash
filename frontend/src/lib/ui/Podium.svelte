<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import { prefersReducedMotion } from './motion';
	import { fade, fly } from 'svelte/transition';
	import { Trophy } from '@lucide/svelte';

	export type PodiumEntry = {
		name: string;
		score: number | string;
		subtitle?: string;
	};

	interface Props {
		entries: PodiumEntry[];
		/** Confetti after staged reveal (final game podium only). */
		celebrate?: boolean;
		/** 3-2-1 countdown then reveal 3rd → 2nd → 1st. */
		staged?: boolean;
	}

	let { entries, celebrate = false, staged = false }: Props = $props();

	let reduced = prefersReducedMotion();
	let phase = $state<'countdown' | 'reveal' | 'done'>('reveal');
	let countdown = $state(3);
	let showThird = $state(true);
	let showSecond = $state(true);
	let showFirst = $state(true);

	let first = $derived(entries[0]);
	let second = $derived(entries[1]);
	let third = $derived(entries[2]);

	async function fireConfetti() {
		if (!browser || !celebrate || reduced) return;
		const confetti = (await import('canvas-confetti')).default;
		confetti({
			particleCount: 90,
			spread: 75,
			origin: { y: 0.62 },
			colors: ['#0ea5e9', '#e8b931', '#f1f5f9']
		});
		setTimeout(
			() => confetti({ particleCount: 45, angle: 60, spread: 55, origin: { x: 0 } }),
			220
		);
		setTimeout(
			() => confetti({ particleCount: 45, angle: 120, spread: 55, origin: { x: 1 } }),
			220
		);
	}

	onMount(() => {
		if (!staged || reduced) {
			phase = 'done';
			if (celebrate) fireConfetti();
			return;
		}
		phase = 'countdown';
		showThird = false;
		showSecond = false;
		showFirst = false;
		const timers: ReturnType<typeof setTimeout>[] = [];
		timers.push(
			setTimeout(() => {
				countdown = 2;
			}, 700)
		);
		timers.push(
			setTimeout(() => {
				countdown = 1;
			}, 1400)
		);
		timers.push(
			setTimeout(() => {
				phase = 'reveal';
				showThird = true;
			}, 2100)
		);
		timers.push(
			setTimeout(() => {
				showSecond = true;
			}, 2800)
		);
		timers.push(
			setTimeout(() => {
				showFirst = true;
				phase = 'done';
				fireConfetti();
			}, 3500)
		);
		return () => timers.forEach(clearTimeout);
	});
</script>

<div class="flex flex-col items-center gap-6 py-8 px-4" aria-label="Final standings">
	{#if phase === 'countdown' && !reduced}
		<p
			class="font-display text-6xl font-bold text-primary tabular-nums"
			in:fade={{ duration: 200 }}
			aria-live="polite"
		>
			{countdown}
		</p>
	{:else if !reduced}
		<div class="flex items-center gap-2 text-gold" in:fade={{ duration: 300 }}>
			<Trophy class="w-5 h-5" aria-hidden="true" />
			<div class="h-1 w-24 rounded-full bg-gold/60" aria-hidden="true"></div>
		</div>
	{/if}

	<div class="flex items-end justify-center gap-3 sm:gap-6 w-full max-w-lg min-h-[10rem]">
		{#if second && showSecond}
			<div
				class="flex flex-col items-center flex-1 max-w-[8rem]"
				in:fly={reduced ? { duration: 0 } : { y: 40, duration: 500 }}
			>
				<div
					class="w-full rounded-t-xl bg-surface border border-ink/10 px-2 py-3 text-center shadow-sm h-20 sm:h-24 flex flex-col justify-end"
				>
					<p class="font-mono text-2xl text-ink-muted">2</p>
				</div>
				<p class="mt-2 font-display font-semibold text-ink text-sm truncate w-full text-center">
					{second.name}
				</p>
				<p class="font-mono text-xs text-ink-muted tabular-nums">{second.score}</p>
			</div>
		{/if}
		{#if first && showFirst}
			<div
				class="flex flex-col items-center flex-1 max-w-[9rem]"
				in:fly={reduced ? { duration: 0 } : { y: 60, duration: 600 }}
			>
				<div
					class="w-full rounded-t-xl bg-gold/20 border-2 border-gold px-2 py-4 text-center shadow-md h-28 sm:h-32 flex flex-col justify-end relative overflow-hidden"
				>
					<div class="absolute inset-x-0 top-0 h-1 bg-gold" aria-hidden="true"></div>
					<p class="font-mono text-3xl text-gold font-bold">1</p>
				</div>
				<p class="mt-2 font-display font-bold text-ink truncate w-full text-center">
					{first.name}
				</p>
				<p class="font-mono text-sm text-ink tabular-nums">{first.score}</p>
				{#if first.subtitle}
					<p class="text-xs text-ink-muted text-center">{first.subtitle}</p>
				{/if}
			</div>
		{/if}
		{#if third && showThird}
			<div
				class="flex flex-col items-center flex-1 max-w-[8rem]"
				in:fly={reduced ? { duration: 0 } : { y: 40, delay: 100, duration: 500 }}
			>
				<div
					class="w-full rounded-t-xl bg-surface border border-ink/10 px-2 py-3 text-center shadow-sm h-20 sm:h-24 flex flex-col justify-end"
				>
					<p class="font-mono text-2xl text-ink-muted">3</p>
				</div>
				<p class="mt-2 font-display font-semibold text-ink text-sm truncate w-full text-center">
					{third.name}
				</p>
				<p class="font-mono text-xs text-ink-muted tabular-nums">{third.score}</p>
			</div>
		{/if}
	</div>
</div>
