<script lang="ts">
	interface Props {
		label: string;
	}

	let { label }: Props = $props();
</script>

<p
	class="inline-flex items-center bg-primary-soft text-primary px-2.5 py-1 text-[0.66rem] font-mono uppercase tracking-[0.18em]"
>
	{label}
</p>
