<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { page } from '$app/state';
	import { Home, RotateCcw } from '@lucide/svelte';

	navbarVisible.visible = true;

	const status = $derived(page.status);
	const message = $derived(
		status === 404
			? 'That page is missing or the link may be outdated.'
			: 'Something went wrong on our side. You can try again or head back home.'
	);
</script>

<svelte:head>
	<title>Error {status} — CMA Clash</title>
</svelte:head>

<div class="min-h-[70vh] flex flex-col items-center justify-center px-4 py-16 text-center">
	<p class="font-display text-gold text-sm tracking-[0.3em] mb-3">Error</p>
	<p class="font-display text-8xl text-ink tabular-nums leading-none">{status}</p>
	<p class="mt-6 max-w-md text-ink-muted text-base leading-relaxed">{message}</p>
	<div class="mt-10 flex flex-wrap items-center justify-center gap-3">
		<a href="/" class="ledger-btn-primary w-auto px-8 inline-flex items-center gap-2">
			<Home class="w-4 h-4" aria-hidden="true" />
			Home
		</a>
		<button
			type="button"
			class="action-button px-8 py-2.5 inline-flex items-center gap-2"
			onclick={() => location.reload()}
		>
			<RotateCcw class="w-4 h-4" aria-hidden="true" />
			Retry
		</button>
	</div>
</div>
