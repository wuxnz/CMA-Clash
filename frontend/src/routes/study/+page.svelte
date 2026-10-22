<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import { onMount } from 'svelte';
	import type { Certification, Topic } from '$lib/cma/client';

	navbarVisible.visible = true;

	let topics = $state<Topic[]>([]);
	let certs = $state<Certification[]>([]);
	let loading = $state(true);

	const withStudy = $derived(
		topics.filter((t) => Array.isArray(t.study_content) && t.study_content.length > 0)
	);

	onMount(async () => {
		try {
			const [certRes, topicRes] = await Promise.all([
				fetch('/api/v1/clash/certifications'),
				fetch('/api/v1/clash/topics')
			]);
			if (certRes.ok) certs = await certRes.json();
			if (topicRes.ok) topics = await topicRes.json();
		} finally {
			loading = false;
		}
	});

	function certName(id: string | null | undefined): string {
		if (!id) return '';
		return certs.find((c) => c.id === id)?.name ?? '';
	}

	function sectionCount(topic: Topic): number {
		return Array.isArray(topic.study_content) ? topic.study_content.length : 0;
	}
</script>

<svelte:head>
	<title>CMA Clash: Study guides</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 pb-20 min-w-0">
		<div class="border-b border-line pb-6">
			<p class="eyebrow">Library</p>
			<h1
				class="font-display text-[clamp(2.2rem,6vw,4rem)] leading-[0.92] tracking-[-0.04em] mt-3"
			>
				Study <b class="font-normal text-primary">guides</b>
			</h1>
			<p class="text-ink-muted mt-4 max-w-2xl leading-relaxed">
				Topic summaries with links to official sources. Pair with practice sets on Explore.
			</p>
		</div>

		{#if loading}
			<p class="text-sm text-ink-muted mt-8" aria-busy="true">Loading topics…</p>
		{:else if withStudy.length === 0}
			<p class="text-sm text-ink-muted mt-8">No study guides are available yet.</p>
		{:else}
			<ul class="mt-4 divide-y divide-line">
				{#each withStudy as topic (topic.slug)}
					<li>
						<a
							href="/study/{topic.slug}"
							class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 py-5 min-h-11 link-hover transition-colors hover:bg-elevated px-2 -mx-2"
						>
							<span class="font-display text-lg sm:text-xl text-ink"
								>{topic.name}</span
							>
							<span class="flex items-center gap-3 text-xs text-ink-muted">
								<span>{sectionCount(topic)} sections</span>
								<span class="eyebrow">{certName(topic.certification_id)}</span>
							</span>
						</a>
					</li>
				{/each}
			</ul>
		{/if}
	</div>
	<Footer />
</div>
