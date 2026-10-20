<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import { getBattle, joinBattle, startBattle, type BattleLobby } from '$lib/cma/client';
	import Card from '$lib/ui/Card.svelte';
	import PlayerChip from '$lib/ui/PlayerChip.svelte';
	import CountdownRing from '$lib/ui/CountdownRing.svelte';
	import { goto } from '$app/navigation';
	import { fly } from 'svelte/transition';
	import { prefersReducedMotion } from '$lib/ui/motion';

	navbarVisible.visible = false;

	let lobby = $state<BattleLobby | null>(null);
	let showVs = $state(true);
	let showCountdown = $state(false);
	let error = $state('');
	const reduced = prefersReducedMotion();

	const code = $derived(page.params.code);

	async function refresh() {
		lobby = await getBattle(code);
	}

	onMount(async () => {
		await joinBattle(code).catch(() => {});
		await refresh();
		const id = setInterval(refresh, 2000);
		return () => clearInterval(id);
	});

	async function handleStart() {
		const updated = await startBattle(code);
		if (!updated?.game_pin) {
			error = 'Could not start — are you the host?';
			return;
		}
		lobby = updated;
		showVs = false;
		showCountdown = true;
	}

	function goToPlay() {
		if (lobby?.game_pin) goto(`/play?pin=${lobby.game_pin}`);
	}

	let playerNames = $derived(
		lobby?.player_slots?.map((s) => s.username ?? 'Player').filter(Boolean) ?? []
	);
</script>

<svelte:head>
	<title>CMA-Clash — Battle {code}</title>
</svelte:head>

<div class="min-h-screen bg-ink text-paper flex flex-col items-center justify-center px-4 relative overflow-hidden">
	<div class="absolute inset-0 bg-gradient-to-b from-primary/20 to-transparent pointer-events-none" aria-hidden="true"></div>

	{#if showCountdown}
		<CountdownRing seconds={5} label="Battle starts" onComplete={goToPlay} />
	{:else if showVs && playerNames.length >= 2}
		<div class="relative z-10 text-center max-w-lg w-full" in:fly={reduced ? { duration: 0 } : { y: 30 }}>
			<p class="text-sm uppercase tracking-[0.3em] text-gold mb-8">Arena</p>
			<div class="flex items-center justify-center gap-4 sm:gap-8">
				<div class="flex-1">
					<p class="font-display text-2xl sm:text-4xl font-bold truncate">{playerNames[0]}</p>
				</div>
				<p class="font-display text-3xl text-gold font-black">VS</p>
				<div class="flex-1">
					<p class="font-display text-2xl sm:text-4xl font-bold truncate">{playerNames[1]}</p>
				</div>
			</div>
			{#if playerNames.length > 2}
				<p class="mt-4 text-sm text-paper/70">+{playerNames.length - 2} more in lobby</p>
			{/if}
		</div>
	{/if}

	<Card class="mt-12 max-w-md w-full relative z-10 !bg-surface text-ink" padding="md">
		<p class="font-mono text-center text-lg tracking-widest mb-4">{code}</p>
		<div class="flex flex-wrap gap-2 justify-center mb-6">
			{#each playerNames as name (name)}
				<PlayerChip {name} />
			{/each}
		</div>
		<p class="text-center text-sm text-ink-muted mb-4">Status: {lobby?.status ?? '…'}</p>
		{#if error}
			<p class="text-danger text-sm text-center mb-2">{error}</p>
		{/if}
		{#if lobby?.status === 'waiting'}
			<button type="button" class="ledger-btn-primary" onclick={handleStart}>Start battle</button>
		{:else if lobby?.game_pin}
			<a href="/play?pin={lobby.game_pin}" class="ledger-btn-primary text-center">Enter game</a>
		{/if}
	</Card>
</div>
