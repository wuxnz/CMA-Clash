<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->
<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	const { t } = getLocalization();
	import SearchCard from '$lib/search-card.svelte';
	import { onMount } from 'svelte';
	import { postSearchClient, type SearchResponse } from '$lib/cma/search-api';

	let search_term = $state('');
	let resp_data = $state<SearchResponse | null>(null);
	let searchLoading = $state(false);
	let searchError = $state('');

	const submit = async () => {
		if (search_term.length <= 2) {
			return;
		}
		searchLoading = true;
		searchError = '';
		const data = await postSearchClient({
			q: search_term,
			attributesToHighlight: ['*']
		});
		searchLoading = false;
		if (!data) {
			searchError = 'Search failed. Try again.';
			return;
		}
		let raw = JSON.stringify(data);
		raw = raw.replaceAll('<em>', '<mark>');
		raw = raw.replaceAll('</em>', '</mark>');
		resp_data = JSON.parse(raw) as SearchResponse;
		const url = new URLSearchParams(window.location.search);
		url.set('q', search_term);
		history.pushState(null, '', '?' + url.toString());
	};

	onMount(() => {
		const url = new URLSearchParams(window.location.search);
		search_term = url.get('q') ?? '';
		if (search_term.length > 2) {
			submit();
		}
	});
</script>

<svelte:head>
	<title>CMA Clash: Search</title>
</svelte:head>

<div>
	<div class="flex justify-center">
		<div class="mb-3 xl:w-96">
			<form
				class="input-group relative flex items-stretch flex-row w-full mb-4"
				onsubmit={(e: Event) => {
					e.preventDefault();
					submit();
				}}
			>
				<input
					type="search"
					class="form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-ink bg-elevated bg-clip-padding border border-solid border-ink/20 rounded-sm transition ease-in-out m-0 focus:text-ink focus:bg-elevated focus:border-primary focus:outline-hidden"
					placeholder={$t('search_page.at_least_3_characters')}
					aria-label="Search"
					aria-describedby="button-addon2"
					bind:value={search_term}
				/>
				<button
					class="px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-sm shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-hidden focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out flex items-center disabled:opacity-50 disabled:cursor-not-allowed"
					id="button-addon2"
					aria-label="Search"
					disabled={search_term.length <= 2 || searchLoading}
					type="submit"
				>
					<svg
						aria-hidden="true"
						focusable="false"
						data-prefix="fas"
						data-icon="search"
						class="w-4"
						role="img"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 512 512"
					>
						<path
							fill="currentColor"
							d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
						/>
					</svg>
				</button>
			</form>
		</div>
	</div>
</div>

{#if searchLoading}
	<p class="text-center text-ink-muted text-sm">Searching…</p>
{:else if searchError}
	<div class="text-center">
		<p class="text-danger text-sm">{searchError}</p>
		<button type="button" class="action-button text-sm px-4 py-2 mt-2" onclick={() => submit()}>
			Retry
		</button>
	</div>
{/if}

{#if resp_data}
	{#if resp_data.hits.length !== 0}
		<div class="grid lg:grid-cols-3 grid-cols-1">
			{#each resp_data.hits as quiz}
				<SearchCard quiz={quiz._formatted ?? quiz} />
			{/each}
		</div>
	{:else}
		<div class="flex justify-center">
			<h1 class="text-4xl">{$t('search_page.nothing_here')}</h1>
		</div>
		<div class="flex justify-center">
			<p>
				Not finding what you are looking for? Search on <a
					class="underline"
					href="https://create.kahoot.it/search?query={search_term}&tags=test&filter=filter%3D1"
					target="_blank">Kahoot!</a
				>
				and <a href="/import" class="underline">import</a> it!
			</p>
		</div>
	{/if}
{/if}
