<script lang="ts">
	interface Props {
		label: string;
	}

	let { label }: Props = $props();
</script>

<p
	class="inline-flex items-center rounded-md bg-primary/10 text-primary px-2.5 py-0.5 text-xs font-mono font-medium tracking-wide"
>
	{label}
</p>
