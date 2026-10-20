<script lang="ts">
	import MediaComponent from '$lib/editor/MediaComponent.svelte';
	import { normalizeQuizText } from '$lib/cma/text';
	import {
		Pencil,
		Ellipsis,
		Eye,
		ChartColumn,
		Download,
		Trash2
	} from '@lucide/svelte';

	interface QuizItem {
		id: string;
		title?: string;
		description?: string;
		cover_image?: string;
		public?: boolean;
		type?: 'quiz' | 'quiztivity';
		questions?: unknown;
		question_count?: number;
		difficulty?: string | null;
		certLabel?: string;
		plays?: number;
		updated_at?: string | number | Date | null;
	}

	interface Props {
		quiz: QuizItem;
		lastPlayed?: string | null;
		onHost: (id: string) => void;
		onAnalytics: (quiz: QuizItem) => void;
		onDelete: (id: string, type: 'quiz' | 'quiztivity') => void;
		onDownload: (id: string) => void;
	}

	let { quiz, lastPlayed = null, onHost, onAnalytics, onDelete, onDownload }: Props = $props();

	let menuOpen = $state(false);

	let count = $derived(
		Array.isArray(quiz.questions) ? quiz.questions.length : (quiz.question_count ?? 0)
	);
	let editHref = $derived(
		quiz.type === 'quiztivity' ? `/quiztivity/edit?id=${quiz.id}` : `/edit?quiz_id=${quiz.id}`
	);
	let playHref = $derived(quiz.type === 'quiztivity' ? `/quiztivity/play?id=${quiz.id}` : null);

	function certDot(label?: string): string {
		const s = (label ?? '').toLowerCase();
		if (s.includes('ekg')) return 'bg-cyan';
		if (s.includes('phleb')) return 'bg-gold';
		if (s.includes('bls') || s.includes('cpr')) return 'bg-signal';
		if (s.includes('skill')) return 'bg-ink-muted';
		return 'bg-violet';
	}
</script>

<li
	class="grid grid-cols-[1fr_auto] md:grid-cols-[minmax(0,1.4fr)_6.5rem_3.5rem_7rem_auto] items-center gap-x-3 gap-y-1 py-3 border-b border-white/[0.07] min-w-0"
	data-quiz-card
>
	<div class="flex items-center gap-3 min-w-0">
		{#if quiz.cover_image}
			<div class="w-9 h-9 rounded-md overflow-hidden bg-elevated shrink-0 hidden sm:block">
				<MediaComponent src={quiz.cover_image} css_classes="w-full h-full object-cover" />
			</div>
		{/if}
		<div class="min-w-0">
			<p class="text-sm font-medium text-ink truncate">{normalizeQuizText(quiz.title)}</p>
			<p class="md:hidden text-xs text-ink-muted mt-0.5 truncate">
				{#if quiz.certLabel}
					<span class="inline-block w-1.5 h-1.5 rounded-full {certDot(quiz.certLabel)} mr-1.5 align-middle"
					></span>{quiz.certLabel}
					<span class="text-ink-muted/80"> · </span>
				{/if}
				{count} q{#if quiz.difficulty}<span> · {quiz.difficulty}</span>{/if}
				{#if lastPlayed}<span> · {lastPlayed}</span>{/if}
			</p>
		</div>
	</div>

	<p class="hidden md:flex items-center gap-2 text-xs text-ink-muted min-w-0">
		{#if quiz.certLabel}
			<span class="inline-block w-1.5 h-1.5 rounded-full {certDot(quiz.certLabel)} shrink-0"></span>
			<span class="truncate">{quiz.certLabel}</span>
		{:else}
			<span class="text-ink-muted/60">—</span>
		{/if}
	</p>
	<p class="hidden md:block text-xs text-ink-muted tabular-nums">{count}</p>
	<p class="hidden md:block text-xs text-ink-muted truncate">{quiz.difficulty ?? '—'}</p>

	<div class="flex items-center justify-end gap-1">
		{#if playHref}
			<a
				href={playHref}
				class="action-button min-h-11 px-3 inline-flex items-center justify-center text-sm"
			>
				Play
			</a>
		{:else}
			<button
				type="button"
				class="action-button min-h-11 px-3 inline-flex items-center justify-center text-sm"
				onclick={() => onHost(quiz.id)}
			>
				Host
			</button>
		{/if}
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
					{#if quiz.public && quiz.type === 'quiz'}
						<li>
							<a
								href="/view/{quiz.id}"
								class="flex items-center gap-2 px-3 py-2.5 min-h-11 text-ink"
								onclick={() => (menuOpen = false)}
							>
								<Eye class="w-4 h-4" aria-hidden="true" /> View
							</a>
						</li>
					{/if}
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
					{#if quiz.type === 'quiz'}
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
				</ul>
			{/if}
		</div>
	</div>
</li>
