import type { PageLoad } from './$types';
import type { Certification } from '$lib/cma/client';
import {
	fetchCerts,
	fetchClashCatalog,
	fetchClashQuizzes,
	rowsFromClash,
	rowsFromMeili,
	searchMeili,
	searchPageSize,
	userMapFromHits,
	type BrowseRow
} from '$lib/quiz/browse';

export const load = (async ({ fetch, url }) => {
	const q = url.searchParams.get('q') ?? '';
	const cert = url.searchParams.get('cert') ?? '';
	const difficulty = url.searchParams.get('difficulty') ?? '';
	const sort = url.searchParams.get('sort') ?? 'relevance';
	const trimmed = q.trim();
	const tooShort = trimmed.length > 0 && trimmed.length < 3;
	const useMeili = trimmed.length >= 3;

	const [meili, clashPage, catalog, certs] = await Promise.all([
		tooShort
			? Promise.resolve({ hits: [], query: trimmed, limit: searchPageSize(), offset: 0 })
			: searchMeili(fetch, {
					q: useMeili ? trimmed : '*',
					offset: 0,
					limit: useMeili ? searchPageSize() : 100,
					sort: sort === 'newest' ? ['created_at:desc'] : undefined
				}),
		useMeili || tooShort
			? Promise.resolve([])
			: fetchClashQuizzes(fetch, {
					certification_slug: cert || undefined,
					difficulty: difficulty || undefined,
					page: 1,
					page_size: searchPageSize()
				}),
		useMeili ? fetchClashCatalog(fetch) : Promise.resolve([]),
		fetchCerts(fetch)
	]);

	let rows: BrowseRow[] = [];
	let hasMore = false;
	let offset = 0;
	let page = 1;

	if (tooShort) {
		rows = [];
	} else if (useMeili) {
		rows = rowsFromMeili(meili.hits, catalog, certs, cert, difficulty, sort);
		hasMore = meili.hits.length >= searchPageSize();
		offset = meili.hits.length;
	} else {
		const users = userMapFromHits(meili.hits);
		rows = rowsFromClash(clashPage, certs, users, sort);
		hasMore = clashPage.length >= searchPageSize();
		page = 1;
	}

	return {
		q,
		cert,
		difficulty,
		sort,
		certs: certs as Certification[],
		rows,
		hasMore,
		offset,
		page
	};
}) satisfies PageLoad;
