<script lang="ts">
	import LedgerTable from '$lib/ui/LedgerTable.svelte';
	import type { LedgerRow } from '$lib/ui/LedgerTable.svelte';

	interface Props {
		rows: LedgerRow[];
		caption?: string;
	}

	let { rows, caption = 'Standings' }: Props = $props();
</script>

<div class="h-dvh min-h-dvh w-full bg-paper flex flex-col items-center justify-center px-4 py-10">
	<p class="font-display text-gold text-sm tracking-[0.3em] mb-2">Scoreboard</p>
	<h1 class="font-display text-5xl sm:text-7xl text-ink mb-8">Rankings</h1>
	<div class="w-full max-w-xl">
		<LedgerTable {rows} {caption} flip={true} />
	</div>
</div>
