<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Button from '$lib/ui/Button.svelte';
	import { focusTrap } from '$lib/ui/focusTrap';

	interface Props {
		title: string;
		body: string;
		open: boolean;
	}

	let { title, body, open = $bindable() }: Props = $props();

	function close() {
		open = false;
	}

	$effect(() => {
		if (!open) return;
		const onKey = (e: KeyboardEvent) => {
			if (e.key === 'Escape') close();
		};
		document.addEventListener('keydown', onKey);
		return () => document.removeEventListener('keydown', onKey);
	});
</script>

{#if open}
	<div
		class="dialog-backdrop"
		onclick={(e) => {
			if (e.target === e.currentTarget) close();
		}}
		role="presentation"
	>
		<div
			use:focusTrap
			class="dialog-panel dialog-panel-in p-5"
			role="dialog"
			aria-modal="true"
			aria-labelledby="alert-title"
			tabindex="-1"
		>
			<h2 id="alert-title" class="text-lg font-semibold text-ink tracking-tight">{title}</h2>
			<p class="text-sm text-ink-muted mt-2 leading-relaxed">{body}</p>
			<div class="mt-6">
				<Button class="w-full" onclick={close}>Close</Button>
			</div>
		</div>
	</div>
{/if}
