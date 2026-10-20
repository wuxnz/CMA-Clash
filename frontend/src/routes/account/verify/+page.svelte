<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import { onMount } from 'svelte';

	navbarVisible.visible = true;

	type Status = 'loading' | 'verified' | 'already_verified' | 'expired' | 'invalid';

	let status = $state<Status>('loading');
	const token = $derived(page.url.searchParams.get('token'));
	const errorParam = $derived(page.url.searchParams.get('error'));
	const statusParam = $derived(page.url.searchParams.get('status'));

	onMount(async () => {
		if (statusParam === 'already_verified') {
			status = 'already_verified';
			return;
		}
		if (errorParam === 'invalid') {
			status = 'invalid';
			return;
		}
		if (!token) {
			status = 'invalid';
			return;
		}
		const res = await fetch('/api/v1/users/verify-email', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ token })
		});
		const body = await res.json().catch(() => ({}));
		if (res.ok && body.status === 'verified') {
			status = 'verified';
			setTimeout(() => goto('/account/login?verified=true'), 2000);
			return;
		}
		if (res.ok && body.status === 'already_verified') {
			status = 'already_verified';
			return;
		}
		const code = body?.detail?.code;
		if (code === 'expired_token') {
			status = 'expired';
		} else {
			status = 'invalid';
		}
	});
</script>

<svelte:head>
	<title>CMA Clash: Verify email</title>
</svelte:head>

<div class="flex items-center justify-center min-h-[80vh] px-4">
	<div class="w-full max-w-md mx-auto bg-surface rounded-2xl border border-white/10 p-8 text-center">
		{#if status === 'loading'}
			<h1 class="text-xl font-display text-ink">Verifying your email…</h1>
			<p class="text-ink-muted text-sm mt-2">One moment.</p>
		{:else if status === 'verified'}
			<h1 class="text-xl font-display text-ink">Email verified</h1>
			<p class="text-ink-muted text-sm mt-2">Redirecting you to login…</p>
		{:else if status === 'already_verified'}
			<h1 class="text-xl font-display text-ink">Already verified</h1>
			<a href="/account/login" class="text-gold text-sm mt-4 inline-block hover:underline">Sign in</a>
		{:else if status === 'expired'}
			<h1 class="text-xl font-display text-ink">Link expired</h1>
			<p class="text-ink-muted text-sm mt-2">Request a new verification email from the login page.</p>
			<a href="/account/login" class="ledger-btn-primary w-auto px-8 mt-6 inline-flex">Go to login</a>
		{:else}
			<h1 class="text-xl font-display text-ink">Invalid link</h1>
			<p class="text-ink-muted text-sm mt-2">This verification link is not valid.</p>
			<a href="/account/register" class="text-gold text-sm mt-4 inline-block hover:underline">Register again</a>
		{/if}
	</div>
</div>
<Footer />
