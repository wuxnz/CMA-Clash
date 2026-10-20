<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { DateTime } from 'luxon';
	import { UAParser } from 'ua-parser-js';
	import Spinner from '$lib/Spinner.svelte';
	import { onMount } from 'svelte';
	import Button from '$lib/ui/Button.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';

	navbarVisible.visible = true;
	const { t } = getLocalization();

	interface UserAccount {
		id: string;
		email: string;
		username: string;
		verified: boolean;
		created_at: string;
	}

	interface ChangePasswordData {
		oldPassword: string;
		newPassword: string;
		newPasswordConfirm: string;
	}

	let changePasswordData: ChangePasswordData = $state({
		oldPassword: '',
		newPassword: '',
		newPasswordConfirm: ''
	});

	let this_session = $state();

	let passwordChangeDataValid = $derived(
		changePasswordData.newPassword === changePasswordData.newPasswordConfirm &&
			changePasswordData.newPassword.length >= 8 &&
			changePasswordData.oldPassword !== changePasswordData.newPassword &&
			changePasswordData.oldPassword !== ''
	);

	const changePassword = async (e: Event) => {
		e.preventDefault();
		if (!passwordChangeDataValid) {
			return;
		}
		const res = await fetch('/api/v1/users/password/update', {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				old_password: changePasswordData.oldPassword,
				new_password: changePasswordData.newPassword
			})
		});
		if (res.status === 200) {
			alert('Password changed');
			window.location.assign('/account/login');
		} else {
			alert('Password change failed');
		}
	};

	const getUser = async (): Promise<UserAccount> => {
		const response = await fetch('/api/v1/users/me', {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		});
		if (response.status === 200) {
			return await response.json();
		} else {
			window.location.assign('/account/login');
		}
	};

	onMount(() => {
		api_keys = get_api_keys();
	});

	const get_api_keys = async (): Promise<Array<string>> => {
		const res = await fetch('/api/v1/users/api_keys');
		const api_keys_temp = await res.json();
		return api_keys_temp;
	};

	let api_keys = $state();

	const add_api_key = async () => {
		await fetch('/api/v1/users/api_keys', { method: 'POST' });
		api_keys = get_api_keys();
	};
	const formatDate = (date: string): string => {
		const dt = DateTime.fromISO(date);
		return dt.toLocaleString(DateTime.DATETIME_MED);
	};

	const delete_api_key = async (key: string) => {
		if (confirm('Delete this API key?')) {
			await fetch(`/api/v1/users/api_keys?api_key=${key}`, { method: 'DELETE' });
			api_keys = get_api_keys();
		}
	};

	const getSessions = async () => {
		const res = await fetch('/api/v1/users/sessions/list');
		if (res.status === 200) {
			const res2 = await fetch('/api/v1/users/session');
			if (res2.status === 200) {
				this_session = await res2.json();
			}
			return await res.json();
		} else {
			window.location.assign('/account/login?returnTo=/account/settings');
		}
		return await res.json();
	};

	const getFormattedUserAgent = (userAgent: string): string => {
		const parser = new UAParser(userAgent);
		const result = parser.getResult();
		return `${result.browser.name} ${result.browser.version} (${result.os.name})`;
	};

	const deleteSession = async (session_id: string) => {
		const res = await fetch(`/api/v1/users/sessions/${session_id}`, {
			method: 'DELETE'
		});
		if (res.status === 200) {
			window.location.reload();
		}
	};
</script>

<svelte:head>
	<title>CMA Clash: Settings</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-3xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Settings</h1>

		{#await getUser()}
			<Spinner />
		{:then user}
			<div class="mt-8 flex flex-col sm:flex-row gap-6 min-w-0">
				<div class="shrink-0">
					<img
						class="rounded-lg w-24 h-24 object-cover bg-elevated"
						src="/api/v1/users/avatar"
						alt=""
					/>
					<Button href="/account/settings/avatar" variant="ghost" size="sm" class="w-auto mt-3">
						Change avatar
					</Button>
				</div>
				<div class="min-w-0">
					<p class="text-lg font-semibold text-ink truncate">{user.username}</p>
					<p class="text-sm text-ink-muted mt-1 break-all">{user.email}</p>
					<nav class="mt-4 flex flex-wrap items-center gap-x-4 gap-y-1 text-sm" aria-label="Account">
						<a href="/account/settings/security" class="min-h-11 inline-flex items-center text-ink-muted link-hover">
							Security
						</a>
						<a href="/account/controllers" class="min-h-11 inline-flex items-center text-ink-muted link-hover">
							Quiz controllers
						</a>
						<a href="/user/{user.id}" class="min-h-11 inline-flex items-center text-ink-muted link-hover">
							Public profile
						</a>
					</nav>
				</div>
			</div>

			<form class="mt-10 space-y-4 max-w-md" onsubmit={changePassword}>
				<h2 class="text-sm font-semibold text-ink">Change password</h2>
				<div>
					<label class="text-sm font-medium text-ink" for="old-password">{$t('settings_page.old_password')}</label>
					<input
						id="old-password"
						type="password"
						class="ledger-input mt-1 min-h-11"
						autocomplete="current-password"
						bind:value={changePasswordData.oldPassword}
					/>
				</div>
				<div>
					<label class="text-sm font-medium text-ink" for="new-password">{$t('settings_page.new_password')}</label>
					<input
						id="new-password"
						type="password"
						class="ledger-input mt-1 min-h-11"
						autocomplete="new-password"
						bind:value={changePasswordData.newPassword}
					/>
				</div>
				<div>
					<label class="text-sm font-medium text-ink" for="repeat-password">{$t('settings_page.repeat_password')}</label>
					<input
						id="repeat-password"
						type="password"
						class="ledger-input mt-1 min-h-11"
						autocomplete="new-password"
						bind:value={changePasswordData.newPasswordConfirm}
					/>
				</div>
				<Button type="submit" disabled={!passwordChangeDataValid} class="w-full sm:w-auto">
					Change password
				</Button>
			</form>

			<div class="mt-10">
				<h2 class="text-sm font-semibold text-ink">API keys</h2>
				<Button variant="secondary" class="w-auto mt-3" onclick={add_api_key}>
					{$t('settings_page.add_api_key')}
				</Button>
				{#await api_keys}
					<Spinner my_20={false} />
				{:then keys}
					<ul class="mt-4 divide-y divide-white/[0.07]">
						{#each keys as key}
							<li class="flex items-center justify-between gap-3 py-3 min-w-0">
								<code class="text-xs text-ink-muted truncate font-mono">{key.key}</code>
								<Button
									variant="ghost"
									size="sm"
									class="w-auto text-danger"
									onclick={() => delete_api_key(key.key)}
								>
									{$t('words.delete')}
								</Button>
							</li>
						{/each}
					</ul>
				{/await}
			</div>
		{/await}

		<div class="mt-10">
			<h2 class="text-sm font-semibold text-ink mb-3">Sessions</h2>
			{#await getSessions()}
				<Spinner my_20={false} />
			{:then sessions}
				<ul class="divide-y divide-white/[0.07]">
					{#each sessions as session}
						<li class="py-3 flex flex-col sm:flex-row sm:items-center gap-2 min-w-0">
							<div class="min-w-0 flex-1">
								<p class="text-sm text-ink truncate">{getFormattedUserAgent(session.user_agent)}</p>
								<p class="text-xs text-ink-muted mt-0.5">
									{formatDate(session.created_at)}
									<span> · last seen {formatDate(session.last_seen)}</span>
									{#if session.id === this_session?.id}
										<span> · this session</span>
									{/if}
								</p>
							</div>
							{#if session.id !== this_session?.id}
								<Button
									variant="ghost"
									size="sm"
									class="w-auto"
									onclick={() => deleteSession(session.id)}
								>
									{$t('words.delete')}
								</Button>
							{/if}
						</li>
					{/each}
				</ul>
			{/await}
		</div>
	</div>
	<Footer />
</div>
