<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { createForm } from 'felte';
	import { resolve } from '$app/paths';
	import { getLocalization } from '$lib/i18n';
	import { validateSchema } from '@felte/validator-yup';
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import Footer from '$lib/footer.svelte';
	import Button from '$lib/ui/Button.svelte';
	import Spinner from '$lib/Spinner.svelte';
	import { focusTrap } from '$lib/ui/focusTrap';
	import AuthShell from '$lib/ui/AuthShell.svelte';
	import { registerConflictFromResponse, registerConflictMessage } from '$lib/registerApiErrors';

	const { t } = getLocalization();
	import reporter from '@felte/reporter-tippy';

	navbarVisible.visible = true;
	import * as yup from 'yup';

	const registerSchema = yup.object({
		email: yup.string().email('Email must be valid!').required(),
		password1: yup
			.string()
			.required()
			.min(8, 'Password must be at least 8 characters long!')
			.max(100, 'Password must be at most 100 characters long!'),
		password2: yup
			.string()
			.required()
			.test('equal', 'Passwords do not match!', function (v) {
				const ref = yup.ref('password1');
				return v === this.resolve(ref);
			}),
		username: yup
			.string()
			.required()
			.min(3, 'Username must be at least 3 characters long')
			.max(20, 'Username must be at most 20 characters long'),
		privacy_accept: yup
			.boolean()
			.oneOf([true], 'You must accept the privacy policy to register!'),
		tos_accept: yup.boolean().oneOf([true], 'You must accept the terms of service to register!')
	});

	let serverFieldError = $state<{ field: 'email' | 'username'; message: string } | null>(null);

	const { form, errors, isValid, isSubmitting } = createForm<
		yup.InferType<typeof registerSchema>
	>({
		validate: validateSchema(registerSchema),
		extend: [reporter()],
		onSubmit: async (values) => {
			serverFieldError = null;
			const res = await fetch('/api/v1/users/create', {
				method: 'post',
				body: JSON.stringify({
					email: values.email,
					password: values.password1,
					username: values.username
				}),
				headers: {
					'Content-Type': 'application/json'
				}
			});
			if (res.status === 200) {
				const payload = await res.json();
				window.location.href = `/account/check-email?email=${encodeURIComponent(payload.email ?? values.email)}`;
				return;
			}
			const body = await res.json().catch(() => ({}));
			const conflict = registerConflictFromResponse(res.status, body.detail);
			if (conflict) {
				serverFieldError = { field: conflict, message: registerConflictMessage(conflict) };
				return;
			}
			if (res.status === 400) {
				responseData.data = '400';
			} else {
				responseData.data = 'error';
			}
			responseData.open = true;
		}
	});
	let responseData = $state({
		open: false,
		data: ''
	});

	function closeResponse() {
		responseData.open = false;
		if (responseData.data === '200') {
			window.location.assign('/');
		} else {
			window.location.reload();
		}
	}

	const heading = $derived(
		responseData.data === 'error'
			? 'Unexpected error'
			: responseData.data === '200'
				? 'Check your email'
				: responseData.data === '400'
					? 'Email not accepted'
					: 'Something went wrong'
	);
</script>

<svelte:head>
	<title>CMA Clash: Register</title>
</svelte:head>
<div class="min-h-screen flex flex-col">
	<AuthShell
		eyebrow="Create account"
		title="Start your"
		accent="streak today."
		lede="An account keeps your XP, your streak and your topic mastery across every device."
		points={[
			{
				label: 'Keep your progress',
				body: 'XP, streaks and mastery charts sync to your profile on every device.'
			},
			{
				label: 'Climb the ladder',
				body: 'Weekly and all-time leaderboards for every certification on the platform.'
			},
			{
				label: 'Your own question sets',
				body: 'Import, edit and host private sets for your cohort or study group.'
			}
		]}
	>
		<div class="px-6 py-7 sm:px-8 sm:py-8">
			<p class="eyebrow mb-5">Register</p>

			<form use:form class="space-y-5">
				<div>
					<label class="eyebrow block" for="email">{$t('words.email')}</label>
					<input
						id="email"
						name="email"
						type="email"
						class="ledger-input mt-2 min-h-11"
						placeholder={$t('words.email')}
						autocomplete="email"
					/>
					{#if serverFieldError?.field === 'email'}
						<p class="text-xs text-danger mt-1" role="alert">
							{serverFieldError.message}
						</p>
					{:else if $errors.email?.length}
						<p class="text-xs text-danger mt-1">{$errors.email[0]}</p>
					{/if}
				</div>
				<div>
					<label class="eyebrow block" for="username">{$t('words.username')}</label>
					<input
						id="username"
						name="username"
						type="text"
						class="ledger-input mt-2 min-h-11"
						placeholder={$t('words.username')}
						autocomplete="username"
					/>
					{#if serverFieldError?.field === 'username'}
						<p class="text-xs text-danger mt-1" role="alert">
							{serverFieldError.message}
						</p>
					{:else if $errors.username?.length}
						<p class="text-xs text-danger mt-1">{$errors.username[0]}</p>
					{/if}
				</div>
				<div>
					<label class="eyebrow block" for="password1">{$t('words.password')}</label>
					<input
						id="password1"
						name="password1"
						type="password"
						class="ledger-input mt-2 min-h-11"
						placeholder={$t('words.password')}
						autocomplete="new-password"
					/>
					{#if $errors.password1?.length}
						<p class="text-xs text-danger mt-1">{$errors.password1[0]}</p>
					{/if}
				</div>
				<div>
					<label class="eyebrow block" for="password2"
						>{$t('words.repeat_password')}</label
					>
					<input
						id="password2"
						name="password2"
						type="password"
						class="ledger-input mt-2 min-h-11"
						placeholder={$t('words.password')}
						autocomplete="new-password"
					/>
					{#if $errors.password2?.length}
						<p class="text-xs text-danger mt-1">{$errors.password2[0]}</p>
					{/if}
				</div>
				<label class="flex items-start gap-3 min-h-11 text-sm text-ink-muted">
					<input type="checkbox" name="privacy_accept" class="mt-1" />
					<span>
						I've read the
						<a href={resolve('/docs/privacy-policy')} class="text-ink link-hover">privacy policy</a
						>.
					</span>
				</label>
				<label class="flex items-start gap-3 min-h-11 text-sm text-ink-muted">
					<input type="checkbox" name="tos_accept" class="mt-1" />
					<span>
						I agree to the
						<a href={resolve('/docs/tos')} class="text-ink link-hover">terms of service</a>.
					</span>
				</label>

				<div class="flex items-center justify-between gap-3 pt-3 border-t border-line">
					<a
						href={resolve('/account/reset-password')}
						class="text-sm text-ink-muted link-hover min-h-11 inline-flex items-center"
					>
						{$t('register_page.forgot_password?')}
					</a>
					<Button type="submit" class="w-auto" disabled={!$isValid || $isSubmitting}>
						{#if $isSubmitting}
							<Spinner class="h-4 w-4" my_20={false} />
						{:else}
							{$t('words.register')}
						{/if}
					</Button>
				</div>
			</form>
		</div>

		<div
			class="flex items-center justify-center py-4 px-6 text-center border-t border-line bg-paper-muted"
		>
			<span class="text-sm text-ink-muted">{$t('register_page.already_have_account?')}</span>
			<a href={resolve('/account/login')} class="mx-2 text-sm text-ink link-hover">{$t('words.login')}</a
			>
		</div>
	</AuthShell>
	<Footer />
</div>

{#if responseData.open}
	<div
		class="dialog-backdrop"
		onclick={(e) => {
			if (e.target === e.currentTarget) closeResponse();
		}}
		role="presentation"
	>
		<div
			use:focusTrap
			class="dialog-panel dialog-panel-in p-5"
			role="dialog"
			aria-modal="true"
			aria-labelledby="register-dialog-title"
			tabindex="-1"
		>
			<h2 id="register-dialog-title" class="text-lg font-semibold text-ink tracking-tight">
				{heading}
			</h2>
			<p class="text-sm text-ink-muted mt-2 leading-relaxed">
				{#if responseData.data === '200'}
					You signed up successfully. Check your mailbox to confirm your email address.
				{:else if responseData.data === '400'}
					This email address isn't accepted.
				{:else}
					Please try again or contact support if the problem persists.
				{/if}
			</p>
			<div class="mt-6">
				<Button class="w-full" onclick={closeResponse}>{$t('words.close')}</Button>
			</div>
		</div>
	</div>
{/if}
