<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->
<script lang="ts">
	import PageHeader from '$lib/ui/PageHeader.svelte';
	import { resolve } from '$app/paths';
	import type { Pathname } from '$app/types';
</script>

<svelte:head>
	<title>CMA Clash: docs - Index</title>
	<meta
		name="description"
		content="The overview about the docs for CMA Clash, the open-source quiz-application"
	/>
</svelte:head>

<div class="w-full max-w-4xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 lg:pt-20 pb-24">
	<PageHeader
		eyebrow="Documentation"
		title="How it"
		accent="all works."
		lede="Setup guides, feature documentation and the roadmap for CMA Clash — the open-source quiz platform."
		meta="Open source"
	/>

	<nav class="border-t border-line" aria-label="Docs index">
		{#each [{ href: '/docs/roadmap', label: 'Roadmap', note: 'What is shipping next.' }, { href: '/docs/import-from-kahoot', label: 'Import from Kahoot', note: 'Move an existing deck across in minutes.' }, { href: '/docs/self-host', label: 'Self-hosting', note: 'Run the whole platform yourself.' }, { href: '/docs/develop', label: 'Development setup', note: 'Local environment and contribution flow.' }, { href: '/docs/features', label: 'Features', note: 'Every mode, explained in depth.' }] as doc, i (doc.href)}
			<a
					href={resolve(doc.href as Pathname)}
				class="group flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-1 sm:gap-6 py-5 border-b border-line transition-colors duration-300 hover:bg-primary-soft px-2 -mx-2"
			>
				<span class="flex items-baseline gap-4">
					<span class="font-mono text-[0.66rem] tracking-[0.2em] text-primary"
						>{String(i + 1).padStart(2, '0')}</span
					>
					<span class="font-display text-xl sm:text-2xl text-ink">{doc.label}</span>
				</span>
				<span class="text-sm text-ink-muted sm:text-right pl-8 sm:pl-0">{doc.note}</span>
			</a>
		{/each}
	</nav>

	<div class="mt-12 border border-line bg-paper p-6 sm:p-8">
		<p class="eyebrow">Open source</p>
		<p class="text-ink-muted leading-relaxed mt-3 max-w-[60ch]">
			CMA Clash is open source and self-hostable. Read the
				<a href={resolve('/docs/develop')} class="text-ink link-hover">development setup</a> to run it
			locally, or browse the
			<a href="https://github.com/wuxnz/CMA-Clash" class="text-ink link-hover" target="_blank"
				>repository</a
			> to contribute.
		</p>
	</div>
</div>
