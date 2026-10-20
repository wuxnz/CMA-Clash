<script lang="ts">
	import { prefersReducedMotion } from './motion';
	import { fade, fly } from 'svelte/transition';

	export type PodiumEntry = {
		name: string;
		score: number | string;
		subtitle?: string;
	};

	interface Props {
		entries: PodiumEntry[];
	}

	let { entries }: Props = $props();

	let reduced = prefersReducedMotion();

	let first = $derived(entries[0]);
	let second = $derived(entries[1]);
	let third = $derived(entries[2]);
</script>

<div class="flex flex-col items-center gap-6 py-8 px-4" aria-label="Final standings">
	{#if !reduced}
		<div
			class="h-1 w-24 rounded-full bg-gold/60"
			in:fade={{ duration: 400 }}
			aria-hidden="true"
		></div>
	{/if}
	<div class="flex items-end justify-center gap-3 sm:gap-6 w-full max-w-lg">
		{#if second}
			<div
				class="flex flex-col items-center flex-1 max-w-[8rem]"
				in:fly={reduced ? { duration: 0 } : { y: 40, delay: 200, duration: 500 }}
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
		{#if first}
			<div
				class="flex flex-col items-center flex-1 max-w-[9rem]"
				in:fly={reduced ? { duration: 0 } : { y: 60, delay: 0, duration: 600 }}
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
		{#if third}
			<div
				class="flex flex-col items-center flex-1 max-w-[8rem]"
				in:fly={reduced ? { duration: 0 } : { y: 30, delay: 350, duration: 500 }}
			>
				<div
					class="w-full rounded-t-xl bg-surface border border-ink/10 px-2 py-2 text-center shadow-sm h-16 sm:h-20 flex flex-col justify-end"
				>
					<p class="font-mono text-xl text-ink-muted">3</p>
				</div>
				<p class="mt-2 font-display font-semibold text-ink text-sm truncate w-full text-center">
					{third.name}
				</p>
				<p class="font-mono text-xs text-ink-muted tabular-nums">{third.score}</p>
			</div>
		{/if}
	</div>
</div>
