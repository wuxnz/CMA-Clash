// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { PageLoad } from './$types';
import type { GamificationProfile, TopicStat } from '$lib/cma/client';

function asList(value: unknown): any[] {
	if (Array.isArray(value)) return value;
	if (value && typeof value === 'object') {
		const record = value as Record<string, unknown>;
		if (Array.isArray(record.items)) return record.items;
		if (Array.isArray(record.quizzes)) return record.quizzes;
	}
	return [];
}

export const load = (async ({ fetch }) => {
	let quizzes: any[] = [];
	let quiztivities: any[] = [];
	try {
		const quiz_res = await fetch('/api/v1/quiz/list?page_size=100');
		if (quiz_res.ok) quizzes = asList(await quiz_res.json());
	} catch {
		quizzes = [];
	}
	try {
		const quiztivity_res = await fetch('/api/v1/quiztivity/');
		if (quiztivity_res.ok) quiztivities = asList(await quiztivity_res.json());
	} catch {
		quiztivities = [];
	}

	let gamification: GamificationProfile | null = null;
	let topicStats: TopicStat[] = [];

	try {
		const gRes = await fetch('/api/v1/clash/me/gamification', { credentials: 'include' });
		if (gRes.ok) {
			gamification = await gRes.json();
		}
	} catch {
		gamification = null;
	}
	try {
		const tRes = await fetch('/api/v1/clash/me/stats/by-topic', { credentials: 'include' });
		if (tRes.ok) {
			topicStats = asList(await tRes.json()) as TopicStat[];
		}
	} catch {
		topicStats = [];
	}

	return {
		quizzes,
		quiztivities,
		gamification,
		topicStats
	};
}) satisfies PageLoad;
