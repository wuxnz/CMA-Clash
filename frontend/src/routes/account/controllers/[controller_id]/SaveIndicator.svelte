<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->
<script lang="ts">
	import { SaveStatus } from './commons';
	import Spinner from '$lib/Spinner.svelte';

	interface Props {
		status: SaveStatus;
	}

	let { status }: Props = $props();
</script>

<div class="h-6 w-6 grow-0 my-auto text-ink">
	{#if status === SaveStatus.Saved}
		<svg
			class="h-full w-full text-success"
			aria-hidden="true"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			viewBox="0 0 24 24"
			xmlns="http://www.w3.org/2000/svg"
		>
			<path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round" />
		</svg>
	{:else if status === SaveStatus.Saving}
		<Spinner class="h-full w-full" my_20={false} />
	{/if}
</div>
