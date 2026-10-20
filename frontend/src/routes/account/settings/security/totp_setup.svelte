<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import QRCode from 'qrcode';
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import Button from '$lib/ui/Button.svelte';
	import { focusTrap } from '$lib/ui/focusTrap';

	const { t } = getLocalization();

	interface Props {
		totp_data: { url: string; secret: string } | undefined;
	}

	let { totp_data = $bindable() }: Props = $props();

	const get_image_url = async () => {
		return await QRCode.toDataURL(totp_data.url);
	};

	function close() {
		totp_data = undefined;
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
		aria-labelledby="totp-setup-title"
		tabindex="-1"
	>
		<div class="dialog-body">
			<h2 id="totp-setup-title" class="text-lg font-semibold text-ink tracking-tight">
				{$t('security_settings.totp_setup.totp_setup')}
			</h2>
			<p class="text-sm text-ink-muted mt-2">
				{$t('security_settings.totp_setup.scan_to_set_up')}
			</p>
			{#await get_image_url()}
				<Spinner my_20={false} />
			{:then data}
				<img src={data} alt="QR code for authenticator setup" class="mx-auto mt-4 w-40 h-40 bg-white p-2 rounded-lg" />
			{/await}
			<p class="mt-4 text-xs text-ink-muted">
				{$t('security_settings.totp_setup.enter_as_secret_if_no_see_code')}
			</p>
			<p class="mt-2 select-all font-mono text-sm text-ink break-all">{totp_data.secret}</p>
			<p class="mt-4 text-sm text-ink-muted">
				{$t('security_settings.totp_setup.do_not_forget_backup_code')}
			</p>
		</div>
		<div class="mt-6">
			<Button class="w-full" onclick={close}>{$t('words.close')}</Button>
		</div>
	</div>
</div>
