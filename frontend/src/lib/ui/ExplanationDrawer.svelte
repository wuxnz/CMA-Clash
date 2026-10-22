<script lang="ts">
	interface Props {
		explanation: string | null | undefined;
		open?: boolean;
	}

	let { explanation, open = false }: Props = $props();
	let visible = $state(open);

	$effect(() => {
		if (explanation) visible = true;
	});
</script>

{#if explanation}
	<div class="border border-line bg-paper overflow-hidden">
		<button
			type="button"
			class="w-full flex items-center justify-between px-4 py-3 text-left font-display text-ink hover:bg-elevated transition"
			aria-expanded={visible}
			onclick={() => (visible = !visible)}
		>
			<span>Explanation</span>
			<span class="eyebrow">{visible ? 'Hide' : 'Show'}</span>
		</button>
		{#if visible}
			<div class="px-4 pb-4 text-sm text-ink-muted leading-relaxed border-t border-line pt-3">
				{explanation}
			</div>
		{/if}
	</div>
{/if}
