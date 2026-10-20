<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import Button from '$lib/ui/Button.svelte';

	interface Props {
		session_data: any;
		selected_method: any;
		done: any;
		step: any;
	}

	let {
		session_data,
		selected_method = $bindable(),
		done = $bindable(),
		step = $bindable()
	}: Props = $props();

	const { t } = getLocalization();
	let isSubmitting = $state(false);
	let totp = $state('');

	let totp_valid = $derived(totp.length === 6);

	const continue_in_login = async (e: Event) => {
		e.preventDefault();
		if (!totp_valid) {
			return;
		}
		isSubmitting = true;
		const res = await fetch(
			`/api/v1/login/step/${step}?session_id=${session_data.session_id}`,
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ auth_type: 'TOTP', data: totp })
			}
		);
		if (res.status === 200) {
			window.location.reload();
			done = true;
		} else if (res.status === 202) {
			step += 1;
			selected_method = null;
			isSubmitting = false;
		} else if (res.status === 401) {
			isSubmitting = false;
			let data;
			try {
				data = await res.json();
			} catch {
				alert('Unknown error');
				window.location.reload();
			}
			if (data.detail === 'totp wrong') {
				alert('TOTP code was incorrect');
				totp = '';
			}
		} else {
			isSubmitting = false;
		}
	};
</script>

<div class="px-6 py-6">
	<h2 class="text-xl font-semibold text-ink tracking-tight text-center">Authenticator code</h2>
	<p class="mt-1 text-sm text-center text-ink-muted">Enter the 6-digit code from your app</p>

	<form onsubmit={continue_in_login} class="mt-6">
		<label class="text-sm font-medium text-ink" for="totp">{$t('words.totp')}</label>
		<input
			id="totp"
			bind:value={totp}
			name="totp"
			type="text"
			inputmode="numeric"
			class="ledger-input mt-1 min-h-11"
			placeholder={$t('words.totp')}
			autocomplete="one-time-code"
		/>
		<div class="flex items-center justify-between gap-3 mt-4">
			<button
				type="button"
				onclick={() => {
					selected_method = 'BACKUP';
				}}
				class="text-sm text-ink-muted link-hover min-h-11"
			>
				{$t('login_page.use_backup_code')}
			</button>
			<Button class="w-auto" disabled={!totp_valid || isSubmitting} type="submit">
				{#if isSubmitting}
					<Spinner class="h-4 w-4" my_20={false} />
				{:else}
					{$t('words.continue')}
				{/if}
			</Button>
		</div>
	</form>
</div>
