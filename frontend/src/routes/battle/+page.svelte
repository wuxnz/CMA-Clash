<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import Footer from '$lib/footer.svelte';
	import { createBattle, type QuizBrowseItem } from '$lib/cma/client';
	import {
		setBattleGuestPlayerId,
		setBattleHostSecret
	} from '$lib/cma/battle-guest';
	import { loadPublicQuizCatalogClient } from '$lib/cma/quiz-catalog';
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
	let hostName = $state('');
	let loading = $state(false);
	let error = $state('');
	let catalogLoading = $state(data.ssrQuizLoadFailed && quizzes.length === 0);

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

	async function startBattle(quizId: string) {
		loading = true;
		error = '';
		const name = hostName.trim();
		if (name.length < 2) {
			loading = false;
			error = 'Enter your nickname (at least 2 characters) to host a battle.';
			return;
		}
		const result = await createBattle(quizId, 4, name);
		loading = false;
		if (!result.ok) {
			error = result.detail ?? 'Could not create battle — try again.';
			return;
		}
		const lobby = result.data;
		if (lobby.guest_player_id) {
			setBattleGuestPlayerId(lobby.guest_player_id);
		}
		if (lobby.host_secret) {
			setBattleHostSecret(lobby.battle_code, lobby.host_secret);
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

		{#if catalogLoading}
			<p class="text-ink-muted text-sm mb-4">Loading quizzes…</p>
		{:else if error}
			<p class="text-danger text-sm mb-4">{error}</p>
		{/if}

		<h2 class="text-sm font-semibold text-ink mb-2">Start a battle</h2>
		<label class="block text-xs text-ink-muted mb-4">
			Your nickname
			<input class="ledger-input mt-1" bind:value={hostName} placeholder="Arena name" maxlength="32" />
		</label>
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
