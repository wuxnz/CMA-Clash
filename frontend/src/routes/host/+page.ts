import type { PageLoad } from './$types';

export const load = (({ url }) => {
	return {
		cert: url.searchParams.get('cert') ?? '',
		difficulty: url.searchParams.get('difficulty') ?? '',
		sort: url.searchParams.get('sort') ?? 'newest',
		certs: [],
		rows: [],
		hasMore: false,
		page: 1,
		hostSsrFailed: false
	};
}) satisfies PageLoad;
