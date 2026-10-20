/** CMA-Clash REST client (`/api/v1/clash/*`). */

export type GamificationProfile = {
	total_xp: number;
	level: number;
	xp_to_next_level: number;
	current_streak_days: number;
	longest_streak_days: number;
	battles_won: number;
	battles_played: number;
	questions_answered: number;
	questions_correct: number;
	accuracy_percent: number;
};

export type LeaderboardEntry = {
	rank: number;
	user_id: string;
	username: string;
	xp: number;
	level: number;
};

export type TopicStat = {
	topic_slug: string | null;
	topic_name: string | null;
	questions_answered: number;
	questions_correct: number;
	accuracy_percent: number;
	xp_earned: number;
};

export type Certification = {
	id: string;
	slug: string;
	name: string;
	description: string | null;
	sort_order: number;
};

export type Topic = {
	id: string;
	slug: string;
	name: string;
	description: string | null;
	certification_id: string | null;
	sort_order: number;
};

export type QuizBrowseItem = {
	id: string;
	title: string;
	description: string | null;
	difficulty: string | null;
	topic_id: string | null;
	certification_id: string | null;
	question_count: number;
	plays: number;
};

export type BattleLobby = {
	battle_code: string;
	quiz_id: string;
	host_user_id: string;
	max_players: number;
	player_slots: Array<{ user_id?: string; username?: string }>;
	status: string;
	game_pin: string | null;
	game_id: string | null;
};

async function clashFetch<T>(path: string, init?: RequestInit): Promise<T | null> {
	try {
		const res = await fetch(`/api/v1/clash${path}`, {
			credentials: 'include',
			...init,
			headers: {
				'Content-Type': 'application/json',
				...(init?.headers ?? {})
			}
		});
		if (!res.ok) return null;
		return (await res.json()) as T;
	} catch {
		return null;
	}
}

export async function fetchGamification(): Promise<GamificationProfile | null> {
	return clashFetch<GamificationProfile>('/me/gamification');
}

export async function fetchTopicStats(): Promise<TopicStat[]> {
	return (await clashFetch<TopicStat[]>('/me/stats/by-topic')) ?? [];
}

export async function fetchLeaderboard(
	period: 'all_time' | 'weekly',
	certificationSlug?: string
): Promise<LeaderboardEntry[]> {
	const params = new URLSearchParams({ period, limit: '50' });
	if (certificationSlug) params.set('certification_slug', certificationSlug);
	return (await clashFetch<LeaderboardEntry[]>(`/leaderboards?${params}`)) ?? [];
}

export async function fetchCertifications(): Promise<Certification[]> {
	return (await clashFetch<Certification[]>('/certifications')) ?? [];
}

export async function fetchTopics(certificationSlug?: string): Promise<Topic[]> {
	const q = certificationSlug ? `?certification_slug=${encodeURIComponent(certificationSlug)}` : '';
	return (await clashFetch<Topic[]>(`/topics${q}`)) ?? [];
}

export async function fetchQuizzes(params: {
	certification_slug?: string;
	page_size?: number;
}): Promise<QuizBrowseItem[]> {
	const search = new URLSearchParams();
	if (params.certification_slug) search.set('certification_slug', params.certification_slug);
	search.set('page_size', String(params.page_size ?? 100));
	return (await clashFetch<QuizBrowseItem[]>(`/quizzes?${search}`)) ?? [];
}

/** Resolve topic + certification labels for a live game title (best-effort, no socket changes). */
export async function resolveQuizContentLabels(quizTitle: string): Promise<{
	certLabel: string | null;
	topicLabel: string | null;
}> {
	const [quizzes, certs, topics] = await Promise.all([
		fetchQuizzes({ page_size: 100 }),
		fetchCertifications(),
		fetchTopics()
	]);
	const quiz = quizzes.find((q) => q.title === quizTitle);
	if (!quiz) return { certLabel: null, topicLabel: null };
	const cert = certs.find((c) => c.id === quiz.certification_id);
	const topic = topics.find((t) => t.id === quiz.topic_id);
	return {
		certLabel: cert?.name ?? null,
		topicLabel: topic?.name ?? null
	};
}

export function formatQuestionTopicTag(
	certLabel: string | null,
	topicLabel: string | null,
	questionIndex: number,
	totalQuestions?: number
): string {
	const qNum = questionIndex + 1;
	const qTotal = totalQuestions ? `Q${qNum}/${totalQuestions}` : `Q${qNum}`;
	if (certLabel && topicLabel) return `${certLabel} · ${topicLabel} · ${qTotal}`;
	if (topicLabel) return `${topicLabel} · ${qTotal}`;
	return `Live · ${qTotal}`;
}

export async function createBattle(quizId: string, maxPlayers = 4): Promise<BattleLobby | null> {
	return clashFetch<BattleLobby>('/battles', {
		method: 'POST',
		body: JSON.stringify({ quiz_id: quizId, max_players: maxPlayers })
	});
}

export async function joinBattle(battleCode: string): Promise<BattleLobby | null> {
	return clashFetch<BattleLobby>(`/battles/${battleCode}/join`, { method: 'POST' });
}

export async function getBattle(battleCode: string): Promise<BattleLobby | null> {
	return clashFetch<BattleLobby>(`/battles/${battleCode}`);
}

export async function startBattle(battleCode: string): Promise<BattleLobby | null> {
	return clashFetch<BattleLobby>(`/battles/${battleCode}/start`, { method: 'POST' });
}
