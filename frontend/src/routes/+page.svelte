<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import { SITE_NAME, SITE_URL, DEFAULT_DESCRIPTION } from '$lib/site';
	import RetentionBar from '$lib/ui/RetentionBar.svelte';
	import Card from '$lib/ui/Card.svelte';

	const { t } = getLocalization();

	navbarVisible.visible = true;

	const steps = [
		{
			title: $t('index_page.cma_step_study_title'),
			body: $t('index_page.cma_step_study_body'),
			href: '/dashboard'
		},
		{
			title: $t('index_page.cma_step_live_title'),
			body: $t('index_page.cma_step_live_body'),
			href: '/play'
		},
		{
			title: $t('index_page.cma_step_climb_title'),
			body: $t('index_page.cma_step_climb_body'),
			href: '/leaderboard'
		}
	];

	const pillars = [
		{ title: $t('index_page.cma_pillar_ledger'), body: $t('index_page.cma_pillar_ledger_body') },
		{ title: $t('index_page.cma_pillar_arena'), body: $t('index_page.cma_pillar_arena_body') },
		{ title: $t('index_page.cma_pillar_climb'), body: $t('index_page.cma_pillar_climb_body') }
	];

	const homeTitle = $derived(`${SITE_NAME} — ${$t('index_page.meta.title')}`);
	const homeDescription = DEFAULT_DESCRIPTION;
	const structuredData = $derived(
		JSON.stringify({
			'@context': 'https://schema.org',
			'@type': 'WebSite',
			name: SITE_NAME,
			url: SITE_URL,
			description: homeDescription,
			publisher: {
				'@type': 'Organization',
				name: SITE_NAME
			}
		})
	);
</script>

<svelte:head>
	<title>{homeTitle}</title>
	<meta name="description" content={homeDescription} />
	<meta property="og:title" content={homeTitle} />
	<meta property="og:description" content={homeDescription} />
	<meta name="twitter:title" content={homeTitle} />
	<meta name="twitter:description" content={homeDescription} />
	{@html `<script type="application/ld+json">${structuredData}</script>`}
</svelte:head>

<div class="min-h-screen flex flex-col">
	<section class="pb-16 px-4" aria-labelledby="home-hero-heading">
		<div class="pt-16 text-center max-w-3xl mx-auto">
			<h1 id="home-hero-heading" class="font-display sm:text-6xl text-5xl font-bold text-ink tracking-tight">
				CMA Clash
			</h1>
			<p class="text-lg sm:text-xl mt-4 text-ink-muted">
				{$t('index_page.cma_hero_subtitle')}
			</p>
			<div class="flex flex-wrap justify-center gap-3 mt-8">
				<a href="/play" class="ledger-btn-primary w-auto px-8">{$t('words.play')}</a>
				<a href="/battle" class="inline-flex items-center justify-center px-8 py-2.5 font-semibold rounded-lg border border-ink/20 bg-surface hover:bg-paper-muted transition"
					>Battle</a
				>
				<a
					href="/account/register"
					class="inline-flex items-center justify-center px-8 py-2.5 font-semibold rounded-lg border border-ink/20 bg-surface hover:bg-paper-muted transition"
					>{$t('words.register')}</a
				>
			</div>
			<div class="mt-10 flex justify-center">
				<RetentionBar
					streakDays={0}
					dailyGoalPercent={0}
					leagueName="Weekly league"
					leagueIsDemo={true}
				/>
			</div>
		</div>
	</section>

	<section class="px-4 max-w-5xl mx-auto w-full pb-16">
		<h2 class="font-display text-3xl sm:text-4xl font-bold text-center text-ink mb-10">
			{$t('index_page.how_cma_clash_works')}
		</h2>
		<div class="grid md:grid-cols-3 gap-6">
			{#each steps as step, i}
				<Card padding="lg" class="flex flex-col h-full">
					<span class="font-mono text-primary text-sm mb-2">0{i + 1}</span>
					<h3 class="font-display text-xl font-semibold text-ink mb-2">{step.title}</h3>
					<p class="text-ink-muted text-sm flex-1">{step.body}</p>
					<a href={step.href} class="mt-4 text-primary font-medium text-sm hover:underline"
						>{$t('words.get_started')} →</a
					>
				</Card>
			{/each}
		</div>
	</section>

	<section class="px-4 max-w-5xl mx-auto w-full pb-20">
		<h2 class="font-display text-2xl font-bold text-center text-ink mb-8">
			{$t('index_page.why_cma_clash')}
		</h2>
		<div class="grid md:grid-cols-3 gap-4">
			{#each pillars as pillar}
				<div class="rounded-xl border border-ink/10 bg-surface p-5">
					<h3 class="font-display font-semibold text-ink">{pillar.title}</h3>
					<p class="text-sm text-ink-muted mt-2">{pillar.body}</p>
				</div>
			{/each}
		</div>
		<p class="text-center text-sm text-ink-muted mt-10 max-w-2xl mx-auto">
			{$t('index_page.stats', { user_count: '—', quiz_count: '—' })}
		</p>
	</section>
</div>
<Footer />
