<script lang="ts">
	import LedgerTable from '$lib/ui/LedgerTable.svelte';
	import type { LedgerRow } from '$lib/ui/LedgerTable.svelte';

	interface Props {
		rows: LedgerRow[];
		caption?: string;
		hostFit?: boolean;
	}

	let { rows, caption = 'Standings', hostFit = false }: Props = $props();
</script>

<div
	class="w-full bg-paper flex flex-col items-center px-4 {hostFit
		? 'h-full min-h-0 py-4 sm:py-6 justify-start'
		: 'h-dvh min-h-dvh py-10 justify-center'}"
>
	<p class="font-display text-gold text-xs sm:text-sm tracking-[0.3em] mb-1">Scoreboard</p>
	<h1
		class="font-display text-ink mb-4 sm:mb-6 {hostFit
			? 'text-3xl sm:text-5xl'
			: 'text-5xl sm:text-7xl mb-8'}"
	>
		Rankings
	</h1>
	<div class="w-full max-w-xl flex-1 min-h-0 overflow-y-auto" data-testid="live-scoreboard">
		<LedgerTable {rows} {caption} flip={true} />
	</div>
</div>
