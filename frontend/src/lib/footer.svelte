<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import LanguageToggle from './language-toggle.svelte';
</script>

<footer class="mt-auto border-t border-white/5 bg-paper text-ink w-full">
	<div class="max-w-6xl mx-auto px-4 py-8 flex flex-col md:flex-row items-center justify-between gap-4 min-w-0">
		<div class="text-center md:text-left min-w-0">
			<p class="text-sm font-semibold text-ink">CMA Clash</p>
			<p class="text-sm text-ink-muted mt-1">Gamified CMA exam prep</p>
		</div>
		<nav class="flex flex-wrap items-center justify-center gap-x-4 gap-y-1 text-sm" aria-label="Footer">
			<a href="/docs" class="min-h-11 inline-flex items-center text-ink-muted link-hover">Docs</a>
			<a href="/docs/privacy-policy" class="min-h-11 inline-flex items-center text-ink-muted link-hover">Privacy</a>
			<a href="/docs/attribution" class="min-h-11 inline-flex items-center text-ink-muted link-hover">Attribution</a>
		</nav>
		<LanguageToggle />
	</div>
</footer>
