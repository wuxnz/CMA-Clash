<script lang="ts">
	import type { TopicStat } from '$lib/cma/client';

	interface Props {
		stats: TopicStat[];
		/** Shown when API returns no topic stats yet. */
		demo?: boolean;
	}

	let { stats, demo = false }: Props = $props();

	function cellClass(accuracy: number): string {
		if (accuracy >= 85) return 'bg-primary text-white';
		if (accuracy >= 70) return 'bg-primary/60 text-white';
		if (accuracy >= 50) return 'bg-gold/40 text-ink';
		if (accuracy > 0) return 'bg-danger/30 text-ink';
		return 'bg-paper-muted text-ink-muted';
	}
</script>

<div>
	<h2 class="font-display font-semibold text-ink mb-3">Section mastery</h2>
	{#if demo && stats.length === 0}
		<p class="text-xs text-ink-muted mb-2" data-demo-label="true">
			No topic stats yet — answer questions to populate via
			<code class="font-mono text-xs">/api/v1/clash/me/stats/by-topic</code>.
		</p>
	{/if}
	<div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2">
		{#each stats.length ? stats : demo ? [{ topic_name: '—', topic_slug: 'demo', accuracy_percent: 0, questions_answered: 0, questions_correct: 0, xp_earned: 0 }] : [] as stat (stat.topic_slug ?? stat.topic_name)}
			<div
				class="rounded-lg p-3 text-center text-xs font-medium border border-ink/5 {cellClass(
					stat.accuracy_percent
				)}"
				title="{stat.topic_name}: {stat.accuracy_percent}% ({stat.questions_answered} answered)"
			>
				<p class="truncate font-display">{stat.topic_name ?? stat.topic_slug}</p>
				<p class="font-mono tabular-nums mt-1">{Math.round(stat.accuracy_percent)}%</p>
			</div>
		{/each}
	</div>
</div>
