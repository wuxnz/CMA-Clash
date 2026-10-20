// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { PageLoad } from './$types';
import type { GamificationProfile, TopicStat } from '$lib/cma/client';

export const load = (async ({ fetch }) => {
	const quiz_res = await fetch('/api/v1/quiz/list?page_size=100');
	const quizzes = await quiz_res.json();
	const quiztivity_res = await fetch('/api/v1/quiztivity/');
	const quiztivities = await quiztivity_res.json();

	let gamification: GamificationProfile | null = null;
	let topicStats: TopicStat[] = [];

	const gRes = await fetch('/api/v1/clash/me/gamification', { credentials: 'include' });
	if (gRes.ok) {
		gamification = await gRes.json();
	}
	const tRes = await fetch('/api/v1/clash/me/stats/by-topic', { credentials: 'include' });
	if (tRes.ok) {
		topicStats = await tRes.json();
	}

	return {
		quizzes,
		quiztivities,
		gamification,
		topicStats
	};
}) satisfies PageLoad;
