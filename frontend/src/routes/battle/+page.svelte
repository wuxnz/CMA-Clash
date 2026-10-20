<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import { createBattle, fetchQuizzes, type QuizBrowseItem } from '$lib/cma/client';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let quizzes = $state<QuizBrowseItem[]>(data.quizzes ?? []);
	let joinCode = $state('');
	let loading = $state(false);
	let error = $state(data.loadError ?? '');

	onMount(async () => {
		if (quizzes.length > 0) return;
		let list = await fetchQuizzes({ certification_slug: 'ccma', page_size: 50 });
		if (list.length === 0) list = await fetchQuizzes({ page_size: 50 });
		quizzes = list;
		if (list.length === 0 && !error) error = 'No public quizzes yet.';
	});

	async function startBattle(quizId: string) {
		loading = true;
		error = '';
		const lobby = await createBattle(quizId, 4);
		loading = false;
		if (!lobby) {
			error = 'Could not create battle — sign in and try again.';
			return;
		}
		goto(`/battle/${lobby.battle_code}`);
	}
</script>

<svelte:head>
	<title>CMA Clash — Battle</title>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<div class="max-w-2xl mx-auto w-full px-4 py-10 flex-1">
		<h1 class="text-2xl font-semibold text-ink tracking-tight">Battle</h1>
		<p class="text-sm text-ink-muted mt-1 mb-8">Start a 1v1 or join with a code.</p>

		<div class="mb-10">
			<h2 class="text-sm font-semibold mb-3">Join with code</h2>
			<form
				class="flex gap-2"
				onsubmit={(e) => {
					e.preventDefault();
					if (joinCode.trim()) goto(`/battle/${joinCode.trim().toUpperCase()}`);
				}}
			>
				<input class="ledger-input flex-1 uppercase" bind:value={joinCode} placeholder="Code" />
				<button type="submit" class="btn btn-primary w-auto">Join</button>
			</form>
		</div>

		{#if error}
			<p class="text-danger text-sm mb-4">{error}</p>
		{/if}

		<h2 class="text-sm font-semibold text-ink mb-4">Start a battle</h2>
		<ul class="divide-y divide-white/[0.07]">
			{#each quizzes as quiz (quiz.id)}
				<li class="py-3 flex justify-between items-center gap-4 min-w-0">
					<div class="min-w-0">
						<p class="font-medium text-ink truncate">{quiz.title}</p>
						<p class="text-xs text-ink-muted">{quiz.question_count} questions</p>
					</div>
					<button
						type="button"
						class="action-button min-h-11 px-4 shrink-0"
						disabled={loading}
						onclick={() => startBattle(quiz.id)}
					>
						Host
					</button>
				</li>
			{:else}
				<p class="text-ink-muted text-sm">No public quizzes yet.</p>
			{/each}
		</ul>
	</div>
	<Footer />
</div>
