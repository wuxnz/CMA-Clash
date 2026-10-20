import type { PageLoad } from './$types';
import type { Certification } from '$lib/cma/client';
import {
	fetchCerts,
	fetchClashQuizzes,
	rowFromClash,
	searchMeili,
	searchPageSize,
	sortRows,
	userMapFromHits,
	type BrowseRow
} from '$lib/quiz/browse';

export const load = (async ({ fetch, url }) => {
	const cert = url.searchParams.get('cert') ?? '';
	const difficulty = url.searchParams.get('difficulty') ?? '';
	const sort = url.searchParams.get('sort') ?? 'newest';

	const [meili, clash, featuredSource, certs] = await Promise.all([
		searchMeili(fetch, { q: '*', limit: 100, sort: ['created_at:desc'] }),
		fetchClashQuizzes(fetch, {
			certification_slug: cert || undefined,
			difficulty: difficulty || undefined,
			page: 1,
			page_size: searchPageSize()
		}),
		fetchClashQuizzes(fetch, { page: 1, page_size: 100 }),
		fetchCerts(fetch)
	]);

	const users = userMapFromHits(meili.hits);
	const rows: BrowseRow[] = sortRows(
		clash.map((item) => rowFromClash(item, certs, users)),
		sort === 'relevance' ? 'newest' : sort
	);
	const featured: BrowseRow[] =
		cert || difficulty
			? []
			: sortRows(
					featuredSource.map((item) => rowFromClash(item, certs, users)),
					'plays'
				).slice(0, 3);

	return {
		cert,
		difficulty,
		sort,
		certs: certs as Certification[],
		rows,
		featured,
		hasMore: clash.length >= searchPageSize(),
		page: 1
	};
}) satisfies PageLoad;
