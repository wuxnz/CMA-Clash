// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

// Multiple-choice practice tests built from the flashcard decks. Each card becomes one question:
// the question is the card's front (or, for phlebotomy terms, the description that fits the term),
// and the correct option is the card's back. The three wrong options are picked from the card's four
// written wrong answers, using a different seed from the quiz, and the right answer is never the only
// longest option. Order is seeded from the card text, so a test is the same on every visit.

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

/** Three of the card's written wrong answers, preferring sets that keep the right answer from being the longest. */
function pickWrongAnswers(card: Flashcard, rng: () => number): string[] {
	const wrong = card.w;
	const combos: string[][] = [];
	for (let skip = 0; skip < wrong.length; skip++) {
		combos.push(wrong.filter((_, i) => i !== skip));
	}
	const rightLength = card.d.length;
	const balanced = combos.filter((combo) => Math.max(...combo.map((text) => text.length)) >= rightLength);
	const pool = balanced.length ? balanced : combos;
	return pool[Math.floor(rng() * pool.length)];
}

function buildDeck(
	id: string,
	title: string,
	cards: Flashcard[],
	categories: string[],
	stemFor: (card: Flashcard) => string,
	explain: (card: Flashcard) => string
): PracticeDeck {
	const questions: PracticeQuestion[] = cards.map((card) => {
		const rng = seeded(hash(`${id}-practice:${card.t}`));
		const options = [card.d, ...pickWrongAnswers(card, rng)];
		// Fisher–Yates with the seeded rng, then find where the right answer landed.
		for (let i = options.length - 1; i > 0; i--) {
			const j = Math.floor(rng() * (i + 1));
			[options[i], options[j]] = [options[j], options[i]];
		}
		return {
			s: card.c,
			q: stemFor(card),
			o: options,
			a: options.indexOf(card.d),
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
	(card) => `Which description fits "${card.t}"?`,
	(card) => `${card.t}: ${card.d}`
);

const DIABETES = buildDeck(
	'diabetes',
	'Diabetes flashcards practice test',
	DIABETES_FLASHCARDS,
	DIABETES_FLASHCARD_CATEGORIES,
	(card) => card.t,
	(card) => card.d
);

const DECKS: Record<string, PracticeDeck> = {
	phlebotomy: PHLEBOTOMY,
	diabetes: DIABETES
};

export function getFlashcardPractice(id: string): PracticeDeck | undefined {
	return DECKS[id];
}
