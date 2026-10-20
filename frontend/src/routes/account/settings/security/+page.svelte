<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import { browser } from '$app/environment';
	import { startRegistration } from '@simplewebauthn/browser';
	import TotpSetup from './totp_setup.svelte';
	import BackupCodes from './backup_codes.svelte';
	import Button from '$lib/ui/Button.svelte';
	import Toggle from '$lib/ui/Toggle.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import { getLocalization } from '$lib/i18n';

	navbarVisible.visible = true;

	const { t } = getLocalization();

	let user_data: { require_password?: boolean } | undefined = $state();
	let security_keys: Array<{ id: number }> | undefined = $state();
	let totp_activated: boolean | undefined = $state();
	let totp_data = $state();
	let backup_code = $state();

	const get_data = async () => {
		const res1 = await fetch('/api/v1/users/me');
		user_data = await res1.json();
		const res2 = await fetch('/api/v1/users/webauthn/list');
		security_keys = await res2.json();
		const res3 = await fetch('/api/v1/users/2fa/totp');
		totp_activated = (await res3.json()).activated;
	};
	let data = $state(get_data());

	const save_password_required = async () => {
		console.log(user_data?.require_password, 'here');
		if (!browser || user_data?.require_password === undefined) {
			return;
		}
		const pw = require_password();
		const res = await fetch('/api/v1/users/2fa/require_password', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ require_password: user_data?.require_password, password: pw })
		});
		user_data.require_password = (await res.json()).require_password;
	};

	const require_password = (): string | null => {
		return prompt('Please enter your password to continue');
	};

	const add_security_key = async () => {
		const pw = require_password();
		if (!pw) return;
		const res1 = await fetch('/api/v1/users/webauthn/add_key_init', {
			method: 'POST',
			body: JSON.stringify({ password: pw }),
			headers: { 'Content-Type': 'application/json' }
		});
		if (res1.status === 401) {
			alert('Password probably wrong');
			return;
		}
		if (!res1.ok) {
			throw Error('Response not ok');
		}
		let attResp;
		const resp_data = await res1.json();
		// eslint-disable-next-line no-useless-catch
		try {
			resp_data.authenticatorSelection.authenticatorAttachment = 'cross-platform';
			for (let i = 0; i++; i < resp_data.excludeCredentials.length) {
				resp_data.excludeCredentials[i].transports = undefined;
			}
			attResp = await startRegistration({ optionsJSON: resp_data });
		} catch (e) {
			throw e;
		}
		await fetch('/api/v1/users/webauthn/add_key', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(attResp)
		});
		data = get_data();
	};

	const remove_security_key = async (key_id: number) => {
		const pw = require_password();
		if (!pw) return;
		const res = await fetch(`/api/v1/users/webauthn/key/${key_id}`, {
			method: 'DELETE',
			body: JSON.stringify({ password: pw }),
			headers: { 'Content-Type': 'application/json' }
		});
		if (res.status === 401) {
			alert('Password probably wrong');
			return;
		}
		data = get_data();
	};

	const disable_totp = async () => {
		const pw = require_password();
		if (!pw) return;
		const res = await fetch(`/api/v1/users/2fa/totp`, {
			method: 'DELETE',
			body: JSON.stringify({ password: pw }),
			headers: { 'Content-Type': 'application/json' }
		});
		if (res.status === 401) {
			alert('Password probably wrong');
			return;
		}
		data = get_data();
	};

	const enable_totp = async () => {
		const pw = require_password();
		if (!pw) return;
		const res = await fetch('/api/v1/users/2fa/totp', {
			method: 'POST',
			body: JSON.stringify({ password: pw }),
			headers: { 'Content-Type': 'application/json' }
		});
		if (res.status === 401) {
			alert('Password probably wrong');
			return;
		}
		data = get_data();
		totp_data = await res.json();
	};

	const get_backup_code = async () => {
		const pw = require_password();
		if (!pw) return;
		if (!confirm('If you continue, your old backup-code will be removed.')) {
			return;
		}
		const res = await fetch('/api/v1/users/2fa/backup_code', {
			method: 'POST',
			body: JSON.stringify({ password: pw }),
			headers: { 'Content-Type': 'application/json' }
		});
		if (res.status === 401) {
			alert('Password probably wrong');
			return;
		}
		backup_code = (await res.json()).code;
	};
</script>

<svelte:head>
	<title>CMA Clash: Security</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-3xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Security</h1>
		{#await data}
			<Spinner />
		{:then _}
			<div class="mt-8 divide-y divide-white/[0.07]">
				<section class="py-5">
					<h2 class="text-sm font-semibold text-ink">{$t('security_settings.backup_code')}</h2>
					<p class="text-xs text-ink-muted mt-1">Generate a one-time code you can store offline.</p>
					<Button class="w-auto mt-3" variant="secondary" onclick={get_backup_code}>
						{$t('security_settings.get_backup_code')}
					</Button>
				</section>

				<section class="py-5">
					<h2 class="text-sm font-semibold text-ink">{$t('security_settings.activate_2fa')}</h2>
					<div class="flex items-center justify-between gap-4 mt-3 min-h-11">
						<p class="text-sm text-ink-muted min-w-0">
							{user_data.require_password
								? $t('security_settings.2fa_activated')
								: $t('security_settings.2fa_deactivated')}
						</p>
						<Toggle
							bind:checked={user_data.require_password}
							disabled={!totp_activated}
							label={$t('security_settings.activate_2fa')}
							onchange={() => save_password_required()}
						/>
					</div>
				</section>

				<section class="py-5">
					<h2 class="text-sm font-semibold text-ink">{$t('security_settings.webauthn')}</h2>
					<p class="text-xs text-ink-muted mt-1">
						{#if security_keys.length > 0}
							{$t('security_settings.webauthn_available')}
						{:else}
							{$t('security_settings.webauthn_unavailable')}
						{/if}
					</p>
					<Button class="w-auto mt-3" variant="secondary" onclick={add_security_key}>
						{$t('security_settings.add_security_key')}
					</Button>
					{#if security_keys.length > 0}
						<ul class="mt-3 divide-y divide-white/[0.07]">
							{#each security_keys as key, i}
								<li class="flex items-center justify-between gap-3 py-2">
									<p class="text-sm text-ink">Key {i + 1}</p>
									<Button
										variant="ghost"
										size="sm"
										class="w-auto text-danger"
										onclick={() => remove_security_key(key.id)}
									>
										{$t('words.delete')}
									</Button>
								</li>
							{/each}
						</ul>
					{/if}
				</section>

				<section class="py-5">
					<h2 class="text-sm font-semibold text-ink">{$t('security_settings.totp')}</h2>
					<p class="text-xs text-ink-muted mt-1">
						{#if totp_activated}
							{$t('security_settings.totp_available')}
						{:else}
							{$t('security_settings.totp_unavailable')}
						{/if}
					</p>
					<div class="mt-3">
						{#if totp_activated}
							<Button variant="secondary" class="w-auto" onclick={disable_totp}>
								{$t('security_settings.disable_totp')}
							</Button>
						{:else}
							<Button class="w-auto" onclick={enable_totp}>
								{$t('security_settings.enable_totp')}
							</Button>
						{/if}
					</div>
				</section>
			</div>
		{/await}
	</div>
	<Footer />
</div>

{#if totp_data}
	<TotpSetup bind:totp_data />
{/if}

{#if backup_code}
	<BackupCodes bind:backup_code />
{/if}
