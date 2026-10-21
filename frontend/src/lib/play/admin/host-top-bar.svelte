<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	interface Props {
		current: number;
		total: number;
		gamePin?: string;
	}

	let { current, total, gamePin }: Props = $props();
</script>

<header
	class="w-full border-b border-white/10 bg-surface/95 backdrop-blur-sm px-4 py-3 flex items-center justify-between gap-3 safe-top"
>
	<div class="min-w-0">
		<p class="text-xs font-semibold uppercase tracking-[0.2em] text-ink-muted">Live host</p>
		<p class="font-display text-2xl text-ink tabular-nums leading-none">
			{current}<span class="text-ink-muted text-lg"> / {total}</span>
		</p>
	</div>
	{#if gamePin}
		<p class="text-sm font-mono text-gold tabular-nums shrink-0">PIN {gamePin}</p>
	{/if}
</header>

<style>
	.safe-top {
		padding-top: max(0.75rem, env(safe-area-inset-top));
	}
</style>
