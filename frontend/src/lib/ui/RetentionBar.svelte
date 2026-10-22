<script lang="ts">
	import { Flame, Target, Medal } from '@lucide/svelte';
	import AnimatedCounter from './AnimatedCounter.svelte';

	/** Climb-style retention cues — shown when data is available (dashboard / leaderboard). */
	interface Props {
		streakDays?: number;
		dailyGoalPercent?: number;
		/** When true, daily goal bar is illustrative until a daily-goal API exists. */
		dailyGoalIsDemo?: boolean;
		leagueName?: string;
		/** When true, league chip is illustrative (no weekly league match yet). */
		leagueIsDemo?: boolean;
	}

	let {
		streakDays = 0,
		dailyGoalPercent = 0,
		dailyGoalIsDemo = false,
		leagueName,
		leagueIsDemo = false
	}: Props = $props();
</script>

{#if streakDays > 0 || dailyGoalPercent > 0 || leagueName}
	<div class="flex flex-wrap gap-3 text-sm">
		{#if streakDays > 0}
			<div class="inline-flex items-center gap-2 border border-line bg-paper px-3 py-2">
				<Flame class="w-4 h-4 text-primary shrink-0" aria-hidden="true" />
				<span
					><AnimatedCounter value={streakDays} duration={0.8} class="font-semibold" />-day
					streak</span
				>
			</div>
		{/if}
		{#if dailyGoalPercent > 0}
			<div
				class="inline-flex items-center gap-2 border border-line bg-paper px-3 py-2 min-w-[10rem]"
				data-demo-label={dailyGoalIsDemo ? 'true' : undefined}
			>
				<Target class="w-4 h-4 text-ink-subtle shrink-0" aria-hidden="true" />
				<span class="text-ink-muted shrink-0"
					>Daily goal{dailyGoalIsDemo ? ' (demo)' : ''}</span
				>
				<div class="flex-1 h-1.5 bg-elevated overflow-hidden">
					<div
						class="h-full bg-primary transition-[width] duration-150 ease-linear"
						style="width: {Math.min(100, dailyGoalPercent)}%"
					></div>
				</div>
				<span class="text-xs tabular-nums">{dailyGoalPercent}%</span>
			</div>
		{/if}
		{#if leagueName}
			<div
				class="inline-flex items-center gap-2 border border-primary/40 bg-primary-soft px-3 py-2"
				data-demo-label={leagueIsDemo ? 'true' : undefined}
			>
				<Medal class="w-4 h-4 text-primary shrink-0" aria-hidden="true" />
				<span class="font-medium text-primary"
					>{leagueName}{leagueIsDemo ? ' (preview)' : ''}</span
				>
			</div>
		{/if}
	</div>
{/if}
