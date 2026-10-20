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
	class="rounded-2xl glass-panel card-interactive {pad[padding]} {className}"
>
	{@render children?.()}
</div>
