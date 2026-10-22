<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { resolve } from '$app/paths';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import { onMount } from 'svelte';
	import { SvelteURLSearchParams } from 'svelte/reactivity';
	import type { PageData } from './$types';
	import type { Certification, Topic } from '$lib/cma/client';
	import { CERT_FILTERS } from '$lib/quiz/labels';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	let topics = $state<Topic[]>([]);
	let certs = $state<Certification[]>([]);
	let cert = $state(data.cert);
	let loading = $state(true);

	const withStudy = $derived(
		topics.filter((t) => Array.isArray(t.study_content) && t.study_content.length > 0)
	);

	const certId = $derived(cert ? (certs.find((c) => c.slug === cert)?.id ?? null) : null);
	const visibleTopics = $derived(
		certId ? withStudy.filter((t) => t.certification_id === certId) : withStudy
	);

	function setCert(slug: string) {
		cert = slug;
		const params = new SvelteURLSearchParams();
		if (cert) params.set('cert', cert);
		const qs = params.toString();
		history.replaceState(null, '', qs ? `?${qs}` : location.pathname);
	}

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

		<div
			class="chip-row -mx-4 px-4 sm:mx-0 sm:px-0 mt-6"
			role="tablist"
			aria-label="Certification"
		>
			{#each CERT_FILTERS as item (item.slug)}
				<button
					type="button"
					role="tab"
					aria-selected={cert === item.slug}
					class="chip {cert === item.slug ? 'chip-active' : ''}"
					onclick={() => setCert(item.slug)}
				>
					{item.label}
				</button>
			{/each}
		</div>

		{#if loading}
			<p class="text-sm text-ink-muted mt-8" aria-busy="true">Loading topics…</p>
		{:else if withStudy.length === 0}
			<p class="text-sm text-ink-muted mt-8">No study guides are available yet.</p>
		{:else if visibleTopics.length === 0}
			<div data-empty-study class="mt-8">
				<p class="text-sm text-ink">No study guides for this filter.</p>
				<button
					type="button"
					class="text-sm text-ink link-hover min-h-11"
					onclick={() => setCert('')}
				>
					Clear filter
				</button>
			</div>
		{:else}
			<ul class="mt-4 divide-y divide-line">
				{#each visibleTopics as topic (topic.slug)}
					<li>
						<a
							href={resolve('/study/[topic_slug]', { topic_slug: topic.slug })}
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
