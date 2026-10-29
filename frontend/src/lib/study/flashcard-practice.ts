// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

// Practice tests built from the flashcard decks. Each card becomes one question, asked in the
// reverse direction from the quiz: the card's back is shown and the options are the fronts.
// Options come from the same category at a similar length, and the prompt's key words are
// blanked out so the right option is not given away by echoed wording. The order is seeded
// from the card text, so a test is the same on every visit.

import { FLASHCARDS, FLASHCARD_CATEGORIES, type Flashcard } from './phlebotomy-flashcards';
import { DIABETES_FLASHCARDS, DIABETES_FLASHCARD_CATEGORIES } from './diabetes-flashcards';

export interface PracticeQuestion {
	/** Section index, the card's category. */
	s: number;
	q: string;
	o: string[];
	/** Index of the correct option. */
	a: number;
	e: string;
}

export interface PracticeDeck {
	id: string;
	title: string;
	categories: string[];
	questions: PracticeQuestion[];
}

const COMMON_WORDS = new Set(
	(
		'about their there these those which where while would could should being through between ' +
		'thought cause causes people group groups what does mean have with from this that into other ' +
		'after before many much more most some such when your they them will just only also'
	).split(' ')
);

function hash(text: string): number {
	let h = 2166136261;
	for (let i = 0; i < text.length; i++) {
		h ^= text.charCodeAt(i);
		h = Math.imul(h, 16777619);
	}
	return h >>> 0;
}

/** Small seeded PRNG (mulberry32), so each question's option order is stable. */
function seeded(seed: number): () => number {
	let s = seed;
	return () => {
		s = (s + 0x6d2b79f5) >>> 0;
		let t = s;
		t = Math.imul(t ^ (t >>> 15), t | 1);
		t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
		return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
	};
}

function keyWords(text: string): string[] {
	const words = text.toLowerCase().match(/[a-z]{5,}/g) ?? [];
	return [...new Set(words.filter((w) => !COMMON_WORDS.has(w)))];
}

function mask(text: string, keys: string[]): string {
	let out = text;
	for (const word of [...keys].sort((a, b) => b.length - a.length)) {
		out = out.replace(new RegExp(`\\b${word}\\b`, 'gi'), '____');
	}
	return out;
}

function pickDistractors(deck: Flashcard[], index: number, rng: () => number): string[] {
	const card = deck[index];
	const sameCategory = deck
		.map((c, j) => ({ c, j }))
		.filter(({ c, j }) => j !== index && c.c === card.c && c.t !== card.t);
	const pool = sameCategory.length >= 3 ? sameCategory : deck.map((c, j) => ({ c, j })).filter(({ j, c }) => j !== index && c.t !== card.t);
	const ranked = [...pool].sort(
		(x, y) =>
			Math.abs(x.c.t.length - card.t.length) - Math.abs(y.c.t.length - card.t.length) || x.j - y.j
	);
	const candidates = ranked.slice(0, 6);
	const picked: string[] = [];
	while (picked.length < 3 && candidates.length) {
		const k = Math.floor(rng() * candidates.length);
		const [chosen] = candidates.splice(k, 1);
		if (!picked.includes(chosen.c.t)) picked.push(chosen.c.t);
	}
	return picked;
}

function buildDeck(
	id: string,
	title: string,
	cards: Flashcard[],
	categories: string[],
	stem: (masked: string) => string,
	describe: (card: Flashcard) => string,
	explain: (card: Flashcard) => string,
	keysFor: (card: Flashcard) => string[]
): PracticeDeck {
	const questions: PracticeQuestion[] = cards.map((card, index) => {
		const rng = seeded(hash(`${id}:${card.t}`));
		const keys = keysFor(card);
		const options = [card.t, ...pickDistractors(cards, index, rng)];
		// Fisher–Yates with the seeded rng, then find where the right answer landed.
		for (let i = options.length - 1; i > 0; i--) {
			const j = Math.floor(rng() * (i + 1));
			[options[i], options[j]] = [options[j], options[i]];
		}
		return {
			s: card.c,
			q: stem(mask(describe(card), keys)),
			o: options,
			a: options.indexOf(card.t),
			e: explain(card)
		};
	});
	return { id, title, categories, questions };
}

const PHLEBOTOMY = buildDeck(
	'phlebotomy',
	'Phlebotomy flashcards practice test',
	FLASHCARDS,
	FLASHCARD_CATEGORIES,
	(masked) => `Which term matches this description?\n\n${masked}`,
	(card) => card.d,
	(card) => `${card.t}: ${card.d}`,
	(card) => keyWords(card.t)
);

const DIABETES = buildDeck(
	'diabetes',
	'Diabetes flashcards practice test',
	DIABETES_FLASHCARDS,
	DIABETES_FLASHCARD_CATEGORIES,
	(masked) => `Which question does this answer belong to?\n\n${masked}`,
	(card) => card.d,
	(card) => card.d,
	(card) => keyWords(card.t)
);

const DECKS: Record<string, PracticeDeck> = {
	phlebotomy: PHLEBOTOMY,
	diabetes: DIABETES
};

export function getFlashcardPractice(id: string): PracticeDeck | undefined {
	return DECKS[id];
}
