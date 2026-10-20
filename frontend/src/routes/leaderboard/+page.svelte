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

	navbarVisible.visible = true;

	/** Demo data until backend leagues API ships (Phase 3). */
	const weeklyRows: LedgerRow[] = [
		{ rank: 1, name: 'A. Okafor', score: '9,420', delta: 0 },
		{ rank: 2, name: 'M. Chen', score: '9,105', delta: 1 },
		{ rank: 3, name: 'You', score: '8,870', isYou: true, delta: 1 },
		{ rank: 4, name: 'J. Rivera', score: '8,640', delta: -1 },
		{ rank: 5, name: 'S. Patel', score: '8,510', delta: 0 }
	];

	const podium = [
		{ name: 'A. Okafor', score: '9,420 pts' },
		{ name: 'M. Chen', score: '9,105 pts' },
		{ name: 'You', score: '8,870 pts', subtitle: 'Top 12% this week' }
	];

	let tab: 'weekly' | 'alltime' = $state('weekly');
</script>

<svelte:head>
	<title>CMA-Clash — Leaderboard</title>
	<meta
		name="description"
		content="Weekly leagues and all-time rankings for CMA-Clash exam prep."
	/>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<main class="flex-1 max-w-3xl mx-auto w-full px-4 py-10">
		<h1 class="font-display text-3xl sm:text-4xl font-bold text-ink">Leaderboard</h1>
		<p class="text-ink-muted mt-2 mb-6">
			Weekly matched leagues reset every Monday. Full backend sync arrives in a later release.
		</p>

		<RetentionBar streakDays={5} dailyGoalPercent={60} leagueName="Emerald League" />

		<div class="flex gap-2 mt-8 mb-6" role="tablist" aria-label="Leaderboard period">
			<button
				type="button"
				role="tab"
				aria-selected={tab === 'weekly'}
				class="px-4 py-2 rounded-lg text-sm font-medium transition {tab === 'weekly'
					? 'bg-primary text-white'
					: 'bg-surface border border-ink/15 text-ink-muted hover:text-ink'}"
				onclick={() => (tab = 'weekly')}
			>
				Weekly league
			</button>
			<button
				type="button"
				role="tab"
				aria-selected={tab === 'alltime'}
				class="px-4 py-2 rounded-lg text-sm font-medium transition {tab === 'alltime'
					? 'bg-primary text-white'
					: 'bg-surface border border-ink/15 text-ink-muted hover:text-ink'}"
				onclick={() => (tab = 'alltime')}
			>
				All-time
			</button>
		</div>

		<Card class="mb-8">
			<Podium entries={podium} />
		</Card>

		<LedgerTable rows={weeklyRows} caption="Weekly league standings" />

		<p class="text-xs text-ink-muted text-center mt-6 font-mono">
			League resets in 4d 12h · Percentile: 88th
		</p>
	</main>
	<Footer />
</div>
