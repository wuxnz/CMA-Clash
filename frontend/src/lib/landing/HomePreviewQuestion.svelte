<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import { LEDGER_ANSWER_COLORS, LEDGER_ANSWER_SHAPES } from '$lib/ui/tokens';
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
		tagLine: 'CCMA · Anatomy',
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

	function toPayload(quizTitle: string, q: Question): PreviewPayload {
		const answers = (q.answers as Answer[]).slice(0, 4).map((a) => ({
			text: a.answer,
			right: Boolean(a.right)
		}));
		const shortTitle = quizTitle.length > 28 ? `${quizTitle.slice(0, 25)}…` : quizTitle;
		return {
			tagLine: `${certificationShortLabel('ccma')} · ${shortTitle}`,
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
		const list = (await res.json()) as QuizBrowseItem[];
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
			const quiz = await res.json();
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
		loadRandomQuestion();
	});

	function answerTileClass(index: number): string {
		const base =
			'rounded-xl p-3 sm:p-4 text-white min-h-[5.25rem] sm:min-h-[5.75rem] flex flex-col items-center justify-center gap-1.5 press-scale cursor-pointer border-2';
		if (!revealed) {
			return `${base} border-transparent`;
		}
		const ans = payload.answers[index];
		if (ans.right) {
			return `${base} border-gold ring-2 ring-gold/40`;
		}
		if (index === selectedIndex) {
			return `${base} border-white/70 opacity-80`;
		}
		return `${base} border-transparent opacity-60`;
	}
</script>

<div
	class="rounded-2xl bg-surface p-5 sm:p-7 w-full min-w-0 text-base sm:text-[1.0625rem]"
	aria-live="polite"
>
	<div class="flex items-center justify-between mb-4 sm:mb-5">
		<span class="font-display text-2xl sm:text-3xl text-gold">VS</span>
		<span class="text-base text-ink-muted tabular-nums font-medium">{questionNumber} / 12</span>
	</div>
	<p class="text-base sm:text-lg text-ink-muted mb-2 leading-snug">{payload.tagLine}</p>
	<p class="font-semibold text-ink mb-4 sm:mb-5 text-lg sm:text-xl leading-snug">
		{#if loading}
			<span class="text-ink-muted">Loading a sample question…</span>
		{:else}
			{@html normalizeQuizText(payload.question)}
		{/if}
	</p>
	<div class="grid grid-cols-2 gap-2.5 sm:gap-3">
		{#each payload.answers as a, i}
			<button
				type="button"
				class={answerTileClass(i)}
				style="background:{LEDGER_ANSWER_COLORS[i]}"
				disabled={loading || revealed}
				onclick={() => selectAnswer(i)}
			>
				<AnswerShapeIcon shape={LEDGER_ANSWER_SHAPES[i]} class="w-7 h-7 sm:w-8 sm:h-8 shrink-0" />
				<span
					class="font-display text-base sm:text-lg normal-case text-center leading-snug line-clamp-3 px-0.5"
					>{normalizeQuizText(a.text)}</span
				>
			</button>
		{/each}
	</div>
	{#if revealed && payload.explanation}
		<p class="mt-4 text-base text-ink-muted leading-relaxed">
			<span class="font-semibold text-ink">{lastCorrect ? 'Correct.' : 'Not quite.'}</span>
			{payload.explanation}
		</p>
	{/if}
	<div class="mt-4 sm:mt-5 text-center text-base text-ink-muted">
		{#if revealed}
			<button
				type="button"
				class="font-display text-gold normal-case hover:underline"
				onclick={nextQuestion}
			>
				Next question
			</button>
			<span class="mx-2" aria-hidden="true">·</span>
		{/if}
		<span class="font-display text-gold normal-case">{streak}</span> streak
		{#if revealed && lastCorrect}
			<span> · +240 XP</span>
		{/if}
	</div>
</div>
