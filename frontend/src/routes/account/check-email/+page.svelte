<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';

	navbarVisible.visible = true;

	const email = $derived(page.url.searchParams.get('email') ?? '');
	let resendBusy = $state(false);
	let resendMessage = $state('');
	let cooldownUntil = $state(0);
	let cooldownLeft = $state(0);

	$effect(() => {
		if (cooldownUntil <= Date.now()) {
			cooldownLeft = 0;
			return;
		}
		const id = setInterval(() => {
			cooldownLeft = Math.max(0, Math.ceil((cooldownUntil - Date.now()) / 1000));
		}, 500);
		return () => clearInterval(id);
	});

	async function resend() {
		if (!email || resendBusy || cooldownLeft > 0) return;
		resendBusy = true;
		resendMessage = '';
		const res = await fetch('/api/v1/users/resend-verification', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ email })
		});
		resendBusy = false;
		if (res.status === 429) {
			resendMessage = 'Too many requests. Please wait a few minutes.';
			cooldownUntil = Date.now() + 60_000;
			return;
		}
		if (res.ok) {
			resendMessage = 'Verification email sent.';
			cooldownUntil = Date.now() + 60_000;
		} else {
			resendMessage = 'Could not resend email. Try again later.';
		}
	}
</script>

<svelte:head>
	<title>CMA Clash: Check your email</title>
</svelte:head>

<div class="flex items-center justify-center min-h-[80vh] px-4">
	<div class="w-full max-w-md mx-auto bg-surface rounded-2xl border border-white/10 p-8 text-center">
		<h1 class="text-xl font-semibold text-ink tracking-tight">Check your inbox</h1>
		<p class="text-ink-muted mt-3 text-sm leading-relaxed">
			We sent a verification link to
			{#if email}<span class="text-ink font-medium">{email}</span>{:else}your email address{/if}. Open it to
			activate your account.
		</p>
		<p class="text-ink-muted text-xs mt-4">The link expires in 48 hours.</p>
		<button
			type="button"
			class="btn btn-primary w-auto mt-8"
			disabled={resendBusy || cooldownLeft > 0 || !email}
			onclick={resend}
		>
			{#if resendBusy}
				Sending…
			{:else if cooldownLeft > 0}
				Resend in {cooldownLeft}s
			{:else}
				Resend email
			{/if}
		</button>
		{#if resendMessage}
			<p class="text-sm text-ink-muted mt-3">{resendMessage}</p>
		{/if}
		<a href={resolve('/account/login')} class="inline-flex items-center min-h-11 mt-6 text-sm text-ink link-hover">Back to login</a>
	</div>
</div>
<Footer />
