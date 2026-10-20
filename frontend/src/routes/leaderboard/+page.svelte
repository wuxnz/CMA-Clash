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

	/** DEMO_FALLBACK: sample rows when leaderboard API returns empty (no scored players yet). */
	const DEMO_WEEKLY: LedgerRow[] = [
		{ rank: 1, name: 'A. Okafor', score: '9,420' },
		{ rank: 2, name: 'M. Chen', score: '9,105' },
		{ rank: 3, name: 'You', score: '8,870', isYou: true }
	];

	let tab: 'weekly' | 'alltime' = $state('weekly');
	let streakDays = $state(0);
	let usingDemo = $derived(!data.apiAvailable);

	let entries = $derived(tab === 'weekly' ? data.weekly : data.allTime);

	let rows = $derived.by((): LedgerRow[] => {
		if (entries.length === 0) {
			return DEMO_WEEKLY;
		}
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
	<title>CMA-Clash — Leaderboard</title>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<div class="flex-1 max-w-3xl mx-auto w-full px-4 py-10">
		<h1 class="font-display text-3xl sm:text-4xl font-bold text-ink">Leaderboard</h1>
		<p class="text-ink-muted mt-2 mb-6">
			Weekly and all-time XP from <code class="font-mono text-xs">/api/v1/clash/leaderboards</code>.
		</p>

		{#if usingDemo}
			<p class="text-sm text-gold bg-gold/10 border border-gold/30 rounded-lg px-3 py-2 mb-4" data-demo-label="true">
				No leaderboard scores in the database yet — showing demo standings below.
			</p>
		{/if}

		<RetentionBar {streakDays} dailyGoalPercent={0} leagueName="Weekly league" leagueIsDemo={usingDemo} />

		<div class="flex gap-2 mt-8 mb-6" role="tablist">
			<button
				type="button"
				role="tab"
				aria-selected={tab === 'weekly'}
				class="px-4 py-2 rounded-lg text-sm font-medium transition {tab === 'weekly'
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
				class="px-4 py-2 rounded-lg text-sm font-medium transition {tab === 'alltime'
					? 'bg-primary text-white'
					: 'bg-surface border border-ink/15 text-ink-muted'}"
				onclick={() => (tab = 'alltime')}
			>
				All-time
			</button>
		</div>

		<Card class="mb-8">
			<Podium entries={podium} />
		</Card>

		<LedgerTable rows={rows} caption="League standings" />
	</div>
	<Footer />
</div>
