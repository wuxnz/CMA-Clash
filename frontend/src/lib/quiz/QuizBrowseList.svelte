<script lang="ts">
	import QuizListHeader from './QuizListHeader.svelte';
	import QuizRow, { type QuizRowItem } from './QuizRow.svelte';

	interface Props {
		items: QuizRowItem[];
		onHost?: (id: string) => void;
	}

	let { items, onHost }: Props = $props();
</script>

<QuizListHeader />
<ul data-browse-list>
	{#each items as quiz (quiz.id)}
		<QuizRow {quiz} mode="browse" {onHost} />
	{/each}
</ul>
