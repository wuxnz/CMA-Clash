<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import Card from '$lib/ui/Card.svelte';
	import LedgerTable from '$lib/ui/LedgerTable.svelte';
	import Podium from '$lib/ui/Podium.svelte';
	import RetentionBar from '$lib/ui/RetentionBar.svelte';
	import type { LedgerRow } from '$lib/ui/LedgerTable.svelte';
	import type { PageData } from './$types';
	import { fetchGamification } from '$lib/cma/client';
	import { onMount } from 'svelte';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	navbarVisible.visible = true;

	let tab: 'weekly' | 'alltime' = $state('weekly');
	let streakDays = $state(0);
	let usingDemo = $derived(!data.apiAvailable);

	let entries = $derived(tab === 'weekly' ? data.weekly : data.allTime);

	let rows = $derived.by((): LedgerRow[] => {
		return entries.map((e) => ({
			rank: e.rank,
			name: e.username,
			score: e.xp.toLocaleString()
		}));
	});

	let podium = $derived(
		rows.slice(0, 3).map((r) => ({
			name: r.name,
			score: `${r.score} XP`
		}))
	);

	onMount(async () => {
		const profile = await fetchGamification();
		if (profile) streakDays = profile.current_streak_days;
	});
</script>

<svelte:head>
	<title>CMA Clash: Leaderboard</title>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<main class="flex-1 max-w-3xl mx-auto w-full px-4 py-10">
		<h1 class="text-2xl font-semibold text-ink tracking-tight">Leaderboard</h1>
		<p class="text-sm text-ink-muted mt-1 mb-8">Weekly XP and all-time standings.</p>

		{#if usingDemo}
			<p class="text-sm text-ink-muted mb-4">Leaderboard scores aren't available right now.</p>
		{/if}

		<RetentionBar {streakDays} dailyGoalPercent={0} />

		<div class="flex gap-2 mt-8 mb-6" role="tablist">
			<button
				type="button"
				role="tab"
				aria-selected={tab === 'weekly'}
				class="min-h-11 px-4 py-2 rounded-lg text-sm font-medium {tab === 'weekly'
					? 'bg-primary text-white'
					: 'bg-surface border border-ink/15 text-ink-muted'}"
				onclick={() => (tab = 'weekly')}
			>
				Weekly
			</button>
			<button
				type="button"
				role="tab"
				aria-selected={tab === 'alltime'}
				class="min-h-11 px-4 py-2 rounded-lg text-sm font-medium {tab === 'alltime'
					? 'bg-primary text-white'
					: 'bg-surface border border-ink/15 text-ink-muted'}"
				onclick={() => (tab = 'alltime')}
			>
				All-time
			</button>
		</div>

		{#if rows.length === 0}
			<p class="text-sm text-ink-muted">No scores yet.</p>
		{:else}
			<Card class="mb-8">
				<Podium entries={podium} />
			</Card>
			<LedgerTable rows={rows} caption="League standings" flip={true} />
		{/if}
	</main>
	<Footer />
</div>
