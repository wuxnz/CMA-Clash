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
	import BentoSpotlightCard from '$lib/ui/BentoSpotlightCard.svelte';
	import MagneticButton from '$lib/ui/MagneticButton.svelte';
	import AuroraShader from '$lib/ui/AuroraShader.svelte';
	import GrainOverlay from '$lib/ui/GrainOverlay.svelte';
	import { fade, fly } from 'svelte/transition';
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { scrollReveal } from '$lib/motion/scrollReveal';
	import { scrollParallax } from '$lib/motion/parallax';
	import { BookOpen, Radio, Trophy, Sparkles, HeartPulse, Swords, Shield } from '@lucide/svelte';

	const { t } = getLocalization();
	const reduced = prefersReducedMotion();

	navbarVisible.visible = true;

	const steps = [
		{
			icon: BookOpen,
			title: $t('index_page.cma_step_study_title'),
			body: $t('index_page.cma_step_study_body'),
			href: '/dashboard',
			span: 'md:col-span-2 md:row-span-2'
		},
		{
			icon: Radio,
			title: $t('index_page.cma_step_live_title'),
			body: $t('index_page.cma_step_live_body'),
			href: '/play',
			span: ''
		},
		{
			icon: Trophy,
			title: $t('index_page.cma_step_climb_title'),
			body: $t('index_page.cma_step_climb_body'),
			href: '/leaderboard',
			span: ''
		},
		{
			icon: Sparkles,
			title: 'Streaks & mastery',
			body: 'Daily goals, XP counters, and topic heatmaps on your dashboard.',
			href: '/dashboard',
			span: 'md:col-span-2'
		}
	];

	const platform = [
		{
			icon: HeartPulse,
			title: 'CCMA question banks',
			body: 'Seeded NHA CCMA, clinical skills, phlebotomy, EKG, and BLS practice sets.',
			span: 'md:col-span-2'
		},
		{
			icon: Swords,
			title: 'Live arena',
			body: 'PIN lobbies, timed questions, and battle VS intros.',
			span: ''
		},
		{
			icon: Shield,
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
		<div
			class="relative z-10 pt-20 text-center max-w-4xl mx-auto"
			use:scrollParallax={reduced ? undefined : { speed: 0.2 }}
		>
			{#if !reduced}
				<p
					class="text-xs uppercase tracking-[0.35em] text-primary mb-4"
					in:fade={{ duration: 500 }}
				>
					NHA CCMA · Clinical skills
				</p>
			{/if}
			<h1
				class="font-display sm:text-7xl text-5xl font-bold tracking-[-0.04em] gradient-text"
				in:fly={reduced ? { duration: 0 } : { y: 24, duration: 600 }}
			>
				CMA-Clash
			</h1>
			<p
				class="text-lg sm:text-xl mt-6 text-ink-muted max-w-2xl mx-auto leading-relaxed"
				in:fly={reduced ? { duration: 0 } : { y: 20, delay: 100, duration: 600 }}
			>
				{$t('index_page.cma_hero_subtitle')}
			</p>
			<div
				class="flex flex-wrap justify-center gap-3 mt-10"
				in:fly={reduced ? { duration: 0 } : { y: 16, delay: 180, duration: 600 }}
			>
				<MagneticButton href="/play" class="ledger-btn-primary w-auto px-10"
					>{$t('words.play')}</MagneticButton
				>
				<a href="/battle" class="px-8 py-2.5 font-semibold rounded-lg glass-panel action-button w-auto"
					>Battle</a
				>
				<a
					href="/account/register"
					class="px-8 py-2.5 font-semibold rounded-lg glass-panel action-button w-auto"
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

	<section class="px-4 max-w-6xl mx-auto w-full pb-20" use:scrollReveal>
		<h2
			class="font-display text-3xl sm:text-4xl font-bold text-center text-ink mb-4 tracking-[-0.03em]"
			use:scrollReveal={{ y: 20 }}
		>
			{$t('index_page.how_cma_clash_works')}
		</h2>
		<p
			class="text-center text-ink-muted text-sm mb-10 max-w-xl mx-auto"
			use:scrollReveal={{ y: 16, delay: 0.05 }}
		>
			Built for certified medical assistant prep — not accounting CMA.
		</p>
		<div
			class="grid md:grid-cols-3 gap-4 auto-rows-fr"
			use:scrollReveal={{ childSelector: '[data-bento]', stagger: 0.1, y: 32 }}
		>
			{#each steps as step}
				<BentoSpotlightCard href={step.href} class="{step.span} min-h-[10rem]" data-bento>
					<div class="flex items-start gap-3 mb-3">
						<span
							class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-primary/15 text-primary shrink-0"
						>
							<step.icon class="w-5 h-5" aria-hidden="true" />
						</span>
						<h3 class="font-display text-xl font-semibold text-ink tracking-tight">{step.title}</h3>
					</div>
					<p class="text-ink-muted text-sm flex-1 leading-relaxed">{step.body}</p>
					<span class="mt-4 text-primary font-medium text-sm group-hover:underline inline-block"
						>{$t('words.get_started')} →</span
					>
				</BentoSpotlightCard>
			{/each}
		</div>
	</section>

	<section class="px-4 max-w-6xl mx-auto w-full pb-24">
		<h2
			class="font-display text-2xl sm:text-3xl font-bold text-center text-ink mb-8 tracking-[-0.03em]"
			use:scrollReveal={{ y: 20 }}
		>
			Platform
		</h2>
		<div
			class="grid md:grid-cols-3 gap-4 auto-rows-fr"
			use:scrollReveal={{ childSelector: '[data-platform]', stagger: 0.08, y: 28 }}
		>
			{#each platform as item}
				<BentoSpotlightCard class="{item.span}" tilt={true} data-platform>
					<div class="flex items-center gap-2 mb-2">
						<item.icon class="w-5 h-5 text-primary" aria-hidden="true" />
						<h3 class="font-display font-semibold text-ink tracking-tight">{item.title}</h3>
					</div>
					<p class="text-sm text-ink-muted leading-relaxed">{item.body}</p>
				</BentoSpotlightCard>
			{/each}
		</div>
	</section>
</div>
<Footer />
