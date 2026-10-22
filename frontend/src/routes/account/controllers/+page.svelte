<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { resolve } from '$app/paths';
	import type { PageData } from './$types';
	import Button from '$lib/ui/Button.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import { getLocalization } from '$lib/i18n';
	const { t } = getLocalization();
	navbarVisible.visible = true;
	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	const controllers: [] = data.controllers;
</script>

<svelte:head>
	<title>CMA Clash: Controllers</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
		<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
			<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Quiz controllers</h1>
			<Button href="/account/controllers/add" class="w-full sm:w-auto">
				{$t('controllers.add_new_controller')}
			</Button>
		</div>

		{#if controllers.length === 0}
			<p class="text-sm text-ink-muted mt-8">No controllers yet.</p>
		{:else}
			<div class="mt-6 overflow-x-auto min-w-0">
				<table class="w-full text-sm text-left min-w-[36rem]">
					<thead>
						<tr class="text-xs text-ink-muted border-b border-white/[0.07]">
							<th class="py-2 pr-3 font-medium">{$t('words.name')}</th>
							<th class="py-2 pr-3 font-medium">{$t('controllers.player_name')}</th>
							<th class="py-2 pr-3 font-medium">{$t('controllers.first_seen')}</th>
							<th class="py-2 pr-3 font-medium">{$t('controllers.last_seen')}</th>
							<th class="py-2 font-medium">{$t('words.version')}</th>
						</tr>
					</thead>
					<tbody>
						{#each data.controllers as controller (controller.id)}
							<tr class="border-b border-white/[0.07]">
								<td class="py-3 pr-3">
									<a href={resolve('/account/controllers/[controller_id]', { controller_id: controller.id })} class="text-ink link-hover visited:text-ink">
										{controller.name}
									</a>
								</td>
								<td class="py-3 pr-3 text-ink-muted">{controller.player_name}</td>
								<td class="py-3 pr-3 text-ink-muted tabular-nums whitespace-nowrap">
									{controller.first_seen
										? new Date(controller.first_seen).toLocaleString()
										: $t('words.never')}
								</td>
								<td class="py-3 pr-3 text-ink-muted tabular-nums whitespace-nowrap">
									{controller.last_seen
										? new Date(controller.last_seen).toLocaleString()
										: $t('words.never')}
								</td>
								<td class="py-3 text-ink-muted">{controller.os_version ?? $t('words.unknown')}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</div>
	<Footer />
</div>
