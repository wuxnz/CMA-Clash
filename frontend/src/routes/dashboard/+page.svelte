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
	import AnimatedCounter from '$lib/ui/AnimatedCounter.svelte';
	import { certificationShortLabel } from '$lib/cma/client';
	import {
		Flame,
		Swords,
		Plus,
		LogIn,
		Timer,
		Upload,
		Folder,
		Settings,
		Trophy,
		Radio
	} from '@lucide/svelte';

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
	const xpNeed = $derived(g ? g.total_xp + g.xp_to_next_level : 100);
	const xpPct = $derived(Math.min(100, Math.round((xp / Math.max(1, xpNeed)) * 100)));

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
		else window.location.assign('/explore');
	}

	const actions = [
		{
			href: '/create',
			icon: Plus,
			label: 'Create quiz',
			hint: 'Write a new set',
			tone: 'text-violet'
		},
		{ href: '/play', icon: LogIn, label: 'Join', hint: 'Enter a live PIN', tone: 'text-cyan' },
		{ href: '/practice', icon: Timer, label: 'Practice', hint: 'Solo time attack', tone: 'text-gold' },
		{ href: '/battle', icon: Swords, label: 'Battle', hint: '1v1 elimination', tone: 'text-signal' }
	] as const;
</script>

<svelte:head>
	<title>CMA Clash - Dashboard</title>
</svelte:head>
<Analytics bind:quiz={analytics_quiz_selected} />
<CommandpaletteNotice />

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 py-6 min-w-0">
		<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-12 gap-3 md:gap-4">
			<section
				class="arena-enter md:col-span-2 xl:col-span-12 rounded-2xl bg-surface shadow-[var(--shadow-card)] p-5 sm:p-6"
			>
				<div class="flex flex-col lg:flex-row lg:items-center gap-5">
					<div class="min-w-0 flex-1">
						<p class="font-display text-gold text-sm tracking-[0.3em]">Arena</p>
						<h1 class="font-display text-4xl sm:text-5xl text-ink leading-none mt-1 min-w-0 break-words">
							Welcome back, {displayName}
						</h1>
						<div class="mt-4 flex flex-wrap items-center gap-3 text-sm">
							<span
								class="inline-flex items-center gap-2 min-h-11 rounded-xl bg-elevated px-3 text-ink"
							>
								<Flame class="w-4 h-4 text-gold shrink-0" aria-hidden="true" />
								<AnimatedCounter
									value={streak}
									duration={0.8}
									suffix="-day streak"
									class="font-semibold"
								/>
							</span>
							<span class="inline-flex items-center gap-2 min-h-11 rounded-xl bg-elevated px-3">
								<span class="font-display text-violet">Lv {level}</span>
								<span class="text-ink-muted tabular-nums">{xp.toLocaleString()} XP</span>
							</span>
						</div>
						<div class="mt-3 max-w-md">
							<div class="h-2 rounded-full bg-elevated overflow-hidden" aria-hidden="true">
								<div
									class="h-full bg-gold rounded-full"
									style="width:{xpPct}%; transition: width 300ms ease-out"
								></div>
							</div>
							<p class="text-xs text-ink-muted mt-1">{xpPct}% to next level</p>
						</div>
					</div>
					<button
						type="button"
						class="ledger-btn-primary w-full sm:w-auto min-h-11 px-8 inline-flex items-center justify-center gap-2"
						onclick={hostFirst}
					>
						<Radio class="w-4 h-4" aria-hidden="true" />
						Host a Clash
					</button>
				</div>
			</section>

			<div class="md:col-span-2 xl:col-span-12 grid grid-cols-2 md:grid-cols-4 gap-3">
				{#each actions as action, i}
					{@const Icon = action.icon}
					<a
						href={action.href}
						class="dash-tile arena-enter rounded-2xl bg-surface shadow-[var(--shadow-card)] p-4 min-h-[5.5rem] flex flex-col gap-2"
						style="animation-delay: {(i + 1) * 100}ms"
					>
						<Icon class="w-5 h-5 {action.tone}" aria-hidden="true" />
						<span class="font-display text-lg text-ink">{action.label}</span>
						<span class="text-xs text-ink-muted">{action.hint}</span>
					</a>
				{/each}
			</div>

			<nav
				class="arena-enter md:col-span-2 xl:col-span-12 flex flex-wrap gap-x-4 gap-y-2 text-sm text-ink-muted"
				style="animation-delay: 200ms"
				aria-label="More dashboard links"
			>
				<a href="/import" class="min-h-11 inline-flex items-center gap-1.5 link-hover">
					<Upload class="w-4 h-4" aria-hidden="true" /> Import
				</a>
				<a href="/results" class="min-h-11 inline-flex items-center gap-1.5 link-hover">
					<Trophy class="w-4 h-4" aria-hidden="true" /> Results
				</a>
				<a href="/edit/files" class="min-h-11 inline-flex items-center gap-1.5 link-hover">
					<Folder class="w-4 h-4" aria-hidden="true" /> Files
				</a>
				<a href="/account/settings" class="min-h-11 inline-flex items-center gap-1.5 link-hover">
					<Settings class="w-4 h-4" aria-hidden="true" /> Settings
				</a>
			</nav>

			<section class="arena-enter md:col-span-2 xl:col-span-8 min-w-0" style="animation-delay: 250ms">
				<div class="flex flex-wrap items-end justify-between gap-3 mb-4">
					<div>
						<p class="font-display text-cyan text-sm tracking-[0.2em]">Library</p>
						<h2 class="font-display text-3xl text-ink">My quizzes</h2>
					</div>
					{#if !forceEmpty && all_items.length > 0}
						<label class="sr-only" for="quiz-search">Search quizzes</label>
						<input
							id="quiz-search"
							bind:value={search_term}
							oninput={search}
							class="ledger-input max-w-xs min-h-11 hidden sm:block"
							placeholder="Search your quizzes"
						/>
					{/if}
				</div>

				{#if visibleItems.length === 0}
					<div
						class="rounded-2xl bg-surface shadow-[var(--shadow-card)] px-6 py-12 text-center"
						data-empty-quizzes
					>
						<p class="font-display text-3xl text-ink">No quizzes yet</p>
						<p class="text-ink-muted mt-2 max-w-sm mx-auto">
							Create a set or import one, then host a Clash from this board.
						</p>
						<div class="mt-6 flex flex-wrap justify-center gap-3">
							<a href="/create" class="ledger-btn-primary w-auto min-h-11 px-6">Create quiz</a>
							<a href="/import" class="action-button min-h-11 px-6 inline-flex items-center"
								>Import</a
							>
						</div>
					</div>
				{:else}
					<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
						{#each visibleItems as quiz, i (quiz.id)}
							<QuizCard
								{quiz}
								enterDelay={Math.min(i, 7) * 80}
								onHost={(id) => (start_game = id)}
								onAnalytics={(q) => (analytics_quiz_selected = q)}
								onDelete={deleteQuiz}
								onDownload={(id) => (download_id = id)}
							/>
						{/each}
					</div>
				{/if}
			</section>

			<aside
				class="md:col-span-2 xl:col-span-4 grid grid-cols-1 md:grid-cols-2 xl:grid-cols-1 gap-4 min-w-0"
			>
				<section
					class="arena-enter rounded-2xl bg-surface shadow-[var(--shadow-card)] p-5"
					style="animation-delay: 300ms"
				>
					<p class="font-display text-violet text-sm tracking-[0.2em]">Progress</p>
					<h2 class="font-display text-2xl text-ink mb-4">Mastery</h2>
					<ul class="space-y-4">
						{#each masteryLanes as lane}
							<li>
								<div class="flex items-center justify-between gap-2 mb-1.5">
									<span class="font-display text-sm text-ink truncate">{lane.name}</span>
									<span
										class="font-display text-sm tabular-nums {lane.started
											? 'text-gold'
											: 'text-ink-muted'}"
									>
										{lane.started ? `${lane.accuracy}%` : '—'}
									</span>
								</div>
								<div class="h-2 rounded-full bg-elevated overflow-hidden">
									<div
										class="h-full rounded-full {lane.started ? 'bg-violet' : 'bg-elevated'}"
										style="width:{lane.started ? lane.accuracy : 0}%; transition: width 300ms ease-out"
									></div>
								</div>
								<p class="text-[11px] text-ink-muted mt-1">
									{lane.started ? `${lane.answered} answered` : 'Play a clash to start this cert'}
								</p>
							</li>
						{/each}
					</ul>
				</section>

				<section
					class="arena-enter rounded-2xl bg-surface shadow-[var(--shadow-card)] p-5"
					style="animation-delay: 400ms"
				>
					<p class="font-display text-signal text-sm tracking-[0.2em]">Tape</p>
					<h2 class="font-display text-2xl text-ink mb-4">Recent games</h2>
					{#if recent.length === 0}
						<p class="text-sm text-ink-muted">
							No hosted games yet. Host a Clash and results will land here.
						</p>
						<a href="/results" class="mt-4 action-button min-h-11 px-4 inline-flex items-center"
							>Open results</a
						>
					{:else}
						<ul class="space-y-2">
							{#each recent as game}
								<li>
									<a
										href="/results/{game.id}"
										class="flex items-center justify-between gap-3 rounded-xl bg-elevated px-3 py-3 min-h-11 min-w-0"
									>
										<span class="truncate text-sm text-ink">{game.title ?? 'Untitled clash'}</span>
										<span class="text-xs text-ink-muted shrink-0 tabular-nums">
											{game.timestamp ? new Date(game.timestamp).toLocaleDateString() : ''}
										</span>
									</a>
								</li>
							{/each}
						</ul>
					{/if}
				</section>

				<section
					class="arena-enter rounded-2xl bg-surface shadow-[var(--shadow-card)] p-5 md:col-span-2 xl:col-span-1"
					style="animation-delay: 500ms"
				>
					<p class="font-display text-gold text-sm tracking-[0.2em]">Season</p>
					<h2 class="font-display text-2xl text-ink mb-4">Weekly board</h2>
					{#if board.length === 0}
						<p class="text-sm text-ink-muted">
							The weekly board is quiet. Climb it by playing clashes.
						</p>
						<a href="/leaderboard" class="mt-4 action-button min-h-11 px-4 inline-flex items-center"
							>Leaderboard</a
						>
					{:else}
						<ol class="space-y-2">
							{#each board as row, i}
								<li class="flex items-center justify-between gap-3 min-h-11">
									<span class="text-sm text-ink truncate">
										<span class="font-display text-ink-muted mr-2">{i + 1}</span>
										{row.username}
									</span>
									<span class="font-display text-gold tabular-nums">{row.xp.toLocaleString()}</span>
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
