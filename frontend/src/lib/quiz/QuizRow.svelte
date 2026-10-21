<script lang="ts">
	import MediaComponent from '$lib/editor/MediaComponent.svelte';
	import { normalizeQuizText } from '$lib/cma/text';
	import Button from '$lib/ui/Button.svelte';
	import { certDotClass, prettyDifficulty } from './labels';
	import {
		quizColActions,
		quizColCert,
		quizColCertDot,
		quizColDifficulty,
		quizColQs,
		quizTableDataRow
	} from './quizTableLayout';
	import {
		Pencil,
		Ellipsis,
		Eye,
		ChartColumn,
		Download,
		Trash2
	} from '@lucide/svelte';

	export type QuizRowItem = {
		id: string;
		title?: string;
		cover_image?: string | null;
		public?: boolean;
		type?: 'quiz' | 'quiztivity';
		questions?: unknown;
		question_count?: number;
		difficulty?: string | null;
		certLabel?: string;
		plays?: number;
		user?: string | null;
		updated_at?: string | number | Date | null;
	};

	interface Props {
		quiz: QuizRowItem;
		mode?: 'owner' | 'browse';
		lastPlayed?: string | null;
		onHost?: (id: string) => void;
		onAnalytics?: (quiz: QuizRowItem) => void;
		onDelete?: (id: string, type: 'quiz' | 'quiztivity') => void;
		onDownload?: (id: string) => void;
	}

	let {
		quiz,
		mode = 'browse',
		lastPlayed = null,
		onHost,
		onAnalytics,
		onDelete,
		onDownload
	}: Props = $props();

	let menuOpen = $state(false);

	let count = $derived(
		Array.isArray(quiz.questions) ? quiz.questions.length : (quiz.question_count ?? 0)
	);
	let editHref = $derived(
		quiz.type === 'quiztivity' ? `/quiztivity/edit?id=${quiz.id}` : `/edit?quiz_id=${quiz.id}`
	);
	let playHref = $derived(quiz.type === 'quiztivity' ? `/quiztivity/play?id=${quiz.id}` : null);
	let viewHref = $derived(`/view/${quiz.id}`);
	let title = $derived(normalizeQuizText(quiz.title));
	let difficulty = $derived(prettyDifficulty(quiz.difficulty));
	let meta = $derived.by(() => {
		const parts: string[] = [];
		if (count) parts.push(`${count} q`);
		if (difficulty) parts.push(difficulty);
		if (mode === 'browse' && quiz.user) parts.push(quiz.user);
		if (mode === 'browse' && (quiz.plays ?? 0) > 0) parts.push(`${quiz.plays} plays`);
		if (mode === 'owner' && lastPlayed) parts.push(lastPlayed);
		return parts;
	});
	let byline = $derived.by(() => {
		if (mode !== 'browse') return '';
		const parts: string[] = [];
		if (quiz.user) parts.push(quiz.user);
		if ((quiz.plays ?? 0) > 0) parts.push(`${quiz.plays} plays`);
		return parts.join(' · ');
	});
</script>

<li class={quizTableDataRow} data-quiz-card>
	<div class="flex min-w-0 items-center gap-3" data-quiz-col="title">
		{#if quiz.cover_image}
			<div class="w-9 h-9 rounded-md overflow-hidden bg-elevated shrink-0 hidden sm:block">
				<MediaComponent src={quiz.cover_image} css_classes="w-full h-full object-cover" />
			</div>
		{/if}
		<div class="min-w-0">
			{#if mode === 'browse'}
				<a href={viewHref} class="text-sm font-medium text-ink truncate block link-hover visited:text-ink">{title}</a>
				{#if byline}
					<p class="hidden md:block text-xs text-ink-muted truncate mt-0.5">{byline}</p>
				{/if}
			{:else}
				<p class="text-sm font-medium text-ink truncate">{title}</p>
			{/if}
			<p class="md:hidden text-xs text-ink-muted mt-0.5 truncate">
				{#if quiz.certLabel}
					<span
						class="inline-block w-1.5 h-1.5 rounded-full {certDotClass(quiz.certLabel)} mr-1.5 align-middle"
					></span>{quiz.certLabel}{#if meta.length}<span> · </span>{/if}
				{/if}
				{meta.join(' · ')}
			</p>
		</div>
	</div>

	<p class={quizColCert} data-quiz-col="cert">
		{#if quiz.certLabel}
			<span class="{quizColCertDot} rounded-full {certDotClass(quiz.certLabel)}"></span>
			<span class="truncate">{quiz.certLabel}</span>
		{:else}
			<span class="{quizColCertDot}" aria-hidden="true"></span>
			<span class="text-ink-muted/60">—</span>
		{/if}
	</p>
	<p class={quizColQs} data-quiz-col="qs">{count || '—'}</p>
	<p class={quizColDifficulty} data-quiz-col="difficulty">
		{difficulty ?? '—'}
	</p>

	<div class={quizColActions} data-quiz-col="actions">
		{#if playHref}
			<Button href={playHref} variant="secondary" size="sm" class="w-auto">Play</Button>
		{:else if onHost}
			<Button variant="secondary" size="sm" class="w-auto" onclick={() => onHost(quiz.id)}>Host</Button>
		{:else}
			<Button href={viewHref} variant="secondary" size="sm" class="w-auto">View</Button>
		{/if}

		{#if mode === 'owner'}
			<a
				href={editHref}
				class="action-button min-h-11 min-w-11 hidden sm:inline-flex items-center justify-center"
				aria-label="Edit quiz"
			>
				<Pencil class="w-4 h-4" aria-hidden="true" />
			</a>
			<div class="relative">
				<button
					type="button"
					class="action-button min-h-11 min-w-11 inline-flex items-center justify-center"
					aria-label="More actions"
					aria-expanded={menuOpen}
					onclick={() => (menuOpen = !menuOpen)}
				>
					<Ellipsis class="w-4 h-4" aria-hidden="true" />
				</button>
				{#if menuOpen}
					<button
						type="button"
						class="fixed inset-0 z-20 cursor-default"
						aria-label="Close menu"
						onclick={() => (menuOpen = false)}
					></button>
					<ul
						class="absolute right-0 top-full mt-1 z-30 w-44 rounded-lg bg-elevated shadow-[var(--shadow-card)] py-1 text-sm"
					>
						<li class="sm:hidden">
							<a
								href={editHref}
								class="flex items-center gap-2 px-3 py-2.5 min-h-11 text-ink"
								onclick={() => (menuOpen = false)}
							>
								<Pencil class="w-4 h-4" aria-hidden="true" /> Edit
							</a>
						</li>
						{#if quiz.public}
							<li>
								<a
									href={viewHref}
									class="flex items-center gap-2 px-3 py-2.5 min-h-11 text-ink"
									onclick={() => (menuOpen = false)}
								>
									<Eye class="w-4 h-4" aria-hidden="true" /> View
								</a>
							</li>
						{/if}
						{#if onAnalytics}
							<li>
								<button
									type="button"
									class="flex items-center gap-2 px-3 py-2.5 min-h-11 w-full text-left text-ink"
									onclick={() => {
										menuOpen = false;
										onAnalytics(quiz);
									}}
								>
									<ChartColumn class="w-4 h-4" aria-hidden="true" /> Analytics
								</button>
							</li>
						{/if}
						{#if quiz.type !== 'quiztivity' && onDownload}
							<li>
								<button
									type="button"
									class="flex items-center gap-2 px-3 py-2.5 min-h-11 w-full text-left text-ink"
									onclick={() => {
										menuOpen = false;
										onDownload(quiz.id);
									}}
								>
									<Download class="w-4 h-4" aria-hidden="true" /> Download
								</button>
							</li>
						{/if}
						{#if onDelete}
							<li>
								<button
									type="button"
									class="flex items-center gap-2 px-3 py-2.5 min-h-11 w-full text-left text-danger"
									onclick={() => {
										menuOpen = false;
										onDelete(quiz.id, quiz.type === 'quiztivity' ? 'quiztivity' : 'quiz');
									}}
								>
									<Trash2 class="w-4 h-4" aria-hidden="true" /> Delete
								</button>
							</li>
						{/if}
					</ul>
				{/if}
			</div>
		{/if}
	</div>
</li>
