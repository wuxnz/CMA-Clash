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
	import type { LeaderboardEntry } from '$lib/cma/client';
	import { fetchGamification } from '$lib/cma/client';
	import { kitOrBackendFetch } from '$lib/server-api';
	import { onMount } from 'svelte';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	navbarVisible.visible = true;

	let tab: 'weekly' | 'alltime' = $state('weekly');
	let streakDays = $state(0);
	let weekly = $state<LeaderboardEntry[]>(data.weekly);
	let allTime = $state<LeaderboardEntry[]>(data.allTime);
	let boardLoading = $state(true);
	let usingDemo = $derived(!boardLoading && weekly.length === 0 && allTime.length === 0);

	let entries = $derived(tab === 'weekly' ? weekly : allTime);

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
		async function loadBoard(period: 'weekly' | 'all_time'): Promise<LeaderboardEntry[]> {
			const res = await kitOrBackendFetch(
				fetch,
				`/api/v1/clash/leaderboards?period=${period}&limit=50`,
				{ credentials: 'include' }
			);
			if (!res?.ok) return [];
			return res.json();
		}
		try {
			const [w, a] = await Promise.all([loadBoard('weekly'), loadBoard('all_time')]);
			weekly = w;
			allTime = a;
		} finally {
			boardLoading = false;
		}
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

		{#if boardLoading}
			<div class="animate-pulse space-y-3 mt-4" aria-busy="true" aria-label="Loading leaderboard">
				{#each [1, 2, 3, 4, 5] as n (n)}
					<div class="h-10 rounded-lg bg-elevated"></div>
				{/each}
			</div>
		{:else if rows.length === 0}
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
