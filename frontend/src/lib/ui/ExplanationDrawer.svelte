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
	<div class="rounded-xl border border-ink/10 bg-surface overflow-hidden">
		<button
			type="button"
			class="w-full flex items-center justify-between px-4 py-3 text-left font-display font-semibold text-ink hover:bg-paper-muted/50 transition"
			aria-expanded={visible}
			onclick={() => (visible = !visible)}
		>
			<span>Explanation</span>
			<span class="text-ink-muted text-sm">{visible ? 'Hide' : 'Show'}</span>
		</button>
		{#if visible}
			<div class="px-4 pb-4 text-sm text-ink-muted leading-relaxed border-t border-ink/5 pt-3">
				{explanation}
			</div>
		{/if}
	</div>
{/if}
