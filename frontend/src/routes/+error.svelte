<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { page } from '$app/state';
	import { Home, RotateCcw } from '@lucide/svelte';
	import Button from '$lib/ui/Button.svelte';

	navbarVisible.visible = true;

	const status = $derived(page.status);
	const message = $derived(
		status === 404
			? 'That page is missing or the link may be outdated.'
			: 'Something went wrong on our side. You can try again or head back home.'
	);
</script>

<svelte:head>
	<title>CMA Clash: Error {status}</title>
</svelte:head>

<div class="min-h-[70vh] flex flex-col items-center justify-center px-4 py-16 text-center">
	<p class="font-display text-8xl text-ink tabular-nums leading-none">{status}</p>
	<p class="mt-6 max-w-md text-ink-muted text-base leading-relaxed">{message}</p>
	<div class="mt-10 flex flex-wrap items-center justify-center gap-3">
		<Button href="/" class="w-auto">
			<Home class="w-4 h-4" aria-hidden="true" />
			Home
		</Button>
		<Button variant="secondary" class="w-auto" onclick={() => location.reload()}>
			<RotateCcw class="w-4 h-4" aria-hidden="true" />
			Retry
		</Button>
	</div>
</div>
