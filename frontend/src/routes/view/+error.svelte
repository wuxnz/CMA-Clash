<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { page } from '$app/state';
	navbarVisible.visible= true;
	let status = page.status;
</script>

<svelte:head>
	<title>CMA Clash: Error {status}</title>
</svelte:head>
<h1 class="text-6xl text-center">{status}</h1>

{#if status === 404}
	<p class="text-center">That quiz is missing or the link may be outdated.</p>
{:else}
	<p class="text-center">Something went wrong on our side. Try again or head back home.</p>
{/if}

<div class="flex justify-center mt-8">
	<img
		class="rounded-lg"
		src="https://http.cat/{status}"
		alt="Cat representing the {status}-http error code"
	/>
</div>
