<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import { getBattle, joinBattle, startBattle, type BattleLobby } from '$lib/cma/client';
	import { prepareBattlePlayHandoff } from '$lib/cma/battle-play-handoff';
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
	let isHost = $state(false);
	let myUserId = $state<string | null>(null);
	const reduced = prefersReducedMotion();

	const code = $derived(page.params.code);

	function amInLobby(l: BattleLobby | null): boolean {
		if (!l?.player_slots?.length) return false;
		const guestId = getBattleGuestPlayerId();
		return l.player_slots.some(
			(s) =>
				(myUserId != null && s.user_id === myUserId) ||
				(guestId != null && s.user_id === guestId)
		);
	}

	function beginArenaCountdown() {
		if (showCountdown) return;
		showVs = false;
		showCountdown = true;
	}

	async function refresh() {
		const next = await getBattle(code);
		if (!next) {
			error = 'Battle not found or expired.';
			return;
		}
		if (next.status === 'started' && next.game_pin) {
			lobby = next;
			beginArenaCountdown();
			return;
		}
		lobby = next;
	}

	async function tryJoinLobby() {
		if (myUserId == null) return;
		const result = await joinBattle(code);
		if (result.ok) {
			if (result.data.guest_player_id) {
				setBattleGuestPlayerId(result.data.guest_player_id);
			}
			lobby = result.data;
			return;
		}
		if (result.status !== 401) {
			error = result.detail ?? 'Could not join this battle lobby.';
		}
	}

	onMount(async () => {
		isHost = Boolean(getBattleHostSecret(code));
		try {
			const me = await fetch('/api/v1/users/me', { credentials: 'include' });
			if (me.ok) {
				const user = await me.json();
				myUserId = user?.id ?? null;
			}
		} catch {
			/* guest */
		}
		await refresh();
		if (myUserId != null && lobby?.host_user_id === myUserId) {
			isHost = true;
		}
		if (myUserId != null) {
			await tryJoinLobby();
		}
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
		const guestId = getBattleGuestPlayerId();
		const result = await joinBattle(code, {
			displayName: name,
			guestPlayerId: guestId ?? undefined
		});
		if (!result.ok) {
			error = result.detail ?? 'Could not join. Check the code and try again.';
			return;
		}
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
			error =
				result.detail ??
				'Could not start. You must be the host and have at least two players.';
			return;
		}
		const updated = result.data;
		if (!updated?.game_pin) {
			error = 'Could not start. Are you the host?';
			return;
		}
		lobby = updated;
		beginArenaCountdown();
	}

	function goToPlay() {
		if (!lobby) return;
		const pin = prepareBattlePlayHandoff(lobby, {
			userId: myUserId,
			guestPlayerId: getBattleGuestPlayerId()
		});
		if (!pin) return;
		goto(`/play?pin=${pin}`);
	}

	function enterGameFromLobby() {
		goToPlay();
	}

	let playerNames = $derived(
		lobby?.player_slots?.map((s) => s.username ?? 'Player').filter(Boolean) ?? []
	);

	let needsJoinForm = $derived(lobby?.status === 'waiting' && !amInLobby(lobby));
</script>

<svelte:head>
	<title>CMA Clash: Battle {code}</title>
</svelte:head>

<div class="min-h-screen bg-paper text-ink flex flex-col items-center justify-center px-4 relative overflow-hidden">
	{#if showCountdown}
		<CountdownRing seconds={5} label="Battle starts" onComplete={goToPlay} />
	{:else if showVs && playerNames.length >= 2}
		<div class="relative z-10 text-center max-w-lg w-full" in:fly={reduced ? { duration: 0 } : { y: 30 }}>
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
				<p class="mt-4 text-sm text-ink-muted">+{playerNames.length - 2} more in lobby</p>
			{/if}
		</div>
	{/if}

	<Card class="mt-12 max-w-md w-full relative z-10 !bg-surface text-ink" padding="md">
		<p class="font-mono text-center text-lg tracking-widest mb-4">{code}</p>
		<div class="flex flex-wrap gap-2 justify-center mb-6" data-testid="battle-lobby-players">
			{#each playerNames as name (name)}
				<PlayerChip {name} />
			{/each}
		</div>
		<p class="text-center text-sm text-ink-muted mb-4">Status: {lobby?.status ?? '…'}</p>

		{#if needsJoinForm}
			<form class="mb-4 flex flex-col gap-2" onsubmit={handleJoinSubmit}>
				<p class="text-sm text-ink-muted text-center">
					{isHost ? 'Enter a nickname to join as a player' : 'Enter a nickname to join this battle'}
				</p>
				<input
					class="ledger-input text-center"
					bind:value={joinName}
					placeholder="Your nickname"
					maxlength="32"
					autocomplete="nickname"
				/>
				<button type="submit" class="btn btn-primary w-full">Join battle</button>
			</form>
		{/if}

		{#if error}
			<p class="text-danger text-sm text-center mb-2" role="alert">{error}</p>
		{/if}
		{#if lobby?.status === 'waiting' && isHost}
			<button type="button" class="btn btn-primary w-full" onclick={handleStart}>Start battle</button>
		{:else if lobby?.status === 'waiting' && !isHost}
			<p class="text-center text-sm text-ink-muted">Waiting for the host to start…</p>
		{:else if lobby?.game_pin}
			<button type="button" class="ledger-btn-primary text-center w-full" onclick={enterGameFromLobby}>
				Enter game
			</button>
		{/if}
	</Card>
</div>
