import type { PageLoad } from './$types';

export const load = (({ url }) => ({
	cert: url.searchParams.get('cert') ?? ''
})) satisfies PageLoad;
