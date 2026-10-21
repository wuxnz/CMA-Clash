<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { signedIn, pathname, isSiteAdmin } from '$lib/stores';
	import { createTippy } from 'svelte-tippy';
	import { beforeNavigate } from '$app/navigation';
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import { isNavLinkActive } from '$lib/navActive';
	import { refreshSiteAdminFlag } from '$lib/site-admin';
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

	onMount(() => {
		void refreshSiteAdminFlag();
	});

	function navLinkClass(href: string, play = false): string {
		const active = isNavLinkActive(page.url.pathname, href);
		const parts = ['btn-nav'];
		if (play) {
			parts.push('border border-gold/50 rounded-md text-gold');
			if (active) parts.push('ring-1 ring-gold/70');
		} else if (active) {
			parts.push('btn-nav-active');
		}
		return parts.join(' ');
	}

	function navAriaCurrent(href: string): 'page' | undefined {
		return isNavLinkActive(page.url.pathname, href) ? 'page' : undefined;
	}
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
				class="font-display font-bold tracking-tight text-xl lg:text-2xl text-ink link-hover px-3 lg:px-5 {isNavLinkActive(
					page.url.pathname,
					'/'
				)
					? 'text-primary'
					: ''}"
				aria-current={navAriaCurrent('/')}
				>CMA Clash</a
			>
			<a class={navLinkClass('/play', true)} href="/play" aria-current={navAriaCurrent('/play')}
				>{$t('words.play')}</a
			>
			<a class={navLinkClass('/host')} href="/host" aria-current={navAriaCurrent('/host')}>Host</a>
			<a class={navLinkClass('/leaderboard')} href="/leaderboard" aria-current={navAriaCurrent('/leaderboard')}
				>Leaderboard</a
			>
			<a class={navLinkClass('/battle')} href="/battle" aria-current={navAriaCurrent('/battle')}>Battle</a>
			<a class={navLinkClass('/explore')} href="/explore" aria-current={navAriaCurrent('/explore')}
				>{$t('words.explore')}</a
			>
			<a class={navLinkClass('/search')} href="/search" aria-current={navAriaCurrent('/search')}
				>{$t('words.search')}</a
			>
			<a class={navLinkClass('/study')} href="/study" aria-current={navAriaCurrent('/study')}>Study</a>
			{#if $signedIn}
				<a class={navLinkClass('/dashboard')} href="/dashboard" aria-current={navAriaCurrent('/dashboard')}
					>{$t('words.dashboard')}</a
				>
				{#if $isSiteAdmin}
					<a
						class={navLinkClass('/site-admin/users')}
						href="/site-admin/users"
						aria-current={navAriaCurrent('/site-admin/users')}>Site admin</a
					>
				{/if}
			{:else}
				<a class={navLinkClass('/docs')} href="/docs" aria-current={navAriaCurrent('/docs')}
					>{$t('words.docs')}</a
				>
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
				{#if !registration_disabled}
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
				class="font-display font-bold tracking-tight text-xl lg:text-2xl text-ink link-hover px-3 lg:px-5 {isNavLinkActive(
					page.url.pathname,
					'/'
				)
					? 'text-primary'
					: ''}"
				aria-current={navAriaCurrent('/')}
				>CMA Clash</a
			>
			<a class="{navLinkClass('/play', true)} flex" href="/play" aria-current={navAriaCurrent('/play')}
				>{$t('words.play')}</a
			>
			<a class="{navLinkClass('/host')} flex" href="/host" aria-current={navAriaCurrent('/host')}>Host</a>

			<div class="flex items-center">
				{#if menuIsClosed}
					<button
						class="px-3 text-ink min-h-11 min-w-11 inline-flex items-center justify-center"
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
						class="px-3 text-ink min-h-11 min-w-11 inline-flex items-center justify-center"
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
				<a class={navLinkClass('/host')} href="/host" aria-current={navAriaCurrent('/host')}>Host</a>
				<a class={navLinkClass('/leaderboard')} href="/leaderboard" aria-current={navAriaCurrent('/leaderboard')}
					>Leaderboard</a
				>
				<a class={navLinkClass('/battle')} href="/battle" aria-current={navAriaCurrent('/battle')}>Battle</a>
				<a class={navLinkClass('/explore')} href="/explore" aria-current={navAriaCurrent('/explore')}
					>{$t('words.explore')}</a
				>
				<a class={navLinkClass('/search')} href="/search" aria-current={navAriaCurrent('/search')}
					>{$t('words.search')}</a
				>
				<a class={navLinkClass('/study')} href="/study" aria-current={navAriaCurrent('/study')}>Study</a>
				{#if $signedIn}
					<a class={navLinkClass('/dashboard')} href="/dashboard" aria-current={navAriaCurrent('/dashboard')}
						>{$t('words.dashboard')}</a
					>
					{#if $isSiteAdmin}
						<a
							class={navLinkClass('/site-admin/users')}
							href="/site-admin/users"
							aria-current={navAriaCurrent('/site-admin/users')}>Site admin</a
						>
					{/if}
				{:else}
					<a class={navLinkClass('/docs')} href="/docs" aria-current={navAriaCurrent('/docs')}
						>{$t('words.docs')}</a
					>
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
					{#if !registration_disabled}
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
