<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import OAuthBlock from './oauth_block.svelte';

	let { session_data = $bindable({}), step = $bindable() } = $props();

	const { t } = getLocalization();
	let email = $state('');
	let emailEmpty = $derived(email === '');
	let isSubmitting = $state(false);

	const start_login = async (e: Event): Promise<void> => {
		e.preventDefault();
		if (emailEmpty) {
			return;
		}
		isSubmitting = true;

		const res = await fetch('/api/v1/login/start', {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ email: email })
		});
		session_data = await res.json();
		step = 1;
	};
</script>

<div class="px-6 py-4">
	<h2 class="text-3xl font-bold text-center font-display font-bold text-ink">CMA Clash</h2>

	<h3 class="mt-1 text-xl font-medium text-center text-gray-600 dark:text-gray-200">
		{$t('login_page.welcome_back')}
	</h3>

	<p class="mt-1 text-center text-gray-500 dark:text-gray-400">
		{$t('login_page.login_or_create_account')}
	</p>

	<form onsubmit={start_login}>
		<div class="w-full mt-4">
			<div class="dark:bg-gray-800 bg-white p-4 rounded-lg">
				<div class="relative bg-inherit w-full">
					<input
						id="email"
						bind:value={email}
						name="email"
						type="text"
						class="w-full peer bg-transparent h-10 rounded-lg text-gray-700 dark:text-white placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
						placeholder={$t('login_page.email_or_username')}
						autocomplete="email"
					/>
					<label
						for="email"
						class="absolute cursor-text left-0 -top-3 text-sm text-gray-700 dark:text-white bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-500 peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
					>
						{$t('login_page.email_or_username')}
					</label>
				</div>
			</div>
			<div class="flex items-center justify-between mt-4">
				<a
					href="/account/reset-password"
					class="text-sm text-gray-600 dark:text-gray-200 hover:text-gray-500"
					>{$t('register_page.forgot_password?')}</a
				>

				<button
					class="px-4 py-2 leading-5 text-white transition-colors duration-200 transform bg-gray-700 rounded-sm hover:bg-gray-600 focus:outline-hidden disabled:cursor-not-allowed disabled:opacity-50"
					disabled={emailEmpty}
					type="submit"
				>
					{#if isSubmitting}
						<Spinner class="h-4 w-4" my_20={false} inverse />
					{:else}
						{$t('words.continue')}
					{/if}
				</button>
			</div>
			<OAuthBlock />
		</div>
	</form>
</div>

<div class="flex items-center justify-center py-4 text-center bg-gray-50 dark:bg-gray-700">
	<span class="text-sm text-gray-600 dark:text-gray-200"
		>{$t('login_page.already_have_account')}
	</span>

	<a
		href="/account/register"
		class="mx-2 text-sm font-bold text-blue-500 dark:text-blue-400 hover:underline"
		>{$t('words.register')}</a
	>
</div>
