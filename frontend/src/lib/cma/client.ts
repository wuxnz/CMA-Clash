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

/** Short cert code for topic tags (seed banks: NHA CCMA, EKG, phlebotomy, etc.). */
export function certificationShortLabel(slug: string | undefined | null, name?: string | null): string {
	if (!slug) {
		if (name?.toUpperCase().includes('CCMA')) return 'CCMA';
		return name ?? 'CCMA';
	}
	const s = slug.toLowerCase();
	if (s === 'ccma') return 'CCMA';
	if (s === 'ekg') return 'EKG';
	if (s === 'phlebotomy') return 'Phlebotomy';
	if (s === 'cpr-bls') return 'BLS';
	if (s === 'clinical-skills') return 'Skills';
	return name?.split('—')[0]?.trim() ?? slug.toUpperCase();
}

export type StudyBlock = {
	title: string;
	summary: string;
	url: string;
};

export type Topic = {
	id: string;
	slug: string;
	name: string;
	description: string | null;
	study_content?: StudyBlock[] | null;
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
	host_secret?: string | null;
	guest_player_id?: string | null;
};

export type ClashFetchResult<T> = { ok: true; data: T } | { ok: false; status: number; detail?: string };

async function clashFetchResult<T>(path: string, init?: RequestInit): Promise<ClashFetchResult<T>> {
	try {
		const res = await fetch(`/api/v1/clash${path}`, {
			credentials: 'include',
			...init,
			headers: {
				'Content-Type': 'application/json',
				...(init?.headers ?? {})
			}
		});
		if (!res.ok) {
			let detail: string | undefined;
			try {
				const body = await res.json();
				detail = typeof body?.detail === 'string' ? body.detail : undefined;
			} catch {
				/* ignore */
			}
			return { ok: false, status: res.status, detail };
		}
		return { ok: true, data: (await res.json()) as T };
	} catch {
		return { ok: false, status: 0 };
	}
}

async function clashFetch<T>(path: string, init?: RequestInit): Promise<T | null> {
	const res = await clashFetchResult<T>(path, init);
	return res.ok ? res.data : null;
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
	difficulty?: string;
	page?: number;
	page_size?: number;
}): Promise<QuizBrowseItem[]> {
	const search = new URLSearchParams();
	if (params.certification_slug) search.set('certification_slug', params.certification_slug);
	if (params.difficulty) search.set('difficulty', params.difficulty);
	if (params.page) search.set('page', String(params.page));
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
	const quiz =
		quizzes.find((q) => q.title === quizTitle) ??
		quizzes.find((q) => quizTitle.startsWith(q.title) || q.title.startsWith(quizTitle));
	if (!quiz) return { certLabel: null, topicLabel: null };
	const cert = certs.find((c) => c.id === quiz.certification_id);
	const topic = topics.find((t) => t.id === quiz.topic_id);
	return {
		certLabel: cert ? certificationShortLabel(cert.slug, cert.name) : null,
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

export async function createBattle(
	quizId: string,
	maxPlayers = 4,
	displayName?: string
): Promise<ClashFetchResult<BattleLobby>> {
	return clashFetchResult<BattleLobby>('/battles', {
		method: 'POST',
		body: JSON.stringify({
			quiz_id: quizId,
			max_players: maxPlayers,
			display_name: displayName
		})
	});
}

export async function joinBattle(
	battleCode: string,
	opts?: { displayName?: string; guestPlayerId?: string }
): Promise<ClashFetchResult<BattleLobby>> {
	return clashFetchResult<BattleLobby>(`/battles/${battleCode}/join`, {
		method: 'POST',
		body: JSON.stringify({
			display_name: opts?.displayName,
			guest_player_id: opts?.guestPlayerId
		})
	});
}

export async function getBattle(battleCode: string): Promise<BattleLobby | null> {
	return clashFetch<BattleLobby>(`/battles/${battleCode}`);
}

export async function startBattle(
	battleCode: string,
	hostSecret?: string
): Promise<ClashFetchResult<BattleLobby>> {
	return clashFetchResult<BattleLobby>(`/battles/${battleCode}/start`, {
		method: 'POST',
		body: JSON.stringify({ host_secret: hostSecret ?? null })
	});
}
