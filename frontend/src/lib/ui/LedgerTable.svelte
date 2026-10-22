<script lang="ts">
	import { tick } from 'svelte';
	import { loadFlip } from '$lib/motion/gsap';
	import AnimatedCounter from './AnimatedCounter.svelte';

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
		flip?: boolean;
	}

	let { rows, caption = 'Leaderboard', flip = false }: Props = $props();

	function scoreAsNumber(score: number | string): number | null {
		if (typeof score === 'number') return score;
		const n = parseFloat(String(score).replace(/,/g, ''));
		return Number.isFinite(n) ? n : null;
	}

	let tbodyRef: HTMLTableSectionElement | undefined;
	let prevKey = $state('');

	const rowKey = (rows: LedgerRow[]) => rows.map((r) => `${r.name}:${r.rank}`).join('|');

	$effect(() => {
		const key = rowKey(rows);
		if (!flip || typeof window === 'undefined') {
			prevKey = key;
			return;
		}
		if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
			prevKey = key;
			return;
		}
		if (prevKey && prevKey !== key && tbodyRef) {
			(async () => {
				const { gsap, Flip } = await loadFlip();
				const state = Flip.getState(tbodyRef.querySelectorAll('tr'));
				await tick();
				Flip.from(state, {
					duration: 0.55,
					ease: 'power2.out',
					absolute: true,
					nested: true,
					onEnter: (els) =>
						gsap.fromTo(
							els,
							{ opacity: 0, y: 8 },
							{ opacity: 1, y: 0, duration: 0.35 }
						),
					onLeave: (els) => gsap.to(els, { opacity: 0, duration: 0.2 })
				});
			})();
		}
		prevKey = key;
	});
</script>

<div class="border border-line bg-paper overflow-hidden">
	<table class="w-full text-sm" aria-label={caption}>
		<thead class="bg-paper-muted text-ink-subtle text-left">
			<tr>
				<th
					class="px-3 py-2.5 font-mono font-normal text-[0.64rem] uppercase tracking-[0.2em] w-12"
					>#</th
				>
				<th
					class="px-3 py-2.5 font-mono font-normal text-[0.64rem] uppercase tracking-[0.2em]"
					>Player</th
				>
				<th
					class="px-3 py-2.5 font-mono font-normal text-[0.64rem] uppercase tracking-[0.2em] text-right"
					>Score</th
				>
			</tr>
		</thead>
		<tbody bind:this={tbodyRef}>
			{#each rows as row (row.name)}
				<tr
					data-testid="scoreboard-row"
					class="border-t border-line transition-colors {row.isYou
						? 'bg-primary-soft font-medium'
						: 'hover:bg-elevated'}"
				>
					<td class="px-3 py-3 font-mono tabular-nums text-ink-subtle">{row.rank}</td>
					<td class="px-3 py-3 text-ink">
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
					<td class="px-3 py-3 text-right font-mono tabular-nums">
						{#if scoreAsNumber(row.score) !== null}
							<AnimatedCounter value={scoreAsNumber(row.score)!} duration={0.9} />
						{:else}
							{row.score}
						{/if}
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
