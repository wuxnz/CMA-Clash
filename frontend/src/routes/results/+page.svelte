<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { resolve } from '$app/paths';
	import type { PageData } from './$types';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import Button from '$lib/ui/Button.svelte';
	import { onMount } from 'svelte';

	navbarVisible.visible = true;
	const { t } = getLocalization();

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
	let results = $state(data.results);
	let resultsLoading = $state(true);

	onMount(async () => {
		try {
			const res = await fetch('/api/v1/results/list?include_quiz=true');
			if (res.ok) {
				results = await res.json();
			}
		} finally {
			resultsLoading = false;
		}
	});
</script>

<svelte:head>
	<title>CMA Clash — Results</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 pb-20 min-w-0 flex-1">
		<div class="border-b border-line pb-6">
			<p class="eyebrow">Archive</p>
			<h1
				class="font-display text-[clamp(2.2rem,6vw,4rem)] leading-[0.92] tracking-[-0.04em] mt-3"
			>
				Session <b class="font-normal text-primary">results</b>
			</h1>
		</div>

		{#if resultsLoading}
			<p class="text-sm text-ink-muted mt-6" aria-busy="true">Loading results…</p>
		{:else if results.length === 0}
			<p class="text-sm text-ink-muted mt-6">Host a game to see scores here.</p>
			<Button href="/host" class="w-auto mt-4">Host a Clash</Button>
		{:else}
			<div class="mt-6 overflow-x-auto min-w-0">
				<table class="w-full text-sm text-left min-w-[36rem]">
					<thead>
						<tr class="text-ink-subtle border-b border-line">
							<th
								class="py-2.5 pr-3 font-mono font-normal text-[0.64rem] uppercase tracking-[0.2em]"
								>{$t('results_page.quiz_title')}</th
							>
							<th
								class="py-2.5 pr-3 font-mono font-normal text-[0.64rem] uppercase tracking-[0.2em]"
								>{$t('results_page.date_played')}</th
							>
							<th
								class="py-2.5 pr-3 font-mono font-normal text-[0.64rem] uppercase tracking-[0.2em]"
								>{$t('results_page.player_count')}</th
							>
							<th
								class="py-2.5 font-mono font-normal text-[0.64rem] uppercase tracking-[0.2em]"
								>{$t('words.note')}</th
							>
						</tr>
					</thead>
					<tbody>
						{#each results as result (result.id)}
							<tr class="border-b border-line transition-colors hover:bg-elevated">
								<td class="py-3 pr-3 min-w-0">
									<a
										href={resolve('/results/[result_id]', { result_id: result.id })}
										class="text-ink link-hover visited:text-ink"
									>
										{@html result.title}
									</a>
								</td>
								<td class="py-3 pr-3 text-ink-muted tabular-nums whitespace-nowrap">
									{new Date(result.timestamp).toLocaleString()}
								</td>
								<td class="py-3 pr-3 text-ink-muted tabular-nums">
									{Object.keys(result.player_scores).length}
								</td>
								<td class="py-3 text-ink-muted">{result.note ?? ''}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</div>
	<Footer />
</div>
