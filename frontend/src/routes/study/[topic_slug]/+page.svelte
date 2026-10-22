<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import Button from '$lib/ui/Button.svelte';
	import type { QuizBrowseItem, StudyBlock, Topic } from '$lib/cma/client';
	import { onMount } from 'svelte';
	import { page } from '$app/state';

	navbarVisible.visible = true;

	const slug = $derived(page.params.topic_slug);

	let topic = $state<Topic | null>(null);
	let quizzes = $state<QuizBrowseItem[]>([]);
	let loading = $state(true);
	let notFound = $state(false);

	const blocks = $derived((topic?.study_content ?? []) as StudyBlock[]);

	onMount(async () => {
		try {
			const topicRes = await fetch(`/api/v1/clash/topics/${slug}`);
			if (topicRes.status === 404) {
				notFound = true;
				return;
			}
			if (topicRes.ok) topic = await topicRes.json();
			const quizRes = await fetch(`/api/v1/clash/quizzes?topic_slug=${encodeURIComponent(slug)}&page_size=50`);
			if (quizRes.ok) quizzes = await quizRes.json();
		} finally {
			loading = false;
		}
	});
</script>

<svelte:head>
	<title>CMA Clash: Study {topic?.name ?? 'topic'}</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-3xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<p class="text-sm text-ink-muted">
			<a href="/study" class="link-hover text-ink-muted">Study guides</a>
		</p>

		{#if loading}
			<p class="text-sm text-ink-muted mt-6" aria-busy="true">Loading…</p>
		{:else if notFound || !topic}
			<h1 class="text-xl font-semibold text-ink mt-4">Topic not found</h1>
			<Button href="/study" class="w-auto mt-6">Back to study guides</Button>
		{:else}
			<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight mt-4">{topic.name}</h1>

			{#if blocks.length === 0}
				<p class="text-sm text-ink-muted mt-4">No study notes for this topic yet.</p>
			{:else}
				<div class="mt-8 space-y-8">
					{#each blocks as block (block.title)}
						<section>
							<div class="flex flex-wrap items-baseline gap-x-3 gap-y-1">
								<h2 class="text-sm font-semibold text-ink">{block.title}</h2>
								{#if block.source}
									<span class="text-xs text-ink-muted">{block.source}</span>
								{/if}
							</div>
							<p class="text-sm text-ink-muted mt-2 leading-relaxed">{block.summary}</p>
							{#if block.bullets && block.bullets.length > 0}
								<ul class="mt-3 space-y-1.5">
									{#each block.bullets as bullet (bullet)}
										<li class="flex gap-2 text-sm text-ink-muted leading-relaxed">
											<span aria-hidden="true" class="text-primary select-none">—</span>
											<span>{bullet}</span>
										</li>
									{/each}
								</ul>
							{/if}
							<p class="mt-2">
								<a
									class="text-sm text-ink link-hover break-all"
									href={block.url}
									target="_blank"
									rel="noreferrer"
								>
									{block.url}
								</a>
							</p>
						</section>
					{/each}
				</div>
			{/if}

			<section class="mt-12">
				<h2 class="text-sm font-semibold text-ink">Practice sets</h2>
				{#if quizzes.length === 0}
					<p class="text-sm text-ink-muted mt-2">Quizzes will appear after the content seed runs.</p>
				{:else}
					<ul class="mt-3 divide-y divide-white/[0.07]">
						{#each quizzes as quiz (quiz.id)}
							<li>
								<a
									href="/view/{quiz.id}"
									class="flex items-center justify-between gap-3 py-3 min-h-11 text-sm text-ink link-hover"
								>
									<span>{quiz.title}</span>
									<span class="text-xs text-ink-muted tabular-nums">{quiz.question_count} questions</span>
								</a>
							</li>
						{/each}
					</ul>
				{/if}
				<div class="mt-6 flex flex-wrap gap-3">
					<Button href="/explore">Explore</Button>
					{#if quizzes[0]}
						<Button variant="secondary" href="/practice?quiz_id={quizzes[0].id}">Practice</Button>
					{/if}
				</div>
			</section>
		{/if}
	</div>
	<Footer />
</div>
