<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import DownloadQuiz from '$lib/components/DownloadQuiz.svelte';
	import { getLocalization } from '$lib/i18n';
	import CollapsSection from '$lib/collapsible.svelte';
	import { QuizQuestionType } from '$lib/quiz_types.js';
	import StartGamePopup from '$lib/dashboard/start_game.svelte';
	import Spinner from '$lib/Spinner.svelte';
	import MediaComponent from '$lib/editor/MediaComponent.svelte';
	import RatingComponent from '$lib/view_quiz/RatingComponent.svelte';
	import { page } from '$app/state';
	import ModComponent from './ModComponent.svelte';
	import Button from '$lib/ui/Button.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import { normalizeQuizText } from '$lib/cma/text';
	import { LEDGER_ANSWER_COLORS } from '$lib/ui/tokens';

	navbarVisible.visible = true;

	let start_game = $state(null);
	let download_id: string | null = $state(null);
	const urlparams = page.url.searchParams;
	const mod_view = Boolean(urlparams.get('mod'));
	const auto_expand = Boolean(urlparams.get('autoExpand'));
	const auto_return = Boolean(urlparams.get('autoReturn'));

	const { t } = getLocalization();
	let { data } = $props();
	let { quiz, logged_in }: { quiz: QuizData; logged_in: boolean } = $state(data);

	interface Question {
		time: string;
		question: string;
		image?: string;
		answers: Answer[];
		type?: string;
	}

	interface Answer {
		right: boolean;
		answer: string;
		color?: string;
		min?: number;
		max?: number;
		min_correct?: number;
		max_correct?: number;
	}

	interface QuizData {
		id: string;
		public: boolean;
		title: string;
		description: string;
		created_at: string;
		updated_at: string;
		user_id: string | { id: string; username?: string };
		imported_from_kahoot?: boolean;
		questions: Question[];
		kahoot_id?: string;
		mod_rating?: number;
		cover_image?: string | null;
	}

	const author = $derived(
		typeof quiz.user_id === 'object' && quiz.user_id
			? quiz.user_id
			: { id: String(quiz.user_id), username: '' }
	);
</script>

<svelte:head>
	<title>CMA Clash — {normalizeQuizText(quiz.title)}</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-3xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">
			{normalizeQuizText(quiz.title)}
		</h1>
		{#if quiz.description}
			<p class="text-sm text-ink-muted mt-2 leading-relaxed">{@html quiz.description}</p>
		{/if}
		<p class="text-sm text-ink-muted mt-2">
			{$t('view_quiz_page.made_by')}
			<a href="/user/{author.id}" class="text-ink link-hover">@{author.username}</a>
			{#if quiz.imported_from_kahoot}
				<span> · Imported from Kahoot</span>
			{/if}
		</p>

		{#if quiz.cover_image}
			<div class="mt-6 rounded-lg overflow-hidden bg-elevated max-h-48">
				<img
					class="max-h-48 w-full object-cover"
					src="/api/v1/storage/download/{quiz.cover_image}"
					alt=""
				/>
			</div>
		{/if}

		<div class="mt-6 flex flex-wrap gap-2">
			<RatingComponent bind:quiz />
			{#if mod_view}
				<ModComponent autoReturn={auto_return} quiz_id={quiz.id} />
			{/if}
		</div>

		<div class="mt-6 flex flex-col sm:flex-row flex-wrap gap-2">
			{#if quiz.imported_from_kahoot && quiz.kahoot_id}
				<Button
					href="https://create.kahoot.it/details/{quiz.kahoot_id}"
					variant="secondary"
					class="w-full sm:w-auto"
				>
					{$t('view_quiz_page.view_on_kahoot')}
				</Button>
			{/if}
			<Button class="w-full sm:w-auto" onclick={() => (start_game = quiz.id)}>Host</Button>
			<Button href="/practice?quiz_id={quiz.id}" variant="secondary" class="w-full sm:w-auto">
				{$t('words.practice')}
			</Button>
			{#if logged_in}
				<Button variant="ghost" class="w-full sm:w-auto" onclick={() => (download_id = quiz.id)}>
					{$t('words.download')}
				</Button>
			{/if}
		</div>
		<p class="mt-3">
			<a href="mailto:abuse@example.com?subject=Report quiz {quiz.id}" class="text-sm text-ink-muted link-hover">
				{$t('words.report')}
			</a>
		</p>

		<div class="mt-10">
			<h2 class="text-sm font-semibold text-ink mb-2">Questions</h2>
			{#each quiz.questions as question, index_question}
				<div class="border-b border-white/[0.07]">
					<CollapsSection headerText={`${index_question + 1}. ${question.question}`} expanded={auto_expand}>
						<div class="pb-4 pt-1">
							{#if question.image}
								<MediaComponent css_classes="mx-auto max-h-48" src={question.image} muted={true} />
							{/if}
							<p class="text-xs text-ink-muted mt-2">{question.time}s</p>
							{#if question.type === QuizQuestionType.ABCD || question.type === undefined || question.type === QuizQuestionType.CHECK}
								<ul class="mt-3 space-y-2">
									{#each question.answers as answer, index_answer}
										<li class="flex items-start gap-2 text-sm min-w-0">
											<span
												class="mt-1.5 w-2 h-2 rounded-full shrink-0"
												style="background:{answer.color ?? LEDGER_ANSWER_COLORS[index_answer % 4]}"
											></span>
											<span class="text-ink min-w-0">
												{answer.answer}
												{#if answer.right && question.type !== QuizQuestionType.VOTING}
													<span class="text-ink-muted"> · correct</span>
												{/if}
											</span>
										</li>
									{/each}
								</ul>
							{:else if question.type === QuizQuestionType.RANGE}
								<p class="mt-2 text-sm text-ink-muted">
									Correct between {question.answers.min_correct} and {question.answers.max_correct}
									(selectable {question.answers.min}–{question.answers.max}).
								</p>
							{:else if question.type === QuizQuestionType.ORDER}
								<ol class="mt-3 space-y-1 text-sm text-ink list-decimal pl-5">
									{#each question.answers as answer}
										<li>{answer.answer}</li>
									{/each}
								</ol>
							{:else if question.type === QuizQuestionType.VOTING || question.type === QuizQuestionType.TEXT}
								<ul class="mt-3 space-y-1 text-sm text-ink">
									{#each question.answers as answer}
										<li>{answer.answer}</li>
									{/each}
								</ul>
							{:else if question.type === QuizQuestionType.SLIDE}
								{#await import('$lib/play/admin/slide.svelte')}
									<Spinner my_20={false} />
								{:then c}
									<c.default question={quiz.questions[index_question]} />
								{/await}
							{/if}
						</div>
					</CollapsSection>
				</div>
			{/each}
		</div>
	</div>
	<Footer />
</div>

{#if start_game !== null}
	<StartGamePopup bind:quiz_id={start_game} title={normalizeQuizText(quiz.title)} />
{/if}

<DownloadQuiz bind:quiz_id={download_id} />
