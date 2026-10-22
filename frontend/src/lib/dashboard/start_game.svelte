<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { resolve } from '$app/paths';
	import { captcha_enabled } from '$lib/config';
	import { onMount } from 'svelte';
	import Button from '$lib/ui/Button.svelte';
	import Toggle from '$lib/ui/Toggle.svelte';
	import { focusTrap } from '$lib/ui/focusTrap';
	import { adminLobbyUrl, startHostGame } from '$lib/cma/host-game';
	import { normalizeQuizText } from '$lib/cma/text';
	import Spinner from '$lib/Spinner.svelte';

	let { quiz_id = $bindable(), title = '' } = $props();

	let captcha_selected = $state(false);
	let selected_game_mode = $state<'kahoot' | 'normal'>('kahoot');
	let loading = $state(false);
	let custom_field = $state('');
	let cqcs_enabled = $state(false);
	let randomized_answers = $state(false);
	let error = $state('');
	let quizTitle = $state(title);
	let quizMeta = $state('');

	onMount(() => {
		const ls_data = localStorage.getItem('custom_field');
		custom_field = ls_data ? ls_data : '';
	});

	$effect(() => {
		const id = quiz_id;
		if (!id) return;
		if (title) quizTitle = title;
		let cancelled = false;
		fetch(`/api/v1/quiz/get/public/${id}`, { credentials: 'include' })
			.then(async (res) => {
				if (!res.ok || cancelled) return;
				const quiz = await res.json();
				if (cancelled) return;
				quizTitle = normalizeQuizText(quiz.title) || 'Host a Clash';
				const count = Array.isArray(quiz.questions) ? quiz.questions.length : 0;
				quizMeta = count ? `${count} questions · public set` : 'Public set';
			})
			.catch(() => {});
		return () => {
			cancelled = true;
		};
	});

	$effect(() => {
		const onKey = (event: KeyboardEvent) => {
			if (event.key === 'Escape') close();
		};
		document.addEventListener('keydown', onKey);
		const prevOverflow = document.body.style.overflow;
		document.body.style.overflow = 'hidden';
		return () => {
			document.removeEventListener('keydown', onKey);
			document.body.style.overflow = prevOverflow;
		};
	});

	function close() {
		if (loading) return;
		quiz_id = null;
	}

	const start_game = async () => {
		if (!quiz_id) return;
		loading = true;
		error = '';
		localStorage.setItem('custom_field', custom_field);
		const result = await startHostGame(quiz_id, {
			captcha_enabled: captcha_enabled && captcha_selected,
			game_mode: selected_game_mode,
			custom_field,
			cqcs_enabled,
			randomize_answers: randomized_answers
		});
		if (result === 'auth') {
			window.location.assign(
				`/account/login?returnTo=${encodeURIComponent(window.location.pathname)}`
			);
			return;
		}
		if (result === 'error') {
			error = 'Could not start the game. Try again.';
			loading = false;
			return;
		}
		const plausible = (window as Window & { plausible?: (..._args: unknown[]) => void }).plausible;
		plausible?.('Started Game', { props: { quiz_id, game_id: result.game_id } });
		window.location.assign(adminLobbyUrl(result));
	};
</script>

<div
	class="dialog-backdrop"
	data-host-modal
	onclick={(e) => {
		if (e.target === e.currentTarget) close();
	}}
	onkeydown={(e) => {
		if (e.key === 'Escape') close();
	}}
	role="presentation"
>
	<div
		use:focusTrap
		class="dialog-panel dialog-panel-in"
		role="dialog"
		aria-modal="true"
		aria-labelledby="host-dialog-title"
		tabindex="-1"
	>
		<div class="dialog-body px-5 pt-5 pb-4 min-w-0">
			<p id="host-dialog-title" class="text-lg font-semibold text-ink tracking-tight truncate">
				{quizTitle || 'Host a Clash'}
			</p>
			{#if quizMeta}
				<p class="text-sm text-ink-muted mt-1">{quizMeta}</p>
			{/if}

			<div class="mt-6" role="radiogroup" aria-label="Game mode">
				<p class="text-sm font-medium text-ink mb-2">Game mode</p>
				<div class="flex flex-col gap-2">
					<button
						type="button"
						role="radio"
						aria-checked={selected_game_mode === 'kahoot'}
						class="mode-option"
						onclick={() => (selected_game_mode = 'kahoot')}
					>
						<span class="text-sm font-medium text-ink">Standard</span>
						<span class="block text-xs text-ink-muted mt-0.5">
							Questions stay on the host screen. Players tap matching colors.
						</span>
					</button>
					<button
						type="button"
						role="radio"
						aria-checked={selected_game_mode === 'normal'}
						class="mode-option"
						onclick={() => (selected_game_mode = 'normal')}
					>
						<span class="text-sm font-medium text-ink">On player devices</span>
						<span class="block text-xs text-ink-muted mt-0.5">
							Players see the question and answers on their own screens.
						</span>
					</button>
				</div>
			</div>

			<div class="mt-5">
				<label class="text-sm font-medium text-ink" for="host-custom-field">Custom field</label>
				<p class="text-xs text-ink-muted mt-0.5">Optional — shown when players join (email, class, etc.).</p>
				<input
					id="host-custom-field"
					class="ledger-input mt-2 min-h-11"
					bind:value={custom_field}
					placeholder="Class period"
					autocomplete="off"
				/>
			</div>

			<div class="mt-2 divide-y divide-white/[0.07]">
				{#if captcha_enabled}
					<div class="flex items-center justify-between gap-4 min-h-11 py-3">
						<div class="min-w-0">
							<p class="text-sm text-ink">Captcha</p>
							<p class="text-xs text-ink-muted mt-0.5">
								Loads Google reCAPTCHA for every player. Only if you need it.
							</p>
						</div>
						<Toggle bind:checked={captcha_selected} label="Captcha" />
					</div>
				{/if}
				<div class="flex items-center justify-between gap-4 min-h-11 py-3">
					<div class="min-w-0">
						<p class="text-sm text-ink">Randomize answers</p>
						<p class="text-xs text-ink-muted mt-0.5">Shuffle answer order for each player.</p>
					</div>
					<Toggle bind:checked={randomized_answers} label="Randomize answers" />
				</div>
				<div class="flex items-center justify-between gap-4 min-h-11 py-3">
					<div class="min-w-0">
						<p class="text-sm text-ink">Quiz controllers</p>
						<p class="text-xs text-ink-muted mt-0.5">
							Allow physical clickers.
							<a href={resolve('/controller')} class="text-ink link-hover" target="_blank" rel="noreferrer">Learn more</a>
						</p>
					</div>
					<Toggle bind:checked={cqcs_enabled} label="Quiz controllers" />
				</div>
			</div>

			{#if error}
				<p class="text-sm text-danger mt-3">{error}</p>
			{/if}
		</div>

		<div
			class="shrink-0 px-5 pt-3 pb-[max(0.75rem,env(safe-area-inset-bottom))] flex flex-col-reverse sm:flex-row gap-2 border-t border-white/[0.07] bg-surface"
		>
			<Button variant="secondary" class="w-full sm:w-auto" onclick={close} disabled={loading}>
				Cancel
			</Button>
			<Button class="w-full sm:flex-1" onclick={start_game} disabled={loading}>
				{#if loading}
					<Spinner my_20={false} class="h-4 w-4" />
					Starting
				{:else}
					Start game
				{/if}
			</Button>
		</div>
	</div>
</div>
