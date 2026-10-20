<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import '../app.css';
	import Navbar from '$lib/navbar.svelte';
	import { pathname } from '$lib/stores';
	import { navbarVisible } from '$lib/stores.svelte';

	import { initLocalizationContext } from '$lib/i18n';
	import { browser } from '$app/environment';
	import CommandPalette from '$lib/components/commandpalette.svelte';
	import { plausible_data_url } from '$lib/config';
	import { page } from '$app/state';
	import { SITE_NAME, OG_IMAGE_URL, canonicalUrl } from '$lib/site';
	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();

	if (browser) {
		pathname.set(window.location.pathname);
		document.documentElement.classList.add('dark');
		import('lenis').then(({ default: Lenis }) => {
			if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
			const lenis = new Lenis({ smoothWheel: true });
			const raf = (time: number) => {
				lenis.raf(time);
				requestAnimationFrame(raf);
			};
			requestAnimationFrame(raf);
		});
	}
	let start_language = 'en';
	const rtl_languages = ['he', 'prs', 'ps'];
	if (browser) {
		start_language = localStorage.getItem('language') ?? 'en';
		document.documentElement.lang = start_language;
		document.documentElement.dir = rtl_languages.includes(start_language) ? 'rtl' : 'ltr';
	}
	initLocalizationContext(start_language);

	const pageCanonical = $derived(canonicalUrl(page.url.pathname));
</script>

<svelte:head>
	<!-- Site-wide tags; robots noindex/nofollow lives in app.html. Pages set title/description. -->
	<link rel="canonical" href={pageCanonical} />
	<meta property="og:site_name" content={SITE_NAME} />
	<meta property="og:url" content={pageCanonical} />
	<meta property="og:type" content="website" />
	<meta property="og:image" content={OG_IMAGE_URL} />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta property="og:image:alt" content="{SITE_NAME}: CCMA and allied health exam prep" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content={OG_IMAGE_URL} />
	{#if plausible_data_url}
		<script
			defer
			data-domain={plausible_data_url}
			src="https://plausible.io/js/script.file-downloads.outbound-links.pageview-props.tagged-events.js"
		></script>
		<script>
			window.plausible =
				window.plausible ||
				function () {
					(window.plausible.q = window.plausible.q || []).push(arguments);
				};
		</script>
	{/if}
</svelte:head>

<a class="skip-link" href="#main-content">Skip to main content</a>
{#if navbarVisible.visible}
	<Navbar />
	<div class="pt-16">
		<div class="z-40"></div>
	</div>
{/if}
<main id="main-content">
	{@render children?.()}
</main>

<CommandPalette />

<style>
	.skip-link {
		position: absolute;
		left: -9999px;
		top: auto;
		width: 1px;
		height: 1px;
		overflow: hidden;
		z-index: 100;
		padding: 0.75rem 1rem;
		background: #0f2702;
		color: #fff;
		font-weight: 600;
		text-decoration: none;
		border-radius: 0.25rem;
	}

	.skip-link:focus {
		position: fixed;
		left: 1rem;
		top: 1rem;
		width: auto;
		height: auto;
		overflow: visible;
	}
</style>
