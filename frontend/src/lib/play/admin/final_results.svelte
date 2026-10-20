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
	}

	let { data = $bindable(), username, show_final_results }: Props = $props();

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
	<div class="min-h-dvh bg-paper flex flex-col">
		<div class="flex-1 px-4 py-8 max-w-2xl mx-auto w-full">
			<p class="font-display text-gold text-sm tracking-[0.3em] text-center mb-2">Final</p>
			<h1
				class="font-display text-5xl sm:text-6xl text-center text-ink mb-8"
				in:fly={reduced ? { duration: 0 } : { y: -20, duration: 400 }}
			>
				Podium
			</h1>

			{#if player_names.length === 0}
				<p class="text-center text-lg text-ink-muted">{$t('admin_page.no_answers')}</p>
			{:else}
				<Podium entries={podiumEntries} staged celebrate />

				{#if player_names.length > 3}
					<ol class="mt-8 space-y-2 border-t border-ink/10 pt-6">
						{#each player_names.slice(3, 8) as player, i}
							<li
								class="flex justify-between font-mono text-sm tabular-nums px-2 py-1 rounded {player ===
								username
									? 'bg-primary/10 font-semibold'
									: ''}"
							>
								<span>{i + 4}. {player === username ? 'You' : player}</span>
								<span>{data[player]}</span>
							</li>
						{/each}
					</ol>
				{/if}
			{/if}

			{#if data[username]}
				<div
					class="mt-10 rounded-xl border-2 border-gold/40 bg-gold/10 p-4 text-center shadow-sm"
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
	</div>
{/if}
