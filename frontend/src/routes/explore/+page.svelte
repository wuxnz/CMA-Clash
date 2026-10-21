<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import StartGamePopup from '$lib/dashboard/start_game.svelte';
	import Button from '$lib/ui/Button.svelte';
	import BrowseFilters from '$lib/quiz/BrowseFilters.svelte';
	import QuizBrowseList from '$lib/quiz/QuizBrowseList.svelte';
	import QuizBrowseSkeleton from '$lib/quiz/QuizBrowseSkeleton.svelte';
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
	let featured = $state<BrowseRow[]>(data.featured);
	let hasMore = $state(data.hasMore);
	let page = $state(data.page);
	let loading = $state(true);
	let loadingMore = $state(false);
	let exploreError = $state('');
	let start_game = $state<string | null>(null);
	let filterKey = $state(`${data.cert}|${data.difficulty}|${data.sort}`);

	const showFeatured = $derived(!cert && !difficulty && featured.length > 0);
	const listRows = $derived(
		showFeatured ? rows.filter((row) => !featured.some((f) => f.id === row.id)) : rows
	);

	function syncUrl() {
		const params = new URLSearchParams();
		if (cert) params.set('cert', cert);
		if (difficulty) params.set('difficulty', difficulty);
		if (sort && sort !== 'newest') params.set('sort', sort);
		const qs = params.toString();
		history.replaceState(null, '', qs ? `?${qs}` : location.pathname);
	}

	async function loadPage(nextPage: number, reset: boolean) {
		if (reset) loading = true;
		else loadingMore = true;
		exploreError = '';
		try {
			const [meili, clash, featuredSource, certs] = await Promise.all([
				searchMeili(fetch, { q: '*', limit: 100, sort: ['created_at:desc'] }),
				fetchClashQuizzes(fetch, {
					certification_slug: cert || undefined,
					difficulty: difficulty || undefined,
					page: nextPage,
					page_size: searchPageSize()
				}),
				reset ? fetchClashQuizzes(fetch, { page: 1, page_size: 100 }) : Promise.resolve([]),
				fetchCerts(fetch)
			]);
			const users = userMapFromHits(meili.hits);
			const catalog = certs.length ? certs : data.certs;
			const next = sortRows(
				clash.map((item) => rowFromClash(item, catalog, users)),
				sort === 'relevance' ? 'newest' : sort
			);
			rows = reset ? next : [...rows, ...next.filter((row) => !rows.some((r) => r.id === row.id))];
			if (reset) {
				featured =
					cert || difficulty
						? []
						: sortRows(
								featuredSource.map((item) => rowFromClash(item, catalog, users)),
								'plays'
							).slice(0, 3);
			}
			page = nextPage;
			hasMore = clash.length >= searchPageSize();
			if (reset && rows.length === 0) {
				exploreError = 'Could not load quizzes from the API.';
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
	<title>CMA Clash: Explore</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Explore</h1>

		<div class="mt-6 min-w-0">
			<BrowseFilters bind:cert bind:difficulty bind:sort />
		</div>

		<div class="mt-8 min-w-0">
			{#if loading}
				<QuizBrowseSkeleton ariaLabel="Loading quizzes" />
			{:else if rows.length === 0}
				<div data-empty-explore>
					<p class="text-sm text-ink">No quizzes for this filter.</p>
					<p class="text-sm text-ink-muted mt-2">
						{#if exploreError}
							{exploreError}
							<button type="button" class="text-ink link-hover min-h-11" onclick={() => loadPage(1, true)}>
								Retry
							</button>
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
					</p>
				</div>
			{:else}
				{#if showFeatured}
					<h2 class="text-sm font-semibold text-ink mb-2">Featured</h2>
					<QuizBrowseList items={featured} onHost={(id) => (start_game = id)} />
					<h2 class="text-sm font-semibold text-ink mt-10 mb-2">All sets</h2>
				{/if}
				<QuizBrowseList items={listRows} onHost={(id) => (start_game = id)} />
				{#if hasMore}
					<div class="mt-6">
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
