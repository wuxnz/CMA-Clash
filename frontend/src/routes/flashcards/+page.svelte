<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import Button from '$lib/ui/Button.svelte';
	import { fitText } from '$lib/ui/fit-text';
	import Card from '$lib/ui/Card.svelte';
	import PageHeader from '$lib/ui/PageHeader.svelte';
	import {
		FLASHCARDS,
		FLASHCARD_CATEGORIES,
		type Flashcard
	} from '$lib/study/phlebotomy-flashcards';
	import {
		DIABETES_FLASHCARDS,
		DIABETES_FLASHCARD_CATEGORIES
	} from '$lib/study/diabetes-flashcards';

	navbarVisible.visible = true;

	const DECKS = [
		{
			id: 'phlebotomy',
			label: 'Phlebotomy',
			title: 'Phlebotomy terms',
			lede: 'Flip a card to check the definition. Use the arrow keys to move, Space to flip, and mark a term known when you have it.',
			cards: FLASHCARDS,
			categories: FLASHCARD_CATEGORIES
		},
		{
			id: 'diabetes',
			label: 'Diabetes',
			title: 'Diabetes facts',
			lede: 'Facts from the CDC diabetes pages. Flip a card to check the answer. Use the arrow keys to move, Space to flip, and mark a card known when you have it.',
			cards: DIABETES_FLASHCARDS,
			categories: DIABETES_FLASHCARD_CATEGORIES
		}
	];

	let deckId = $state(DECKS[0].id);
	const deckDef = $derived(DECKS.find((d) => d.id === deckId) ?? DECKS[0]);
	const cards = $derived<Flashcard[]>(deckDef.cards);
	const categories = $derived<string[]>(deckDef.categories);

	// Category filter: -1 = all cards in the deck.
	let category = $state(-1);
	let order = $state<number[]>(FLASHCARDS.map((_, i) => i));
	let index = $state(0);
	let flipped = $state(false);
	// Known cards are keyed by deck, so two decks never share progress.
	let known = $state<Set<string>>(new Set());
	let shuffled = $state(false);

	const deck = $derived<Flashcard[]>(
		order.map((i) => cards[i]).filter((c) => c && (category < 0 || c.c === category))
	);
	const current = $derived(deck[index]);
	const total = $derived(deck.length);

	function knownKey(card: Flashcard) {
		return `${deckId}:${cards.indexOf(card)}`;
	}

	const knownInDeck = $derived(deck.filter((c) => known.has(knownKey(c))).length);
	const isKnown = $derived(current ? known.has(knownKey(current)) : false);

	function resetDeckOrder() {
		order = cards.map((_, i) => i);
		shuffled = false;
		index = 0;
		flipped = false;
	}

	function setDeck(id: string) {
		deckId = id;
		category = -1;
		resetDeckOrder();
	}

	function setCategory(c: number) {
		category = c;
		index = 0;
		flipped = false;
	}

	function next() {
		if (total === 0) return;
		flipped = false;
		index = (index + 1) % total;
	}

	function prev() {
		if (total === 0) return;
		flipped = false;
		index = (index - 1 + total) % total;
	}

	function flip() {
		flipped = !flipped;
	}

	function shuffle() {
		const arr = [...order];
		for (let i = arr.length - 1; i > 0; i--) {
			const j = Math.floor(Math.random() * (i + 1));
			[arr[i], arr[j]] = [arr[j], arr[i]];
		}
		order = arr;
		shuffled = true;
		index = 0;
		flipped = false;
	}

	function resetOrder() {
		resetDeckOrder();
	}

	function markKnown() {
		if (!current) return;
		const key = knownKey(current);
		const s = new Set(known);
		if (s.has(key)) s.delete(key);
		else s.add(key);
		known = s;
	}

	function onKey(e: KeyboardEvent) {
		const target = e.target as HTMLElement | null;
		if (target?.closest('button, a, input, textarea, select')) {
			// Let buttons handle their own Enter/Space; only arrows are global here.
			if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
		}
		if (e.key === 'ArrowRight') next();
		else if (e.key === 'ArrowLeft') prev();
		else if (e.key === ' ' && !target?.closest('button')) {
			e.preventDefault();
			flip();
		}
	}
</script>

<svelte:window onkeydown={onKey} />

<svelte:head>
	<title>CMA Clash: Flashcards</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-4xl mx-auto px-4 sm:px-8 pt-10 pb-16 min-w-0">
		<p class="text-sm text-ink-muted">
			<a href="/study" class="link-hover text-ink-muted">Study guides</a>
		</p>

		<div class="mt-4">
			{#key deckId}
				<PageHeader
					eyebrow="Flashcards"
					title={deckDef.title}
					lede={deckDef.lede}
					meta={`${cards.length} cards`}
				/>
			{/key}
		</div>

		<!-- Deck picker -->
		<div class="flex flex-wrap gap-2" role="group" aria-label="Choose a deck">
			{#each DECKS as d (d.id)}
				<button
					type="button"
					class="px-3 py-1.5 text-xs font-mono uppercase tracking-[0.14em] border border-line press-scale {deckId === d.id
						? 'bg-primary text-white border-primary'
						: 'text-ink-muted hover:text-ink'}"
					aria-pressed={deckId === d.id}
					onclick={() => setDeck(d.id)}>{d.label}</button
				>
			{/each}
		</div>

		<p class="mt-3 text-sm">
			<a href={`/practice-test/flashcards/${deckId}`} class="link-hover text-ink">Take the {deckDef.label.toLowerCase()} practice test</a>
		</p>

		<!-- Category filter -->
		<div class="flex flex-wrap gap-2 mt-3" role="group" aria-label="Filter by category">
			<button
				type="button"
				class="px-3 py-1.5 text-xs font-mono uppercase tracking-[0.14em] border border-line press-scale {category < 0
					? 'bg-primary text-white border-primary'
					: 'text-ink-muted hover:text-ink'}"
				aria-pressed={category < 0}
				onclick={() => setCategory(-1)}>All</button
			>
			{#each categories as name, c (c)}
				<button
					type="button"
					class="px-3 py-1.5 text-xs font-mono uppercase tracking-[0.14em] border border-line press-scale {category === c
						? 'bg-primary text-white border-primary'
						: 'text-ink-muted hover:text-ink'}"
					aria-pressed={category === c}
					onclick={() => setCategory(c)}>{name}</button
				>
			{/each}
		</div>

		<!-- Progress -->
		<div class="mt-8">
			<div class="flex items-center justify-between text-xs font-mono text-ink-muted tabular-nums">
				<span>Card {total ? index + 1 : 0} of {total}</span>
				<span>{knownInDeck} known</span>
			</div>
			<div class="h-1 bg-line mt-2" role="progressbar" aria-valuemin="0" aria-valuemax={total} aria-valuenow={total ? index + 1 : 0}>
				<div class="h-full bg-primary transition-[width] duration-200" style="width: {total ? ((index + 1) / total) * 100 : 0}%"></div>
			</div>
		</div>

		<!-- Card -->
		{#if current}
			<button
				type="button"
				class="flip-stage mt-6 block w-full h-[18rem] sm:h-[20rem] text-left"
				aria-pressed={flipped}
				aria-label={flipped ? `Definition of ${current.t}. Press to flip back.` : `${current.t}. Press to see the definition.`}
				onclick={flip}
			>
				<span class="flip-inner {flipped ? 'is-flipped' : ''} block relative w-full h-full">
					<span class="flip-face border border-line glass-panel p-8 sm:p-12 flex flex-col justify-between">
						<span class="eyebrow">{categories[current.c]}</span>
						<span
							class="block font-display leading-[1.02] tracking-[-0.035em] text-balance wrap-break-word"
							use:fitText={{ min: 18, max: 60 }}>{current.t}</span
						>
						<span class="eyebrow">Tap to flip</span>
					</span>
					<span class="flip-face flip-back border border-primary/60 bg-elevated p-8 sm:p-12 flex flex-col justify-between">
						<span class="eyebrow text-primary">Definition</span>
						<span
						class="block leading-snug text-balance wrap-break-word"
						use:fitText={{ min: 14, max: 36 }}>{current.d}</span
					>
						<span class="eyebrow">{current.t}</span>
					</span>
				</span>
			</button>

			<!-- Controls -->
			<div class="mt-6 flex flex-wrap items-center justify-between gap-4">
				<div class="flex items-center gap-3">
					<Button variant="secondary" onclick={prev}>Previous</Button>
					<Button onclick={next}>Next</Button>
				</div>
				<div class="flex items-center gap-3">
					<button
						type="button"
						class="btn btn-ghost press-scale"
						aria-pressed={isKnown}
						onclick={markKnown}>{isKnown ? 'Known' : 'Mark known'}</button
					>
					{#if shuffled}
						<button type="button" class="btn btn-ghost press-scale" onclick={resetOrder}>Reset order</button>
					{:else}
						<button type="button" class="btn btn-ghost press-scale" onclick={shuffle}>Shuffle</button>
					{/if}
				</div>
			</div>
		{:else}
			<Card class="mt-6" padding="lg">
				<p class="text-ink-muted">No cards in this category.</p>
			</Card>
		{/if}
	</div>
	<Footer />
</div>

<style>
	.flip-stage {
		perspective: 1400px;
		cursor: pointer;
	}
	.flip-inner {
		transform-style: preserve-3d;
		transition: transform 500ms cubic-bezier(0.22, 1, 0.36, 1);
	}
	.flip-inner.is-flipped {
		transform: rotateY(180deg);
	}
	.flip-face {
		position: absolute;
		inset: 0;
		backface-visibility: hidden;
		-webkit-backface-visibility: hidden;
	}
	.flip-back {
		transform: rotateY(180deg);
	}
	@media (prefers-reduced-motion: reduce) {
		.flip-inner {
			transition: none;
		}
	}
</style>
