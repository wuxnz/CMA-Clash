<script lang="ts">
	export type LedgerRow = {
		rank: number;
		name: string;
		score: number | string;
		isYou?: boolean;
		delta?: number;
	};

	interface Props {
		rows: LedgerRow[];
		caption?: string;
	}

	let { rows, caption = 'Leaderboard' }: Props = $props();
</script>

<div class="rounded-xl border border-ink/10 bg-surface overflow-hidden shadow-sm">
	<table class="w-full text-sm" aria-label={caption}>
		<thead class="bg-paper-muted/80 text-ink-muted text-left">
			<tr>
				<th class="px-3 py-2 font-medium w-12">#</th>
				<th class="px-3 py-2 font-medium">Player</th>
				<th class="px-3 py-2 font-medium text-right">Score</th>
			</tr>
		</thead>
		<tbody>
			{#each rows as row (row.rank + row.name)}
				<tr
					class="border-t border-ink/5 transition-colors {row.isYou
						? 'bg-primary/10 font-medium'
						: 'hover:bg-paper-muted/50'}"
				>
					<td class="px-3 py-2.5 font-mono tabular-nums text-ink-muted">{row.rank}</td>
					<td class="px-3 py-2.5 text-ink">
						{row.name}
						{#if row.delta !== undefined && row.delta !== 0}
							<span
								class="ml-1.5 text-xs font-mono {row.delta > 0
									? 'text-success'
									: 'text-danger'}"
								aria-label={row.delta > 0 ? 'Rank up' : 'Rank down'}
							>
								{row.delta > 0 ? '▲' : '▼'}{Math.abs(row.delta)}
							</span>
						{/if}
					</td>
					<td class="px-3 py-2.5 text-right font-mono tabular-nums">{row.score}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
