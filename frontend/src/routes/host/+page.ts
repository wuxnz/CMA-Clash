// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { PageLoad } from './$types';
import { loadPublicQuizCatalog } from '$lib/cma/quiz-catalog';

export const load = (async ({ fetch }) => {
	const quizzes = await loadPublicQuizCatalog(fetch);
	return {
		quizzes,
		ssrQuizLoadFailed: quizzes.length === 0
	};
}) satisfies PageLoad;
