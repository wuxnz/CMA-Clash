import type { PageLoad } from './$types';
import type { QuizBrowseItem } from '$lib/cma/client';

export const load: PageLoad = async ({ fetch }) => {
	try {
		const res = await fetch('/api/v1/clash/quizzes?page_size=50&certification_slug=ccma');
		if (res.ok) {
			const ccma = (await res.json()) as QuizBrowseItem[];
			if (ccma.length > 0) return { quizzes: ccma, loadError: null };
		}
		const all = await fetch('/api/v1/clash/quizzes?page_size=50');
		if (all.ok) {
			return { quizzes: (await all.json()) as QuizBrowseItem[], loadError: null };
		}
		return { quizzes: [] as QuizBrowseItem[], loadError: 'Could not load quizzes from the API.' };
	} catch {
		return { quizzes: [] as QuizBrowseItem[], loadError: 'Could not reach the API.' };
	}
};
