<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import { createBattle, type QuizBrowseItem } from '$lib/cma/client';
	import { setBattleHostSecret } from '$lib/cma/battle-guest';
	import { loadPublicQuizCatalogClient } from '$lib/cma/quiz-catalog';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	import PageHeader from '$lib/ui/PageHeader.svelte';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let quizzes = $state<QuizBrowseItem[]>(data.quizzes ?? []);
	let joinCode = $state('');
	let loading = $state(false);
	let error = $state('');
	let catalogLoading = $state(true);

	onMount(async () => {
		error = '';
		const list = await loadPublicQuizCatalogClient();
		catalogLoading = false;
		quizzes = list;
		if (list.length === 0) {
			error = 'Could not load quizzes from the API.';
		}
	});

	async function startBattle(quizId: string) {
		loading = true;
		error = '';
		const result = await createBattle(quizId, 4);
		loading = false;
		if (!result.ok) {
			error = result.detail ?? 'Could not create battle. Try again.';
			return;
		}
		const lobby = result.data;
		if (lobby.host_secret) {
			setBattleHostSecret(lobby.battle_code, lobby.host_secret);
		}
		goto(`/battle/${lobby.battle_code}`);
	}
</script>

<svelte:head>
	<title>CMA Clash: Battle</title>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<div class="w-full max-w-5xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 lg:pt-20 pb-20 flex-1">
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
					if (joinCode.trim()) goto(`/battle/${joinCode.trim().toUpperCase()}`);
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

		{#if catalogLoading}
			<p class="text-ink-muted text-sm mt-10">Loading quizzes…</p>
		{:else if error}
			<p class="text-danger text-sm mt-10">{error}</p>
		{/if}

		<div class="mt-12">
			<p class="eyebrow">Start a battle</p>
			<p class="text-xs text-ink-muted mt-2 mb-4">
				Pick a quiz. You can set your nickname in the lobby if you are playing.
			</p>
			<ul class="border-t border-line">
				{#each quizzes as quiz (quiz.id)}
					<li
						class="py-4 flex justify-between items-center gap-4 min-w-0 border-b border-line"
					>
						<div class="min-w-0">
							<p class="font-display text-lg text-ink truncate">{quiz.title}</p>
							<p class="eyebrow mt-1">{quiz.question_count} questions</p>
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
					<li class="py-6">
						<p class="text-ink-muted text-sm">No public quizzes yet.</p>
					</li>
				{/each}
			</ul>
		</div>
	</div>
	<Footer />
</div>
