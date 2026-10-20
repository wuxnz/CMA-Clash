<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { socket } from '$lib/socket';
	import { onDestroy, onMount } from 'svelte';
	import { browser } from '$app/environment';
	import * as Sentry from '@sentry/browser';
	import { getLocalization } from '$lib/i18n';
	import Cookies from 'js-cookie';
	import { hcaptcha_site_key, recaptcha_key, sentry_dsn } from '$lib/config';

	const { t } = getLocalization();

	interface Props {
		game_pin: string;
		game_mode: any;
		username: any;
	}

	let {
		game_pin = $bindable(),
		game_mode = $bindable(),
		username = $bindable()
	}: Props = $props();
	let custom_field = $state();
	let custom_field_value = $state();
	let captcha_enabled = $state();

	let hcaptchaSitekey = hcaptcha_site_key;

	let hcaptcha = {
		execute: async (_a, _b) => ({ response: '' }),
		render: (_a, _b) => {}
	};
	let hcaptchaWidgetID;

	onMount(() => {
		if (browser) {
			prefetch_username();
			hcaptcha = window.hcaptcha;
			if (hcaptcha.render) {
				hcaptchaWidgetID = hcaptcha.render('hcaptcha', {
					sitekey: hcaptchaSitekey,
					size: 'invisible',
					theme: 'dark'
				});
			}
		}
	});

	onDestroy(() => {
		if (browser) {
			hcaptcha = {
				execute: async () => ({ response: '' }),
				render: () => {}
			};
		}
	});

	const prefetch_username = async () => {
		try {
			const res = await fetch('/api/v1/users/me');
			if (res.status !== 200) return;
			const json = await res.json();
			username = json.username;
		} catch {
			/* guest join */
		}
	};

	const set_game_pin = async () => {
		try {
			const res = await fetch(`/api/v1/quiz/play/check_captcha/${game_pin}`);
			const json = await res.json().catch(() => ({}));
			game_mode = json.game_mode;
			if (res.status === 200) {
				captcha_enabled = json.enabled;
				custom_field = json.custom_field;
			}
			if (res.status === 404) {
				if (browser) alert('Game not found');
				game_pin = '';
				return;
			}
		} catch {
			captcha_enabled = false;
		}
	};

	$effect(() => {
		if (game_pin.length > 5) set_game_pin();
	});

	const setUsername = async (e: Event) => {
		e.preventDefault();
		if (username.length <= 3) return;
		if (Cookies.get('kicked')) return;
		let captcha_resp: string;
		if (captcha_enabled) {
			if (hcaptchaSitekey) {
				try {
					const { response } = await hcaptcha.execute(hcaptchaWidgetID, { async: true });
					captcha_resp = response;
					socket.emit('join_game', {
						username,
						game_pin,
						captcha: captcha_resp,
						custom_field: custom_field ? custom_field_value : undefined
					});
				} catch (err) {
					if (sentry_dsn !== null) Sentry.captureException(err);
					alert('Captcha failed!');
					window.location.reload();
				}
			} else if (recaptcha_key) {
				grecaptcha.ready(() => {
					grecaptcha.execute(recaptcha_key, { action: 'submit' }).then(function (token) {
						socket.emit('join_game', {
							username,
							game_pin,
							captcha: token,
							custom_field: custom_field ? custom_field_value : undefined
						});
					});
				});
			}
		} else {
			socket.emit('join_game', {
				username,
				game_pin,
				captcha: undefined,
				custom_field: custom_field ? custom_field_value : undefined
			});
		}
	};
	socket.on('game_not_found', () => {
		game_pin = '';
		if (browser) alert('Game not found');
	});
	$effect(() => {
		const cleaned = game_pin.replace(/\D/g, '');
		if (game_pin.replace(/\D/g, '') === game_pin) return;
		game_pin = cleaned;
	});
</script>

<svelte:head>
	{#if captcha_enabled && hcaptchaSitekey}
		<script src="https://js.hcaptcha.com/1/api.js" async defer></script>
	{/if}
	{#if recaptcha_key && captcha_enabled}
		<script src="https://www.google.com/recaptcha/api.js?render={recaptcha_key}"></script>
	{/if}
</svelte:head>

<div class="min-h-screen bg-paper flex flex-col items-center justify-center p-4">
	<p class="font-display text-gold text-sm tracking-[0.35em] mb-4">Arena</p>
	{#if game_pin === '' || game_pin.length < 6}
		<h1 class="font-display text-6xl sm:text-8xl text-ink mb-3">Join</h1>
		<p class="text-ink-muted mb-4 text-center">Enter the 6-digit PIN from the host screen</p>
		<p class="text-ink-muted mb-8 text-center text-sm">
			Hosting?
			<a href="/host" class="link-hover text-ink">Start a Clash</a>
		</p>
		<input
			class="ledger-input text-center font-display text-4xl tracking-[0.4em] max-w-sm"
			bind:value={game_pin}
			maxlength="6"
			inputmode="numeric"
			autocomplete="one-time-code"
			aria-label={$t('words.game_pin')}
		/>
	{:else}
		<p class="font-display text-5xl text-gold tabular-nums tracking-widest mb-6">{game_pin}</p>
		<form onsubmit={setUsername} class="flex flex-col gap-4 w-full max-w-sm">
			<input
				class="ledger-input text-center font-display text-2xl"
				bind:value={username}
				maxlength="17"
				placeholder={$t('words.username')}
				autocomplete="nickname"
			/>
			{#if custom_field}
				<input class="ledger-input text-center" bind:value={custom_field_value} placeholder={custom_field} />
			{/if}
			<button
				type="submit"
				class="btn btn-primary w-full"
				disabled={username.length <= 3}>{$t('words.submit')}</button
			>
		</form>
	{/if}
</div>
<div
	id="hcaptcha"
	class="h-captcha"
	data-sitekey={hcaptchaSitekey}
	data-size="invisible"
	data-theme="dark"
></div>
