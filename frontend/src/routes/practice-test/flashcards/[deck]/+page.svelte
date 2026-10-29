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
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	navbarVisible.visible = true;

	const QUESTIONS = data.deck.questions;
	const SECTIONS = data.deck.categories;
	const total = QUESTIONS.length;
	const LETTERS = ['A', 'B', 'C', 'D'];

	let picks = $state<(number | null)[]>(QUESTIONS.map(() => null));
	let submitted = $state(false);
	let confirmUnanswered = $state(false);

	const answered = $derived(picks.filter((p) => p !== null).length);
	const unanswered = $derived(total - answered);
	const correct = $derived(QUESTIONS.reduce((n, q, i) => n + (picks[i] === q.a ? 1 : 0), 0));
	const percent = $derived(Math.round((correct / total) * 100));

	const sectionTotals = $derived(
		SECTIONS.map((name, si) => {
			const indexes = QUESTIONS.map((_, i) => i).filter((i) => QUESTIONS[i].s === si);
			return {
				name,
				total: indexes.length,
				right: indexes.filter((i) => picks[i] === QUESTIONS[i].a).length
			};
		})
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

	function submitAnyway() {
		confirmUnanswered = false;
		submitted = true;
		window.scrollTo(0, 0);
	}

	function retake() {
		picks = QUESTIONS.map(() => null);
		submitted = false;
		confirmUnanswered = false;
		window.scrollTo(0, 0);
	}

	function isFirstOfSection(i: number) {
		return i === 0 || QUESTIONS[i - 1].s !== QUESTIONS[i].s;
	}

	function longestOption(i: number) {
		return Math.max(...QUESTIONS[i].o.map((o) => o.length));
	}
</script>

<svelte:head>
	<title>CMA Clash: {data.deck.title}</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-3xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<p class="text-sm text-ink-muted">
			<a href="/flashcards" class="link-hover text-ink-muted">Flashcards</a>
		</p>

		<div class="mt-4">
			<PageHeader
				eyebrow="Practice test"
				title={data.deck.title.replace(' practice test', '')}
				lede="No time limit. Work at your own pace. Every flashcard appears once. Answers and explanations appear when you submit, along with your score."
			/>
		</div>

		{#if !submitted}
			<div class="sticky top-0 z-10 bg-paper py-3 border-b border-line">
				<div class="h-1 bg-line">
					<div class="h-full bg-primary transition-[width] duration-200" style="width: {(answered / total) * 100}%"></div>
				</div>
				<p class="mt-2 text-xs font-mono text-ink-muted tabular-nums">{answered} of {total} answered</p>
			</div>

			{#each QUESTIONS as question, i (i)}
				{#if isFirstOfSection(i)}
					<h2 class="mt-10 text-xs font-mono uppercase tracking-[0.18em] text-ink-muted border-b border-line pb-2">
						{SECTIONS[question.s]}
					</h2>
				{/if}

				<Card class="mt-4" padding="sm">
					<p class="text-xs font-mono uppercase tracking-[0.16em] text-ink-subtle">
						Question {String(i + 1).padStart(2, '0')} of {total}
					</p>
					<p class="font-display text-lg sm:text-xl leading-snug mt-2 whitespace-pre-line text-balance">{question.q}</p>

					<div
						class="grid gap-px bg-line border border-line mt-4 {longestOption(i) > 60
							? 'grid-cols-1'
							: 'grid-cols-1 sm:grid-cols-2'}"
						role="radiogroup"
						aria-label="Question {i + 1}"
					>
						{#each question.o as option, j (j)}
							<button
								type="button"
								role="radio"
								aria-checked={picks[i] === j}
								class="bg-paper text-left min-h-[5.5rem] px-4 py-3 flex flex-col justify-between gap-3 text-ink press-scale transition-colors duration-200 {picks[i] === j
									? 'bg-primary-soft shadow-[inset_3px_0_0_0_var(--color-primary)]'
									: 'hover:bg-elevated'}"
								onclick={() => pick(i, j)}
							>
								<span
									class="font-mono text-[0.7rem] tracking-[0.2em] {picks[i] === j
										? 'text-primary'
										: 'text-ink-subtle'}">{LETTERS[j]}</span
								>
								<span class="text-sm sm:text-base font-medium leading-snug">{option}</span>
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
						<button type="button" class="link-hover text-ink underline underline-offset-4 ml-1" onclick={submitAnyway}>
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
			</Card>

			{#each QUESTIONS as question, i (i)}
				{@const pickedIndex = picks[i]}
				{@const isRight = pickedIndex === question.a}
				<Card
					class="mt-3 border-l-[3px] {pickedIndex === null
						? 'border-l-line-strong'
						: isRight
							? 'border-l-success'
							: 'border-l-danger'}"
					padding="sm"
				>
					<div class="flex items-center justify-between gap-4">
						<p class="text-xs font-mono uppercase tracking-[0.16em] text-ink-subtle">
							Question {String(i + 1).padStart(2, '0')}
						</p>
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
					<p class="font-display text-lg leading-snug mt-2 whitespace-pre-line">{question.q}</p>
					<dl class="mt-3 grid grid-cols-[7.5rem_1fr] gap-x-4 gap-y-1 text-sm">
						<dt class="font-mono text-[0.68rem] uppercase tracking-[0.12em] text-ink-subtle pt-0.5">Your answer</dt>
						<dd class="text-ink">{pickedIndex === null ? '(none)' : question.o[pickedIndex]}</dd>
						<dt class="font-mono text-[0.68rem] uppercase tracking-[0.12em] text-ink-subtle pt-0.5">Correct answer</dt>
						<dd class="text-ink">{question.o[question.a]}</dd>
					</dl>
					<p class="mt-3 pt-3 border-t border-line text-sm text-ink-muted leading-relaxed">{question.e}</p>
				</Card>
			{/each}

			<div class="mt-8">
				<Button variant="secondary" onclick={retake}>Take the test again</Button>
			</div>
		{/if}
	</div>
	<Footer />
</div>
