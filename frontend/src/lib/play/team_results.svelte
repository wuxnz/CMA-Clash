<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts" module>
	export type TeamResultsPayload = { count: number; teams: TeamResult[] };
	export type TeamResult = {
		index: number;
		name: string;
		members: string[];
		answer: string | null;
		right: boolean | null;
		reason: string | null;
		streak: number;
		points: number;
		total: number;
	};
</script>

<script lang="ts">
	interface Props {
		teams: TeamResultsPayload | null;
		username?: string;
	}

	let { teams, username = '' }: Props = $props();

	const reasonText: Record<string, string> = {
		majority: 'Majority pick',
		tie_first_submitted: 'Tie: first pick won'
	};
</script>

{#if teams && teams.teams.length > 0}
	<section class="max-w-4xl mx-auto w-full px-4 pb-6" aria-label="Team results">
		<p class="eyebrow text-center">Team results</p>
		<div class="team-grid mt-4" style="--cols: {Math.min(teams.teams.length, 4)}">
			{#each teams.teams as team (team.index)}
				<div
					class="border p-4 bg-surface {team.members.includes(username) ? 'border-primary' : 'border-line'}"
				>
					<div class="flex items-center justify-between gap-2">
						<p class="font-display text-lg text-ink">{team.name}</p>
						<p class="text-xs font-mono text-ink-muted tabular-nums">Total {team.total}</p>
					</div>
					{#if team.answer === null}
						<p class="text-sm text-ink-muted mt-3">No answer from this team</p>
					{:else}
						<p class="text-sm mt-3 {team.right ? 'text-success' : 'text-danger'}">
							{team.right ? 'Correct' : 'Wrong'}: {team.answer || '(blank)'}
						</p>
						<p class="text-xs text-ink-muted mt-1">
							{reasonText[team.reason ?? ''] ?? ''}
						</p>
						<p class="text-sm text-ink mt-2 tabular-nums">
							+{team.points}{team.streak > 1 ? ` · streak ${team.streak}` : ''}
						</p>
					{/if}
					<p class="text-xs text-ink-muted mt-3 truncate">{team.members.join(', ')}</p>
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
