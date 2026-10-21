<script lang="ts">
	import QuizListHeader from './QuizListHeader.svelte';
	import {
		quizColActions,
		quizColCert,
		quizColCertDot,
		quizColDifficulty,
		quizColQs,
		quizTableGrid,
		quizTableRowShell
	} from './quizTableLayout';

	interface Props {
		count?: number;
		ariaLabel?: string;
	}

	let { count = 5, ariaLabel = 'Loading quizzes' }: Props = $props();
</script>

<QuizListHeader />
<ul class="animate-pulse" aria-busy="true" aria-label={ariaLabel}>
	{#each { length: count } as _, n (n)}
		<li class="{quizTableGrid} {quizTableRowShell}">
			<div class="flex items-center gap-3 min-w-0">
				<div
					class="w-9 h-9 rounded-md bg-elevated shrink-0 hidden sm:block"
					aria-hidden="true"
				></div>
				<div class="min-w-0 flex-1">
					<div class="h-3 w-2/5 max-w-xs rounded bg-elevated" aria-hidden="true"></div>
					<div class="h-2 w-24 rounded bg-elevated mt-2 md:hidden" aria-hidden="true"></div>
					<div class="hidden md:block h-2 w-32 max-w-full rounded bg-elevated mt-1" aria-hidden="true"></div>
				</div>
			</div>
			<div class={quizColCert} aria-hidden="true">
				<span class="{quizColCertDot} rounded-full bg-elevated"></span>
				<div class="h-2 w-12 rounded bg-elevated"></div>
			</div>
			<div class={quizColQs} aria-hidden="true">
				<div class="h-2 w-4 rounded bg-elevated ml-auto"></div>
			</div>
			<div class={quizColDifficulty} aria-hidden="true">
				<div class="h-2 w-16 max-w-full rounded bg-elevated"></div>
			</div>
			<div class={quizColActions} aria-hidden="true">
				<div class="h-9 w-14 rounded-md bg-elevated"></div>
			</div>
		</li>
	{/each}
</ul>
