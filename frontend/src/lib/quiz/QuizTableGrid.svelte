<script lang="ts">
	import type { Snippet } from 'svelte';
	import QuizListHeader from './QuizListHeader.svelte';
	import { quizTableDesktopShell } from './quizTableLayout';

	interface Props {
		listClass?: string;
		ariaLabel?: string;
		/** Extra attributes for the list (e.g. data-browse-list). */
		listAttrs?: Record<string, string | boolean | undefined>;
		rows: Snippet;
	}

	let { listClass = '', ariaLabel, listAttrs = {}, rows }: Props = $props();
</script>

<div class={quizTableDesktopShell} data-quiz-table>
	<QuizListHeader />
	<ul
		class="m-0 list-none p-0 md:contents {listClass}"
		aria-label={ariaLabel}
		{...listAttrs}
	>
		{@render rows()}
	</ul>
</div>
