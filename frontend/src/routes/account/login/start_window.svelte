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
	let unverifiedEmail = $state('');
	let unverifiedMessage = $state('');
	let resendBusy = $state(false);

	const start_login = async (e: Event): Promise<void> => {
		e.preventDefault();
		if (emailEmpty) {
			return;
		}
		isSubmitting = true;

		unverifiedMessage = '';
		const res = await fetch('/api/v1/login/start', {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ email: email })
		});
		if (res.status === 403) {
			const body = await res.json().catch(() => ({}));
			if (body?.detail?.code === 'email_not_verified') {
				unverifiedEmail = body.detail.email ?? email;
				unverifiedMessage = 'Verify your email before signing in.';
				isSubmitting = false;
				return;
			}
		}
		if (!res.ok) {
			isSubmitting = false;
			return;
		}
		session_data = await res.json();
		step = 1;
		isSubmitting = false;
	};

	const resendVerification = async () => {
		if (!unverifiedEmail || resendBusy) return;
		resendBusy = true;
		const res = await fetch('/api/v1/users/resend-verification', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ email: unverifiedEmail })
		});
		resendBusy = false;
		unverifiedMessage = res.ok
			? 'Verification email sent. Check your inbox.'
			: 'Could not resend verification email.';
	};
</script>

<div class="px-6 py-6">
	<p class="font-display text-gold text-xs tracking-[0.35em] text-center mb-2">Arena</p>
	<h2 class="text-4xl text-center font-display text-ink">CMA Clash</h2>

	<h3 class="mt-1 text-lg font-medium text-center text-ink-muted">
		{$t('login_page.welcome_back')}
	</h3>

	<p class="mt-1 text-center text-ink-muted">
		{$t('login_page.login_or_create_account')}
	</p>

	{#if unverifiedMessage}
		<div class="mt-4 p-3 rounded-lg bg-surface border border-gold/30 text-sm text-ink-muted">
			<p>{unverifiedMessage}</p>
			{#if unverifiedEmail}
				<button
					type="button"
					class="text-gold mt-2 hover:underline"
					disabled={resendBusy}
					onclick={resendVerification}
				>
					{resendBusy ? 'Sending…' : 'Resend verification email'}
				</button>
			{/if}
		</div>
	{/if}

	<form onsubmit={start_login}>
		<div class="w-full mt-4">
			<div class="bg-surface p-4 rounded-lg">
				<div class="relative bg-inherit w-full">
					<input
						id="email"
						bind:value={email}
						name="email"
						type="text"
						class="w-full peer bg-transparent h-10 rounded-lg text-ink placeholder-transparent ring-2 px-2 ring-ink/30 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
						placeholder={$t('login_page.email_or_username')}
						autocomplete="email"
					/>
					<label
						for="email"
						class="absolute cursor-text left-0 -top-3 text-sm text-ink bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-ink-muted peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
					>
						{$t('login_page.email_or_username')}
					</label>
				</div>
			</div>
			<div class="flex items-center justify-between mt-4">
				<a
					href="/account/reset-password"
					class="text-sm text-ink-muted hover:text-ink-muted"
					>{$t('register_page.forgot_password?')}</a
				>

				<button
					class="ledger-btn-primary w-auto px-6"
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

<div class="flex items-center justify-center py-4 text-center bg-paper-muted">
	<span class="text-sm text-ink-muted"
		>{$t('login_page.already_have_account')}
	</span>

	<a
		href="/account/register"
		class="mx-2 text-sm font-bold text-primary hover:underline"
		>{$t('words.register')}</a
	>
</div>
