<script lang="ts">
	import QuizTableGrid from './QuizTableGrid.svelte';
	import {
		quizColActions,
		quizColCert,
		quizColCertDot,
		quizColDifficulty,
		quizColQs,
		quizTableDataRow
	} from './quizTableLayout';

	interface Props {
		count?: number;
		ariaLabel?: string;
	}

	let { count = 5, ariaLabel = 'Loading quizzes' }: Props = $props();
</script>

<QuizTableGrid listClass="animate-pulse" ariaLabel={ariaLabel} listAttrs={{ 'aria-busy': true }}>
	{#snippet rows()}
		{#each { length: count } as _, n (n)}
			<li class={quizTableDataRow}>
				<div class="flex min-w-0 items-center gap-3" data-quiz-col="title">
					<div
						class="hidden h-9 w-9 shrink-0 rounded-md bg-elevated sm:block"
						aria-hidden="true"
					></div>
					<div class="min-w-0 flex-1">
						<div class="h-3 w-2/5 max-w-xs rounded bg-elevated" aria-hidden="true"></div>
						<div class="mt-2 h-2 w-24 rounded bg-elevated md:hidden" aria-hidden="true"></div>
						<div
							class="mt-1 hidden h-2 w-32 max-w-full rounded bg-elevated md:block"
							aria-hidden="true"
						></div>
					</div>
				</div>
				<div class={quizColCert} data-quiz-col="cert" aria-hidden="true">
					<span class="{quizColCertDot} rounded-full bg-elevated"></span>
					<div class="h-2 w-12 rounded bg-elevated"></div>
				</div>
				<div class={quizColQs} data-quiz-col="qs" aria-hidden="true">
					<div class="ml-auto h-2 w-4 rounded bg-elevated"></div>
				</div>
				<div class={quizColDifficulty} data-quiz-col="difficulty" aria-hidden="true">
					<div class="h-2 w-16 max-w-full rounded bg-elevated"></div>
				</div>
				<div class={quizColActions} data-quiz-col="actions" aria-hidden="true">
					<div class="h-9 w-14 rounded-md bg-elevated"></div>
				</div>
			</li>
		{/each}
	{/snippet}
</QuizTableGrid>
