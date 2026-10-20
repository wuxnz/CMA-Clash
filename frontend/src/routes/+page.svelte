<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import { SITE_NAME, SITE_URL, DEFAULT_DESCRIPTION } from '$lib/site';
	import Button from '$lib/ui/Button.svelte';
	import HomePreviewQuestion from '$lib/landing/HomePreviewQuestion.svelte';
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { fade } from 'svelte/transition';

	const { t } = getLocalization();
	const reduced = prefersReducedMotion();
	navbarVisible.visible = true;

	const homeTitle = $derived(`${SITE_NAME}: ${$t('index_page.meta.title')}`);
	const homeDescription = DEFAULT_DESCRIPTION;
	const structuredData = $derived(
		JSON.stringify({
			'@context': 'https://schema.org',
			'@type': 'WebSite',
			name: SITE_NAME,
			url: SITE_URL,
			description: homeDescription,
			publisher: { '@type': 'Organization', name: SITE_NAME }
		})
	);

	let nextClash = $state(134);
	$effect(() => {
		if (reduced) return;
		const id = setInterval(() => {
			nextClash = nextClash > 0 ? nextClash - 1 : 134;
		}, 1000);
		return () => clearInterval(id);
	});
	let mm = $derived(String(Math.floor(nextClash / 60)).padStart(2, '0'));
	let ss = $derived(String(nextClash % 60).padStart(2, '0'));

</script>

<svelte:head>
	<title>{homeTitle}</title>
	<meta name="description" content={homeDescription} />
	<meta property="og:title" content={homeTitle} />
	<meta property="og:description" content={homeDescription} />
	<meta name="twitter:title" content={homeTitle} />
	<meta name="twitter:description" content={homeDescription} />
	{@html `<script type="application/ld+json">${structuredData}</script>`}
</svelte:head>

<div class="min-h-screen flex flex-col">
	<section
		class="relative px-4 min-h-[88vh] flex flex-col justify-center"
		aria-labelledby="home-hero-heading"
	>
		<div class="relative z-10 max-w-6xl mx-auto w-full grid lg:grid-cols-2 gap-12 items-center py-16">
			<div>
				<p
					class="text-sm text-ink-muted mb-4"
					in:fade={reduced ? { duration: 0 } : { duration: 300 }}
				>
					NHA CCMA exam prep
				</p>
				<h1
					id="home-hero-heading"
					class="font-display text-6xl sm:text-8xl text-ink leading-[0.85]"
				>
					Clash.
				</h1>
				<p class="mt-5 text-lg text-ink-muted max-w-md leading-relaxed">
					{$t('index_page.cma_hero_subtitle')}
				</p>
				<div class="mt-8 flex items-baseline gap-3">
					<span class="text-sm text-ink-muted">Next daily clash</span>
					<span class="font-display text-3xl text-gold tabular-nums leading-none">{mm}:{ss}</span>
				</div>
				<div class="mt-8 grid grid-cols-2 gap-3 sm:flex sm:flex-row sm:items-center">
					<Button href="/play" class="col-span-2 sm:col-auto w-full sm:w-auto"
						>{$t('words.play')}</Button
					>
					<Button href="/battle" variant="secondary" class="w-full sm:w-auto">Battle</Button>
					<Button href="/account/register" variant="secondary" class="w-full sm:w-auto"
						>{$t('words.register')}</Button
					>
				</div>
			</div>
			<HomePreviewQuestion />
		</div>
	</section>

	<section class="px-4 max-w-6xl mx-auto w-full pb-24">
		<h2 class="text-sm font-semibold text-ink mb-8">How it works</h2>
		<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-x-10 gap-y-8">
			<a href="/play" class="min-w-0 group">
				<h3 class="text-base font-semibold text-ink">Live quiz</h3>
				<p class="text-sm text-ink-muted mt-1 leading-relaxed transition-[color] duration-150 [@media(hover:hover)]:group-hover:text-ink">
					Host a session or join with a PIN.
				</p>
			</a>
			<a href="/practice" class="min-w-0 group">
				<h3 class="text-base font-semibold text-ink">Practice</h3>
				<p class="text-sm text-ink-muted mt-1 leading-relaxed transition-[color] duration-150 [@media(hover:hover)]:group-hover:text-ink">
					Drill questions against a timer.
				</p>
			</a>
			<a href="/battle" class="min-w-0 group">
				<h3 class="text-base font-semibold text-ink">Battle</h3>
				<p class="text-sm text-ink-muted mt-1 leading-relaxed transition-[color] duration-150 [@media(hover:hover)]:group-hover:text-ink">
					Compete one-on-one.
				</p>
			</a>
			<a href="/leaderboard" class="min-w-0 group">
				<h3 class="text-base font-semibold text-ink">Leaderboard</h3>
				<p class="text-sm text-ink-muted mt-1 leading-relaxed transition-[color] duration-150 [@media(hover:hover)]:group-hover:text-ink">
					Weekly XP standings.
				</p>
			</a>
		</div>
	</section>
</div>
<Footer />
