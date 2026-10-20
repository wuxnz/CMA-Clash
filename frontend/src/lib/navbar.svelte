<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { signedIn, pathname } from '$lib/stores';
	import { createTippy } from 'svelte-tippy';
	import { beforeNavigate } from '$app/navigation';
	import { draw, slide } from 'svelte/transition';
	import { registration_disabled } from './config';

	const tippy = createTippy({
		arrow: true,
		animation: 'perspective-subtle',
		placement: 'bottom'
	});

	const { t } = getLocalization();

	let menuIsClosed = $state(true);
	const toggleMenu = () => {
		menuIsClosed = !menuIsClosed;
	};

	beforeNavigate(() => {
		menuIsClosed = true; // Closes menu to let the user see the page beneath
	});

</script>

<nav
	class="w-screen px-4 lg:px-10 py-2.5 fixed bg-paper/90 backdrop-blur-xl border-b border-white/5 z-30 top-0"
	aria-label="Main navigation"
>
	<!-- Desktop navbar -->
	<div class="hidden lg:flex lg:items-center lg:flex-row lg:justify-between">
		<div class="lg:flex lg:items-center lg:flex-row gap-1">
			<a
				href="/"
				class="font-display font-bold tracking-tight text-xl lg:text-2xl text-ink link-hover px-3 lg:px-5"
				>CMA Clash</a
			>
			<a class="btn-nav border border-gold/50 rounded-md text-gold" href="/play"
				>{$t('words.play')}</a
			>
			<a class="btn-nav" href="/leaderboard">Leaderboard</a>
			<a class="btn-nav" href="/battle">Battle</a>
			<a class="btn-nav" href="/explore">{$t('words.explore')}</a>
			<a class="btn-nav" href="/search">{$t('words.search')}</a>
			{#if $signedIn}
				<a class="btn-nav" href="/dashboard">{$t('words.dashboard')}</a>
			{:else}
				<a class="btn-nav" href="/docs">{$t('words.docs')}</a>
				<a
					target="_blank"
					class="btn-nav flex items-center gap-1"
					href="https://github.com/wuxnz/CMA-Clash"
					>GitHub
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width="17"
						height="17"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
						class="lucide lucide-external-link shrink-0"
						><path
							d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"
						/><polyline points="15 3 21 3 21 9" /><line
							x1="10"
							x2="21"
							y1="14"
							y2="3"
						/></svg
					>
				</a>
			{/if}
		</div>
		<div class="lg:flex lg:items-center lg:flex-row gap-1">
			{#if $signedIn}
				<a class="btn-nav" href="/api/v1/users/logout">{$t('words.logout')}</a>
			{:else}
				{#if registration_disabled}
					<a class="btn-nav" href="/account/register">{$t('words.register')}</a>
				{/if}

				<a class="btn-nav" href="/account/login?returnTo={$pathname}">{$t('words.login')}</a
				>
			{/if}

		</div>
	</div>

	<!-- Mobile navbar -->
	<div class="lg:hidden">
		<!-- Navbar header -->
		<div class="flex items-center justify-between">
			<a
				href="/"
				class="font-display font-bold tracking-tight text-xl lg:text-2xl text-ink link-hover px-3 lg:px-5"
				>CMA Clash</a
			>
			<a class="btn-nav flex" href="/play">{$t('words.play')}</a>

			<div class="flex items-center">
				{#if menuIsClosed}
					<button
						class="px-3 text-ink"
						id="open-menu"
						onclick={toggleMenu}
						aria-label="Open navbar"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="w-6 h-6"
						>
							<path d="M3 6h18M3 12h18M3 18h18" />
						</svg>
					</button>
				{:else}
					<button
						class="px-3 text-ink"
						id="close-menu"
						onclick={toggleMenu}
						aria-label="Close navbar"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="w-6 h-6"
							><path in:draw|global={{ duration: 300 }} d="M18 6 6 18" /><path
								in:draw|global={{ duration: 300 }}
								d="m6 6 12 12"
							/></svg
						>
					</button>
				{/if}
			</div>
		</div>

		<!-- Navbar content -->
		{#if !menuIsClosed}
			<div class="flex flex-col" transition:slide|global={{ duration: 400 }}>
				<a class="btn-nav" href="/leaderboard">Leaderboard</a>
				<a class="btn-nav" href="/battle">Battle</a>
				<a class="btn-nav" href="/explore">{$t('words.explore')}</a>
				<a class="btn-nav" href="/search">{$t('words.search')}</a>
				{#if $signedIn}
					<a class="btn-nav" href="/dashboard">{$t('words.dashboard')}</a>
				{:else}
					<a class="btn-nav" href="/docs">{$t('words.docs')}</a>
					<a
						target="_blank"
						class="btn-nav flex items-center gap-1"
						href="https://github.com/wuxnz/CMA-Clash"
						>GitHub
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="17"
							height="17"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="lucide lucide-external-link shrink-0"
							><path
								d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"
							/><polyline points="15 3 21 3 21 9" /><line
								x1="10"
								x2="21"
								y1="14"
								y2="3"
							/></svg
						>
					</a>
				{/if}

				<hr class="my-1 border" />
				{#if $signedIn}
					<a class="btn-nav" href="/api/v1/users/logout">{$t('words.logout')}</a>
				{:else}
					{#if registration_disabled}
						<a class="btn-nav" href="/account/register">{$t('words.register')}</a>
					{/if}

					<a class="btn-nav" href="/account/login?returnTo={$pathname}"
						>{$t('words.login')}</a
					>
				{/if}

			</div>
		{/if}
	</div>
</nav>
