<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import type { PageData } from './$types';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import Button from '$lib/ui/Button.svelte';

	navbarVisible.visible = true;
	const { t } = getLocalization();

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
</script>

<svelte:head>
	<title>CMA Clash — Results</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Results</h1>

		{#if data.results.length === 0}
			<p class="text-sm text-ink-muted mt-6">Host a game to see scores here.</p>
			<Button href="/host" class="w-auto mt-4">Host a Clash</Button>
		{:else}
			<div class="mt-6 overflow-x-auto min-w-0">
				<table class="w-full text-sm text-left min-w-[36rem]">
					<thead>
						<tr class="text-xs text-ink-muted border-b border-white/[0.07]">
							<th class="py-2 pr-3 font-medium">{$t('results_page.quiz_title')}</th>
							<th class="py-2 pr-3 font-medium">{$t('results_page.date_played')}</th>
							<th class="py-2 pr-3 font-medium">{$t('results_page.player_count')}</th>
							<th class="py-2 font-medium">{$t('words.note')}</th>
						</tr>
					</thead>
					<tbody>
						{#each data.results as result}
							<tr class="border-b border-white/[0.07]">
								<td class="py-3 pr-3 min-w-0">
									<a href="/results/{result.id}" class="text-ink link-hover visited:text-ink">
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
