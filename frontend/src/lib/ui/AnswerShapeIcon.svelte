<script lang="ts">
	import type { AnswerShape } from './tokens';

	interface Props {
		shape: AnswerShape;
		class?: string;
	}

	let { shape, class: className = 'w-10 h-10' }: Props = $props();
</script>

<svg
	class={className}
	viewBox="0 0 48 48"
	fill="currentColor"
	aria-hidden="true"
	xmlns="http://www.w3.org/2000/svg"
>
	{#if shape === 'triangle'}
		<polygon points="24,6 44,42 4,42" />
	{:else if shape === 'diamond'}
		<polygon points="24,4 44,24 24,44 4,24" />
	{:else if shape === 'circle'}
		<circle cx="24" cy="24" r="18" />
	{:else}
		<rect x="8" y="8" width="32" height="32" rx="4" />
	{/if}
</svg>
