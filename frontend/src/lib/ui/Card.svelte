<script lang="ts">
	interface Props {
		class?: string;
		padding?: 'sm' | 'md' | 'lg';
		children?: import('svelte').Snippet;
	}

	let { class: className = '', padding = 'md', children }: Props = $props();

	const pad = { sm: 'p-4', md: 'p-6', lg: 'p-8' };
</script>

<div
	class="rounded-2xl glass-panel {pad[padding]} transition-shadow duration-300 hover:shadow-[var(--shadow-glow)] {className}"
>
	{@render children?.()}
</div>
