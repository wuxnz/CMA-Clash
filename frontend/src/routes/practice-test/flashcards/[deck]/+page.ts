// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { error } from '@sveltejs/kit';
import { getFlashcardPractice } from '$lib/study/flashcard-practice';
import type { PageLoad } from './$types';

export const load = (({ params }) => {
	const deck = getFlashcardPractice(params.deck);
	if (!deck) error(404, 'Practice test not found');
	return { deck };
}) satisfies PageLoad;
