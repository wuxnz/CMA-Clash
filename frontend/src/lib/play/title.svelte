<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { onMount } from 'svelte';
	import Countdown from '$lib/ui/Countdown.svelte';
	import Card from '$lib/ui/Card.svelte';
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';

	interface Props {
		title: string;
		description: string;
		cover_image: string | undefined;
	}

	let { title, description, cover_image }: Props = $props();

	let showCountdown = $state(true);

	onMount(() => {
		showCountdown = true;
	});
</script>

{#if showCountdown}
	<Countdown onComplete={() => (showCountdown = false)} />
{/if}

<div class="min-h-screen bg-paper flex flex-col">
	<LivePlayHeader />
	<div class="flex-1 flex flex-col justify-center items-center px-4 py-12">
		<Card class="max-w-xl w-full text-center">
			<h1 class="font-display text-3xl sm:text-4xl font-bold text-ink">{@html title}</h1>
			{#if description}
				<p class="text-ink-muted mt-4 text-lg">{@html description}</p>
			{/if}
			{#if cover_image}
				<div class="mt-8 flex justify-center">
					<img
						class="max-h-[28vh] rounded-lg border border-ink/10 object-contain"
						src="/api/v1/storage/download/{cover_image}"
						alt=""
					/>
				</div>
			{/if}
			<p class="mt-8 text-sm text-primary font-medium animate-pulse motion-reduce:animate-none">
				Get ready…
			</p>
		</Card>
	</div>
</div>
