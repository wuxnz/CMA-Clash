<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { onDestroy, onMount } from 'svelte';
	import { socket } from '$lib/socket';

	type Roster = {
		count: number;
		assign: 'random' | 'choose' | null;
		started: boolean;
		teams: Record<string, string[]>;
		unassigned: string[];
	};

	interface Props {
		/** 'player' lets a player pick a team in the lobby; 'host' only shows the roster. */
		mode: 'player' | 'host';
		username?: string;
	}

	let { mode, username = '' }: Props = $props();

	let roster = $state<Roster | null>(null);
	let error = $state('');

	const ERRORS: Record<string, string> = {
		invalid_team: 'That team is not available.',
		already_started: 'The game has started. Teams are locked.',
		teams_are_random: 'The host assigns teams randomly for this game.',
		no_team_mode: 'This game does not use teams.'
	};

	function onRoster(data: Roster) {
		roster = data;
		error = '';
	}

	function onError(payload: { code?: string }) {
		error = ERRORS[payload?.code ?? ''] ?? 'Could not update teams.';
	}

	onMount(() => {
		socket.on('team_roster', onRoster);
		socket.on('team_error', onError);
		socket.emit('get_team_roster', {});
	});

	onDestroy(() => {
		socket.off('team_roster', onRoster);
		socket.off('team_error', onError);
	});

	const myTeam = $derived.by(() => {
		if (!roster || !username) return -1;
		for (const [idx, names] of Object.entries(roster.teams)) {
			if (names.includes(username)) return Number(idx);
		}
		return -1;
	});

	const canChoose = $derived(
		mode === 'player' && roster?.assign === 'choose' && !roster?.started
	);

	function choose(team: number) {
		error = '';
		socket.emit('choose_team', { team });
	}
</script>

{#if roster && roster.count > 0}
	<section class="max-w-4xl mx-auto w-full px-4 pb-8" aria-label="Teams">
		<p class="eyebrow text-center">
			{canChoose ? 'Pick a team' : 'Teams'}
		</p>
		<div class="team-grid mt-4" style="--cols: {Math.min(roster.count, 4)}">
			{#each Array.from({ length: roster.count }, (_, i) => i) as idx (idx)}
				{@const names = roster.teams[String(idx)] ?? []}
				<div
					class="border p-4 {myTeam === idx ? 'border-primary' : 'border-line'} bg-surface"
				>
					<div class="flex items-center justify-between gap-2">
						<p class="font-display text-lg text-ink">Team {idx + 1}</p>
						<p class="text-xs font-mono text-ink-muted tabular-nums">{names.length}</p>
					</div>
					<ul class="mt-3 space-y-1 min-h-[1.5rem]">
						{#each names as name (name)}
							<li class="text-sm text-ink truncate {name === username ? 'font-semibold' : ''}">{name}</li>
						{:else}
							<li class="text-sm text-ink-muted">No one yet</li>
						{/each}
					</ul>
					{#if canChoose}
						<button
							type="button"
							class="btn mt-4 w-full {myTeam === idx ? 'btn-primary' : 'btn-ghost'} press-scale"
							aria-pressed={myTeam === idx}
							onclick={() => choose(idx)}
						>
							{myTeam === idx ? 'Your team' : 'Join team'}
						</button>
					{/if}
				</div>
			{/each}
		</div>
		{#if roster.unassigned.length > 0 && roster.assign === 'choose' && !roster.started}
			<p class="text-xs text-ink-muted text-center mt-3">
				Still choosing: {roster.unassigned.join(', ')}
			</p>
		{/if}
		{#if error}
			<p class="text-sm text-danger text-center mt-3" role="alert">{error}</p>
		{/if}
	</section>
{/if}

<style>
	.team-grid {
		display: grid;
		gap: 0.75rem;
		grid-template-columns: repeat(1, minmax(0, 1fr));
	}
	@media (min-width: 640px) {
		.team-grid {
			grid-template-columns: repeat(min(var(--cols, 2), 2), minmax(0, 1fr));
		}
	}
	@media (min-width: 1024px) {
		.team-grid {
			grid-template-columns: repeat(var(--cols, 2), minmax(0, 1fr));
		}
	}
</style>
