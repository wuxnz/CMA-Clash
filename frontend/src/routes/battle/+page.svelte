<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import Card from '$lib/ui/Card.svelte';
	import { fetchQuizzes, createBattle, type QuizBrowseItem } from '$lib/cma/client';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	navbarVisible.visible = true;

	let quizzes = $state<QuizBrowseItem[]>([]);
	let joinCode = $state('');
	let loading = $state(false);
	let error = $state('');

	onMount(async () => {
		quizzes = await fetchQuizzes({ page_size: 20 });
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
		<h1 class="font-display text-3xl font-bold text-ink">Battle mode</h1>
		<p class="text-ink-muted mt-2 mb-8">
			1v1–8 player battles via <code class="font-mono text-xs">/api/v1/clash/battles</code>.
		</p>

		<Card class="mb-8">
			<h2 class="font-display font-semibold mb-3">Join with code</h2>
			<form
				class="flex gap-2"
				onsubmit={(e) => {
					e.preventDefault();
					if (joinCode.trim()) goto(`/battle/${joinCode.trim().toUpperCase()}`);
				}}
			>
				<input class="ledger-input flex-1 font-mono uppercase" bind:value={joinCode} placeholder="BATTLE CODE" />
				<button type="submit" class="ledger-btn-primary w-auto px-6">Join</button>
			</form>
		</Card>

		{#if error}
			<p class="text-danger text-sm mb-4">{error}</p>
		{/if}

		<h2 class="font-display font-semibold text-ink mb-4">Start a battle</h2>
		<ul class="space-y-3">
			{#each quizzes as quiz (quiz.id)}
				<li class="rounded-xl border border-ink/10 bg-surface p-4 flex justify-between items-center gap-4">
					<div>
						<p class="font-medium text-ink">{quiz.title}</p>
						<p class="text-xs text-ink-muted font-mono">{quiz.question_count} questions</p>
					</div>
					<button
						type="button"
						class="ledger-btn-primary w-auto px-4 shrink-0"
						disabled={loading}
						onclick={() => startBattle(quiz.id)}
					>
						Host
					</button>
				</li>
			{:else}
				<p class="text-ink-muted text-sm">No public quizzes — run content seed or create a quiz.</p>
			{/each}
		</ul>
	</div>
	<Footer />
</div>
