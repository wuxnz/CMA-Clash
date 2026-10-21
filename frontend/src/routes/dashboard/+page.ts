// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { PageLoad } from './$types';

/** Shell only — data loads on the client after paint (see loadDashboardData). */
export const load = (() => ({
	quizzes: [],
	quiztivities: [],
	gamification: null,
	topicStats: [],
	certifications: [],
	topics: [],
	results: [],
	leaderboard: [],
	username: null
})) satisfies PageLoad;
