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

	type Place = '1' | '2' | '3';

	interface Props {
		entries: PodiumEntry[];
		/** Confetti after staged reveal (final game podium only). */
		celebrate?: boolean;
		/** 3-2-1 countdown then reveal 3rd → 2nd → 1st. */
		staged?: boolean;
		/** Tighter layout for phone host / small viewports. */
		compact?: boolean;
	}

	let { entries, celebrate = false, staged = false, compact = false }: Props = $props();

	let reduced = prefersReducedMotion();
	let phase = $state<'countdown' | 'reveal' | 'done'>('reveal');
	let countdown = $state(3);
	let showThird = $state(true);
	let showSecond = $state(true);
	let showFirst = $state(true);

	let first = $derived(entries[0]);
	let second = $derived(entries[1]);
	let third = $derived(entries[2]);

	/** 1st tallest, 2nd mid, 3rd shortest — same step ratio in compact and full layouts. */
	let pedestal = $derived(
		compact
			? {
					first: 'h-14 sm:h-28',
					second: 'h-11 sm:h-[5.5rem]',
					third: 'h-9 sm:h-20'
				}
			: {
					first: 'h-32 sm:h-36',
					second: 'h-24 sm:h-28',
					third: 'h-[4.5rem] sm:h-20'
				}
	);

	type Column = {
		place: Place;
		entry: PodiumEntry;
		visible: boolean;
		heightClass: string;
		flyY: number;
		flyDelay?: number;
	};

	let columns = $derived.by((): Column[] => {
		const cols: Column[] = [];
		if (second)
			cols.push({
				place: '2',
				entry: second,
				visible: showSecond,
				heightClass: pedestal.second,
				flyY: 40
			});
		if (first)
			cols.push({
				place: '1',
				entry: first,
				visible: showFirst,
				heightClass: pedestal.first,
				flyY: 60
			});
		if (third)
			cols.push({
				place: '3',
				entry: third,
				visible: showThird,
				heightClass: pedestal.third,
				flyY: 40,
				flyDelay: 100
			});
		return cols;
	});

	async function fireConfetti() {
		if (!browser || !celebrate || reduced) return;
		const confetti = (await import('canvas-confetti')).default;
		confetti({
			particleCount: 90,
			spread: 75,
			origin: { y: 0.62 },
			colors: ['#C8FF2E', '#7B5CFF', '#FF3B5C', '#22D3EE']
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

<div
	class="relative flex flex-col items-center px-2 sm:px-4 {compact
		? 'gap-2 py-1'
		: 'gap-6 py-8'}"
	aria-label="Final standings"
	data-testid="podium-root"
>
	<div
		class="pointer-events-none absolute inset-0"
		style="background: radial-gradient(ellipse at 50% 70%, rgba(200,255,46,0.18), transparent 55%);"
		aria-hidden="true"
	></div>
	{#if phase === 'countdown' && !reduced}
		<p
			class="font-display font-bold text-primary tabular-nums {compact
				? 'text-4xl'
				: 'text-6xl'}"
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

	<div
		class="grid grid-cols-3 w-full mx-auto items-end {compact
			? 'gap-1.5 max-w-[17.5rem] sm:max-w-lg'
			: 'gap-3 sm:gap-5 max-w-md sm:max-w-lg'}"
	>
		{#each columns as col (col.place)}
			{#if col.visible}
				<div
					class="flex flex-col items-center min-w-0 w-full"
					in:fly={reduced ? { duration: 0 } : { y: col.flyY, delay: col.flyDelay ?? 0, duration: 500 }}
				>
					<div
						class="w-full shrink-0 text-center mb-1 sm:mb-2 {compact
							? 'min-h-[2rem] sm:min-h-[2.5rem]'
							: 'min-h-[2.75rem] sm:min-h-[3.25rem]'}"
					>
						<p
							class="font-display text-ink truncate w-full px-0.5 {col.place === '1'
								? 'font-bold'
								: 'font-semibold'} {compact
								? 'text-[11px] sm:text-sm'
								: 'text-sm sm:text-base'}"
							title={col.entry.name}
						>
							{col.entry.name}
						</p>
						<p
							class="font-mono text-ink-muted tabular-nums {compact
								? 'text-[10px] sm:text-xs'
								: 'text-xs sm:text-sm'}"
						>
							{col.entry.score}
						</p>
						{#if col.place === '1' && col.entry.subtitle}
							<p class="text-[10px] sm:text-xs text-ink-muted truncate w-full px-0.5">
								{col.entry.subtitle}
							</p>
						{/if}
					</div>
					<div
						data-testid="podium-pedestal-{col.place}"
						class="w-full box-border rounded-t-lg sm:rounded-t-xl flex flex-col justify-end text-center shadow-sm border-2 {col.heightClass} {col.place ===
						'1'
							? 'bg-gold/20 border-gold shadow-md relative overflow-hidden'
							: 'bg-surface border-transparent'}"
					>
						{#if col.place === '1'}
							<div class="absolute inset-x-0 top-0 h-0.5 sm:h-1 bg-gold" aria-hidden="true"></div>
						{/if}
						<p
							class="font-mono font-bold pb-1 sm:pb-2 {col.place === '1'
								? 'text-gold'
								: 'text-ink-muted'} {compact
								? col.place === '1'
									? 'text-xl sm:text-3xl'
									: 'text-lg sm:text-2xl'
								: col.place === '1'
									? 'text-3xl sm:text-4xl'
									: 'text-2xl sm:text-3xl'}"
						>
							{col.place}
						</p>
					</div>
				</div>
			{:else}
				<div class="min-w-0 w-full" aria-hidden="true"></div>
			{/if}
		{/each}
	</div>
</div>
