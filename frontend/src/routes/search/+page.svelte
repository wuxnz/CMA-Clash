<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import StartGamePopup from '$lib/dashboard/start_game.svelte';
	import Button from '$lib/ui/Button.svelte';
	import BrowseFilters from '$lib/quiz/BrowseFilters.svelte';
	import QuizBrowseList from '$lib/quiz/QuizBrowseList.svelte';
	import {
		fetchCerts,
		fetchClashCatalog,
		fetchClashQuizzes,
		rowsFromClash,
		rowsFromMeili,
		searchMeili,
		searchPageSize,
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

	let search_term = $state(data.q);
	let cert = $state(data.cert);
	let difficulty = $state(data.difficulty);
	let sort = $state(data.sort);
	let rows = $state<BrowseRow[]>(data.rows);
	let hasMore = $state(data.hasMore);
	let offset = $state(data.offset);
	let page = $state(data.page);
	let loading = $state(false);
	let loadingMore = $state(false);
	let searchError = $state('');
	let start_game = $state<string | null>(null);
	let inputEl: HTMLInputElement | undefined = $state();
	let debounce: ReturnType<typeof setTimeout> | undefined;
	let filterKey = $state(`${data.cert}|${data.difficulty}|${data.sort}`);

	const tooShort = $derived(search_term.trim().length > 0 && search_term.trim().length < 3);
	const useMeili = $derived(search_term.trim().length >= 3);

	function syncUrl() {
		const params = new URLSearchParams();
		if (search_term.trim()) params.set('q', search_term.trim());
		if (cert) params.set('cert', cert);
		if (difficulty) params.set('difficulty', difficulty);
		if (sort && sort !== 'relevance') params.set('sort', sort);
		const qs = params.toString();
		history.replaceState(null, '', qs ? `?${qs}` : location.pathname);
	}

	async function runSearch(reset: boolean) {
		if (tooShort) {
			rows = [];
			hasMore = false;
			syncUrl();
			return;
		}
		if (reset) {
			loading = true;
			offset = 0;
			page = 1;
		} else {
			loadingMore = true;
		}
		searchError = '';
		try {
			const q = search_term.trim();
			const nextPage = reset ? 1 : page + 1;
			const nextOffset = reset ? 0 : offset;
			const [meili, clashPage, catalog, certs] = await Promise.all([
				searchMeili(fetch, {
					q: useMeili ? q : '*',
					offset: useMeili ? nextOffset : 0,
					limit: useMeili ? searchPageSize() : 100,
					sort: sort === 'newest' ? ['created_at:desc'] : undefined
				}),
				useMeili
					? Promise.resolve([])
					: fetchClashQuizzes(fetch, {
							certification_slug: cert || undefined,
							difficulty: difficulty || undefined,
							page: nextPage,
							page_size: searchPageSize()
						}),
				useMeili ? fetchClashCatalog(fetch) : Promise.resolve([]),
				fetchCerts(fetch)
			]);
			if (useMeili) {
				const next = rowsFromMeili(meili.hits, catalog, certs, cert, difficulty, sort);
				rows = reset ? next : [...rows, ...next.filter((row) => !rows.some((r) => r.id === row.id))];
				offset = nextOffset + meili.hits.length;
				hasMore = meili.hits.length >= searchPageSize();
			} else {
				const users = userMapFromHits(meili.hits);
				const next = rowsFromClash(clashPage, certs, users, sort);
				rows = reset ? next : [...rows, ...next.filter((row) => !rows.some((r) => r.id === row.id))];
				page = nextPage;
				hasMore = clashPage.length >= searchPageSize();
			}
			if (reset && rows.length === 0 && !useMeili) {
				searchError = 'Could not load quizzes from the API.';
			}
			syncUrl();
		} finally {
			loading = false;
			loadingMore = false;
		}
	}

	function onInput() {
		clearTimeout(debounce);
		if (search_term.trim().length === 1 || search_term.trim().length === 2) {
			return;
		}
		debounce = setTimeout(() => runSearch(true), 280);
	}

	$effect(() => {
		const next = `${cert}|${difficulty}|${sort}`;
		if (next === filterKey) return;
		filterKey = next;
		runSearch(true);
	});

	onMount(() => {
		if (rows.length === 0 && !tooShort) runSearch(true);
	});

	function onSlash(event: KeyboardEvent) {
		if (event.key !== '/' || event.metaKey || event.ctrlKey || event.altKey) return;
		const tag = (event.target as HTMLElement | null)?.tagName;
		if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
		event.preventDefault();
		inputEl?.focus();
	}
</script>

<svelte:window onkeydown={onSlash} />

<svelte:head>
	<title>CMA Clash: Search</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Search</h1>

		<form
			class="mt-5 flex flex-col sm:flex-row gap-2 min-w-0"
			onsubmit={(e) => {
				e.preventDefault();
				if (!tooShort) runSearch(true);
			}}
		>
			<label class="sr-only" for="quiz-search-q">Search quizzes</label>
			<input
				id="quiz-search-q"
				bind:this={inputEl}
				bind:value={search_term}
				oninput={onInput}
				type="search"
				class="ledger-input min-h-12 text-base"
				placeholder="Search quizzes"
				autocomplete="off"
				data-search-input
			/>
			<Button type="submit" class="w-full sm:w-auto shrink-0" disabled={tooShort || loading}>
				Search
			</Button>
		</form>
		{#if tooShort}
			<p class="text-sm text-ink-muted mt-2">Enter at least 3 characters.</p>
		{/if}

		<div class="mt-6 min-w-0">
			<BrowseFilters bind:cert bind:difficulty bind:sort />
		</div>

		<div class="mt-8 min-w-0">
			{#if loading}
				<ul class="animate-pulse" aria-busy="true" aria-label="Loading results">
					{#each [1, 2, 3, 4, 5] as n (n)}
						<li class="border-b border-white/[0.07] py-3">
							<div class="h-3 w-2/5 max-w-xs rounded bg-elevated"></div>
							<div class="h-2 w-24 rounded bg-elevated mt-2 md:hidden"></div>
						</li>
					{/each}
				</ul>
			{:else if rows.length === 0}
				<div data-empty-search>
					<p class="text-sm text-ink">No results</p>
					<p class="text-sm text-ink-muted mt-1">
						{#if searchError}
							{searchError}
							<button type="button" class="text-ink link-hover min-h-11" onclick={() => runSearch(true)}>
								Retry
							</button>
						{:else}
							Try another term, or
							<a href="/import" class="text-ink link-hover">import</a> a set.
							{#if search_term.trim().length >= 3}
								Search on
								<a
									class="text-ink link-hover"
									href="https://create.kahoot.it/search?query={encodeURIComponent(search_term)}&tags=test&filter=filter%3D1"
									target="_blank"
									rel="noreferrer">Kahoot!</a
								>
								and import it.
							{/if}
						{/if}
					</p>
				</div>
			{:else}
				<QuizBrowseList items={rows} onHost={(id) => (start_game = id)} />
				{#if hasMore}
					<div class="mt-6">
						<Button
							variant="secondary"
							class="w-full sm:w-auto"
							disabled={loadingMore}
							onclick={() => runSearch(false)}
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
