<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import Button from '$lib/ui/Button.svelte';
	import { createBattle } from '$lib/cma/client';
	import { setBattleHostSecret } from '$lib/cma/battle-guest';
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { onMount } from 'svelte';
	import { SvelteURLSearchParams } from 'svelte/reactivity';
	import type { PageData } from './$types';
	import PageHeader from '$lib/ui/PageHeader.svelte';
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

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let joinCode = $state('');
	let starting = $state(false);
	let battleError = $state('');

	let cert = $state(data.cert);
	let difficulty = $state(data.difficulty);
	let sort = $state(data.sort);
	let rows = $state<BrowseRow[]>([]);
	let hasMore = $state(false);
	let page = $state(1);
	let catalogLoading = $state(true);
	let loadingMore = $state(false);
	let catalogError = $state('');
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
		if (reset) catalogLoading = true;
		else loadingMore = true;
		catalogError = '';
		try {
			const [meili, clash, certs] = await Promise.all([
				searchMeili(fetch, { q: '*', limit: 100, sort: ['created_at:desc'] }),
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
				catalogError = 'Could not load quizzes from the API.';
			}
			syncUrl();
		} finally {
			catalogLoading = false;
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

	async function startBattle(quizId: string) {
		if (starting) return;
		starting = true;
		battleError = '';
		const result = await createBattle(quizId, 4);
		starting = false;
		if (!result.ok) {
			const detail = 'detail' in result ? result.detail : undefined;
			battleError = detail ?? 'Could not create battle. Try again.';
			return;
		}
		const lobby = result.data;
		if (lobby.host_secret) {
			setBattleHostSecret(lobby.battle_code, lobby.host_secret);
		}
		goto(resolve('/battle/[code]', { code: lobby.battle_code }));
	}
</script>

<svelte:head>
	<title>CMA Clash: Battle</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-5xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 lg:pt-20 pb-20 flex-1 min-w-0">
		<PageHeader
			eyebrow="Head to head"
			title="Two players."
			accent="One scoreboard."
			lede="Start a duel with any public set, or join a friend with the code they read out."
			meta="Rank-based · speed bonus"
		/>

		<div class="border border-line bg-paper p-6 sm:p-8 max-w-xl">
			<p class="eyebrow mb-4">Join with code</p>
			<form
				class="flex flex-col sm:flex-row gap-2"
				onsubmit={(e) => {
					e.preventDefault();
					if (joinCode.trim())
						goto(resolve('/battle/[code]', { code: joinCode.trim().toUpperCase() }));
				}}
			>
				<input
					class="ledger-input flex-1 uppercase text-center sm:text-left font-mono tracking-[0.3em]"
					bind:value={joinCode}
					placeholder="CODE"
					aria-label="Battle code"
				/>
				<button type="submit" class="btn btn-primary w-auto shrink-0">Join</button>
			</form>
		</div>

		<div class="mt-12 min-w-0">
			<p class="eyebrow mb-4">Start a battle</p>
			<p class="text-xs text-ink-muted mb-4">
				Pick a quiz. You can set your nickname in the lobby if you are playing.
			</p>

			<div class="min-w-0">
				<BrowseFilters bind:cert bind:difficulty bind:sort />
			</div>

			{#if battleError}
				<p class="text-danger text-sm mt-6" role="alert">{battleError}</p>
			{/if}
			{#if starting}
				<p class="text-ink-muted text-sm mt-6">Starting battle…</p>
			{/if}

			<div class="mt-10 min-w-0">
				{#if catalogLoading}
					<QuizBrowseSkeleton ariaLabel="Loading quizzes" />
				{:else if rows.length === 0}
					<div data-empty-battle>
						<p class="text-sm text-ink">No quizzes for this filter.</p>
						<p class="text-sm text-ink-muted mt-2">
							{#if catalogError}
								{catalogError}
								<button
									type="button"
									class="text-ink link-hover min-h-11"
									onclick={() => loadPage(1, true)}
								>
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
					<QuizBrowseList items={rows} onHost={(id) => startBattle(id)} />
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
	</div>
	<Footer />
</div>
