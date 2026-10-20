<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';

	let {
		session_data,
		selected_method = $bindable(),
		done = $bindable(),
		step = $bindable()
	} = $props();

	const { t } = getLocalization();
	let isSubmitting;
	let password = $state();

	const continue_in_login = async (e: Event) => {
		e.preventDefault();
		if (!password) {
			return;
		}
		const res = await fetch(`/api/v1/login/step/1?session_id=${session_data.session_id}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ auth_type: 'PASSWORD', data: password })
		});
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
				alert("This shouldn't happen");
				window.location.reload();
			}
			if (data.detail === 'wrong credentials') {
				/*				alertModal.set({
					open: true,
					body: 'Please try again. Your email and or password were incorrect.',
					title: 'Wrong Credentials'
				});*/
				alert('Wrong credentials');
			}
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
						id="password"
						bind:value={password}
						name="password"
						type="password"
						class="w-full peer bg-transparent h-10 rounded-lg text-gray-700 dark:text-white placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
						placeholder={$t('words.password')}
						autocomplete="current-password"
					/>
					<label
						for="password"
						class="absolute cursor-text left-0 -top-3 text-sm text-gray-700 dark:text-white bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-500 peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
					>
						{$t('words.password')}
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
					disabled={!password}
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
