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
	let boardLoading = $state(false);

	let entries = $derived(tab === 'weekly' ? weekly : allTime);

	let rows = $derived.by((): LedgerRow[] => {
		return entries.map((e) => ({
			rank: e.rank,
			name: e.level > 1 ? `${e.username} (Lv ${e.level})` : e.username,
			score: e.xp.toLocaleString(),
			isYou: e.is_you
		}));
	});

	let podium = $derived(
		rows.slice(0, 3).map((r) => ({
			name: r.name,
			score: `${r.score} XP`
		}))
	);

	onMount(async () => {
		boardLoading = true;
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
	<main class="flex-1 w-full px-4 sm:px-8 lg:px-12 max-w-[1200px] mx-auto py-16 lg:py-24">
		<div
			class="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4 border-b border-line pb-6"
		>
			<div>
				<p class="eyebrow">Standings</p>
				<h1
					class="font-display text-[clamp(2.4rem,7vw,4.6rem)] leading-[0.92] tracking-[-0.04em] mt-3"
				>
					Leader<b class="font-normal text-primary">board</b>
				</h1>
			</div>
			<p class="eyebrow text-right">Weekly XP and all-time standings</p>
		</div>

		<div class="mt-6">
			<RetentionBar {streakDays} dailyGoalPercent={0} />
		</div>

		<div class="flex gap-px bg-line border border-line mt-8 mb-8 w-fit" role="tablist">
			<button
				type="button"
				role="tab"
				aria-selected={tab === 'weekly'}
				class="min-h-11 px-5 py-2 font-mono text-[0.7rem] uppercase tracking-[0.18em] transition-colors {tab ===
				'weekly'
					? 'bg-primary text-white'
					: 'bg-paper text-ink-muted hover:bg-elevated'}"
				onclick={() => (tab = 'weekly')}
			>
				Weekly
			</button>
			<button
				type="button"
				role="tab"
				aria-selected={tab === 'alltime'}
				class="min-h-11 px-5 py-2 font-mono text-[0.7rem] uppercase tracking-[0.18em] transition-colors {tab ===
				'alltime'
					? 'bg-primary text-white'
					: 'bg-paper text-ink-muted hover:bg-elevated'}"
				onclick={() => (tab = 'alltime')}
			>
				All-time
			</button>
		</div>

		{#if boardLoading}
			<div
				class="animate-pulse space-y-3 mt-4"
				aria-busy="true"
				aria-label="Loading leaderboard"
			>
				{#each [1, 2, 3, 4, 5] as n (n)}
					<div class="h-10 bg-elevated"></div>
				{/each}
			</div>
		{:else if rows.length === 0}
			<p class="text-sm text-ink-muted">
				No one has earned XP yet. Play a game or battle while logged in to appear here.
			</p>
		{:else}
			<Card class="mb-8">
				<Podium entries={podium} />
			</Card>
			<LedgerTable {rows} caption="League standings" flip={true} />
		{/if}
	</main>
	<Footer />
</div>
