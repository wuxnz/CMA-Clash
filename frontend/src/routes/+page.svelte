<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import JpgOpenGraph from '$lib/assets/landing/opengraph-home.jpg';
	import RetentionBar from '$lib/ui/RetentionBar.svelte';
	import Card from '$lib/ui/Card.svelte';
	import AuroraShader from '$lib/ui/AuroraShader.svelte';
	import GrainOverlay from '$lib/ui/GrainOverlay.svelte';
	import { fade, fly } from 'svelte/transition';
	import { prefersReducedMotion } from '$lib/ui/motion';

	const { t } = getLocalization();
	const reduced = prefersReducedMotion();

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

	const bento = [
		{
			title: 'CCMA question banks',
			body: 'Seeded NHA CCMA, clinical skills, phlebotomy, EKG, and BLS practice sets.',
			span: 'md:col-span-2'
		},
		{
			title: 'Live arena',
			body: 'PIN lobbies, timed questions, and battle VS intros.',
			span: ''
		},
		{
			title: 'Streaks & leagues',
			body: 'XP, weekly boards, and topic mastery heatmaps.',
			span: ''
		},
		{
			title: 'Accessible by design',
			body: 'Shape + color answers, reduced-motion paths, WCAG AA contrast.',
			span: 'md:col-span-2'
		}
	];
</script>

<svelte:head>
	<title>CMA-Clash — {$t('index_page.meta.title')}</title>
	<meta
		name="description"
		content="Gamified medical assistant exam prep (NHA CCMA) with live quizzes, battles, and leaderboards."
	/>
	<meta property="og:title" content="CMA-Clash — {$t('index_page.meta.title')}" />
	<meta
		property="og:description"
		content="Gamified medical assistant exam prep with live quizzes, multiplayer battles, and leaderboards."
	/>
	<meta property="og:image" content={JpgOpenGraph} />
</svelte:head>

<div class="min-h-screen flex flex-col">
	<section class="relative overflow-hidden pb-20 px-4 min-h-[85vh] flex flex-col justify-center">
		<AuroraShader class="z-0" />
		<GrainOverlay />
		<div class="relative z-10 pt-20 text-center max-w-4xl mx-auto">
			{#if !reduced}
				<p
					class="text-xs uppercase tracking-[0.35em] text-primary mb-4"
					in:fade={{ duration: 500 }}
				>
					NHA CCMA · Clinical skills
				</p>
			{/if}
			<h1
				class="font-display sm:text-7xl text-5xl font-bold tracking-tight gradient-text"
				in:fly={reduced ? { duration: 0 } : { y: 24, duration: 600 }}
			>
				CMA-Clash
			</h1>
			<p
				class="text-lg sm:text-xl mt-6 text-ink-muted max-w-2xl mx-auto"
				in:fly={reduced ? { duration: 0 } : { y: 20, delay: 100, duration: 600 }}
			>
				{$t('index_page.cma_hero_subtitle')}
			</p>
			<div
				class="flex flex-wrap justify-center gap-3 mt-10"
				in:fly={reduced ? { duration: 0 } : { y: 16, delay: 180, duration: 600 }}
			>
				<a href="/play" class="ledger-btn-primary w-auto px-10">{$t('words.play')}</a>
				<a
					href="/battle"
					class="inline-flex items-center justify-center px-8 py-2.5 font-semibold rounded-lg glass-panel hover:border-primary/40 transition"
					>Battle</a
				>
				<a
					href="/account/register"
					class="inline-flex items-center justify-center px-8 py-2.5 font-semibold rounded-lg glass-panel hover:border-primary/40 transition"
					>{$t('words.register')}</a
				>
			</div>
			<div class="mt-12 flex justify-center">
				<RetentionBar
					streakDays={0}
					dailyGoalPercent={0}
					leagueName="Weekly league"
					leagueIsDemo={true}
				/>
			</div>
		</div>
	</section>

	<section class="px-4 max-w-6xl mx-auto w-full pb-20">
		<h2 class="font-display text-3xl sm:text-4xl font-bold text-center text-ink mb-4">
			{$t('index_page.how_cma_clash_works')}
		</h2>
		<p class="text-center text-ink-muted text-sm mb-10 max-w-xl mx-auto">
			Built for certified medical assistant prep — not accounting CMA.
		</p>
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

	<section class="px-4 max-w-6xl mx-auto w-full pb-24">
		<h2 class="font-display text-2xl font-bold text-center text-ink mb-8">Platform</h2>
		<div class="grid md:grid-cols-3 gap-4 auto-rows-fr">
			{#each bento as item}
				<div class="glass-panel rounded-2xl p-6 {item.span}">
					<h3 class="font-display font-semibold text-ink">{item.title}</h3>
					<p class="text-sm text-ink-muted mt-2">{item.body}</p>
				</div>
			{/each}
		</div>
	</section>
</div>
<Footer />
