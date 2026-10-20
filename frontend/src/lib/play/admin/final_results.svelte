<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { onMount } from 'svelte';
	import { getLocalization } from '$lib/i18n';
	import { fly } from 'svelte/transition';
	import confetti from 'canvas-confetti';
	import Podium from '$lib/ui/Podium.svelte';
	import type { PodiumEntry } from '$lib/ui/Podium.svelte';
	import { prefersReducedMotion } from '$lib/ui/motion';
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';

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

	let canvas: HTMLCanvasElement = $state();
	let reduced = prefersReducedMotion();

	onMount(() => {
		if (reduced || !show_final_results) return;
		setTimeout(() => {
			if (!canvas) return;
			confetti.create(canvas, { resize: true, useWorker: true });
			confetti({ particleCount: 120, spread: 100, colors: ['#E8B931', '#0E7C74', '#0E1A2B'] });
		}, 600);
	});
</script>

{#if show_final_results}
	<canvas bind:this={canvas} class="fixed inset-0 pointer-events-none z-50" aria-hidden="true"
	></canvas>
	<div class="min-h-screen bg-paper flex flex-col">
		<LivePlayHeader />
		<div class="flex-1 px-4 py-8 max-w-2xl mx-auto w-full">
			<h1
				class="font-display text-3xl sm:text-4xl font-bold text-center text-ink mb-2"
				in:fly={reduced ? { duration: 0 } : { y: -20, duration: 400 }}
			>
				{$t('play_page.end_sentence')}
			</h1>
			<p class="text-center text-ink-muted mb-8">Final standings</p>

			{#if player_names.length === 0}
				<p class="text-center text-lg text-ink-muted">{$t('admin_page.no_answers')}</p>
			{:else}
				<Podium entries={podiumEntries} />

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
						{$t('play_page.your_score', { score: data[username] })}
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
