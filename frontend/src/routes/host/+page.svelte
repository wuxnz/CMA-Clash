<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import { loadPublicQuizCatalogClient } from '$lib/cma/quiz-catalog';
	import { adminLobbyUrl, startHostGame } from '$lib/cma/host-game';
	import type { QuizBrowseItem } from '$lib/cma/client';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let quizzes = $state<QuizBrowseItem[]>(data.quizzes ?? []);
	let loading = $state(false);
	let catalogLoading = $state(data.ssrQuizLoadFailed && quizzes.length === 0);
	let error = $state('');

	onMount(async () => {
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

	async function hostQuiz(quizId: string) {
		loading = true;
		error = '';
		const result = await startHostGame(quizId);
		loading = false;
		if (result === 'auth') {
			window.location.assign(`/account/login?returnTo=${encodeURIComponent('/host')}`);
			return;
		}
		if (result === 'error') {
			error = 'Could not start the game. Sign in and try again.';
			return;
		}
		window.location.assign(adminLobbyUrl(result));
	}
</script>

<svelte:head>
	<title>CMA Clash — Host a Clash</title>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<div class="max-w-2xl mx-auto w-full px-4 py-10 flex-1">
		<h1 class="text-2xl font-semibold text-ink tracking-tight">Host a Clash</h1>
		<p class="text-sm text-ink-muted mt-1 mb-8">
			Pick a public quiz set, get a PIN, and share
			<a href="/play" class="link-hover text-ink">/play</a>
			so players can join.
		</p>

		{#if catalogLoading}
			<p class="text-ink-muted text-sm">Loading quizzes…</p>
		{:else if error}
			<p class="text-danger text-sm mb-4">{error}</p>
		{/if}

		<ul class="divide-y divide-white/[0.07]">
			{#each quizzes as quiz (quiz.id)}
				<li class="py-3 flex justify-between items-center gap-4 min-w-0">
					<div class="min-w-0">
						<p class="font-medium text-ink truncate">{quiz.title}</p>
						<p class="text-xs text-ink-muted">{quiz.question_count} questions</p>
					</div>
					<button
						type="button"
						class="ledger-btn-primary w-auto min-h-11 px-4 shrink-0"
						disabled={loading}
						onclick={() => hostQuiz(quiz.id)}
					>
						Host
					</button>
				</li>
			{:else}
				{#if !catalogLoading}
					<p class="text-ink-muted text-sm">No public quizzes yet.</p>
				{/if}
			{/each}
		</ul>
	</div>
	<Footer />
</div>
