import type { PageLoad } from './$types';

export const load = (({ url }) => ({
	cert: url.searchParams.get('cert') ?? '',
	difficulty: url.searchParams.get('difficulty') ?? '',
	sort: url.searchParams.get('sort') ?? 'newest',
	certs: []
})) satisfies PageLoad;
