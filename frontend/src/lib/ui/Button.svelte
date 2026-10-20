<script lang="ts">
	interface Props {
		href?: string;
		variant?: 'primary' | 'secondary' | 'ghost';
		type?: 'button' | 'submit';
		disabled?: boolean;
		class?: string;
		onclick?: (e: MouseEvent) => void;
		children?: import('svelte').Snippet;
	}

	let {
		href,
		variant = 'primary',
		type = 'button',
		disabled = false,
		class: className = '',
		onclick,
		children
	}: Props = $props();

	const variantClass = $derived(
		variant === 'secondary' ? 'btn-secondary' : variant === 'ghost' ? 'btn-ghost' : 'btn-primary'
	);
	const classes = $derived(`btn ${variantClass} ${className}`);
</script>

{#if href}
	<a {href} class={classes} aria-disabled={disabled || undefined} {onclick}>
		{@render children?.()}
	</a>
{:else}
	<button {type} {disabled} class={classes} {onclick}>
		{@render children?.()}
	</button>
{/if}
