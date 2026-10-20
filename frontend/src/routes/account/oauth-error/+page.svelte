<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Button from '$lib/ui/Button.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';

	navbarVisible.visible = true;
	let { data } = $props();
	const { error } = data;
</script>

<svelte:head>
	<title>CMA Clash: Sign-in error</title>
</svelte:head>

<div class="min-h-[80vh] flex flex-col items-center justify-center px-4 text-center">
	<h1 class="text-xl font-semibold text-ink tracking-tight">Could not sign in</h1>
	<p class="mt-3 max-w-md text-sm text-ink-muted leading-relaxed">
		{#if error === 'email'}
			GitHub didn't return an email address. Confirm your GitHub email is verified, then try again.
		{:else}
			There was a problem authenticating you. Check that your email is verified, then try again.
		{/if}
	</p>
	<div class="mt-8">
		<Button href="/account/login" class="w-auto">Back to login</Button>
	</div>
	<p class="mt-6 text-sm text-ink-muted">
		If this keeps happening, open an
		<a
			href="https://github.com/wuxnz/CMA-Clash/issues/new?assignees=&labels=&template=Bug_report.md"
			class="text-ink link-hover"
		>
			issue on GitHub
		</a>.
	</p>
</div>
<Footer />
