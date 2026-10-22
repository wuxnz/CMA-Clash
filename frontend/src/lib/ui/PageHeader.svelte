<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { reveal, maskLines } from '$lib/motion/editorial';

	interface Props {
		/** Small mono label above the title. */
		eyebrow: string;
		/** Main display title. */
		title: string;
		/** Optional trailing word rendered in accent italic. */
		accent?: string;
		/** Supporting sentence under the title. */
		lede?: string;
		/** Right-hand meta line, e.g. a build number. */
		meta?: string;
		/** Optional action row under the lede. */
		actions?: import('svelte').Snippet;
	}

	let { eyebrow, title, accent, lede, meta, actions }: Props = $props();
</script>

<header class="mb-10 lg:mb-14">
	<div
		class="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-4 border-b border-line pb-5"
	>
		<p class="eyebrow" use:reveal>{eyebrow}</p>
		{#if meta}
			<p class="eyebrow lg:text-right" use:reveal={{ delay: 0.08 }}>{meta}</p>
		{/if}
	</div>

	<h1 class="headline text-[clamp(2.2rem,6vw,4.4rem)] mt-6 lg:mt-8">
		<span class="block" use:maskLines>{title}</span>
		{#if accent}
			<span class="block" use:maskLines={{ delay: 0.08 }}>
				<em class="accent-italic">{accent}</em>
			</span>
		{/if}
	</h1>

	{#if lede}
		<p
			class="text-ink-muted leading-relaxed max-w-[52ch] mt-5 text-base sm:text-lg"
			use:reveal={{ delay: 0.14 }}
		>
			{lede}
		</p>
	{/if}

	{#if actions}
		<div class="mt-7" use:reveal={{ delay: 0.2 }}>
			{@render actions()}
		</div>
	{/if}
</header>
