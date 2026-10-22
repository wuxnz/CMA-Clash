<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	// import AudioPlayer from '$lib/play/audio_player.svelte';
	import ControllerCodeDisplay from '$lib/components/controller/code.svelte';
	import { getLocalization } from '$lib/i18n';
	import GrayButton from '$lib/components/buttons/gray.svelte';
	import { fade } from 'svelte/transition';
	import PinDisplay from '$lib/ui/PinDisplay.svelte';
	import PlayerChip from '$lib/ui/PlayerChip.svelte';
	import Card from '$lib/ui/Card.svelte';
	import { SocketGameControls } from '$lib/play/admin/socket_game_controls.ts';
	import type { GameState } from '$lib/play/admin/game_state';

	interface Props {
		game_pin: string;
		game_state: GameState;
		socket_game_controls: SocketGameControls;
		cqc_code: string;
	}

	let {
		game_pin,
		game_state = $bindable(),
		socket_game_controls,
		cqc_code = $bindable()
	}: Props = $props();

	let fullscreen_open = $state(false);
	const { t } = getLocalization();
	let play_music = $state(false);

	if (cqc_code === 'null') {
		cqc_code = null;
	}
</script>

<div class="w-full h-dvh max-h-dvh bg-paper flex flex-col overflow-hidden">
	<div class="flex-1 min-h-0 overflow-y-auto px-4 pt-6 pb-4 sm:py-8">
		<!-- <AudioPlayer bind:play={play_music} /> -->
		<div class="max-w-5xl mx-auto text-center mb-10">
			<p class="eyebrow">Arena stage</p>
			<h1
				class="font-display text-4xl sm:text-6xl text-ink mt-3 leading-[0.95] tracking-[-0.035em]"
			>
				Host <em class="italic font-normal text-primary">lobby</em>
			</h1>
			<p class="text-ink-muted mt-3">Share the PIN or QR so players can drop in</p>
			<div class="mt-6">
				<PinDisplay pin={game_pin} />
			</div>
		</div>
		<div class="grid grid-cols-1 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
			<!--mt-12 -->
			<div class="flex justify-center">
				<p class="m-auto text-2xl">
					{$t('play_page.join_description', {
						url:
							window.location.host === ''
								? 'cquiz.de'
								: `${window.location.host}/play`,
						pin: game_pin
					})}
				</p>
			</div>
			<img
				onclick={() => (fullscreen_open = true)}
				alt="QR code to join the game"
				src="/api/v1/utils/qr/{game_pin}"
				class="block mx-auto w-full max-w-xs bg-paper p-4 border border-line hover:cursor-pointer"
			/>
			{#if cqc_code}
				<div class="m-auto">
					<div class="flex justify-center my-4">
						<p class="m-auto text-2xl">
							{#if game_state.players.length <= 1}
								{$t('play_page.players_waiting', {
									count: game_state.players.length ?? 0
								})}
							{:else}
								{$t('play_page.players_waiting_plural', {
									count: game_state.players.length ?? 0
								})}
							{/if}
						</p>
					</div>
					<div class="flex-col flex justify-center">
						<p class="mx-auto">{$t('play_page.join_by_entering_code')}</p>
						<ControllerCodeDisplay code={cqc_code} />
					</div>
				</div>
			{:else}
				<div class="flex justify-center">
					<p class="m-auto text-2xl">
						{#if game_state.players.length <= 1}
							{$t('play_page.players_waiting', {
								count: game_state.players.length ?? 0
							})}
						{:else}
							{$t('play_page.players_waiting_plural', {
								count: game_state.players.length ?? 0
							})}
						{/if}
					</p>
				</div>
			{/if}
		</div>
		<Card class="max-w-5xl mx-auto mt-6 sm:mt-8" padding="md">
			<h2 class="font-display font-semibold text-ink mb-4">Players in lobby</h2>
			<div class="flex flex-row w-full flex-wrap gap-2">
				{#if game_state.players.length > 0}
					{#each game_state.players as player}
						<button
							type="button"
							class="hover:opacity-70"
							title="Click to kick"
							onclick={() => {
								socket_game_controls.kick_player(
									player.username,
									game_state.players
								);
							}}
						>
							<PlayerChip name={player.username} />
						</button>
					{/each}
				{:else}
					<p class="text-ink-muted text-sm">Waiting for the first player…</p>
				{/if}
			</div>
		</Card>
	</div>
	<div
		class="shrink-0 border-t border-white/10 bg-surface/95 backdrop-blur-md px-3 py-3 safe-bottom"
		data-testid="host-lobby-controls"
	>
		<div class="max-w-xl mx-auto w-full [&_button]:w-full [&_button]:justify-center">
			<GrayButton
				data-testid="lobby-start-game"
				flex={true}
				disabled={game_state.players.length < 1}
				onclick={() => {
					socket_game_controls.start_game();
				}}
				>{$t('admin_page.start_game')}
			</GrayButton>
		</div>
	</div>
</div>

{#if fullscreen_open}
	<div
		class="fixed top-0 left-0 z-50 w-screen h-screen bg-black/50 flex p-2"
		transition:fade|global={{ duration: 80 }}
		onclick={() => (fullscreen_open = false)}
		tabindex="0"
		role="button"
		aria-label="Close modal"
		onkeydown={(e) =>
			e.key === 'Enter' || e.key === ' '
				? () => {
						fullscreen_open = false;
					}
				: null}
	>
		<img
			alt="QR code to join the game"
			src="/api/v1/utils/qr/{game_pin}"
			class="object-contain rounded-sm m-auto h-full bg-white"
		/>
	</div>
{/if}

<style>
	.safe-bottom {
		padding-bottom: max(0.75rem, env(safe-area-inset-bottom));
	}
</style>
