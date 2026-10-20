<script lang="ts">
	interface Props {
		name: string;
	}

	let { name }: Props = $props();
</script>

<span
	class="inline-flex items-center rounded-full bg-surface border border-ink/15 px-3 py-1 text-sm font-medium text-ink shadow-sm"
>
	<span class="w-2 h-2 rounded-full bg-primary mr-2" aria-hidden="true"></span>
	{name}
</span>
