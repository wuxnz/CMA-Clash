<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { resolve } from '$app/paths';
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import Button from '$lib/ui/Button.svelte';
	import Footer from '$lib/footer.svelte';

	navbarVisible.visible = true;

	const { t } = getLocalization();

	let isSubmitting = $state(false);
	let message = $state('');

	const submit = async (e: Event) => {
		e.preventDefault();
		isSubmitting = true;
		message = '';
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
			message = 'Email was sent. Check your inbox.';
			isSubmitting = false;
			return;
		} else if (res.status === 404) {
			message = 'No account found for that email.';
		} else {
			message = 'Could not send a reset email.';
		}
		isSubmitting = false;
	};

	let email = $state('');
</script>

<svelte:head>
	<title>CMA Clash: Reset your password</title>
</svelte:head>

<div class="flex items-center justify-center min-h-[80vh] px-4">
	<div
		class="w-full max-w-sm mx-auto overflow-hidden bg-surface rounded-2xl border border-white/10 shadow-[var(--shadow-card)]"
	>
		<div class="px-6 py-6">
			<h1 class="text-xl font-semibold text-ink tracking-tight text-center">Reset password</h1>
			<p class="mt-1 text-sm text-center text-ink-muted">
				{$t('password_reset_page.reset_password')}
			</p>

			<form onsubmit={submit} class="mt-6 space-y-4">
				<div>
					<label class="text-sm font-medium text-ink" for="email">{$t('words.email')}</label>
					<input
						id="email"
						bind:value={email}
						name="email"
						type="email"
						class="ledger-input mt-1 min-h-11"
						placeholder={$t('words.email')}
						autocomplete="email"
					/>
				</div>
				{#if message}
					<p class="text-sm text-ink-muted">{message}</p>
				{/if}
				<div class="flex items-center justify-between gap-3">
					<a href={resolve('/account/login')} class="text-sm text-ink-muted link-hover min-h-11 inline-flex items-center">
						{$t('words.login')}
					</a>
					<Button class="w-auto" disabled={email === '' || isSubmitting} type="submit">
						{#if isSubmitting}
							<Spinner class="h-4 w-4" my_20={false} />
						{:else}
							{$t('words.submit')}
						{/if}
					</Button>
				</div>
			</form>
		</div>
		<div class="flex items-center justify-center py-4 text-center bg-paper-muted">
			<span class="text-sm text-ink-muted">{$t('login_page.already_have_account')}</span>
			<a href={resolve('/account/register')} class="mx-2 text-sm text-ink link-hover">{$t('words.register')}</a>
		</div>
	</div>
</div>
<Footer />
