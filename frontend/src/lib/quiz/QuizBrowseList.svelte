<script lang="ts">
	import QuizTableGrid from './QuizTableGrid.svelte';
	import QuizRow, { type QuizRowItem } from './QuizRow.svelte';

	interface Props {
		items: QuizRowItem[];
		onHost?: (id: string) => void;
	}

	let { items, onHost }: Props = $props();
</script>

<QuizTableGrid listAttrs={{ 'data-browse-list': true }}>
	{#snippet rows()}
		{#each items as quiz (quiz.id)}
			<QuizRow {quiz} mode="browse" {onHost} />
		{/each}
	{/snippet}
</QuizTableGrid>
