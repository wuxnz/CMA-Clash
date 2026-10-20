<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { startAuthentication } from '@simplewebauthn/browser';
	import { getLocalization } from '$lib/i18n';
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

<div class="px-6 py-4">
	<h2 class="text-3xl font-bold text-center font-display font-bold text-ink">CMA Clash</h2>
	<p class="mt-1 text-center text-gray-500 dark:text-gray-400">
		Start the Security-Key verification
	</p>

	<div class="w-full mt-4">
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
				disabled={isLoading}
				onclick={start_thing}
			>
				{#if isLoading}
					<Spinner class="h-4 w-4" my_20={false} inverse />
				{:else}
					{$t('words.start')}
				{/if}
			</button>
		</div>
	</div>
</div>
