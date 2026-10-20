<script lang="ts">
	import MediaComponent from '$lib/editor/MediaComponent.svelte';
	import { normalizeQuizText } from '$lib/cma/text';
	import {
		Play,
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
	}

	interface Props {
		quiz: QuizItem;
		enterDelay?: number;
		onHost: (id: string) => void;
		onAnalytics: (quiz: QuizItem) => void;
		onDelete: (id: string, type: 'quiz' | 'quiztivity') => void;
		onDownload: (id: string) => void;
	}

	let { quiz, enterDelay = 0, onHost, onAnalytics, onDelete, onDownload }: Props = $props();

	let menuOpen = $state(false);

	let count = $derived(
		Array.isArray(quiz.questions) ? quiz.questions.length : (quiz.question_count ?? 0)
	);
	let editHref = $derived(
		quiz.type === 'quiztivity' ? `/quiztivity/edit?id=${quiz.id}` : `/edit?quiz_id=${quiz.id}`
	);
	let playHref = $derived(quiz.type === 'quiztivity' ? `/quiztivity/play?id=${quiz.id}` : null);
</script>

<article
	class="arena-enter rounded-2xl bg-surface shadow-[var(--shadow-card)] overflow-hidden flex flex-col min-w-0 card-interactive"
	style="animation-delay: {enterDelay}ms"
	data-quiz-card
>
	<div class="relative h-24 bg-elevated overflow-hidden">
		{#if quiz.cover_image}
			<MediaComponent
				src={quiz.cover_image}
				css_classes="absolute inset-0 w-full h-full object-cover"
			/>
		{:else}
			<div
				class="absolute inset-0 flex items-end p-3"
				style="background: radial-gradient(80% 120% at 100% 0%, rgba(123,92,255,0.45), transparent 55%), #1b2338;"
				aria-hidden="true"
			>
				<span class="font-display text-3xl text-ink/80 leading-none">
					{quiz.certLabel ?? 'Quiz'}
				</span>
			</div>
		{/if}
		{#if quiz.certLabel}
			<span
				class="absolute top-2 left-2 rounded-md bg-paper/80 px-2 py-1 text-[11px] font-display tracking-wide text-cyan"
			>
				{quiz.certLabel}
			</span>
		{/if}
	</div>

	<div class="flex flex-col gap-2 p-4 flex-1 min-w-0">
		<h3 class="font-display text-xl text-ink leading-tight normal-case truncate">
			{normalizeQuizText(quiz.title)}
		</h3>
		<p class="text-sm text-ink-muted">
			{count} {count === 1 ? 'question' : 'questions'}
			{#if quiz.difficulty}
				<span class="text-ink-muted/70"> · {quiz.difficulty}</span>
			{/if}
		</p>

		<div class="mt-auto flex items-center gap-2 pt-2">
			{#if playHref}
				<a
					href={playHref}
					class="action-button min-h-11 px-4 inline-flex items-center justify-center gap-2 flex-1"
				>
					<Play class="w-4 h-4" aria-hidden="true" />
					Play
				</a>
			{:else}
				<button
					type="button"
					class="action-button min-h-11 px-4 inline-flex items-center justify-center gap-2 flex-1"
					onclick={() => onHost(quiz.id)}
				>
					<Play class="w-4 h-4" aria-hidden="true" />
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
						class="absolute right-0 bottom-full mb-2 z-30 w-44 rounded-xl bg-elevated shadow-[var(--shadow-card)] py-1 text-sm"
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
	</div>
</article>
