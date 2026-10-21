import type { PageLoad } from './$types';

export const load = (({ url }) => {
	return {
		cert: url.searchParams.get('cert') ?? '',
		difficulty: url.searchParams.get('difficulty') ?? '',
		sort: url.searchParams.get('sort') ?? 'newest',
		certs: [],
		rows: [],
		featured: [],
		hasMore: false,
		page: 1,
		exploreSsrFailed: false
	};
}) satisfies PageLoad;
