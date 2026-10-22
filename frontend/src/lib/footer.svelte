<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { resolve } from '$app/paths';
	import LanguageToggle from './language-toggle.svelte';
</script>

<footer class="mt-auto border-t border-line bg-paper text-ink w-full">
	<div
		class="max-w-6xl mx-auto px-4 sm:px-8 py-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6 min-w-0"
	>
		<div class="text-left min-w-0">
			<p class="font-display text-xl">
				CMA <em class="italic font-normal text-primary">Clash</em>
			</p>
			<p class="eyebrow mt-2">Gamified CMA exam prep</p>
		</div>
		<nav
			class="flex flex-wrap items-center justify-start gap-x-6 gap-y-1 text-sm"
			aria-label="Footer"
		>
			<a href={resolve('/docs')} class="min-h-11 inline-flex items-center text-ink-muted link-hover"
				>Docs</a
			>
			<a
				href={resolve('/docs/privacy-policy')}
				class="min-h-11 inline-flex items-center text-ink-muted link-hover">Privacy</a
			>
			<a
				href={resolve('/docs/attribution')}
				class="min-h-11 inline-flex items-center text-ink-muted link-hover">Attribution</a
			>
		</nav>
		<LanguageToggle />
	</div>
</footer>
