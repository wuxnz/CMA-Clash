<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import StartGamePopup from '$lib/dashboard/start_game.svelte';
	import Button from '$lib/ui/Button.svelte';
	import BrowseFilters from '$lib/quiz/BrowseFilters.svelte';
	import QuizBrowseList from '$lib/quiz/QuizBrowseList.svelte';
	import QuizBrowseSkeleton from '$lib/quiz/QuizBrowseSkeleton.svelte';
	import PageHeader from '$lib/ui/PageHeader.svelte';
	import {
		fetchCerts,
		fetchClashQuizzes,
		rowFromClash,
		searchMeili,
		searchPageSize,
		sortRows,
		userMapFromHits,
		type BrowseRow
	} from '$lib/quiz/browse';
	import { onMount } from 'svelte';
	import { SvelteURLSearchParams } from 'svelte/reactivity';
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
	navbarVisible.visible = true;

	let cert = $state(data.cert);
	let difficulty = $state(data.difficulty);
	let sort = $state(data.sort);
	let rows = $state<BrowseRow[]>(data.rows);
	let hasMore = $state(data.hasMore);
	let page = $state(data.page);
	let loading = $state(true);
	let loadingMore = $state(false);
	let hostError = $state('');
	let start_game = $state<string | null>(null);
	let filterKey = $state(`${data.cert}|${data.difficulty}|${data.sort}`);

	function syncUrl() {
		const params = new SvelteURLSearchParams();
		if (cert) params.set('cert', cert);
		if (difficulty) params.set('difficulty', difficulty);
		if (sort && sort !== 'newest') params.set('sort', sort);
		const qs = params.toString();
		history.replaceState(null, '', qs ? `?${qs}` : location.pathname);
	}

	async function loadPage(nextPage: number, reset: boolean) {
		if (reset) loading = true;
		else loadingMore = true;
		hostError = '';
		try {
			const [meili, clash, certs] = await Promise.all([
				searchMeili(fetch, { q: '*', limit: searchPageSize(), sort: ['created_at:desc'] }),
				fetchClashQuizzes(fetch, {
					certification_slug: cert || undefined,
					difficulty: difficulty || undefined,
					page: nextPage,
					page_size: searchPageSize()
				}),
				fetchCerts(fetch)
			]);
			const users = userMapFromHits(meili.hits);
			const catalog = certs.length ? certs : data.certs;
			const next = sortRows(
				clash.map((item) => rowFromClash(item, catalog, users)),
				sort === 'relevance' ? 'newest' : sort
			);
			rows = reset
				? next
				: [...rows, ...next.filter((row) => !rows.some((r) => r.id === row.id))];
			page = nextPage;
			hasMore = clash.length >= searchPageSize();
			if (reset && rows.length === 0) {
				hostError = 'Could not load quizzes from the API.';
			}
			syncUrl();
		} finally {
			loading = false;
			loadingMore = false;
		}
	}

	$effect(() => {
		const next = `${cert}|${difficulty}|${sort}`;
		if (next === filterKey) return;
		filterKey = next;
		loadPage(1, true);
	});

	onMount(() => {
		void loadPage(1, true);
	});
</script>

<svelte:head>
	<title>CMA Clash — Host</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 lg:pt-20 pb-20 min-w-0 flex-1">
		<PageHeader
			eyebrow="Host a session"
			title="Pick a set."
			accent="Share the PIN."
			lede="Choose any public question set, then read the six-digit PIN at /play to your room."
			meta="Live · real-time scoring"
		/>

		<div class="mt-8 min-w-0">
			<BrowseFilters bind:cert bind:difficulty bind:sort />
		</div>

		<div class="mt-10 min-w-0">
			{#if loading}
				<QuizBrowseSkeleton ariaLabel="Loading quizzes" />
			{:else if rows.length === 0}
				<div>
					<p class="text-sm text-ink">No quizzes for this filter.</p>
					{#if hostError}
						<p class="text-sm text-ink-muted mt-1">{hostError}</p>
						<Button variant="secondary" class="w-auto mt-2" onclick={() => loadPage(1, true)}
							>Retry</Button
						>
					{:else}
						<button
							type="button"
							class="text-ink link-hover min-h-11"
							onclick={() => {
								cert = '';
								difficulty = '';
							}}
						>
							Clear filters
						</button>
					{/if}
				</div>
			{:else}
				<QuizBrowseList items={rows} onHost={(id) => (start_game = id)} />
				{#if hasMore}
					<div class="mt-8">
						<Button
							variant="secondary"
							class="w-full sm:w-auto"
							disabled={loadingMore}
							onclick={() => loadPage(page + 1, false)}
						>
							{loadingMore ? 'Loading' : 'Load more'}
						</Button>
					</div>
				{/if}
			{/if}
		</div>
	</div>
	<Footer />
</div>

{#if start_game !== null}
	<StartGamePopup bind:quiz_id={start_game} />
{/if}
