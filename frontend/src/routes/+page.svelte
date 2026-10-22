<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import { SITE_NAME, SITE_URL, DEFAULT_DESCRIPTION } from '$lib/site';
	import Button from '$lib/ui/Button.svelte';
	import HomePreviewQuestion from '$lib/landing/HomePreviewQuestion.svelte';
	import { prefersReducedMotion } from '$lib/ui/motion';
	import { fade } from 'svelte/transition';
	import { reveal, maskLines } from '$lib/motion/editorial';

	const { t } = getLocalization();
	const reduced = prefersReducedMotion();
	navbarVisible.visible = true;

	const homeTitle = $derived(`${SITE_NAME}: ${$t('index_page.meta.title')}`);
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

	const topics = [
		'HIPAA',
		'Venipuncture',
		'Rhythm Recognition',
		'POCT',
		'Chain of Survival',
		'Law & Ethics',
		'Diabetes',
		'Specimen Handling'
	];

	const pillars = [
		{
			index: '01',
			title: $t('index_page.cma_step_study_title'),
			body: $t('index_page.cma_step_study_body'),
			href: '/study'
		},
		{
			index: '02',
			title: $t('index_page.cma_step_live_title'),
			body: $t('index_page.cma_step_live_body'),
			href: '/play'
		},
		{
			index: '03',
			title: $t('index_page.cma_step_climb_title'),
			body: $t('index_page.cma_step_climb_body'),
			href: '/leaderboard'
		}
	];

	const modes = [
		{
			title: 'Live quiz',
			body: 'Host a session or join with a PIN. Real-time standings and speed-bonus scoring.',
			href: '/play'
		},
		{
			title: 'Practice',
			body: 'Drill questions against a timer, with an explanation after every item.',
			href: '/practice'
		},
		{
			title: 'Battle',
			body: 'Compete one-on-one. Rank-based scoring with momentum streaks.',
			href: '/battle'
		},
		{
			title: 'Leaderboard',
			body: 'Weekly XP standings across every certification on the platform.',
			href: '/leaderboard'
		}
	];

	const certifications = [
		{ name: 'NHA CCMA', items: 1204 },
		{ name: 'EKG Technician', items: 642 },
		{ name: 'Phlebotomy', items: 518 },
		{ name: 'CPR / BLS', items: 430 }
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
	<!-- ================= HERO ================= -->
	<section class="px-4 sm:px-8 lg:px-12 max-w-[1500px] w-full mx-auto pt-6 lg:pt-10 pb-12">
		<div
			class="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6 border-b border-line pb-5"
		>
			<p class="eyebrow" use:reveal>NHA CCMA exam prep · est. 2024</p>
			<p class="eyebrow text-right" use:reveal={{ delay: 0.08 }}>
				Edition 04 — Kinetic Editorial
			</p>
		</div>

		<div class="grid lg:grid-cols-12 gap-8 lg:gap-10 mt-6 lg:mt-8 items-start">
			<div class="lg:col-span-7">
				<h1 class="headline text-[clamp(2.6rem,6.4vw,5.6rem)] leading-[0.92]">
					<span class="block" use:maskLines
						>Pass the <em class="accent-italic">exam.</em></span
					>
				</h1>

				<p
					class="text-base sm:text-lg text-ink-muted leading-relaxed max-w-[44ch] mt-6"
					use:reveal={{ delay: 0.12 }}
				>
					{$t('index_page.cma_hero_subtitle')}
				</p>

				<div class="flex flex-wrap items-center gap-3 mt-7" use:reveal={{ delay: 0.18 }}>
					<Button href="/play" class="text-base">{$t('words.play')}</Button>
					<Button href="/battle" variant="secondary" class="text-base">Battle</Button>
					<Button href="/account/register" variant="secondary" class="text-base"
						>{$t('words.register')}</Button
					>
				</div>

				<div
					class="flex items-baseline gap-3 mt-8 pt-5 border-t border-line"
					use:reveal={{ delay: 0.24 }}
				>
					<span class="eyebrow">Next daily clash</span>
					<span class="font-mono text-2xl text-primary tabular-nums leading-none"
						>{mm}:{ss}</span
					>
				</div>

				<div class="mt-8" use:reveal={{ delay: 0.3 }}>
					<p class="eyebrow mb-3">Certifications in the bank</p>
					<ul class="border-t border-line">
						{#each certifications as cert (cert.name)}
							<li
								class="flex items-baseline justify-between gap-4 py-2.5 border-b border-line"
							>
								<span class="text-sm text-ink">{cert.name}</span>
								<span class="font-mono text-xs text-ink-subtle tabular-nums"
									>{cert.items} items</span
								>
							</li>
						{/each}
					</ul>
				</div>
			</div>

			<div class="lg:col-span-5" use:reveal={{ delay: 0.16, y: 36 }}>
				<HomePreviewQuestion />
			</div>
		</div>
	</section>

	<!-- ================= MARQUEE ================= -->
	<div class="border-y border-line overflow-hidden py-4" aria-hidden="true">
		<div class="marquee-track">
			{#each [...topics, ...topics] as topic, i (i)}
				<span
					class="headline text-2xl sm:text-3xl flex items-center gap-10 whitespace-nowrap"
				>
					{topic}
					<span class="w-2 h-2 bg-primary rotate-45 inline-block"></span>
				</span>
			{/each}
		</div>
	</div>

	<!-- ================= PILLARS ================= -->
	<section class="px-4 sm:px-8 lg:px-12 max-w-[1500px] w-full mx-auto py-16 lg:py-24">
		<div class="grid lg:grid-cols-12 gap-8 lg:gap-12 mb-12">
			<div class="lg:col-span-5">
				<p class="eyebrow" use:reveal>How it works</p>
				<h2
					class="headline text-[clamp(2rem,5vw,3.6rem)] mt-4"
					use:reveal={{ delay: 0.05 }}
				>
					Four steps, <em class="accent-italic">one scoreboard.</em>
				</h2>
			</div>
			<p
				class="lg:col-span-6 lg:col-start-7 text-ink-muted leading-relaxed self-end"
				use:reveal={{ delay: 0.1 }}
			>
				Every mode shares the same validated bank and the same scoring engine, so a quiet
				practice run and a live clash are directly comparable.
			</p>
		</div>

		<div>
			{#each pillars as pillar, i (pillar.index)}
				<a
					href={pillar.href}
					class="group grid lg:grid-cols-12 gap-4 lg:gap-8 items-start py-7 border-t border-line transition-colors duration-300 hover:bg-primary-soft px-2 -mx-2"
					use:reveal={{ delay: i * 0.06, y: 20 }}
				>
					<span class="lg:col-span-1 font-mono text-xs tracking-[0.2em] text-primary"
						>{pillar.index}</span
					>
					<h3
						class="lg:col-span-4 headline text-2xl sm:text-3xl"
						data-title={pillar.title}
					>
						{pillar.title}
					</h3>
					<p class="lg:col-span-5 text-ink-muted leading-relaxed">{pillar.body}</p>
					<span
						class="lg:col-span-2 lg:text-right font-mono text-xs tracking-[0.16em] text-ink-subtle group-hover:text-primary transition-colors"
					>
						Explore →
					</span>
				</a>
			{/each}
		</div>
	</section>

	<!-- ================= MODES ================= -->
	<section class="px-4 sm:px-8 lg:px-12 max-w-[1500px] w-full mx-auto pb-16 lg:pb-24">
		<div class="border-t border-line pt-10">
			<p class="eyebrow" use:reveal>Four modes</p>
		</div>
		<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-px bg-line mt-8 border border-line">
			{#each modes as mode, i (mode.title)}
				<a
					href={mode.href}
					class="group bg-paper p-6 lg:p-7 transition-colors duration-300 hover:bg-elevated flex flex-col min-h-[13rem]"
					use:reveal={{ delay: i * 0.06, y: 22 }}
				>
					<span class="font-mono text-[0.66rem] tracking-[0.2em] text-primary"
						>{String(i + 1).padStart(2, '0')}</span
					>
					<h3 class="headline text-xl mt-auto mb-2">{mode.title}</h3>
					<p class="text-sm text-ink-muted leading-relaxed">{mode.body}</p>
					<span
						class="font-mono text-[0.66rem] tracking-[0.18em] text-ink-subtle mt-4 group-hover:text-primary transition-colors"
						>Open →</span
					>
				</a>
			{/each}
		</div>
	</section>
</div>
<Footer />

<style>
	/* Editorial headings get a touch of optical refinement. */
	.headline em {
		font-style: italic;
		font-variation-settings:
			'SOFT' 40,
			'WONK' 1;
	}
</style>
