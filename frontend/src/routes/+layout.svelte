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
	import {
		SITE_NAME,
		SITE_URL,
		DEFAULT_DESCRIPTION,
		OG_IMAGE_URL,
		canonicalUrl
	} from '$lib/site';
	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();

	if (browser) {
		pathname.set(window.location.pathname);
		if (
			localStorage.theme === 'dark' ||
			(!('theme' in localStorage) &&
				window.matchMedia('(prefers-color-scheme: dark)').matches)
		) {
			document.documentElement.classList.add('dark');
		} else {
			document.documentElement.classList.remove('dark');
		}
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
	<meta name="robots" content="noindex, nofollow" />
	<link rel="canonical" href={pageCanonical} />
	<meta property="og:site_name" content={SITE_NAME} />
	<meta property="og:url" content={pageCanonical} />
	<meta property="og:type" content="website" />
	<meta property="og:image" content={OG_IMAGE_URL} />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content={OG_IMAGE_URL} />
	<meta name="description" content={DEFAULT_DESCRIPTION} />
	<meta property="og:description" content={DEFAULT_DESCRIPTION} />
	<meta name="twitter:description" content={DEFAULT_DESCRIPTION} />
	{#if plausible_data_url}
		<script
			defer
			data-domain={plausible_data_url}
			src="https://plausible.nexus.mawoka.eu/js/script.file-downloads.outbound-links.pageview-props.tagged-events.js"
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

<style lang="scss">
	:global(html:not(.dark)) {
		// height: 100%;
		// width: 100%;

		// bg-gradient-to-r from-[#009444] via-[#39b54a] to-[#8dc63f]
		//background: linear-gradient(to right, #009444, #39b54a, #8dc63f) repeat-y;
		background-color: #d6edc9;
		background-size: cover;
		/*background: linear-gradient(-225deg, #231557 0%, #44107A 29%, #FF1361 67%, #FFF800 100%); */
		/*background: linear-gradient(-225deg, #22E1FF 0%, #1D8FE1 48%, #625EB1 100%); */
		color: black;

		// background-size: 400% 400%;

		//animation: background_animation 5s ease infinite;
	}

	:global(html.dark) {
		//background-color: #0f2702;
		background-color: #4e6e58;
		background-size: cover;
		color: white;

		:global(#pips-slider) {
			--pip: white;
			--pip-active: white;
		}
	}

	@keyframes background_animation {
		0% {
			background-position: 0% 50%;
		}
		50% {
			background-position: 100% 50%;
		}
		100% {
			background-position: 0% 50%;
		}
	}

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
