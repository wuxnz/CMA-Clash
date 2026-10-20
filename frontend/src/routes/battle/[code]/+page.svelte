<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import { getBattle, joinBattle, startBattle, type BattleLobby } from '$lib/cma/client';
	import {
		getBattleGuestPlayerId,
		getBattleHostSecret,
		setBattleGuestPlayerId
	} from '$lib/cma/battle-guest';
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
	let joinName = $state('');
	let joined = $state(false);
	const reduced = prefersReducedMotion();

	const code = $derived(page.params.code);

	async function refresh() {
		lobby = await getBattle(code);
	}

	async function tryJoinLobby() {
		const guestId = getBattleGuestPlayerId();
		const result = await joinBattle(code, {
			displayName: joinName.trim() || undefined,
			guestPlayerId: guestId ?? undefined
		});
		if (result.ok) {
			joined = true;
			if (result.data.guest_player_id) {
				setBattleGuestPlayerId(result.data.guest_player_id);
			}
			lobby = result.data;
			return;
		}
		if (result.status === 400 && result.detail?.includes('display_name')) {
			return;
		}
		if (result.status !== 401) {
			error = result.detail ?? 'Could not join this battle lobby.';
		}
	}

	onMount(async () => {
		await refresh();
		await tryJoinLobby();
		const id = setInterval(refresh, 2000);
		return () => clearInterval(id);
	});

	async function handleJoinSubmit(e: Event) {
		e.preventDefault();
		error = '';
		const name = joinName.trim();
		if (name.length < 2) {
			error = 'Nickname must be at least 2 characters.';
			return;
		}
		const result = await joinBattle(code, { displayName: name });
		if (!result.ok) {
			error = result.detail ?? 'Could not join — check the code and try again.';
			return;
		}
		joined = true;
		if (result.data.guest_player_id) {
			setBattleGuestPlayerId(result.data.guest_player_id);
		}
		lobby = result.data;
	}

	async function handleStart() {
		error = '';
		const hostSecret = getBattleHostSecret(code);
		const result = await startBattle(code, hostSecret ?? undefined);
		if (!result.ok) {
			error = result.detail ?? 'Could not start — you must be the host with at least two players.';
			return;
		}
		const updated = result.data;
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

	let needsGuestJoin = $derived(!joined && playerNames.length < 2);
</script>

<svelte:head>
	<title>CMA Clash — Battle {code}</title>
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

		{#if needsGuestJoin && lobby?.status === 'waiting'}
			<form class="mb-4 flex flex-col gap-2" onsubmit={handleJoinSubmit}>
				<p class="text-sm text-ink-muted text-center">Enter a nickname to join this battle</p>
				<input
					class="ledger-input text-center"
					bind:value={joinName}
					placeholder="Your nickname"
					maxlength="32"
					autocomplete="nickname"
				/>
				<button type="submit" class="ledger-btn-primary">Join battle</button>
			</form>
		{/if}

		{#if error}
			<p class="text-danger text-sm text-center mb-2" role="alert">{error}</p>
		{/if}
		{#if lobby?.status === 'waiting'}
			<button type="button" class="ledger-btn-primary" onclick={handleStart}>Start battle</button>
		{:else if lobby?.game_pin}
			<a href="/play?pin={lobby.game_pin}" class="ledger-btn-primary text-center">Enter game</a>
		{/if}
	</Card>
</div>
