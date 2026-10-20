<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import Button from '$lib/ui/Button.svelte';

	const { t } = getLocalization();
	let {
		session_data,
		selected_method = $bindable(),
		done = $bindable(),
		step = $bindable()
	} = $props();

	let backup_code = $state('');
	let isSubmitting = $state(false);

	let backup_code_valid = $derived(backup_code.length === 64);

	const continue_in_login = async (e: Event) => {
		e.preventDefault();
		if (!backup_code_valid) {
			return;
		}
		isSubmitting = true;
		const res = await fetch(`/api/v1/login/step/1?session_id=${session_data.session_id}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ auth_type: 'BACKUP', data: backup_code })
		});
		if (res.status === 200) {
			window.location.reload();
			done = true;
		} else {
			step += 1;
			selected_method = null;
			isSubmitting = false;
		}
	};
</script>

<div class="px-6 py-6">
	<h2 class="text-xl font-semibold text-ink tracking-tight text-center">Backup code</h2>
	<p class="mt-1 text-sm text-center text-ink-muted">Paste a one-time backup code</p>

	<form onsubmit={continue_in_login} class="mt-6">
		<label class="text-sm font-medium text-ink" for="backup_code">{$t('words.backup_code')}</label>
		<input
			id="backup_code"
			bind:value={backup_code}
			name="backup_code"
			type="text"
			class="ledger-input mt-1 min-h-11 font-mono"
			placeholder={$t('words.backup_code')}
			autocomplete="off"
		/>
		<div class="flex items-center justify-end mt-4">
			<Button class="w-auto" disabled={!backup_code_valid || isSubmitting} type="submit">
				{#if isSubmitting}
					<Spinner class="h-4 w-4" my_20={false} />
				{:else}
					{$t('words.continue')}
				{/if}
			</Button>
		</div>
	</form>
</div>
