<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->
<script lang="ts">
	import Button from '$lib/ui/Button.svelte';
	import { getLocalization } from '$lib/i18n';
	import { focusTrap } from '$lib/ui/focusTrap';

	const { t } = getLocalization();
	interface Props {
		quiz_id?: string | null;
	}

	let { quiz_id = $bindable(null) }: Props = $props();

	function close() {
		quiz_id = null;
	}

	$effect(() => {
		if (!quiz_id) return;
		const onKey = (e: KeyboardEvent) => {
			if (e.key === 'Escape') close();
		};
		document.addEventListener('keydown', onKey);
		return () => document.removeEventListener('keydown', onKey);
	});
</script>

{#if quiz_id}
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
			aria-labelledby="download-title"
			tabindex="-1"
		>
			<h2 id="download-title" class="text-lg font-semibold text-ink tracking-tight">
				{$t('downloader.select_download_type')}
			</h2>
			<p class="text-sm text-ink-muted mt-2">{$t('downloader.help')}</p>
			<div class="mt-6 flex flex-col gap-2">
				<Button href="/api/v1/eximport/{quiz_id}" class="w-full">
					{$t('downloader.own_format')}
				</Button>
				<Button href="/api/v1/eximport/excel/{quiz_id}" variant="secondary" class="w-full">
					{$t('downloader.excel_format')}
				</Button>
				<Button variant="ghost" class="w-full" onclick={close}>Cancel</Button>
			</div>
		</div>
	</div>
{/if}
