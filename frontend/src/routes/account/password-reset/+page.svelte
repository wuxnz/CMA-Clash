<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';

	const { t } = getLocalization();
	let { data } = $props();
	let { token: string } = data;
	let isSubmitting = $state(false);
	interface PasswordData {
		password1: string;
		password2: string;
	}
	let passwordData: PasswordData = $state({
		password1: '',
		password2: ''
	});
	let passwordsValid = $derived(
		passwordData.password1 === passwordData.password2 && passwordData.password1.length >= 8
	);

	const submit = async (e: Event) => {
		e.preventDefault();
		if (!passwordsValid) {
			return;
		}
		isSubmitting = true;
		const response = await fetch('/api/v1/users/reset-password', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				password: passwordData.password1,
				token
			})
		});
		const data = await response.json();
		if (response.status === 200) {
			window.location.assign('/account/login');
		} else {
			alert(data.detail);
		}
		isSubmitting = false;
	};
</script>

<svelte:head>
	<title>CMA Clash - Reset your Password</title>
</svelte:head>

<div class="flex items-center justify-center h-full px-4">
	<div>
		<div
			class="w-full max-w-sm mx-auto overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800"
		>
			<div class="px-6 py-4">
				<h2 class="text-3xl font-bold text-center text-gray-700 dark:text-white">
					CMA Clash
				</h2>

				<!--
								<h3 class='mt-1 text-xl font-medium text-center text-gray-600 dark:text-gray-200'>
								</h3>
				-->

				<p class="mt-1 text-center text-gray-500 dark:text-gray-400">
					{$t('password_reset_page.reset_password')}
				</p>

				<form onsubmit={submit}>
					<div class="w-full mt-4">
						<div class="dark:bg-gray-800 bg-white p-4 rounded-lg">
							<div class="relative bg-inherit w-full">
								<input
									id="password1"
									bind:value={passwordData.password1}
									name="password1"
									type="password"
									class="w-full peer bg-transparent h-10 rounded-lg text-gray-700 dark:text-white placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
									placeholder={$t('words.password')}
								/>
								<label
									for="password1"
									class="absolute cursor-text left-0 -top-3 text-sm text-gray-700 dark:text-white bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-500 peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
								>
									{$t('words.password')}
								</label>
							</div>
						</div>
						<div class="dark:bg-gray-800 bg-white p-4 rounded-lg">
							<div class="relative bg-inherit w-full">
								<input
									id="password2"
									name="password2"
									type="password"
									bind:value={passwordData.password2}
									class="w-full peer bg-transparent h-10 rounded-lg text-gray-700 dark:text-white placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
									placeholder={$t('words.repeat_password')}
								/>
								<label
									for="password2"
									class="absolute cursor-text left-0 -top-3 text-sm text-gray-500 bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-500 peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
								>
									{$t('words.repeat_password')}
								</label>
							</div>
						</div>

						<div class="flex items-center justify-between mt-4">
							<a
								href="/account/login"
								class="text-sm text-gray-600 dark:text-gray-200 hover:text-gray-500"
								>{$t('register_page.already_have_account?')}</a
							>

							<button
								class="px-4 py-2 leading-5 text-white transition-colors duration-200 transform bg-gray-700 rounded-sm hover:bg-gray-600 focus:outline-hidden disabled:cursor-not-allowed disabled:opacity-50"
								disabled={!passwordsValid}
								type="submit"
							>
								{#if isSubmitting}
									<Spinner class="h-4 w-4" my_20={false} inverse />
								{:else}
									{$t('words.submit')}
								{/if}
							</button>
						</div>
					</div>
				</form>
			</div>

			<div
				class="flex items-center justify-center py-4 text-center bg-gray-50 dark:bg-gray-700"
			>
				<span class="text-sm text-gray-600 dark:text-gray-200"
					>{$t('login_page.already_have_account')}
				</span>

				<a
					href="/account/register"
					class="mx-2 text-sm font-bold text-blue-500 dark:text-blue-400 hover:underline"
					>{$t('words.register')}</a
				>
			</div>
		</div>
	</div>
</div>
