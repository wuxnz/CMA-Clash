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
</script>

<svelte:head>
	<title>CMA Clash: Study guides</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Study guides</h1>
		<p class="text-sm text-ink-muted mt-2 max-w-2xl">
			Topic summaries with links to official sources. Pair with practice sets on Explore.
		</p>

		{#if loading}
			<p class="text-sm text-ink-muted mt-8" aria-busy="true">Loading topics…</p>
		{:else if withStudy.length === 0}
			<p class="text-sm text-ink-muted mt-8">No study guides are available yet.</p>
		{:else}
			<ul class="mt-8 divide-y divide-white/[0.07]">
				{#each withStudy as topic (topic.slug)}
					<li>
						<a
							href="/study/{topic.slug}"
							class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 py-4 min-h-11 link-hover"
						>
							<span class="text-sm font-medium text-ink">{topic.name}</span>
							<span class="text-xs text-ink-muted">{certName(topic.certification_id)}</span>
						</a>
					</li>
				{/each}
			</ul>
		{/if}
	</div>
	<Footer />
</div>
