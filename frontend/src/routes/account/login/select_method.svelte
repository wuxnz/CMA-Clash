<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->
<script lang="ts">
	let { session_data = {}, step, selected_method = $bindable() } = $props();

	const set_available_methods = (step_var: number): string => {
		if (step_var === 1) {
			return session_data.step_1;
		} else if (step_var === 2) {
			return session_data.step_2;
		}
	};
	let available_methods = $derived(set_available_methods(step));
</script>

<div class="px-6 py-6">
	<h2 class="text-xl font-semibold text-ink tracking-tight text-center">Choose a method</h2>
	<p class="mt-1 text-sm text-center text-ink-muted">How do you want to sign in?</p>

	<div class="mt-6 flex flex-col gap-2">
		{#if available_methods.includes('PASSKEY')}
			<button
				type="button"
				class="mode-option"
				onclick={() => {
					selected_method = 'PASSKEY';
				}}
			>
				<span class="text-sm font-medium text-ink">Security key</span>
				<span class="block text-xs text-ink-muted mt-0.5">Use a passkey or hardware key</span>
			</button>
		{/if}
		{#if available_methods.includes('PASSWORD')}
			<button
				type="button"
				class="mode-option"
				onclick={() => {
					selected_method = 'PASSWORD';
				}}
			>
				<span class="text-sm font-medium text-ink">Password</span>
				<span class="block text-xs text-ink-muted mt-0.5">Sign in with your password</span>
			</button>
		{/if}
		{#if available_methods.includes('TOTP')}
			<button
				type="button"
				class="mode-option"
				onclick={() => {
					selected_method = 'TOTP';
				}}
			>
				<span class="text-sm font-medium text-ink">Authenticator</span>
				<span class="block text-xs text-ink-muted mt-0.5">Use a one-time code from your app</span>
			</button>
		{/if}
	</div>
</div>
