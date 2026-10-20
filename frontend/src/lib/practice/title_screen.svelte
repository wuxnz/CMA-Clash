<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { fly } from 'svelte/transition';
	import Card from '$lib/ui/Card.svelte';

	let { data = $bindable() } = $props();

	const { t } = getLocalization();
</script>

<div
	class="w-full px-4 lg:px-12 h-[80vh] absolute flex justify-center"
	in:fly|global={{ x: 100 }}
	out:fly|global={{ x: -100 }}
>
	<Card class="w-full max-w-2xl h-full overflow-auto" padding="lg">
		<h1 class="font-display text-2xl font-bold text-ink text-center">{@html data.title}</h1>
		<p class="text-ink-muted text-center mt-4">{@html data.description}</p>

		{#if data.cover_image != undefined && data.cover_image !== ''}
			<div class="flex justify-center pt-8">
				<img
					src="/api/v1/storage/download/{data.cover_image}"
					alt=""
					class="max-h-48 rounded-lg border border-ink/10 object-contain"
					oncontextmenu={(e) => {
						e.preventDefault();
						data.cover_image = '';
					}}
				/>
			</div>
		{/if}
		<div class="pt-8 w-full flex justify-center gap-2 text-sm text-ink-muted">
			{#if data.public}
				<span aria-hidden="true">🌐</span>
				<span>{$t('words.public')}</span>
			{:else}
				<span aria-hidden="true">🔒</span>
				<span>{$t('words.private')}</span>
			{/if}
		</div>
	</Card>
</div>
