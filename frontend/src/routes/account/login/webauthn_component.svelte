<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { startAuthentication } from '@simplewebauthn/browser';
	import { getLocalization } from '$lib/i18n';
	import Button from '$lib/ui/Button.svelte';
	// import { alertModal } from '$lib/stores';

	const { t } = getLocalization();
	let {
		session_data,
		selected_method = $bindable(),
		done = $bindable(),
		step = $bindable()
	} = $props();

	let isLoading = $state(false);

	const start_thing = async () => {
		const data = JSON.parse(session_data.webauthn_data);
		let asseResp;
		isLoading = true;
		try {
			asseResp = await startAuthentication({ optionsJSON: data });
		} catch (e) {
			console.error(e);
			/*			alertModal.set({
				open: true,
				body: e,
				title: 'Unknown error'
			});*/
			alert('Unknown error');
			isLoading = false;
		}
		const res = await fetch(
			`/api/v1/login/step/${step}?session_id=${session_data.session_id}`,
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ auth_type: 'PASSKEY', data: asseResp })
			}
		);
		if (res.status === 200) {
			window.location.reload();
			done = true;
		} else if (res.status === 202) {
			step += 1;
			selected_method = null;
		} else if (res.status === 401) {
			let data;
			try {
				data = await res.json();
			} catch {
				/*				alertModal.set({
					open: true,
					body: "This shouldn't happen. Please try again.",
					title: 'Unknown error'
				});*/
				alert('Unknown error');
				window.location.reload();
			}
			if (data.detail === 'webauthn failed') {
				/*				alertModal.set({
					open: true,
					body: 'Webauthn failed. Please try again.',
					title: 'Webauthn Error'
				});*/
				alert('Webauthn failed');
			}
		}
		isLoading = false;
	};
</script>

<div class="px-6 py-6">
	<h2 class="text-xl font-semibold text-ink tracking-tight text-center">Security key</h2>
	<p class="mt-1 text-sm text-center text-ink-muted">Use your passkey or hardware key</p>

	<div class="flex items-center justify-between gap-3 mt-6">
		<button
			type="button"
			onclick={() => {
				selected_method = 'BACKUP';
			}}
			class="text-sm text-ink-muted link-hover min-h-11"
		>
			{$t('login_page.use_backup_code')}
		</button>
		<Button class="w-auto" disabled={isLoading} onclick={start_thing}>
			{#if isLoading}
				<Spinner class="h-4 w-4" my_20={false} />
			{:else}
				{$t('words.start')}
			{/if}
		</Button>
	</div>
</div>
