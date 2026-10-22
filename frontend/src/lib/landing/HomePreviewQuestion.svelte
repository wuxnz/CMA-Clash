<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { certificationShortLabel, type QuizBrowseItem } from '$lib/cma/client';
	import { QuizQuestionType, type Answer, type Question } from '$lib/quiz_types';
	import { normalizeQuizText } from '$lib/cma/text';
	import { onMount } from 'svelte';

	type PreviewAnswer = { text: string; right: boolean };

	type PreviewPayload = {
		tagLine: string;
		question: string;
		answers: PreviewAnswer[];
		explanation: string | null;
	};

	const STATIC_FALLBACK: PreviewPayload = {
		tagLine: 'CCMA — Anatomy',
		question: 'Which chamber of the heart receives oxygenated blood from the pulmonary veins?',
		answers: [
			{ text: 'Left ventricle', right: false },
			{ text: 'Right atrium', right: false },
			{ text: 'Left atrium', right: true },
			{ text: 'Right ventricle', right: false }
		],
		explanation:
			'Oxygenated blood from the pulmonary veins enters the left atrium before passing to the left ventricle.'
	};

	let loading = $state(true);
	let payload = $state<PreviewPayload>(STATIC_FALLBACK);
	let selectedIndex = $state<number | null>(null);
	let streak = $state(0);
	let questionNumber = $state(1);
	let quizPool = $state<QuizBrowseItem[] | null>(null);

	const revealed = $derived(selectedIndex !== null);
	const lastCorrect = $derived(
		selectedIndex !== null && payload.answers[selectedIndex]?.right === true
	);

	async function sleep(ms: number) {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}

	async function fetchWithRetry(url: string, attempts = 4): Promise<Response | null> {
		for (let i = 0; i < attempts; i++) {
			try {
				const res = await fetch(url);
				if (res.ok) {
					return res;
				}
				if (res.status >= 500 && i < attempts - 1) {
					await sleep(1500 * (i + 1));
					continue;
				}
				return res;
			} catch {
				if (i < attempts - 1) {
					await sleep(1500 * (i + 1));
					continue;
				}
			}
		}
		return null;
	}

	function pickAbcdQuestion(questions: Question[]): Question | null {
		const abcd = questions.filter(
			(q) =>
				(q.type === QuizQuestionType.ABCD || q.type === undefined) &&
				Array.isArray(q.answers) &&
				q.answers.length >= 2 &&
				q.answers.length <= 4
		);
		if (!abcd.length) {
			return null;
		}
		return abcd[Math.floor(Math.random() * abcd.length)];
	}

	/** Shorten a quiz title on a word boundary so the eyebrow never ends mid-word. */
	function truncateTitle(title: string, max = 28): string {
		if (title.length <= max) {
			return title;
		}
		const clipped = title.slice(0, max - 1);
		const lastSpace = clipped.lastIndexOf(' ');
		const base = lastSpace > 12 ? clipped.slice(0, lastSpace) : clipped;
		return `${base.replace(/[\s.,;:—–-]+$/, '')}…`;
	}

	function toPayload(quizTitle: string, q: Question): PreviewPayload {
		const answers = (q.answers as Answer[]).slice(0, 4).map((a) => ({
			text: a.answer,
			right: Boolean(a.right)
		}));
		const shortTitle = truncateTitle(quizTitle);
		return {
			tagLine: `${certificationShortLabel('ccma')} — ${shortTitle}`,
			question: q.question,
			answers,
			explanation: q.explanation ?? null
		};
	}

	async function ensureQuizPool(): Promise<QuizBrowseItem[]> {
		if (quizPool?.length) {
			return quizPool;
		}
		const res = await fetchWithRetry(
			'/api/v1/clash/quizzes?certification_slug=ccma&page_size=30'
		);
		if (!res?.ok) {
			return [];
		}
		let list: QuizBrowseItem[];
		try {
			list = (await res.json()) as QuizBrowseItem[];
		} catch {
			return [];
		}
		if (!Array.isArray(list)) {
			return [];
		}
		quizPool = list.filter((q) => q.question_count > 0);
		return quizPool;
	}

	async function loadRandomQuestion(useFallbackOnFailure = true) {
		loading = true;
		selectedIndex = null;
		const pool = await ensureQuizPool();
		if (!pool.length) {
			if (useFallbackOnFailure) {
				payload = STATIC_FALLBACK;
			}
			loading = false;
			return;
		}

		const tries = Math.min(5, pool.length);
		const shuffled = [...pool].sort(() => Math.random() - 0.5);
		for (let i = 0; i < tries; i++) {
			const item = shuffled[i];
			const res = await fetchWithRetry(`/api/v1/quiz/get/public/${item.id}`);
			if (!res?.ok) {
				continue;
			}
			let quiz: { questions?: Question[] };
			try {
				quiz = (await res.json()) as { questions?: Question[] };
			} catch {
				continue;
			}
			const picked = pickAbcdQuestion(quiz.questions ?? []);
			if (!picked) {
				continue;
			}
			payload = toPayload(item.title, picked);
			loading = false;
			return;
		}

		if (useFallbackOnFailure) {
			payload = STATIC_FALLBACK;
		}
		loading = false;
	}

	function selectAnswer(index: number) {
		if (loading || revealed) {
			return;
		}
		selectedIndex = index;
		if (payload.answers[index]?.right) {
			streak += 1;
		} else {
			streak = 0;
		}
	}

	function nextQuestion() {
		questionNumber += 1;
		loadRandomQuestion();
	}

	onMount(() => {
		void loadRandomQuestion();
	});

	function answerTileClass(index: number): string {
		const base =
			'rounded-none p-4 sm:p-5 text-ink min-h-[6rem] sm:min-h-[7rem] flex flex-col items-start justify-between gap-3 press-scale cursor-pointer border-l-2 text-left transition-colors duration-200';
		if (!revealed) {
			return `${base} border-line bg-paper hover:bg-elevated`;
		}
		const ans = payload.answers[index];
		if (ans.right) {
			return `${base} border-success bg-success/10`;
		}
		if (index === selectedIndex) {
			return `${base} border-danger bg-danger/10`;
		}
		return `${base} border-line bg-paper opacity-50`;
	}
</script>

<div
	class="border border-line bg-paper p-5 sm:p-8 w-full min-w-0"
	aria-live="polite"
	data-testid="home-preview-question"
>
	<div class="flex items-center justify-between pb-4 border-b border-line">
		<span class="font-mono text-[0.66rem] tracking-[0.2em] text-primary">Sample item</span>
		<span class="font-mono text-xs text-ink-muted tabular-nums">{questionNumber} / 12</span>
	</div>

	<p class="eyebrow mt-5">{payload.tagLine}</p>
	<p class="font-display text-xl sm:text-2xl leading-snug mt-2 text-ink">
		{#if loading}
			<span class="text-ink-muted">Loading a sample question.</span>
		{:else}
			{@html normalizeQuizText(payload.question)}
		{/if}
	</p>

	<div class="grid grid-cols-2 gap-2.5 sm:gap-3 mt-5">
		{#each payload.answers as a, i}
			<button
				type="button"
				class={answerTileClass(i)}
				disabled={loading || revealed}
				onclick={() => selectAnswer(i)}
			>
				<span class="font-mono text-[0.66rem] tracking-[0.18em] text-ink-subtle"
					>{String.fromCharCode(65 + i)}</span
				>
				<span class="text-sm sm:text-base leading-snug line-clamp-3"
					>{normalizeQuizText(a.text)}</span
				>
			</button>
		{/each}
	</div>

	{#if revealed && payload.explanation}
		<p
			class="mt-5 pt-4 border-t border-line text-sm sm:text-base text-ink-muted leading-relaxed"
		>
			<span class="text-ink font-semibold">{lastCorrect ? 'Correct.' : 'Not quite.'}</span>
			{payload.explanation}
		</p>
	{/if}

	<div
		class="mt-5 pt-4 border-t border-line flex flex-wrap items-center gap-3 text-sm text-ink-muted"
	>
		{#if revealed}
			<button
				type="button"
				class="font-mono text-[0.68rem] tracking-[0.18em] text-primary hover:underline"
				onclick={nextQuestion}
			>
				Next question
			</button>
			<span aria-hidden="true">·</span>
		{/if}
		<span class="font-mono text-[0.68rem] tracking-[0.18em] text-ink-subtle"
			>{streak} streak</span
		>
		{#if revealed && lastCorrect}
			<span class="font-mono text-[0.68rem] tracking-[0.18em] text-success">+240 XP</span>
		{/if}
	</div>
</div>
