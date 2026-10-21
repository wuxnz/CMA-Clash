<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { socket } from '$lib/socket';
	import { onDestroy, onMount } from 'svelte';
	import { browser } from '$app/environment';
	import { getBattlePlayUsername } from '$lib/cma/battle-guest';
	import { joinErrorMessage } from '$lib/play/join-errors';
	import { normalizeGameMode } from '$lib/play/live-game';
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
	let joinError = $state('');
	let joining = $state(false);
	let socketConnected = $state(false);
	let battleAutoJoinStarted = $state(false);

	const onJoinError = (payload?: { code?: string }) => {
		joining = false;
		joinError = joinErrorMessage(payload?.code);
	};

	const onSocketConnect = () => {
		socketConnected = true;
	};
	const onSocketDisconnect = () => {
		socketConnected = false;
	};
	const onGameNotFound = () => {
		joining = false;
		joinError = 'Game not found. Check the PIN with your host.';
	};
	const onUsernameAlreadyExists = () => {
		onJoinError({ code: 'username_taken' });
	};
	const onJoinedGameJoinUi = () => {
		joining = false;
		joinError = '';
	};

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
		socket.on('connect', onSocketConnect);
		socket.on('disconnect', onSocketDisconnect);
		socket.on('join_error', onJoinError);
		socket.on('game_not_found', onGameNotFound);
		socket.on('username_already_exists', onUsernameAlreadyExists);
		socket.on('joined_game', onJoinedGameJoinUi);
		if (socket.connected) {
			socketConnected = true;
		}
	});

	onDestroy(() => {
		if (browser) {
			hcaptcha = {
				execute: async () => ({ response: '' }),
				render: () => {}
			};
			socket.off('connect', onSocketConnect);
			socket.off('disconnect', onSocketDisconnect);
			socket.off('join_error', onJoinError);
			socket.off('game_not_found', onGameNotFound);
			socket.off('username_already_exists', onUsernameAlreadyExists);
			socket.off('joined_game', onJoinedGameJoinUi);
		}
	});

	const prefetch_username = async () => {
		if (game_pin.length >= 6) {
			const battleName = getBattlePlayUsername(game_pin);
			if (battleName) {
				username = battleName;
				return;
			}
		}
		try {
			const res = await fetch('/api/v1/users/me');
			if (res.status !== 200) return;
			const json = await res.json();
			username = json.username;
		} catch {
			/* guest join */
		}
	};

	$effect(() => {
		if (!browser || game_pin.length < 6) return;
		const battleName = getBattlePlayUsername(game_pin);
		if (battleName && username !== battleName) {
			username = battleName;
		}
	});

	const set_game_pin = async () => {
		try {
			const res = await fetch(`/api/v1/quiz/play/check_captcha/${game_pin}`);
			const json = await res.json().catch(() => ({}));
			game_mode = normalizeGameMode(json.game_mode) ?? json.game_mode;
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

	const emitJoin = (captcha_resp?: string) => {
		socket.emit('join_game', {
			username,
			game_pin,
			captcha: captcha_resp,
			custom_field: custom_field ? custom_field_value : undefined
		});
	};

	const performJoin = async () => {
		joinError = '';
		if (username.length <= 3) {
			joinError = 'Nickname must be at least 4 characters.';
			return;
		}
		if (Cookies.get('kicked')) return;
		if (!socket.connected) {
			joinError = joinErrorMessage('not_connected');
			socket.connect();
			return;
		}
		joining = true;
		if (captcha_enabled) {
			if (hcaptchaSitekey) {
				try {
					const { response } = await hcaptcha.execute(hcaptchaWidgetID, { async: true });
					emitJoin(response);
				} catch (err) {
					joining = false;
					if (sentry_dsn !== null) Sentry.captureException(err);
					joinError = joinErrorMessage('captcha_failed');
				}
			} else if (recaptcha_key) {
				grecaptcha.ready(() => {
					grecaptcha.execute(recaptcha_key, { action: 'submit' }).then(
						function (token) {
							emitJoin(token);
						},
						function () {
							joining = false;
							joinError = joinErrorMessage('captcha_failed');
						}
					);
				});
			} else {
				joining = false;
				joinError = joinErrorMessage('captcha_failed');
			}
		} else {
			emitJoin();
		}
	};

	const setUsername = async (e: Event) => {
		e.preventDefault();
		await performJoin();
	};

	$effect(() => {
		if (!browser || battleAutoJoinStarted || joining) return;
		if (normalizeGameMode(game_mode) !== 'battle') return;
		if (game_pin.length < 6 || username.length <= 3) return;
		if (!socketConnected) return;
		battleAutoJoinStarted = true;
		void performJoin();
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
			{#if joinError}
				<p class="text-danger text-sm text-center" role="alert">{joinError}</p>
			{/if}
			{#if !socketConnected}
				<p class="text-ink-muted text-xs text-center">Connecting to game server…</p>
			{/if}
			<button
				type="submit"
				class="btn btn-primary w-full"
				disabled={username.length <= 3 || joining}
				>{joining ? 'Joining…' : $t('words.submit')}</button
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
