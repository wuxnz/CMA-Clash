<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import SearchCard from '$lib/search-card.svelte';
	import type { PageData } from './$types';
	import { postSearchClient } from '$lib/cma/search-api';
	import { onMount } from 'svelte';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let results = $state(data.results);
	let exploreError = $state('');
	let exploreLoading = $state(data.exploreSsrFailed && !results?.hits?.length);

	onMount(async () => {
		if (results?.hits?.length) return;
		exploreLoading = true;
		exploreError = '';
		const data = await postSearchClient({ q: '*', sort: ['created_at:desc'] });
		exploreLoading = false;
		if (data) {
			results = data;
		} else if (!results?.hits?.length) {
			exploreError = 'Could not load quizzes from the API.';
		}
	});
</script>

<svelte:head>
	<title>CMA Clash — Explore</title>
</svelte:head>

{#if exploreLoading}
	<p class="text-ink-muted text-sm px-4">Loading quizzes…</p>
{:else if exploreError}
	<div class="px-4 flex flex-wrap items-center gap-3">
		<p class="text-danger text-sm">{exploreError}</p>
		<button
			type="button"
			class="action-button text-sm px-4 py-2"
			onclick={async () => {
				exploreLoading = true;
				exploreError = '';
				const data = await postSearchClient({ q: '*', sort: ['created_at:desc'] });
				exploreLoading = false;
				if (data) results = data;
				else exploreError = 'Could not load quizzes from the API.';
			}}
		>
			Retry
		</button>
	</div>
{/if}
<div class="grid lg:grid-cols-3 grid-cols-1">
	{#each results?.hits ?? [] as quiz}
		<SearchCard {quiz} />
	{/each}
</div>
