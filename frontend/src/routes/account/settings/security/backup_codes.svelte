<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import Button from '$lib/ui/Button.svelte';
	import { focusTrap } from '$lib/ui/focusTrap';

	const { t } = getLocalization();
	let { backup_code = $bindable() } = $props();

	let already_downloaded = false;

	const download_code = (force = false) => {
		if (already_downloaded && !force) {
			return;
		}
		const el = document.createElement('a');
		el.setAttribute('href', `data:text/plain;charset=utf-8,${backup_code}`);
		el.setAttribute('download', 'CMA-Clash-Backup-Code.txt');
		el.style.display = 'none';
		document.body.appendChild(el);
		el.click();
		document.body.removeChild(el);
		already_downloaded = true;
	};

	function close() {
		backup_code = undefined;
	}
</script>

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
		aria-labelledby="backup-code-title"
		tabindex="-1"
	>
		<h2 id="backup-code-title" class="text-lg font-semibold text-ink tracking-tight">
			{$t('security_settings.backup_codes.your_backup_code')}
		</h2>
		<p
			class="select-all font-mono text-sm text-ink break-all mt-4"
			onclick={() => download_code(false)}
		>
			{backup_code}
		</p>
		<p class="text-sm text-ink-muted mt-3">
			{$t('security_settings.backup_codes.save_somewhere_save')}
		</p>
		<div class="mt-6 flex flex-col-reverse sm:flex-row gap-2">
			<Button variant="secondary" class="w-full sm:w-auto" onclick={close}>
				{$t('words.close')}
			</Button>
			<Button class="w-full sm:flex-1" onclick={() => download_code(true)}>
				{$t('security_settings.backup_codes.download_code')}
			</Button>
		</div>
	</div>
</div>
