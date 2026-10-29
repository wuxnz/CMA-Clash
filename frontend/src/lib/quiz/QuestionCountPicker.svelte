<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	interface Props {
		/** Fewest questions a game can use. */
		min: number;
		/** Size of the quiz bank: the most questions a game can use. */
		max: number;
		/** Chosen question count. */
		value: number;
		disabled?: boolean;
	}

	let { min, max, value = $bindable(), disabled = false }: Props = $props();

	const id = `question-count-${Math.random().toString(36).slice(2, 8)}`;
</script>

<div class="flex flex-col gap-2">
	<div class="flex items-baseline justify-between gap-4">
		<label for={id} class="text-sm font-medium text-ink">Questions in this game</label>
		<span class="font-mono text-sm text-ink tabular-nums">{value} of {max}</span>
	</div>
	<input
		{id}
		type="range"
		{min}
		{max}
		step="1"
		bind:value
		{disabled}
		class="w-full accent-primary"
		aria-describedby="{id}-help"
	/>
	<p id="{id}-help" class="text-xs text-ink-muted">
		Choose between {min} and {max} questions. Each player sees the same questions in a random order.
	</p>
</div>
