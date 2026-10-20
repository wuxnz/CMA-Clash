import type { PageLoad } from './$types';
import type { LeaderboardEntry } from '$lib/cma/client';
import { kitOrBackendFetch } from '$lib/server-api';

export const load = (async ({ fetch }) => {
	async function loadBoard(period: 'weekly' | 'all_time'): Promise<LeaderboardEntry[]> {
		const res = await kitOrBackendFetch(
			fetch,
			`/api/v1/clash/leaderboards?period=${period}&limit=50`,
			{ credentials: 'include' }
		);
		if (!res?.ok) return [];
		return res.json();
	}

	const [weekly, allTime] = await Promise.all([loadBoard('weekly'), loadBoard('all_time')]);

	return {
		weekly,
		allTime,
		apiAvailable: weekly.length > 0 || allTime.length > 0
	};
}) satisfies PageLoad;
