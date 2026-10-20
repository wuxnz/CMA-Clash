<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import VotingResults from './voting_results.svelte';
	import { fly } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { getLocalization } from '$lib/i18n';
	import type { Question } from '$lib/quiz_types';
	import { QuizQuestionType } from '$lib/quiz_types';
	import LedgerTable from '$lib/ui/LedgerTable.svelte';
	import type { LedgerRow } from '$lib/ui/LedgerTable.svelte';
	import ExplanationDrawer from '$lib/ui/ExplanationDrawer.svelte';
	import { LEDGER_ANSWER_COLORS } from '$lib/ui/tokens';
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';

	const { t } = getLocalization();

	interface Props {
		data: any;
		question: Question;
		new_data: Array<{
			username: string;
			answer: string;
			right: boolean;
			time_taken: number;
			score: number;
		}>;
	}

	let { data = $bindable(), question, new_data }: Props = $props();

	const group_username_by_score = (new_d: typeof new_data): Record<string, number> => {
		const ret_data: Record<string, number> = {};
		for (const i of new_d) {
			ret_data[i.username] = i.score;
		}
		return ret_data;
	};
	let score_by_username = $derived(group_username_by_score(new_data));

	let player_names = $derived(
		Object.keys(data).sort((a, b) => {
			const scoreA = parseFloat(String(data[a])) || 0;
			const scoreB = parseFloat(String(data[b])) || 0;
			return scoreB - scoreA;
		})
	);

	if (JSON.stringify(data) === '{}') {
		for (const i of new_data) {
			data[i.username] = 0;
		}
	}

	let show_new_score_clicked = $state(false);

	const show_new_score = () => {
		for (const i of player_names) {
			if (isNaN(data[i])) {
				data[i] = 0;
			}
			data[i] = (score_by_username[i] ?? 0) + data[i];
		}
		for (const i of new_data) {
			if (!data[i.username]) {
				data[i.username] = score_by_username[i.username];
			}
		}
		show_new_score_clicked = true;
		setTimeout(() => {
			data = data;
		}, 800);
	};

	onMount(() => {
		setTimeout(show_new_score, 1000);
	});

	let answerDistribution = $derived.by(() => {
		const counts: Record<string, number> = {};
		for (const r of new_data) {
			const key = r.answer ?? '(blank)';
			counts[key] = (counts[key] ?? 0) + 1;
		}
		return Object.entries(counts).sort((a, b) => b[1] - a[1]);
	});

	let maxCount = $derived(
		answerDistribution.length ? Math.max(...answerDistribution.map(([, c]) => c)) : 1
	);

	let ledgerRows = $derived.by((): LedgerRow[] => {
		return player_names.slice(0, 5).map((name, idx) => ({
			rank: idx + 1,
			name,
			score: data[name],
			delta: show_new_score_clicked ? score_by_username[name] : undefined
		}));
	});
</script>

<div class="min-h-screen bg-paper flex flex-col pb-12">
	<LivePlayHeader />
	<div class="max-w-3xl mx-auto w-full px-4 py-8 flex flex-col gap-8">
		<h2 class="font-display text-2xl font-bold text-center text-ink">
			{$t('words.result', { count: 2 })}
		</h2>

		<LedgerTable rows={ledgerRows} caption="Question leaderboard" />

		{#if show_new_score_clicked}
			<p class="text-center text-sm text-ink-muted" in:fly={{ y: 8 }}>
				{$t('play_page.points_added')} applied
			</p>
		{/if}

		{#if answerDistribution.length > 0}
			<div class="rounded-xl border border-ink/10 bg-surface p-4">
				<h3 class="font-display font-semibold mb-4">Answer distribution</h3>
				<ul class="space-y-3">
					{#each answerDistribution as [answer, count], i (answer)}
						<li>
							<div class="flex justify-between text-sm mb-1">
								<span class="font-mono truncate pr-2">{answer}</span>
								<span class="tabular-nums text-ink-muted">{count}</span>
							</div>
							<div class="h-2 rounded-full bg-paper-muted overflow-hidden">
								<div
									class="h-full rounded-full"
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

		<ExplanationDrawer explanation={question.explanation} />

		{#if [QuizQuestionType.ABCD, QuizQuestionType.VOTING, QuizQuestionType.TEXT].includes(question.type)}
			<div class="mt-4">
				<VotingResults data={new_data} {question} />
			</div>
		{/if}
	</div>
</div>
