<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { fly } from 'svelte/transition';
	import Podium from '$lib/ui/Podium.svelte';
	import AnimatedCounter from '$lib/ui/AnimatedCounter.svelte';
	import type { PodiumEntry } from '$lib/ui/Podium.svelte';
	import { prefersReducedMotion } from '$lib/ui/motion';

	const { t } = getLocalization();

	interface Props {
		data: any;
		username?: any;
		show_final_results: boolean;
		/** Host admin: fit phone viewport with scroll only on ranks 4+. */
		hostLayout?: boolean;
		/** Optional line under the Podium title (e.g. battle winner / tie). */
		outcomeNote?: string;
		actions?: import('svelte').Snippet;
	}

	let {
		data = $bindable(),
		username,
		show_final_results,
		hostLayout = false,
		outcomeNote,
		actions
	}: Props = $props();

	let player_names = $derived(
		Object.keys(data).sort((a, b) => {
			const scoreA = parseFloat(data[a]) || 0;
			const scoreB = parseFloat(data[b]) || 0;
			return scoreB - scoreA;
		})
	);

	let podiumEntries = $derived.by((): PodiumEntry[] => {
		return player_names.slice(0, 3).map((name) => ({
			name: name === username ? 'You' : name,
			score: data[name]
		}));
	});

	let reduced = prefersReducedMotion();

	function scoreNumber(raw: string | number): number {
		if (typeof raw === 'number') return raw;
		const n = parseFloat(String(raw).replace(/,/g, ''));
		return Number.isFinite(n) ? n : 0;
	}
</script>

{#if show_final_results}
	<div
		data-testid="host-final-podium"
		class:bg-paper={!hostLayout}
		class="flex flex-col w-full {hostLayout
			? 'h-full min-h-0 overflow-hidden'
			: 'min-h-dvh bg-paper'}"
	>
		<div
			class="flex flex-col w-full max-w-2xl mx-auto min-h-0 {hostLayout
				? 'flex-1 px-3 pt-3 pb-2'
				: 'flex-1 px-4 py-8'}"
		>
			<header class="shrink-0 text-center {hostLayout ? 'mb-2' : 'mb-8'}">
				<p
					class="font-display text-gold tracking-[0.3em] {hostLayout
						? 'text-[10px] sm:text-sm'
						: 'text-sm mb-2'}"
				>
					Final
				</p>
				<h1
					class="font-display text-center text-ink {hostLayout
						? 'text-2xl sm:text-5xl'
						: 'text-5xl sm:text-6xl'}"
					in:fly={reduced ? { duration: 0 } : { y: -20, duration: 400 }}
				>
					Podium
				</h1>
				{#if outcomeNote}
					<p
						class="mt-2 font-mono text-sm sm:text-base text-ink-muted"
						data-testid="battle-final-outcome"
					>
						{outcomeNote}
					</p>
				{/if}
			</header>

			{#if player_names.length === 0}
				<p class="text-center text-lg text-ink-muted">{$t('admin_page.no_answers')}</p>
			{:else}
				<div class="shrink-0">
					<Podium
						entries={podiumEntries}
						staged={!hostLayout}
						celebrate={!hostLayout}
						compact={hostLayout}
					/>
				</div>

				{#if player_names.length > 3}
					<div
						class="{hostLayout
							? 'flex-1 min-h-0 overflow-y-auto mt-2 border-t border-ink/10 pt-2'
							: 'mt-8 border-t border-ink/10 pt-6'}"
					>
						<ol class="space-y-0.5 sm:space-y-2">
							{#each player_names.slice(3) as player, i}
								<li
									class="flex justify-between font-mono tabular-nums px-2 rounded {hostLayout
										? 'text-xs py-1'
										: 'text-sm py-1'} {player === username
										? 'bg-primary/10 font-semibold'
										: ''}"
								>
									<span class="truncate pr-2"
										>{i + 4}. {player === username ? 'You' : player}</span
									>
									<span class="shrink-0">{data[player]}</span>
								</li>
							{/each}
						</ol>
					</div>
				{/if}
			{/if}

			{#if !hostLayout && data[username]}
				<div
					class="mt-10 rounded-xl border-2 border-gold/40 bg-gold/10 p-4 text-center shadow-sm shrink-0"
				>
					<p class="font-mono text-lg tabular-nums">
						Your score:
						<AnimatedCounter class="font-semibold" value={scoreNumber(data[username])} duration={1} />
					</p>
					{#each player_names as player, i}
						{#if player === username}
							<p class="text-ink-muted mt-1">
								{$t('play_page.your_place', { place: i + 1 })}
							</p>
						{/if}
					{/each}
				</div>
			{/if}
		</div>

		{#if hostLayout && actions}
			<footer
				class="shrink-0 border-t border-white/10 bg-surface/95 backdrop-blur-md px-3 py-3 safe-bottom flex flex-wrap gap-2 justify-center"
			>
				{@render actions()}
			</footer>
		{/if}
	</div>
{/if}

<style>
	.safe-bottom {
		padding-bottom: max(0.75rem, env(safe-area-inset-bottom));
	}
</style>
