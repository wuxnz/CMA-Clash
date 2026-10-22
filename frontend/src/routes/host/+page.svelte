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
	import PageHeader from '$lib/ui/PageHeader.svelte';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let quizzes = $state<QuizBrowseItem[]>(data.quizzes ?? []);
	let certs = $state<Certification[]>([]);
	let catalogLoading = $state(true);
	let error = $state('');
	let start_game = $state<string | null>(null);

	onMount(async () => {
		certs = await fetchCerts(fetch);
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
	<div class="w-full max-w-6xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 lg:pt-20 pb-20 min-w-0 flex-1">
		<PageHeader
			eyebrow="Host a session"
			title="Pick a set."
			accent="Share the PIN."
			lede="Choose any public question set, then read the six-digit PIN at /play to your room."
			meta="Live · real-time scoring"
		/>

		{#if catalogLoading}
			<p class="text-sm text-ink-muted">Loading quizzes</p>
		{:else if error && rows.length === 0}
			<p class="text-sm text-danger mb-4">{error}</p>
			<Button variant="secondary" class="w-auto" onclick={() => location.reload()}
				>Retry</Button
			>
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
