import type { PageLoad } from './$types';

export const load: PageLoad = () => ({
	quizzes: [],
	ssrQuizLoadFailed: false
});
