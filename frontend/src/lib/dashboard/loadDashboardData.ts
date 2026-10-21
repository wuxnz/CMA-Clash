// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type {
	Certification,
	GamificationProfile,
	LeaderboardEntry,
	Topic,
	TopicStat
} from '$lib/cma/client';

function asList(value: unknown): any[] {
	if (Array.isArray(value)) return value;
	if (value && typeof value === 'object') {
		const record = value as Record<string, unknown>;
		if (Array.isArray(record.items)) return record.items;
		if (Array.isArray(record.quizzes)) return record.quizzes;
		if (Array.isArray(record.results)) return record.results;
	}
	return [];
}

async function safeJson(fetchFn: typeof fetch, url: string): Promise<unknown> {
	try {
		const res = await fetchFn(url, { credentials: 'include' });
		if (!res.ok) return null;
		return await res.json();
	} catch {
		return null;
	}
}

export type DashboardLoadResult = {
	quizzes: any[];
	quiztivities: any[];
	gamification: GamificationProfile | null;
	topicStats: TopicStat[];
	certifications: Certification[];
	topics: Topic[];
	results: any[];
	leaderboard: LeaderboardEntry[];
	username: string | null;
};

export async function loadDashboardData(fetchFn: typeof fetch): Promise<DashboardLoadResult> {
	const [
		quizRaw,
		quiztivityRaw,
		gamificationRaw,
		topicRaw,
		certRaw,
		topicsRaw,
		resultsRaw,
		boardRaw,
		meRaw
	] = await Promise.all([
		safeJson(fetchFn, '/api/v1/quiz/list?page_size=100'),
		safeJson(fetchFn, '/api/v1/quiztivity/'),
		safeJson(fetchFn, '/api/v1/clash/me/gamification'),
		safeJson(fetchFn, '/api/v1/clash/me/stats/by-topic'),
		safeJson(fetchFn, '/api/v1/clash/certifications'),
		safeJson(fetchFn, '/api/v1/clash/topics'),
		safeJson(fetchFn, '/api/v1/results/list?include_quiz=true'),
		safeJson(fetchFn, '/api/v1/clash/leaderboards?period=weekly&limit=5'),
		safeJson(fetchFn, '/api/v1/users/me')
	]);

	const me = (meRaw && typeof meRaw === 'object' ? meRaw : {}) as {
		username?: string;
		email?: string;
	};

	return {
		quizzes: asList(quizRaw),
		quiztivities: asList(quiztivityRaw),
		gamification: (gamificationRaw as GamificationProfile | null) ?? null,
		topicStats: asList(topicRaw) as TopicStat[],
		certifications: asList(certRaw) as Certification[],
		topics: asList(topicsRaw) as Topic[],
		results: asList(resultsRaw),
		leaderboard: asList(boardRaw) as LeaderboardEntry[],
		username: me.username ?? null
	};
}
