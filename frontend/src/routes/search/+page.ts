import type { PageLoad } from './$types';

export const load = (({ url }) => {
	return {
		q: url.searchParams.get('q') ?? '',
		cert: url.searchParams.get('cert') ?? '',
		difficulty: url.searchParams.get('difficulty') ?? '',
		sort: url.searchParams.get('sort') ?? 'relevance',
		certs: [],
		rows: [],
		hasMore: false,
		offset: 0,
		page: 1
	};
}) satisfies PageLoad;
