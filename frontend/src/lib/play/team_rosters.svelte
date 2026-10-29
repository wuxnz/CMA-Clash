<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts" module>
	export type TeamFinalPayload = {
		count: number;
		teams: TeamRoster[];
	};
	export type TeamRoster = {
		index: number;
		name: string;
		members: string[];
		total: number;
	};
</script>

<script lang="ts">
	interface Props {
		teams: TeamFinalPayload | null;
		username?: string;
	}

	let { teams, username = '' }: Props = $props();
</script>

{#if teams && teams.teams.length > 0}
	<section class="max-w-4xl mx-auto w-full px-4 pt-6" aria-label="Team rosters" data-testid="team-rosters">
		<p class="eyebrow text-center">Teams</p>
		<div class="team-grid mt-4" style="--cols: {Math.min(teams.teams.length, 4)}">
			{#each teams.teams as team (team.index)}
				<div
					class="border p-4 bg-surface {team.members.includes(username) ? 'border-primary' : 'border-line'}"
					data-testid="team-roster-card"
				>
					<div class="flex items-center justify-between gap-2">
						<p class="font-display text-lg text-ink">{team.name}</p>
						<p class="text-xs font-mono text-ink-muted tabular-nums">Total {team.total}</p>
					</div>
					{#if team.members.length === 0}
						<p class="text-sm text-ink-muted mt-3">No players</p>
					{:else}
						<ul class="mt-3 space-y-1">
							{#each team.members as member (member)}
								<li
									class="text-sm {member === username ? 'text-ink font-semibold' : 'text-ink-muted'}"
								>
									{member}{member === username ? ' (you)' : ''}
								</li>
							{/each}
						</ul>
					{/if}
				</div>
			{/each}
		</div>
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
