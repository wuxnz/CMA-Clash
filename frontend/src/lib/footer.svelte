<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import LanguageToggle from './language-toggle.svelte';
	import { getLocalization } from '$lib/i18n';

	const { t } = getLocalization();
</script>

<footer class="mt-auto border-t border-ink/10 bg-ink text-paper w-full">
	<div class="max-w-6xl mx-auto px-4 py-8 flex flex-col md:flex-row items-center justify-between gap-4">
		<div class="text-center md:text-left">
			<p class="font-display font-semibold text-lg">CMA Clash</p>
			<p class="text-sm text-paper/70 mt-1">Gamified CMA exam prep — live quizzes &amp; leaderboards</p>
		</div>
		<div class="flex flex-wrap items-center justify-center gap-4 text-sm">
			<a href="/docs" class="text-paper/80 hover:text-gold transition">{$t('words.docs')}</a>
			<a href="/docs/attribution" class="text-paper/80 hover:text-gold transition"
				>{$t('words.other', { count: 2 })}</a
			>
			<a href="/docs/privacy-policy" class="text-paper/80 hover:text-gold transition"
				>Privacy</a
			>
		</div>
		<LanguageToggle />
	</div>
	<p class="text-center text-xs text-paper/50 pb-4 px-4">
		Built on open-source quiz technology.
		<a href="/docs/attribution" class="underline hover:text-gold">Attribution</a>
	</p>
</footer>
