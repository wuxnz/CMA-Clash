<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';

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
		}
	};
</script>

<div class="px-6 py-4">
	<h2 class="text-3xl font-bold text-center font-display font-bold text-ink">CMA Clash</h2>

	<form onsubmit={continue_in_login}>
		<div class="w-full mt-4">
			<div class="dark:bg-gray-800 bg-white p-4 rounded-lg">
				<div class="relative bg-inherit w-full">
					<input
						id="backup_code"
						bind:value={backup_code}
						name="backup_code"
						type="text"
						class="w-full peer bg-transparent h-10 rounded-lg text-gray-700 dark:text-white placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
						placeholder={$t('words.backup_code')}
					/>
					<label
						for="backup_code"
						class="absolute cursor-text left-0 -top-3 text-sm text-gray-700 dark:text-white bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-500 peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
					>
						{$t('words.backup_code')}
					</label>
				</div>
			</div>
			<div class="flex items-center justify-between mt-4">
				<button
					onclick={() => {
						selected_method = 'BACKUP';
					}}
					class="text-sm text-gray-600 dark:text-gray-200 hover:text-gray-500"
					>{$t('login_page.use_backup_code')}</button
				>
				<button
					class="px-4 py-2 leading-5 text-white transition-colors duration-200 transform bg-gray-700 rounded-sm hover:bg-gray-600 focus:outline-hidden disabled:cursor-not-allowed disabled:opacity-50"
					disabled={!backup_code_valid}
					type="submit"
				>
					{#if isSubmitting}
						<Spinner class="h-4 w-4" my_20={false} inverse />
					{:else}
						{$t('words.continue')}
					{/if}
				</button>
			</div>
		</div>
	</form>
</div>
