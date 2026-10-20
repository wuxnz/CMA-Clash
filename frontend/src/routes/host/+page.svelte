<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import { loadPublicQuizCatalogClient } from '$lib/cma/quiz-catalog';
	import type { QuizBrowseItem } from '$lib/cma/client';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	import StartGamePopup from '$lib/dashboard/start_game.svelte';
	import QuizBrowseList from '$lib/quiz/QuizBrowseList.svelte';
	import { certLabelFor, prettyDifficulty } from '$lib/quiz/labels';
	import { fetchCerts } from '$lib/quiz/browse';
	import type { Certification } from '$lib/cma/client';
	import Button from '$lib/ui/Button.svelte';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let quizzes = $state<QuizBrowseItem[]>(data.quizzes ?? []);
	let certs = $state<Certification[]>([]);
	let catalogLoading = $state(data.ssrQuizLoadFailed && quizzes.length === 0);
	let error = $state('');
	let start_game = $state<string | null>(null);

	onMount(async () => {
		certs = await fetchCerts(fetch);
		if (quizzes.length > 0) return;
		catalogLoading = true;
		error = '';
		const list = await loadPublicQuizCatalogClient();
		catalogLoading = false;
		quizzes = list;
		if (list.length === 0) {
			error = 'Could not load quizzes from the API.';
		}
	});

	const rows = $derived(
		quizzes.map((quiz) => ({
			...quiz,
			difficulty: prettyDifficulty(quiz.difficulty),
			certLabel: certLabelFor(quiz, certs)
		}))
	);
</script>

<svelte:head>
	<title>CMA Clash — Host</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Host</h1>
		<p class="text-sm text-ink-muted mt-1 mb-8">
			Pick a set, then share the PIN at
			<a href="/play" class="text-ink link-hover">/play</a>.
		</p>

		{#if catalogLoading}
			<p class="text-sm text-ink-muted">Loading quizzes</p>
		{:else if error && rows.length === 0}
			<p class="text-sm text-danger mb-4">{error}</p>
			<Button variant="secondary" class="w-auto" onclick={() => location.reload()}>Retry</Button>
		{:else if rows.length === 0}
			<p class="text-sm text-ink-muted">No public quizzes yet.</p>
		{:else}
			<QuizBrowseList items={rows} onHost={(id) => (start_game = id)} />
		{/if}
	</div>
	<Footer />
</div>

{#if start_game !== null}
	<StartGamePopup bind:quiz_id={start_game} />
{/if}
