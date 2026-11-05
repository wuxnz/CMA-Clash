<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import Button from '$lib/ui/Button.svelte';
	import Card from '$lib/ui/Card.svelte';
	import PageHeader from '$lib/ui/PageHeader.svelte';
	import { fitText } from '$lib/ui/fit-text';
	import type { TestCard } from '$lib/study/diabetes-test-2nd-half';

	interface Props {
		title: string;
		cards: TestCard[];
		categories: string[];
		backHref: string;
		backLabel: string;
	}

	let { title, cards, categories, backHref, backLabel }: Props = $props();

	navbarVisible.visible = true;

	const LETTERS = ['A', 'B', 'C', 'D'];
	const total = cards.length;

	type PracticeQuestion = { s: number; q: string; o: string[]; a: number; e: string; u: string; src: string };

	// Fisher–Yates shuffle with Math.random, so every visit has a new question order and new option order.
	function shuffle<T>(items: T[]): T[] {
		const out = [...items];
		for (let i = out.length - 1; i > 0; i--) {
			const j = Math.floor(Math.random() * (i + 1));
			[out[i], out[j]] = [out[j], out[i]];
		}
		return out;
	}

	function buildTest(): PracticeQuestion[] {
		return shuffle(cards).map((card) => {
			const options = shuffle([card.d, ...card.w]);
			return { s: card.c, q: card.t, o: options, a: options.indexOf(card.d), e: card.e, u: card.u, src: card.s };
		});
	}

	let questions = $state<PracticeQuestion[]>(buildTest());
	let picks = $state<(number | null)[]>(cards.map(() => null));
	let submitted = $state(false);
	let confirmUnanswered = $state(false);

	const answered = $derived(picks.filter((p) => p !== null).length);
	const unanswered = $derived(total - answered);
	const correct = $derived(questions.reduce((n, q, i) => n + (picks[i] === q.a ? 1 : 0), 0));
	const percent = $derived(Math.round((correct / total) * 100));

	const sectionTotals = $derived(
		categories
			.map((name, si) => {
				const indexes = questions.map((_, i) => i).filter((i) => questions[i].s === si);
				return {
					name,
					total: indexes.length,
					right: indexes.filter((i) => picks[i] === questions[i].a).length
				};
			})
			.filter((section) => section.total > 0)
	);

	function pick(i: number, j: number) {
		if (!submitted) picks[i] = j;
	}

	function submit() {
		if (unanswered > 0 && !confirmUnanswered) {
			confirmUnanswered = true;
			return;
		}
		confirmUnanswered = false;
		submitted = true;
		window.scrollTo(0, 0);
	}

	function retake() {
		questions = buildTest();
		picks = questions.map(() => null);
		submitted = false;
		confirmUnanswered = false;
		window.scrollTo(0, 0);
	}

	function longestOption(i: number) {
		return Math.max(...questions[i].o.map((o) => o.length));
	}
</script>

<svelte:head>
	<title>CMA Clash: {title} practice test</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-3xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<p class="text-sm text-ink-muted">
			<a href={backHref} class="link-hover text-ink-muted">{backLabel}</a>
		</p>

		<div class="mt-4">
			<PageHeader
				eyebrow="Practice test"
				{title}
				lede="No time limit. Questions and answer choices are shuffled on every visit. Answers and explanations appear when you submit, along with your score."
			/>
		</div>

		{#if !submitted}
			<div class="sticky top-0 z-10 bg-paper py-3 border-b border-line">
				<div class="h-1 bg-line">
					<div class="h-full bg-primary transition-[width] duration-200" style="width: {(answered / total) * 100}%"></div>
				</div>
				<p class="mt-2 text-xs font-mono text-ink-muted tabular-nums">{answered} of {total} answered</p>
			</div>

			{#each questions as question, i (question.q + i)}
				<Card class="mt-4" padding="sm">
					<p class="text-xs font-mono uppercase tracking-[0.16em] text-ink-subtle">
						Question {String(i + 1).padStart(3, '0')} of {total}
					</p>
					<p class="font-display text-lg sm:text-xl leading-snug mt-2 text-balance">{question.q}</p>

					<div
						class="grid gap-px bg-line border border-line mt-4 auto-rows-fr {longestOption(i) > 60 ? 'grid-cols-1' : 'grid-cols-1 sm:grid-cols-2'}"
						role="radiogroup"
						aria-label="Question {i + 1}"
					>
						{#each question.o as option, j (j)}
							<button
								type="button"
								role="radio"
								aria-checked={picks[i] === j}
								class="bg-paper text-left min-h-[7.5rem] sm:min-h-[8rem] px-4 py-3 flex flex-col justify-between gap-3 text-ink press-scale transition-colors duration-200 {picks[i] === j
									? 'bg-primary-soft shadow-[inset_3px_0_0_0_var(--color-primary)]'
									: 'hover:bg-elevated'}"
								onclick={() => pick(i, j)}
							>
								<span class="font-mono text-[0.7rem] tracking-[0.2em] {picks[i] === j ? 'text-primary' : 'text-ink-subtle'}">{LETTERS[j]}</span>
								<span class="block text-sm sm:text-base font-medium leading-snug wrap-break-word" use:fitText={{ min: 11, max: 18 }}>{option}</span>
							</button>
						{/each}
					</div>
				</Card>
			{/each}

			<div class="sticky bottom-0 mt-10 py-4 bg-paper border-t border-line">
				<div class="flex flex-wrap items-center justify-between gap-4">
					<p class="text-xs font-mono text-ink-muted tabular-nums">
						{unanswered > 0 ? `${unanswered} unanswered` : 'All questions answered'}
					</p>
					<Button onclick={submit}>Submit test</Button>
				</div>
				{#if confirmUnanswered}
					<p class="mt-3 text-sm text-ink-muted" role="alert">
						{unanswered} question{unanswered === 1 ? '' : 's'} unanswered. They will count as wrong.
						<button
							type="button"
							class="link-hover text-ink underline underline-offset-4 ml-1"
							onclick={() => {
								confirmUnanswered = false;
								submitted = true;
								window.scrollTo(0, 0);
							}}
						>
							Submit anyway
						</button>
					</p>
				{/if}
			</div>
		{:else}
			<Card class="mt-8" padding="lg">
				<p class="text-xs font-mono uppercase tracking-[0.16em] text-ink-muted">Your score</p>
				<p class="font-display text-6xl leading-none mt-3 tabular-nums">
					{correct}<span class="text-2xl text-ink-muted"> / {total} · {percent}%</span>
				</p>
				<div class="grid grid-cols-2 gap-px bg-line border border-line mt-6">
					{#each sectionTotals as section (section.name)}
						<div class="bg-paper p-4">
							<p class="text-xs font-mono uppercase tracking-[0.14em] text-ink-muted">{section.name}</p>
							<p class="font-display text-2xl mt-1 tabular-nums">{section.right} / {section.total}</p>
						</div>
					{/each}
				</div>
				<div class="mt-6">
					<Button variant="secondary" onclick={retake}>Take a new shuffled test</Button>
				</div>
			</Card>

			{#each questions as question, i (question.q + i)}
				{@const pickedIndex = picks[i]}
				{@const isRight = pickedIndex === question.a}
				<Card
					class="mt-3 border-l-[3px] {pickedIndex === null ? 'border-l-line-strong' : isRight ? 'border-l-success' : 'border-l-danger'}"
					padding="sm"
				>
					<div class="flex items-center justify-between gap-4">
						<p class="text-xs font-mono uppercase tracking-[0.16em] text-ink-subtle">Question {String(i + 1).padStart(3, '0')}</p>
						<p
							class="text-xs font-mono uppercase tracking-[0.16em] {pickedIndex === null
								? 'text-ink-subtle'
								: isRight
									? 'text-success'
									: 'text-danger'}"
						>
							{pickedIndex === null ? 'Unanswered' : isRight ? 'Correct' : 'Incorrect'}
						</p>
					</div>
					<p class="font-display text-lg leading-snug mt-2">{question.q}</p>
					<dl class="mt-3 grid grid-cols-[7.5rem_1fr] gap-x-4 gap-y-1 text-sm">
						<dt class="text-ink-muted">Correct answer</dt>
						<dd class="text-ink">{question.o[question.a]}</dd>
						{#if pickedIndex !== null && !isRight}
							<dt class="text-ink-muted">Your answer</dt>
							<dd class="text-danger">{question.o[pickedIndex]}</dd>
						{/if}
					</dl>
					<p class="text-sm text-ink-muted mt-3 leading-relaxed">{question.e}</p>
					<p class="text-xs text-ink-subtle mt-2">
						Source: <a href={question.u} class="link-hover underline underline-offset-4" target="_blank" rel="noopener noreferrer">{question.src}</a>
					</p>
				</Card>
			{/each}
		{/if}
	</div>
	<Footer />
</div>
