<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import { navbarVisible } from '$lib/stores.svelte.ts';

	navbarVisible.visible = true;

	const { t } = getLocalization();

	let isSubmitting = $state(false);

	const submit = async (e: Event) => {
		e.preventDefault();
		isSubmitting = true;
		const res = await fetch('/api/v1/users/forgot-password', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email: email
			})
		});
		if (res.status === 200) {
			alert('Email was sent! Please check your inbox.');
			return;
		} else if (res.status === 404) {
			alert('user not found!');
		}
		isSubmitting = false;
	};

	let email = $state('');
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
									id="email"
									bind:value={email}
									name="email"
									type="email"
									class="w-full peer bg-transparent h-10 rounded-lg text-gray-700 dark:text-white placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
									placeholder={$t('words.email')}
								/>
								<label
									for="email"
									class="absolute cursor-text left-0 -top-3 text-sm text-gray-700 dark:text-white bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-500 peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
								>
									{$t('words.email')}
								</label>
							</div>
						</div>

						<div class="flex items-center justify-between mt-4 gap-2">
							<a
								href="/account/login"
								class="text-sm text-gray-600 dark:text-gray-200 hover:text-gray-500"
								>{$t('register_page.already_have_account?')}</a
							>

							<button
								class="px-4 py-2 leading-5 text-white transition-colors duration-200 transform bg-gray-700 rounded-sm hover:bg-gray-600 focus:outline-hidden disabled:cursor-not-allowed disabled:opacity-50"
								disabled={email === ''}
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
