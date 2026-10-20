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
	import { page } from '$app/state';
	import QuizCard from '$lib/dashboard/QuizCard.svelte';
	import { certificationShortLabel } from '$lib/cma/client';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
	signedIn.set(true);
	navbarVisible.visible = true;

	const CERT_LANES = [
		{ slug: 'ccma', name: 'NHA CCMA', prefix: 'ccma-' },
		{ slug: 'ekg', name: 'EKG Technician', prefix: 'ekg-' },
		{ slug: 'phlebotomy', name: 'Phlebotomy', prefix: 'phleb-' },
		{ slug: 'cpr-bls', name: 'CPR / BLS', prefix: 'cpr-' },
		{ slug: 'clinical-skills', name: 'Clinical skills', prefix: 'skill-' }
	] as const;

	type DashItem = Record<string, any> & { type: 'quiz' | 'quiztivity'; certLabel?: string };

	function certLabelFor(item: Record<string, any>): string | undefined {
		const certs = data.certifications ?? [];
		const match = certs.find((c) => c.id === item.certification_id);
		if (match) return certificationShortLabel(match.slug, match.name);
		const fromTitle = certificationShortLabel(null, item.title);
		return fromTitle === 'CCMA' && !/ccma/i.test(String(item.title ?? '')) ? undefined : fromTitle;
	}

	function buildItems(): DashItem[] {
		const quizzes = Array.isArray(data.quizzes) ? data.quizzes : [];
		const quiztivities = Array.isArray(data.quiztivities) ? data.quiztivities : [];
		return [
			...quizzes.map((q) => ({ ...q, type: 'quiz' as const, certLabel: certLabelFor(q) })),
			...quiztivities.map((q) => ({ ...q, type: 'quiztivity' as const, certLabel: certLabelFor(q) }))
		];
	}

	function formatDay(value: unknown): string | null {
		if (value == null || value === '') return null;
		const d = value instanceof Date ? value : new Date(value as string | number);
		if (Number.isNaN(d.getTime())) return null;
		return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
	}

	function lastPlayedFor(item: DashItem): string | null {
		const results = data.results ?? [];
		const hit = results.find((r) => {
			const q = r.quiz;
			const id = typeof q === 'object' && q ? q.id : q;
			return String(id) === String(item.id);
		});
		return formatDay(hit?.timestamp) ?? formatDay(item.updated_at) ?? formatDay(item.created_at);
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

	const displayName = $derived(data.username || 'there');
	const g = $derived(data.gamification);
	const level = $derived(g?.level ?? 1);
	const xp = $derived(g?.total_xp ?? 0);
	const streak = $derived(g?.current_streak_days ?? 0);
	const hasStats = $derived(streak > 0 || xp > 0);

	const masteryLanes = $derived.by(() => {
		const stats = data.topicStats ?? [];
		const topics = data.topics ?? [];
		const certs = data.certifications ?? [];
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
						? Math.round(rows.reduce((n, r) => n + (r.accuracy_percent ?? 0), 0) / rows.length)
						: 0;
			return { ...lane, answered, accuracy, started: answered > 0 };
		});
	});
	const startedMastery = $derived(masteryLanes.filter((l) => l.started));

	const recent = $derived((data.results ?? []).slice(0, 5));
	const board = $derived((data.leaderboard ?? []).slice(0, 5));

	const search = () => {
		if (!fuse || search_term === '') {
			items_to_show = all_items;
			return;
		}
		items_to_show = fuse.search(search_term).map((r) => r.item);
	};

	onMount(() => {
		all_items = buildItems();
		items_to_show = all_items;
		fuse = new Fuse(all_items, {
			keys: ['title', 'description', 'questions.title'],
			findAllMatches: true
		});
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
	<title>CMA Clash - Dashboard</title>
</svelte:head>
<Analytics bind:quiz={analytics_quiz_selected} />
<CommandpaletteNotice />

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<header class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
			<div class="min-w-0">
				<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Hi, {displayName}</h1>
				{#if hasStats}
					<p class="text-sm text-ink-muted mt-1">
						{#if streak > 0}{streak}-day streak{/if}
						{#if streak > 0 && xp > 0}<span> · </span>{/if}
						{#if xp > 0}Level {level} · {xp.toLocaleString()} XP{/if}
					</p>
				{/if}
			</div>
			<button
				type="button"
				class="ledger-btn-primary w-full sm:w-auto min-h-11 px-5"
				onclick={hostFirst}
			>
				Host a Clash
			</button>
		</header>

		<nav
			class="mt-4 flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-ink-muted"
			aria-label="Dashboard"
		>
			{#each links as link}
				<a href={link.href} class="min-h-11 inline-flex items-center link-hover">{link.label}</a>
			{/each}
		</nav>

		<div class="mt-12 grid grid-cols-1 xl:grid-cols-12 gap-12 xl:gap-14">
			<section class="xl:col-span-9 min-w-0">
				<div class="flex flex-wrap items-center justify-between gap-3 mb-2">
					<h2 class="text-sm font-semibold text-ink">Quizzes</h2>
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

				{#if visibleItems.length === 0}
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
					<div
						class="hidden md:grid md:grid-cols-[minmax(0,1.4fr)_6.5rem_3.5rem_7rem_auto] gap-x-3 text-xs text-ink-muted pb-2 border-b border-white/[0.07]"
					>
						<span>Title</span>
						<span>Cert</span>
						<span>Qs</span>
						<span>Difficulty</span>
						<span class="text-right"> </span>
					</div>
					<ul>
						{#each visibleItems as quiz (quiz.id)}
							<QuizCard
								{quiz}
								lastPlayed={lastPlayedFor(quiz)}
								onHost={(id) => (start_game = id)}
								onAnalytics={(q) => (analytics_quiz_selected = q)}
								onDelete={deleteQuiz}
								onDownload={(id) => (download_id = id)}
							/>
						{/each}
					</ul>
				{/if}
			</section>

			<aside class="xl:col-span-3 min-w-0 xl:border-l xl:border-white/[0.07] xl:pl-8">
				<section>
					<h2 class="text-sm font-semibold text-ink">Mastery</h2>
					{#if startedMastery.length === 0}
						<p class="text-sm text-ink-muted mt-2">
							No cert stats yet.
							<a href="/practice" class="text-ink link-hover">Practice</a>
						</p>
					{:else}
						<ul class="mt-4 space-y-3">
							{#each startedMastery as lane}
								<li>
									<div class="flex items-baseline justify-between gap-3 text-sm">
										<span class="text-ink truncate">{lane.name}</span>
										<span class="tabular-nums text-ink-muted">{lane.accuracy}%</span>
									</div>
									<div class="mt-1.5 h-1 rounded-full bg-elevated overflow-hidden">
										<div
											class="h-full rounded-full bg-violet"
											style="width:{lane.accuracy}%; transition: width 300ms ease-out"
										></div>
									</div>
								</li>
							{/each}
						</ul>
					{/if}
				</section>

				<section class="mt-10">
					<h2 class="text-sm font-semibold text-ink">Recent games</h2>
					{#if recent.length === 0}
						<p class="text-sm text-ink-muted mt-2">
							None yet.
							<a href="/results" class="text-ink link-hover">Results</a>
						</p>
					{:else}
						<ul class="mt-3 divide-y divide-white/[0.07]">
							{#each recent as game}
								<li>
									<a
										href="/results/{game.id}"
										class="flex items-center justify-between gap-3 py-2.5 min-h-11 min-w-0"
									>
										<span class="truncate text-sm text-ink">{game.title ?? 'Untitled'}</span>
										<span class="text-xs text-ink-muted shrink-0 tabular-nums">
											{formatDay(game.timestamp) ?? ''}
										</span>
									</a>
								</li>
							{/each}
						</ul>
					{/if}
				</section>

				<section class="mt-10">
					<h2 class="text-sm font-semibold text-ink">Weekly</h2>
					{#if board.length === 0}
						<p class="text-sm text-ink-muted mt-2">
							No scores this week.
							<a href="/leaderboard" class="text-ink link-hover">Leaderboard</a>
						</p>
					{:else}
						<ol class="mt-3 space-y-1">
							{#each board as row, i}
								<li class="flex items-center justify-between gap-3 min-h-11 text-sm">
									<span class="text-ink truncate">
										<span class="text-ink-muted tabular-nums mr-2">{i + 1}</span>
										{row.username}
									</span>
									<span class="tabular-nums text-ink-muted">{row.xp.toLocaleString()}</span>
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
