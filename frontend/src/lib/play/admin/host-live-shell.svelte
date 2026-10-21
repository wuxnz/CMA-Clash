<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import HostTopBar from '$lib/play/admin/host-top-bar.svelte';
	import type { Snippet } from 'svelte';

	interface Props {
		current: number;
		total: number;
		gamePin?: string;
		showTopBar?: boolean;
		children: Snippet;
	}

	let { current, total, gamePin, showTopBar = true, children }: Props = $props();
</script>

<div class="h-dvh max-h-dvh w-full bg-paper flex flex-col overflow-hidden">
	{#if showTopBar && total > 0}
		<HostTopBar {current} {total} {gamePin} />
	{/if}
	<main class="flex-1 min-h-0 overflow-y-auto overflow-x-hidden">
		{@render children()}
	</main>
</div>
