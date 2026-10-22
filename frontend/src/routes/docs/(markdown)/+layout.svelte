<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { onMount } from 'svelte';
	import '$lib/hljs.css';
	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();

	onMount(async () => {
		const { default: hljs } = await import('highlight.js/lib/common');
		hljs.highlightAll();
	});
</script>

<article
	class="dsg-doc prose prose-sm sm:prose lg:prose-lg mx-auto mt-10 w-full max-w-3xl px-4 sm:px-8"
>
	{@render children?.()}
</article>

<style>
	:global(.dsg-doc) {
		--tw-prose-body: var(--color-ink-muted);
		--tw-prose-headings: var(--color-ink);
		--tw-prose-lead: var(--color-ink-2);
		--tw-prose-links: var(--color-primary);
		--tw-prose-bold: var(--color-ink);
		--tw-prose-counters: var(--color-ink-subtle);
		--tw-prose-bullets: var(--color-primary);
		--tw-prose-hr: var(--color-line);
		--tw-prose-quotes: var(--color-ink);
		--tw-prose-quote-borders: var(--color-primary);
		--tw-prose-captions: var(--color-ink-subtle);
		--tw-prose-code: var(--color-ink);
		--tw-prose-pre-code: var(--color-ink);
		--tw-prose-pre-bg: var(--color-surface);
		--tw-prose-th-borders: var(--color-line-strong);
		--tw-prose-td-borders: var(--color-line);
	}

	:global(.dsg-doc h1),
	:global(.dsg-doc h2),
	:global(.dsg-doc h3) {
		font-family: var(--font-display);
		letter-spacing: -0.03em;
		text-transform: none;
	}

	:global(.dsg-doc h1) {
		font-size: 2.4rem;
		line-height: 1.02;
	}

	:global(.dsg-doc h2) {
		font-size: 1.6rem;
		margin-top: 2.2em;
		padding-top: 0.6em;
		border-top: 1px solid var(--color-line);
	}

	:global(.dsg-doc a) {
		text-decoration-color: color-mix(in oklch, var(--color-primary) 50%, transparent);
		text-underline-offset: 3px;
	}

	:global(.dsg-doc a:hover) {
		text-decoration-color: var(--color-primary);
	}

	:global(.dsg-doc code) {
		background: var(--color-elevated);
		padding: 0.15em 0.35em;
		border-radius: 2px;
	}

	:global(.dsg-doc pre) {
		border: 1px solid var(--color-line);
		border-radius: 0;
	}
</style>
