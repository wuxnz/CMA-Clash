<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import LedgerTable from '$lib/ui/LedgerTable.svelte';
	import type { LedgerRow } from '$lib/ui/LedgerTable.svelte';
	import { LEDGER_ANSWER_COLORS } from '$lib/ui/tokens';
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';
	import ExplanationDrawer from '$lib/ui/ExplanationDrawer.svelte';
	import type { Question } from '$lib/quiz_types';

	function sortObjectbyValue(obj) {
		const ret = {};
		Object.keys(obj)
			.sort((a, b) => obj[b] - obj[a])
			.forEach((s) => (ret[s] = obj[s]));
		return ret;
	}

	interface Props {
		scores: any;
		question_results: Array<{
			username: string;
			answer: string;
			right: boolean | string;
			time_taken?: number;
			score?: number;
		}>;
		username: any;
		question?: Question;
	}

	let { scores = $bindable(), question_results, username, question }: Props = $props();

	let sorted_scores = $derived(sortObjectbyValue(scores));

	let answerDistribution = $derived.by(() => {
		const counts: Record<string, number> = {};
		for (const r of question_results) {
			const key = r.answer ?? '(blank)';
			counts[key] = (counts[key] ?? 0) + 1;
		}
		return Object.entries(counts).sort((a, b) => b[1] - a[1]);
	});

	let maxCount = $derived(
		answerDistribution.length ? Math.max(...answerDistribution.map(([, c]) => c)) : 1
	);

	let ledgerRows = $derived.by((): LedgerRow[] => {
		return Object.keys(sorted_scores)
			.slice(0, 5)
			.map((name, idx) => ({
				rank: idx + 1,
				name: name === username ? 'You' : name,
				score: sorted_scores[name],
				isYou: name === username
			}));
	});

	let myRank = $derived(
		Object.keys(sorted_scores).findIndex((n) => n === username) + 1
	);
</script>

<div class="min-h-screen bg-paper flex flex-col">
	<LivePlayHeader rank={myRank > 0 ? myRank : undefined} totalPlayers={Object.keys(sorted_scores).length} />
	<div class="flex-1 max-w-lg mx-auto w-full px-4 py-8 flex flex-col gap-8">
		<div class="text-center">
			<p class="text-sm text-ink-muted uppercase tracking-wide">This question</p>
			<p class="font-mono text-4xl font-bold text-gold tabular-nums mt-1">
				+{score_by_username[username] ?? '0'}
			</p>
			<p class="text-ink-muted mt-2">
				Total: <span class="font-mono tabular-nums text-ink"
					>{sorted_scores[username] ?? '0'}</span
				>
			</p>
		</div>

		{#if answerDistribution.length > 0}
			<div class="rounded-xl border border-ink/10 bg-surface p-4" aria-label="Answer distribution">
				<h2 class="font-display font-semibold text-ink mb-4">Answer distribution</h2>
				<ul class="space-y-3">
					{#each answerDistribution as [answer, count], i}
						<li>
							<div class="flex justify-between text-sm mb-1">
								<span class="font-mono truncate pr-2">{answer}</span>
								<span class="text-ink-muted tabular-nums">{count}</span>
							</div>
							<div class="h-2 rounded-full bg-paper-muted overflow-hidden">
								<div
									class="h-full rounded-full transition-all duration-500"
									style="width: {(count / maxCount) * 100}%; background: {LEDGER_ANSWER_COLORS[
										i % LEDGER_ANSWER_COLORS.length
									]}"
								></div>
							</div>
						</li>
					{/each}
				</ul>
			</div>
		{/if}

		<LedgerTable rows={ledgerRows} caption="Top 5 this game" flip={true} />

		<ExplanationDrawer explanation={question?.explanation} />
	</div>
</div>
