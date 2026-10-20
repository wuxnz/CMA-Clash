<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	interface Props {
		headerText: any;
		expanded?: boolean;
		children?: import('svelte').Snippet;
	}

	let { headerText, expanded = $bindable(false), children }: Props = $props();
</script>

<div>
	<h3 class="m-0">
		<button
			type="button"
			aria-expanded={expanded}
			onclick={() => (expanded = !expanded)}
			class="flex items-center justify-between w-full min-h-11 gap-3 py-2 text-left text-sm font-medium text-ink press-scale"
		>
			<span class="min-w-0">{@html headerText}</span>
			<svg
				viewBox="0 0 20 20"
				fill="none"
				class="shrink-0 text-ink-muted w-3 h-3"
				class:rotate-45={expanded}
				stroke="currentColor"
				aria-hidden="true"
			>
				<path d="M10 1V19" stroke-width="2" />
				<path d="M1 10L19 10" stroke-width="2" />
			</svg>
		</button>
	</h3>

	<div class:hidden={!expanded}>
		{@render children?.()}
	</div>
</div>
