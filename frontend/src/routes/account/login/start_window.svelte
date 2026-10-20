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
	<h1 class="text-xl font-semibold text-ink tracking-tight text-center">Sign in</h1>
	<p class="mt-1 text-sm text-center text-ink-muted">
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
		<div class="w-full mt-6">
			<label class="sr-only" for="email">{$t('login_page.email_or_username')}</label>
			<input
				id="email"
				bind:value={email}
				name="email"
				type="text"
				class="ledger-input min-h-11"
				placeholder={$t('login_page.email_or_username')}
				autocomplete="email"
			/>
			<div class="flex items-center justify-between gap-3 mt-4">
				<a
					href="/account/reset-password"
					class="text-sm text-ink-muted link-hover min-h-11 inline-flex items-center"
					>{$t('register_page.forgot_password?')}</a
				>

				<button
					class="btn btn-primary w-auto"
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

	<a href="/account/register" class="mx-2 text-sm text-ink link-hover">{$t('words.register')}</a>
</div>
