import type { PageLoad } from './$types';
import type { LeaderboardEntry } from '$lib/cma/client';
import { kitOrBackendFetch } from '$lib/server-api';

async function loadBoard(
	fetchFn: typeof fetch,
	period: 'weekly' | 'all_time'
): Promise<LeaderboardEntry[]> {
	const res = await kitOrBackendFetch(
		fetchFn,
		`/api/v1/clash/leaderboards?period=${period}&limit=50`,
		{ credentials: 'include' }
	);
	if (!res?.ok) {
		return [];
	}
	return res.json();
}

export const load: PageLoad = async ({ fetch }) => {
	const [weekly, allTime] = await Promise.all([loadBoard(fetch, 'weekly'), loadBoard(fetch, 'all_time')]);
	return {
		weekly,
		allTime,
		apiAvailable: weekly.length > 0 || allTime.length > 0
	};
};
