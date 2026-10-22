<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { reveal, maskLines } from '$lib/motion/editorial';

	interface Props {
		eyebrow: string;
		title: string;
		accent?: string;
		lede?: string;
		/** Numbered supporting points shown under the statement. */
		points?: { label: string; body: string }[];
		/** The form / card body. */
		children?: import('svelte').Snippet;
	}

	let { eyebrow, title, accent, lede, points = [], children }: Props = $props();
</script>

<div
	class="w-full max-w-6xl mx-auto px-4 sm:px-8 lg:px-12 py-14 lg:py-20 grid lg:grid-cols-2 gap-10 lg:gap-16 items-start"
>
	<aside class="min-w-0">
		<p class="eyebrow" use:reveal>{eyebrow}</p>
		<h1 class="headline text-[clamp(2.2rem,6vw,4.2rem)] mt-5">
			<span class="block" use:maskLines>{title}</span>
			{#if accent}
				<span class="block" use:maskLines={{ delay: 0.08 }}>
					<em class="accent-italic">{accent}</em>
				</span>
			{/if}
		</h1>

		{#if lede}
			<p
				class="text-ink-muted leading-relaxed mt-5 max-w-[46ch]"
				use:reveal={{ delay: 0.14 }}
			>
				{lede}
			</p>
		{/if}

		{#if points.length}
			<ul class="mt-8 border-t border-line" use:reveal={{ delay: 0.2 }}>
				{#each points as point, i (point.label)}
					<li class="py-4 border-b border-line">
						<div class="flex items-baseline gap-4">
							<span class="font-mono text-[0.66rem] tracking-[0.2em] text-primary"
								>{String(i + 1).padStart(2, '0')}</span
							>
							<span class="text-sm font-medium text-ink">{point.label}</span>
						</div>
						<p class="text-sm text-ink-muted leading-relaxed mt-1.5 pl-8">
							{point.body}
						</p>
					</li>
				{/each}
			</ul>
		{/if}
	</aside>

	<div class="min-w-0" use:reveal={{ delay: 0.1, y: 26 }}>
		<div class="border border-line bg-paper">
			{@render children?.()}
		</div>
	</div>
</div>
