<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import { SITE_NAME, SITE_URL, DEFAULT_DESCRIPTION } from '$lib/site';
	import MagneticButton from '$lib/ui/MagneticButton.svelte';
	import BentoSpotlightCard from '$lib/ui/BentoSpotlightCard.svelte';
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import { LEDGER_ANSWER_COLORS, LEDGER_ANSWER_SHAPES } from '$lib/ui/tokens';
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { scrollReveal } from '$lib/motion/scrollReveal';
	import { fade } from 'svelte/transition';
	import { Swords, Radio, Trophy, Zap } from '@lucide/svelte';

	const { t } = getLocalization();
	const reduced = prefersReducedMotion();
	navbarVisible.visible = true;

	const homeTitle = $derived(`${SITE_NAME} — ${$t('index_page.meta.title')}`);
	const homeDescription = DEFAULT_DESCRIPTION;
	const structuredData = $derived(
		JSON.stringify({
			'@context': 'https://schema.org',
			'@type': 'WebSite',
			name: SITE_NAME,
			url: SITE_URL,
			description: homeDescription,
			publisher: { '@type': 'Organization', name: SITE_NAME }
		})
	);

	let nextClash = $state(134);
	$effect(() => {
		if (reduced) return;
		const id = setInterval(() => {
			nextClash = nextClash > 0 ? nextClash - 1 : 134;
		}, 1000);
		return () => clearInterval(id);
	});
	let mm = $derived(String(Math.floor(nextClash / 60)).padStart(2, '0'));
	let ss = $derived(String(nextClash % 60).padStart(2, '0'));

	const previewAnswers = [
		{ t: 'Left ventricle', i: 0 },
		{ t: 'Right atrium', i: 1 },
		{ t: 'Left atrium', i: 2 },
		{ t: 'Right ventricle', i: 3 }
	];
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
	<section
		class="relative overflow-hidden px-4 min-h-[88vh] flex flex-col justify-center"
		aria-labelledby="home-hero-heading"
	>
		<div
			class="pointer-events-none absolute inset-0"
			style="background: radial-gradient(80% 60% at 70% 40%, rgba(123,92,255,0.28), transparent 60%), radial-gradient(50% 40% at 20% 80%, rgba(34,211,238,0.12), transparent 50%);"
			aria-hidden="true"
		></div>
		<div class="relative z-10 max-w-6xl mx-auto w-full grid lg:grid-cols-2 gap-10 items-center py-16">
			<div>
				<p
					class="text-cyan text-xs font-semibold uppercase tracking-[0.35em] mb-4"
					in:fade={reduced ? { duration: 0 } : { duration: 300 }}
				>
					NHA CCMA · Clinical skills
				</p>
				<h1
					id="home-hero-heading"
					class="font-display text-6xl sm:text-8xl text-ink leading-[0.85]"
				>
					Clash.
				</h1>
				<p class="mt-5 text-lg text-ink-muted max-w-md leading-relaxed">
					{$t('index_page.cma_hero_subtitle')}
				</p>
				<div class="mt-8 flex flex-wrap items-center gap-4">
					<div class="rounded-xl border border-white/10 bg-surface px-4 py-3">
						<p class="text-[10px] uppercase tracking-[0.2em] text-ink-muted">Next Daily Clash</p>
						<p class="font-display text-3xl text-gold tabular-nums leading-none mt-1">
							{mm}:{ss}
						</p>
					</div>
				</div>
				<div class="flex flex-wrap gap-3 mt-8">
					<MagneticButton href="/play" class="ledger-btn-primary w-auto px-10 text-lg"
						>{$t('words.play')}</MagneticButton
					>
					<a href="/battle" class="action-button w-auto px-8">Battle</a>
					<a href="/account/register" class="action-button w-auto px-8">{$t('words.register')}</a>
				</div>
			</div>
			<div class="rounded-3xl bg-surface border border-transparent shadow-[var(--shadow-card)] p-5 sm:p-6">
				<div class="flex items-center justify-between mb-4">
					<span class="font-display text-2xl text-gold">VS</span>
					<span class="font-display text-sm text-ink-muted">Q7/12</span>
				</div>
				<p class="font-sans text-sm text-ink-muted mb-2">CCMA · Anatomy</p>
				<p class="font-sans font-semibold text-ink mb-4">
					Which chamber of the heart receives oxygenated blood from the pulmonary veins?
				</p>
				<div class="grid grid-cols-2 gap-2">
					{#each previewAnswers as a}
						<div
							class="rounded-xl p-4 text-white min-h-[4.5rem] flex flex-col items-center justify-center gap-1"
							style="background:{LEDGER_ANSWER_COLORS[a.i]}"
						>
							<AnswerShapeIcon shape={LEDGER_ANSWER_SHAPES[a.i]} class="w-6 h-6" />
							<span class="font-display text-sm normal-case">{a.t}</span>
						</div>
					{/each}
				</div>
				<p class="mt-4 text-center font-display text-gold text-sm">3-streak · +240 XP · Rank ▲2</p>
			</div>
		</div>
	</section>

	<section class="px-4 max-w-6xl mx-auto w-full pb-24" use:scrollReveal>
		<h2 class="font-display text-4xl sm:text-5xl text-center text-ink mb-10">
			{$t('index_page.how_cma_clash_works')}
		</h2>
		<div
			class="grid md:grid-cols-3 gap-4"
			use:scrollReveal={{ childSelector: '[data-bento]', stagger: 0.1, y: 12 }}
		>
			<BentoSpotlightCard href="/play" class="md:col-span-2 min-h-[10rem]" data-bento>
				<div class="flex items-center gap-3 mb-3">
					<Radio class="w-6 h-6 text-cyan" />
					<h3 class="font-display text-2xl text-ink">Live arena</h3>
				</div>
				<p class="text-ink-muted text-sm leading-relaxed">PIN lobbies, Kahoot-style tiles, VS intros.</p>
			</BentoSpotlightCard>
			<BentoSpotlightCard href="/dashboard" data-bento>
				<Zap class="w-6 h-6 text-gold mb-3" />
				<h3 class="font-display text-2xl text-ink">Study</h3>
				<p class="text-ink-muted text-sm">CCMA banks and daily goals.</p>
			</BentoSpotlightCard>
			<BentoSpotlightCard href="/leaderboard" class="md:col-span-2" data-bento>
				<Trophy class="w-6 h-6 text-gold mb-3" />
				<h3 class="font-display text-2xl text-ink">Climb</h3>
				<p class="text-ink-muted text-sm">Volt XP, streaks, and weekly boards.</p>
			</BentoSpotlightCard>
			<BentoSpotlightCard href="/battle" data-bento>
				<Swords class="w-6 h-6 text-signal mb-3" />
				<h3 class="font-display text-2xl text-ink">1v1</h3>
				<p class="text-ink-muted text-sm">Head-to-head battles.</p>
			</BentoSpotlightCard>
		</div>
	</section>
</div>
<Footer />
