<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { getLocalization } from '$lib/i18n';
	import Button from '$lib/ui/Button.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';

	navbarVisible.visible = true;
	const { t } = getLocalization();
	let { data } = $props();
	const token = data.token;
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
		const payload = await response.json();
		if (response.status === 200) {
			window.location.assign('/account/login');
		} else {
			alert(payload.detail);
		}
		isSubmitting = false;
	};
</script>

<svelte:head>
	<title>CMA Clash: Reset your password</title>
</svelte:head>

<div class="flex items-center justify-center min-h-[80vh] px-4">
	<div
		class="w-full max-w-sm mx-auto overflow-hidden bg-surface rounded-2xl border border-white/10 shadow-[var(--shadow-card)]"
	>
		<div class="px-6 py-6">
			<h1 class="text-xl font-semibold text-ink tracking-tight text-center">Set a new password</h1>
			<p class="mt-1 text-sm text-center text-ink-muted">
				{$t('password_reset_page.reset_password')}
			</p>

			<form onsubmit={submit} class="mt-6 space-y-4">
				<div>
					<label class="text-sm font-medium text-ink" for="password1">{$t('words.password')}</label>
					<input
						id="password1"
						bind:value={passwordData.password1}
						name="password1"
						type="password"
						class="ledger-input mt-1 min-h-11"
						placeholder={$t('words.password')}
						autocomplete="new-password"
					/>
				</div>
				<div>
					<label class="text-sm font-medium text-ink" for="password2">{$t('words.repeat_password')}</label>
					<input
						id="password2"
						name="password2"
						type="password"
						bind:value={passwordData.password2}
						class="ledger-input mt-1 min-h-11"
						placeholder={$t('words.repeat_password')}
						autocomplete="new-password"
					/>
				</div>
				<div class="flex items-center justify-between gap-3">
					<a href="/account/login" class="text-sm text-ink-muted link-hover min-h-11 inline-flex items-center">
						{$t('words.login')}
					</a>
					<Button class="w-auto" disabled={!passwordsValid || isSubmitting} type="submit">
						{#if isSubmitting}
							<Spinner class="h-4 w-4" my_20={false} />
						{:else}
							{$t('words.submit')}
						{/if}
					</Button>
				</div>
			</form>
		</div>
	</div>
</div>
<Footer />
