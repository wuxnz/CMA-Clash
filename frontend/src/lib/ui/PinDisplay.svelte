<script lang="ts">
	interface Props {
		pin: string;
		size?: 'md' | 'lg';
	}

	let { pin, size = 'lg' }: Props = $props();

	let formatted = $derived(
		pin.replace(/\D/g, '').replace(/(\d{3})(?=\d)/g, '$1 ').trim()
	);
</script>

<p
	class="font-mono tabular-nums tracking-widest text-ink select-all {size === 'lg'
		? 'text-4xl sm:text-5xl'
		: 'text-2xl'}"
	aria-label="Game PIN {formatted}"
>
	{formatted}
</p>
