<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { signedIn, pathname, isSiteAdmin } from '$lib/stores';
	import { beforeNavigate } from '$app/navigation';
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import { isNavLinkActive } from '$lib/navActive';
	import { refreshSiteAdminFlag } from '$lib/site-admin';
	import { draw, fly } from 'svelte/transition';
	import { registration_disabled } from './config';
	import ThemeToggle from '$lib/ui/ThemeToggle.svelte';
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { resolve } from '$app/paths';
	import type { Pathname } from '$app/types';

	const reduced = prefersReducedMotion();

	const { t } = getLocalization();

	let menuIsClosed = $state(true);
	let moreIsOpen = $state(false);
	const toggleMenu = () => {
		menuIsClosed = !menuIsClosed;
		if (menuIsClosed) moreIsOpen = false;
	};
	const toggleMore = () => {
		moreIsOpen = !moreIsOpen;
	};

	beforeNavigate(() => {
		menuIsClosed = true; // Closes menu to let the user see the page beneath
		moreIsOpen = false;
	});

	onMount(() => {
		void refreshSiteAdminFlag();

		const onKeydown = (e: KeyboardEvent) => {
			if (e.key !== 'Escape') return;
			moreIsOpen = false;
			menuIsClosed = true;
		};
		const onPointerDown = (e: PointerEvent) => {
			const target = e.target as HTMLElement | null;
			if (!moreIsOpen) return;
			if (target?.closest('[data-more-menu]')) return;
			moreIsOpen = false;
		};
		window.addEventListener('keydown', onKeydown);
		window.addEventListener('pointerdown', onPointerDown);
		return () => {
			window.removeEventListener('keydown', onKeydown);
			window.removeEventListener('pointerdown', onPointerDown);
		};
	});

	function navLinkClass(href: string, play = false): string {
		const active = isNavLinkActive(page.url.pathname, href);
		const parts = ['btn-nav'];
		if (play) {
			parts.push('border border-primary/60 text-primary');
			if (active) parts.push('bg-primary text-white border-primary');
		} else if (active) {
			parts.push('btn-nav-active');
		}
		return parts.join(' ');
	}

	function navAriaCurrent(href: string): 'page' | undefined {
		return isNavLinkActive(page.url.pathname, href) ? 'page' : undefined;
	}

	/** Style for rows inside the "More" dropdown. */
	function navMenuItemClass(href: string): string {
		const base = 'block px-3 py-2.5 text-sm hover:text-ink hover:bg-elevated transition-colors';
		return isNavLinkActive(page.url.pathname, href)
			? `${base} text-ink bg-elevated font-medium`
			: `${base} text-ink-muted`;
	}

	/** Style for secondary rows inside the mobile panel. */
	function navMobileItemClass(href: string): string {
		const base =
			'flex items-center justify-between gap-4 py-3.5 border-b border-line text-base';
		return isNavLinkActive(page.url.pathname, href)
			? `${base} btn-nav-active`
			: `${base} text-ink-muted`;
	}

	/** Shown inline at every desktop width. */
	const primaryLinks = [
		{ href: '/play', label: 'words.play', play: true },
		{ href: '/host', label: 'Host' },
		{ href: '/leaderboard', label: 'Leaderboard' },
		{ href: '/battle', label: 'Battle' },
		{ href: '/study', label: 'Study' }
	] as const;

	/** Collapsed into the "More" menu below xl, inline at xl and above. */
	const secondaryLinks = $derived.by(() => {
		const links: { href: Pathname; label: string }[] = [
			{ href: '/explore', label: $t('words.explore') },
			{ href: '/search', label: $t('words.search') }
		];
		if (!$signedIn) links.push({ href: '/docs', label: $t('words.docs') });
		return links;
	});

	/** Always available in the dropdown, never inline. */
	const adminLinks = $derived.by(() => {
		const links: { href: Pathname; label: string }[] = [];
		if ($signedIn && $isSiteAdmin)
			links.push({ href: '/site-admin/users', label: 'Site admin' });
		return links;
	});

	/**
	 * Absolute external link. It must never be routed through `resolve()` - that
	 * would prefix the app base path onto another origin.
	 */
	const githubUrl = 'https://github.com/wuxnz/CMA-Clash';
	const externalGithub = {
		label: 'GitHub'
	};
</script>

<svelte:head>
	<meta name="theme-color" content="#070707" />
</svelte:head>

<nav
	class="fixed inset-x-0 top-0 z-40 border-b border-line bg-paper/92 backdrop-blur-xl"
	aria-label="Main navigation"
>
	<!-- ==================== DESKTOP ==================== -->
	<div class="hidden lg:block px-6 xl:px-10">
		<div class="flex items-center justify-between gap-4 h-16">
			<!-- Brand + primary links -->
			<div class="flex items-center gap-4 xl:gap-6 min-w-0">
				<a
					href={resolve('/')}
					class="font-display text-2xl text-ink link-hover whitespace-nowrap shrink-0 {isNavLinkActive(
						page.url.pathname,
						'/'
					)
						? 'text-primary'
						: ''}"
					aria-current={navAriaCurrent('/')}
				>
					CMA <em class="italic font-normal">Clash</em>
				</a>

				<span
					class="hidden xl:inline font-mono text-[0.62rem] uppercase tracking-[0.24em] text-ink-subtle whitespace-nowrap"
					>Edition 04</span
				>

				<nav class="flex items-center gap-0.5 min-w-0" aria-label="Sections">
					{#each primaryLinks as link (link.href)}
						<a
							class={navLinkClass(link.href, 'play' in link && link.play)}
							href={resolve(link.href)}
							aria-current={navAriaCurrent(link.href)}
						>
							{'label' in link && link.label.startsWith('words.')
								? $t(link.label as never)
								: link.label}
						</a>
					{/each}

					<!-- Secondary links: inline at xl, dropdown below -->
					{#each secondaryLinks as link (link.href)}
						<a
							class="{navLinkClass(link.href)} hidden xl:inline-flex"
							href={resolve(link.href)}
							aria-current={navAriaCurrent(link.href)}
						>
							{link.label}
						</a>
					{/each}

					<a
						class="hidden xl:inline-flex btn-nav items-center gap-1"
						target="_blank"
						href={githubUrl}
					>
						GitHub
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="15"
							height="15"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="shrink-0"
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
				</nav>
			</div>

			<!-- Right cluster -->
			<div class="flex items-center gap-3 shrink-0">
				<ThemeToggle />
				{#if $signedIn}
					<a class="btn-nav" href={resolve('/dashboard')} aria-current={navAriaCurrent('/dashboard')}
						>{$t('words.dashboard')}</a
					>
					<a class="btn-nav" href={resolve('/api/v1/users/logout' as Pathname)}>{$t('words.logout')}</a>
				{:else}
					{#if !registration_disabled}
						<a class="btn-nav" href={resolve('/account/register')}>{$t('words.register')}</a>
					{/if}
					<a class="btn-nav" href={resolve('/account/login?returnTo=' + $pathname as Pathname)}
						>{$t('words.login')}</a
					>
				{/if}

				<div class="relative" data-more-menu>
					<button
						type="button"
						class="btn-nav inline-flex items-center gap-1.5 xl:hidden"
						aria-expanded={moreIsOpen}
						aria-haspopup="true"
						onclick={toggleMore}
					>
						More
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="14"
							height="14"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2.2"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="shrink-0 transition-transform duration-200"
							style="transform: {moreIsOpen ? 'rotate(180deg)' : 'none'}"
							><polyline points="6 9 12 15 18 9" /></svg
						>
					</button>

					{#if moreIsOpen}
						<div
							class="absolute right-0 top-full mt-2 w-56 border border-line bg-paper p-1 shadow-[var(--shadow-card)]"
							transition:fly={{ y: -6, duration: reduced ? 0 : 180 }}
						>
							{#each secondaryLinks as link (link.href)}
								<a
									class={navMenuItemClass(link.href)}
									href={resolve(link.href)}
									aria-current={navAriaCurrent(link.href)}
									onclick={() => (moreIsOpen = false)}
								>
									{link.label}
								</a>
							{/each}
							{#each adminLinks as link (link.href)}
								<a
									class={navMenuItemClass(link.href)}
									href={resolve(link.href)}
									aria-current={navAriaCurrent(link.href)}
									onclick={() => (moreIsOpen = false)}
								>
									{link.label}
								</a>
							{/each}
							<a
								class="block px-3 py-2.5 text-sm text-ink-muted hover:text-ink hover:bg-elevated transition-colors"
								target="_blank"
								href={githubUrl}
							>
								{externalGithub.label} ↗
							</a>
						</div>
					{/if}
				</div>
			</div>
		</div>
	</div>

	<!-- ==================== MOBILE ==================== -->
	<div class="lg:hidden px-4">
		<div class="flex items-center justify-between gap-2 h-16">
			<a
				href={resolve('/')}
				class="font-display text-xl text-ink link-hover whitespace-nowrap shrink-0 {isNavLinkActive(
					page.url.pathname,
					'/'
				)
					? 'text-primary'
					: ''}"
				aria-current={navAriaCurrent('/')}>CMA <em class="italic font-normal">Clash</em></a
			>

			<div class="flex items-center gap-1 shrink-0">
				<a
					class="{navLinkClass('/play', true)} flex px-2.5"
					href={resolve('/play')}
					aria-current={navAriaCurrent('/play')}>{$t('words.play')}</a
				>
				<a
					class="hidden sm:inline-flex btn-nav"
					href={resolve('/host')}
					aria-current={navAriaCurrent('/host')}>Host</a
				>
				<ThemeToggle />
				<button
					class="px-2 text-ink min-h-11 min-w-11 inline-flex items-center justify-center"
					id="open-menu"
					onclick={toggleMenu}
					aria-label={menuIsClosed ? 'Open navbar' : 'Close navbar'}
					aria-expanded={!menuIsClosed}
					aria-controls="mobile-nav"
				>
					{#if menuIsClosed}
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="22"
							height="22"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="1.8"
							stroke-linecap="round"
							stroke-linejoin="round"
						>
							<path d="M3 6h18M3 12h18M3 18h18" />
						</svg>
					{:else}
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="22"
							height="22"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="1.8"
							stroke-linecap="round"
							stroke-linejoin="round"
						>
							<path in:draw|global={{ duration: 300 }} d="M18 6 6 18" /><path
								in:draw|global={{ duration: 300 }}
								d="m6 6 12 12"
							/></svg
						>
					{/if}
				</button>
			</div>
		</div>
	</div>
</nav>

<!--
	The mobile panel lives outside <nav> on purpose: the nav uses
	`backdrop-blur`, which makes it a containing block for `position: fixed`
	descendants. Nested inside it, the panel would be sized to the nav bar
	instead of the viewport.
-->
{#if !menuIsClosed}
	<nav
		id="mobile-nav"
		class="fixed inset-x-0 top-16 bottom-0 z-30 overflow-y-auto border-t border-line bg-paper px-4 pb-10"
		aria-label="Mobile navigation"
		transition:fly={{ y: -10, duration: reduced ? 0 : 220 }}
	>
		<p class="eyebrow pt-6 pb-2">Sections</p>
		<ul class="border-t border-line">
			{#each primaryLinks as link (link.href)}
				<li>
					<a
						class="flex items-center justify-between gap-4 py-4 border-b border-line font-display text-2xl text-ink"
						href={resolve(link.href)}
						aria-current={navAriaCurrent(link.href)}
					>
						{'label' in link && link.label.startsWith('words.')
							? $t(link.label as never)
							: link.label}
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="18"
							height="18"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="1.6"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="text-ink-subtle"
							><line x1="5" y1="12" x2="19" y2="12" /><polyline
								points="12 5 19 12 12 19"
							/></svg
						>
					</a>
				</li>
			{/each}
			{#each secondaryLinks as link (link.href)}
				<li>
					<a
						class={navMobileItemClass(link.href)}
						href={resolve(link.href)}
						aria-current={navAriaCurrent(link.href)}
					>
						{link.label}
					</a>
				</li>
			{/each}
			{#each adminLinks as link (link.href)}
				<li>
					<a
						class={navMobileItemClass(link.href)}
						href={resolve(link.href)}
						aria-current={navAriaCurrent(link.href)}
					>
						{link.label}
					</a>
				</li>
			{/each}
		</ul>

		<p class="eyebrow pt-8 pb-2">Account</p>
		<div class="border-t border-line">
			{#if $signedIn}
				<a
					class="flex items-center justify-between py-3.5 border-b border-line text-base text-ink-muted"
					href={resolve('/dashboard')}>{$t('words.dashboard')}</a
				>
				<a
					class="flex items-center justify-between py-3.5 border-b border-line text-base text-ink-muted"
					href={resolve('/api/v1/users/logout' as Pathname)}>{$t('words.logout')}</a
				>
			{:else}
				{#if !registration_disabled}
					<a
						class="flex items-center justify-between py-3.5 border-b border-line text-base text-ink-muted"
						href={resolve('/account/register')}>{$t('words.register')}</a
					>
				{/if}
				<a
					class="flex items-center justify-between py-3.5 border-b border-line text-base text-ink-muted"
					href={resolve('/account/login?returnTo=' + $pathname as Pathname)}>{$t('words.login')}</a
				>
			{/if}
			<a
				class="flex items-center justify-between py-3.5 border-b border-line text-base text-ink-muted"
				target="_blank"
				href={githubUrl}>GitHub <span aria-hidden="true">↗</span></a
			>
		</div>

		<div class="pt-8 flex items-center justify-between gap-4">
			<span class="eyebrow">Theme</span>
			<ThemeToggle />
		</div>
	</nav>
{/if}
