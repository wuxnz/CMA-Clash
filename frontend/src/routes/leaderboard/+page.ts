import type { PageLoad } from './$types';

export const load = (() => ({
	weekly: [],
	allTime: [],
	apiAvailable: false
})) satisfies PageLoad;
