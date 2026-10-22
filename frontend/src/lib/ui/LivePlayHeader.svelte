<script lang="ts">
	interface Props {
		pin?: string;
		rank?: number;
		totalPlayers?: number;
		rankDelta?: number;
	}

	let { pin, rank, totalPlayers, rankDelta }: Props = $props();
</script>

<header
	class="flex flex-wrap items-center justify-between gap-2 px-4 sm:px-8 py-3 border-b border-line bg-paper/95 backdrop-blur-sm"
>
	<div class="flex items-baseline gap-3 min-w-0">
		<span class="font-display text-lg text-ink shrink-0"
			>CMA <em class="italic font-normal">Clash</em></span
		>
		{#if pin}
			<span class="eyebrow truncate">
				Live · PIN <span class="font-mono tabular-nums">{pin}</span>
			</span>
		{/if}
	</div>
	{#if rank !== undefined && totalPlayers !== undefined}
		<div class="font-mono text-sm tabular-nums text-ink flex items-center gap-1">
			<span>#{rank} / {totalPlayers}</span>
			{#if rankDelta !== undefined && rankDelta !== 0}
				<span class={rankDelta > 0 ? 'text-success' : 'text-danger'} aria-hidden="true">
					{rankDelta > 0 ? '▲' : '▼'}{Math.abs(rankDelta)}
				</span>
			{/if}
		</div>
	{/if}
</header>
