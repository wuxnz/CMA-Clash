<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import DownloadQuiz from '$lib/components/DownloadQuiz.svelte';
	import Footer from '$lib/footer.svelte';
	import { signedIn } from '$lib/stores';
	import { navbarVisible } from '$lib/stores.svelte';
	import CommandpaletteNotice from '$lib/components/popover/commandpalettenotice.svelte';
	import Fuse from 'fuse.js';
	import type { PageData } from './$types';
	import StartGamePopup from '$lib/dashboard/start_game.svelte';
	import Analytics from './Analytics.svelte';
	import { onMount } from 'svelte';
	import { isSiteAdmin } from '$lib/stores';
	import { refreshSiteAdminFlag } from '$lib/site-admin';
	import { page } from '$app/state';
	import QuizTableGrid from '$lib/quiz/QuizTableGrid.svelte';
	import QuizRow from '$lib/quiz/QuizRow.svelte';
	import Button from '$lib/ui/Button.svelte';
	import { certificationShortLabel } from '$lib/cma/client';
	import { loadDashboardData } from '$lib/dashboard/loadDashboardData';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
	signedIn.set(true);
	navbarVisible.visible = true;

	let dashLoading = $state(true);
	let dashboardData = $state(data);

	const CERT_LANES = [
		{ slug: 'ccma', name: 'NHA CCMA', prefix: 'ccma-' },
		{ slug: 'ekg', name: 'EKG Technician', prefix: 'ekg-' },
		{ slug: 'phlebotomy', name: 'Phlebotomy', prefix: 'phleb-' },
		{ slug: 'cpr-bls', name: 'CPR / BLS', prefix: 'cpr-' },
		{ slug: 'clinical-skills', name: 'Clinical skills', prefix: 'skill-' }
	] as const;

	type DashItem = Record<string, any> & { type: 'quiz' | 'quiztivity'; certLabel?: string };

	function certLabelFor(item: Record<string, any>): string | undefined {
		const certs = dashboardData.certifications ?? [];
		const match = certs.find((c) => c.id === item.certification_id);
		if (match) return certificationShortLabel(match.slug, match.name);
		const fromTitle = certificationShortLabel(null, item.title);
		return fromTitle === 'CCMA' && !/ccma/i.test(String(item.title ?? ''))
			? undefined
			: fromTitle;
	}

	function buildItems(): DashItem[] {
		const quizzes = Array.isArray(dashboardData.quizzes) ? dashboardData.quizzes : [];
		const quiztivities = Array.isArray(dashboardData.quiztivities)
			? dashboardData.quiztivities
			: [];
		return [
			...quizzes.map((q) => ({ ...q, type: 'quiz' as const, certLabel: certLabelFor(q) })),
			...quiztivities.map((q) => ({
				...q,
				type: 'quiztivity' as const,
				certLabel: certLabelFor(q)
			}))
		];
	}

	function formatDay(value: unknown): string | null {
		if (value == null || value === '') return null;
		const d = value instanceof Date ? value : new Date(value as string | number);
		if (Number.isNaN(d.getTime())) return null;
		return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
	}

	function lastPlayedFor(item: DashItem): string | null {
		const results = dashboardData.results ?? [];
		const hit = results.find((r) => {
			const q = r.quiz;
			const id = typeof q === 'object' && q ? q.id : q;
			return String(id) === String(item.id);
		});
		return (
			formatDay(hit?.timestamp) ?? formatDay(item.updated_at) ?? formatDay(item.created_at)
		);
	}

	let search_term = $state('');
	let start_game = $state<string | null>(null);
	let download_id: string | null = $state(null);
	let all_items: DashItem[] = $state(buildItems());
	let items_to_show: DashItem[] = $state(buildItems());
	let fuse: Fuse<DashItem> | undefined;
	let analytics_quiz_selected = $state<any>(undefined);

	const forceEmpty = $derived(page.url.searchParams.get('empty') === '1');
	const visibleItems = $derived(forceEmpty ? [] : items_to_show);

	const displayName = $derived(dashboardData.username || 'there');
	const g = $derived(dashboardData.gamification);
	const level = $derived(g?.level ?? 1);
	const xp = $derived(g?.total_xp ?? 0);
	const streak = $derived(g?.current_streak_days ?? 0);
	const hasStats = $derived(streak > 0 || xp > 0);

	const masteryLanes = $derived.by(() => {
		const stats = dashboardData.topicStats ?? [];
		const topics = dashboardData.topics ?? [];
		const certs = dashboardData.certifications ?? [];
		return CERT_LANES.map((lane) => {
			const cert = certs.find((c) => c.slug === lane.slug);
			const slugs = new Set(
				topics.filter((t) => t.certification_id === cert?.id).map((t) => t.slug)
			);
			const rows = stats.filter((s) => {
				const slug = s.topic_slug ?? '';
				return slugs.has(slug) || slug.startsWith(lane.prefix);
			});
			const answered = rows.reduce((n, r) => n + (r.questions_answered ?? 0), 0);
			const correct = rows.reduce((n, r) => n + (r.questions_correct ?? 0), 0);
			const accuracy =
				answered > 0
					? Math.round((correct / answered) * 100)
					: rows.length
						? Math.round(
								rows.reduce((n, r) => n + (r.accuracy_percent ?? 0), 0) /
									rows.length
							)
						: 0;
			return { ...lane, answered, accuracy, started: answered > 0 };
		});
	});
	const startedMastery = $derived(masteryLanes.filter((l) => l.started));

	const recent = $derived((dashboardData.results ?? []).slice(0, 5));
	const board = $derived((dashboardData.leaderboard ?? []).slice(0, 5));

	const search = () => {
		if (!fuse || search_term === '') {
			items_to_show = all_items;
			return;
		}
		items_to_show = fuse.search(search_term).map((r) => r.item);
	};

	function applyDashboardData() {
		all_items = buildItems();
		items_to_show = all_items;
		fuse = new Fuse(all_items, {
			keys: ['title', 'description', 'questions.title'],
			findAllMatches: true
		});
	}

	onMount(() => {
		void refreshSiteAdminFlag();
		void (async () => {
			try {
				dashboardData = await loadDashboardData(fetch);
			} finally {
				dashLoading = false;
				applyDashboardData();
			}
		})();
	});

	const deleteQuiz = async (to_delete: string, type: 'quiz' | 'quiztivity') => {
		if (!confirm('Do you really want to delete this quiz?')) {
			return;
		}
		if (type === 'quiz') {
			await fetch(`/api/v1/quiz/delete/${to_delete}`, { method: 'DELETE' });
		} else {
			await fetch(`/api/v1/quiztivity/${to_delete}`, { method: 'DELETE' });
		}
		window.location.reload();
	};

	function hostFirst() {
		const first =
			visibleItems.find((i) => i.type === 'quiz') ?? all_items.find((i) => i.type === 'quiz');
		if (first && !forceEmpty) start_game = first.id;
		else window.location.assign('/host');
	}

	const links = [
		{ href: '/create', label: 'Create' },
		{ href: '/play', label: 'Join with PIN' },
		{ href: '/practice', label: 'Practice' },
		{ href: '/battle', label: 'Battle' },
		{ href: '/import', label: 'Import' },
		{ href: '/results', label: 'Results' },
		{ href: '/edit/files', label: 'Files' },
		{ href: '/account/settings', label: 'Settings' }
	] as const;
</script>

<svelte:head>
	<title>CMA Clash: Dashboard</title>
</svelte:head>
<Analytics bind:quiz={analytics_quiz_selected} />
<CommandpaletteNotice />

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 sm:px-8 lg:px-12 pt-14 lg:pt-20 pb-20 min-w-0">
		<header class="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-6">
			<div class="min-w-0">
				<p class="eyebrow">Operator dashboard</p>
				<h1
					class="font-display text-[clamp(2.2rem,6vw,4.2rem)] leading-[0.92] tracking-[-0.04em] mt-4"
				>
					Hi, <em class="italic font-normal text-primary">{displayName}</em>
				</h1>
				{#if hasStats}
					<p class="text-sm text-ink-muted mt-4">
						{#if streak > 0}{streak}-day streak{/if}
						{#if streak > 0 && xp > 0}<span> · </span>{/if}
						{#if xp > 0}Level {level} · {xp.toLocaleString()} XP{/if}
					</p>
				{/if}
			</div>
			<Button class="w-full sm:w-auto" onclick={hostFirst}>Host a Clash</Button>
		</header>

		<nav
			class="mt-8 flex flex-wrap items-center gap-x-5 gap-y-1 text-sm text-ink-muted border-t border-line pt-5"
			aria-label="Dashboard"
		>
			{#each links as link}
				<a href={link.href} class="min-h-11 inline-flex items-center link-hover"
					>{link.label}</a
				>
			{/each}
			{#if $isSiteAdmin}
				<a href="/site-admin/users" class="min-h-11 inline-flex items-center link-hover"
					>Site admin</a
				>
			{/if}
		</nav>

		<div class="mt-12 grid grid-cols-1 xl:grid-cols-12 gap-12 xl:gap-14">
			<section class="xl:col-span-9 min-w-0">
				<div class="flex flex-wrap items-center justify-between gap-3 mb-4">
					<h2 class="eyebrow">Quizzes</h2>
					{#if !forceEmpty && all_items.length > 0}
						<label class="sr-only" for="quiz-search">Search quizzes</label>
						<input
							id="quiz-search"
							bind:value={search_term}
							oninput={search}
							class="ledger-input max-w-[14rem] min-h-11 hidden sm:block text-sm"
							placeholder="Search"
						/>
					{/if}
				</div>

				{#if dashLoading}
					<ul class="animate-pulse pt-2" aria-busy="true" aria-label="Loading quizzes">
						{#each [1, 2, 3, 4, 5] as n (n)}
							<li class="border-b border-line py-3">
								<div class="h-3 w-2/5 max-w-xs bg-elevated"></div>
							</li>
						{/each}
					</ul>
				{:else if visibleItems.length === 0}
					<div class="pt-5" data-empty-quizzes>
						<p class="text-sm text-ink">No quizzes yet.</p>
						<p class="text-sm text-ink-muted mt-1">
							<a href="/create" class="text-ink link-hover">Create</a>
							or
							<a href="/import" class="text-ink link-hover">import</a>
							one, then host it from this list.
						</p>
					</div>
				{:else}
					<QuizTableGrid>
						{#snippet rows()}
							{#each visibleItems as quiz (quiz.id)}
								<QuizRow
									mode="owner"
									{quiz}
									lastPlayed={lastPlayedFor(quiz)}
									onHost={(id) => (start_game = id)}
									onAnalytics={(q) => (analytics_quiz_selected = q)}
									onDelete={deleteQuiz}
									onDownload={(id) => (download_id = id)}
								/>
							{/each}
						{/snippet}
					</QuizTableGrid>
				{/if}
			</section>

			<aside class="xl:col-span-3 min-w-0 xl:border-l xl:border-line xl:pl-8">
				<section>
					<h2 class="eyebrow">Mastery</h2>
					{#if startedMastery.length === 0}
						<p class="text-sm text-ink-muted mt-3">
							No cert stats yet.
							<a href="/practice" class="text-ink link-hover">Practice</a>
						</p>
					{:else}
						<ul class="mt-4 space-y-4">
							{#each startedMastery as lane}
								<li>
									<div class="flex items-baseline justify-between gap-3 text-sm">
										<span class="text-ink truncate">{lane.name}</span>
										<span class="tabular-nums text-ink-muted"
											>{lane.accuracy}%</span
										>
									</div>
									<div class="mt-1.5 h-1 bg-elevated overflow-hidden">
										<div
											class="h-full bg-primary"
											style="width:{lane.accuracy}%; transition: width 300ms ease-out"
										></div>
									</div>
								</li>
							{/each}
						</ul>
					{/if}
				</section>

				<section class="mt-12">
					<h2 class="eyebrow">Recent games</h2>
					{#if recent.length === 0}
						<p class="text-sm text-ink-muted mt-3">
							None yet.
							<a href="/results" class="text-ink link-hover">Results</a>
						</p>
					{:else}
						<ul class="mt-3 border-t border-line">
							{#each recent as game}
								<li>
									<a
										href="/results/{game.id}"
										class="flex items-center justify-between gap-3 py-2.5 min-h-11 min-w-0 border-b border-line"
									>
										<span class="truncate text-sm text-ink"
											>{game.title ?? 'Untitled'}</span
										>
										<span class="text-xs text-ink-muted shrink-0 tabular-nums">
											{formatDay(game.timestamp) ?? ''}
										</span>
									</a>
								</li>
							{/each}
						</ul>
					{/if}
				</section>

				<section class="mt-12">
					<h2 class="eyebrow">Weekly</h2>
					{#if board.length === 0}
						<p class="text-sm text-ink-muted mt-3">
							No scores this week.
							<a href="/leaderboard" class="text-ink link-hover">Leaderboard</a>
						</p>
					{:else}
						<ol class="mt-3 space-y-1">
							{#each board as row, i}
								<li
									class="flex items-center justify-between gap-3 min-h-11 text-sm"
								>
									<span class="text-ink truncate">
										<span class="text-ink-subtle tabular-nums mr-2"
											>{i + 1}</span
										>
										{row.username}
									</span>
									<span class="tabular-nums text-ink-muted"
										>{row.xp.toLocaleString()}</span
									>
								</li>
							{/each}
						</ol>
					{/if}
				</section>
			</aside>
		</div>
	</div>
	<Footer />
</div>

{#if start_game !== null}
	<StartGamePopup bind:quiz_id={start_game} />
{/if}
<DownloadQuiz bind:quiz_id={download_id} />
