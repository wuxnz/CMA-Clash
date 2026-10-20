<script lang="ts">
	/** Climb-style retention cues — shown when data is available (dashboard / leaderboard). */
	interface Props {
		streakDays?: number;
		dailyGoalPercent?: number;
		leagueName?: string;
	}

	let { streakDays = 0, dailyGoalPercent = 0, leagueName }: Props = $props();
</script>

{#if streakDays > 0 || dailyGoalPercent > 0 || leagueName}
	<div class="flex flex-wrap gap-3 text-sm">
		{#if streakDays > 0}
			<div
				class="inline-flex items-center gap-2 rounded-lg border border-ink/10 bg-surface px-3 py-2"
			>
				<span class="text-gold" aria-hidden="true">🔥</span>
				<span><span class="font-mono tabular-nums font-semibold">{streakDays}</span>-day streak</span>
			</div>
		{/if}
		{#if dailyGoalPercent > 0}
			<div
				class="inline-flex items-center gap-2 rounded-lg border border-ink/10 bg-surface px-3 py-2 min-w-[10rem]"
			>
				<span class="text-ink-muted shrink-0">Daily goal</span>
				<div class="flex-1 h-2 rounded-full bg-paper-muted overflow-hidden">
					<div
						class="h-full bg-primary rounded-full transition-all"
						style="width: {Math.min(100, dailyGoalPercent)}%"
					></div>
				</div>
				<span class="font-mono text-xs tabular-nums">{dailyGoalPercent}%</span>
			</div>
		{/if}
		{#if leagueName}
			<div
				class="inline-flex items-center gap-2 rounded-lg border border-primary/30 bg-primary/5 px-3 py-2"
			>
				<span class="font-medium text-primary">{leagueName}</span>
			</div>
		{/if}
	</div>
{/if}
