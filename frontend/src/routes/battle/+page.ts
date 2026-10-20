import type { PageLoad } from './$types';
import type { QuizBrowseItem } from '$lib/cma/client';
import { loadPublicQuizCatalog } from '$lib/cma/quiz-catalog';

export const load: PageLoad = async ({ fetch }) => {
	try {
		const quizzes = await loadPublicQuizCatalog(fetch);
		return {
			quizzes,
			ssrQuizLoadFailed: quizzes.length === 0
		};
	} catch {
		return {
			quizzes: [] as QuizBrowseItem[],
			ssrQuizLoadFailed: true
		};
	}
};
